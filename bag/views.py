from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """ A View to render the bag contents"""
    
    return render(request, 'bag/view_bag.html')