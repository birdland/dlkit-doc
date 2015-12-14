
.. currentmodule:: dlkit.services.grading

Service Catalog
===============


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



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: Gradebook.gradebook_id

   .. autoattribute:: Gradebook.gradebook

   .. automethod:: Gradebook.can_lookup_gradebook_columns

   .. automethod:: Gradebook.use_comparative_gradebook_column_view

   .. automethod:: Gradebook.use_plenary_gradebook_column_view

   .. automethod:: Gradebook.use_federated_gradebook_view

   .. automethod:: Gradebook.use_isolated_gradebook_view

   .. automethod:: Gradebook.get_gradebook_column

   .. automethod:: Gradebook.get_gradebook_columns_by_ids

   .. automethod:: Gradebook.get_gradebook_columns_by_genus_type

   .. automethod:: Gradebook.get_gradebook_columns_by_parent_genus_type

   .. automethod:: Gradebook.get_gradebook_columns_by_record_type

   .. autoattribute:: Gradebook.gradebook_columns

   .. automethod:: Gradebook.supports_summary

   .. automethod:: Gradebook.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: Gradebook.gradebook_id

   .. autoattribute:: Gradebook.gradebook

   .. automethod:: Gradebook.can_search_gradebook_columns

   .. automethod:: Gradebook.use_federated_gradebook_view

   .. automethod:: Gradebook.use_isolated_gradebook_view

   .. autoattribute:: Gradebook.gradebook_column_query

   .. automethod:: Gradebook.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: Gradebook.gradebook_id

   .. autoattribute:: Gradebook.gradebook

   .. automethod:: Gradebook.can_create_gradebook_columns

   .. automethod:: Gradebook.can_create_gradebook_column_with_record_types

   .. automethod:: Gradebook.get_gradebook_column_form_for_create

   .. automethod:: Gradebook.create_gradebook_column

   .. automethod:: Gradebook.can_update_gradebook_columns

   .. automethod:: Gradebook.get_gradebook_column_form_for_update

   .. automethod:: Gradebook.update_gradebook_column

   .. automethod:: Gradebook.sequence_gradebook_columns

   .. automethod:: Gradebook.move_gradebook_column

   .. automethod:: Gradebook.copy_gradebook_column_entries

   .. automethod:: Gradebook.can_delete_gradebook_columns

   .. automethod:: Gradebook.delete_gradebook_column

   .. automethod:: Gradebook.can_manage_gradebook_column_aliases

   .. automethod:: Gradebook.alias_gradebook_column



