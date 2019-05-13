import pytest
from django.conf import settings
from django.test import RequestFactory

from sendengo.apps.users.tests.factories import UserFactory
from rest_framework.test import APIClient


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> settings.AUTH_USER_MODEL:
    return UserFactory()


@pytest.fixture
def apiclient() -> APIClient:
    return APIClient()


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()
