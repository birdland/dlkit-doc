Summary
=======
.. currentmodule:: dlkit.services.grading
.. automodule:: dlkit.services.grading

Service Managers
================


Grading Manager
---------------

.. autoclass:: GradingManager
   :show-inheritance:

   .. autoattribute:: GradingManager.grading_batch_manager

   .. autoattribute:: GradingManager.grading_calculation_manager

   .. autoattribute:: GradingManager.grading_transform_manager



Grading Profile Methods
_______________

   .. automethod:: GradingManager.supports_visible_federation

   .. automethod:: GradingManager.supports_grade_system_lookup

   .. automethod:: GradingManager.supports_grade_system_query

   .. automethod:: GradingManager.supports_grade_system_search

   .. automethod:: GradingManager.supports_grade_system_admin

   .. automethod:: GradingManager.supports_grade_system_notification

   .. automethod:: GradingManager.supports_grade_system_gradebook

   .. automethod:: GradingManager.supports_grade_system_gradebook_assignment

   .. automethod:: GradingManager.supports_grade_system_smart_gradebook

   .. automethod:: GradingManager.supports_grade_entry_lookup

   .. automethod:: GradingManager.supports_grade_entry_query

   .. automethod:: GradingManager.supports_grade_entry_search

   .. automethod:: GradingManager.supports_grade_entry_admin

   .. automethod:: GradingManager.supports_grade_entry_notification

   .. automethod:: GradingManager.supports_gradebook_column_lookup

   .. automethod:: GradingManager.supports_gradebook_column_query

   .. automethod:: GradingManager.supports_gradebook_column_search

   .. automethod:: GradingManager.supports_gradebook_column_admin

   .. automethod:: GradingManager.supports_gradebook_column_notification

   .. automethod:: GradingManager.supports_gradebook_column_gradebook

   .. automethod:: GradingManager.supports_gradebook_column_gradebook_assignment

   .. automethod:: GradingManager.supports_gradebook_column_smart_gradebook

   .. automethod:: GradingManager.supports_gradebook_lookup

   .. automethod:: GradingManager.supports_gradebook_query

   .. automethod:: GradingManager.supports_gradebook_search

   .. automethod:: GradingManager.supports_gradebook_admin

   .. automethod:: GradingManager.supports_gradebook_notification

   .. automethod:: GradingManager.supports_gradebook_hierarchy

   .. automethod:: GradingManager.supports_gradebook_hierarchy_design

   .. automethod:: GradingManager.supports_grading_batch

   .. automethod:: GradingManager.supports_grading_calculation

   .. automethod:: GradingManager.supports_grading_transform

   .. autoattribute:: GradingManager.grade_record_types

   .. automethod:: GradingManager.supports_grade_record_type

   .. autoattribute:: GradingManager.grade_system_record_types

   .. automethod:: GradingManager.supports_grade_system_record_type

   .. autoattribute:: GradingManager.grade_system_search_record_types

   .. automethod:: GradingManager.supports_grade_system_search_record_type

   .. autoattribute:: GradingManager.grade_entry_record_types

   .. automethod:: GradingManager.supports_grade_entry_record_type

   .. autoattribute:: GradingManager.grade_entry_search_record_types

   .. automethod:: GradingManager.supports_grade_entry_search_record_type

   .. autoattribute:: GradingManager.gradebook_column_record_types

   .. automethod:: GradingManager.supports_gradebook_column_record_type

   .. autoattribute:: GradingManager.gradebook_column_search_record_types

   .. automethod:: GradingManager.supports_gradebook_column_search_record_type

   .. autoattribute:: GradingManager.gradebook_column_summary_record_types

   .. automethod:: GradingManager.supports_gradebook_column_summary_record_type

   .. autoattribute:: GradingManager.gradebook_record_types

   .. automethod:: GradingManager.supports_gradebook_record_type

   .. autoattribute:: GradingManager.gradebook_search_record_types

   .. automethod:: GradingManager.supports_gradebook_search_record_type



