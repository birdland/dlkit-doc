from ..osid import queries as osid_queries


class AuthorizationQuery(osid_queries.OsidRelationshipQuery):
    """The query for authorizations."""
    def match_explicit_authorizations(self, match):
        """Matches explciit authorizations.

        :param match: ``true`` to match explicit authorizations, ``false`` to match implciit authorizations
        :type match: ``boolean``

        """
        pass

    def clear_explicit_authorizations_terms(self):
        """Clears the explicit authorization query terms."""
        pass

    explicit_authorizations_terms = property(fdel=clear_explicit_authorizations_terms)

    def match_related_authorization_id(self, id_, match):
        """Adds an ``Id`` to match explicit or implicitly related authorizations depending on ``matchExplicitAuthorizations()``.

        Multiple ``Ids`` can be added to perform a boolean ``OR`` among
        them.

        :param id: ``Id`` to match
        :type id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``id`` is ``null``

        """
        pass

    def clear_related_authorization_id_terms(self):
        """Clears the related authorization ``Id`` query terms."""
        pass

    related_authorization_id_terms = property(fdel=clear_related_authorization_id_terms)

    def supports_related_authorization_query(self):
        """Tests if an ``AuthorizationQuery`` is available.

        :return: ``true`` if an authorization query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_related_authorization_query(self, match):
        """Gets the authorization query.

        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :return: the ``AuthorizationQuery``
        :rtype: ``osid.authorization.AuthorizationQuery``
        :raise: ``Unimplemented`` -- ``supports_related_authorization_query()`` is ``false``

        """
        return # osid.authorization.AuthorizationQuery

    def clear_related_authorization_terms(self):
        """Clears the related authorization query terms."""
        pass

    related_authorization_terms = property(fdel=clear_related_authorization_terms)

    def match_resource_id(self, resource_id, match):
        """Matches the resource identified by the given ``Id``.

        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        """
        pass

    def clear_resource_id_terms(self):
        """Clears the resource ``Id`` query terms."""
        pass

    resource_id_terms = property(fdel=clear_resource_id_terms)

    def supports_resource_query(self):
        """Tests if a ``ResourceQuery`` is available.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_resource_query(self, match):
        """Gets the resource query.

        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :return: the ``ResourceQuery``
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` is ``false``

        """
        return # osid.resource.ResourceQuery

    def match_any_resource(self, match):
        """Matches authorizations that have any resource.

        :param match: ``true`` to match authorizations with any resource, ``false`` to match authorizations with no resource
        :type match: ``boolean``

        """
        pass

    def clear_resource_terms(self):
        """Clears the resource query terms."""
        pass

    resource_terms = property(fdel=clear_resource_terms)

    def match_trust_id(self, trust_id, match):
        """Matches the trust identified by the given ``Id``.

        :param trust_id: the ``Id`` of the ``Trust``
        :type trust_id: ``osid.id.Id``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``trust_id`` is ``null``

        """
        pass

    def match_any_trust_id(self, match):
        """Matches authorizations that have any trust defined.

        :param match: ``true`` to match authorizations with any trust, ``false`` to match authorizations with no trusts
        :type match: ``boolean``

        """
        pass

    def clear_trust_id_terms(self):
        """Clears the trust ``Id`` query terms."""
        pass

    trust_id_terms = property(fdel=clear_trust_id_terms)

    def match_agent_id(self, agent_id, match):
        """Matches the agent identified by the given ``Id``.

        :param agent_id: the Id of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        """
        pass

    def clear_agent_id_terms(self):
        """Clears the agent ``Id`` query terms."""
        pass

    agent_id_terms = property(fdel=clear_agent_id_terms)

    def supports_agent_query(self):
        """Tests if an ``AgentQuery`` is available.

        :return: ``true`` if an agent query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_agent_query(self, match):
        """Gets the agent query.

        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :return: the ``AgentQuery``
        :rtype: ``osid.authentication.AgentQuery``
        :raise: ``Unimplemented`` -- ``supports_agent_query()`` is ``false``

        """
        return # osid.authentication.AgentQuery

    def match_any_agent(self, match):
        """Matches authorizations that have any agent.

        :param match: ``true`` to match authorizations with any agent, ``false`` to match authorizations with no agent
        :type match: ``boolean``

        """
        pass

    def clear_agent_terms(self):
        """Clears the agent query terms."""
        pass

    agent_terms = property(fdel=clear_agent_terms)

    def match_function_id(self, function_id, match):
        """Matches the function identified by the given ``Id``.

        :param function_id: the Id of the ``Function``
        :type function_id: ``osid.id.Id``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``function_id`` is ``null``

        """
        pass

    def clear_function_id_terms(self):
        """Clears the function ``Id`` query terms."""
        pass

    function_id_terms = property(fdel=clear_function_id_terms)

    def supports_function_query(self):
        """Tests if a ``FunctionQuery`` is available.

        :return: ``true`` if a function query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_function_query(self, match):
        """Gets the function query.

        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :return: the ``FunctinQuery``
        :rtype: ``osid.authorization.FunctionQuery``
        :raise: ``Unimplemented`` -- ``supports_function_query()`` is ``false``

        """
        return # osid.authorization.FunctionQuery

    def clear_function_terms(self):
        """Clears the function query terms."""
        pass

    function_terms = property(fdel=clear_function_terms)

    def match_qualifier_id(self, qualifier_id, match):
        """Matches the qualifier identified by the given ``Id``.

        :param qualifier_id: the Id of the ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``

        """
        pass

    def clear_qualifier_id_terms(self):
        """Clears the qualifier ``Id`` query terms."""
        pass

    qualifier_id_terms = property(fdel=clear_qualifier_id_terms)

    def supports_qualifier_query(self):
        """Tests if a ``QualifierQuery`` is available.

        :return: ``true`` if a qualifier query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_qualifier_query(self, match):
        """Gets the qualiier query.

        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :return: the ``QualifierQuery``
        :rtype: ``osid.authorization.QualifierQuery``
        :raise: ``Unimplemented`` -- ``supports_qualifier_query()`` is ``false``

        """
        return # osid.authorization.QualifierQuery

    def clear_qualifier_terms(self):
        """Clears the qualifier query terms."""
        pass

    qualifier_terms = property(fdel=clear_qualifier_terms)

    def match_vault_id(self, vault_id, match):
        """Sets the vault ``Id`` for this query.

        :param vault_id: a vault ``Id``
        :type vault_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``

        """
        pass

    def clear_vault_id_terms(self):
        """Clears the vault ``Id`` query terms."""
        pass

    vault_id_terms = property(fdel=clear_vault_id_terms)

    def supports_vault_query(self):
        """Tests if a ``VaultQuery`` is available.

        :return: ``true`` if a vault query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_vault_query(self):
        """Gets the query for a vault.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the vault query
        :rtype: ``osid.authorization.VaultQuery``
        :raise: ``Unimplemented`` -- ``supports_vault_query()`` is ``false``

        """
        return # osid.authorization.VaultQuery

    vault_query = property(fget=get_vault_query)

    def clear_vault_terms(self):
        """Clears the vault query terms."""
        pass

    vault_terms = property(fdel=clear_vault_terms)

    def get_authorization_query_record(self, authorization_record_type):
        """Gets the authorization query record corresponding to the given ``Authorization`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param authorization_record_type: an authorization record type
        :type authorization_record_type: ``osid.type.Type``
        :return: the authorization query record
        :rtype: ``osid.authorization.records.AuthorizationQueryRecord``
        :raise: ``NullArgument`` -- ``authorization_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(authorization_record_type)`` is ``false``

        """
        return # osid.authorization.records.AuthorizationQueryRecord


