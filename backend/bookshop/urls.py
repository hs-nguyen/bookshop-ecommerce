"""
URL configuration for bookshop project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/', include('books.urls')),
    path('api/', include('cart.urls')),
    path('api/', include('orders.urls')),
]