Gradebook Column Lookup
_______________________

   .. autoattribute:: GradingManager.gradebook_id

   .. autoattribute:: GradingManager.gradebook

   .. automethod:: GradingManager.can_lookup_gradebook_columns

   .. automethod:: GradingManager.use_comparative_gradebook_column_view

   .. automethod:: GradingManager.use_plenary_gradebook_column_view

   .. automethod:: GradingManager.use_federated_gradebook_view

   .. automethod:: GradingManager.use_isolated_gradebook_view

   .. automethod:: GradingManager.get_gradebook_column

   .. automethod:: GradingManager.get_gradebook_columns_by_ids

   .. automethod:: GradingManager.get_gradebook_columns_by_genus_type

   .. automethod:: GradingManager.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradingManager.get_gradebook_columns_by_record_type

   .. autoattribute:: GradingManager.gradebook_columns

   .. automethod:: GradingManager.supports_summary

   .. automethod:: GradingManager.get_gradebook_column_summary



Gradebook Column Query
______________________

   .. autoattribute:: GradingManager.gradebook_id

   .. autoattribute:: GradingManager.gradebook

   .. automethod:: GradingManager.can_search_gradebook_columns

   .. automethod:: GradingManager.use_federated_gradebook_view

   .. automethod:: GradingManager.use_isolated_gradebook_view

   .. autoattribute:: GradingManager.gradebook_column_query

   .. automethod:: GradingManager.get_gradebook_columns_by_query



Gradebook Column Search
_______________________

   .. autoattribute:: GradingManager.gradebook_column_search

   .. autoattribute:: GradingManager.gradebook_column_search_order

   .. automethod:: GradingManager.get_gradebook_columns_by_search

   .. automethod:: GradingManager.get_gradebook_column_query_from_inspector



Gradebook Column Admin
______________________

   .. autoattribute:: GradingManager.gradebook_id

   .. autoattribute:: GradingManager.gradebook

   .. automethod:: GradingManager.can_create_gradebook_columns

   .. automethod:: GradingManager.can_create_gradebook_column_with_record_types

   .. automethod:: GradingManager.get_gradebook_column_form_for_create

   .. automethod:: GradingManager.create_gradebook_column

   .. automethod:: GradingManager.can_update_gradebook_columns

   .. automethod:: GradingManager.get_gradebook_column_form_for_update

   .. automethod:: GradingManager.update_gradebook_column

   .. automethod:: GradingManager.sequence_gradebook_columns

   .. automethod:: GradingManager.move_gradebook_column

   .. automethod:: GradingManager.copy_gradebook_column_entries

   .. automethod:: GradingManager.can_delete_gradebook_columns

   .. automethod:: GradingManager.delete_gradebook_column

   .. automethod:: GradingManager.can_manage_gradebook_column_aliases

   .. automethod:: GradingManager.alias_gradebook_column



Gradebook Column Notification
_____________________________

   .. autoattribute:: GradingManager.gradebook_id

   .. autoattribute:: GradingManager.gradebook

   .. automethod:: GradingManager.can_register_for_gradebook_column_notifications

   .. automethod:: GradingManager.use_federated_gradebook_view

   .. automethod:: GradingManager.use_isolated_gradebook_view

   .. automethod:: GradingManager.register_for_new_gradebook_columns

   .. automethod:: GradingManager.register_for_changed_gradebook_columns

   .. automethod:: GradingManager.register_for_changed_gradebook_column

   .. automethod:: GradingManager.register_for_deleted_gradebook_columns

   .. automethod:: GradingManager.register_for_deleted_gradebook_column



Gradebook Column Gradebook
__________________________

   .. automethod:: GradingManager.use_comparative_gradebook_view

   .. automethod:: GradingManager.use_plenary_gradebook_view

   .. automethod:: GradingManager.can_lookup_gradebook_column_gradebook_mappings

   .. automethod:: GradingManager.get_gradebook_column_ids_by_gradebook

   .. automethod:: GradingManager.get_gradebook_columns_by_gradebook

   .. automethod:: GradingManager.get_gradebook_column_ids_by_gradebooks

   .. automethod:: GradingManager.get_gradebook_columns_by_gradebooks

   .. automethod:: GradingManager.get_gradebook_ids_by_gradebook_column

   .. automethod:: GradingManager.get_gradebooks_by_gradebook_column



