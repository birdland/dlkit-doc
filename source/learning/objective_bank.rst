.. currentmodule:: dlkit.services.learning


Objective_Bank
==============


Objective Bank
--------------

.. autoclass:: ObjectiveBank
   :show-inheritance:

   .. automethod:: ObjectiveBank.get_objective_bank_record



Objective Lookup Methods
------------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_lookup_objectives

   .. automethod:: ObjectiveBank.use_comparative_objective_view

   .. automethod:: ObjectiveBank.use_plenary_objective_view

   .. automethod:: ObjectiveBank.use_federated_objective_bank_view

   .. automethod:: ObjectiveBank.use_isolated_objective_bank_view

   .. automethod:: ObjectiveBank.get_objective

   .. automethod:: ObjectiveBank.get_objectives_by_ids

   .. automethod:: ObjectiveBank.get_objectives_by_genus_type

   .. automethod:: ObjectiveBank.get_objectives_by_parent_genus_type

   .. automethod:: ObjectiveBank.get_objectives_by_record_type

   .. autoattribute:: ObjectiveBank.objectives



Objective Query Methods
-----------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_search_objectives

   .. automethod:: ObjectiveBank.use_federated_objective_bank_view

   .. automethod:: ObjectiveBank.use_isolated_objective_bank_view

   .. autoattribute:: ObjectiveBank.objective_query

   .. automethod:: ObjectiveBank.get_objectives_by_query



Objective Search Methods
------------------------

   .. autoattribute:: ObjectiveBank.objective_search

   .. autoattribute:: ObjectiveBank.objective_search_order

   .. automethod:: ObjectiveBank.get_objectives_by_search

   .. automethod:: ObjectiveBank.get_objective_query_from_inspector



Objective Admin Methods
-----------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_create_objectives

   .. automethod:: ObjectiveBank.can_create_objective_with_record_types

   .. automethod:: ObjectiveBank.get_objective_form_for_create

   .. automethod:: ObjectiveBank.create_objective

   .. automethod:: ObjectiveBank.can_update_objectives

   .. automethod:: ObjectiveBank.get_objective_form_for_update

   .. automethod:: ObjectiveBank.update_objective

   .. automethod:: ObjectiveBank.can_delete_objectives

   .. automethod:: ObjectiveBank.delete_objective

   .. automethod:: ObjectiveBank.can_manage_objective_aliases

   .. automethod:: ObjectiveBank.alias_objective



Objective Notification Methods
------------------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_register_for_objective_notifications

   .. automethod:: ObjectiveBank.use_federated_objective_bank_view

   .. automethod:: ObjectiveBank.use_isolated_objective_bank_view

   .. automethod:: ObjectiveBank.register_for_new_objectives

   .. automethod:: ObjectiveBank.register_for_new_objective_ancestors

   .. automethod:: ObjectiveBank.register_for_new_objective_descendants

   .. automethod:: ObjectiveBank.register_for_changed_objectives

   .. automethod:: ObjectiveBank.register_for_changed_objective

   .. automethod:: ObjectiveBank.register_for_deleted_objectives

   .. automethod:: ObjectiveBank.register_for_deleted_objective

   .. automethod:: ObjectiveBank.register_for_deleted_objective_ancestors

   .. automethod:: ObjectiveBank.register_for_deleted_objective_descendants



Objective Hierarchy Methods
---------------------------

   .. autoattribute:: ObjectiveBank.objective_hierarchy_id

   .. autoattribute:: ObjectiveBank.objective_hierarchy

   .. automethod:: ObjectiveBank.can_access_objective_hierarchy

   .. automethod:: ObjectiveBank.use_comparative_objective_view

   .. automethod:: ObjectiveBank.use_plenary_objective_view

   .. autoattribute:: ObjectiveBank.root_objective_ids

   .. autoattribute:: ObjectiveBank.root_objectives

   .. automethod:: ObjectiveBank.has_parent_objectives

   .. automethod:: ObjectiveBank.is_parent_of_objective

   .. automethod:: ObjectiveBank.get_parent_objective_ids

   .. automethod:: ObjectiveBank.get_parent_objectives

   .. automethod:: ObjectiveBank.is_ancestor_of_objective

   .. automethod:: ObjectiveBank.has_child_objectives

   .. automethod:: ObjectiveBank.is_child_of_objective

   .. automethod:: ObjectiveBank.get_child_objective_ids

   .. automethod:: ObjectiveBank.get_child_objectives

   .. automethod:: ObjectiveBank.is_descendant_of_objective

   .. automethod:: ObjectiveBank.get_objective_node_ids

   .. automethod:: ObjectiveBank.get_objective_nodes



