
.. currentmodule:: dlkit.grading.queries
.. automodule:: dlkit.grading.queries

Queries
=======


Grade Query
-----------

.. autoclass:: GradeQuery
   :show-inheritance:

   .. automethod:: GradeQuery.match_grade_system_id

   .. autoattribute:: GradeQuery.grade_system_id_terms

   .. automethod:: GradeQuery.supports_grade_system_query

   .. autoattribute:: GradeQuery.grade_system_query

   .. autoattribute:: GradeQuery.grade_system_terms

   .. automethod:: GradeQuery.match_input_score_start_range

   .. autoattribute:: GradeQuery.input_score_start_range_terms

   .. automethod:: GradeQuery.match_input_score_end_range

   .. autoattribute:: GradeQuery.input_score_end_range_terms

   .. automethod:: GradeQuery.match_input_score

   .. autoattribute:: GradeQuery.input_score_terms

   .. automethod:: GradeQuery.match_output_score

   .. autoattribute:: GradeQuery.output_score_terms

   .. automethod:: GradeQuery.match_grade_entry_id

   .. autoattribute:: GradeQuery.grade_entry_id_terms

   .. automethod:: GradeQuery.supports_grade_entry_query

   .. autoattribute:: GradeQuery.grade_entry_query

   .. automethod:: GradeQuery.match_any_grade_entry

   .. autoattribute:: GradeQuery.grade_entry_terms

   .. automethod:: GradeQuery.match_gradebook_id

   .. autoattribute:: GradeQuery.gradebook_id_terms

   .. automethod:: GradeQuery.supports_gradebook_query

   .. autoattribute:: GradeQuery.gradebook_query

   .. autoattribute:: GradeQuery.gradebook_terms

   .. automethod:: GradeQuery.get_grade_query_record



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



Grade System Query
------------------

.. autoclass:: GradeSystemQuery
   :show-inheritance:

   .. automethod:: GradeSystemQuery.match_based_on_grades

   .. autoattribute:: GradeSystemQuery.based_on_grades_terms

   .. automethod:: GradeSystemQuery.match_grade_id

   .. autoattribute:: GradeSystemQuery.grade_id_terms

   .. automethod:: GradeSystemQuery.supports_grade_query

   .. autoattribute:: GradeSystemQuery.grade_query

   .. automethod:: GradeSystemQuery.match_any_grade

   .. autoattribute:: GradeSystemQuery.grade_terms

   .. automethod:: GradeSystemQuery.match_lowest_numeric_score

   .. autoattribute:: GradeSystemQuery.lowest_numeric_score_terms

   .. automethod:: GradeSystemQuery.match_numeric_score_increment

   .. autoattribute:: GradeSystemQuery.numeric_score_increment_terms

   .. automethod:: GradeSystemQuery.match_highest_numeric_score

   .. autoattribute:: GradeSystemQuery.highest_numeric_score_terms

   .. automethod:: GradeSystemQuery.match_gradebook_column_id

   .. autoattribute:: GradeSystemQuery.gradebook_column_id_terms

   .. automethod:: GradeSystemQuery.supports_gradebook_column_query

   .. autoattribute:: GradeSystemQuery.gradebook_column_query

   .. automethod:: GradeSystemQuery.match_any_gradebook_column

   .. autoattribute:: GradeSystemQuery.gradebook_column_terms

   .. automethod:: GradeSystemQuery.match_gradebook_id

   .. autoattribute:: GradeSystemQuery.gradebook_id_terms

   .. automethod:: GradeSystemQuery.supports_gradebook_query

   .. autoattribute:: GradeSystemQuery.gradebook_query

   .. autoattribute:: GradeSystemQuery.gradebook_terms

   .. automethod:: GradeSystemQuery.get_grade_system_query_record



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



Grade Entry Query
-----------------

.. autoclass:: GradeEntryQuery
   :show-inheritance:

   .. automethod:: GradeEntryQuery.match_gradebook_column_id

   .. autoattribute:: GradeEntryQuery.gradebook_column_id_terms

   .. automethod:: GradeEntryQuery.supports_gradebook_column_query

   .. autoattribute:: GradeEntryQuery.gradebook_column_query

   .. autoattribute:: GradeEntryQuery.gradebook_column_terms

   .. automethod:: GradeEntryQuery.match_key_resource_id

   .. autoattribute:: GradeEntryQuery.key_resource_id_terms

   .. automethod:: GradeEntryQuery.supports_key_resource_query

   .. autoattribute:: GradeEntryQuery.key_resource_query

   .. automethod:: GradeEntryQuery.match_any_key_resource

   .. autoattribute:: GradeEntryQuery.key_resource_terms

   .. automethod:: GradeEntryQuery.match_derived

   .. autoattribute:: GradeEntryQuery.derived_terms

   .. automethod:: GradeEntryQuery.match_overridden_grade_entry_id

   .. autoattribute:: GradeEntryQuery.overridden_grade_entry_id_terms

   .. automethod:: GradeEntryQuery.supports_overridden_grade_entry_query

   .. autoattribute:: GradeEntryQuery.overridden_grade_entry_query

   .. automethod:: GradeEntryQuery.match_any_overridden_grade_entry

   .. autoattribute:: GradeEntryQuery.overridden_grade_entry_terms

   .. automethod:: GradeEntryQuery.match_ignored_for_calculations

   .. autoattribute:: GradeEntryQuery.ignored_for_calculations_terms

   .. automethod:: GradeEntryQuery.match_grade_id

   .. autoattribute:: GradeEntryQuery.grade_id_terms

   .. automethod:: GradeEntryQuery.supports_grade_query

   .. autoattribute:: GradeEntryQuery.grade_query

   .. automethod:: GradeEntryQuery.match_any_grade

   .. autoattribute:: GradeEntryQuery.grade_terms

   .. automethod:: GradeEntryQuery.match_score

   .. automethod:: GradeEntryQuery.match_any_score

   .. autoattribute:: GradeEntryQuery.score_terms

   .. automethod:: GradeEntryQuery.match_time_graded

   .. autoattribute:: GradeEntryQuery.time_graded_terms

   .. automethod:: GradeEntryQuery.match_grader_id

   .. autoattribute:: GradeEntryQuery.grader_id_terms

   .. automethod:: GradeEntryQuery.supports_grader_query

   .. autoattribute:: GradeEntryQuery.grader_query

   .. automethod:: GradeEntryQuery.match_any_grader

   .. autoattribute:: GradeEntryQuery.grader_terms

   .. automethod:: GradeEntryQuery.match_grading_agent_id

   .. autoattribute:: GradeEntryQuery.grading_agent_id_terms

   .. automethod:: GradeEntryQuery.supports_grading_agent_query

   .. autoattribute:: GradeEntryQuery.grading_agent_query

   .. automethod:: GradeEntryQuery.match_any_grading_agent

   .. autoattribute:: GradeEntryQuery.grading_agent_terms

   .. automethod:: GradeEntryQuery.match_gradebook_id

   .. autoattribute:: GradeEntryQuery.gradebook_id_terms

   .. automethod:: GradeEntryQuery.supports_gradebook_query

   .. autoattribute:: GradeEntryQuery.gradebook_query

   .. autoattribute:: GradeEntryQuery.gradebook_terms

   .. automethod:: GradeEntryQuery.get_grade_entry_query_record



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



Gradebook Column Query
----------------------

.. autoclass:: GradebookColumnQuery
   :show-inheritance:

   .. automethod:: GradebookColumnQuery.match_grade_system_id

   .. autoattribute:: GradebookColumnQuery.grade_system_id_terms

   .. automethod:: GradebookColumnQuery.supports_grade_system_query

   .. autoattribute:: GradebookColumnQuery.grade_system_query

   .. automethod:: GradebookColumnQuery.match_any_grade_system

   .. autoattribute:: GradebookColumnQuery.grade_system_terms

   .. automethod:: GradebookColumnQuery.match_grade_entry_id

   .. autoattribute:: GradebookColumnQuery.grade_entry_id_terms

   .. automethod:: GradebookColumnQuery.supports_grade_entry_query

   .. autoattribute:: GradebookColumnQuery.grade_entry_query

   .. automethod:: GradebookColumnQuery.match_any_grade_entry

   .. autoattribute:: GradebookColumnQuery.grade_entry_terms

   .. automethod:: GradebookColumnQuery.supports_gradebook_column_summary_query

   .. autoattribute:: GradebookColumnQuery.gradebook_column_summary_query

   .. autoattribute:: GradebookColumnQuery.gradebook_column_summary_terms

   .. automethod:: GradebookColumnQuery.match_gradebook_id

   .. autoattribute:: GradebookColumnQuery.gradebook_id_terms

   .. automethod:: GradebookColumnQuery.supports_gradebook_query

   .. autoattribute:: GradebookColumnQuery.gradebook_query

   .. autoattribute:: GradebookColumnQuery.gradebook_terms

   .. automethod:: GradebookColumnQuery.get_gradebook_column_query_record



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



Gradebook Column Summary Query
------------------------------

.. autoclass:: GradebookColumnSummaryQuery
   :show-inheritance:

   .. automethod:: GradebookColumnSummaryQuery.match_gradebook_column_id

   .. autoattribute:: GradebookColumnSummaryQuery.gradebook_column_id_terms

   .. automethod:: GradebookColumnSummaryQuery.supports_gradebook_column_query

   .. autoattribute:: GradebookColumnSummaryQuery.gradebook_column_query

   .. automethod:: GradebookColumnSummaryQuery.match_any_gradebook_column

   .. autoattribute:: GradebookColumnSummaryQuery.gradebook_column_terms

   .. automethod:: GradebookColumnSummaryQuery.match_mean

   .. autoattribute:: GradebookColumnSummaryQuery.mean_terms

   .. automethod:: GradebookColumnSummaryQuery.match_minimum_mean

   .. autoattribute:: GradebookColumnSummaryQuery.minimum_mean_terms

   .. automethod:: GradebookColumnSummaryQuery.match_median

   .. autoattribute:: GradebookColumnSummaryQuery.median_terms

   .. automethod:: GradebookColumnSummaryQuery.match_minimum_median

   .. autoattribute:: GradebookColumnSummaryQuery.minimum_median_terms

   .. automethod:: GradebookColumnSummaryQuery.match_mode

   .. autoattribute:: GradebookColumnSummaryQuery.mode_terms

   .. automethod:: GradebookColumnSummaryQuery.match_minimum_mode

   .. autoattribute:: GradebookColumnSummaryQuery.minimum_mode_terms

   .. automethod:: GradebookColumnSummaryQuery.match_rms

   .. autoattribute:: GradebookColumnSummaryQuery.rms_terms

   .. automethod:: GradebookColumnSummaryQuery.match_minimum_rms

   .. autoattribute:: GradebookColumnSummaryQuery.minimum_rms_terms

   .. automethod:: GradebookColumnSummaryQuery.match_standard_deviation

   .. autoattribute:: GradebookColumnSummaryQuery.standard_deviation_terms

   .. automethod:: GradebookColumnSummaryQuery.match_minimum_standard_deviation

   .. autoattribute:: GradebookColumnSummaryQuery.minimum_standard_deviation_terms

   .. automethod:: GradebookColumnSummaryQuery.match_sum

   .. autoattribute:: GradebookColumnSummaryQuery.sum_terms

   .. automethod:: GradebookColumnSummaryQuery.match_minimum_sum

   .. autoattribute:: GradebookColumnSummaryQuery.minimum_sum_terms

   .. automethod:: GradebookColumnSummaryQuery.match_gradebook_id

   .. autoattribute:: GradebookColumnSummaryQuery.gradebook_id_terms

   .. automethod:: GradebookColumnSummaryQuery.supports_gradebook_query

   .. autoattribute:: GradebookColumnSummaryQuery.gradebook_query

   .. autoattribute:: GradebookColumnSummaryQuery.gradebook_terms

   .. automethod:: GradebookColumnSummaryQuery.get_gradebook_column_summary_query_record



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



Gradebook Query
---------------

.. autoclass:: GradebookQuery
   :show-inheritance:

   .. automethod:: GradebookQuery.match_grade_system_id

   .. autoattribute:: GradebookQuery.grade_system_id_terms

   .. automethod:: GradebookQuery.supports_grade_system_query

   .. autoattribute:: GradebookQuery.grade_system_query

   .. automethod:: GradebookQuery.match_any_grade_system

   .. autoattribute:: GradebookQuery.grade_system_terms

   .. automethod:: GradebookQuery.match_grade_entry_id

   .. autoattribute:: GradebookQuery.grade_entry_id_terms

   .. automethod:: GradebookQuery.supports_grade_entry_query

   .. autoattribute:: GradebookQuery.grade_entry_query

   .. automethod:: GradebookQuery.match_any_grade_entry

   .. autoattribute:: GradebookQuery.grade_entry_terms

   .. automethod:: GradebookQuery.match_gradebook_column_id

   .. autoattribute:: GradebookQuery.gradebook_column_id_terms

   .. automethod:: GradebookQuery.supports_gradebook_column_query

   .. autoattribute:: GradebookQuery.gradebook_column_query

   .. automethod:: GradebookQuery.match_any_gradebook_column

   .. autoattribute:: GradebookQuery.gradebook_column_terms

   .. automethod:: GradebookQuery.match_ancestor_gradebook_id

   .. autoattribute:: GradebookQuery.ancestor_gradebook_id_terms

   .. automethod:: GradebookQuery.supports_ancestor_gradebook_query

   .. autoattribute:: GradebookQuery.ancestor_gradebook_query

   .. automethod:: GradebookQuery.match_any_ancestor_gradebook

   .. autoattribute:: GradebookQuery.ancestor_gradebook_terms

   .. automethod:: GradebookQuery.match_descendant_gradebook_id

   .. autoattribute:: GradebookQuery.descendant_gradebook_id_terms

   .. automethod:: GradebookQuery.supports_descendant_gradebook_query

   .. autoattribute:: GradebookQuery.descendant_gradebook_query

   .. automethod:: GradebookQuery.match_any_descendant_gradebook

   .. autoattribute:: GradebookQuery.descendant_gradebook_terms

   .. automethod:: GradebookQuery.get_gradebook_query_record



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