class FunctionQuery(osid_queries.OsidRuleQuery):
    """This is the query for searching functions.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    def match_qualifier_hierarchy_id(self, qualifier_hierarchy_id, match):
        """Sets the qualifier hierarchy ``Id`` for this query.

        :param qualifier_hierarchy_id: a hierarchy ``Id``
        :type qualifier_hierarchy_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``qualifier_hierarchy_id`` is ``null``

        """
        pass

    def clear_qualifier_hierarchy_id_terms(self):
        """Clears the qualifier hierarchy ``Id`` query terms."""
        pass

    qualifier_hierarchy_id_terms = property(fdel=clear_qualifier_hierarchy_id_terms)

    def supports_qualifier_hierarchy_query(self):
        """Tests if a ``HierarchyQuery`` is available.

        :return: ``true`` if a qualifier hierarchy query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_qualifier_hierarchy_query(self):
        """Gets the query for a qualifier hierarchy.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the qualifier hierarchy query
        :rtype: ``osid.hierarchy.HierarchyQuery``
        :raise: ``Unimplemented`` -- ``supports_qualifier_hierarchy_query()`` is ``false``

        """
        return # osid.hierarchy.HierarchyQuery

    qualifier_hierarchy_query = property(fget=get_qualifier_hierarchy_query)

    def match_any_qualifier_hierarchy(self, match):
        """Matches functions that have any qualifier hierarchy.

        :param match: ``true`` to match functions with any qualifier hierarchy, ``false`` to match functions with no qualifier hierarchy
        :type match: ``boolean``

        """
        pass

    def clear_qualifier_hierarchy_terms(self):
        """Clears the qualifier hierarchy query terms."""
        pass

    qualifier_hierarchy_terms = property(fdel=clear_qualifier_hierarchy_terms)

    def match_authorization_id(self, authorization_id, match):
        """Sets the authorization ``Id`` for this query.

        :param authorization_id: an authorization ``Id``
        :type authorization_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``

        """
        pass

    def clear_authorization_id_terms(self):
        """Clears the authorization ``Id`` query terms."""
        pass

    authorization_id_terms = property(fdel=clear_authorization_id_terms)

    def supports_authorization_query(self):
        """Tests if an ``AuthorizationQuery`` is available.

        :return: ``true`` if an authorization query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_authorization_query(self):
        """Gets the query for an authorization.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the authorization query
        :rtype: ``osid.authorization.AuthorizationQuery``
        :raise: ``Unimplemented`` -- ``supports_authorization_query()`` is ``false``

        """
        return # osid.authorization.AuthorizationQuery

    authorization_query = property(fget=get_authorization_query)

    def match_any_authorization(self, match):
        """Matches functions that have any authorization mapping.

        :param match: ``true`` to match functions with any authorization mapping, ``false`` to match functions with no authorization mapping
        :type match: ``boolean``

        """
        pass

    def clear_authorization_terms(self):
        """Clears the authorization query terms."""
        pass

    authorization_terms = property(fdel=clear_authorization_terms)

    def match_vault_id(self, vault_id, match):
        """Sets the vault ``Id`` for this query.

        :param vault_id: a vault ``Id``
        :type vault_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``

        """
        pass

    def clear_vault_id_terms(self):
        """Clears the vault ``Id`` query terms."""
        pass

    vault_id_terms = property(fdel=clear_vault_id_terms)

    def supports_vault_query(self):
        """Tests if a ``VaultQuery`` is available.

        :return: ``true`` if a vault query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_vault_query(self):
        """Gets the query for a vault.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the vault query
        :rtype: ``osid.authorization.VaultQuery``
        :raise: ``Unimplemented`` -- ``supports_vault_query()`` is ``false``

        """
        return # osid.authorization.VaultQuery

    vault_query = property(fget=get_vault_query)

    def clear_vault_terms(self):
        """Clears the vault query terms."""
        pass

    vault_terms = property(fdel=clear_vault_terms)

    def get_function_query_record(self, function_record_type):
        """Gets the function query record corresponding to the given ``Function`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param function_record_type: a function record type
        :type function_record_type: ``osid.type.Type``
        :return: the function query record
        :rtype: ``osid.authorization.records.FunctionQueryRecord``
        :raise: ``NullArgument`` -- ``function_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(function_record_type)`` is ``false``

        """
        return # osid.authorization.records.FunctionQueryRecord


