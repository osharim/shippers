# enconding: utf-8
from rest_framework import viewsets
from .serializer import CarrierRequirementSerializer, CarrierSerializer 
from .models import Carrier, Vehicle, CarrierRequirement, Driver 
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from sendengo.apps.shippers.models import Shipper
from sendengo.apps.shippers.serializer import ShipperSerializer


class CarrierViewSet(viewsets.ModelViewSet):

    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer

    def list(self, request):
        if self.request.user.is_authenticated:
            serializer = self.serializer_class(self.queryset, many=True)
            return Response(serializer.data)
        else:
            raise PermissionDenied()


class CarrierRequirementViewSet(viewsets.ModelViewSet):
    
    queryset = CarrierRequirement.objects.all()
    serializer_class = CarrierRequirementSerializer 

    def list(self, request, carrier_pk):
        if self.request.user.is_authenticated:
            serializer = self.serializer_class(self.queryset.filter(carrier=carrier_pk), many=True)
            return Response(serializer.data)
        else:
            raise PermissionDenied()


class CarrierViewShippersInComplianceViewSet(viewsets.ModelViewSet):
    
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer 

    def list(self, request, carrier_pk):

        # Get list of the shippers in which the condition of being in compliance is fulfilled
        get_shippers_list = Carrier.objects.get(pk=carrier_pk).get_shippers_in_compliance()

        if self.request.user.is_authenticated:
            serializer = self.serializer_class(get_shippers_list, many=True)
            return Response(serializer.data)
        else:
            raise PermissionDenied()
