.. currentmodule:: dlkit.journaling.query_inspectors
.. automodule:: dlkit.journaling.query_inspectors

Query Inspectors
================


Journal Entry Query Inspector
-----------------------------

.. autoclass:: JournalEntryQueryInspector
   :show-inheritance:

   .. autoattribute:: JournalEntryQueryInspector.branch_id_terms

   .. autoattribute:: JournalEntryQueryInspector.branch_terms

   .. autoattribute:: JournalEntryQueryInspector.source_id_terms

   .. autoattribute:: JournalEntryQueryInspector.version_id_terms

   .. autoattribute:: JournalEntryQueryInspector.timestamp_terms

   .. autoattribute:: JournalEntryQueryInspector.entries_since_terms

   .. autoattribute:: JournalEntryQueryInspector.resource_id_terms

   .. autoattribute:: JournalEntryQueryInspector.resource_terms

   .. autoattribute:: JournalEntryQueryInspector.agent_id_terms

   .. autoattribute:: JournalEntryQueryInspector.agent_terms

   .. autoattribute:: JournalEntryQueryInspector.journal_id_terms

   .. autoattribute:: JournalEntryQueryInspector.journal_terms

   .. automethod:: JournalEntryQueryInspector.get_journal_entry_query_inspector_record



Branch Query Inspector
----------------------

.. autoclass:: BranchQueryInspector
   :show-inheritance:

   .. autoattribute:: BranchQueryInspector.origin_journal_entry_id_terms

   .. autoattribute:: BranchQueryInspector.origin_journal_entry_terms

   .. autoattribute:: BranchQueryInspector.latest_journal_entry_id_terms

   .. autoattribute:: BranchQueryInspector.latest_journal_entry_terms

   .. automethod:: BranchQueryInspector.get_branch_query_inspector_record



Journal Query Inspector
-----------------------

.. autoclass:: JournalQueryInspector
   :show-inheritance:

   .. autoattribute:: JournalQueryInspector.journal_entry_id_terms

   .. autoattribute:: JournalQueryInspector.journal_entry_terms

   .. autoattribute:: JournalQueryInspector.branch_id_terms

   .. autoattribute:: JournalQueryInspector.branch_terms

   .. autoattribute:: JournalQueryInspector.ancestor_journal_id_terms

   .. autoattribute:: JournalQueryInspector.ancestor_journal_terms

   .. autoattribute:: JournalQueryInspector.descendant_journal_id_terms

   .. autoattribute:: JournalQueryInspector.descendant_journal_terms

   .. automethod:: JournalQueryInspector.get_journal_query_inspector_record



