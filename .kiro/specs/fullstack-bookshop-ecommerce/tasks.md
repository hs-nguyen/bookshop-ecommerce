# Implementation Plan: Fullstack Bookshop Ecommerce

## Overview

This implementation plan breaks down the fullstack bookshop ecommerce platform into discrete coding tasks. The system consists of a Django REST Framework backend with PostgreSQL database and a Vue.js frontend. Tasks are organized to build incrementally, starting with backend infrastructure, then frontend components, and finally integration.

## Tasks

- [x] 1. Set up backend project structure and database
  - Create Django project with REST framework configuration
  - Configure PostgreSQL database connection
  - Set up JWT authentication with djangorestframework-simplejwt
  - Create initial Django apps: books, cart, orders, authentication
  - Configure CORS for frontend communication
  - Create requirements.txt with all dependencies
  - _Requirements: 11.1, 11.2, 11.3, 11.4, 11.5, 11.6_

- [-] 2. Implement database models and migrations
  - [x] 2.1 Create Category model with validation
    - Implement Category model with name and description fields
    - Add unique constraint on category name
    - Create and run migrations
    - _Requirements: 2.6, 11.2_
  
  - [x] 2.2 Create Book model with validation
    - Implement Book model with all required fields
    - Add validation for positive price and non-negative stock
    - Add foreign key relationship to Category with SET_NULL on delete
    - Create and run migrations
    - _Requirements: 1.6, 1.7, 1.8, 11.1, 11.8_
  
  - [ ] 2.3 Create CartItem model with validation
    - Implement CartItem model with user, book, and quantity fields
    - Add unique constraint on (user, book) combination
    - Add validation for quantity against stock availability
    - Create and run migrations
    - _Requirements: 4.6, 11.4_
  
  - [ ] 2.4 Create Order and OrderItem models
    - Implement Order model with user, order_date, total_price, and status fields
    - Implement OrderItem model with order, book, quantity, and price_at_purchase fields
    - Add foreign key relationships with appropriate cascade rules
    - Create and run migrations
    - _Requirements: 5.7, 11.5, 11.6, 11.7_

- [ ] 3. Implement authentication system
  - [ ] 3.1 Create user registration endpoint
    - Implement UserSerializer with password hashing
    - Create RegisterView for user registration
    - Add validation for username, email, and password requirements
    - _Requirements: 3.1, 3.3_
  
  - [ ] 3.2 Create login and token endpoints
    - Implement LoginView using JWT authentication
    - Configure token generation and refresh endpoints
    - Return authentication token on successful login
    - _Requirements: 3.2, 3.4_
  
  - [ ] 3.3 Create user profile endpoints
    - Implement UserProfileView for GET, PUT, and DELETE operations
    - Add authentication requirement using JWT middleware
    - Add validation for profile updates
    - _Requirements: 3.5, 3.6, 3.7, 3.8, 3.9_

- [ ] 4. Implement category management API
  - [ ] 4.1 Create CategorySerializer and ViewSet
    - Implement CategorySerializer with validation
    - Create CategoryViewSet with CRUD operations
    - Add admin-only permissions for create, update, delete
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5_
  
  - [ ] 4.2 Add category books endpoint
    - Implement custom action to retrieve all books in a category
    - Add filtering and pagination
    - _Requirements: 2.7_
  
  - [ ]* 4.3 Write unit tests for category endpoints
    - Test category creation, retrieval, update, and deletion
    - Test permission restrictions for non-admin users
    - Test category books retrieval
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.7_

- [ ] 5. Implement book management API
  - [ ] 5.1 Create BookSerializer with validation
    - Implement BookSerializer with all fields
    - Add validation for price, stock quantity, and image URL format
    - Include category relationship serialization
    - _Requirements: 1.7, 1.8, 10.6_
  
  - [ ] 5.2 Create BookViewSet with CRUD operations
    - Implement BookViewSet with list, create, retrieve, update, delete actions
    - Add admin-only permissions for create, update, delete
    - Add category filtering support
    - Add pagination for book list
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5_
  
  - [ ]* 5.3 Write unit tests for book endpoints
    - Test book creation with validation
    - Test book retrieval, update, and deletion
    - Test category filtering
    - Test permission restrictions
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.7, 1.8_

- [ ] 6. Checkpoint - Ensure backend catalog tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 7. Implement shopping cart API
  - [ ] 7.1 Create CartItemSerializer with validation
    - Implement CartItemSerializer with book and quantity fields
    - Add validation for quantity against available stock
    - Include book details in serialization
    - _Requirements: 4.7, 4.8_
  
  - [ ] 7.2 Create CartViewSet with cart operations
    - Implement endpoints for add, retrieve, update, remove cart items
    - Add custom action for clearing entire cart
    - Ensure all operations are user-specific (filter by authenticated user)
    - Add validation to prevent quantity exceeding stock
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6_
  
  - [ ]* 7.3 Write unit tests for cart endpoints
    - Test adding items to cart with stock validation
    - Test updating quantities and removing items
    - Test cart clearing
    - Test user isolation (users can only access their own cart)
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.7, 4.8_

- [ ] 8. Implement order processing API
  - [ ] 8.1 Create OrderSerializer with nested items
    - Implement OrderSerializer with order details
    - Implement OrderItemSerializer for line items
    - Include nested serialization of order items
    - _Requirements: 5.2, 5.7_
  
  - [ ] 8.2 Create order creation endpoint with transaction handling
    - Implement create order endpoint that processes cart items
    - Add transaction wrapper to ensure atomicity
    - Validate stock availability for all cart items before processing
    - Reduce stock quantity for each ordered book
    - Calculate and store total price
    - Clear user's cart after successful order creation
    - Return stock error if any item has insufficient stock
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.8_
  
  - [ ] 8.3 Create order retrieval endpoints
    - Implement endpoint to list all orders for authenticated user
    - Implement endpoint to retrieve single order by ID
    - Add admin endpoint to retrieve all orders from all customers
    - Add permission checks for user-specific orders
    - _Requirements: 5.5, 5.6, 5.9_
  
  - [ ]* 8.4 Write unit tests for order endpoints
    - Test order creation from cart with stock reduction
    - Test stock validation and error handling
    - Test cart clearing after order
    - Test order retrieval with user isolation
    - Test admin access to all orders
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.8, 5.9_

- [ ] 9. Add backend error handling and validation
  - [ ] 9.1 Implement global exception handler
    - Create custom exception handler for DRF
    - Add descriptive error messages for validation errors
    - Add error logging for database failures
    - Return appropriate HTTP status codes
    - _Requirements: 10.1, 10.2, 10.5_
  
  - [ ] 9.2 Add request validation middleware
    - Implement middleware to validate required fields
    - Add validation for data types and formats
    - Return clear error messages for invalid requests
    - _Requirements: 10.1, 10.5_

- [ ] 10. Checkpoint - Ensure all backend tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 11. Set up frontend project structure
  - Create Vue.js 3 project with Vite
  - Install dependencies: Vue Router, Vuex/Pinia, Axios
  - Configure Vue Router with route definitions
  - Set up Vuex store with modules for auth, books, categories, cart, orders
  - Create base layout components (AppHeader, AppFooter)
  - Configure Axios client with base URL and interceptors
  - _Requirements: 6.4, 7.7, 9.3_

- [ ] 12. Implement API communication layer
  - [ ] 12.1 Create Axios client configuration
    - Set up Axios instance with base URL
    - Add request interceptor to attach authentication token
    - Add response interceptor for error handling
    - _Requirements: 9.3_
  
  - [ ] 12.2 Create API service modules
    - Implement api/auth.js with register, login, profile methods
    - Implement api/books.js with book CRUD methods
    - Implement api/categories.js with category methods
    - Implement api/cart.js with cart management methods
    - Implement api/orders.js with order methods
    - _Requirements: 6.4, 7.7_

- [ ] 13. Implement authentication components and store
  - [ ] 13.1 Create auth Vuex store module
    - Implement state for user, token, isAuthenticated
    - Implement actions for login, logout, register, profile operations
    - Implement mutations for updating auth state
    - Add token persistence to localStorage
    - _Requirements: 9.3, 9.4_
  
  - [ ] 13.2 Create LoginForm component
    - Implement login form with username and password fields
    - Add form validation
    - Call auth store action on submit
    - Display error messages
    - Redirect to home on successful login
    - _Requirements: 9.2, 9.3_
  
  - [ ] 13.3 Create RegisterForm component
    - Implement registration form with username, email, password fields
    - Add password confirmation validation
    - Call auth store action on submit
    - Display error messages
    - Redirect to login on successful registration
    - _Requirements: 9.1_
  
  - [ ] 13.4 Create UserProfile component
    - Display user profile information
    - Implement edit mode for updating profile
    - Add delete account functionality with confirmation
    - _Requirements: 9.6_
  
  - [ ] 13.5 Update AppHeader with authentication state
    - Display login/register links when not authenticated
    - Display username and logout button when authenticated
    - Add navigation to profile page
    - _Requirements: 9.4, 9.5_

- [ ] 14. Implement category components and store
  - [ ] 14.1 Create categories Vuex store module
    - Implement state for categories list and selected category
    - Implement actions to fetch categories
    - Implement mutations for updating category state
    - _Requirements: 6.5_
  
  - [ ] 14.2 Create CategoryFilter component
    - Display list of all categories
    - Add "All Categories" option
    - Emit category-selected event on selection
    - Highlight selected category
    - _Requirements: 6.5_

- [ ] 15. Implement book display components and store
  - [ ] 15.1 Create books Vuex store module
    - Implement state for books list, current book, loading state
    - Implement actions to fetch books with optional category filter
    - Implement action to fetch single book details
    - Implement mutations for updating book state
    - _Requirements: 6.4_
  
  - [ ] 15.2 Create BookCard component
    - Display book image, title, author, and price
    - Display stock availability status
    - Show "Out of Stock" indicator when stock is zero
    - Add "Add to Cart" button (disabled when out of stock)
    - Emit add-to-cart event
    - _Requirements: 6.1, 6.2, 6.6_
  
  - [ ] 15.3 Create BookList component
    - Display grid of BookCard components
    - Integrate CategoryFilter component
    - Fetch books on mount and when category changes
    - Handle loading and error states
    - Call cart store action when add-to-cart is triggered
    - _Requirements: 6.1, 6.4, 6.5_
  
  - [ ] 15.4 Create BookDetail component
    - Display full book information including description and category
    - Display stock availability
    - Add "Add to Cart" button with quantity selector
    - Fetch book details on mount
    - _Requirements: 6.3_

- [ ] 16. Checkpoint - Ensure frontend book display works
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 17. Implement shopping cart components and store
  - [ ] 17.1 Create cart Vuex store module
    - Implement state for cart items, item count, total price
    - Implement actions for add, update, remove, clear cart operations
    - Implement computed getters for item count and total price
    - Sync with backend API for all operations
    - _Requirements: 7.7_
  
  - [ ] 17.2 Create CartIcon component
    - Display cart icon with item count badge
    - Update count reactively from store
    - Navigate to cart page on click
    - _Requirements: 7.1_
  
  - [ ] 17.3 Create CartItem component
    - Display book details, quantity, and subtotal
    - Add increment/decrement quantity controls
    - Add remove button
    - Emit update-quantity and remove-item events
    - _Requirements: 7.3, 7.5, 7.6_
  
  - [ ] 17.4 Create CartView component
    - Display list of CartItem components
    - Display total price for all items
    - Add "Clear Cart" button
    - Add "Checkout" button
    - Handle empty cart state
    - Call store actions for quantity updates and item removal
    - Navigate to order confirmation on successful checkout
    - _Requirements: 7.3, 7.4, 7.5, 7.6, 7.7_
  
  - [ ] 17.5 Add cart button to book components
    - Update BookCard and BookDetail to trigger cart actions
    - Display success feedback when item added
    - Update cart icon count immediately
    - _Requirements: 7.2_

- [ ] 18. Implement order components and store
  - [ ] 18.1 Create orders Vuex store module
    - Implement state for orders list and current order
    - Implement actions to create order and fetch orders
    - Implement action to fetch single order details
    - Implement mutations for updating order state
    - _Requirements: 8.1_
  
  - [ ] 18.2 Create OrderConfirmation component
    - Display order success message with order ID
    - Fetch and display order details
    - Add link to view full order details
    - Add link to continue shopping
    - _Requirements: 8.2_
  
  - [ ] 18.3 Create OrderHistory component
    - Display list of all user orders
    - Show order date, total price, and status for each order
    - Add link to view order details
    - Handle empty state when no orders exist
    - _Requirements: 8.3_
  
  - [ ] 18.4 Create OrderDetail component
    - Display complete order information
    - Show order items with quantities and prices
    - Display order total and status
    - _Requirements: 8.4_
  
  - [ ] 18.5 Integrate checkout flow
    - Update CartView to call order creation action
    - Clear cart display after successful order
    - Handle stock errors during checkout
    - Redirect to order confirmation page
    - _Requirements: 8.1, 8.5_

- [ ] 19. Implement frontend error handling
  - [ ] 19.1 Add error handling to API client
    - Implement response interceptor to catch errors
    - Display user-friendly error messages for API errors
    - Handle network connection errors
    - Handle authentication errors (redirect to login)
    - _Requirements: 10.3, 10.4_
  
  - [ ] 19.2 Add error display components
    - Create ErrorMessage component for inline errors
    - Create Toast/Notification component for global errors
    - Integrate error display in all forms and views
    - _Requirements: 10.3_

- [ ] 20. Implement route guards and authentication flow
  - [ ] 20.1 Add navigation guards
    - Implement beforeEach guard to check authentication
    - Redirect to login for protected routes when not authenticated
    - Restore authentication state from localStorage on app load
    - _Requirements: 9.7_
  
  - [ ] 20.2 Protect cart and order routes
    - Add authentication requirement to cart routes
    - Add authentication requirement to order routes
    - Add authentication requirement to profile routes
    - _Requirements: 9.7_

- [ ] 21. Final integration and testing
  - [ ] 21.1 Test complete user flows
    - Test registration and login flow
    - Test browsing books and filtering by category
    - Test adding items to cart and updating quantities
    - Test checkout and order creation
    - Test viewing order history
    - _Requirements: All_
  
  - [ ] 21.2 Test error scenarios
    - Test stock validation errors
    - Test authentication errors
    - Test network error handling
    - Test form validation errors
    - _Requirements: 10.1, 10.2, 10.3, 10.4_
  
  - [ ] 21.3 Test admin functionality
    - Test admin access to all orders
    - Test book and category management (if admin UI implemented)
    - _Requirements: 5.9_

- [ ] 22. Final checkpoint - Complete system validation
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Backend tasks (1-10) should be completed before frontend tasks (11-21)
- Checkpoints ensure incremental validation at key milestones
- The implementation assumes Django and Vue.js development environments are set up
- Database migrations should be run after each model change
- Frontend development server and backend API server should run concurrently during development
