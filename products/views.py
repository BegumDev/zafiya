from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view to show product details """

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'products': products,
    }
    
    return render(request, 'products/product_details.html', context)