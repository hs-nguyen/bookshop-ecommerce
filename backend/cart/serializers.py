from rest_framework import serializers
from .models import CartItem
from books.serializers import BookSerializer


class CartItemSerializer(serializers.ModelSerializer):
    """Serializer for CartItem model."""
    book_details = BookSerializer(source='book', read_only=True)
    subtotal = serializers.SerializerMethodField()
    
    class Meta:
        model = CartItem
        fields = ['id', 'book', 'book_details', 'quantity', 'subtotal', 'added_at']
        read_only_fields = ['added_at']
    
    def get_subtotal(self, obj):
        """Calculate subtotal for this cart item."""
        return obj.quantity * obj.book.price
    
    def validate_quantity(self, value):
        """Validate that quantity is positive."""
        if value <= 0:
            raise serializers.ValidationError("Quantity must be positive")
        return value
    
    def validate(self, data):
        """Validate that quantity doesn't exceed stock."""
        book = data.get('book')
        quantity = data.get('quantity')
        
        if book and quantity and quantity > book.stock_quantity:
            raise serializers.ValidationError(
                "Requested quantity exceeds available stock"
            )
        
        return data
