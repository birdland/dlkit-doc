.. currentmodule:: dlkit.services.dictionary


Dictionary
==========


Dictionary
----------

.. autoclass:: Dictionary
   :show-inheritance:

   .. automethod:: Dictionary.get_dictionary_record



Entry Retrieval Methods
-----------------------

   .. autoattribute:: Dictionary.dictionary_id

   .. autoattribute:: Dictionary.dictionary

   .. automethod:: Dictionary.can_lookup_entries

   .. automethod:: Dictionary.use_federated_dictionary_view

   .. automethod:: Dictionary.use_isolated_dictionary_view

   .. automethod:: Dictionary.retrieve_entry



Entry Lookup Methods
--------------------

   .. automethod:: Dictionary.use_comparative_entry_view

   .. automethod:: Dictionary.use_plenary_entry_view

   .. automethod:: Dictionary.get_entry

   .. automethod:: Dictionary.get_entries_by_ids

   .. automethod:: Dictionary.get_entries_by_genus_type

   .. automethod:: Dictionary.get_entries_by_parent_genus_type

   .. automethod:: Dictionary.get_entries_by_record_type

   .. automethod:: Dictionary.get_entries_by_key_type

   .. automethod:: Dictionary.get_entries_by_key_type_and_value_type

   .. automethod:: Dictionary.get_entries_by_key_and_key_type

   .. autoattribute:: Dictionary.entries



Entry Query Methods
-------------------

   .. autoattribute:: Dictionary.dictionary_id

   .. autoattribute:: Dictionary.dictionary

   .. automethod:: Dictionary.can_search_entries

   .. automethod:: Dictionary.use_federated_dictionary_view

   .. automethod:: Dictionary.use_isolated_dictionary_view

   .. autoattribute:: Dictionary.entry_query

   .. automethod:: Dictionary.get_entries_by_query



Entry Search Methods
--------------------

   .. autoattribute:: Dictionary.entry_search

   .. autoattribute:: Dictionary.entry_search_order

   .. automethod:: Dictionary.get_entries_by_search

   .. automethod:: Dictionary.get_entry_query_from_inspector



Entry Admin Methods
-------------------

   .. autoattribute:: Dictionary.dictionary_id

   .. autoattribute:: Dictionary.dictionary

   .. automethod:: Dictionary.can_create_entries

   .. automethod:: Dictionary.can_create_entry_with_record_types

   .. automethod:: Dictionary.get_entry_form_for_create

   .. automethod:: Dictionary.create_entry

   .. automethod:: Dictionary.can_update_entries

   .. automethod:: Dictionary.get_entry_form_for_update

   .. automethod:: Dictionary.update_entry

   .. automethod:: Dictionary.can_delete_entries

   .. automethod:: Dictionary.delete_entry

   .. automethod:: Dictionary.can_manage_entry_aliases

   .. automethod:: Dictionary.alias_entry



Entry Notification Methods
--------------------------

   .. autoattribute:: Dictionary.dictionary_id

   .. autoattribute:: Dictionary.dictionary

   .. automethod:: Dictionary.can_register_for_entry_notifications

   .. automethod:: Dictionary.use_federated_dictionary_view

   .. automethod:: Dictionary.use_isolated_dictionary_view

   .. automethod:: Dictionary.register_for_new_entries

   .. automethod:: Dictionary.register_for_new_entries_by_key_type_and_value_type

   .. automethod:: Dictionary.register_for_changed_entries

   .. automethod:: Dictionary.register_for_changed_entries_by_key_type_and_value_type

   .. automethod:: Dictionary.register_for_changed_entry

   .. automethod:: Dictionary.register_for_deleted_entries

   .. automethod:: Dictionary.register_for_deleted_entries_by_key_type_and_value_type

   .. automethod:: Dictionary.register_for_deleted_entry



Entry Dictionary Methods
------------------------

   .. automethod:: Dictionary.use_comparative_dictionary_view

   .. automethod:: Dictionary.use_plenary_dictionary_view

   .. automethod:: Dictionary.can_lookup_entry_dictionary_mappings

   .. automethod:: Dictionary.get_entry_ids_by_dictionary

   .. automethod:: Dictionary.get_entries_by_dictionary

   .. automethod:: Dictionary.get_entry_ids_by_dictionaries

   .. automethod:: Dictionary.get_entries_by_dictionaries

   .. automethod:: Dictionary.get_dictionary_ids_by_entry

   .. automethod:: Dictionary.get_dictionaries_by_entry



Entry Dictionary Assignment Methods
-----------------------------------

   .. automethod:: Dictionary.can_assign_entries

   .. automethod:: Dictionary.can_assign_entries_to_dictionary

   .. automethod:: Dictionary.get_assignable_dictionary_ids

   .. automethod:: Dictionary.get_assignable_dictionary_ids_for_entry

   .. automethod:: Dictionary.assign_entry_to_dictionary

   .. automethod:: Dictionary.unassign_entry_from_dictionary



Entry Smart Dictionary Methods
------------------------------

   .. autoattribute:: Dictionary.dictionary_id

   .. autoattribute:: Dictionary.dictionary

   .. automethod:: Dictionary.can_manage_smart_dictionaries

   .. autoattribute:: Dictionary.entry_query

   .. autoattribute:: Dictionary.entry_search_order

   .. automethod:: Dictionary.apply_entry_query

   .. automethod:: Dictionary.inspect_entry_query

   .. automethod:: Dictionary.apply_entry_sequencing

   .. automethod:: Dictionary.get_entry_query_from_inspector



