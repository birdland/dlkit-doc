

Managers
========


Assessment Profile
------------------

.. py:class:: AssessmentProfile(osid_managers.OsidProfile, assessment_managers.AssessmentProfile)
    The ``AssessmentProfile`` describes the interoperability among assessment services.

    .. py:method:: supports_visible_federation():
        :noindex:


    .. py:method:: supports_my_assessment_taken():
        :noindex:


    .. py:method:: supports_assessment():
        :noindex:


    .. py:method:: supports_assessment_results():
        :noindex:


    .. py:method:: supports_item_lookup():
        :noindex:


    .. py:method:: supports_item_query():
        :noindex:


    .. py:method:: supports_item_search():
        :noindex:


    .. py:method:: supports_item_admin():
        :noindex:


    .. py:method:: supports_item_notification():
        :noindex:


    .. py:method:: supports_item_bank():
        :noindex:


    .. py:method:: supports_item_bank_assignment():
        :noindex:


    .. py:method:: supports_item_smart_bank():
        :noindex:


    .. py:method:: supports_assessment_lookup():
        :noindex:


    .. py:method:: supports_assessment_query():
        :noindex:


    .. py:method:: supports_assessment_search():
        :noindex:


    .. py:method:: supports_assessment_admin():
        :noindex:


    .. py:method:: supports_assessment_notification():
        :noindex:


    .. py:method:: supports_assessment_bank():
        :noindex:


    .. py:method:: supports_assessment_bank_assignment():
        :noindex:


    .. py:method:: supports_assessment_smart_bank():
        :noindex:


    .. py:method:: supports_assessment_basic_authoring():
        :noindex:


    .. py:method:: supports_assessment_offered_lookup():
        :noindex:


    .. py:method:: supports_assessment_offered_query():
        :noindex:


    .. py:method:: supports_assessment_offered_search():
        :noindex:


    .. py:method:: supports_assessment_offered_admin():
        :noindex:


    .. py:method:: supports_assessment_offered_notification():
        :noindex:


    .. py:method:: supports_assessment_offered_bank():
        :noindex:


    .. py:method:: supports_assessment_offered_bank_assignment():
        :noindex:


    .. py:method:: supports_assessment_offered_smart_bank():
        :noindex:


    .. py:method:: supports_assessment_taken_lookup():
        :noindex:


    .. py:method:: supports_assessment_taken_query():
        :noindex:


    .. py:method:: supports_assessment_taken_search():
        :noindex:


    .. py:method:: supports_assessment_taken_admin():
        :noindex:


    .. py:method:: supports_assessment_taken_notification():
        :noindex:


    .. py:method:: supports_assessment_taken_bank():
        :noindex:


    .. py:method:: supports_assessment_taken_bank_assignment():
        :noindex:


    .. py:method:: supports_assessment_taken_smart_bank():
        :noindex:


    .. py:method:: supports_bank_lookup():
        :noindex:


    .. py:method:: supports_bank_query():
        :noindex:


    .. py:method:: supports_bank_search():
        :noindex:


    .. py:method:: supports_bank_admin():
        :noindex:


    .. py:method:: supports_bank_notification():
        :noindex:


    .. py:method:: supports_bank_hierarchy():
        :noindex:


    .. py:method:: supports_bank_hierarchy_design():
        :noindex:


    .. py:method:: supports_assessment_authoring():
        :noindex:


    .. py:method:: supports_assessment_batch():
        :noindex:


    .. py:method:: get_item_record_types():
        :noindex:


    .. py:attribute:: item_record_types
        :noindex:


    .. py:method:: supports_item_record_type(item_record_type):
        :noindex:


    .. py:method:: get_item_search_record_types():
        :noindex:


    .. py:attribute:: item_search_record_types
        :noindex:


    .. py:method:: supports_item_search_record_type(item_search_record_type):
        :noindex:


    .. py:method:: get_assessment_record_types():
        :noindex:


    .. py:attribute:: assessment_record_types
        :noindex:


    .. py:method:: supports_assessment_record_type(assessment_record_type):
        :noindex:


    .. py:method:: get_assessment_search_record_types():
        :noindex:


    .. py:attribute:: assessment_search_record_types
        :noindex:


    .. py:method:: supports_assessment_search_record_type(assessment_search_record_type):
        :noindex:


    .. py:method:: get_assessment_offered_record_types():
        :noindex:


    .. py:attribute:: assessment_offered_record_types
        :noindex:


    .. py:method:: supports_assessment_offered_record_type(assessment_offered_record_type):
        :noindex:


    .. py:method:: get_assessment_offered_search_record_types():
        :noindex:


    .. py:attribute:: assessment_offered_search_record_types
        :noindex:


    .. py:method:: supports_assessment_offered_search_record_type(assessment_offered_search_record_type):
        :noindex:


    .. py:method:: get_assessment_taken_record_types():
        :noindex:


    .. py:attribute:: assessment_taken_record_types
        :noindex:


    .. py:method:: supports_assessment_taken_record_type(assessment_taken_record_type):
        :noindex:


    .. py:method:: get_assessment_taken_search_record_types():
        :noindex:


    .. py:attribute:: assessment_taken_search_record_types
        :noindex:


    .. py:method:: supports_assessment_taken_search_record_type(assessment_taken_search_record_type):
        :noindex:


    .. py:method:: get_assessment_section_record_types():
        :noindex:


    .. py:attribute:: assessment_section_record_types
        :noindex:


    .. py:method:: supports_assessment_section_record_type(assessment_section_record_type):
        :noindex:


    .. py:method:: get_bank_record_types():
        :noindex:


    .. py:attribute:: bank_record_types
        :noindex:


    .. py:method:: supports_bank_record_type(bank_record_type):
        :noindex:


    .. py:method:: get_bank_search_record_types():
        :noindex:


    .. py:attribute:: bank_search_record_types
        :noindex:


    .. py:method:: supports_bank_search_record_type(bank_search_record_type):
        :noindex:


Assessment Manager
------------------

.. py:class:: AssessmentManager(osid_managers.OsidManager, AssessmentProfile, assessment_managers.AssessmentManager)
        :noindex:

    .. py:method:: get_my_assessment_taken_session():
        :noindex:


    .. py:attribute:: my_assessment_taken_session
        :noindex:


    .. py:method:: get_my_assessment_taken_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_session():
        :noindex:


    .. py:attribute:: assessment_session
        :noindex:


    .. py:method:: get_assessment_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_results_session():
        :noindex:


    .. py:attribute:: assessment_results_session
        :noindex:


    .. py:method:: get_assessment_results_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_item_lookup_session():
        :noindex:


    .. py:attribute:: item_lookup_session
        :noindex:


    .. py:method:: get_item_lookup_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_item_query_session():
        :noindex:


    .. py:attribute:: item_query_session
        :noindex:


    .. py:method:: get_item_query_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_item_search_session():
        :noindex:


    .. py:attribute:: item_search_session
        :noindex:


    .. py:method:: get_item_search_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_item_admin_session():
        :noindex:


    .. py:attribute:: item_admin_session
        :noindex:


    .. py:method:: get_item_admin_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_item_notification_session(item_receiver):
        :noindex:


    .. py:method:: get_item_notification_session_for_bank(item_receiver, bank_id):
        :noindex:


    .. py:method:: get_item_bank_session():
        :noindex:


    .. py:attribute:: item_bank_session
        :noindex:


    .. py:method:: get_item_bank_assignment_session():
        :noindex:


    .. py:attribute:: item_bank_assignment_session
        :noindex:


    .. py:method:: get_item_smart_bank_session(bank_id):
        :noindex:


    .. py:method:: get_assessment_lookup_session():
        :noindex:


    .. py:attribute:: assessment_lookup_session
        :noindex:


    .. py:method:: get_assessment_lookup_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_query_session():
        :noindex:


    .. py:attribute:: assessment_query_session
        :noindex:


    .. py:method:: get_assessment_query_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_search_session():
        :noindex:


    .. py:attribute:: assessment_search_session
        :noindex:


    .. py:method:: get_assessment_search_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_admin_session():
        :noindex:


    .. py:attribute:: assessment_admin_session
        :noindex:


    .. py:method:: get_assessment_admin_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_notification_session(assessment_receiver):
        :noindex:


    .. py:method:: get_assessment_notification_session_for_bank(assessment_receiver, bank_id):
        :noindex:


    .. py:method:: get_assessment_bank_session():
        :noindex:


    .. py:attribute:: assessment_bank_session
        :noindex:


    .. py:method:: get_assessment_bank_assignment_session():
        :noindex:


    .. py:attribute:: assessment_bank_assignment_session
        :noindex:


    .. py:method:: get_assessment_smart_bank_session(bank_id):
        :noindex:


    .. py:method:: get_assessment_basic_authoring_session():
        :noindex:


    .. py:attribute:: assessment_basic_authoring_session
        :noindex:


    .. py:method:: get_assessment_basic_authoring_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_offered_lookup_session():
        :noindex:


    .. py:attribute:: assessment_offered_lookup_session
        :noindex:


    .. py:method:: get_assessment_offered_lookup_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_offered_query_session():
        :noindex:


    .. py:attribute:: assessment_offered_query_session
        :noindex:


    .. py:method:: get_assessment_offered_query_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_offered_search_session():
        :noindex:


    .. py:attribute:: assessment_offered_search_session
        :noindex:


    .. py:method:: get_assessment_offered_search_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_offered_admin_session():
        :noindex:


    .. py:attribute:: assessment_offered_admin_session
        :noindex:


    .. py:method:: get_assessment_offered_admin_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_offered_notification_session(assessment_offered_receiver):
        :noindex:


    .. py:method:: get_assessment_offered_notification_session_for_bank(assessment_offered_receiver, bank_id):
        :noindex:


    .. py:method:: get_assessment_offered_bank_session():
        :noindex:


    .. py:attribute:: assessment_offered_bank_session
        :noindex:


    .. py:method:: get_assessment_offered_bank_assignment_session():
        :noindex:


    .. py:attribute:: assessment_offered_bank_assignment_session
        :noindex:


    .. py:method:: get_assessment_offered_smart_bank_session(bank_id):
        :noindex:


    .. py:method:: get_assessment_taken_lookup_session():
        :noindex:


    .. py:attribute:: assessment_taken_lookup_session
        :noindex:


    .. py:method:: get_assessment_taken_lookup_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_taken_query_session():
        :noindex:


    .. py:attribute:: assessment_taken_query_session
        :noindex:


    .. py:method:: get_assessment_taken_query_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_taken_search_session():
        :noindex:


    .. py:attribute:: assessment_taken_search_session
        :noindex:


    .. py:method:: get_assessment_taken_search_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_taken_admin_session():
        :noindex:


    .. py:attribute:: assessment_taken_admin_session
        :noindex:


    .. py:method:: get_assessment_taken_admin_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_taken_notification_session(assessment_taken_receiver):
        :noindex:


    .. py:method:: get_assessment_taken_notification_session_for_bank(assessment_taken_receiver, bank_id):
        :noindex:


    .. py:method:: get_assessment_taken_bank_session():
        :noindex:


    .. py:attribute:: assessment_taken_bank_session
        :noindex:


    .. py:method:: get_assessment_taken_bank_assignment_session():
        :noindex:


    .. py:attribute:: assessment_taken_bank_assignment_session
        :noindex:


    .. py:method:: get_assessment_taken_smart_bank_session(bank_id):
        :noindex:


    .. py:method:: get_bank_lookup_session():
        :noindex:


    .. py:attribute:: bank_lookup_session
        :noindex:


    .. py:method:: get_bank_query_session():
        :noindex:


    .. py:attribute:: bank_query_session
        :noindex:


    .. py:method:: get_bank_search_session():
        :noindex:


    .. py:attribute:: bank_search_session
        :noindex:


    .. py:method:: get_bank_admin_session():
        :noindex:


    .. py:attribute:: bank_admin_session
        :noindex:


    .. py:method:: get_bank_notification_session(bankreceiver):
        :noindex:


    .. py:method:: get_bank_hierarchy_session():
        :noindex:


    .. py:attribute:: bank_hierarchy_session
        :noindex:


    .. py:method:: get_bank_hierarchy_design_session():
        :noindex:


    .. py:attribute:: bank_hierarchy_design_session
        :noindex:


    .. py:method:: get_assessment_authoring_manager():
        :noindex:


    .. py:attribute:: assessment_authoring_manager
        :noindex:


    .. py:method:: get_assessment_batch_manager():
        :noindex:


    .. py:attribute:: assessment_batch_manager
        :noindex:


Assessment Proxy Manager
------------------------

.. py:class:: AssessmentProxyManager(osid_managers.OsidProxyManager, AssessmentProfile, assessment_managers.AssessmentProxyManager)
        :noindex:

    .. py:method:: get_my_assessment_taken_session(proxy):
        :noindex:


    .. py:method:: get_my_assessment_taken_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_session(proxy):
        :noindex:


    .. py:method:: get_assessment_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_results_session(proxy):
        :noindex:


    .. py:method:: get_assessment_results_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_item_lookup_session(proxy):
        :noindex:


    .. py:method:: get_item_lookup_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_item_query_session(proxy):
        :noindex:


    .. py:method:: get_item_query_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_item_search_session(proxy):
        :noindex:


    .. py:method:: get_item_search_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_item_admin_session(proxy):
        :noindex:


    .. py:method:: get_item_admin_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_item_notification_session(item_receiver, proxy):
        :noindex:


    .. py:method:: get_item_notification_session_for_bank(item_receiver, bank_id, proxy):
        :noindex:


    .. py:method:: get_item_bank_session(proxy):
        :noindex:


    .. py:method:: get_item_bank_assignment_session(proxy):
        :noindex:


    .. py:method:: get_item_smart_bank_session(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_lookup_session(proxy):
        :noindex:


    .. py:method:: get_assessment_lookup_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_query_session(proxy):
        :noindex:


    .. py:method:: get_assessment_query_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_search_session(proxy):
        :noindex:


    .. py:method:: get_assessment_search_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_admin_session(proxy):
        :noindex:


    .. py:method:: get_assessment_admin_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_notification_session(assessment_receiver, proxy):
        :noindex:


    .. py:method:: get_assessment_notification_session_for_bank(assessment_receiver, bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_bank_session(proxy):
        :noindex:


    .. py:method:: get_assessment_bank_assignment_session(proxy):
        :noindex:


    .. py:method:: get_assessment_smart_bank_session(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_basic_authoring_session(proxy):
        :noindex:


    .. py:method:: get_assessment_basic_authoring_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_offered_lookup_session(proxy):
        :noindex:


    .. py:method:: get_assessment_offered_lookup_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_offered_query_session(proxy):
        :noindex:


    .. py:method:: get_assessment_offered_query_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_offered_search_session(proxy):
        :noindex:


    .. py:method:: get_assessment_offered_search_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_offered_admin_session(proxy):
        :noindex:


    .. py:method:: get_assessment_offered_admin_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_offered_notification_session(assessment_offered_receiver, proxy):
        :noindex:


    .. py:method:: get_assessment_offered_notification_session_for_bank(assessment_offered_receiver, bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_offered_bank_session(proxy):
        :noindex:


    .. py:method:: get_assessment_offered_bank_assignment_session(proxy):
        :noindex:


    .. py:method:: get_assessment_offered_smart_bank_session(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_taken_lookup_session(proxy):
        :noindex:


    .. py:method:: get_assessment_taken_lookup_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_taken_query_session(proxy):
        :noindex:


    .. py:method:: get_assessment_taken_query_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_taken_search_session(proxy):
        :noindex:


    .. py:method:: get_assessment_taken_search_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_taken_admin_session(proxy):
        :noindex:


    .. py:method:: get_assessment_taken_admin_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_taken_notification_session(assessment_taken_receiver, proxy):
        :noindex:


    .. py:method:: get_assessment_taken_notification_session_for_bank(assessment_taken_receiver, bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_taken_bank_session(proxy):
        :noindex:


    .. py:method:: get_assessment_taken_bank_assignment_session(proxy):
        :noindex:


    .. py:method:: get_assessment_taken_smart_bank_session(bank_id, proxy):
        :noindex:


    .. py:method:: get_bank_lookup_session(proxy):
        :noindex:


    .. py:method:: get_bank_query_session(proxy):
        :noindex:


    .. py:method:: get_bank_search_session(proxy):
        :noindex:


    .. py:method:: get_bank_admin_session(proxy):
        :noindex:


    .. py:method:: get_bank_notification_session(bank_receiver, proxy):
        :noindex:


    .. py:method:: get_bank_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_bank_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_assessment_authoring_proxy_manager():
        :noindex:


    .. py:attribute:: assessment_authoring_proxy_manager
        :noindex:


    .. py:method:: get_assessment_batch_proxy_manager():
        :noindex:


    .. py:attribute:: assessment_batch_proxy_manager
        :noindex:


