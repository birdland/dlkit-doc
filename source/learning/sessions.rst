
.. currentmodule:: dlkit.learning.sessions
.. automodule:: dlkit.learning.sessions

Sessions
========


Objective Lookup Session
------------------------

.. autoclass:: ObjectiveLookupSession
   :show-inheritance:

   .. autoattribute:: ObjectiveLookupSession.objective_bank_id

   .. autoattribute:: ObjectiveLookupSession.objective_bank

   .. automethod:: ObjectiveLookupSession.can_lookup_objectives

   .. automethod:: ObjectiveLookupSession.use_comparative_objective_view

   .. automethod:: ObjectiveLookupSession.use_plenary_objective_view

   .. automethod:: ObjectiveLookupSession.use_federated_objective_bank_view

   .. automethod:: ObjectiveLookupSession.use_isolated_objective_bank_view

   .. automethod:: ObjectiveLookupSession.get_objective

   .. automethod:: ObjectiveLookupSession.get_objectives_by_ids

   .. automethod:: ObjectiveLookupSession.get_objectives_by_genus_type

   .. automethod:: ObjectiveLookupSession.get_objectives_by_parent_genus_type

   .. automethod:: ObjectiveLookupSession.get_objectives_by_record_type

   .. autoattribute:: ObjectiveLookupSession.objectives

Objective Query Session
-----------------------

.. autoclass:: ObjectiveQuerySession
   :show-inheritance:

   .. autoattribute:: ObjectiveQuerySession.objective_bank_id

   .. autoattribute:: ObjectiveQuerySession.objective_bank

   .. automethod:: ObjectiveQuerySession.can_search_objectives

   .. automethod:: ObjectiveQuerySession.use_federated_objective_bank_view

   .. automethod:: ObjectiveQuerySession.use_isolated_objective_bank_view

   .. autoattribute:: ObjectiveQuerySession.objective_query

   .. automethod:: ObjectiveQuerySession.get_objectives_by_query

Objective Admin Session
-----------------------

.. autoclass:: ObjectiveAdminSession
   :show-inheritance:

   .. autoattribute:: ObjectiveAdminSession.objective_bank_id

   .. autoattribute:: ObjectiveAdminSession.objective_bank

   .. automethod:: ObjectiveAdminSession.can_create_objectives

   .. automethod:: ObjectiveAdminSession.can_create_objective_with_record_types

   .. automethod:: ObjectiveAdminSession.get_objective_form_for_create

   .. automethod:: ObjectiveAdminSession.create_objective

   .. automethod:: ObjectiveAdminSession.can_update_objectives

   .. automethod:: ObjectiveAdminSession.get_objective_form_for_update

   .. automethod:: ObjectiveAdminSession.update_objective

   .. automethod:: ObjectiveAdminSession.can_delete_objectives

   .. automethod:: ObjectiveAdminSession.delete_objective

   .. automethod:: ObjectiveAdminSession.can_manage_objective_aliases

   .. automethod:: ObjectiveAdminSession.alias_objective

Objective Hierarchy Session
---------------------------

.. autoclass:: ObjectiveHierarchySession
   :show-inheritance:

   .. autoattribute:: ObjectiveHierarchySession.objective_hierarchy_id

   .. autoattribute:: ObjectiveHierarchySession.objective_hierarchy

   .. automethod:: ObjectiveHierarchySession.can_access_objective_hierarchy

   .. automethod:: ObjectiveHierarchySession.use_comparative_objective_view

   .. automethod:: ObjectiveHierarchySession.use_plenary_objective_view

   .. autoattribute:: ObjectiveHierarchySession.root_objective_ids

   .. autoattribute:: ObjectiveHierarchySession.root_objectives

   .. automethod:: ObjectiveHierarchySession.has_parent_objectives

   .. automethod:: ObjectiveHierarchySession.is_parent_of_objective

   .. automethod:: ObjectiveHierarchySession.get_parent_objective_ids

   .. automethod:: ObjectiveHierarchySession.get_parent_objectives

   .. automethod:: ObjectiveHierarchySession.is_ancestor_of_objective

   .. automethod:: ObjectiveHierarchySession.has_child_objectives

   .. automethod:: ObjectiveHierarchySession.is_child_of_objective

   .. automethod:: ObjectiveHierarchySession.get_child_objective_ids

   .. automethod:: ObjectiveHierarchySession.get_child_objectives

   .. automethod:: ObjectiveHierarchySession.is_descendant_of_objective

   .. automethod:: ObjectiveHierarchySession.get_objective_node_ids

   .. automethod:: ObjectiveHierarchySession.get_objective_nodes

