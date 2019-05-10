from sendengo.apps.carrier.models import Carrier
from factory import DjangoModelFactory, Faker, post_generation


class CarrierFactory(DjangoModelFactory):

    username = Faker("user_name")
    email = Faker("email")
    name = Faker("name")

    class Meta:
        model = Carrier 
