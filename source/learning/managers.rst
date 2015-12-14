
.. currentmodule:: dlkit.learning.managers
.. automodule:: dlkit.learning.managers

Managers
========


Learning Profile
----------------

.. autoclass:: LearningProfile
   :show-inheritance:

   .. automethod:: LearningProfile.supports_visible_federation

   .. automethod:: LearningProfile.supports_objective_lookup

   .. automethod:: LearningProfile.supports_objective_query

   .. automethod:: LearningProfile.supports_objective_search

   .. automethod:: LearningProfile.supports_objective_admin

   .. automethod:: LearningProfile.supports_objective_notification

   .. automethod:: LearningProfile.supports_objective_hierarchy

   .. automethod:: LearningProfile.supports_objective_hierarchy_design

   .. automethod:: LearningProfile.supports_objective_sequencing

   .. automethod:: LearningProfile.supports_objective_objective_bank

   .. automethod:: LearningProfile.supports_objective_objective_bank_assignment

   .. automethod:: LearningProfile.supports_objective_smart_objective_bank

   .. automethod:: LearningProfile.supports_objective_requisite

   .. automethod:: LearningProfile.supports_objective_requisite_assignment

   .. automethod:: LearningProfile.supports_activity_lookup

   .. automethod:: LearningProfile.supports_activity_query

   .. automethod:: LearningProfile.supports_activity_search

   .. automethod:: LearningProfile.supports_activity_admin

   .. automethod:: LearningProfile.supports_activity_notification

   .. automethod:: LearningProfile.supports_activity_objective_bank

   .. automethod:: LearningProfile.supports_activity_objective_bank_assignment

   .. automethod:: LearningProfile.supports_activity_smart_objective_bank

   .. automethod:: LearningProfile.supports_proficiency_lookup

   .. automethod:: LearningProfile.supports_proficiency_query

   .. automethod:: LearningProfile.supports_proficiency_search

   .. automethod:: LearningProfile.supports_proficiency_admin

   .. automethod:: LearningProfile.supports_proficiency_notification

   .. automethod:: LearningProfile.supports_proficiency_objective_bank

   .. automethod:: LearningProfile.supports_proficiency_objective_bank_assignment

   .. automethod:: LearningProfile.supports_proficiency_smart_objective_bank

   .. automethod:: LearningProfile.supports_my_learning_path

   .. automethod:: LearningProfile.supports_learning_path

   .. automethod:: LearningProfile.supports_objective_bank_lookup

   .. automethod:: LearningProfile.supports_objective_bank_query

   .. automethod:: LearningProfile.supports_objective_bank_search

   .. automethod:: LearningProfile.supports_objective_bank_admin

   .. automethod:: LearningProfile.supports_objective_bank_notification

   .. automethod:: LearningProfile.supports_objective_bank_hierarchy

   .. automethod:: LearningProfile.supports_objective_bank_hierarchy_design

   .. automethod:: LearningProfile.supports_learning_batch

   .. autoattribute:: LearningProfile.objective_record_types

   .. automethod:: LearningProfile.supports_objective_record_type

   .. autoattribute:: LearningProfile.objective_search_record_types

   .. automethod:: LearningProfile.supports_objective_search_record_type

   .. autoattribute:: LearningProfile.activity_record_types

   .. automethod:: LearningProfile.supports_activity_record_type

   .. autoattribute:: LearningProfile.activity_search_record_types

   .. automethod:: LearningProfile.supports_activity_search_record_type

   .. autoattribute:: LearningProfile.proficiency_record_types

   .. automethod:: LearningProfile.supports_proficiency_record_type

   .. autoattribute:: LearningProfile.proficiency_search_record_types

   .. automethod:: LearningProfile.supports_proficiency_search_record_type

   .. autoattribute:: LearningProfile.objective_bank_record_types

   .. automethod:: LearningProfile.supports_objective_bank_record_type

   .. autoattribute:: LearningProfile.objective_bank_search_record_types

   .. automethod:: LearningProfile.supports_objective_bank_search_record_type

Learning Manager
----------------