Gradebook Column Gradebook Assignment
_____________________________________

   .. automethod:: GradingManager.can_assign_gradebook_columns

   .. automethod:: GradingManager.can_assign_gradebook_columns_to_gradebook

   .. automethod:: GradingManager.get_assignable_gradebook_ids

   .. automethod:: GradingManager.get_assignable_gradebook_ids_for_gradebook_column

   .. automethod:: GradingManager.assign_gradebook_column_to_gradebook

   .. automethod:: GradingManager.unassign_gradebook_column_from_gradebook



Gradebook Column Smart Gradebook
________________________________

   .. autoattribute:: GradingManager.gradebook_id

   .. autoattribute:: GradingManager.gradebook

   .. automethod:: GradingManager.can_manage_smart_gradebooks

   .. autoattribute:: GradingManager.gradebook_column_query

   .. autoattribute:: GradingManager.gradebook_column_search_order

   .. automethod:: GradingManager.apply_gradebook_column_query

   .. automethod:: GradingManager.inspect_gradebook_column_query

   .. automethod:: GradingManager.apply_gradebook_column_sequencing

   .. automethod:: GradingManager.get_gradebook_column_query_from_inspector



Gradebook Lookup
________________

   .. automethod:: GradingManager.can_lookup_gradebooks

   .. automethod:: GradingManager.use_comparative_gradebook_view

   .. automethod:: GradingManager.use_plenary_gradebook_view

   .. automethod:: GradingManager.get_gradebook

   .. automethod:: GradingManager.get_gradebooks_by_ids

   .. automethod:: GradingManager.get_gradebooks_by_genus_type

   .. automethod:: GradingManager.get_gradebooks_by_parent_genus_type

   .. automethod:: GradingManager.get_gradebooks_by_record_type

   .. automethod:: GradingManager.get_gradebooks_by_provider

   .. autoattribute:: GradingManager.gradebooks



Gradebook Query
_______________

   .. automethod:: GradingManager.can_search_gradebooks

   .. autoattribute:: GradingManager.gradebook_query

   .. automethod:: GradingManager.get_gradebooks_by_query



Gradebook Search
________________

   .. autoattribute:: GradingManager.gradebook_search

   .. autoattribute:: GradingManager.gradebook_search_order

   .. automethod:: GradingManager.get_gradebooks_by_search

   .. automethod:: GradingManager.get_gradebook_query_from_inspector



Gradebook Admin
_______________

   .. automethod:: GradingManager.can_create_gradebooks

   .. automethod:: GradingManager.can_create_gradebook_with_record_types

   .. automethod:: GradingManager.get_gradebook_form_for_create

   .. automethod:: GradingManager.create_gradebook

   .. automethod:: GradingManager.can_update_gradebooks

   .. automethod:: GradingManager.get_gradebook_form_for_update

   .. automethod:: GradingManager.update_gradebook

   .. automethod:: GradingManager.can_delete_gradebooks

   .. automethod:: GradingManager.delete_gradebook

   .. automethod:: GradingManager.can_manage_gradebook_aliases

   .. automethod:: GradingManager.alias_gradebook



Gradebook Notification
______________________

   .. automethod:: GradingManager.can_register_for_gradebook_notifications

   .. automethod:: GradingManager.register_for_new_gradebooks

   .. automethod:: GradingManager.register_for_new_gradebook_ancestors

   .. automethod:: GradingManager.register_for_new_gradebook_descendants

   .. automethod:: GradingManager.register_for_changed_gradebooks

   .. automethod:: GradingManager.register_for_changed_gradebook

   .. automethod:: GradingManager.register_for_deleted_gradebooks

   .. automethod:: GradingManager.register_for_deleted_gradebook

   .. automethod:: GradingManager.register_for_deleted_gradebook_ancestors

   .. automethod:: GradingManager.register_for_deleted_gradebook_descendants



