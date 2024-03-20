========================
django-import-export-xml
========================

:Version: 0.2.0
:Source: https://github.com/maykinmedia/django-import-export-xml
:PythonVersion: 3.9

|build-status| |code-quality| |black| |coverage|

|python-versions| |django-versions| |pypi-version|

An XML *export* format for django-import-export

.. contents::

.. section-numbering::

Installation
============

Requirements
------------

* Python 3.9 or above
* Django 3.2 or newer


Install
-------

.. code-block:: bash

    pip install django-import-export-xml


Usage
=====

Use it like any of the built-in formats: https://django-import-export.readthedocs.io/en/stable/installation.html#import-export-formats

Local development
=================

To install and develop the library locally, use:

.. code-block:: bash

    pip install -e .[tests,coverage,release]

When running management commands via ``django-admin``, make sure to add the root
directory to the python path (or use ``python -m django <command>``):

.. code-block:: bash

    export PYTHONPATH=. DJANGO_SETTINGS_MODULE=testapp.settings
    django-admin check
    # or other commands like:
    # django-admin makemessages -l nl


.. |build-status| image:: https://github.com/maykinmedia/django-import-export-xml/workflows/Run%20CI/badge.svg
    :alt: Build status
    :target: https://github.com/maykinmedia/django-import-export-xml/actions?query=workflow%3A%22Run+CI%22

.. |code-quality| image:: https://github.com/maykinmedia/django-import-export-xml/workflows/Code%20quality%20checks/badge.svg
     :alt: Code quality checks
     :target: https://github.com/maykinmedia/django-import-export-xml/actions?query=workflow%3A%22Code+quality+checks%22

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. |coverage| image:: https://codecov.io/gh/maykinmedia/django_import_export_xml/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/maykinmedia/django_import_export_xml
    :alt: Coverage status

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/django_import_export_xml.svg

.. |django-versions| image:: https://img.shields.io/pypi/djversions/django_import_export_xml.svg

.. |pypi-version| image:: https://img.shields.io/pypi/v/django_import_export_xml.svg
    :target: https://pypi.org/project/django_import_export_xml/
