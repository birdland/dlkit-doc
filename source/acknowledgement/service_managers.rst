Summary
=======
.. currentmodule:: dlkit.services.acknowledgement
.. automodule:: dlkit.services.acknowledgement

Service Managers
================


Acknowledgement Manager
-----------------------

.. autoclass:: AcknowledgementManager
   :show-inheritance:

   .. autoattribute:: AcknowledgementManager.acknowledgement_batch_manager



Acknowledgement Profile Methods
_______________________

   .. automethod:: AcknowledgementManager.supports_visible_federation

   .. automethod:: AcknowledgementManager.supports_credit_lookup

   .. automethod:: AcknowledgementManager.supports_credit_query

   .. automethod:: AcknowledgementManager.supports_credit_search

   .. automethod:: AcknowledgementManager.supports_credit_admin

   .. automethod:: AcknowledgementManager.supports_credit_notification

   .. automethod:: AcknowledgementManager.supports_credit_billing

   .. automethod:: AcknowledgementManager.supports_credit_billing_assignment

   .. automethod:: AcknowledgementManager.supports_credit_smart_billing

   .. automethod:: AcknowledgementManager.supports_billing_lookup

   .. automethod:: AcknowledgementManager.supports_billing_query

   .. automethod:: AcknowledgementManager.supports_billing_search

   .. automethod:: AcknowledgementManager.supports_billing_admin

   .. automethod:: AcknowledgementManager.supports_billing_notification

   .. automethod:: AcknowledgementManager.supports_billing_hierarchy

   .. automethod:: AcknowledgementManager.supports_billing_hierarchy_design

   .. automethod:: AcknowledgementManager.supports_acknowledgement_batch

   .. autoattribute:: AcknowledgementManager.credit_record_types

   .. automethod:: AcknowledgementManager.supports_credit_record_type

   .. autoattribute:: AcknowledgementManager.credit_search_record_types

   .. automethod:: AcknowledgementManager.supports_credit_search_record_type

   .. autoattribute:: AcknowledgementManager.billing_record_types

   .. automethod:: AcknowledgementManager.supports_billing_record_type

   .. autoattribute:: AcknowledgementManager.billing_search_record_types

   .. automethod:: AcknowledgementManager.supports_billing_search_record_type



Billing Lookup
______________

   .. automethod:: AcknowledgementManager.can_lookup_billings

   .. automethod:: AcknowledgementManager.use_comparative_billing_view

   .. automethod:: AcknowledgementManager.use_plenary_billing_view

   .. automethod:: AcknowledgementManager.get_billing

   .. automethod:: AcknowledgementManager.get_billings_by_ids

   .. automethod:: AcknowledgementManager.get_billings_by_genus_type

   .. automethod:: AcknowledgementManager.get_billings_by_parent_genus_type

   .. automethod:: AcknowledgementManager.get_billings_by_record_type

   .. automethod:: AcknowledgementManager.get_billings_by_provider

   .. autoattribute:: AcknowledgementManager.billings



Billing Query
_____________

   .. automethod:: AcknowledgementManager.can_search_billings

   .. autoattribute:: AcknowledgementManager.billing_query

   .. automethod:: AcknowledgementManager.get_billings_by_query



Billing Search
______________

   .. autoattribute:: AcknowledgementManager.billing_search

   .. autoattribute:: AcknowledgementManager.billing_search_order

   .. automethod:: AcknowledgementManager.get_billings_by_search

   .. automethod:: AcknowledgementManager.get_billing_query_from_inspector



Billing Admin
_____________

   .. automethod:: AcknowledgementManager.can_create_billings

   .. automethod:: AcknowledgementManager.can_create_billing_with_record_types

   .. automethod:: AcknowledgementManager.get_billing_form_for_create

   .. automethod:: AcknowledgementManager.create_billing

   .. automethod:: AcknowledgementManager.can_update_billings

   .. automethod:: AcknowledgementManager.get_billing_form_for_update

   .. automethod:: AcknowledgementManager.update_billing

   .. automethod:: AcknowledgementManager.can_delete_billings

   .. automethod:: AcknowledgementManager.delete_billing

   .. automethod:: AcknowledgementManager.can_manage_billing_aliases

   .. automethod:: AcknowledgementManager.alias_billing



Billing Notification
____________________

   .. automethod:: AcknowledgementManager.can_register_for_billing_notifications

   .. automethod:: AcknowledgementManager.reliable_billing_notifications

   .. automethod:: AcknowledgementManager.unreliable_billing_notifications

   .. automethod:: AcknowledgementManager.acknowledge_billing_notification

   .. automethod:: AcknowledgementManager.register_for_new_billings

   .. automethod:: AcknowledgementManager.register_for_changed_billings

   .. automethod:: AcknowledgementManager.register_for_changed_billing

   .. automethod:: AcknowledgementManager.register_for_deleted_billings

   .. automethod:: AcknowledgementManager.register_for_deleted_billing

   .. automethod:: AcknowledgementManager.register_for_changed_billing_hierarchy

   .. automethod:: AcknowledgementManager.register_for_changed_billing_hierarchy_for_ancestors

   .. automethod:: AcknowledgementManager.register_for_changed_billing_hierarchy_for_descendants



