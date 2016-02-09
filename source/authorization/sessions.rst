
.. currentmodule:: dlkit.authorization.sessions
.. automodule:: dlkit.authorization.sessions

Sessions
========


Authorization Session
---------------------

.. autoclass:: AuthorizationSession
   :show-inheritance:

   .. autoattribute:: AuthorizationSession.vault_id

   .. autoattribute:: AuthorizationSession.vault

   .. automethod:: AuthorizationSession.can_access_authorizations

   .. automethod:: AuthorizationSession.is_authorized

   .. automethod:: AuthorizationSession.get_authorization_condition

   .. automethod:: AuthorizationSession.is_authorized_on_condition

Authorization Lookup Session
----------------------------

.. autoclass:: AuthorizationLookupSession
   :show-inheritance:

   .. autoattribute:: AuthorizationLookupSession.vault_id

   .. autoattribute:: AuthorizationLookupSession.vault

   .. automethod:: AuthorizationLookupSession.can_lookup_authorizations

   .. automethod:: AuthorizationLookupSession.use_comparative_authorization_view

   .. automethod:: AuthorizationLookupSession.use_plenary_authorization_view

   .. automethod:: AuthorizationLookupSession.use_federated_vault_view

   .. automethod:: AuthorizationLookupSession.use_isolated_vault_view

   .. automethod:: AuthorizationLookupSession.use_effective_authorization_view

   .. automethod:: AuthorizationLookupSession.use_any_effective_authorization_view

   .. automethod:: AuthorizationLookupSession.use_implicit_authorization_view

   .. automethod:: AuthorizationLookupSession.use_explicit_authorization_view

   .. automethod:: AuthorizationLookupSession.get_authorization

   .. automethod:: AuthorizationLookupSession.get_authorizations_by_ids

   .. automethod:: AuthorizationLookupSession.get_authorizations_by_genus_type

   .. automethod:: AuthorizationLookupSession.get_authorizations_by_parent_genus_type

   .. automethod:: AuthorizationLookupSession.get_authorizations_by_record_type

   .. automethod:: AuthorizationLookupSession.get_authorizations_on_date

   .. automethod:: AuthorizationLookupSession.get_authorizations_for_resource

   .. automethod:: AuthorizationLookupSession.get_authorizations_for_resource_on_date

   .. automethod:: AuthorizationLookupSession.get_authorizations_for_agent

   .. automethod:: AuthorizationLookupSession.get_authorizations_for_agent_on_date

   .. automethod:: AuthorizationLookupSession.get_authorizations_for_function

   .. automethod:: AuthorizationLookupSession.get_authorizations_for_function_on_date

   .. automethod:: AuthorizationLookupSession.get_authorizations_for_resource_and_function

   .. automethod:: AuthorizationLookupSession.get_authorizations_for_resource_and_function_on_date

   .. automethod:: AuthorizationLookupSession.get_authorizations_for_agent_and_function

   .. automethod:: AuthorizationLookupSession.get_authorizations_for_agent_and_function_on_date

   .. automethod:: AuthorizationLookupSession.get_authorizations_by_qualifier

   .. automethod:: AuthorizationLookupSession.get_explicit_authorization

   .. autoattribute:: AuthorizationLookupSession.authorizations

Authorization Admin Session
---------------------------

.. autoclass:: AuthorizationAdminSession
   :show-inheritance:

   .. autoattribute:: AuthorizationAdminSession.vault_id

   .. autoattribute:: AuthorizationAdminSession.vault

   .. automethod:: AuthorizationAdminSession.can_create_authorizations

   .. automethod:: AuthorizationAdminSession.can_create_authorization_with_record_types

   .. automethod:: AuthorizationAdminSession.get_authorization_form_for_create_for_agent

   .. automethod:: AuthorizationAdminSession.get_authorization_form_for_create_for_resource

   .. automethod:: AuthorizationAdminSession.get_authorization_form_for_create_for_resource_and_trust

   .. automethod:: AuthorizationAdminSession.create_authorization

   .. automethod:: AuthorizationAdminSession.can_update_authorizations

   .. automethod:: AuthorizationAdminSession.get_authorization_form_for_update

   .. automethod:: AuthorizationAdminSession.update_authorization

   .. automethod:: AuthorizationAdminSession.can_delete_authorizations

   .. automethod:: AuthorizationAdminSession.delete_authorization

   .. automethod:: AuthorizationAdminSession.can_manage_authorization_aliases

   .. automethod:: AuthorizationAdminSession.alias_authorization

Vault Lookup Session
--------------------

.. autoclass:: VaultLookupSession
   :show-inheritance:

   .. automethod:: VaultLookupSession.can_lookup_vaults

   .. automethod:: VaultLookupSession.use_comparative_vault_view

   .. automethod:: VaultLookupSession.use_plenary_vault_view

   .. automethod:: VaultLookupSession.get_vault

   .. automethod:: VaultLookupSession.get_vaults_by_ids

   .. automethod:: VaultLookupSession.get_vaults_by_genus_type

   .. automethod:: VaultLookupSession.get_vaults_by_parent_genus_type

   .. automethod:: VaultLookupSession.get_vaults_by_record_type

   .. automethod:: VaultLookupSession.get_vaults_by_provider

   .. autoattribute:: VaultLookupSession.vaults

Vault Admin Session
-------------------

.. autoclass:: VaultAdminSession
   :show-inheritance:

   .. automethod:: VaultAdminSession.can_create_vaults

   .. automethod:: VaultAdminSession.can_create_vault_with_record_types

   .. automethod:: VaultAdminSession.get_vault_form_for_create

   .. automethod:: VaultAdminSession.create_vault

   .. automethod:: VaultAdminSession.can_update_vaults

   .. automethod:: VaultAdminSession.get_vault_form_for_update

   .. automethod:: VaultAdminSession.update_vault

   .. automethod:: VaultAdminSession.can_delete_vaults

   .. automethod:: VaultAdminSession.delete_vault

   .. automethod:: VaultAdminSession.can_manage_vault_aliases

   .. automethod:: VaultAdminSession.alias_vault

