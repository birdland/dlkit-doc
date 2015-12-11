
from ..osid import queries as osid_queries


class RelationshipQuery(osid_queries.OsidRelationshipQuery):
    """This is the query for searching relationships.

    Each method match specifies an ``AND`` term while multiple
    invocations of the same method produce a nested ``OR``.

    """
    



    def match_source_id(self, peer, match):
        """Matches a relationship peer.

        arg:    peer (osid.id.Id): peer ``Id`` to match
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``peer`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_source_id_terms(self):
        """Clears the peer ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    source_id_terms = property(fdel=clear_source_id_terms)


    def match_destination_id(self, peer, match):
        """Matches the other relationship peer.

        arg:    peer (osid.id.Id): peer ``Id`` to match
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``peer`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_destination_id_terms(self):
        """Clears the other peer ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    destination_id_terms = property(fdel=clear_destination_id_terms)


    def match_same_peer_id(self, match):
        """Matches circular relationships to the same peer.

        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_same_peer_id_terms(self):
        """Clears the same peer ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    same_peer_id_terms = property(fdel=clear_same_peer_id_terms)


    def match_family_id(self, family_id, match):
        """Sets the family ``Id`` for this query.

        arg:    family_id (osid.id.Id): a family ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``family_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_family_id_terms(self):
        """Clears the family ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    family_id_terms = property(fdel=clear_family_id_terms)


    def supports_family_query(self):
        """Tests if a ``FamilyQuery`` is available.

        return: (boolean) - ``true`` if a family query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_family_query(self):
        """Gets the query for a family.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.relationship.FamilyQuery) - the family query
        raise:  Unimplemented - ``supports_family_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_family_query()`` is ``true``.*

        """
        return # osid.relationship.FamilyQuery

    family_query = property(fget=get_family_query)


    def clear_family_terms(self):
        """Clears the family terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    family_terms = property(fdel=clear_family_terms)


    def get_relationship_query_record(self, relationship_record_type):
        """Gets the relationship query record corresponding to the given ``Relationship`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        arg:    relationship_record_type (osid.type.Type): a
                relationship record type
        return: (osid.relationship.records.RelationshipQueryRecord) -
                the relationship query record
        raise:  NullArgument - ``relationship_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported -
                ``has_record_type(relationship_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.relationship.records.RelationshipQueryRecord


class FamilyQuery(osid_queries.OsidCatalogQuery):
    """This is the query interface for searching for families.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    



    def match_relationship_id(self, relationship_id, match):
        """Matches a relationship ``Id``.

        arg:    relationship_id (osid.id.Id): a relationship ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``relationship_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_relationship_id_terms(self):
        """Clears the relationship ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    relationship_id_terms = property(fdel=clear_relationship_id_terms)


    def supports_relationship_query(self):
        """Tests if a relationship query is available.

        return: (boolean) - ``true`` if a relationship query is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_relationship_query(self):
        """Gets the query interface for a relationship.

        return: (osid.relationship.RelationshipQuery) - the relationship
                query
        raise:  Unimplemented - ``supports_relationship_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_relationship_query()`` is ``true``.*

        """
        return # osid.relationship.RelationshipQuery

    relationship_query = property(fget=get_relationship_query)


    def match_any_relationship(self, match):
        """Matches families with any relationship.

        arg:    match (boolean): ``true`` to match families with any
                relationship, ``false`` to match families with no
                relationship
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_relationship_terms(self):
        """Clears the relationship terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    relationship_terms = property(fdel=clear_relationship_terms)


    def match_ancestor_family_id(self, family_id, match):
        """Sets the family ``Id`` for this query to match families that have the specified family as an ancestor.

        arg:    family_id (osid.id.Id): a family ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``family_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_ancestor_family_id_terms(self):
        """Clears the ancestor family ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_family_id_terms = property(fdel=clear_ancestor_family_id_terms)


    def supports_ancestor_family_query(self):
        """Tests if a ``FamilyQuery`` is available.

        return: (boolean) - ``true`` if a family query interface is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_ancestor_family_query(self):
        """Gets the query interface for a family.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.relationship.FamilyQuery) - the family query
        raise:  Unimplemented - ``supports_ancestor_family_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_family_query()`` is ``true``.*

        """
        return # osid.relationship.FamilyQuery

    ancestor_family_query = property(fget=get_ancestor_family_query)


    def match_any_ancestor_family(self, match):
        """Matches families with any ancestor.

        arg:    match (boolean): ``true`` to match families with any
                ancestor, ``false`` to match root families
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_ancestor_family_terms(self):
        """Clears the ancestor family terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_family_terms = property(fdel=clear_ancestor_family_terms)


    def match_descendant_family_id(self, family_id, match):
        """Sets the family ``Id`` for this query to match families that have the specified family as a descednant.

        arg:    family_id (osid.id.Id): a family ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``family_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_descendant_family_id_terms(self):
        """Clears the descendant family ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_family_id_terms = property(fdel=clear_descendant_family_id_terms)


    def supports_descendant_family_query(self):
        """Tests if a ``FamilyQuery`` is available.

        return: (boolean) - ``true`` if a family query interface is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_descendant_family_query(self):
        """Gets the query interface for a family.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.relationship.FamilyQuery) - the family query
        raise:  Unimplemented - ``supports_descendant_family_query()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_descendant_family_query()`` is ``true``.*

        """
        return # osid.relationship.FamilyQuery

    descendant_family_query = property(fget=get_descendant_family_query)


    def match_any_descendant_family(self, match):
        """Matches families with any decendant.

        arg:    match (boolean): ``true`` to match families with any
                decendants, ``false`` to match leaf families
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_descendant_family_terms(self):
        """Clears the descendant family terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_family_terms = property(fdel=clear_descendant_family_terms)


    def get_family_query_record(self, family_record_type):
        """Gets the family query record corresponding to the given ``Family`` record ``Type``.

        Multiple record retrievals produce a nested boolean ``OR`` term.

        arg:    family_record_type (osid.type.Type): a family record
                type
        return: (osid.relationship.records.FamilyQueryRecord) - the
                family query record
        raise:  NullArgument - ``family_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``has_record_type(family_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.relationship.records.FamilyQueryRecord


