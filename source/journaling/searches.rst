.. currentmodule:: dlkit.journaling.searches
.. automodule:: dlkit.journaling.searches

Searches
========


Journal Entry Search
--------------------

.. autoclass:: JournalEntrySearch
   :show-inheritance:

   .. automethod:: JournalEntrySearch.search_among_journal_entries

   .. automethod:: JournalEntrySearch.order_journal_entry_results

   .. automethod:: JournalEntrySearch.get_journal_entry_search_record



Journal Entry Search Results
----------------------------

.. autoclass:: JournalEntrySearchResults
   :show-inheritance:

   .. autoattribute:: JournalEntrySearchResults.journal_entries

   .. autoattribute:: JournalEntrySearchResults.journal_entry_query_inspector

   .. automethod:: JournalEntrySearchResults.get_journal_entry_search_results_record



Branch Search
-------------

.. autoclass:: BranchSearch
   :show-inheritance:

   .. automethod:: BranchSearch.search_among_branches

   .. automethod:: BranchSearch.order_branch_results

   .. automethod:: BranchSearch.get_branch_search_record



Branch Search Results
---------------------

.. autoclass:: BranchSearchResults
   :show-inheritance:

   .. autoattribute:: BranchSearchResults.branches

   .. autoattribute:: BranchSearchResults.branch_query_inspector

   .. automethod:: BranchSearchResults.get_branch_search_results_record



Journal Search
--------------

.. autoclass:: JournalSearch
   :show-inheritance:

   .. automethod:: JournalSearch.search_among_journals

   .. automethod:: JournalSearch.order_journal_results

   .. automethod:: JournalSearch.get_journal_search_record



Journal Search Results
----------------------

.. autoclass:: JournalSearchResults
   :show-inheritance:

   .. autoattribute:: JournalSearchResults.journals

   .. autoattribute:: JournalSearchResults.journal_query_inspector

   .. automethod:: JournalSearchResults.get_journal_search_results_record



