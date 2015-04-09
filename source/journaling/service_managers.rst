Summary
=======
.. currentmodule:: dlkit.services.journaling
.. automodule:: dlkit.services.journaling

Service Managers
================


Journaling Manager
------------------

.. autoclass:: JournalingManager
   :show-inheritance:

   .. autoattribute:: JournalingManager.journaling_batch_manager



Journaling Profile Methods
__________________

   .. automethod:: JournalingManager.supports_visible_federation

   .. automethod:: JournalingManager.supports_journal_entry_lookup

   .. automethod:: JournalingManager.supports_journal_entry_query

   .. automethod:: JournalingManager.supports_journal_entry_search

   .. automethod:: JournalingManager.supports_journal_entry_admin

   .. automethod:: JournalingManager.supports_journal_entry_notification

   .. automethod:: JournalingManager.supports_branch_lookup

   .. automethod:: JournalingManager.supports_branch_query

   .. automethod:: JournalingManager.supports_branch_search

   .. automethod:: JournalingManager.supports_branch_admin

   .. automethod:: JournalingManager.supports_branch_notification

   .. automethod:: JournalingManager.supports_branch_smart_journal

   .. automethod:: JournalingManager.supports_journal_lookup

   .. automethod:: JournalingManager.supports_journal_query

   .. automethod:: JournalingManager.supports_journal_search

   .. automethod:: JournalingManager.supports_journal_admin

   .. automethod:: JournalingManager.supports_journal_notification

   .. automethod:: JournalingManager.supports_journal_hierarchy

   .. automethod:: JournalingManager.supports_journal_hierarchy_design

   .. automethod:: JournalingManager.supports_journalng_batch

   .. autoattribute:: JournalingManager.journal_entry_record_types

   .. automethod:: JournalingManager.supports_journal_entry_record_type

   .. autoattribute:: JournalingManager.journal_entry_search_record_types

   .. automethod:: JournalingManager.supports_journal_entry_search_record_type

   .. autoattribute:: JournalingManager.branch_record_types

   .. automethod:: JournalingManager.supports_branch_record_type

   .. autoattribute:: JournalingManager.branch_search_record_types

   .. automethod:: JournalingManager.supports_branch_search_record_type

   .. autoattribute:: JournalingManager.journal_record_types

   .. automethod:: JournalingManager.supports_journal_record_type

   .. autoattribute:: JournalingManager.journal_search_record_types

   .. automethod:: JournalingManager.supports_journal_search_record_type



Journal Entry Lookup
____________________

   .. autoattribute:: JournalingManager.journal_id

   .. autoattribute:: JournalingManager.journal

   .. automethod:: JournalingManager.can_read_journal

   .. automethod:: JournalingManager.use_comparative_journal_entry_view

   .. automethod:: JournalingManager.use_plenary_journal_entry_view

   .. automethod:: JournalingManager.use_federated_journal_view

   .. automethod:: JournalingManager.use_isolated_journal_view

   .. automethod:: JournalingManager.get_journal_entry

   .. automethod:: JournalingManager.get_journal_entries_by_ids

   .. automethod:: JournalingManager.get_journal_entries_by_genus_type

   .. automethod:: JournalingManager.get_journal_entries_by_parent_genus_type

   .. automethod:: JournalingManager.get_journal_entries_by_record_type

   .. automethod:: JournalingManager.get_journal_entries_for_branch

   .. automethod:: JournalingManager.get_journal_entries_by_date_for_branch

   .. automethod:: JournalingManager.get_journal_entries_by_date_range_for_branch

   .. automethod:: JournalingManager.get_journal_entries_for_source

   .. automethod:: JournalingManager.get_journal_entries_by_date_for_source

   .. automethod:: JournalingManager.get_journal_entries_by_date_range_for_source

   .. automethod:: JournalingManager.get_journal_entries_for_branch_and_source

   .. automethod:: JournalingManager.get_journal_entries_by_date_for_branch_and_source

   .. automethod:: JournalingManager.get_journal_entries_by_date_range_for_branch_and_source

   .. automethod:: JournalingManager.get_journal_entries_for_resource

   .. automethod:: JournalingManager.get_journal_entries_by_date_for_resource

   .. automethod:: JournalingManager.get_journal_entries_by_date_range_for_resource

   .. autoattribute:: JournalingManager.journal_entries



