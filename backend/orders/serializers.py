from rest_framework import serializers
from .models import Order, OrderItem
from books.serializers import BookSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for OrderItem model."""
    book_details = BookSerializer(source='book', read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'book', 'book_details', 'quantity', 'price_at_purchase']


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order model."""
    items = OrderItemSerializer(many=True, read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Order
        fields = [
            'id', 'user', 'user_username', 'order_date',
            'total_price', 'status', 'items'
        ]
        read_only_fields = ['order_date', 'total_price']
