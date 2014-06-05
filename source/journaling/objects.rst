.. currentmodule:: dlkit.journaling.objects
.. automodule:: dlkit.journaling.objects

Objects
=======


Journal Entry
-------------

.. autoclass:: JournalEntry
   :show-inheritance:

   .. autoattribute:: JournalEntry.branch_id

   .. autoattribute:: JournalEntry.branch

   .. autoattribute:: JournalEntry.source_id

   .. autoattribute:: JournalEntry.version_id

   .. autoattribute:: JournalEntry.timestamp

   .. autoattribute:: JournalEntry.resource_id

   .. autoattribute:: JournalEntry.resource

   .. autoattribute:: JournalEntry.agent_id

   .. autoattribute:: JournalEntry.agent

   .. automethod:: JournalEntry.get_journal_entry_record



Journal Entry Form
------------------

.. autoclass:: JournalEntryForm
   :show-inheritance:

   .. automethod:: JournalEntryForm.get_journal_entry_form_record



Journal Entry List
------------------

.. autoclass:: JournalEntryList
   :show-inheritance:

   .. autoattribute:: JournalEntryList.next_journal_entry

   .. automethod:: JournalEntryList.get_next_journal_entries



Branch
------

.. autoclass:: Branch
   :show-inheritance:

   .. autoattribute:: Branch.origin_journal_entry_id

   .. autoattribute:: Branch.origin_journal_entry

   .. autoattribute:: Branch.latest_journal_entry_id

   .. autoattribute:: Branch.latest_journal_entry

   .. automethod:: Branch.get_branch_record



Branch Form
-----------

.. autoclass:: BranchForm
   :show-inheritance:

   .. automethod:: BranchForm.get_branch_form_record



Branch List
-----------

.. autoclass:: BranchList
   :show-inheritance:

   .. autoattribute:: BranchList.next_branch

   .. automethod:: BranchList.get_next_branches



Journal Form
------------

.. autoclass:: JournalForm
   :show-inheritance:

   .. automethod:: JournalForm.get_journal_form_record



Journal List
------------

.. autoclass:: JournalList
   :show-inheritance:

   .. autoattribute:: JournalList.next_journal

   .. automethod:: JournalList.get_next_journals



Journal Node
------------

.. autoclass:: JournalNode
   :show-inheritance:

   .. autoattribute:: JournalNode.journal

   .. autoattribute:: JournalNode.parent_journal_nodes

   .. autoattribute:: JournalNode.child_journal_nodes



Journal Node List
-----------------

.. autoclass:: JournalNodeList
   :show-inheritance:

   .. autoattribute:: JournalNodeList.next_journal_node

   .. automethod:: JournalNodeList.get_next_journal_nodes



