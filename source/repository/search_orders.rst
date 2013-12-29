.. currentmodule:: dlkit.repository.search_orders
.. automodule:: dlkit.repository.search_orders

Search_Orders
=============


Asset Search Order
------------------

.. autoclass:: AssetSearchOrder
   :show-inheritance:

.. automethod:: AssetSearchOrder.order_by_title

.. automethod:: AssetSearchOrder.order_by_public_domain

.. automethod:: AssetSearchOrder.order_by_distribute_verbatim

.. automethod:: AssetSearchOrder.order_by_distribute_alterations

.. automethod:: AssetSearchOrder.order_by_distribute_compositions

.. automethod:: AssetSearchOrder.order_by_source

.. automethod:: AssetSearchOrder.supports_source_search_order

.. autoattribute:: AssetSearchOrder.source_search_order

.. automethod:: AssetSearchOrder.order_by_created_date

.. automethod:: AssetSearchOrder.order_by_published

.. automethod:: AssetSearchOrder.order_by_published_date

.. automethod:: AssetSearchOrder.order_by_principal_credit_string

.. automethod:: AssetSearchOrder.order_by_temporal_coverage

.. automethod:: AssetSearchOrder.get_asset_search_order_record



Composition Search Order
------------------------

.. autoclass:: CompositionSearchOrder
   :show-inheritance:

.. automethod:: CompositionSearchOrder.get_composition_search_order_record



Repository Search Order
-----------------------

.. autoclass:: RepositorySearchOrder
   :show-inheritance:

.. automethod:: RepositorySearchOrder.get_repository_search_order_record



