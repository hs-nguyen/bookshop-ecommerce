from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['book', 'quantity', 'price_at_purchase']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'order_date', 'total_price', 'status']
    list_filter = ['status', 'order_date']
    search_fields = ['user__username']
    readonly_fields = ['order_date', 'total_price']
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'book', 'quantity', 'price_at_purchase']
    list_filter = ['order__order_date']
    search_fields = ['book__title', 'order__user__username']
