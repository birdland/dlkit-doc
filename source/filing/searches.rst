.. currentmodule:: dlkit.filing.searches
.. automodule:: dlkit.filing.searches

Searches
========


File Search
-----------

.. autoclass:: FileSearch
   :show-inheritance:

   .. automethod:: FileSearch.search_among_files

   .. automethod:: FileSearch.order_file_results

   .. automethod:: FileSearch.get_file_search_record



File Search Results
-------------------

.. autoclass:: FileSearchResults
   :show-inheritance:

   .. autoattribute:: FileSearchResults.files

   .. autoattribute:: FileSearchResults.file_query_inspector

   .. automethod:: FileSearchResults.get_file_search_results_record



Directory Search
----------------

.. autoclass:: DirectorySearch
   :show-inheritance:

   .. automethod:: DirectorySearch.search_among_directories

   .. automethod:: DirectorySearch.order_directory_results

   .. automethod:: DirectorySearch.get_directory_search_record



Directory Search Results
------------------------

.. autoclass:: DirectorySearchResults
   :show-inheritance:

   .. autoattribute:: DirectorySearchResults.directories

   .. autoattribute:: DirectorySearchResults.directory_query_inspector

   .. automethod:: DirectorySearchResults.get_directory_search_results_record



