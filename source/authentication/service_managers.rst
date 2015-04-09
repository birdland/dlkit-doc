Summary
=======
.. currentmodule:: dlkit.services.authentication
.. automodule:: dlkit.services.authentication

Service_Managers
================


Authentication Manager
----------------------

.. autoclass:: AuthenticationManager
   :show-inheritance:

   .. autoattribute:: AuthenticationManager.authentication_batch_manager

   .. autoattribute:: AuthenticationManager.authentication_keys_manager

   .. autoattribute:: AuthenticationManager.authentication_process_manager



Authentication Profile Methods
______________________

   .. automethod:: AuthenticationManager.supports_visible_federation

   .. automethod:: AuthenticationManager.supports_authentication_acquisition

   .. automethod:: AuthenticationManager.supports_authentication_validation

   .. automethod:: AuthenticationManager.supports_agent_lookup

   .. automethod:: AuthenticationManager.supports_agent_query

   .. automethod:: AuthenticationManager.supports_agent_search

   .. automethod:: AuthenticationManager.supports_agent_admin

   .. automethod:: AuthenticationManager.supports_agent_notification

   .. automethod:: AuthenticationManager.supports_agent_agency

   .. automethod:: AuthenticationManager.supports_agent_agency_assignment

   .. automethod:: AuthenticationManager.supports_agent_smart_agency

   .. automethod:: AuthenticationManager.supports_agency_lookup

   .. automethod:: AuthenticationManager.supports_agency_query

   .. automethod:: AuthenticationManager.supports_agency_search

   .. automethod:: AuthenticationManager.supports_agency_admin

   .. automethod:: AuthenticationManager.supports_agency_notification

   .. automethod:: AuthenticationManager.supports_agency_hierarchy

   .. automethod:: AuthenticationManager.supports_agency_hierarchy_design

   .. automethod:: AuthenticationManager.supports_authentication_keys

   .. automethod:: AuthenticationManager.supports_authentication_process

   .. autoattribute:: AuthenticationManager.agent_record_types

   .. automethod:: AuthenticationManager.supports_agent_record_type

   .. autoattribute:: AuthenticationManager.agent_search_record_types

   .. automethod:: AuthenticationManager.supports_agent_search_record_type

   .. autoattribute:: AuthenticationManager.agency_record_types

   .. automethod:: AuthenticationManager.supports_agency_record_type

   .. autoattribute:: AuthenticationManager.agency_search_record_types

   .. automethod:: AuthenticationManager.supports_agency_search_record_type



Agency Lookup
_____________

   .. automethod:: AuthenticationManager.can_lookup_agencies

   .. automethod:: AuthenticationManager.use_comparative_agency_view

   .. automethod:: AuthenticationManager.use_plenary_agency_view

   .. automethod:: AuthenticationManager.get_agency

   .. automethod:: AuthenticationManager.get_agencies_by_ids

   .. automethod:: AuthenticationManager.get_agencies_by_genus_type

   .. automethod:: AuthenticationManager.get_agencies_by_parent_genus_type

   .. automethod:: AuthenticationManager.get_agencies_by_record_type

   .. automethod:: AuthenticationManager.get_agencies_by_provider

   .. autoattribute:: AuthenticationManager.agencies



Agency Query
____________

   .. automethod:: AuthenticationManager.can_search_agencies

   .. autoattribute:: AuthenticationManager.agency_query

   .. automethod:: AuthenticationManager.get_agencies_by_query



Agency Search
_____________

   .. autoattribute:: AuthenticationManager.agency_search

   .. autoattribute:: AuthenticationManager.agency_search_order

   .. automethod:: AuthenticationManager.get_agencies_by_search

   .. automethod:: AuthenticationManager.get_agency_query_from_inspector



Agency Admin
____________

   .. automethod:: AuthenticationManager.can_create_agencies

   .. automethod:: AuthenticationManager.can_create_agency_with_record_types

   .. automethod:: AuthenticationManager.get_agency_form_for_create

   .. automethod:: AuthenticationManager.create_agency

   .. automethod:: AuthenticationManager.can_update_agencies

   .. automethod:: AuthenticationManager.get_agency_form_for_update

   .. automethod:: AuthenticationManager.update_agency

   .. automethod:: AuthenticationManager.can_delete_agencies

   .. automethod:: AuthenticationManager.delete_agency

   .. automethod:: AuthenticationManager.can_manage_agency_aliases

   .. automethod:: AuthenticationManager.alias_agency



Agency Notification
___________________

   .. automethod:: AuthenticationManager.can_register_for_agency_notifications

   .. automethod:: AuthenticationManager.register_for_new_agencies

   .. automethod:: AuthenticationManager.register_for_new_agency_ancestors

   .. automethod:: AuthenticationManager.register_for_new_agency_descendants

   .. automethod:: AuthenticationManager.register_for_changed_agencies

   .. automethod:: AuthenticationManager.register_for_changed_agency

   .. automethod:: AuthenticationManager.register_for_deleted_agencies

   .. automethod:: AuthenticationManager.register_for_deleted_agency

   .. automethod:: AuthenticationManager.register_for_deleted_agency_ancestors

   .. automethod:: AuthenticationManager.register_for_deleted_agency_descendants



