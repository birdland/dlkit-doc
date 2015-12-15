

Managers
========


Learning Profile
----------------

.. py:class:: LearningProfile(osid_managers.OsidProfile, learning_managers.LearningProfile)
    The ``LearningProfile`` describes the interoperability among learning services.

    .. py:method:: supports_visible_federation():
        :noindex:


    .. py:method:: supports_objective_lookup():
        :noindex:


    .. py:method:: supports_objective_query():
        :noindex:


    .. py:method:: supports_objective_search():
        :noindex:


    .. py:method:: supports_objective_admin():
        :noindex:


    .. py:method:: supports_objective_notification():
        :noindex:


    .. py:method:: supports_objective_hierarchy():
        :noindex:


    .. py:method:: supports_objective_hierarchy_design():
        :noindex:


    .. py:method:: supports_objective_sequencing():
        :noindex:


    .. py:method:: supports_objective_objective_bank():
        :noindex:


    .. py:method:: supports_objective_objective_bank_assignment():
        :noindex:


    .. py:method:: supports_objective_smart_objective_bank():
        :noindex:


    .. py:method:: supports_objective_requisite():
        :noindex:


    .. py:method:: supports_objective_requisite_assignment():
        :noindex:


    .. py:method:: supports_activity_lookup():
        :noindex:


    .. py:method:: supports_activity_query():
        :noindex:


    .. py:method:: supports_activity_search():
        :noindex:


    .. py:method:: supports_activity_admin():
        :noindex:


    .. py:method:: supports_activity_notification():
        :noindex:


    .. py:method:: supports_activity_objective_bank():
        :noindex:


    .. py:method:: supports_activity_objective_bank_assignment():
        :noindex:


    .. py:method:: supports_activity_smart_objective_bank():
        :noindex:


    .. py:method:: supports_proficiency_lookup():
        :noindex:


    .. py:method:: supports_proficiency_query():
        :noindex:


    .. py:method:: supports_proficiency_search():
        :noindex:


    .. py:method:: supports_proficiency_admin():
        :noindex:


    .. py:method:: supports_proficiency_notification():
        :noindex:


    .. py:method:: supports_proficiency_objective_bank():
        :noindex:


    .. py:method:: supports_proficiency_objective_bank_assignment():
        :noindex:


    .. py:method:: supports_proficiency_smart_objective_bank():
        :noindex:


    .. py:method:: supports_my_learning_path():
        :noindex:


    .. py:method:: supports_learning_path():
        :noindex:


    .. py:method:: supports_objective_bank_lookup():
        :noindex:


    .. py:method:: supports_objective_bank_query():
        :noindex:


    .. py:method:: supports_objective_bank_search():
        :noindex:


    .. py:method:: supports_objective_bank_admin():
        :noindex:


    .. py:method:: supports_objective_bank_notification():
        :noindex:


    .. py:method:: supports_objective_bank_hierarchy():
        :noindex:


    .. py:method:: supports_objective_bank_hierarchy_design():
        :noindex:


    .. py:method:: supports_learning_batch():
        :noindex:


    .. py:method:: get_objective_record_types():
        :noindex:


    .. py:attribute:: objective_record_types
        :noindex:


    .. py:method:: supports_objective_record_type(objective_record_type):
        :noindex:


    .. py:method:: get_objective_search_record_types():
        :noindex:


    .. py:attribute:: objective_search_record_types
        :noindex:


    .. py:method:: supports_objective_search_record_type(objective_search_record_type):
        :noindex:


    .. py:method:: get_activity_record_types():
        :noindex:


    .. py:attribute:: activity_record_types
        :noindex:


    .. py:method:: supports_activity_record_type(activity_record_type):
        :noindex:


    .. py:method:: get_activity_search_record_types():
        :noindex:


    .. py:attribute:: activity_search_record_types
        :noindex:


    .. py:method:: supports_activity_search_record_type(activity_search_record_type):
        :noindex:


    .. py:method:: get_proficiency_record_types():
        :noindex:


    .. py:attribute:: proficiency_record_types
        :noindex:


    .. py:method:: supports_proficiency_record_type(proficiency_record_type):
        :noindex:


    .. py:method:: get_proficiency_search_record_types():
        :noindex:


    .. py:attribute:: proficiency_search_record_types
        :noindex:


    .. py:method:: supports_proficiency_search_record_type(proficiency_search_record_type):
        :noindex:


    .. py:method:: get_objective_bank_record_types():
        :noindex:


    .. py:attribute:: objective_bank_record_types
        :noindex:


    .. py:method:: supports_objective_bank_record_type(objective_bank_record_type):
        :noindex:


    .. py:method:: get_objective_bank_search_record_types():
        :noindex:


    .. py:attribute:: objective_bank_search_record_types
        :noindex:


    .. py:method:: supports_objective_bank_search_record_type(objective_bank_search_record_type):
        :noindex:


Learning Manager
----------------

.. py:class:: LearningManager(osid_managers.OsidManager, LearningProfile, learning_managers.LearningManager)
        :noindex:

    .. py:method:: get_objective_lookup_session():
        :noindex:


    .. py:attribute:: objective_lookup_session
        :noindex:


    .. py:method:: get_objective_lookup_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_query_session():
        :noindex:


    .. py:attribute:: objective_query_session
        :noindex:


    .. py:method:: get_objective_query_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_search_session():
        :noindex:


    .. py:attribute:: objective_search_session
        :noindex:


    .. py:method:: get_objective_search_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_admin_session():
        :noindex:


    .. py:attribute:: objective_admin_session
        :noindex:


    .. py:method:: get_objective_admin_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_notification_session(objective_receiver):
        :noindex:


    .. py:method:: get_objective_notification_session_for_objective_bank(objective_receiver, objective_bank_id):
        :noindex:


    .. py:method:: get_objective_hierarchy_session():
        :noindex:


    .. py:attribute:: objective_hierarchy_session
        :noindex:


    .. py:method:: get_objective_hierarchy_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_hierarchy_design_session():
        :noindex:


    .. py:attribute:: objective_hierarchy_design_session
        :noindex:


    .. py:method:: get_objective_hierarchy_design_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_sequencing_session():
        :noindex:


    .. py:attribute:: objective_sequencing_session
        :noindex:


    .. py:method:: get_objective_sequencing_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_objective_bank_session():
        :noindex:


    .. py:attribute:: objective_objective_bank_session
        :noindex:


    .. py:method:: get_objective_objective_bank_assignment_session():
        :noindex:


    .. py:attribute:: objective_objective_bank_assignment_session
        :noindex:


    .. py:method:: get_objective_smart_objective_bank_session(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_requisite_session():
        :noindex:


    .. py:attribute:: objective_requisite_session
        :noindex:


    .. py:method:: get_objective_requisite_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_requisite_assignment_session():
        :noindex:


    .. py:attribute:: objective_requisite_assignment_session
        :noindex:


    .. py:method:: get_objective_requisite_assignment_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_activity_lookup_session():
        :noindex:


    .. py:attribute:: activity_lookup_session
        :noindex:


    .. py:method:: get_activity_lookup_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_activity_query_session():
        :noindex:


    .. py:attribute:: activity_query_session
        :noindex:


    .. py:method:: get_activity_query_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_activity_search_session():
        :noindex:


    .. py:attribute:: activity_search_session
        :noindex:


    .. py:method:: get_activity_search_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_activity_admin_session():
        :noindex:


    .. py:attribute:: activity_admin_session
        :noindex:


    .. py:method:: get_activity_admin_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_activity_notification_session(activity_receiver):
        :noindex:


    .. py:method:: get_activity_notification_session_for_objective_bank(activity_receiver, objective_bank_id):
        :noindex:


    .. py:method:: get_activity_objective_bank_session():
        :noindex:


    .. py:attribute:: activity_objective_bank_session
        :noindex:


    .. py:method:: get_activity_objective_bank_assignment_session():
        :noindex:


    .. py:attribute:: activity_objective_bank_assignment_session
        :noindex:


    .. py:method:: get_activity_smart_objective_bank_session(objective_bank_id):
        :noindex:


    .. py:method:: get_proficiency_lookup_session():
        :noindex:


    .. py:attribute:: proficiency_lookup_session
        :noindex:


    .. py:method:: get_proficiency_lookup_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_proficiency_query_session():
        :noindex:


    .. py:attribute:: proficiency_query_session
        :noindex:


    .. py:method:: get_proficiency_query_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_proficiency_search_session():
        :noindex:


    .. py:attribute:: proficiency_search_session
        :noindex:


    .. py:method:: get_proficiency_search_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_proficiency_admin_session():
        :noindex:


    .. py:attribute:: proficiency_admin_session
        :noindex:


    .. py:method:: get_proficiency_admin_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_proficiency_notification_session(proficiency_receiver):
        :noindex:


    .. py:method:: get_proficiency_notification_session_for_objective_bank(proficiency_receiver, objective_bank_id):
        :noindex:


    .. py:method:: get_proficiency_objective_bank_session():
        :noindex:


    .. py:attribute:: proficiency_objective_bank_session
        :noindex:


    .. py:method:: get_proficiency_objective_bank_assignment_session():
        :noindex:


    .. py:attribute:: proficiency_objective_bank_assignment_session
        :noindex:


    .. py:method:: get_proficiency_smart_objective_bank_session(objective_bank_id):
        :noindex:


    .. py:method:: get_my_learning_path_session():
        :noindex:


    .. py:attribute:: my_learning_path_session
        :noindex:


    .. py:method:: get_my_learning_path_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_learning_path_session():
        :noindex:


    .. py:attribute:: learning_path_session
        :noindex:


    .. py:method:: get_learning_path_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_bank_lookup_session():
        :noindex:


    .. py:attribute:: objective_bank_lookup_session
        :noindex:


    .. py:method:: get_objective_bank_query_session():
        :noindex:


    .. py:attribute:: objective_bank_query_session
        :noindex:


    .. py:method:: get_objective_bank_search_session():
        :noindex:


    .. py:attribute:: objective_bank_search_session
        :noindex:


    .. py:method:: get_objective_bank_admin_session():
        :noindex:


    .. py:attribute:: objective_bank_admin_session
        :noindex:


    .. py:method:: get_objective_bank_notification_session(objective_bank_receiver):
        :noindex:


    .. py:method:: get_objective_bank_hierarchy_session():
        :noindex:


    .. py:attribute:: objective_bank_hierarchy_session
        :noindex:


    .. py:method:: get_objective_bank_hierarchy_design_session():
        :noindex:


    .. py:attribute:: objective_bank_hierarchy_design_session
        :noindex:


    .. py:method:: get_learning_batch_manager():
        :noindex:


    .. py:attribute:: learning_batch_manager
        :noindex:


Learning Proxy Manager
----------------------

.. py:class:: LearningProxyManager(osid_managers.OsidProxyManager, LearningProfile, learning_managers.LearningProxyManager)
        :noindex:

    .. py:method:: get_objective_lookup_session(proxy):
        :noindex:


    .. py:method:: get_objective_lookup_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_query_session(proxy):
        :noindex:


    .. py:method:: get_objective_query_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_search_session(proxy):
        :noindex:


    .. py:method:: get_objective_search_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_admin_session(proxy):
        :noindex:


    .. py:method:: get_objective_admin_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_notification_session(objective_receiver, proxy):
        :noindex:


    .. py:method:: get_objective_notification_session_for_objective_bank(objective_receiver, objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_objective_hierarchy_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_objective_hierarchy_design_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_sequencing_session(proxy):
        :noindex:


    .. py:method:: get_objective_sequencing_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_objective_bank_session(proxy):
        :noindex:


    .. py:method:: get_objective_objective_bank_assignment_session(proxy):
        :noindex:


    .. py:method:: get_objective_smart_objective_bank_session(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_requisite_session(proxy):
        :noindex:


    .. py:method:: get_objective_requisite_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_requisite_assignment_session(proxy):
        :noindex:


    .. py:method:: get_objective_requisite_assignment_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_activity_lookup_session(proxy):
        :noindex:


    .. py:method:: get_activity_lookup_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_activity_query_session(proxy):
        :noindex:


    .. py:method:: get_activity_query_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_activity_search_session(proxy):
        :noindex:


    .. py:method:: get_activity_search_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_activity_admin_session(proxy):
        :noindex:


    .. py:method:: get_activity_admin_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_activity_notification_session(activity_receiver, proxy):
        :noindex:


    .. py:method:: get_activity_notification_session_for_objective_bank(activity_receiver, objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_activity_objective_bank_session(proxy):
        :noindex:


    .. py:method:: get_activity_objective_bank_assignment_session(proxy):
        :noindex:


    .. py:method:: get_activity_smart_objective_bank_session(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_proficiency_lookup_session(proxy):
        :noindex:


    .. py:method:: get_proficiency_lookup_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_proficiency_query_session(proxy):
        :noindex:


    .. py:method:: get_proficiency_query_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_proficiency_search_session(proxy):
        :noindex:


    .. py:method:: get_proficiency_search_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_proficiency_admin_session(proxy):
        :noindex:


    .. py:method:: get_proficiency_admin_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_proficiency_notification_session(proficiency_receiver, proxy):
        :noindex:


    .. py:method:: get_proficiency_notification_session_for_objective_bank(proficiency_receiver, objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_proficiency_objective_bank_session(proxy):
        :noindex:


    .. py:method:: get_proficiency_objective_bank_assignment_session(proxy):
        :noindex:


    .. py:method:: get_proficiency_smart_objective_bank_session(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_my_learning_path_session(proxy):
        :noindex:


    .. py:method:: get_my_learning_path_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_learning_path_session(proxy):
        :noindex:


    .. py:method:: get_learning_path_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_bank_lookup_session(proxy):
        :noindex:


    .. py:method:: get_objective_bank_query_session(proxy):
        :noindex:


    .. py:method:: get_objective_bank_search_session(proxy):
        :noindex:


    .. py:method:: get_objective_bank_admin_session(proxy):
        :noindex:


    .. py:method:: get_objective_bank_notification_session(objective_bank_receiver, proxy):
        :noindex:


    .. py:method:: get_objective_bank_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_objective_bank_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_learning_batch_proxy_manager():
        :noindex:


    .. py:attribute:: learning_batch_proxy_manager
        :noindex:


