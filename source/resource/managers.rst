

Managers
========


Resource Profile
----------------

.. py:class:: ResourceProfile(osid_managers.OsidProfile, resource_managers.ResourceProfile)
    The resource profile describes interoperability among resource services.

    .. py:method:: supports_visible_federation():
        :noindex:


    .. py:method:: supports_resource_lookup():
        :noindex:


    .. py:method:: supports_resource_query():
        :noindex:


    .. py:method:: supports_resource_search():
        :noindex:


    .. py:method:: supports_resource_admin():
        :noindex:


    .. py:method:: supports_resource_notification():
        :noindex:


    .. py:method:: supports_resource_bin():
        :noindex:


    .. py:method:: supports_resource_bin_assignment():
        :noindex:


    .. py:method:: supports_resource_smart_bin():
        :noindex:


    .. py:method:: supports_membership():
        :noindex:


    .. py:method:: supports_group():
        :noindex:


    .. py:method:: supports_group_assignment():
        :noindex:


    .. py:method:: supports_group_notification():
        :noindex:


    .. py:method:: supports_group_hierarchy():
        :noindex:


    .. py:method:: supports_resource_agent():
        :noindex:


    .. py:method:: supports_resource_agent_assignment():
        :noindex:


    .. py:method:: supports_resource_relationship_lookup():
        :noindex:


    .. py:method:: supports_resource_relationship_query():
        :noindex:


    .. py:method:: supports_resource_relationship_search():
        :noindex:


    .. py:method:: supports_resource_relationship_admin():
        :noindex:


    .. py:method:: supports_resource_relationship_notification():
        :noindex:


    .. py:method:: supports_resource_relationship_bin():
        :noindex:


    .. py:method:: supports_resource_relationship_bin_assignment():
        :noindex:


    .. py:method:: supports_resource_relationship_smart_bin():
        :noindex:


    .. py:method:: supports_bin_lookup():
        :noindex:


    .. py:method:: supports_bin_query():
        :noindex:


    .. py:method:: supports_bin_search():
        :noindex:


    .. py:method:: supports_bin_admin():
        :noindex:


    .. py:method:: supports_bin_notification():
        :noindex:


    .. py:method:: supports_bin_hierarchy():
        :noindex:


    .. py:method:: supports_bin_hierarchy_design():
        :noindex:


    .. py:method:: supports_resource_batch():
        :noindex:


    .. py:method:: supports_resource_demographic():
        :noindex:


    .. py:method:: get_resource_record_types():
        :noindex:


    .. py:attribute:: resource_record_types
        :noindex:


    .. py:method:: supports_resource_record_type(resource_record_type):
        :noindex:


    .. py:method:: get_resource_search_record_types():
        :noindex:


    .. py:attribute:: resource_search_record_types
        :noindex:


    .. py:method:: supports_resource_search_record_type(resource_search_record_type):
        :noindex:


    .. py:method:: get_resource_relationship_record_types():
        :noindex:


    .. py:attribute:: resource_relationship_record_types
        :noindex:


    .. py:method:: supports_resource_relationship_record_type(resource_relationship_record_type):
        :noindex:


    .. py:method:: get_resource_relationship_search_record_types():
        :noindex:


    .. py:attribute:: resource_relationship_search_record_types
        :noindex:


    .. py:method:: supports_resource_relationship_search_record_type(resource_relationship_search_record_type):
        :noindex:


    .. py:method:: get_bin_record_types():
        :noindex:


    .. py:attribute:: bin_record_types
        :noindex:


    .. py:method:: supports_bin_record_type(bin_record_type):
        :noindex:


    .. py:method:: get_bin_search_record_types():
        :noindex:


    .. py:attribute:: bin_search_record_types
        :noindex:


    .. py:method:: supports_bin_search_record_type(bin_search_record_type):
        :noindex:


Resource Manager
----------------

