
from ..osid import query_inspectors as osid_query_inspectors


class RelationshipQueryInspector(osid_query_inspectors.OsidRelationshipQueryInspector):
    """This is the query inspector for examining relationship queries."""

    def get_source_id_terms(self):
        """Gets the peer ``Id`` terms.

        :return: the peer ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    source_id_terms = property(fget=get_source_id_terms)

    def get_destination_id_terms(self):
        """Gets the other peer ``Id`` terms.

        :return: the other peer ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    destination_id_terms = property(fget=get_destination_id_terms)

    def get_same_peer_id_terms(self):
        """Gets the same peer terms.

        :return: the same peer terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.BooleanTerm

    same_peer_id_terms = property(fget=get_same_peer_id_terms)

    def get_family_id_terms(self):
        """Gets the family ``Id`` terms.

        :return: the family ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    family_id_terms = property(fget=get_family_id_terms)

    def get_family_terms(self):
        """Gets the family terms.

        :return: the family terms
        :rtype: ``osid.relationship.FamilyQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.relationship.FamilyQueryInspector

    family_terms = property(fget=get_family_terms)

    def get_relationship_query_inspector_record(self, relationship_record_type):
        """Gets the relationship query inspector record corresponding to the given ``Relationship`` record ``Type``.

        :param relationship_record_type: a relationship record type
        :type relationship_record_type: ``osid.type.Type``
        :return: the relationship query inspector record
        :rtype: ``osid.relationship.records.RelationshipQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``relationship_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(relationship_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.relationship.records.RelationshipQueryInspectorRecord


class FamilyQueryInspector(osid_query_inspectors.OsidCatalogQueryInspector):
    """This is the query inspector for examining family queries."""

    def get_relationship_id_terms(self):
        """Gets the relationship ``Id`` terms.

        :return: the relationship ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    relationship_id_terms = property(fget=get_relationship_id_terms)

    def get_relationship_terms(self):
        """Gets the relationship terms.

        :return: the relationship terms
        :rtype: ``osid.relationship.RelationshipQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.relationship.RelationshipQueryInspector

    relationship_terms = property(fget=get_relationship_terms)

    def get_ancestor_family_id_terms(self):
        """Gets the ancestor family ``Id`` terms.

        :return: the ancestor family ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    ancestor_family_id_terms = property(fget=get_ancestor_family_id_terms)

    def get_ancestor_family_terms(self):
        """Gets the ancestor family terms.

        :return: the ancestor family terms
        :rtype: ``osid.relationship.FamilyQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.relationship.FamilyQueryInspector

    ancestor_family_terms = property(fget=get_ancestor_family_terms)

    def get_descendant_family_id_terms(self):
        """Gets the descendant family ``Id`` terms.

        :return: the descendant family ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    descendant_family_id_terms = property(fget=get_descendant_family_id_terms)

    def get_descendant_family_terms(self):
        """Gets the descendant family terms.

        :return: the descendant family terms
        :rtype: ``osid.relationship.FamilyQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.relationship.FamilyQueryInspector

    descendant_family_terms = property(fget=get_descendant_family_terms)

    def get_family_query_inspector_record(self, family_record_type):
        """Gets the family query inspector record corresponding to the given ``Family`` record ``Type``.

        :param family_record_type: a family record type
        :type family_record_type: ``osid.type.Type``
        :return: the family query inspector record
        :rtype: ``osid.relationship.records.FamilyQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``family_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(family_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.relationship.records.FamilyQueryInspectorRecord


