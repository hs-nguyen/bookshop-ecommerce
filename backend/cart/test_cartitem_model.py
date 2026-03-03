"""
Simple test script to verify CartItem model validation without Django TestCase.
Run with: python manage.py shell < cart/test_cartitem_model.py
"""
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from decimal import Decimal
from books.models import Category, Book
from cart.models import CartItem

print("Testing CartItem model validation...")

# Setup: Create test user, category, and book
print("\n0. Setting up test data...")
user = User.objects.create_user(username='testuser', email='test@example.com', password='test_password')
category = Category.objects.create(name="Test Category", description="Test")
book = Book.objects.create(
    title="Test Book",
    author="Test Author",
    description="Test description",
    price=Decimal("19.99"),
    stock_quantity=10,
    category=category,
    image_url="https://example.com/image.jpg"
)
print("✓ Test data created successfully")

# Test 1: Create a valid cart item
print("\n1. Creating valid cart item...")
cart_item = CartItem(
    user=user,
    book=book,
    quantity=5
)
cart_item.clean()
cart_item.save()
print(f"✓ CartItem created successfully: {cart_item}")

# Test 2: Test unique constraint (user, book)
print("\n2. Testing unique constraint on (user, book)...")
try:
    duplicate_item = CartItem(
        user=user,
        book=book,
        quantity=3
    )
    duplicate_item.save()
    print("✗ FAILED: Should have raised IntegrityError for duplicate (user, book)")
except Exception as e:
    if "unique" in str(e).lower() or "duplicate" in str(e).lower():
        print("✓ Correctly rejected duplicate (user, book) combination")
    else:
        print(f"✗ FAILED: Wrong error: {e}")

# Test 3: Test quantity validation (zero quantity)
print("\n3. Testing zero quantity validation...")
try:
    invalid_item = CartItem(
        user=user,
        book=book,
        quantity=0
    )
    invalid_item.clean()
    print("✗ FAILED: Should have raised ValidationError for zero quantity")
except ValidationError as e:
    if "Quantity must be positive" in str(e):
        print("✓ Correctly rejected zero quantity")
    else:
        print(f"✗ FAILED: Wrong error message: {e}")

# Test 4: Test quantity validation (negative quantity)
print("\n4. Testing negative quantity validation...")
try:
    invalid_item = CartItem(
        user=user,
        book=book,
        quantity=-5
    )
    invalid_item.clean()
    print("✗ FAILED: Should have raised ValidationError for negative quantity")
except ValidationError as e:
    if "Quantity must be positive" in str(e):
        print("✓ Correctly rejected negative quantity")
    else:
        print(f"✗ FAILED: Wrong error message: {e}")

# Test 5: Test stock availability validation (exceeds stock)
print("\n5. Testing stock availability validation...")
try:
    invalid_item = CartItem(
        user=user,
        book=book,
        quantity=15  # book has stock_quantity=10
    )
    invalid_item.clean()
    print("✗ FAILED: Should have raised ValidationError for quantity exceeding stock")
except ValidationError as e:
    if "exceeds available stock" in str(e):
        print("✓ Correctly rejected quantity exceeding stock")
    else:
        print(f"✗ FAILED: Wrong error message: {e}")

# Test 6: Test quantity equal to stock (should be allowed)
print("\n6. Testing quantity equal to stock (should be allowed)...")
try:
    # Create a new user to avoid unique constraint
    user2 = User.objects.create_user(username='testuser2', email='test2@example.com', password='test_password')
    valid_item = CartItem(
        user=user2,
        book=book,
        quantity=10  # exactly equal to stock_quantity
    )
    valid_item.clean()
    valid_item.save()
    print("✓ Quantity equal to stock correctly allowed")
except ValidationError as e:
    print(f"✗ FAILED: Should allow quantity equal to stock: {e}")

# Test 7: Test CASCADE delete on user deletion
print("\n7. Testing CASCADE delete on user deletion...")
test_user = User.objects.create_user(username='tempuser', email='temp@example.com', password='test_password')
test_item = CartItem.objects.create(
    user=test_user,
    book=book,
    quantity=2
)
item_id = test_item.id
test_user.delete()
if not CartItem.objects.filter(id=item_id).exists():
    print("✓ CartItem correctly deleted when user is deleted (CASCADE)")
else:
    print("✗ FAILED: CartItem should be deleted when user is deleted")

# Test 8: Test CASCADE delete on book deletion
print("\n8. Testing CASCADE delete on book deletion...")
test_book = Book.objects.create(
    title="Temp Book",
    author="Temp Author",
    description="Temp description",
    price=Decimal("15.00"),
    stock_quantity=5,
    image_url="https://example.com/temp.jpg"
)
test_item = CartItem.objects.create(
    user=user,
    book=test_book,
    quantity=2
)
item_id = test_item.id
test_book.delete()
if not CartItem.objects.filter(id=item_id).exists():
    print("✓ CartItem correctly deleted when book is deleted (CASCADE)")
else:
    print("✗ FAILED: CartItem should be deleted when book is deleted")

# Test 9: Test ordering (most recent first)
print("\n9. Testing cart item ordering (most recent first)...")
user3 = User.objects.create_user(username='testuser3', email='test3@example.com', password='test_password')
book2 = Book.objects.create(
    title="Book 2",
    author="Author 2",
    description="Description 2",
    price=Decimal("20.00"),
    stock_quantity=10,
    image_url="https://example.com/image2.jpg"
)
item1 = CartItem.objects.create(user=user3, book=book, quantity=1)
item2 = CartItem.objects.create(user=user3, book=book2, quantity=2)
items = CartItem.objects.filter(user=user3)
if items[0].id == item2.id:
    print("✓ CartItems correctly ordered by added_at descending")
else:
    print(f"✗ FAILED: Expected item2 first, got item with id {items[0].id}")

# Test 10: Test default quantity value
print("\n10. Testing default quantity value...")
item_with_default = CartItem(
    user=user,
    book=book2
)
if item_with_default.quantity == 1:
    print("✓ Default quantity correctly set to 1")
else:
    print(f"✗ FAILED: Expected default quantity 1, got {item_with_default.quantity}")

print("\n" + "="*50)
print("All CartItem model validation tests completed!")
print("="*50)

# Cleanup
print("\nCleaning up test data...")
CartItem.objects.all().delete()
Book.objects.all().delete()
Category.objects.all().delete()
User.objects.filter(username__startswith='test').delete()
User.objects.filter(username='tempuser').delete()
print("✓ Cleanup complete")
