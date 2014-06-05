.. currentmodule:: dlkit.services.journaling


Journal
=======


Journal
-------

.. autoclass:: Journal
   :show-inheritance:

   .. automethod:: Journal.get_journal_record



Branch Lookup Methods
---------------------

   .. autoattribute:: Journal.journal_id

   .. autoattribute:: Journal.journal

   .. automethod:: Journal.can_lookup_branches

   .. automethod:: Journal.use_comparative_branch_view

   .. automethod:: Journal.use_plenary_branch_view

   .. automethod:: Journal.use_federated_journal_view

   .. automethod:: Journal.use_isolated_journal_view

   .. automethod:: Journal.use_active_branch_view

   .. automethod:: Journal.use_any_status_branch_view

   .. automethod:: Journal.get_branch

   .. automethod:: Journal.get_branches_by_ids

   .. automethod:: Journal.get_branches_by_genus_type

   .. automethod:: Journal.get_branches_by_parent_genus_type

   .. automethod:: Journal.get_branches_by_record_type

   .. autoattribute:: Journal.branches



Branch Query Methods
--------------------

   .. autoattribute:: Journal.journal_id

   .. autoattribute:: Journal.journal

   .. automethod:: Journal.can_search_branches

   .. automethod:: Journal.use_federated_journal_view

   .. automethod:: Journal.use_isolated_journal_view

   .. autoattribute:: Journal.branch_query

   .. automethod:: Journal.get_branches_by_query



Branch Search Methods
---------------------

   .. autoattribute:: Journal.branch_search

   .. autoattribute:: Journal.branch_search_order

   .. automethod:: Journal.get_branches_by_search

   .. automethod:: Journal.get_branch_query_from_inspector



Branch Admin Methods
--------------------

   .. autoattribute:: Journal.journal_id

   .. autoattribute:: Journal.journal

   .. automethod:: Journal.can_create_branches

   .. automethod:: Journal.can_create_branch

   .. automethod:: Journal.can_create_branch_with_record_types

   .. automethod:: Journal.get_branch_form_for_create

   .. automethod:: Journal.create_branch

   .. automethod:: Journal.can_update_branches

   .. automethod:: Journal.get_branch_form_for_update

   .. automethod:: Journal.update_branch

   .. automethod:: Journal.can_merge_branches

   .. automethod:: Journal.merge_branches

   .. automethod:: Journal.can_supersede_branches

   .. automethod:: Journal.supersede_branch

   .. automethod:: Journal.can_delete_branches

   .. automethod:: Journal.delete_branch

   .. automethod:: Journal.can_manage_branch_aliases

   .. automethod:: Journal.alias_branch



Branch Notification Methods
---------------------------

   .. autoattribute:: Journal.journal_id

   .. autoattribute:: Journal.journal

   .. automethod:: Journal.can_register_for_branch_notifications

   .. automethod:: Journal.use_federated_journal_view

   .. automethod:: Journal.use_isolated_journal_view

   .. automethod:: Journal.register_for_new_branches

   .. automethod:: Journal.register_for_changed_branches

   .. automethod:: Journal.register_for_changed_branch

   .. automethod:: Journal.register_for_deleted_branches

   .. automethod:: Journal.register_for_deleted_branch



Branch Smart Journal Methods
----------------------------

   .. autoattribute:: Journal.journal_id

   .. autoattribute:: Journal.journal

   .. automethod:: Journal.can_manage_smart_journals

   .. autoattribute:: Journal.branch_query

   .. autoattribute:: Journal.branch_search_order

   .. automethod:: Journal.apply_branch_query

   .. automethod:: Journal.inspect_branch_query

   .. automethod:: Journal.apply_branch_sequencing

   .. automethod:: Journal.get_branch_query_from_inspector



