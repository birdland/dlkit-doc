
.. currentmodule:: dlkit.grading.objects
.. automodule:: dlkit.grading.objects

Objects
=======


Grade
-----

.. autoclass:: Grade
   :show-inheritance:

   .. autoattribute:: Grade.grade_system_id

   .. autoattribute:: Grade.grade_system

   .. autoattribute:: Grade.input_score_start_range

   .. autoattribute:: Grade.input_score_end_range

   .. autoattribute:: Grade.output_score

   .. automethod:: Grade.get_grade_record



Gradebook Lookup Methods
------------------------

   .. automethod:: GradebookLookupSession.can_lookup_gradebooks

   .. automethod:: GradebookLookupSession.use_comparative_gradebook_view

   .. automethod:: GradebookLookupSession.use_plenary_gradebook_view

   .. automethod:: GradebookLookupSession.get_gradebook

   .. automethod:: GradebookLookupSession.get_gradebooks_by_ids

   .. automethod:: GradebookLookupSession.get_gradebooks_by_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_parent_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_record_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_provider

   .. autoattribute:: GradebookLookupSession.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradebookAdminSession.can_create_gradebooks

   .. automethod:: GradebookAdminSession.can_create_gradebook_with_record_types

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_create

   .. automethod:: GradebookAdminSession.create_gradebook

   .. automethod:: GradebookAdminSession.can_update_gradebooks

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_update

   .. automethod:: GradebookAdminSession.update_gradebook

   .. automethod:: GradebookAdminSession.can_delete_gradebooks

   .. automethod:: GradebookAdminSession.delete_gradebook

   .. automethod:: GradebookAdminSession.can_manage_gradebook_aliases

   .. automethod:: GradebookAdminSession.alias_gradebook



Grade System Lookup Methods
---------------------------

   .. autoattribute:: GradeSystemLookupSession.gradebook_id

   .. autoattribute:: GradeSystemLookupSession.gradebook

   .. automethod:: GradeSystemLookupSession.can_lookup_grade_systems

   .. automethod:: GradeSystemLookupSession.use_comparative_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_plenary_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_federated_gradebook_view

   .. automethod:: GradeSystemLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeSystemLookupSession.get_grade_system

   .. automethod:: GradeSystemLookupSession.get_grade_system_by_grade

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_ids

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_parent_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_record_type

   .. autoattribute:: GradeSystemLookupSession.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: GradeSystemQuerySession.gradebook_id

   .. autoattribute:: GradeSystemQuerySession.gradebook

   .. automethod:: GradeSystemQuerySession.can_search_grade_systems

   .. automethod:: GradeSystemQuerySession.use_federated_gradebook_view

   .. automethod:: GradeSystemQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeSystemQuerySession.grade_system_query

   .. automethod:: GradeSystemQuerySession.get_grade_systems_by_query



Grade System Admin Methods
--------------------------

   .. autoattribute:: GradeSystemAdminSession.gradebook_id

   .. autoattribute:: GradeSystemAdminSession.gradebook

   .. automethod:: GradeSystemAdminSession.can_create_grade_systems

   .. automethod:: GradeSystemAdminSession.can_create_grade_system_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade_system

   .. automethod:: GradeSystemAdminSession.can_update_grade_systems

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade_system

   .. automethod:: GradeSystemAdminSession.can_delete_grade_systems

   .. automethod:: GradeSystemAdminSession.delete_grade_system

   .. automethod:: GradeSystemAdminSession.can_manage_grade_system_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade_system

   .. automethod:: GradeSystemAdminSession.can_create_grades

   .. automethod:: GradeSystemAdminSession.can_create_grade_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade

   .. automethod:: GradeSystemAdminSession.can_update_grades

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade

   .. automethod:: GradeSystemAdminSession.can_delete_grades

   .. automethod:: GradeSystemAdminSession.delete_grade

   .. automethod:: GradeSystemAdminSession.can_manage_grade_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: GradeEntryLookupSession.gradebook_id

   .. autoattribute:: GradeEntryLookupSession.gradebook

   .. automethod:: GradeEntryLookupSession.can_lookup_grade_entries

   .. automethod:: GradeEntryLookupSession.use_comparative_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_plenary_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_federated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_any_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.get_grade_entry

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_ids

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_parent_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_record_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_grader

   .. autoattribute:: GradeEntryLookupSession.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: GradeEntryQuerySession.gradebook_id

   .. autoattribute:: GradeEntryQuerySession.gradebook

   .. automethod:: GradeEntryQuerySession.can_search_grade_entries

   .. automethod:: GradeEntryQuerySession.use_federated_gradebook_view

   .. automethod:: GradeEntryQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeEntryQuerySession.grade_entry_query

   .. automethod:: GradeEntryQuerySession.get_grade_entries_by_query



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: GradeEntryAdminSession.gradebook_id

   .. autoattribute:: GradeEntryAdminSession.gradebook

   .. automethod:: GradeEntryAdminSession.can_create_grade_entries

   .. automethod:: GradeEntryAdminSession.can_create_grade_entry_with_record_types

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_create

   .. automethod:: GradeEntryAdminSession.create_grade_entry

   .. automethod:: GradeEntryAdminSession.can_overridecalculated_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_override

   .. automethod:: GradeEntryAdminSession.override_calculated_grade_entry

   .. automethod:: GradeEntryAdminSession.can_update_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_update

   .. automethod:: GradeEntryAdminSession.update_grade_entry

   .. automethod:: GradeEntryAdminSession.can_delete_grade_entries

   .. automethod:: GradeEntryAdminSession.delete_grade_entry

   .. automethod:: GradeEntryAdminSession.can_manage_grade_entry_aliases

   .. automethod:: GradeEntryAdminSession.alias_grade_entry



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradebookColumnLookupSession.gradebook_id

   .. autoattribute:: GradebookColumnLookupSession.gradebook

   .. automethod:: GradebookColumnLookupSession.can_lookup_gradebook_columns

   .. automethod:: GradebookColumnLookupSession.use_comparative_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_plenary_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_federated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.use_isolated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_ids

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_record_type

   .. autoattribute:: GradebookColumnLookupSession.gradebook_columns

   .. automethod:: GradebookColumnLookupSession.supports_summary

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradebookColumnQuerySession.gradebook_id

   .. autoattribute:: GradebookColumnQuerySession.gradebook

   .. automethod:: GradebookColumnQuerySession.can_search_gradebook_columns

   .. automethod:: GradebookColumnQuerySession.use_federated_gradebook_view

   .. automethod:: GradebookColumnQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradebookColumnQuerySession.gradebook_column_query

   .. automethod:: GradebookColumnQuerySession.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradebookColumnAdminSession.gradebook_id

   .. autoattribute:: GradebookColumnAdminSession.gradebook

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_column_with_record_types

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_create

   .. automethod:: GradebookColumnAdminSession.create_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_update_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_update

   .. automethod:: GradebookColumnAdminSession.update_gradebook_column

   .. automethod:: GradebookColumnAdminSession.sequence_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.move_gradebook_column

   .. automethod:: GradebookColumnAdminSession.copy_gradebook_column_entries

   .. automethod:: GradebookColumnAdminSession.can_delete_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.delete_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_manage_gradebook_column_aliases

   .. automethod:: GradebookColumnAdminSession.alias_gradebook_column



Grade Form
----------

.. autoclass:: GradeForm
   :show-inheritance:

   .. autoattribute:: GradeForm.input_score_start_range_metadata

   .. autoattribute:: GradeForm.input_score_start_range

   .. autoattribute:: GradeForm.input_score_end_range_metadata

   .. autoattribute:: GradeForm.input_score_end_range

   .. autoattribute:: GradeForm.output_score_metadata

   .. autoattribute:: GradeForm.output_score

   .. automethod:: GradeForm.get_grade_form_record



Gradebook Lookup Methods
------------------------

   .. automethod:: GradebookLookupSession.can_lookup_gradebooks

   .. automethod:: GradebookLookupSession.use_comparative_gradebook_view

   .. automethod:: GradebookLookupSession.use_plenary_gradebook_view

   .. automethod:: GradebookLookupSession.get_gradebook

   .. automethod:: GradebookLookupSession.get_gradebooks_by_ids

   .. automethod:: GradebookLookupSession.get_gradebooks_by_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_parent_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_record_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_provider

   .. autoattribute:: GradebookLookupSession.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradebookAdminSession.can_create_gradebooks

   .. automethod:: GradebookAdminSession.can_create_gradebook_with_record_types

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_create

   .. automethod:: GradebookAdminSession.create_gradebook

   .. automethod:: GradebookAdminSession.can_update_gradebooks

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_update

   .. automethod:: GradebookAdminSession.update_gradebook

   .. automethod:: GradebookAdminSession.can_delete_gradebooks

   .. automethod:: GradebookAdminSession.delete_gradebook

   .. automethod:: GradebookAdminSession.can_manage_gradebook_aliases

   .. automethod:: GradebookAdminSession.alias_gradebook



Grade System Lookup Methods
---------------------------

   .. autoattribute:: GradeSystemLookupSession.gradebook_id

   .. autoattribute:: GradeSystemLookupSession.gradebook

   .. automethod:: GradeSystemLookupSession.can_lookup_grade_systems

   .. automethod:: GradeSystemLookupSession.use_comparative_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_plenary_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_federated_gradebook_view

   .. automethod:: GradeSystemLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeSystemLookupSession.get_grade_system

   .. automethod:: GradeSystemLookupSession.get_grade_system_by_grade

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_ids

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_parent_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_record_type

   .. autoattribute:: GradeSystemLookupSession.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: GradeSystemQuerySession.gradebook_id

   .. autoattribute:: GradeSystemQuerySession.gradebook

   .. automethod:: GradeSystemQuerySession.can_search_grade_systems

   .. automethod:: GradeSystemQuerySession.use_federated_gradebook_view

   .. automethod:: GradeSystemQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeSystemQuerySession.grade_system_query

   .. automethod:: GradeSystemQuerySession.get_grade_systems_by_query



Grade System Admin Methods
--------------------------

   .. autoattribute:: GradeSystemAdminSession.gradebook_id

   .. autoattribute:: GradeSystemAdminSession.gradebook

   .. automethod:: GradeSystemAdminSession.can_create_grade_systems

   .. automethod:: GradeSystemAdminSession.can_create_grade_system_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade_system

   .. automethod:: GradeSystemAdminSession.can_update_grade_systems

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade_system

   .. automethod:: GradeSystemAdminSession.can_delete_grade_systems

   .. automethod:: GradeSystemAdminSession.delete_grade_system

   .. automethod:: GradeSystemAdminSession.can_manage_grade_system_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade_system

   .. automethod:: GradeSystemAdminSession.can_create_grades

   .. automethod:: GradeSystemAdminSession.can_create_grade_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade

   .. automethod:: GradeSystemAdminSession.can_update_grades

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade

   .. automethod:: GradeSystemAdminSession.can_delete_grades

   .. automethod:: GradeSystemAdminSession.delete_grade

   .. automethod:: GradeSystemAdminSession.can_manage_grade_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: GradeEntryLookupSession.gradebook_id

   .. autoattribute:: GradeEntryLookupSession.gradebook

   .. automethod:: GradeEntryLookupSession.can_lookup_grade_entries

   .. automethod:: GradeEntryLookupSession.use_comparative_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_plenary_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_federated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_any_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.get_grade_entry

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_ids

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_parent_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_record_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_grader

   .. autoattribute:: GradeEntryLookupSession.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: GradeEntryQuerySession.gradebook_id

   .. autoattribute:: GradeEntryQuerySession.gradebook

   .. automethod:: GradeEntryQuerySession.can_search_grade_entries

   .. automethod:: GradeEntryQuerySession.use_federated_gradebook_view

   .. automethod:: GradeEntryQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeEntryQuerySession.grade_entry_query

   .. automethod:: GradeEntryQuerySession.get_grade_entries_by_query



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: GradeEntryAdminSession.gradebook_id

   .. autoattribute:: GradeEntryAdminSession.gradebook

   .. automethod:: GradeEntryAdminSession.can_create_grade_entries

   .. automethod:: GradeEntryAdminSession.can_create_grade_entry_with_record_types

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_create

   .. automethod:: GradeEntryAdminSession.create_grade_entry

   .. automethod:: GradeEntryAdminSession.can_overridecalculated_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_override

   .. automethod:: GradeEntryAdminSession.override_calculated_grade_entry

   .. automethod:: GradeEntryAdminSession.can_update_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_update

   .. automethod:: GradeEntryAdminSession.update_grade_entry

   .. automethod:: GradeEntryAdminSession.can_delete_grade_entries

   .. automethod:: GradeEntryAdminSession.delete_grade_entry

   .. automethod:: GradeEntryAdminSession.can_manage_grade_entry_aliases

   .. automethod:: GradeEntryAdminSession.alias_grade_entry



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradebookColumnLookupSession.gradebook_id

   .. autoattribute:: GradebookColumnLookupSession.gradebook

   .. automethod:: GradebookColumnLookupSession.can_lookup_gradebook_columns

   .. automethod:: GradebookColumnLookupSession.use_comparative_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_plenary_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_federated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.use_isolated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_ids

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_record_type

   .. autoattribute:: GradebookColumnLookupSession.gradebook_columns

   .. automethod:: GradebookColumnLookupSession.supports_summary

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradebookColumnQuerySession.gradebook_id

   .. autoattribute:: GradebookColumnQuerySession.gradebook

   .. automethod:: GradebookColumnQuerySession.can_search_gradebook_columns

   .. automethod:: GradebookColumnQuerySession.use_federated_gradebook_view

   .. automethod:: GradebookColumnQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradebookColumnQuerySession.gradebook_column_query

   .. automethod:: GradebookColumnQuerySession.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradebookColumnAdminSession.gradebook_id

   .. autoattribute:: GradebookColumnAdminSession.gradebook

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_column_with_record_types

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_create

   .. automethod:: GradebookColumnAdminSession.create_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_update_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_update

   .. automethod:: GradebookColumnAdminSession.update_gradebook_column

   .. automethod:: GradebookColumnAdminSession.sequence_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.move_gradebook_column

   .. automethod:: GradebookColumnAdminSession.copy_gradebook_column_entries

   .. automethod:: GradebookColumnAdminSession.can_delete_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.delete_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_manage_gradebook_column_aliases

   .. automethod:: GradebookColumnAdminSession.alias_gradebook_column



Grade List
----------

.. autoclass:: GradeList
   :show-inheritance:

   .. autoattribute:: GradeList.next_grade

   .. automethod:: GradeList.get_next_grades



Gradebook Lookup Methods
------------------------

   .. automethod:: GradebookLookupSession.can_lookup_gradebooks

   .. automethod:: GradebookLookupSession.use_comparative_gradebook_view

   .. automethod:: GradebookLookupSession.use_plenary_gradebook_view

   .. automethod:: GradebookLookupSession.get_gradebook

   .. automethod:: GradebookLookupSession.get_gradebooks_by_ids

   .. automethod:: GradebookLookupSession.get_gradebooks_by_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_parent_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_record_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_provider

   .. autoattribute:: GradebookLookupSession.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradebookAdminSession.can_create_gradebooks

   .. automethod:: GradebookAdminSession.can_create_gradebook_with_record_types

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_create

   .. automethod:: GradebookAdminSession.create_gradebook

   .. automethod:: GradebookAdminSession.can_update_gradebooks

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_update

   .. automethod:: GradebookAdminSession.update_gradebook

   .. automethod:: GradebookAdminSession.can_delete_gradebooks

   .. automethod:: GradebookAdminSession.delete_gradebook

   .. automethod:: GradebookAdminSession.can_manage_gradebook_aliases

   .. automethod:: GradebookAdminSession.alias_gradebook



Grade System Lookup Methods
---------------------------

   .. autoattribute:: GradeSystemLookupSession.gradebook_id

   .. autoattribute:: GradeSystemLookupSession.gradebook

   .. automethod:: GradeSystemLookupSession.can_lookup_grade_systems

   .. automethod:: GradeSystemLookupSession.use_comparative_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_plenary_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_federated_gradebook_view

   .. automethod:: GradeSystemLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeSystemLookupSession.get_grade_system

   .. automethod:: GradeSystemLookupSession.get_grade_system_by_grade

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_ids

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_parent_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_record_type

   .. autoattribute:: GradeSystemLookupSession.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: GradeSystemQuerySession.gradebook_id

   .. autoattribute:: GradeSystemQuerySession.gradebook

   .. automethod:: GradeSystemQuerySession.can_search_grade_systems

   .. automethod:: GradeSystemQuerySession.use_federated_gradebook_view

   .. automethod:: GradeSystemQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeSystemQuerySession.grade_system_query

   .. automethod:: GradeSystemQuerySession.get_grade_systems_by_query



Grade System Admin Methods
--------------------------

   .. autoattribute:: GradeSystemAdminSession.gradebook_id

   .. autoattribute:: GradeSystemAdminSession.gradebook

   .. automethod:: GradeSystemAdminSession.can_create_grade_systems

   .. automethod:: GradeSystemAdminSession.can_create_grade_system_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade_system

   .. automethod:: GradeSystemAdminSession.can_update_grade_systems

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade_system

   .. automethod:: GradeSystemAdminSession.can_delete_grade_systems

   .. automethod:: GradeSystemAdminSession.delete_grade_system

   .. automethod:: GradeSystemAdminSession.can_manage_grade_system_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade_system

   .. automethod:: GradeSystemAdminSession.can_create_grades

   .. automethod:: GradeSystemAdminSession.can_create_grade_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade

   .. automethod:: GradeSystemAdminSession.can_update_grades

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade

   .. automethod:: GradeSystemAdminSession.can_delete_grades

   .. automethod:: GradeSystemAdminSession.delete_grade

   .. automethod:: GradeSystemAdminSession.can_manage_grade_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: GradeEntryLookupSession.gradebook_id

   .. autoattribute:: GradeEntryLookupSession.gradebook

   .. automethod:: GradeEntryLookupSession.can_lookup_grade_entries

   .. automethod:: GradeEntryLookupSession.use_comparative_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_plenary_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_federated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_any_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.get_grade_entry

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_ids

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_parent_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_record_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_grader

   .. autoattribute:: GradeEntryLookupSession.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: GradeEntryQuerySession.gradebook_id

   .. autoattribute:: GradeEntryQuerySession.gradebook

   .. automethod:: GradeEntryQuerySession.can_search_grade_entries

   .. automethod:: GradeEntryQuerySession.use_federated_gradebook_view

   .. automethod:: GradeEntryQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeEntryQuerySession.grade_entry_query

   .. automethod:: GradeEntryQuerySession.get_grade_entries_by_query



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: GradeEntryAdminSession.gradebook_id

   .. autoattribute:: GradeEntryAdminSession.gradebook

   .. automethod:: GradeEntryAdminSession.can_create_grade_entries

   .. automethod:: GradeEntryAdminSession.can_create_grade_entry_with_record_types

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_create

   .. automethod:: GradeEntryAdminSession.create_grade_entry

   .. automethod:: GradeEntryAdminSession.can_overridecalculated_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_override

   .. automethod:: GradeEntryAdminSession.override_calculated_grade_entry

   .. automethod:: GradeEntryAdminSession.can_update_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_update

   .. automethod:: GradeEntryAdminSession.update_grade_entry

   .. automethod:: GradeEntryAdminSession.can_delete_grade_entries

   .. automethod:: GradeEntryAdminSession.delete_grade_entry

   .. automethod:: GradeEntryAdminSession.can_manage_grade_entry_aliases

   .. automethod:: GradeEntryAdminSession.alias_grade_entry



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradebookColumnLookupSession.gradebook_id

   .. autoattribute:: GradebookColumnLookupSession.gradebook

   .. automethod:: GradebookColumnLookupSession.can_lookup_gradebook_columns

   .. automethod:: GradebookColumnLookupSession.use_comparative_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_plenary_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_federated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.use_isolated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_ids

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_record_type

   .. autoattribute:: GradebookColumnLookupSession.gradebook_columns

   .. automethod:: GradebookColumnLookupSession.supports_summary

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradebookColumnQuerySession.gradebook_id

   .. autoattribute:: GradebookColumnQuerySession.gradebook

   .. automethod:: GradebookColumnQuerySession.can_search_gradebook_columns

   .. automethod:: GradebookColumnQuerySession.use_federated_gradebook_view

   .. automethod:: GradebookColumnQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradebookColumnQuerySession.gradebook_column_query

   .. automethod:: GradebookColumnQuerySession.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradebookColumnAdminSession.gradebook_id

   .. autoattribute:: GradebookColumnAdminSession.gradebook

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_column_with_record_types

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_create

   .. automethod:: GradebookColumnAdminSession.create_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_update_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_update

   .. automethod:: GradebookColumnAdminSession.update_gradebook_column

   .. automethod:: GradebookColumnAdminSession.sequence_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.move_gradebook_column

   .. automethod:: GradebookColumnAdminSession.copy_gradebook_column_entries

   .. automethod:: GradebookColumnAdminSession.can_delete_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.delete_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_manage_gradebook_column_aliases

   .. automethod:: GradebookColumnAdminSession.alias_gradebook_column



Grade System
------------

.. autoclass:: GradeSystem
   :show-inheritance:

   .. automethod:: GradeSystem.is_based_on_grades

   .. autoattribute:: GradeSystem.grade_ids

   .. autoattribute:: GradeSystem.grades

   .. autoattribute:: GradeSystem.lowest_numeric_score

   .. autoattribute:: GradeSystem.numeric_score_increment

   .. autoattribute:: GradeSystem.highest_numeric_score

   .. automethod:: GradeSystem.get_grade_system_record



Gradebook Lookup Methods
------------------------

   .. automethod:: GradebookLookupSession.can_lookup_gradebooks

   .. automethod:: GradebookLookupSession.use_comparative_gradebook_view

   .. automethod:: GradebookLookupSession.use_plenary_gradebook_view

   .. automethod:: GradebookLookupSession.get_gradebook

   .. automethod:: GradebookLookupSession.get_gradebooks_by_ids

   .. automethod:: GradebookLookupSession.get_gradebooks_by_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_parent_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_record_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_provider

   .. autoattribute:: GradebookLookupSession.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradebookAdminSession.can_create_gradebooks

   .. automethod:: GradebookAdminSession.can_create_gradebook_with_record_types

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_create

   .. automethod:: GradebookAdminSession.create_gradebook

   .. automethod:: GradebookAdminSession.can_update_gradebooks

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_update

   .. automethod:: GradebookAdminSession.update_gradebook

   .. automethod:: GradebookAdminSession.can_delete_gradebooks

   .. automethod:: GradebookAdminSession.delete_gradebook

   .. automethod:: GradebookAdminSession.can_manage_gradebook_aliases

   .. automethod:: GradebookAdminSession.alias_gradebook



Grade System Lookup Methods
---------------------------

   .. autoattribute:: GradeSystemLookupSession.gradebook_id

   .. autoattribute:: GradeSystemLookupSession.gradebook

   .. automethod:: GradeSystemLookupSession.can_lookup_grade_systems

   .. automethod:: GradeSystemLookupSession.use_comparative_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_plenary_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_federated_gradebook_view

   .. automethod:: GradeSystemLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeSystemLookupSession.get_grade_system

   .. automethod:: GradeSystemLookupSession.get_grade_system_by_grade

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_ids

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_parent_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_record_type

   .. autoattribute:: GradeSystemLookupSession.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: GradeSystemQuerySession.gradebook_id

   .. autoattribute:: GradeSystemQuerySession.gradebook

   .. automethod:: GradeSystemQuerySession.can_search_grade_systems

   .. automethod:: GradeSystemQuerySession.use_federated_gradebook_view

   .. automethod:: GradeSystemQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeSystemQuerySession.grade_system_query

   .. automethod:: GradeSystemQuerySession.get_grade_systems_by_query



Grade System Admin Methods
--------------------------

   .. autoattribute:: GradeSystemAdminSession.gradebook_id

   .. autoattribute:: GradeSystemAdminSession.gradebook

   .. automethod:: GradeSystemAdminSession.can_create_grade_systems

   .. automethod:: GradeSystemAdminSession.can_create_grade_system_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade_system

   .. automethod:: GradeSystemAdminSession.can_update_grade_systems

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade_system

   .. automethod:: GradeSystemAdminSession.can_delete_grade_systems

   .. automethod:: GradeSystemAdminSession.delete_grade_system

   .. automethod:: GradeSystemAdminSession.can_manage_grade_system_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade_system

   .. automethod:: GradeSystemAdminSession.can_create_grades

   .. automethod:: GradeSystemAdminSession.can_create_grade_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade

   .. automethod:: GradeSystemAdminSession.can_update_grades

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade

   .. automethod:: GradeSystemAdminSession.can_delete_grades

   .. automethod:: GradeSystemAdminSession.delete_grade

   .. automethod:: GradeSystemAdminSession.can_manage_grade_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: GradeEntryLookupSession.gradebook_id

   .. autoattribute:: GradeEntryLookupSession.gradebook

   .. automethod:: GradeEntryLookupSession.can_lookup_grade_entries

   .. automethod:: GradeEntryLookupSession.use_comparative_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_plenary_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_federated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_any_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.get_grade_entry

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_ids

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_parent_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_record_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_grader

   .. autoattribute:: GradeEntryLookupSession.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: GradeEntryQuerySession.gradebook_id

   .. autoattribute:: GradeEntryQuerySession.gradebook

   .. automethod:: GradeEntryQuerySession.can_search_grade_entries

   .. automethod:: GradeEntryQuerySession.use_federated_gradebook_view

   .. automethod:: GradeEntryQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeEntryQuerySession.grade_entry_query

   .. automethod:: GradeEntryQuerySession.get_grade_entries_by_query



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: GradeEntryAdminSession.gradebook_id

   .. autoattribute:: GradeEntryAdminSession.gradebook

   .. automethod:: GradeEntryAdminSession.can_create_grade_entries

   .. automethod:: GradeEntryAdminSession.can_create_grade_entry_with_record_types

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_create

   .. automethod:: GradeEntryAdminSession.create_grade_entry

   .. automethod:: GradeEntryAdminSession.can_overridecalculated_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_override

   .. automethod:: GradeEntryAdminSession.override_calculated_grade_entry

   .. automethod:: GradeEntryAdminSession.can_update_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_update

   .. automethod:: GradeEntryAdminSession.update_grade_entry

   .. automethod:: GradeEntryAdminSession.can_delete_grade_entries

   .. automethod:: GradeEntryAdminSession.delete_grade_entry

   .. automethod:: GradeEntryAdminSession.can_manage_grade_entry_aliases

   .. automethod:: GradeEntryAdminSession.alias_grade_entry



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradebookColumnLookupSession.gradebook_id

   .. autoattribute:: GradebookColumnLookupSession.gradebook

   .. automethod:: GradebookColumnLookupSession.can_lookup_gradebook_columns

   .. automethod:: GradebookColumnLookupSession.use_comparative_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_plenary_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_federated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.use_isolated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_ids

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_record_type

   .. autoattribute:: GradebookColumnLookupSession.gradebook_columns

   .. automethod:: GradebookColumnLookupSession.supports_summary

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradebookColumnQuerySession.gradebook_id

   .. autoattribute:: GradebookColumnQuerySession.gradebook

   .. automethod:: GradebookColumnQuerySession.can_search_gradebook_columns

   .. automethod:: GradebookColumnQuerySession.use_federated_gradebook_view

   .. automethod:: GradebookColumnQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradebookColumnQuerySession.gradebook_column_query

   .. automethod:: GradebookColumnQuerySession.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradebookColumnAdminSession.gradebook_id

   .. autoattribute:: GradebookColumnAdminSession.gradebook

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_column_with_record_types

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_create

   .. automethod:: GradebookColumnAdminSession.create_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_update_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_update

   .. automethod:: GradebookColumnAdminSession.update_gradebook_column

   .. automethod:: GradebookColumnAdminSession.sequence_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.move_gradebook_column

   .. automethod:: GradebookColumnAdminSession.copy_gradebook_column_entries

   .. automethod:: GradebookColumnAdminSession.can_delete_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.delete_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_manage_gradebook_column_aliases

   .. automethod:: GradebookColumnAdminSession.alias_gradebook_column



Grade System Form
-----------------

.. autoclass:: GradeSystemForm
   :show-inheritance:

   .. autoattribute:: GradeSystemForm.based_on_grades_metadata

   .. autoattribute:: GradeSystemForm.based_on_grades

   .. autoattribute:: GradeSystemForm.lowest_numeric_score_metadata

   .. autoattribute:: GradeSystemForm.lowest_numeric_score

   .. autoattribute:: GradeSystemForm.numeric_score_increment_metadata

   .. autoattribute:: GradeSystemForm.numeric_score_increment

   .. autoattribute:: GradeSystemForm.highest_numeric_score_metadata

   .. autoattribute:: GradeSystemForm.highest_numeric_score

   .. automethod:: GradeSystemForm.get_grade_system_form_record



Gradebook Lookup Methods
------------------------

   .. automethod:: GradebookLookupSession.can_lookup_gradebooks

   .. automethod:: GradebookLookupSession.use_comparative_gradebook_view

   .. automethod:: GradebookLookupSession.use_plenary_gradebook_view

   .. automethod:: GradebookLookupSession.get_gradebook

   .. automethod:: GradebookLookupSession.get_gradebooks_by_ids

   .. automethod:: GradebookLookupSession.get_gradebooks_by_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_parent_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_record_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_provider

   .. autoattribute:: GradebookLookupSession.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradebookAdminSession.can_create_gradebooks

   .. automethod:: GradebookAdminSession.can_create_gradebook_with_record_types

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_create

   .. automethod:: GradebookAdminSession.create_gradebook

   .. automethod:: GradebookAdminSession.can_update_gradebooks

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_update

   .. automethod:: GradebookAdminSession.update_gradebook

   .. automethod:: GradebookAdminSession.can_delete_gradebooks

   .. automethod:: GradebookAdminSession.delete_gradebook

   .. automethod:: GradebookAdminSession.can_manage_gradebook_aliases

   .. automethod:: GradebookAdminSession.alias_gradebook



Grade System Lookup Methods
---------------------------

   .. autoattribute:: GradeSystemLookupSession.gradebook_id

   .. autoattribute:: GradeSystemLookupSession.gradebook

   .. automethod:: GradeSystemLookupSession.can_lookup_grade_systems

   .. automethod:: GradeSystemLookupSession.use_comparative_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_plenary_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_federated_gradebook_view

   .. automethod:: GradeSystemLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeSystemLookupSession.get_grade_system

   .. automethod:: GradeSystemLookupSession.get_grade_system_by_grade

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_ids

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_parent_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_record_type

   .. autoattribute:: GradeSystemLookupSession.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: GradeSystemQuerySession.gradebook_id

   .. autoattribute:: GradeSystemQuerySession.gradebook

   .. automethod:: GradeSystemQuerySession.can_search_grade_systems

   .. automethod:: GradeSystemQuerySession.use_federated_gradebook_view

   .. automethod:: GradeSystemQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeSystemQuerySession.grade_system_query

   .. automethod:: GradeSystemQuerySession.get_grade_systems_by_query



Grade System Admin Methods
--------------------------

   .. autoattribute:: GradeSystemAdminSession.gradebook_id

   .. autoattribute:: GradeSystemAdminSession.gradebook

   .. automethod:: GradeSystemAdminSession.can_create_grade_systems

   .. automethod:: GradeSystemAdminSession.can_create_grade_system_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade_system

   .. automethod:: GradeSystemAdminSession.can_update_grade_systems

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade_system

   .. automethod:: GradeSystemAdminSession.can_delete_grade_systems

   .. automethod:: GradeSystemAdminSession.delete_grade_system

   .. automethod:: GradeSystemAdminSession.can_manage_grade_system_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade_system

   .. automethod:: GradeSystemAdminSession.can_create_grades

   .. automethod:: GradeSystemAdminSession.can_create_grade_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade

   .. automethod:: GradeSystemAdminSession.can_update_grades

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade

   .. automethod:: GradeSystemAdminSession.can_delete_grades

   .. automethod:: GradeSystemAdminSession.delete_grade

   .. automethod:: GradeSystemAdminSession.can_manage_grade_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: GradeEntryLookupSession.gradebook_id

   .. autoattribute:: GradeEntryLookupSession.gradebook

   .. automethod:: GradeEntryLookupSession.can_lookup_grade_entries

   .. automethod:: GradeEntryLookupSession.use_comparative_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_plenary_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_federated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_any_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.get_grade_entry

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_ids

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_parent_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_record_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_grader

   .. autoattribute:: GradeEntryLookupSession.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: GradeEntryQuerySession.gradebook_id

   .. autoattribute:: GradeEntryQuerySession.gradebook

   .. automethod:: GradeEntryQuerySession.can_search_grade_entries

   .. automethod:: GradeEntryQuerySession.use_federated_gradebook_view

   .. automethod:: GradeEntryQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeEntryQuerySession.grade_entry_query

   .. automethod:: GradeEntryQuerySession.get_grade_entries_by_query



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: GradeEntryAdminSession.gradebook_id

   .. autoattribute:: GradeEntryAdminSession.gradebook

   .. automethod:: GradeEntryAdminSession.can_create_grade_entries

   .. automethod:: GradeEntryAdminSession.can_create_grade_entry_with_record_types

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_create

   .. automethod:: GradeEntryAdminSession.create_grade_entry

   .. automethod:: GradeEntryAdminSession.can_overridecalculated_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_override

   .. automethod:: GradeEntryAdminSession.override_calculated_grade_entry

   .. automethod:: GradeEntryAdminSession.can_update_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_update

   .. automethod:: GradeEntryAdminSession.update_grade_entry

   .. automethod:: GradeEntryAdminSession.can_delete_grade_entries

   .. automethod:: GradeEntryAdminSession.delete_grade_entry

   .. automethod:: GradeEntryAdminSession.can_manage_grade_entry_aliases

   .. automethod:: GradeEntryAdminSession.alias_grade_entry



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradebookColumnLookupSession.gradebook_id

   .. autoattribute:: GradebookColumnLookupSession.gradebook

   .. automethod:: GradebookColumnLookupSession.can_lookup_gradebook_columns

   .. automethod:: GradebookColumnLookupSession.use_comparative_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_plenary_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_federated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.use_isolated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_ids

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_record_type

   .. autoattribute:: GradebookColumnLookupSession.gradebook_columns

   .. automethod:: GradebookColumnLookupSession.supports_summary

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradebookColumnQuerySession.gradebook_id

   .. autoattribute:: GradebookColumnQuerySession.gradebook

   .. automethod:: GradebookColumnQuerySession.can_search_gradebook_columns

   .. automethod:: GradebookColumnQuerySession.use_federated_gradebook_view

   .. automethod:: GradebookColumnQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradebookColumnQuerySession.gradebook_column_query

   .. automethod:: GradebookColumnQuerySession.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradebookColumnAdminSession.gradebook_id

   .. autoattribute:: GradebookColumnAdminSession.gradebook

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_column_with_record_types

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_create

   .. automethod:: GradebookColumnAdminSession.create_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_update_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_update

   .. automethod:: GradebookColumnAdminSession.update_gradebook_column

   .. automethod:: GradebookColumnAdminSession.sequence_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.move_gradebook_column

   .. automethod:: GradebookColumnAdminSession.copy_gradebook_column_entries

   .. automethod:: GradebookColumnAdminSession.can_delete_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.delete_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_manage_gradebook_column_aliases

   .. automethod:: GradebookColumnAdminSession.alias_gradebook_column



Grade System List
-----------------

.. autoclass:: GradeSystemList
   :show-inheritance:

   .. autoattribute:: GradeSystemList.next_grade_system

   .. automethod:: GradeSystemList.get_next_grade_systems



Gradebook Lookup Methods
------------------------

   .. automethod:: GradebookLookupSession.can_lookup_gradebooks

   .. automethod:: GradebookLookupSession.use_comparative_gradebook_view

   .. automethod:: GradebookLookupSession.use_plenary_gradebook_view

   .. automethod:: GradebookLookupSession.get_gradebook

   .. automethod:: GradebookLookupSession.get_gradebooks_by_ids

   .. automethod:: GradebookLookupSession.get_gradebooks_by_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_parent_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_record_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_provider

   .. autoattribute:: GradebookLookupSession.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradebookAdminSession.can_create_gradebooks

   .. automethod:: GradebookAdminSession.can_create_gradebook_with_record_types

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_create

   .. automethod:: GradebookAdminSession.create_gradebook

   .. automethod:: GradebookAdminSession.can_update_gradebooks

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_update

   .. automethod:: GradebookAdminSession.update_gradebook

   .. automethod:: GradebookAdminSession.can_delete_gradebooks

   .. automethod:: GradebookAdminSession.delete_gradebook

   .. automethod:: GradebookAdminSession.can_manage_gradebook_aliases

   .. automethod:: GradebookAdminSession.alias_gradebook



Grade System Lookup Methods
---------------------------

   .. autoattribute:: GradeSystemLookupSession.gradebook_id

   .. autoattribute:: GradeSystemLookupSession.gradebook

   .. automethod:: GradeSystemLookupSession.can_lookup_grade_systems

   .. automethod:: GradeSystemLookupSession.use_comparative_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_plenary_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_federated_gradebook_view

   .. automethod:: GradeSystemLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeSystemLookupSession.get_grade_system

   .. automethod:: GradeSystemLookupSession.get_grade_system_by_grade

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_ids

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_parent_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_record_type

   .. autoattribute:: GradeSystemLookupSession.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: GradeSystemQuerySession.gradebook_id

   .. autoattribute:: GradeSystemQuerySession.gradebook

   .. automethod:: GradeSystemQuerySession.can_search_grade_systems

   .. automethod:: GradeSystemQuerySession.use_federated_gradebook_view

   .. automethod:: GradeSystemQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeSystemQuerySession.grade_system_query

   .. automethod:: GradeSystemQuerySession.get_grade_systems_by_query



Grade System Admin Methods
--------------------------

   .. autoattribute:: GradeSystemAdminSession.gradebook_id

   .. autoattribute:: GradeSystemAdminSession.gradebook

   .. automethod:: GradeSystemAdminSession.can_create_grade_systems

   .. automethod:: GradeSystemAdminSession.can_create_grade_system_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade_system

   .. automethod:: GradeSystemAdminSession.can_update_grade_systems

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade_system

   .. automethod:: GradeSystemAdminSession.can_delete_grade_systems

   .. automethod:: GradeSystemAdminSession.delete_grade_system

   .. automethod:: GradeSystemAdminSession.can_manage_grade_system_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade_system

   .. automethod:: GradeSystemAdminSession.can_create_grades

   .. automethod:: GradeSystemAdminSession.can_create_grade_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade

   .. automethod:: GradeSystemAdminSession.can_update_grades

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade

   .. automethod:: GradeSystemAdminSession.can_delete_grades

   .. automethod:: GradeSystemAdminSession.delete_grade

   .. automethod:: GradeSystemAdminSession.can_manage_grade_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: GradeEntryLookupSession.gradebook_id

   .. autoattribute:: GradeEntryLookupSession.gradebook

   .. automethod:: GradeEntryLookupSession.can_lookup_grade_entries

   .. automethod:: GradeEntryLookupSession.use_comparative_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_plenary_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_federated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_any_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.get_grade_entry

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_ids

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_parent_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_record_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_grader

   .. autoattribute:: GradeEntryLookupSession.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: GradeEntryQuerySession.gradebook_id

   .. autoattribute:: GradeEntryQuerySession.gradebook

   .. automethod:: GradeEntryQuerySession.can_search_grade_entries

   .. automethod:: GradeEntryQuerySession.use_federated_gradebook_view

   .. automethod:: GradeEntryQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeEntryQuerySession.grade_entry_query

   .. automethod:: GradeEntryQuerySession.get_grade_entries_by_query



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: GradeEntryAdminSession.gradebook_id

   .. autoattribute:: GradeEntryAdminSession.gradebook

   .. automethod:: GradeEntryAdminSession.can_create_grade_entries

   .. automethod:: GradeEntryAdminSession.can_create_grade_entry_with_record_types

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_create

   .. automethod:: GradeEntryAdminSession.create_grade_entry

   .. automethod:: GradeEntryAdminSession.can_overridecalculated_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_override

   .. automethod:: GradeEntryAdminSession.override_calculated_grade_entry

   .. automethod:: GradeEntryAdminSession.can_update_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_update

   .. automethod:: GradeEntryAdminSession.update_grade_entry

   .. automethod:: GradeEntryAdminSession.can_delete_grade_entries

   .. automethod:: GradeEntryAdminSession.delete_grade_entry

   .. automethod:: GradeEntryAdminSession.can_manage_grade_entry_aliases

   .. automethod:: GradeEntryAdminSession.alias_grade_entry



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradebookColumnLookupSession.gradebook_id

   .. autoattribute:: GradebookColumnLookupSession.gradebook

   .. automethod:: GradebookColumnLookupSession.can_lookup_gradebook_columns

   .. automethod:: GradebookColumnLookupSession.use_comparative_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_plenary_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_federated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.use_isolated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_ids

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_record_type

   .. autoattribute:: GradebookColumnLookupSession.gradebook_columns

   .. automethod:: GradebookColumnLookupSession.supports_summary

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradebookColumnQuerySession.gradebook_id

   .. autoattribute:: GradebookColumnQuerySession.gradebook

   .. automethod:: GradebookColumnQuerySession.can_search_gradebook_columns

   .. automethod:: GradebookColumnQuerySession.use_federated_gradebook_view

   .. automethod:: GradebookColumnQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradebookColumnQuerySession.gradebook_column_query

   .. automethod:: GradebookColumnQuerySession.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradebookColumnAdminSession.gradebook_id

   .. autoattribute:: GradebookColumnAdminSession.gradebook

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_column_with_record_types

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_create

   .. automethod:: GradebookColumnAdminSession.create_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_update_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_update

   .. automethod:: GradebookColumnAdminSession.update_gradebook_column

   .. automethod:: GradebookColumnAdminSession.sequence_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.move_gradebook_column

   .. automethod:: GradebookColumnAdminSession.copy_gradebook_column_entries

   .. automethod:: GradebookColumnAdminSession.can_delete_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.delete_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_manage_gradebook_column_aliases

   .. automethod:: GradebookColumnAdminSession.alias_gradebook_column



Grade Entry
-----------

.. autoclass:: GradeEntry
   :show-inheritance:

   .. autoattribute:: GradeEntry.gradebook_column_id

   .. autoattribute:: GradeEntry.gradebook_column

   .. autoattribute:: GradeEntry.key_resource_id

   .. autoattribute:: GradeEntry.key_resource

   .. automethod:: GradeEntry.is_derived

   .. automethod:: GradeEntry.overrides_calculated_entry

   .. autoattribute:: GradeEntry.overridden_calculated_entry_id

   .. autoattribute:: GradeEntry.overridden_calculated_entry

   .. automethod:: GradeEntry.is_ignored_for_calculations

   .. automethod:: GradeEntry.is_graded

   .. autoattribute:: GradeEntry.grade_id

   .. autoattribute:: GradeEntry.grade

   .. autoattribute:: GradeEntry.score

   .. autoattribute:: GradeEntry.time_graded

   .. autoattribute:: GradeEntry.grader_id

   .. autoattribute:: GradeEntry.grader

   .. autoattribute:: GradeEntry.grading_agent_id

   .. autoattribute:: GradeEntry.grading_agent

   .. automethod:: GradeEntry.get_grade_entry_record



Gradebook Lookup Methods
------------------------

   .. automethod:: GradebookLookupSession.can_lookup_gradebooks

   .. automethod:: GradebookLookupSession.use_comparative_gradebook_view

   .. automethod:: GradebookLookupSession.use_plenary_gradebook_view

   .. automethod:: GradebookLookupSession.get_gradebook

   .. automethod:: GradebookLookupSession.get_gradebooks_by_ids

   .. automethod:: GradebookLookupSession.get_gradebooks_by_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_parent_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_record_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_provider

   .. autoattribute:: GradebookLookupSession.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradebookAdminSession.can_create_gradebooks

   .. automethod:: GradebookAdminSession.can_create_gradebook_with_record_types

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_create

   .. automethod:: GradebookAdminSession.create_gradebook

   .. automethod:: GradebookAdminSession.can_update_gradebooks

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_update

   .. automethod:: GradebookAdminSession.update_gradebook

   .. automethod:: GradebookAdminSession.can_delete_gradebooks

   .. automethod:: GradebookAdminSession.delete_gradebook

   .. automethod:: GradebookAdminSession.can_manage_gradebook_aliases

   .. automethod:: GradebookAdminSession.alias_gradebook



Grade System Lookup Methods
---------------------------

   .. autoattribute:: GradeSystemLookupSession.gradebook_id

   .. autoattribute:: GradeSystemLookupSession.gradebook

   .. automethod:: GradeSystemLookupSession.can_lookup_grade_systems

   .. automethod:: GradeSystemLookupSession.use_comparative_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_plenary_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_federated_gradebook_view

   .. automethod:: GradeSystemLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeSystemLookupSession.get_grade_system

   .. automethod:: GradeSystemLookupSession.get_grade_system_by_grade

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_ids

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_parent_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_record_type

   .. autoattribute:: GradeSystemLookupSession.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: GradeSystemQuerySession.gradebook_id

   .. autoattribute:: GradeSystemQuerySession.gradebook

   .. automethod:: GradeSystemQuerySession.can_search_grade_systems

   .. automethod:: GradeSystemQuerySession.use_federated_gradebook_view

   .. automethod:: GradeSystemQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeSystemQuerySession.grade_system_query

   .. automethod:: GradeSystemQuerySession.get_grade_systems_by_query



Grade System Admin Methods
--------------------------

   .. autoattribute:: GradeSystemAdminSession.gradebook_id

   .. autoattribute:: GradeSystemAdminSession.gradebook

   .. automethod:: GradeSystemAdminSession.can_create_grade_systems

   .. automethod:: GradeSystemAdminSession.can_create_grade_system_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade_system

   .. automethod:: GradeSystemAdminSession.can_update_grade_systems

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade_system

   .. automethod:: GradeSystemAdminSession.can_delete_grade_systems

   .. automethod:: GradeSystemAdminSession.delete_grade_system

   .. automethod:: GradeSystemAdminSession.can_manage_grade_system_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade_system

   .. automethod:: GradeSystemAdminSession.can_create_grades

   .. automethod:: GradeSystemAdminSession.can_create_grade_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade

   .. automethod:: GradeSystemAdminSession.can_update_grades

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade

   .. automethod:: GradeSystemAdminSession.can_delete_grades

   .. automethod:: GradeSystemAdminSession.delete_grade

   .. automethod:: GradeSystemAdminSession.can_manage_grade_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: GradeEntryLookupSession.gradebook_id

   .. autoattribute:: GradeEntryLookupSession.gradebook

   .. automethod:: GradeEntryLookupSession.can_lookup_grade_entries

   .. automethod:: GradeEntryLookupSession.use_comparative_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_plenary_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_federated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_any_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.get_grade_entry

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_ids

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_parent_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_record_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_grader

   .. autoattribute:: GradeEntryLookupSession.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: GradeEntryQuerySession.gradebook_id

   .. autoattribute:: GradeEntryQuerySession.gradebook

   .. automethod:: GradeEntryQuerySession.can_search_grade_entries

   .. automethod:: GradeEntryQuerySession.use_federated_gradebook_view

   .. automethod:: GradeEntryQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeEntryQuerySession.grade_entry_query

   .. automethod:: GradeEntryQuerySession.get_grade_entries_by_query



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: GradeEntryAdminSession.gradebook_id

   .. autoattribute:: GradeEntryAdminSession.gradebook

   .. automethod:: GradeEntryAdminSession.can_create_grade_entries

   .. automethod:: GradeEntryAdminSession.can_create_grade_entry_with_record_types

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_create

   .. automethod:: GradeEntryAdminSession.create_grade_entry

   .. automethod:: GradeEntryAdminSession.can_overridecalculated_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_override

   .. automethod:: GradeEntryAdminSession.override_calculated_grade_entry

   .. automethod:: GradeEntryAdminSession.can_update_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_update

   .. automethod:: GradeEntryAdminSession.update_grade_entry

   .. automethod:: GradeEntryAdminSession.can_delete_grade_entries

   .. automethod:: GradeEntryAdminSession.delete_grade_entry

   .. automethod:: GradeEntryAdminSession.can_manage_grade_entry_aliases

   .. automethod:: GradeEntryAdminSession.alias_grade_entry



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradebookColumnLookupSession.gradebook_id

   .. autoattribute:: GradebookColumnLookupSession.gradebook

   .. automethod:: GradebookColumnLookupSession.can_lookup_gradebook_columns

   .. automethod:: GradebookColumnLookupSession.use_comparative_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_plenary_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_federated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.use_isolated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_ids

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_record_type

   .. autoattribute:: GradebookColumnLookupSession.gradebook_columns

   .. automethod:: GradebookColumnLookupSession.supports_summary

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradebookColumnQuerySession.gradebook_id

   .. autoattribute:: GradebookColumnQuerySession.gradebook

   .. automethod:: GradebookColumnQuerySession.can_search_gradebook_columns

   .. automethod:: GradebookColumnQuerySession.use_federated_gradebook_view

   .. automethod:: GradebookColumnQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradebookColumnQuerySession.gradebook_column_query

   .. automethod:: GradebookColumnQuerySession.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradebookColumnAdminSession.gradebook_id

   .. autoattribute:: GradebookColumnAdminSession.gradebook

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_column_with_record_types

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_create

   .. automethod:: GradebookColumnAdminSession.create_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_update_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_update

   .. automethod:: GradebookColumnAdminSession.update_gradebook_column

   .. automethod:: GradebookColumnAdminSession.sequence_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.move_gradebook_column

   .. automethod:: GradebookColumnAdminSession.copy_gradebook_column_entries

   .. automethod:: GradebookColumnAdminSession.can_delete_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.delete_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_manage_gradebook_column_aliases

   .. automethod:: GradebookColumnAdminSession.alias_gradebook_column



Grade Entry Form
----------------

.. autoclass:: GradeEntryForm
   :show-inheritance:

   .. autoattribute:: GradeEntryForm.ignored_for_calculations_metadata

   .. autoattribute:: GradeEntryForm.ignored_for_calculations

   .. autoattribute:: GradeEntryForm.grade_metadata

   .. autoattribute:: GradeEntryForm.grade

   .. autoattribute:: GradeEntryForm.score_metadata

   .. autoattribute:: GradeEntryForm.score

   .. automethod:: GradeEntryForm.get_grade_entry_form_record



Gradebook Lookup Methods
------------------------

   .. automethod:: GradebookLookupSession.can_lookup_gradebooks

   .. automethod:: GradebookLookupSession.use_comparative_gradebook_view

   .. automethod:: GradebookLookupSession.use_plenary_gradebook_view

   .. automethod:: GradebookLookupSession.get_gradebook

   .. automethod:: GradebookLookupSession.get_gradebooks_by_ids

   .. automethod:: GradebookLookupSession.get_gradebooks_by_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_parent_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_record_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_provider

   .. autoattribute:: GradebookLookupSession.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradebookAdminSession.can_create_gradebooks

   .. automethod:: GradebookAdminSession.can_create_gradebook_with_record_types

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_create

   .. automethod:: GradebookAdminSession.create_gradebook

   .. automethod:: GradebookAdminSession.can_update_gradebooks

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_update

   .. automethod:: GradebookAdminSession.update_gradebook

   .. automethod:: GradebookAdminSession.can_delete_gradebooks

   .. automethod:: GradebookAdminSession.delete_gradebook

   .. automethod:: GradebookAdminSession.can_manage_gradebook_aliases

   .. automethod:: GradebookAdminSession.alias_gradebook



Grade System Lookup Methods
---------------------------

   .. autoattribute:: GradeSystemLookupSession.gradebook_id

   .. autoattribute:: GradeSystemLookupSession.gradebook

   .. automethod:: GradeSystemLookupSession.can_lookup_grade_systems

   .. automethod:: GradeSystemLookupSession.use_comparative_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_plenary_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_federated_gradebook_view

   .. automethod:: GradeSystemLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeSystemLookupSession.get_grade_system

   .. automethod:: GradeSystemLookupSession.get_grade_system_by_grade

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_ids

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_parent_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_record_type

   .. autoattribute:: GradeSystemLookupSession.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: GradeSystemQuerySession.gradebook_id

   .. autoattribute:: GradeSystemQuerySession.gradebook

   .. automethod:: GradeSystemQuerySession.can_search_grade_systems

   .. automethod:: GradeSystemQuerySession.use_federated_gradebook_view

   .. automethod:: GradeSystemQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeSystemQuerySession.grade_system_query

   .. automethod:: GradeSystemQuerySession.get_grade_systems_by_query



Grade System Admin Methods
--------------------------

   .. autoattribute:: GradeSystemAdminSession.gradebook_id

   .. autoattribute:: GradeSystemAdminSession.gradebook

   .. automethod:: GradeSystemAdminSession.can_create_grade_systems

   .. automethod:: GradeSystemAdminSession.can_create_grade_system_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade_system

   .. automethod:: GradeSystemAdminSession.can_update_grade_systems

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade_system

   .. automethod:: GradeSystemAdminSession.can_delete_grade_systems

   .. automethod:: GradeSystemAdminSession.delete_grade_system

   .. automethod:: GradeSystemAdminSession.can_manage_grade_system_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade_system

   .. automethod:: GradeSystemAdminSession.can_create_grades

   .. automethod:: GradeSystemAdminSession.can_create_grade_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade

   .. automethod:: GradeSystemAdminSession.can_update_grades

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade

   .. automethod:: GradeSystemAdminSession.can_delete_grades

   .. automethod:: GradeSystemAdminSession.delete_grade

   .. automethod:: GradeSystemAdminSession.can_manage_grade_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: GradeEntryLookupSession.gradebook_id

   .. autoattribute:: GradeEntryLookupSession.gradebook

   .. automethod:: GradeEntryLookupSession.can_lookup_grade_entries

   .. automethod:: GradeEntryLookupSession.use_comparative_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_plenary_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_federated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_any_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.get_grade_entry

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_ids

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_parent_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_record_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_grader

   .. autoattribute:: GradeEntryLookupSession.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: GradeEntryQuerySession.gradebook_id

   .. autoattribute:: GradeEntryQuerySession.gradebook

   .. automethod:: GradeEntryQuerySession.can_search_grade_entries

   .. automethod:: GradeEntryQuerySession.use_federated_gradebook_view

   .. automethod:: GradeEntryQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeEntryQuerySession.grade_entry_query

   .. automethod:: GradeEntryQuerySession.get_grade_entries_by_query



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: GradeEntryAdminSession.gradebook_id

   .. autoattribute:: GradeEntryAdminSession.gradebook

   .. automethod:: GradeEntryAdminSession.can_create_grade_entries

   .. automethod:: GradeEntryAdminSession.can_create_grade_entry_with_record_types

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_create

   .. automethod:: GradeEntryAdminSession.create_grade_entry

   .. automethod:: GradeEntryAdminSession.can_overridecalculated_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_override

   .. automethod:: GradeEntryAdminSession.override_calculated_grade_entry

   .. automethod:: GradeEntryAdminSession.can_update_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_update

   .. automethod:: GradeEntryAdminSession.update_grade_entry

   .. automethod:: GradeEntryAdminSession.can_delete_grade_entries

   .. automethod:: GradeEntryAdminSession.delete_grade_entry

   .. automethod:: GradeEntryAdminSession.can_manage_grade_entry_aliases

   .. automethod:: GradeEntryAdminSession.alias_grade_entry



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradebookColumnLookupSession.gradebook_id

   .. autoattribute:: GradebookColumnLookupSession.gradebook

   .. automethod:: GradebookColumnLookupSession.can_lookup_gradebook_columns

   .. automethod:: GradebookColumnLookupSession.use_comparative_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_plenary_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_federated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.use_isolated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_ids

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_record_type

   .. autoattribute:: GradebookColumnLookupSession.gradebook_columns

   .. automethod:: GradebookColumnLookupSession.supports_summary

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradebookColumnQuerySession.gradebook_id

   .. autoattribute:: GradebookColumnQuerySession.gradebook

   .. automethod:: GradebookColumnQuerySession.can_search_gradebook_columns

   .. automethod:: GradebookColumnQuerySession.use_federated_gradebook_view

   .. automethod:: GradebookColumnQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradebookColumnQuerySession.gradebook_column_query

   .. automethod:: GradebookColumnQuerySession.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradebookColumnAdminSession.gradebook_id

   .. autoattribute:: GradebookColumnAdminSession.gradebook

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_column_with_record_types

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_create

   .. automethod:: GradebookColumnAdminSession.create_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_update_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_update

   .. automethod:: GradebookColumnAdminSession.update_gradebook_column

   .. automethod:: GradebookColumnAdminSession.sequence_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.move_gradebook_column

   .. automethod:: GradebookColumnAdminSession.copy_gradebook_column_entries

   .. automethod:: GradebookColumnAdminSession.can_delete_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.delete_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_manage_gradebook_column_aliases

   .. automethod:: GradebookColumnAdminSession.alias_gradebook_column



Grade Entry List
----------------

.. autoclass:: GradeEntryList
   :show-inheritance:

   .. autoattribute:: GradeEntryList.next_grade_entry

   .. automethod:: GradeEntryList.get_next_grade_entries



Gradebook Lookup Methods
------------------------

   .. automethod:: GradebookLookupSession.can_lookup_gradebooks

   .. automethod:: GradebookLookupSession.use_comparative_gradebook_view

   .. automethod:: GradebookLookupSession.use_plenary_gradebook_view

   .. automethod:: GradebookLookupSession.get_gradebook

   .. automethod:: GradebookLookupSession.get_gradebooks_by_ids

   .. automethod:: GradebookLookupSession.get_gradebooks_by_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_parent_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_record_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_provider

   .. autoattribute:: GradebookLookupSession.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradebookAdminSession.can_create_gradebooks

   .. automethod:: GradebookAdminSession.can_create_gradebook_with_record_types

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_create

   .. automethod:: GradebookAdminSession.create_gradebook

   .. automethod:: GradebookAdminSession.can_update_gradebooks

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_update

   .. automethod:: GradebookAdminSession.update_gradebook

   .. automethod:: GradebookAdminSession.can_delete_gradebooks

   .. automethod:: GradebookAdminSession.delete_gradebook

   .. automethod:: GradebookAdminSession.can_manage_gradebook_aliases

   .. automethod:: GradebookAdminSession.alias_gradebook



Grade System Lookup Methods
---------------------------

   .. autoattribute:: GradeSystemLookupSession.gradebook_id

   .. autoattribute:: GradeSystemLookupSession.gradebook

   .. automethod:: GradeSystemLookupSession.can_lookup_grade_systems

   .. automethod:: GradeSystemLookupSession.use_comparative_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_plenary_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_federated_gradebook_view

   .. automethod:: GradeSystemLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeSystemLookupSession.get_grade_system

   .. automethod:: GradeSystemLookupSession.get_grade_system_by_grade

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_ids

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_parent_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_record_type

   .. autoattribute:: GradeSystemLookupSession.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: GradeSystemQuerySession.gradebook_id

   .. autoattribute:: GradeSystemQuerySession.gradebook

   .. automethod:: GradeSystemQuerySession.can_search_grade_systems

   .. automethod:: GradeSystemQuerySession.use_federated_gradebook_view

   .. automethod:: GradeSystemQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeSystemQuerySession.grade_system_query

   .. automethod:: GradeSystemQuerySession.get_grade_systems_by_query



