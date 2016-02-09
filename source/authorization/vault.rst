
.. currentmodule:: dlkit.services.authorization

Vault
=====


Vault
-----

.. autoclass:: Vault
   :show-inheritance:

   .. automethod:: Vault.get_vault_record



Authorization Methods
---------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_access_authorizations

   .. automethod:: Vault.is_authorized

   .. automethod:: Vault.get_authorization_condition

   .. automethod:: Vault.is_authorized_on_condition



Authorization Lookup Methods
----------------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_lookup_authorizations

   .. automethod:: Vault.use_comparative_authorization_view

   .. automethod:: Vault.use_plenary_authorization_view

   .. automethod:: Vault.use_federated_vault_view

   .. automethod:: Vault.use_isolated_vault_view

   .. automethod:: Vault.use_effective_authorization_view

   .. automethod:: Vault.use_any_effective_authorization_view

   .. automethod:: Vault.use_implicit_authorization_view

   .. automethod:: Vault.use_explicit_authorization_view

   .. automethod:: Vault.get_authorization

   .. automethod:: Vault.get_authorizations_by_ids

   .. automethod:: Vault.get_authorizations_by_genus_type

   .. automethod:: Vault.get_authorizations_by_parent_genus_type

   .. automethod:: Vault.get_authorizations_by_record_type

   .. automethod:: Vault.get_authorizations_on_date

   .. automethod:: Vault.get_authorizations_for_resource

   .. automethod:: Vault.get_authorizations_for_resource_on_date

   .. automethod:: Vault.get_authorizations_for_agent

   .. automethod:: Vault.get_authorizations_for_agent_on_date

   .. automethod:: Vault.get_authorizations_for_function

   .. automethod:: Vault.get_authorizations_for_function_on_date

   .. automethod:: Vault.get_authorizations_for_resource_and_function

   .. automethod:: Vault.get_authorizations_for_resource_and_function_on_date

   .. automethod:: Vault.get_authorizations_for_agent_and_function

   .. automethod:: Vault.get_authorizations_for_agent_and_function_on_date

   .. automethod:: Vault.get_authorizations_by_qualifier

   .. automethod:: Vault.get_explicit_authorization

   .. autoattribute:: Vault.authorizations



Authorization Admin Methods
---------------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_create_authorizations

   .. automethod:: Vault.can_create_authorization_with_record_types

   .. automethod:: Vault.get_authorization_form_for_create_for_agent

   .. automethod:: Vault.get_authorization_form_for_create_for_resource

   .. automethod:: Vault.get_authorization_form_for_create_for_resource_and_trust

   .. automethod:: Vault.create_authorization

   .. automethod:: Vault.can_update_authorizations

   .. automethod:: Vault.get_authorization_form_for_update

   .. automethod:: Vault.update_authorization

   .. automethod:: Vault.can_delete_authorizations

   .. automethod:: Vault.delete_authorization

   .. automethod:: Vault.can_manage_authorization_aliases

   .. automethod:: Vault.alias_authorization



