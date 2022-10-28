from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.
# view the shopping bag
def view_bag(request):
    """ A View to render the bag contents"""
    
    return render(request, 'bag/view_bag.html')


# add to bag view
def add_to_bag(request, item_id):
    """ A view to add items to the bag contents """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})  # Get the bag items if there is one or CREATE one if there isnt.

    if item_id in list(bag.keys()):
        bag[item_id] += quantity  # If theres already that item in the bag - add to it
        messages.success(request, f'Updated {product.name} to {bag[item_id]}')
    else:
        bag[item_id] = quantity  # Or if not, then add just that one.
        messages.success(request, f'Added {product.name} to your bag')
    
    request.session['bag'] = bag  # Then store the new information in the session with the updated quantity.

    # print(request.session['bag'])
    return redirect(redirect_url)

# adjust the bag
def adjust_bag(request, item_id):
    """ A view to adjust the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from the bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


# remove from bag view
def remove_from_bag(request, item_id):
    """ A view to delete from the bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from the bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing from bag: {e}')
        return HttpResponse(status=500)