Grade System Admin Methods
--------------------------

   .. autoattribute:: GradeSystemAdminSession.gradebook_id

   .. autoattribute:: GradeSystemAdminSession.gradebook

   .. automethod:: GradeSystemAdminSession.can_create_grade_systems

   .. automethod:: GradeSystemAdminSession.can_create_grade_system_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade_system

   .. automethod:: GradeSystemAdminSession.can_update_grade_systems

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade_system

   .. automethod:: GradeSystemAdminSession.can_delete_grade_systems

   .. automethod:: GradeSystemAdminSession.delete_grade_system

   .. automethod:: GradeSystemAdminSession.can_manage_grade_system_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade_system

   .. automethod:: GradeSystemAdminSession.can_create_grades

   .. automethod:: GradeSystemAdminSession.can_create_grade_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade

   .. automethod:: GradeSystemAdminSession.can_update_grades

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade

   .. automethod:: GradeSystemAdminSession.can_delete_grades

   .. automethod:: GradeSystemAdminSession.delete_grade

   .. automethod:: GradeSystemAdminSession.can_manage_grade_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: GradeEntryLookupSession.gradebook_id

   .. autoattribute:: GradeEntryLookupSession.gradebook

   .. automethod:: GradeEntryLookupSession.can_lookup_grade_entries

   .. automethod:: GradeEntryLookupSession.use_comparative_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_plenary_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_federated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_any_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.get_grade_entry

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_ids

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_parent_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_record_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_grader

   .. autoattribute:: GradeEntryLookupSession.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: GradeEntryQuerySession.gradebook_id

   .. autoattribute:: GradeEntryQuerySession.gradebook

   .. automethod:: GradeEntryQuerySession.can_search_grade_entries

   .. automethod:: GradeEntryQuerySession.use_federated_gradebook_view

   .. automethod:: GradeEntryQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeEntryQuerySession.grade_entry_query

   .. automethod:: GradeEntryQuerySession.get_grade_entries_by_query



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: GradeEntryAdminSession.gradebook_id

   .. autoattribute:: GradeEntryAdminSession.gradebook

   .. automethod:: GradeEntryAdminSession.can_create_grade_entries

   .. automethod:: GradeEntryAdminSession.can_create_grade_entry_with_record_types

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_create

   .. automethod:: GradeEntryAdminSession.create_grade_entry

   .. automethod:: GradeEntryAdminSession.can_overridecalculated_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_override

   .. automethod:: GradeEntryAdminSession.override_calculated_grade_entry

   .. automethod:: GradeEntryAdminSession.can_update_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_update

   .. automethod:: GradeEntryAdminSession.update_grade_entry

   .. automethod:: GradeEntryAdminSession.can_delete_grade_entries

   .. automethod:: GradeEntryAdminSession.delete_grade_entry

   .. automethod:: GradeEntryAdminSession.can_manage_grade_entry_aliases

   .. automethod:: GradeEntryAdminSession.alias_grade_entry



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradebookColumnLookupSession.gradebook_id

   .. autoattribute:: GradebookColumnLookupSession.gradebook

   .. automethod:: GradebookColumnLookupSession.can_lookup_gradebook_columns

   .. automethod:: GradebookColumnLookupSession.use_comparative_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_plenary_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_federated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.use_isolated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_ids

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_record_type

   .. autoattribute:: GradebookColumnLookupSession.gradebook_columns

   .. automethod:: GradebookColumnLookupSession.supports_summary

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradebookColumnQuerySession.gradebook_id

   .. autoattribute:: GradebookColumnQuerySession.gradebook

   .. automethod:: GradebookColumnQuerySession.can_search_gradebook_columns

   .. automethod:: GradebookColumnQuerySession.use_federated_gradebook_view

   .. automethod:: GradebookColumnQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradebookColumnQuerySession.gradebook_column_query

   .. automethod:: GradebookColumnQuerySession.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradebookColumnAdminSession.gradebook_id

   .. autoattribute:: GradebookColumnAdminSession.gradebook

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_column_with_record_types

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_create

   .. automethod:: GradebookColumnAdminSession.create_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_update_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_update

   .. automethod:: GradebookColumnAdminSession.update_gradebook_column

   .. automethod:: GradebookColumnAdminSession.sequence_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.move_gradebook_column

   .. automethod:: GradebookColumnAdminSession.copy_gradebook_column_entries

   .. automethod:: GradebookColumnAdminSession.can_delete_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.delete_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_manage_gradebook_column_aliases

   .. automethod:: GradebookColumnAdminSession.alias_gradebook_column



Gradebook Column
----------------

.. autoclass:: GradebookColumn
   :show-inheritance:

   .. autoattribute:: GradebookColumn.grade_system_id

   .. autoattribute:: GradebookColumn.grade_system

   .. automethod:: GradebookColumn.get_gradebook_column_record



Gradebook Lookup Methods
------------------------

   .. automethod:: GradebookLookupSession.can_lookup_gradebooks

   .. automethod:: GradebookLookupSession.use_comparative_gradebook_view

   .. automethod:: GradebookLookupSession.use_plenary_gradebook_view

   .. automethod:: GradebookLookupSession.get_gradebook

   .. automethod:: GradebookLookupSession.get_gradebooks_by_ids

   .. automethod:: GradebookLookupSession.get_gradebooks_by_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_parent_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_record_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_provider

   .. autoattribute:: GradebookLookupSession.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradebookAdminSession.can_create_gradebooks

   .. automethod:: GradebookAdminSession.can_create_gradebook_with_record_types

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_create

   .. automethod:: GradebookAdminSession.create_gradebook

   .. automethod:: GradebookAdminSession.can_update_gradebooks

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_update

   .. automethod:: GradebookAdminSession.update_gradebook

   .. automethod:: GradebookAdminSession.can_delete_gradebooks

   .. automethod:: GradebookAdminSession.delete_gradebook

   .. automethod:: GradebookAdminSession.can_manage_gradebook_aliases

   .. automethod:: GradebookAdminSession.alias_gradebook



Grade System Lookup Methods
---------------------------

   .. autoattribute:: GradeSystemLookupSession.gradebook_id

   .. autoattribute:: GradeSystemLookupSession.gradebook

   .. automethod:: GradeSystemLookupSession.can_lookup_grade_systems

   .. automethod:: GradeSystemLookupSession.use_comparative_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_plenary_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_federated_gradebook_view

   .. automethod:: GradeSystemLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeSystemLookupSession.get_grade_system

   .. automethod:: GradeSystemLookupSession.get_grade_system_by_grade

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_ids

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_parent_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_record_type

   .. autoattribute:: GradeSystemLookupSession.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: GradeSystemQuerySession.gradebook_id

   .. autoattribute:: GradeSystemQuerySession.gradebook

   .. automethod:: GradeSystemQuerySession.can_search_grade_systems

   .. automethod:: GradeSystemQuerySession.use_federated_gradebook_view

   .. automethod:: GradeSystemQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeSystemQuerySession.grade_system_query

   .. automethod:: GradeSystemQuerySession.get_grade_systems_by_query



Grade System Admin Methods
--------------------------

   .. autoattribute:: GradeSystemAdminSession.gradebook_id

   .. autoattribute:: GradeSystemAdminSession.gradebook

   .. automethod:: GradeSystemAdminSession.can_create_grade_systems

   .. automethod:: GradeSystemAdminSession.can_create_grade_system_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade_system

   .. automethod:: GradeSystemAdminSession.can_update_grade_systems

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade_system

   .. automethod:: GradeSystemAdminSession.can_delete_grade_systems

   .. automethod:: GradeSystemAdminSession.delete_grade_system

   .. automethod:: GradeSystemAdminSession.can_manage_grade_system_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade_system

   .. automethod:: GradeSystemAdminSession.can_create_grades

   .. automethod:: GradeSystemAdminSession.can_create_grade_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade

   .. automethod:: GradeSystemAdminSession.can_update_grades

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade

   .. automethod:: GradeSystemAdminSession.can_delete_grades

   .. automethod:: GradeSystemAdminSession.delete_grade

   .. automethod:: GradeSystemAdminSession.can_manage_grade_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: GradeEntryLookupSession.gradebook_id

   .. autoattribute:: GradeEntryLookupSession.gradebook

   .. automethod:: GradeEntryLookupSession.can_lookup_grade_entries

   .. automethod:: GradeEntryLookupSession.use_comparative_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_plenary_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_federated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_any_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.get_grade_entry

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_ids

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_parent_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_record_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_grader

   .. autoattribute:: GradeEntryLookupSession.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: GradeEntryQuerySession.gradebook_id

   .. autoattribute:: GradeEntryQuerySession.gradebook

   .. automethod:: GradeEntryQuerySession.can_search_grade_entries

   .. automethod:: GradeEntryQuerySession.use_federated_gradebook_view

   .. automethod:: GradeEntryQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeEntryQuerySession.grade_entry_query

   .. automethod:: GradeEntryQuerySession.get_grade_entries_by_query



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: GradeEntryAdminSession.gradebook_id

   .. autoattribute:: GradeEntryAdminSession.gradebook

   .. automethod:: GradeEntryAdminSession.can_create_grade_entries

   .. automethod:: GradeEntryAdminSession.can_create_grade_entry_with_record_types

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_create

   .. automethod:: GradeEntryAdminSession.create_grade_entry

   .. automethod:: GradeEntryAdminSession.can_overridecalculated_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_override

   .. automethod:: GradeEntryAdminSession.override_calculated_grade_entry

   .. automethod:: GradeEntryAdminSession.can_update_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_update

   .. automethod:: GradeEntryAdminSession.update_grade_entry

   .. automethod:: GradeEntryAdminSession.can_delete_grade_entries

   .. automethod:: GradeEntryAdminSession.delete_grade_entry

   .. automethod:: GradeEntryAdminSession.can_manage_grade_entry_aliases

   .. automethod:: GradeEntryAdminSession.alias_grade_entry



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradebookColumnLookupSession.gradebook_id

   .. autoattribute:: GradebookColumnLookupSession.gradebook

   .. automethod:: GradebookColumnLookupSession.can_lookup_gradebook_columns

   .. automethod:: GradebookColumnLookupSession.use_comparative_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_plenary_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_federated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.use_isolated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_ids

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_record_type

   .. autoattribute:: GradebookColumnLookupSession.gradebook_columns

   .. automethod:: GradebookColumnLookupSession.supports_summary

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradebookColumnQuerySession.gradebook_id

   .. autoattribute:: GradebookColumnQuerySession.gradebook

   .. automethod:: GradebookColumnQuerySession.can_search_gradebook_columns

   .. automethod:: GradebookColumnQuerySession.use_federated_gradebook_view

   .. automethod:: GradebookColumnQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradebookColumnQuerySession.gradebook_column_query

   .. automethod:: GradebookColumnQuerySession.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradebookColumnAdminSession.gradebook_id

   .. autoattribute:: GradebookColumnAdminSession.gradebook

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_column_with_record_types

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_create

   .. automethod:: GradebookColumnAdminSession.create_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_update_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_update

   .. automethod:: GradebookColumnAdminSession.update_gradebook_column

   .. automethod:: GradebookColumnAdminSession.sequence_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.move_gradebook_column

   .. automethod:: GradebookColumnAdminSession.copy_gradebook_column_entries

   .. automethod:: GradebookColumnAdminSession.can_delete_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.delete_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_manage_gradebook_column_aliases

   .. automethod:: GradebookColumnAdminSession.alias_gradebook_column



Gradebook Column Form
---------------------

.. autoclass:: GradebookColumnForm
   :show-inheritance:

   .. autoattribute:: GradebookColumnForm.grade_system_metadata

   .. autoattribute:: GradebookColumnForm.grade_system

   .. automethod:: GradebookColumnForm.get_gradebook_column_form_record



Gradebook Lookup Methods
------------------------

   .. automethod:: GradebookLookupSession.can_lookup_gradebooks

   .. automethod:: GradebookLookupSession.use_comparative_gradebook_view

   .. automethod:: GradebookLookupSession.use_plenary_gradebook_view

   .. automethod:: GradebookLookupSession.get_gradebook

   .. automethod:: GradebookLookupSession.get_gradebooks_by_ids

   .. automethod:: GradebookLookupSession.get_gradebooks_by_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_parent_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_record_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_provider

   .. autoattribute:: GradebookLookupSession.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradebookAdminSession.can_create_gradebooks

   .. automethod:: GradebookAdminSession.can_create_gradebook_with_record_types

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_create

   .. automethod:: GradebookAdminSession.create_gradebook

   .. automethod:: GradebookAdminSession.can_update_gradebooks

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_update

   .. automethod:: GradebookAdminSession.update_gradebook

   .. automethod:: GradebookAdminSession.can_delete_gradebooks

   .. automethod:: GradebookAdminSession.delete_gradebook

   .. automethod:: GradebookAdminSession.can_manage_gradebook_aliases

   .. automethod:: GradebookAdminSession.alias_gradebook



Grade System Lookup Methods
---------------------------

   .. autoattribute:: GradeSystemLookupSession.gradebook_id

   .. autoattribute:: GradeSystemLookupSession.gradebook

   .. automethod:: GradeSystemLookupSession.can_lookup_grade_systems

   .. automethod:: GradeSystemLookupSession.use_comparative_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_plenary_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_federated_gradebook_view

   .. automethod:: GradeSystemLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeSystemLookupSession.get_grade_system

   .. automethod:: GradeSystemLookupSession.get_grade_system_by_grade

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_ids

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_parent_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_record_type

   .. autoattribute:: GradeSystemLookupSession.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: GradeSystemQuerySession.gradebook_id

   .. autoattribute:: GradeSystemQuerySession.gradebook

   .. automethod:: GradeSystemQuerySession.can_search_grade_systems

   .. automethod:: GradeSystemQuerySession.use_federated_gradebook_view

   .. automethod:: GradeSystemQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeSystemQuerySession.grade_system_query

   .. automethod:: GradeSystemQuerySession.get_grade_systems_by_query



Grade System Admin Methods
--------------------------

   .. autoattribute:: GradeSystemAdminSession.gradebook_id

   .. autoattribute:: GradeSystemAdminSession.gradebook

   .. automethod:: GradeSystemAdminSession.can_create_grade_systems

   .. automethod:: GradeSystemAdminSession.can_create_grade_system_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade_system

   .. automethod:: GradeSystemAdminSession.can_update_grade_systems

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade_system

   .. automethod:: GradeSystemAdminSession.can_delete_grade_systems

   .. automethod:: GradeSystemAdminSession.delete_grade_system

   .. automethod:: GradeSystemAdminSession.can_manage_grade_system_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade_system

   .. automethod:: GradeSystemAdminSession.can_create_grades

   .. automethod:: GradeSystemAdminSession.can_create_grade_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade

   .. automethod:: GradeSystemAdminSession.can_update_grades

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade

   .. automethod:: GradeSystemAdminSession.can_delete_grades

   .. automethod:: GradeSystemAdminSession.delete_grade

   .. automethod:: GradeSystemAdminSession.can_manage_grade_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: GradeEntryLookupSession.gradebook_id

   .. autoattribute:: GradeEntryLookupSession.gradebook

   .. automethod:: GradeEntryLookupSession.can_lookup_grade_entries

   .. automethod:: GradeEntryLookupSession.use_comparative_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_plenary_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_federated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_any_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.get_grade_entry

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_ids

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_parent_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_record_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_grader

   .. autoattribute:: GradeEntryLookupSession.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: GradeEntryQuerySession.gradebook_id

   .. autoattribute:: GradeEntryQuerySession.gradebook

   .. automethod:: GradeEntryQuerySession.can_search_grade_entries

   .. automethod:: GradeEntryQuerySession.use_federated_gradebook_view

   .. automethod:: GradeEntryQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeEntryQuerySession.grade_entry_query

   .. automethod:: GradeEntryQuerySession.get_grade_entries_by_query



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: GradeEntryAdminSession.gradebook_id

   .. autoattribute:: GradeEntryAdminSession.gradebook

   .. automethod:: GradeEntryAdminSession.can_create_grade_entries

   .. automethod:: GradeEntryAdminSession.can_create_grade_entry_with_record_types

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_create

   .. automethod:: GradeEntryAdminSession.create_grade_entry

   .. automethod:: GradeEntryAdminSession.can_overridecalculated_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_override

   .. automethod:: GradeEntryAdminSession.override_calculated_grade_entry

   .. automethod:: GradeEntryAdminSession.can_update_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_update

   .. automethod:: GradeEntryAdminSession.update_grade_entry

   .. automethod:: GradeEntryAdminSession.can_delete_grade_entries

   .. automethod:: GradeEntryAdminSession.delete_grade_entry

   .. automethod:: GradeEntryAdminSession.can_manage_grade_entry_aliases

   .. automethod:: GradeEntryAdminSession.alias_grade_entry



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradebookColumnLookupSession.gradebook_id

   .. autoattribute:: GradebookColumnLookupSession.gradebook

   .. automethod:: GradebookColumnLookupSession.can_lookup_gradebook_columns

   .. automethod:: GradebookColumnLookupSession.use_comparative_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_plenary_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_federated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.use_isolated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_ids

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_record_type

   .. autoattribute:: GradebookColumnLookupSession.gradebook_columns

   .. automethod:: GradebookColumnLookupSession.supports_summary

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradebookColumnQuerySession.gradebook_id

   .. autoattribute:: GradebookColumnQuerySession.gradebook

   .. automethod:: GradebookColumnQuerySession.can_search_gradebook_columns

   .. automethod:: GradebookColumnQuerySession.use_federated_gradebook_view

   .. automethod:: GradebookColumnQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradebookColumnQuerySession.gradebook_column_query

   .. automethod:: GradebookColumnQuerySession.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradebookColumnAdminSession.gradebook_id

   .. autoattribute:: GradebookColumnAdminSession.gradebook

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_column_with_record_types

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_create

   .. automethod:: GradebookColumnAdminSession.create_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_update_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_update

   .. automethod:: GradebookColumnAdminSession.update_gradebook_column

   .. automethod:: GradebookColumnAdminSession.sequence_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.move_gradebook_column

   .. automethod:: GradebookColumnAdminSession.copy_gradebook_column_entries

   .. automethod:: GradebookColumnAdminSession.can_delete_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.delete_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_manage_gradebook_column_aliases

   .. automethod:: GradebookColumnAdminSession.alias_gradebook_column



Gradebook Column List
---------------------

.. autoclass:: GradebookColumnList
   :show-inheritance:

   .. autoattribute:: GradebookColumnList.next_gradebook_column

   .. automethod:: GradebookColumnList.get_next_gradebook_columns



Gradebook Lookup Methods
------------------------

   .. automethod:: GradebookLookupSession.can_lookup_gradebooks

   .. automethod:: GradebookLookupSession.use_comparative_gradebook_view

   .. automethod:: GradebookLookupSession.use_plenary_gradebook_view

   .. automethod:: GradebookLookupSession.get_gradebook

   .. automethod:: GradebookLookupSession.get_gradebooks_by_ids

   .. automethod:: GradebookLookupSession.get_gradebooks_by_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_parent_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_record_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_provider

   .. autoattribute:: GradebookLookupSession.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradebookAdminSession.can_create_gradebooks

   .. automethod:: GradebookAdminSession.can_create_gradebook_with_record_types

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_create

   .. automethod:: GradebookAdminSession.create_gradebook

   .. automethod:: GradebookAdminSession.can_update_gradebooks

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_update

   .. automethod:: GradebookAdminSession.update_gradebook

   .. automethod:: GradebookAdminSession.can_delete_gradebooks

   .. automethod:: GradebookAdminSession.delete_gradebook

   .. automethod:: GradebookAdminSession.can_manage_gradebook_aliases

   .. automethod:: GradebookAdminSession.alias_gradebook



Grade System Lookup Methods
---------------------------

   .. autoattribute:: GradeSystemLookupSession.gradebook_id

   .. autoattribute:: GradeSystemLookupSession.gradebook

   .. automethod:: GradeSystemLookupSession.can_lookup_grade_systems

   .. automethod:: GradeSystemLookupSession.use_comparative_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_plenary_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_federated_gradebook_view

   .. automethod:: GradeSystemLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeSystemLookupSession.get_grade_system

   .. automethod:: GradeSystemLookupSession.get_grade_system_by_grade

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_ids

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_parent_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_record_type

   .. autoattribute:: GradeSystemLookupSession.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: GradeSystemQuerySession.gradebook_id

   .. autoattribute:: GradeSystemQuerySession.gradebook

   .. automethod:: GradeSystemQuerySession.can_search_grade_systems

   .. automethod:: GradeSystemQuerySession.use_federated_gradebook_view

   .. automethod:: GradeSystemQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeSystemQuerySession.grade_system_query

   .. automethod:: GradeSystemQuerySession.get_grade_systems_by_query



Grade System Admin Methods
--------------------------

   .. autoattribute:: GradeSystemAdminSession.gradebook_id

   .. autoattribute:: GradeSystemAdminSession.gradebook

   .. automethod:: GradeSystemAdminSession.can_create_grade_systems

   .. automethod:: GradeSystemAdminSession.can_create_grade_system_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade_system

   .. automethod:: GradeSystemAdminSession.can_update_grade_systems

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade_system

   .. automethod:: GradeSystemAdminSession.can_delete_grade_systems

   .. automethod:: GradeSystemAdminSession.delete_grade_system

   .. automethod:: GradeSystemAdminSession.can_manage_grade_system_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade_system

   .. automethod:: GradeSystemAdminSession.can_create_grades

   .. automethod:: GradeSystemAdminSession.can_create_grade_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade

   .. automethod:: GradeSystemAdminSession.can_update_grades

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade

   .. automethod:: GradeSystemAdminSession.can_delete_grades

   .. automethod:: GradeSystemAdminSession.delete_grade

   .. automethod:: GradeSystemAdminSession.can_manage_grade_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: GradeEntryLookupSession.gradebook_id

   .. autoattribute:: GradeEntryLookupSession.gradebook

   .. automethod:: GradeEntryLookupSession.can_lookup_grade_entries

   .. automethod:: GradeEntryLookupSession.use_comparative_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_plenary_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_federated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_any_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.get_grade_entry

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_ids

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_parent_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_record_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_grader

   .. autoattribute:: GradeEntryLookupSession.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: GradeEntryQuerySession.gradebook_id

   .. autoattribute:: GradeEntryQuerySession.gradebook

   .. automethod:: GradeEntryQuerySession.can_search_grade_entries

   .. automethod:: GradeEntryQuerySession.use_federated_gradebook_view

   .. automethod:: GradeEntryQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeEntryQuerySession.grade_entry_query

   .. automethod:: GradeEntryQuerySession.get_grade_entries_by_query



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: GradeEntryAdminSession.gradebook_id

   .. autoattribute:: GradeEntryAdminSession.gradebook

   .. automethod:: GradeEntryAdminSession.can_create_grade_entries

   .. automethod:: GradeEntryAdminSession.can_create_grade_entry_with_record_types

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_create

   .. automethod:: GradeEntryAdminSession.create_grade_entry

   .. automethod:: GradeEntryAdminSession.can_overridecalculated_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_override

   .. automethod:: GradeEntryAdminSession.override_calculated_grade_entry

   .. automethod:: GradeEntryAdminSession.can_update_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_update

   .. automethod:: GradeEntryAdminSession.update_grade_entry

   .. automethod:: GradeEntryAdminSession.can_delete_grade_entries

   .. automethod:: GradeEntryAdminSession.delete_grade_entry

   .. automethod:: GradeEntryAdminSession.can_manage_grade_entry_aliases

   .. automethod:: GradeEntryAdminSession.alias_grade_entry



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradebookColumnLookupSession.gradebook_id

   .. autoattribute:: GradebookColumnLookupSession.gradebook

   .. automethod:: GradebookColumnLookupSession.can_lookup_gradebook_columns

   .. automethod:: GradebookColumnLookupSession.use_comparative_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_plenary_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_federated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.use_isolated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_ids

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_record_type

   .. autoattribute:: GradebookColumnLookupSession.gradebook_columns

   .. automethod:: GradebookColumnLookupSession.supports_summary

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradebookColumnQuerySession.gradebook_id

   .. autoattribute:: GradebookColumnQuerySession.gradebook

   .. automethod:: GradebookColumnQuerySession.can_search_gradebook_columns

   .. automethod:: GradebookColumnQuerySession.use_federated_gradebook_view

   .. automethod:: GradebookColumnQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradebookColumnQuerySession.gradebook_column_query

   .. automethod:: GradebookColumnQuerySession.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradebookColumnAdminSession.gradebook_id

   .. autoattribute:: GradebookColumnAdminSession.gradebook

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_column_with_record_types

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_create

   .. automethod:: GradebookColumnAdminSession.create_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_update_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_update

   .. automethod:: GradebookColumnAdminSession.update_gradebook_column

   .. automethod:: GradebookColumnAdminSession.sequence_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.move_gradebook_column

   .. automethod:: GradebookColumnAdminSession.copy_gradebook_column_entries

   .. automethod:: GradebookColumnAdminSession.can_delete_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.delete_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_manage_gradebook_column_aliases

   .. automethod:: GradebookColumnAdminSession.alias_gradebook_column



Gradebook Column Summary
------------------------

.. autoclass:: GradebookColumnSummary
   :show-inheritance:

   .. autoattribute:: GradebookColumnSummary.gradebook_column_id

   .. autoattribute:: GradebookColumnSummary.gradebook_column

   .. autoattribute:: GradebookColumnSummary.mean

   .. autoattribute:: GradebookColumnSummary.median

   .. autoattribute:: GradebookColumnSummary.mode

   .. autoattribute:: GradebookColumnSummary.rms

   .. autoattribute:: GradebookColumnSummary.standard_deviation

   .. autoattribute:: GradebookColumnSummary.sum

   .. automethod:: GradebookColumnSummary.get_gradebook_column_summary_record



Gradebook Lookup Methods
------------------------

   .. automethod:: GradebookLookupSession.can_lookup_gradebooks

   .. automethod:: GradebookLookupSession.use_comparative_gradebook_view

   .. automethod:: GradebookLookupSession.use_plenary_gradebook_view

   .. automethod:: GradebookLookupSession.get_gradebook

   .. automethod:: GradebookLookupSession.get_gradebooks_by_ids

   .. automethod:: GradebookLookupSession.get_gradebooks_by_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_parent_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_record_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_provider

   .. autoattribute:: GradebookLookupSession.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradebookAdminSession.can_create_gradebooks

   .. automethod:: GradebookAdminSession.can_create_gradebook_with_record_types

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_create

   .. automethod:: GradebookAdminSession.create_gradebook

   .. automethod:: GradebookAdminSession.can_update_gradebooks

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_update

   .. automethod:: GradebookAdminSession.update_gradebook

   .. automethod:: GradebookAdminSession.can_delete_gradebooks

   .. automethod:: GradebookAdminSession.delete_gradebook

   .. automethod:: GradebookAdminSession.can_manage_gradebook_aliases

   .. automethod:: GradebookAdminSession.alias_gradebook



Grade System Lookup Methods
---------------------------

   .. autoattribute:: GradeSystemLookupSession.gradebook_id

   .. autoattribute:: GradeSystemLookupSession.gradebook

   .. automethod:: GradeSystemLookupSession.can_lookup_grade_systems

   .. automethod:: GradeSystemLookupSession.use_comparative_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_plenary_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_federated_gradebook_view

   .. automethod:: GradeSystemLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeSystemLookupSession.get_grade_system

   .. automethod:: GradeSystemLookupSession.get_grade_system_by_grade

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_ids

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_parent_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_record_type

   .. autoattribute:: GradeSystemLookupSession.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: GradeSystemQuerySession.gradebook_id

   .. autoattribute:: GradeSystemQuerySession.gradebook

   .. automethod:: GradeSystemQuerySession.can_search_grade_systems

   .. automethod:: GradeSystemQuerySession.use_federated_gradebook_view

   .. automethod:: GradeSystemQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeSystemQuerySession.grade_system_query

   .. automethod:: GradeSystemQuerySession.get_grade_systems_by_query



Grade System Admin Methods
--------------------------

   .. autoattribute:: GradeSystemAdminSession.gradebook_id

   .. autoattribute:: GradeSystemAdminSession.gradebook

   .. automethod:: GradeSystemAdminSession.can_create_grade_systems

   .. automethod:: GradeSystemAdminSession.can_create_grade_system_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade_system

   .. automethod:: GradeSystemAdminSession.can_update_grade_systems

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade_system

   .. automethod:: GradeSystemAdminSession.can_delete_grade_systems

   .. automethod:: GradeSystemAdminSession.delete_grade_system

   .. automethod:: GradeSystemAdminSession.can_manage_grade_system_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade_system

   .. automethod:: GradeSystemAdminSession.can_create_grades

   .. automethod:: GradeSystemAdminSession.can_create_grade_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade

   .. automethod:: GradeSystemAdminSession.can_update_grades

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade

   .. automethod:: GradeSystemAdminSession.can_delete_grades

   .. automethod:: GradeSystemAdminSession.delete_grade

   .. automethod:: GradeSystemAdminSession.can_manage_grade_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: GradeEntryLookupSession.gradebook_id

   .. autoattribute:: GradeEntryLookupSession.gradebook

   .. automethod:: GradeEntryLookupSession.can_lookup_grade_entries

   .. automethod:: GradeEntryLookupSession.use_comparative_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_plenary_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_federated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_any_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.get_grade_entry

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_ids

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_parent_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_record_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_grader

   .. autoattribute:: GradeEntryLookupSession.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: GradeEntryQuerySession.gradebook_id

   .. autoattribute:: GradeEntryQuerySession.gradebook

   .. automethod:: GradeEntryQuerySession.can_search_grade_entries

   .. automethod:: GradeEntryQuerySession.use_federated_gradebook_view

   .. automethod:: GradeEntryQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeEntryQuerySession.grade_entry_query

   .. automethod:: GradeEntryQuerySession.get_grade_entries_by_query



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: GradeEntryAdminSession.gradebook_id

   .. autoattribute:: GradeEntryAdminSession.gradebook

   .. automethod:: GradeEntryAdminSession.can_create_grade_entries

   .. automethod:: GradeEntryAdminSession.can_create_grade_entry_with_record_types

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_create

   .. automethod:: GradeEntryAdminSession.create_grade_entry

   .. automethod:: GradeEntryAdminSession.can_overridecalculated_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_override

   .. automethod:: GradeEntryAdminSession.override_calculated_grade_entry

   .. automethod:: GradeEntryAdminSession.can_update_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_update

   .. automethod:: GradeEntryAdminSession.update_grade_entry

   .. automethod:: GradeEntryAdminSession.can_delete_grade_entries

   .. automethod:: GradeEntryAdminSession.delete_grade_entry

   .. automethod:: GradeEntryAdminSession.can_manage_grade_entry_aliases

   .. automethod:: GradeEntryAdminSession.alias_grade_entry



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradebookColumnLookupSession.gradebook_id

   .. autoattribute:: GradebookColumnLookupSession.gradebook

   .. automethod:: GradebookColumnLookupSession.can_lookup_gradebook_columns

   .. automethod:: GradebookColumnLookupSession.use_comparative_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_plenary_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_federated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.use_isolated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_ids

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_record_type

   .. autoattribute:: GradebookColumnLookupSession.gradebook_columns

   .. automethod:: GradebookColumnLookupSession.supports_summary

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradebookColumnQuerySession.gradebook_id

   .. autoattribute:: GradebookColumnQuerySession.gradebook

   .. automethod:: GradebookColumnQuerySession.can_search_gradebook_columns

   .. automethod:: GradebookColumnQuerySession.use_federated_gradebook_view

   .. automethod:: GradebookColumnQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradebookColumnQuerySession.gradebook_column_query

   .. automethod:: GradebookColumnQuerySession.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradebookColumnAdminSession.gradebook_id

   .. autoattribute:: GradebookColumnAdminSession.gradebook

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_column_with_record_types

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_create

   .. automethod:: GradebookColumnAdminSession.create_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_update_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_update

   .. automethod:: GradebookColumnAdminSession.update_gradebook_column

   .. automethod:: GradebookColumnAdminSession.sequence_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.move_gradebook_column

   .. automethod:: GradebookColumnAdminSession.copy_gradebook_column_entries

   .. automethod:: GradebookColumnAdminSession.can_delete_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.delete_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_manage_gradebook_column_aliases

   .. automethod:: GradebookColumnAdminSession.alias_gradebook_column



