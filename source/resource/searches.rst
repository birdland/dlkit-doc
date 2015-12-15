

Searches
========


Resource Search
---------------

.. py:class:: ResourceSearch(abc_resource_searches.ResourceSearch, osid_searches.OsidSearch)
    The search interface for governing resource searches.

    .. py:method:: search_among_resources(resource_ids):
        :noindex:


    .. py:method:: order_resource_results(resource_search_order):
        :noindex:


    .. py:method:: get_resource_search_record(resource_search_record_type):
        :noindex:


Resource Search Results
-----------------------

.. py:class:: ResourceSearchResults(abc_resource_searches.ResourceSearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_resources():
        :noindex:


    .. py:attribute:: resources
        :noindex:


    .. py:method:: get_resource_query_inspector():
        :noindex:


    .. py:attribute:: resource_query_inspector
        :noindex:


    .. py:method:: get_resource_search_results_record(resource_search_record_type):
        :noindex:


Bin Search
----------

.. py:class:: BinSearch(abc_resource_searches.BinSearch, osid_searches.OsidSearch)
    The interface for governing bin searches.

    .. py:method:: search_among_bins(bin_ids):
        :noindex:


    .. py:method:: order_bin_results(bin_search_order):
        :noindex:


    .. py:method:: get_bin_search_record(bin_search_record_type):
        :noindex:


Bin Search Results
------------------

.. py:class:: BinSearchResults(abc_resource_searches.BinSearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_bins():
        :noindex:


    .. py:attribute:: bins
        :noindex:


    .. py:method:: get_bin_query_inspector():
        :noindex:


    .. py:attribute:: bin_query_inspector
        :noindex:


    .. py:method:: get_bin_search_results_record(bin_search_record_type):
        :noindex:


