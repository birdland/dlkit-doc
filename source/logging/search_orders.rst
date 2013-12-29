.. currentmodule:: dlkit.abstract_osid.logging.search_orders
.. automodule:: dlkit.abstract_osid.logging.search_orders

Search_Orders
=============


Log Entry Search Order
----------------------

.. autoclass:: LogEntrySearchOrder
   :show-inheritance:

.. automethod:: LogEntrySearchOrder.order_by_priority_type

.. automethod:: LogEntrySearchOrder.order_by_timestamp

.. automethod:: LogEntrySearchOrder.order_by_resource

.. automethod:: LogEntrySearchOrder.supports_resource_search_order

.. autoattribute:: LogEntrySearchOrder.resource_search_order

.. automethod:: LogEntrySearchOrder.order_by_agent

.. automethod:: LogEntrySearchOrder.supports_agent_search_order

.. autoattribute:: LogEntrySearchOrder.agent_search_order

.. automethod:: LogEntrySearchOrder.get_log_entry_search_order_record



Log Search Order
----------------

.. autoclass:: LogSearchOrder
   :show-inheritance:

.. automethod:: LogSearchOrder.get_log_search_order_record