Objective Hierarchy Design Session
----------------------------------

.. autoclass:: ObjectiveHierarchyDesignSession
   :show-inheritance:

   .. autoattribute:: ObjectiveHierarchyDesignSession.objective_hierarchy_id

   .. autoattribute:: ObjectiveHierarchyDesignSession.objective_hierarchy

   .. automethod:: ObjectiveHierarchyDesignSession.can_modify_objective_hierarchy

   .. automethod:: ObjectiveHierarchyDesignSession.add_root_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_root_objective

   .. automethod:: ObjectiveHierarchyDesignSession.add_child_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_child_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_child_objectives

Objective Sequencing Session
----------------------------

.. autoclass:: ObjectiveSequencingSession
   :show-inheritance:

   .. autoattribute:: ObjectiveSequencingSession.objective_hierarchy_id

   .. autoattribute:: ObjectiveSequencingSession.objective_hierarchy

   .. automethod:: ObjectiveSequencingSession.can_sequence_objectives

   .. automethod:: ObjectiveSequencingSession.move_objective_ahead

   .. automethod:: ObjectiveSequencingSession.move_objective_behind

   .. automethod:: ObjectiveSequencingSession.sequence_objectives

Objective Objective Bank Session
--------------------------------

.. autoclass:: ObjectiveObjectiveBankSession
   :show-inheritance:

   .. automethod:: ObjectiveObjectiveBankSession.can_lookup_objective_objective_bank_mappings

   .. automethod:: ObjectiveObjectiveBankSession.use_comparative_objective_bank_view

   .. automethod:: ObjectiveObjectiveBankSession.use_plenary_objective_bank_view

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_ids_by_objective_bank

   .. automethod:: ObjectiveObjectiveBankSession.get_objectives_by_objective_bank

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_ids_by_objective_banks

   .. automethod:: ObjectiveObjectiveBankSession.get_objectives_by_objective_banks

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_bank_ids_by_objective

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_banks_by_objective

Objective Objective Bank Assignment Session
-------------------------------------------

.. autoclass:: ObjectiveObjectiveBankAssignmentSession
   :show-inheritance:

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.can_assign_objectives

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.can_assign_objectives_to_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_objective

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.assign_objective_to_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.unassign_objective_from_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.reassign_proficiency_to_objective_bank

Objective Requisite Session
---------------------------

.. autoclass:: ObjectiveRequisiteSession
   :show-inheritance:

   .. autoattribute:: ObjectiveRequisiteSession.objective_bank_id

   .. autoattribute:: ObjectiveRequisiteSession.objective_bank

   .. automethod:: ObjectiveRequisiteSession.can_lookup_objective_prerequisites

   .. automethod:: ObjectiveRequisiteSession.use_comparative_objective_view

   .. automethod:: ObjectiveRequisiteSession.use_plenary_objective_view

   .. automethod:: ObjectiveRequisiteSession.use_federated_objective_bank_view

   .. automethod:: ObjectiveRequisiteSession.use_isolated_objective_bank_view

   .. automethod:: ObjectiveRequisiteSession.get_requisite_objectives

   .. automethod:: ObjectiveRequisiteSession.get_all_requisite_objectives

   .. automethod:: ObjectiveRequisiteSession.get_dependent_objectives

   .. automethod:: ObjectiveRequisiteSession.is_objective_required

   .. automethod:: ObjectiveRequisiteSession.get_equivalent_objectives

Objective Requisite Assignment Session
--------------------------------------

.. autoclass:: ObjectiveRequisiteAssignmentSession
   :show-inheritance:

   .. autoattribute:: ObjectiveRequisiteAssignmentSession.objective_bank_id

   .. autoattribute:: ObjectiveRequisiteAssignmentSession.objective_bank

   .. automethod:: ObjectiveRequisiteAssignmentSession.can_assign_requisites

   .. automethod:: ObjectiveRequisiteAssignmentSession.assign_objective_requisite

   .. automethod:: ObjectiveRequisiteAssignmentSession.unassign_objective_requisite

   .. automethod:: ObjectiveRequisiteAssignmentSession.assign_equivalent_objective

   .. automethod:: ObjectiveRequisiteAssignmentSession.unassign_equivalent_objective

