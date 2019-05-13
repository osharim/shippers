import pytest
from django.urls import reverse  # https://docs.djangoproject.com/en/2.1/ref/urlresolvers/#reverse
from rest_framework import status
from django.test import RequestFactory
from django.conf import settings
from sendengo.apps.users.tests.factories import UserFactory
from .factories import CarrierFactory


pytestmark = pytest.mark.django_db


class TestCarrierViews:

   def test_carrier_permission_forbidden(self, apiclient):
       response = apiclient.get(reverse('carrier-list'),)
       assert response.status_code == status.HTTP_403_FORBIDDEN

   def test_carrier_list(self, apiclient, user: settings.AUTH_USER_MODEL):

       max_carriers = 10

       password = 'sendengo'

       # Create <max_carriers> Carriers
       carrier = CarrierFactory.create_batch(max_carriers)

       # Authenticate user
       proto_user = UserFactory(password=password)
       apiclient.login(username=proto_user.username, password=password)

       # Make our API call
       response = apiclient.get(reverse('carrier-list'),)

       # We create <max_carriers> and our API must return the save max_carriers numbers
       assert len(response.data) == max_carriers
