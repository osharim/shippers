from sendengo.apps.carrier.models import Carrier, CarrierRequirement, Driver, Vehicle
from factory import DjangoModelFactory, Faker, post_generation, SubFactory
from sendengo.apps.catalog.tests.factories import CatalogRequirementFactory

Faker.override_default_locale('es_ES')


class CarrierFactory(DjangoModelFactory):

    company_name = Faker("company", locale='es_MX')
    email = Faker("email")
    owner_name = Faker("name")
    owner_surname = Faker("last_name")
    address = Faker("address")
    phone = Faker("random_number")

    status = ''

    class Meta:
        model = Carrier


class DriverFactory(DjangoModelFactory):
    
    carrier = SubFactory(CarrierFactory)
    name = Faker("name")
    surname = Faker("last_name")
    license_expiration = Faker("date")
    license_type = "A" 
    status = ''

    class Meta:
        model = Driver 

class VehicleFactory(DjangoModelFactory):
    
    carrier = SubFactory(CarrierFactory)
    status = ''
    year = 2019
    make = 'NISAN'

    class Meta:
        model = Vehicle



class CarrierRequirementFactory(DjangoModelFactory):

    carrier = SubFactory(CarrierFactory)

    requirement = SubFactory(CatalogRequirementFactory)
    # category is assigned automaticly in <carrier.models.py save method>

    class Meta:
        model = CarrierRequirement 


class CarrierWithRequirementsFactory(CarrierFactory):
    """
    Create a carrier with N <Instance Requirements>
    """
    @post_generation
    def requirements(obj, create, extracted, **kwargs):

        if not create:
            return

        if extracted:
            for requirement in extracted:
                # añadir este requerimiento al carrier 
                CarrierRequirementFactory(carrier=obj, requirement=requirement)