Objective Hierarchy Design Methods
----------------------------------

   .. autoattribute:: ObjectiveBank.objective_hierarchy_id

   .. autoattribute:: ObjectiveBank.objective_hierarchy

   .. automethod:: ObjectiveBank.can_modify_objective_hierarchy

   .. automethod:: ObjectiveBank.add_root_objective

   .. automethod:: ObjectiveBank.remove_root_objective

   .. automethod:: ObjectiveBank.add_child_objective

   .. automethod:: ObjectiveBank.remove_child_objective

   .. automethod:: ObjectiveBank.remove_child_objectives



Objective Sequencing Methods
----------------------------

   .. autoattribute:: ObjectiveBank.objective_hierarchy_id

   .. autoattribute:: ObjectiveBank.objective_hierarchy

   .. automethod:: ObjectiveBank.can_sequence_objectives

   .. automethod:: ObjectiveBank.move_objective_ahead

   .. automethod:: ObjectiveBank.move_objective_behind

   .. automethod:: ObjectiveBank.sequence_objectives



Objective Objective Bank Methods
--------------------------------

   .. automethod:: ObjectiveBank.can_lookup_objective_objective_bank_mappings

   .. automethod:: ObjectiveBank.use_comparative_objective_bank_view

   .. automethod:: ObjectiveBank.use_plenary_objective_bank_view

   .. automethod:: ObjectiveBank.get_objective_ids_by_objective_bank

   .. automethod:: ObjectiveBank.get_objectives_by_objective_bank

   .. automethod:: ObjectiveBank.get_objective_ids_by_objective_banks

   .. automethod:: ObjectiveBank.get_objectives_by_objective_banks

   .. automethod:: ObjectiveBank.get_objective_bank_ids_by_objective

   .. automethod:: ObjectiveBank.get_objective_banks_by_objective



Objective Objective Bank Assignment Methods
-------------------------------------------

   .. automethod:: ObjectiveBank.can_assign_objectives

   .. automethod:: ObjectiveBank.can_assign_objectives_to_objective_bank

   .. automethod:: ObjectiveBank.get_assignable_objective_bank_ids

   .. automethod:: ObjectiveBank.get_assignable_objective_bank_ids_for_objective

   .. automethod:: ObjectiveBank.assign_objective_to_objective_bank

   .. automethod:: ObjectiveBank.unassign_objective_from_objective_bank



Objective Smart Objective Bank Methods
--------------------------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_manage_smart_objective_banks

   .. autoattribute:: ObjectiveBank.objective_query

   .. autoattribute:: ObjectiveBank.objective_search_order

   .. automethod:: ObjectiveBank.apply_objective_query

   .. automethod:: ObjectiveBank.inspect_objective_query

   .. automethod:: ObjectiveBank.apply_objective_sequencing

   .. automethod:: ObjectiveBank.get_objective_query_from_inspector



Objective Requisite Methods
---------------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_lookup_objective_prerequisites

   .. automethod:: ObjectiveBank.use_comparative_objective_view

   .. automethod:: ObjectiveBank.use_plenary_objective_view

   .. automethod:: ObjectiveBank.use_federated_objective_bank_view

   .. automethod:: ObjectiveBank.use_isolated_objective_bank_view

   .. automethod:: ObjectiveBank.get_requisite_objectives

   .. automethod:: ObjectiveBank.get_all_requisite_objectives

   .. automethod:: ObjectiveBank.get_dependent_objectives

   .. automethod:: ObjectiveBank.is_objective_required

   .. automethod:: ObjectiveBank.get_equivalent_objectives



Objective Requisite Assignment Methods
--------------------------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_assign_requisites

   .. automethod:: ObjectiveBank.assign_objective_requisite

   .. automethod:: ObjectiveBank.unassign_objective_requisite

   .. automethod:: ObjectiveBank.assign_equivalent_objective

   .. automethod:: ObjectiveBank.unassign_equivalent_objective



Activity Lookup Methods
-----------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_lookup_activities

   .. automethod:: ObjectiveBank.use_comparative_activity_view

   .. automethod:: ObjectiveBank.use_plenary_activity_view

   .. automethod:: ObjectiveBank.use_federated_objective_bank_view

   .. automethod:: ObjectiveBank.use_isolated_objective_bank_view

   .. automethod:: ObjectiveBank.get_activity

   .. automethod:: ObjectiveBank.get_activities_by_ids

   .. automethod:: ObjectiveBank.get_activities_by_genus_type

   .. automethod:: ObjectiveBank.get_activities_by_parent_genus_type

   .. automethod:: ObjectiveBank.get_activities_by_record_type

   .. automethod:: ObjectiveBank.get_activities_for_objective

   .. automethod:: ObjectiveBank.get_activities_for_objectives

   .. automethod:: ObjectiveBank.get_activities_by_asset

   .. automethod:: ObjectiveBank.get_activities_by_assets

   .. autoattribute:: ObjectiveBank.activities



Activity Query Methods
----------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_search_activities

   .. automethod:: ObjectiveBank.use_federated_objective_bank_view

   .. automethod:: ObjectiveBank.use_isolated_objective_bank_view

   .. autoattribute:: ObjectiveBank.activity_query

   .. automethod:: ObjectiveBank.get_activities_by_query



Activity Search Methods
-----------------------

   .. autoattribute:: ObjectiveBank.activity_search

   .. autoattribute:: ObjectiveBank.activity_search_order

   .. automethod:: ObjectiveBank.get_activities_by_search

   .. automethod:: ObjectiveBank.get_activity_query_from_inspector



Activity Admin Methods
----------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_create_activities

   .. automethod:: ObjectiveBank.can_create_activity_with_record_types

   .. automethod:: ObjectiveBank.get_activity_form_for_create

   .. automethod:: ObjectiveBank.create_activity

   .. automethod:: ObjectiveBank.can_update_activities

   .. automethod:: ObjectiveBank.get_activity_form_for_update

   .. automethod:: ObjectiveBank.update_activity

   .. automethod:: ObjectiveBank.can_delete_activities

   .. automethod:: ObjectiveBank.delete_activity

   .. automethod:: ObjectiveBank.can_manage_activity_aliases

   .. automethod:: ObjectiveBank.alias_activity



Activity Notification Methods
-----------------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_register_for_activity_notifications

   .. automethod:: ObjectiveBank.use_federated_objective_bank_view

   .. automethod:: ObjectiveBank.use_isolated_objective_bank_view

   .. automethod:: ObjectiveBank.register_for_new_activities

   .. automethod:: ObjectiveBank.register_for_new_activities_for_objective

   .. automethod:: ObjectiveBank.register_for_changed_activities

   .. automethod:: ObjectiveBank.register_for_changed_activities_for_objective

   .. automethod:: ObjectiveBank.register_for_changed_activity

   .. automethod:: ObjectiveBank.register_for_deleted_activities

   .. automethod:: ObjectiveBank.register_for_deleted_activities_for_objective

   .. automethod:: ObjectiveBank.register_for_deleted_activity



Activity Objective Bank Methods
-------------------------------

   .. automethod:: ObjectiveBank.can_lookup_activity_objective_bank_mappings

   .. automethod:: ObjectiveBank.use_comparative_objective_bank_view

   .. automethod:: ObjectiveBank.use_plenary_objective_bank_view

   .. automethod:: ObjectiveBank.get_activity_ids_by_objective_bank

   .. automethod:: ObjectiveBank.get_activities_by_objective_bank

   .. automethod:: ObjectiveBank.get_activity_ids_by_objective_banks

   .. automethod:: ObjectiveBank.get_activities_by_objective_banks

   .. automethod:: ObjectiveBank.get_objective_bank_ids_by_activity

   .. automethod:: ObjectiveBank.get_objective_banks_by_activity



Activity Objective Bank Assignment Methods
------------------------------------------

   .. automethod:: ObjectiveBank.can_assign_activities

   .. automethod:: ObjectiveBank.can_assign_activities_to_objective_bank

   .. automethod:: ObjectiveBank.get_assignable_objective_bank_ids

   .. automethod:: ObjectiveBank.get_assignable_objective_bank_ids_for_activity

   .. automethod:: ObjectiveBank.assign_activity_to_objective_bank

   .. automethod:: ObjectiveBank.unassign_activity_from_objective_bank



Activity Smart Objective Bank Methods
-------------------------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_manage_smart_objective_banks

   .. autoattribute:: ObjectiveBank.activity_query

   .. autoattribute:: ObjectiveBank.activity_search_order

   .. automethod:: ObjectiveBank.apply_activity_query

   .. automethod:: ObjectiveBank.inspect_activity_query

   .. automethod:: ObjectiveBank.apply_activity_sequencing

   .. automethod:: ObjectiveBank.get_activity_query_from_inspector



Proficiency Lookup Methods
--------------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_lookup_proficiencies

   .. automethod:: ObjectiveBank.use_comparative_proficiency_view

   .. automethod:: ObjectiveBank.use_plenary_proficiency_view

   .. automethod:: ObjectiveBank.use_federated_objective_bank_view

   .. automethod:: ObjectiveBank.use_isolated_objective_bank_view

   .. automethod:: ObjectiveBank.use_effective_proficiency_view

   .. automethod:: ObjectiveBank.use_any_effective_proficiency_view

   .. automethod:: ObjectiveBank.get_proficiency

   .. automethod:: ObjectiveBank.get_proficiencies_by_ids

   .. automethod:: ObjectiveBank.get_proficiencies_by_genus_type

   .. automethod:: ObjectiveBank.get_proficiencies_by_parent_genus_type

   .. automethod:: ObjectiveBank.get_proficiencies_by_record_type

   .. automethod:: ObjectiveBank.get_proficiencies_on_date

   .. automethod:: ObjectiveBank.get_proficiencies_for_objective

   .. automethod:: ObjectiveBank.get_proficiencies_for_objective_on_date

   .. automethod:: ObjectiveBank.get_proficiencies_by_genus_type_for_objective

   .. automethod:: ObjectiveBank.get_proficiencies_by_genus_type_for_objective_on_date

   .. automethod:: ObjectiveBank.get_proficiencies_for_objectives

   .. automethod:: ObjectiveBank.get_proficiencies_for_resource

   .. automethod:: ObjectiveBank.get_proficiencies_for_resource_on_date

   .. automethod:: ObjectiveBank.get_proficiencies_by_genus_type_for_resource

   .. automethod:: ObjectiveBank.get_proficiencies_by_genus_type_for_resource_on_date

   .. automethod:: ObjectiveBank.get_proficiencies_for_resources

   .. automethod:: ObjectiveBank.get_proficiencies_for_objective_and_resource

   .. automethod:: ObjectiveBank.get_proficiencies_for_objective_and_resource_on_date

   .. automethod:: ObjectiveBank.get_proficiencies_by_genus_type_for_objective_and_resource

   .. automethod:: ObjectiveBank.get_proficiencies_by_genus_type_for_objective_and_resource_on_date

   .. autoattribute:: ObjectiveBank.proficiencies



Proficiency Query Methods
-------------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_search_proficiencies

   .. automethod:: ObjectiveBank.use_federated_objective_bank_view

   .. automethod:: ObjectiveBank.use_isolated_objective_bank_view

   .. autoattribute:: ObjectiveBank.proficiency_query

   .. automethod:: ObjectiveBank.get_proficiencies_by_query



Proficiency Search Methods
--------------------------

   .. autoattribute:: ObjectiveBank.proficiency_search

   .. autoattribute:: ObjectiveBank.proficiency_search_order

   .. automethod:: ObjectiveBank.get_proficiencies_by_search

   .. automethod:: ObjectiveBank.get_proficiency_query_from_inspector



Proficiency Admin Methods
-------------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_create_proficiencies

   .. automethod:: ObjectiveBank.can_create_proficiency_with_record_types

   .. automethod:: ObjectiveBank.get_proficiency_form_for_create

   .. automethod:: ObjectiveBank.create_proficiency

   .. automethod:: ObjectiveBank.can_update_proficiencies

   .. automethod:: ObjectiveBank.get_proficiency_form_for_update

   .. automethod:: ObjectiveBank.update_proficiency

   .. automethod:: ObjectiveBank.can_delete_proficiencies

   .. automethod:: ObjectiveBank.delete_proficiency

   .. automethod:: ObjectiveBank.delete_proficiencies

   .. automethod:: ObjectiveBank.can_manage_proficiency_aliases

   .. automethod:: ObjectiveBank.alias_proficiency



