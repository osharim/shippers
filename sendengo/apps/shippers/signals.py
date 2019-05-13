# encoding: utf-8
# Manage increment and decrements in shipper.num_requirements 
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.db.models import F 
from .models import ShipperRequirement


@receiver(post_delete, sender=ShipperRequirement, dispatch_uid="delete_counter_requirements")
def decrement_requirements(sender, instance, **kwargs):

    if instance.shipper.num_requirements > 0:
        instance.shipper.num_requirements = instance.shipper.shipperrequirement_set.all().count() 
        instance.shipper.save(update_fields=["num_requirements"])


@receiver(post_save, sender=ShipperRequirement, dispatch_uid="save_counter_requirements")
def increment_requirements(sender, instance, created, **kwargs):
    if created:
        instance.shipper.num_requirements = instance.shipper.shipperrequirement_set.all().count() 
        instance.shipper.save(update_fields=["num_requirements"])