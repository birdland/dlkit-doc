.. currentmodule:: dlkit.services.authorization
.. automodule:: dlkit.services.authorization

Services
========


Authorization Manager
---------------------

.. autoclass:: AuthorizationManager
   :show-inheritance:

.. autoattribute:: AuthorizationManager.authorization_batch_manager

.. autoattribute:: AuthorizationManager.authorization_rules_manager



Authorization Profile Methods
_____________________

.. automethod:: AuthorizationManager.supports_visible_federation

.. automethod:: AuthorizationManager.supports_authorization

.. automethod:: AuthorizationManager.supports_authorization_lookup

.. automethod:: AuthorizationManager.supports_authorization_query

.. automethod:: AuthorizationManager.supports_authorization_search

.. automethod:: AuthorizationManager.supports_authorization_admin

.. automethod:: AuthorizationManager.supports_authorization_notification

.. automethod:: AuthorizationManager.supports_authorization_vault

.. automethod:: AuthorizationManager.supports_authorization_vault_assignment

.. automethod:: AuthorizationManager.supports_authorization_smart_vault

.. automethod:: AuthorizationManager.supports_function_lookup

.. automethod:: AuthorizationManager.supports_function_query

.. automethod:: AuthorizationManager.supports_function_search

.. automethod:: AuthorizationManager.supports_function_admin

.. automethod:: AuthorizationManager.supports_function_notification

.. automethod:: AuthorizationManager.supports_function_vault

.. automethod:: AuthorizationManager.supports_function_vault_assignment

.. automethod:: AuthorizationManager.supports_function_smart_vault

.. automethod:: AuthorizationManager.supports_qualifier_lookup

.. automethod:: AuthorizationManager.supports_qualifier_query

.. automethod:: AuthorizationManager.supports_qualifier_search

.. automethod:: AuthorizationManager.supports_qualifier_admin

.. automethod:: AuthorizationManager.supports_qualifier_notification

.. automethod:: AuthorizationManager.supports_qualifier_hierarchy

.. automethod:: AuthorizationManager.supports_qualifier_hierarchy_design

.. automethod:: AuthorizationManager.supports_qualifier_vault

.. automethod:: AuthorizationManager.supports_qualifier_vault_assignment

.. automethod:: AuthorizationManager.supports_qualifier_smart_vault

.. automethod:: AuthorizationManager.supports_vault_lookup

.. automethod:: AuthorizationManager.supports_vault_query

.. automethod:: AuthorizationManager.supports_vault_search

.. automethod:: AuthorizationManager.supports_vault_admin

.. automethod:: AuthorizationManager.supports_vault_notification

.. automethod:: AuthorizationManager.supports_vault_hierarchy

.. automethod:: AuthorizationManager.supports_vault_hierarchy_design

.. automethod:: AuthorizationManager.supports_authorizatin_batch

.. automethod:: AuthorizationManager.supports_authorizatin_rules

.. autoattribute:: AuthorizationManager.authorization_record_types

.. automethod:: AuthorizationManager.supports_authorization_record_type

.. autoattribute:: AuthorizationManager.authorization_search_record_types

.. automethod:: AuthorizationManager.supports_authorization_search_record_type

.. autoattribute:: AuthorizationManager.function_record_types

.. automethod:: AuthorizationManager.supports_function_record_type

.. autoattribute:: AuthorizationManager.function_search_record_types

.. automethod:: AuthorizationManager.supports_function_search_record_type

.. autoattribute:: AuthorizationManager.qualifier_record_types

.. automethod:: AuthorizationManager.supports_qualifier_record_type

.. autoattribute:: AuthorizationManager.qualifier_search_record_types

.. automethod:: AuthorizationManager.supports_qualifier_search_record_type

.. autoattribute:: AuthorizationManager.vault_record_types

.. automethod:: AuthorizationManager.supports_vault_record_type

.. autoattribute:: AuthorizationManager.vault_search_record_types

.. automethod:: AuthorizationManager.supports_vault_search_record_type

.. autoattribute:: AuthorizationManager.authorization_condition_record_types

.. automethod:: AuthorizationManager.supports_authorization_condition_record_type



Vault Lookup
____________

.. automethod:: AuthorizationManager.can_lookup_vaults

.. automethod:: AuthorizationManager.use_comparative_vault_view

