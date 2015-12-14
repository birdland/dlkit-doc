
.. currentmodule:: dlkit.services.assessment
.. automodule:: dlkit.services.assessment

Service Managers
================


Assessment Manager
------------------

.. autoclass:: AssessmentManager
   :show-inheritance:

   .. autoattribute:: AssessmentManager.my_assessment_taken_session

   .. automethod:: AssessmentManager.get_my_assessment_taken_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_session

   .. automethod:: AssessmentManager.get_assessment_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_results_session

   .. automethod:: AssessmentManager.get_assessment_results_session_for_bank

   .. autoattribute:: AssessmentManager.item_lookup_session

   .. automethod:: AssessmentManager.get_item_lookup_session_for_bank

   .. autoattribute:: AssessmentManager.item_query_session

   .. automethod:: AssessmentManager.get_item_query_session_for_bank

   .. autoattribute:: AssessmentManager.item_search_session

   .. automethod:: AssessmentManager.get_item_search_session_for_bank

   .. autoattribute:: AssessmentManager.item_admin_session

   .. automethod:: AssessmentManager.get_item_admin_session_for_bank

   .. automethod:: AssessmentManager.get_item_notification_session

   .. automethod:: AssessmentManager.get_item_notification_session_for_bank

   .. autoattribute:: AssessmentManager.item_bank_session

   .. autoattribute:: AssessmentManager.item_bank_assignment_session

   .. automethod:: AssessmentManager.get_item_smart_bank_session

   .. autoattribute:: AssessmentManager.assessment_lookup_session

   .. automethod:: AssessmentManager.get_assessment_lookup_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_query_session

   .. automethod:: AssessmentManager.get_assessment_query_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_search_session

   .. automethod:: AssessmentManager.get_assessment_search_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_admin_session

   .. automethod:: AssessmentManager.get_assessment_admin_session_for_bank

   .. automethod:: AssessmentManager.get_assessment_notification_session

   .. automethod:: AssessmentManager.get_assessment_notification_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_bank_session

   .. autoattribute:: AssessmentManager.assessment_bank_assignment_session

   .. automethod:: AssessmentManager.get_assessment_smart_bank_session

   .. autoattribute:: AssessmentManager.assessment_basic_authoring_session

   .. automethod:: AssessmentManager.get_assessment_basic_authoring_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_offered_lookup_session

   .. automethod:: AssessmentManager.get_assessment_offered_lookup_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_offered_query_session

   .. automethod:: AssessmentManager.get_assessment_offered_query_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_offered_search_session

   .. automethod:: AssessmentManager.get_assessment_offered_search_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_offered_admin_session

   .. automethod:: AssessmentManager.get_assessment_offered_admin_session_for_bank

   .. automethod:: AssessmentManager.get_assessment_offered_notification_session

   .. automethod:: AssessmentManager.get_assessment_offered_notification_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_offered_bank_session

   .. autoattribute:: AssessmentManager.assessment_offered_bank_assignment_session

   .. automethod:: AssessmentManager.get_assessment_offered_smart_bank_session

   .. autoattribute:: AssessmentManager.assessment_taken_lookup_session

   .. automethod:: AssessmentManager.get_assessment_taken_lookup_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_taken_query_session

   .. automethod:: AssessmentManager.get_assessment_taken_query_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_taken_search_session

   .. automethod:: AssessmentManager.get_assessment_taken_search_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_taken_admin_session

   .. automethod:: AssessmentManager.get_assessment_taken_admin_session_for_bank

   .. automethod:: AssessmentManager.get_assessment_taken_notification_session

   .. automethod:: AssessmentManager.get_assessment_taken_notification_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_taken_bank_session

   .. autoattribute:: AssessmentManager.assessment_taken_bank_assignment_session

   .. automethod:: AssessmentManager.get_assessment_taken_smart_bank_session

   .. autoattribute:: AssessmentManager.bank_lookup_session

   .. autoattribute:: AssessmentManager.bank_query_session

   .. autoattribute:: AssessmentManager.bank_search_session

   .. autoattribute:: AssessmentManager.bank_admin_session

   .. automethod:: AssessmentManager.get_bank_notification_session

   .. autoattribute:: AssessmentManager.bank_hierarchy_session

   .. autoattribute:: AssessmentManager.bank_hierarchy_design_session

   .. autoattribute:: AssessmentManager.assessment_authoring_manager

   .. autoattribute:: AssessmentManager.assessment_batch_manager



Item Bank Methods
-----------------

   .. automethod:: AssessmentManager.can_lookup_item_bank_mappings

   .. automethod:: AssessmentManager.use_comparative_bank_view

   .. automethod:: AssessmentManager.use_plenary_bank_view

   .. automethod:: AssessmentManager.get_item_ids_by_bank

   .. automethod:: AssessmentManager.get_items_by_bank

   .. automethod:: AssessmentManager.get_item_ids_by_banks

   .. automethod:: AssessmentManager.get_items_by_banks

   .. automethod:: AssessmentManager.get_bank_ids_by_item

   .. automethod:: AssessmentManager.get_banks_by_item



Item Bank Assignment Methods
----------------------------

   .. automethod:: AssessmentManager.can_assign_items

   .. automethod:: AssessmentManager.can_assign_items_to_bank

   .. automethod:: AssessmentManager.get_assignable_bank_ids

   .. automethod:: AssessmentManager.get_assignable_bank_ids_for_item

   .. automethod:: AssessmentManager.assign_item_to_bank

   .. automethod:: AssessmentManager.unassign_item_from_bank

   .. automethod:: AssessmentManager.reassign_item_to_billing



Assessment Bank Methods
-----------------------

   .. automethod:: AssessmentManager.can_lookup_assessment_bank_mappings

   .. automethod:: AssessmentManager.use_comparative_bank_view

   .. automethod:: AssessmentManager.use_plenary_bank_view

   .. automethod:: AssessmentManager.get_assessment_ids_by_bank

   .. automethod:: AssessmentManager.get_assessments_by_bank

   .. automethod:: AssessmentManager.get_assessment_ids_by_banks

   .. automethod:: AssessmentManager.get_assessments_by_banks

   .. automethod:: AssessmentManager.get_bank_ids_by_assessment

   .. automethod:: AssessmentManager.get_banks_by_assessment



Assessment Bank Assignment Methods
----------------------------------

   .. automethod:: AssessmentManager.can_assign_assessments

   .. automethod:: AssessmentManager.can_assign_assessments_to_bank

   .. automethod:: AssessmentManager.get_assignable_bank_ids

   .. automethod:: AssessmentManager.get_assignable_bank_ids_for_assessment

   .. automethod:: AssessmentManager.assign_assessment_to_bank

   .. automethod:: AssessmentManager.unassign_assessment_from_bank

   .. automethod:: AssessmentManager.reassign_assessment_to_billing



Assessment Offered Bank Methods
-------------------------------

   .. automethod:: AssessmentManager.can_lookup_assessment_offered_bank_mappings

   .. automethod:: AssessmentManager.use_comparative_bank_view

   .. automethod:: AssessmentManager.use_plenary_bank_view

   .. automethod:: AssessmentManager.get_assessment_offered_ids_by_bank

   .. automethod:: AssessmentManager.get_assessments_offered_by_bank

   .. automethod:: AssessmentManager.get_assessment_offered_ids_by_banks

   .. automethod:: AssessmentManager.get_assessments_offered_by_banks

   .. automethod:: AssessmentManager.get_bank_ids_by_assessment_offered

   .. automethod:: AssessmentManager.get_banks_by_assessment_offered



Assessment Offered Bank Assignment Methods
------------------------------------------

   .. automethod:: AssessmentManager.can_assign_assessments_offered

   .. automethod:: AssessmentManager.can_assign_assessments_offered_to_bank

   .. automethod:: AssessmentManager.get_assignable_bank_ids

   .. automethod:: AssessmentManager.get_assignable_bank_ids_for_assessment_offered

   .. automethod:: AssessmentManager.assign_assessment_offered_to_bank

   .. automethod:: AssessmentManager.unassign_assessment_offered_from_bank

   .. automethod:: AssessmentManager.reassign_assessment_offered_to_billing



