from django.contrib import admin
from .models import Order, OrderLineItem

# The inline item will allow to add and edit line items in the admin console
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

# Fields that will be calculated by the model methods, these will not be editable by anyone
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)
# This allow the specifity of the order of the fields in the admin console
    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total',)
# Restricts columns that show in the order list to a minimal amout of key items
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

# Sets the order to be in reverse by chronological order
    ordering = ('-date',)

# Registrtation of order model and orderAdmin model
admin.site.register(Order, OrderAdmin)