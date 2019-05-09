# enconding: uf-8
# @osharim
from django.db.models import F, Count
from sendengo.apps.shippers.models import Shipper

"""
# How it works

# 1.- Match Carrier requirements with shipper requirements, our output will be only the coincidences between each model
# 2.- We Count these coincicendes. It means that Carrier is in complience with the same objects that shipper requirements need
# 3.- Compare these match coincidences now called "in_compliance" with "num_requirements" from every Shipper model

# Also check Carry, vehicle and driver must be approved

# Return <Shipper Models> with the following structure.



- The following structure means that this Carrier only has 3 out of 4 requirements

{
    '_state': <django.db.models.base.ModelState at 0x7f738a4db8d0>,
    'id': 1,
    'created': datetime.datetime(2019, 5, 9, 3, 49, 49, 886842, tzinfo=<UTC>),
    'company_name': 'Omar Shipper Company',
    'address': 'av adolfo lopez mateos',
    'phone': '5519300630',
    'email': 'omar.sh.bentel@gmail.com',
    'num_requirements': 4,
    'in_compliance': 3
 }

- This is a perfect Match, a Carrier has 4 out of 4 shipper requirements =)

{
 '_state': <django.db.models.base.ModelState at 0x7f738a4db8d0>,
 'id': 1,
 'created': datetime.datetime(2019, 5, 9, 3, 49, 49, 886842, tzinfo=<UTC>),
 'company_name': 'Omar Shipper Company',
 'address': 'av adolfo lopez mateos',
 'phone': '5519300630',
 'email': 'omar.sh.bentel@gmail.com',
 'num_requirements': 4,
 'in_compliance': 4
}

# Extra: If you need to know what requirement is needed please, exec the following Query

> carrier = Carrier.objects.all()[0] # First user randomly
> carrier_requirements = list(carrier.carrierrequirement_set.all().values_list('requirement_id', flat=True))
> Shipper.objects.prefetch_related('shipperrequirement_set')[1]._prefetched_objects_cache['shipperrequirement'].filter(~Q(requirement_id__in=carrier_requirements)) 

> <QuerySet [<ShipperRequirement: Documentación de transportista, Comprobante de domicilio del representante legal>]>

Response means that this carrier need this document to be in compliance 

"""


def get_shippers_list(carrier_instance):

    shippers = []

    # copied from google docs

    # La línea de transporte debe contar con al menos un vehículo y debe estar aprobad
    exists_one_driver_approved = carrier_instance.vehicle_set.filter(status='VALIDATED').exists()

    # La línea de transporte debe contar con al menos un operador y debe estar aprobado
    exists_one_vehicle_approved = carrier_instance.driver_set.filter(status='VALIDATED').exists()

    # La línea de transporte y al menos un vehículo y un operador que estén aprobados deben cumplir
    # con los requerimientos del embarcador.
    if exists_one_vehicle_approved and exists_one_driver_approved:

        carrier = carrier_instance

        # Carrier requirements
        carrier_requirements = list(carrier.carrierrequirement_set.all().values_list('requirement_id', flat=True))

        shippers = Shipper.objects.filter(shipperrequirement__requirement__in=carrier_requirements)\
            .annotate(in_compliance=Count('shipperrequirement'))\
            .filter(num_requirements=F('in_compliance'))

    return shippers
