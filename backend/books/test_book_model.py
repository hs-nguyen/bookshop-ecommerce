"""
Simple test script to verify Book model validation without Django TestCase.
Run with: python manage.py shell < books/test_book_model.py
"""
from django.core.exceptions import ValidationError
from decimal import Decimal
from books.models import Category, Book

print("Testing Book model validation...")

# Test 1: Create a category
print("\n1. Creating test category...")
category = Category(name="Test Fiction", description="Test category")
category.save()
print("✓ Category created successfullv1")

# Test 2: Create a valid book
print("\n2. Creating valid book...")
book = Book(
    title="Test Book",
    author="Test Author",
    description="Test description",
    price=Decimal("19.99"),
    stock_quantity=10,
    category=category,
    image_url="https://example.com/image.jpg"
)
book.clean()
book.save()
print(f"✓ Book created successfully: {book}")

# Test 3: Test price validation (negative price)
print("\n3. Testing negative price validation...")
try:
    invalid_book = Book(
        title="Invalid Book",
        author="Test Author",
        description="Test description",
        price=Decimal("-10.00"),
        stock_quantity=10,
        category=category,
        image_url="https://example.com/image.jpg"
    )
    invalid_book.clean()
    print("✗ FAILED: Should have raised ValidationError for negative price")
except ValidationError as e:
    if "Price must be positive" in str(e):
        print("✓ Correctly rejected negative price")
    else:
        print(f"✗ FAILED: Wrong error message: {e}")

# Test 4: Test price validation (zero price)
print("\n4. Testing zero price validation...")
try:
    invalid_book = Book(
        title="Invalid Book",
        author="Test Author",
        description="Test description",
        price=Decimal("0.00"),
        stock_quantity=10,
        category=category,
        image_url="https://example.com/image.jpg"
    )
    invalid_book.clean()
    print("✗ FAILED: Should have raised ValidationError for zero price")
except ValidationError as e:
    if "Price must be positive" in str(e):
        print("✓ Correctly rejected zero price")
    else:
        print(f"✗ FAILED: Wrong error message: {e}")

# Test 5: Test stock quantity validation (negative)
print("\n5. Testing negative stock quantity validation...")
try:
    invalid_book = Book(
        title="Invalid Book",
        author="Test Author",
        description="Test description",
        price=Decimal("19.99"),
        stock_quantity=-5,
        category=category,
        image_url="https://example.com/image.jpg"
    )
    invalid_book.clean()
    print("✗ FAILED: Should have raised ValidationError for negative stock")
except ValidationError as e:
    if "Stock quantity cannot be negative" in str(e):
        print("✓ Correctly rejected negative stock quantity")
    else:
        print(f"✗ FAILED: Wrong error message: {e}")

# Test 6: Test zero stock quantity (should be allowed)
print("\n6. Testing zero stock quantity (should be allowed)...")
try:
    valid_book = Book(
        title="Out of Stock Book",
        author="Test Author",
        description="Test description",
        price=Decimal("19.99"),
        stock_quantity=0,
        category=category,
        image_url="https://example.com/image.jpg"
    )
    valid_book.clean()
    valid_book.save()
    print("✓ Zero stock quantity correctly allowed")
except ValidationError as e:
    print(f"✗ FAILED: Should allow zero stock quantity: {e}")

# Test 7: Test category SET_NULL on delete
print("\n7. Testing category SET_NULL on delete...")
test_category = Category(name="Temp Category", description="Temporary")
test_category.save()
test_book = Book(
    title="Book with Category",
    author="Test Author",
    description="Test description",
    price=Decimal("15.00"),
    stock_quantity=5,
    category=test_category,
    image_url="https://example.com/image.jpg"
)
test_book.save()
category_id = test_category.id
test_category.delete()
test_book.refresh_from_db()
if test_book.category is None:
    print("✓ Category correctly set to NULL on delete")
else:
    print(f"✗ FAILED: Category should be NULL but is: {test_book.category}")

# Test 8: Test ordering
print("\n8. Testing book ordering (most recent first)...")
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
if books[0].id == book2.id:
    print("✓ Books correctly ordered by created_at descending")
else:
    print(f"✗ FAILED: Expected book2 first, got book with id {books[0].id}")

print("\n" + "="*50)
print("All Book model validation tests completed!")
print("="*50)

# Cleanup
print("\nCleaning up test data...")
Book.objects.all().delete()
Category.objects.all().delete()
print("✓ Cleanup complete")