Gradebook Form
--------------

.. autoclass:: GradebookForm
   :show-inheritance:

   .. automethod:: GradebookForm.get_gradebook_form_record



Gradebook Lookup Methods
------------------------

   .. automethod:: GradebookLookupSession.can_lookup_gradebooks

   .. automethod:: GradebookLookupSession.use_comparative_gradebook_view

   .. automethod:: GradebookLookupSession.use_plenary_gradebook_view

   .. automethod:: GradebookLookupSession.get_gradebook

   .. automethod:: GradebookLookupSession.get_gradebooks_by_ids

   .. automethod:: GradebookLookupSession.get_gradebooks_by_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_parent_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_record_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_provider

   .. autoattribute:: GradebookLookupSession.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradebookAdminSession.can_create_gradebooks

   .. automethod:: GradebookAdminSession.can_create_gradebook_with_record_types

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_create

   .. automethod:: GradebookAdminSession.create_gradebook

   .. automethod:: GradebookAdminSession.can_update_gradebooks

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_update

   .. automethod:: GradebookAdminSession.update_gradebook

   .. automethod:: GradebookAdminSession.can_delete_gradebooks

   .. automethod:: GradebookAdminSession.delete_gradebook

   .. automethod:: GradebookAdminSession.can_manage_gradebook_aliases

   .. automethod:: GradebookAdminSession.alias_gradebook



Grade System Lookup Methods
---------------------------

   .. autoattribute:: GradeSystemLookupSession.gradebook_id

   .. autoattribute:: GradeSystemLookupSession.gradebook

   .. automethod:: GradeSystemLookupSession.can_lookup_grade_systems

   .. automethod:: GradeSystemLookupSession.use_comparative_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_plenary_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_federated_gradebook_view

   .. automethod:: GradeSystemLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeSystemLookupSession.get_grade_system

   .. automethod:: GradeSystemLookupSession.get_grade_system_by_grade

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_ids

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_parent_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_record_type

   .. autoattribute:: GradeSystemLookupSession.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: GradeSystemQuerySession.gradebook_id

   .. autoattribute:: GradeSystemQuerySession.gradebook

   .. automethod:: GradeSystemQuerySession.can_search_grade_systems

   .. automethod:: GradeSystemQuerySession.use_federated_gradebook_view

   .. automethod:: GradeSystemQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeSystemQuerySession.grade_system_query

   .. automethod:: GradeSystemQuerySession.get_grade_systems_by_query



Grade System Admin Methods
--------------------------

   .. autoattribute:: GradeSystemAdminSession.gradebook_id

   .. autoattribute:: GradeSystemAdminSession.gradebook

   .. automethod:: GradeSystemAdminSession.can_create_grade_systems

   .. automethod:: GradeSystemAdminSession.can_create_grade_system_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade_system

   .. automethod:: GradeSystemAdminSession.can_update_grade_systems

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade_system

   .. automethod:: GradeSystemAdminSession.can_delete_grade_systems

   .. automethod:: GradeSystemAdminSession.delete_grade_system

   .. automethod:: GradeSystemAdminSession.can_manage_grade_system_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade_system

   .. automethod:: GradeSystemAdminSession.can_create_grades

   .. automethod:: GradeSystemAdminSession.can_create_grade_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade

   .. automethod:: GradeSystemAdminSession.can_update_grades

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade

   .. automethod:: GradeSystemAdminSession.can_delete_grades

   .. automethod:: GradeSystemAdminSession.delete_grade

   .. automethod:: GradeSystemAdminSession.can_manage_grade_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: GradeEntryLookupSession.gradebook_id

   .. autoattribute:: GradeEntryLookupSession.gradebook

   .. automethod:: GradeEntryLookupSession.can_lookup_grade_entries

   .. automethod:: GradeEntryLookupSession.use_comparative_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_plenary_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_federated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_any_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.get_grade_entry

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_ids

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_parent_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_record_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_grader

   .. autoattribute:: GradeEntryLookupSession.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: GradeEntryQuerySession.gradebook_id

   .. autoattribute:: GradeEntryQuerySession.gradebook

   .. automethod:: GradeEntryQuerySession.can_search_grade_entries

   .. automethod:: GradeEntryQuerySession.use_federated_gradebook_view

   .. automethod:: GradeEntryQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeEntryQuerySession.grade_entry_query

   .. automethod:: GradeEntryQuerySession.get_grade_entries_by_query



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: GradeEntryAdminSession.gradebook_id

   .. autoattribute:: GradeEntryAdminSession.gradebook

   .. automethod:: GradeEntryAdminSession.can_create_grade_entries

   .. automethod:: GradeEntryAdminSession.can_create_grade_entry_with_record_types

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_create

   .. automethod:: GradeEntryAdminSession.create_grade_entry

   .. automethod:: GradeEntryAdminSession.can_overridecalculated_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_override

   .. automethod:: GradeEntryAdminSession.override_calculated_grade_entry

   .. automethod:: GradeEntryAdminSession.can_update_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_update

   .. automethod:: GradeEntryAdminSession.update_grade_entry

   .. automethod:: GradeEntryAdminSession.can_delete_grade_entries

   .. automethod:: GradeEntryAdminSession.delete_grade_entry

   .. automethod:: GradeEntryAdminSession.can_manage_grade_entry_aliases

   .. automethod:: GradeEntryAdminSession.alias_grade_entry



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradebookColumnLookupSession.gradebook_id

   .. autoattribute:: GradebookColumnLookupSession.gradebook

   .. automethod:: GradebookColumnLookupSession.can_lookup_gradebook_columns

   .. automethod:: GradebookColumnLookupSession.use_comparative_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_plenary_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_federated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.use_isolated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_ids

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_record_type

   .. autoattribute:: GradebookColumnLookupSession.gradebook_columns

   .. automethod:: GradebookColumnLookupSession.supports_summary

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradebookColumnQuerySession.gradebook_id

   .. autoattribute:: GradebookColumnQuerySession.gradebook

   .. automethod:: GradebookColumnQuerySession.can_search_gradebook_columns

   .. automethod:: GradebookColumnQuerySession.use_federated_gradebook_view

   .. automethod:: GradebookColumnQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradebookColumnQuerySession.gradebook_column_query

   .. automethod:: GradebookColumnQuerySession.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradebookColumnAdminSession.gradebook_id

   .. autoattribute:: GradebookColumnAdminSession.gradebook

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_column_with_record_types

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_create

   .. automethod:: GradebookColumnAdminSession.create_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_update_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_update

   .. automethod:: GradebookColumnAdminSession.update_gradebook_column

   .. automethod:: GradebookColumnAdminSession.sequence_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.move_gradebook_column

   .. automethod:: GradebookColumnAdminSession.copy_gradebook_column_entries

   .. automethod:: GradebookColumnAdminSession.can_delete_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.delete_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_manage_gradebook_column_aliases

   .. automethod:: GradebookColumnAdminSession.alias_gradebook_column



Gradebook List
--------------

.. autoclass:: GradebookList
   :show-inheritance:

   .. autoattribute:: GradebookList.next_gradebook

   .. automethod:: GradebookList.get_next_gradebooks



Gradebook Lookup Methods
------------------------

   .. automethod:: GradebookLookupSession.can_lookup_gradebooks

   .. automethod:: GradebookLookupSession.use_comparative_gradebook_view

   .. automethod:: GradebookLookupSession.use_plenary_gradebook_view

   .. automethod:: GradebookLookupSession.get_gradebook

   .. automethod:: GradebookLookupSession.get_gradebooks_by_ids

   .. automethod:: GradebookLookupSession.get_gradebooks_by_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_parent_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_record_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_provider

   .. autoattribute:: GradebookLookupSession.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradebookAdminSession.can_create_gradebooks

   .. automethod:: GradebookAdminSession.can_create_gradebook_with_record_types

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_create

   .. automethod:: GradebookAdminSession.create_gradebook

   .. automethod:: GradebookAdminSession.can_update_gradebooks

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_update

   .. automethod:: GradebookAdminSession.update_gradebook

   .. automethod:: GradebookAdminSession.can_delete_gradebooks

   .. automethod:: GradebookAdminSession.delete_gradebook

   .. automethod:: GradebookAdminSession.can_manage_gradebook_aliases

   .. automethod:: GradebookAdminSession.alias_gradebook



Grade System Lookup Methods
---------------------------

   .. autoattribute:: GradeSystemLookupSession.gradebook_id

   .. autoattribute:: GradeSystemLookupSession.gradebook

   .. automethod:: GradeSystemLookupSession.can_lookup_grade_systems

   .. automethod:: GradeSystemLookupSession.use_comparative_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_plenary_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_federated_gradebook_view

   .. automethod:: GradeSystemLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeSystemLookupSession.get_grade_system

   .. automethod:: GradeSystemLookupSession.get_grade_system_by_grade

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_ids

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_parent_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_record_type

   .. autoattribute:: GradeSystemLookupSession.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: GradeSystemQuerySession.gradebook_id

   .. autoattribute:: GradeSystemQuerySession.gradebook

   .. automethod:: GradeSystemQuerySession.can_search_grade_systems

   .. automethod:: GradeSystemQuerySession.use_federated_gradebook_view

   .. automethod:: GradeSystemQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeSystemQuerySession.grade_system_query

   .. automethod:: GradeSystemQuerySession.get_grade_systems_by_query



Grade System Admin Methods
--------------------------

   .. autoattribute:: GradeSystemAdminSession.gradebook_id

   .. autoattribute:: GradeSystemAdminSession.gradebook

   .. automethod:: GradeSystemAdminSession.can_create_grade_systems

   .. automethod:: GradeSystemAdminSession.can_create_grade_system_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade_system

   .. automethod:: GradeSystemAdminSession.can_update_grade_systems

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade_system

   .. automethod:: GradeSystemAdminSession.can_delete_grade_systems

   .. automethod:: GradeSystemAdminSession.delete_grade_system

   .. automethod:: GradeSystemAdminSession.can_manage_grade_system_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade_system

   .. automethod:: GradeSystemAdminSession.can_create_grades

   .. automethod:: GradeSystemAdminSession.can_create_grade_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade

   .. automethod:: GradeSystemAdminSession.can_update_grades

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade

   .. automethod:: GradeSystemAdminSession.can_delete_grades

   .. automethod:: GradeSystemAdminSession.delete_grade

   .. automethod:: GradeSystemAdminSession.can_manage_grade_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: GradeEntryLookupSession.gradebook_id

   .. autoattribute:: GradeEntryLookupSession.gradebook

   .. automethod:: GradeEntryLookupSession.can_lookup_grade_entries

   .. automethod:: GradeEntryLookupSession.use_comparative_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_plenary_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_federated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_any_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.get_grade_entry

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_ids

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_parent_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_record_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_grader

   .. autoattribute:: GradeEntryLookupSession.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: GradeEntryQuerySession.gradebook_id

   .. autoattribute:: GradeEntryQuerySession.gradebook

   .. automethod:: GradeEntryQuerySession.can_search_grade_entries

   .. automethod:: GradeEntryQuerySession.use_federated_gradebook_view

   .. automethod:: GradeEntryQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeEntryQuerySession.grade_entry_query

   .. automethod:: GradeEntryQuerySession.get_grade_entries_by_query



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: GradeEntryAdminSession.gradebook_id

   .. autoattribute:: GradeEntryAdminSession.gradebook

   .. automethod:: GradeEntryAdminSession.can_create_grade_entries

   .. automethod:: GradeEntryAdminSession.can_create_grade_entry_with_record_types

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_create

   .. automethod:: GradeEntryAdminSession.create_grade_entry

   .. automethod:: GradeEntryAdminSession.can_overridecalculated_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_override

   .. automethod:: GradeEntryAdminSession.override_calculated_grade_entry

   .. automethod:: GradeEntryAdminSession.can_update_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_update

   .. automethod:: GradeEntryAdminSession.update_grade_entry

   .. automethod:: GradeEntryAdminSession.can_delete_grade_entries

   .. automethod:: GradeEntryAdminSession.delete_grade_entry

   .. automethod:: GradeEntryAdminSession.can_manage_grade_entry_aliases

   .. automethod:: GradeEntryAdminSession.alias_grade_entry



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradebookColumnLookupSession.gradebook_id

   .. autoattribute:: GradebookColumnLookupSession.gradebook

   .. automethod:: GradebookColumnLookupSession.can_lookup_gradebook_columns

   .. automethod:: GradebookColumnLookupSession.use_comparative_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_plenary_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_federated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.use_isolated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_ids

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_record_type

   .. autoattribute:: GradebookColumnLookupSession.gradebook_columns

   .. automethod:: GradebookColumnLookupSession.supports_summary

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradebookColumnQuerySession.gradebook_id

   .. autoattribute:: GradebookColumnQuerySession.gradebook

   .. automethod:: GradebookColumnQuerySession.can_search_gradebook_columns

   .. automethod:: GradebookColumnQuerySession.use_federated_gradebook_view

   .. automethod:: GradebookColumnQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradebookColumnQuerySession.gradebook_column_query

   .. automethod:: GradebookColumnQuerySession.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradebookColumnAdminSession.gradebook_id

   .. autoattribute:: GradebookColumnAdminSession.gradebook

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_column_with_record_types

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_create

   .. automethod:: GradebookColumnAdminSession.create_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_update_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_update

   .. automethod:: GradebookColumnAdminSession.update_gradebook_column

   .. automethod:: GradebookColumnAdminSession.sequence_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.move_gradebook_column

   .. automethod:: GradebookColumnAdminSession.copy_gradebook_column_entries

   .. automethod:: GradebookColumnAdminSession.can_delete_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.delete_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_manage_gradebook_column_aliases

   .. automethod:: GradebookColumnAdminSession.alias_gradebook_column



Gradebook Node
--------------

.. autoclass:: GradebookNode
   :show-inheritance:

   .. autoattribute:: GradebookNode.gradebook

   .. autoattribute:: GradebookNode.parent_gradebook_nodes

   .. autoattribute:: GradebookNode.child_gradebook_nodes



Gradebook Lookup Methods
------------------------

   .. automethod:: GradebookLookupSession.can_lookup_gradebooks

   .. automethod:: GradebookLookupSession.use_comparative_gradebook_view

   .. automethod:: GradebookLookupSession.use_plenary_gradebook_view

   .. automethod:: GradebookLookupSession.get_gradebook

   .. automethod:: GradebookLookupSession.get_gradebooks_by_ids

   .. automethod:: GradebookLookupSession.get_gradebooks_by_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_parent_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_record_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_provider

   .. autoattribute:: GradebookLookupSession.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradebookAdminSession.can_create_gradebooks

   .. automethod:: GradebookAdminSession.can_create_gradebook_with_record_types

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_create

   .. automethod:: GradebookAdminSession.create_gradebook

   .. automethod:: GradebookAdminSession.can_update_gradebooks

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_update

   .. automethod:: GradebookAdminSession.update_gradebook

   .. automethod:: GradebookAdminSession.can_delete_gradebooks

   .. automethod:: GradebookAdminSession.delete_gradebook

   .. automethod:: GradebookAdminSession.can_manage_gradebook_aliases

   .. automethod:: GradebookAdminSession.alias_gradebook



Grade System Lookup Methods
---------------------------

   .. autoattribute:: GradeSystemLookupSession.gradebook_id

   .. autoattribute:: GradeSystemLookupSession.gradebook

   .. automethod:: GradeSystemLookupSession.can_lookup_grade_systems

   .. automethod:: GradeSystemLookupSession.use_comparative_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_plenary_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_federated_gradebook_view

   .. automethod:: GradeSystemLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeSystemLookupSession.get_grade_system

   .. automethod:: GradeSystemLookupSession.get_grade_system_by_grade

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_ids

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_parent_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_record_type

   .. autoattribute:: GradeSystemLookupSession.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: GradeSystemQuerySession.gradebook_id

   .. autoattribute:: GradeSystemQuerySession.gradebook

   .. automethod:: GradeSystemQuerySession.can_search_grade_systems

   .. automethod:: GradeSystemQuerySession.use_federated_gradebook_view

   .. automethod:: GradeSystemQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeSystemQuerySession.grade_system_query

   .. automethod:: GradeSystemQuerySession.get_grade_systems_by_query



Grade System Admin Methods
--------------------------

   .. autoattribute:: GradeSystemAdminSession.gradebook_id

   .. autoattribute:: GradeSystemAdminSession.gradebook

   .. automethod:: GradeSystemAdminSession.can_create_grade_systems

   .. automethod:: GradeSystemAdminSession.can_create_grade_system_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade_system

   .. automethod:: GradeSystemAdminSession.can_update_grade_systems

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade_system

   .. automethod:: GradeSystemAdminSession.can_delete_grade_systems

   .. automethod:: GradeSystemAdminSession.delete_grade_system

   .. automethod:: GradeSystemAdminSession.can_manage_grade_system_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade_system

   .. automethod:: GradeSystemAdminSession.can_create_grades

   .. automethod:: GradeSystemAdminSession.can_create_grade_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade

   .. automethod:: GradeSystemAdminSession.can_update_grades

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade

   .. automethod:: GradeSystemAdminSession.can_delete_grades

   .. automethod:: GradeSystemAdminSession.delete_grade

   .. automethod:: GradeSystemAdminSession.can_manage_grade_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: GradeEntryLookupSession.gradebook_id

   .. autoattribute:: GradeEntryLookupSession.gradebook

   .. automethod:: GradeEntryLookupSession.can_lookup_grade_entries

   .. automethod:: GradeEntryLookupSession.use_comparative_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_plenary_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_federated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_any_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.get_grade_entry

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_ids

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_parent_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_record_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_grader

   .. autoattribute:: GradeEntryLookupSession.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: GradeEntryQuerySession.gradebook_id

   .. autoattribute:: GradeEntryQuerySession.gradebook

   .. automethod:: GradeEntryQuerySession.can_search_grade_entries

   .. automethod:: GradeEntryQuerySession.use_federated_gradebook_view

   .. automethod:: GradeEntryQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeEntryQuerySession.grade_entry_query

   .. automethod:: GradeEntryQuerySession.get_grade_entries_by_query



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: GradeEntryAdminSession.gradebook_id

   .. autoattribute:: GradeEntryAdminSession.gradebook

   .. automethod:: GradeEntryAdminSession.can_create_grade_entries

   .. automethod:: GradeEntryAdminSession.can_create_grade_entry_with_record_types

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_create

   .. automethod:: GradeEntryAdminSession.create_grade_entry

   .. automethod:: GradeEntryAdminSession.can_overridecalculated_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_override

   .. automethod:: GradeEntryAdminSession.override_calculated_grade_entry

   .. automethod:: GradeEntryAdminSession.can_update_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_update

   .. automethod:: GradeEntryAdminSession.update_grade_entry

   .. automethod:: GradeEntryAdminSession.can_delete_grade_entries

   .. automethod:: GradeEntryAdminSession.delete_grade_entry

   .. automethod:: GradeEntryAdminSession.can_manage_grade_entry_aliases

   .. automethod:: GradeEntryAdminSession.alias_grade_entry



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradebookColumnLookupSession.gradebook_id

   .. autoattribute:: GradebookColumnLookupSession.gradebook

   .. automethod:: GradebookColumnLookupSession.can_lookup_gradebook_columns

   .. automethod:: GradebookColumnLookupSession.use_comparative_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_plenary_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_federated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.use_isolated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_ids

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_record_type

   .. autoattribute:: GradebookColumnLookupSession.gradebook_columns

   .. automethod:: GradebookColumnLookupSession.supports_summary

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradebookColumnQuerySession.gradebook_id

   .. autoattribute:: GradebookColumnQuerySession.gradebook

   .. automethod:: GradebookColumnQuerySession.can_search_gradebook_columns

   .. automethod:: GradebookColumnQuerySession.use_federated_gradebook_view

   .. automethod:: GradebookColumnQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradebookColumnQuerySession.gradebook_column_query

   .. automethod:: GradebookColumnQuerySession.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradebookColumnAdminSession.gradebook_id

   .. autoattribute:: GradebookColumnAdminSession.gradebook

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_column_with_record_types

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_create

   .. automethod:: GradebookColumnAdminSession.create_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_update_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_update

   .. automethod:: GradebookColumnAdminSession.update_gradebook_column

   .. automethod:: GradebookColumnAdminSession.sequence_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.move_gradebook_column

   .. automethod:: GradebookColumnAdminSession.copy_gradebook_column_entries

   .. automethod:: GradebookColumnAdminSession.can_delete_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.delete_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_manage_gradebook_column_aliases

   .. automethod:: GradebookColumnAdminSession.alias_gradebook_column



Gradebook Node List
-------------------

.. autoclass:: GradebookNodeList
   :show-inheritance:

   .. autoattribute:: GradebookNodeList.next_gradebook_node

   .. automethod:: GradebookNodeList.get_next_gradebook_nodes



Gradebook Lookup Methods
------------------------

   .. automethod:: GradebookLookupSession.can_lookup_gradebooks

   .. automethod:: GradebookLookupSession.use_comparative_gradebook_view

   .. automethod:: GradebookLookupSession.use_plenary_gradebook_view

   .. automethod:: GradebookLookupSession.get_gradebook

   .. automethod:: GradebookLookupSession.get_gradebooks_by_ids

   .. automethod:: GradebookLookupSession.get_gradebooks_by_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_parent_genus_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_record_type

   .. automethod:: GradebookLookupSession.get_gradebooks_by_provider

   .. autoattribute:: GradebookLookupSession.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradebookAdminSession.can_create_gradebooks

   .. automethod:: GradebookAdminSession.can_create_gradebook_with_record_types

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_create

   .. automethod:: GradebookAdminSession.create_gradebook

   .. automethod:: GradebookAdminSession.can_update_gradebooks

   .. automethod:: GradebookAdminSession.get_gradebook_form_for_update

   .. automethod:: GradebookAdminSession.update_gradebook

   .. automethod:: GradebookAdminSession.can_delete_gradebooks

   .. automethod:: GradebookAdminSession.delete_gradebook

   .. automethod:: GradebookAdminSession.can_manage_gradebook_aliases

   .. automethod:: GradebookAdminSession.alias_gradebook



Grade System Lookup Methods
---------------------------

   .. autoattribute:: GradeSystemLookupSession.gradebook_id

   .. autoattribute:: GradeSystemLookupSession.gradebook

   .. automethod:: GradeSystemLookupSession.can_lookup_grade_systems

   .. automethod:: GradeSystemLookupSession.use_comparative_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_plenary_grade_system_view

   .. automethod:: GradeSystemLookupSession.use_federated_gradebook_view

   .. automethod:: GradeSystemLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeSystemLookupSession.get_grade_system

   .. automethod:: GradeSystemLookupSession.get_grade_system_by_grade

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_ids

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_parent_genus_type

   .. automethod:: GradeSystemLookupSession.get_grade_systems_by_record_type

   .. autoattribute:: GradeSystemLookupSession.grade_systems



Grade System Query Methods
--------------------------

   .. autoattribute:: GradeSystemQuerySession.gradebook_id

   .. autoattribute:: GradeSystemQuerySession.gradebook

   .. automethod:: GradeSystemQuerySession.can_search_grade_systems

   .. automethod:: GradeSystemQuerySession.use_federated_gradebook_view

   .. automethod:: GradeSystemQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeSystemQuerySession.grade_system_query

   .. automethod:: GradeSystemQuerySession.get_grade_systems_by_query



Grade System Admin Methods
--------------------------

   .. autoattribute:: GradeSystemAdminSession.gradebook_id

   .. autoattribute:: GradeSystemAdminSession.gradebook

   .. automethod:: GradeSystemAdminSession.can_create_grade_systems

   .. automethod:: GradeSystemAdminSession.can_create_grade_system_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade_system

   .. automethod:: GradeSystemAdminSession.can_update_grade_systems

   .. automethod:: GradeSystemAdminSession.get_grade_system_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade_system

   .. automethod:: GradeSystemAdminSession.can_delete_grade_systems

   .. automethod:: GradeSystemAdminSession.delete_grade_system

   .. automethod:: GradeSystemAdminSession.can_manage_grade_system_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade_system

   .. automethod:: GradeSystemAdminSession.can_create_grades

   .. automethod:: GradeSystemAdminSession.can_create_grade_with_record_types

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_create

   .. automethod:: GradeSystemAdminSession.create_grade

   .. automethod:: GradeSystemAdminSession.can_update_grades

   .. automethod:: GradeSystemAdminSession.get_grade_form_for_update

   .. automethod:: GradeSystemAdminSession.update_grade

   .. automethod:: GradeSystemAdminSession.can_delete_grades

   .. automethod:: GradeSystemAdminSession.delete_grade

   .. automethod:: GradeSystemAdminSession.can_manage_grade_aliases

   .. automethod:: GradeSystemAdminSession.alias_grade



Grade Entry Lookup Methods
--------------------------

   .. autoattribute:: GradeEntryLookupSession.gradebook_id

   .. autoattribute:: GradeEntryLookupSession.gradebook

   .. automethod:: GradeEntryLookupSession.can_lookup_grade_entries

   .. automethod:: GradeEntryLookupSession.use_comparative_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_plenary_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_federated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_isolated_gradebook_view

   .. automethod:: GradeEntryLookupSession.use_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.use_any_effective_grade_entry_view

   .. automethod:: GradeEntryLookupSession.get_grade_entry

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_ids

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_parent_genus_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_record_type

   .. automethod:: GradeEntryLookupSession.get_grade_entries_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource

   .. automethod:: GradeEntryLookupSession.get_grade_entries_for_gradebook_column_and_resource_on_date

   .. automethod:: GradeEntryLookupSession.get_grade_entries_by_grader

   .. autoattribute:: GradeEntryLookupSession.grade_entries



Grade Entry Query Methods
-------------------------

   .. autoattribute:: GradeEntryQuerySession.gradebook_id

   .. autoattribute:: GradeEntryQuerySession.gradebook

   .. automethod:: GradeEntryQuerySession.can_search_grade_entries

   .. automethod:: GradeEntryQuerySession.use_federated_gradebook_view

   .. automethod:: GradeEntryQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradeEntryQuerySession.grade_entry_query

   .. automethod:: GradeEntryQuerySession.get_grade_entries_by_query



Grade Entry Admin Methods
-------------------------

   .. autoattribute:: GradeEntryAdminSession.gradebook_id

   .. autoattribute:: GradeEntryAdminSession.gradebook

   .. automethod:: GradeEntryAdminSession.can_create_grade_entries

   .. automethod:: GradeEntryAdminSession.can_create_grade_entry_with_record_types

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_create

   .. automethod:: GradeEntryAdminSession.create_grade_entry

   .. automethod:: GradeEntryAdminSession.can_overridecalculated_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_override

   .. automethod:: GradeEntryAdminSession.override_calculated_grade_entry

   .. automethod:: GradeEntryAdminSession.can_update_grade_entries

   .. automethod:: GradeEntryAdminSession.get_grade_entry_form_for_update

   .. automethod:: GradeEntryAdminSession.update_grade_entry

   .. automethod:: GradeEntryAdminSession.can_delete_grade_entries

   .. automethod:: GradeEntryAdminSession.delete_grade_entry

   .. automethod:: GradeEntryAdminSession.can_manage_grade_entry_aliases

   .. automethod:: GradeEntryAdminSession.alias_grade_entry



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradebookColumnLookupSession.gradebook_id

   .. autoattribute:: GradebookColumnLookupSession.gradebook

   .. automethod:: GradebookColumnLookupSession.can_lookup_gradebook_columns

   .. automethod:: GradebookColumnLookupSession.use_comparative_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_plenary_gradebook_column_view

   .. automethod:: GradebookColumnLookupSession.use_federated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.use_isolated_gradebook_view

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_ids

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradebookColumnLookupSession.get_gradebook_columns_by_record_type

   .. autoattribute:: GradebookColumnLookupSession.gradebook_columns

   .. automethod:: GradebookColumnLookupSession.supports_summary

   .. automethod:: GradebookColumnLookupSession.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradebookColumnQuerySession.gradebook_id

   .. autoattribute:: GradebookColumnQuerySession.gradebook

   .. automethod:: GradebookColumnQuerySession.can_search_gradebook_columns

   .. automethod:: GradebookColumnQuerySession.use_federated_gradebook_view

   .. automethod:: GradebookColumnQuerySession.use_isolated_gradebook_view

   .. autoattribute:: GradebookColumnQuerySession.gradebook_column_query

   .. automethod:: GradebookColumnQuerySession.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradebookColumnAdminSession.gradebook_id

   .. autoattribute:: GradebookColumnAdminSession.gradebook

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.can_create_gradebook_column_with_record_types

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_create

   .. automethod:: GradebookColumnAdminSession.create_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_update_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.get_gradebook_column_form_for_update

   .. automethod:: GradebookColumnAdminSession.update_gradebook_column

   .. automethod:: GradebookColumnAdminSession.sequence_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.move_gradebook_column

   .. automethod:: GradebookColumnAdminSession.copy_gradebook_column_entries

   .. automethod:: GradebookColumnAdminSession.can_delete_gradebook_columns

   .. automethod:: GradebookColumnAdminSession.delete_gradebook_column

   .. automethod:: GradebookColumnAdminSession.can_manage_gradebook_column_aliases

   .. automethod:: GradebookColumnAdminSession.alias_gradebook_column



