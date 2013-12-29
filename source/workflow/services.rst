.. currentmodule:: dlkit_doc.workflow
.. automodule:: dlkit_doc.workflow

Services
========


Workflow Manager
----------------

.. autoclass:: WorkflowManager
   :show-inheritance:

.. autoattribute:: WorkflowManager.workflow_batch_manager

.. autoattribute:: WorkflowManager.workflow_rules_manager



Workflow Profile Methods
________________

.. automethod:: WorkflowManager.supports_visible_federation

.. automethod:: WorkflowManager.supports_process_lookup

.. automethod:: WorkflowManager.supports_process_query

.. automethod:: WorkflowManager.supports_process_search

.. automethod:: WorkflowManager.supports_process_admin

.. automethod:: WorkflowManager.supports_process_notification

.. automethod:: WorkflowManager.supports_process_office

.. automethod:: WorkflowManager.supports_process_office_assignment

.. automethod:: WorkflowManager.supports_process_smart_office

.. automethod:: WorkflowManager.supports_step_lookup

.. automethod:: WorkflowManager.supports_step_query

.. automethod:: WorkflowManager.supports_step_search

.. automethod:: WorkflowManager.supports_step_admin

.. automethod:: WorkflowManager.supports_step_notification

.. automethod:: WorkflowManager.supports_step_office

.. automethod:: WorkflowManager.supports_step_office_assignment

.. automethod:: WorkflowManager.supports_step_smart_office

.. automethod:: WorkflowManager.supports_work_lookup

.. automethod:: WorkflowManager.supports_work_query

.. automethod:: WorkflowManager.supports_work_search

.. automethod:: WorkflowManager.supports_work_admin

.. automethod:: WorkflowManager.supports_work_notification

.. automethod:: WorkflowManager.supports_work_office

.. automethod:: WorkflowManager.supports_work_office_assignment

.. automethod:: WorkflowManager.supports_work_smart_office

.. automethod:: WorkflowManager.supports_workflow

.. automethod:: WorkflowManager.supports_workflow_initiation

.. automethod:: WorkflowManager.supports_workflow_management

.. automethod:: WorkflowManager.supports_manual_workflow

.. automethod:: WorkflowManager.supports_workflow_event_lookup

.. automethod:: WorkflowManager.supports_workflow_event_notification

.. automethod:: WorkflowManager.supports_office_lookup

.. automethod:: WorkflowManager.supports_office_query

.. automethod:: WorkflowManager.supports_office_search

.. automethod:: WorkflowManager.supports_office_admin

.. automethod:: WorkflowManager.supports_office_notification

.. automethod:: WorkflowManager.supports_office_hierarchy

.. automethod:: WorkflowManager.supports_office_hierarchy_design

.. automethod:: WorkflowManager.supports_workflow_batch

.. automethod:: WorkflowManager.supports_workflow_rules

.. autoattribute:: WorkflowManager.process_record_types

.. automethod:: WorkflowManager.supports_process_record_type

.. autoattribute:: WorkflowManager.process_search_record_types

.. automethod:: WorkflowManager.supports_process_search_record_type

.. autoattribute:: WorkflowManager.step_record_types

.. automethod:: WorkflowManager.supports_step_record_type

.. autoattribute:: WorkflowManager.step_search_record_types

.. automethod:: WorkflowManager.supports_step_search_record_type

.. autoattribute:: WorkflowManager.work_record_types

.. automethod:: WorkflowManager.supports_work_record_type

.. autoattribute:: WorkflowManager.work_search_record_types

.. automethod:: WorkflowManager.supports_work_search_record_type

.. autoattribute:: WorkflowManager.workflow_event_record_types

.. automethod:: WorkflowManager.supports_workflow_event_record_type

.. autoattribute:: WorkflowManager.office_record_types

.. automethod:: WorkflowManager.supports_office_record_type

.. autoattribute:: WorkflowManager.office_search_record_types

.. automethod:: WorkflowManager.supports_office_search_record_type



Office Lookup
_____________

.. automethod:: WorkflowManager.can_lookup_offices

.. automethod:: WorkflowManager.use_comparative_office_view

.. automethod:: WorkflowManager.use_plenary_office_view

.. automethod:: WorkflowManager.get_office

.. automethod:: WorkflowManager.get_offices_by_ids

.. automethod:: WorkflowManager.get_offices_by_genus_type

.. automethod:: WorkflowManager.get_offices_by_parent_genus_type

.. automethod:: WorkflowManager.get_offices_by_record_type

.. automethod:: WorkflowManager.get_offices_by_provider

.. autoattribute:: WorkflowManager.offices



Office Query
____________

.. automethod:: WorkflowManager.can_search_offices

.. autoattribute:: WorkflowManager.office_query

.. automethod:: WorkflowManager.get_offices_by_query



Office Search
_____________

.. autoattribute:: WorkflowManager.office_search

.. autoattribute:: WorkflowManager.office_search_order

.. automethod:: WorkflowManager.get_offices_by_search

.. automethod:: WorkflowManager.get_office_query_from_inspector



Office Admin
____________

.. automethod:: WorkflowManager.can_create_offices

.. automethod:: WorkflowManager.can_create_office_with_record_types

.. automethod:: WorkflowManager.get_office_form_for_create

.. automethod:: WorkflowManager.create_office

.. automethod:: WorkflowManager.can_update_offices

.. automethod:: WorkflowManager.get_office_form_for_update

.. automethod:: WorkflowManager.update_office

.. automethod:: WorkflowManager.can_delete_offices

.. automethod:: WorkflowManager.delete_office

.. automethod:: WorkflowManager.can_manage_office_aliases

.. automethod:: WorkflowManager.alias_office



Office Notification
___________________

.. automethod:: WorkflowManager.can_register_for_office_notifications

.. automethod:: WorkflowManager.register_for_new_offices

.. automethod:: WorkflowManager.register_for_new_office_ancestors

.. automethod:: WorkflowManager.register_for_new_office_descendants

.. automethod:: WorkflowManager.register_for_changed_offices

.. automethod:: WorkflowManager.register_for_changed_office

.. automethod:: WorkflowManager.register_for_deleted_offices

.. automethod:: WorkflowManager.register_for_deleted_office

.. automethod:: WorkflowManager.register_for_deleted_office_ancestors

.. automethod:: WorkflowManager.register_for_deleted_office_descendants



Office Hierarchy
________________

.. autoattribute:: WorkflowManager.office_hierarchy_id

.. autoattribute:: WorkflowManager.office_hierarchy

.. automethod:: WorkflowManager.can_access_office_hierarchy

.. automethod:: WorkflowManager.use_comparative_office_view

.. automethod:: WorkflowManager.use_plenary_office_view

.. autoattribute:: WorkflowManager.root_office_ids

.. autoattribute:: WorkflowManager.root_offices

.. automethod:: WorkflowManager.has_parent_offices

.. automethod:: WorkflowManager.is_parent_of_office

.. automethod:: WorkflowManager.get_parent_office_ids

.. automethod:: WorkflowManager.get_parent_offices

.. automethod:: WorkflowManager.is_ancestor_of_office

.. automethod:: WorkflowManager.has_child_offices

.. automethod:: WorkflowManager.is_child_of_office

.. automethod:: WorkflowManager.get_child_office_ids

.. automethod:: WorkflowManager.get_child_offices

.. automethod:: WorkflowManager.is_descendant_of_office

.. automethod:: WorkflowManager.get_office_node_ids

.. automethod:: WorkflowManager.get_office_nodes



Office Hierarchy Design
_______________________

.. autoattribute:: WorkflowManager.office_hierarchy_id

.. autoattribute:: WorkflowManager.office_hierarchy

.. automethod:: WorkflowManager.can_modify_office_hierarchy

.. automethod:: WorkflowManager.add_root_office

.. automethod:: WorkflowManager.remove_root_office

.. automethod:: WorkflowManager.add_child_office

.. automethod:: WorkflowManager.remove_child_office

.. automethod:: WorkflowManager.remove_child_offices



Workflow Proxy Manager
----------------------

.. autoclass:: WorkflowProxyManager
   :show-inheritance:

.. automethod:: WorkflowProxyManager.get_process_lookup_session

.. automethod:: WorkflowProxyManager.get_process_lookup_session_for_office

.. automethod:: WorkflowProxyManager.get_process_query_session

