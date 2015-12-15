

Managers
========


Grading Profile
---------------

.. py:class:: GradingProfile(osid_managers.OsidProfile, grading_managers.GradingProfile)
    The ``GradingProfile`` describes the interoperability among grading services.

    .. py:method:: supports_visible_federation():
        :noindex:


    .. py:method:: supports_grade_system_lookup():
        :noindex:


    .. py:method:: supports_grade_system_query():
        :noindex:


    .. py:method:: supports_grade_system_search():
        :noindex:


    .. py:method:: supports_grade_system_admin():
        :noindex:


    .. py:method:: supports_grade_system_notification():
        :noindex:


    .. py:method:: supports_grade_system_gradebook():
        :noindex:


    .. py:method:: supports_grade_system_gradebook_assignment():
        :noindex:


    .. py:method:: supports_grade_system_smart_gradebook():
        :noindex:


    .. py:method:: supports_grade_entry_lookup():
        :noindex:


    .. py:method:: supports_grade_entry_query():
        :noindex:


    .. py:method:: supports_grade_entry_search():
        :noindex:


    .. py:method:: supports_grade_entry_admin():
        :noindex:


    .. py:method:: supports_grade_entry_notification():
        :noindex:


    .. py:method:: supports_gradebook_column_lookup():
        :noindex:


    .. py:method:: supports_gradebook_column_query():
        :noindex:


    .. py:method:: supports_gradebook_column_search():
        :noindex:


    .. py:method:: supports_gradebook_column_admin():
        :noindex:


    .. py:method:: supports_gradebook_column_notification():
        :noindex:


    .. py:method:: supports_gradebook_column_gradebook():
        :noindex:


    .. py:method:: supports_gradebook_column_gradebook_assignment():
        :noindex:


    .. py:method:: supports_gradebook_column_smart_gradebook():
        :noindex:


    .. py:method:: supports_gradebook_lookup():
        :noindex:


    .. py:method:: supports_gradebook_query():
        :noindex:


    .. py:method:: supports_gradebook_search():
        :noindex:


    .. py:method:: supports_gradebook_admin():
        :noindex:


    .. py:method:: supports_gradebook_notification():
        :noindex:


    .. py:method:: supports_gradebook_hierarchy():
        :noindex:


    .. py:method:: supports_gradebook_hierarchy_design():
        :noindex:


    .. py:method:: supports_grading_batch():
        :noindex:


    .. py:method:: supports_grading_calculation():
        :noindex:


    .. py:method:: supports_grading_transform():
        :noindex:


    .. py:method:: get_grade_record_types():
        :noindex:


    .. py:attribute:: grade_record_types
        :noindex:


    .. py:method:: supports_grade_record_type(grade_record_type):
        :noindex:


    .. py:method:: get_grade_system_record_types():
        :noindex:


    .. py:attribute:: grade_system_record_types
        :noindex:


    .. py:method:: supports_grade_system_record_type(grade_system_record_type):
        :noindex:


    .. py:method:: get_grade_system_search_record_types():
        :noindex:


    .. py:attribute:: grade_system_search_record_types
        :noindex:


    .. py:method:: supports_grade_system_search_record_type(grade_system_search_record_type):
        :noindex:


    .. py:method:: get_grade_entry_record_types():
        :noindex:


    .. py:attribute:: grade_entry_record_types
        :noindex:


    .. py:method:: supports_grade_entry_record_type(grade_entry_record_type):
        :noindex:


    .. py:method:: get_grade_entry_search_record_types():
        :noindex:


    .. py:attribute:: grade_entry_search_record_types
        :noindex:


    .. py:method:: supports_grade_entry_search_record_type(grade_entry_search_record_type):
        :noindex:


    .. py:method:: get_gradebook_column_record_types():
        :noindex:


    .. py:attribute:: gradebook_column_record_types
        :noindex:


    .. py:method:: supports_gradebook_column_record_type(gradebook_column_record_type):
        :noindex:


    .. py:method:: get_gradebook_column_search_record_types():
        :noindex:


    .. py:attribute:: gradebook_column_search_record_types
        :noindex:


    .. py:method:: supports_gradebook_column_search_record_type(gradebook_column_search_record_type):
        :noindex:


    .. py:method:: get_gradebook_column_summary_record_types():
        :noindex:


    .. py:attribute:: gradebook_column_summary_record_types
        :noindex:


    .. py:method:: supports_gradebook_column_summary_record_type(gradebook_column_summary_record_type):
        :noindex:


    .. py:method:: get_gradebook_record_types():
        :noindex:


    .. py:attribute:: gradebook_record_types
        :noindex:


    .. py:method:: supports_gradebook_record_type(gradebook_record_type):
        :noindex:


    .. py:method:: get_gradebook_search_record_types():
        :noindex:


    .. py:attribute:: gradebook_search_record_types
        :noindex:


    .. py:method:: supports_gradebook_search_record_type(gradebook_search_record_type):
        :noindex:


Grading Manager
---------------

.. py:class:: GradingManager(osid_managers.OsidManager, GradingProfile, grading_managers.GradingManager)
        :noindex:

    .. py:method:: get_grade_system_lookup_session():
        :noindex:


    .. py:attribute:: grade_system_lookup_session
        :noindex:


    .. py:method:: get_grade_system_lookup_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_grade_system_query_session():
        :noindex:


    .. py:attribute:: grade_system_query_session
        :noindex:


    .. py:method:: get_grade_system_query_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_grade_system_search_session():
        :noindex:


    .. py:attribute:: grade_system_search_session
        :noindex:


    .. py:method:: get_grade_system_search_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_grade_system_admin_session():
        :noindex:


    .. py:attribute:: grade_system_admin_session
        :noindex:


    .. py:method:: get_grade_system_admin_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_grade_system_notification_session(grade_system_receiver):
        :noindex:


    .. py:method:: get_grade_system_notification_session_for_gradebook(grade_system_receiver, gradebook_id):
        :noindex:


    .. py:method:: get_grade_system_gradebook_session():
        :noindex:


    .. py:attribute:: grade_system_gradebook_session
        :noindex:


    .. py:method:: get_grade_system_gradebook_assignment_session():
        :noindex:


    .. py:attribute:: grade_system_gradebook_assignment_session
        :noindex:


    .. py:method:: get_grade_system_smart_gradebook_session(gradebook_id):
        :noindex:


    .. py:method:: get_grade_entry_lookup_session():
        :noindex:


    .. py:attribute:: grade_entry_lookup_session
        :noindex:


    .. py:method:: get_grade_entry_lookup_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_grade_entry_query_session():
        :noindex:


    .. py:attribute:: grade_entry_query_session
        :noindex:


    .. py:method:: get_grade_entry_query_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_grade_entry_search_session():
        :noindex:


    .. py:attribute:: grade_entry_search_session
        :noindex:


    .. py:method:: get_grade_entry_search_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_grade_entry_admin_session():
        :noindex:


    .. py:attribute:: grade_entry_admin_session
        :noindex:


    .. py:method:: get_grade_entry_admin_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_grade_entry_notification_session(receiver):
        :noindex:


    .. py:method:: get_grade_entry_notification_session_for_gradebook(receiver, gradebook_id):
        :noindex:


    .. py:method:: get_gradebook_column_lookup_session():
        :noindex:


    .. py:attribute:: gradebook_column_lookup_session
        :noindex:


    .. py:method:: get_gradebook_column_lookup_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_gradebook_column_query_session():
        :noindex:


    .. py:attribute:: gradebook_column_query_session
        :noindex:


    .. py:method:: get_gradebook_column_query_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_gradebook_column_search_session():
        :noindex:


    .. py:attribute:: gradebook_column_search_session
        :noindex:


    .. py:method:: get_gradebook_column_search_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_gradebook_column_admin_session():
        :noindex:


    .. py:attribute:: gradebook_column_admin_session
        :noindex:


    .. py:method:: get_gradebook_column_admin_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_gradebook_column_notification_session(gradebook_column_receiver):
        :noindex:


    .. py:method:: get_gradebook_column_notification_session_for_gradebook(gradebook_column_receiver, gradebook_id):
        :noindex:


    .. py:method:: get_gradebook_column_gradebook_session():
        :noindex:


    .. py:attribute:: gradebook_column_gradebook_session
        :noindex:


    .. py:method:: get_gradebook_column_gradebook_assignment_session():
        :noindex:


    .. py:attribute:: gradebook_column_gradebook_assignment_session
        :noindex:


    .. py:method:: get_gradebook_column_smart_gradebook_session(gradebook_id):
        :noindex:


    .. py:method:: get_gradebook_lookup_session():
        :noindex:


    .. py:attribute:: gradebook_lookup_session
        :noindex:


    .. py:method:: get_gradebook_query_session():
        :noindex:


    .. py:attribute:: gradebook_query_session
        :noindex:


    .. py:method:: get_gradebook_search_session():
        :noindex:


    .. py:attribute:: gradebook_search_session
        :noindex:


    .. py:method:: get_gradebook_admin_session():
        :noindex:


    .. py:attribute:: gradebook_admin_session
        :noindex:


    .. py:method:: get_gradebook_notification_session(gradebook_receiver):
        :noindex:


    .. py:method:: get_gradebook_hierarchy_session():
        :noindex:


    .. py:attribute:: gradebook_hierarchy_session
        :noindex:


    .. py:method:: get_gradebook_hierarchy_design_session():
        :noindex:


    .. py:attribute:: gradebook_hierarchy_design_session
        :noindex:


    .. py:method:: get_grading_batch_manager():
        :noindex:


    .. py:attribute:: grading_batch_manager
        :noindex:


    .. py:method:: get_grading_calculation_manager():
        :noindex:


    .. py:attribute:: grading_calculation_manager
        :noindex:


    .. py:method:: get_grading_transform_manager():
        :noindex:


    .. py:attribute:: grading_transform_manager
        :noindex:


Grading Proxy Manager
---------------------

.. py:class:: GradingProxyManager(osid_managers.OsidProxyManager, GradingProfile, grading_managers.GradingProxyManager)
        :noindex:

    .. py:method:: get_grade_system_lookup_session(proxy):
        :noindex:


    .. py:method:: get_grade_system_lookup_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_system_query_session(proxy):
        :noindex:


    .. py:method:: get_grade_system_query_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_system_search_session(proxy):
        :noindex:


    .. py:method:: get_grade_system_search_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_system_admin_session(proxy):
        :noindex:


    .. py:method:: get_grade_system_admin_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_system_notification_session(grade_system_receiver, proxy):
        :noindex:


    .. py:method:: get_grade_system_notification_session_for_gradebook(grade_system_receiver, gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_system_gradebook_session(proxy):
        :noindex:


    .. py:method:: get_grade_system_gradebook_assignment_session(proxy):
        :noindex:


    .. py:method:: get_grade_system_smart_gradebook_session(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_entry_lookup_session(proxy):
        :noindex:


    .. py:method:: get_grade_entry_lookup_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_entry_query_session(proxy):
        :noindex:


    .. py:method:: get_grade_entry_query_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_entry_search_session(proxy):
        :noindex:


    .. py:method:: get_grade_entry_search_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_entry_admin_session(proxy):
        :noindex:


    .. py:method:: get_grade_entry_admin_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_entry_notification_session(grade_entry_receiver, proxy):
        :noindex:


    .. py:method:: get_grade_entry_notification_session_for_gradebook(grade_entry_receiver, gradebook_id, proxy):
        :noindex:


    .. py:method:: get_gradebook_column_lookup_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_column_lookup_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_gradebook_column_query_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_column_query_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_gradebook_column_search_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_column_search_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_gradebook_column_admin_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_column_admin_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_gradebook_column_notification_session(gradebook_column_receiver, proxy):
        :noindex:


    .. py:method:: get_gradebook_column_notification_session_for_gradebook(gradebook_column_receiver, gradebook_id, proxy):
        :noindex:


    .. py:method:: get_gradebook_column_gradebook_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_column_gradebook_assignment_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_column_smart_gradebook_session(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_gradebook_lookup_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_query_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_search_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_admin_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_notification_session(gradebook_receiver, proxy):
        :noindex:


    .. py:method:: get_gradebook_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_grading_batch_proxy_manager():
        :noindex:


    .. py:attribute:: grading_batch_proxy_manager
        :noindex:


    .. py:method:: get_grading_calculation_proxy_manager():
        :noindex:


    .. py:attribute:: grading_calculation_proxy_manager
        :noindex:


    .. py:method:: get_grading_transform_proxy_manager():
        :noindex:


    .. py:attribute:: grading_transform_proxy_manager
        :noindex:


