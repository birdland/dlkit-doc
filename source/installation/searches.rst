.. currentmodule:: dlkit.installation.searches
.. automodule:: dlkit.installation.searches

Searches
========


Package Search
--------------

.. autoclass:: PackageSearch
   :show-inheritance:

   .. automethod:: PackageSearch.search_among_packages

   .. automethod:: PackageSearch.order_package_results

   .. automethod:: PackageSearch.get_package_search_record



Package Search Results
----------------------

.. autoclass:: PackageSearchResults
   :show-inheritance:

   .. autoattribute:: PackageSearchResults.packages

   .. autoattribute:: PackageSearchResults.package_query_inspector

   .. automethod:: PackageSearchResults.get_package_search_results_record



Depot Search
------------

.. autoclass:: DepotSearch
   :show-inheritance:

   .. automethod:: DepotSearch.search_among_depots

   .. automethod:: DepotSearch.order_depot_results

   .. automethod:: DepotSearch.get_depot_search_record



Depot Search Results
--------------------

.. autoclass:: DepotSearchResults
   :show-inheritance:

   .. autoattribute:: DepotSearchResults.depots

   .. autoattribute:: DepotSearchResults.depot_query_inspector

   .. automethod:: DepotSearchResults.get_depot_search_results_record



Installation Search
-------------------

.. autoclass:: InstallationSearch
   :show-inheritance:

   .. automethod:: InstallationSearch.search_among_installations

   .. automethod:: InstallationSearch.order_installation_results

   .. automethod:: InstallationSearch.get_installation_search_record



Installation Search Results
---------------------------

.. autoclass:: InstallationSearchResults
   :show-inheritance:

   .. autoattribute:: InstallationSearchResults.installations

   .. autoattribute:: InstallationSearchResults.installation_query_inspector

   .. automethod:: InstallationSearchResults.get_installation_search_results_record



