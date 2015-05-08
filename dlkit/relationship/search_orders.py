from ..osid import search_orders as osid_search_orders


class RelationshipSearchOrder(osid_search_orders.OsidRelationshipSearchOrder):
    """An interface for specifying the ordering of search results."""
    def order_by_source(self, style):
        """Specifies a preference for ordering the result set by the source peer.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_destination(self, style):
        """Specifies a preference for ordering the result set by the destination peer.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def get_relationship_search_order_record(self, relationship_record_type):
        """Gets the relationship search order record corresponding to the given relationship record ``Type``.

        Multiple retrievals return the same underlying object.

        :param relationship_record_type: a relationship record type
        :type relationship_record_type: ``osid.type.Type``
        :return: the relationship search order record
        :rtype: ``osid.relationship.records.RelationshipSearchOrderRecord``
        :raise: ``NullArgument`` -- ``relationship_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(relationship_record_type)`` is ``false``

        """
        return # osid.relationship.records.RelationshipSearchOrderRecord


class FamilySearchOrder(osid_search_orders.OsidCatalogSearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_family_search_order_record(self, family_record_type):
        """Gets the family search record order corresponding to the given family record Type.

        Multiple retrievals return the same underlying object.

        :param family_record_type: a family record type
        :type family_record_type: ``osid.type.Type``
        :return: the family search order record
        :rtype: ``osid.relationship.records.FamilySearchOrderRecord``
        :raise: ``NullArgument`` -- ``family_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(family_record_type)`` is ``false``

        """
        return # osid.relationship.records.FamilySearchOrderRecord


