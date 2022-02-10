from django.db.models.signals import post_save, post_delete # Post means the signals are sent to django to the entire application
from django.dispatch import receiver # Enables the ability to receive signals

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """

    instance.order.update_total()