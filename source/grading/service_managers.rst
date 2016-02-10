
.. currentmodule:: dlkit.services.grading
.. automodule:: dlkit.services.grading

Service Managers
================


Grading Profile
---------------

.. autoclass:: GradingProfile
   :show-inheritance:

   .. automethod:: GradingProfile.supports_grade_system_lookup

   .. automethod:: GradingProfile.supports_grade_system_query

   .. automethod:: GradingProfile.supports_grade_system_admin

   .. automethod:: GradingProfile.supports_grade_entry_lookup

   .. automethod:: GradingProfile.supports_grade_entry_query

   .. automethod:: GradingProfile.supports_grade_entry_admin

   .. automethod:: GradingProfile.supports_gradebook_column_lookup

   .. automethod:: GradingProfile.supports_gradebook_column_query

   .. automethod:: GradingProfile.supports_gradebook_column_admin

   .. automethod:: GradingProfile.supports_gradebook_lookup

   .. automethod:: GradingProfile.supports_gradebook_admin

   .. autoattribute:: GradingProfile.grade_record_types

   .. autoattribute:: GradingProfile.grade_system_record_types

   .. autoattribute:: GradingProfile.grade_system_search_record_types

   .. autoattribute:: GradingProfile.grade_entry_record_types

   .. autoattribute:: GradingProfile.grade_entry_search_record_types

   .. autoattribute:: GradingProfile.gradebook_column_record_types

   .. autoattribute:: GradingProfile.gradebook_column_search_record_types

   .. autoattribute:: GradingProfile.gradebook_column_summary_record_types

   .. autoattribute:: GradingProfile.gradebook_record_types

   .. autoattribute:: GradingProfile.gradebook_search_record_types

Grading Manager
---------------

.. autoclass:: GradingManager
   :show-inheritance:

   .. autoattribute:: GradingManager.grading_batch_manager

   .. autoattribute:: GradingManager.grading_calculation_manager

   .. autoattribute:: GradingManager.grading_transform_manager



Gradebook Column Lookup Methods
-------------------------------

   .. autoattribute:: GradingManager.gradebook_id

   .. autoattribute:: GradingManager.gradebook

   .. automethod:: GradingManager.can_lookup_gradebook_columns

   .. automethod:: GradingManager.use_comparative_gradebook_column_view

   .. automethod:: GradingManager.use_plenary_gradebook_column_view

   .. automethod:: GradingManager.use_federated_gradebook_view

   .. automethod:: GradingManager.use_isolated_gradebook_view

   .. automethod:: GradingManager.get_gradebook_column

   .. automethod:: GradingManager.get_gradebook_columns_by_ids

   .. automethod:: GradingManager.get_gradebook_columns_by_genus_type

   .. automethod:: GradingManager.get_gradebook_columns_by_parent_genus_type

   .. automethod:: GradingManager.get_gradebook_columns_by_record_type

   .. autoattribute:: GradingManager.gradebook_columns

   .. automethod:: GradingManager.supports_summary

   .. automethod:: GradingManager.get_gradebook_column_summary



Gradebook Column Query Methods
------------------------------

   .. autoattribute:: GradingManager.gradebook_id

   .. autoattribute:: GradingManager.gradebook

   .. automethod:: GradingManager.can_search_gradebook_columns

   .. automethod:: GradingManager.use_federated_gradebook_view

   .. automethod:: GradingManager.use_isolated_gradebook_view

   .. autoattribute:: GradingManager.gradebook_column_query

   .. automethod:: GradingManager.get_gradebook_columns_by_query



Gradebook Column Admin Methods
------------------------------

   .. autoattribute:: GradingManager.gradebook_id

   .. autoattribute:: GradingManager.gradebook

   .. automethod:: GradingManager.can_create_gradebook_columns

   .. automethod:: GradingManager.can_create_gradebook_column_with_record_types

   .. automethod:: GradingManager.get_gradebook_column_form_for_create

   .. automethod:: GradingManager.create_gradebook_column

   .. automethod:: GradingManager.can_update_gradebook_columns

   .. automethod:: GradingManager.get_gradebook_column_form_for_update

   .. automethod:: GradingManager.update_gradebook_column

   .. automethod:: GradingManager.sequence_gradebook_columns

   .. automethod:: GradingManager.move_gradebook_column

   .. automethod:: GradingManager.copy_gradebook_column_entries

   .. automethod:: GradingManager.can_delete_gradebook_columns

   .. automethod:: GradingManager.delete_gradebook_column

   .. automethod:: GradingManager.can_manage_gradebook_column_aliases

   .. automethod:: GradingManager.alias_gradebook_column



Gradebook Lookup Methods
------------------------

   .. automethod:: GradingManager.can_lookup_gradebooks

   .. automethod:: GradingManager.use_comparative_gradebook_view

   .. automethod:: GradingManager.use_plenary_gradebook_view

   .. automethod:: GradingManager.get_gradebook

   .. automethod:: GradingManager.get_gradebooks_by_ids

   .. automethod:: GradingManager.get_gradebooks_by_genus_type

   .. automethod:: GradingManager.get_gradebooks_by_parent_genus_type

   .. automethod:: GradingManager.get_gradebooks_by_record_type

   .. automethod:: GradingManager.get_gradebooks_by_provider

   .. autoattribute:: GradingManager.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradingManager.can_create_gradebooks

   .. automethod:: GradingManager.can_create_gradebook_with_record_types

   .. automethod:: GradingManager.get_gradebook_form_for_create

   .. automethod:: GradingManager.create_gradebook

   .. automethod:: GradingManager.can_update_gradebooks

   .. automethod:: GradingManager.get_gradebook_form_for_update

   .. automethod:: GradingManager.update_gradebook

   .. automethod:: GradingManager.can_delete_gradebooks

   .. automethod:: GradingManager.delete_gradebook

   .. automethod:: GradingManager.can_manage_gradebook_aliases

   .. automethod:: GradingManager.alias_gradebook



