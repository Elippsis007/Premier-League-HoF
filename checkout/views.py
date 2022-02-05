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
    }

    return render(request, template, context)