Gradebook Hierarchy
___________________

   .. autoattribute:: GradingManager.gradebook_hierarchy_id

   .. autoattribute:: GradingManager.gradebook_hierarchy

   .. automethod:: GradingManager.can_access_gradebook_hierarchy

   .. automethod:: GradingManager.use_comparative_gradebook_view

   .. automethod:: GradingManager.use_plenary_gradebook_view

   .. autoattribute:: GradingManager.root_gradebook_ids

   .. autoattribute:: GradingManager.root_gradebooks

   .. automethod:: GradingManager.has_parent_gradebooks

   .. automethod:: GradingManager.is_parent_of_gradebook

   .. automethod:: GradingManager.get_parent_gradebook_ids

   .. automethod:: GradingManager.get_parent_gradebooks

   .. automethod:: GradingManager.is_ancestor_of_gradebook

   .. automethod:: GradingManager.has_child_gradebooks

   .. automethod:: GradingManager.is_child_of_gradebook

   .. automethod:: GradingManager.get_child_gradebook_ids

   .. automethod:: GradingManager.get_child_gradebooks

   .. automethod:: GradingManager.is_descendant_of_gradebook

   .. automethod:: GradingManager.get_gradebook_node_ids

   .. automethod:: GradingManager.get_gradebook_nodes



Gradebook Hierarchy Design
__________________________

   .. autoattribute:: GradingManager.gradebook_hierarchy_id

   .. autoattribute:: GradingManager.gradebook_hierarchy

   .. automethod:: GradingManager.can_modify_gradebook_hierarchy

   .. automethod:: GradingManager.add_root_gradebook

   .. automethod:: GradingManager.remove_root_gradebook

   .. automethod:: GradingManager.add_child_gradebook

   .. automethod:: GradingManager.remove_child_gradebook



Grading Proxy Manager
---------------------

.. autoclass:: GradingProxyManager
   :show-inheritance:

   .. autoattribute:: GradingProxyManager.grading_batch_proxy_manager

   .. autoattribute:: GradingProxyManager.grading_calculation_proxy_manager

   .. autoattribute:: GradingProxyManager.grading_transform_proxy_manager



Grading Profile Methods
_______________

   .. automethod:: GradingProxyManager.supports_visible_federation

   .. automethod:: GradingProxyManager.supports_grade_system_lookup

   .. automethod:: GradingProxyManager.supports_grade_system_query

   .. automethod:: GradingProxyManager.supports_grade_system_search

   .. automethod:: GradingProxyManager.supports_grade_system_admin

   .. automethod:: GradingProxyManager.supports_grade_system_notification

   .. automethod:: GradingProxyManager.supports_grade_system_gradebook

   .. automethod:: GradingProxyManager.supports_grade_system_gradebook_assignment

   .. automethod:: GradingProxyManager.supports_grade_system_smart_gradebook

   .. automethod:: GradingProxyManager.supports_grade_entry_lookup

   .. automethod:: GradingProxyManager.supports_grade_entry_query

   .. automethod:: GradingProxyManager.supports_grade_entry_search

   .. automethod:: GradingProxyManager.supports_grade_entry_admin

   .. automethod:: GradingProxyManager.supports_grade_entry_notification

   .. automethod:: GradingProxyManager.supports_gradebook_column_lookup

   .. automethod:: GradingProxyManager.supports_gradebook_column_query

   .. automethod:: GradingProxyManager.supports_gradebook_column_search

   .. automethod:: GradingProxyManager.supports_gradebook_column_admin

   .. automethod:: GradingProxyManager.supports_gradebook_column_notification

   .. automethod:: GradingProxyManager.supports_gradebook_column_gradebook

   .. automethod:: GradingProxyManager.supports_gradebook_column_gradebook_assignment

   .. automethod:: GradingProxyManager.supports_gradebook_column_smart_gradebook

   .. automethod:: GradingProxyManager.supports_gradebook_lookup

   .. automethod:: GradingProxyManager.supports_gradebook_query

   .. automethod:: GradingProxyManager.supports_gradebook_search

   .. automethod:: GradingProxyManager.supports_gradebook_admin

   .. automethod:: GradingProxyManager.supports_gradebook_notification

   .. automethod:: GradingProxyManager.supports_gradebook_hierarchy

   .. automethod:: GradingProxyManager.supports_gradebook_hierarchy_design

   .. automethod:: GradingProxyManager.supports_grading_batch

   .. automethod:: GradingProxyManager.supports_grading_calculation

   .. automethod:: GradingProxyManager.supports_grading_transform

   .. autoattribute:: GradingProxyManager.grade_record_types

   .. automethod:: GradingProxyManager.supports_grade_record_type

   .. autoattribute:: GradingProxyManager.grade_system_record_types

   .. automethod:: GradingProxyManager.supports_grade_system_record_type

   .. autoattribute:: GradingProxyManager.grade_system_search_record_types

   .. automethod:: GradingProxyManager.supports_grade_system_search_record_type

   .. autoattribute:: GradingProxyManager.grade_entry_record_types

   .. automethod:: GradingProxyManager.supports_grade_entry_record_type

   .. autoattribute:: GradingProxyManager.grade_entry_search_record_types

   .. automethod:: GradingProxyManager.supports_grade_entry_search_record_type

   .. autoattribute:: GradingProxyManager.gradebook_column_record_types

   .. automethod:: GradingProxyManager.supports_gradebook_column_record_type

   .. autoattribute:: GradingProxyManager.gradebook_column_search_record_types

   .. automethod:: GradingProxyManager.supports_gradebook_column_search_record_type

   .. autoattribute:: GradingProxyManager.gradebook_column_summary_record_types

   .. automethod:: GradingProxyManager.supports_gradebook_column_summary_record_type

   .. autoattribute:: GradingProxyManager.gradebook_record_types

   .. automethod:: GradingProxyManager.supports_gradebook_record_type

   .. autoattribute:: GradingProxyManager.gradebook_search_record_types

   .. automethod:: GradingProxyManager.supports_gradebook_search_record_type



