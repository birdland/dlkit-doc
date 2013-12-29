from ..osid import query_inspectors as osid_query_inspectors


class HierarchyQueryInspector(osid_query_inspectors.OsidCatalogQueryInspector):
    """This is the query inspector for examining hierarchy queries."""
    def get_node_id_terms(self):
        """Gets the node ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    node_id_terms = property(fget=get_node_id_terms)

    def get_hierarchy_query_inspector_record(self, hierarchy_record_type):
        """Gets the hierarchy query inspector record corresponding to the given ``Hierarchy`` record ``Type``.

        :param hierarchy_record_type: a hierarchy record type
        :type hierarchy_record_type: ``osid.type.Type``
        :return: the hierarchy query inspector record
        :rtype: ``osid.hierarchy.records.HierarchyQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``hierarchy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(hierarchy_record_type)`` is ``false``

        """
        return # osid.hierarchy.records.HierarchyQueryInspectorRecord


