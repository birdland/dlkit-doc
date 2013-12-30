from ..osid import queries as osid_queries


class RelationshipQuery(osid_queries.OsidRelationshipQuery):
    """This is the query for searching relationships.

    Each method match specifies an ``AND`` term while multiple
    invocations of the same method produce a nested ``OR``.

    """
    def match_source_id(self, peer, match):
        """Matches a relationship peer.

        :param peer: peer ``Id`` to match
        :type peer: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``peer`` is ``null``

        """
        pass

    def clear_source_id_terms(self):
        """Clears the peer ``Id`` terms."""
        pass

    source_id_terms = property(fdel=clear_source_id_terms)

    def match_destination_id(self, peer, match):
        """Matches the other relationship peer.

        :param peer: peer ``Id`` to match
        :type peer: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``peer`` is ``null``

        """
        pass

    def clear_destination_id_terms(self):
        """Clears the other peer ``Id`` terms."""
        pass

    destination_id_terms = property(fdel=clear_destination_id_terms)

    def match_same_peer_id(self, match):
        """Matches circular relationships to the same peer.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def clear_same_peer_id_terms(self):
        """Clears the same peer ``Id`` terms."""
        pass

    same_peer_id_terms = property(fdel=clear_same_peer_id_terms)

    def match_family_id(self, family_id, match):
        """Sets the family ``Id`` for this query.

        :param family_id: a family ``Id``
        :type family_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``

        """
        pass

    def clear_family_id_terms(self):
        """Clears the family ``Id`` terms."""
        pass

    family_id_terms = property(fdel=clear_family_id_terms)

    def supports_family_query(self):
        """Tests if a ``FamilyQuery`` is available.

        :return: ``true`` if a family query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_family_query(self):
        """Gets the query for a family.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the family query
        :rtype: ``osid.relationship.FamilyQuery``
        :raise: ``Unimplemented`` -- ``supports_family_query()`` is ``false``

        """
        return # osid.relationship.FamilyQuery

    family_query = property(fget=get_family_query)

    def clear_family_terms(self):
        """Clears the family terms."""
        pass

    family_terms = property(fdel=clear_family_terms)

    def get_relationship_query_record(self, relationship_record_type):
        """Gets the relationship query record corresponding to the given ``Relationship`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param relationship_record_type: a relationship record type
        :type relationship_record_type: ``osid.type.Type``
        :return: the relationship query record
        :rtype: ``osid.relationship.records.RelationshipQueryRecord``
        :raise: ``NullArgument`` -- ``relationship_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(relationship_record_type)`` is ``false``

        """
        return # osid.relationship.records.RelationshipQueryRecord


class FamilyQuery(osid_queries.OsidCatalogQuery):
    """This is the query interface for searching for families.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def match_relationship_id(self, relationship_id, match):
        """Matches a relationship ``Id``.

        :param relationship_id: a relationship ``Id``
        :type relationship_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``relationship_id`` is ``null``

        """
        pass

    def clear_relationship_id_terms(self):
        """Clears the relationship ``Id`` terms."""
        pass

    relationship_id_terms = property(fdel=clear_relationship_id_terms)

    def supports_relationship_query(self):
        """Tests if a relationship query is available.

        :return: ``true`` if a relationship query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_relationship_query(self):
        """Gets the query interface for a relationship.

        :return: the relationship query
        :rtype: ``osid.relationship.RelationshipQuery``
        :raise: ``Unimplemented`` -- ``supports_relationship_query()`` is ``false``

        """
        return # osid.relationship.RelationshipQuery

    relationship_query = property(fget=get_relationship_query)

    def match_any_relationship(self, match):
        """Matches families with any relationship.

        :param match: ``true`` to match families with any relationship, ``false`` to match families with no relationship
        :type match: ``boolean``

        """
        pass

    def clear_relationship_terms(self):
        """Clears the relationship terms."""
        pass

    relationship_terms = property(fdel=clear_relationship_terms)

    def match_ancestor_family_id(self, family_id, match):
        """Sets the family ``Id`` for this query to match families that have the specified family as an ancestor.

        :param family_id: a family ``Id``
        :type family_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``

        """
        pass

    def clear_ancestor_family_id_terms(self):
        """Clears the ancestor family ``Id`` terms."""
        pass

    ancestor_family_id_terms = property(fdel=clear_ancestor_family_id_terms)

    def supports_ancestor_family_query(self):
        """Tests if a ``FamilyQuery`` is available.

        :return: ``true`` if a family query interface is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_ancestor_family_query(self):
        """Gets the query interface for a family.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the family query
        :rtype: ``osid.relationship.FamilyQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_family_query()`` is ``false``

        """
        return # osid.relationship.FamilyQuery

    ancestor_family_query = property(fget=get_ancestor_family_query)

    def match_any_ancestor_family(self, match):
        """Matches families with any ancestor.

        :param match: ``true`` to match families with any ancestor, ``false`` to match root families
        :type match: ``boolean``

        """
        pass

    def clear_ancestor_family_terms(self):
        """Clears the ancestor family terms."""
        pass

    ancestor_family_terms = property(fdel=clear_ancestor_family_terms)

    def match_descendant_family_id(self, family_id, match):
        """Sets the family ``Id`` for this query to match families that have the specified family as a descednant.

        :param family_id: a family ``Id``
        :type family_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``

        """
        pass

    def clear_descendant_family_id_terms(self):
        """Clears the descendant family ``Id`` terms."""
        pass

    descendant_family_id_terms = property(fdel=clear_descendant_family_id_terms)

    def supports_descendant_family_query(self):
        """Tests if a ``FamilyQuery`` is available.

        :return: ``true`` if a family query interface is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_descendant_family_query(self):
        """Gets the query interface for a family.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the family query
        :rtype: ``osid.relationship.FamilyQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_family_query()`` is ``false``

        """
        return # osid.relationship.FamilyQuery

    descendant_family_query = property(fget=get_descendant_family_query)

    def match_any_descendant_family(self, match):
        """Matches families with any decendant.

        :param match: ``true`` to match families with any decendants, ``false`` to match leaf families
        :type match: ``boolean``

        """
        pass

    def clear_descendant_family_terms(self):
        """Clears the descendant family terms."""
        pass

    descendant_family_terms = property(fdel=clear_descendant_family_terms)

    def get_family_query_record(self, family_record_type):
        """Gets the family query record corresponding to the given ``Family`` record ``Type``.

        Multiple record retrievals produce a nested boolean ``OR`` term.

        :param family_record_type: a family record type
        :type family_record_type: ``osid.type.Type``
        :return: the family query record
        :rtype: ``osid.relationship.records.FamilyQueryRecord``
        :raise: ``NullArgument`` -- ``family_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(family_record_type)`` is ``false``

        """
        return # osid.relationship.records.FamilyQueryRecord

