"""Mongodb implementations of hierarchy queries."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package mongo package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification



from .. import utilities
from ...abstract_osid.hierarchy import queries as abc_hierarchy_queries
from ..osid.osid_errors import Unimplemented
from ..primitives import Id
from dlkit.mongo.osid import queries as osid_queries




class HierarchyQuery(abc_hierarchy_queries.HierarchyQuery, osid_queries.OsidCatalogQuery):
    """This is the query for searching hierarchies.


    Results are returned if all the specified elements match. Each
    method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR,`` except for
    accessing the ``HierarchyQuery`` record.


    """


    def __init__(self, runtime):
        self._runtime = runtime
        record_type_data_sets = self._get_registry('_RECORD_TYPES')
        self._all_supported_record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_ids = []
        for data_set in record_type_data_sets:
            self._all_supported_record_type_ids.append(str(Id(**record_type_data_sets[data_set])))
        osid_queries.OsidCatalogQuery.__init__(self, runtime)
    @utilities.arguments_not_none
    def match_node_id(self, id_, match):
        """Matches an ``Id`` of a node in this hierarchy.


        Multiple nodes can be added to this query which behave as a
        boolean ``AND``.


        arg:    id (osid.id.Id): ``Id`` to match
        arg:    match (boolean): ``true`` if a positive match, ``false``
                for negative match
        raise:  NullArgument - ``id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def match_any_node_id(self, match):
        """Matches hierarchies with any node.


        arg:    match (boolean): ``true`` to match hierarchies with any
                nodes, ``false`` to match hierarchies with no nodes
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    def clear_node_id_terms(self):
        """Clears the node ``Id`` terms.


        *compliance: mandatory -- This method must be implemented.*


        """
        self._clear_terms('nodeId')

    node_id_terms = property(fdel=clear_node_id_terms)

    @utilities.arguments_not_none
    def get_hierarchy_query_record(self, hierarchy_record_type):
        """Gets the hierarchy record query corresponding to the given ``Hierarchy`` record ``Type``.


        Multiple record retrievals of the same type may return the same
        underlying object and do not result in adding terms to the
        query. Multiple record retrievals of different types add ``AND``
        terms to the other elements set in this form.


        arg:    hierarchy_record_type (osid.type.Type): a hierarchy
                record type
        return: (osid.hierarchy.records.HierarchyQueryRecord) - the
                hierarchy query record
        raise:  NullArgument - ``hierarchy_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(hierarchy_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()


