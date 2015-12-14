
.. currentmodule:: dlkit.resource.managers
.. automodule:: dlkit.resource.managers

Managers
========


Resource Profile
----------------

.. autoclass:: ResourceProfile
   :show-inheritance:

   .. automethod:: ResourceProfile.supports_visible_federation

   .. automethod:: ResourceProfile.supports_resource_lookup

   .. automethod:: ResourceProfile.supports_resource_query

   .. automethod:: ResourceProfile.supports_resource_search

   .. automethod:: ResourceProfile.supports_resource_admin

   .. automethod:: ResourceProfile.supports_resource_notification

   .. automethod:: ResourceProfile.supports_resource_bin

   .. automethod:: ResourceProfile.supports_resource_bin_assignment

   .. automethod:: ResourceProfile.supports_resource_smart_bin

   .. automethod:: ResourceProfile.supports_membership

   .. automethod:: ResourceProfile.supports_group

   .. automethod:: ResourceProfile.supports_group_assignment

   .. automethod:: ResourceProfile.supports_group_notification

   .. automethod:: ResourceProfile.supports_group_hierarchy

   .. automethod:: ResourceProfile.supports_resource_agent

   .. automethod:: ResourceProfile.supports_resource_agent_assignment

   .. automethod:: ResourceProfile.supports_resource_relationship_lookup

   .. automethod:: ResourceProfile.supports_resource_relationship_query

   .. automethod:: ResourceProfile.supports_resource_relationship_search

   .. automethod:: ResourceProfile.supports_resource_relationship_admin

   .. automethod:: ResourceProfile.supports_resource_relationship_notification

   .. automethod:: ResourceProfile.supports_resource_relationship_bin

   .. automethod:: ResourceProfile.supports_resource_relationship_bin_assignment

   .. automethod:: ResourceProfile.supports_resource_relationship_smart_bin

   .. automethod:: ResourceProfile.supports_bin_lookup

   .. automethod:: ResourceProfile.supports_bin_query

   .. automethod:: ResourceProfile.supports_bin_search

   .. automethod:: ResourceProfile.supports_bin_admin

   .. automethod:: ResourceProfile.supports_bin_notification

   .. automethod:: ResourceProfile.supports_bin_hierarchy

   .. automethod:: ResourceProfile.supports_bin_hierarchy_design

   .. automethod:: ResourceProfile.supports_resource_batch

   .. automethod:: ResourceProfile.supports_resource_demographic

   .. autoattribute:: ResourceProfile.resource_record_types

   .. automethod:: ResourceProfile.supports_resource_record_type

   .. autoattribute:: ResourceProfile.resource_search_record_types

   .. automethod:: ResourceProfile.supports_resource_search_record_type

   .. autoattribute:: ResourceProfile.resource_relationship_record_types

   .. automethod:: ResourceProfile.supports_resource_relationship_record_type

   .. autoattribute:: ResourceProfile.resource_relationship_search_record_types

   .. automethod:: ResourceProfile.supports_resource_relationship_search_record_type

   .. autoattribute:: ResourceProfile.bin_record_types

   .. automethod:: ResourceProfile.supports_bin_record_type

   .. autoattribute:: ResourceProfile.bin_search_record_types

   .. automethod:: ResourceProfile.supports_bin_search_record_type

Resource Manager
----------------

.. autoclass:: ResourceManager
   :show-inheritance:

   .. autoattribute:: ResourceManager.resource_lookup_session

   .. automethod:: ResourceManager.get_resource_lookup_session_for_bin

   .. autoattribute:: ResourceManager.resource_query_session

   .. automethod:: ResourceManager.get_resource_query_session_for_bin

   .. autoattribute:: ResourceManager.resource_search_session

   .. automethod:: ResourceManager.get_resource_search_session_for_bin

   .. autoattribute:: ResourceManager.resource_admin_session

   .. automethod:: ResourceManager.get_resource_admin_session_for_bin

   .. automethod:: ResourceManager.get_resource_notification_session

   .. automethod:: ResourceManager.get_resource_notification_session_for_bin

   .. autoattribute:: ResourceManager.resource_bin_session

   .. autoattribute:: ResourceManager.resource_bin_assignment_session

   .. automethod:: ResourceManager.get_resource_smart_bin_session

   .. autoattribute:: ResourceManager.membership_session

   .. automethod:: ResourceManager.get_membership_session_for_bin

   .. autoattribute:: ResourceManager.group_session

   .. automethod:: ResourceManager.get_group_session_for_bin

   .. autoattribute:: ResourceManager.group_assignment_session

   .. automethod:: ResourceManager.get_group_assignment_session_for_bin

   .. automethod:: ResourceManager.get_group_notification_session

   .. automethod:: ResourceManager.get_group_notification_session_for_bin

   .. autoattribute:: ResourceManager.group_hierarchy_session

   .. automethod:: ResourceManager.get_group_hierarchy_session_for_bin

   .. autoattribute:: ResourceManager.resource_agent_session

   .. automethod:: ResourceManager.get_resource_agent_session_for_bin

   .. autoattribute:: ResourceManager.resource_agent_assignment_session

   .. automethod:: ResourceManager.get_resource_agent_assignment_session_for_bin

   .. autoattribute:: ResourceManager.resource_relationship_lookup_session

   .. automethod:: ResourceManager.get_resource_relationship_lookup_session_for_bin

   .. autoattribute:: ResourceManager.resource_relationship_query_session

   .. automethod:: ResourceManager.get_resource_relationship_query_session_for_bin

   .. autoattribute:: ResourceManager.resource_relationship_search_session

   .. automethod:: ResourceManager.get_resource_relationship_search_session_for_bin

   .. autoattribute:: ResourceManager.resource_relationship_admin_session

   .. automethod:: ResourceManager.get_resource_relationship_admin_session_for_bin

   .. automethod:: ResourceManager.get_resource_relationship_notification_session

   .. automethod:: ResourceManager.get_resource_relationship_notification_session_for_bin

   .. autoattribute:: ResourceManager.resource_relationship_bin_session

   .. autoattribute:: ResourceManager.resource_relationship_bin_assignment_session

   .. automethod:: ResourceManager.get_resource_relationship_smart_bin_session

   .. autoattribute:: ResourceManager.bin_lookup_session

   .. autoattribute:: ResourceManager.bin_query_session

   .. autoattribute:: ResourceManager.bin_search_session

   .. autoattribute:: ResourceManager.bin_admin_session

   .. automethod:: ResourceManager.get_bin_notification_session

   .. autoattribute:: ResourceManager.bin_hierarchy_session

   .. autoattribute:: ResourceManager.bin_hierarchy_design_session

   .. autoattribute:: ResourceManager.resource_batch_manager

   .. autoattribute:: ResourceManager.resource_demographic_manager

Resource Proxy Manager
----------------------

.. autoclass:: ResourceProxyManager
   :show-inheritance:

   .. automethod:: ResourceProxyManager.get_resource_lookup_session

   .. automethod:: ResourceProxyManager.get_resource_lookup_session_for_bin

   .. automethod:: ResourceProxyManager.get_resource_query_session

   .. automethod:: ResourceProxyManager.get_resource_query_session_for_bin

   .. automethod:: ResourceProxyManager.get_resource_search_session

   .. automethod:: ResourceProxyManager.get_resource_search_session_for_bin

   .. automethod:: ResourceProxyManager.get_resource_admin_session

   .. automethod:: ResourceProxyManager.get_resource_admin_session_for_bin

   .. automethod:: ResourceProxyManager.get_resource_notification_session

   .. automethod:: ResourceProxyManager.get_resource_notification_session_for_bin

   .. automethod:: ResourceProxyManager.get_resource_bin_session

   .. automethod:: ResourceProxyManager.get_resource_bin_assignment_session

   .. automethod:: ResourceProxyManager.get_resource_smart_bin_session

   .. automethod:: ResourceProxyManager.get_membership_session

   .. automethod:: ResourceProxyManager.get_membership_session_for_bin

   .. automethod:: ResourceProxyManager.get_group_session

   .. automethod:: ResourceProxyManager.get_group_session_for_bin

   .. automethod:: ResourceProxyManager.get_group_assignment_session

   .. automethod:: ResourceProxyManager.get_group_assignment_session_for_bin

   .. automethod:: ResourceProxyManager.get_group_notification_session

   .. automethod:: ResourceProxyManager.get_group_notification_session_for_bin

   .. automethod:: ResourceProxyManager.get_group_hierarchy_session

   .. automethod:: ResourceProxyManager.get_group_hierarchy_session_for_bin

   .. automethod:: ResourceProxyManager.get_resource_agent_session

   .. automethod:: ResourceProxyManager.get_resource_agent_session_for_bin

   .. automethod:: ResourceProxyManager.get_resource_agent_assignment_session

   .. automethod:: ResourceProxyManager.get_resource_agent_assignment_session_for_bin

   .. automethod:: ResourceProxyManager.get_resource_relationship_lookup_session

   .. automethod:: ResourceProxyManager.get_resource_relationship_lookup_session_for_bin

   .. automethod:: ResourceProxyManager.get_resource_relationship_query_session

   .. automethod:: ResourceProxyManager.get_resource_relationship_query_session_for_bin

   .. automethod:: ResourceProxyManager.get_resource_relationship_search_session

   .. automethod:: ResourceProxyManager.get_resource_relationship_search_session_for_bin

   .. automethod:: ResourceProxyManager.get_resource_relationship_admin_session

   .. automethod:: ResourceProxyManager.get_resource_relationship_admin_session_for_bin

   .. automethod:: ResourceProxyManager.get_resource_relationship_notification_session

   .. automethod:: ResourceProxyManager.get_resource_relationship_notification_session_for_bin

   .. automethod:: ResourceProxyManager.get_resource_relationship_bin_session

   .. automethod:: ResourceProxyManager.get_resource_relationship_bin_assignment_session

   .. automethod:: ResourceProxyManager.get_resource_relationship_smart_bin_session

   .. automethod:: ResourceProxyManager.get_bin_lookup_session

   .. automethod:: ResourceProxyManager.get_bin_query_session

   .. automethod:: ResourceProxyManager.get_bin_search_session

   .. automethod:: ResourceProxyManager.get_bin_admin_session

   .. automethod:: ResourceProxyManager.get_bin_notification_session

   .. automethod:: ResourceProxyManager.get_bin_hierarchy_session

   .. automethod:: ResourceProxyManager.get_bin_hierarchy_design_session

   .. autoattribute:: ResourceProxyManager.resource_batch_proxy_manager

   .. autoattribute:: ResourceProxyManager.resource_demographic_proxy_manager