Gradebook Column Lookup
_______________________

   .. autoattribute:: GradingProxyManager.gradebook_id

   .. autoattribute:: GradingProxyManager.gradebook

   .. automethod:: GradingProxyManager.can_lookup_gradebook_columns

   .. automethod:: GradingProxyManager.use_comparative_gradebook_column_view

   .. automethod:: GradingProxyManager.use_plenary_gradebook_column_view

   .. automethod:: GradingProxyManager.use_federated_gradebook_view

   .. automethod:: GradingProxyManager.use_isolated_gradebook_view

   .. automethod:: GradingProxyManager.get_gradebook_column

   .. automethod:: GradingProxyManager.get_gradebook_columns_by_ids

   .. automethod:: GradingProxyManager.get_gradebook_columns_by_genus_type

   .. automethod:: GradingProxyManager.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradingProxyManager.get_gradebook_columns_by_record_type

   .. autoattribute:: GradingProxyManager.gradebook_columns

   .. automethod:: GradingProxyManager.supports_summary

   .. automethod:: GradingProxyManager.get_gradebook_column_summary



Gradebook Column Query
______________________

   .. autoattribute:: GradingProxyManager.gradebook_id

   .. autoattribute:: GradingProxyManager.gradebook

   .. automethod:: GradingProxyManager.can_search_gradebook_columns

   .. automethod:: GradingProxyManager.use_federated_gradebook_view

   .. automethod:: GradingProxyManager.use_isolated_gradebook_view

   .. autoattribute:: GradingProxyManager.gradebook_column_query

   .. automethod:: GradingProxyManager.get_gradebook_columns_by_query



Gradebook Column Search
_______________________

   .. autoattribute:: GradingProxyManager.gradebook_column_search

   .. autoattribute:: GradingProxyManager.gradebook_column_search_order

   .. automethod:: GradingProxyManager.get_gradebook_columns_by_search

   .. automethod:: GradingProxyManager.get_gradebook_column_query_from_inspector



Gradebook Column Admin
______________________

   .. autoattribute:: GradingProxyManager.gradebook_id

   .. autoattribute:: GradingProxyManager.gradebook

   .. automethod:: GradingProxyManager.can_create_gradebook_columns

   .. automethod:: GradingProxyManager.can_create_gradebook_column_with_record_types

   .. automethod:: GradingProxyManager.get_gradebook_column_form_for_create

   .. automethod:: GradingProxyManager.create_gradebook_column

   .. automethod:: GradingProxyManager.can_update_gradebook_columns

   .. automethod:: GradingProxyManager.get_gradebook_column_form_for_update

   .. automethod:: GradingProxyManager.update_gradebook_column

   .. automethod:: GradingProxyManager.sequence_gradebook_columns

   .. automethod:: GradingProxyManager.move_gradebook_column

   .. automethod:: GradingProxyManager.copy_gradebook_column_entries

   .. automethod:: GradingProxyManager.can_delete_gradebook_columns

   .. automethod:: GradingProxyManager.delete_gradebook_column

   .. automethod:: GradingProxyManager.can_manage_gradebook_column_aliases

   .. automethod:: GradingProxyManager.alias_gradebook_column



