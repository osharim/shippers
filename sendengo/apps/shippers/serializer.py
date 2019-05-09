# encoding: utf-8
from rest_framework import serializers
from .models import Shipper, ShipperRequirement
from sendengo.apps.catalog.serializer import CatalogRequirementSerializer, CatalogSerializer


class ShipperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipper 
        exclude = ()


class ShipperRequirementSerializer(serializers.ModelSerializer):

    requirement = CatalogRequirementSerializer( read_only=True, )
    category = CatalogSerializer( read_only=True, )
    
    class Meta:
        model = ShipperRequirement 
        exclude = ()
