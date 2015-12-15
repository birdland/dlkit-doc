

Searches
========


Relationship Search
-------------------

.. py:class:: RelationshipSearch(abc_relationship_searches.RelationshipSearch, osid_searches.OsidSearch)
    The search interface for governing relationship searches.

    .. py:method:: search_among_relationships(relationship_ids):
        :noindex:


    .. py:method:: order_relationship_results(relationship_search_order):
        :noindex:


    .. py:method:: get_relationship_search_record(relationship_search_record_type):
        :noindex:


Relationship Search Results
---------------------------

.. py:class:: RelationshipSearchResults(abc_relationship_searches.RelationshipSearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_relationships():
        :noindex:


    .. py:attribute:: relationships
        :noindex:


    .. py:method:: get_relationship_query_inspector():
        :noindex:


    .. py:attribute:: relationship_query_inspector
        :noindex:


    .. py:method:: get_relationship_search_results_record(relationship_search_record_type):
        :noindex:


Family Search
-------------

.. py:class:: FamilySearch(abc_relationship_searches.FamilySearch, osid_searches.OsidSearch)
    The search interface for governing family searches.

    .. py:method:: search_among_families(family_ids):
        :noindex:


    .. py:method:: order_family_results(family_search_order):
        :noindex:


    .. py:method:: get_family_search_record(family_search_record_type):
        :noindex:


Family Search Results
---------------------

.. py:class:: FamilySearchResults(abc_relationship_searches.FamilySearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search and is used as a vehicle to
        perform a
    search within a previous result set.

    .. py:method:: get_families():
        :noindex:


    .. py:attribute:: families
        :noindex:


    .. py:method:: get_family_query_inspector():
        :noindex:


    .. py:attribute:: family_query_inspector
        :noindex:


    .. py:method:: get_family_search_results_record(family_search_record_type):
        :noindex:


