from ..osid import search_orders as osid_search_orders


class HierarchySearchOrder(osid_search_orders.OsidCatalogSearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_hierarchy_search_order_record(self, hierarchy_record_type):
        """Gets the hierarchy search order record corresponding to the given hierarchy record ``Type``.

        Multiple retrievals return the same underlying object.

        :param hierarchy_record_type: a hierarchy record type
        :type hierarchy_record_type: ``osid.type.Type``
        :return: the hierarchy search order record
        :rtype: ``osid.hierarchy.records.HierarchySearchOrderRecord``
        :raise: ``NullArgument`` -- ``hierarchy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(hierarchy_record_type)`` is ``false``

        """
        return # osid.hierarchy.records.HierarchySearchOrderRecord