Agency Hierarchy
________________

   .. autoattribute:: AuthenticationManager.agency_hierarchy_id

   .. autoattribute:: AuthenticationManager.agency_hierarchy

   .. automethod:: AuthenticationManager.can_access_agency_hierarchy

   .. automethod:: AuthenticationManager.use_comparative_agency_view

   .. automethod:: AuthenticationManager.use_plenary_agency_view

   .. autoattribute:: AuthenticationManager.root_agency_ids

   .. autoattribute:: AuthenticationManager.root_agencies

   .. automethod:: AuthenticationManager.has_parent_agencies

   .. automethod:: AuthenticationManager.is_parent_of_agency

   .. automethod:: AuthenticationManager.get_parent_agency_ids

   .. automethod:: AuthenticationManager.get_parent_agencies

   .. automethod:: AuthenticationManager.is_ancestor_of_agency

   .. automethod:: AuthenticationManager.has_child_agencies

   .. automethod:: AuthenticationManager.is_child_of_agency

   .. automethod:: AuthenticationManager.get_child_agency_ids

   .. automethod:: AuthenticationManager.get_child_agencies

   .. automethod:: AuthenticationManager.is_descendant_of_agency

   .. automethod:: AuthenticationManager.get_agency_node_ids

   .. automethod:: AuthenticationManager.get_agency_nodes



Agency Hierarchy Design
_______________________

   .. autoattribute:: AuthenticationManager.agency_hierarchy_id

   .. autoattribute:: AuthenticationManager.agency_hierarchy

   .. automethod:: AuthenticationManager.can_modify_agency_hierarchy

   .. automethod:: AuthenticationManager.add_root_agency

   .. automethod:: AuthenticationManager.remove_root_agency

   .. automethod:: AuthenticationManager.add_child_agency

   .. automethod:: AuthenticationManager.remove_child_agency

   .. automethod:: AuthenticationManager.remove_child_agencies



Authentication Proxy Manager
----------------------------

.. autoclass:: AuthenticationProxyManager
   :show-inheritance:

   .. autoattribute:: AuthenticationProxyManager.authentication_batch_proxy_manager

   .. autoattribute:: AuthenticationProxyManager.authentication_keys_proxy_manager

   .. autoattribute:: AuthenticationProxyManager.authentication_process_proxy_manager



Authentication Profile Methods
______________________

   .. automethod:: AuthenticationProxyManager.supports_visible_federation

   .. automethod:: AuthenticationProxyManager.supports_authentication_acquisition

   .. automethod:: AuthenticationProxyManager.supports_authentication_validation

   .. automethod:: AuthenticationProxyManager.supports_agent_lookup

   .. automethod:: AuthenticationProxyManager.supports_agent_query

   .. automethod:: AuthenticationProxyManager.supports_agent_search

   .. automethod:: AuthenticationProxyManager.supports_agent_admin

   .. automethod:: AuthenticationProxyManager.supports_agent_notification

   .. automethod:: AuthenticationProxyManager.supports_agent_agency

   .. automethod:: AuthenticationProxyManager.supports_agent_agency_assignment

   .. automethod:: AuthenticationProxyManager.supports_agent_smart_agency

   .. automethod:: AuthenticationProxyManager.supports_agency_lookup

   .. automethod:: AuthenticationProxyManager.supports_agency_query

   .. automethod:: AuthenticationProxyManager.supports_agency_search

   .. automethod:: AuthenticationProxyManager.supports_agency_admin

   .. automethod:: AuthenticationProxyManager.supports_agency_notification

   .. automethod:: AuthenticationProxyManager.supports_agency_hierarchy

   .. automethod:: AuthenticationProxyManager.supports_agency_hierarchy_design

   .. automethod:: AuthenticationProxyManager.supports_authentication_keys

   .. automethod:: AuthenticationProxyManager.supports_authentication_process

   .. autoattribute:: AuthenticationProxyManager.agent_record_types

   .. automethod:: AuthenticationProxyManager.supports_agent_record_type

   .. autoattribute:: AuthenticationProxyManager.agent_search_record_types

   .. automethod:: AuthenticationProxyManager.supports_agent_search_record_type

   .. autoattribute:: AuthenticationProxyManager.agency_record_types

   .. automethod:: AuthenticationProxyManager.supports_agency_record_type

   .. autoattribute:: AuthenticationProxyManager.agency_search_record_types

   .. automethod:: AuthenticationProxyManager.supports_agency_search_record_type



