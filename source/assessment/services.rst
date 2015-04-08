Summary
=======
.. currentmodule:: dlkit.services.assessment
.. automodule:: dlkit.services.assessment

Service Managers
========


Assessment Manager
------------------

.. autoclass:: AssessmentManager
   :show-inheritance:

   .. autoattribute:: AssessmentManager.assessment_authoring_manager

   .. autoattribute:: AssessmentManager.assessment_batch_manager



Assessment Profile Methods
__________________

   .. automethod:: AssessmentManager.supports_visible_federation

   .. automethod:: AssessmentManager.supports_my_assessment_taken

   .. automethod:: AssessmentManager.supports_assessment

   .. automethod:: AssessmentManager.supports_assessment_results

   .. automethod:: AssessmentManager.supports_item_lookup

   .. automethod:: AssessmentManager.supports_item_query

   .. automethod:: AssessmentManager.supports_item_search

   .. automethod:: AssessmentManager.supports_item_admin

   .. automethod:: AssessmentManager.supports_item_notification

   .. automethod:: AssessmentManager.supports_item_bank

   .. automethod:: AssessmentManager.supports_item_bank_assignment

   .. automethod:: AssessmentManager.supports_item_smart_bank

   .. automethod:: AssessmentManager.supports_assessment_lookup

   .. automethod:: AssessmentManager.supports_assessment_query

   .. automethod:: AssessmentManager.supports_assessment_search

   .. automethod:: AssessmentManager.supports_assessment_admin

   .. automethod:: AssessmentManager.supports_assessment_notification

   .. automethod:: AssessmentManager.supports_assessment_bank

   .. automethod:: AssessmentManager.supports_assessment_bank_assignment

   .. automethod:: AssessmentManager.supports_assessment_smart_bank

   .. automethod:: AssessmentManager.supports_assessment_basic_authoring

   .. automethod:: AssessmentManager.supports_assessment_offered_lookup

   .. automethod:: AssessmentManager.supports_assessment_offered_query

   .. automethod:: AssessmentManager.supports_assessment_offered_search

   .. automethod:: AssessmentManager.supports_assessment_offered_admin

   .. automethod:: AssessmentManager.supports_assessment_offered_notification

   .. automethod:: AssessmentManager.supports_assessment_offered_bank

   .. automethod:: AssessmentManager.supports_assessment_offered_bank_assignment

   .. automethod:: AssessmentManager.supports_assessment_offered_smart_bank

   .. automethod:: AssessmentManager.supports_assessment_taken_lookup

   .. automethod:: AssessmentManager.supports_assessment_taken_query

   .. automethod:: AssessmentManager.supports_assessment_taken_search

   .. automethod:: AssessmentManager.supports_assessment_taken_admin

   .. automethod:: AssessmentManager.supports_assessment_taken_notification

   .. automethod:: AssessmentManager.supports_assessment_taken_bank

   .. automethod:: AssessmentManager.supports_assessment_taken_bank_assignment

   .. automethod:: AssessmentManager.supports_assessment_taken_smart_bank

   .. automethod:: AssessmentManager.supports_bank_lookup

   .. automethod:: AssessmentManager.supports_bank_query

   .. automethod:: AssessmentManager.supports_bank_search

   .. automethod:: AssessmentManager.supports_bank_admin

   .. automethod:: AssessmentManager.supports_bank_notification

   .. automethod:: AssessmentManager.supports_bank_hierarchy

   .. automethod:: AssessmentManager.supports_bank_hierarchy_design

   .. automethod:: AssessmentManager.supports_assessment_authoring

   .. automethod:: AssessmentManager.supports_assessment_batch

   .. autoattribute:: AssessmentManager.item_record_types

   .. automethod:: AssessmentManager.supports_item_record_type

   .. autoattribute:: AssessmentManager.item_search_record_types

   .. automethod:: AssessmentManager.supports_item_search_record_type

   .. autoattribute:: AssessmentManager.assessment_record_types

   .. automethod:: AssessmentManager.supports_assessment_record_type

   .. autoattribute:: AssessmentManager.assessment_search_record_types

   .. automethod:: AssessmentManager.supports_assessment_search_record_type

   .. autoattribute:: AssessmentManager.assessment_offered_record_types

   .. automethod:: AssessmentManager.supports_assessment_offered_record_type

   .. autoattribute:: AssessmentManager.assessment_offered_search_record_types

   .. automethod:: AssessmentManager.supports_assessment_offered_search_record_type

   .. autoattribute:: AssessmentManager.assessment_taken_record_types

   .. automethod:: AssessmentManager.supports_assessment_taken_record_type

   .. autoattribute:: AssessmentManager.assessment_taken_search_record_types

   .. automethod:: AssessmentManager.supports_assessment_taken_search_record_type

   .. autoattribute:: AssessmentManager.assessment_section_record_types

   .. automethod:: AssessmentManager.supports_assessment_section_record_type

   .. autoattribute:: AssessmentManager.bank_record_types

   .. automethod:: AssessmentManager.supports_bank_record_type

   .. autoattribute:: AssessmentManager.bank_search_record_types

   .. automethod:: AssessmentManager.supports_bank_search_record_type



Bank Lookup
___________

   .. automethod:: AssessmentManager.can_lookup_banks

   .. automethod:: AssessmentManager.use_comparative_bank_view

   .. automethod:: AssessmentManager.use_plenary_bank_view

   .. automethod:: AssessmentManager.get_bank

   .. automethod:: AssessmentManager.get_banks_by_ids

   .. automethod:: AssessmentManager.get_banks_by_genus_type

   .. automethod:: AssessmentManager.get_banks_by_parent_genus_type

   .. automethod:: AssessmentManager.get_banks_by_record_type

   .. automethod:: AssessmentManager.get_banks_by_provider

   .. autoattribute:: AssessmentManager.banks



Bank Query
__________

   .. automethod:: AssessmentManager.can_search_banks

   .. autoattribute:: AssessmentManager.bank_query

   .. automethod:: AssessmentManager.get_banks_by_query



Bank Search
___________

   .. autoattribute:: AssessmentManager.bank_search

   .. autoattribute:: AssessmentManager.bank_search_order

   .. automethod:: AssessmentManager.get_banks_by_search

   .. automethod:: AssessmentManager.get_bank_query_from_inspector



Bank Admin
__________

   .. automethod:: AssessmentManager.can_create_banks

   .. automethod:: AssessmentManager.can_create_bank_with_record_types

   .. automethod:: AssessmentManager.get_bank_form_for_create

   .. automethod:: AssessmentManager.create_bank

   .. automethod:: AssessmentManager.can_update_banks

   .. automethod:: AssessmentManager.get_bank_form_for_update

   .. automethod:: AssessmentManager.update_bank

   .. automethod:: AssessmentManager.can_delete_banks

   .. automethod:: AssessmentManager.delete_bank

   .. automethod:: AssessmentManager.can_manage_bank_aliases

   .. automethod:: AssessmentManager.alias_bank



Bank Notification
_________________

   .. automethod:: AssessmentManager.can_register_for_bank_notifications

   .. automethod:: AssessmentManager.reliable_bank_notifications

   .. automethod:: AssessmentManager.unreliable_bank_notifications

   .. automethod:: AssessmentManager.acknowledge_bank_notification

   .. automethod:: AssessmentManager.register_for_new_banks

   .. automethod:: AssessmentManager.register_for_changed_banks

   .. automethod:: AssessmentManager.register_for_changed_bank

   .. automethod:: AssessmentManager.register_for_deleted_banks

   .. automethod:: AssessmentManager.register_for_deleted_bank

   .. automethod:: AssessmentManager.register_for_changed_bank_hierarchy

   .. automethod:: AssessmentManager.register_for_changed_bank_hierarchy_for_ancestors

   .. automethod:: AssessmentManager.register_for_changed_bank_hierarchy_for_descendants



