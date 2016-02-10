
.. currentmodule:: dlkit.services.learning
.. automodule:: dlkit.services.learning

Service Managers
================


Learning Profile
----------------

.. autoclass:: LearningProfile
   :show-inheritance:

   .. automethod:: LearningProfile.supports_visible_federation

   .. automethod:: LearningProfile.supports_objective_lookup

   .. automethod:: LearningProfile.supports_objective_query

   .. automethod:: LearningProfile.supports_objective_search

   .. automethod:: LearningProfile.supports_objective_admin

   .. automethod:: LearningProfile.supports_objective_notification

   .. automethod:: LearningProfile.supports_objective_hierarchy

   .. automethod:: LearningProfile.supports_objective_hierarchy_design

   .. automethod:: LearningProfile.supports_objective_sequencing

   .. automethod:: LearningProfile.supports_objective_objective_bank

   .. automethod:: LearningProfile.supports_objective_objective_bank_assignment

   .. automethod:: LearningProfile.supports_objective_smart_objective_bank

   .. automethod:: LearningProfile.supports_objective_requisite

   .. automethod:: LearningProfile.supports_objective_requisite_assignment

   .. automethod:: LearningProfile.supports_activity_lookup

   .. automethod:: LearningProfile.supports_activity_query

   .. automethod:: LearningProfile.supports_activity_search

   .. automethod:: LearningProfile.supports_activity_admin

   .. automethod:: LearningProfile.supports_activity_notification

   .. automethod:: LearningProfile.supports_activity_objective_bank

   .. automethod:: LearningProfile.supports_activity_objective_bank_assignment

   .. automethod:: LearningProfile.supports_activity_smart_objective_bank

   .. automethod:: LearningProfile.supports_proficiency_lookup

   .. automethod:: LearningProfile.supports_proficiency_query

   .. automethod:: LearningProfile.supports_proficiency_search

   .. automethod:: LearningProfile.supports_proficiency_admin

   .. automethod:: LearningProfile.supports_proficiency_notification

   .. automethod:: LearningProfile.supports_proficiency_objective_bank

   .. automethod:: LearningProfile.supports_proficiency_objective_bank_assignment

   .. automethod:: LearningProfile.supports_proficiency_smart_objective_bank

   .. automethod:: LearningProfile.supports_my_learning_path

   .. automethod:: LearningProfile.supports_learning_path

   .. automethod:: LearningProfile.supports_objective_bank_lookup

   .. automethod:: LearningProfile.supports_objective_bank_query

   .. automethod:: LearningProfile.supports_objective_bank_search

   .. automethod:: LearningProfile.supports_objective_bank_admin

   .. automethod:: LearningProfile.supports_objective_bank_notification

   .. automethod:: LearningProfile.supports_objective_bank_hierarchy

   .. automethod:: LearningProfile.supports_objective_bank_hierarchy_design

   .. automethod:: LearningProfile.supports_learning_batch

   .. autoattribute:: LearningProfile.objective_record_types

   .. automethod:: LearningProfile.supports_objective_record_type

   .. autoattribute:: LearningProfile.objective_search_record_types

   .. automethod:: LearningProfile.supports_objective_search_record_type

   .. autoattribute:: LearningProfile.activity_record_types

   .. automethod:: LearningProfile.supports_activity_record_type

   .. autoattribute:: LearningProfile.activity_search_record_types

   .. automethod:: LearningProfile.supports_activity_search_record_type

   .. autoattribute:: LearningProfile.proficiency_record_types

   .. automethod:: LearningProfile.supports_proficiency_record_type

   .. autoattribute:: LearningProfile.proficiency_search_record_types

   .. automethod:: LearningProfile.supports_proficiency_search_record_type

   .. autoattribute:: LearningProfile.objective_bank_record_types

   .. automethod:: LearningProfile.supports_objective_bank_record_type

   .. autoattribute:: LearningProfile.objective_bank_search_record_types

   .. automethod:: LearningProfile.supports_objective_bank_search_record_type

Learning Manager
----------------

.. autoclass:: LearningManager
   :show-inheritance:

   .. autoattribute:: LearningManager.learning_batch_manager



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



