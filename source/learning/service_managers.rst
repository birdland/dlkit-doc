Summary
=======
.. currentmodule:: dlkit.services.learning
.. automodule:: dlkit.services.learning

Service_Managers
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



Objective Bank Query
____________________

   .. automethod:: LearningManager.can_search_objective_banks

   .. autoattribute:: LearningManager.objective_bank_query

   .. automethod:: LearningManager.get_objective_banks_by_query



Objective Bank Search
_____________________

   .. autoattribute:: LearningManager.objective_bank_search

   .. autoattribute:: LearningManager.objective_bank_search_order

   .. automethod:: LearningManager.get_objective_banks_by_search

   .. automethod:: LearningManager.get_objective_bank_query_from_inspector



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



Objective Bank Notification
___________________________

   .. automethod:: LearningManager.can_register_for_objective_bank_notifications

   .. automethod:: LearningManager.register_for_new_objective_banks

   .. automethod:: LearningManager.register_for_new_objective_bank_ancestors

   .. automethod:: LearningManager.register_for_new_objective_bank_descendants

   .. automethod:: LearningManager.register_for_changed_objective_banks

   .. automethod:: LearningManager.register_for_changed_objective_bank

   .. automethod:: LearningManager.register_for_deleted_objective_banks

   .. automethod:: LearningManager.register_for_deleted_objective_bank

   .. automethod:: LearningManager.register_for_deleted_objective_bank_ancestors

   .. automethod:: LearningManager.register_for_deleted_objective_bank_descendants



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



Learning Proxy Manager
----------------------

.. autoclass:: LearningProxyManager
   :show-inheritance:

   .. autoattribute:: LearningProxyManager.learning_batch_proxy_manager



Learning Profile Methods
________________

   .. automethod:: LearningProxyManager.supports_visible_federation

   .. automethod:: LearningProxyManager.supports_objective_lookup

   .. automethod:: LearningProxyManager.supports_objective_query

   .. automethod:: LearningProxyManager.supports_objective_search

   .. automethod:: LearningProxyManager.supports_objective_admin

   .. automethod:: LearningProxyManager.supports_objective_notification

   .. automethod:: LearningProxyManager.supports_objective_hierarchy

   .. automethod:: LearningProxyManager.supports_objective_hierarchy_design

   .. automethod:: LearningProxyManager.supports_objective_sequencing

   .. automethod:: LearningProxyManager.supports_objective_objective_bank

   .. automethod:: LearningProxyManager.supports_objective_objective_bank_assignment

   .. automethod:: LearningProxyManager.supports_objective_smart_objective_bank

   .. automethod:: LearningProxyManager.supports_objective_requisite

   .. automethod:: LearningProxyManager.supports_objective_requisite_assignment

   .. automethod:: LearningProxyManager.supports_activity_lookup

   .. automethod:: LearningProxyManager.supports_activity_query

   .. automethod:: LearningProxyManager.supports_activity_search

   .. automethod:: LearningProxyManager.supports_activity_admin

   .. automethod:: LearningProxyManager.supports_activity_notification

   .. automethod:: LearningProxyManager.supports_activity_objective_bank

   .. automethod:: LearningProxyManager.supports_activity_objective_bank_assignment

   .. automethod:: LearningProxyManager.supports_activity_smart_objective_bank

   .. automethod:: LearningProxyManager.supports_proficiency_lookup

   .. automethod:: LearningProxyManager.supports_proficiency_query

   .. automethod:: LearningProxyManager.supports_proficiency_search

   .. automethod:: LearningProxyManager.supports_proficiency_admin

   .. automethod:: LearningProxyManager.supports_proficiency_notification

   .. automethod:: LearningProxyManager.supports_proficiency_objective_bank

   .. automethod:: LearningProxyManager.supports_proficiency_objective_bank_assignment

   .. automethod:: LearningProxyManager.supports_proficiency_smart_objective_bank

   .. automethod:: LearningProxyManager.supports_my_learning_path

   .. automethod:: LearningProxyManager.supports_learning_path

   .. automethod:: LearningProxyManager.supports_objective_bank_lookup

   .. automethod:: LearningProxyManager.supports_objective_bank_query

   .. automethod:: LearningProxyManager.supports_objective_bank_search

   .. automethod:: LearningProxyManager.supports_objective_bank_admin

   .. automethod:: LearningProxyManager.supports_objective_bank_notification

   .. automethod:: LearningProxyManager.supports_objective_bank_hierarchy

   .. automethod:: LearningProxyManager.supports_objective_bank_hierarchy_design

   .. automethod:: LearningProxyManager.supports_learning_batch

   .. autoattribute:: LearningProxyManager.objective_record_types

   .. automethod:: LearningProxyManager.supports_objective_record_type

   .. autoattribute:: LearningProxyManager.objective_search_record_types

   .. automethod:: LearningProxyManager.supports_objective_search_record_type

   .. autoattribute:: LearningProxyManager.activity_record_types

   .. automethod:: LearningProxyManager.supports_activity_record_type

   .. autoattribute:: LearningProxyManager.activity_search_record_types

   .. automethod:: LearningProxyManager.supports_activity_search_record_type

   .. autoattribute:: LearningProxyManager.proficiency_record_types

   .. automethod:: LearningProxyManager.supports_proficiency_record_type

   .. autoattribute:: LearningProxyManager.proficiency_search_record_types

   .. automethod:: LearningProxyManager.supports_proficiency_search_record_type

   .. autoattribute:: LearningProxyManager.objective_bank_record_types

   .. automethod:: LearningProxyManager.supports_objective_bank_record_type

   .. autoattribute:: LearningProxyManager.objective_bank_search_record_types

   .. automethod:: LearningProxyManager.supports_objective_bank_search_record_type



