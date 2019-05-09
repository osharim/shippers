# enconding: utf-8
# osharim
from django.db.models import CharField, ForeignKey, PROTECT, PositiveSmallIntegerField, DateField
from django.utils.translation import ugettext_lazy as _
from sendengo.utils.model import ModelDateTimeField, StatusRequirementDisplay
from sendengo.utils.shippers_in_complience import get_shippers_list
from sendengo.apps.catalog.models import CatalogCategory, CatalogRequirement
from django.utils.safestring import mark_safe


LICENSE_TYPE = tuple(map(lambda element: (element, element), ["A", "B", "C", "D", "E", "F", ]))

VEHICLES = ["Sin especificar", "Camioneta de 1.5 toneladas", "Camioneta de 3.5 toneladas",
            "Camioneta de 5.5 toneladas", "Rabón con caja seca", "Rabón con caja refrigerada"
            "Torton con caja seca", "Torton con caja refrigerada", "Trailer de 48ft con caja seca",
            "Trailer de 48ft con caja refrigerada", "Trailer de 53ft con caja seca", "Trailer de 53ft con caja refrigerada"]

# I'd rather build an entire module for Vehicles types.
VEHICLE_TYPE = tuple(map(lambda element: (str(element[0]), element[1]), enumerate(VEHICLES)))


class Carrier(ModelDateTimeField, StatusRequirementDisplay):
    """
    Called Transportista
    """

    # Nombre de la línea de transporte
    company_name = CharField(_("Company name"), blank=True, max_length=256)

    # Nombre del dueño de la línea de transporte
    owner_name = CharField(_("Owner name"), blank=True, max_length=256)

    # Apellido del dueño de la línea de transporte
    owner_surname = CharField(_("Owner surname"), blank=True, max_length=256)

    # Domicilio de la línea de transporte
    address = CharField(_("Address"), blank=True, max_length=512)

    # Teléfono de la empresa embarcadora
    phone = CharField(_("Phone"), blank=True, max_length=10)

    # Correo electrónico de la línea de transporte
    email = CharField(_("Email"), blank=True, max_length=254)

    def view_requirements(self):
        status_verbose_service = _("View requirements")
        count_requirements = self.carrierrequirement_set.all().count()

        return mark_safe(F'<a href="/carrier/carrierrequirement/?carrier__id__exact={self.id}" class="button">{status_verbose_service} ({count_requirements})</a>')
    view_requirements.short_description = _("View requirements")

    def get_shippers_in_compliance(self):
        # how the list of the shippers in which the condition of being in compliance is fulfilled
        print(get_shippers_list(self))

    def get_shippers_in_compliance_count(self):
        return len(get_shippers_list(self))
    get_shippers_in_compliance_count.short_description = _('Shippers in compliance')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Transportista"
        verbose_name_plural = "Transportistas"


class Driver(ModelDateTimeField, StatusRequirementDisplay):
    """
    Called Operador
    """

    carrier = ForeignKey(Carrier, verbose_name=_('Carrier'), on_delete=PROTECT, null=True)

    # Nombre del operado
    name = CharField(_("Driver name"), blank=True, max_length=256)

    # Apellido paterno del operador
    surname = CharField(_("Surname"), blank=True, max_length=256)

    # ipo de licencia con la que cuenta el operador
    license_type = CharField(_("Licence type"), choices=LICENSE_TYPE, blank=True, max_length=1)

    # Número de licencia del operador
    license_number = CharField(_("Licence number"), blank=True, max_length=20)

    # Fecha de vencimiento de la licencia del operador
    license_expiration = DateField(_("License exp"), blank=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Operador"
        verbose_name_plural = "Operadores"


class Vehicle(ModelDateTimeField, StatusRequirementDisplay):
    """
    Called Unidades 
    """

    carrier = ForeignKey(Carrier, verbose_name=_('Carrier'), on_delete=PROTECT, null=True)

    # Placas del vehículo
    license_plate = CharField(_("Licence plate"), blank=True, max_length=8)

    # Marca del vehcículo
    make = CharField(_("Brand"), blank=True, max_length=128)

    # Modelo del vehículo
    model_type = CharField(_("Model type"), blank=True, max_length=128)

    # Año del vehículo
    year = PositiveSmallIntegerField(_("Year"), blank=True,)

    type = CharField(_("Type vehicle"), choices=VEHICLE_TYPE,
                     max_length=1,)

    def __str__(self):
        return self.license_plate

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"


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

    carrier = ForeignKey(Carrier, verbose_name=_('Carrier'), on_delete=PROTECT)

    category = ForeignKey(CatalogCategory, verbose_name=_('Category Requirement'),
                          blank=True, null=True, on_delete=PROTECT)

    requirement = ForeignKey(CatalogRequirement, verbose_name=_('Requirement'), on_delete=PROTECT)

    def save(self, *args, **kwargs):

        if not self.category:
            self.category = self.requirement.category

        super(CarrierRequirement, self).save(*args, **kwargs)

    def __str__(self):
        return F"{self.requirement}"

    class Meta:
        verbose_name = "Requerimiento"
        verbose_name_plural = "Requerimientos"