Assessment Taken Bank Methods
-----------------------------

   .. automethod:: AssessmentManager.can_lookup_assessment_taken_bank_mappings

   .. automethod:: AssessmentManager.use_comparative_bank_view

   .. automethod:: AssessmentManager.use_plenary_bank_view

   .. automethod:: AssessmentManager.get_assessment_taken_ids_by_bank

   .. automethod:: AssessmentManager.get_assessments_taken_by_bank

   .. automethod:: AssessmentManager.get_assessment_taken_ids_by_banks

   .. automethod:: AssessmentManager.get_assessments_taken_by_banks

   .. automethod:: AssessmentManager.get_bank_ids_by_assessment_taken

   .. automethod:: AssessmentManager.get_banks_by_assessment_taken



Assessment Taken Bank Assignment Methods
----------------------------------------

   .. automethod:: AssessmentManager.can_assign_assessments_taken

   .. automethod:: AssessmentManager.can_assign_assessments_taken_to_bank

   .. automethod:: AssessmentManager.get_assignable_bank_ids

   .. automethod:: AssessmentManager.get_assignable_bank_ids_for_assessment_taken

   .. automethod:: AssessmentManager.assign_assessment_taken_to_bank

   .. automethod:: AssessmentManager.unassign_assessment_taken_from_bank

   .. automethod:: AssessmentManager.reassign_assessment_taken_to_billing



Bank Lookup Methods
-------------------

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



Bank Query Methods
------------------

   .. automethod:: AssessmentManager.can_search_banks

   .. autoattribute:: AssessmentManager.bank_query

   .. automethod:: AssessmentManager.get_banks_by_query



Bank Admin Methods
------------------

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



Bank Hierarchy Methods
----------------------

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



Bank Hierarchy Design Methods
-----------------------------

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

   .. automethod:: AssessmentProxyManager.get_my_assessment_taken_session

   .. automethod:: AssessmentProxyManager.get_my_assessment_taken_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_session

   .. automethod:: AssessmentProxyManager.get_assessment_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_results_session

   .. automethod:: AssessmentProxyManager.get_assessment_results_session_for_bank

   .. automethod:: AssessmentProxyManager.get_item_lookup_session

   .. automethod:: AssessmentProxyManager.get_item_lookup_session_for_bank

   .. automethod:: AssessmentProxyManager.get_item_query_session

   .. automethod:: AssessmentProxyManager.get_item_query_session_for_bank

   .. automethod:: AssessmentProxyManager.get_item_search_session

   .. automethod:: AssessmentProxyManager.get_item_search_session_for_bank

   .. automethod:: AssessmentProxyManager.get_item_admin_session

   .. automethod:: AssessmentProxyManager.get_item_admin_session_for_bank

   .. automethod:: AssessmentProxyManager.get_item_notification_session

   .. automethod:: AssessmentProxyManager.get_item_notification_session_for_bank

   .. automethod:: AssessmentProxyManager.get_item_bank_session

   .. automethod:: AssessmentProxyManager.get_item_bank_assignment_session

   .. automethod:: AssessmentProxyManager.get_item_smart_bank_session

   .. automethod:: AssessmentProxyManager.get_assessment_lookup_session

   .. automethod:: AssessmentProxyManager.get_assessment_lookup_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_query_session

   .. automethod:: AssessmentProxyManager.get_assessment_query_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_search_session

   .. automethod:: AssessmentProxyManager.get_assessment_search_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_admin_session

   .. automethod:: AssessmentProxyManager.get_assessment_admin_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_notification_session

   .. automethod:: AssessmentProxyManager.get_assessment_notification_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_bank_session

   .. automethod:: AssessmentProxyManager.get_assessment_bank_assignment_session

   .. automethod:: AssessmentProxyManager.get_assessment_smart_bank_session

   .. automethod:: AssessmentProxyManager.get_assessment_basic_authoring_session

   .. automethod:: AssessmentProxyManager.get_assessment_basic_authoring_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_offered_lookup_session

   .. automethod:: AssessmentProxyManager.get_assessment_offered_lookup_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_offered_query_session

   .. automethod:: AssessmentProxyManager.get_assessment_offered_query_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_offered_search_session

   .. automethod:: AssessmentProxyManager.get_assessment_offered_search_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_offered_admin_session

   .. automethod:: AssessmentProxyManager.get_assessment_offered_admin_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_offered_notification_session

   .. automethod:: AssessmentProxyManager.get_assessment_offered_notification_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_offered_bank_session

   .. automethod:: AssessmentProxyManager.get_assessment_offered_bank_assignment_session

   .. automethod:: AssessmentProxyManager.get_assessment_offered_smart_bank_session

   .. automethod:: AssessmentProxyManager.get_assessment_taken_lookup_session

   .. automethod:: AssessmentProxyManager.get_assessment_taken_lookup_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_taken_query_session

   .. automethod:: AssessmentProxyManager.get_assessment_taken_query_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_taken_search_session

   .. automethod:: AssessmentProxyManager.get_assessment_taken_search_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_taken_admin_session

   .. automethod:: AssessmentProxyManager.get_assessment_taken_admin_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_taken_notification_session

   .. automethod:: AssessmentProxyManager.get_assessment_taken_notification_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_taken_bank_session

   .. automethod:: AssessmentProxyManager.get_assessment_taken_bank_assignment_session

   .. automethod:: AssessmentProxyManager.get_assessment_taken_smart_bank_session

   .. automethod:: AssessmentProxyManager.get_bank_lookup_session

   .. automethod:: AssessmentProxyManager.get_bank_query_session

   .. automethod:: AssessmentProxyManager.get_bank_search_session

   .. automethod:: AssessmentProxyManager.get_bank_admin_session

   .. automethod:: AssessmentProxyManager.get_bank_notification_session

   .. automethod:: AssessmentProxyManager.get_bank_hierarchy_session

   .. automethod:: AssessmentProxyManager.get_bank_hierarchy_design_session

   .. autoattribute:: AssessmentProxyManager.assessment_authoring_proxy_manager

   .. autoattribute:: AssessmentProxyManager.assessment_batch_proxy_manager