Journal Entry Query
___________________

   .. autoattribute:: JournalingManager.journal_id

   .. autoattribute:: JournalingManager.journal

   .. automethod:: JournalingManager.can_search_journal_entries

   .. automethod:: JournalingManager.use_federated_journal_view

   .. automethod:: JournalingManager.use_isolated_journal_view

   .. autoattribute:: JournalingManager.journal_entry_query

   .. automethod:: JournalingManager.get_journal_entries_by_query



Journal Entry Search
____________________

   .. autoattribute:: JournalingManager.journal_entry_search

   .. autoattribute:: JournalingManager.journal_entry_search_order

   .. automethod:: JournalingManager.get_journal_entries_by_search

   .. automethod:: JournalingManager.get_journal_entry_query_from_inspector



Journal Entry Admin
___________________

   .. autoattribute:: JournalingManager.journal_id

   .. autoattribute:: JournalingManager.journal

   .. automethod:: JournalingManager.can_create_journal_entries

   .. automethod:: JournalingManager.can_create_journal_entry_with_record_types

   .. automethod:: JournalingManager.get_journal_entry_form_for_create

   .. automethod:: JournalingManager.create_journal_entry

   .. automethod:: JournalingManager.can_update_journal_entries

   .. automethod:: JournalingManager.get_journal_entry_form_for_update

   .. automethod:: JournalingManager.update_journal_entry

   .. automethod:: JournalingManager.can_delete_journal_entries

   .. automethod:: JournalingManager.delete_journal_entry

   .. automethod:: JournalingManager.can_manage_journal_entry_aliases

   .. automethod:: JournalingManager.alias_journal_entry



Journal Entry Notification
__________________________

   .. autoattribute:: JournalingManager.journal_id

   .. autoattribute:: JournalingManager.journal

   .. automethod:: JournalingManager.can_register_for_journal_entry_notifications

   .. automethod:: JournalingManager.use_federated_journal_view

   .. automethod:: JournalingManager.use_isolated_journal_view

   .. automethod:: JournalingManager.register_for_new_journal_entries

   .. automethod:: JournalingManager.register_for_new_journal_entries_for_branch

   .. automethod:: JournalingManager.register_for_new_journal_entries_for_source

   .. automethod:: JournalingManager.register_for_new_journal_entries_for_resource

   .. automethod:: JournalingManager.register_for_changed_journal_entries

   .. automethod:: JournalingManager.register_for_changed_journal_entries_for_branch

   .. automethod:: JournalingManager.register_for_changed_journal_entries_for_source

   .. automethod:: JournalingManager.register_for_changed_journal_entries_for_resource

   .. automethod:: JournalingManager.register_for_changed_journal_entry

   .. automethod:: JournalingManager.register_for_deleted_journal_entries

   .. automethod:: JournalingManager.register_for_deleted_journal_entries_for_branch

   .. automethod:: JournalingManager.register_for_deleted_journal_entries_for_source

   .. automethod:: JournalingManager.register_for_deleted_journal_entries_for_resource

   .. automethod:: JournalingManager.register_for_deleted_journal_entry



Journal Lookup
______________

   .. automethod:: JournalingManager.can_lookup_journals

   .. automethod:: JournalingManager.use_comparative_journal_view

   .. automethod:: JournalingManager.use_plenary_journal_view

   .. automethod:: JournalingManager.get_journal

   .. automethod:: JournalingManager.get_journals_by_ids

   .. automethod:: JournalingManager.get_journals_by_genus_type

   .. automethod:: JournalingManager.get_journals_by_parent_genus_type

   .. automethod:: JournalingManager.get_journals_by_record_type

   .. automethod:: JournalingManager.get_journals_by_provider

   .. autoattribute:: JournalingManager.journals



Journal Query
_____________

   .. automethod:: JournalingManager.can_search_journals

   .. autoattribute:: JournalingManager.journal_query

   .. automethod:: JournalingManager.get_journals_by_query



Journal Search
______________

   .. autoattribute:: JournalingManager.journal_search

   .. autoattribute:: JournalingManager.journal_search_order

   .. automethod:: JournalingManager.get_journals_by_search

   .. automethod:: JournalingManager.get_journal_query_from_inspector



Journal Admin
_____________

   .. automethod:: JournalingManager.can_create_journals

   .. automethod:: JournalingManager.can_create_journal_with_record_types

   .. automethod:: JournalingManager.get_journal_form_for_create

   .. automethod:: JournalingManager.create_journal

   .. automethod:: JournalingManager.can_update_journals

   .. automethod:: JournalingManager.get_journal_form_for_update

   .. automethod:: JournalingManager.update_journal

   .. automethod:: JournalingManager.can_delete_journals

   .. automethod:: JournalingManager.delete_journal

   .. automethod:: JournalingManager.can_manage_journal_aliases

   .. automethod:: JournalingManager.alias_journal



Journal Notification
____________________

   .. automethod:: JournalingManager.can_register_for_journal_notifications

   .. automethod:: JournalingManager.register_for_new_journals

   .. automethod:: JournalingManager.register_for_new_journal_ancestors

   .. automethod:: JournalingManager.register_for_new_journal_descendants

   .. automethod:: JournalingManager.register_for_changed_journals

   .. automethod:: JournalingManager.register_for_changed_journal

   .. automethod:: JournalingManager.register_for_deleted_journals

   .. automethod:: JournalingManager.register_for_deleted_journal

   .. automethod:: JournalingManager.register_for_deleted_journal_ancestors

   .. automethod:: JournalingManager.register_for_deleted_journal_descendants



Journal Hierarchy
_________________

   .. autoattribute:: JournalingManager.journal_hierarchy_id

   .. autoattribute:: JournalingManager.journal_hierarchy

   .. automethod:: JournalingManager.can_access_journal_hierarchy

   .. automethod:: JournalingManager.use_comparative_journal_view

   .. automethod:: JournalingManager.use_plenary_journal_view

   .. autoattribute:: JournalingManager.root_journal_ids

   .. autoattribute:: JournalingManager.root_journals

   .. automethod:: JournalingManager.has_parent_journals

   .. automethod:: JournalingManager.is_parent_of_journal

   .. automethod:: JournalingManager.get_parent_journal_ids

   .. automethod:: JournalingManager.get_parent_journals

   .. automethod:: JournalingManager.is_ancestor_of_journal

   .. automethod:: JournalingManager.has_child_journals

   .. automethod:: JournalingManager.is_child_of_journal

   .. automethod:: JournalingManager.get_child_journal_ids

   .. automethod:: JournalingManager.get_child_journals

   .. automethod:: JournalingManager.is_descendant_of_journal

   .. automethod:: JournalingManager.get_journal_node_ids

   .. automethod:: JournalingManager.get_journal_nodes



Journal Hierarchy Design
________________________

   .. autoattribute:: JournalingManager.journal_hierarchy_id

   .. autoattribute:: JournalingManager.journal_hierarchy

   .. automethod:: JournalingManager.can_modify_journal_hierarchy

   .. automethod:: JournalingManager.add_root_journal

   .. automethod:: JournalingManager.remove_root_journal

   .. automethod:: JournalingManager.add_child_journal

   .. automethod:: JournalingManager.remove_child_journal

   .. automethod:: JournalingManager.remove_child_journals



Journaling Proxy Manager
------------------------

.. autoclass:: JournalingProxyManager
   :show-inheritance:

   .. autoattribute:: JournalingProxyManager.journaling_batch_proxy_manager



Journaling Profile Methods
__________________

   .. automethod:: JournalingProxyManager.supports_visible_federation

   .. automethod:: JournalingProxyManager.supports_journal_entry_lookup

   .. automethod:: JournalingProxyManager.supports_journal_entry_query

   .. automethod:: JournalingProxyManager.supports_journal_entry_search

   .. automethod:: JournalingProxyManager.supports_journal_entry_admin

   .. automethod:: JournalingProxyManager.supports_journal_entry_notification

   .. automethod:: JournalingProxyManager.supports_branch_lookup

   .. automethod:: JournalingProxyManager.supports_branch_query

   .. automethod:: JournalingProxyManager.supports_branch_search

   .. automethod:: JournalingProxyManager.supports_branch_admin

   .. automethod:: JournalingProxyManager.supports_branch_notification

   .. automethod:: JournalingProxyManager.supports_branch_smart_journal

   .. automethod:: JournalingProxyManager.supports_journal_lookup

   .. automethod:: JournalingProxyManager.supports_journal_query

   .. automethod:: JournalingProxyManager.supports_journal_search

   .. automethod:: JournalingProxyManager.supports_journal_admin

   .. automethod:: JournalingProxyManager.supports_journal_notification

   .. automethod:: JournalingProxyManager.supports_journal_hierarchy

   .. automethod:: JournalingProxyManager.supports_journal_hierarchy_design

   .. automethod:: JournalingProxyManager.supports_journalng_batch

   .. autoattribute:: JournalingProxyManager.journal_entry_record_types

   .. automethod:: JournalingProxyManager.supports_journal_entry_record_type

   .. autoattribute:: JournalingProxyManager.journal_entry_search_record_types

   .. automethod:: JournalingProxyManager.supports_journal_entry_search_record_type

   .. autoattribute:: JournalingProxyManager.branch_record_types

   .. automethod:: JournalingProxyManager.supports_branch_record_type

   .. autoattribute:: JournalingProxyManager.branch_search_record_types

   .. automethod:: JournalingProxyManager.supports_branch_search_record_type

   .. autoattribute:: JournalingProxyManager.journal_record_types

   .. automethod:: JournalingProxyManager.supports_journal_record_type

   .. autoattribute:: JournalingProxyManager.journal_search_record_types

   .. automethod:: JournalingProxyManager.supports_journal_search_record_type



Journal Entry Lookup
____________________

   .. autoattribute:: JournalingProxyManager.journal_id

   .. autoattribute:: JournalingProxyManager.journal

   .. automethod:: JournalingProxyManager.can_read_journal

   .. automethod:: JournalingProxyManager.use_comparative_journal_entry_view

   .. automethod:: JournalingProxyManager.use_plenary_journal_entry_view

   .. automethod:: JournalingProxyManager.use_federated_journal_view

   .. automethod:: JournalingProxyManager.use_isolated_journal_view

   .. automethod:: JournalingProxyManager.get_journal_entry

   .. automethod:: JournalingProxyManager.get_journal_entries_by_ids

   .. automethod:: JournalingProxyManager.get_journal_entries_by_genus_type

   .. automethod:: JournalingProxyManager.get_journal_entries_by_parent_genus_type

   .. automethod:: JournalingProxyManager.get_journal_entries_by_record_type

   .. automethod:: JournalingProxyManager.get_journal_entries_for_branch

   .. automethod:: JournalingProxyManager.get_journal_entries_by_date_for_branch

   .. automethod:: JournalingProxyManager.get_journal_entries_by_date_range_for_branch

   .. automethod:: JournalingProxyManager.get_journal_entries_for_source

   .. automethod:: JournalingProxyManager.get_journal_entries_by_date_for_source

   .. automethod:: JournalingProxyManager.get_journal_entries_by_date_range_for_source

   .. automethod:: JournalingProxyManager.get_journal_entries_for_branch_and_source

   .. automethod:: JournalingProxyManager.get_journal_entries_by_date_for_branch_and_source

   .. automethod:: JournalingProxyManager.get_journal_entries_by_date_range_for_branch_and_source

   .. automethod:: JournalingProxyManager.get_journal_entries_for_resource

   .. automethod:: JournalingProxyManager.get_journal_entries_by_date_for_resource

   .. automethod:: JournalingProxyManager.get_journal_entries_by_date_range_for_resource

   .. autoattribute:: JournalingProxyManager.journal_entries



Journal Entry Query
___________________

   .. autoattribute:: JournalingProxyManager.journal_id

   .. autoattribute:: JournalingProxyManager.journal

   .. automethod:: JournalingProxyManager.can_search_journal_entries

   .. automethod:: JournalingProxyManager.use_federated_journal_view

   .. automethod:: JournalingProxyManager.use_isolated_journal_view

   .. autoattribute:: JournalingProxyManager.journal_entry_query

   .. automethod:: JournalingProxyManager.get_journal_entries_by_query



Journal Entry Search
____________________

   .. autoattribute:: JournalingProxyManager.journal_entry_search

   .. autoattribute:: JournalingProxyManager.journal_entry_search_order

   .. automethod:: JournalingProxyManager.get_journal_entries_by_search

   .. automethod:: JournalingProxyManager.get_journal_entry_query_from_inspector



Journal Entry Admin
___________________

   .. autoattribute:: JournalingProxyManager.journal_id

   .. autoattribute:: JournalingProxyManager.journal

   .. automethod:: JournalingProxyManager.can_create_journal_entries

   .. automethod:: JournalingProxyManager.can_create_journal_entry_with_record_types

   .. automethod:: JournalingProxyManager.get_journal_entry_form_for_create

   .. automethod:: JournalingProxyManager.create_journal_entry

   .. automethod:: JournalingProxyManager.can_update_journal_entries

   .. automethod:: JournalingProxyManager.get_journal_entry_form_for_update

   .. automethod:: JournalingProxyManager.update_journal_entry

   .. automethod:: JournalingProxyManager.can_delete_journal_entries

   .. automethod:: JournalingProxyManager.delete_journal_entry

   .. automethod:: JournalingProxyManager.can_manage_journal_entry_aliases

   .. automethod:: JournalingProxyManager.alias_journal_entry



Journal Entry Notification
__________________________

   .. autoattribute:: JournalingProxyManager.journal_id

   .. autoattribute:: JournalingProxyManager.journal

   .. automethod:: JournalingProxyManager.can_register_for_journal_entry_notifications

   .. automethod:: JournalingProxyManager.use_federated_journal_view

   .. automethod:: JournalingProxyManager.use_isolated_journal_view

   .. automethod:: JournalingProxyManager.register_for_new_journal_entries

   .. automethod:: JournalingProxyManager.register_for_new_journal_entries_for_branch

   .. automethod:: JournalingProxyManager.register_for_new_journal_entries_for_source

   .. automethod:: JournalingProxyManager.register_for_new_journal_entries_for_resource

   .. automethod:: JournalingProxyManager.register_for_changed_journal_entries

   .. automethod:: JournalingProxyManager.register_for_changed_journal_entries_for_branch

   .. automethod:: JournalingProxyManager.register_for_changed_journal_entries_for_source

   .. automethod:: JournalingProxyManager.register_for_changed_journal_entries_for_resource

   .. automethod:: JournalingProxyManager.register_for_changed_journal_entry

   .. automethod:: JournalingProxyManager.register_for_deleted_journal_entries

   .. automethod:: JournalingProxyManager.register_for_deleted_journal_entries_for_branch

   .. automethod:: JournalingProxyManager.register_for_deleted_journal_entries_for_source

   .. automethod:: JournalingProxyManager.register_for_deleted_journal_entries_for_resource

   .. automethod:: JournalingProxyManager.register_for_deleted_journal_entry



Journal Lookup
______________

   .. automethod:: JournalingProxyManager.can_lookup_journals

   .. automethod:: JournalingProxyManager.use_comparative_journal_view

   .. automethod:: JournalingProxyManager.use_plenary_journal_view

   .. automethod:: JournalingProxyManager.get_journal

   .. automethod:: JournalingProxyManager.get_journals_by_ids

   .. automethod:: JournalingProxyManager.get_journals_by_genus_type

   .. automethod:: JournalingProxyManager.get_journals_by_parent_genus_type

   .. automethod:: JournalingProxyManager.get_journals_by_record_type

   .. automethod:: JournalingProxyManager.get_journals_by_provider

   .. autoattribute:: JournalingProxyManager.journals



Journal Query
_____________

   .. automethod:: JournalingProxyManager.can_search_journals

   .. autoattribute:: JournalingProxyManager.journal_query

   .. automethod:: JournalingProxyManager.get_journals_by_query



Journal Search
______________

   .. autoattribute:: JournalingProxyManager.journal_search

   .. autoattribute:: JournalingProxyManager.journal_search_order

   .. automethod:: JournalingProxyManager.get_journals_by_search

   .. automethod:: JournalingProxyManager.get_journal_query_from_inspector



Journal Admin
_____________

   .. automethod:: JournalingProxyManager.can_create_journals

   .. automethod:: JournalingProxyManager.can_create_journal_with_record_types

   .. automethod:: JournalingProxyManager.get_journal_form_for_create

   .. automethod:: JournalingProxyManager.create_journal

   .. automethod:: JournalingProxyManager.can_update_journals

   .. automethod:: JournalingProxyManager.get_journal_form_for_update

   .. automethod:: JournalingProxyManager.update_journal

   .. automethod:: JournalingProxyManager.can_delete_journals

   .. automethod:: JournalingProxyManager.delete_journal

   .. automethod:: JournalingProxyManager.can_manage_journal_aliases

   .. automethod:: JournalingProxyManager.alias_journal



Journal Notification
____________________

   .. automethod:: JournalingProxyManager.can_register_for_journal_notifications

   .. automethod:: JournalingProxyManager.register_for_new_journals

   .. automethod:: JournalingProxyManager.register_for_new_journal_ancestors

   .. automethod:: JournalingProxyManager.register_for_new_journal_descendants

   .. automethod:: JournalingProxyManager.register_for_changed_journals

   .. automethod:: JournalingProxyManager.register_for_changed_journal

   .. automethod:: JournalingProxyManager.register_for_deleted_journals

   .. automethod:: JournalingProxyManager.register_for_deleted_journal

   .. automethod:: JournalingProxyManager.register_for_deleted_journal_ancestors

   .. automethod:: JournalingProxyManager.register_for_deleted_journal_descendants



Journal Hierarchy
_________________

   .. autoattribute:: JournalingProxyManager.journal_hierarchy_id

   .. autoattribute:: JournalingProxyManager.journal_hierarchy

   .. automethod:: JournalingProxyManager.can_access_journal_hierarchy

   .. automethod:: JournalingProxyManager.use_comparative_journal_view

   .. automethod:: JournalingProxyManager.use_plenary_journal_view

   .. autoattribute:: JournalingProxyManager.root_journal_ids

   .. autoattribute:: JournalingProxyManager.root_journals

   .. automethod:: JournalingProxyManager.has_parent_journals

   .. automethod:: JournalingProxyManager.is_parent_of_journal

   .. automethod:: JournalingProxyManager.get_parent_journal_ids

   .. automethod:: JournalingProxyManager.get_parent_journals

   .. automethod:: JournalingProxyManager.is_ancestor_of_journal

   .. automethod:: JournalingProxyManager.has_child_journals

   .. automethod:: JournalingProxyManager.is_child_of_journal

   .. automethod:: JournalingProxyManager.get_child_journal_ids

   .. automethod:: JournalingProxyManager.get_child_journals

   .. automethod:: JournalingProxyManager.is_descendant_of_journal

   .. automethod:: JournalingProxyManager.get_journal_node_ids

   .. automethod:: JournalingProxyManager.get_journal_nodes



Journal Hierarchy Design
________________________

   .. autoattribute:: JournalingProxyManager.journal_hierarchy_id

   .. autoattribute:: JournalingProxyManager.journal_hierarchy

   .. automethod:: JournalingProxyManager.can_modify_journal_hierarchy

   .. automethod:: JournalingProxyManager.add_root_journal

   .. automethod:: JournalingProxyManager.remove_root_journal

   .. automethod:: JournalingProxyManager.add_child_journal

   .. automethod:: JournalingProxyManager.remove_child_journal

   .. automethod:: JournalingProxyManager.remove_child_journals



