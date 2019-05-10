from django.urls import reverse  # https://docs.djangoproject.com/en/2.1/ref/urlresolvers/#reverse
from rest_framework.test import APITestCase
from rest_framework import status


class CarrierTest(APITestCase):

   def test_carrier_permission_forbidden(self):
       response = self.client.get(reverse('carrier-list'),)
       self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