.. automethod:: AuthorizationManager.use_plenary_vault_view

.. automethod:: AuthorizationManager.get_vault

.. automethod:: AuthorizationManager.get_vaults_by_ids

.. automethod:: AuthorizationManager.get_vaults_by_genus_type

.. automethod:: AuthorizationManager.get_vaults_by_parent_genus_type

.. automethod:: AuthorizationManager.get_vaults_by_record_type

.. automethod:: AuthorizationManager.get_vaults_by_provider

.. autoattribute:: AuthorizationManager.vaults



Vault Query
___________

.. automethod:: AuthorizationManager.can_search_vaults

.. autoattribute:: AuthorizationManager.vault_query

.. automethod:: AuthorizationManager.get_vaults_by_query



Vault Search
____________

.. autoattribute:: AuthorizationManager.vault_search

.. autoattribute:: AuthorizationManager.vault_search_order

.. automethod:: AuthorizationManager.get_vaults_by_search

.. automethod:: AuthorizationManager.get_vault_query_from_inspector



Vault Admin
___________

.. automethod:: AuthorizationManager.can_create_vaults

.. automethod:: AuthorizationManager.can_create_vault_with_record_types

.. automethod:: AuthorizationManager.get_vault_form_for_create

.. automethod:: AuthorizationManager.create_vault

.. automethod:: AuthorizationManager.can_update_vaults

.. automethod:: AuthorizationManager.get_vault_form_for_update

.. automethod:: AuthorizationManager.update_vault

.. automethod:: AuthorizationManager.can_delete_vaults

.. automethod:: AuthorizationManager.delete_vault

.. automethod:: AuthorizationManager.can_manage_vault_aliases

.. automethod:: AuthorizationManager.alias_vault



Vault Notification
__________________

.. automethod:: AuthorizationManager.can_register_for_vault_notifications

.. automethod:: AuthorizationManager.register_for_new_vaults

.. automethod:: AuthorizationManager.register_for_new_vault_ancestors

.. automethod:: AuthorizationManager.register_for_new_vault_descendants

.. automethod:: AuthorizationManager.register_for_changed_vaults

.. automethod:: AuthorizationManager.register_for_changed_vault

.. automethod:: AuthorizationManager.register_for_deleted_vaults

.. automethod:: AuthorizationManager.register_for_deleted_vault

.. automethod:: AuthorizationManager.register_for_deleted_vault_ancestors

.. automethod:: AuthorizationManager.register_for_deleted_vault_descendants



Vault Hierarchy
_______________

.. autoattribute:: AuthorizationManager.vault_hierarchy_id

.. autoattribute:: AuthorizationManager.vault_hierarchy

.. automethod:: AuthorizationManager.can_access_vault_hierarchy

.. automethod:: AuthorizationManager.use_comparative_vault_view

.. automethod:: AuthorizationManager.use_plenary_vault_view

.. autoattribute:: AuthorizationManager.root_vault_ids

.. autoattribute:: AuthorizationManager.root_vaults

.. automethod:: AuthorizationManager.has_parent_vaults

.. automethod:: AuthorizationManager.is_parent_of_vault

.. automethod:: AuthorizationManager.get_parent_vault_ids

.. automethod:: AuthorizationManager.get_parent_vaults

.. automethod:: AuthorizationManager.is_ancestor_of_vault

.. automethod:: AuthorizationManager.has_child_vaults

.. automethod:: AuthorizationManager.is_child_of_vault

.. automethod:: AuthorizationManager.get_child_vault_ids

.. automethod:: AuthorizationManager.get_child_vaults

.. automethod:: AuthorizationManager.is_descendant_of_vault

.. automethod:: AuthorizationManager.get_vault_node_ids

.. automethod:: AuthorizationManager.get_vault_nodes



Vault Hierarchy Design
______________________

.. autoattribute:: AuthorizationManager.vault_hierarchy_id

.. autoattribute:: AuthorizationManager.vault_hierarchy

.. automethod:: AuthorizationManager.can_modify_vault_hierarchy

.. automethod:: AuthorizationManager.add_root_vault

.. automethod:: AuthorizationManager.remove_root_vault

.. automethod:: AuthorizationManager.add_child_vault

.. automethod:: AuthorizationManager.remove_child_vault

.. automethod:: AuthorizationManager.remove_child_vaults



Authorization Proxy Manager
---------------------------

.. autoclass:: AuthorizationProxyManager
   :show-inheritance:

.. automethod:: AuthorizationProxyManager.get_authorization_session

.. automethod:: AuthorizationProxyManager.get_authorization_session_for_vault

.. automethod:: AuthorizationProxyManager.get_authorization_lookup_session

.. automethod:: AuthorizationProxyManager.get_authorization_lookup_session_for_vault

.. automethod:: AuthorizationProxyManager.get_authorization_query_session

.. automethod:: AuthorizationProxyManager.get_authorization_query_session_for_vault

.. automethod:: AuthorizationProxyManager.get_authorization_search_session

.. automethod:: AuthorizationProxyManager.get_authorization_search_session_for_vault

.. automethod:: AuthorizationProxyManager.get_authorization_admin_session

.. automethod:: AuthorizationProxyManager.get_authorization_admin_session_for_vault

.. automethod:: AuthorizationProxyManager.get_authorization_notification_session

.. automethod:: AuthorizationProxyManager.get_authorization_notification_session_for_vault

.. automethod:: AuthorizationProxyManager.get_authorization_vault_session

.. automethod:: AuthorizationProxyManager.get_authorization_vault_assignment_session

.. automethod:: AuthorizationProxyManager.get_authorization_smart_vault_session

.. automethod:: AuthorizationProxyManager.get_function_lookup_session

.. automethod:: AuthorizationProxyManager.get_function_lookup_session_for_vault

.. automethod:: AuthorizationProxyManager.get_function_query_session

.. automethod:: AuthorizationProxyManager.get_function_query_session_for_vault

.. automethod:: AuthorizationProxyManager.get_function_search_session

.. automethod:: AuthorizationProxyManager.get_function_search_session_for_vault

.. automethod:: AuthorizationProxyManager.get_function_admin_session

.. automethod:: AuthorizationProxyManager.get_function_admin_session_for_vault

.. automethod:: AuthorizationProxyManager.get_function_notification_session

.. automethod:: AuthorizationProxyManager.get_function_notification_session_for_vault

.. automethod:: AuthorizationProxyManager.get_function_vault_session

.. automethod:: AuthorizationProxyManager.get_function_vault_assignment_session

.. automethod:: AuthorizationProxyManager.get_function_smart_vault_session

.. automethod:: AuthorizationProxyManager.get_qualifier_lookup_session

.. automethod:: AuthorizationProxyManager.get_qualifier_lookup_session_for_vault

.. automethod:: AuthorizationProxyManager.get_qualifier_query_session

.. automethod:: AuthorizationProxyManager.get_qualifier_query_session_for_vault

.. automethod:: AuthorizationProxyManager.get_qualifier_search_session

.. automethod:: AuthorizationProxyManager.get_qualifier_search_session_for_vault

.. automethod:: AuthorizationProxyManager.get_qualifier_admin_session

.. automethod:: AuthorizationProxyManager.get_qualifier_admin_session_for_vault

.. automethod:: AuthorizationProxyManager.get_qualifier_notification_session

.. automethod:: AuthorizationProxyManager.get_qualifier_notification_session_for_vault

.. automethod:: AuthorizationProxyManager.get_qualifier_hierarchy_session

.. automethod:: AuthorizationProxyManager.get_qualifier_hierarchy_design_session

.. automethod:: AuthorizationProxyManager.get_qualifier_vault_session

.. automethod:: AuthorizationProxyManager.get_qualifier_vault_assignment_session

.. automethod:: AuthorizationProxyManager.get_qualifier_smart_vault_session

.. automethod:: AuthorizationProxyManager.get_vault_lookup_session

.. automethod:: AuthorizationProxyManager.get_vault_query_session

.. automethod:: AuthorizationProxyManager.get_vault_search_session

.. automethod:: AuthorizationProxyManager.get_vault_admin_session

.. automethod:: AuthorizationProxyManager.get_vault_notification_session

.. automethod:: AuthorizationProxyManager.get_vault_hierarchy_session

.. automethod:: AuthorizationProxyManager.get_vault_hierarchy_design_session

.. autoattribute:: AuthorizationProxyManager.authorization_batch_proxy_manager

.. autoattribute:: AuthorizationProxyManager.authorization_rules_proxy_manager



