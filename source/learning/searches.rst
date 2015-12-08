
.. currentmodule:: dlkit.learning.searches
.. automodule:: dlkit.learning.searches

Searches
========


Objective Search
----------------

.. autoclass:: ObjectiveSearch
   :show-inheritance:

   .. automethod:: ObjectiveSearch.search_among_objectives

   .. automethod:: ObjectiveSearch.order_objective_results

   .. automethod:: ObjectiveSearch.get_objective_search_record



Objective Objective Bank Methods
--------------------------------

   .. automethod:: ObjectiveObjectiveBankSession.can_lookup_objective_objective_bank_mappings

   .. automethod:: ObjectiveObjectiveBankSession.use_comparative_objective_bank_view

   .. automethod:: ObjectiveObjectiveBankSession.use_plenary_objective_bank_view

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_ids_by_objective_bank

   .. automethod:: ObjectiveObjectiveBankSession.get_objectives_by_objective_bank

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_ids_by_objective_banks

   .. automethod:: ObjectiveObjectiveBankSession.get_objectives_by_objective_banks

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_bank_ids_by_objective

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_banks_by_objective



Objective Objective Bank Assignment Methods
-------------------------------------------

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.can_assign_objectives

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.can_assign_objectives_to_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_objective

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.assign_objective_to_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.unassign_objective_from_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.reassign_proficiency_to_objective_bank



Activity Objective Bank Methods
-------------------------------

   .. automethod:: ActivityObjectiveBankSession.can_lookup_activity_objective_bank_mappings

   .. automethod:: ActivityObjectiveBankSession.use_comparative_objective_bank_view

   .. automethod:: ActivityObjectiveBankSession.use_plenary_objective_bank_view

   .. automethod:: ActivityObjectiveBankSession.get_activity_ids_by_objective_bank

   .. automethod:: ActivityObjectiveBankSession.get_activities_by_objective_bank

   .. automethod:: ActivityObjectiveBankSession.get_activity_ids_by_objective_banks

   .. automethod:: ActivityObjectiveBankSession.get_activities_by_objective_banks

   .. automethod:: ActivityObjectiveBankSession.get_objective_bank_ids_by_activity

   .. automethod:: ActivityObjectiveBankSession.get_objective_banks_by_activity



Activity Objective Bank Assignment Methods
------------------------------------------

   .. automethod:: ActivityObjectiveBankAssignmentSession.can_assign_activities

   .. automethod:: ActivityObjectiveBankAssignmentSession.can_assign_activities_to_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.get_assignable_objective_bank_ids

   .. automethod:: ActivityObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_activity

   .. automethod:: ActivityObjectiveBankAssignmentSession.assign_activity_to_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.unassign_activity_from_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.reassign_activity_to_objective_bank



Objective Bank Lookup Methods
-----------------------------

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



Objective Bank Admin Methods
----------------------------

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



Objective Bank Hierarchy Methods
--------------------------------

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



Objective Bank Hierarchy Design Methods
---------------------------------------

   .. autoattribute:: ObjectiveBankHierarchyDesignSession.objective_bank_hierarchy_id

   .. autoattribute:: ObjectiveBankHierarchyDesignSession.objective_bank_hierarchy

   .. automethod:: ObjectiveBankHierarchyDesignSession.can_modify_objective_bank_hierarchy

   .. automethod:: ObjectiveBankHierarchyDesignSession.add_root_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_root_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.add_child_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_child_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_child_objective_banks



Objective Lookup Methods
------------------------

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



Objective Query Methods
-----------------------

   .. autoattribute:: ObjectiveQuerySession.objective_bank_id

   .. autoattribute:: ObjectiveQuerySession.objective_bank

   .. automethod:: ObjectiveQuerySession.can_search_objectives

   .. automethod:: ObjectiveQuerySession.use_federated_objective_bank_view

   .. automethod:: ObjectiveQuerySession.use_isolated_objective_bank_view

   .. autoattribute:: ObjectiveQuerySession.objective_query

   .. automethod:: ObjectiveQuerySession.get_objectives_by_query



Objective Admin Methods
-----------------------

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



Objective Hierarchy Methods
---------------------------

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



Objective Hierarchy Design Methods
----------------------------------

   .. autoattribute:: ObjectiveHierarchyDesignSession.objective_hierarchy_id

   .. autoattribute:: ObjectiveHierarchyDesignSession.objective_hierarchy

   .. automethod:: ObjectiveHierarchyDesignSession.can_modify_objective_hierarchy

   .. automethod:: ObjectiveHierarchyDesignSession.add_root_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_root_objective

   .. automethod:: ObjectiveHierarchyDesignSession.add_child_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_child_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_child_objectives



Objective Sequencing Methods
----------------------------

   .. autoattribute:: ObjectiveSequencingSession.objective_hierarchy_id

   .. autoattribute:: ObjectiveSequencingSession.objective_hierarchy

   .. automethod:: ObjectiveSequencingSession.can_sequence_objectives

   .. automethod:: ObjectiveSequencingSession.move_objective_ahead

   .. automethod:: ObjectiveSequencingSession.move_objective_behind

   .. automethod:: ObjectiveSequencingSession.sequence_objectives



Objective Requisite Methods
---------------------------

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



Objective Requisite Assignment Methods
--------------------------------------

   .. autoattribute:: ObjectiveRequisiteAssignmentSession.objective_bank_id

   .. autoattribute:: ObjectiveRequisiteAssignmentSession.objective_bank

   .. automethod:: ObjectiveRequisiteAssignmentSession.can_assign_requisites

   .. automethod:: ObjectiveRequisiteAssignmentSession.assign_objective_requisite

   .. automethod:: ObjectiveRequisiteAssignmentSession.unassign_objective_requisite

   .. automethod:: ObjectiveRequisiteAssignmentSession.assign_equivalent_objective

   .. automethod:: ObjectiveRequisiteAssignmentSession.unassign_equivalent_objective



Activity Lookup Methods
-----------------------

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



Activity Admin Methods
----------------------

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



Objective Search Results
------------------------

.. autoclass:: ObjectiveSearchResults
   :show-inheritance:

   .. autoattribute:: ObjectiveSearchResults.objectives

   .. autoattribute:: ObjectiveSearchResults.objective_query_inspector

   .. automethod:: ObjectiveSearchResults.get_objective_search_results_record



Objective Objective Bank Methods
--------------------------------

   .. automethod:: ObjectiveObjectiveBankSession.can_lookup_objective_objective_bank_mappings

   .. automethod:: ObjectiveObjectiveBankSession.use_comparative_objective_bank_view

   .. automethod:: ObjectiveObjectiveBankSession.use_plenary_objective_bank_view

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_ids_by_objective_bank

   .. automethod:: ObjectiveObjectiveBankSession.get_objectives_by_objective_bank

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_ids_by_objective_banks

   .. automethod:: ObjectiveObjectiveBankSession.get_objectives_by_objective_banks

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_bank_ids_by_objective

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_banks_by_objective



Objective Objective Bank Assignment Methods
-------------------------------------------

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.can_assign_objectives

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.can_assign_objectives_to_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_objective

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.assign_objective_to_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.unassign_objective_from_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.reassign_proficiency_to_objective_bank



Activity Objective Bank Methods
-------------------------------

   .. automethod:: ActivityObjectiveBankSession.can_lookup_activity_objective_bank_mappings

   .. automethod:: ActivityObjectiveBankSession.use_comparative_objective_bank_view

   .. automethod:: ActivityObjectiveBankSession.use_plenary_objective_bank_view

   .. automethod:: ActivityObjectiveBankSession.get_activity_ids_by_objective_bank

   .. automethod:: ActivityObjectiveBankSession.get_activities_by_objective_bank

   .. automethod:: ActivityObjectiveBankSession.get_activity_ids_by_objective_banks

   .. automethod:: ActivityObjectiveBankSession.get_activities_by_objective_banks

   .. automethod:: ActivityObjectiveBankSession.get_objective_bank_ids_by_activity

   .. automethod:: ActivityObjectiveBankSession.get_objective_banks_by_activity



Activity Objective Bank Assignment Methods
------------------------------------------

   .. automethod:: ActivityObjectiveBankAssignmentSession.can_assign_activities

   .. automethod:: ActivityObjectiveBankAssignmentSession.can_assign_activities_to_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.get_assignable_objective_bank_ids

   .. automethod:: ActivityObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_activity

   .. automethod:: ActivityObjectiveBankAssignmentSession.assign_activity_to_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.unassign_activity_from_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.reassign_activity_to_objective_bank



Objective Bank Lookup Methods
-----------------------------

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



Objective Bank Admin Methods
----------------------------

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



Objective Bank Hierarchy Methods
--------------------------------

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



