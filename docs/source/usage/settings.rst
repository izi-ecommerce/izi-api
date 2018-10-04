==================
IZI API Settings
==================

.. _main-settings-label:

Main settings
=============

``IZIAPI_BLOCK_ADMIN_API_ACCESS``
-----------------------------------
Default: ``True``

Useful in production websites wehere you want to make sure that admin users 
can't access the API (they can read/write anything which is exposed by the API).


Serializer settings
===================

Most of the model serializers in IZI API have a default set of fields to use in the REST API. If you customized the IZI models you can reflect this customization by adding settings for this serializer.

For example, the ``RecommendedProduct`` serializer is defined as following:

.. code-block:: python

    class RecommmendedProductSerializer(IZIModelSerializer):
        url = serializers.HyperlinkedIdentityField(view_name='product-detail')

        class Meta:
            model = Product
            fields = overridable(
                'IZIAPI_RECOMMENDED_PRODUCT_FIELDS',
                default=('url',)
            )

When you add the following section to your ``settings.py`` you will add the 'title' field as well:

.. code-block:: python

    IZIAPI_RECOMMENDED_PRODUCT_FIELDS = ('url', 'title')


The following serializers have customizable field settings:

Basket serializers
------------------

.. autoclass:: iziapi.serializers.basket.BasketSerializer
.. autoclass:: iziapi.serializers.basket.BasketLineSerializer
.. autoclass:: iziapi.serializers.basket.VoucherSerializer

Checkout serializers
--------------------

.. autoclass:: iziapi.serializers.checkout.OrderSerializer
.. autoclass:: iziapi.serializers.checkout.OrderLineSerializer
.. autoclass:: iziapi.serializers.checkout.UserAddressSerializer

Login serializers
-----------------

.. autoclass:: iziapi.serializers.login.UserSerializer

Product serializers
-------------------

.. autoclass:: iziapi.serializers.product.OptionSerializer
.. autoclass:: iziapi.serializers.product.ProductLinkSerializer
.. autoclass:: iziapi.serializers.product.RecommmendedProductSerializer
.. autoclass:: iziapi.serializers.product.ChildProductSerializer
.. autoclass:: iziapi.serializers.product.ProductSerializer
.. autoclass:: iziapi.serializers.product.ProductAttributeSerializer
.. autoclass:: iziapi.serializers.product.ProductAttributeValueSerializer

