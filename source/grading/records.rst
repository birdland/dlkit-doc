
.. currentmodule:: dlkit.grading.records
.. automodule:: dlkit.grading.records

Records
=======


Grade Record
------------

.. autoclass:: GradeRecord
   :show-inheritance:





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



Grade Query Record
------------------

.. autoclass:: GradeQueryRecord
   :show-inheritance:





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



Grade Form Record
-----------------

.. autoclass:: GradeFormRecord
   :show-inheritance:





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



Grade System Record
-------------------

.. autoclass:: GradeSystemRecord
   :show-inheritance:





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



Grade System Query Record
-------------------------

.. autoclass:: GradeSystemQueryRecord
   :show-inheritance:





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



Grade System Form Record
------------------------

.. autoclass:: GradeSystemFormRecord
   :show-inheritance:





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



Grade System Search Record
--------------------------

.. autoclass:: GradeSystemSearchRecord
   :show-inheritance:





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



Grade Entry Record
------------------

.. autoclass:: GradeEntryRecord
   :show-inheritance:





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



Grade Entry Query Record
------------------------

.. autoclass:: GradeEntryQueryRecord
   :show-inheritance:





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



Grade Entry Form Record
-----------------------

.. autoclass:: GradeEntryFormRecord
   :show-inheritance:





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



Grade Entry Search Record
-------------------------

.. autoclass:: GradeEntrySearchRecord
   :show-inheritance:





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



Gradebook Column Record
-----------------------

.. autoclass:: GradebookColumnRecord
   :show-inheritance:





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



Gradebook Column Query Record
-----------------------------

.. autoclass:: GradebookColumnQueryRecord
   :show-inheritance:





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



Gradebook Column Form Record
----------------------------

.. autoclass:: GradebookColumnFormRecord
   :show-inheritance:





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



Gradebook Column Search Record
------------------------------

.. autoclass:: GradebookColumnSearchRecord
   :show-inheritance:





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



Gradebook Column Summary Record
-------------------------------

.. autoclass:: GradebookColumnSummaryRecord
   :show-inheritance:





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



Gradebook Column Summary Query Record
-------------------------------------

.. autoclass:: GradebookColumnSummaryQueryRecord
   :show-inheritance:





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



Gradebook Record
----------------

.. autoclass:: GradebookRecord
   :show-inheritance:





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



Gradebook Query Record
----------------------

.. autoclass:: GradebookQueryRecord
   :show-inheritance:





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



Gradebook Form Record
---------------------

.. autoclass:: GradebookFormRecord
   :show-inheritance:





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



Gradebook Search Record
-----------------------

.. autoclass:: GradebookSearchRecord
   :show-inheritance:





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



