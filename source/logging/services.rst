.. currentmodule:: dlkit.services.logging
.. automodule:: dlkit.services.logging

Services
========


Logging Manager
---------------

.. autoclass:: LoggingManager
   :show-inheritance:

.. autoattribute:: LoggingManager.logging_batch_manager



Logging Profile Methods
_______________

.. automethod:: LoggingManager.supports_visible_federation

.. automethod:: LoggingManager.supports_logging

.. automethod:: LoggingManager.supports_log_entry_lookup

.. automethod:: LoggingManager.supports_log_entry_query

.. automethod:: LoggingManager.supports_log_entry_search

.. automethod:: LoggingManager.supports_log_entry_notification

.. automethod:: LoggingManager.supports_log_entry_log

.. automethod:: LoggingManager.supports_log_entry_log_assignment

.. automethod:: LoggingManager.supports_log_entry_smart_log

.. automethod:: LoggingManager.supports_log_lookup

.. automethod:: LoggingManager.supports_log_query

.. automethod:: LoggingManager.supports_log_search

.. automethod:: LoggingManager.supports_log_admin

.. automethod:: LoggingManager.supports_log_notification

.. automethod:: LoggingManager.supports_log_hierarchy

.. automethod:: LoggingManager.supports_log_hierarchy_design

.. automethod:: LoggingManager.supports_logging_batch

.. autoattribute:: LoggingManager.log_entry_record_types

.. automethod:: LoggingManager.supports_log_entry_record_type

.. autoattribute:: LoggingManager.log_entry_search_record_types

.. automethod:: LoggingManager.supports_log_entry_search_record_type

.. autoattribute:: LoggingManager.log_record_types

.. automethod:: LoggingManager.supports_log_record_type

.. autoattribute:: LoggingManager.log_search_record_types

.. automethod:: LoggingManager.supports_log_search_record_type

.. autoattribute:: LoggingManager.priority_types

.. automethod:: LoggingManager.supports_priority_type

.. autoattribute:: LoggingManager.content_types

.. automethod:: LoggingManager.supports_content_type



Logging
_______

.. autoattribute:: LoggingManager.log_id

.. autoattribute:: LoggingManager.log

.. automethod:: LoggingManager.can_log

.. automethod:: LoggingManager.log

.. automethod:: LoggingManager.log_at_priority

.. autoattribute:: LoggingManager.log_entry_form

.. automethod:: LoggingManager.create_log_entry



Log Entry Lookup
________________

.. autoattribute:: LoggingManager.log_id

.. autoattribute:: LoggingManager.log

.. automethod:: LoggingManager.can_read_log

.. automethod:: LoggingManager.use_comparative_log_entry_view

.. automethod:: LoggingManager.use_plenary_log_entry_view

.. automethod:: LoggingManager.use_federated_log_view

.. automethod:: LoggingManager.use_isolated_log_view

.. automethod:: LoggingManager.get_log_entry

.. automethod:: LoggingManager.get_log_entries_by_ids

.. automethod:: LoggingManager.get_log_entries_by_genus_type

.. automethod:: LoggingManager.get_log_entries_by_parent_genus_type

.. automethod:: LoggingManager.get_log_entries_by_record_type

.. automethod:: LoggingManager.get_log_entries_by_priority_type

.. automethod:: LoggingManager.get_log_entries_by_date

.. automethod:: LoggingManager.get_log_entries_by_priority_type_and_date

.. automethod:: LoggingManager.get_log_entries_for_resource

.. automethod:: LoggingManager.get_log_entries_by_date_for_resource

.. automethod:: LoggingManager.get_log_entries_by_priority_type_and_date_for_resource

.. autoattribute:: LoggingManager.log_entries



Log Entry Query
_______________

.. autoattribute:: LoggingManager.log_id

.. autoattribute:: LoggingManager.log

.. automethod:: LoggingManager.can_search_log_entries

.. automethod:: LoggingManager.use_federated_log_view

.. automethod:: LoggingManager.use_isolated_log_view

.. autoattribute:: LoggingManager.log_entry_query

.. automethod:: LoggingManager.get_log_entries_by_query



Log Entry Search
________________

.. autoattribute:: LoggingManager.log_entry_search

.. autoattribute:: LoggingManager.log_entry_search_order

.. automethod:: LoggingManager.get_log_entries_by_search

.. automethod:: LoggingManager.get_log_entry_query_from_inspector



Log Entry Admin
_______________

.. autoattribute:: LoggingManager.log_id

.. autoattribute:: LoggingManager.log

.. automethod:: LoggingManager.can_create_log_entries

