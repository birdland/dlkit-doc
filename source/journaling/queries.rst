.. currentmodule:: dlkit.journaling.queries
.. automodule:: dlkit.journaling.queries

Queries
=======


Journal Entry Query
-------------------

.. autoclass:: JournalEntryQuery
   :show-inheritance:

   .. automethod:: JournalEntryQuery.match_branch_id

   .. autoattribute:: JournalEntryQuery.branch_id_terms

   .. automethod:: JournalEntryQuery.supports_branch_query

   .. autoattribute:: JournalEntryQuery.branch_query

   .. autoattribute:: JournalEntryQuery.branch_terms

   .. automethod:: JournalEntryQuery.match_source_id

   .. autoattribute:: JournalEntryQuery.source_id_terms

   .. automethod:: JournalEntryQuery.match_version_id

   .. autoattribute:: JournalEntryQuery.version_id_terms

   .. automethod:: JournalEntryQuery.match_timestamp

   .. autoattribute:: JournalEntryQuery.timestamp_terms

   .. automethod:: JournalEntryQuery.match_entries_since

   .. autoattribute:: JournalEntryQuery.entries_since_terms

   .. automethod:: JournalEntryQuery.match_resource_id

   .. autoattribute:: JournalEntryQuery.resource_id_terms

   .. automethod:: JournalEntryQuery.supports_resource_query

   .. autoattribute:: JournalEntryQuery.resource_query

   .. autoattribute:: JournalEntryQuery.resource_terms

   .. automethod:: JournalEntryQuery.match_agent_id

   .. autoattribute:: JournalEntryQuery.agent_id_terms

   .. automethod:: JournalEntryQuery.supports_agent_query

   .. autoattribute:: JournalEntryQuery.agent_query

   .. autoattribute:: JournalEntryQuery.agent_terms

   .. automethod:: JournalEntryQuery.match_journal_id

   .. autoattribute:: JournalEntryQuery.journal_id_terms

   .. automethod:: JournalEntryQuery.supports_journal_query

   .. autoattribute:: JournalEntryQuery.journal_query

   .. autoattribute:: JournalEntryQuery.journal_terms

   .. automethod:: JournalEntryQuery.get_journal_entry_query_record



Branch Query
------------

.. autoclass:: BranchQuery
   :show-inheritance:

   .. automethod:: BranchQuery.match_origin_journal_entry_id

   .. autoattribute:: BranchQuery.origin_journal_entry_id_terms

   .. automethod:: BranchQuery.supports_origin_journal_entry_query

   .. autoattribute:: BranchQuery.origin_journal_entry_query

   .. autoattribute:: BranchQuery.origin_journal_entry_terms

   .. automethod:: BranchQuery.match_latest_journal_entry_id

   .. autoattribute:: BranchQuery.latest_journal_entry_id_terms

   .. automethod:: BranchQuery.supports_latest_journal_entry_query

   .. autoattribute:: BranchQuery.latest_journal_entry_query

   .. autoattribute:: BranchQuery.latest_journal_entry_terms

   .. automethod:: BranchQuery.get_branch_query_record



Journal Query
-------------

.. autoclass:: JournalQuery
   :show-inheritance:

   .. automethod:: JournalQuery.match_journal_entry_id

   .. autoattribute:: JournalQuery.journal_entry_id_terms

   .. automethod:: JournalQuery.supports_journal_entry_query

   .. autoattribute:: JournalQuery.journal_entry_query

   .. automethod:: JournalQuery.match_any_journal_entry

   .. autoattribute:: JournalQuery.journal_entry_terms

   .. automethod:: JournalQuery.match_branch_id

   .. autoattribute:: JournalQuery.branch_id_terms

   .. automethod:: JournalQuery.supports_branch_query

   .. autoattribute:: JournalQuery.branch_query

   .. automethod:: JournalQuery.match_any_branch

   .. autoattribute:: JournalQuery.branch_terms

   .. automethod:: JournalQuery.match_ancestor_journal_id

   .. autoattribute:: JournalQuery.ancestor_journal_id_terms

   .. automethod:: JournalQuery.supports_ancestor_journal_query

   .. autoattribute:: JournalQuery.ancestor_journal_query

   .. automethod:: JournalQuery.match_any_ancestor_journal

   .. autoattribute:: JournalQuery.ancestor_journal_terms

   .. automethod:: JournalQuery.match_descendant_journal_id

   .. autoattribute:: JournalQuery.descendant_journal_id_terms

   .. automethod:: JournalQuery.supports_descendant_journal_query

   .. autoattribute:: JournalQuery.descendant_journal_query

   .. automethod:: JournalQuery.match_any_descendant_journal

   .. autoattribute:: JournalQuery.descendant_journal_terms

   .. automethod:: JournalQuery.get_journal_query_record



