from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
# Create your views here.


# Getting the cart from the session
# If nothing in the cart then we send the user a simple message
# Return the user back to the products page, prevents users from manual trying to go to checkout with /checkout
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))


    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KPtzwBGgu454z77IzaPYy6MShReGnWUwoTwL2DRppH8l5nmE3j6pXDRERD8U1V5hJf3pijYDerLCKyqiD76Rve200V9kmOilI',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)