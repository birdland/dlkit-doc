.. currentmodule:: dlkit.abstract_osid.authorization.query_inspectors
.. automodule:: dlkit.abstract_osid.authorization.query_inspectors

Query_Inspectors
================


Authorization Query Inspector
-----------------------------

.. autoclass:: AuthorizationQueryInspector
   :show-inheritance:

.. autoattribute:: AuthorizationQueryInspector.explicit_authorizations_terms

.. autoattribute:: AuthorizationQueryInspector.related_authorization_id_terms

.. autoattribute:: AuthorizationQueryInspector.related_authorization_terms

.. autoattribute:: AuthorizationQueryInspector.resource_id_terms

.. autoattribute:: AuthorizationQueryInspector.resource_terms

.. autoattribute:: AuthorizationQueryInspector.trust_id_terms

.. autoattribute:: AuthorizationQueryInspector.agent_id_terms

.. autoattribute:: AuthorizationQueryInspector.agent_terms

.. autoattribute:: AuthorizationQueryInspector.function_id_terms

.. autoattribute:: AuthorizationQueryInspector.function_terms

.. autoattribute:: AuthorizationQueryInspector.qualifier_id_terms

.. autoattribute:: AuthorizationQueryInspector.qualifier_terms

.. autoattribute:: AuthorizationQueryInspector.vault_id_terms

.. autoattribute:: AuthorizationQueryInspector.vault_terms

.. automethod:: AuthorizationQueryInspector.get_authorization_query_inspector_record



Function Query Inspector
------------------------

.. autoclass:: FunctionQueryInspector
   :show-inheritance:

.. autoattribute:: FunctionQueryInspector.qualifier_hierarchy_id_terms

.. autoattribute:: FunctionQueryInspector.qualifier_hierarchy_terms

.. autoattribute:: FunctionQueryInspector.authorization_id_terms

.. autoattribute:: FunctionQueryInspector.authorization_terms

.. autoattribute:: FunctionQueryInspector.vault_id_terms

.. autoattribute:: FunctionQueryInspector.vault_terms

.. automethod:: FunctionQueryInspector.get_function_query_inspector_record



Qualifier Query Inspector
-------------------------

.. autoclass:: QualifierQueryInspector
   :show-inheritance:

.. autoattribute:: QualifierQueryInspector.qualifier_hierarchy_id_terms

.. autoattribute:: QualifierQueryInspector.qualifier_hierarchy_terms

.. autoattribute:: QualifierQueryInspector.authorization_id_terms

.. autoattribute:: QualifierQueryInspector.authorization_terms

.. autoattribute:: QualifierQueryInspector.ancestor_qualifier_id_terms

.. autoattribute:: QualifierQueryInspector.ancestor_qualifier_terms

.. autoattribute:: QualifierQueryInspector.descendant_qualifier_id_terms

.. autoattribute:: QualifierQueryInspector.descendant_qualifier_terms

.. autoattribute:: QualifierQueryInspector.vault_id_terms

.. autoattribute:: QualifierQueryInspector.vault_terms

.. automethod:: QualifierQueryInspector.get_qualifier_query_inspector_record



Vault Query Inspector
---------------------

.. autoclass:: VaultQueryInspector
   :show-inheritance:

.. autoattribute:: VaultQueryInspector.function_id_terms

.. autoattribute:: VaultQueryInspector.function_terms

.. autoattribute:: VaultQueryInspector.qualifier_id_terms

.. autoattribute:: VaultQueryInspector.qualifier_terms

.. autoattribute:: VaultQueryInspector.authorization_id_terms

.. autoattribute:: VaultQueryInspector.authorization_terms

.. autoattribute:: VaultQueryInspector.ancestor_vault_id_terms

.. autoattribute:: VaultQueryInspector.ancestor_vault_terms

.. autoattribute:: VaultQueryInspector.descendant_vault_id_terms

.. autoattribute:: VaultQueryInspector.descendant_vault_terms

.. automethod:: VaultQueryInspector.get_vault_query_inspector_record



