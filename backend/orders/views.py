from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.db import transaction
from .models import Order, OrderItem
from .serializers import OrderSerializer
from cart.models import CartItem


class OrderViewSet(viewsets.ModelViewSet):
    """ViewSet for Order operations."""
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post']
    
    def get_queryset(self):
        """Return orders for the authenticated user, or all orders for admin."""
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)
    
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        """Create an order from the user's cart."""
        cart_items = CartItem.objects.filter(user=request.user)
        
        if not cart_items.exists():
            return Response(
                {'error': 'Cart is empty'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check stock availability for all items
        for cart_item in cart_items:
            if cart_item.quantity > cart_item.book.stock_quantity:
                return Response(
                    {'error': f'Insufficient stock for {cart_item.book.title}'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        # Calculate total price
        total_price = sum(
            cart_item.quantity * cart_item.book.price
            for cart_item in cart_items
        )
        
        # Create order
        order = Order.objects.create(
            user=request.user,
            total_price=total_price
        )
        
        # Create order items and reduce stock
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                book=cart_item.book,
                quantity=cart_item.quantity,
                price_at_purchase=cart_item.book.price
            )
            
            # Reduce stock quantity
            cart_item.book.stock_quantity -= cart_item.quantity
            cart_item.book.save()
        
        # Clear cart
        cart_items.delete()
        
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