Objective Bank Hierarchy Design Methods
---------------------------------------

   .. autoattribute:: ObjectiveBankHierarchyDesignSession.objective_bank_hierarchy_id

   .. autoattribute:: ObjectiveBankHierarchyDesignSession.objective_bank_hierarchy

   .. automethod:: ObjectiveBankHierarchyDesignSession.can_modify_objective_bank_hierarchy

   .. automethod:: ObjectiveBankHierarchyDesignSession.add_root_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_root_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.add_child_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_child_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_child_objective_banks



Objective Lookup Methods
------------------------

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



Objective Query Methods
-----------------------

   .. autoattribute:: ObjectiveQuerySession.objective_bank_id

   .. autoattribute:: ObjectiveQuerySession.objective_bank

   .. automethod:: ObjectiveQuerySession.can_search_objectives

   .. automethod:: ObjectiveQuerySession.use_federated_objective_bank_view

   .. automethod:: ObjectiveQuerySession.use_isolated_objective_bank_view

   .. autoattribute:: ObjectiveQuerySession.objective_query

   .. automethod:: ObjectiveQuerySession.get_objectives_by_query



Objective Admin Methods
-----------------------

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



Objective Hierarchy Methods
---------------------------

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



Objective Hierarchy Design Methods
----------------------------------

   .. autoattribute:: ObjectiveHierarchyDesignSession.objective_hierarchy_id

   .. autoattribute:: ObjectiveHierarchyDesignSession.objective_hierarchy

   .. automethod:: ObjectiveHierarchyDesignSession.can_modify_objective_hierarchy

   .. automethod:: ObjectiveHierarchyDesignSession.add_root_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_root_objective

   .. automethod:: ObjectiveHierarchyDesignSession.add_child_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_child_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_child_objectives



Objective Sequencing Methods
----------------------------

   .. autoattribute:: ObjectiveSequencingSession.objective_hierarchy_id

   .. autoattribute:: ObjectiveSequencingSession.objective_hierarchy

   .. automethod:: ObjectiveSequencingSession.can_sequence_objectives

   .. automethod:: ObjectiveSequencingSession.move_objective_ahead

   .. automethod:: ObjectiveSequencingSession.move_objective_behind

   .. automethod:: ObjectiveSequencingSession.sequence_objectives



Objective Requisite Methods
---------------------------

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



Objective Requisite Assignment Methods
--------------------------------------

   .. autoattribute:: ObjectiveRequisiteAssignmentSession.objective_bank_id

   .. autoattribute:: ObjectiveRequisiteAssignmentSession.objective_bank

   .. automethod:: ObjectiveRequisiteAssignmentSession.can_assign_requisites

   .. automethod:: ObjectiveRequisiteAssignmentSession.assign_objective_requisite

   .. automethod:: ObjectiveRequisiteAssignmentSession.unassign_objective_requisite

   .. automethod:: ObjectiveRequisiteAssignmentSession.assign_equivalent_objective

   .. automethod:: ObjectiveRequisiteAssignmentSession.unassign_equivalent_objective



Activity Lookup Methods
-----------------------

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



Activity Admin Methods
----------------------

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



Activity Search
---------------

.. autoclass:: ActivitySearch
   :show-inheritance:

   .. automethod:: ActivitySearch.search_among_activities

   .. automethod:: ActivitySearch.order_activity_results

   .. automethod:: ActivitySearch.get_activity_search_record



Objective Objective Bank Methods
--------------------------------

   .. automethod:: ObjectiveObjectiveBankSession.can_lookup_objective_objective_bank_mappings

   .. automethod:: ObjectiveObjectiveBankSession.use_comparative_objective_bank_view

   .. automethod:: ObjectiveObjectiveBankSession.use_plenary_objective_bank_view

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_ids_by_objective_bank

   .. automethod:: ObjectiveObjectiveBankSession.get_objectives_by_objective_bank

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_ids_by_objective_banks

   .. automethod:: ObjectiveObjectiveBankSession.get_objectives_by_objective_banks

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_bank_ids_by_objective

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_banks_by_objective



Objective Objective Bank Assignment Methods
-------------------------------------------

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.can_assign_objectives

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.can_assign_objectives_to_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_objective

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.assign_objective_to_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.unassign_objective_from_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.reassign_proficiency_to_objective_bank



Activity Objective Bank Methods
-------------------------------

   .. automethod:: ActivityObjectiveBankSession.can_lookup_activity_objective_bank_mappings

   .. automethod:: ActivityObjectiveBankSession.use_comparative_objective_bank_view

   .. automethod:: ActivityObjectiveBankSession.use_plenary_objective_bank_view

   .. automethod:: ActivityObjectiveBankSession.get_activity_ids_by_objective_bank

   .. automethod:: ActivityObjectiveBankSession.get_activities_by_objective_bank

   .. automethod:: ActivityObjectiveBankSession.get_activity_ids_by_objective_banks

   .. automethod:: ActivityObjectiveBankSession.get_activities_by_objective_banks

   .. automethod:: ActivityObjectiveBankSession.get_objective_bank_ids_by_activity

   .. automethod:: ActivityObjectiveBankSession.get_objective_banks_by_activity



Activity Objective Bank Assignment Methods
------------------------------------------

   .. automethod:: ActivityObjectiveBankAssignmentSession.can_assign_activities

   .. automethod:: ActivityObjectiveBankAssignmentSession.can_assign_activities_to_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.get_assignable_objective_bank_ids

   .. automethod:: ActivityObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_activity

   .. automethod:: ActivityObjectiveBankAssignmentSession.assign_activity_to_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.unassign_activity_from_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.reassign_activity_to_objective_bank



Objective Bank Lookup Methods
-----------------------------

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



Objective Bank Admin Methods
----------------------------

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



Objective Bank Hierarchy Methods
--------------------------------

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



Objective Bank Hierarchy Design Methods
---------------------------------------

   .. autoattribute:: ObjectiveBankHierarchyDesignSession.objective_bank_hierarchy_id

   .. autoattribute:: ObjectiveBankHierarchyDesignSession.objective_bank_hierarchy

   .. automethod:: ObjectiveBankHierarchyDesignSession.can_modify_objective_bank_hierarchy

   .. automethod:: ObjectiveBankHierarchyDesignSession.add_root_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_root_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.add_child_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_child_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_child_objective_banks



Objective Lookup Methods
------------------------

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



Objective Query Methods
-----------------------

   .. autoattribute:: ObjectiveQuerySession.objective_bank_id

   .. autoattribute:: ObjectiveQuerySession.objective_bank

   .. automethod:: ObjectiveQuerySession.can_search_objectives

   .. automethod:: ObjectiveQuerySession.use_federated_objective_bank_view

   .. automethod:: ObjectiveQuerySession.use_isolated_objective_bank_view

   .. autoattribute:: ObjectiveQuerySession.objective_query

   .. automethod:: ObjectiveQuerySession.get_objectives_by_query



Objective Admin Methods
-----------------------

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



Objective Hierarchy Methods
---------------------------

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



Objective Hierarchy Design Methods
----------------------------------

   .. autoattribute:: ObjectiveHierarchyDesignSession.objective_hierarchy_id

   .. autoattribute:: ObjectiveHierarchyDesignSession.objective_hierarchy

   .. automethod:: ObjectiveHierarchyDesignSession.can_modify_objective_hierarchy

   .. automethod:: ObjectiveHierarchyDesignSession.add_root_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_root_objective

   .. automethod:: ObjectiveHierarchyDesignSession.add_child_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_child_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_child_objectives



Objective Sequencing Methods
----------------------------

   .. autoattribute:: ObjectiveSequencingSession.objective_hierarchy_id

   .. autoattribute:: ObjectiveSequencingSession.objective_hierarchy

   .. automethod:: ObjectiveSequencingSession.can_sequence_objectives

   .. automethod:: ObjectiveSequencingSession.move_objective_ahead

   .. automethod:: ObjectiveSequencingSession.move_objective_behind

   .. automethod:: ObjectiveSequencingSession.sequence_objectives



Objective Requisite Methods
---------------------------

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



Objective Requisite Assignment Methods
--------------------------------------

   .. autoattribute:: ObjectiveRequisiteAssignmentSession.objective_bank_id

   .. autoattribute:: ObjectiveRequisiteAssignmentSession.objective_bank

   .. automethod:: ObjectiveRequisiteAssignmentSession.can_assign_requisites

   .. automethod:: ObjectiveRequisiteAssignmentSession.assign_objective_requisite

   .. automethod:: ObjectiveRequisiteAssignmentSession.unassign_objective_requisite

   .. automethod:: ObjectiveRequisiteAssignmentSession.assign_equivalent_objective

   .. automethod:: ObjectiveRequisiteAssignmentSession.unassign_equivalent_objective



Activity Lookup Methods
-----------------------

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



Activity Admin Methods
----------------------

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



Activity Search Results
-----------------------

.. autoclass:: ActivitySearchResults
   :show-inheritance:

   .. autoattribute:: ActivitySearchResults.activities

   .. autoattribute:: ActivitySearchResults.activity_query_inspector

   .. automethod:: ActivitySearchResults.get_activity_search_results_record



Objective Objective Bank Methods
--------------------------------

   .. automethod:: ObjectiveObjectiveBankSession.can_lookup_objective_objective_bank_mappings

   .. automethod:: ObjectiveObjectiveBankSession.use_comparative_objective_bank_view

   .. automethod:: ObjectiveObjectiveBankSession.use_plenary_objective_bank_view

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_ids_by_objective_bank

   .. automethod:: ObjectiveObjectiveBankSession.get_objectives_by_objective_bank

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_ids_by_objective_banks

   .. automethod:: ObjectiveObjectiveBankSession.get_objectives_by_objective_banks

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_bank_ids_by_objective

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_banks_by_objective



Objective Objective Bank Assignment Methods
-------------------------------------------

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.can_assign_objectives

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.can_assign_objectives_to_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_objective

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.assign_objective_to_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.unassign_objective_from_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.reassign_proficiency_to_objective_bank



Activity Objective Bank Methods
-------------------------------

   .. automethod:: ActivityObjectiveBankSession.can_lookup_activity_objective_bank_mappings

   .. automethod:: ActivityObjectiveBankSession.use_comparative_objective_bank_view

   .. automethod:: ActivityObjectiveBankSession.use_plenary_objective_bank_view

   .. automethod:: ActivityObjectiveBankSession.get_activity_ids_by_objective_bank

   .. automethod:: ActivityObjectiveBankSession.get_activities_by_objective_bank

   .. automethod:: ActivityObjectiveBankSession.get_activity_ids_by_objective_banks

   .. automethod:: ActivityObjectiveBankSession.get_activities_by_objective_banks

   .. automethod:: ActivityObjectiveBankSession.get_objective_bank_ids_by_activity

   .. automethod:: ActivityObjectiveBankSession.get_objective_banks_by_activity



Activity Objective Bank Assignment Methods
------------------------------------------

   .. automethod:: ActivityObjectiveBankAssignmentSession.can_assign_activities

   .. automethod:: ActivityObjectiveBankAssignmentSession.can_assign_activities_to_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.get_assignable_objective_bank_ids

   .. automethod:: ActivityObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_activity

   .. automethod:: ActivityObjectiveBankAssignmentSession.assign_activity_to_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.unassign_activity_from_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.reassign_activity_to_objective_bank



Objective Bank Lookup Methods
-----------------------------

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



Objective Bank Admin Methods
----------------------------

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



Objective Bank Hierarchy Methods
--------------------------------

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



Objective Bank Hierarchy Design Methods
---------------------------------------

   .. autoattribute:: ObjectiveBankHierarchyDesignSession.objective_bank_hierarchy_id

   .. autoattribute:: ObjectiveBankHierarchyDesignSession.objective_bank_hierarchy

   .. automethod:: ObjectiveBankHierarchyDesignSession.can_modify_objective_bank_hierarchy

   .. automethod:: ObjectiveBankHierarchyDesignSession.add_root_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_root_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.add_child_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_child_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_child_objective_banks



Objective Lookup Methods
------------------------

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



Objective Query Methods
-----------------------

   .. autoattribute:: ObjectiveQuerySession.objective_bank_id

   .. autoattribute:: ObjectiveQuerySession.objective_bank

   .. automethod:: ObjectiveQuerySession.can_search_objectives

   .. automethod:: ObjectiveQuerySession.use_federated_objective_bank_view

   .. automethod:: ObjectiveQuerySession.use_isolated_objective_bank_view

   .. autoattribute:: ObjectiveQuerySession.objective_query

   .. automethod:: ObjectiveQuerySession.get_objectives_by_query



Objective Admin Methods
-----------------------

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



Objective Hierarchy Methods
---------------------------

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



Objective Hierarchy Design Methods
----------------------------------

   .. autoattribute:: ObjectiveHierarchyDesignSession.objective_hierarchy_id

   .. autoattribute:: ObjectiveHierarchyDesignSession.objective_hierarchy

   .. automethod:: ObjectiveHierarchyDesignSession.can_modify_objective_hierarchy

   .. automethod:: ObjectiveHierarchyDesignSession.add_root_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_root_objective

   .. automethod:: ObjectiveHierarchyDesignSession.add_child_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_child_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_child_objectives



Objective Sequencing Methods
----------------------------

   .. autoattribute:: ObjectiveSequencingSession.objective_hierarchy_id

   .. autoattribute:: ObjectiveSequencingSession.objective_hierarchy

   .. automethod:: ObjectiveSequencingSession.can_sequence_objectives

   .. automethod:: ObjectiveSequencingSession.move_objective_ahead

   .. automethod:: ObjectiveSequencingSession.move_objective_behind

   .. automethod:: ObjectiveSequencingSession.sequence_objectives



Objective Requisite Methods
---------------------------

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



Objective Requisite Assignment Methods
--------------------------------------

   .. autoattribute:: ObjectiveRequisiteAssignmentSession.objective_bank_id

   .. autoattribute:: ObjectiveRequisiteAssignmentSession.objective_bank

   .. automethod:: ObjectiveRequisiteAssignmentSession.can_assign_requisites

   .. automethod:: ObjectiveRequisiteAssignmentSession.assign_objective_requisite

   .. automethod:: ObjectiveRequisiteAssignmentSession.unassign_objective_requisite

   .. automethod:: ObjectiveRequisiteAssignmentSession.assign_equivalent_objective

   .. automethod:: ObjectiveRequisiteAssignmentSession.unassign_equivalent_objective



Activity Lookup Methods
-----------------------

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



Activity Admin Methods
----------------------

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



Objective Bank Search
---------------------

.. autoclass:: ObjectiveBankSearch
   :show-inheritance:

   .. automethod:: ObjectiveBankSearch.search_among_objective_banks

   .. automethod:: ObjectiveBankSearch.order_objective_bank_results

   .. automethod:: ObjectiveBankSearch.get_objective_bank_search_record



Objective Objective Bank Methods
--------------------------------

   .. automethod:: ObjectiveObjectiveBankSession.can_lookup_objective_objective_bank_mappings

   .. automethod:: ObjectiveObjectiveBankSession.use_comparative_objective_bank_view

   .. automethod:: ObjectiveObjectiveBankSession.use_plenary_objective_bank_view

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_ids_by_objective_bank

   .. automethod:: ObjectiveObjectiveBankSession.get_objectives_by_objective_bank

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_ids_by_objective_banks

   .. automethod:: ObjectiveObjectiveBankSession.get_objectives_by_objective_banks

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_bank_ids_by_objective

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_banks_by_objective



Objective Objective Bank Assignment Methods
-------------------------------------------

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.can_assign_objectives

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.can_assign_objectives_to_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_objective

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.assign_objective_to_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.unassign_objective_from_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.reassign_proficiency_to_objective_bank



Activity Objective Bank Methods
-------------------------------

   .. automethod:: ActivityObjectiveBankSession.can_lookup_activity_objective_bank_mappings

   .. automethod:: ActivityObjectiveBankSession.use_comparative_objective_bank_view

   .. automethod:: ActivityObjectiveBankSession.use_plenary_objective_bank_view

   .. automethod:: ActivityObjectiveBankSession.get_activity_ids_by_objective_bank

   .. automethod:: ActivityObjectiveBankSession.get_activities_by_objective_bank

   .. automethod:: ActivityObjectiveBankSession.get_activity_ids_by_objective_banks

   .. automethod:: ActivityObjectiveBankSession.get_activities_by_objective_banks

   .. automethod:: ActivityObjectiveBankSession.get_objective_bank_ids_by_activity

   .. automethod:: ActivityObjectiveBankSession.get_objective_banks_by_activity



Activity Objective Bank Assignment Methods
------------------------------------------

   .. automethod:: ActivityObjectiveBankAssignmentSession.can_assign_activities

   .. automethod:: ActivityObjectiveBankAssignmentSession.can_assign_activities_to_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.get_assignable_objective_bank_ids

   .. automethod:: ActivityObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_activity

   .. automethod:: ActivityObjectiveBankAssignmentSession.assign_activity_to_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.unassign_activity_from_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.reassign_activity_to_objective_bank



Objective Bank Lookup Methods
-----------------------------

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



Objective Bank Admin Methods
----------------------------

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



Objective Bank Hierarchy Methods
--------------------------------

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



Objective Bank Hierarchy Design Methods
---------------------------------------

   .. autoattribute:: ObjectiveBankHierarchyDesignSession.objective_bank_hierarchy_id

   .. autoattribute:: ObjectiveBankHierarchyDesignSession.objective_bank_hierarchy

   .. automethod:: ObjectiveBankHierarchyDesignSession.can_modify_objective_bank_hierarchy

   .. automethod:: ObjectiveBankHierarchyDesignSession.add_root_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_root_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.add_child_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_child_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_child_objective_banks



