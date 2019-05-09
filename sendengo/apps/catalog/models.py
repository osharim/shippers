# enconding: utf-8
from django.db.models import CharField, ForeignKey, PROTECT 
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from sendengo.utils.model import ModelDateTimeField


class CatalogCategory(ModelDateTimeField):
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

    # Category types eg. Carrier, Driver, Vehicle and even new categories
    # that we dont know they exists.
    name = CharField(_("Name for this category e.g carrier documents, driver, vehicle"),
                     blank=True, max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class CatalogRequirement(ModelDateTimeField):

    # Relation to a category
    category = ForeignKey(CatalogCategory, verbose_name=_('Category type'), on_delete=PROTECT)

    # Name requirement
    name = CharField(_("Name requirement"), blank=True, max_length=128)

    def __str__(self):
        return F"{self.category}, {self.name}"

    class Meta:
        verbose_name = "Requerimiento"
        verbose_name_plural = "Requerimientos"
