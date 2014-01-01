.. currentmodule:: dlkit.mapping.searches
.. automodule:: dlkit.mapping.searches

Searches
========


Location Search
---------------

.. autoclass:: LocationSearch
   :show-inheritance:

   .. automethod:: LocationSearch.search_among_locations

   .. automethod:: LocationSearch.order_location_results

   .. automethod:: LocationSearch.get_location_search_record



Location Search Results
-----------------------

.. autoclass:: LocationSearchResults
   :show-inheritance:

   .. autoattribute:: LocationSearchResults.locations

   .. autoattribute:: LocationSearchResults.location_query_inspector

   .. automethod:: LocationSearchResults.get_location_search_results_record



Map Search
----------

.. autoclass:: MapSearch
   :show-inheritance:

   .. automethod:: MapSearch.search_among_maps

   .. automethod:: MapSearch.order_map_results

   .. automethod:: MapSearch.get_map_search_record



Map Search Results
------------------

.. autoclass:: MapSearchResults
   :show-inheritance:

   .. autoattribute:: MapSearchResults.maps

   .. autoattribute:: MapSearchResults.map_query_inspector

   .. automethod:: MapSearchResults.get_map_search_results_record



