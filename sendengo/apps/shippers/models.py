# enconding: utf-8
from django.db.models import CharField , IntegerField, ForeignKey, PROTECT, Count, Q, F
from django.utils.translation import ugettext_lazy as _
from sendengo.utils.model import ModelDateTimeField
from sendengo.apps.catalog.models import CatalogCategory, CatalogRequirement
from django.utils.safestring import mark_safe


class Shipper(ModelDateTimeField):

    # Nombre de la empresa embarcadora
    company_name = CharField(_("Company name"), blank=True, max_length=256)

    # Domicilio de la empresa embarcadora
    address = CharField(_("Address"), blank=True, max_length=512)

    # Teléfono de la empresa embarcadora
    phone = CharField(_("Phone"), blank=True, max_length=10)

    # Correo electrónico de la empresa embarcadora
    email = CharField(_("Email"), blank=True, max_length=254)

    # Register to increment o decrement the number of requirements to prevent the use of COUNT QUERIES
    num_requirements = IntegerField(_('Num requirements'), default=0)

    def view_requirements(self):
        status_verbose_service = _("View requirements")
        count_requirements = self.num_requirements

        return mark_safe(F'<a href="/shippers/shipperrequirement/?shipper__id__exact={self.id}" class="button">{status_verbose_service} ({count_requirements})</a>')
    view_requirements.short_description = _("View requirements")

    def __str__(self):
        return self.company_name

    def delete(self, *args, **kwargs):
        print("DELETING")
        super(Shipper, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = "Embarcador"
        verbose_name_plural = "Embarcadores"


class ShipperRequirement(ModelDateTimeField):
    """
    This model aims to organize an entire requirement list. eg.

    Shipper Requirements:
        -Para Carriers (CatalogCategory)
            * Certificación de línea R-Control (CatalogRequirement)
            * Permiso ante la SCT
            * Acta constitutiva
            * RFC
            * Comprobante de domicilio del representante legal
        - Para Operadores (Drivers) (CatalogCategory)
            * Casco de seguridad (CatalogRequirement)
            * Chaleco reflejante
            * Certificación de oeprador R-Control
            * Identificación oficial
            * COmprobante de domicilio
        - Para Unidades (Vehicles) (CatalogCategory)
            * Póliza de seguro (CatalogRequirement)
            * GPS
            * Antijammer
            * Paro de motor
            * Tarjeta de circulación
    """

    shipper = ForeignKey(Shipper, verbose_name=_('Shipper'), on_delete=PROTECT)

    category = ForeignKey(CatalogCategory, verbose_name=_('Category Requirement'),
                          blank=True, null=True, on_delete=PROTECT)

    requirement = ForeignKey(CatalogRequirement, verbose_name=_('Requirement'), on_delete=PROTECT)

    def save(self, *args, **kwargs):

        if not self.category:
            self.category = self.requirement.category

        super(ShipperRequirement, self).save(*args, **kwargs)

    def __str__(self):
        return F"{self.requirement}"

    class Meta:
        verbose_name = "Requerimiento"
        verbose_name_plural = "Requerimientos"

