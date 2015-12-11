
from ..osid import queries as osid_queries


class ResourceQuery(osid_queries.OsidObjectQuery):
    """This is the query for searching resources.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    



    def match_group(self, match):
        """Matches resources that are also groups.

        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_group_terms(self):
        """Clears the group terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    group_terms = property(fdel=clear_group_terms)


    def match_demographic(self, match):
        """Matches resources that are also demographics.

        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_demographic_terms(self):
        """Clears the demographic terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    demographic_terms = property(fdel=clear_demographic_terms)


    def match_containing_group_id(self, resource_id, match):
        """Sets the group ``Id`` for this query to match resources within the given group.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``resource_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_containing_group_id_terms(self):
        """Clears the group ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    containing_group_id_terms = property(fdel=clear_containing_group_id_terms)


    def supports_containing_group_query(self):
        """Tests if a ``ResourceQuery`` is available for querying containing groups.

        return: (boolean) - ``true`` if a group resource query is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_containing_group_query(self):
        """Gets the query for a a containing group.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.resource.ResourceQuery) - the resource query
        raise:  Unimplemented - ``supports_containing_group_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_agent_query()`` is ``true``.*

        """
        return # osid.resource.ResourceQuery

    containing_group_query = property(fget=get_containing_group_query)


    def match_any_containing_group(self, match):
        """Matches resources inside any group.

        arg:    match (boolean): ``true`` to match any containing group,
                ``false`` to match resources part of no groups
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_containing_group_terms(self):
        """Clears the containing group terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    containing_group_terms = property(fdel=clear_containing_group_terms)


    def match_avatar_id(self, asset_id, match):
        """Sets the asset ``Id`` for this query.

        arg:    asset_id (osid.id.Id): the asset ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``asset_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_avatar_id_terms(self):
        """Clears the asset ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    avatar_id_terms = property(fdel=clear_avatar_id_terms)


    def supports_avatar_query(self):
        """Tests if an ``AssetQuery`` is available.

        return: (boolean) - ``true`` if an asset query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_avatar_query(self):
        """Gets the query for an asset.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.repository.AssetQuery) - the asset query
        raise:  Unimplemented - ``supports_avatar_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_avatar_query()`` is ``true``.*

        """
        return # osid.repository.AssetQuery

    avatar_query = property(fget=get_avatar_query)


    def match_any_avatar(self, match):
        """Matches resources with any asset.

        arg:    match (boolean): ``true`` to match any asset, ``false``
                to match resources with no asset
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_avatar_terms(self):
        """Clears the asset terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    avatar_terms = property(fdel=clear_avatar_terms)


    def match_agent_id(self, agent_id, match):
        """Sets the agent ``Id`` for this query.

        arg:    agent_id (osid.id.Id): the agent ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``agent_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_agent_id_terms(self):
        """Clears the agent ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    agent_id_terms = property(fdel=clear_agent_id_terms)


    def supports_agent_query(self):
        """Tests if an ``AgentQuery`` is available.

        return: (boolean) - ``true`` if an agent query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_agent_query(self):
        """Gets the query for an agent.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.authentication.AgentQuery) - the agent query
        raise:  Unimplemented - ``supports_agent_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_agent_query()`` is ``true``.*

        """
        return # osid.authentication.AgentQuery

    agent_query = property(fget=get_agent_query)


    def match_any_agent(self, match):
        """Matches resources with any agent.

        arg:    match (boolean): ``true`` to match any agent, ``false``
                to match resources with no agent
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_agent_terms(self):
        """Clears the agent terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    agent_terms = property(fdel=clear_agent_terms)


    def match_resource_relationship_id(self, resource_relationship_id, match):
        """Sets the resource relationship ``Id`` for this query.

        arg:    resource_relationship_id (osid.id.Id): the resource
                relationship ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``resource_relationship_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_resource_relationship_id_terms(self):
        """Clears the resource relationship ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    resource_relationship_id_terms = property(fdel=clear_resource_relationship_id_terms)


    def supports_resource_relationship_query(self):
        """Tests if a ``ResourceRelationshipQuery`` is available.

        return: (boolean) - ``true`` if a resource relationship query is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_resource_relationship_query(self):
        """Gets the query for aa resource relationship.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.resource.ResourceRelationshipQuery) - the resource
                relationship query
        raise:  Unimplemented -
                ``supports_resource_relationship_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_query()`` is ``true``.*

        """
        return # osid.resource.ResourceRelationshipQuery

    resource_relationship_query = property(fget=get_resource_relationship_query)


    def match_any_resource_relationship(self, match):
        """Matches resources with any resource relationship.

        arg:    match (boolean): ``true`` to match any resource
                relationship, ``false`` to match resources with no
                relationship
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_resource_relationship_terms(self):
        """Clears the resource relationship terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    resource_relationship_terms = property(fdel=clear_resource_relationship_terms)


    def match_bin_id(self, bin_id, match):
        """Sets the bin ``Id`` for this query.

        arg:    bin_id (osid.id.Id): the bin ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``bin_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_bin_id_terms(self):
        """Clears the bin ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    bin_id_terms = property(fdel=clear_bin_id_terms)


    def supports_bin_query(self):
        """Tests if a ``BinQuery`` is available.

        return: (boolean) - ``true`` if a bin query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_bin_query(self):
        """Gets the query for a bin.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.resource.BinQuery) - the bin query
        raise:  Unimplemented - ``supports_bin_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_bin_query()`` is ``true``.*

        """
        return # osid.resource.BinQuery

    bin_query = property(fget=get_bin_query)


    def clear_bin_terms(self):
        """Clears the bin terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    bin_terms = property(fdel=clear_bin_terms)


    def get_resource_query_record(self, resource_record_type):
        """Gets the resource query record corresponding to the given ``Resource`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        arg:    resource_record_type (osid.type.Type): a resource record
                type
        return: (osid.resource.records.ResourceQueryRecord) - the
                resource query record
        raise:  NullArgument - ``resource_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(resource_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.records.ResourceQueryRecord


class BinQuery(osid_queries.OsidCatalogQuery):
    """This is the query for searching bins.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    



    def match_resource_id(self, resource_id, match):
        """Sets the resource ``Id`` for this query.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``resource_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_resource_id_terms(self):
        """Clears the resource ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    resource_id_terms = property(fdel=clear_resource_id_terms)


    def supports_resource_query(self):
        """Tests if a ``ResourceQuery`` is available.

        return: (boolean) - ``true`` if a resource query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_resource_query(self):
        """Gets the query for a resource.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.resource.ResourceQuery) - the resource query
        raise:  Unimplemented - ``supports_resource_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` is ``true``.*

        """
        return # osid.resource.ResourceQuery

    resource_query = property(fget=get_resource_query)


    def match_any_resource(self, match):
        """Matches bins with any resource.

        arg:    match (boolean): ``true`` to match bins with any
                resource, ``false`` to match bins with no resources
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_resource_terms(self):
        """Clears the resource terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    resource_terms = property(fdel=clear_resource_terms)


    def match_ancestor_bin_id(self, binid, match):
        """Sets the bin ``Id`` for this query to match bins that have the specified bin as an ancestor.

        arg:    binid (osid.id.Id): a bin ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``bin_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_ancestor_bin_id_terms(self):
        """Clears the ancestor bin ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_bin_id_terms = property(fdel=clear_ancestor_bin_id_terms)


    def supports_ancestor_bin_query(self):
        """Tests if a ``BinQuery`` is available.

        return: (boolean) - ``true`` if a bin query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_ancestor_bin_query(self):
        """Gets the query for a bin.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.resource.BinQuery) - the bin query
        raise:  Unimplemented - ``supports_ancestor_bin_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_bin_query()`` is ``true``.*

        """
        return # osid.resource.BinQuery

    ancestor_bin_query = property(fget=get_ancestor_bin_query)


    def match_any_ancestor_bin(self, match):
        """Matches bins with any ancestor.

        arg:    match (boolean): ``true`` to match bins with any
                ancestor, ``false`` to match root bins
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_ancestor_bin_terms(self):
        """Clears the ancestor bin terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_bin_terms = property(fdel=clear_ancestor_bin_terms)


    def match_descendant_bin_id(self, binid, match):
        """Sets the bin ``Id`` for this query to match bins that have the specified bin as a descendant.

        arg:    binid (osid.id.Id): a bin ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``bin_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_descendant_bin_id_terms(self):
        """Clears the descendant bin ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_bin_id_terms = property(fdel=clear_descendant_bin_id_terms)


    def supports_descendant_bin_query(self):
        """Tests if a ``BinQuery`` is available.

        return: (boolean) - ``true`` if a bin query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_descendant_bin_query(self):
        """Gets the query for a bin.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.resource.BinQuery) - the bin query
        raise:  Unimplemented - ``supports_descendant_bin_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_descendant_bin_query()`` is ``true``.*

        """
        return # osid.resource.BinQuery

    descendant_bin_query = property(fget=get_descendant_bin_query)


    def match_any_descendant_bin(self, match):
        """Matches bins with any descendant.

        arg:    match (boolean): ``true`` to match bins with any
                descendant, ``false`` to match leaf bins
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_descendant_bin_terms(self):
        """Clears the descendant bin terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_bin_terms = property(fdel=clear_descendant_bin_terms)


    def get_bin_query_record(self, bin_record_type):
        """Gets the bin query record corresponding to the given ``Bin`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        arg:    bin_record_type (osid.type.Type): a bin record type
        return: (osid.resource.records.BinQueryRecord) - the bin query
                record
        raise:  NullArgument - ``bin_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(bin_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.records.BinQueryRecord