Objective Lookup Methods
------------------------

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



Objective Query Methods
-----------------------

   .. autoattribute:: ObjectiveQuerySession.objective_bank_id

   .. autoattribute:: ObjectiveQuerySession.objective_bank

   .. automethod:: ObjectiveQuerySession.can_search_objectives

   .. automethod:: ObjectiveQuerySession.use_federated_objective_bank_view

   .. automethod:: ObjectiveQuerySession.use_isolated_objective_bank_view

   .. autoattribute:: ObjectiveQuerySession.objective_query

   .. automethod:: ObjectiveQuerySession.get_objectives_by_query



Objective Admin Methods
-----------------------

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



Objective Hierarchy Methods
---------------------------

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



Objective Hierarchy Design Methods
----------------------------------

   .. autoattribute:: ObjectiveHierarchyDesignSession.objective_hierarchy_id

   .. autoattribute:: ObjectiveHierarchyDesignSession.objective_hierarchy

   .. automethod:: ObjectiveHierarchyDesignSession.can_modify_objective_hierarchy

   .. automethod:: ObjectiveHierarchyDesignSession.add_root_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_root_objective

   .. automethod:: ObjectiveHierarchyDesignSession.add_child_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_child_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_child_objectives



Objective Sequencing Methods
----------------------------

   .. autoattribute:: ObjectiveSequencingSession.objective_hierarchy_id

   .. autoattribute:: ObjectiveSequencingSession.objective_hierarchy

   .. automethod:: ObjectiveSequencingSession.can_sequence_objectives

   .. automethod:: ObjectiveSequencingSession.move_objective_ahead

   .. automethod:: ObjectiveSequencingSession.move_objective_behind

   .. automethod:: ObjectiveSequencingSession.sequence_objectives



Objective Requisite Methods
---------------------------

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



Objective Requisite Assignment Methods
--------------------------------------

   .. autoattribute:: ObjectiveRequisiteAssignmentSession.objective_bank_id

   .. autoattribute:: ObjectiveRequisiteAssignmentSession.objective_bank

   .. automethod:: ObjectiveRequisiteAssignmentSession.can_assign_requisites

   .. automethod:: ObjectiveRequisiteAssignmentSession.assign_objective_requisite

   .. automethod:: ObjectiveRequisiteAssignmentSession.unassign_objective_requisite

   .. automethod:: ObjectiveRequisiteAssignmentSession.assign_equivalent_objective

   .. automethod:: ObjectiveRequisiteAssignmentSession.unassign_equivalent_objective



Activity Lookup Methods
-----------------------

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



Activity Admin Methods
----------------------

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



Objective Bank Search Results
-----------------------------

.. autoclass:: ObjectiveBankSearchResults
   :show-inheritance:

   .. autoattribute:: ObjectiveBankSearchResults.objective_banks

   .. autoattribute:: ObjectiveBankSearchResults.objective_bank_query_inspector

   .. automethod:: ObjectiveBankSearchResults.get_objective_bank_search_results_record



Objective Objective Bank Methods
--------------------------------

   .. automethod:: ObjectiveObjectiveBankSession.can_lookup_objective_objective_bank_mappings

   .. automethod:: ObjectiveObjectiveBankSession.use_comparative_objective_bank_view

   .. automethod:: ObjectiveObjectiveBankSession.use_plenary_objective_bank_view

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_ids_by_objective_bank

   .. automethod:: ObjectiveObjectiveBankSession.get_objectives_by_objective_bank

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_ids_by_objective_banks

   .. automethod:: ObjectiveObjectiveBankSession.get_objectives_by_objective_banks

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_bank_ids_by_objective

   .. automethod:: ObjectiveObjectiveBankSession.get_objective_banks_by_objective



Objective Objective Bank Assignment Methods
-------------------------------------------

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.can_assign_objectives

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.can_assign_objectives_to_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_objective

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.assign_objective_to_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.unassign_objective_from_objective_bank

   .. automethod:: ObjectiveObjectiveBankAssignmentSession.reassign_proficiency_to_objective_bank



Activity Objective Bank Methods
-------------------------------

   .. automethod:: ActivityObjectiveBankSession.can_lookup_activity_objective_bank_mappings

   .. automethod:: ActivityObjectiveBankSession.use_comparative_objective_bank_view

   .. automethod:: ActivityObjectiveBankSession.use_plenary_objective_bank_view

   .. automethod:: ActivityObjectiveBankSession.get_activity_ids_by_objective_bank

   .. automethod:: ActivityObjectiveBankSession.get_activities_by_objective_bank

   .. automethod:: ActivityObjectiveBankSession.get_activity_ids_by_objective_banks

   .. automethod:: ActivityObjectiveBankSession.get_activities_by_objective_banks

   .. automethod:: ActivityObjectiveBankSession.get_objective_bank_ids_by_activity

   .. automethod:: ActivityObjectiveBankSession.get_objective_banks_by_activity



