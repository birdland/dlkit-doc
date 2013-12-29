.. currentmodule:: dlkit.abstract_osid.authorization.search_orders
.. automodule:: dlkit.abstract_osid.authorization.search_orders

Search_Orders
=============


Authorization Search Order
--------------------------

.. autoclass:: AuthorizationSearchOrder
   :show-inheritance:

.. automethod:: AuthorizationSearchOrder.order_by_resource

.. automethod:: AuthorizationSearchOrder.supports_resource_search_order

.. autoattribute:: AuthorizationSearchOrder.resource_search_order

.. automethod:: AuthorizationSearchOrder.order_by_trust

.. automethod:: AuthorizationSearchOrder.order_by_agent

.. automethod:: AuthorizationSearchOrder.supports_agent_search_order

.. autoattribute:: AuthorizationSearchOrder.agent_search_order

.. automethod:: AuthorizationSearchOrder.order_by_function

.. automethod:: AuthorizationSearchOrder.supports_function_search_order

.. autoattribute:: AuthorizationSearchOrder.function_search_order

.. automethod:: AuthorizationSearchOrder.order_by_qualifier

.. automethod:: AuthorizationSearchOrder.supports_qualifier_search_order

.. autoattribute:: AuthorizationSearchOrder.qualifier_search_order

.. automethod:: AuthorizationSearchOrder.get_authorization_search_order_record



Function Search Order
---------------------

.. autoclass:: FunctionSearchOrder
   :show-inheritance:

.. automethod:: FunctionSearchOrder.order_by_qualifier_hierarchy

.. automethod:: FunctionSearchOrder.supports_qualifier_hierarchy_search_order

.. autoattribute:: FunctionSearchOrder.qualifier_hierarchy_search_order

.. automethod:: FunctionSearchOrder.get_function_search_order_record



Qualifier Search Order
----------------------

.. autoclass:: QualifierSearchOrder
   :show-inheritance:

.. automethod:: QualifierSearchOrder.get_qualifier_search_order_record



Vault Search Order
------------------

.. autoclass:: VaultSearchOrder
   :show-inheritance:

.. automethod:: VaultSearchOrder.get_vault_search_order_record



