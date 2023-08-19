from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the cart contents page """

    return render(request, 'bag/bag.html')

# A view that takes both the request and the item_id which is the id of the product the user would like to add to the bag
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """
    
    product = get_object_or_404(Product, pk=item_id)
# Getting the quantity from the form, it has to be converted to an interger since it will come from the template as a string
    quantity = int(request.POST.get('quantity'))
# I want to get the redirect URL from the form so I know where to redirect once the process is finished
    redirect_url = request.POST.get('redirect_url')
    # Adding size equal to None at first then if product size is in request.post it will be set equal to that request.
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    # This is an if statement to see if the product with 'sizes' is being added to the cart
    # If items are not already in the cart the user just has to add it.
    if size:
        # If the item is already in the cart then there is a check to see if the same 'id' and same 'size'
        # already exist
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
    # If it is the case then the qty is increased for that size and otherwise set to equal to the qty as the item exists in the bag
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['item_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your cart')
        else:
            # A dictionary with a key of 'items_by_size' for the case that if there are multiple
            # items with the same 'item_id' but when there are diffirent sizes
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your cart')
    # if there is no size I can run the following
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')
    
    request.session['bag'] = bag
    return redirect(redirect_url)
    

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your cart')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your cart')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item {e}')
        return HttpResponse(status=500)

# A session allows information to be stored until the client and server are done communicating.
# Allowing me to store the contents in the shopping cart while in the HTTP session while a user browses the site and adds
# items to be purchased, without the fear of losing all items in the cart.

# Creating a variable called cart which accesses the request session trying to get this variable if it already exists
# and initializing it to an "empty dictionary" if it doesn't
# Checking to see if there is a cart variable in the session and if not then one will be created.