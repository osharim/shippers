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


Settings
--------

Moved to config/settings 

Basic Commands
--------------


Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest


Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

Need more time to explain how to upload this project to Heroku


Docker
^^^^^^

Need more time to explain how this docker recipe works 



API Doc.
^^^^^^

Need more time to explain how this docker recipe works 




