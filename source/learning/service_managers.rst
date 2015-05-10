Summary
=======
.. currentmodule:: dlkit.services.learning
.. automodule:: dlkit.services.learning

Service Managers
================


Learning Manager
----------------

.. autoclass:: LearningManager
   :show-inheritance:

   .. autoattribute:: LearningManager.learning_batch_manager



Learning Profile Methods
________________

   .. automethod:: LearningManager.supports_visible_federation

   .. automethod:: LearningManager.supports_objective_lookup

   .. automethod:: LearningManager.supports_objective_query

   .. automethod:: LearningManager.supports_objective_search

   .. automethod:: LearningManager.supports_objective_admin

   .. automethod:: LearningManager.supports_objective_notification

   .. automethod:: LearningManager.supports_objective_hierarchy

   .. automethod:: LearningManager.supports_objective_hierarchy_design

   .. automethod:: LearningManager.supports_objective_sequencing

   .. automethod:: LearningManager.supports_objective_objective_bank

   .. automethod:: LearningManager.supports_objective_objective_bank_assignment

   .. automethod:: LearningManager.supports_objective_smart_objective_bank

   .. automethod:: LearningManager.supports_objective_requisite

   .. automethod:: LearningManager.supports_objective_requisite_assignment

   .. automethod:: LearningManager.supports_activity_lookup

   .. automethod:: LearningManager.supports_activity_query

   .. automethod:: LearningManager.supports_activity_search

   .. automethod:: LearningManager.supports_activity_admin

   .. automethod:: LearningManager.supports_activity_notification

   .. automethod:: LearningManager.supports_activity_objective_bank

   .. automethod:: LearningManager.supports_activity_objective_bank_assignment

   .. automethod:: LearningManager.supports_activity_smart_objective_bank

   .. automethod:: LearningManager.supports_proficiency_lookup

   .. automethod:: LearningManager.supports_proficiency_query

   .. automethod:: LearningManager.supports_proficiency_search

   .. automethod:: LearningManager.supports_proficiency_admin

   .. automethod:: LearningManager.supports_proficiency_notification

   .. automethod:: LearningManager.supports_proficiency_objective_bank

   .. automethod:: LearningManager.supports_proficiency_objective_bank_assignment

   .. automethod:: LearningManager.supports_proficiency_smart_objective_bank

   .. automethod:: LearningManager.supports_my_learning_path

   .. automethod:: LearningManager.supports_learning_path

   .. automethod:: LearningManager.supports_objective_bank_lookup

   .. automethod:: LearningManager.supports_objective_bank_query

   .. automethod:: LearningManager.supports_objective_bank_search

   .. automethod:: LearningManager.supports_objective_bank_admin

   .. automethod:: LearningManager.supports_objective_bank_notification

   .. automethod:: LearningManager.supports_objective_bank_hierarchy

   .. automethod:: LearningManager.supports_objective_bank_hierarchy_design

   .. automethod:: LearningManager.supports_learning_batch

   .. autoattribute:: LearningManager.objective_record_types

   .. automethod:: LearningManager.supports_objective_record_type

   .. autoattribute:: LearningManager.objective_search_record_types

   .. automethod:: LearningManager.supports_objective_search_record_type

   .. autoattribute:: LearningManager.activity_record_types

   .. automethod:: LearningManager.supports_activity_record_type

   .. autoattribute:: LearningManager.activity_search_record_types

   .. automethod:: LearningManager.supports_activity_search_record_type

   .. autoattribute:: LearningManager.proficiency_record_types

   .. automethod:: LearningManager.supports_proficiency_record_type

   .. autoattribute:: LearningManager.proficiency_search_record_types

   .. automethod:: LearningManager.supports_proficiency_search_record_type

   .. autoattribute:: LearningManager.objective_bank_record_types

   .. automethod:: LearningManager.supports_objective_bank_record_type

   .. autoattribute:: LearningManager.objective_bank_search_record_types

   .. automethod:: LearningManager.supports_objective_bank_search_record_type



Objective Bank Lookup
_____________________

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



Objective Bank Admin
____________________

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



Objective Bank Hierarchy
________________________

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



Objective Bank Hierarchy Design
_______________________________

   .. autoattribute:: LearningManager.objective_bank_hierarchy_id

   .. autoattribute:: LearningManager.objective_bank_hierarchy

   .. automethod:: LearningManager.can_modify_objective_bank_hierarchy

   .. automethod:: LearningManager.add_root_objective_bank

   .. automethod:: LearningManager.remove_root_objective_bank

   .. automethod:: LearningManager.add_child_objective_bank

   .. automethod:: LearningManager.remove_child_objective_bank

   .. automethod:: LearningManager.remove_child_objective_banks



