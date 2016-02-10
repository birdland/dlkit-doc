
.. currentmodule:: dlkit.services.resource
.. automodule:: dlkit.services.resource

Service Managers
================


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

   .. autoattribute:: ResourceManager.resource_batch_manager

   .. autoattribute:: ResourceManager.resource_demographic_manager



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



