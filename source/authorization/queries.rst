
.. currentmodule:: dlkit.authorization.queries
.. automodule:: dlkit.authorization.queries

Queries
=======


Authorization Query
-------------------

.. autoclass:: AuthorizationQuery
   :show-inheritance:

   .. automethod:: AuthorizationQuery.match_explicit_authorizations

   .. autoattribute:: AuthorizationQuery.explicit_authorizations_terms

   .. automethod:: AuthorizationQuery.match_related_authorization_id

   .. autoattribute:: AuthorizationQuery.related_authorization_id_terms

   .. automethod:: AuthorizationQuery.supports_related_authorization_query

   .. automethod:: AuthorizationQuery.get_related_authorization_query

   .. autoattribute:: AuthorizationQuery.related_authorization_terms

   .. automethod:: AuthorizationQuery.match_resource_id

   .. autoattribute:: AuthorizationQuery.resource_id_terms

   .. automethod:: AuthorizationQuery.supports_resource_query

   .. automethod:: AuthorizationQuery.get_resource_query

   .. automethod:: AuthorizationQuery.match_any_resource

   .. autoattribute:: AuthorizationQuery.resource_terms

   .. automethod:: AuthorizationQuery.match_trust_id

   .. automethod:: AuthorizationQuery.match_any_trust_id

   .. autoattribute:: AuthorizationQuery.trust_id_terms

   .. automethod:: AuthorizationQuery.match_agent_id

   .. autoattribute:: AuthorizationQuery.agent_id_terms

   .. automethod:: AuthorizationQuery.supports_agent_query

   .. automethod:: AuthorizationQuery.get_agent_query

   .. automethod:: AuthorizationQuery.match_any_agent

   .. autoattribute:: AuthorizationQuery.agent_terms

   .. automethod:: AuthorizationQuery.match_function_id

   .. autoattribute:: AuthorizationQuery.function_id_terms

   .. automethod:: AuthorizationQuery.supports_function_query

   .. automethod:: AuthorizationQuery.get_function_query

   .. autoattribute:: AuthorizationQuery.function_terms

   .. automethod:: AuthorizationQuery.match_qualifier_id

   .. autoattribute:: AuthorizationQuery.qualifier_id_terms

   .. automethod:: AuthorizationQuery.supports_qualifier_query

   .. automethod:: AuthorizationQuery.get_qualifier_query

   .. autoattribute:: AuthorizationQuery.qualifier_terms

   .. automethod:: AuthorizationQuery.match_vault_id

   .. autoattribute:: AuthorizationQuery.vault_id_terms

   .. automethod:: AuthorizationQuery.supports_vault_query

   .. autoattribute:: AuthorizationQuery.vault_query

   .. autoattribute:: AuthorizationQuery.vault_terms

   .. automethod:: AuthorizationQuery.get_authorization_query_record

Vault Query
-----------

.. autoclass:: VaultQuery
   :show-inheritance:

   .. automethod:: VaultQuery.match_function_id

   .. autoattribute:: VaultQuery.function_id_terms

   .. automethod:: VaultQuery.supports_function_query

   .. autoattribute:: VaultQuery.function_query

   .. automethod:: VaultQuery.match_any_function

   .. autoattribute:: VaultQuery.function_terms

   .. automethod:: VaultQuery.match_qualifier_id

   .. autoattribute:: VaultQuery.qualifier_id_terms

   .. automethod:: VaultQuery.supports_qualifier_query

   .. autoattribute:: VaultQuery.qualifier_query

   .. automethod:: VaultQuery.match_any_qualifier

   .. autoattribute:: VaultQuery.qualifier_terms

   .. automethod:: VaultQuery.match_authorization_id

   .. autoattribute:: VaultQuery.authorization_id_terms

   .. automethod:: VaultQuery.supports_authorization_query

   .. autoattribute:: VaultQuery.authorization_query

   .. automethod:: VaultQuery.match_any_authorization

   .. autoattribute:: VaultQuery.authorization_terms

   .. automethod:: VaultQuery.match_ancestor_vault_id

   .. autoattribute:: VaultQuery.ancestor_vault_id_terms

   .. automethod:: VaultQuery.supports_ancestor_vault_query

   .. autoattribute:: VaultQuery.ancestor_vault_query

   .. automethod:: VaultQuery.match_any_ancestor_vault

   .. autoattribute:: VaultQuery.ancestor_vault_terms

   .. automethod:: VaultQuery.match_descendant_vault_id

   .. autoattribute:: VaultQuery.descendant_vault_id_terms

   .. automethod:: VaultQuery.supports_descendant_vault_query

   .. autoattribute:: VaultQuery.descendant_vault_query

   .. automethod:: VaultQuery.match_any_descendant_vault

   .. autoattribute:: VaultQuery.descendant_vault_terms

   .. automethod:: VaultQuery.get_vault_query_record

