.. currentmodule:: dlkit.services.learning


Objective Bank
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



