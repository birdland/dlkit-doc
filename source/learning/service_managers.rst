
.. currentmodule:: dlkit.services.learning
.. automodule:: dlkit.services.learning

Service Managers
================


Learning Manager
----------------

.. autoclass:: LearningManager
   :show-inheritance:

   .. autoattribute:: LearningManager.objective_lookup_session

   .. automethod:: LearningManager.get_objective_lookup_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_query_session

   .. automethod:: LearningManager.get_objective_query_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_search_session

   .. automethod:: LearningManager.get_objective_search_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_admin_session

   .. automethod:: LearningManager.get_objective_admin_session_for_objective_bank

   .. automethod:: LearningManager.get_objective_notification_session

   .. automethod:: LearningManager.get_objective_notification_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_hierarchy_session

   .. automethod:: LearningManager.get_objective_hierarchy_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_hierarchy_design_session

   .. automethod:: LearningManager.get_objective_hierarchy_design_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_sequencing_session

   .. automethod:: LearningManager.get_objective_sequencing_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_objective_bank_session

   .. autoattribute:: LearningManager.objective_objective_bank_assignment_session

   .. automethod:: LearningManager.get_objective_smart_objective_bank_session

   .. autoattribute:: LearningManager.objective_requisite_session

   .. automethod:: LearningManager.get_objective_requisite_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_requisite_assignment_session

   .. automethod:: LearningManager.get_objective_requisite_assignment_session_for_objective_bank

   .. autoattribute:: LearningManager.activity_lookup_session

   .. automethod:: LearningManager.get_activity_lookup_session_for_objective_bank

   .. autoattribute:: LearningManager.activity_query_session

   .. automethod:: LearningManager.get_activity_query_session_for_objective_bank

   .. autoattribute:: LearningManager.activity_search_session

   .. automethod:: LearningManager.get_activity_search_session_for_objective_bank

   .. autoattribute:: LearningManager.activity_admin_session

   .. automethod:: LearningManager.get_activity_admin_session_for_objective_bank

   .. automethod:: LearningManager.get_activity_notification_session

   .. automethod:: LearningManager.get_activity_notification_session_for_objective_bank

   .. autoattribute:: LearningManager.activity_objective_bank_session

   .. autoattribute:: LearningManager.activity_objective_bank_assignment_session

   .. automethod:: LearningManager.get_activity_smart_objective_bank_session

   .. autoattribute:: LearningManager.proficiency_lookup_session

   .. automethod:: LearningManager.get_proficiency_lookup_session_for_objective_bank

   .. autoattribute:: LearningManager.proficiency_query_session

   .. automethod:: LearningManager.get_proficiency_query_session_for_objective_bank

   .. autoattribute:: LearningManager.proficiency_search_session

   .. automethod:: LearningManager.get_proficiency_search_session_for_objective_bank

   .. autoattribute:: LearningManager.proficiency_admin_session

   .. automethod:: LearningManager.get_proficiency_admin_session_for_objective_bank

   .. automethod:: LearningManager.get_proficiency_notification_session

   .. automethod:: LearningManager.get_proficiency_notification_session_for_objective_bank

   .. autoattribute:: LearningManager.proficiency_objective_bank_session

   .. autoattribute:: LearningManager.proficiency_objective_bank_assignment_session

   .. automethod:: LearningManager.get_proficiency_smart_objective_bank_session

   .. autoattribute:: LearningManager.my_learning_path_session

   .. automethod:: LearningManager.get_my_learning_path_session_for_objective_bank

   .. autoattribute:: LearningManager.learning_path_session

   .. automethod:: LearningManager.get_learning_path_session_for_objective_bank

   .. autoattribute:: LearningManager.objective_bank_lookup_session

   .. autoattribute:: LearningManager.objective_bank_query_session

   .. autoattribute:: LearningManager.objective_bank_search_session

   .. autoattribute:: LearningManager.objective_bank_admin_session

   .. automethod:: LearningManager.get_objective_bank_notification_session

   .. autoattribute:: LearningManager.objective_bank_hierarchy_session

   .. autoattribute:: LearningManager.objective_bank_hierarchy_design_session

   .. autoattribute:: LearningManager.learning_batch_manager



Objective Objective Bank Methods
--------------------------------

   .. automethod:: LearningManager.can_lookup_objective_objective_bank_mappings

   .. automethod:: LearningManager.use_comparative_objective_bank_view

   .. automethod:: LearningManager.use_plenary_objective_bank_view

   .. automethod:: LearningManager.get_objective_ids_by_objective_bank

   .. automethod:: LearningManager.get_objectives_by_objective_bank

   .. automethod:: LearningManager.get_objective_ids_by_objective_banks

   .. automethod:: LearningManager.get_objectives_by_objective_banks

   .. automethod:: LearningManager.get_objective_bank_ids_by_objective

   .. automethod:: LearningManager.get_objective_banks_by_objective



Objective Objective Bank Assignment Methods
-------------------------------------------

   .. automethod:: LearningManager.can_assign_objectives

   .. automethod:: LearningManager.can_assign_objectives_to_objective_bank

   .. automethod:: LearningManager.get_assignable_objective_bank_ids

   .. automethod:: LearningManager.get_assignable_objective_bank_ids_for_objective

   .. automethod:: LearningManager.assign_objective_to_objective_bank

   .. automethod:: LearningManager.unassign_objective_from_objective_bank

   .. automethod:: LearningManager.reassign_proficiency_to_objective_bank



Activity Objective Bank Methods
-------------------------------

   .. automethod:: LearningManager.can_lookup_activity_objective_bank_mappings

   .. automethod:: LearningManager.use_comparative_objective_bank_view

   .. automethod:: LearningManager.use_plenary_objective_bank_view

   .. automethod:: LearningManager.get_activity_ids_by_objective_bank

   .. automethod:: LearningManager.get_activities_by_objective_bank

   .. automethod:: LearningManager.get_activity_ids_by_objective_banks

   .. automethod:: LearningManager.get_activities_by_objective_banks

   .. automethod:: LearningManager.get_objective_bank_ids_by_activity

   .. automethod:: LearningManager.get_objective_banks_by_activity



Activity Objective Bank Assignment Methods
------------------------------------------

   .. automethod:: LearningManager.can_assign_activities

   .. automethod:: LearningManager.can_assign_activities_to_objective_bank

   .. automethod:: LearningManager.get_assignable_objective_bank_ids

   .. automethod:: LearningManager.get_assignable_objective_bank_ids_for_activity

   .. automethod:: LearningManager.assign_activity_to_objective_bank

   .. automethod:: LearningManager.unassign_activity_from_objective_bank

   .. automethod:: LearningManager.reassign_activity_to_objective_bank



Objective Bank Lookup Methods
-----------------------------

   .. automethod:: LearningManager.can_lookup_objective_banks

   .. automethod:: LearningManager.use_comparative_objective_bank_view

   .. automethod:: LearningManager.use_plenary_objective_bank_view

   .. automethod:: LearningManager.get_objective_bank

   .. automethod:: LearningManager.get_objective_banks_by_ids

   .. automethod:: LearningManager.get_objective_banks_by_genus_type

   .. automethod:: LearningManager.get_objective_banks_by_parent_genus_type

   .. automethod:: LearningManager.get_objective_banks_by_record_type

   .. automethod:: LearningManager.get_objective_banks_by_provider

   .. autoattribute:: LearningManager.objective_banks



Objective Bank Admin Methods
----------------------------

   .. automethod:: LearningManager.can_create_objective_banks

   .. automethod:: LearningManager.can_create_objective_bank_with_record_types

   .. automethod:: LearningManager.get_objective_bank_form_for_create

   .. automethod:: LearningManager.create_objective_bank

   .. automethod:: LearningManager.can_update_objective_banks

   .. automethod:: LearningManager.get_objective_bank_form_for_update

   .. automethod:: LearningManager.update_objective_bank

   .. automethod:: LearningManager.can_delete_objective_banks

   .. automethod:: LearningManager.delete_objective_bank

   .. automethod:: LearningManager.can_manage_objective_bank_aliases

   .. automethod:: LearningManager.alias_objective_bank



Objective Bank Hierarchy Methods
--------------------------------

   .. autoattribute:: LearningManager.objective_bank_hierarchy_id

   .. autoattribute:: LearningManager.objective_bank_hierarchy

   .. automethod:: LearningManager.can_access_objective_bank_hierarchy

   .. automethod:: LearningManager.use_comparative_objective_bank_view

   .. automethod:: LearningManager.use_plenary_objective_bank_view

   .. autoattribute:: LearningManager.root_objective_bank_ids

   .. autoattribute:: LearningManager.root_objective_banks

   .. automethod:: LearningManager.has_parent_objective_banks

   .. automethod:: LearningManager.is_parent_of_objective_bank

   .. automethod:: LearningManager.get_parent_objective_bank_ids

   .. automethod:: LearningManager.get_parent_objective_banks

   .. automethod:: LearningManager.is_ancestor_of_objective_bank

   .. automethod:: LearningManager.has_child_objective_banks

   .. automethod:: LearningManager.is_child_of_objective_bank

   .. automethod:: LearningManager.get_child_objective_bank_ids

   .. automethod:: LearningManager.get_child_objective_banks

   .. automethod:: LearningManager.is_descendant_of_objective_bank

   .. automethod:: LearningManager.get_objective_bank_node_ids

   .. automethod:: LearningManager.get_objective_bank_nodes



Objective Bank Hierarchy Design Methods
---------------------------------------

   .. autoattribute:: LearningManager.objective_bank_hierarchy_id

   .. autoattribute:: LearningManager.objective_bank_hierarchy

   .. automethod:: LearningManager.can_modify_objective_bank_hierarchy

   .. automethod:: LearningManager.add_root_objective_bank

   .. automethod:: LearningManager.remove_root_objective_bank

   .. automethod:: LearningManager.add_child_objective_bank

   .. automethod:: LearningManager.remove_child_objective_bank

   .. automethod:: LearningManager.remove_child_objective_banks



Learning Proxy Manager
----------------------

.. autoclass:: LearningProxyManager
   :show-inheritance:

   .. automethod:: LearningProxyManager.get_objective_lookup_session

   .. automethod:: LearningProxyManager.get_objective_lookup_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_query_session

   .. automethod:: LearningProxyManager.get_objective_query_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_search_session

   .. automethod:: LearningProxyManager.get_objective_search_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_admin_session

   .. automethod:: LearningProxyManager.get_objective_admin_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_notification_session

   .. automethod:: LearningProxyManager.get_objective_notification_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_hierarchy_session

   .. automethod:: LearningProxyManager.get_objective_hierarchy_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_hierarchy_design_session

   .. automethod:: LearningProxyManager.get_objective_hierarchy_design_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_sequencing_session

   .. automethod:: LearningProxyManager.get_objective_sequencing_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_objective_bank_session

   .. automethod:: LearningProxyManager.get_objective_objective_bank_assignment_session

   .. automethod:: LearningProxyManager.get_objective_smart_objective_bank_session

   .. automethod:: LearningProxyManager.get_objective_requisite_session

   .. automethod:: LearningProxyManager.get_objective_requisite_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_requisite_assignment_session

   .. automethod:: LearningProxyManager.get_objective_requisite_assignment_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_activity_lookup_session

   .. automethod:: LearningProxyManager.get_activity_lookup_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_activity_query_session

   .. automethod:: LearningProxyManager.get_activity_query_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_activity_search_session

   .. automethod:: LearningProxyManager.get_activity_search_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_activity_admin_session

   .. automethod:: LearningProxyManager.get_activity_admin_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_activity_notification_session

   .. automethod:: LearningProxyManager.get_activity_notification_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_activity_objective_bank_session

   .. automethod:: LearningProxyManager.get_activity_objective_bank_assignment_session

   .. automethod:: LearningProxyManager.get_activity_smart_objective_bank_session

   .. automethod:: LearningProxyManager.get_proficiency_lookup_session

   .. automethod:: LearningProxyManager.get_proficiency_lookup_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_proficiency_query_session

   .. automethod:: LearningProxyManager.get_proficiency_query_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_proficiency_search_session

   .. automethod:: LearningProxyManager.get_proficiency_search_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_proficiency_admin_session

   .. automethod:: LearningProxyManager.get_proficiency_admin_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_proficiency_notification_session

   .. automethod:: LearningProxyManager.get_proficiency_notification_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_proficiency_objective_bank_session

   .. automethod:: LearningProxyManager.get_proficiency_objective_bank_assignment_session

   .. automethod:: LearningProxyManager.get_proficiency_smart_objective_bank_session

   .. automethod:: LearningProxyManager.get_my_learning_path_session

   .. automethod:: LearningProxyManager.get_my_learning_path_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_learning_path_session

   .. automethod:: LearningProxyManager.get_learning_path_session_for_objective_bank

   .. automethod:: LearningProxyManager.get_objective_bank_lookup_session

   .. automethod:: LearningProxyManager.get_objective_bank_query_session

   .. automethod:: LearningProxyManager.get_objective_bank_search_session

   .. automethod:: LearningProxyManager.get_objective_bank_admin_session

   .. automethod:: LearningProxyManager.get_objective_bank_notification_session

   .. automethod:: LearningProxyManager.get_objective_bank_hierarchy_session

   .. automethod:: LearningProxyManager.get_objective_bank_hierarchy_design_session

   .. autoattribute:: LearningProxyManager.learning_batch_proxy_manager



Objective Objective Bank Methods
--------------------------------

   .. automethod:: LearningProxyManager.can_lookup_objective_objective_bank_mappings

   .. automethod:: LearningProxyManager.use_comparative_objective_bank_view

   .. automethod:: LearningProxyManager.use_plenary_objective_bank_view

   .. automethod:: LearningProxyManager.get_objective_ids_by_objective_bank

   .. automethod:: LearningProxyManager.get_objectives_by_objective_bank

   .. automethod:: LearningProxyManager.get_objective_ids_by_objective_banks

   .. automethod:: LearningProxyManager.get_objectives_by_objective_banks

   .. automethod:: LearningProxyManager.get_objective_bank_ids_by_objective

   .. automethod:: LearningProxyManager.get_objective_banks_by_objective



Objective Objective Bank Assignment Methods
-------------------------------------------

   .. automethod:: LearningProxyManager.can_assign_objectives

   .. automethod:: LearningProxyManager.can_assign_objectives_to_objective_bank

   .. automethod:: LearningProxyManager.get_assignable_objective_bank_ids

   .. automethod:: LearningProxyManager.get_assignable_objective_bank_ids_for_objective

   .. automethod:: LearningProxyManager.assign_objective_to_objective_bank

   .. automethod:: LearningProxyManager.unassign_objective_from_objective_bank

   .. automethod:: LearningProxyManager.reassign_proficiency_to_objective_bank



Activity Objective Bank Methods
-------------------------------

   .. automethod:: LearningProxyManager.can_lookup_activity_objective_bank_mappings

   .. automethod:: LearningProxyManager.use_comparative_objective_bank_view

   .. automethod:: LearningProxyManager.use_plenary_objective_bank_view

   .. automethod:: LearningProxyManager.get_activity_ids_by_objective_bank

   .. automethod:: LearningProxyManager.get_activities_by_objective_bank

   .. automethod:: LearningProxyManager.get_activity_ids_by_objective_banks

   .. automethod:: LearningProxyManager.get_activities_by_objective_banks

   .. automethod:: LearningProxyManager.get_objective_bank_ids_by_activity

   .. automethod:: LearningProxyManager.get_objective_banks_by_activity



Activity Objective Bank Assignment Methods
------------------------------------------

   .. automethod:: LearningProxyManager.can_assign_activities

   .. automethod:: LearningProxyManager.can_assign_activities_to_objective_bank

   .. automethod:: LearningProxyManager.get_assignable_objective_bank_ids

   .. automethod:: LearningProxyManager.get_assignable_objective_bank_ids_for_activity

   .. automethod:: LearningProxyManager.assign_activity_to_objective_bank

   .. automethod:: LearningProxyManager.unassign_activity_from_objective_bank

   .. automethod:: LearningProxyManager.reassign_activity_to_objective_bank



Objective Bank Lookup Methods
-----------------------------

   .. automethod:: LearningProxyManager.can_lookup_objective_banks

   .. automethod:: LearningProxyManager.use_comparative_objective_bank_view

   .. automethod:: LearningProxyManager.use_plenary_objective_bank_view

   .. automethod:: LearningProxyManager.get_objective_bank

   .. automethod:: LearningProxyManager.get_objective_banks_by_ids

   .. automethod:: LearningProxyManager.get_objective_banks_by_genus_type

   .. automethod:: LearningProxyManager.get_objective_banks_by_parent_genus_type

   .. automethod:: LearningProxyManager.get_objective_banks_by_record_type

   .. automethod:: LearningProxyManager.get_objective_banks_by_provider

   .. autoattribute:: LearningProxyManager.objective_banks



Objective Bank Admin Methods
----------------------------

   .. automethod:: LearningProxyManager.can_create_objective_banks

   .. automethod:: LearningProxyManager.can_create_objective_bank_with_record_types

   .. automethod:: LearningProxyManager.get_objective_bank_form_for_create

   .. automethod:: LearningProxyManager.create_objective_bank

   .. automethod:: LearningProxyManager.can_update_objective_banks

   .. automethod:: LearningProxyManager.get_objective_bank_form_for_update

   .. automethod:: LearningProxyManager.update_objective_bank

   .. automethod:: LearningProxyManager.can_delete_objective_banks

   .. automethod:: LearningProxyManager.delete_objective_bank

   .. automethod:: LearningProxyManager.can_manage_objective_bank_aliases

   .. automethod:: LearningProxyManager.alias_objective_bank



Objective Bank Hierarchy Methods
--------------------------------

   .. autoattribute:: LearningProxyManager.objective_bank_hierarchy_id

   .. autoattribute:: LearningProxyManager.objective_bank_hierarchy

   .. automethod:: LearningProxyManager.can_access_objective_bank_hierarchy

   .. automethod:: LearningProxyManager.use_comparative_objective_bank_view

   .. automethod:: LearningProxyManager.use_plenary_objective_bank_view

   .. autoattribute:: LearningProxyManager.root_objective_bank_ids

   .. autoattribute:: LearningProxyManager.root_objective_banks

   .. automethod:: LearningProxyManager.has_parent_objective_banks

   .. automethod:: LearningProxyManager.is_parent_of_objective_bank

   .. automethod:: LearningProxyManager.get_parent_objective_bank_ids

   .. automethod:: LearningProxyManager.get_parent_objective_banks

   .. automethod:: LearningProxyManager.is_ancestor_of_objective_bank

   .. automethod:: LearningProxyManager.has_child_objective_banks

   .. automethod:: LearningProxyManager.is_child_of_objective_bank

   .. automethod:: LearningProxyManager.get_child_objective_bank_ids

   .. automethod:: LearningProxyManager.get_child_objective_banks

   .. automethod:: LearningProxyManager.is_descendant_of_objective_bank

   .. automethod:: LearningProxyManager.get_objective_bank_node_ids

   .. automethod:: LearningProxyManager.get_objective_bank_nodes



Objective Bank Hierarchy Design Methods
---------------------------------------

   .. autoattribute:: LearningProxyManager.objective_bank_hierarchy_id

   .. autoattribute:: LearningProxyManager.objective_bank_hierarchy

   .. automethod:: LearningProxyManager.can_modify_objective_bank_hierarchy

   .. automethod:: LearningProxyManager.add_root_objective_bank

   .. automethod:: LearningProxyManager.remove_root_objective_bank

   .. automethod:: LearningProxyManager.add_child_objective_bank

   .. automethod:: LearningProxyManager.remove_child_objective_bank

   .. automethod:: LearningProxyManager.remove_child_objective_banks



