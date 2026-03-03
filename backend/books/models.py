from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    """Category model for organizing books."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Book(models.Model):
    """Book model representing items in the catalog."""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )
    image_url = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def clean(self):
        """Validate book data."""
        if self.price is not None and self.price <= 0:
            raise ValidationError("Price must be positive")
        if self.stock_quantity is not None and self.stock_quantity < 0:
            raise ValidationError("Stock quantity cannot be negative")
