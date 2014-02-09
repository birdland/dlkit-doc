.. currentmodule:: dlkit.osid.search_orders
.. automodule:: dlkit.osid.search_orders

Search_Orders
=============


Osid Search Order
-----------------

.. autoclass:: OsidSearchOrder
   :show-inheritance:





Osid Identifiable Search Order
------------------------------

.. autoclass:: OsidIdentifiableSearchOrder
   :show-inheritance:

   .. automethod:: OsidIdentifiableSearchOrder.order_by_id



Osid Extensible Search Order
----------------------------

.. autoclass:: OsidExtensibleSearchOrder
   :show-inheritance:





Osid Browsable Search Order
---------------------------

.. autoclass:: OsidBrowsableSearchOrder
   :show-inheritance:





Osid Temporal Search Order
--------------------------

.. autoclass:: OsidTemporalSearchOrder
   :show-inheritance:

   .. automethod:: OsidTemporalSearchOrder.order_by_effective

   .. automethod:: OsidTemporalSearchOrder.order_by_start_date

   .. automethod:: OsidTemporalSearchOrder.order_by_end_date



Osid Subjugateable Search Order
-------------------------------

.. autoclass:: OsidSubjugateableSearchOrder
   :show-inheritance:





Osid Aggregateable Search Order
-------------------------------

.. autoclass:: OsidAggregateableSearchOrder
   :show-inheritance:





Osid Containable Search Order
-----------------------------

.. autoclass:: OsidContainableSearchOrder
   :show-inheritance:

   .. automethod:: OsidContainableSearchOrder.order_by_sequestered



Osid Sourceable Search Order
----------------------------

.. autoclass:: OsidSourceableSearchOrder
   :show-inheritance:

   .. automethod:: OsidSourceableSearchOrder.order_by_provider

   .. automethod:: OsidSourceableSearchOrder.supports_provider_search_order

   .. autoattribute:: OsidSourceableSearchOrder.provider_search_order



Osid Federateable Search Order
------------------------------

.. autoclass:: OsidFederateableSearchOrder
   :show-inheritance:





Osid Operable Search Order
--------------------------

.. autoclass:: OsidOperableSearchOrder
   :show-inheritance:

   .. automethod:: OsidOperableSearchOrder.order_by_active

   .. automethod:: OsidOperableSearchOrder.order_by_enabled

   .. automethod:: OsidOperableSearchOrder.order_by_disabled

   .. automethod:: OsidOperableSearchOrder.order_by_operational



Osid Object Search Order
------------------------

.. autoclass:: OsidObjectSearchOrder
   :show-inheritance:

   .. automethod:: OsidObjectSearchOrder.order_by_display_name

   .. automethod:: OsidObjectSearchOrder.order_by_description

   .. automethod:: OsidObjectSearchOrder.order_by_genus_type

   .. automethod:: OsidObjectSearchOrder.order_by_state

   .. automethod:: OsidObjectSearchOrder.order_by_cumulative_rating

   .. automethod:: OsidObjectSearchOrder.order_by_statistic

   .. automethod:: OsidObjectSearchOrder.order_by_create_time

   .. automethod:: OsidObjectSearchOrder.order_by_last_modified_time



Osid Relationship Search Order
------------------------------

.. autoclass:: OsidRelationshipSearchOrder
   :show-inheritance:

   .. automethod:: OsidRelationshipSearchOrder.order_by_end_reason

   .. automethod:: OsidRelationshipSearchOrder.supports_end_reason_search_order

   .. autoattribute:: OsidRelationshipSearchOrder.end_reason_search_order



Osid Catalog Search Order
-------------------------

.. autoclass:: OsidCatalogSearchOrder
   :show-inheritance:





Osid Rule Search Order
----------------------

.. autoclass:: OsidRuleSearchOrder
   :show-inheritance:

   .. automethod:: OsidRuleSearchOrder.order_by_rule

   .. automethod:: OsidRuleSearchOrder.supports_rule_search_order

   .. autoattribute:: OsidRuleSearchOrder.rule_search_order



Osid Enabler Search Order
-------------------------

.. autoclass:: OsidEnablerSearchOrder
   :show-inheritance:

   .. automethod:: OsidEnablerSearchOrder.order_by_schedule

   .. automethod:: OsidEnablerSearchOrder.supports_schedule_search_order

   .. autoattribute:: OsidEnablerSearchOrder.schedule_search_order

   .. automethod:: OsidEnablerSearchOrder.order_by_event

   .. automethod:: OsidEnablerSearchOrder.supports_event_search_order

   .. autoattribute:: OsidEnablerSearchOrder.event_search_order

   .. automethod:: OsidEnablerSearchOrder.order_by_cyclic_event

   .. automethod:: OsidEnablerSearchOrder.supports_cyclic_event_search_order

   .. autoattribute:: OsidEnablerSearchOrder.cyclic_event_search_order

   .. automethod:: OsidEnablerSearchOrder.order_by_demographic

   .. automethod:: OsidEnablerSearchOrder.supports_demographic_search_order

   .. autoattribute:: OsidEnablerSearchOrder.demographic_search_order



Osid Constrainer Search Order
-----------------------------

.. autoclass:: OsidConstrainerSearchOrder
   :show-inheritance:





Osid Processor Search Order
---------------------------

.. autoclass:: OsidProcessorSearchOrder
   :show-inheritance:





Osid Governator Search Order
----------------------------

.. autoclass:: OsidGovernatorSearchOrder
   :show-inheritance:





Osid Compendium Search Order
----------------------------

.. autoclass:: OsidCompendiumSearchOrder
   :show-inheritance:

   .. automethod:: OsidCompendiumSearchOrder.order_by_start_date

   .. automethod:: OsidCompendiumSearchOrder.order_by_end_date

   .. automethod:: OsidCompendiumSearchOrder.order_by_interpolated

   .. automethod:: OsidCompendiumSearchOrder.order_by_extrapolated



Osid Capsule Search Order
-------------------------

.. autoclass:: OsidCapsuleSearchOrder
   :show-inheritance:





