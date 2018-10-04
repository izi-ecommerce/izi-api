================
Django IZI API
================

This package provides a RESTful API for `izi-core`_.

.. _`izi-core`: https://github.com/izi-ecommerce/izi-core

.. image:: https://travis-ci.org/izi-ecommerce/izi-api.svg?branch=master
    :target: https://travis-ci.org/izi-ecommerce/izi-api

.. image:: http://codecov.io/github/izi-core/izi-api/coverage.svg?branch=master 
    :alt: Coverage
    :target: http://codecov.io/github/izi-core/izi-api?branch=master

.. image:: https://readthedocs.org/projects/izi-api/badge/
   :alt: Documentation Status
   :target: https://izi-api.readthedocs.io/

.. image:: https://badge.fury.io/py/izi-api.svg
   :alt: Latest PyPi release
   :target: https://pypi.python.org/pypi/izi-api

Usage
=====

To use the IZI API application in an IZI E-commerce site, follow these
steps:

1. Install the `izi-api` package (``pip install izi-api``).
2. Add iziapi to INSTALLED_APPS.
3. Add the application's urls to your urlconf::
    
    from iziapi.app import application as api

    urlpatterns = (
        # all the things you already have
        url(r'^api/', api.urls),
    )

See the Documentation_ for more information and the Changelog_ for release notes.

.. _Documentation: https://izi-api.readthedocs.io
.. _Changelog: https://izi-api.readthedocs.io/en/latest/changelog.html

