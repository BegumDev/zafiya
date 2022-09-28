from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_bag(request):
    """ A View to render the bag contents"""
    
    return render(request, 'bag/view_bag.html')


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