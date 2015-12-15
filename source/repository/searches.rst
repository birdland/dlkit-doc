

Searches
========


Asset Search
------------

.. py:class:: AssetSearch(abc_repository_searches.AssetSearch, osid_searches.OsidSearch)
    The search interface for governing asset searches.

    .. py:method:: search_among_assets(asset_ids):
        :noindex:


    .. py:method:: order_asset_results(asset_search_order):
        :noindex:


    .. py:method:: get_asset_search_record(asset_search_record_type):
        :noindex:


Asset Search Results
--------------------

.. py:class:: AssetSearchResults(abc_repository_searches.AssetSearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_assets():
        :noindex:


    .. py:attribute:: assets
        :noindex:


    .. py:method:: get_asset_query_inspector():
        :noindex:


    .. py:attribute:: asset_query_inspector
        :noindex:


    .. py:method:: get_asset_search_results_record(asset_search_record_type):
        :noindex:


Composition Search
------------------

.. py:class:: CompositionSearch(abc_repository_searches.CompositionSearch, osid_searches.OsidSearch)
    The interface for governing composition searches.

    .. py:method:: search_among_compositions(composition_ids):
        :noindex:


    .. py:method:: order_composition_results(composition_search_order):
        :noindex:


    .. py:method:: get_composition_search_record(composition_search_record_type):
        :noindex:


Composition Search Results
--------------------------

.. py:class:: CompositionSearchResults(abc_repository_searches.CompositionSearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_compositions():
        :noindex:


    .. py:attribute:: compositions
        :noindex:


    .. py:method:: get_composition_query_inspector():
        :noindex:


    .. py:attribute:: composition_query_inspector
        :noindex:


    .. py:method:: get_composition_search_results_record(composition_search_record_type):
        :noindex:


Repository Search
-----------------

.. py:class:: RepositorySearch(abc_repository_searches.RepositorySearch, osid_searches.OsidSearch)
    The interface for governing repository searches.

    .. py:method:: search_among_repositories(repository_ids):
        :noindex:


    .. py:method:: order_repository_results(repository_search_order):
        :noindex:


    .. py:method:: get_repository_search_record(repository_search_record_type):
        :noindex:


Repository Search Results
-------------------------

.. py:class:: RepositorySearchResults(abc_repository_searches.RepositorySearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_repositories():
        :noindex:


    .. py:attribute:: repositories
        :noindex:


    .. py:method:: get_repository_query_inspector():
        :noindex:


    .. py:attribute:: repository_query_inspector
        :noindex:


    .. py:method:: get_repository_search_results_record(repository_search_record_type):
        :noindex:


