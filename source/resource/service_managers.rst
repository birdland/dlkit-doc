
.. currentmodule:: dlkit.services.resource
.. automodule:: dlkit.services.resource

Service Managers
================


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



Resource Lookup Methods
-----------------------

   .. autoattribute:: ResourceManager.bin_id

   .. autoattribute:: ResourceManager.bin

   .. automethod:: ResourceManager.can_lookup_resources

   .. automethod:: ResourceManager.use_comparative_resource_view

   .. automethod:: ResourceManager.use_plenary_resource_view

   .. automethod:: ResourceManager.use_federated_bin_view

   .. automethod:: ResourceManager.use_isolated_bin_view

   .. automethod:: ResourceManager.get_resource

   .. automethod:: ResourceManager.get_resources_by_ids

   .. automethod:: ResourceManager.get_resources_by_genus_type

   .. automethod:: ResourceManager.get_resources_by_parent_genus_type

   .. automethod:: ResourceManager.get_resources_by_record_type

   .. autoattribute:: ResourceManager.resources



Resource Query Methods
----------------------

   .. autoattribute:: ResourceManager.bin_id

   .. autoattribute:: ResourceManager.bin

   .. automethod:: ResourceManager.can_search_resources

   .. automethod:: ResourceManager.use_federated_bin_view

   .. automethod:: ResourceManager.use_isolated_bin_view

   .. autoattribute:: ResourceManager.resource_query

   .. automethod:: ResourceManager.get_resources_by_query



Resource Search Methods
-----------------------

   .. autoattribute:: ResourceManager.resource_search

   .. autoattribute:: ResourceManager.resource_search_order

   .. automethod:: ResourceManager.get_resources_by_search

   .. automethod:: ResourceManager.get_resource_query_from_inspector



Resource Admin Methods
----------------------

   .. autoattribute:: ResourceManager.bin_id

   .. autoattribute:: ResourceManager.bin

   .. automethod:: ResourceManager.can_create_resources

   .. automethod:: ResourceManager.can_create_resource_with_record_types

   .. automethod:: ResourceManager.get_resource_form_for_create

   .. automethod:: ResourceManager.create_resource

   .. automethod:: ResourceManager.can_update_resources

   .. automethod:: ResourceManager.get_resource_form_for_update

   .. automethod:: ResourceManager.update_resource

   .. automethod:: ResourceManager.can_delete_resources

   .. automethod:: ResourceManager.delete_resource

   .. automethod:: ResourceManager.can_manage_resource_aliases

   .. automethod:: ResourceManager.alias_resource



Resource Notification Methods
-----------------------------

   .. autoattribute:: ResourceManager.bin_id

   .. autoattribute:: ResourceManager.bin

   .. automethod:: ResourceManager.can_register_for_resource_notifications

   .. automethod:: ResourceManager.use_federated_bin_view

   .. automethod:: ResourceManager.use_isolated_bin_view

   .. automethod:: ResourceManager.register_for_new_resources

   .. automethod:: ResourceManager.register_for_changed_resources

   .. automethod:: ResourceManager.register_for_changed_resource

   .. automethod:: ResourceManager.register_for_deleted_resources

   .. automethod:: ResourceManager.register_for_deleted_resource

   .. automethod:: ResourceManager.reliable_resource_notifications

   .. automethod:: ResourceManager.unreliable_resource_notifications

   .. automethod:: ResourceManager.acknowledge_resource_notification



Resource Bin Methods
--------------------

   .. automethod:: ResourceManager.use_comparative_bin_view

   .. automethod:: ResourceManager.use_plenary_bin_view

   .. automethod:: ResourceManager.can_lookup_resource_bin_mappings

   .. automethod:: ResourceManager.get_resource_ids_by_bin

   .. automethod:: ResourceManager.get_resources_by_bin

   .. automethod:: ResourceManager.get_resource_ids_by_bins

   .. automethod:: ResourceManager.get_resources_by_bins

   .. automethod:: ResourceManager.get_bin_ids_by_resource

   .. automethod:: ResourceManager.get_bins_by_resource