Proficiency Notification Methods
--------------------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_register_for_proficiency_notifications

   .. automethod:: ObjectiveBank.use_federated_objective_bank_view

   .. automethod:: ObjectiveBank.use_isolated_objective_bank_view

   .. automethod:: ObjectiveBank.register_for_new_proficiencies

   .. automethod:: ObjectiveBank.register_for_new_proficiencies_by_genus_type

   .. automethod:: ObjectiveBank.register_for_new_proficiencies_for_objective

   .. automethod:: ObjectiveBank.register_for_new_proficiencies_for_resource

   .. automethod:: ObjectiveBank.register_for_changed_proficiencies

   .. automethod:: ObjectiveBank.register_for_changed_proficiencies_by_genus_type

   .. automethod:: ObjectiveBank.register_for_changed_proficiency_for_objective

   .. automethod:: ObjectiveBank.register_for_changed_proficiency_for_resource

   .. automethod:: ObjectiveBank.register_for_changed_proficiency

   .. automethod:: ObjectiveBank.register_for_deleted_proficiencies

   .. automethod:: ObjectiveBank.register_for_deleted_proficiencies_by_genus_type

   .. automethod:: ObjectiveBank.register_for_deleted_proficiency_for_objective

   .. automethod:: ObjectiveBank.register_for_deleted_proficiency_for_resource

   .. automethod:: ObjectiveBank.register_for_deleted_proficiency



Proficiency Objective Bank Methods
----------------------------------

   .. automethod:: ObjectiveBank.can_lookup_proficiency_objective_bank_mappings

   .. automethod:: ObjectiveBank.use_comparative_proficiency_objective_bank_view

   .. automethod:: ObjectiveBank.use_plenary_proficiency_objective_bank_view

   .. automethod:: ObjectiveBank.get_proficiency_ids_by_objective_bank

   .. automethod:: ObjectiveBank.get_proficiencies_by_objective_bank

   .. automethod:: ObjectiveBank.get_proficiency_ids_by_objective_banks

   .. automethod:: ObjectiveBank.get_proficiencies_by_objective_banks

   .. automethod:: ObjectiveBank.get_objective_bank_ids_by_proficiency

   .. automethod:: ObjectiveBank.get_objective_banks_by_proficiency



Proficiency Objective Bank Assignment Methods
---------------------------------------------

   .. automethod:: ObjectiveBank.can_assign_proficiencies

   .. automethod:: ObjectiveBank.can_assign_proficiencies_to_objective_bank

   .. automethod:: ObjectiveBank.get_assignable_objective_bank_ids

   .. automethod:: ObjectiveBank.get_assignable_objective_bank_ids_for_proficiency

   .. automethod:: ObjectiveBank.assign_proficiency_to_objective_bank

   .. automethod:: ObjectiveBank.unassign_proficiency_from_objective_bank



Proficiency Smart Objective Bank Methods
----------------------------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_manage_smart_objective_banks

   .. autoattribute:: ObjectiveBank.proficiency_query

   .. autoattribute:: ObjectiveBank.proficiency_search_order

   .. automethod:: ObjectiveBank.apply_proficiency_query

   .. automethod:: ObjectiveBank.inspect_proficiency_query

   .. automethod:: ObjectiveBank.apply_proficiency_sequencing

   .. automethod:: ObjectiveBank.get_proficiency_query_from_inspector



My Learning Path Methods
------------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_lookup_learning_paths

   .. automethod:: ObjectiveBank.use_comparative_proficiency_view

   .. automethod:: ObjectiveBank.use_plenary_proficiency_view

   .. automethod:: ObjectiveBank.use_federated_objective_bank_view

   .. automethod:: ObjectiveBank.use_isolated_objective_bank_view

   .. automethod:: ObjectiveBank.find_path

   .. automethod:: ObjectiveBank.find_path_at_proficiency

   .. automethod:: ObjectiveBank.get_objectives_by_completion



Learning Path Methods
---------------------

   .. autoattribute:: ObjectiveBank.objective_bank_id

   .. autoattribute:: ObjectiveBank.objective_bank

   .. automethod:: ObjectiveBank.can_lookup_learning_paths

   .. automethod:: ObjectiveBank.use_comparative_proficiency_view

   .. automethod:: ObjectiveBank.use_plenary_proficiency_view

   .. automethod:: ObjectiveBank.use_federated_objective_bank_view

   .. automethod:: ObjectiveBank.use_isolated_objective_bank_view

   .. automethod:: ObjectiveBank.find_path_for_resource

   .. automethod:: ObjectiveBank.find_path_for_resource_at_proficiency

   .. automethod:: ObjectiveBank.get_objectives_for_resource_by_completion



