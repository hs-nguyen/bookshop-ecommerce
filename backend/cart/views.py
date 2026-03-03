from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CartItem
from .serializers import CartItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    """ViewSet for Cart operations."""
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """Return cart items for the authenticated user."""
        return CartItem.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """Create cart item for the authenticated user."""
        book = serializer.validated_data['book']
        quantity = serializer.validated_data['quantity']
        
        # Check if item already exists in cart
        cart_item = CartItem.objects.filter(
            user=self.request.user,
            book=book
        ).first()
        
        if cart_item:
            # Update existing cart item
            cart_item.quantity += quantity
            cart_item.save()
            serializer.instance = cart_item
        else:
            # Create new cart item
            serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['delete'])
    def clear(self, request):
        """Clear all items from the cart."""
        CartItem.objects.filter(user=request.user).delete()
        return Response(
            {'message': 'Cart cleared successfully'},
            status=status.HTTP_204_NO_CONTENT
        )
