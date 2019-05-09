# encoding: utf-8
from rest_framework import serializers
from .models import CatalogCategory, CatalogRequirement


class CatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = CatalogCategory 
        exclude = ()


class CatalogRequirementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CatalogRequirement 
        exclude = ()
