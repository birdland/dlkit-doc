.. currentmodule:: dlkit_doc.resource
.. automodule:: dlkit_doc.resource

Bin
===


Bin
---

.. autoclass:: Bin
   :show-inheritance:

.. automethod:: Bin.get_bin_record



Resource Lookup Methods
-----------------------

.. autoattribute:: Bin.bin_id

.. autoattribute:: Bin.bin

.. automethod:: Bin.can_lookup_resources

.. automethod:: Bin.use_comparative_resource_view

.. automethod:: Bin.use_plenary_resource_view

.. automethod:: Bin.use_federated_bin_view

.. automethod:: Bin.use_isolated_bin_view

.. automethod:: Bin.get_resource

.. automethod:: Bin.get_resources_by_ids

.. automethod:: Bin.get_resources_by_genus_type

.. automethod:: Bin.get_resources_by_parent_genus_type

.. automethod:: Bin.get_resources_by_record_type

.. autoattribute:: Bin.resources



Resource Query Methods
----------------------

.. autoattribute:: Bin.bin_id

.. autoattribute:: Bin.bin

.. automethod:: Bin.can_search_resources

.. automethod:: Bin.use_federated_bin_view

.. automethod:: Bin.use_isolated_bin_view

.. autoattribute:: Bin.resource_query

.. automethod:: Bin.get_resources_by_query



Resource Search Methods
-----------------------

.. autoattribute:: Bin.resource_search

.. autoattribute:: Bin.resource_search_order

.. automethod:: Bin.get_resources_by_search

.. automethod:: Bin.get_resource_query_from_inspector



Resource Admin Methods
----------------------

.. autoattribute:: Bin.bin_id

.. autoattribute:: Bin.bin

.. automethod:: Bin.can_create_resources

.. automethod:: Bin.can_create_resource_with_record_types

.. automethod:: Bin.get_resource_form_for_create

.. automethod:: Bin.create_resource

.. automethod:: Bin.can_update_resources

.. automethod:: Bin.get_resource_form_for_update

.. automethod:: Bin.update_resource

.. automethod:: Bin.can_delete_resources

.. automethod:: Bin.delete_resource

.. automethod:: Bin.can_manage_resource_aliases

.. automethod:: Bin.alias_resource



Resource Notification Methods
-----------------------------

.. autoattribute:: Bin.bin_id

.. autoattribute:: Bin.bin

.. automethod:: Bin.can_register_for_resource_notifications

.. automethod:: Bin.use_federated_bin_view

.. automethod:: Bin.use_isolated_bin_view

.. automethod:: Bin.register_for_new_resources

.. automethod:: Bin.register_for_changed_resources

.. automethod:: Bin.register_for_changed_resource

.. automethod:: Bin.register_for_deleted_resources

.. automethod:: Bin.register_for_deleted_resource



Resource Bin Methods
--------------------

.. automethod:: Bin.use_comparative_bin_view

.. automethod:: Bin.use_plenary_bin_view

.. automethod:: Bin.can_lookup_resource_bin_mappings

.. automethod:: Bin.get_resource_ids_by_bin

.. automethod:: Bin.get_resources_by_bin

.. automethod:: Bin.get_resource_ids_by_bins

.. automethod:: Bin.get_resources_by_bins

.. automethod:: Bin.get_bin_ids_by_resource

.. automethod:: Bin.get_bins_by_resource



Resource Bin Assignment Methods
-------------------------------

.. automethod:: Bin.can_assign_resources

.. automethod:: Bin.can_assign_resources_to_bin

.. automethod:: Bin.get_assignable_bin_ids

.. automethod:: Bin.get_assignable_bin_ids_for_resource

.. automethod:: Bin.assign_resource_to_bin

.. automethod:: Bin.unassign_resource_from_bin



Resource Smart Bin Methods
--------------------------

.. autoattribute:: Bin.bin_id

.. autoattribute:: Bin.bin

.. automethod:: Bin.can_manage_smart_bins

.. autoattribute:: Bin.resource_query

.. autoattribute:: Bin.resource_search_order

.. automethod:: Bin.apply_resource_query

.. automethod:: Bin.inspect_resource_query

.. automethod:: Bin.apply_resource_sequencing

.. automethod:: Bin.get_resource_query_from_inspector



Membership Methods
------------------

.. autoattribute:: Bin.bin_id

.. autoattribute:: Bin.bin

.. automethod:: Bin.can_query_membership

.. automethod:: Bin.use_federated_bin_view

.. automethod:: Bin.use_isolated_bin_view

.. automethod:: Bin.is_member



Group Methods
-------------

.. autoattribute:: Bin.bin_id

.. autoattribute:: Bin.bin

.. automethod:: Bin.can_lookup_resource_members

.. automethod:: Bin.use_comparative_resource_view

.. automethod:: Bin.use_plenary_resource_view

.. automethod:: Bin.use_federated_bin_view

.. automethod:: Bin.use_isolated_bin_view

.. automethod:: Bin.use_federated_group_view

.. automethod:: Bin.use_isolated_group_view

.. automethod:: Bin.get_resource_ids_by_group

.. automethod:: Bin.get_resources_by_group

.. automethod:: Bin.get_resource_ids_by_groups

.. automethod:: Bin.get_resources_by_groups

.. automethod:: Bin.get_group_ids_by_resource

.. automethod:: Bin.get_groups_by_resource



Group Assignment Methods
------------------------

.. autoattribute:: Bin.bin_id

.. autoattribute:: Bin.bin

.. automethod:: Bin.can_assign_resources

.. automethod:: Bin.can_assign_resources_to_group

.. automethod:: Bin.assign_resource_to_group

.. automethod:: Bin.unassign_resource_from_group



Group Notification Methods
--------------------------

.. autoattribute:: Bin.bin_id

.. autoattribute:: Bin.bin

.. automethod:: Bin.can_register_for_group_notifications

.. automethod:: Bin.use_federated_bin_view

.. automethod:: Bin.use_isolated_bin_view

.. automethod:: Bin.register_for_new_members

.. automethod:: Bin.register_for_deleted_members



Group Hierarchy Methods
-----------------------

.. autoattribute:: Bin.bin_id

.. autoattribute:: Bin.bin

.. automethod:: Bin.can_access_group_hierarchy

.. automethod:: Bin.use_comparative_resource_view

.. automethod:: Bin.use_plenary_resource_view

.. automethod:: Bin.use_federated_bin_view

.. automethod:: Bin.use_isolated_bin_view

.. automethod:: Bin.is_member_of_group

.. automethod:: Bin.get_resource_node_ids

.. automethod:: Bin.get_resource_nodes



Resource Agent Methods
----------------------

.. autoattribute:: Bin.bin_id

.. autoattribute:: Bin.bin

.. automethod:: Bin.can_lookup_resource_agent_mappings

.. automethod:: Bin.use_comparative_agent_view

.. automethod:: Bin.use_plenary_agent_view

.. automethod:: Bin.use_federated_bin_view

.. automethod:: Bin.use_isolated_bin_view

.. automethod:: Bin.get_resource_id_by_agent

.. automethod:: Bin.get_resource_by_agent

.. automethod:: Bin.get_agent_ids_by_resource

.. automethod:: Bin.get_agents_by_resource



Resource Agent Assignment Methods
---------------------------------

.. autoattribute:: Bin.bin_id

.. autoattribute:: Bin.bin

.. automethod:: Bin.can_assign_agents

.. automethod:: Bin.can_assign_agents_to_resource

.. automethod:: Bin.assign_agent_to_resource

.. automethod:: Bin.unassign_agent_from_resource



Resource Relationship Lookup Methods
------------------------------------

.. autoattribute:: Bin.bin_id

.. autoattribute:: Bin.bin

.. automethod:: Bin.can_lookup_resource_relationships

.. automethod:: Bin.use_comparative_resource_relationship_view

.. automethod:: Bin.use_plenary_resource_relationship_view

.. automethod:: Bin.use_federated_bin_view

.. automethod:: Bin.use_isolated_bin_view

.. automethod:: Bin.use_effective_resource_relationship_view

.. automethod:: Bin.use_any_effective_resource_relationship_view

.. automethod:: Bin.get_resource_relationship

.. automethod:: Bin.get_resource_relationships_by_ids

.. automethod:: Bin.get_resource_relationships_by_genus_type

.. automethod:: Bin.get_resource_relationships_by_parent_genus_type

.. automethod:: Bin.get_resource_relationships_by_record_type

.. automethod:: Bin.get_resource_relationships_on_date

.. automethod:: Bin.get_resource_relationships_for_source_resource

.. automethod:: Bin.get_resource_relationships_for_source_resource_on_date

.. automethod:: Bin.get_resource_relationships_by_genus_type_for_source_resource

.. automethod:: Bin.get_resource_relationships_by_genus_type_for_source_resource_on_date

.. automethod:: Bin.get_resource_relationships_for_destination_resource

.. automethod:: Bin.get_resource_relationships_for_destination_resource_on_date

.. automethod:: Bin.get_resource_relationships_by_genus_type_for_destination_resource

.. automethod:: Bin.get_resource_relationships_by_genus_type_for_destination_resource_on_date

.. automethod:: Bin.get_resource_relationships_for_resources

.. automethod:: Bin.get_resource_relationships_for_resources_on_date

.. automethod:: Bin.get_resource_relationships_by_genus_type_for_resources

.. automethod:: Bin.get_resource_relationships_by_genus_type_for_resources_on_date

.. autoattribute:: Bin.resource_relationships



Resource Relationship Query Methods
-----------------------------------

.. autoattribute:: Bin.bin_id

.. autoattribute:: Bin.bin

.. automethod:: Bin.can_search_resource_relationships

.. automethod:: Bin.use_federated_bin_view

.. automethod:: Bin.use_isolated_bin_view

.. autoattribute:: Bin.resource_relationship_query

.. automethod:: Bin.get_resource_relationships_by_query



Resource Relationship Search Methods
------------------------------------

.. autoattribute:: Bin.resource_relationship_search

.. autoattribute:: Bin.resource_relationship_search_order

.. automethod:: Bin.get_resource_relationships_by_search

.. automethod:: Bin.get_resource_relationship_query_from_inspector



Resource Relationship Admin Methods
-----------------------------------

.. autoattribute:: Bin.bin_id

.. autoattribute:: Bin.bin

.. automethod:: Bin.can_create_resource_relationships

.. automethod:: Bin.can_create_resource_relationship_with_record_types

.. automethod:: Bin.get_resource_relationship_form_for_create

.. automethod:: Bin.create_resource_relationship

.. automethod:: Bin.can_update_resource_relationships

.. automethod:: Bin.get_resource_relationship_form_for_update

.. automethod:: Bin.update_resource_relationship

.. automethod:: Bin.can_delete_resource_relationships

.. automethod:: Bin.delete_resource_relationship

.. automethod:: Bin.can_manage_resource_relationship_aliases

.. automethod:: Bin.alias_resource_relationship



Resource Relationship Notification Methods
------------------------------------------

.. autoattribute:: Bin.bin_id

.. autoattribute:: Bin.bin

.. automethod:: Bin.can_register_for_resource_relationship_notifications

.. automethod:: Bin.use_federated_bin_view

.. automethod:: Bin.use_isolated_bin_view

.. automethod:: Bin.register_for_new_resource_relationships

.. automethod:: Bin.register_for_new_resource_relationships_by_genus_type

.. automethod:: Bin.register_for_new_resource_relationships_for_resource

.. automethod:: Bin.register_for_changed_resource_relationships

.. automethod:: Bin.register_for_changed_resource_relationships_by_genus_type

.. automethod:: Bin.register_for_changed_resource_relationships_for_resource

.. automethod:: Bin.register_for_changed_resource_relationship

.. automethod:: Bin.register_for_deleted_resource_relationships

.. automethod:: Bin.register_for_deleted_resource_relationships_for_resource

.. automethod:: Bin.register_for_deleted_resource_relationship



Resource Relationship Bin Methods
---------------------------------

.. automethod:: Bin.use_comparative_bin_view

.. automethod:: Bin.use_plenary_bin_view

.. automethod:: Bin.can_lookup_resource_relationship_bin_mappings

.. automethod:: Bin.get_resource_relationship_ids_by_bin

.. automethod:: Bin.get_resource_relationships_by_bin

.. automethod:: Bin.get_resource_relationships_ids_by_bins

.. automethod:: Bin.get_resource_relationships_by_bins

.. automethod:: Bin.get_bin_ids_by_resource_relationship

.. automethod:: Bin.get_bins_by_resource_relationship



Resource Relationship Bin Assignment Methods
--------------------------------------------

.. automethod:: Bin.can_assign_resource_relationships

.. automethod:: Bin.can_assign_resource_relationships_to_bin

.. automethod:: Bin.get_assignable_bin_ids

.. automethod:: Bin.get_assignable_bin_ids_for_resource_relationship

.. automethod:: Bin.assign_resource_relationship_to_bin

.. automethod:: Bin.unassign_resource_relationship_from_bin



Resource Relationship Smart Bin Methods
---------------------------------------

.. autoattribute:: Bin.bin_id

.. autoattribute:: Bin.bin

.. automethod:: Bin.can_manage_smart_bins

.. autoattribute:: Bin.resource_relationship_query

.. autoattribute:: Bin.resource_relationship_search_order

.. automethod:: Bin.apply_resource_relationship_query

.. automethod:: Bin.inspect_resource_relationship_query

.. automethod:: Bin.apply_resource_relationship_sequencing

.. automethod:: Bin.get_resource_relationship_query_from_inspector



