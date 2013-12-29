.. currentmodule:: dlkit.abstract_osid.resource.searches
.. automodule:: dlkit.abstract_osid.resource.searches

Searches
========


Resource Search
---------------

.. autoclass:: ResourceSearch
   :show-inheritance:

.. automethod:: ResourceSearch.search_among_resources

.. automethod:: ResourceSearch.order_resource_results

.. automethod:: ResourceSearch.get_resource_search_record



Resource Search Results
-----------------------

.. autoclass:: ResourceSearchResults
   :show-inheritance:

.. autoattribute:: ResourceSearchResults.resources

.. autoattribute:: ResourceSearchResults.resource_query_inspector

.. automethod:: ResourceSearchResults.get_resource_search_results_record



Resource Relationship Search
----------------------------

.. autoclass:: ResourceRelationshipSearch
   :show-inheritance:

.. automethod:: ResourceRelationshipSearch.search_among_resource_relationships

.. automethod:: ResourceRelationshipSearch.order_resource_relationship_results

.. automethod:: ResourceRelationshipSearch.get_resource_relationship_search_record



Resource Relationship Search Results
------------------------------------

.. autoclass:: ResourceRelationshipSearchResults
   :show-inheritance:

.. autoattribute:: ResourceRelationshipSearchResults.resource_relationships

.. autoattribute:: ResourceRelationshipSearchResults.resource_relationship_query_inspector

.. automethod:: ResourceRelationshipSearchResults.get_resource_relationship_search_results_record



Bin Search
----------

.. autoclass:: BinSearch
   :show-inheritance:

.. automethod:: BinSearch.search_among_bins

.. automethod:: BinSearch.order_bin_results

.. automethod:: BinSearch.get_bin_search_record



Bin Search Results
------------------

.. autoclass:: BinSearchResults
   :show-inheritance:

.. autoattribute:: BinSearchResults.bins

.. autoattribute:: BinSearchResults.bin_query_inspector

.. automethod:: BinSearchResults.get_bin_search_results_record



