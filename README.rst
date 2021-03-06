Django PyPi
============

Keep PyPi versions and release dates in your database for easy querying.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-pypi

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/Celc/django-pypi.git#egg=pypi

Add ``pypi`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'pypi',
    )

Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate pypi

You'll need to have ``django-celery`` already setup.

Usage
-----

Use ``./manage.py pypi_refresh`` to fetch pypi, this is going to take a couple
of hours.

Then just start querying the ORM:

.. code-block:: python

    >>> package = Package.objects.filter(name='Django').latest()
    >>> package.version
    '1.5.2'


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-pypi
    $ python setup.py install

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch
