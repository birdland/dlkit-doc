
.. currentmodule:: dlkit.resource.objects
.. automodule:: dlkit.resource.objects

Objects
=======


Resource
--------

.. autoclass:: Resource
   :show-inheritance:

   .. automethod:: Resource.is_group

   .. automethod:: Resource.is_demographic

   .. automethod:: Resource.has_avatar

   .. autoattribute:: Resource.avatar_id

   .. autoattribute:: Resource.avatar

   .. automethod:: Resource.get_resource_record



Resource Bin Methods
--------------------

   .. automethod:: ResourceBinSession.use_comparative_bin_view

   .. automethod:: ResourceBinSession.use_plenary_bin_view

   .. automethod:: ResourceBinSession.can_lookup_resource_bin_mappings

   .. automethod:: ResourceBinSession.get_resource_ids_by_bin

   .. automethod:: ResourceBinSession.get_resources_by_bin

   .. automethod:: ResourceBinSession.get_resource_ids_by_bins

   .. automethod:: ResourceBinSession.get_resources_by_bins

   .. automethod:: ResourceBinSession.get_bin_ids_by_resource

   .. automethod:: ResourceBinSession.get_bins_by_resource



Resource Bin Assignment Methods
-------------------------------

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources_to_bin

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource

   .. automethod:: ResourceBinAssignmentSession.assign_resource_to_bin

   .. automethod:: ResourceBinAssignmentSession.unassign_resource_from_bin



Bin Lookup Methods
------------------

   .. automethod:: BinLookupSession.can_lookup_bins

   .. automethod:: BinLookupSession.use_comparative_bin_view

   .. automethod:: BinLookupSession.use_plenary_bin_view

   .. automethod:: BinLookupSession.get_bin

   .. automethod:: BinLookupSession.get_bins_by_ids

   .. automethod:: BinLookupSession.get_bins_by_genus_type

   .. automethod:: BinLookupSession.get_bins_by_parent_genus_type

   .. automethod:: BinLookupSession.get_bins_by_record_type

   .. automethod:: BinLookupSession.get_bins_by_provider

   .. autoattribute:: BinLookupSession.bins



Bin Query Methods
-----------------

   .. automethod:: BinQuerySession.can_search_bins

   .. autoattribute:: BinQuerySession.bin_query

   .. automethod:: BinQuerySession.get_bins_by_query



Bin Admin Methods
-----------------

   .. automethod:: BinAdminSession.can_create_bins

   .. automethod:: BinAdminSession.can_create_bin_with_record_types

   .. automethod:: BinAdminSession.get_bin_form_for_create

   .. automethod:: BinAdminSession.create_bin

   .. automethod:: BinAdminSession.can_update_bins

   .. automethod:: BinAdminSession.get_bin_form_for_update

   .. automethod:: BinAdminSession.update_bin

   .. automethod:: BinAdminSession.can_delete_bins

   .. automethod:: BinAdminSession.delete_bin

   .. automethod:: BinAdminSession.can_manage_bin_aliases

   .. automethod:: BinAdminSession.alias_bin



Bin Hierarchy Methods
---------------------

   .. autoattribute:: BinHierarchySession.bin_hierarchy_id

   .. autoattribute:: BinHierarchySession.bin_hierarchy

   .. automethod:: BinHierarchySession.can_access_bin_hierarchy

   .. automethod:: BinHierarchySession.use_comparative_bin_view

   .. automethod:: BinHierarchySession.use_plenary_bin_view

   .. autoattribute:: BinHierarchySession.root_bin_ids

   .. autoattribute:: BinHierarchySession.root_bins

   .. automethod:: BinHierarchySession.has_parent_bins

   .. automethod:: BinHierarchySession.is_parent_of_bin

   .. automethod:: BinHierarchySession.get_parent_bin_ids

   .. automethod:: BinHierarchySession.get_parent_bins

   .. automethod:: BinHierarchySession.is_ancestor_of_bin

   .. automethod:: BinHierarchySession.has_child_bins

   .. automethod:: BinHierarchySession.is_child_of_bin

   .. automethod:: BinHierarchySession.get_child_bin_ids

   .. automethod:: BinHierarchySession.get_child_bins

   .. automethod:: BinHierarchySession.is_descendant_of_bin

   .. automethod:: BinHierarchySession.get_bin_node_ids

   .. automethod:: BinHierarchySession.get_bin_nodes



Bin Hierarchy Design Methods
----------------------------

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy_id

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.can_modify_bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.add_root_bin

   .. automethod:: BinHierarchyDesignSession.remove_root_bin

   .. automethod:: BinHierarchyDesignSession.add_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bins



Resource Lookup Methods
-----------------------

   .. autoattribute:: ResourceLookupSession.bin_id

   .. autoattribute:: ResourceLookupSession.bin

   .. automethod:: ResourceLookupSession.can_lookup_resources

   .. automethod:: ResourceLookupSession.use_comparative_resource_view

   .. automethod:: ResourceLookupSession.use_plenary_resource_view

   .. automethod:: ResourceLookupSession.use_federated_bin_view

   .. automethod:: ResourceLookupSession.use_isolated_bin_view

   .. automethod:: ResourceLookupSession.get_resource

   .. automethod:: ResourceLookupSession.get_resources_by_ids

   .. automethod:: ResourceLookupSession.get_resources_by_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_parent_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_record_type

   .. autoattribute:: ResourceLookupSession.resources



Resource Query Methods
----------------------

   .. autoattribute:: ResourceQuerySession.bin_id

   .. autoattribute:: ResourceQuerySession.bin

   .. automethod:: ResourceQuerySession.can_search_resources

   .. automethod:: ResourceQuerySession.use_federated_bin_view

   .. automethod:: ResourceQuerySession.use_isolated_bin_view

   .. autoattribute:: ResourceQuerySession.resource_query

   .. automethod:: ResourceQuerySession.get_resources_by_query



Resource Search Methods
-----------------------

   .. autoattribute:: ResourceSearchSession.resource_search

   .. autoattribute:: ResourceSearchSession.resource_search_order

   .. automethod:: ResourceSearchSession.get_resources_by_search

   .. automethod:: ResourceSearchSession.get_resource_query_from_inspector



Resource Admin Methods
----------------------

   .. autoattribute:: ResourceAdminSession.bin_id

   .. autoattribute:: ResourceAdminSession.bin

   .. automethod:: ResourceAdminSession.can_create_resources

   .. automethod:: ResourceAdminSession.can_create_resource_with_record_types

   .. automethod:: ResourceAdminSession.get_resource_form_for_create

   .. automethod:: ResourceAdminSession.create_resource

   .. automethod:: ResourceAdminSession.can_update_resources

   .. automethod:: ResourceAdminSession.get_resource_form_for_update

   .. automethod:: ResourceAdminSession.update_resource

   .. automethod:: ResourceAdminSession.can_delete_resources

   .. automethod:: ResourceAdminSession.delete_resource

   .. automethod:: ResourceAdminSession.can_manage_resource_aliases

   .. automethod:: ResourceAdminSession.alias_resource



Resource Notification Methods
-----------------------------

   .. autoattribute:: ResourceNotificationSession.bin_id

   .. autoattribute:: ResourceNotificationSession.bin

   .. automethod:: ResourceNotificationSession.can_register_for_resource_notifications

   .. automethod:: ResourceNotificationSession.use_federated_bin_view

   .. automethod:: ResourceNotificationSession.use_isolated_bin_view

   .. automethod:: ResourceNotificationSession.register_for_new_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resource

   .. automethod:: ResourceNotificationSession.register_for_deleted_resources

   .. automethod:: ResourceNotificationSession.register_for_deleted_resource

   .. automethod:: ResourceNotificationSession.reliable_resource_notifications

   .. automethod:: ResourceNotificationSession.unreliable_resource_notifications

   .. automethod:: ResourceNotificationSession.acknowledge_resource_notification



Resource Agent Methods
----------------------

   .. autoattribute:: ResourceAgentSession.bin_id

   .. autoattribute:: ResourceAgentSession.bin

   .. automethod:: ResourceAgentSession.can_lookup_resource_agent_mappings

   .. automethod:: ResourceAgentSession.use_comparative_agent_view

   .. automethod:: ResourceAgentSession.use_plenary_agent_view

   .. automethod:: ResourceAgentSession.use_federated_bin_view

   .. automethod:: ResourceAgentSession.use_isolated_bin_view

   .. automethod:: ResourceAgentSession.get_resource_id_by_agent

   .. automethod:: ResourceAgentSession.get_resource_by_agent

   .. automethod:: ResourceAgentSession.get_agent_ids_by_resource

   .. automethod:: ResourceAgentSession.get_agents_by_resource



Resource Agent Assignment Methods
---------------------------------

   .. autoattribute:: ResourceAgentAssignmentSession.bin_id

   .. autoattribute:: ResourceAgentAssignmentSession.bin

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents_to_resource

   .. automethod:: ResourceAgentAssignmentSession.assign_agent_to_resource

   .. automethod:: ResourceAgentAssignmentSession.unassign_agent_from_resource



Resource Form
-------------

.. autoclass:: ResourceForm
   :show-inheritance:

   .. autoattribute:: ResourceForm.group_metadata

   .. autoattribute:: ResourceForm.group

   .. autoattribute:: ResourceForm.avatar_metadata

   .. autoattribute:: ResourceForm.avatar

   .. automethod:: ResourceForm.get_resource_form_record



Resource Bin Methods
--------------------

   .. automethod:: ResourceBinSession.use_comparative_bin_view

   .. automethod:: ResourceBinSession.use_plenary_bin_view

   .. automethod:: ResourceBinSession.can_lookup_resource_bin_mappings

   .. automethod:: ResourceBinSession.get_resource_ids_by_bin

   .. automethod:: ResourceBinSession.get_resources_by_bin

   .. automethod:: ResourceBinSession.get_resource_ids_by_bins

   .. automethod:: ResourceBinSession.get_resources_by_bins

   .. automethod:: ResourceBinSession.get_bin_ids_by_resource

   .. automethod:: ResourceBinSession.get_bins_by_resource



Resource Bin Assignment Methods
-------------------------------

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources_to_bin

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource

   .. automethod:: ResourceBinAssignmentSession.assign_resource_to_bin

   .. automethod:: ResourceBinAssignmentSession.unassign_resource_from_bin



Bin Lookup Methods
------------------

   .. automethod:: BinLookupSession.can_lookup_bins

   .. automethod:: BinLookupSession.use_comparative_bin_view

   .. automethod:: BinLookupSession.use_plenary_bin_view

   .. automethod:: BinLookupSession.get_bin

   .. automethod:: BinLookupSession.get_bins_by_ids

   .. automethod:: BinLookupSession.get_bins_by_genus_type

   .. automethod:: BinLookupSession.get_bins_by_parent_genus_type

   .. automethod:: BinLookupSession.get_bins_by_record_type

   .. automethod:: BinLookupSession.get_bins_by_provider

   .. autoattribute:: BinLookupSession.bins



Bin Query Methods
-----------------

   .. automethod:: BinQuerySession.can_search_bins

   .. autoattribute:: BinQuerySession.bin_query

   .. automethod:: BinQuerySession.get_bins_by_query



Bin Admin Methods
-----------------

   .. automethod:: BinAdminSession.can_create_bins

   .. automethod:: BinAdminSession.can_create_bin_with_record_types

   .. automethod:: BinAdminSession.get_bin_form_for_create

   .. automethod:: BinAdminSession.create_bin

   .. automethod:: BinAdminSession.can_update_bins

   .. automethod:: BinAdminSession.get_bin_form_for_update

   .. automethod:: BinAdminSession.update_bin

   .. automethod:: BinAdminSession.can_delete_bins

   .. automethod:: BinAdminSession.delete_bin

   .. automethod:: BinAdminSession.can_manage_bin_aliases

   .. automethod:: BinAdminSession.alias_bin



Bin Hierarchy Methods
---------------------

   .. autoattribute:: BinHierarchySession.bin_hierarchy_id

   .. autoattribute:: BinHierarchySession.bin_hierarchy

   .. automethod:: BinHierarchySession.can_access_bin_hierarchy

   .. automethod:: BinHierarchySession.use_comparative_bin_view

   .. automethod:: BinHierarchySession.use_plenary_bin_view

   .. autoattribute:: BinHierarchySession.root_bin_ids

   .. autoattribute:: BinHierarchySession.root_bins

   .. automethod:: BinHierarchySession.has_parent_bins

   .. automethod:: BinHierarchySession.is_parent_of_bin

   .. automethod:: BinHierarchySession.get_parent_bin_ids

   .. automethod:: BinHierarchySession.get_parent_bins

   .. automethod:: BinHierarchySession.is_ancestor_of_bin

   .. automethod:: BinHierarchySession.has_child_bins

   .. automethod:: BinHierarchySession.is_child_of_bin

   .. automethod:: BinHierarchySession.get_child_bin_ids

   .. automethod:: BinHierarchySession.get_child_bins

   .. automethod:: BinHierarchySession.is_descendant_of_bin

   .. automethod:: BinHierarchySession.get_bin_node_ids

   .. automethod:: BinHierarchySession.get_bin_nodes



Bin Hierarchy Design Methods
----------------------------

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy_id

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.can_modify_bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.add_root_bin

   .. automethod:: BinHierarchyDesignSession.remove_root_bin

   .. automethod:: BinHierarchyDesignSession.add_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bins



Resource Lookup Methods
-----------------------

   .. autoattribute:: ResourceLookupSession.bin_id

   .. autoattribute:: ResourceLookupSession.bin

   .. automethod:: ResourceLookupSession.can_lookup_resources

   .. automethod:: ResourceLookupSession.use_comparative_resource_view

   .. automethod:: ResourceLookupSession.use_plenary_resource_view

   .. automethod:: ResourceLookupSession.use_federated_bin_view

   .. automethod:: ResourceLookupSession.use_isolated_bin_view

   .. automethod:: ResourceLookupSession.get_resource

   .. automethod:: ResourceLookupSession.get_resources_by_ids

   .. automethod:: ResourceLookupSession.get_resources_by_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_parent_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_record_type

   .. autoattribute:: ResourceLookupSession.resources



Resource Query Methods
----------------------

   .. autoattribute:: ResourceQuerySession.bin_id

   .. autoattribute:: ResourceQuerySession.bin

   .. automethod:: ResourceQuerySession.can_search_resources

   .. automethod:: ResourceQuerySession.use_federated_bin_view

   .. automethod:: ResourceQuerySession.use_isolated_bin_view

   .. autoattribute:: ResourceQuerySession.resource_query

   .. automethod:: ResourceQuerySession.get_resources_by_query



Resource Search Methods
-----------------------

   .. autoattribute:: ResourceSearchSession.resource_search

   .. autoattribute:: ResourceSearchSession.resource_search_order

   .. automethod:: ResourceSearchSession.get_resources_by_search

   .. automethod:: ResourceSearchSession.get_resource_query_from_inspector



Resource Admin Methods
----------------------

   .. autoattribute:: ResourceAdminSession.bin_id

   .. autoattribute:: ResourceAdminSession.bin

   .. automethod:: ResourceAdminSession.can_create_resources

   .. automethod:: ResourceAdminSession.can_create_resource_with_record_types

   .. automethod:: ResourceAdminSession.get_resource_form_for_create

   .. automethod:: ResourceAdminSession.create_resource

   .. automethod:: ResourceAdminSession.can_update_resources

   .. automethod:: ResourceAdminSession.get_resource_form_for_update

   .. automethod:: ResourceAdminSession.update_resource

   .. automethod:: ResourceAdminSession.can_delete_resources

   .. automethod:: ResourceAdminSession.delete_resource

   .. automethod:: ResourceAdminSession.can_manage_resource_aliases

   .. automethod:: ResourceAdminSession.alias_resource



Resource Notification Methods
-----------------------------

   .. autoattribute:: ResourceNotificationSession.bin_id

   .. autoattribute:: ResourceNotificationSession.bin

   .. automethod:: ResourceNotificationSession.can_register_for_resource_notifications

   .. automethod:: ResourceNotificationSession.use_federated_bin_view

   .. automethod:: ResourceNotificationSession.use_isolated_bin_view

   .. automethod:: ResourceNotificationSession.register_for_new_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resource

   .. automethod:: ResourceNotificationSession.register_for_deleted_resources

   .. automethod:: ResourceNotificationSession.register_for_deleted_resource

   .. automethod:: ResourceNotificationSession.reliable_resource_notifications

   .. automethod:: ResourceNotificationSession.unreliable_resource_notifications

   .. automethod:: ResourceNotificationSession.acknowledge_resource_notification



Resource Agent Methods
----------------------

   .. autoattribute:: ResourceAgentSession.bin_id

   .. autoattribute:: ResourceAgentSession.bin

   .. automethod:: ResourceAgentSession.can_lookup_resource_agent_mappings

   .. automethod:: ResourceAgentSession.use_comparative_agent_view

   .. automethod:: ResourceAgentSession.use_plenary_agent_view

   .. automethod:: ResourceAgentSession.use_federated_bin_view

   .. automethod:: ResourceAgentSession.use_isolated_bin_view

   .. automethod:: ResourceAgentSession.get_resource_id_by_agent

   .. automethod:: ResourceAgentSession.get_resource_by_agent

   .. automethod:: ResourceAgentSession.get_agent_ids_by_resource

   .. automethod:: ResourceAgentSession.get_agents_by_resource



Resource Agent Assignment Methods
---------------------------------

   .. autoattribute:: ResourceAgentAssignmentSession.bin_id

   .. autoattribute:: ResourceAgentAssignmentSession.bin

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents_to_resource

   .. automethod:: ResourceAgentAssignmentSession.assign_agent_to_resource

   .. automethod:: ResourceAgentAssignmentSession.unassign_agent_from_resource



Resource List
-------------

.. autoclass:: ResourceList
   :show-inheritance:

   .. autoattribute:: ResourceList.next_resource

   .. automethod:: ResourceList.get_next_resources



Resource Bin Methods
--------------------

   .. automethod:: ResourceBinSession.use_comparative_bin_view

   .. automethod:: ResourceBinSession.use_plenary_bin_view

   .. automethod:: ResourceBinSession.can_lookup_resource_bin_mappings

   .. automethod:: ResourceBinSession.get_resource_ids_by_bin

   .. automethod:: ResourceBinSession.get_resources_by_bin

   .. automethod:: ResourceBinSession.get_resource_ids_by_bins

   .. automethod:: ResourceBinSession.get_resources_by_bins

   .. automethod:: ResourceBinSession.get_bin_ids_by_resource

   .. automethod:: ResourceBinSession.get_bins_by_resource



Resource Bin Assignment Methods
-------------------------------

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources_to_bin

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource

   .. automethod:: ResourceBinAssignmentSession.assign_resource_to_bin

   .. automethod:: ResourceBinAssignmentSession.unassign_resource_from_bin



Bin Lookup Methods
------------------

   .. automethod:: BinLookupSession.can_lookup_bins

   .. automethod:: BinLookupSession.use_comparative_bin_view

   .. automethod:: BinLookupSession.use_plenary_bin_view

   .. automethod:: BinLookupSession.get_bin

   .. automethod:: BinLookupSession.get_bins_by_ids

   .. automethod:: BinLookupSession.get_bins_by_genus_type

   .. automethod:: BinLookupSession.get_bins_by_parent_genus_type

   .. automethod:: BinLookupSession.get_bins_by_record_type

   .. automethod:: BinLookupSession.get_bins_by_provider

   .. autoattribute:: BinLookupSession.bins



Bin Query Methods
-----------------

   .. automethod:: BinQuerySession.can_search_bins

   .. autoattribute:: BinQuerySession.bin_query

   .. automethod:: BinQuerySession.get_bins_by_query



Bin Admin Methods
-----------------

   .. automethod:: BinAdminSession.can_create_bins

   .. automethod:: BinAdminSession.can_create_bin_with_record_types

   .. automethod:: BinAdminSession.get_bin_form_for_create

   .. automethod:: BinAdminSession.create_bin

   .. automethod:: BinAdminSession.can_update_bins

   .. automethod:: BinAdminSession.get_bin_form_for_update

   .. automethod:: BinAdminSession.update_bin

   .. automethod:: BinAdminSession.can_delete_bins

   .. automethod:: BinAdminSession.delete_bin

   .. automethod:: BinAdminSession.can_manage_bin_aliases

   .. automethod:: BinAdminSession.alias_bin



Bin Hierarchy Methods
---------------------

   .. autoattribute:: BinHierarchySession.bin_hierarchy_id

   .. autoattribute:: BinHierarchySession.bin_hierarchy

   .. automethod:: BinHierarchySession.can_access_bin_hierarchy

   .. automethod:: BinHierarchySession.use_comparative_bin_view

   .. automethod:: BinHierarchySession.use_plenary_bin_view

   .. autoattribute:: BinHierarchySession.root_bin_ids

   .. autoattribute:: BinHierarchySession.root_bins

   .. automethod:: BinHierarchySession.has_parent_bins

   .. automethod:: BinHierarchySession.is_parent_of_bin

   .. automethod:: BinHierarchySession.get_parent_bin_ids

   .. automethod:: BinHierarchySession.get_parent_bins

   .. automethod:: BinHierarchySession.is_ancestor_of_bin

   .. automethod:: BinHierarchySession.has_child_bins

   .. automethod:: BinHierarchySession.is_child_of_bin

   .. automethod:: BinHierarchySession.get_child_bin_ids

   .. automethod:: BinHierarchySession.get_child_bins

   .. automethod:: BinHierarchySession.is_descendant_of_bin

   .. automethod:: BinHierarchySession.get_bin_node_ids

   .. automethod:: BinHierarchySession.get_bin_nodes



Bin Hierarchy Design Methods
----------------------------

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy_id

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.can_modify_bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.add_root_bin

   .. automethod:: BinHierarchyDesignSession.remove_root_bin

   .. automethod:: BinHierarchyDesignSession.add_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bins



Resource Lookup Methods
-----------------------

   .. autoattribute:: ResourceLookupSession.bin_id

   .. autoattribute:: ResourceLookupSession.bin

   .. automethod:: ResourceLookupSession.can_lookup_resources

   .. automethod:: ResourceLookupSession.use_comparative_resource_view

   .. automethod:: ResourceLookupSession.use_plenary_resource_view

   .. automethod:: ResourceLookupSession.use_federated_bin_view

   .. automethod:: ResourceLookupSession.use_isolated_bin_view

   .. automethod:: ResourceLookupSession.get_resource

   .. automethod:: ResourceLookupSession.get_resources_by_ids

   .. automethod:: ResourceLookupSession.get_resources_by_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_parent_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_record_type

   .. autoattribute:: ResourceLookupSession.resources



Resource Query Methods
----------------------

   .. autoattribute:: ResourceQuerySession.bin_id

   .. autoattribute:: ResourceQuerySession.bin

   .. automethod:: ResourceQuerySession.can_search_resources

   .. automethod:: ResourceQuerySession.use_federated_bin_view

   .. automethod:: ResourceQuerySession.use_isolated_bin_view

   .. autoattribute:: ResourceQuerySession.resource_query

   .. automethod:: ResourceQuerySession.get_resources_by_query



Resource Search Methods
-----------------------

   .. autoattribute:: ResourceSearchSession.resource_search

   .. autoattribute:: ResourceSearchSession.resource_search_order

   .. automethod:: ResourceSearchSession.get_resources_by_search

   .. automethod:: ResourceSearchSession.get_resource_query_from_inspector



Resource Admin Methods
----------------------

   .. autoattribute:: ResourceAdminSession.bin_id

   .. autoattribute:: ResourceAdminSession.bin

   .. automethod:: ResourceAdminSession.can_create_resources

   .. automethod:: ResourceAdminSession.can_create_resource_with_record_types

   .. automethod:: ResourceAdminSession.get_resource_form_for_create

   .. automethod:: ResourceAdminSession.create_resource

   .. automethod:: ResourceAdminSession.can_update_resources

   .. automethod:: ResourceAdminSession.get_resource_form_for_update

   .. automethod:: ResourceAdminSession.update_resource

   .. automethod:: ResourceAdminSession.can_delete_resources

   .. automethod:: ResourceAdminSession.delete_resource

   .. automethod:: ResourceAdminSession.can_manage_resource_aliases

   .. automethod:: ResourceAdminSession.alias_resource



Resource Notification Methods
-----------------------------

   .. autoattribute:: ResourceNotificationSession.bin_id

   .. autoattribute:: ResourceNotificationSession.bin

   .. automethod:: ResourceNotificationSession.can_register_for_resource_notifications

   .. automethod:: ResourceNotificationSession.use_federated_bin_view

   .. automethod:: ResourceNotificationSession.use_isolated_bin_view

   .. automethod:: ResourceNotificationSession.register_for_new_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resource

   .. automethod:: ResourceNotificationSession.register_for_deleted_resources

   .. automethod:: ResourceNotificationSession.register_for_deleted_resource

   .. automethod:: ResourceNotificationSession.reliable_resource_notifications

   .. automethod:: ResourceNotificationSession.unreliable_resource_notifications

   .. automethod:: ResourceNotificationSession.acknowledge_resource_notification



Resource Agent Methods
----------------------

   .. autoattribute:: ResourceAgentSession.bin_id

   .. autoattribute:: ResourceAgentSession.bin

   .. automethod:: ResourceAgentSession.can_lookup_resource_agent_mappings

   .. automethod:: ResourceAgentSession.use_comparative_agent_view

   .. automethod:: ResourceAgentSession.use_plenary_agent_view

   .. automethod:: ResourceAgentSession.use_federated_bin_view

   .. automethod:: ResourceAgentSession.use_isolated_bin_view

   .. automethod:: ResourceAgentSession.get_resource_id_by_agent

   .. automethod:: ResourceAgentSession.get_resource_by_agent

   .. automethod:: ResourceAgentSession.get_agent_ids_by_resource

   .. automethod:: ResourceAgentSession.get_agents_by_resource



Resource Agent Assignment Methods
---------------------------------

   .. autoattribute:: ResourceAgentAssignmentSession.bin_id

   .. autoattribute:: ResourceAgentAssignmentSession.bin

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents_to_resource

   .. automethod:: ResourceAgentAssignmentSession.assign_agent_to_resource

   .. automethod:: ResourceAgentAssignmentSession.unassign_agent_from_resource



Resource Node
-------------

.. autoclass:: ResourceNode
   :show-inheritance:

   .. autoattribute:: ResourceNode.resource

   .. autoattribute:: ResourceNode.parent_resource_nodes

   .. autoattribute:: ResourceNode.child_resource_nodes



Resource Bin Methods
--------------------

   .. automethod:: ResourceBinSession.use_comparative_bin_view

   .. automethod:: ResourceBinSession.use_plenary_bin_view

   .. automethod:: ResourceBinSession.can_lookup_resource_bin_mappings

   .. automethod:: ResourceBinSession.get_resource_ids_by_bin

   .. automethod:: ResourceBinSession.get_resources_by_bin

   .. automethod:: ResourceBinSession.get_resource_ids_by_bins

   .. automethod:: ResourceBinSession.get_resources_by_bins

   .. automethod:: ResourceBinSession.get_bin_ids_by_resource

   .. automethod:: ResourceBinSession.get_bins_by_resource



Resource Bin Assignment Methods
-------------------------------

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources_to_bin

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource

   .. automethod:: ResourceBinAssignmentSession.assign_resource_to_bin

   .. automethod:: ResourceBinAssignmentSession.unassign_resource_from_bin



Bin Lookup Methods
------------------

   .. automethod:: BinLookupSession.can_lookup_bins

   .. automethod:: BinLookupSession.use_comparative_bin_view

   .. automethod:: BinLookupSession.use_plenary_bin_view

   .. automethod:: BinLookupSession.get_bin

   .. automethod:: BinLookupSession.get_bins_by_ids

   .. automethod:: BinLookupSession.get_bins_by_genus_type

   .. automethod:: BinLookupSession.get_bins_by_parent_genus_type

   .. automethod:: BinLookupSession.get_bins_by_record_type

   .. automethod:: BinLookupSession.get_bins_by_provider

   .. autoattribute:: BinLookupSession.bins



Bin Query Methods
-----------------

   .. automethod:: BinQuerySession.can_search_bins

   .. autoattribute:: BinQuerySession.bin_query

   .. automethod:: BinQuerySession.get_bins_by_query



Bin Admin Methods
-----------------

   .. automethod:: BinAdminSession.can_create_bins

   .. automethod:: BinAdminSession.can_create_bin_with_record_types

   .. automethod:: BinAdminSession.get_bin_form_for_create

   .. automethod:: BinAdminSession.create_bin

   .. automethod:: BinAdminSession.can_update_bins

   .. automethod:: BinAdminSession.get_bin_form_for_update

   .. automethod:: BinAdminSession.update_bin

   .. automethod:: BinAdminSession.can_delete_bins

   .. automethod:: BinAdminSession.delete_bin

   .. automethod:: BinAdminSession.can_manage_bin_aliases

   .. automethod:: BinAdminSession.alias_bin



Bin Hierarchy Methods
---------------------

   .. autoattribute:: BinHierarchySession.bin_hierarchy_id

   .. autoattribute:: BinHierarchySession.bin_hierarchy

   .. automethod:: BinHierarchySession.can_access_bin_hierarchy

   .. automethod:: BinHierarchySession.use_comparative_bin_view

   .. automethod:: BinHierarchySession.use_plenary_bin_view

   .. autoattribute:: BinHierarchySession.root_bin_ids

   .. autoattribute:: BinHierarchySession.root_bins

   .. automethod:: BinHierarchySession.has_parent_bins

   .. automethod:: BinHierarchySession.is_parent_of_bin

   .. automethod:: BinHierarchySession.get_parent_bin_ids

   .. automethod:: BinHierarchySession.get_parent_bins

   .. automethod:: BinHierarchySession.is_ancestor_of_bin

   .. automethod:: BinHierarchySession.has_child_bins

   .. automethod:: BinHierarchySession.is_child_of_bin

   .. automethod:: BinHierarchySession.get_child_bin_ids

   .. automethod:: BinHierarchySession.get_child_bins

   .. automethod:: BinHierarchySession.is_descendant_of_bin

   .. automethod:: BinHierarchySession.get_bin_node_ids

   .. automethod:: BinHierarchySession.get_bin_nodes



Bin Hierarchy Design Methods
----------------------------

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy_id

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.can_modify_bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.add_root_bin

   .. automethod:: BinHierarchyDesignSession.remove_root_bin

   .. automethod:: BinHierarchyDesignSession.add_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bins



Resource Lookup Methods
-----------------------

   .. autoattribute:: ResourceLookupSession.bin_id

   .. autoattribute:: ResourceLookupSession.bin

   .. automethod:: ResourceLookupSession.can_lookup_resources

   .. automethod:: ResourceLookupSession.use_comparative_resource_view

   .. automethod:: ResourceLookupSession.use_plenary_resource_view

   .. automethod:: ResourceLookupSession.use_federated_bin_view

   .. automethod:: ResourceLookupSession.use_isolated_bin_view

   .. automethod:: ResourceLookupSession.get_resource

   .. automethod:: ResourceLookupSession.get_resources_by_ids

   .. automethod:: ResourceLookupSession.get_resources_by_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_parent_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_record_type

   .. autoattribute:: ResourceLookupSession.resources



Resource Query Methods
----------------------

   .. autoattribute:: ResourceQuerySession.bin_id

   .. autoattribute:: ResourceQuerySession.bin

   .. automethod:: ResourceQuerySession.can_search_resources

   .. automethod:: ResourceQuerySession.use_federated_bin_view

   .. automethod:: ResourceQuerySession.use_isolated_bin_view

   .. autoattribute:: ResourceQuerySession.resource_query

   .. automethod:: ResourceQuerySession.get_resources_by_query



Resource Search Methods
-----------------------

   .. autoattribute:: ResourceSearchSession.resource_search

   .. autoattribute:: ResourceSearchSession.resource_search_order

   .. automethod:: ResourceSearchSession.get_resources_by_search

   .. automethod:: ResourceSearchSession.get_resource_query_from_inspector



Resource Admin Methods
----------------------

   .. autoattribute:: ResourceAdminSession.bin_id

   .. autoattribute:: ResourceAdminSession.bin

   .. automethod:: ResourceAdminSession.can_create_resources

   .. automethod:: ResourceAdminSession.can_create_resource_with_record_types

   .. automethod:: ResourceAdminSession.get_resource_form_for_create

   .. automethod:: ResourceAdminSession.create_resource

   .. automethod:: ResourceAdminSession.can_update_resources

   .. automethod:: ResourceAdminSession.get_resource_form_for_update

   .. automethod:: ResourceAdminSession.update_resource

   .. automethod:: ResourceAdminSession.can_delete_resources

   .. automethod:: ResourceAdminSession.delete_resource

   .. automethod:: ResourceAdminSession.can_manage_resource_aliases

   .. automethod:: ResourceAdminSession.alias_resource



Resource Notification Methods
-----------------------------

   .. autoattribute:: ResourceNotificationSession.bin_id

   .. autoattribute:: ResourceNotificationSession.bin

   .. automethod:: ResourceNotificationSession.can_register_for_resource_notifications

   .. automethod:: ResourceNotificationSession.use_federated_bin_view

   .. automethod:: ResourceNotificationSession.use_isolated_bin_view

   .. automethod:: ResourceNotificationSession.register_for_new_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resource

   .. automethod:: ResourceNotificationSession.register_for_deleted_resources

   .. automethod:: ResourceNotificationSession.register_for_deleted_resource

   .. automethod:: ResourceNotificationSession.reliable_resource_notifications

   .. automethod:: ResourceNotificationSession.unreliable_resource_notifications

   .. automethod:: ResourceNotificationSession.acknowledge_resource_notification



Resource Agent Methods
----------------------

   .. autoattribute:: ResourceAgentSession.bin_id

   .. autoattribute:: ResourceAgentSession.bin

   .. automethod:: ResourceAgentSession.can_lookup_resource_agent_mappings

   .. automethod:: ResourceAgentSession.use_comparative_agent_view

   .. automethod:: ResourceAgentSession.use_plenary_agent_view

   .. automethod:: ResourceAgentSession.use_federated_bin_view

   .. automethod:: ResourceAgentSession.use_isolated_bin_view

   .. automethod:: ResourceAgentSession.get_resource_id_by_agent

   .. automethod:: ResourceAgentSession.get_resource_by_agent

   .. automethod:: ResourceAgentSession.get_agent_ids_by_resource

   .. automethod:: ResourceAgentSession.get_agents_by_resource



Resource Agent Assignment Methods
---------------------------------

   .. autoattribute:: ResourceAgentAssignmentSession.bin_id

   .. autoattribute:: ResourceAgentAssignmentSession.bin

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents_to_resource

   .. automethod:: ResourceAgentAssignmentSession.assign_agent_to_resource

   .. automethod:: ResourceAgentAssignmentSession.unassign_agent_from_resource



Resource Node List
------------------

.. autoclass:: ResourceNodeList
   :show-inheritance:

   .. autoattribute:: ResourceNodeList.next_resource_node

   .. automethod:: ResourceNodeList.get_next_resource_nodes



Resource Bin Methods
--------------------

   .. automethod:: ResourceBinSession.use_comparative_bin_view

   .. automethod:: ResourceBinSession.use_plenary_bin_view

   .. automethod:: ResourceBinSession.can_lookup_resource_bin_mappings

   .. automethod:: ResourceBinSession.get_resource_ids_by_bin

   .. automethod:: ResourceBinSession.get_resources_by_bin

   .. automethod:: ResourceBinSession.get_resource_ids_by_bins

   .. automethod:: ResourceBinSession.get_resources_by_bins

   .. automethod:: ResourceBinSession.get_bin_ids_by_resource

   .. automethod:: ResourceBinSession.get_bins_by_resource



Resource Bin Assignment Methods
-------------------------------

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources_to_bin

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource

   .. automethod:: ResourceBinAssignmentSession.assign_resource_to_bin

   .. automethod:: ResourceBinAssignmentSession.unassign_resource_from_bin



Bin Lookup Methods
------------------

   .. automethod:: BinLookupSession.can_lookup_bins

   .. automethod:: BinLookupSession.use_comparative_bin_view

   .. automethod:: BinLookupSession.use_plenary_bin_view

   .. automethod:: BinLookupSession.get_bin

   .. automethod:: BinLookupSession.get_bins_by_ids

   .. automethod:: BinLookupSession.get_bins_by_genus_type

   .. automethod:: BinLookupSession.get_bins_by_parent_genus_type

   .. automethod:: BinLookupSession.get_bins_by_record_type

   .. automethod:: BinLookupSession.get_bins_by_provider

   .. autoattribute:: BinLookupSession.bins



Bin Query Methods
-----------------

   .. automethod:: BinQuerySession.can_search_bins

   .. autoattribute:: BinQuerySession.bin_query

   .. automethod:: BinQuerySession.get_bins_by_query



Bin Admin Methods
-----------------

   .. automethod:: BinAdminSession.can_create_bins

   .. automethod:: BinAdminSession.can_create_bin_with_record_types

   .. automethod:: BinAdminSession.get_bin_form_for_create

   .. automethod:: BinAdminSession.create_bin

   .. automethod:: BinAdminSession.can_update_bins

   .. automethod:: BinAdminSession.get_bin_form_for_update

   .. automethod:: BinAdminSession.update_bin

   .. automethod:: BinAdminSession.can_delete_bins

   .. automethod:: BinAdminSession.delete_bin

   .. automethod:: BinAdminSession.can_manage_bin_aliases

   .. automethod:: BinAdminSession.alias_bin



Bin Hierarchy Methods
---------------------

   .. autoattribute:: BinHierarchySession.bin_hierarchy_id

   .. autoattribute:: BinHierarchySession.bin_hierarchy

   .. automethod:: BinHierarchySession.can_access_bin_hierarchy

   .. automethod:: BinHierarchySession.use_comparative_bin_view

   .. automethod:: BinHierarchySession.use_plenary_bin_view

   .. autoattribute:: BinHierarchySession.root_bin_ids

   .. autoattribute:: BinHierarchySession.root_bins

   .. automethod:: BinHierarchySession.has_parent_bins

   .. automethod:: BinHierarchySession.is_parent_of_bin

   .. automethod:: BinHierarchySession.get_parent_bin_ids

   .. automethod:: BinHierarchySession.get_parent_bins

   .. automethod:: BinHierarchySession.is_ancestor_of_bin

   .. automethod:: BinHierarchySession.has_child_bins

   .. automethod:: BinHierarchySession.is_child_of_bin

   .. automethod:: BinHierarchySession.get_child_bin_ids

   .. automethod:: BinHierarchySession.get_child_bins

   .. automethod:: BinHierarchySession.is_descendant_of_bin

   .. automethod:: BinHierarchySession.get_bin_node_ids

   .. automethod:: BinHierarchySession.get_bin_nodes



Bin Hierarchy Design Methods
----------------------------

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy_id

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.can_modify_bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.add_root_bin

   .. automethod:: BinHierarchyDesignSession.remove_root_bin

   .. automethod:: BinHierarchyDesignSession.add_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bins



Resource Lookup Methods
-----------------------

   .. autoattribute:: ResourceLookupSession.bin_id

   .. autoattribute:: ResourceLookupSession.bin

   .. automethod:: ResourceLookupSession.can_lookup_resources

   .. automethod:: ResourceLookupSession.use_comparative_resource_view

   .. automethod:: ResourceLookupSession.use_plenary_resource_view

   .. automethod:: ResourceLookupSession.use_federated_bin_view

   .. automethod:: ResourceLookupSession.use_isolated_bin_view

   .. automethod:: ResourceLookupSession.get_resource

   .. automethod:: ResourceLookupSession.get_resources_by_ids

   .. automethod:: ResourceLookupSession.get_resources_by_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_parent_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_record_type

   .. autoattribute:: ResourceLookupSession.resources



Resource Query Methods
----------------------

   .. autoattribute:: ResourceQuerySession.bin_id

   .. autoattribute:: ResourceQuerySession.bin

   .. automethod:: ResourceQuerySession.can_search_resources

   .. automethod:: ResourceQuerySession.use_federated_bin_view

   .. automethod:: ResourceQuerySession.use_isolated_bin_view

   .. autoattribute:: ResourceQuerySession.resource_query

   .. automethod:: ResourceQuerySession.get_resources_by_query



Resource Search Methods
-----------------------

   .. autoattribute:: ResourceSearchSession.resource_search

   .. autoattribute:: ResourceSearchSession.resource_search_order

   .. automethod:: ResourceSearchSession.get_resources_by_search

   .. automethod:: ResourceSearchSession.get_resource_query_from_inspector



Resource Admin Methods
----------------------

   .. autoattribute:: ResourceAdminSession.bin_id

   .. autoattribute:: ResourceAdminSession.bin

   .. automethod:: ResourceAdminSession.can_create_resources

   .. automethod:: ResourceAdminSession.can_create_resource_with_record_types

   .. automethod:: ResourceAdminSession.get_resource_form_for_create

   .. automethod:: ResourceAdminSession.create_resource

   .. automethod:: ResourceAdminSession.can_update_resources

   .. automethod:: ResourceAdminSession.get_resource_form_for_update

   .. automethod:: ResourceAdminSession.update_resource

   .. automethod:: ResourceAdminSession.can_delete_resources

   .. automethod:: ResourceAdminSession.delete_resource

   .. automethod:: ResourceAdminSession.can_manage_resource_aliases

   .. automethod:: ResourceAdminSession.alias_resource



Resource Notification Methods
-----------------------------

   .. autoattribute:: ResourceNotificationSession.bin_id

   .. autoattribute:: ResourceNotificationSession.bin

   .. automethod:: ResourceNotificationSession.can_register_for_resource_notifications

   .. automethod:: ResourceNotificationSession.use_federated_bin_view

   .. automethod:: ResourceNotificationSession.use_isolated_bin_view

   .. automethod:: ResourceNotificationSession.register_for_new_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resource

   .. automethod:: ResourceNotificationSession.register_for_deleted_resources

   .. automethod:: ResourceNotificationSession.register_for_deleted_resource

   .. automethod:: ResourceNotificationSession.reliable_resource_notifications

   .. automethod:: ResourceNotificationSession.unreliable_resource_notifications

   .. automethod:: ResourceNotificationSession.acknowledge_resource_notification



Resource Agent Methods
----------------------

   .. autoattribute:: ResourceAgentSession.bin_id

   .. autoattribute:: ResourceAgentSession.bin

   .. automethod:: ResourceAgentSession.can_lookup_resource_agent_mappings

   .. automethod:: ResourceAgentSession.use_comparative_agent_view

   .. automethod:: ResourceAgentSession.use_plenary_agent_view

   .. automethod:: ResourceAgentSession.use_federated_bin_view

   .. automethod:: ResourceAgentSession.use_isolated_bin_view

   .. automethod:: ResourceAgentSession.get_resource_id_by_agent

   .. automethod:: ResourceAgentSession.get_resource_by_agent

   .. automethod:: ResourceAgentSession.get_agent_ids_by_resource

   .. automethod:: ResourceAgentSession.get_agents_by_resource



Resource Agent Assignment Methods
---------------------------------

   .. autoattribute:: ResourceAgentAssignmentSession.bin_id

   .. autoattribute:: ResourceAgentAssignmentSession.bin

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents_to_resource

   .. automethod:: ResourceAgentAssignmentSession.assign_agent_to_resource

   .. automethod:: ResourceAgentAssignmentSession.unassign_agent_from_resource



Bin Form
--------

.. autoclass:: BinForm
   :show-inheritance:

   .. automethod:: BinForm.get_bin_form_record



Resource Bin Methods
--------------------

   .. automethod:: ResourceBinSession.use_comparative_bin_view

   .. automethod:: ResourceBinSession.use_plenary_bin_view

   .. automethod:: ResourceBinSession.can_lookup_resource_bin_mappings

   .. automethod:: ResourceBinSession.get_resource_ids_by_bin

   .. automethod:: ResourceBinSession.get_resources_by_bin

   .. automethod:: ResourceBinSession.get_resource_ids_by_bins

   .. automethod:: ResourceBinSession.get_resources_by_bins

   .. automethod:: ResourceBinSession.get_bin_ids_by_resource

   .. automethod:: ResourceBinSession.get_bins_by_resource



Resource Bin Assignment Methods
-------------------------------

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources_to_bin

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource

   .. automethod:: ResourceBinAssignmentSession.assign_resource_to_bin

   .. automethod:: ResourceBinAssignmentSession.unassign_resource_from_bin



Bin Lookup Methods
------------------

   .. automethod:: BinLookupSession.can_lookup_bins

   .. automethod:: BinLookupSession.use_comparative_bin_view

   .. automethod:: BinLookupSession.use_plenary_bin_view

   .. automethod:: BinLookupSession.get_bin

   .. automethod:: BinLookupSession.get_bins_by_ids

   .. automethod:: BinLookupSession.get_bins_by_genus_type

   .. automethod:: BinLookupSession.get_bins_by_parent_genus_type

   .. automethod:: BinLookupSession.get_bins_by_record_type

   .. automethod:: BinLookupSession.get_bins_by_provider

   .. autoattribute:: BinLookupSession.bins



Bin Query Methods
-----------------

   .. automethod:: BinQuerySession.can_search_bins

   .. autoattribute:: BinQuerySession.bin_query

   .. automethod:: BinQuerySession.get_bins_by_query



Bin Admin Methods
-----------------

   .. automethod:: BinAdminSession.can_create_bins

   .. automethod:: BinAdminSession.can_create_bin_with_record_types

   .. automethod:: BinAdminSession.get_bin_form_for_create

   .. automethod:: BinAdminSession.create_bin

   .. automethod:: BinAdminSession.can_update_bins

   .. automethod:: BinAdminSession.get_bin_form_for_update

   .. automethod:: BinAdminSession.update_bin

   .. automethod:: BinAdminSession.can_delete_bins

   .. automethod:: BinAdminSession.delete_bin

   .. automethod:: BinAdminSession.can_manage_bin_aliases

   .. automethod:: BinAdminSession.alias_bin



Bin Hierarchy Methods
---------------------

   .. autoattribute:: BinHierarchySession.bin_hierarchy_id

   .. autoattribute:: BinHierarchySession.bin_hierarchy

   .. automethod:: BinHierarchySession.can_access_bin_hierarchy

   .. automethod:: BinHierarchySession.use_comparative_bin_view

   .. automethod:: BinHierarchySession.use_plenary_bin_view

   .. autoattribute:: BinHierarchySession.root_bin_ids

   .. autoattribute:: BinHierarchySession.root_bins

   .. automethod:: BinHierarchySession.has_parent_bins

   .. automethod:: BinHierarchySession.is_parent_of_bin

   .. automethod:: BinHierarchySession.get_parent_bin_ids

   .. automethod:: BinHierarchySession.get_parent_bins

   .. automethod:: BinHierarchySession.is_ancestor_of_bin

   .. automethod:: BinHierarchySession.has_child_bins

   .. automethod:: BinHierarchySession.is_child_of_bin

   .. automethod:: BinHierarchySession.get_child_bin_ids

   .. automethod:: BinHierarchySession.get_child_bins

   .. automethod:: BinHierarchySession.is_descendant_of_bin

   .. automethod:: BinHierarchySession.get_bin_node_ids

   .. automethod:: BinHierarchySession.get_bin_nodes



Bin Hierarchy Design Methods
----------------------------

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy_id

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.can_modify_bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.add_root_bin

   .. automethod:: BinHierarchyDesignSession.remove_root_bin

   .. automethod:: BinHierarchyDesignSession.add_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bins



Resource Lookup Methods
-----------------------

   .. autoattribute:: ResourceLookupSession.bin_id

   .. autoattribute:: ResourceLookupSession.bin

   .. automethod:: ResourceLookupSession.can_lookup_resources

   .. automethod:: ResourceLookupSession.use_comparative_resource_view

   .. automethod:: ResourceLookupSession.use_plenary_resource_view

   .. automethod:: ResourceLookupSession.use_federated_bin_view

   .. automethod:: ResourceLookupSession.use_isolated_bin_view

   .. automethod:: ResourceLookupSession.get_resource

   .. automethod:: ResourceLookupSession.get_resources_by_ids

   .. automethod:: ResourceLookupSession.get_resources_by_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_parent_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_record_type

   .. autoattribute:: ResourceLookupSession.resources



Resource Query Methods
----------------------

   .. autoattribute:: ResourceQuerySession.bin_id

   .. autoattribute:: ResourceQuerySession.bin

   .. automethod:: ResourceQuerySession.can_search_resources

   .. automethod:: ResourceQuerySession.use_federated_bin_view

   .. automethod:: ResourceQuerySession.use_isolated_bin_view

   .. autoattribute:: ResourceQuerySession.resource_query

   .. automethod:: ResourceQuerySession.get_resources_by_query



Resource Search Methods
-----------------------

   .. autoattribute:: ResourceSearchSession.resource_search

   .. autoattribute:: ResourceSearchSession.resource_search_order

   .. automethod:: ResourceSearchSession.get_resources_by_search

   .. automethod:: ResourceSearchSession.get_resource_query_from_inspector



Resource Admin Methods
----------------------

   .. autoattribute:: ResourceAdminSession.bin_id

   .. autoattribute:: ResourceAdminSession.bin

   .. automethod:: ResourceAdminSession.can_create_resources

   .. automethod:: ResourceAdminSession.can_create_resource_with_record_types

   .. automethod:: ResourceAdminSession.get_resource_form_for_create

   .. automethod:: ResourceAdminSession.create_resource

   .. automethod:: ResourceAdminSession.can_update_resources

   .. automethod:: ResourceAdminSession.get_resource_form_for_update

   .. automethod:: ResourceAdminSession.update_resource

   .. automethod:: ResourceAdminSession.can_delete_resources

   .. automethod:: ResourceAdminSession.delete_resource

   .. automethod:: ResourceAdminSession.can_manage_resource_aliases

   .. automethod:: ResourceAdminSession.alias_resource



Resource Notification Methods
-----------------------------

   .. autoattribute:: ResourceNotificationSession.bin_id

   .. autoattribute:: ResourceNotificationSession.bin

   .. automethod:: ResourceNotificationSession.can_register_for_resource_notifications

   .. automethod:: ResourceNotificationSession.use_federated_bin_view

   .. automethod:: ResourceNotificationSession.use_isolated_bin_view

   .. automethod:: ResourceNotificationSession.register_for_new_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resource

   .. automethod:: ResourceNotificationSession.register_for_deleted_resources

   .. automethod:: ResourceNotificationSession.register_for_deleted_resource

   .. automethod:: ResourceNotificationSession.reliable_resource_notifications

   .. automethod:: ResourceNotificationSession.unreliable_resource_notifications

   .. automethod:: ResourceNotificationSession.acknowledge_resource_notification



Resource Agent Methods
----------------------

   .. autoattribute:: ResourceAgentSession.bin_id

   .. autoattribute:: ResourceAgentSession.bin

   .. automethod:: ResourceAgentSession.can_lookup_resource_agent_mappings

   .. automethod:: ResourceAgentSession.use_comparative_agent_view

   .. automethod:: ResourceAgentSession.use_plenary_agent_view

   .. automethod:: ResourceAgentSession.use_federated_bin_view

   .. automethod:: ResourceAgentSession.use_isolated_bin_view

   .. automethod:: ResourceAgentSession.get_resource_id_by_agent

   .. automethod:: ResourceAgentSession.get_resource_by_agent

   .. automethod:: ResourceAgentSession.get_agent_ids_by_resource

   .. automethod:: ResourceAgentSession.get_agents_by_resource



Resource Agent Assignment Methods
---------------------------------

   .. autoattribute:: ResourceAgentAssignmentSession.bin_id

   .. autoattribute:: ResourceAgentAssignmentSession.bin

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents_to_resource

   .. automethod:: ResourceAgentAssignmentSession.assign_agent_to_resource

   .. automethod:: ResourceAgentAssignmentSession.unassign_agent_from_resource



Bin List
--------

.. autoclass:: BinList
   :show-inheritance:

   .. autoattribute:: BinList.next_bin

   .. automethod:: BinList.get_next_bins



Resource Bin Methods
--------------------

   .. automethod:: ResourceBinSession.use_comparative_bin_view

   .. automethod:: ResourceBinSession.use_plenary_bin_view

   .. automethod:: ResourceBinSession.can_lookup_resource_bin_mappings

   .. automethod:: ResourceBinSession.get_resource_ids_by_bin

   .. automethod:: ResourceBinSession.get_resources_by_bin

   .. automethod:: ResourceBinSession.get_resource_ids_by_bins

   .. automethod:: ResourceBinSession.get_resources_by_bins

   .. automethod:: ResourceBinSession.get_bin_ids_by_resource

   .. automethod:: ResourceBinSession.get_bins_by_resource



Resource Bin Assignment Methods
-------------------------------

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources_to_bin

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource

   .. automethod:: ResourceBinAssignmentSession.assign_resource_to_bin

   .. automethod:: ResourceBinAssignmentSession.unassign_resource_from_bin



Bin Lookup Methods
------------------

   .. automethod:: BinLookupSession.can_lookup_bins

   .. automethod:: BinLookupSession.use_comparative_bin_view

   .. automethod:: BinLookupSession.use_plenary_bin_view

   .. automethod:: BinLookupSession.get_bin

   .. automethod:: BinLookupSession.get_bins_by_ids

   .. automethod:: BinLookupSession.get_bins_by_genus_type

   .. automethod:: BinLookupSession.get_bins_by_parent_genus_type

   .. automethod:: BinLookupSession.get_bins_by_record_type

   .. automethod:: BinLookupSession.get_bins_by_provider

   .. autoattribute:: BinLookupSession.bins



Bin Query Methods
-----------------

   .. automethod:: BinQuerySession.can_search_bins

   .. autoattribute:: BinQuerySession.bin_query

   .. automethod:: BinQuerySession.get_bins_by_query



Bin Admin Methods
-----------------

   .. automethod:: BinAdminSession.can_create_bins

   .. automethod:: BinAdminSession.can_create_bin_with_record_types

   .. automethod:: BinAdminSession.get_bin_form_for_create

   .. automethod:: BinAdminSession.create_bin

   .. automethod:: BinAdminSession.can_update_bins

   .. automethod:: BinAdminSession.get_bin_form_for_update

   .. automethod:: BinAdminSession.update_bin

   .. automethod:: BinAdminSession.can_delete_bins

   .. automethod:: BinAdminSession.delete_bin

   .. automethod:: BinAdminSession.can_manage_bin_aliases

   .. automethod:: BinAdminSession.alias_bin



Bin Hierarchy Methods
---------------------

   .. autoattribute:: BinHierarchySession.bin_hierarchy_id

   .. autoattribute:: BinHierarchySession.bin_hierarchy

   .. automethod:: BinHierarchySession.can_access_bin_hierarchy

   .. automethod:: BinHierarchySession.use_comparative_bin_view

   .. automethod:: BinHierarchySession.use_plenary_bin_view

   .. autoattribute:: BinHierarchySession.root_bin_ids

   .. autoattribute:: BinHierarchySession.root_bins

   .. automethod:: BinHierarchySession.has_parent_bins

   .. automethod:: BinHierarchySession.is_parent_of_bin

   .. automethod:: BinHierarchySession.get_parent_bin_ids

   .. automethod:: BinHierarchySession.get_parent_bins

   .. automethod:: BinHierarchySession.is_ancestor_of_bin

   .. automethod:: BinHierarchySession.has_child_bins

   .. automethod:: BinHierarchySession.is_child_of_bin

   .. automethod:: BinHierarchySession.get_child_bin_ids

   .. automethod:: BinHierarchySession.get_child_bins

   .. automethod:: BinHierarchySession.is_descendant_of_bin

   .. automethod:: BinHierarchySession.get_bin_node_ids

   .. automethod:: BinHierarchySession.get_bin_nodes



Bin Hierarchy Design Methods
----------------------------

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy_id

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.can_modify_bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.add_root_bin

   .. automethod:: BinHierarchyDesignSession.remove_root_bin

   .. automethod:: BinHierarchyDesignSession.add_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bins



Resource Lookup Methods
-----------------------

   .. autoattribute:: ResourceLookupSession.bin_id

   .. autoattribute:: ResourceLookupSession.bin

   .. automethod:: ResourceLookupSession.can_lookup_resources

   .. automethod:: ResourceLookupSession.use_comparative_resource_view

   .. automethod:: ResourceLookupSession.use_plenary_resource_view

   .. automethod:: ResourceLookupSession.use_federated_bin_view

   .. automethod:: ResourceLookupSession.use_isolated_bin_view

   .. automethod:: ResourceLookupSession.get_resource

   .. automethod:: ResourceLookupSession.get_resources_by_ids

   .. automethod:: ResourceLookupSession.get_resources_by_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_parent_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_record_type

   .. autoattribute:: ResourceLookupSession.resources



Resource Query Methods
----------------------

   .. autoattribute:: ResourceQuerySession.bin_id

   .. autoattribute:: ResourceQuerySession.bin

   .. automethod:: ResourceQuerySession.can_search_resources

   .. automethod:: ResourceQuerySession.use_federated_bin_view

   .. automethod:: ResourceQuerySession.use_isolated_bin_view

   .. autoattribute:: ResourceQuerySession.resource_query

   .. automethod:: ResourceQuerySession.get_resources_by_query



Resource Search Methods
-----------------------

   .. autoattribute:: ResourceSearchSession.resource_search

   .. autoattribute:: ResourceSearchSession.resource_search_order

   .. automethod:: ResourceSearchSession.get_resources_by_search

   .. automethod:: ResourceSearchSession.get_resource_query_from_inspector



Resource Admin Methods
----------------------

   .. autoattribute:: ResourceAdminSession.bin_id

   .. autoattribute:: ResourceAdminSession.bin

   .. automethod:: ResourceAdminSession.can_create_resources

   .. automethod:: ResourceAdminSession.can_create_resource_with_record_types

   .. automethod:: ResourceAdminSession.get_resource_form_for_create

   .. automethod:: ResourceAdminSession.create_resource

   .. automethod:: ResourceAdminSession.can_update_resources

   .. automethod:: ResourceAdminSession.get_resource_form_for_update

   .. automethod:: ResourceAdminSession.update_resource

   .. automethod:: ResourceAdminSession.can_delete_resources

   .. automethod:: ResourceAdminSession.delete_resource

   .. automethod:: ResourceAdminSession.can_manage_resource_aliases

   .. automethod:: ResourceAdminSession.alias_resource



