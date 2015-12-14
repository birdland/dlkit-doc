
.. currentmodule:: dlkit.grading.managers
.. automodule:: dlkit.grading.managers

Managers
========


Grading Profile
---------------

.. autoclass:: GradingProfile
   :show-inheritance:

   .. automethod:: GradingProfile.supports_visible_federation

   .. automethod:: GradingProfile.supports_grade_system_lookup

   .. automethod:: GradingProfile.supports_grade_system_query

   .. automethod:: GradingProfile.supports_grade_system_search

   .. automethod:: GradingProfile.supports_grade_system_admin

   .. automethod:: GradingProfile.supports_grade_system_notification

   .. automethod:: GradingProfile.supports_grade_system_gradebook

   .. automethod:: GradingProfile.supports_grade_system_gradebook_assignment

   .. automethod:: GradingProfile.supports_grade_system_smart_gradebook

   .. automethod:: GradingProfile.supports_grade_entry_lookup

   .. automethod:: GradingProfile.supports_grade_entry_query

   .. automethod:: GradingProfile.supports_grade_entry_search

   .. automethod:: GradingProfile.supports_grade_entry_admin

   .. automethod:: GradingProfile.supports_grade_entry_notification

   .. automethod:: GradingProfile.supports_gradebook_column_lookup

   .. automethod:: GradingProfile.supports_gradebook_column_query

   .. automethod:: GradingProfile.supports_gradebook_column_search

   .. automethod:: GradingProfile.supports_gradebook_column_admin

   .. automethod:: GradingProfile.supports_gradebook_column_notification

   .. automethod:: GradingProfile.supports_gradebook_column_gradebook

   .. automethod:: GradingProfile.supports_gradebook_column_gradebook_assignment

   .. automethod:: GradingProfile.supports_gradebook_column_smart_gradebook

   .. automethod:: GradingProfile.supports_gradebook_lookup

   .. automethod:: GradingProfile.supports_gradebook_query

   .. automethod:: GradingProfile.supports_gradebook_search

   .. automethod:: GradingProfile.supports_gradebook_admin

   .. automethod:: GradingProfile.supports_gradebook_notification

   .. automethod:: GradingProfile.supports_gradebook_hierarchy

   .. automethod:: GradingProfile.supports_gradebook_hierarchy_design

   .. automethod:: GradingProfile.supports_grading_batch

   .. automethod:: GradingProfile.supports_grading_calculation

   .. automethod:: GradingProfile.supports_grading_transform

   .. autoattribute:: GradingProfile.grade_record_types

   .. automethod:: GradingProfile.supports_grade_record_type

   .. autoattribute:: GradingProfile.grade_system_record_types

   .. automethod:: GradingProfile.supports_grade_system_record_type

   .. autoattribute:: GradingProfile.grade_system_search_record_types

   .. automethod:: GradingProfile.supports_grade_system_search_record_type

   .. autoattribute:: GradingProfile.grade_entry_record_types

   .. automethod:: GradingProfile.supports_grade_entry_record_type

   .. autoattribute:: GradingProfile.grade_entry_search_record_types

   .. automethod:: GradingProfile.supports_grade_entry_search_record_type

   .. autoattribute:: GradingProfile.gradebook_column_record_types

   .. automethod:: GradingProfile.supports_gradebook_column_record_type

   .. autoattribute:: GradingProfile.gradebook_column_search_record_types

   .. automethod:: GradingProfile.supports_gradebook_column_search_record_type

   .. autoattribute:: GradingProfile.gradebook_column_summary_record_types

   .. automethod:: GradingProfile.supports_gradebook_column_summary_record_type

   .. autoattribute:: GradingProfile.gradebook_record_types

   .. automethod:: GradingProfile.supports_gradebook_record_type

   .. autoattribute:: GradingProfile.gradebook_search_record_types

   .. automethod:: GradingProfile.supports_gradebook_search_record_type

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

