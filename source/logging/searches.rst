.. currentmodule:: dlkit.logging.searches
.. automodule:: dlkit.logging.searches

Searches
========


Log Entry Search
----------------

.. autoclass:: LogEntrySearch
   :show-inheritance:

.. automethod:: LogEntrySearch.search_among_log_entries

.. automethod:: LogEntrySearch.order_log_entry_results

.. automethod:: LogEntrySearch.get_log_entry_search_record



Log Entry Search Results
------------------------

.. autoclass:: LogEntrySearchResults
   :show-inheritance:

.. autoattribute:: LogEntrySearchResults.log_entries

.. autoattribute:: LogEntrySearchResults.log_entry_query_inspector

.. automethod:: LogEntrySearchResults.get_log_entry_search_results_record



Log Search
----------

.. autoclass:: LogSearch
   :show-inheritance:

.. automethod:: LogSearch.search_among_logs

.. automethod:: LogSearch.order_log_results

.. automethod:: LogSearch.get_log_search_record



Log Search Results
------------------

.. autoclass:: LogSearchResults
   :show-inheritance:

.. autoattribute:: LogSearchResults.logs

.. autoattribute:: LogSearchResults.log_query_inspector

.. automethod:: LogSearchResults.get_log_search_results_record