Resource Notification Methods
-----------------------------

   .. autoattribute:: ResourceNotificationSession.bin_id

   .. autoattribute:: ResourceNotificationSession.bin

   .. automethod:: ResourceNotificationSession.can_register_for_resource_notifications

   .. automethod:: ResourceNotificationSession.use_federated_bin_view

   .. automethod:: ResourceNotificationSession.use_isolated_bin_view

   .. automethod:: ResourceNotificationSession.register_for_new_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resource

   .. automethod:: ResourceNotificationSession.register_for_deleted_resources

   .. automethod:: ResourceNotificationSession.register_for_deleted_resource

   .. automethod:: ResourceNotificationSession.reliable_resource_notifications

   .. automethod:: ResourceNotificationSession.unreliable_resource_notifications

   .. automethod:: ResourceNotificationSession.acknowledge_resource_notification



Resource Agent Methods
----------------------

   .. autoattribute:: ResourceAgentSession.bin_id

   .. autoattribute:: ResourceAgentSession.bin

   .. automethod:: ResourceAgentSession.can_lookup_resource_agent_mappings

   .. automethod:: ResourceAgentSession.use_comparative_agent_view

   .. automethod:: ResourceAgentSession.use_plenary_agent_view

   .. automethod:: ResourceAgentSession.use_federated_bin_view

   .. automethod:: ResourceAgentSession.use_isolated_bin_view

   .. automethod:: ResourceAgentSession.get_resource_id_by_agent

   .. automethod:: ResourceAgentSession.get_resource_by_agent

   .. automethod:: ResourceAgentSession.get_agent_ids_by_resource

   .. automethod:: ResourceAgentSession.get_agents_by_resource



Resource Agent Assignment Methods
---------------------------------

   .. autoattribute:: ResourceAgentAssignmentSession.bin_id

   .. autoattribute:: ResourceAgentAssignmentSession.bin

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents_to_resource

   .. automethod:: ResourceAgentAssignmentSession.assign_agent_to_resource

   .. automethod:: ResourceAgentAssignmentSession.unassign_agent_from_resource



Bin Node
--------

.. autoclass:: BinNode
   :show-inheritance:

   .. autoattribute:: BinNode.bin

   .. autoattribute:: BinNode.parent_bin_nodes

   .. autoattribute:: BinNode.child_bin_nodes



Resource Bin Methods
--------------------

   .. automethod:: ResourceBinSession.use_comparative_bin_view

   .. automethod:: ResourceBinSession.use_plenary_bin_view

   .. automethod:: ResourceBinSession.can_lookup_resource_bin_mappings

   .. automethod:: ResourceBinSession.get_resource_ids_by_bin

   .. automethod:: ResourceBinSession.get_resources_by_bin

   .. automethod:: ResourceBinSession.get_resource_ids_by_bins

   .. automethod:: ResourceBinSession.get_resources_by_bins

   .. automethod:: ResourceBinSession.get_bin_ids_by_resource

   .. automethod:: ResourceBinSession.get_bins_by_resource



Resource Bin Assignment Methods
-------------------------------

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources_to_bin

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource

   .. automethod:: ResourceBinAssignmentSession.assign_resource_to_bin

   .. automethod:: ResourceBinAssignmentSession.unassign_resource_from_bin



Bin Lookup Methods
------------------

   .. automethod:: BinLookupSession.can_lookup_bins

   .. automethod:: BinLookupSession.use_comparative_bin_view

   .. automethod:: BinLookupSession.use_plenary_bin_view

   .. automethod:: BinLookupSession.get_bin

   .. automethod:: BinLookupSession.get_bins_by_ids

   .. automethod:: BinLookupSession.get_bins_by_genus_type

   .. automethod:: BinLookupSession.get_bins_by_parent_genus_type

   .. automethod:: BinLookupSession.get_bins_by_record_type

   .. automethod:: BinLookupSession.get_bins_by_provider

   .. autoattribute:: BinLookupSession.bins



Bin Query Methods
-----------------

   .. automethod:: BinQuerySession.can_search_bins

   .. autoattribute:: BinQuerySession.bin_query

   .. automethod:: BinQuerySession.get_bins_by_query



Bin Admin Methods
-----------------

   .. automethod:: BinAdminSession.can_create_bins

   .. automethod:: BinAdminSession.can_create_bin_with_record_types

   .. automethod:: BinAdminSession.get_bin_form_for_create

   .. automethod:: BinAdminSession.create_bin

   .. automethod:: BinAdminSession.can_update_bins

   .. automethod:: BinAdminSession.get_bin_form_for_update

   .. automethod:: BinAdminSession.update_bin

   .. automethod:: BinAdminSession.can_delete_bins

   .. automethod:: BinAdminSession.delete_bin

   .. automethod:: BinAdminSession.can_manage_bin_aliases

   .. automethod:: BinAdminSession.alias_bin



Bin Hierarchy Methods
---------------------

   .. autoattribute:: BinHierarchySession.bin_hierarchy_id

   .. autoattribute:: BinHierarchySession.bin_hierarchy

   .. automethod:: BinHierarchySession.can_access_bin_hierarchy

   .. automethod:: BinHierarchySession.use_comparative_bin_view

   .. automethod:: BinHierarchySession.use_plenary_bin_view

   .. autoattribute:: BinHierarchySession.root_bin_ids

   .. autoattribute:: BinHierarchySession.root_bins

   .. automethod:: BinHierarchySession.has_parent_bins

   .. automethod:: BinHierarchySession.is_parent_of_bin

   .. automethod:: BinHierarchySession.get_parent_bin_ids

   .. automethod:: BinHierarchySession.get_parent_bins

   .. automethod:: BinHierarchySession.is_ancestor_of_bin

   .. automethod:: BinHierarchySession.has_child_bins

   .. automethod:: BinHierarchySession.is_child_of_bin

   .. automethod:: BinHierarchySession.get_child_bin_ids

   .. automethod:: BinHierarchySession.get_child_bins

   .. automethod:: BinHierarchySession.is_descendant_of_bin

   .. automethod:: BinHierarchySession.get_bin_node_ids

   .. automethod:: BinHierarchySession.get_bin_nodes



Bin Hierarchy Design Methods
----------------------------

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy_id

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.can_modify_bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.add_root_bin

   .. automethod:: BinHierarchyDesignSession.remove_root_bin

   .. automethod:: BinHierarchyDesignSession.add_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bins



Resource Lookup Methods
-----------------------

   .. autoattribute:: ResourceLookupSession.bin_id

   .. autoattribute:: ResourceLookupSession.bin

   .. automethod:: ResourceLookupSession.can_lookup_resources

   .. automethod:: ResourceLookupSession.use_comparative_resource_view

   .. automethod:: ResourceLookupSession.use_plenary_resource_view

   .. automethod:: ResourceLookupSession.use_federated_bin_view

   .. automethod:: ResourceLookupSession.use_isolated_bin_view

   .. automethod:: ResourceLookupSession.get_resource

   .. automethod:: ResourceLookupSession.get_resources_by_ids

   .. automethod:: ResourceLookupSession.get_resources_by_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_parent_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_record_type

   .. autoattribute:: ResourceLookupSession.resources



Resource Query Methods
----------------------

   .. autoattribute:: ResourceQuerySession.bin_id

   .. autoattribute:: ResourceQuerySession.bin

   .. automethod:: ResourceQuerySession.can_search_resources

   .. automethod:: ResourceQuerySession.use_federated_bin_view

   .. automethod:: ResourceQuerySession.use_isolated_bin_view

   .. autoattribute:: ResourceQuerySession.resource_query

   .. automethod:: ResourceQuerySession.get_resources_by_query



Resource Search Methods
-----------------------

   .. autoattribute:: ResourceSearchSession.resource_search

   .. autoattribute:: ResourceSearchSession.resource_search_order

   .. automethod:: ResourceSearchSession.get_resources_by_search

   .. automethod:: ResourceSearchSession.get_resource_query_from_inspector



Resource Admin Methods
----------------------

   .. autoattribute:: ResourceAdminSession.bin_id

   .. autoattribute:: ResourceAdminSession.bin

   .. automethod:: ResourceAdminSession.can_create_resources

   .. automethod:: ResourceAdminSession.can_create_resource_with_record_types

   .. automethod:: ResourceAdminSession.get_resource_form_for_create

   .. automethod:: ResourceAdminSession.create_resource

   .. automethod:: ResourceAdminSession.can_update_resources

   .. automethod:: ResourceAdminSession.get_resource_form_for_update

   .. automethod:: ResourceAdminSession.update_resource

   .. automethod:: ResourceAdminSession.can_delete_resources

   .. automethod:: ResourceAdminSession.delete_resource

   .. automethod:: ResourceAdminSession.can_manage_resource_aliases

   .. automethod:: ResourceAdminSession.alias_resource



Resource Notification Methods
-----------------------------

   .. autoattribute:: ResourceNotificationSession.bin_id

   .. autoattribute:: ResourceNotificationSession.bin

   .. automethod:: ResourceNotificationSession.can_register_for_resource_notifications

   .. automethod:: ResourceNotificationSession.use_federated_bin_view

   .. automethod:: ResourceNotificationSession.use_isolated_bin_view

   .. automethod:: ResourceNotificationSession.register_for_new_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resource

   .. automethod:: ResourceNotificationSession.register_for_deleted_resources

   .. automethod:: ResourceNotificationSession.register_for_deleted_resource

   .. automethod:: ResourceNotificationSession.reliable_resource_notifications

   .. automethod:: ResourceNotificationSession.unreliable_resource_notifications

   .. automethod:: ResourceNotificationSession.acknowledge_resource_notification



Resource Agent Methods
----------------------

   .. autoattribute:: ResourceAgentSession.bin_id

   .. autoattribute:: ResourceAgentSession.bin

   .. automethod:: ResourceAgentSession.can_lookup_resource_agent_mappings

   .. automethod:: ResourceAgentSession.use_comparative_agent_view

   .. automethod:: ResourceAgentSession.use_plenary_agent_view

   .. automethod:: ResourceAgentSession.use_federated_bin_view

   .. automethod:: ResourceAgentSession.use_isolated_bin_view

   .. automethod:: ResourceAgentSession.get_resource_id_by_agent

   .. automethod:: ResourceAgentSession.get_resource_by_agent

   .. automethod:: ResourceAgentSession.get_agent_ids_by_resource

   .. automethod:: ResourceAgentSession.get_agents_by_resource



