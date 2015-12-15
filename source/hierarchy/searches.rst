

Searches
========


Hierarchy Search
----------------

.. py:class:: HierarchySearch(abc_hierarchy_searches.HierarchySearch, osid_searches.OsidSearch)
    ``HierarchySearch`` defines the interface for specifying hierarchy search options.

    .. py:method:: search_among_hierarchies(hierarchy_ids):
        :noindex:


    .. py:method:: order_hierarchy_results(hierarchy_search_order):
        :noindex:


    .. py:method:: get_hierarchy_search_record(hierarchy_search_record_type):
        :noindex:


Hierarchy Search Results
------------------------

.. py:class:: HierarchySearchResults(abc_hierarchy_searches.HierarchySearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_hierarchies():
        :noindex:


    .. py:attribute:: hierarchies
        :noindex:


    .. py:method:: get_hierarchy_query_inspector():
        :noindex:


    .. py:attribute:: hierarchy_query_inspector
        :noindex:


    .. py:method:: get_hierarchy_search_results_record(hierarchy_search_record_type):
        :noindex:


