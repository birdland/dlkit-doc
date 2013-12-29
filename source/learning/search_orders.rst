.. currentmodule:: dlkit.abstract_osid.learning.search_orders
.. automodule:: dlkit.abstract_osid.learning.search_orders

Search_Orders
=============


Objective Search Order
----------------------

.. autoclass:: ObjectiveSearchOrder
   :show-inheritance:

.. automethod:: ObjectiveSearchOrder.order_by_assessment

.. automethod:: ObjectiveSearchOrder.supports_assessment_search_order

.. autoattribute:: ObjectiveSearchOrder.assessment_search_order

.. automethod:: ObjectiveSearchOrder.order_by_knowledge_category

.. automethod:: ObjectiveSearchOrder.supports_knowledge_category_search_order

.. autoattribute:: ObjectiveSearchOrder.knowledge_category_search_order

.. automethod:: ObjectiveSearchOrder.order_by_cognitive_process

.. automethod:: ObjectiveSearchOrder.supports_cognitive_process_search_order

.. autoattribute:: ObjectiveSearchOrder.cognitive_process_search_order

.. automethod:: ObjectiveSearchOrder.get_objective_search_order_record



Activity Search Order
---------------------

.. autoclass:: ActivitySearchOrder
   :show-inheritance:

.. automethod:: ActivitySearchOrder.order_by_objective

.. automethod:: ActivitySearchOrder.supports_objective_search_order

.. autoattribute:: ActivitySearchOrder.objective_search_order

.. automethod:: ActivitySearchOrder.get_activity_search_order_record



Proficiency Search Order
------------------------

.. autoclass:: ProficiencySearchOrder
   :show-inheritance:

.. automethod:: ProficiencySearchOrder.order_by_resource

.. automethod:: ProficiencySearchOrder.supports_resource_search_order

.. autoattribute:: ProficiencySearchOrder.resource_search_order

.. automethod:: ProficiencySearchOrder.order_by_objective

.. automethod:: ProficiencySearchOrder.supports_objective_search_order

.. autoattribute:: ProficiencySearchOrder.objective_search_order

.. automethod:: ProficiencySearchOrder.order_by_completion

.. automethod:: ProficiencySearchOrder.order_by_level

.. automethod:: ProficiencySearchOrder.supports_level_search_order

.. autoattribute:: ProficiencySearchOrder.level_search_order

.. automethod:: ProficiencySearchOrder.get_proficiency_search_order_record



Objective Bank Search Order
---------------------------

.. autoclass:: ObjectiveBankSearchOrder
   :show-inheritance:

.. automethod:: ObjectiveBankSearchOrder.get_objective_bank_search_order_record



