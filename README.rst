Sendengo
========
by @osharim 


Install
--------

Build docker Image

    $ docker-compose -f local.yml build

Run recent docker instance with the following command and wait.

    $ docker-compose -f local.yml up


Create a superuser attaching this command to our running instance 

    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

Now open the current port on your browser (must be http://0.0.0.0:8000/) and will appear a loggin session 

.. image:: ./docs/admin.png

.. image:: ./docs/admin_view.png

Settings
--------

Moved to config/settings 

Basic Commands
--------------


Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ docker-compose -f local.yml run django coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ docker-compose -f local.yml run django pytest
  

Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

Need more time to explain how to upload this project to Heroku


Docker
^^^^^^

Need more time to explain how this docker recipe works 



API Doc
----------
.. image:: ./docs/api_view.png


Catalogos
^^^^^^

Todos los requerimientos de la plataforma se han consentrado en un listado de catalogos, este catalogo tiene como finalidad
el organizar todos los requerimientos a través de categorias.

Un Catalogo tiene categorias y todos los requerimientos estan relacionados a una categoria.

Obtener todos los catálogos
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  GET /api/v1/catalog/

  HTTP 200 OK
  Allow: GET, POST, HEAD, OPTIONS
  Content-Type: application/json
  Vary: Accept

  [
      {
          "id": 3,
          "created": "2019-05-09T03:19:18.867203Z",
          "name": "Conductor"
      },
      {
          "id": 2,
          "created": "2019-05-09T03:10:43.965946Z",
          "name": "Vehiculo"
      },
      {
          "id": 1,
          "created": "2019-05-09T02:59:13.760607Z",
          "name": "Documentación de transportista"
      }
  ]


Obtener la instancia de un solo catalogo 
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  GET /api/v1/catalog/1/

  HTTP 200 OK
  Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
  Content-Type: application/json
  Vary: Accept

  {
      "id": 1,
      "created": "2019-05-09T02:59:13.760607Z",
      "name": "Documentación de transportista"
  }


Obtener la todos los requerimientos organizados en un catalogo
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  GET /api/v1/catalog/1/requirements/

  HTTP 200 OK
  Allow: GET, POST, HEAD, OPTIONS
  Content-Type: application/json
  Vary: Accept

  [
      {
          "id": 10,
          "created": "2019-05-09T03:22:20.878837Z",
          "name": "Comprobante de domicilio del representante legal",
          "category": 1
      },
      {
          "id": 2,
          "created": "2019-05-09T03:02:53.885238Z",
          "name": "Acta constitutiva",
          "category": 1
      },
      {
          "id": 1,
          "created": "2019-05-09T03:02:45.816558Z",
          "name": "RFC",
          "category": 1
      }
  ]

Shipper(Embarcadero)
^^^^^^

Obtener todos los embarcaderos
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  GET /api/v1/shipper/

  HTTP 200 OK
  Allow: GET, POST, HEAD, OPTIONS
  Content-Type: application/json
  Vary: Accept

  [
      {
          "id": 1,
          "created": "2019-05-09T03:49:49.886842Z",
          "company_name": "Omar Shipper Company",
          "address": "av adolfo lopez mateos",
          "phone": "5519300630",
          "email": "omar.sh.bentel@gmail.com",
          "num_requirements": 4
      },
      {
          "id": 2,
          "created": "2019-05-09T03:50:41.487076Z",
          "company_name": "Amairani Shipper Company",
          "address": "Lago chiem 104 Reforma pencil",
          "phone": "5519300629",
          "email": "amairani@gmail.com",
          "num_requirements": 2
      }
  ]


Obtener el detalle de un embarcadero 
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  GET /api/v1/shipper/1/

  HTTP 200 OK
  Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
  Content-Type: application/json
  Vary: Accept

  {
      "id": 1,
      "created": "2019-05-09T03:49:49.886842Z",
      "company_name": "Omar Shipper Company",
      "address": "av adolfo lopez mateos",
      "phone": "5519300630",
      "email": "omar.sh.bentel@gmail.com",
      "num_requirements": 4 # Ha guardado 4 requerimientos este embarcadero; Más adelante se explica su funcionamiento (en el código)
  }

Obtener los requerimientos de un embarcadero determinado a traves de su ID 
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  GET /api/v1/shipper/1/requirements/

  HTTP 200 OK
  Allow: GET, POST, HEAD, OPTIONS
  Content-Type: application/json
  Vary: Accept

  [
      {
          "id": 23,
          "requirement": {
              "id": 1,
              "created": "2019-05-09T03:02:45.816558Z",
              "name": "RFC",
              "category": 1
          },
          "category": {
              "id": 1,
              "created": "2019-05-09T02:59:13.760607Z",
              "name": "Documentación de transportista"
          },
          "created": "2019-05-09T18:34:10.632731Z",
          "shipper": 2
      },
      {
          "id": 27,
          "requirement": {
              "id": 1,
              "created": "2019-05-09T03:02:45.816558Z",
              "name": "RFC",
              "category": 1
          },
          "category": {
              "id": 1,
              "created": "2019-05-09T02:59:13.760607Z",
              "name": "Documentación de transportista"
          },
          "created": "2019-05-09T18:37:44.015967Z",
          "shipper": 1
      },
      {
          "id": 28,
          "requirement": {
              "id": 10,
              "created": "2019-05-09T03:22:20.878837Z",
              "name": "Comprobante de domicilio del representante legal",
              "category": 1
          },
          "category": {
              "id": 1,
              "created": "2019-05-09T02:59:13.760607Z",
              "name": "Documentación de transportista"
          },
          "created": "2019-05-09T18:42:38.557929Z",
          "shipper": 2
      }
  ]

Carrier(Transportista)
^^^^^

Obtener el listado de todos los transportistas 
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  GET /api/v1/carrier/

  HTTP 200 OK
  Allow: GET, POST, HEAD, OPTIONS
  Content-Type: application/json
  Vary: Accept

  [
      {
          "id": 1,
          "created": "2019-05-09T06:12:50.751804Z",
          "status": "VALIDATED",
          "company_name": "Omar Transportista",
          "owner_name": "Omar",
          "owner_surname": "Sharim",
          "address": "av adolfo lopez mateos",
          "phone": "5519300630",
          "email": "omar@bentel.mx"
      }
  ]


Obtener el detalle de un transportista 
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  GET /api/v1/carrier/1/

  HTTP 200 OK
  Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
  Content-Type: application/json
  Vary: Accept

  {
      "id": 1,
      "created": "2019-05-09T06:12:50.751804Z",
      "status": "VALIDATED",
      "company_name": "Omar Transportista",
      "owner_name": "Omar",
      "owner_surname": "Sharim",
      "address": "av adolfo lopez mateos",
      "phone": "5519300630",
      "email": "omar@bentel.mx"
  }

Obtener los requerimientos ingresados por el transportista
~~~~~~~~~~~~~~~~~~~~~~~~~~
- podrian tambien entenderse como "requerimientos que son cumplidos por el transportista y son requeridos por el embarcador"

::

  GET /api/v1/carrier/1/requirements/
  HTTP 200 OK
  Allow: GET, POST, HEAD, OPTIONS
  Content-Type: application/json
  Vary: Accept

  [
      {
          "id": 2,
          "requirement": {
              "id": 7,
              "created": "2019-05-09T03:19:37.403924Z",
              "name": "Chaleco reflejante",
              "category": 3
          },
          "category": {
              "id": 3,
              "created": "2019-05-09T03:19:18.867203Z",
              "name": "Conductor"
          },
          "created": "2019-05-09T14:01:28.418765Z",
          "carrier": 1
      },
      {
          "id": 4,
          "requirement": {
              "id": 4,
              "created": "2019-05-09T03:18:55.294592Z",
              "name": "GPS",
              "category": 2
          },
          "category": {
              "id": 2,
              "created": "2019-05-09T03:10:43.965946Z",
              "name": "Vehiculo"
          },
          "created": "2019-05-09T15:29:02.625177Z",
          "carrier": 1
      },
      {
          "id": 5,
          "requirement": {
              "id": 3,
              "created": "2019-05-09T03:18:47.031084Z",
              "name": "Póliza de seguro",
              "category": 2
          },
          "category": {
              "id": 2,
              "created": "2019-05-09T03:10:43.965946Z",
              "name": "Vehiculo"
          },
          "created": "2019-05-09T15:55:01.682442Z",
          "carrier": 1
      },
      {
          "id": 10,
          "requirement": {
              "id": 6,
              "created": "2019-05-09T03:19:31.200341Z",
              "name": "Casco de seguridad",
              "category": 3
          },
          "category": {
              "id": 3,
              "created": "2019-05-09T03:19:18.867203Z",
              "name": "Conductor"
          },
          "created": "2019-05-09T17:13:56.792923Z",
          "carrier": 1
      },
      {
          "id": 12,
          "requirement": {
              "id": 8,
              "created": "2019-05-09T03:19:43.185860Z",
              "name": "Certificación de oeprador R-Control",
              "category": 3
          },
          "category": {
              "id": 3,
              "created": "2019-05-09T03:19:18.867203Z",
              "name": "Conductor"
          },
          "created": "2019-05-09T17:20:57.346037Z",
          "carrier": 1
      },
      {
          "id": 19,
          "requirement": {
              "id": 8,
              "created": "2019-05-09T03:19:43.185860Z",
              "name": "Certificación de oeprador R-Control",
              "category": 3
          },
          "category": {
              "id": 3,
              "created": "2019-05-09T03:19:18.867203Z",
              "name": "Conductor"
          },
          "created": "2019-05-09T19:45:53.706467Z",
          "carrier": 1
      },
      {
          "id": 20,
          "requirement": {
              "id": 1,
              "created": "2019-05-09T03:02:45.816558Z",
              "name": "RFC",
              "category": 1
          },
          "category": {
              "id": 1,
              "created": "2019-05-09T02:59:13.760607Z",
              "name": "Documentación de transportista"
          },
          "created": "2019-05-09T19:46:13.506806Z",
          "carrier": 1
      }
  ]


Ver todos los embarcaderos a los cuales puede hacer uso este transportista
~~~~~~~~~~~~~~~~~~~~~~~~~~

Esta mostrando que el embarcador "Omar Shipper" es el unico con el cual puede transportar nuestro transportista
ya que esta cumpliendo con todos los requerimientos que solicita el Shipper(Embarcadero)

::

  GET /api/v1/carrier/1/compliance/

  HTTP 200 OK
  Allow: GET, POST, HEAD, OPTIONS
  Content-Type: application/json
  Vary: Accept

  [
      {
          "id": 1,
          "created": "2019-05-09T03:49:49.886842Z",
          "company_name": "Omar Shipper Company",
          "address": "av adolfo lopez mateos",
          "phone": "5519300630",
          "email": "omar.sh.bentel@gmail.com",
          "num_requirements": 4
      }
  ]


¿Cómo funciona?
^^^^


Partiendo de un sistema de catalogos y organización de requerimientos a través de categorias, resulta generar mayor versatilidad
para el manejo de información ya se tanto <Shipper> como <Carrier> comparten los mismos <Catalogos Requerimientos>.

El siguiente reto es encontrar un algoritmo que encuentre los modelos en <Shipper> que cumplan exactamente con los datos del modelo <Carrier> 

Explicación copiada directamente del código en `sendengo/utils/shippers_in_compliance.py`

1.- Match Carrier requirements with shipper requirements, our output will be only the coincidences between each model
2.- Count these coincidences. It means that Carrier is in complience with the same objects that shipper needs 
3.- Compare these match coincidences now called "in_compliance" with "num_requirements" from every Shipper model

Code to find shippers 
^^^^

::

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

- The following structure means that this Carrier only has 3 out of 4 requirements

::

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

- The following example is a perfect Match, a Carrier has 4 out of 4 shipper requirements =)

::

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
^^^^

::

  > carrier = Carrier.objects.all()[0] # First user randomly
  > carrier_requirements = list(carrier.carrierrequirement_set.all().values_list('requirement_id', flat=True))
  > Shipper.objects.prefetch_related('shipperrequirement_set')[1]._prefetched_objects_cache['shipperrequirement'].filter(~Q(requirement_id__in=carrier_requirements)) 

  > <QuerySet [<ShipperRequirement: Documentación de transportista, Comprobante de domicilio del representante legal>]>

  This response means that this carrier need this document to be in compliance 


