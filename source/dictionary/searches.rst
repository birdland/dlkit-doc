.. currentmodule:: dlkit.dictionary.searches
.. automodule:: dlkit.dictionary.searches

Searches
========


Entry Search
------------

.. autoclass:: EntrySearch
   :show-inheritance:

   .. automethod:: EntrySearch.search_among_entries

   .. automethod:: EntrySearch.order_entry_results

   .. automethod:: EntrySearch.get_entry_search_record



Entry Search Results
--------------------

.. autoclass:: EntrySearchResults
   :show-inheritance:

   .. autoattribute:: EntrySearchResults.entries

   .. autoattribute:: EntrySearchResults.entry_query_inspector

   .. automethod:: EntrySearchResults.get_entry_search_results_record



Dictionary Search
-----------------

.. autoclass:: DictionarySearch
   :show-inheritance:

   .. automethod:: DictionarySearch.search_among_dictionaries

   .. automethod:: DictionarySearch.order_dictionary_results

   .. automethod:: DictionarySearch.get_dictionary_search_record



Dictionary Search Results
-------------------------

.. autoclass:: DictionarySearchResults
   :show-inheritance:

   .. autoattribute:: DictionarySearchResults.dictionaries

   .. autoattribute:: DictionarySearchResults.dictionary_query_inspector

   .. automethod:: DictionarySearchResults.get_dictionary_search_results_record