Activity Objective Bank Assignment Methods
------------------------------------------

   .. automethod:: ActivityObjectiveBankAssignmentSession.can_assign_activities

   .. automethod:: ActivityObjectiveBankAssignmentSession.can_assign_activities_to_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.get_assignable_objective_bank_ids

   .. automethod:: ActivityObjectiveBankAssignmentSession.get_assignable_objective_bank_ids_for_activity

   .. automethod:: ActivityObjectiveBankAssignmentSession.assign_activity_to_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.unassign_activity_from_objective_bank

   .. automethod:: ActivityObjectiveBankAssignmentSession.reassign_activity_to_objective_bank



Objective Bank Lookup Methods
-----------------------------

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



Objective Bank Admin Methods
----------------------------

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



Objective Bank Hierarchy Methods
--------------------------------

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



Objective Bank Hierarchy Design Methods
---------------------------------------

   .. autoattribute:: ObjectiveBankHierarchyDesignSession.objective_bank_hierarchy_id

   .. autoattribute:: ObjectiveBankHierarchyDesignSession.objective_bank_hierarchy

   .. automethod:: ObjectiveBankHierarchyDesignSession.can_modify_objective_bank_hierarchy

   .. automethod:: ObjectiveBankHierarchyDesignSession.add_root_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_root_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.add_child_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_child_objective_bank

   .. automethod:: ObjectiveBankHierarchyDesignSession.remove_child_objective_banks



Objective Lookup Methods
------------------------

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



Objective Query Methods
-----------------------

   .. autoattribute:: ObjectiveQuerySession.objective_bank_id

   .. autoattribute:: ObjectiveQuerySession.objective_bank

   .. automethod:: ObjectiveQuerySession.can_search_objectives

   .. automethod:: ObjectiveQuerySession.use_federated_objective_bank_view

   .. automethod:: ObjectiveQuerySession.use_isolated_objective_bank_view

   .. autoattribute:: ObjectiveQuerySession.objective_query

   .. automethod:: ObjectiveQuerySession.get_objectives_by_query



Objective Admin Methods
-----------------------

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



Objective Hierarchy Methods
---------------------------

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



Objective Hierarchy Design Methods
----------------------------------

   .. autoattribute:: ObjectiveHierarchyDesignSession.objective_hierarchy_id

   .. autoattribute:: ObjectiveHierarchyDesignSession.objective_hierarchy

   .. automethod:: ObjectiveHierarchyDesignSession.can_modify_objective_hierarchy

   .. automethod:: ObjectiveHierarchyDesignSession.add_root_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_root_objective

   .. automethod:: ObjectiveHierarchyDesignSession.add_child_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_child_objective

   .. automethod:: ObjectiveHierarchyDesignSession.remove_child_objectives



Objective Sequencing Methods
----------------------------

   .. autoattribute:: ObjectiveSequencingSession.objective_hierarchy_id

   .. autoattribute:: ObjectiveSequencingSession.objective_hierarchy

   .. automethod:: ObjectiveSequencingSession.can_sequence_objectives

   .. automethod:: ObjectiveSequencingSession.move_objective_ahead

   .. automethod:: ObjectiveSequencingSession.move_objective_behind

   .. automethod:: ObjectiveSequencingSession.sequence_objectives



Objective Requisite Methods
---------------------------

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



Objective Requisite Assignment Methods
--------------------------------------

   .. autoattribute:: ObjectiveRequisiteAssignmentSession.objective_bank_id

   .. autoattribute:: ObjectiveRequisiteAssignmentSession.objective_bank

   .. automethod:: ObjectiveRequisiteAssignmentSession.can_assign_requisites

   .. automethod:: ObjectiveRequisiteAssignmentSession.assign_objective_requisite

   .. automethod:: ObjectiveRequisiteAssignmentSession.unassign_objective_requisite

   .. automethod:: ObjectiveRequisiteAssignmentSession.assign_equivalent_objective

   .. automethod:: ObjectiveRequisiteAssignmentSession.unassign_equivalent_objective



Activity Lookup Methods
-----------------------

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



Activity Admin Methods
----------------------

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