Item Bank Methods
-----------------

   .. automethod:: AssessmentProxyManager.can_lookup_item_bank_mappings

   .. automethod:: AssessmentProxyManager.use_comparative_bank_view

   .. automethod:: AssessmentProxyManager.use_plenary_bank_view

   .. automethod:: AssessmentProxyManager.get_item_ids_by_bank

   .. automethod:: AssessmentProxyManager.get_items_by_bank

   .. automethod:: AssessmentProxyManager.get_item_ids_by_banks

   .. automethod:: AssessmentProxyManager.get_items_by_banks

   .. automethod:: AssessmentProxyManager.get_bank_ids_by_item

   .. automethod:: AssessmentProxyManager.get_banks_by_item



Item Bank Assignment Methods
----------------------------

   .. automethod:: AssessmentProxyManager.can_assign_items

   .. automethod:: AssessmentProxyManager.can_assign_items_to_bank

   .. automethod:: AssessmentProxyManager.get_assignable_bank_ids

   .. automethod:: AssessmentProxyManager.get_assignable_bank_ids_for_item

   .. automethod:: AssessmentProxyManager.assign_item_to_bank

   .. automethod:: AssessmentProxyManager.unassign_item_from_bank

   .. automethod:: AssessmentProxyManager.reassign_item_to_billing



Assessment Bank Methods
-----------------------

   .. automethod:: AssessmentProxyManager.can_lookup_assessment_bank_mappings

   .. automethod:: AssessmentProxyManager.use_comparative_bank_view

   .. automethod:: AssessmentProxyManager.use_plenary_bank_view

   .. automethod:: AssessmentProxyManager.get_assessment_ids_by_bank

   .. automethod:: AssessmentProxyManager.get_assessments_by_bank

   .. automethod:: AssessmentProxyManager.get_assessment_ids_by_banks

   .. automethod:: AssessmentProxyManager.get_assessments_by_banks

   .. automethod:: AssessmentProxyManager.get_bank_ids_by_assessment

   .. automethod:: AssessmentProxyManager.get_banks_by_assessment



Assessment Bank Assignment Methods
----------------------------------

   .. automethod:: AssessmentProxyManager.can_assign_assessments

   .. automethod:: AssessmentProxyManager.can_assign_assessments_to_bank

   .. automethod:: AssessmentProxyManager.get_assignable_bank_ids

   .. automethod:: AssessmentProxyManager.get_assignable_bank_ids_for_assessment

   .. automethod:: AssessmentProxyManager.assign_assessment_to_bank

   .. automethod:: AssessmentProxyManager.unassign_assessment_from_bank

   .. automethod:: AssessmentProxyManager.reassign_assessment_to_billing



Assessment Offered Bank Methods
-------------------------------

   .. automethod:: AssessmentProxyManager.can_lookup_assessment_offered_bank_mappings

   .. automethod:: AssessmentProxyManager.use_comparative_bank_view

   .. automethod:: AssessmentProxyManager.use_plenary_bank_view

   .. automethod:: AssessmentProxyManager.get_assessment_offered_ids_by_bank

   .. automethod:: AssessmentProxyManager.get_assessments_offered_by_bank

   .. automethod:: AssessmentProxyManager.get_assessment_offered_ids_by_banks

   .. automethod:: AssessmentProxyManager.get_assessments_offered_by_banks

   .. automethod:: AssessmentProxyManager.get_bank_ids_by_assessment_offered

   .. automethod:: AssessmentProxyManager.get_banks_by_assessment_offered



Assessment Offered Bank Assignment Methods
------------------------------------------

   .. automethod:: AssessmentProxyManager.can_assign_assessments_offered

   .. automethod:: AssessmentProxyManager.can_assign_assessments_offered_to_bank

   .. automethod:: AssessmentProxyManager.get_assignable_bank_ids

   .. automethod:: AssessmentProxyManager.get_assignable_bank_ids_for_assessment_offered

   .. automethod:: AssessmentProxyManager.assign_assessment_offered_to_bank

   .. automethod:: AssessmentProxyManager.unassign_assessment_offered_from_bank

   .. automethod:: AssessmentProxyManager.reassign_assessment_offered_to_billing



Assessment Taken Bank Methods
-----------------------------

   .. automethod:: AssessmentProxyManager.can_lookup_assessment_taken_bank_mappings

   .. automethod:: AssessmentProxyManager.use_comparative_bank_view

   .. automethod:: AssessmentProxyManager.use_plenary_bank_view

   .. automethod:: AssessmentProxyManager.get_assessment_taken_ids_by_bank

   .. automethod:: AssessmentProxyManager.get_assessments_taken_by_bank

   .. automethod:: AssessmentProxyManager.get_assessment_taken_ids_by_banks

   .. automethod:: AssessmentProxyManager.get_assessments_taken_by_banks

   .. automethod:: AssessmentProxyManager.get_bank_ids_by_assessment_taken

   .. automethod:: AssessmentProxyManager.get_banks_by_assessment_taken



Assessment Taken Bank Assignment Methods
----------------------------------------

   .. automethod:: AssessmentProxyManager.can_assign_assessments_taken

   .. automethod:: AssessmentProxyManager.can_assign_assessments_taken_to_bank

   .. automethod:: AssessmentProxyManager.get_assignable_bank_ids

   .. automethod:: AssessmentProxyManager.get_assignable_bank_ids_for_assessment_taken

   .. automethod:: AssessmentProxyManager.assign_assessment_taken_to_bank

   .. automethod:: AssessmentProxyManager.unassign_assessment_taken_from_bank

   .. automethod:: AssessmentProxyManager.reassign_assessment_taken_to_billing



Bank Lookup Methods
-------------------

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



Bank Query Methods
------------------

   .. automethod:: AssessmentProxyManager.can_search_banks

   .. autoattribute:: AssessmentProxyManager.bank_query

   .. automethod:: AssessmentProxyManager.get_banks_by_query



Bank Admin Methods
------------------

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



Bank Hierarchy Methods
----------------------

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



Bank Hierarchy Design Methods
-----------------------------

   .. autoattribute:: AssessmentProxyManager.bank_hierarchy_id

   .. autoattribute:: AssessmentProxyManager.bank_hierarchy

   .. automethod:: AssessmentProxyManager.can_modify_bank_hierarchy

   .. automethod:: AssessmentProxyManager.add_root_bank

   .. automethod:: AssessmentProxyManager.remove_root_bank

   .. automethod:: AssessmentProxyManager.add_child_bank

   .. automethod:: AssessmentProxyManager.remove_child_bank

   .. automethod:: AssessmentProxyManager.remove_child_banks



