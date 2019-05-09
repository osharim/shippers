# encoding: utf-8
from rest_framework import serializers
from .models import Carrier, Vehicle, CarrierRequirement, Driver
from sendengo.apps.catalog.serializer import CatalogRequirementSerializer, CatalogSerializer


class CarrierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carrier 
        exclude = ()


class CarrierRequirementSerializer(serializers.ModelSerializer):

    requirement = CatalogRequirementSerializer( read_only=True, )
    category = CatalogSerializer( read_only=True, )
    
    class Meta:
        model = CarrierRequirement 
        exclude = ()