.. autoclass:: LearningManager
   :show-inheritance:

   .. autoattribute:: LearningManager.objective_lookup_session

   .. automethod:: LearningManager.get_objective_lookup_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_query_session

   .. automethod:: LearningManager.get_objective_query_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_search_session

   .. automethod:: LearningManager.get_objective_search_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_admin_session

   .. automethod:: LearningManager.get_objective_admin_session_for_objective_bank

   .. automethod:: LearningManager.get_objective_notification_session

   .. automethod:: LearningManager.get_objective_notification_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_hierarchy_session

   .. automethod:: LearningManager.get_objective_hierarchy_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_hierarchy_design_session

   .. automethod:: LearningManager.get_objective_hierarchy_design_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_sequencing_session

   .. automethod:: LearningManager.get_objective_sequencing_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_objective_bank_session

   .. autoattribute:: LearningManager.objective_objective_bank_assignment_session

   .. automethod:: LearningManager.get_objective_smart_objective_bank_session

   .. autoattribute:: LearningManager.objective_requisite_session

   .. automethod:: LearningManager.get_objective_requisite_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_requisite_assignment_session

   .. automethod:: LearningManager.get_objective_requisite_assignment_session_for_objective_bank

   .. autoattribute:: LearningManager.activity_lookup_session

   .. automethod:: LearningManager.get_activity_lookup_session_for_objective_bank

   .. autoattribute:: LearningManager.activity_query_session

   .. automethod:: LearningManager.get_activity_query_session_for_objective_bank

   .. autoattribute:: LearningManager.activity_search_session

   .. automethod:: LearningManager.get_activity_search_session_for_objective_bank

   .. autoattribute:: LearningManager.activity_admin_session

   .. automethod:: LearningManager.get_activity_admin_session_for_objective_bank

   .. automethod:: LearningManager.get_activity_notification_session

   .. automethod:: LearningManager.get_activity_notification_session_for_objective_bank

   .. autoattribute:: LearningManager.activity_objective_bank_session

   .. autoattribute:: LearningManager.activity_objective_bank_assignment_session

   .. automethod:: LearningManager.get_activity_smart_objective_bank_session

   .. autoattribute:: LearningManager.proficiency_lookup_session

   .. automethod:: LearningManager.get_proficiency_lookup_session_for_objective_bank

   .. autoattribute:: LearningManager.proficiency_query_session

   .. automethod:: LearningManager.get_proficiency_query_session_for_objective_bank

   .. autoattribute:: LearningManager.proficiency_search_session

   .. automethod:: LearningManager.get_proficiency_search_session_for_objective_bank

   .. autoattribute:: LearningManager.proficiency_admin_session

   .. automethod:: LearningManager.get_proficiency_admin_session_for_objective_bank

   .. automethod:: LearningManager.get_proficiency_notification_session

   .. automethod:: LearningManager.get_proficiency_notification_session_for_objective_bank

   .. autoattribute:: LearningManager.proficiency_objective_bank_session

   .. autoattribute:: LearningManager.proficiency_objective_bank_assignment_session

   .. automethod:: LearningManager.get_proficiency_smart_objective_bank_session

   .. autoattribute:: LearningManager.my_learning_path_session

   .. automethod:: LearningManager.get_my_learning_path_session_for_objective_bank

   .. autoattribute:: LearningManager.learning_path_session

   .. automethod:: LearningManager.get_learning_path_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_bank_lookup_session

   .. autoattribute:: LearningManager.objective_bank_query_session

   .. autoattribute:: LearningManager.objective_bank_search_session

   .. autoattribute:: LearningManager.objective_bank_admin_session

   .. automethod:: LearningManager.get_objective_bank_notification_session

   .. autoattribute:: LearningManager.objective_bank_hierarchy_session

   .. autoattribute:: LearningManager.objective_bank_hierarchy_design_session

   .. autoattribute:: LearningManager.learning_batch_manager

Learning Proxy Manager
----------------------

.. autoclass:: LearningProxyManager
   :show-inheritance:

   .. automethod:: LearningProxyManager.get_objective_lookup_session

   .. automethod:: LearningProxyManager.get_objective_lookup_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_query_session

   .. automethod:: LearningProxyManager.get_objective_query_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_search_session

   .. automethod:: LearningProxyManager.get_objective_search_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_admin_session

   .. automethod:: LearningProxyManager.get_objective_admin_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_notification_session

   .. automethod:: LearningProxyManager.get_objective_notification_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_hierarchy_session

   .. automethod:: LearningProxyManager.get_objective_hierarchy_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_hierarchy_design_session

   .. automethod:: LearningProxyManager.get_objective_hierarchy_design_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_sequencing_session

   .. automethod:: LearningProxyManager.get_objective_sequencing_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_objective_bank_session

   .. automethod:: LearningProxyManager.get_objective_objective_bank_assignment_session

   .. automethod:: LearningProxyManager.get_objective_smart_objective_bank_session

   .. automethod:: LearningProxyManager.get_objective_requisite_session

   .. automethod:: LearningProxyManager.get_objective_requisite_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_requisite_assignment_session

   .. automethod:: LearningProxyManager.get_objective_requisite_assignment_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_activity_lookup_session

   .. automethod:: LearningProxyManager.get_activity_lookup_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_activity_query_session

   .. automethod:: LearningProxyManager.get_activity_query_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_activity_search_session

   .. automethod:: LearningProxyManager.get_activity_search_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_activity_admin_session

   .. automethod:: LearningProxyManager.get_activity_admin_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_activity_notification_session

   .. automethod:: LearningProxyManager.get_activity_notification_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_activity_objective_bank_session

   .. automethod:: LearningProxyManager.get_activity_objective_bank_assignment_session

   .. automethod:: LearningProxyManager.get_activity_smart_objective_bank_session

   .. automethod:: LearningProxyManager.get_proficiency_lookup_session

   .. automethod:: LearningProxyManager.get_proficiency_lookup_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_proficiency_query_session

   .. automethod:: LearningProxyManager.get_proficiency_query_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_proficiency_search_session

   .. automethod:: LearningProxyManager.get_proficiency_search_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_proficiency_admin_session

   .. automethod:: LearningProxyManager.get_proficiency_admin_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_proficiency_notification_session

   .. automethod:: LearningProxyManager.get_proficiency_notification_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_proficiency_objective_bank_session

   .. automethod:: LearningProxyManager.get_proficiency_objective_bank_assignment_session

   .. automethod:: LearningProxyManager.get_proficiency_smart_objective_bank_session

   .. automethod:: LearningProxyManager.get_my_learning_path_session

   .. automethod:: LearningProxyManager.get_my_learning_path_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_learning_path_session

   .. automethod:: LearningProxyManager.get_learning_path_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_bank_lookup_session

   .. automethod:: LearningProxyManager.get_objective_bank_query_session

   .. automethod:: LearningProxyManager.get_objective_bank_search_session

   .. automethod:: LearningProxyManager.get_objective_bank_admin_session

   .. automethod:: LearningProxyManager.get_objective_bank_notification_session

   .. automethod:: LearningProxyManager.get_objective_bank_hierarchy_session

   .. automethod:: LearningProxyManager.get_objective_bank_hierarchy_design_session

   .. autoattribute:: LearningProxyManager.learning_batch_proxy_manager

