.. currentmodule:: dlkit.services.resource
.. automodule:: dlkit.services.resource

Services
========


Resource Manager
----------------

.. autoclass:: ResourceManager
   :show-inheritance:

.. autoattribute:: ResourceManager.resource_batch_manager

.. autoattribute:: ResourceManager.resource_demographic_manager



Resource Profile Methods
________________

.. automethod:: ResourceManager.supports_visible_federation

.. automethod:: ResourceManager.supports_resource_lookup

.. automethod:: ResourceManager.supports_resource_query

.. automethod:: ResourceManager.supports_resource_search

.. automethod:: ResourceManager.supports_resource_admin

.. automethod:: ResourceManager.supports_resource_notification

.. automethod:: ResourceManager.supports_resource_bin

.. automethod:: ResourceManager.supports_resource_bin_assignment

.. automethod:: ResourceManager.supports_resource_smart_bin

.. automethod:: ResourceManager.supports_membership

.. automethod:: ResourceManager.supports_group

.. automethod:: ResourceManager.supports_group_assignment

.. automethod:: ResourceManager.supports_group_notification

.. automethod:: ResourceManager.supports_group_hierarchy

.. automethod:: ResourceManager.supports_resource_agent

.. automethod:: ResourceManager.supports_resource_agent_assignment

.. automethod:: ResourceManager.supports_resource_relationship_lookup

.. automethod:: ResourceManager.supports_resource_relationship_query

.. automethod:: ResourceManager.supports_resource_relationship_search

.. automethod:: ResourceManager.supports_resource_relationship_admin

.. automethod:: ResourceManager.supports_resource_relationship_notification

.. automethod:: ResourceManager.supports_resource_relationship_bin

.. automethod:: ResourceManager.supports_resource_relationship_bin_assignment

.. automethod:: ResourceManager.supports_resource_relationship_smart_bin

.. automethod:: ResourceManager.supports_bin_lookup

.. automethod:: ResourceManager.supports_bin_query

.. automethod:: ResourceManager.supports_bin_search

.. automethod:: ResourceManager.supports_bin_admin

.. automethod:: ResourceManager.supports_bin_notification

.. automethod:: ResourceManager.supports_bin_hierarchy

.. automethod:: ResourceManager.supports_bin_hierarchy_design

.. automethod:: ResourceManager.supports_resource_batch

.. automethod:: ResourceManager.supports_resource_demographic

.. autoattribute:: ResourceManager.resource_record_types

.. automethod:: ResourceManager.supports_resource_record_type

.. autoattribute:: ResourceManager.resource_search_record_types

.. automethod:: ResourceManager.supports_resource_search_record_type

.. autoattribute:: ResourceManager.resource_relationship_record_types

.. automethod:: ResourceManager.supports_resource_relationship_record_type

.. autoattribute:: ResourceManager.resource_relationship_search_record_types

.. automethod:: ResourceManager.supports_resource_relationship_search_record_type

.. autoattribute:: ResourceManager.bin_record_types

.. automethod:: ResourceManager.supports_bin_record_type

.. autoattribute:: ResourceManager.bin_search_record_types

.. automethod:: ResourceManager.supports_bin_search_record_type



Bin Lookup
__________

.. automethod:: ResourceManager.can_lookup_bins

.. automethod:: ResourceManager.use_comparative_bin_view

.. automethod:: ResourceManager.use_plenary_bin_view

.. automethod:: ResourceManager.get_bin

.. automethod:: ResourceManager.get_bins_by_ids

.. automethod:: ResourceManager.get_bins_by_genus_type

.. automethod:: ResourceManager.get_bins_by_parent_genus_type

.. automethod:: ResourceManager.get_bins_by_record_type

.. automethod:: ResourceManager.get_bins_by_provider

.. autoattribute:: ResourceManager.bins



Bin Query
_________

.. automethod:: ResourceManager.can_search_bins

.. autoattribute:: ResourceManager.bin_query

.. automethod:: ResourceManager.get_bins_by_query



Bin Search
__________

.. autoattribute:: ResourceManager.bin_search

.. autoattribute:: ResourceManager.bin_search_order

.. automethod:: ResourceManager.get_bins_by_search

.. automethod:: ResourceManager.get_bin_query_from_inspector



Bin Admin
_________

.. automethod:: ResourceManager.can_create_bins

.. automethod:: ResourceManager.can_create_bin_with_record_types

.. automethod:: ResourceManager.get_bin_form_for_create

.. automethod:: ResourceManager.create_bin

.. automethod:: ResourceManager.can_update_bins

.. automethod:: ResourceManager.get_bin_form_for_update

.. automethod:: ResourceManager.update_bin

.. automethod:: ResourceManager.can_delete_bins

.. automethod:: ResourceManager.delete_bin

.. automethod:: ResourceManager.can_manage_bin_aliases

.. automethod:: ResourceManager.alias_bin



Bin Notification
________________

.. automethod:: ResourceManager.can_register_for_bin_notifications

.. automethod:: ResourceManager.register_for_new_bins

.. automethod:: ResourceManager.register_for_new_bin_ancestors

.. automethod:: ResourceManager.register_for_new_bin_descendants

.. automethod:: ResourceManager.register_for_changed_bins

.. automethod:: ResourceManager.register_for_changed_bin

.. automethod:: ResourceManager.register_for_deleted_bins

.. automethod:: ResourceManager.register_for_deleted_bin

.. automethod:: ResourceManager.register_for_deleted_bin_ancestors

.. automethod:: ResourceManager.register_for_deleted_bin_descendants



Bin Hierarchy
_____________

.. autoattribute:: ResourceManager.bin_hierarchy_id

.. autoattribute:: ResourceManager.bin_hierarchy

.. automethod:: ResourceManager.can_access_bin_hierarchy

.. automethod:: ResourceManager.use_comparative_bin_view

.. automethod:: ResourceManager.use_plenary_bin_view

.. autoattribute:: ResourceManager.root_bin_ids

.. autoattribute:: ResourceManager.root_bins

.. automethod:: ResourceManager.has_parent_bins

.. automethod:: ResourceManager.is_parent_of_bin

.. automethod:: ResourceManager.get_parent_bin_ids

.. automethod:: ResourceManager.get_parent_bins

.. automethod:: ResourceManager.is_ancestor_of_bin

.. automethod:: ResourceManager.has_child_bins

.. automethod:: ResourceManager.is_child_of_bin

.. automethod:: ResourceManager.get_child_bin_ids

.. automethod:: ResourceManager.get_child_bins

.. automethod:: ResourceManager.is_descendant_of_bin

.. automethod:: ResourceManager.get_bin_node_ids

.. automethod:: ResourceManager.get_bin_nodes



Bin Hierarchy Design
____________________

.. autoattribute:: ResourceManager.bin_hierarchy_id

.. autoattribute:: ResourceManager.bin_hierarchy

.. automethod:: ResourceManager.can_modify_bin_hierarchy

.. automethod:: ResourceManager.add_root_bin

.. automethod:: ResourceManager.remove_root_bin

.. automethod:: ResourceManager.add_child_bin

.. automethod:: ResourceManager.remove_child_bin

.. automethod:: ResourceManager.remove_child_bins



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



