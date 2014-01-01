.. currentmodule:: dlkit.resource.search_orders
.. automodule:: dlkit.resource.search_orders

Search_Orders
=============


Resource Search Order
---------------------

.. autoclass:: ResourceSearchOrder
   :show-inheritance:

   .. automethod:: ResourceSearchOrder.order_by_group

   .. automethod:: ResourceSearchOrder.order_by_demographic

   .. automethod:: ResourceSearchOrder.order_by_avatar

   .. automethod:: ResourceSearchOrder.supports_avatar_search_order

   .. autoattribute:: ResourceSearchOrder.avatar_search_order

   .. automethod:: ResourceSearchOrder.get_resource_search_order_record



Resource Relationship Search Order
----------------------------------

.. autoclass:: ResourceRelationshipSearchOrder
   :show-inheritance:

   .. automethod:: ResourceRelationshipSearchOrder.order_by_source_resource

   .. automethod:: ResourceRelationshipSearchOrder.supports_source_resource_search_order

   .. autoattribute:: ResourceRelationshipSearchOrder.source_resource_search_order

   .. automethod:: ResourceRelationshipSearchOrder.order_by_destination_resource

   .. automethod:: ResourceRelationshipSearchOrder.supports_destination_resource_search_order

   .. autoattribute:: ResourceRelationshipSearchOrder.destination_resource_search_order

   .. automethod:: ResourceRelationshipSearchOrder.get_resource_relationship_search_order_record



Bin Search Order
----------------

.. autoclass:: BinSearchOrder
   :show-inheritance:

   .. automethod:: BinSearchOrder.get_bin_search_order_record