Bank Hierarchy
______________

   .. autoattribute:: AssessmentManager.bank_hierarchy_id

   .. autoattribute:: AssessmentManager.bank_hierarchy

   .. automethod:: AssessmentManager.can_access_bank_hierarchy

   .. automethod:: AssessmentManager.use_comparative_bank_view

   .. automethod:: AssessmentManager.use_plenary_bank_view

   .. autoattribute:: AssessmentManager.root_bank_ids

   .. autoattribute:: AssessmentManager.root_banks

   .. automethod:: AssessmentManager.has_parent_banks

   .. automethod:: AssessmentManager.is_parent_of_bank

   .. automethod:: AssessmentManager.get_parent_bank_ids

   .. automethod:: AssessmentManager.get_parent_banks

   .. automethod:: AssessmentManager.is_ancestor_of_bank

   .. automethod:: AssessmentManager.has_child_banks

   .. automethod:: AssessmentManager.is_child_of_bank

   .. automethod:: AssessmentManager.get_child_bank_ids

   .. automethod:: AssessmentManager.get_child_banks

   .. automethod:: AssessmentManager.is_descendant_of_bank

   .. automethod:: AssessmentManager.get_bank_node_ids

   .. automethod:: AssessmentManager.get_bank_nodes



Bank Hierarchy Design
_____________________

   .. autoattribute:: AssessmentManager.bank_hierarchy_id

   .. autoattribute:: AssessmentManager.bank_hierarchy

   .. automethod:: AssessmentManager.can_modify_bank_hierarchy

   .. automethod:: AssessmentManager.add_root_bank

   .. automethod:: AssessmentManager.remove_root_bank

   .. automethod:: AssessmentManager.add_child_bank

   .. automethod:: AssessmentManager.remove_child_bank

   .. automethod:: AssessmentManager.remove_child_banks



Assessment Proxy Manager
------------------------

.. autoclass:: AssessmentProxyManager
   :show-inheritance:

   .. autoattribute:: AssessmentProxyManager.assessment_authoring_proxy_manager

   .. autoattribute:: AssessmentProxyManager.assessment_batch_proxy_manager



