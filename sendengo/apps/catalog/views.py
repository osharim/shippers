# enconding: utf-8
from rest_framework import viewsets
from .serializer import CatalogSerializer, CatalogRequirementSerializer
from .models import CatalogCategory, CatalogRequirement
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import MultiPartParser, FormParser,  JSONParser


class CatalogViewSet(viewsets.ModelViewSet):

    queryset = CatalogCategory.objects.all()
    serializer_class = CatalogSerializer

    def list(self, request):
        if self.request.user.is_authenticated:
            serializer = self.serializer_class(self.queryset, many=True)
            return Response(serializer.data)
        else:
            raise PermissionDenied()


class CatalogRequirementViewSet(viewsets.ModelViewSet):
    
    queryset = CatalogRequirement.objects.all()
    serializer_class = CatalogRequirementSerializer 

    def list(self, request, catalog_pk):
        if self.request.user.is_authenticated:
            serializer = self.serializer_class(self.queryset.filter(category=catalog_pk), many=True)
            return Response(serializer.data)
        else:
            raise PermissionDenied()
