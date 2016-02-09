
.. currentmodule:: dlkit.services.authorization
.. automodule:: dlkit.services.authorization

Service Managers
================


Authorization Profile
---------------------

.. autoclass:: AuthorizationProfile
   :show-inheritance:

   .. automethod:: AuthorizationProfile.supports_visible_federation

   .. automethod:: AuthorizationProfile.supports_authorization

   .. automethod:: AuthorizationProfile.supports_authorization_lookup

   .. automethod:: AuthorizationProfile.supports_authorization_query

   .. automethod:: AuthorizationProfile.supports_authorization_search

   .. automethod:: AuthorizationProfile.supports_authorization_admin

   .. automethod:: AuthorizationProfile.supports_authorization_notification

   .. automethod:: AuthorizationProfile.supports_authorization_vault

   .. automethod:: AuthorizationProfile.supports_authorization_vault_assignment

   .. automethod:: AuthorizationProfile.supports_authorization_smart_vault

   .. automethod:: AuthorizationProfile.supports_function_lookup

   .. automethod:: AuthorizationProfile.supports_function_query

   .. automethod:: AuthorizationProfile.supports_function_search

   .. automethod:: AuthorizationProfile.supports_function_admin

   .. automethod:: AuthorizationProfile.supports_function_notification

   .. automethod:: AuthorizationProfile.supports_function_vault

   .. automethod:: AuthorizationProfile.supports_function_vault_assignment

   .. automethod:: AuthorizationProfile.supports_function_smart_vault

   .. automethod:: AuthorizationProfile.supports_qualifier_lookup

   .. automethod:: AuthorizationProfile.supports_qualifier_query

   .. automethod:: AuthorizationProfile.supports_qualifier_search

   .. automethod:: AuthorizationProfile.supports_qualifier_admin

   .. automethod:: AuthorizationProfile.supports_qualifier_notification

   .. automethod:: AuthorizationProfile.supports_qualifier_hierarchy

   .. automethod:: AuthorizationProfile.supports_qualifier_hierarchy_design

   .. automethod:: AuthorizationProfile.supports_qualifier_vault

   .. automethod:: AuthorizationProfile.supports_qualifier_vault_assignment

   .. automethod:: AuthorizationProfile.supports_qualifier_smart_vault

   .. automethod:: AuthorizationProfile.supports_vault_lookup

   .. automethod:: AuthorizationProfile.supports_vault_query

   .. automethod:: AuthorizationProfile.supports_vault_search

   .. automethod:: AuthorizationProfile.supports_vault_admin

   .. automethod:: AuthorizationProfile.supports_vault_notification

   .. automethod:: AuthorizationProfile.supports_vault_hierarchy

   .. automethod:: AuthorizationProfile.supports_vault_hierarchy_design

   .. automethod:: AuthorizationProfile.supports_authorizatin_batch

   .. automethod:: AuthorizationProfile.supports_authorizatin_rules

   .. autoattribute:: AuthorizationProfile.authorization_record_types

   .. automethod:: AuthorizationProfile.supports_authorization_record_type

   .. autoattribute:: AuthorizationProfile.authorization_search_record_types

   .. automethod:: AuthorizationProfile.supports_authorization_search_record_type

   .. autoattribute:: AuthorizationProfile.function_record_types

   .. automethod:: AuthorizationProfile.supports_function_record_type

   .. autoattribute:: AuthorizationProfile.function_search_record_types

   .. automethod:: AuthorizationProfile.supports_function_search_record_type

   .. autoattribute:: AuthorizationProfile.qualifier_record_types

   .. automethod:: AuthorizationProfile.supports_qualifier_record_type

   .. autoattribute:: AuthorizationProfile.qualifier_search_record_types

   .. automethod:: AuthorizationProfile.supports_qualifier_search_record_type

   .. autoattribute:: AuthorizationProfile.vault_record_types

   .. automethod:: AuthorizationProfile.supports_vault_record_type

   .. autoattribute:: AuthorizationProfile.vault_search_record_types

   .. automethod:: AuthorizationProfile.supports_vault_search_record_type

   .. autoattribute:: AuthorizationProfile.authorization_condition_record_types

   .. automethod:: AuthorizationProfile.supports_authorization_condition_record_type

Authorization Manager
---------------------

.. autoclass:: AuthorizationManager
   :show-inheritance:

   .. autoattribute:: AuthorizationManager.authorization_batch_manager

   .. autoattribute:: AuthorizationManager.authorization_rules_manager



Vault Lookup Methods
--------------------

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



Vault Admin Methods
-------------------

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