Assessment Profile Methods
__________________

   .. automethod:: AssessmentProxyManager.supports_visible_federation

   .. automethod:: AssessmentProxyManager.supports_my_assessment_taken

   .. automethod:: AssessmentProxyManager.supports_assessment

   .. automethod:: AssessmentProxyManager.supports_assessment_results

   .. automethod:: AssessmentProxyManager.supports_item_lookup

   .. automethod:: AssessmentProxyManager.supports_item_query

   .. automethod:: AssessmentProxyManager.supports_item_search

   .. automethod:: AssessmentProxyManager.supports_item_admin

   .. automethod:: AssessmentProxyManager.supports_item_notification

   .. automethod:: AssessmentProxyManager.supports_item_bank

   .. automethod:: AssessmentProxyManager.supports_item_bank_assignment

   .. automethod:: AssessmentProxyManager.supports_item_smart_bank

   .. automethod:: AssessmentProxyManager.supports_assessment_lookup

   .. automethod:: AssessmentProxyManager.supports_assessment_query

   .. automethod:: AssessmentProxyManager.supports_assessment_search

   .. automethod:: AssessmentProxyManager.supports_assessment_admin

   .. automethod:: AssessmentProxyManager.supports_assessment_notification

   .. automethod:: AssessmentProxyManager.supports_assessment_bank

   .. automethod:: AssessmentProxyManager.supports_assessment_bank_assignment

   .. automethod:: AssessmentProxyManager.supports_assessment_smart_bank

   .. automethod:: AssessmentProxyManager.supports_assessment_basic_authoring

   .. automethod:: AssessmentProxyManager.supports_assessment_offered_lookup

   .. automethod:: AssessmentProxyManager.supports_assessment_offered_query

   .. automethod:: AssessmentProxyManager.supports_assessment_offered_search

   .. automethod:: AssessmentProxyManager.supports_assessment_offered_admin

   .. automethod:: AssessmentProxyManager.supports_assessment_offered_notification

   .. automethod:: AssessmentProxyManager.supports_assessment_offered_bank

   .. automethod:: AssessmentProxyManager.supports_assessment_offered_bank_assignment

   .. automethod:: AssessmentProxyManager.supports_assessment_offered_smart_bank

   .. automethod:: AssessmentProxyManager.supports_assessment_taken_lookup

   .. automethod:: AssessmentProxyManager.supports_assessment_taken_query

   .. automethod:: AssessmentProxyManager.supports_assessment_taken_search

   .. automethod:: AssessmentProxyManager.supports_assessment_taken_admin

   .. automethod:: AssessmentProxyManager.supports_assessment_taken_notification

   .. automethod:: AssessmentProxyManager.supports_assessment_taken_bank

   .. automethod:: AssessmentProxyManager.supports_assessment_taken_bank_assignment

   .. automethod:: AssessmentProxyManager.supports_assessment_taken_smart_bank

   .. automethod:: AssessmentProxyManager.supports_bank_lookup

   .. automethod:: AssessmentProxyManager.supports_bank_query

   .. automethod:: AssessmentProxyManager.supports_bank_search

   .. automethod:: AssessmentProxyManager.supports_bank_admin

   .. automethod:: AssessmentProxyManager.supports_bank_notification

   .. automethod:: AssessmentProxyManager.supports_bank_hierarchy

   .. automethod:: AssessmentProxyManager.supports_bank_hierarchy_design

   .. automethod:: AssessmentProxyManager.supports_assessment_authoring

   .. automethod:: AssessmentProxyManager.supports_assessment_batch

   .. autoattribute:: AssessmentProxyManager.item_record_types

   .. automethod:: AssessmentProxyManager.supports_item_record_type

   .. autoattribute:: AssessmentProxyManager.item_search_record_types

   .. automethod:: AssessmentProxyManager.supports_item_search_record_type

   .. autoattribute:: AssessmentProxyManager.assessment_record_types

   .. automethod:: AssessmentProxyManager.supports_assessment_record_type

   .. autoattribute:: AssessmentProxyManager.assessment_search_record_types

   .. automethod:: AssessmentProxyManager.supports_assessment_search_record_type

   .. autoattribute:: AssessmentProxyManager.assessment_offered_record_types

   .. automethod:: AssessmentProxyManager.supports_assessment_offered_record_type

   .. autoattribute:: AssessmentProxyManager.assessment_offered_search_record_types

   .. automethod:: AssessmentProxyManager.supports_assessment_offered_search_record_type

   .. autoattribute:: AssessmentProxyManager.assessment_taken_record_types

   .. automethod:: AssessmentProxyManager.supports_assessment_taken_record_type

   .. autoattribute:: AssessmentProxyManager.assessment_taken_search_record_types

   .. automethod:: AssessmentProxyManager.supports_assessment_taken_search_record_type

   .. autoattribute:: AssessmentProxyManager.assessment_section_record_types

   .. automethod:: AssessmentProxyManager.supports_assessment_section_record_type

   .. autoattribute:: AssessmentProxyManager.bank_record_types

   .. automethod:: AssessmentProxyManager.supports_bank_record_type

   .. autoattribute:: AssessmentProxyManager.bank_search_record_types

   .. automethod:: AssessmentProxyManager.supports_bank_search_record_type



Bank Lookup
___________

   .. automethod:: AssessmentProxyManager.can_lookup_banks

   .. automethod:: AssessmentProxyManager.use_comparative_bank_view

   .. automethod:: AssessmentProxyManager.use_plenary_bank_view

   .. automethod:: AssessmentProxyManager.get_bank

   .. automethod:: AssessmentProxyManager.get_banks_by_ids

   .. automethod:: AssessmentProxyManager.get_banks_by_genus_type

   .. automethod:: AssessmentProxyManager.get_banks_by_parent_genus_type

   .. automethod:: AssessmentProxyManager.get_banks_by_record_type

   .. automethod:: AssessmentProxyManager.get_banks_by_provider

   .. autoattribute:: AssessmentProxyManager.banks



Bank Query
__________

   .. automethod:: AssessmentProxyManager.can_search_banks

   .. autoattribute:: AssessmentProxyManager.bank_query

   .. automethod:: AssessmentProxyManager.get_banks_by_query