Agency Lookup
_____________

   .. automethod:: AuthenticationProxyManager.can_lookup_agencies

   .. automethod:: AuthenticationProxyManager.use_comparative_agency_view

   .. automethod:: AuthenticationProxyManager.use_plenary_agency_view

   .. automethod:: AuthenticationProxyManager.get_agency

   .. automethod:: AuthenticationProxyManager.get_agencies_by_ids

   .. automethod:: AuthenticationProxyManager.get_agencies_by_genus_type

   .. automethod:: AuthenticationProxyManager.get_agencies_by_parent_genus_type

   .. automethod:: AuthenticationProxyManager.get_agencies_by_record_type

   .. automethod:: AuthenticationProxyManager.get_agencies_by_provider

   .. autoattribute:: AuthenticationProxyManager.agencies



Agency Query
____________

   .. automethod:: AuthenticationProxyManager.can_search_agencies

   .. autoattribute:: AuthenticationProxyManager.agency_query

   .. automethod:: AuthenticationProxyManager.get_agencies_by_query



Agency Search
_____________

   .. autoattribute:: AuthenticationProxyManager.agency_search

   .. autoattribute:: AuthenticationProxyManager.agency_search_order

   .. automethod:: AuthenticationProxyManager.get_agencies_by_search

   .. automethod:: AuthenticationProxyManager.get_agency_query_from_inspector



Agency Admin
____________

   .. automethod:: AuthenticationProxyManager.can_create_agencies

   .. automethod:: AuthenticationProxyManager.can_create_agency_with_record_types

   .. automethod:: AuthenticationProxyManager.get_agency_form_for_create

   .. automethod:: AuthenticationProxyManager.create_agency

   .. automethod:: AuthenticationProxyManager.can_update_agencies

   .. automethod:: AuthenticationProxyManager.get_agency_form_for_update

   .. automethod:: AuthenticationProxyManager.update_agency

   .. automethod:: AuthenticationProxyManager.can_delete_agencies

   .. automethod:: AuthenticationProxyManager.delete_agency

   .. automethod:: AuthenticationProxyManager.can_manage_agency_aliases

   .. automethod:: AuthenticationProxyManager.alias_agency



Agency Notification
___________________

   .. automethod:: AuthenticationProxyManager.can_register_for_agency_notifications

   .. automethod:: AuthenticationProxyManager.register_for_new_agencies

   .. automethod:: AuthenticationProxyManager.register_for_new_agency_ancestors

   .. automethod:: AuthenticationProxyManager.register_for_new_agency_descendants

   .. automethod:: AuthenticationProxyManager.register_for_changed_agencies

   .. automethod:: AuthenticationProxyManager.register_for_changed_agency

   .. automethod:: AuthenticationProxyManager.register_for_deleted_agencies

   .. automethod:: AuthenticationProxyManager.register_for_deleted_agency

   .. automethod:: AuthenticationProxyManager.register_for_deleted_agency_ancestors

   .. automethod:: AuthenticationProxyManager.register_for_deleted_agency_descendants



Agency Hierarchy
________________

   .. autoattribute:: AuthenticationProxyManager.agency_hierarchy_id

   .. autoattribute:: AuthenticationProxyManager.agency_hierarchy

   .. automethod:: AuthenticationProxyManager.can_access_agency_hierarchy

   .. automethod:: AuthenticationProxyManager.use_comparative_agency_view

   .. automethod:: AuthenticationProxyManager.use_plenary_agency_view

   .. autoattribute:: AuthenticationProxyManager.root_agency_ids

   .. autoattribute:: AuthenticationProxyManager.root_agencies

   .. automethod:: AuthenticationProxyManager.has_parent_agencies

   .. automethod:: AuthenticationProxyManager.is_parent_of_agency

   .. automethod:: AuthenticationProxyManager.get_parent_agency_ids

   .. automethod:: AuthenticationProxyManager.get_parent_agencies

   .. automethod:: AuthenticationProxyManager.is_ancestor_of_agency

   .. automethod:: AuthenticationProxyManager.has_child_agencies

   .. automethod:: AuthenticationProxyManager.is_child_of_agency

   .. automethod:: AuthenticationProxyManager.get_child_agency_ids

   .. automethod:: AuthenticationProxyManager.get_child_agencies

   .. automethod:: AuthenticationProxyManager.is_descendant_of_agency

   .. automethod:: AuthenticationProxyManager.get_agency_node_ids

   .. automethod:: AuthenticationProxyManager.get_agency_nodes



Agency Hierarchy Design
_______________________

   .. autoattribute:: AuthenticationProxyManager.agency_hierarchy_id

   .. autoattribute:: AuthenticationProxyManager.agency_hierarchy

   .. automethod:: AuthenticationProxyManager.can_modify_agency_hierarchy

   .. automethod:: AuthenticationProxyManager.add_root_agency

   .. automethod:: AuthenticationProxyManager.remove_root_agency

   .. automethod:: AuthenticationProxyManager.add_child_agency

   .. automethod:: AuthenticationProxyManager.remove_child_agency

   .. automethod:: AuthenticationProxyManager.remove_child_agencies