.. automethod:: WorkflowProxyManager.get_process_query_session_for_office

.. automethod:: WorkflowProxyManager.get_process_search_session

.. automethod:: WorkflowProxyManager.get_process_search_session_for_office

.. automethod:: WorkflowProxyManager.get_process_admin_session

.. automethod:: WorkflowProxyManager.get_process_admin_session_for_office

.. automethod:: WorkflowProxyManager.get_process_notification_session

.. automethod:: WorkflowProxyManager.get_process_notification_session_for_office

.. automethod:: WorkflowProxyManager.get_process_office_session

.. automethod:: WorkflowProxyManager.get_process_office_assignment_session

.. automethod:: WorkflowProxyManager.get_process_smart_office_session

.. automethod:: WorkflowProxyManager.get_step_lookup_session

.. automethod:: WorkflowProxyManager.get_step_lookup_session_for_office

.. automethod:: WorkflowProxyManager.get_step_query_session

.. automethod:: WorkflowProxyManager.get_step_query_session_for_office

.. automethod:: WorkflowProxyManager.get_step_search_session

.. automethod:: WorkflowProxyManager.get_step_search_session_for_office

.. automethod:: WorkflowProxyManager.get_step_admin_session

.. automethod:: WorkflowProxyManager.get_step_admin_session_for_office

.. automethod:: WorkflowProxyManager.get_step_notification_session

.. automethod:: WorkflowProxyManager.get_step_notification_session_for_office

.. automethod:: WorkflowProxyManager.get_step_office_session

.. automethod:: WorkflowProxyManager.get_step_office_assignment_session

.. automethod:: WorkflowProxyManager.get_step_smart_office_session

.. automethod:: WorkflowProxyManager.get_work_lookup_session

.. automethod:: WorkflowProxyManager.get_work_lookup_session_for_office

.. automethod:: WorkflowProxyManager.get_work_query_session

.. automethod:: WorkflowProxyManager.get_work_query_session_for_office

.. automethod:: WorkflowProxyManager.get_work_search_session

.. automethod:: WorkflowProxyManager.get_work_search_session_for_office

.. automethod:: WorkflowProxyManager.get_work_admin_session

.. automethod:: WorkflowProxyManager.get_work_admin_session_for_office

.. automethod:: WorkflowProxyManager.get_work_notification_session

.. automethod:: WorkflowProxyManager.get_work_notification_session_for_office

.. automethod:: WorkflowProxyManager.get_work_office_session

.. automethod:: WorkflowProxyManager.get_work_office_assignment_session

.. automethod:: WorkflowProxyManager.get_work_smart_office_session

.. automethod:: WorkflowProxyManager.get_workflow_session

.. automethod:: WorkflowProxyManager.get_workflow_session_for_office

.. automethod:: WorkflowProxyManager.get_workflow_initiation_session

.. automethod:: WorkflowProxyManager.get_workflow_initiation_session_for_office

.. automethod:: WorkflowProxyManager.get_workflow_management_session

.. automethod:: WorkflowProxyManager.get_workflow_management_session_for_office

.. automethod:: WorkflowProxyManager.get_manual_workflow_session

.. automethod:: WorkflowProxyManager.get_manual_workflow_session_for_office

.. automethod:: WorkflowProxyManager.get_workflow_event_lookup_session

.. automethod:: WorkflowProxyManager.get_workflow_event_lookup_session_for_office

.. automethod:: WorkflowProxyManager.get_workflow_event_notification_session

.. automethod:: WorkflowProxyManager.get_workflow_event_notification_session_for_office

.. automethod:: WorkflowProxyManager.get_office_lookup_session

.. automethod:: WorkflowProxyManager.get_office_query_session

.. automethod:: WorkflowProxyManager.get_office_search_session

.. automethod:: WorkflowProxyManager.get_office_admin_session

.. automethod:: WorkflowProxyManager.get_office_notification_session

.. automethod:: WorkflowProxyManager.get_office_hierarchy_session

.. automethod:: WorkflowProxyManager.get_office_hierarchy_design_session

.. autoattribute:: WorkflowProxyManager.workflow_batch_proxy_manager

.. autoattribute:: WorkflowProxyManager.workflow_rules_proxy_manager



