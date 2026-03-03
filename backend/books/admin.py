from django.contrib import admin
from .models import Category, Book


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'stock_quantity', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'author']
    readonly_fields = ['created_at', 'updated_at']
