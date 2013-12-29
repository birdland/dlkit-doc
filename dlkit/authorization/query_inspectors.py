from ..osid import query_inspectors as osid_query_inspectors


class AuthorizationQueryInspector(osid_query_inspectors.OsidRelationshipQueryInspector):
    """The query inspector for examining authorization queries."""
    def get_explicit_authorizations_terms(self):
        """Gets the explicit authorization query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``

        """
        return # osid.search.terms.BooleanTerm

    explicit_authorizations_terms = property(fget=get_explicit_authorizations_terms)

    def get_related_authorization_id_terms(self):
        """Gets the related authorization ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    related_authorization_id_terms = property(fget=get_related_authorization_id_terms)

    def get_related_authorization_terms(self):
        """Gets the related authorization query terms.

        :return: the query terms
        :rtype: ``osid.authorization.AuthorizationQueryInspector``

        """
        return # osid.authorization.AuthorizationQueryInspector

    related_authorization_terms = property(fget=get_related_authorization_terms)

    def get_resource_id_terms(self):
        """Gets the resource ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    resource_id_terms = property(fget=get_resource_id_terms)

    def get_resource_terms(self):
        """Gets the resource query terms.

        :return: the query terms
        :rtype: ``osid.resource.ResourceQueryInspector``

        """
        return # osid.resource.ResourceQueryInspector

    resource_terms = property(fget=get_resource_terms)

    def get_trust_id_terms(self):
        """Gets the trust ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    trust_id_terms = property(fget=get_trust_id_terms)

    def get_agent_id_terms(self):
        """Gets the agent ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    agent_id_terms = property(fget=get_agent_id_terms)

    def get_agent_terms(self):
        """Gets the agent query terms.

        :return: the query terms
        :rtype: ``osid.authentication.AgentQueryInspector``

        """
        return # osid.authentication.AgentQueryInspector

    agent_terms = property(fget=get_agent_terms)

    def get_function_id_terms(self):
        """Gets the function ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    function_id_terms = property(fget=get_function_id_terms)

    def get_function_terms(self):
        """Gets the function query terms.

        :return: the query terms
        :rtype: ``osid.authorization.FunctionQueryInspector``

        """
        return # osid.authorization.FunctionQueryInspector

    function_terms = property(fget=get_function_terms)

    def get_qualifier_id_terms(self):
        """Gets the qualifier ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    qualifier_id_terms = property(fget=get_qualifier_id_terms)

    def get_qualifier_terms(self):
        """Gets the qualifier query terms.

        :return: the query terms
        :rtype: ``osid.authorization.QualifierQueryInspector``

        """
        return # osid.authorization.QualifierQueryInspector

    qualifier_terms = property(fget=get_qualifier_terms)

    def get_vault_id_terms(self):
        """Gets the vault ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    vault_id_terms = property(fget=get_vault_id_terms)

    def get_vault_terms(self):
        """Gets the vault query terms.

        :return: the query terms
        :rtype: ``osid.authorization.VaultQueryInspector``

        """
        return # osid.authorization.VaultQueryInspector

    vault_terms = property(fget=get_vault_terms)

    def get_authorization_query_inspector_record(self, authorization_record_type):
        """Gets the authorization query inspector record corresponding to the given ``Authorization`` record ``Type``.

        :param authorization_record_type: an authorization record type
        :type authorization_record_type: ``osid.type.Type``
        :return: the authorization query inspector record
        :rtype: ``osid.authorization.records.AuthorizationQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``authorization_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(authorization_record_type)`` is ``false``

        """
        return # osid.authorization.records.AuthorizationQueryInspectorRecord


class FunctionQueryInspector(osid_query_inspectors.OsidRuleQueryInspector):
    """This is the query inspector for examining function queries."""
    def get_qualifier_hierarchy_id_terms(self):
        """Gets the qualifier hierarchy ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    qualifier_hierarchy_id_terms = property(fget=get_qualifier_hierarchy_id_terms)

    def get_qualifier_hierarchy_terms(self):
        """Gets the qualifier hierarchy query terms.

        :return: the query terms
        :rtype: ``osid.hierarchy.HierarchyQueryInspector``

        """
        return # osid.hierarchy.HierarchyQueryInspector

    qualifier_hierarchy_terms = property(fget=get_qualifier_hierarchy_terms)

    def get_authorization_id_terms(self):
        """Gets the authorization ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    authorization_id_terms = property(fget=get_authorization_id_terms)

    def get_authorization_terms(self):
        """Gets the authorization query terms.

        :return: the query terms
        :rtype: ``osid.authorization.AuthorizationQueryInspector``

        """
        return # osid.authorization.AuthorizationQueryInspector

    authorization_terms = property(fget=get_authorization_terms)

    def get_vault_id_terms(self):
        """Gets the vault ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    vault_id_terms = property(fget=get_vault_id_terms)

    def get_vault_terms(self):
        """Gets the vault query terms.

        :return: the query terms
        :rtype: ``osid.authorization.VaultQueryInspector``

        """
        return # osid.authorization.VaultQueryInspector

    vault_terms = property(fget=get_vault_terms)

    def get_function_query_inspector_record(self, function_record_type):
        """Gets the function query inspector record corresponding to the given ``Function`` record ``Type``.

        :param function_record_type: a function record type
        :type function_record_type: ``osid.type.Type``
        :return: the function query inspector record
        :rtype: ``osid.authorization.records.FunctionQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``function_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(function_record_type)`` is ``false``

        """
        return # osid.authorization.records.FunctionQueryInspectorRecord