Resource Bin Assignment Methods
-------------------------------

   .. automethod:: ResourceManager.can_assign_resources

   .. automethod:: ResourceManager.can_assign_resources_to_bin

   .. automethod:: ResourceManager.get_assignable_bin_ids

   .. automethod:: ResourceManager.get_assignable_bin_ids_for_resource

   .. automethod:: ResourceManager.assign_resource_to_bin

   .. automethod:: ResourceManager.unassign_resource_from_bin



Resource Agent Methods
----------------------

   .. autoattribute:: ResourceManager.bin_id

   .. autoattribute:: ResourceManager.bin

   .. automethod:: ResourceManager.can_lookup_resource_agent_mappings

   .. automethod:: ResourceManager.use_comparative_agent_view

   .. automethod:: ResourceManager.use_plenary_agent_view

   .. automethod:: ResourceManager.use_federated_bin_view

   .. automethod:: ResourceManager.use_isolated_bin_view

   .. automethod:: ResourceManager.get_resource_id_by_agent

   .. automethod:: ResourceManager.get_resource_by_agent

   .. automethod:: ResourceManager.get_agent_ids_by_resource

   .. automethod:: ResourceManager.get_agents_by_resource



Resource Agent Assignment Methods
---------------------------------

   .. autoattribute:: ResourceManager.bin_id

   .. autoattribute:: ResourceManager.bin

   .. automethod:: ResourceManager.can_assign_agents

   .. automethod:: ResourceManager.can_assign_agents_to_resource

   .. automethod:: ResourceManager.assign_agent_to_resource

   .. automethod:: ResourceManager.unassign_agent_from_resource



Bin Lookup Methods
------------------

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



Bin Query Methods
-----------------

   .. automethod:: ResourceManager.can_search_bins

   .. autoattribute:: ResourceManager.bin_query

   .. automethod:: ResourceManager.get_bins_by_query



Bin Admin Methods
-----------------

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



Bin Hierarchy Methods
---------------------

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



Bin Hierarchy Design Methods
----------------------------

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



Resource Lookup Methods
-----------------------

   .. autoattribute:: ResourceProxyManager.bin_id

   .. autoattribute:: ResourceProxyManager.bin

   .. automethod:: ResourceProxyManager.can_lookup_resources

   .. automethod:: ResourceProxyManager.use_comparative_resource_view

   .. automethod:: ResourceProxyManager.use_plenary_resource_view

   .. automethod:: ResourceProxyManager.use_federated_bin_view

   .. automethod:: ResourceProxyManager.use_isolated_bin_view

   .. automethod:: ResourceProxyManager.get_resource

   .. automethod:: ResourceProxyManager.get_resources_by_ids

   .. automethod:: ResourceProxyManager.get_resources_by_genus_type

   .. automethod:: ResourceProxyManager.get_resources_by_parent_genus_type

   .. automethod:: ResourceProxyManager.get_resources_by_record_type

   .. autoattribute:: ResourceProxyManager.resources



Resource Query Methods
----------------------

   .. autoattribute:: ResourceProxyManager.bin_id

   .. autoattribute:: ResourceProxyManager.bin

   .. automethod:: ResourceProxyManager.can_search_resources

   .. automethod:: ResourceProxyManager.use_federated_bin_view

   .. automethod:: ResourceProxyManager.use_isolated_bin_view

   .. autoattribute:: ResourceProxyManager.resource_query

   .. automethod:: ResourceProxyManager.get_resources_by_query



Resource Search Methods
-----------------------

   .. autoattribute:: ResourceProxyManager.resource_search

   .. autoattribute:: ResourceProxyManager.resource_search_order

   .. automethod:: ResourceProxyManager.get_resources_by_search

   .. automethod:: ResourceProxyManager.get_resource_query_from_inspector



Resource Admin Methods
----------------------

   .. autoattribute:: ResourceProxyManager.bin_id

   .. autoattribute:: ResourceProxyManager.bin

   .. automethod:: ResourceProxyManager.can_create_resources

   .. automethod:: ResourceProxyManager.can_create_resource_with_record_types

   .. automethod:: ResourceProxyManager.get_resource_form_for_create

   .. automethod:: ResourceProxyManager.create_resource

   .. automethod:: ResourceProxyManager.can_update_resources

   .. automethod:: ResourceProxyManager.get_resource_form_for_update

   .. automethod:: ResourceProxyManager.update_resource

   .. automethod:: ResourceProxyManager.can_delete_resources

   .. automethod:: ResourceProxyManager.delete_resource

   .. automethod:: ResourceProxyManager.can_manage_resource_aliases

   .. automethod:: ResourceProxyManager.alias_resource



Resource Notification Methods
-----------------------------

   .. autoattribute:: ResourceProxyManager.bin_id

   .. autoattribute:: ResourceProxyManager.bin

   .. automethod:: ResourceProxyManager.can_register_for_resource_notifications

   .. automethod:: ResourceProxyManager.use_federated_bin_view

   .. automethod:: ResourceProxyManager.use_isolated_bin_view

   .. automethod:: ResourceProxyManager.register_for_new_resources

   .. automethod:: ResourceProxyManager.register_for_changed_resources

   .. automethod:: ResourceProxyManager.register_for_changed_resource

   .. automethod:: ResourceProxyManager.register_for_deleted_resources

   .. automethod:: ResourceProxyManager.register_for_deleted_resource

   .. automethod:: ResourceProxyManager.reliable_resource_notifications

   .. automethod:: ResourceProxyManager.unreliable_resource_notifications

   .. automethod:: ResourceProxyManager.acknowledge_resource_notification



Resource Bin Methods
--------------------

   .. automethod:: ResourceProxyManager.use_comparative_bin_view

   .. automethod:: ResourceProxyManager.use_plenary_bin_view

   .. automethod:: ResourceProxyManager.can_lookup_resource_bin_mappings

   .. automethod:: ResourceProxyManager.get_resource_ids_by_bin

   .. automethod:: ResourceProxyManager.get_resources_by_bin

   .. automethod:: ResourceProxyManager.get_resource_ids_by_bins

   .. automethod:: ResourceProxyManager.get_resources_by_bins

   .. automethod:: ResourceProxyManager.get_bin_ids_by_resource

   .. automethod:: ResourceProxyManager.get_bins_by_resource



Resource Bin Assignment Methods
-------------------------------

   .. automethod:: ResourceProxyManager.can_assign_resources

   .. automethod:: ResourceProxyManager.can_assign_resources_to_bin

   .. automethod:: ResourceProxyManager.get_assignable_bin_ids

   .. automethod:: ResourceProxyManager.get_assignable_bin_ids_for_resource

   .. automethod:: ResourceProxyManager.assign_resource_to_bin

   .. automethod:: ResourceProxyManager.unassign_resource_from_bin



Resource Agent Methods
----------------------

   .. autoattribute:: ResourceProxyManager.bin_id

   .. autoattribute:: ResourceProxyManager.bin

   .. automethod:: ResourceProxyManager.can_lookup_resource_agent_mappings

   .. automethod:: ResourceProxyManager.use_comparative_agent_view

   .. automethod:: ResourceProxyManager.use_plenary_agent_view

   .. automethod:: ResourceProxyManager.use_federated_bin_view

   .. automethod:: ResourceProxyManager.use_isolated_bin_view

   .. automethod:: ResourceProxyManager.get_resource_id_by_agent

   .. automethod:: ResourceProxyManager.get_resource_by_agent

   .. automethod:: ResourceProxyManager.get_agent_ids_by_resource

   .. automethod:: ResourceProxyManager.get_agents_by_resource