Objective Bank Lookup
_____________________

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



Objective Bank Query
____________________

   .. automethod:: LearningProxyManager.can_search_objective_banks

   .. autoattribute:: LearningProxyManager.objective_bank_query

   .. automethod:: LearningProxyManager.get_objective_banks_by_query



Objective Bank Search
_____________________

   .. autoattribute:: LearningProxyManager.objective_bank_search

   .. autoattribute:: LearningProxyManager.objective_bank_search_order

   .. automethod:: LearningProxyManager.get_objective_banks_by_search

   .. automethod:: LearningProxyManager.get_objective_bank_query_from_inspector



Objective Bank Admin
____________________

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



Objective Bank Notification
___________________________

   .. automethod:: LearningProxyManager.can_register_for_objective_bank_notifications

   .. automethod:: LearningProxyManager.register_for_new_objective_banks

   .. automethod:: LearningProxyManager.register_for_new_objective_bank_ancestors

   .. automethod:: LearningProxyManager.register_for_new_objective_bank_descendants

   .. automethod:: LearningProxyManager.register_for_changed_objective_banks

   .. automethod:: LearningProxyManager.register_for_changed_objective_bank

   .. automethod:: LearningProxyManager.register_for_deleted_objective_banks

   .. automethod:: LearningProxyManager.register_for_deleted_objective_bank

   .. automethod:: LearningProxyManager.register_for_deleted_objective_bank_ancestors

   .. automethod:: LearningProxyManager.register_for_deleted_objective_bank_descendants



Objective Bank Hierarchy
________________________

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



Objective Bank Hierarchy Design
_______________________________

   .. autoattribute:: LearningProxyManager.objective_bank_hierarchy_id

   .. autoattribute:: LearningProxyManager.objective_bank_hierarchy

   .. automethod:: LearningProxyManager.can_modify_objective_bank_hierarchy

   .. automethod:: LearningProxyManager.add_root_objective_bank

   .. automethod:: LearningProxyManager.remove_root_objective_bank

   .. automethod:: LearningProxyManager.add_child_objective_bank

   .. automethod:: LearningProxyManager.remove_child_objective_bank

   .. automethod:: LearningProxyManager.remove_child_objective_banks



