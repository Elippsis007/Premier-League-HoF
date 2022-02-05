from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


# Getting the cart from the session
# If nothing in the cart then we send the user a simple message
# Return the user back to the products page, prevents users from manual trying to go to checkout with /checkout
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KPtzwBGgu454z77IzaPYy6MShReGnWUwoTwL2DRppH8l5nmE3j6pXDRERD8U1V5hJf3pijYDerLCKyqiD76Rve200V9kmOilI',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)