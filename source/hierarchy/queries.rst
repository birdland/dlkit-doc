

Queries
=======


Hierarchy Query
---------------

.. py:class:: HierarchyQuery(abc_hierarchy_queries.HierarchyQuery, osid_queries.OsidCatalogQuery)
    This is the query for searching hierarchies.


    Results are returned if all the specified elements match. Each
    method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR,`` except for
    accessing the ``HierarchyQuery`` record.





    .. py:method:: match_node_id(id_, match):
        :noindex:


    .. py:method:: match_any_node_id(match):
        :noindex:


    .. py:method:: clear_node_id_terms():
        :noindex:


    .. py:attribute:: node_id_terms
        :noindex:


    .. py:method:: get_hierarchy_query_record(hierarchy_record_type):
        :noindex:


