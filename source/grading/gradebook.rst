.. currentmodule:: dlkit.services.grading


Gradebook
=========


Gradebook
---------

.. autoclass:: Gradebook
   :show-inheritance:

   .. automethod:: Gradebook.get_gradebook_record



Grade System Lookup Methods
---------------------------

   .. autoattribute:: Gradebook.gradebook_id

   .. autoattribute:: Gradebook.gradebook

   .. automethod:: Gradebook.can_lookup_grade_systems

   .. automethod:: Gradebook.use_comparative_grade_system_view

   .. automethod:: Gradebook.use_plenary_grade_system_view

   .. automethod:: Gradebook.use_federated_gradebook_view

   .. automethod:: Gradebook.use_isolated_gradebook_view

   .. automethod:: Gradebook.get_grade_system

   .. automethod:: Gradebook.get_grade_system_by_grade

   .. automethod:: Gradebook.get_grade_systems_by_ids

   .. automethod:: Gradebook.get_grade_systems_by_genus_type

   .. automethod:: Gradebook.get_grade_systems_by_parent_genus_type

   .. automethod:: Gradebook.get_grade_systems_by_record_type

   .. autoattribute:: Gradebook.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: Gradebook.gradebook_id

   .. autoattribute:: Gradebook.gradebook

   .. automethod:: Gradebook.can_search_grade_systems

   .. automethod:: Gradebook.use_federated_gradebook_view

   .. automethod:: Gradebook.use_isolated_gradebook_view

   .. autoattribute:: Gradebook.grade_system_query

   .. automethod:: Gradebook.get_grade_systems_by_query



Grade System Search Methods
---------------------------

   .. autoattribute:: Gradebook.grade_system_search

   .. autoattribute:: Gradebook.grade_system_search_order

   .. automethod:: Gradebook.get_grade_systems_by_search

   .. automethod:: Gradebook.get_grade_system_query_from_inspector



Grade System Admin Methods
--------------------------

   .. autoattribute:: Gradebook.gradebook_id

   .. autoattribute:: Gradebook.gradebook

   .. automethod:: Gradebook.can_create_grade_systems

   .. automethod:: Gradebook.can_create_grade_system_with_record_types

   .. automethod:: Gradebook.get_grade_system_form_for_create

   .. automethod:: Gradebook.create_grade_system

   .. automethod:: Gradebook.can_update_grade_systems

   .. automethod:: Gradebook.get_grade_system_form_for_update

   .. automethod:: Gradebook.update_grade_system

   .. automethod:: Gradebook.can_delete_grade_systems

   .. automethod:: Gradebook.delete_grade_system

   .. automethod:: Gradebook.can_manage_grade_system_aliases

   .. automethod:: Gradebook.alias_grade_system

   .. automethod:: Gradebook.can_create_grades

   .. automethod:: Gradebook.can_create_grade_with_record_types

   .. automethod:: Gradebook.get_grade_form_for_create

   .. automethod:: Gradebook.create_grade

   .. automethod:: Gradebook.can_update_grades

   .. automethod:: Gradebook.get_grade_form_for_update

   .. automethod:: Gradebook.update_grade

   .. automethod:: Gradebook.can_delete_grades

   .. automethod:: Gradebook.delete_grade

   .. automethod:: Gradebook.can_manage_grade_aliases

   .. automethod:: Gradebook.alias_grade



Grade System Notification Methods
---------------------------------

   .. autoattribute:: Gradebook.gradebook_id

   .. autoattribute:: Gradebook.gradebook

   .. automethod:: Gradebook.can_register_for_grade_system_notifications

   .. automethod:: Gradebook.use_federated_gradebook_view

   .. automethod:: Gradebook.use_isolated_gradebook_view

   .. automethod:: Gradebook.register_for_new_grade_systems

   .. automethod:: Gradebook.register_for_changed_grade_systems

   .. automethod:: Gradebook.register_for_changed_grade_system

   .. automethod:: Gradebook.register_for_deleted_grade_systems

   .. automethod:: Gradebook.register_for_deleted_grade_system



Grade System Gradebook Methods
------------------------------

   .. automethod:: Gradebook.use_comparative_gradebook_view

   .. automethod:: Gradebook.use_plenary_gradebook_view

   .. automethod:: Gradebook.can_lookup_grade_system_gradebook_mappings

   .. automethod:: Gradebook.get_grade_system_ids_by_gradebook

   .. automethod:: Gradebook.get_grade_systems_by_gradebook

   .. automethod:: Gradebook.get_grade_system_ids_by_gradebooks

   .. automethod:: Gradebook.get_grade_systems_by_gradebooks

   .. automethod:: Gradebook.get_gradebook_ids_by_grade_system

   .. automethod:: Gradebook.get_gradebooks_by_grade_system



Grade System Gradebook Assignment Methods
-----------------------------------------

   .. automethod:: Gradebook.can_assign_grade_system

   .. automethod:: Gradebook.can_assign_grade_systems_to_gradebook

   .. automethod:: Gradebook.get_assignable_gradebook_ids

   .. automethod:: Gradebook.get_assignable_gradebook_ids_for_grade_system

   .. automethod:: Gradebook.assign_grade_system_to_gradebook

   .. automethod:: Gradebook.unassign_grade_system_from_gradebook



