
.. currentmodule:: dlkit.assessment.managers
.. automodule:: dlkit.assessment.managers

Managers
========


Assessment Profile
------------------

.. autoclass:: AssessmentProfile
   :show-inheritance:

   .. automethod:: AssessmentProfile.supports_visible_federation

   .. automethod:: AssessmentProfile.supports_my_assessment_taken

   .. automethod:: AssessmentProfile.supports_assessment

   .. automethod:: AssessmentProfile.supports_assessment_results

   .. automethod:: AssessmentProfile.supports_item_lookup

   .. automethod:: AssessmentProfile.supports_item_query

   .. automethod:: AssessmentProfile.supports_item_search

   .. automethod:: AssessmentProfile.supports_item_admin

   .. automethod:: AssessmentProfile.supports_item_notification

   .. automethod:: AssessmentProfile.supports_item_bank

   .. automethod:: AssessmentProfile.supports_item_bank_assignment

   .. automethod:: AssessmentProfile.supports_item_smart_bank

   .. automethod:: AssessmentProfile.supports_assessment_lookup

   .. automethod:: AssessmentProfile.supports_assessment_query

   .. automethod:: AssessmentProfile.supports_assessment_search

   .. automethod:: AssessmentProfile.supports_assessment_admin

   .. automethod:: AssessmentProfile.supports_assessment_notification

   .. automethod:: AssessmentProfile.supports_assessment_bank

   .. automethod:: AssessmentProfile.supports_assessment_bank_assignment

   .. automethod:: AssessmentProfile.supports_assessment_smart_bank

   .. automethod:: AssessmentProfile.supports_assessment_basic_authoring

   .. automethod:: AssessmentProfile.supports_assessment_offered_lookup

   .. automethod:: AssessmentProfile.supports_assessment_offered_query

   .. automethod:: AssessmentProfile.supports_assessment_offered_search

   .. automethod:: AssessmentProfile.supports_assessment_offered_admin

   .. automethod:: AssessmentProfile.supports_assessment_offered_notification

   .. automethod:: AssessmentProfile.supports_assessment_offered_bank

   .. automethod:: AssessmentProfile.supports_assessment_offered_bank_assignment

   .. automethod:: AssessmentProfile.supports_assessment_offered_smart_bank

   .. automethod:: AssessmentProfile.supports_assessment_taken_lookup

   .. automethod:: AssessmentProfile.supports_assessment_taken_query

   .. automethod:: AssessmentProfile.supports_assessment_taken_search

   .. automethod:: AssessmentProfile.supports_assessment_taken_admin

   .. automethod:: AssessmentProfile.supports_assessment_taken_notification

   .. automethod:: AssessmentProfile.supports_assessment_taken_bank

   .. automethod:: AssessmentProfile.supports_assessment_taken_bank_assignment

   .. automethod:: AssessmentProfile.supports_assessment_taken_smart_bank

   .. automethod:: AssessmentProfile.supports_bank_lookup

   .. automethod:: AssessmentProfile.supports_bank_query

   .. automethod:: AssessmentProfile.supports_bank_search

   .. automethod:: AssessmentProfile.supports_bank_admin

   .. automethod:: AssessmentProfile.supports_bank_notification

   .. automethod:: AssessmentProfile.supports_bank_hierarchy

   .. automethod:: AssessmentProfile.supports_bank_hierarchy_design

   .. automethod:: AssessmentProfile.supports_assessment_authoring

   .. automethod:: AssessmentProfile.supports_assessment_batch

   .. autoattribute:: AssessmentProfile.item_record_types

   .. automethod:: AssessmentProfile.supports_item_record_type

   .. autoattribute:: AssessmentProfile.item_search_record_types

   .. automethod:: AssessmentProfile.supports_item_search_record_type

   .. autoattribute:: AssessmentProfile.assessment_record_types

   .. automethod:: AssessmentProfile.supports_assessment_record_type

   .. autoattribute:: AssessmentProfile.assessment_search_record_types

   .. automethod:: AssessmentProfile.supports_assessment_search_record_type

   .. autoattribute:: AssessmentProfile.assessment_offered_record_types

   .. automethod:: AssessmentProfile.supports_assessment_offered_record_type

   .. autoattribute:: AssessmentProfile.assessment_offered_search_record_types

   .. automethod:: AssessmentProfile.supports_assessment_offered_search_record_type

   .. autoattribute:: AssessmentProfile.assessment_taken_record_types

   .. automethod:: AssessmentProfile.supports_assessment_taken_record_type

   .. autoattribute:: AssessmentProfile.assessment_taken_search_record_types

   .. automethod:: AssessmentProfile.supports_assessment_taken_search_record_type

   .. autoattribute:: AssessmentProfile.assessment_section_record_types

   .. automethod:: AssessmentProfile.supports_assessment_section_record_type

   .. autoattribute:: AssessmentProfile.bank_record_types

   .. automethod:: AssessmentProfile.supports_bank_record_type

   .. autoattribute:: AssessmentProfile.bank_search_record_types

   .. automethod:: AssessmentProfile.supports_bank_search_record_type

Assessment Manager
------------------

.. autoclass:: AssessmentManager
   :show-inheritance:

   .. autoattribute:: AssessmentManager.my_assessment_taken_session

   .. automethod:: AssessmentManager.get_my_assessment_taken_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_session

   .. automethod:: AssessmentManager.get_assessment_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_results_session

   .. automethod:: AssessmentManager.get_assessment_results_session_for_bank

   .. autoattribute:: AssessmentManager.item_lookup_session

   .. automethod:: AssessmentManager.get_item_lookup_session_for_bank

   .. autoattribute:: AssessmentManager.item_query_session

   .. automethod:: AssessmentManager.get_item_query_session_for_bank

   .. autoattribute:: AssessmentManager.item_search_session

   .. automethod:: AssessmentManager.get_item_search_session_for_bank

   .. autoattribute:: AssessmentManager.item_admin_session

   .. automethod:: AssessmentManager.get_item_admin_session_for_bank

   .. automethod:: AssessmentManager.get_item_notification_session

   .. automethod:: AssessmentManager.get_item_notification_session_for_bank

   .. autoattribute:: AssessmentManager.item_bank_session

   .. autoattribute:: AssessmentManager.item_bank_assignment_session

   .. automethod:: AssessmentManager.get_item_smart_bank_session

   .. autoattribute:: AssessmentManager.assessment_lookup_session

   .. automethod:: AssessmentManager.get_assessment_lookup_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_query_session

   .. automethod:: AssessmentManager.get_assessment_query_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_search_session

   .. automethod:: AssessmentManager.get_assessment_search_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_admin_session

   .. automethod:: AssessmentManager.get_assessment_admin_session_for_bank

   .. automethod:: AssessmentManager.get_assessment_notification_session

   .. automethod:: AssessmentManager.get_assessment_notification_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_bank_session

   .. autoattribute:: AssessmentManager.assessment_bank_assignment_session

   .. automethod:: AssessmentManager.get_assessment_smart_bank_session

   .. autoattribute:: AssessmentManager.assessment_basic_authoring_session

   .. automethod:: AssessmentManager.get_assessment_basic_authoring_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_offered_lookup_session

   .. automethod:: AssessmentManager.get_assessment_offered_lookup_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_offered_query_session

   .. automethod:: AssessmentManager.get_assessment_offered_query_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_offered_search_session

   .. automethod:: AssessmentManager.get_assessment_offered_search_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_offered_admin_session

   .. automethod:: AssessmentManager.get_assessment_offered_admin_session_for_bank

   .. automethod:: AssessmentManager.get_assessment_offered_notification_session

   .. automethod:: AssessmentManager.get_assessment_offered_notification_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_offered_bank_session

   .. autoattribute:: AssessmentManager.assessment_offered_bank_assignment_session

   .. automethod:: AssessmentManager.get_assessment_offered_smart_bank_session

   .. autoattribute:: AssessmentManager.assessment_taken_lookup_session

   .. automethod:: AssessmentManager.get_assessment_taken_lookup_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_taken_query_session

   .. automethod:: AssessmentManager.get_assessment_taken_query_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_taken_search_session

   .. automethod:: AssessmentManager.get_assessment_taken_search_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_taken_admin_session

   .. automethod:: AssessmentManager.get_assessment_taken_admin_session_for_bank

   .. automethod:: AssessmentManager.get_assessment_taken_notification_session

   .. automethod:: AssessmentManager.get_assessment_taken_notification_session_for_bank

   .. autoattribute:: AssessmentManager.assessment_taken_bank_session

   .. autoattribute:: AssessmentManager.assessment_taken_bank_assignment_session

   .. automethod:: AssessmentManager.get_assessment_taken_smart_bank_session

   .. autoattribute:: AssessmentManager.bank_lookup_session

   .. autoattribute:: AssessmentManager.bank_query_session

   .. autoattribute:: AssessmentManager.bank_search_session

   .. autoattribute:: AssessmentManager.bank_admin_session

   .. automethod:: AssessmentManager.get_bank_notification_session

   .. autoattribute:: AssessmentManager.bank_hierarchy_session

   .. autoattribute:: AssessmentManager.bank_hierarchy_design_session

   .. autoattribute:: AssessmentManager.assessment_authoring_manager

   .. autoattribute:: AssessmentManager.assessment_batch_manager

Assessment Proxy Manager
------------------------

.. autoclass:: AssessmentProxyManager
   :show-inheritance:

   .. automethod:: AssessmentProxyManager.get_my_assessment_taken_session

   .. automethod:: AssessmentProxyManager.get_my_assessment_taken_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_session

   .. automethod:: AssessmentProxyManager.get_assessment_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_results_session

   .. automethod:: AssessmentProxyManager.get_assessment_results_session_for_bank

   .. automethod:: AssessmentProxyManager.get_item_lookup_session

   .. automethod:: AssessmentProxyManager.get_item_lookup_session_for_bank

   .. automethod:: AssessmentProxyManager.get_item_query_session

   .. automethod:: AssessmentProxyManager.get_item_query_session_for_bank

   .. automethod:: AssessmentProxyManager.get_item_search_session

   .. automethod:: AssessmentProxyManager.get_item_search_session_for_bank

   .. automethod:: AssessmentProxyManager.get_item_admin_session

   .. automethod:: AssessmentProxyManager.get_item_admin_session_for_bank

   .. automethod:: AssessmentProxyManager.get_item_notification_session

   .. automethod:: AssessmentProxyManager.get_item_notification_session_for_bank

   .. automethod:: AssessmentProxyManager.get_item_bank_session

   .. automethod:: AssessmentProxyManager.get_item_bank_assignment_session

   .. automethod:: AssessmentProxyManager.get_item_smart_bank_session

   .. automethod:: AssessmentProxyManager.get_assessment_lookup_session

   .. automethod:: AssessmentProxyManager.get_assessment_lookup_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_query_session

   .. automethod:: AssessmentProxyManager.get_assessment_query_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_search_session

   .. automethod:: AssessmentProxyManager.get_assessment_search_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_admin_session

   .. automethod:: AssessmentProxyManager.get_assessment_admin_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_notification_session

   .. automethod:: AssessmentProxyManager.get_assessment_notification_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_bank_session

   .. automethod:: AssessmentProxyManager.get_assessment_bank_assignment_session

   .. automethod:: AssessmentProxyManager.get_assessment_smart_bank_session

   .. automethod:: AssessmentProxyManager.get_assessment_basic_authoring_session

   .. automethod:: AssessmentProxyManager.get_assessment_basic_authoring_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_offered_lookup_session

   .. automethod:: AssessmentProxyManager.get_assessment_offered_lookup_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_offered_query_session

   .. automethod:: AssessmentProxyManager.get_assessment_offered_query_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_offered_search_session

   .. automethod:: AssessmentProxyManager.get_assessment_offered_search_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_offered_admin_session

   .. automethod:: AssessmentProxyManager.get_assessment_offered_admin_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_offered_notification_session

   .. automethod:: AssessmentProxyManager.get_assessment_offered_notification_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_offered_bank_session

   .. automethod:: AssessmentProxyManager.get_assessment_offered_bank_assignment_session

   .. automethod:: AssessmentProxyManager.get_assessment_offered_smart_bank_session

   .. automethod:: AssessmentProxyManager.get_assessment_taken_lookup_session

   .. automethod:: AssessmentProxyManager.get_assessment_taken_lookup_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_taken_query_session

   .. automethod:: AssessmentProxyManager.get_assessment_taken_query_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_taken_search_session

   .. automethod:: AssessmentProxyManager.get_assessment_taken_search_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_taken_admin_session

   .. automethod:: AssessmentProxyManager.get_assessment_taken_admin_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_taken_notification_session

   .. automethod:: AssessmentProxyManager.get_assessment_taken_notification_session_for_bank

   .. automethod:: AssessmentProxyManager.get_assessment_taken_bank_session

   .. automethod:: AssessmentProxyManager.get_assessment_taken_bank_assignment_session

   .. automethod:: AssessmentProxyManager.get_assessment_taken_smart_bank_session

   .. automethod:: AssessmentProxyManager.get_bank_lookup_session

   .. automethod:: AssessmentProxyManager.get_bank_query_session

   .. automethod:: AssessmentProxyManager.get_bank_search_session

   .. automethod:: AssessmentProxyManager.get_bank_admin_session

   .. automethod:: AssessmentProxyManager.get_bank_notification_session

   .. automethod:: AssessmentProxyManager.get_bank_hierarchy_session

   .. automethod:: AssessmentProxyManager.get_bank_hierarchy_design_session

   .. autoattribute:: AssessmentProxyManager.assessment_authoring_proxy_manager

   .. autoattribute:: AssessmentProxyManager.assessment_batch_proxy_manager

