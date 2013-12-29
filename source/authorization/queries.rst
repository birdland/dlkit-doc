.. currentmodule:: dlkit.abstract_osid.authorization.queries
.. automodule:: dlkit.abstract_osid.authorization.queries

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



Function Query
--------------

.. autoclass:: FunctionQuery
   :show-inheritance:

.. automethod:: FunctionQuery.match_qualifier_hierarchy_id

.. autoattribute:: FunctionQuery.qualifier_hierarchy_id_terms

.. automethod:: FunctionQuery.supports_qualifier_hierarchy_query

.. autoattribute:: FunctionQuery.qualifier_hierarchy_query

.. automethod:: FunctionQuery.match_any_qualifier_hierarchy

.. autoattribute:: FunctionQuery.qualifier_hierarchy_terms

.. automethod:: FunctionQuery.match_authorization_id

.. autoattribute:: FunctionQuery.authorization_id_terms

.. automethod:: FunctionQuery.supports_authorization_query

.. autoattribute:: FunctionQuery.authorization_query

.. automethod:: FunctionQuery.match_any_authorization

.. autoattribute:: FunctionQuery.authorization_terms

.. automethod:: FunctionQuery.match_vault_id

.. autoattribute:: FunctionQuery.vault_id_terms

.. automethod:: FunctionQuery.supports_vault_query

.. autoattribute:: FunctionQuery.vault_query

.. autoattribute:: FunctionQuery.vault_terms

.. automethod:: FunctionQuery.get_function_query_record



Qualifier Query
---------------

.. autoclass:: QualifierQuery
   :show-inheritance:

.. automethod:: QualifierQuery.match_qualifier_hierarchy_id

.. autoattribute:: QualifierQuery.qualifier_hierarchy_id_terms

.. automethod:: QualifierQuery.supports_qualifier_hierarchy_query

.. autoattribute:: QualifierQuery.qualifier_hierarchy_query

.. autoattribute:: QualifierQuery.qualifier_hierarchy_terms

.. automethod:: QualifierQuery.match_authorization_id

.. autoattribute:: QualifierQuery.authorization_id_terms

.. automethod:: QualifierQuery.supports_authorization_query

.. autoattribute:: QualifierQuery.authorization_query

.. automethod:: QualifierQuery.match_any_authorization

.. autoattribute:: QualifierQuery.authorization_terms

.. automethod:: QualifierQuery.match_ancestor_qualifier_id

.. autoattribute:: QualifierQuery.ancestor_qualifier_id_terms

.. automethod:: QualifierQuery.supports_ancestor_qualifier_query

.. autoattribute:: QualifierQuery.ancestor_qualifier_query

.. automethod:: QualifierQuery.match_any_ancestor_qualifier

.. autoattribute:: QualifierQuery.ancestor_qualifier_terms

.. automethod:: QualifierQuery.match_descendant_qualifier_id

.. autoattribute:: QualifierQuery.descendant_qualifier_id_terms

.. automethod:: QualifierQuery.supports_descendant_qualifier_query

.. autoattribute:: QualifierQuery.descendant_qualifier_query

.. automethod:: QualifierQuery.match_any_descendant_qualifier

.. autoattribute:: QualifierQuery.descendant_qualifier_terms

.. automethod:: QualifierQuery.match_vault_id

.. autoattribute:: QualifierQuery.vault_id_terms

.. automethod:: QualifierQuery.supports_vault_query

.. autoattribute:: QualifierQuery.vault_query

.. autoattribute:: QualifierQuery.vault_terms

.. automethod:: QualifierQuery.get_qualifier_query_record



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



