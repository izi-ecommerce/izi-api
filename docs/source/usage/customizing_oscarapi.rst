============================
Customizing Oscar API
============================

By using the `django-rest-framework`_ life has become easy, at least for customizing the Oscar API. Oscar API exists of a collection of views and serializers which can be overriden by following the steps below.

.. note::
    In izi you can `fork an app`_ to easily customize only the things you want to change.

.. _`fork an app`: https://django-izi.readthedocs.io/en/releases-1.1/topics/fork_app.html
.. _`django-rest-framework`: http://www.django-rest-framework.org

Oscar API is using the basics of this so you can see Oscar API as one of the apps you customized just like in Oscar. Each Oscar app (or forked app) has a ``app.py`` which manages the url's to your custom views. 

In Oscar API the entry point of this is ``iziapi.app:RESTApiApplication``.

In your own app, you can extend this class, and override some of the urls to
direct them to your own views. You can subclass any of the views in iziapi,
or just write your own from scratch.

So, to modify some of the functionality in iziapi, do the following:

1. In your project, create a new django app with ``manage.py startapp mycustomapi``.
2. In your app, create a file named ``app.py`` and in there extend ``iziapi.app:RESTApiApplication``, like the following example:

.. code-block:: python

    from iziapi.app import RESTApiApplication

        class MyRESTApiApplication(RESTApiApplication):

            def get_urls(self):
                urls = super(MyRESTApiApplication, self).get_urls()
                return urls

    application = MyRESTApiApplication()

3. Make sure you use this application instead of the app shipped with iziapi in your `urls.py`:

.. literalinclude:: ../../../demosite/mycustomapi/urls.py

.. note::
    If you think that this is not changing anything (yet) then this is correct, see below.

4. Include your own app in INSTALLED_APPS instead of ``izi-api`` (and add ``izi-api`` to your app's dependencies) and see if this works.
5. Add a serializer and a view for the parts you want to change. In this example, we will override the ``ProductList`` view so we can specify a different ``ProductLinkSerializer`` which includes images and the price as well:

`serializers.py`

.. literalinclude:: ../../../demosite/mycustomapi/serializers.py

`views.py`

.. literalinclude:: ../../../demosite/mycustomapi/views.py

6. Adjust your ``app.py`` with your custom urls:

.. literalinclude:: ../../../demosite/mycustomapi/app.py

7. Your ``urls.py`` still looks the same, as we have configured the override in ``app.py``:

.. literalinclude:: ../../../demosite/mycustomapi/urls.py


The complete example above is available in the `Github repository of Oscar API`_ if you want to try it out.

.. _`Github repository of Oscar API`: https://github.com/izi-ecommerce/izi-api/tree/master/demosite/
 



