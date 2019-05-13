from sendengo.apps.shippers.models import Shipper, ShipperRequirement
from factory import DjangoModelFactory, Faker, post_generation, SubFactory
from sendengo.apps.catalog.tests.factories import CatalogRequirementFactory


Faker.override_default_locale('es_ES')


class ShipperFactory(DjangoModelFactory):

    company_name = Faker("company", locale='es_MX')
    address = Faker("address")
    phone = Faker("random_number")
    email = Faker("email")
    num_requirements = 0

    class Meta:
        model = Shipper


class ShipperRequirementFactory(DjangoModelFactory):

    shipper = SubFactory(ShipperFactory)

    requirement = SubFactory(CatalogRequirementFactory)
    # category is assigned automiticly <shipper.models.py save method>

    class Meta:
        model = ShipperRequirement


class ShipperWithRequirementsFactory(ShipperFactory):
    """
    Create a shipper with N <Instance Requirements>
    """

    @post_generation
    def requirements(obj, create, extracted, **kwargs):

        if not create:
            return

        if extracted:
            for requirement in extracted:
                # añadir este requerimiento al carrier
                ShipperRequirementFactory(shipper=obj, requirement=requirement)