Gradebook Column Notification
_____________________________

   .. autoattribute:: GradingProxyManager.gradebook_id

   .. autoattribute:: GradingProxyManager.gradebook

   .. automethod:: GradingProxyManager.can_register_for_gradebook_column_notifications

   .. automethod:: GradingProxyManager.use_federated_gradebook_view

   .. automethod:: GradingProxyManager.use_isolated_gradebook_view

   .. automethod:: GradingProxyManager.register_for_new_gradebook_columns

   .. automethod:: GradingProxyManager.register_for_changed_gradebook_columns

   .. automethod:: GradingProxyManager.register_for_changed_gradebook_column

   .. automethod:: GradingProxyManager.register_for_deleted_gradebook_columns

   .. automethod:: GradingProxyManager.register_for_deleted_gradebook_column



Gradebook Column Gradebook
__________________________

   .. automethod:: GradingProxyManager.use_comparative_gradebook_view

   .. automethod:: GradingProxyManager.use_plenary_gradebook_view

   .. automethod:: GradingProxyManager.can_lookup_gradebook_column_gradebook_mappings

   .. automethod:: GradingProxyManager.get_gradebook_column_ids_by_gradebook

   .. automethod:: GradingProxyManager.get_gradebook_columns_by_gradebook

   .. automethod:: GradingProxyManager.get_gradebook_column_ids_by_gradebooks

   .. automethod:: GradingProxyManager.get_gradebook_columns_by_gradebooks

   .. automethod:: GradingProxyManager.get_gradebook_ids_by_gradebook_column

   .. automethod:: GradingProxyManager.get_gradebooks_by_gradebook_column



Gradebook Column Gradebook Assignment
_____________________________________

   .. automethod:: GradingProxyManager.can_assign_gradebook_columns

   .. automethod:: GradingProxyManager.can_assign_gradebook_columns_to_gradebook

   .. automethod:: GradingProxyManager.get_assignable_gradebook_ids

   .. automethod:: GradingProxyManager.get_assignable_gradebook_ids_for_gradebook_column

   .. automethod:: GradingProxyManager.assign_gradebook_column_to_gradebook

   .. automethod:: GradingProxyManager.unassign_gradebook_column_from_gradebook



Gradebook Column Smart Gradebook
________________________________

   .. autoattribute:: GradingProxyManager.gradebook_id

   .. autoattribute:: GradingProxyManager.gradebook

   .. automethod:: GradingProxyManager.can_manage_smart_gradebooks

   .. autoattribute:: GradingProxyManager.gradebook_column_query

   .. autoattribute:: GradingProxyManager.gradebook_column_search_order

   .. automethod:: GradingProxyManager.apply_gradebook_column_query

   .. automethod:: GradingProxyManager.inspect_gradebook_column_query

   .. automethod:: GradingProxyManager.apply_gradebook_column_sequencing

   .. automethod:: GradingProxyManager.get_gradebook_column_query_from_inspector



Gradebook Lookup
________________

   .. automethod:: GradingProxyManager.can_lookup_gradebooks

   .. automethod:: GradingProxyManager.use_comparative_gradebook_view

   .. automethod:: GradingProxyManager.use_plenary_gradebook_view

   .. automethod:: GradingProxyManager.get_gradebook

   .. automethod:: GradingProxyManager.get_gradebooks_by_ids

   .. automethod:: GradingProxyManager.get_gradebooks_by_genus_type

   .. automethod:: GradingProxyManager.get_gradebooks_by_parent_genus_type

   .. automethod:: GradingProxyManager.get_gradebooks_by_record_type

   .. automethod:: GradingProxyManager.get_gradebooks_by_provider

   .. autoattribute:: GradingProxyManager.gradebooks



