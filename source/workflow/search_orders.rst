.. currentmodule:: dlkit.abstract_osid.workflow.search_orders
.. automodule:: dlkit.abstract_osid.workflow.search_orders

Search_Orders
=============


Process Search Order
--------------------

.. autoclass:: ProcessSearchOrder
   :show-inheritance:

.. automethod:: ProcessSearchOrder.order_by_enabled

.. automethod:: ProcessSearchOrder.order_by_initial_step

.. automethod:: ProcessSearchOrder.supports_initial_step_search_order

.. autoattribute:: ProcessSearchOrder.initial_step_search_order

.. automethod:: ProcessSearchOrder.order_by_initial_state

.. automethod:: ProcessSearchOrder.supports_initial_state_search_order

.. autoattribute:: ProcessSearchOrder.initial_state_search_order

.. automethod:: ProcessSearchOrder.get_process_search_order_record



Step Search Order
-----------------

.. autoclass:: StepSearchOrder
   :show-inheritance:

.. automethod:: StepSearchOrder.order_by_process

.. automethod:: StepSearchOrder.supports_process_search_order

.. autoattribute:: StepSearchOrder.process_search_order

.. automethod:: StepSearchOrder.order_by_initial

.. automethod:: StepSearchOrder.order_by_terminal

.. automethod:: StepSearchOrder.order_by_next_state

.. automethod:: StepSearchOrder.supports_next_state_search_order

.. autoattribute:: StepSearchOrder.next_state_search_order

.. automethod:: StepSearchOrder.get_step_search_order_record



Work Search Order
-----------------

.. autoclass:: WorkSearchOrder
   :show-inheritance:

.. automethod:: WorkSearchOrder.get_work_search_order_record



Office Search Order
-------------------

.. autoclass:: OfficeSearchOrder
   :show-inheritance:

.. automethod:: OfficeSearchOrder.get_office_search_order_record



