# enconding: utf-8
from rest_framework import viewsets
from .serializer import ShipperSerializer, ShipperRequirementSerializer 
from .models import Shipper, ShipperRequirement 
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied


class ShipperViewSet(viewsets.ModelViewSet):

    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer

    def list(self, request):
        if self.request.user.is_authenticated:
            serializer = self.serializer_class(self.queryset, many=True)
            return Response(serializer.data)
        else:
            raise PermissionDenied()


class ShipperRequirementViewSet(viewsets.ModelViewSet):
    
    queryset = ShipperRequirement.objects.all()
    serializer_class = ShipperRequirementSerializer 

    def list(self, request, shipper_pk):
        print(shipper_pk)
        if self.request.user.is_authenticated:
            serializer = self.serializer_class(self.queryset.filter(category=shipper_pk), many=True)
            return Response(serializer.data)
        else:
            raise PermissionDenied()