Resource Agent Assignment Methods
---------------------------------

   .. autoattribute:: ResourceAgentAssignmentSession.bin_id

   .. autoattribute:: ResourceAgentAssignmentSession.bin

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents_to_resource

   .. automethod:: ResourceAgentAssignmentSession.assign_agent_to_resource

   .. automethod:: ResourceAgentAssignmentSession.unassign_agent_from_resource



Bin Node List
-------------

.. autoclass:: BinNodeList
   :show-inheritance:

   .. autoattribute:: BinNodeList.next_bin_node

   .. automethod:: BinNodeList.get_next_bin_nodes



Resource Bin Methods
--------------------

   .. automethod:: ResourceBinSession.use_comparative_bin_view

   .. automethod:: ResourceBinSession.use_plenary_bin_view

   .. automethod:: ResourceBinSession.can_lookup_resource_bin_mappings

   .. automethod:: ResourceBinSession.get_resource_ids_by_bin

   .. automethod:: ResourceBinSession.get_resources_by_bin

   .. automethod:: ResourceBinSession.get_resource_ids_by_bins

   .. automethod:: ResourceBinSession.get_resources_by_bins

   .. automethod:: ResourceBinSession.get_bin_ids_by_resource

   .. automethod:: ResourceBinSession.get_bins_by_resource



Resource Bin Assignment Methods
-------------------------------

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources

   .. automethod:: ResourceBinAssignmentSession.can_assign_resources_to_bin

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids

   .. automethod:: ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource

   .. automethod:: ResourceBinAssignmentSession.assign_resource_to_bin

   .. automethod:: ResourceBinAssignmentSession.unassign_resource_from_bin



Bin Lookup Methods
------------------

   .. automethod:: BinLookupSession.can_lookup_bins

   .. automethod:: BinLookupSession.use_comparative_bin_view

   .. automethod:: BinLookupSession.use_plenary_bin_view

   .. automethod:: BinLookupSession.get_bin

   .. automethod:: BinLookupSession.get_bins_by_ids

   .. automethod:: BinLookupSession.get_bins_by_genus_type

   .. automethod:: BinLookupSession.get_bins_by_parent_genus_type

   .. automethod:: BinLookupSession.get_bins_by_record_type

   .. automethod:: BinLookupSession.get_bins_by_provider

   .. autoattribute:: BinLookupSession.bins



Bin Query Methods
-----------------

   .. automethod:: BinQuerySession.can_search_bins

   .. autoattribute:: BinQuerySession.bin_query

   .. automethod:: BinQuerySession.get_bins_by_query



Bin Admin Methods
-----------------

   .. automethod:: BinAdminSession.can_create_bins

   .. automethod:: BinAdminSession.can_create_bin_with_record_types

   .. automethod:: BinAdminSession.get_bin_form_for_create

   .. automethod:: BinAdminSession.create_bin

   .. automethod:: BinAdminSession.can_update_bins

   .. automethod:: BinAdminSession.get_bin_form_for_update

   .. automethod:: BinAdminSession.update_bin

   .. automethod:: BinAdminSession.can_delete_bins

   .. automethod:: BinAdminSession.delete_bin

   .. automethod:: BinAdminSession.can_manage_bin_aliases

   .. automethod:: BinAdminSession.alias_bin



Bin Hierarchy Methods
---------------------

   .. autoattribute:: BinHierarchySession.bin_hierarchy_id

   .. autoattribute:: BinHierarchySession.bin_hierarchy

   .. automethod:: BinHierarchySession.can_access_bin_hierarchy

   .. automethod:: BinHierarchySession.use_comparative_bin_view

   .. automethod:: BinHierarchySession.use_plenary_bin_view

   .. autoattribute:: BinHierarchySession.root_bin_ids

   .. autoattribute:: BinHierarchySession.root_bins

   .. automethod:: BinHierarchySession.has_parent_bins

   .. automethod:: BinHierarchySession.is_parent_of_bin

   .. automethod:: BinHierarchySession.get_parent_bin_ids

   .. automethod:: BinHierarchySession.get_parent_bins

   .. automethod:: BinHierarchySession.is_ancestor_of_bin

   .. automethod:: BinHierarchySession.has_child_bins

   .. automethod:: BinHierarchySession.is_child_of_bin

   .. automethod:: BinHierarchySession.get_child_bin_ids

   .. automethod:: BinHierarchySession.get_child_bins

   .. automethod:: BinHierarchySession.is_descendant_of_bin

   .. automethod:: BinHierarchySession.get_bin_node_ids

   .. automethod:: BinHierarchySession.get_bin_nodes



Bin Hierarchy Design Methods
----------------------------

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy_id

   .. autoattribute:: BinHierarchyDesignSession.bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.can_modify_bin_hierarchy

   .. automethod:: BinHierarchyDesignSession.add_root_bin

   .. automethod:: BinHierarchyDesignSession.remove_root_bin

   .. automethod:: BinHierarchyDesignSession.add_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bin

   .. automethod:: BinHierarchyDesignSession.remove_child_bins



Resource Lookup Methods
-----------------------

   .. autoattribute:: ResourceLookupSession.bin_id

   .. autoattribute:: ResourceLookupSession.bin

   .. automethod:: ResourceLookupSession.can_lookup_resources

   .. automethod:: ResourceLookupSession.use_comparative_resource_view

   .. automethod:: ResourceLookupSession.use_plenary_resource_view

   .. automethod:: ResourceLookupSession.use_federated_bin_view

   .. automethod:: ResourceLookupSession.use_isolated_bin_view

   .. automethod:: ResourceLookupSession.get_resource

   .. automethod:: ResourceLookupSession.get_resources_by_ids

   .. automethod:: ResourceLookupSession.get_resources_by_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_parent_genus_type

   .. automethod:: ResourceLookupSession.get_resources_by_record_type

   .. autoattribute:: ResourceLookupSession.resources



Resource Query Methods
----------------------

   .. autoattribute:: ResourceQuerySession.bin_id

   .. autoattribute:: ResourceQuerySession.bin

   .. automethod:: ResourceQuerySession.can_search_resources

   .. automethod:: ResourceQuerySession.use_federated_bin_view

   .. automethod:: ResourceQuerySession.use_isolated_bin_view

   .. autoattribute:: ResourceQuerySession.resource_query

   .. automethod:: ResourceQuerySession.get_resources_by_query



Resource Search Methods
-----------------------

   .. autoattribute:: ResourceSearchSession.resource_search

   .. autoattribute:: ResourceSearchSession.resource_search_order

   .. automethod:: ResourceSearchSession.get_resources_by_search

   .. automethod:: ResourceSearchSession.get_resource_query_from_inspector



Resource Admin Methods
----------------------

   .. autoattribute:: ResourceAdminSession.bin_id

   .. autoattribute:: ResourceAdminSession.bin

   .. automethod:: ResourceAdminSession.can_create_resources

   .. automethod:: ResourceAdminSession.can_create_resource_with_record_types

   .. automethod:: ResourceAdminSession.get_resource_form_for_create

   .. automethod:: ResourceAdminSession.create_resource

   .. automethod:: ResourceAdminSession.can_update_resources

   .. automethod:: ResourceAdminSession.get_resource_form_for_update

   .. automethod:: ResourceAdminSession.update_resource

   .. automethod:: ResourceAdminSession.can_delete_resources

   .. automethod:: ResourceAdminSession.delete_resource

   .. automethod:: ResourceAdminSession.can_manage_resource_aliases

   .. automethod:: ResourceAdminSession.alias_resource



Resource Notification Methods
-----------------------------

   .. autoattribute:: ResourceNotificationSession.bin_id

   .. autoattribute:: ResourceNotificationSession.bin

   .. automethod:: ResourceNotificationSession.can_register_for_resource_notifications

   .. automethod:: ResourceNotificationSession.use_federated_bin_view

   .. automethod:: ResourceNotificationSession.use_isolated_bin_view

   .. automethod:: ResourceNotificationSession.register_for_new_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resources

   .. automethod:: ResourceNotificationSession.register_for_changed_resource

   .. automethod:: ResourceNotificationSession.register_for_deleted_resources

   .. automethod:: ResourceNotificationSession.register_for_deleted_resource

   .. automethod:: ResourceNotificationSession.reliable_resource_notifications

   .. automethod:: ResourceNotificationSession.unreliable_resource_notifications

   .. automethod:: ResourceNotificationSession.acknowledge_resource_notification



Resource Agent Methods
----------------------

   .. autoattribute:: ResourceAgentSession.bin_id

   .. autoattribute:: ResourceAgentSession.bin

   .. automethod:: ResourceAgentSession.can_lookup_resource_agent_mappings

   .. automethod:: ResourceAgentSession.use_comparative_agent_view

   .. automethod:: ResourceAgentSession.use_plenary_agent_view

   .. automethod:: ResourceAgentSession.use_federated_bin_view

   .. automethod:: ResourceAgentSession.use_isolated_bin_view

   .. automethod:: ResourceAgentSession.get_resource_id_by_agent

   .. automethod:: ResourceAgentSession.get_resource_by_agent

   .. automethod:: ResourceAgentSession.get_agent_ids_by_resource

   .. automethod:: ResourceAgentSession.get_agents_by_resource



Resource Agent Assignment Methods
---------------------------------

   .. autoattribute:: ResourceAgentAssignmentSession.bin_id

   .. autoattribute:: ResourceAgentAssignmentSession.bin

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents

   .. automethod:: ResourceAgentAssignmentSession.can_assign_agents_to_resource

   .. automethod:: ResourceAgentAssignmentSession.assign_agent_to_resource

   .. automethod:: ResourceAgentAssignmentSession.unassign_agent_from_resource