Activity Lookup Session
-----------------------

.. autoclass:: ActivityLookupSession
   :show-inheritance:

   .. autoattribute:: ActivityLookupSession.objective_bank_id

   .. autoattribute:: ActivityLookupSession.objective_bank

   .. automethod:: ActivityLookupSession.can_lookup_activities

   .. automethod:: ActivityLookupSession.use_comparative_activity_view

   .. automethod:: ActivityLookupSession.use_plenary_activity_view

   .. automethod:: ActivityLookupSession.use_federated_objective_bank_view

   .. automethod:: ActivityLookupSession.use_isolated_objective_bank_view

   .. automethod:: ActivityLookupSession.get_activity

   .. automethod:: ActivityLookupSession.get_activities_by_ids

   .. automethod:: ActivityLookupSession.get_activities_by_genus_type

   .. automethod:: ActivityLookupSession.get_activities_by_parent_genus_type

   .. automethod:: ActivityLookupSession.get_activities_by_record_type

   .. automethod:: ActivityLookupSession.get_activities_for_objective

   .. automethod:: ActivityLookupSession.get_activities_for_objectives

   .. automethod:: ActivityLookupSession.get_activities_by_asset

   .. automethod:: ActivityLookupSession.get_activities_by_assets

   .. autoattribute:: ActivityLookupSession.activities

Activity Admin Session
----------------------

.. autoclass:: ActivityAdminSession
   :show-inheritance:

   .. autoattribute:: ActivityAdminSession.objective_bank_id

   .. autoattribute:: ActivityAdminSession.objective_bank

   .. automethod:: ActivityAdminSession.can_create_activities

   .. automethod:: ActivityAdminSession.can_create_activity_with_record_types

   .. automethod:: ActivityAdminSession.get_activity_form_for_create

   .. automethod:: ActivityAdminSession.create_activity

   .. automethod:: ActivityAdminSession.can_update_activities

   .. automethod:: ActivityAdminSession.get_activity_form_for_update

   .. automethod:: ActivityAdminSession.update_activity

   .. automethod:: ActivityAdminSession.can_delete_activities

   .. automethod:: ActivityAdminSession.delete_activity

   .. automethod:: ActivityAdminSession.can_manage_activity_aliases

   .. automethod:: ActivityAdminSession.alias_activity

Activity Objective Bank Session
-------------------------------

.. autoclass:: ActivityObjectiveBankSession
   :show-inheritance:

   .. automethod:: ActivityObjectiveBankSession.can_lookup_activity_objective_bank_mappings

   .. automethod:: ActivityObjectiveBankSession.use_comparative_objective_bank_view

   .. automethod:: ActivityObjectiveBankSession.use_plenary_objective_bank_view

   .. automethod:: ActivityObjectiveBankSession.get_activity_ids_by_objective_bank

   .. automethod:: ActivityObjectiveBankSession.get_activities_by_objective_bank

   .. automethod:: ActivityObjectiveBankSession.get_activity_ids_by_objective_banks

   .. automethod:: ActivityObjectiveBankSession.get_activities_by_objective_banks

   .. automethod:: ActivityObjectiveBankSession.get_objective_bank_ids_by_activity

   .. automethod:: ActivityObjectiveBankSession.get_objective_banks_by_activity

Activity Objective Bank Assignment Session
------------------------------------------

.. autoclass:: ActivityObjectiveBankAssignmentSession
   :show-inheritance:

   .. automethod:: ActivityObjectiveBankAssignmentSession.can_assign_activities

   .. automethod:: ActivityObjectiveBankAssignmentSession.can_assign_activities_to_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.get_assignable_objective_bank_ids

   .. automethod:: ActivityObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_activity

   .. automethod:: ActivityObjectiveBankAssignmentSession.assign_activity_to_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.unassign_activity_from_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.reassign_activity_to_objective_bank

Proficiency Lookup Session
--------------------------

.. autoclass:: ProficiencyLookupSession
   :show-inheritance:

   .. autoattribute:: ProficiencyLookupSession.objective_bank_id

   .. autoattribute:: ProficiencyLookupSession.objective_bank

   .. automethod:: ProficiencyLookupSession.can_lookup_proficiencies

   .. automethod:: ProficiencyLookupSession.use_comparative_proficiency_view

   .. automethod:: ProficiencyLookupSession.use_plenary_proficiency_view

   .. automethod:: ProficiencyLookupSession.use_federated_objective_bank_view

   .. automethod:: ProficiencyLookupSession.use_isolated_objective_bank_view

   .. automethod:: ProficiencyLookupSession.use_effective_proficiency_view

   .. automethod:: ProficiencyLookupSession.use_any_effective_proficiency_view

   .. automethod:: ProficiencyLookupSession.get_proficiency

   .. automethod:: ProficiencyLookupSession.get_proficiencies_by_ids

   .. automethod:: ProficiencyLookupSession.get_proficiencies_by_genus_type

   .. automethod:: ProficiencyLookupSession.get_proficiencies_by_parent_genus_type

   .. automethod:: ProficiencyLookupSession.get_proficiencies_by_record_type

   .. automethod:: ProficiencyLookupSession.get_proficiencies_on_date

   .. automethod:: ProficiencyLookupSession.get_proficiencies_by_genus_type_on_date

   .. automethod:: ProficiencyLookupSession.get_proficiencies_for_objective

   .. automethod:: ProficiencyLookupSession.get_proficiencies_for_objective_on_date

   .. automethod:: ProficiencyLookupSession.get_proficiencies_by_genus_type_for_objective

   .. automethod:: ProficiencyLookupSession.get_proficiencies_by_genus_type_for_objective_on_date

   .. automethod:: ProficiencyLookupSession.get_proficiencies_for_objectives

   .. automethod:: ProficiencyLookupSession.get_proficiencies_for_resource

   .. automethod:: ProficiencyLookupSession.get_proficiencies_for_resource_on_date

   .. automethod:: ProficiencyLookupSession.get_proficiencies_by_genus_type_for_resource

   .. automethod:: ProficiencyLookupSession.get_proficiencies_by_genus_type_for_resource_on_date

   .. automethod:: ProficiencyLookupSession.get_proficiencies_for_resources

   .. automethod:: ProficiencyLookupSession.get_proficiencies_for_objective_and_resource

   .. automethod:: ProficiencyLookupSession.get_proficiencies_for_objective_and_resource_on_date

   .. automethod:: ProficiencyLookupSession.get_proficiencies_by_genus_type_for_objective_and_resource

   .. automethod:: ProficiencyLookupSession.get_proficiencies_by_genus_type_for_objective_and_resource_on_date

   .. autoattribute:: ProficiencyLookupSession.proficiencies

Proficiency Query Session
-------------------------

.. autoclass:: ProficiencyQuerySession
   :show-inheritance:

   .. autoattribute:: ProficiencyQuerySession.objective_bank_id

   .. autoattribute:: ProficiencyQuerySession.objective_bank

   .. automethod:: ProficiencyQuerySession.can_search_proficiencies

   .. automethod:: ProficiencyQuerySession.use_federated_objective_bank_view

   .. automethod:: ProficiencyQuerySession.use_isolated_objective_bank_view

   .. autoattribute:: ProficiencyQuerySession.proficiency_query

   .. automethod:: ProficiencyQuerySession.get_proficiencies_by_query

Proficiency Admin Session
-------------------------

.. autoclass:: ProficiencyAdminSession
   :show-inheritance:

   .. autoattribute:: ProficiencyAdminSession.objective_bank_id

   .. autoattribute:: ProficiencyAdminSession.objective_bank

   .. automethod:: ProficiencyAdminSession.can_create_proficiencies

   .. automethod:: ProficiencyAdminSession.can_create_proficiency_with_record_types

   .. automethod:: ProficiencyAdminSession.get_proficiency_form_for_create

   .. automethod:: ProficiencyAdminSession.create_proficiency

   .. automethod:: ProficiencyAdminSession.can_update_proficiencies

   .. automethod:: ProficiencyAdminSession.get_proficiency_form_for_update

   .. automethod:: ProficiencyAdminSession.update_proficiency

   .. automethod:: ProficiencyAdminSession.can_delete_proficiencies

   .. automethod:: ProficiencyAdminSession.delete_proficiency

   .. automethod:: ProficiencyAdminSession.delete_proficiencies

   .. automethod:: ProficiencyAdminSession.can_manage_proficiency_aliases

   .. automethod:: ProficiencyAdminSession.alias_proficiency

Objective Bank Lookup Session
-----------------------------