.. py:class:: ResourceManager(osid_managers.OsidManager, ResourceProfile, resource_managers.ResourceManager)
        :noindex:

    .. py:method:: get_resource_lookup_session():
        :noindex:


    .. py:attribute:: resource_lookup_session
        :noindex:


    .. py:method:: get_resource_lookup_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_query_session():
        :noindex:


    .. py:attribute:: resource_query_session
        :noindex:


    .. py:method:: get_resource_query_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_search_session():
        :noindex:


    .. py:attribute:: resource_search_session
        :noindex:


    .. py:method:: get_resource_search_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_admin_session():
        :noindex:


    .. py:attribute:: resource_admin_session
        :noindex:


    .. py:method:: get_resource_admin_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_notification_session(resource_receiver):
        :noindex:


    .. py:method:: get_resource_notification_session_for_bin(resource_receiver, bin_id):
        :noindex:


    .. py:method:: get_resource_bin_session():
        :noindex:


    .. py:attribute:: resource_bin_session
        :noindex:


    .. py:method:: get_resource_bin_assignment_session():
        :noindex:


    .. py:attribute:: resource_bin_assignment_session
        :noindex:


    .. py:method:: get_resource_smart_bin_session(bin_id):
        :noindex:


    .. py:method:: get_membership_session():
        :noindex:


    .. py:attribute:: membership_session
        :noindex:


    .. py:method:: get_membership_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_group_session():
        :noindex:


    .. py:attribute:: group_session
        :noindex:


    .. py:method:: get_group_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_group_assignment_session():
        :noindex:


    .. py:attribute:: group_assignment_session
        :noindex:


    .. py:method:: get_group_assignment_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_group_notification_session(group_rceeiver):
        :noindex:


    .. py:method:: get_group_notification_session_for_bin(group_rceeiver, bin_id):
        :noindex:


    .. py:method:: get_group_hierarchy_session():
        :noindex:


    .. py:attribute:: group_hierarchy_session
        :noindex:


    .. py:method:: get_group_hierarchy_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_agent_session():
        :noindex:


    .. py:attribute:: resource_agent_session
        :noindex:


    .. py:method:: get_resource_agent_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_agent_assignment_session():
        :noindex:


    .. py:attribute:: resource_agent_assignment_session
        :noindex:


    .. py:method:: get_resource_agent_assignment_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_relationship_lookup_session():
        :noindex:


    .. py:attribute:: resource_relationship_lookup_session
        :noindex:


    .. py:method:: get_resource_relationship_lookup_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_relationship_query_session():
        :noindex:


    .. py:attribute:: resource_relationship_query_session
        :noindex:


    .. py:method:: get_resource_relationship_query_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_relationship_search_session():
        :noindex:


    .. py:attribute:: resource_relationship_search_session
        :noindex:


    .. py:method:: get_resource_relationship_search_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_relationship_admin_session():
        :noindex:


    .. py:attribute:: resource_relationship_admin_session
        :noindex:


    .. py:method:: get_resource_relationship_admin_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_relationship_notification_session(resource_relationship_receiver):
        :noindex:


    .. py:method:: get_resource_relationship_notification_session_for_bin(resource_relationship_receiver, bin_id):
        :noindex:


    .. py:method:: get_resource_relationship_bin_session():
        :noindex:


    .. py:attribute:: resource_relationship_bin_session
        :noindex:


    .. py:method:: get_resource_relationship_bin_assignment_session():
        :noindex:


    .. py:attribute:: resource_relationship_bin_assignment_session
        :noindex:


    .. py:method:: get_resource_relationship_smart_bin_session(bin_id):
        :noindex:


    .. py:method:: get_bin_lookup_session():
        :noindex:


    .. py:attribute:: bin_lookup_session
        :noindex:


    .. py:method:: get_bin_query_session():
        :noindex:


    .. py:attribute:: bin_query_session
        :noindex:


    .. py:method:: get_bin_search_session():
        :noindex:


    .. py:attribute:: bin_search_session
        :noindex:


    .. py:method:: get_bin_admin_session():
        :noindex:


    .. py:attribute:: bin_admin_session
        :noindex:


    .. py:method:: get_bin_notification_session(bin_receiver):
        :noindex:


    .. py:method:: get_bin_hierarchy_session():
        :noindex:


    .. py:attribute:: bin_hierarchy_session
        :noindex:


    .. py:method:: get_bin_hierarchy_design_session():
        :noindex:


    .. py:attribute:: bin_hierarchy_design_session
        :noindex:


    .. py:method:: get_resource_batch_manager():
        :noindex:


    .. py:attribute:: resource_batch_manager
        :noindex:


    .. py:method:: get_resource_demographic_manager():
        :noindex:


    .. py:attribute:: resource_demographic_manager
        :noindex:


Resource Proxy Manager
----------------------

.. py:class:: ResourceProxyManager(osid_managers.OsidProxyManager, ResourceProfile, resource_managers.ResourceProxyManager)
        :noindex:

    .. py:method:: get_resource_lookup_session(proxy):
        :noindex:


    .. py:method:: get_resource_lookup_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_query_session(proxy):
        :noindex:


    .. py:method:: get_resource_query_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_search_session(proxy):
        :noindex:


    .. py:method:: get_resource_search_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_admin_session(proxy):
        :noindex:


    .. py:method:: get_resource_admin_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_notification_session(resource_receiver, proxy):
        :noindex:


    .. py:method:: get_resource_notification_session_for_bin(resource_receiver, bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_bin_session(proxy):
        :noindex:


    .. py:method:: get_resource_bin_assignment_session(proxy):
        :noindex:


    .. py:method:: get_resource_smart_bin_session(bin_id, proxy):
        :noindex:


    .. py:method:: get_membership_session(proxy):
        :noindex:


    .. py:method:: get_membership_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_group_session(proxy):
        :noindex:


    .. py:method:: get_group_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_group_assignment_session(proxy):
        :noindex:


    .. py:method:: get_group_assignment_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_group_notification_session(group_rceeiver, proxy):
        :noindex:


    .. py:method:: get_group_notification_session_for_bin(group_rceeiver, bin_id, proxy):
        :noindex:


    .. py:method:: get_group_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_group_hierarchy_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_agent_session(proxy):
        :noindex:


    .. py:method:: get_resource_agent_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_agent_assignment_session(proxy):
        :noindex:


    .. py:method:: get_resource_agent_assignment_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_relationship_lookup_session(proxy):
        :noindex:


    .. py:method:: get_resource_relationship_lookup_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_relationship_query_session(proxy):
        :noindex:


    .. py:method:: get_resource_relationship_query_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_relationship_search_session(proxy):
        :noindex:


    .. py:method:: get_resource_relationship_search_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_relationship_admin_session(proxy):
        :noindex:


    .. py:method:: get_resource_relationship_admin_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_relationship_notification_session(resource_relationship_receiver, proxy):
        :noindex:


    .. py:method:: get_resource_relationship_notification_session_for_bin(resource_relationship_receiver, bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_relationship_bin_session(proxy):
        :noindex:


    .. py:method:: get_resource_relationship_bin_assignment_session(proxy):
        :noindex:


    .. py:method:: get_resource_relationship_smart_bin_session(bin_id, proxy):
        :noindex:


    .. py:method:: get_bin_lookup_session(proxy):
        :noindex:


    .. py:method:: get_bin_query_session(proxy):
        :noindex:


    .. py:method:: get_bin_search_session(proxy):
        :noindex:


    .. py:method:: get_bin_admin_session(proxy):
        :noindex:


    .. py:method:: get_bin_notification_session(bin_receiver, proxy):
        :noindex:


    .. py:method:: get_bin_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_bin_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_resource_batch_proxy_manager():
        :noindex:


    .. py:attribute:: resource_batch_proxy_manager
        :noindex:


    .. py:method:: get_resource_demographic_proxy_manager():
        :noindex:


    .. py:attribute:: resource_demographic_proxy_manager
        :noindex:


