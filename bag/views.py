from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.
# view the shopping bag
def view_bag(request):
    """ A View to render the bag contents"""
    
    return render(request, 'bag/view_bag.html')

# add to bag view
def add_to_bag(request, item_id):
    """ A view to add items to the bag contents """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})  # Get the bag items if there is one or CREATE one if there isnt.

    if item_id in list(bag.keys()):
        bag[item_id] += quantity  # If theres already that item in the bag - add to it
    else:
        bag[item_id] = quantity  # Or if not, then add just that one.
    
    request.session['bag'] = bag  # Then store the new information in the session with the updated quantity.

    print(request.session['bag'])
    return redirect(redirect_url)

# adjust the bag
def adjust_bag(request, item_id):
    """ A view to adjust the shopping bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


# remove from bag view
def remove_from_bag(request, item_id):
    """ A view to delete from the bag """
    try:
        bag = request.session.get('bag', {})

        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)