Gradebook Query
_______________

   .. automethod:: GradingProxyManager.can_search_gradebooks

   .. autoattribute:: GradingProxyManager.gradebook_query

   .. automethod:: GradingProxyManager.get_gradebooks_by_query



Gradebook Search
________________

   .. autoattribute:: GradingProxyManager.gradebook_search

   .. autoattribute:: GradingProxyManager.gradebook_search_order

   .. automethod:: GradingProxyManager.get_gradebooks_by_search

   .. automethod:: GradingProxyManager.get_gradebook_query_from_inspector



Gradebook Admin
_______________

   .. automethod:: GradingProxyManager.can_create_gradebooks

   .. automethod:: GradingProxyManager.can_create_gradebook_with_record_types

   .. automethod:: GradingProxyManager.get_gradebook_form_for_create

   .. automethod:: GradingProxyManager.create_gradebook

   .. automethod:: GradingProxyManager.can_update_gradebooks

   .. automethod:: GradingProxyManager.get_gradebook_form_for_update

   .. automethod:: GradingProxyManager.update_gradebook

   .. automethod:: GradingProxyManager.can_delete_gradebooks

   .. automethod:: GradingProxyManager.delete_gradebook

   .. automethod:: GradingProxyManager.can_manage_gradebook_aliases

   .. automethod:: GradingProxyManager.alias_gradebook



Gradebook Notification
______________________

   .. automethod:: GradingProxyManager.can_register_for_gradebook_notifications

   .. automethod:: GradingProxyManager.register_for_new_gradebooks

   .. automethod:: GradingProxyManager.register_for_new_gradebook_ancestors

   .. automethod:: GradingProxyManager.register_for_new_gradebook_descendants

   .. automethod:: GradingProxyManager.register_for_changed_gradebooks

   .. automethod:: GradingProxyManager.register_for_changed_gradebook

   .. automethod:: GradingProxyManager.register_for_deleted_gradebooks

   .. automethod:: GradingProxyManager.register_for_deleted_gradebook

   .. automethod:: GradingProxyManager.register_for_deleted_gradebook_ancestors

   .. automethod:: GradingProxyManager.register_for_deleted_gradebook_descendants



Gradebook Hierarchy
___________________

   .. autoattribute:: GradingProxyManager.gradebook_hierarchy_id

   .. autoattribute:: GradingProxyManager.gradebook_hierarchy

   .. automethod:: GradingProxyManager.can_access_gradebook_hierarchy

   .. automethod:: GradingProxyManager.use_comparative_gradebook_view

   .. automethod:: GradingProxyManager.use_plenary_gradebook_view

   .. autoattribute:: GradingProxyManager.root_gradebook_ids

   .. autoattribute:: GradingProxyManager.root_gradebooks

   .. automethod:: GradingProxyManager.has_parent_gradebooks

   .. automethod:: GradingProxyManager.is_parent_of_gradebook

   .. automethod:: GradingProxyManager.get_parent_gradebook_ids

   .. automethod:: GradingProxyManager.get_parent_gradebooks

   .. automethod:: GradingProxyManager.is_ancestor_of_gradebook

   .. automethod:: GradingProxyManager.has_child_gradebooks

   .. automethod:: GradingProxyManager.is_child_of_gradebook

   .. automethod:: GradingProxyManager.get_child_gradebook_ids

   .. automethod:: GradingProxyManager.get_child_gradebooks

   .. automethod:: GradingProxyManager.is_descendant_of_gradebook

   .. automethod:: GradingProxyManager.get_gradebook_node_ids

   .. automethod:: GradingProxyManager.get_gradebook_nodes



Gradebook Hierarchy Design
__________________________

   .. autoattribute:: GradingProxyManager.gradebook_hierarchy_id

   .. autoattribute:: GradingProxyManager.gradebook_hierarchy

   .. automethod:: GradingProxyManager.can_modify_gradebook_hierarchy

   .. automethod:: GradingProxyManager.add_root_gradebook

   .. automethod:: GradingProxyManager.remove_root_gradebook

   .. automethod:: GradingProxyManager.add_child_gradebook

   .. automethod:: GradingProxyManager.remove_child_gradebook



