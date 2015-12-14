
.. currentmodule:: dlkit.services.grading
.. automodule:: dlkit.services.grading

Service Managers
================


Grading Manager
---------------

.. autoclass:: GradingManager
   :show-inheritance:

   .. autoattribute:: GradingManager.grade_system_lookup_session

   .. automethod:: GradingManager.get_grade_system_lookup_session_for_gradebook

   .. autoattribute:: GradingManager.grade_system_query_session

   .. automethod:: GradingManager.get_grade_system_query_session_for_gradebook

   .. autoattribute:: GradingManager.grade_system_search_session

   .. automethod:: GradingManager.get_grade_system_search_session_for_gradebook

   .. autoattribute:: GradingManager.grade_system_admin_session

   .. automethod:: GradingManager.get_grade_system_admin_session_for_gradebook

   .. automethod:: GradingManager.get_grade_system_notification_session

   .. automethod:: GradingManager.get_grade_system_notification_session_for_gradebook

   .. autoattribute:: GradingManager.grade_system_gradebook_session

   .. autoattribute:: GradingManager.grade_system_gradebook_assignment_session

   .. automethod:: GradingManager.get_grade_system_smart_gradebook_session

   .. autoattribute:: GradingManager.grade_entry_lookup_session

   .. automethod:: GradingManager.get_grade_entry_lookup_session_for_gradebook

   .. autoattribute:: GradingManager.grade_entry_query_session

   .. automethod:: GradingManager.get_grade_entry_query_session_for_gradebook

   .. autoattribute:: GradingManager.grade_entry_search_session

   .. automethod:: GradingManager.get_grade_entry_search_session_for_gradebook

   .. autoattribute:: GradingManager.grade_entry_admin_session

   .. automethod:: GradingManager.get_grade_entry_admin_session_for_gradebook

   .. automethod:: GradingManager.get_grade_entry_notification_session

   .. automethod:: GradingManager.get_grade_entry_notification_session_for_gradebook

   .. autoattribute:: GradingManager.gradebook_column_lookup_session

   .. automethod:: GradingManager.get_gradebook_column_lookup_session_for_gradebook

   .. autoattribute:: GradingManager.gradebook_column_query_session

   .. automethod:: GradingManager.get_gradebook_column_query_session_for_gradebook

   .. autoattribute:: GradingManager.gradebook_column_search_session

   .. automethod:: GradingManager.get_gradebook_column_search_session_for_gradebook

   .. autoattribute:: GradingManager.gradebook_column_admin_session

   .. automethod:: GradingManager.get_gradebook_column_admin_session_for_gradebook

   .. automethod:: GradingManager.get_gradebook_column_notification_session

   .. automethod:: GradingManager.get_gradebook_column_notification_session_for_gradebook

   .. autoattribute:: GradingManager.gradebook_column_gradebook_session

   .. autoattribute:: GradingManager.gradebook_column_gradebook_assignment_session

   .. automethod:: GradingManager.get_gradebook_column_smart_gradebook_session

   .. autoattribute:: GradingManager.gradebook_lookup_session

   .. autoattribute:: GradingManager.gradebook_query_session

   .. autoattribute:: GradingManager.gradebook_search_session

   .. autoattribute:: GradingManager.gradebook_admin_session

   .. automethod:: GradingManager.get_gradebook_notification_session

   .. autoattribute:: GradingManager.gradebook_hierarchy_session

   .. autoattribute:: GradingManager.gradebook_hierarchy_design_session

   .. autoattribute:: GradingManager.grading_batch_manager

   .. autoattribute:: GradingManager.grading_calculation_manager

   .. autoattribute:: GradingManager.grading_transform_manager



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



Grading Proxy Manager
---------------------

.. autoclass:: GradingProxyManager
   :show-inheritance:

   .. automethod:: GradingProxyManager.get_grade_system_lookup_session

   .. automethod:: GradingProxyManager.get_grade_system_lookup_session_for_gradebook

   .. automethod:: GradingProxyManager.get_grade_system_query_session

   .. automethod:: GradingProxyManager.get_grade_system_query_session_for_gradebook

   .. automethod:: GradingProxyManager.get_grade_system_search_session

   .. automethod:: GradingProxyManager.get_grade_system_search_session_for_gradebook

   .. automethod:: GradingProxyManager.get_grade_system_admin_session

   .. automethod:: GradingProxyManager.get_grade_system_admin_session_for_gradebook

   .. automethod:: GradingProxyManager.get_grade_system_notification_session

   .. automethod:: GradingProxyManager.get_grade_system_notification_session_for_gradebook

   .. automethod:: GradingProxyManager.get_grade_system_gradebook_session

   .. automethod:: GradingProxyManager.get_grade_system_gradebook_assignment_session

   .. automethod:: GradingProxyManager.get_grade_system_smart_gradebook_session

   .. automethod:: GradingProxyManager.get_grade_entry_lookup_session

   .. automethod:: GradingProxyManager.get_grade_entry_lookup_session_for_gradebook

   .. automethod:: GradingProxyManager.get_grade_entry_query_session

   .. automethod:: GradingProxyManager.get_grade_entry_query_session_for_gradebook

   .. automethod:: GradingProxyManager.get_grade_entry_search_session

   .. automethod:: GradingProxyManager.get_grade_entry_search_session_for_gradebook

   .. automethod:: GradingProxyManager.get_grade_entry_admin_session

   .. automethod:: GradingProxyManager.get_grade_entry_admin_session_for_gradebook

   .. automethod:: GradingProxyManager.get_grade_entry_notification_session

   .. automethod:: GradingProxyManager.get_grade_entry_notification_session_for_gradebook

   .. automethod:: GradingProxyManager.get_gradebook_column_lookup_session

   .. automethod:: GradingProxyManager.get_gradebook_column_lookup_session_for_gradebook

   .. automethod:: GradingProxyManager.get_gradebook_column_query_session

   .. automethod:: GradingProxyManager.get_gradebook_column_query_session_for_gradebook

   .. automethod:: GradingProxyManager.get_gradebook_column_search_session

   .. automethod:: GradingProxyManager.get_gradebook_column_search_session_for_gradebook

   .. automethod:: GradingProxyManager.get_gradebook_column_admin_session

   .. automethod:: GradingProxyManager.get_gradebook_column_admin_session_for_gradebook

   .. automethod:: GradingProxyManager.get_gradebook_column_notification_session

   .. automethod:: GradingProxyManager.get_gradebook_column_notification_session_for_gradebook

   .. automethod:: GradingProxyManager.get_gradebook_column_gradebook_session

   .. automethod:: GradingProxyManager.get_gradebook_column_gradebook_assignment_session

   .. automethod:: GradingProxyManager.get_gradebook_column_smart_gradebook_session

   .. automethod:: GradingProxyManager.get_gradebook_lookup_session

   .. automethod:: GradingProxyManager.get_gradebook_query_session

   .. automethod:: GradingProxyManager.get_gradebook_search_session

   .. automethod:: GradingProxyManager.get_gradebook_admin_session

   .. automethod:: GradingProxyManager.get_gradebook_notification_session

   .. automethod:: GradingProxyManager.get_gradebook_hierarchy_session

   .. automethod:: GradingProxyManager.get_gradebook_hierarchy_design_session

   .. autoattribute:: GradingProxyManager.grading_batch_proxy_manager

   .. autoattribute:: GradingProxyManager.grading_calculation_proxy_manager

   .. autoattribute:: GradingProxyManager.grading_transform_proxy_manager



Gradebook Lookup Methods
------------------------

   .. automethod:: GradingProxyManager.can_lookup_gradebooks

   .. automethod:: GradingProxyManager.use_comparative_gradebook_view

   .. automethod:: GradingProxyManager.use_plenary_gradebook_view

   .. automethod:: GradingProxyManager.get_gradebook

   .. automethod:: GradingProxyManager.get_gradebooks_by_ids

   .. automethod:: GradingProxyManager.get_gradebooks_by_genus_type

   .. automethod:: GradingProxyManager.get_gradebooks_by_parent_genus_type

   .. automethod:: GradingProxyManager.get_gradebooks_by_record_type

   .. automethod:: GradingProxyManager.get_gradebooks_by_provider

   .. autoattribute:: GradingProxyManager.gradebooks



Gradebook Admin Methods
-----------------------

   .. automethod:: GradingProxyManager.can_create_gradebooks

   .. automethod:: GradingProxyManager.can_create_gradebook_with_record_types

   .. automethod:: GradingProxyManager.get_gradebook_form_for_create

   .. automethod:: GradingProxyManager.create_gradebook

   .. automethod:: GradingProxyManager.can_update_gradebooks

   .. automethod:: GradingProxyManager.get_gradebook_form_for_update

   .. automethod:: GradingProxyManager.update_gradebook

   .. automethod:: GradingProxyManager.can_delete_gradebooks

   .. automethod:: GradingProxyManager.delete_gradebook

   .. automethod:: GradingProxyManager.can_manage_gradebook_aliases

   .. automethod:: GradingProxyManager.alias_gradebook



