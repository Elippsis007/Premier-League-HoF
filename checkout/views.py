from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
# Create your views here.

def checkout(request):
    # Getting the bag from the session
    bag = request.session.get('bag', {})
    # If nothing in the bag then we send the user a simple message
    if not bag:
        messages.error(request, "There's nothing in your cart at the moment")
        # Return the user back to the products page, prevents users from manual trying to go to checkout with /checkout 
        return redirect(reverse('products'))

    order_form = OrderForm()
    # Creating the template
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)