Billing Hierarchy
_________________

   .. autoattribute:: AcknowledgementManager.billing_hierarchy_id

   .. autoattribute:: AcknowledgementManager.billing_hierarchy

   .. automethod:: AcknowledgementManager.can_access_billing_hierarchy

   .. automethod:: AcknowledgementManager.use_comparative_billing_view

   .. automethod:: AcknowledgementManager.use_plenary_billing_view

   .. autoattribute:: AcknowledgementManager.root_billing_ids

   .. autoattribute:: AcknowledgementManager.root_billings

   .. automethod:: AcknowledgementManager.has_parent_billings

   .. automethod:: AcknowledgementManager.is_parent_of_billing

   .. automethod:: AcknowledgementManager.get_parent_billing_ids

   .. automethod:: AcknowledgementManager.get_parent_billings

   .. automethod:: AcknowledgementManager.is_ancestor_of_billing

   .. automethod:: AcknowledgementManager.has_child_billings

   .. automethod:: AcknowledgementManager.is_child_of_billing

   .. automethod:: AcknowledgementManager.get_child_billing_ids

   .. automethod:: AcknowledgementManager.get_child_billings

   .. automethod:: AcknowledgementManager.is_descendant_of_billing

   .. automethod:: AcknowledgementManager.get_billing_node_ids

   .. automethod:: AcknowledgementManager.get_billing_nodes



Billing Hierarchy Design
________________________

   .. autoattribute:: AcknowledgementManager.billing_hierarchy_id

   .. autoattribute:: AcknowledgementManager.billing_hierarchy

   .. automethod:: AcknowledgementManager.can_modify_billing_hierarchy

   .. automethod:: AcknowledgementManager.add_root_billing

   .. automethod:: AcknowledgementManager.remove_root_billing

   .. automethod:: AcknowledgementManager.add_child_billing

   .. automethod:: AcknowledgementManager.remove_child_billing

   .. automethod:: AcknowledgementManager.remove_child_billings



Acknowledgement Proxy Manager
-----------------------------

.. autoclass:: AcknowledgementProxyManager
   :show-inheritance:

   .. autoattribute:: AcknowledgementProxyManager.acknowledgement_batch_proxy_manager



Acknowledgement Profile Methods
_______________________

   .. automethod:: AcknowledgementProxyManager.supports_visible_federation

   .. automethod:: AcknowledgementProxyManager.supports_credit_lookup

   .. automethod:: AcknowledgementProxyManager.supports_credit_query

   .. automethod:: AcknowledgementProxyManager.supports_credit_search

   .. automethod:: AcknowledgementProxyManager.supports_credit_admin

   .. automethod:: AcknowledgementProxyManager.supports_credit_notification

   .. automethod:: AcknowledgementProxyManager.supports_credit_billing

   .. automethod:: AcknowledgementProxyManager.supports_credit_billing_assignment

   .. automethod:: AcknowledgementProxyManager.supports_credit_smart_billing

   .. automethod:: AcknowledgementProxyManager.supports_billing_lookup

   .. automethod:: AcknowledgementProxyManager.supports_billing_query

   .. automethod:: AcknowledgementProxyManager.supports_billing_search

   .. automethod:: AcknowledgementProxyManager.supports_billing_admin

   .. automethod:: AcknowledgementProxyManager.supports_billing_notification

   .. automethod:: AcknowledgementProxyManager.supports_billing_hierarchy

   .. automethod:: AcknowledgementProxyManager.supports_billing_hierarchy_design

   .. automethod:: AcknowledgementProxyManager.supports_acknowledgement_batch

   .. autoattribute:: AcknowledgementProxyManager.credit_record_types

   .. automethod:: AcknowledgementProxyManager.supports_credit_record_type

   .. autoattribute:: AcknowledgementProxyManager.credit_search_record_types

   .. automethod:: AcknowledgementProxyManager.supports_credit_search_record_type

   .. autoattribute:: AcknowledgementProxyManager.billing_record_types

   .. automethod:: AcknowledgementProxyManager.supports_billing_record_type

   .. autoattribute:: AcknowledgementProxyManager.billing_search_record_types

   .. automethod:: AcknowledgementProxyManager.supports_billing_search_record_type



Billing Lookup
______________

   .. automethod:: AcknowledgementProxyManager.can_lookup_billings

   .. automethod:: AcknowledgementProxyManager.use_comparative_billing_view

   .. automethod:: AcknowledgementProxyManager.use_plenary_billing_view

   .. automethod:: AcknowledgementProxyManager.get_billing

   .. automethod:: AcknowledgementProxyManager.get_billings_by_ids

   .. automethod:: AcknowledgementProxyManager.get_billings_by_genus_type

   .. automethod:: AcknowledgementProxyManager.get_billings_by_parent_genus_type

   .. automethod:: AcknowledgementProxyManager.get_billings_by_record_type

   .. automethod:: AcknowledgementProxyManager.get_billings_by_provider

   .. autoattribute:: AcknowledgementProxyManager.billings