class QualifierQueryInspector(osid_query_inspectors.OsidObjectQueryInspector, osid_query_inspectors.OsidFederateableQueryInspector):
    """This is the query inspector for examining qualifiers queries."""
    def get_qualifier_hierarchy_id_terms(self):
        """Gets the qualifier hierarchy ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    qualifier_hierarchy_id_terms = property(fget=get_qualifier_hierarchy_id_terms)

    def get_qualifier_hierarchy_terms(self):
        """Gets the qualifier hierarchy query terms.

        :return: the query terms
        :rtype: ``osid.hierarchy.HierarchyQueryInspector``

        """
        return # osid.hierarchy.HierarchyQueryInspector

    qualifier_hierarchy_terms = property(fget=get_qualifier_hierarchy_terms)

    def get_authorization_id_terms(self):
        """Gets the authorization ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    authorization_id_terms = property(fget=get_authorization_id_terms)

    def get_authorization_terms(self):
        """Gets the authorization query terms.

        :return: the query terms
        :rtype: ``osid.authorization.AuthorizationQueryInspector``

        """
        return # osid.authorization.AuthorizationQueryInspector

    authorization_terms = property(fget=get_authorization_terms)

    def get_ancestor_qualifier_id_terms(self):
        """Gets the ancestor qualifier ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    ancestor_qualifier_id_terms = property(fget=get_ancestor_qualifier_id_terms)

    def get_ancestor_qualifier_terms(self):
        """Gets the ancestor qualifier query terms.

        :return: the query terms
        :rtype: ``osid.authorization.FunctionQueryInspector``

        """
        return # osid.authorization.FunctionQueryInspector

    ancestor_qualifier_terms = property(fget=get_ancestor_qualifier_terms)

    def get_descendant_qualifier_id_terms(self):
        """Gets the descendant qualifier ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    descendant_qualifier_id_terms = property(fget=get_descendant_qualifier_id_terms)

    def get_descendant_qualifier_terms(self):
        """Gets the descendant qualifier query terms.

        :return: the query terms
        :rtype: ``osid.authorization.FunctionQueryInspector``

        """
        return # osid.authorization.FunctionQueryInspector

    descendant_qualifier_terms = property(fget=get_descendant_qualifier_terms)

    def get_vault_id_terms(self):
        """Gets the vault ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    vault_id_terms = property(fget=get_vault_id_terms)

    def get_vault_terms(self):
        """Gets the vault query terms.

        :return: the query terms
        :rtype: ``osid.authorization.VaultQueryInspector``

        """
        return # osid.authorization.VaultQueryInspector

    vault_terms = property(fget=get_vault_terms)

    def get_qualifier_query_inspector_record(self, qualifier_record_type):
        """Gets the qualifier query inspector record corresponding to the given ``Qualifier`` record ``Type``.

        :param qualifier_record_type: a qualifier query inspector record type
        :type qualifier_record_type: ``osid.type.Type``
        :return: the qualifier query inspector record
        :rtype: ``osid.authorization.records.QualifierQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``qualifier_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(qualifier_record_type)`` is ``false``

        """
        return # osid.authorization.records.QualifierQueryInspectorRecord


class VaultQueryInspector(osid_query_inspectors.OsidCatalogQueryInspector):
    """This is the query inspector for examining vault queries."""
    def get_function_id_terms(self):
        """Gets the function ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    function_id_terms = property(fget=get_function_id_terms)

    def get_function_terms(self):
        """Gets the function query terms.

        :return: the query terms
        :rtype: ``osid.authorization.FunctionQueryInspector``

        """
        return # osid.authorization.FunctionQueryInspector

    function_terms = property(fget=get_function_terms)

    def get_qualifier_id_terms(self):
        """Gets the qualifier ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    qualifier_id_terms = property(fget=get_qualifier_id_terms)

    def get_qualifier_terms(self):
        """Gets the qualifier query terms.

        :return: the query terms
        :rtype: ``osid.authorization.QualifierQueryInspector``

        """
        return # osid.authorization.QualifierQueryInspector

    qualifier_terms = property(fget=get_qualifier_terms)

    def get_authorization_id_terms(self):
        """Gets the authorization ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    authorization_id_terms = property(fget=get_authorization_id_terms)

    def get_authorization_terms(self):
        """Gets the authorization query terms.

        :return: the query terms
        :rtype: ``osid.authorization.AuthorizationQueryInspector``

        """
        return # osid.authorization.AuthorizationQueryInspector

    authorization_terms = property(fget=get_authorization_terms)

    def get_ancestor_vault_id_terms(self):
        """Gets the ancestor vault ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    ancestor_vault_id_terms = property(fget=get_ancestor_vault_id_terms)

    def get_ancestor_vault_terms(self):
        """Gets the ancestor vault query terms.

        :return: the query terms
        :rtype: ``osid.authorization.VaultQueryInspector``

        """
        return # osid.authorization.VaultQueryInspector

    ancestor_vault_terms = property(fget=get_ancestor_vault_terms)

    def get_descendant_vault_id_terms(self):
        """Gets the descendant vault ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    descendant_vault_id_terms = property(fget=get_descendant_vault_id_terms)

    def get_descendant_vault_terms(self):
        """Gets the descendant vault query terms.

        :return: the query terms
        :rtype: ``osid.authorization.VaultQueryInspector``

        """
        return # osid.authorization.VaultQueryInspector

    descendant_vault_terms = property(fget=get_descendant_vault_terms)

    def get_vault_query_inspector_record(self, vault_record_type):
        """Gets the vault query inspector record corresponding to the given ``Vault`` record ``Type``.

        :param vault_record_type: a vault query inspector record type
        :type vault_record_type: ``osid.type.Type``
        :return: the vault query inspector record
        :rtype: ``osid.authorization.records.VaultQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``vault_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(vault_record_type)`` is ``false``

        """
        return # osid.authorization.records.VaultQueryInspectorRecord