Bank Search
___________

   .. autoattribute:: AssessmentProxyManager.bank_search

   .. autoattribute:: AssessmentProxyManager.bank_search_order

   .. automethod:: AssessmentProxyManager.get_banks_by_search

   .. automethod:: AssessmentProxyManager.get_bank_query_from_inspector



Bank Admin
__________

   .. automethod:: AssessmentProxyManager.can_create_banks

   .. automethod:: AssessmentProxyManager.can_create_bank_with_record_types

   .. automethod:: AssessmentProxyManager.get_bank_form_for_create

   .. automethod:: AssessmentProxyManager.create_bank

   .. automethod:: AssessmentProxyManager.can_update_banks

   .. automethod:: AssessmentProxyManager.get_bank_form_for_update

   .. automethod:: AssessmentProxyManager.update_bank

   .. automethod:: AssessmentProxyManager.can_delete_banks

   .. automethod:: AssessmentProxyManager.delete_bank

   .. automethod:: AssessmentProxyManager.can_manage_bank_aliases

   .. automethod:: AssessmentProxyManager.alias_bank



Bank Notification
_________________

   .. automethod:: AssessmentProxyManager.can_register_for_bank_notifications

   .. automethod:: AssessmentProxyManager.reliable_bank_notifications

   .. automethod:: AssessmentProxyManager.unreliable_bank_notifications

   .. automethod:: AssessmentProxyManager.acknowledge_bank_notification

   .. automethod:: AssessmentProxyManager.register_for_new_banks

   .. automethod:: AssessmentProxyManager.register_for_changed_banks

   .. automethod:: AssessmentProxyManager.register_for_changed_bank

   .. automethod:: AssessmentProxyManager.register_for_deleted_banks

   .. automethod:: AssessmentProxyManager.register_for_deleted_bank

   .. automethod:: AssessmentProxyManager.register_for_changed_bank_hierarchy

   .. automethod:: AssessmentProxyManager.register_for_changed_bank_hierarchy_for_ancestors

   .. automethod:: AssessmentProxyManager.register_for_changed_bank_hierarchy_for_descendants



Bank Hierarchy
______________

   .. autoattribute:: AssessmentProxyManager.bank_hierarchy_id

   .. autoattribute:: AssessmentProxyManager.bank_hierarchy

   .. automethod:: AssessmentProxyManager.can_access_bank_hierarchy

   .. automethod:: AssessmentProxyManager.use_comparative_bank_view

   .. automethod:: AssessmentProxyManager.use_plenary_bank_view

   .. autoattribute:: AssessmentProxyManager.root_bank_ids

   .. autoattribute:: AssessmentProxyManager.root_banks

   .. automethod:: AssessmentProxyManager.has_parent_banks

   .. automethod:: AssessmentProxyManager.is_parent_of_bank

   .. automethod:: AssessmentProxyManager.get_parent_bank_ids

   .. automethod:: AssessmentProxyManager.get_parent_banks

   .. automethod:: AssessmentProxyManager.is_ancestor_of_bank

   .. automethod:: AssessmentProxyManager.has_child_banks

   .. automethod:: AssessmentProxyManager.is_child_of_bank

   .. automethod:: AssessmentProxyManager.get_child_bank_ids

   .. automethod:: AssessmentProxyManager.get_child_banks

   .. automethod:: AssessmentProxyManager.is_descendant_of_bank

   .. automethod:: AssessmentProxyManager.get_bank_node_ids

   .. automethod:: AssessmentProxyManager.get_bank_nodes



Bank Hierarchy Design
_____________________

   .. autoattribute:: AssessmentProxyManager.bank_hierarchy_id

   .. autoattribute:: AssessmentProxyManager.bank_hierarchy

   .. automethod:: AssessmentProxyManager.can_modify_bank_hierarchy

   .. automethod:: AssessmentProxyManager.add_root_bank

   .. automethod:: AssessmentProxyManager.remove_root_bank

   .. automethod:: AssessmentProxyManager.add_child_bank

   .. automethod:: AssessmentProxyManager.remove_child_bank

   .. automethod:: AssessmentProxyManager.remove_child_banks



