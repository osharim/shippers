# encoding: utf-8
import pytest
from sendengo.apps.carrier.tests.factories import CarrierWithRequirementsFactory, VehicleFactory, DriverFactory
from sendengo.apps.catalog.tests.factories import CatalogRequirementFactory, CatalogFactory
from sendengo.apps.shippers.tests.factories import ShipperWithRequirementsFactory
from sendengo.apps.shippers.models import Shipper

from django.conf import settings

pytestmark = pytest.mark.django_db


class TestCarrier:

    def test_carrier_is_in_full_compliance_with_one_shipper(self):
        """
        Mostrar que el carrier este en cumplimiento por completo con un shipper
        """

        # Crear catalogos de documentacion
        catalog_category = CatalogFactory(name='Requerimientos para transportista')

        catalog_category_permiso_sct = CatalogRequirementFactory(name='Permiso ante la SCT')
        catalog_category_acta_constitutiva = CatalogRequirementFactory(name='Acta constitutiva')
        catalog_category_rfc = CatalogRequirementFactory(name='RFC')

        # Crear requerimientos para vehiculos

        vehicle_category = CatalogFactory(name='Requerimientos para vehiculos')

        vehicle_poliza_seguro = CatalogRequirementFactory(name='Póliza de seguro')
        vehicle_tarjeta_circulacion = CatalogRequirementFactory(name='Tarjeta de circulación')
        vehicle_rfc = CatalogRequirementFactory(name='RFC')

        # Crear requerimientos para operadores

        driver_category = CatalogFactory(name='Requerimientos para operadores')

        driver_chaleco_reflejante = CatalogRequirementFactory(name='Chaleco reflejante')
        driver_operador_control = CatalogRequirementFactory(name='Certificación de oeprador R-Control')
        driver_identificacion_oficial = CatalogRequirementFactory(name='Identificación oficial')

        # Shipper #1
        # agregar requerimientos que solcita el shipper
        shipper_1 = ShipperWithRequirementsFactory(company_name='Omar el shipper', requirements=[
            catalog_category_rfc, vehicle_poliza_seguro,
            vehicle_rfc, driver_chaleco_reflejante,
            driver_operador_control, driver_identificacion_oficial])

        # Shipper #2 - El test va a coincidir con este shipper
        shipper_2 = ShipperWithRequirementsFactory(company_name='Omar el shipper', requirements=[
            catalog_category_rfc,
            vehicle_rfc, driver_chaleco_reflejante,
            driver_operador_control, driver_identificacion_oficial])

        # Shipper #3
        shipper_3 = ShipperWithRequirementsFactory(company_name='Omar el shipper', requirements=[
            catalog_category_rfc,
            vehicle_rfc, vehicle_tarjeta_circulacion,
            driver_operador_control, driver_identificacion_oficial])

        # Shipper #4
        shipper_4 = ShipperWithRequirementsFactory(company_name='Omar el shipper', requirements=[
            catalog_category_rfc,
            vehicle_rfc, vehicle_tarjeta_circulacion,
            driver_operador_control, catalog_category_acta_constitutiva])

        # agregar requerimientos que cumple el carrier
        # Crear un Carrier <Transportista> con los siguientes cumplimientos
        carrier = CarrierWithRequirementsFactory(
            company_name='Mike Transportista', status='VALIDATED', requirements=[
                catalog_category_rfc, vehicle_rfc,
                driver_chaleco_reflejante, driver_operador_control,
                driver_identificacion_oficial])

        # En esta punto necesitamos que tenga un conductor aprobado
        driver = DriverFactory(carrier=carrier, status='VALIDATED')

        # En esta punto necesitamos que tenga un vehiculo aprobado
        vechile = VehicleFactory(carrier=carrier, status='VALIDATED')

        shipper_in_compliance = carrier.get_shippers_in_compliance()

        # El resultado debe arrojar que este carrier <Transportista> cumple con todos los requisitos que solita un shipper
        assert len(shipper_in_compliance) == 1
        # El shipper el cual cumplimos todos los requisitos debe ser el mismo que regresa  "shipper_in_compliance"
        assert shipper_in_compliance[0].id == shipper_2.id