.. autoclass:: ObjectiveBankLookupSession
   :show-inheritance:

   .. automethod:: ObjectiveBankLookupSession.can_lookup_objective_banks

   .. automethod:: ObjectiveBankLookupSession.use_comparative_objective_bank_view

   .. automethod:: ObjectiveBankLookupSession.use_plenary_objective_bank_view

   .. automethod:: ObjectiveBankLookupSession.get_objective_bank

   .. automethod:: ObjectiveBankLookupSession.get_objective_banks_by_ids

   .. automethod:: ObjectiveBankLookupSession.get_objective_banks_by_genus_type

   .. automethod:: ObjectiveBankLookupSession.get_objective_banks_by_parent_genus_type

   .. automethod:: ObjectiveBankLookupSession.get_objective_banks_by_record_type

   .. automethod:: ObjectiveBankLookupSession.get_objective_banks_by_provider

   .. autoattribute:: ObjectiveBankLookupSession.objective_banks

Objective Bank Admin Session
----------------------------

.. autoclass:: ObjectiveBankAdminSession
   :show-inheritance:

   .. automethod:: ObjectiveBankAdminSession.can_create_objective_banks

   .. automethod:: ObjectiveBankAdminSession.can_create_objective_bank_with_record_types

   .. automethod:: ObjectiveBankAdminSession.get_objective_bank_form_for_create

   .. automethod:: ObjectiveBankAdminSession.create_objective_bank

   .. automethod:: ObjectiveBankAdminSession.can_update_objective_banks

   .. automethod:: ObjectiveBankAdminSession.get_objective_bank_form_for_update

   .. automethod:: ObjectiveBankAdminSession.update_objective_bank

   .. automethod:: ObjectiveBankAdminSession.can_delete_objective_banks

   .. automethod:: ObjectiveBankAdminSession.delete_objective_bank

   .. automethod:: ObjectiveBankAdminSession.can_manage_objective_bank_aliases

   .. automethod:: ObjectiveBankAdminSession.alias_objective_bank

Objective Bank Hierarchy Session
--------------------------------

.. autoclass:: ObjectiveBankHierarchySession
   :show-inheritance:

   .. autoattribute:: ObjectiveBankHierarchySession.objective_bank_hierarchy_id

   .. autoattribute:: ObjectiveBankHierarchySession.objective_bank_hierarchy

   .. automethod:: ObjectiveBankHierarchySession.can_access_objective_bank_hierarchy

   .. automethod:: ObjectiveBankHierarchySession.use_comparative_objective_bank_view

   .. automethod:: ObjectiveBankHierarchySession.use_plenary_objective_bank_view

   .. autoattribute:: ObjectiveBankHierarchySession.root_objective_bank_ids

   .. autoattribute:: ObjectiveBankHierarchySession.root_objective_banks

   .. automethod:: ObjectiveBankHierarchySession.has_parent_objective_banks

   .. automethod:: ObjectiveBankHierarchySession.is_parent_of_objective_bank

   .. automethod:: ObjectiveBankHierarchySession.get_parent_objective_bank_ids

   .. automethod:: ObjectiveBankHierarchySession.get_parent_objective_banks

   .. automethod:: ObjectiveBankHierarchySession.is_ancestor_of_objective_bank

   .. automethod:: ObjectiveBankHierarchySession.has_child_objective_banks

   .. automethod:: ObjectiveBankHierarchySession.is_child_of_objective_bank

   .. automethod:: ObjectiveBankHierarchySession.get_child_objective_bank_ids

   .. automethod:: ObjectiveBankHierarchySession.get_child_objective_banks

   .. automethod:: ObjectiveBankHierarchySession.is_descendant_of_objective_bank

   .. automethod:: ObjectiveBankHierarchySession.get_objective_bank_node_ids

   .. automethod:: ObjectiveBankHierarchySession.get_objective_bank_nodes

Objective Bank Hierarchy Design Session
---------------------------------------

.. autoclass:: ObjectiveBankHierarchyDesignSession
   :show-inheritance:

   .. autoattribute:: ObjectiveBankHierarchyDesignSession.objective_bank_hierarchy_id

   .. autoattribute:: ObjectiveBankHierarchyDesignSession.objective_bank_hierarchy

   .. automethod:: ObjectiveBankHierarchyDesignSession.can_modify_objective_bank_hierarchy

   .. automethod:: ObjectiveBankHierarchyDesignSession.add_root_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_root_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.add_child_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_child_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_child_objective_banks

