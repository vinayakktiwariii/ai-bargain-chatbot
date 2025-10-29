from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'list_price', 'min_price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
