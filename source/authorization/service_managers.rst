Summary
=======
.. currentmodule:: dlkit.services.authorization
.. automodule:: dlkit.services.authorization

Service Managers
================


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

   .. autoattribute:: AuthorizationProxyManager.authorization_batch_proxy_manager

   .. autoattribute:: AuthorizationProxyManager.authorization_rules_proxy_manager



Authorization Profile Methods
_____________________

   .. automethod:: AuthorizationProxyManager.supports_visible_federation

   .. automethod:: AuthorizationProxyManager.supports_authorization

   .. automethod:: AuthorizationProxyManager.supports_authorization_lookup

   .. automethod:: AuthorizationProxyManager.supports_authorization_query

   .. automethod:: AuthorizationProxyManager.supports_authorization_search

   .. automethod:: AuthorizationProxyManager.supports_authorization_admin

   .. automethod:: AuthorizationProxyManager.supports_authorization_notification

   .. automethod:: AuthorizationProxyManager.supports_authorization_vault

   .. automethod:: AuthorizationProxyManager.supports_authorization_vault_assignment

   .. automethod:: AuthorizationProxyManager.supports_authorization_smart_vault

   .. automethod:: AuthorizationProxyManager.supports_function_lookup

   .. automethod:: AuthorizationProxyManager.supports_function_query

   .. automethod:: AuthorizationProxyManager.supports_function_search

   .. automethod:: AuthorizationProxyManager.supports_function_admin

   .. automethod:: AuthorizationProxyManager.supports_function_notification

   .. automethod:: AuthorizationProxyManager.supports_function_vault

   .. automethod:: AuthorizationProxyManager.supports_function_vault_assignment

   .. automethod:: AuthorizationProxyManager.supports_function_smart_vault

   .. automethod:: AuthorizationProxyManager.supports_qualifier_lookup

   .. automethod:: AuthorizationProxyManager.supports_qualifier_query

   .. automethod:: AuthorizationProxyManager.supports_qualifier_search

   .. automethod:: AuthorizationProxyManager.supports_qualifier_admin

   .. automethod:: AuthorizationProxyManager.supports_qualifier_notification

   .. automethod:: AuthorizationProxyManager.supports_qualifier_hierarchy

   .. automethod:: AuthorizationProxyManager.supports_qualifier_hierarchy_design

   .. automethod:: AuthorizationProxyManager.supports_qualifier_vault

   .. automethod:: AuthorizationProxyManager.supports_qualifier_vault_assignment

   .. automethod:: AuthorizationProxyManager.supports_qualifier_smart_vault

   .. automethod:: AuthorizationProxyManager.supports_vault_lookup

   .. automethod:: AuthorizationProxyManager.supports_vault_query

   .. automethod:: AuthorizationProxyManager.supports_vault_search

   .. automethod:: AuthorizationProxyManager.supports_vault_admin

   .. automethod:: AuthorizationProxyManager.supports_vault_notification

   .. automethod:: AuthorizationProxyManager.supports_vault_hierarchy

   .. automethod:: AuthorizationProxyManager.supports_vault_hierarchy_design

   .. automethod:: AuthorizationProxyManager.supports_authorizatin_batch

   .. automethod:: AuthorizationProxyManager.supports_authorizatin_rules

   .. autoattribute:: AuthorizationProxyManager.authorization_record_types

   .. automethod:: AuthorizationProxyManager.supports_authorization_record_type

   .. autoattribute:: AuthorizationProxyManager.authorization_search_record_types

   .. automethod:: AuthorizationProxyManager.supports_authorization_search_record_type

   .. autoattribute:: AuthorizationProxyManager.function_record_types

   .. automethod:: AuthorizationProxyManager.supports_function_record_type

   .. autoattribute:: AuthorizationProxyManager.function_search_record_types

   .. automethod:: AuthorizationProxyManager.supports_function_search_record_type

   .. autoattribute:: AuthorizationProxyManager.qualifier_record_types

   .. automethod:: AuthorizationProxyManager.supports_qualifier_record_type

   .. autoattribute:: AuthorizationProxyManager.qualifier_search_record_types

   .. automethod:: AuthorizationProxyManager.supports_qualifier_search_record_type

   .. autoattribute:: AuthorizationProxyManager.vault_record_types

   .. automethod:: AuthorizationProxyManager.supports_vault_record_type

   .. autoattribute:: AuthorizationProxyManager.vault_search_record_types

   .. automethod:: AuthorizationProxyManager.supports_vault_search_record_type

   .. autoattribute:: AuthorizationProxyManager.authorization_condition_record_types

   .. automethod:: AuthorizationProxyManager.supports_authorization_condition_record_type



Vault Lookup
____________

   .. automethod:: AuthorizationProxyManager.can_lookup_vaults

   .. automethod:: AuthorizationProxyManager.use_comparative_vault_view

   .. automethod:: AuthorizationProxyManager.use_plenary_vault_view

   .. automethod:: AuthorizationProxyManager.get_vault

   .. automethod:: AuthorizationProxyManager.get_vaults_by_ids

   .. automethod:: AuthorizationProxyManager.get_vaults_by_genus_type

   .. automethod:: AuthorizationProxyManager.get_vaults_by_parent_genus_type

   .. automethod:: AuthorizationProxyManager.get_vaults_by_record_type

   .. automethod:: AuthorizationProxyManager.get_vaults_by_provider

   .. autoattribute:: AuthorizationProxyManager.vaults



Vault Query
___________

   .. automethod:: AuthorizationProxyManager.can_search_vaults

   .. autoattribute:: AuthorizationProxyManager.vault_query

   .. automethod:: AuthorizationProxyManager.get_vaults_by_query



Vault Search
____________

   .. autoattribute:: AuthorizationProxyManager.vault_search

   .. autoattribute:: AuthorizationProxyManager.vault_search_order

   .. automethod:: AuthorizationProxyManager.get_vaults_by_search

   .. automethod:: AuthorizationProxyManager.get_vault_query_from_inspector



Vault Admin
___________

   .. automethod:: AuthorizationProxyManager.can_create_vaults

   .. automethod:: AuthorizationProxyManager.can_create_vault_with_record_types

   .. automethod:: AuthorizationProxyManager.get_vault_form_for_create

   .. automethod:: AuthorizationProxyManager.create_vault

   .. automethod:: AuthorizationProxyManager.can_update_vaults

   .. automethod:: AuthorizationProxyManager.get_vault_form_for_update

   .. automethod:: AuthorizationProxyManager.update_vault

   .. automethod:: AuthorizationProxyManager.can_delete_vaults

   .. automethod:: AuthorizationProxyManager.delete_vault

   .. automethod:: AuthorizationProxyManager.can_manage_vault_aliases

   .. automethod:: AuthorizationProxyManager.alias_vault



Vault Notification
__________________

   .. automethod:: AuthorizationProxyManager.can_register_for_vault_notifications

   .. automethod:: AuthorizationProxyManager.register_for_new_vaults

   .. automethod:: AuthorizationProxyManager.register_for_new_vault_ancestors

   .. automethod:: AuthorizationProxyManager.register_for_new_vault_descendants

   .. automethod:: AuthorizationProxyManager.register_for_changed_vaults

   .. automethod:: AuthorizationProxyManager.register_for_changed_vault

   .. automethod:: AuthorizationProxyManager.register_for_deleted_vaults

   .. automethod:: AuthorizationProxyManager.register_for_deleted_vault

   .. automethod:: AuthorizationProxyManager.register_for_deleted_vault_ancestors

   .. automethod:: AuthorizationProxyManager.register_for_deleted_vault_descendants



Vault Hierarchy
_______________

   .. autoattribute:: AuthorizationProxyManager.vault_hierarchy_id

   .. autoattribute:: AuthorizationProxyManager.vault_hierarchy

   .. automethod:: AuthorizationProxyManager.can_access_vault_hierarchy

   .. automethod:: AuthorizationProxyManager.use_comparative_vault_view

   .. automethod:: AuthorizationProxyManager.use_plenary_vault_view

   .. autoattribute:: AuthorizationProxyManager.root_vault_ids

   .. autoattribute:: AuthorizationProxyManager.root_vaults

   .. automethod:: AuthorizationProxyManager.has_parent_vaults

   .. automethod:: AuthorizationProxyManager.is_parent_of_vault

   .. automethod:: AuthorizationProxyManager.get_parent_vault_ids

   .. automethod:: AuthorizationProxyManager.get_parent_vaults

   .. automethod:: AuthorizationProxyManager.is_ancestor_of_vault

   .. automethod:: AuthorizationProxyManager.has_child_vaults

   .. automethod:: AuthorizationProxyManager.is_child_of_vault

   .. automethod:: AuthorizationProxyManager.get_child_vault_ids

   .. automethod:: AuthorizationProxyManager.get_child_vaults

   .. automethod:: AuthorizationProxyManager.is_descendant_of_vault

   .. automethod:: AuthorizationProxyManager.get_vault_node_ids

   .. automethod:: AuthorizationProxyManager.get_vault_nodes



Vault Hierarchy Design
______________________

   .. autoattribute:: AuthorizationProxyManager.vault_hierarchy_id

   .. autoattribute:: AuthorizationProxyManager.vault_hierarchy

   .. automethod:: AuthorizationProxyManager.can_modify_vault_hierarchy

   .. automethod:: AuthorizationProxyManager.add_root_vault

   .. automethod:: AuthorizationProxyManager.remove_root_vault

   .. automethod:: AuthorizationProxyManager.add_child_vault

   .. automethod:: AuthorizationProxyManager.remove_child_vault

   .. automethod:: AuthorizationProxyManager.remove_child_vaults



