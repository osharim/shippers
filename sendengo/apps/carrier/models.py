# enconding: utf-8
from django.db.models import CharField, ForeignKey, CASCADE
from django.utils.translation import ugettext_lazy as _
from sendengo.utils.model import ModelDateTimeField
from sendengo.apps.catalog.models import CatalogCategory, CatalogRequirement
from django.utils.safestring import mark_safe
from django.utils.safestring import mark_safe


VALIDATION_PROCESS_STATUS = (
    ("VALIDATION_IN_PROCCESS", _("Validation in proccess")),
    ("VALIDATED", _("Validated")),
    ("SUSPENDED", _("Suspended")),
)

class Carrier(ModelDateTimeField):

    # Nombre de la empresa embarcadora
    company_name = CharField(_("Company name"), blank=True, max_length=256)

    owner_name = CharField(_("Owner name"), blank=True, max_length=256)

    owner_surname = CharField(_("Owner surname"), blank=True, max_length=256)

    # Domicilio de la empresa embarcadora
    address = CharField(_("Address"), blank=True, max_length=512)

    # Teléfono de la empresa embarcadora
    phone = CharField(_("Phone"), blank=True, max_length=10)

    # Correo electrónico de la empresa embarcadora
    email = CharField(_("Email"), blank=True, max_length=254)

    status = CharField(_("Status"), choices=VALIDATION_PROCESS_STATUS, blank=True, max_length=254, default="VALIDATION_IN_PROCCESS")

    def view_requirements(self):
        status_verbose_service = _("View requirements")
        count_requirements = self.carrierrequirement_set.all().count()

        return mark_safe(F'<a href="/carrier/carrierrequirement/?carrier__id__exact={self.id}" class="button">{status_verbose_service} ({count_requirements})</a>')
    view_requirements.short_description = _("View requirements")

    def get_status(self):
        background = '#9e9e9e'
        status = self.get_status_display()    

        if self.status == 'VALIDATION_IN_PROCCESS':
            background = '#e89657'

        if self.status == 'SUSPENDED':
            background = '#9e9e9e'

        if self.status == 'VALIDATED':
            background = '#11ad36'

        return mark_safe(F"<div style='background:{background};' class='status-tag'>{status}</div> ")
    
    get_status.allow_tags = True
    get_status.short_description = 'Status'

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Transportista"
        verbose_name_plural = "Transportistas"


class CarrierRequirement(ModelDateTimeField):
    """
    This model aims to organize an entire requirement list. eg.

    - This model must match with ShipperRequirements -

    Carrier Requirements:
        - Documentacion (CatalogCategory)
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

    carrier = ForeignKey(Carrier, verbose_name=_('Carrier'), on_delete=CASCADE)

    category = ForeignKey(CatalogCategory, verbose_name=_('Category Requirement'),
                          blank=True, null=True, on_delete=CASCADE)

    requirement = ForeignKey(CatalogRequirement, verbose_name=_('Requirement'), on_delete=CASCADE)

    def save(self, *args, **kwargs):

        if not self.category:
            self.category = self.requirement.category

        super(CarrierRequirement, self).save(*args, **kwargs)

    def __str__(self):
        return F"{self.requirement}"

    class Meta:
        verbose_name = "Requerimiento"
        verbose_name_plural = "Requerimientos"
