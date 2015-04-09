.. currentmodule:: dlkit.journaling.search_orders
.. automodule:: dlkit.journaling.search_orders

Search Orders
=============


Journal Entry Search Order
--------------------------

.. autoclass:: JournalEntrySearchOrder
   :show-inheritance:

   .. automethod:: JournalEntrySearchOrder.order_by_branch

   .. automethod:: JournalEntrySearchOrder.supports_branch_search_order

   .. autoattribute:: JournalEntrySearchOrder.branch_search_order

   .. automethod:: JournalEntrySearchOrder.order_by_source

   .. automethod:: JournalEntrySearchOrder.order_by_timestamp

   .. automethod:: JournalEntrySearchOrder.order_by_resource

   .. automethod:: JournalEntrySearchOrder.supports_resource_search_order

   .. autoattribute:: JournalEntrySearchOrder.resource_search_order

   .. automethod:: JournalEntrySearchOrder.order_by_agent

   .. automethod:: JournalEntrySearchOrder.supports_agent_search_order

   .. autoattribute:: JournalEntrySearchOrder.agent_search_order

   .. automethod:: JournalEntrySearchOrder.get_journal_entry_search_order_record



Branch Search Order
-------------------

.. autoclass:: BranchSearchOrder
   :show-inheritance:

   .. automethod:: BranchSearchOrder.order_by_origin_journal_entry

   .. automethod:: BranchSearchOrder.supports_origin_journal_entry_search_order

   .. autoattribute:: BranchSearchOrder.origin_journal_entry_search_order

   .. automethod:: BranchSearchOrder.order_by_latest_journal_entry

   .. automethod:: BranchSearchOrder.supports_latest_journal_entry_search_order

   .. autoattribute:: BranchSearchOrder.latest_journal_entry_search_order

   .. automethod:: BranchSearchOrder.get_branch_search_order_record



Journal Search Order
--------------------

.. autoclass:: JournalSearchOrder
   :show-inheritance:

   .. automethod:: JournalSearchOrder.get_journal_search_order_record



