"""
Seed data script for bookshop database.
Run with: python manage.py shell < seed_data.py
"""
from books.models import Category, Book
from decimal import Decimal

print("Starting database seeding...")

# Clear existing data
print("\nClearing existing data...")
Book.objects.all().delete()
Category.objects.all().delete()

# Create categories
print("\nCreating categories...")
categories = {
    'Fiction': Category.objects.create(name='Fiction', description='Fictional stories and novels'),
    'Science': Category.objects.create(name='Science', description='Scientific books and research'),
    'Technology': Category.objects.create(name='Technology', description='Technology and programming books'),
    'History': Category.objects.create(name='History', description='Historical books and biographies'),
    'Business': Category.objects.create(name='Business', description='Business and entrepreneurship'),
    'Self-Help': Category.objects.create(name='Self-Help', description='Personal development and motivation'),
}
print(f"✓ Created {len(categories)} categories")

# Create books
print("\nCreating books...")
books_data = [
    # Fiction
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'category': 'Fiction', 'price': '12.99', 'stock': 25, 'image': 'https://covers.openlibrary.org/b/id/7222246-L.jpg'},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'category': 'Fiction', 'price': '14.99', 'stock': 18, 'image': 'https://covers.openlibrary.org/b/id/8228691-L.jpg'},
    {'title': '1984', 'author': 'George Orwell', 'category': 'Fiction', 'price': '13.99', 'stock': 30, 'image': 'https://covers.openlibrary.org/b/id/7222246-L.jpg'},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'category': 'Fiction', 'price': '11.99', 'stock': 22, 'image': 'https://covers.openlibrary.org/b/id/8235657-L.jpg'},
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'category': 'Fiction', 'price': '13.50', 'stock': 15, 'image': 'https://covers.openlibrary.org/b/id/8228691-L.jpg'},
    {'title': 'Harry Potter and the Sorcerer\'s Stone', 'author': 'J.K. Rowling', 'category': 'Fiction', 'price': '16.99', 'stock': 40, 'image': 'https://covers.openlibrary.org/b/id/10521270-L.jpg'},
    {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'category': 'Fiction', 'price': '15.99', 'stock': 28, 'image': 'https://covers.openlibrary.org/b/id/8235657-L.jpg'},
    {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'category': 'Fiction', 'price': '24.99', 'stock': 20, 'image': 'https://covers.openlibrary.org/b/id/7222246-L.jpg'},
    {'title': 'Animal Farm', 'author': 'George Orwell', 'category': 'Fiction', 'price': '10.99', 'stock': 3, 'image': 'https://covers.openlibrary.org/b/id/8228691-L.jpg'},
    {'title': 'Brave New World', 'author': 'Aldous Huxley', 'category': 'Fiction', 'price': '12.50', 'stock': 0, 'image': 'https://covers.openlibrary.org/b/id/8235657-L.jpg'},
    
    # Science
    {'title': 'A Brief History of Time', 'author': 'Stephen Hawking', 'category': 'Science', 'price': '18.99', 'stock': 12, 'image': 'https://covers.openlibrary.org/b/id/8228691-L.jpg'},
    {'title': 'Sapiens', 'author': 'Yuval Noah Harari', 'category': 'Science', 'price': '19.99', 'stock': 35, 'image': 'https://covers.openlibrary.org/b/id/10521270-L.jpg'},
    {'title': 'The Selfish Gene', 'author': 'Richard Dawkins', 'category': 'Science', 'price': '17.99', 'stock': 14, 'image': 'https://covers.openlibrary.org/b/id/7222246-L.jpg'},
    {'title': 'Cosmos', 'author': 'Carl Sagan', 'category': 'Science', 'price': '16.99', 'stock': 20, 'image': 'https://covers.openlibrary.org/b/id/8235657-L.jpg'},
    {'title': 'The Origin of Species', 'author': 'Charles Darwin', 'category': 'Science', 'price': '15.99', 'stock': 8, 'image': 'https://covers.openlibrary.org/b/id/8228691-L.jpg'},
    {'title': 'Astrophysics for People in a Hurry', 'author': 'Neil deGrasse Tyson', 'category': 'Science', 'price': '14.99', 'stock': 25, 'image': 'https://covers.openlibrary.org/b/id/10521270-L.jpg'},
    {'title': 'The Gene', 'author': 'Siddhartha Mukherjee', 'category': 'Science', 'price': '20.99', 'stock': 2, 'image': 'https://covers.openlibrary.org/b/id/7222246-L.jpg'},
    
    # Technology
    {'title': 'Clean Code', 'author': 'Robert C. Martin', 'category': 'Technology', 'price': '42.99', 'stock': 18, 'image': 'https://covers.openlibrary.org/b/id/8235657-L.jpg'},
    {'title': 'The Pragmatic Programmer', 'author': 'Andrew Hunt', 'category': 'Technology', 'price': '39.99', 'stock': 22, 'image': 'https://covers.openlibrary.org/b/id/8228691-L.jpg'},
    {'title': 'Design Patterns', 'author': 'Gang of Four', 'category': 'Technology', 'price': '44.99', 'stock': 15, 'image': 'https://covers.openlibrary.org/b/id/10521270-L.jpg'},
    {'title': 'Introduction to Algorithms', 'author': 'Thomas H. Cormen', 'category': 'Technology', 'price': '89.99', 'stock': 10, 'image': 'https://covers.openlibrary.org/b/id/7222246-L.jpg'},
    {'title': 'Python Crash Course', 'author': 'Eric Matthes', 'category': 'Technology', 'price': '34.99', 'stock': 30, 'image': 'https://covers.openlibrary.org/b/id/8235657-L.jpg'},
    {'title': 'JavaScript: The Good Parts', 'author': 'Douglas Crockford', 'category': 'Technology', 'price': '29.99', 'stock': 4, 'image': 'https://covers.openlibrary.org/b/id/8228691-L.jpg'},
    {'title': 'You Don\'t Know JS', 'author': 'Kyle Simpson', 'category': 'Technology', 'price': '32.99', 'stock': 0, 'image': 'https://covers.openlibrary.org/b/id/10521270-L.jpg'},
    
    # History
    {'title': 'The Diary of a Young Girl', 'author': 'Anne Frank', 'category': 'History', 'price': '11.99', 'stock': 20, 'image': 'https://covers.openlibrary.org/b/id/7222246-L.jpg'},
    {'title': 'Guns, Germs, and Steel', 'author': 'Jared Diamond', 'category': 'History', 'price': '18.99', 'stock': 16, 'image': 'https://covers.openlibrary.org/b/id/8235657-L.jpg'},
    {'title': 'The Rise and Fall of the Third Reich', 'author': 'William L. Shirer', 'category': 'History', 'price': '22.99', 'stock': 12, 'image': 'https://covers.openlibrary.org/b/id/8228691-L.jpg'},
    {'title': 'A People\'s History of the United States', 'author': 'Howard Zinn', 'category': 'History', 'price': '19.99', 'stock': 14, 'image': 'https://covers.openlibrary.org/b/id/10521270-L.jpg'},
    {'title': 'The Silk Roads', 'author': 'Peter Frankopan', 'category': 'History', 'price': '21.99', 'stock': 3, 'image': 'https://covers.openlibrary.org/b/id/7222246-L.jpg'},
    
    # Business
    {'title': 'Think and Grow Rich', 'author': 'Napoleon Hill', 'category': 'Business', 'price': '14.99', 'stock': 28, 'image': 'https://covers.openlibrary.org/b/id/8235657-L.jpg'},
    {'title': 'Rich Dad Poor Dad', 'author': 'Robert Kiyosaki', 'category': 'Business', 'price': '16.99', 'stock': 32, 'image': 'https://covers.openlibrary.org/b/id/8228691-L.jpg'},
    {'title': 'The Lean Startup', 'author': 'Eric Ries', 'category': 'Business', 'price': '24.99', 'stock': 18, 'image': 'https://covers.openlibrary.org/b/id/10521270-L.jpg'},
    {'title': 'Zero to One', 'author': 'Peter Thiel', 'category': 'Business', 'price': '22.99', 'stock': 20, 'image': 'https://covers.openlibrary.org/b/id/7222246-L.jpg'},
    {'title': 'Good to Great', 'author': 'Jim Collins', 'category': 'Business', 'price': '26.99', 'stock': 15, 'image': 'https://covers.openlibrary.org/b/id/8235657-L.jpg'},
    {'title': 'The 4-Hour Workweek', 'author': 'Tim Ferriss', 'category': 'Business', 'price': '19.99', 'stock': 25, 'image': 'https://covers.openlibrary.org/b/id/8228691-L.jpg'},
    {'title': 'Start with Why', 'author': 'Simon Sinek', 'category': 'Business', 'price': '21.99', 'stock': 2, 'image': 'https://covers.openlibrary.org/b/id/10521270-L.jpg'},
    
    # Self-Help
    {'title': 'Atomic Habits', 'author': 'James Clear', 'category': 'Self-Help', 'price': '16.99', 'stock': 45, 'image': 'https://covers.openlibrary.org/b/id/7222246-L.jpg'},
    {'title': 'The 7 Habits of Highly Effective People', 'author': 'Stephen Covey', 'category': 'Self-Help', 'price': '17.99', 'stock': 30, 'image': 'https://covers.openlibrary.org/b/id/8235657-L.jpg'},
    {'title': 'How to Win Friends and Influence People', 'author': 'Dale Carnegie', 'category': 'Self-Help', 'price': '13.99', 'stock': 28, 'image': 'https://covers.openlibrary.org/b/id/8228691-L.jpg'},
    {'title': 'The Power of Now', 'author': 'Eckhart Tolle', 'category': 'Self-Help', 'price': '15.99', 'stock': 22, 'image': 'https://covers.openlibrary.org/b/id/10521270-L.jpg'},
    {'title': 'Mindset', 'author': 'Carol S. Dweck', 'category': 'Self-Help', 'price': '16.99', 'stock': 20, 'image': 'https://covers.openlibrary.org/b/id/7222246-L.jpg'},
    {'title': 'The Subtle Art of Not Giving a F*ck', 'author': 'Mark Manson', 'category': 'Self-Help', 'price': '18.99', 'stock': 35, 'image': 'https://covers.openlibrary.org/b/id/8235657-L.jpg'},
    {'title': 'Can\'t Hurt Me', 'author': 'David Goggins', 'category': 'Self-Help', 'price': '19.99', 'stock': 4, 'image': 'https://covers.openlibrary.org/b/id/8228691-L.jpg'},
    {'title': 'The Alchemist', 'author': 'Paulo Coelho', 'category': 'Self-Help', 'price': '14.99', 'stock': 0, 'image': 'https://covers.openlibrary.org/b/id/10521270-L.jpg'},
]

for book_data in books_data:
    Book.objects.create(
        title=book_data['title'],
        author=book_data['author'],
        description=f"A great book about {book_data['title']}",
        price=Decimal(book_data['price']),
        stock_quantity=book_data['stock'],
        category=categories[book_data['category']],
        image_url=book_data['image']
    )

print(f"✓ Created {len(books_data)} books")

# Summary
print("\n" + "="*50)
print("Database seeding completed successfully!")
print("="*50)
print(f"\nCategories: {Category.objects.count()}")
print(f"Books: {Book.objects.count()}")
print("\nStock summary:")
print(f"  In stock: {Book.objects.filter(stock_quantity__gt=5).count()}")
print(f"  Low stock: {Book.objects.filter(stock_quantity__lte=5, stock_quantity__gt=0).count()}")
print(f"  Out of stock: {Book.objects.filter(stock_quantity=0).count()}")
