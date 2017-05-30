
.. currentmodule:: dlkit.services.authorization
.. automodule:: dlkit.services.authorization

Service Managers
================


Authorization Profile
---------------------

.. autoclass:: AuthorizationProfile
   :show-inheritance:

   .. automethod:: AuthorizationProfile.supports_authorization

   .. automethod:: AuthorizationProfile.supports_authorization_lookup

   .. automethod:: AuthorizationProfile.supports_authorization_query

   .. automethod:: AuthorizationProfile.supports_authorization_admin

   .. automethod:: AuthorizationProfile.supports_vault_lookup

   .. automethod:: AuthorizationProfile.supports_vault_query

   .. automethod:: AuthorizationProfile.supports_vault_admin

   .. autoattribute:: AuthorizationProfile.authorization_record_types

   .. autoattribute:: AuthorizationProfile.authorization_search_record_types

   .. autoattribute:: AuthorizationProfile.function_record_types

   .. autoattribute:: AuthorizationProfile.function_search_record_types

   .. autoattribute:: AuthorizationProfile.qualifier_record_types

   .. autoattribute:: AuthorizationProfile.qualifier_search_record_types

   .. autoattribute:: AuthorizationProfile.vault_record_types

   .. autoattribute:: AuthorizationProfile.vault_search_record_types

   .. autoattribute:: AuthorizationProfile.authorization_condition_record_types

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



Vault Query Methods
-------------------

   .. automethod:: AuthorizationManager.can_search_vaults

   .. autoattribute:: AuthorizationManager.vault_query

   .. automethod:: AuthorizationManager.get_vaults_by_query



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



