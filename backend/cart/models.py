from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from books.models import Book


class CartItem(models.Model):
    """Cart item model linking user, book, and quantity."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'book']
        ordering = ['-added_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.quantity})"
    
    def clean(self):
        """Validate cart item data."""
        if self.quantity <= 0:
            raise ValidationError("Quantity must be positive")
        if self.book and self.quantity > self.book.stock_quantity:
            raise ValidationError("Requested quantity exceeds available stock")
