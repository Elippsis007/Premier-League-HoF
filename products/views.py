from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    # This will return products/products.html and also context so we can send things back to the template
    return render(request, 'products/products.html', context)