class QualifierQuery(osid_queries.OsidObjectQuery, osid_queries.OsidFederateableQuery):
    """This is the query for searching qualifiers.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    def match_qualifier_hierarchy_id(self, qualifier_hierarchy_id, match):
        """Sets the qualifier hierarchy ``Id`` for this query.

        :param qualifier_hierarchy_id: a hierarchy ``Id``
        :type qualifier_hierarchy_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``qualifier_hierarchy_id`` is ``null``

        """
        pass

    def clear_qualifier_hierarchy_id_terms(self):
        """Clears the qualifier hierarchy ``Id`` query terms."""
        pass

    qualifier_hierarchy_id_terms = property(fdel=clear_qualifier_hierarchy_id_terms)

    def supports_qualifier_hierarchy_query(self):
        """Tests if a ``HierarchyQuery`` is available.

        :return: ``true`` if a qualifier hierarchy query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_qualifier_hierarchy_query(self):
        """Gets the query for a qualifier hierarchy.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the qualifier hierarchy query
        :rtype: ``osid.hierarchy.HierarchyQuery``
        :raise: ``Unimplemented`` -- ``supports_qualifier_hierarchy_query()`` is ``false``

        """
        return # osid.hierarchy.HierarchyQuery

    qualifier_hierarchy_query = property(fget=get_qualifier_hierarchy_query)

    def clear_qualifier_hierarchy_terms(self):
        """Clears the qualifier hierarchy query terms."""
        pass

    qualifier_hierarchy_terms = property(fdel=clear_qualifier_hierarchy_terms)

    def match_authorization_id(self, authorization_id, match):
        """Sets the authorization ``Id`` for this query.

        :param authorization_id: an authorization ``Id``
        :type authorization_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``

        """
        pass

    def clear_authorization_id_terms(self):
        """Clears the authorization ``Id`` query terms."""
        pass

    authorization_id_terms = property(fdel=clear_authorization_id_terms)

    def supports_authorization_query(self):
        """Tests if an ``AuthorizationQuery`` is available.

        :return: ``true`` if an authorization query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_authorization_query(self):
        """Gets the query for an authorization.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the authorization query
        :rtype: ``osid.authorization.AuthorizationQuery``
        :raise: ``Unimplemented`` -- ``supports_authorization_query()`` is ``false``

        """
        return # osid.authorization.AuthorizationQuery

    authorization_query = property(fget=get_authorization_query)

    def match_any_authorization(self, match):
        """Matches qualifiers that have any authorization mapping.

        :param match: ``true`` to match qualifiers with any authorization mapping, ``false`` to match qualifiers with no authorization mapping
        :type match: ``boolean``

        """
        pass

    def clear_authorization_terms(self):
        """Clears the authorization query terms."""
        pass

    authorization_terms = property(fdel=clear_authorization_terms)

    def match_ancestor_qualifier_id(self, qualifier_id, match):
        """Sets the qualifier ``Id`` for this query to match qualifiers that have the specified qualifier as an ancestor.

        :param qualifier_id: a qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``

        """
        pass

    def clear_ancestor_qualifier_id_terms(self):
        """Clears the ancestor qualifier ``Id`` query terms."""
        pass

    ancestor_qualifier_id_terms = property(fdel=clear_ancestor_qualifier_id_terms)

    def supports_ancestor_qualifier_query(self):
        """Tests if a ``QualifierQuery`` is available.

        :return: ``true`` if a qualifier query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_ancestor_qualifier_query(self):
        """Gets the query for a qualifier.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the qualifier query
        :rtype: ``osid.authorization.QualifierQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_qualifier_query()`` is ``false``

        """
        return # osid.authorization.QualifierQuery

    ancestor_qualifier_query = property(fget=get_ancestor_qualifier_query)

    def match_any_ancestor_qualifier(self, match):
        """Matches qualifiers that have any ancestor.

        :param match: ``true`` to match qualifiers with any ancestor, ``false`` to match root qualifiers
        :type match: ``boolean``

        """
        pass

    def clear_ancestor_qualifier_terms(self):
        """Clears the ancestor qualifier query terms."""
        pass

    ancestor_qualifier_terms = property(fdel=clear_ancestor_qualifier_terms)

    def match_descendant_qualifier_id(self, qualifier_id, match):
        """Sets the qualifier ``Id`` for this query to match qualifiers that have the specified qualifier as a descendant.

        :param qualifier_id: a qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``

        """
        pass

    def clear_descendant_qualifier_id_terms(self):
        """Clears the descendant qualifier ``Id`` query terms."""
        pass

    descendant_qualifier_id_terms = property(fdel=clear_descendant_qualifier_id_terms)

    def supports_descendant_qualifier_query(self):
        """Tests if a ``QualifierQuery`` is available.

        :return: ``true`` if a qualifier query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_descendant_qualifier_query(self):
        """Gets the query for a qualifier.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the qualifier query
        :rtype: ``osid.authorization.QualifierQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_qualifier_query()`` is ``false``

        """
        return # osid.authorization.QualifierQuery

    descendant_qualifier_query = property(fget=get_descendant_qualifier_query)

    def match_any_descendant_qualifier(self, match):
        """Matches qualifiers that have any ancestor.

        :param match: ``true`` to match qualifiers with any ancestor, ``false`` to match leaf qualifiers
        :type match: ``boolean``

        """
        pass

    def clear_descendant_qualifier_terms(self):
        """Clears the descendant qualifier query terms."""
        pass

    descendant_qualifier_terms = property(fdel=clear_descendant_qualifier_terms)

    def match_vault_id(self, vault_id, match):
        """Sets the vault ``Id`` for this query.

        :param vault_id: a vault ``Id``
        :type vault_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``

        """
        pass

    def clear_vault_id_terms(self):
        """Clears the vault ``Id`` query terms."""
        pass

    vault_id_terms = property(fdel=clear_vault_id_terms)

    def supports_vault_query(self):
        """Tests if a ``VaultQuery`` is available.

        :return: ``true`` if a vault query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_vault_query(self):
        """Gets the query for a vault.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the vault query
        :rtype: ``osid.authorization.VaultQuery``
        :raise: ``Unimplemented`` -- ``supports_vault_query()`` is ``false``

        """
        return # osid.authorization.VaultQuery

    vault_query = property(fget=get_vault_query)

    def clear_vault_terms(self):
        """Clears the vault query terms."""
        pass

    vault_terms = property(fdel=clear_vault_terms)

    def get_qualifier_query_record(self, qualifier_record_type):
        """Gets the qualfiier query record corresponding to the given ``Qualifier`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param qualifier_record_type: a qualifier record type
        :type qualifier_record_type: ``osid.type.Type``
        :return: the qualifier query record
        :rtype: ``osid.authorization.records.QualifierQueryRecord``
        :raise: ``NullArgument`` -- ``qualifier_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(qualifier_record_type)`` is ``false``

        """
        return # osid.authorization.records.QualifierQueryRecord