.. automethod:: LoggingManager.can_create_log_entry_with_record_types

.. automethod:: LoggingManager.get_log_entry_form_for_create

.. automethod:: LoggingManager.create_log_entry

.. automethod:: LoggingManager.can_update_log_entries

.. automethod:: LoggingManager.get_log_entry_form_for_update

.. automethod:: LoggingManager.update_log_entry

.. automethod:: LoggingManager.can_delete_log_entries

.. automethod:: LoggingManager.delete_log_entry

.. automethod:: LoggingManager.can_manage_log_entry_aliases

.. automethod:: LoggingManager.alias_log_entry



Log Entry Notification
______________________

.. autoattribute:: LoggingManager.log_id

.. autoattribute:: LoggingManager.log

.. automethod:: LoggingManager.can_register_for_log_entry_notifications

.. automethod:: LoggingManager.use_federated_log_view

.. automethod:: LoggingManager.use_isolated_log_view

.. automethod:: LoggingManager.register_for_new_log_entries

.. automethod:: LoggingManager.register_for_new_log_entries_at_priority

.. automethod:: LoggingManager.register_for_new_log_entries_for_resource

.. automethod:: LoggingManager.register_for_changed_log_entries

.. automethod:: LoggingManager.register_for_new_changed_entries_at_priority

.. automethod:: LoggingManager.register_for_new_changed_entries_for_resource

.. automethod:: LoggingManager.register_for_changed_log_entry

.. automethod:: LoggingManager.register_for_deleted_log_entries

.. automethod:: LoggingManager.register_for_deleted_log_entries_at_priority

.. automethod:: LoggingManager.register_for_deleted_log_entries_for_resource

.. automethod:: LoggingManager.register_for_deleted_log_entry



Log Entry Log
_____________

.. automethod:: LoggingManager.use_comparative_log_view

.. automethod:: LoggingManager.use_plenary_log_view

.. automethod:: LoggingManager.can_lookup_log_entry_log_mappings

.. automethod:: LoggingManager.get_log_entry_ids_by_log

.. automethod:: LoggingManager.get_log_entries_by_log

.. automethod:: LoggingManager.get_log_entrie_by_log

.. automethod:: LoggingManager.get_log_ids_by_log_entry

.. automethod:: LoggingManager.get_log_by_log_entry



Log Entry Log Assignment
________________________

.. automethod:: LoggingManager.can_assign_log_entries

.. automethod:: LoggingManager.can_assign_log_entries_to_log

.. automethod:: LoggingManager.get_assignable_log_ids

.. automethod:: LoggingManager.get_assignable_log_ids_for_log_entry

.. automethod:: LoggingManager.assign_log_entry_to_log

.. automethod:: LoggingManager.unassign_log_entry_from_log



Log Entry Smart Log
___________________

.. autoattribute:: LoggingManager.log_id

.. autoattribute:: LoggingManager.log

.. automethod:: LoggingManager.can_manage_smart_log

.. autoattribute:: LoggingManager.log_entry_query

.. autoattribute:: LoggingManager.log_entry_search_order

.. automethod:: LoggingManager.apply_log_entry_query

.. automethod:: LoggingManager.inspect_log_entry_query

.. automethod:: LoggingManager.apply_log_entry_sequencing

.. automethod:: LoggingManager.get_log_entry_query_from_inspector



Log Lookup
__________

.. automethod:: LoggingManager.can_lookup_logs

.. automethod:: LoggingManager.use_comparative_log_view

.. automethod:: LoggingManager.use_plenary_log_view

.. automethod:: LoggingManager.get_log

.. automethod:: LoggingManager.get_logs_by_ids

.. automethod:: LoggingManager.get_logs_by_genus_type

.. automethod:: LoggingManager.get_logs_by_parent_genus_type

.. automethod:: LoggingManager.get_logs_by_record_type

.. automethod:: LoggingManager.get_logs_by_provider

.. autoattribute:: LoggingManager.logs



Log Query
_________

.. automethod:: LoggingManager.can_search_logs

.. autoattribute:: LoggingManager.log_query

.. automethod:: LoggingManager.get_logs_by_query



Log Search
__________

.. autoattribute:: LoggingManager.log_search

.. autoattribute:: LoggingManager.log_search_order

.. automethod:: LoggingManager.get_logs_by_search

.. automethod:: LoggingManager.get_log_query_from_inspector



Log Admin
_________

.. automethod:: LoggingManager.can_create_logs

.. automethod:: LoggingManager.can_create_log_with_record_types

