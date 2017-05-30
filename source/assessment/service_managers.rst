
.. currentmodule:: dlkit.services.assessment
.. automodule:: dlkit.services.assessment

Service Managers
================


Assessment Profile
------------------

.. autoclass:: AssessmentProfile
   :show-inheritance:

   .. automethod:: AssessmentProfile.supports_assessment

   .. automethod:: AssessmentProfile.supports_assessment_results

   .. automethod:: AssessmentProfile.supports_item_lookup

   .. automethod:: AssessmentProfile.supports_item_query

   .. automethod:: AssessmentProfile.supports_item_search

   .. automethod:: AssessmentProfile.supports_item_admin

   .. automethod:: AssessmentProfile.supports_item_notification

   .. automethod:: AssessmentProfile.supports_item_bank

   .. automethod:: AssessmentProfile.supports_item_bank_assignment

   .. automethod:: AssessmentProfile.supports_assessment_lookup

   .. automethod:: AssessmentProfile.supports_assessment_query

   .. automethod:: AssessmentProfile.supports_assessment_admin

   .. automethod:: AssessmentProfile.supports_assessment_bank

   .. automethod:: AssessmentProfile.supports_assessment_bank_assignment

   .. automethod:: AssessmentProfile.supports_assessment_basic_authoring

   .. automethod:: AssessmentProfile.supports_assessment_offered_lookup

   .. automethod:: AssessmentProfile.supports_assessment_offered_query

   .. automethod:: AssessmentProfile.supports_assessment_offered_admin

   .. automethod:: AssessmentProfile.supports_assessment_offered_bank

   .. automethod:: AssessmentProfile.supports_assessment_offered_bank_assignment

   .. automethod:: AssessmentProfile.supports_assessment_taken_lookup

   .. automethod:: AssessmentProfile.supports_assessment_taken_query

   .. automethod:: AssessmentProfile.supports_assessment_taken_admin

   .. automethod:: AssessmentProfile.supports_assessment_taken_bank

   .. automethod:: AssessmentProfile.supports_assessment_taken_bank_assignment

   .. automethod:: AssessmentProfile.supports_bank_lookup

   .. automethod:: AssessmentProfile.supports_bank_query

   .. automethod:: AssessmentProfile.supports_bank_admin

   .. automethod:: AssessmentProfile.supports_bank_hierarchy

   .. automethod:: AssessmentProfile.supports_bank_hierarchy_design

   .. autoattribute:: AssessmentProfile.item_record_types

   .. autoattribute:: AssessmentProfile.item_search_record_types

   .. autoattribute:: AssessmentProfile.assessment_record_types

   .. autoattribute:: AssessmentProfile.assessment_search_record_types

   .. autoattribute:: AssessmentProfile.assessment_offered_record_types

   .. autoattribute:: AssessmentProfile.assessment_offered_search_record_types

   .. autoattribute:: AssessmentProfile.assessment_taken_record_types

   .. autoattribute:: AssessmentProfile.assessment_taken_search_record_types

   .. autoattribute:: AssessmentProfile.assessment_section_record_types

   .. autoattribute:: AssessmentProfile.bank_record_types

   .. autoattribute:: AssessmentProfile.bank_search_record_types

Assessment Manager
------------------

.. autoclass:: AssessmentManager
   :show-inheritance:

   .. autoattribute:: AssessmentManager.assessment_authoring_manager

   .. autoattribute:: AssessmentManager.assessment_batch_manager



Bank Lookup Methods
-------------------

   .. automethod:: AssessmentManager.can_lookup_banks

   .. automethod:: AssessmentManager.use_comparative_bank_view

   .. automethod:: AssessmentManager.use_plenary_bank_view

   .. automethod:: AssessmentManager.get_bank

   .. automethod:: AssessmentManager.get_banks_by_ids

   .. automethod:: AssessmentManager.get_banks_by_genus_type

   .. automethod:: AssessmentManager.get_banks_by_parent_genus_type

   .. automethod:: AssessmentManager.get_banks_by_record_type

   .. automethod:: AssessmentManager.get_banks_by_provider

   .. autoattribute:: AssessmentManager.banks



Bank Query Methods
------------------

   .. automethod:: AssessmentManager.can_search_banks

   .. autoattribute:: AssessmentManager.bank_query

   .. automethod:: AssessmentManager.get_banks_by_query



Bank Admin Methods
------------------

   .. automethod:: AssessmentManager.can_create_banks

   .. automethod:: AssessmentManager.can_create_bank_with_record_types

   .. automethod:: AssessmentManager.get_bank_form_for_create

   .. automethod:: AssessmentManager.create_bank

   .. automethod:: AssessmentManager.can_update_banks

   .. automethod:: AssessmentManager.get_bank_form_for_update

   .. automethod:: AssessmentManager.update_bank

   .. automethod:: AssessmentManager.can_delete_banks

   .. automethod:: AssessmentManager.delete_bank

   .. automethod:: AssessmentManager.can_manage_bank_aliases

   .. automethod:: AssessmentManager.alias_bank



Bank Hierarchy Methods
----------------------

   .. autoattribute:: AssessmentManager.bank_hierarchy_id

   .. autoattribute:: AssessmentManager.bank_hierarchy

   .. automethod:: AssessmentManager.can_access_bank_hierarchy

   .. automethod:: AssessmentManager.use_comparative_bank_view

   .. automethod:: AssessmentManager.use_plenary_bank_view

   .. autoattribute:: AssessmentManager.root_bank_ids

   .. autoattribute:: AssessmentManager.root_banks

   .. automethod:: AssessmentManager.has_parent_banks

   .. automethod:: AssessmentManager.is_parent_of_bank

   .. automethod:: AssessmentManager.get_parent_bank_ids

   .. automethod:: AssessmentManager.get_parent_banks

   .. automethod:: AssessmentManager.is_ancestor_of_bank

   .. automethod:: AssessmentManager.has_child_banks

   .. automethod:: AssessmentManager.is_child_of_bank

   .. automethod:: AssessmentManager.get_child_bank_ids

   .. automethod:: AssessmentManager.get_child_banks

   .. automethod:: AssessmentManager.is_descendant_of_bank

   .. automethod:: AssessmentManager.get_bank_node_ids

   .. automethod:: AssessmentManager.get_bank_nodes



Bank Hierarchy Design Methods
-----------------------------

   .. autoattribute:: AssessmentManager.bank_hierarchy_id

   .. autoattribute:: AssessmentManager.bank_hierarchy

   .. automethod:: AssessmentManager.can_modify_bank_hierarchy

   .. automethod:: AssessmentManager.add_root_bank

   .. automethod:: AssessmentManager.remove_root_bank

   .. automethod:: AssessmentManager.add_child_bank

   .. automethod:: AssessmentManager.remove_child_bank

   .. automethod:: AssessmentManager.remove_child_banks



