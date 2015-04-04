.. currentmodule:: dlkit.configuration.search_orders
.. automodule:: dlkit.configuration.search_orders

Search_Orders
=============


Parameter Search Order
----------------------

.. autoclass:: ParameterSearchOrder
   :show-inheritance:

   .. automethod:: ParameterSearchOrder.order_by_value_syntax

   .. automethod:: ParameterSearchOrder.order_by_values_shuffled

   .. automethod:: ParameterSearchOrder.get_parameter_search_order_record



Value Search Order
------------------

.. autoclass:: ValueSearchOrder
   :show-inheritance:

   .. automethod:: ValueSearchOrder.order_by_priority

   .. automethod:: ValueSearchOrder.order_by_value

   .. automethod:: ValueSearchOrder.supports_parameter_search_order

   .. autoattribute:: ValueSearchOrder.parameter_search_order

   .. automethod:: ValueSearchOrder.get_value_search_order_record



Configuration Search Order
--------------------------

.. autoclass:: ConfigurationSearchOrder
   :show-inheritance:

   .. automethod:: ConfigurationSearchOrder.get_configuration_search_order_record



