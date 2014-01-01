.. currentmodule:: dlkit.repository.searches
.. automodule:: dlkit.repository.searches

Searches
========


Asset Search
------------

.. autoclass:: AssetSearch
   :show-inheritance:

   .. automethod:: AssetSearch.search_among_assets

   .. automethod:: AssetSearch.order_asset_results

   .. automethod:: AssetSearch.get_asset_search_record



Asset Search Results
--------------------

.. autoclass:: AssetSearchResults
   :show-inheritance:

   .. autoattribute:: AssetSearchResults.assets

   .. autoattribute:: AssetSearchResults.asset_query_inspector

   .. automethod:: AssetSearchResults.get_asset_search_results_record



Composition Search
------------------

.. autoclass:: CompositionSearch
   :show-inheritance:

   .. automethod:: CompositionSearch.search_among_compositions

   .. automethod:: CompositionSearch.order_composition_results

   .. automethod:: CompositionSearch.get_composition_search_record



Composition Search Results
--------------------------

.. autoclass:: CompositionSearchResults
   :show-inheritance:

   .. autoattribute:: CompositionSearchResults.compositions

   .. autoattribute:: CompositionSearchResults.composition_query_inspector

   .. automethod:: CompositionSearchResults.get_composition_search_results_record



Repository Search
-----------------

.. autoclass:: RepositorySearch
   :show-inheritance:

   .. automethod:: RepositorySearch.search_among_repositories

   .. automethod:: RepositorySearch.order_repository_results

   .. automethod:: RepositorySearch.get_repository_search_record



Repository Search Results
-------------------------

.. autoclass:: RepositorySearchResults
   :show-inheritance:

   .. autoattribute:: RepositorySearchResults.repositories

   .. autoattribute:: RepositorySearchResults.repository_query_inspector

   .. automethod:: RepositorySearchResults.get_repository_search_results_record