Grade System Smart Gradebook Methods
------------------------------------

   .. autoattribute:: Gradebook.gradebook_id

   .. autoattribute:: Gradebook.gradebook

   .. automethod:: Gradebook.can_manage_smart_gradebooks

   .. autoattribute:: Gradebook.grade_system_query

   .. autoattribute:: Gradebook.grade_system_search_order

   .. automethod:: Gradebook.apply_grade_system_query

   .. automethod:: Gradebook.inspect_grade_system_query

   .. automethod:: Gradebook.apply_grade_system_sequencing

   .. automethod:: Gradebook.get_grade_system_query_from_inspector



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: Gradebook.gradebook_id

   .. autoattribute:: Gradebook.gradebook

   .. automethod:: Gradebook.can_lookup_grade_entries

   .. automethod:: Gradebook.use_comparative_grade_entry_view

   .. automethod:: Gradebook.use_plenary_grade_entry_view

   .. automethod:: Gradebook.use_federated_gradebook_view

   .. automethod:: Gradebook.use_isolated_gradebook_view

   .. automethod:: Gradebook.use_effective_grade_entry_view

   .. automethod:: Gradebook.use_any_effective_grade_entry_view

   .. automethod:: Gradebook.get_grade_entry

   .. automethod:: Gradebook.get_grade_entries_by_ids

   .. automethod:: Gradebook.get_grade_entries_by_genus_type

   .. automethod:: Gradebook.get_grade_entries_by_parent_genus_type

   .. automethod:: Gradebook.get_grade_entries_by_record_type

   .. automethod:: Gradebook.get_grade_entries_on_date

   .. automethod:: Gradebook.get_grade_entries_for_gradebook_column

   .. automethod:: Gradebook.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: Gradebook.get_grade_entries_for_resource

   .. automethod:: Gradebook.get_grade_entries_for_resource_on_date

   .. automethod:: Gradebook.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: Gradebook.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: Gradebook.get_grade_entries_by_grader

   .. autoattribute:: Gradebook.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: Gradebook.gradebook_id

   .. autoattribute:: Gradebook.gradebook

   .. automethod:: Gradebook.can_search_grade_entries

   .. automethod:: Gradebook.use_federated_gradebook_view

   .. automethod:: Gradebook.use_isolated_gradebook_view

   .. autoattribute:: Gradebook.grade_entry_query

   .. automethod:: Gradebook.get_grade_entries_by_query



Grade Entry Search Methods
--------------------------

   .. autoattribute:: Gradebook.grade_entry_search

   .. autoattribute:: Gradebook.grade_entry_search_order

   .. automethod:: Gradebook.get_grade_entries_by_search

   .. automethod:: Gradebook.get_grade_entry_query_from_inspector



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: Gradebook.gradebook_id

   .. autoattribute:: Gradebook.gradebook

   .. automethod:: Gradebook.can_create_grade_entries

   .. automethod:: Gradebook.can_create_grade_entry_with_record_types

   .. automethod:: Gradebook.get_grade_entry_form_for_create

   .. automethod:: Gradebook.create_grade_entry

   .. automethod:: Gradebook.can_overridecalculated_grade_entries

   .. automethod:: Gradebook.get_grade_entry_form_for_override

   .. automethod:: Gradebook.override_calculated_grade_entry

   .. automethod:: Gradebook.can_update_grade_entries

   .. automethod:: Gradebook.get_grade_entry_form_for_update

   .. automethod:: Gradebook.update_grade_entry

   .. automethod:: Gradebook.can_delete_grade_entries

   .. automethod:: Gradebook.delete_grade_entry

   .. automethod:: Gradebook.can_manage_grade_entry_aliases

   .. automethod:: Gradebook.alias_grade_entry



Grade Entry Notification Methods
--------------------------------

   .. autoattribute:: Gradebook.gradebook_id

   .. autoattribute:: Gradebook.gradebook

   .. automethod:: Gradebook.can_register_for_grade_entry_notifications

   .. automethod:: Gradebook.use_federated_gradebook_view

   .. automethod:: Gradebook.use_isolated_gradebook_view

   .. automethod:: Gradebook.register_for_new_grade_entries

   .. automethod:: Gradebook.register_for_new_grade_entries_for_gradebook_column

   .. automethod:: Gradebook.register_for_new_grade_entries_for_resource

   .. automethod:: Gradebook.register_for_new_grade_entries_by_grader

   .. automethod:: Gradebook.register_for_changed_grade_entries

   .. automethod:: Gradebook.register_for_changed_grade_entries_for_gradebook_column

   .. automethod:: Gradebook.register_for_changed_grade_entries_for_resource

   .. automethod:: Gradebook.register_for_changed_grade_entries_by_grader

   .. automethod:: Gradebook.register_for_changed_grade_entry

   .. automethod:: Gradebook.register_for_deleted_grade_entries

   .. automethod:: Gradebook.register_for_deleted_grade_entries_for_gradebook_column

   .. automethod:: Gradebook.register_for_deleted_grade_entries_for_resource

   .. automethod:: Gradebook.register_for_deleted_grade_entries_by_grader

   .. automethod:: Gradebook.register_for_deleted_grade_entry



