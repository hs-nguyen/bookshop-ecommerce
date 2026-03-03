from django.test import TestCase, TransactionTestCase
from django.core.exceptions import ValidationError
from decimal import Decimal
from .models import Category, Book


class BookModelTest(TransactionTestCase):
    """Test cases for Book model validation."""
    
    def setUp(self):
        """Set up test data."""
        self.category = Category.objects.create(
            name="Fiction",
            description="Fiction books"
        )
    
    def test_book_creation_with_valid_data(self):
        """Test creating a book with valid data."""
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="Test description",
            price=Decimal("19.99"),
            stock_quantity=10,
            category=self.category,
            image_url="https://example.com/image.jpg"
        )
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(book.price, Decimal("19.99"))
        self.assertEqual(book.stock_quantity, 10)
        self.assertEqual(book.category, self.category)
    
    def test_book_price_validation_positive(self):
        """Test that price must be positive."""
        book = Book(
            title="Test Book",
            author="Test Author",
            description="Test description",
            price=Decimal("-10.00"),
            stock_quantity=10,
            category=self.category,
            image_url="https://example.com/image.jpg"
        )
        with self.assertRaises(ValidationError) as context:
            book.clean()
        self.assertIn("Price must be positive", str(context.exception))
    
    def test_book_price_validation_zero(self):
        """Test that price cannot be zero."""
        book = Book(
            title="Test Book",
            author="Test Author",
            description="Test description",
            price=Decimal("0.00"),
            stock_quantity=10,
            category=self.category,
            image_url="https://example.com/image.jpg"
        )
        with self.assertRaises(ValidationError) as context:
            book.clean()
        self.assertIn("Price must be positive", str(context.exception))
    
    def test_book_stock_quantity_validation_negative(self):
        """Test that stock quantity cannot be negative."""
        book = Book(
            title="Test Book",
            author="Test Author",
            description="Test description",
            price=Decimal("19.99"),
            stock_quantity=-5,
            category=self.category,
            image_url="https://example.com/image.jpg"
        )
        with self.assertRaises(ValidationError) as context:
            book.clean()
        self.assertIn("Stock quantity cannot be negative", str(context.exception))
    
    def test_book_stock_quantity_zero_allowed(self):
        """Test that stock quantity can be zero."""
        book = Book(
            title="Test Book",
            author="Test Author",
            description="Test description",
            price=Decimal("19.99"),
            stock_quantity=0,
            category=self.category,
            image_url="https://example.com/image.jpg"
        )
        # Should not raise ValidationError
        book.clean()
        book.save()
        self.assertEqual(book.stock_quantity, 0)
    
    def test_book_category_set_null_on_delete(self):
        """Test that book's category is set to NULL when category is deleted."""
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="Test description",
            price=Decimal("19.99"),
            stock_quantity=10,
            category=self.category,
            image_url="https://example.com/image.jpg"
        )
        self.assertEqual(book.category, self.category)
        
        # Delete the category
        self.category.delete()
        
        # Refresh book from database
        book.refresh_from_db()
        
        # Category should be NULL
        self.assertIsNone(book.category)
    
    def test_book_ordering(self):
        """Test that books are ordered by created_at descending."""
        book1 = Book.objects.create(
            title="Book 1",
            author="Author 1",
            description="Description 1",
            price=Decimal("10.00"),
            stock_quantity=5,
            image_url="https://example.com/image1.jpg"
        )
        book2 = Book.objects.create(
            title="Book 2",
            author="Author 2",
            description="Description 2",
            price=Decimal("20.00"),
            stock_quantity=10,
            image_url="https://example.com/image2.jpg"
        )
        
        books = Book.objects.all()
        # Most recent book should be first
        self.assertEqual(books[0], book2)
        self.assertEqual(books[1], book1)
    
    def test_book_str_representation(self):
        """Test the string representation of a book."""
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="Test description",
            price=Decimal("19.99"),
            stock_quantity=10,
            image_url="https://example.com/image.jpg"
        )
        self.assertEqual(str(book), "Test Book")
