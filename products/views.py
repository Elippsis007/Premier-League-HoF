from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """ A view to show all individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    # This will return products/products.html and also context so we can send things back to the template
    return render(request, 'products/product_detail.html', context)