Billing Query
_____________

   .. automethod:: AcknowledgementProxyManager.can_search_billings

   .. autoattribute:: AcknowledgementProxyManager.billing_query

   .. automethod:: AcknowledgementProxyManager.get_billings_by_query



Billing Search
______________

   .. autoattribute:: AcknowledgementProxyManager.billing_search

   .. autoattribute:: AcknowledgementProxyManager.billing_search_order

   .. automethod:: AcknowledgementProxyManager.get_billings_by_search

   .. automethod:: AcknowledgementProxyManager.get_billing_query_from_inspector



Billing Admin
_____________

   .. automethod:: AcknowledgementProxyManager.can_create_billings

   .. automethod:: AcknowledgementProxyManager.can_create_billing_with_record_types

   .. automethod:: AcknowledgementProxyManager.get_billing_form_for_create

   .. automethod:: AcknowledgementProxyManager.create_billing

   .. automethod:: AcknowledgementProxyManager.can_update_billings

   .. automethod:: AcknowledgementProxyManager.get_billing_form_for_update

   .. automethod:: AcknowledgementProxyManager.update_billing

   .. automethod:: AcknowledgementProxyManager.can_delete_billings

   .. automethod:: AcknowledgementProxyManager.delete_billing

   .. automethod:: AcknowledgementProxyManager.can_manage_billing_aliases

   .. automethod:: AcknowledgementProxyManager.alias_billing



Billing Notification
____________________

   .. automethod:: AcknowledgementProxyManager.can_register_for_billing_notifications

   .. automethod:: AcknowledgementProxyManager.reliable_billing_notifications

   .. automethod:: AcknowledgementProxyManager.unreliable_billing_notifications

   .. automethod:: AcknowledgementProxyManager.acknowledge_billing_notification

   .. automethod:: AcknowledgementProxyManager.register_for_new_billings

   .. automethod:: AcknowledgementProxyManager.register_for_changed_billings

   .. automethod:: AcknowledgementProxyManager.register_for_changed_billing

   .. automethod:: AcknowledgementProxyManager.register_for_deleted_billings

   .. automethod:: AcknowledgementProxyManager.register_for_deleted_billing

   .. automethod:: AcknowledgementProxyManager.register_for_changed_billing_hierarchy

   .. automethod:: AcknowledgementProxyManager.register_for_changed_billing_hierarchy_for_ancestors

   .. automethod:: AcknowledgementProxyManager.register_for_changed_billing_hierarchy_for_descendants



Billing Hierarchy
_________________

   .. autoattribute:: AcknowledgementProxyManager.billing_hierarchy_id

   .. autoattribute:: AcknowledgementProxyManager.billing_hierarchy

   .. automethod:: AcknowledgementProxyManager.can_access_billing_hierarchy

   .. automethod:: AcknowledgementProxyManager.use_comparative_billing_view

   .. automethod:: AcknowledgementProxyManager.use_plenary_billing_view

   .. autoattribute:: AcknowledgementProxyManager.root_billing_ids

   .. autoattribute:: AcknowledgementProxyManager.root_billings

   .. automethod:: AcknowledgementProxyManager.has_parent_billings

   .. automethod:: AcknowledgementProxyManager.is_parent_of_billing

   .. automethod:: AcknowledgementProxyManager.get_parent_billing_ids

   .. automethod:: AcknowledgementProxyManager.get_parent_billings

   .. automethod:: AcknowledgementProxyManager.is_ancestor_of_billing

   .. automethod:: AcknowledgementProxyManager.has_child_billings

   .. automethod:: AcknowledgementProxyManager.is_child_of_billing

   .. automethod:: AcknowledgementProxyManager.get_child_billing_ids

   .. automethod:: AcknowledgementProxyManager.get_child_billings

   .. automethod:: AcknowledgementProxyManager.is_descendant_of_billing

   .. automethod:: AcknowledgementProxyManager.get_billing_node_ids

   .. automethod:: AcknowledgementProxyManager.get_billing_nodes



Billing Hierarchy Design
________________________

   .. autoattribute:: AcknowledgementProxyManager.billing_hierarchy_id

   .. autoattribute:: AcknowledgementProxyManager.billing_hierarchy

   .. automethod:: AcknowledgementProxyManager.can_modify_billing_hierarchy

   .. automethod:: AcknowledgementProxyManager.add_root_billing

   .. automethod:: AcknowledgementProxyManager.remove_root_billing

   .. automethod:: AcknowledgementProxyManager.add_child_billing

   .. automethod:: AcknowledgementProxyManager.remove_child_billing

   .. automethod:: AcknowledgementProxyManager.remove_child_billings