class VaultQuery(osid_queries.OsidCatalogQuery):
    """This is the query for searching vaults.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def match_function_id(self, function_id, match):
        """Sets the function ``Id`` for this query.

        :param function_id: a function ``Id``
        :type function_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``function_id`` is ``null``

        """
        pass

    def clear_function_id_terms(self):
        """Clears the function ``Id`` query terms."""
        pass

    function_id_terms = property(fdel=clear_function_id_terms)

    def supports_function_query(self):
        """Tests if a ``FunctionQuery`` is available.

        :return: ``true`` if a function query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_function_query(self):
        """Gets the query for a function.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the function query
        :rtype: ``osid.authorization.FunctionQuery``
        :raise: ``Unimplemented`` -- ``supports_function_query()`` is ``false``

        """
        return # osid.authorization.FunctionQuery

    function_query = property(fget=get_function_query)

    def match_any_function(self, match):
        """Matches vaults that have any function.

        :param match: ``true`` to match vaults with any function mapping, ``false`` to match vaults with no function mapping
        :type match: ``boolean``

        """
        pass

    def clear_function_terms(self):
        """Clears the function query terms."""
        pass

    function_terms = property(fdel=clear_function_terms)

    def match_qualifier_id(self, qualifier_id, match):
        """Sets the qualifier ``Id`` for this query.

        :param qualifier_id: a qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``

        """
        pass

    def clear_qualifier_id_terms(self):
        """Clears the qualifier ``Id`` query terms."""
        pass

    qualifier_id_terms = property(fdel=clear_qualifier_id_terms)

    def supports_qualifier_query(self):
        """Tests if a ``QualifierQuery`` is available.

        :return: ``true`` if a qualifier query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_qualifier_query(self):
        """Gets the query for a qualifier.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the qualifier query
        :rtype: ``osid.authorization.QualifierQuery``
        :raise: ``Unimplemented`` -- ``supports_qualifier_query()`` is ``false``

        """
        return # osid.authorization.QualifierQuery

    qualifier_query = property(fget=get_qualifier_query)

    def match_any_qualifier(self, match):
        """Matches vaults that have any qualifier.

        :param match: ``true`` to match vaults with any qualifier mapping, ``false`` to match vaults with no qualifier mapping
        :type match: ``boolean``

        """
        pass

    def clear_qualifier_terms(self):
        """Clears the qualifier query terms."""
        pass

    qualifier_terms = property(fdel=clear_qualifier_terms)

    def match_authorization_id(self, authorization_id, match):
        """Sets the authorization ``Id`` for this query.

        :param authorization_id: an authorization ``Id``
        :type authorization_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``

        """
        pass

    def clear_authorization_id_terms(self):
        """Clears the authorization ``Id`` query terms."""
        pass

    authorization_id_terms = property(fdel=clear_authorization_id_terms)

    def supports_authorization_query(self):
        """Tests if an ``AuthorizationQuery`` is available.

        :return: ``true`` if an authorization query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_authorization_query(self):
        """Gets the query for an authorization.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the authorization query
        :rtype: ``osid.authorization.AuthorizationQuery``
        :raise: ``Unimplemented`` -- ``supports_authorization_query()`` is ``false``

        """
        return # osid.authorization.AuthorizationQuery

    authorization_query = property(fget=get_authorization_query)

    def match_any_authorization(self, match):
        """Matches vaults that have any authorization.

        :param match: ``true`` to match vaults with any authorization mapping, ``false`` to match vaults with no authorization mapping
        :type match: ``boolean``

        """
        pass

    def clear_authorization_terms(self):
        """Clears the authorization query terms."""
        pass

    authorization_terms = property(fdel=clear_authorization_terms)

    def match_ancestor_vault_id(self, vault_id, match):
        """Sets the vault ``Id`` for this query to match vaults that have the specified vault as an ancestor.

        :param vault_id: a vault ``Id``
        :type vault_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``

        """
        pass

    def clear_ancestor_vault_id_terms(self):
        """Clears the ancestor vault ``Id`` query terms."""
        pass

    ancestor_vault_id_terms = property(fdel=clear_ancestor_vault_id_terms)

    def supports_ancestor_vault_query(self):
        """Tests if a ``VaultQuery`` is available.

        :return: ``true`` if a vault query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_ancestor_vault_query(self):
        """Gets the query for a vault.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the vault query
        :rtype: ``osid.authorization.VaultQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_vault_query()`` is ``false``

        """
        return # osid.authorization.VaultQuery

    ancestor_vault_query = property(fget=get_ancestor_vault_query)

    def match_any_ancestor_vault(self, match):
        """Matches vaults that have any ancestor.

        :param match: ``true`` to match vaults with any ancestor, ``false`` to match root vaults
        :type match: ``boolean``

        """
        pass

    def clear_ancestor_vault_terms(self):
        """Clears the ancestor vault query terms."""
        pass

    ancestor_vault_terms = property(fdel=clear_ancestor_vault_terms)

    def match_descendant_vault_id(self, vault_id, match):
        """Sets the vault ``Id`` for this query to match vaults that have the specified vault as a descendant.

        :param vault_id: a vault ``Id``
        :type vault_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``

        """
        pass

    def clear_descendant_vault_id_terms(self):
        """Clears the descendant vault ``Id`` query terms."""
        pass

    descendant_vault_id_terms = property(fdel=clear_descendant_vault_id_terms)

    def supports_descendant_vault_query(self):
        """Tests if a ``VaultQuery`` is available.

        :return: ``true`` if a vault query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_descendant_vault_query(self):
        """Gets the query for a vault.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the vault query
        :rtype: ``osid.authorization.VaultQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_vault_query()`` is ``false``

        """
        return # osid.authorization.VaultQuery

    descendant_vault_query = property(fget=get_descendant_vault_query)

    def match_any_descendant_vault(self, match):
        """Matches vaults that have any descendant.

        :param match: ``true`` to match vaults with any Ddscendant, ``false`` to match leaf vaults
        :type match: ``boolean``

        """
        pass

    def clear_descendant_vault_terms(self):
        """Clears the descendant vault query terms."""
        pass

    descendant_vault_terms = property(fdel=clear_descendant_vault_terms)

    def get_vault_query_record(self, vault_record_type):
        """Gets the vault query record corresponding to the given ``Vault`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param vault_record_type: a vault record type
        :type vault_record_type: ``osid.type.Type``
        :return: the vault query record
        :rtype: ``osid.authorization.records.VaultQueryRecord``
        :raise: ``NullArgument`` -- ``vault_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(vault_record_type)`` is ``false``

        """
        return # osid.authorization.records.VaultQueryRecord


