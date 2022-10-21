from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Product
from .forms import ProductForm


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view to show product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    
    return render(request, 'products/product_details.html', context)


def add_product(request):
    """ A view for admin to add products """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product.')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please try again.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ A view to edit the product """
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sucessfully updated product')
            return redirect(reverse('product_details', args=[product_id]))
        else:
            messages.error(request, 'Failed to update product. Please check the form again.')
    else:
        form = ProductForm(instance=product)
        messages.success(request, f'You are updating {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)