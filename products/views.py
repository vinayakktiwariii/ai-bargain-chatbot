from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    """Display all products"""
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    """Display single product with chat interface"""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def about(request):
    """Display about page"""
    return render(request, 'products/about.html')
