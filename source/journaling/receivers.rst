.. currentmodule:: dlkit.journaling.receivers
.. automodule:: dlkit.journaling.receivers

Receivers
=========


Journal Entry Receiver
----------------------

.. autoclass:: JournalEntryReceiver
   :show-inheritance:

   .. automethod:: JournalEntryReceiver.new_journal_entry

   .. automethod:: JournalEntryReceiver.changed_journal_entry

   .. automethod:: JournalEntryReceiver.deleted_journal_entry



Branch Receiver
---------------

.. autoclass:: BranchReceiver
   :show-inheritance:

   .. automethod:: BranchReceiver.new_branch

   .. automethod:: BranchReceiver.changed_branch

   .. automethod:: BranchReceiver.deleted_branch



Journal Receiver
----------------

.. autoclass:: JournalReceiver
   :show-inheritance:

   .. automethod:: JournalReceiver.new_journal

   .. automethod:: JournalReceiver.new_ancestor_journal

   .. automethod:: JournalReceiver.new_descendant_journal

   .. automethod:: JournalReceiver.changed_journal

   .. automethod:: JournalReceiver.deleted_journal

   .. automethod:: JournalReceiver.deleted_ancestor_journal

   .. automethod:: JournalReceiver.deleted_descendant_journal



