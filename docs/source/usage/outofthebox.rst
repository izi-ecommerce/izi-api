============================
Use IZI API out-of-the-box
============================

To use the iziapi application in an izi ecommerce site without overriding or customizing the default views and serializers just follow these steps:

1. Install it (see :ref:`izi-api-installation`)
2. Add ``rest_framework`` and ``iziapi`` to your INSTALLED_APPS section in ``settings.py``
3. Add the application's urls to your own app's `url.py`:

.. code-block:: python

    from iziapi.app import application as api
    urlpatterns = [
        # ... all the things you allready got
        url(r'^api/', api.urls),
    ]

.. _mixed-usage-label:

Middleware and mixed usage
--------------------------

There are some middleware classes shipped with IZI API which can be useful for your project. For example, we have seen in practice that it can be useful to mix plain IZI and the API (fill your basket with the API and use plain IZI views for checkout).

See the :doc:`/usage/middleware` section for more information.