Resource Agent Assignment Methods
---------------------------------

   .. autoattribute:: ResourceProxyManager.bin_id

   .. autoattribute:: ResourceProxyManager.bin

   .. automethod:: ResourceProxyManager.can_assign_agents

   .. automethod:: ResourceProxyManager.can_assign_agents_to_resource

   .. automethod:: ResourceProxyManager.assign_agent_to_resource

   .. automethod:: ResourceProxyManager.unassign_agent_from_resource



Bin Lookup Methods
------------------

   .. automethod:: ResourceProxyManager.can_lookup_bins

   .. automethod:: ResourceProxyManager.use_comparative_bin_view

   .. automethod:: ResourceProxyManager.use_plenary_bin_view

   .. automethod:: ResourceProxyManager.get_bin

   .. automethod:: ResourceProxyManager.get_bins_by_ids

   .. automethod:: ResourceProxyManager.get_bins_by_genus_type

   .. automethod:: ResourceProxyManager.get_bins_by_parent_genus_type

   .. automethod:: ResourceProxyManager.get_bins_by_record_type

   .. automethod:: ResourceProxyManager.get_bins_by_provider

   .. autoattribute:: ResourceProxyManager.bins



Bin Query Methods
-----------------

   .. automethod:: ResourceProxyManager.can_search_bins

   .. autoattribute:: ResourceProxyManager.bin_query

   .. automethod:: ResourceProxyManager.get_bins_by_query



Bin Admin Methods
-----------------

   .. automethod:: ResourceProxyManager.can_create_bins

   .. automethod:: ResourceProxyManager.can_create_bin_with_record_types

   .. automethod:: ResourceProxyManager.get_bin_form_for_create

   .. automethod:: ResourceProxyManager.create_bin

   .. automethod:: ResourceProxyManager.can_update_bins

   .. automethod:: ResourceProxyManager.get_bin_form_for_update

   .. automethod:: ResourceProxyManager.update_bin

   .. automethod:: ResourceProxyManager.can_delete_bins

   .. automethod:: ResourceProxyManager.delete_bin

   .. automethod:: ResourceProxyManager.can_manage_bin_aliases

   .. automethod:: ResourceProxyManager.alias_bin



Bin Hierarchy Methods
---------------------

   .. autoattribute:: ResourceProxyManager.bin_hierarchy_id

   .. autoattribute:: ResourceProxyManager.bin_hierarchy

   .. automethod:: ResourceProxyManager.can_access_bin_hierarchy

   .. automethod:: ResourceProxyManager.use_comparative_bin_view

   .. automethod:: ResourceProxyManager.use_plenary_bin_view

   .. autoattribute:: ResourceProxyManager.root_bin_ids

   .. autoattribute:: ResourceProxyManager.root_bins

   .. automethod:: ResourceProxyManager.has_parent_bins

   .. automethod:: ResourceProxyManager.is_parent_of_bin

   .. automethod:: ResourceProxyManager.get_parent_bin_ids

   .. automethod:: ResourceProxyManager.get_parent_bins

   .. automethod:: ResourceProxyManager.is_ancestor_of_bin

   .. automethod:: ResourceProxyManager.has_child_bins

   .. automethod:: ResourceProxyManager.is_child_of_bin

   .. automethod:: ResourceProxyManager.get_child_bin_ids

   .. automethod:: ResourceProxyManager.get_child_bins

   .. automethod:: ResourceProxyManager.is_descendant_of_bin

   .. automethod:: ResourceProxyManager.get_bin_node_ids

   .. automethod:: ResourceProxyManager.get_bin_nodes



Bin Hierarchy Design Methods
----------------------------

   .. autoattribute:: ResourceProxyManager.bin_hierarchy_id

   .. autoattribute:: ResourceProxyManager.bin_hierarchy

   .. automethod:: ResourceProxyManager.can_modify_bin_hierarchy

   .. automethod:: ResourceProxyManager.add_root_bin

   .. automethod:: ResourceProxyManager.remove_root_bin

   .. automethod:: ResourceProxyManager.add_child_bin

   .. automethod:: ResourceProxyManager.remove_child_bin

   .. automethod:: ResourceProxyManager.remove_child_bins



