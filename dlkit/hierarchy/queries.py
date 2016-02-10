
from ..osid import queries as osid_queries


class HierarchyQuery(osid_queries.OsidCatalogQuery):
    """This is the query for searching hierarchies.


    Results are returned if all the specified elements match. Each
    method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR,`` except for
    accessing the ``HierarchyQuery`` record.


    """

    def match_node_id(self, id_, match):
        """Matches an ``Id`` of a node in this hierarchy.


        Multiple nodes can be added to this query which behave as a
        boolean ``AND``.


        :param id: ``Id`` to match
        :type id: ``osid.id.Id``
        :param match: ``true`` if a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``id`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def match_any_node_id(self, match):
        """Matches hierarchies with any node.


        :param match: ``true`` to match hierarchies with any nodes, ``false`` to match hierarchies with no nodes
        :type match: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def clear_node_id_terms(self):
        """Clears the node ``Id`` terms.






        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    node_id_terms = property(fdel=clear_node_id_terms)

    def get_hierarchy_query_record(self, hierarchy_record_type):
        """Gets the hierarchy record query corresponding to the given ``Hierarchy`` record ``Type``.


        Multiple record retrievals of the same type may return the same
        underlying object and do not result in adding terms to the
        query. Multiple record retrievals of different types add ``AND``
        terms to the other elements set in this form.


        :param hierarchy_record_type: a hierarchy record type
        :type hierarchy_record_type: ``osid.type.Type``
        :return: the hierarchy query record
        :rtype: ``osid.hierarchy.records.HierarchyQueryRecord``
        :raise: ``NullArgument`` -- ``hierarchy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(hierarchy_record_type)`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.records.HierarchyQueryRecord


