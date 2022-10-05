from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KXp07HzSDZpmx6DtJTZjjqIQxiZfhX7zAAGRhUf1KXUQ39cgRc8AqZmsZzBpIV63g5hY1rbKqomiafppywxc3Pq00N8VACZsg',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)