.. automethod:: LoggingManager.get_log_form_for_create

.. automethod:: LoggingManager.create_log

.. automethod:: LoggingManager.can_update_logs

.. automethod:: LoggingManager.get_log_form_for_update

.. automethod:: LoggingManager.update_log

.. automethod:: LoggingManager.can_delete_logs

.. automethod:: LoggingManager.delete_log

.. automethod:: LoggingManager.can_manage_log_aliases

.. automethod:: LoggingManager.alias_log



Log Notification
________________

.. automethod:: LoggingManager.can_register_for_log_notifications

.. automethod:: LoggingManager.register_for_new_logs

.. automethod:: LoggingManager.register_for_new_log_ancestors

.. automethod:: LoggingManager.register_for_new_log_descendants

.. automethod:: LoggingManager.register_for_changed_logs

.. automethod:: LoggingManager.register_for_changed_log

.. automethod:: LoggingManager.register_for_deleted_logs

.. automethod:: LoggingManager.register_for_deleted_log

.. automethod:: LoggingManager.register_for_deleted_log_ancestors

.. automethod:: LoggingManager.register_for_deleted_log_descendants



Log Hierarchy
_____________

.. autoattribute:: LoggingManager.log_hierarchy_id

.. autoattribute:: LoggingManager.log_hierarchy

.. automethod:: LoggingManager.can_access_log_hierarchy

.. automethod:: LoggingManager.use_comparative_log_view

.. automethod:: LoggingManager.use_plenary_log_view

.. autoattribute:: LoggingManager.root_log_ids

.. autoattribute:: LoggingManager.root_logs

.. automethod:: LoggingManager.has_parent_logs

.. automethod:: LoggingManager.is_parent_of_log

.. automethod:: LoggingManager.get_parent_log_ids

.. automethod:: LoggingManager.get_parent_logs

.. automethod:: LoggingManager.is_ancestor_of_log

.. automethod:: LoggingManager.has_child_logs

.. automethod:: LoggingManager.is_child_of_log

.. automethod:: LoggingManager.get_child_log_ids

.. automethod:: LoggingManager.get_child_logs

.. automethod:: LoggingManager.is_descendant_of_log

.. automethod:: LoggingManager.get_log_node_ids

.. automethod:: LoggingManager.get_log_nodes



Log Hierarchy Design
____________________

.. autoattribute:: LoggingManager.log_hierarchy_id

.. autoattribute:: LoggingManager.log_hierarchy

.. automethod:: LoggingManager.can_modify_log_hierarchy

.. automethod:: LoggingManager.add_root_log

.. automethod:: LoggingManager.remove_root_log

.. automethod:: LoggingManager.add_child_log

.. automethod:: LoggingManager.remove_child_log

.. automethod:: LoggingManager.remove_child_logs



Logging Proxy Manager
---------------------

.. autoclass:: LoggingProxyManager
   :show-inheritance:

.. automethod:: LoggingProxyManager.get_logging_session

.. automethod:: LoggingProxyManager.get_logging_session_for_log

.. automethod:: LoggingProxyManager.get_log_entry_lookup_session

.. automethod:: LoggingProxyManager.get_log_entry_lookup_session_for_log

.. automethod:: LoggingProxyManager.get_log_entry_query_session

.. automethod:: LoggingProxyManager.get_log_entry_query_session_for_log

.. automethod:: LoggingProxyManager.get_log_entry_search_session

.. automethod:: LoggingProxyManager.get_log_entry_search_session_for_log

.. automethod:: LoggingProxyManager.get_log_entry_admin_session

.. automethod:: LoggingProxyManager.get_log_entry_admin_session_for_log

.. automethod:: LoggingProxyManager.get_log_entry_notification_session

.. automethod:: LoggingProxyManager.get_log_entry_notification_session_for_log

.. automethod:: LoggingProxyManager.get_log_entry_log_session

.. automethod:: LoggingProxyManager.get_log_entry_log_assignment_session

.. automethod:: LoggingProxyManager.get_log_entry_smart_log_session

.. automethod:: LoggingProxyManager.get_log_lookup_session

.. automethod:: LoggingProxyManager.get_log_query_session

.. automethod:: LoggingProxyManager.get_log_search_session

.. automethod:: LoggingProxyManager.get_log_admin_session

.. automethod:: LoggingProxyManager.get_log_notification_session

.. automethod:: LoggingProxyManager.get_log_hierarchy_session

.. automethod:: LoggingProxyManager.get_log_hierarchy_design_session

.. autoattribute:: LoggingProxyManager.logging_batch_proxy_manager



