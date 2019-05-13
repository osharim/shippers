from sendengo.apps.catalog.models import CatalogCategory, CatalogRequirement
from factory import DjangoModelFactory, Faker, post_generation, SubFactory

Faker.override_default_locale('es_ES')


class CatalogFactory(DjangoModelFactory):
    """
    CatalogCategory: This model aims to manage requirements as a catalog through 
    categories eg.

    Let's create a new catalog category called 'Legal complience', and then add
    requirements to this catalog created.

    Model CatalogCategory:

        - Legal Complience

    Model CatalogRequierments <related to  - Legal Complience

        - Permiso ante la SCT
        - Acta constitutiva
        - RFC

    TThis way of organizing information allows us to scale to more catalogs and
    add any type of requirements in an automated way
    """

    name = '' 

    class Meta:
        model = CatalogCategory
        django_get_or_create = ["name"]


class CatalogRequirementFactory(DjangoModelFactory):

    category = SubFactory(CatalogFactory)
    name = '' 

    class Meta:
        model = CatalogRequirement
        django_get_or_create = ["name"]


class CatalogWithRequirementsFactory(CatalogFactory):
    """
    Create a catalog with N Requirements
    """

    @post_generation
    def requirements(obj, create, extracted, **kwargs):
        """
        If requirements is provided, then we create and add requirements to this Catalog
        in a simple line 
        
        """
        if not create:
            # Build, not create related
            return

        if extracted:
            for requirement in extracted:
                CatalogRequirementFactory(name=requirement, category=obj)
