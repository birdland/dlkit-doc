
.. currentmodule:: dlkit.assessment.queries
.. automodule:: dlkit.assessment.queries

Queries
=======


Question Query
--------------

.. autoclass:: QuestionQuery
   :show-inheritance:

   .. automethod:: QuestionQuery.get_question_query_record



Item Bank Methods
-----------------

   .. automethod:: ItemBankSession.can_lookup_item_bank_mappings

   .. automethod:: ItemBankSession.use_comparative_bank_view

   .. automethod:: ItemBankSession.use_plenary_bank_view

   .. automethod:: ItemBankSession.get_item_ids_by_bank

   .. automethod:: ItemBankSession.get_items_by_bank

   .. automethod:: ItemBankSession.get_item_ids_by_banks

   .. automethod:: ItemBankSession.get_items_by_banks

   .. automethod:: ItemBankSession.get_bank_ids_by_item

   .. automethod:: ItemBankSession.get_banks_by_item



Item Bank Assignment Methods
----------------------------

   .. automethod:: ItemBankAssignmentSession.can_assign_items

   .. automethod:: ItemBankAssignmentSession.can_assign_items_to_bank

   .. automethod:: ItemBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: ItemBankAssignmentSession.get_assignable_bank_ids_for_item

   .. automethod:: ItemBankAssignmentSession.assign_item_to_bank

   .. automethod:: ItemBankAssignmentSession.unassign_item_from_bank

   .. automethod:: ItemBankAssignmentSession.reassign_item_to_billing



Assessment Bank Methods
-----------------------

   .. automethod:: AssessmentBankSession.can_lookup_assessment_bank_mappings

   .. automethod:: AssessmentBankSession.use_comparative_bank_view

   .. automethod:: AssessmentBankSession.use_plenary_bank_view

   .. automethod:: AssessmentBankSession.get_assessment_ids_by_bank

   .. automethod:: AssessmentBankSession.get_assessments_by_bank

   .. automethod:: AssessmentBankSession.get_assessment_ids_by_banks

   .. automethod:: AssessmentBankSession.get_assessments_by_banks

   .. automethod:: AssessmentBankSession.get_bank_ids_by_assessment

   .. automethod:: AssessmentBankSession.get_banks_by_assessment



Assessment Bank Assignment Methods
----------------------------------

   .. automethod:: AssessmentBankAssignmentSession.can_assign_assessments

   .. automethod:: AssessmentBankAssignmentSession.can_assign_assessments_to_bank

   .. automethod:: AssessmentBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentBankAssignmentSession.get_assignable_bank_ids_for_assessment

   .. automethod:: AssessmentBankAssignmentSession.assign_assessment_to_bank

   .. automethod:: AssessmentBankAssignmentSession.unassign_assessment_from_bank

   .. automethod:: AssessmentBankAssignmentSession.reassign_assessment_to_billing



Assessment Offered Bank Methods
-------------------------------

   .. automethod:: AssessmentOfferedBankSession.can_lookup_assessment_offered_bank_mappings

   .. automethod:: AssessmentOfferedBankSession.use_comparative_bank_view

   .. automethod:: AssessmentOfferedBankSession.use_plenary_bank_view

   .. automethod:: AssessmentOfferedBankSession.get_assessment_offered_ids_by_bank

   .. automethod:: AssessmentOfferedBankSession.get_assessments_offered_by_bank

   .. automethod:: AssessmentOfferedBankSession.get_assessment_offered_ids_by_banks

   .. automethod:: AssessmentOfferedBankSession.get_assessments_offered_by_banks

   .. automethod:: AssessmentOfferedBankSession.get_bank_ids_by_assessment_offered

   .. automethod:: AssessmentOfferedBankSession.get_banks_by_assessment_offered



Assessment Offered Bank Assignment Methods
------------------------------------------

   .. automethod:: AssessmentOfferedBankAssignmentSession.can_assign_assessments_offered

   .. automethod:: AssessmentOfferedBankAssignmentSession.can_assign_assessments_offered_to_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentOfferedBankAssignmentSession.get_assignable_bank_ids_for_assessment_offered

   .. automethod:: AssessmentOfferedBankAssignmentSession.assign_assessment_offered_to_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.unassign_assessment_offered_from_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.reassign_assessment_offered_to_billing



Assessment Taken Bank Methods
-----------------------------

   .. automethod:: AssessmentTakenBankSession.can_lookup_assessment_taken_bank_mappings

   .. automethod:: AssessmentTakenBankSession.use_comparative_bank_view

   .. automethod:: AssessmentTakenBankSession.use_plenary_bank_view

   .. automethod:: AssessmentTakenBankSession.get_assessment_taken_ids_by_bank

   .. automethod:: AssessmentTakenBankSession.get_assessments_taken_by_bank

   .. automethod:: AssessmentTakenBankSession.get_assessment_taken_ids_by_banks

   .. automethod:: AssessmentTakenBankSession.get_assessments_taken_by_banks

   .. automethod:: AssessmentTakenBankSession.get_bank_ids_by_assessment_taken

   .. automethod:: AssessmentTakenBankSession.get_banks_by_assessment_taken



Assessment Taken Bank Assignment Methods
----------------------------------------

   .. automethod:: AssessmentTakenBankAssignmentSession.can_assign_assessments_taken

   .. automethod:: AssessmentTakenBankAssignmentSession.can_assign_assessments_taken_to_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentTakenBankAssignmentSession.get_assignable_bank_ids_for_assessment_taken

   .. automethod:: AssessmentTakenBankAssignmentSession.assign_assessment_taken_to_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.unassign_assessment_taken_from_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.reassign_assessment_taken_to_billing



Bank Lookup Methods
-------------------

   .. automethod:: BankLookupSession.can_lookup_banks

   .. automethod:: BankLookupSession.use_comparative_bank_view

   .. automethod:: BankLookupSession.use_plenary_bank_view

   .. automethod:: BankLookupSession.get_bank

   .. automethod:: BankLookupSession.get_banks_by_ids

   .. automethod:: BankLookupSession.get_banks_by_genus_type

   .. automethod:: BankLookupSession.get_banks_by_parent_genus_type

   .. automethod:: BankLookupSession.get_banks_by_record_type

   .. automethod:: BankLookupSession.get_banks_by_provider

   .. autoattribute:: BankLookupSession.banks



Bank Query Methods
------------------

   .. automethod:: BankQuerySession.can_search_banks

   .. autoattribute:: BankQuerySession.bank_query

   .. automethod:: BankQuerySession.get_banks_by_query



Bank Admin Methods
------------------

   .. automethod:: BankAdminSession.can_create_banks

   .. automethod:: BankAdminSession.can_create_bank_with_record_types

   .. automethod:: BankAdminSession.get_bank_form_for_create

   .. automethod:: BankAdminSession.create_bank

   .. automethod:: BankAdminSession.can_update_banks

   .. automethod:: BankAdminSession.get_bank_form_for_update

   .. automethod:: BankAdminSession.update_bank

   .. automethod:: BankAdminSession.can_delete_banks

   .. automethod:: BankAdminSession.delete_bank

   .. automethod:: BankAdminSession.can_manage_bank_aliases

   .. automethod:: BankAdminSession.alias_bank



Bank Hierarchy Methods
----------------------

   .. autoattribute:: BankHierarchySession.bank_hierarchy_id

   .. autoattribute:: BankHierarchySession.bank_hierarchy

   .. automethod:: BankHierarchySession.can_access_bank_hierarchy

   .. automethod:: BankHierarchySession.use_comparative_bank_view

   .. automethod:: BankHierarchySession.use_plenary_bank_view

   .. autoattribute:: BankHierarchySession.root_bank_ids

   .. autoattribute:: BankHierarchySession.root_banks

   .. automethod:: BankHierarchySession.has_parent_banks

   .. automethod:: BankHierarchySession.is_parent_of_bank

   .. automethod:: BankHierarchySession.get_parent_bank_ids

   .. automethod:: BankHierarchySession.get_parent_banks

   .. automethod:: BankHierarchySession.is_ancestor_of_bank

   .. automethod:: BankHierarchySession.has_child_banks

   .. automethod:: BankHierarchySession.is_child_of_bank

   .. automethod:: BankHierarchySession.get_child_bank_ids

   .. automethod:: BankHierarchySession.get_child_banks

   .. automethod:: BankHierarchySession.is_descendant_of_bank

   .. automethod:: BankHierarchySession.get_bank_node_ids

   .. automethod:: BankHierarchySession.get_bank_nodes



Bank Hierarchy Design Methods
-----------------------------

   .. autoattribute:: BankHierarchyDesignSession.bank_hierarchy_id

   .. autoattribute:: BankHierarchyDesignSession.bank_hierarchy

   .. automethod:: BankHierarchyDesignSession.can_modify_bank_hierarchy

   .. automethod:: BankHierarchyDesignSession.add_root_bank

   .. automethod:: BankHierarchyDesignSession.remove_root_bank

   .. automethod:: BankHierarchyDesignSession.add_child_bank

   .. automethod:: BankHierarchyDesignSession.remove_child_bank

   .. automethod:: BankHierarchyDesignSession.remove_child_banks



Assessment Methods
------------------

   .. autoattribute:: AssessmentSession.bank_id

   .. autoattribute:: AssessmentSession.bank

   .. automethod:: AssessmentSession.can_take_assessments

   .. automethod:: AssessmentSession.has_assessment_begun

   .. automethod:: AssessmentSession.is_assessment_over

   .. automethod:: AssessmentSession.requires_synchronous_sections

   .. automethod:: AssessmentSession.get_first_assessment_section

   .. automethod:: AssessmentSession.has_next_assessment_section

   .. automethod:: AssessmentSession.get_next_assessment_section

   .. automethod:: AssessmentSession.has_previous_assessment_section

   .. automethod:: AssessmentSession.get_previous_assessment_section

   .. automethod:: AssessmentSession.get_assessment_section

   .. automethod:: AssessmentSession.get_assessment_sections

   .. automethod:: AssessmentSession.is_assessment_section_complete

   .. automethod:: AssessmentSession.get_incomplete_assessment_sections

   .. automethod:: AssessmentSession.has_assessment_section_begun

   .. automethod:: AssessmentSession.is_assessment_section_over

   .. automethod:: AssessmentSession.requires_synchronous_responses

   .. automethod:: AssessmentSession.get_first_question

   .. automethod:: AssessmentSession.has_next_question

   .. automethod:: AssessmentSession.get_next_question

   .. automethod:: AssessmentSession.has_previous_question

   .. automethod:: AssessmentSession.get_previous_question

   .. automethod:: AssessmentSession.get_question

   .. automethod:: AssessmentSession.get_questions

   .. automethod:: AssessmentSession.get_response_form

   .. automethod:: AssessmentSession.submit_response

   .. automethod:: AssessmentSession.skip_item

   .. automethod:: AssessmentSession.is_question_answered

   .. automethod:: AssessmentSession.get_unanswered_questions

   .. automethod:: AssessmentSession.has_unanswered_questions

   .. automethod:: AssessmentSession.get_first_unanswered_question

   .. automethod:: AssessmentSession.has_next_unanswered_question

   .. automethod:: AssessmentSession.get_next_unanswered_question

   .. automethod:: AssessmentSession.has_previous_unanswered_question

   .. automethod:: AssessmentSession.get_previous_unanswered_question

   .. automethod:: AssessmentSession.get_response

   .. automethod:: AssessmentSession.get_responses

   .. automethod:: AssessmentSession.clear_response

   .. automethod:: AssessmentSession.finish_assessment_section

   .. automethod:: AssessmentSession.is_answer_available

   .. automethod:: AssessmentSession.get_answers

   .. automethod:: AssessmentSession.finish_assessment



Item Lookup Methods
-------------------

   .. autoattribute:: ItemLookupSession.bank_id

   .. autoattribute:: ItemLookupSession.bank

   .. automethod:: ItemLookupSession.can_lookup_items

   .. automethod:: ItemLookupSession.use_comparative_item_view

   .. automethod:: ItemLookupSession.use_plenary_item_view

   .. automethod:: ItemLookupSession.use_federated_bank_view

   .. automethod:: ItemLookupSession.use_isolated_bank_view

   .. automethod:: ItemLookupSession.get_item

   .. automethod:: ItemLookupSession.get_items_by_ids

   .. automethod:: ItemLookupSession.get_items_by_genus_type

   .. automethod:: ItemLookupSession.get_items_by_parent_genus_type

   .. automethod:: ItemLookupSession.get_items_by_record_type

   .. automethod:: ItemLookupSession.get_items_by_question

   .. automethod:: ItemLookupSession.get_items_by_answer

   .. automethod:: ItemLookupSession.get_items_by_learning_objective

   .. automethod:: ItemLookupSession.get_items_by_learning_objectives

   .. autoattribute:: ItemLookupSession.items



Item Query Methods
------------------

   .. autoattribute:: ItemQuerySession.bank_id

   .. autoattribute:: ItemQuerySession.bank

   .. automethod:: ItemQuerySession.can_search_items

   .. automethod:: ItemQuerySession.use_federated_bank_view

   .. automethod:: ItemQuerySession.use_isolated_bank_view

   .. autoattribute:: ItemQuerySession.item_query

   .. automethod:: ItemQuerySession.get_items_by_query



Item Search Methods
-------------------

   .. autoattribute:: ItemSearchSession.item_search

   .. autoattribute:: ItemSearchSession.item_search_order

   .. automethod:: ItemSearchSession.get_items_by_search

   .. automethod:: ItemSearchSession.get_item_query_from_inspector



Item Admin Methods
------------------

   .. autoattribute:: ItemAdminSession.bank_id

   .. autoattribute:: ItemAdminSession.bank

   .. automethod:: ItemAdminSession.can_create_items

   .. automethod:: ItemAdminSession.can_create_item_with_record_types

   .. automethod:: ItemAdminSession.get_item_form_for_create

   .. automethod:: ItemAdminSession.create_item

   .. automethod:: ItemAdminSession.can_update_items

   .. automethod:: ItemAdminSession.get_item_form_for_update

   .. automethod:: ItemAdminSession.update_item

   .. automethod:: ItemAdminSession.can_delete_items

   .. automethod:: ItemAdminSession.delete_item

   .. automethod:: ItemAdminSession.can_manage_item_aliases

   .. automethod:: ItemAdminSession.alias_item

   .. automethod:: ItemAdminSession.can_create_questions

   .. automethod:: ItemAdminSession.can_create_question_with_record_types

   .. automethod:: ItemAdminSession.get_question_form_for_create

   .. automethod:: ItemAdminSession.create_question

   .. automethod:: ItemAdminSession.can_update_questions

   .. automethod:: ItemAdminSession.get_question_form_for_update

   .. automethod:: ItemAdminSession.update_question

   .. automethod:: ItemAdminSession.can_delete_questions

   .. automethod:: ItemAdminSession.delete_question

   .. automethod:: ItemAdminSession.can_create_answers

   .. automethod:: ItemAdminSession.can_create_answers_with_record_types

   .. automethod:: ItemAdminSession.get_answer_form_for_create

   .. automethod:: ItemAdminSession.create_answer

   .. automethod:: ItemAdminSession.can_update_answers

   .. automethod:: ItemAdminSession.get_answer_form_for_update

   .. automethod:: ItemAdminSession.update_answer

   .. automethod:: ItemAdminSession.can_delete_answers

   .. automethod:: ItemAdminSession.delete_answer



Item Notification Methods
-------------------------

   .. autoattribute:: ItemNotificationSession.bank_id

   .. autoattribute:: ItemNotificationSession.bank

   .. automethod:: ItemNotificationSession.can_register_for_item_notifications

   .. automethod:: ItemNotificationSession.use_federated_bank_view

   .. automethod:: ItemNotificationSession.use_isolated_bank_view

   .. automethod:: ItemNotificationSession.reliable_item_notifications

   .. automethod:: ItemNotificationSession.unreliable_item_notifications

   .. automethod:: ItemNotificationSession.acknowledge_item_notification

   .. automethod:: ItemNotificationSession.register_for_new_items

   .. automethod:: ItemNotificationSession.register_for_changed_items

   .. automethod:: ItemNotificationSession.register_for_changed_item

   .. automethod:: ItemNotificationSession.register_for_deleted_items

   .. automethod:: ItemNotificationSession.register_for_deleted_item



Assessment Lookup Methods
-------------------------

   .. autoattribute:: AssessmentLookupSession.bank_id

   .. autoattribute:: AssessmentLookupSession.bank

   .. automethod:: AssessmentLookupSession.can_lookup_assessments

   .. automethod:: AssessmentLookupSession.use_comparative_assessment_view

   .. automethod:: AssessmentLookupSession.use_plenary_assessment_view

   .. automethod:: AssessmentLookupSession.use_federated_bank_view

   .. automethod:: AssessmentLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentLookupSession.get_assessment

   .. automethod:: AssessmentLookupSession.get_assessments_by_ids

   .. automethod:: AssessmentLookupSession.get_assessments_by_genus_type

   .. automethod:: AssessmentLookupSession.get_assessments_by_parent_genus_type

   .. automethod:: AssessmentLookupSession.get_assessments_by_record_type

   .. autoattribute:: AssessmentLookupSession.assessments



Assessment Query Methods
------------------------

   .. autoattribute:: AssessmentQuerySession.bank_id

   .. autoattribute:: AssessmentQuerySession.bank

   .. automethod:: AssessmentQuerySession.can_search_assessments

   .. automethod:: AssessmentQuerySession.use_federated_bank_view

   .. automethod:: AssessmentQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentQuerySession.assessment_query

   .. automethod:: AssessmentQuerySession.get_assessments_by_query



Assessment Admin Methods
------------------------

   .. autoattribute:: AssessmentAdminSession.bank_id

   .. autoattribute:: AssessmentAdminSession.bank

   .. automethod:: AssessmentAdminSession.can_create_assessments

   .. automethod:: AssessmentAdminSession.can_create_assessment_with_record_types

   .. automethod:: AssessmentAdminSession.get_assessment_form_for_create

   .. automethod:: AssessmentAdminSession.create_assessment

   .. automethod:: AssessmentAdminSession.can_update_assessments

   .. automethod:: AssessmentAdminSession.get_assessment_form_for_update

   .. automethod:: AssessmentAdminSession.update_assessment

   .. automethod:: AssessmentAdminSession.can_delete_assessments

   .. automethod:: AssessmentAdminSession.delete_assessment

   .. automethod:: AssessmentAdminSession.can_manage_assessment_aliases

   .. automethod:: AssessmentAdminSession.alias_assessment



Assessment Basic Authoring Methods
----------------------------------

   .. autoattribute:: AssessmentBasicAuthoringSession.bank_id

   .. autoattribute:: AssessmentBasicAuthoringSession.bank

   .. automethod:: AssessmentBasicAuthoringSession.can_author_assessments

   .. automethod:: AssessmentBasicAuthoringSession.get_items

   .. automethod:: AssessmentBasicAuthoringSession.add_item

   .. automethod:: AssessmentBasicAuthoringSession.remove_item

   .. automethod:: AssessmentBasicAuthoringSession.move_item

   .. automethod:: AssessmentBasicAuthoringSession.order_items



Assessment Offered Lookup Methods
---------------------------------

   .. autoattribute:: AssessmentOfferedLookupSession.bank_id

   .. autoattribute:: AssessmentOfferedLookupSession.bank

   .. automethod:: AssessmentOfferedLookupSession.can_lookup_assessments_offered

   .. automethod:: AssessmentOfferedLookupSession.use_comparative_assessment_offered_view

   .. automethod:: AssessmentOfferedLookupSession.use_plenary_assessment_offered_view

   .. automethod:: AssessmentOfferedLookupSession.use_federated_bank_view

   .. automethod:: AssessmentOfferedLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentOfferedLookupSession.get_assessment_offered

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_ids

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_genus_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_parent_genus_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_record_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_date

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_for_assessment

   .. autoattribute:: AssessmentOfferedLookupSession.assessments_offered



Assessment Offered Query Methods
--------------------------------

   .. autoattribute:: AssessmentOfferedQuerySession.bank_id

   .. autoattribute:: AssessmentOfferedQuerySession.bank

   .. automethod:: AssessmentOfferedQuerySession.can_search_assessments_offered

   .. automethod:: AssessmentOfferedQuerySession.use_federated_bank_view

   .. automethod:: AssessmentOfferedQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentOfferedQuerySession.assessment_offered_query

   .. automethod:: AssessmentOfferedQuerySession.get_assessments_offered_by_query



Assessment Offered Admin Methods
--------------------------------

   .. autoattribute:: AssessmentOfferedAdminSession.bank_id

   .. autoattribute:: AssessmentOfferedAdminSession.bank

   .. automethod:: AssessmentOfferedAdminSession.can_create_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.can_create_assessment_offered_with_record_types

   .. automethod:: AssessmentOfferedAdminSession.get_assessment_offered_form_for_create

   .. automethod:: AssessmentOfferedAdminSession.create_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_update_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.get_assessment_offered_form_for_update

   .. automethod:: AssessmentOfferedAdminSession.update_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_delete_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.delete_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_manage_assessment_offered_aliases

   .. automethod:: AssessmentOfferedAdminSession.alias_assessment_offered



Assessment Taken Lookup Methods
-------------------------------

   .. autoattribute:: AssessmentTakenLookupSession.bank_id

   .. autoattribute:: AssessmentTakenLookupSession.bank

   .. automethod:: AssessmentTakenLookupSession.can_lookup_assessments_taken

   .. automethod:: AssessmentTakenLookupSession.use_comparative_assessment_taken_view

   .. automethod:: AssessmentTakenLookupSession.use_plenary_assessment_taken_view

   .. automethod:: AssessmentTakenLookupSession.use_federated_bank_view

   .. automethod:: AssessmentTakenLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentTakenLookupSession.get_assessment_taken

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_ids

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_genus_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_parent_genus_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_record_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker_and_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker_and_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker_and_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker_and_assessment_offered

   .. autoattribute:: AssessmentTakenLookupSession.assessments_taken



Assessment Taken Query Methods
------------------------------

   .. autoattribute:: AssessmentTakenQuerySession.bank_id

   .. autoattribute:: AssessmentTakenQuerySession.bank

   .. automethod:: AssessmentTakenQuerySession.can_search_assessments_taken

   .. automethod:: AssessmentTakenQuerySession.use_federated_bank_view

   .. automethod:: AssessmentTakenQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentTakenQuerySession.assessment_taken_query

   .. automethod:: AssessmentTakenQuerySession.get_assessments_taken_by_query



Assessment Taken Admin Methods
------------------------------

   .. autoattribute:: AssessmentTakenAdminSession.bank_id

   .. autoattribute:: AssessmentTakenAdminSession.bank

   .. automethod:: AssessmentTakenAdminSession.can_create_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.can_create_assessment_taken_with_record_types

   .. automethod:: AssessmentTakenAdminSession.get_assessment_taken_form_for_create

   .. automethod:: AssessmentTakenAdminSession.create_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_update_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.get_assessment_taken_form_for_update

   .. automethod:: AssessmentTakenAdminSession.update_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_delete_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.delete_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_manage_assessment_taken_aliases

   .. automethod:: AssessmentTakenAdminSession.alias_assessment_taken



Answer Query
------------

.. autoclass:: AnswerQuery
   :show-inheritance:

   .. automethod:: AnswerQuery.get_answer_query_record



Item Bank Methods
-----------------

   .. automethod:: ItemBankSession.can_lookup_item_bank_mappings

   .. automethod:: ItemBankSession.use_comparative_bank_view

   .. automethod:: ItemBankSession.use_plenary_bank_view

   .. automethod:: ItemBankSession.get_item_ids_by_bank

   .. automethod:: ItemBankSession.get_items_by_bank

   .. automethod:: ItemBankSession.get_item_ids_by_banks

   .. automethod:: ItemBankSession.get_items_by_banks

   .. automethod:: ItemBankSession.get_bank_ids_by_item

   .. automethod:: ItemBankSession.get_banks_by_item



Item Bank Assignment Methods
----------------------------

   .. automethod:: ItemBankAssignmentSession.can_assign_items

   .. automethod:: ItemBankAssignmentSession.can_assign_items_to_bank

   .. automethod:: ItemBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: ItemBankAssignmentSession.get_assignable_bank_ids_for_item

   .. automethod:: ItemBankAssignmentSession.assign_item_to_bank

   .. automethod:: ItemBankAssignmentSession.unassign_item_from_bank

   .. automethod:: ItemBankAssignmentSession.reassign_item_to_billing



Assessment Bank Methods
-----------------------

   .. automethod:: AssessmentBankSession.can_lookup_assessment_bank_mappings

   .. automethod:: AssessmentBankSession.use_comparative_bank_view

   .. automethod:: AssessmentBankSession.use_plenary_bank_view

   .. automethod:: AssessmentBankSession.get_assessment_ids_by_bank

   .. automethod:: AssessmentBankSession.get_assessments_by_bank

   .. automethod:: AssessmentBankSession.get_assessment_ids_by_banks

   .. automethod:: AssessmentBankSession.get_assessments_by_banks

   .. automethod:: AssessmentBankSession.get_bank_ids_by_assessment

   .. automethod:: AssessmentBankSession.get_banks_by_assessment



Assessment Bank Assignment Methods
----------------------------------

   .. automethod:: AssessmentBankAssignmentSession.can_assign_assessments

   .. automethod:: AssessmentBankAssignmentSession.can_assign_assessments_to_bank

   .. automethod:: AssessmentBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentBankAssignmentSession.get_assignable_bank_ids_for_assessment

   .. automethod:: AssessmentBankAssignmentSession.assign_assessment_to_bank

   .. automethod:: AssessmentBankAssignmentSession.unassign_assessment_from_bank

   .. automethod:: AssessmentBankAssignmentSession.reassign_assessment_to_billing



Assessment Offered Bank Methods
-------------------------------

   .. automethod:: AssessmentOfferedBankSession.can_lookup_assessment_offered_bank_mappings

   .. automethod:: AssessmentOfferedBankSession.use_comparative_bank_view

   .. automethod:: AssessmentOfferedBankSession.use_plenary_bank_view

   .. automethod:: AssessmentOfferedBankSession.get_assessment_offered_ids_by_bank

   .. automethod:: AssessmentOfferedBankSession.get_assessments_offered_by_bank

   .. automethod:: AssessmentOfferedBankSession.get_assessment_offered_ids_by_banks

   .. automethod:: AssessmentOfferedBankSession.get_assessments_offered_by_banks

   .. automethod:: AssessmentOfferedBankSession.get_bank_ids_by_assessment_offered

   .. automethod:: AssessmentOfferedBankSession.get_banks_by_assessment_offered



Assessment Offered Bank Assignment Methods
------------------------------------------

   .. automethod:: AssessmentOfferedBankAssignmentSession.can_assign_assessments_offered

   .. automethod:: AssessmentOfferedBankAssignmentSession.can_assign_assessments_offered_to_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentOfferedBankAssignmentSession.get_assignable_bank_ids_for_assessment_offered

   .. automethod:: AssessmentOfferedBankAssignmentSession.assign_assessment_offered_to_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.unassign_assessment_offered_from_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.reassign_assessment_offered_to_billing



Assessment Taken Bank Methods
-----------------------------

   .. automethod:: AssessmentTakenBankSession.can_lookup_assessment_taken_bank_mappings

   .. automethod:: AssessmentTakenBankSession.use_comparative_bank_view

   .. automethod:: AssessmentTakenBankSession.use_plenary_bank_view

   .. automethod:: AssessmentTakenBankSession.get_assessment_taken_ids_by_bank

   .. automethod:: AssessmentTakenBankSession.get_assessments_taken_by_bank

   .. automethod:: AssessmentTakenBankSession.get_assessment_taken_ids_by_banks

   .. automethod:: AssessmentTakenBankSession.get_assessments_taken_by_banks

   .. automethod:: AssessmentTakenBankSession.get_bank_ids_by_assessment_taken

   .. automethod:: AssessmentTakenBankSession.get_banks_by_assessment_taken



Assessment Taken Bank Assignment Methods
----------------------------------------

   .. automethod:: AssessmentTakenBankAssignmentSession.can_assign_assessments_taken

   .. automethod:: AssessmentTakenBankAssignmentSession.can_assign_assessments_taken_to_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentTakenBankAssignmentSession.get_assignable_bank_ids_for_assessment_taken

   .. automethod:: AssessmentTakenBankAssignmentSession.assign_assessment_taken_to_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.unassign_assessment_taken_from_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.reassign_assessment_taken_to_billing



Bank Lookup Methods
-------------------

   .. automethod:: BankLookupSession.can_lookup_banks

   .. automethod:: BankLookupSession.use_comparative_bank_view

   .. automethod:: BankLookupSession.use_plenary_bank_view

   .. automethod:: BankLookupSession.get_bank

   .. automethod:: BankLookupSession.get_banks_by_ids

   .. automethod:: BankLookupSession.get_banks_by_genus_type

   .. automethod:: BankLookupSession.get_banks_by_parent_genus_type

   .. automethod:: BankLookupSession.get_banks_by_record_type

   .. automethod:: BankLookupSession.get_banks_by_provider

   .. autoattribute:: BankLookupSession.banks



Bank Query Methods
------------------

   .. automethod:: BankQuerySession.can_search_banks

   .. autoattribute:: BankQuerySession.bank_query

   .. automethod:: BankQuerySession.get_banks_by_query



Bank Admin Methods
------------------

   .. automethod:: BankAdminSession.can_create_banks

   .. automethod:: BankAdminSession.can_create_bank_with_record_types

   .. automethod:: BankAdminSession.get_bank_form_for_create

   .. automethod:: BankAdminSession.create_bank

   .. automethod:: BankAdminSession.can_update_banks

   .. automethod:: BankAdminSession.get_bank_form_for_update

   .. automethod:: BankAdminSession.update_bank

   .. automethod:: BankAdminSession.can_delete_banks

   .. automethod:: BankAdminSession.delete_bank

   .. automethod:: BankAdminSession.can_manage_bank_aliases

   .. automethod:: BankAdminSession.alias_bank



Bank Hierarchy Methods
----------------------

   .. autoattribute:: BankHierarchySession.bank_hierarchy_id

   .. autoattribute:: BankHierarchySession.bank_hierarchy

   .. automethod:: BankHierarchySession.can_access_bank_hierarchy

   .. automethod:: BankHierarchySession.use_comparative_bank_view

   .. automethod:: BankHierarchySession.use_plenary_bank_view

   .. autoattribute:: BankHierarchySession.root_bank_ids

   .. autoattribute:: BankHierarchySession.root_banks

   .. automethod:: BankHierarchySession.has_parent_banks

   .. automethod:: BankHierarchySession.is_parent_of_bank

   .. automethod:: BankHierarchySession.get_parent_bank_ids

   .. automethod:: BankHierarchySession.get_parent_banks

   .. automethod:: BankHierarchySession.is_ancestor_of_bank

   .. automethod:: BankHierarchySession.has_child_banks

   .. automethod:: BankHierarchySession.is_child_of_bank

   .. automethod:: BankHierarchySession.get_child_bank_ids

   .. automethod:: BankHierarchySession.get_child_banks

   .. automethod:: BankHierarchySession.is_descendant_of_bank

   .. automethod:: BankHierarchySession.get_bank_node_ids

   .. automethod:: BankHierarchySession.get_bank_nodes



Bank Hierarchy Design Methods
-----------------------------

   .. autoattribute:: BankHierarchyDesignSession.bank_hierarchy_id

   .. autoattribute:: BankHierarchyDesignSession.bank_hierarchy

   .. automethod:: BankHierarchyDesignSession.can_modify_bank_hierarchy

   .. automethod:: BankHierarchyDesignSession.add_root_bank

   .. automethod:: BankHierarchyDesignSession.remove_root_bank

   .. automethod:: BankHierarchyDesignSession.add_child_bank

   .. automethod:: BankHierarchyDesignSession.remove_child_bank

   .. automethod:: BankHierarchyDesignSession.remove_child_banks



Assessment Methods
------------------

   .. autoattribute:: AssessmentSession.bank_id

   .. autoattribute:: AssessmentSession.bank

   .. automethod:: AssessmentSession.can_take_assessments

   .. automethod:: AssessmentSession.has_assessment_begun

   .. automethod:: AssessmentSession.is_assessment_over

   .. automethod:: AssessmentSession.requires_synchronous_sections

   .. automethod:: AssessmentSession.get_first_assessment_section

   .. automethod:: AssessmentSession.has_next_assessment_section

   .. automethod:: AssessmentSession.get_next_assessment_section

   .. automethod:: AssessmentSession.has_previous_assessment_section

   .. automethod:: AssessmentSession.get_previous_assessment_section

   .. automethod:: AssessmentSession.get_assessment_section

   .. automethod:: AssessmentSession.get_assessment_sections

   .. automethod:: AssessmentSession.is_assessment_section_complete

   .. automethod:: AssessmentSession.get_incomplete_assessment_sections

   .. automethod:: AssessmentSession.has_assessment_section_begun

   .. automethod:: AssessmentSession.is_assessment_section_over

   .. automethod:: AssessmentSession.requires_synchronous_responses

   .. automethod:: AssessmentSession.get_first_question

   .. automethod:: AssessmentSession.has_next_question

   .. automethod:: AssessmentSession.get_next_question

   .. automethod:: AssessmentSession.has_previous_question

   .. automethod:: AssessmentSession.get_previous_question

   .. automethod:: AssessmentSession.get_question

   .. automethod:: AssessmentSession.get_questions

   .. automethod:: AssessmentSession.get_response_form

   .. automethod:: AssessmentSession.submit_response

   .. automethod:: AssessmentSession.skip_item

   .. automethod:: AssessmentSession.is_question_answered

   .. automethod:: AssessmentSession.get_unanswered_questions

   .. automethod:: AssessmentSession.has_unanswered_questions

   .. automethod:: AssessmentSession.get_first_unanswered_question

   .. automethod:: AssessmentSession.has_next_unanswered_question

   .. automethod:: AssessmentSession.get_next_unanswered_question

   .. automethod:: AssessmentSession.has_previous_unanswered_question

   .. automethod:: AssessmentSession.get_previous_unanswered_question

   .. automethod:: AssessmentSession.get_response

   .. automethod:: AssessmentSession.get_responses

   .. automethod:: AssessmentSession.clear_response

   .. automethod:: AssessmentSession.finish_assessment_section

   .. automethod:: AssessmentSession.is_answer_available

   .. automethod:: AssessmentSession.get_answers

   .. automethod:: AssessmentSession.finish_assessment



Item Lookup Methods
-------------------

   .. autoattribute:: ItemLookupSession.bank_id

   .. autoattribute:: ItemLookupSession.bank

   .. automethod:: ItemLookupSession.can_lookup_items

   .. automethod:: ItemLookupSession.use_comparative_item_view

   .. automethod:: ItemLookupSession.use_plenary_item_view

   .. automethod:: ItemLookupSession.use_federated_bank_view

   .. automethod:: ItemLookupSession.use_isolated_bank_view

   .. automethod:: ItemLookupSession.get_item

   .. automethod:: ItemLookupSession.get_items_by_ids

   .. automethod:: ItemLookupSession.get_items_by_genus_type

   .. automethod:: ItemLookupSession.get_items_by_parent_genus_type

   .. automethod:: ItemLookupSession.get_items_by_record_type

   .. automethod:: ItemLookupSession.get_items_by_question

   .. automethod:: ItemLookupSession.get_items_by_answer

   .. automethod:: ItemLookupSession.get_items_by_learning_objective

   .. automethod:: ItemLookupSession.get_items_by_learning_objectives

   .. autoattribute:: ItemLookupSession.items



Item Query Methods
------------------

   .. autoattribute:: ItemQuerySession.bank_id

   .. autoattribute:: ItemQuerySession.bank

   .. automethod:: ItemQuerySession.can_search_items

   .. automethod:: ItemQuerySession.use_federated_bank_view

   .. automethod:: ItemQuerySession.use_isolated_bank_view

   .. autoattribute:: ItemQuerySession.item_query

   .. automethod:: ItemQuerySession.get_items_by_query



Item Search Methods
-------------------

   .. autoattribute:: ItemSearchSession.item_search

   .. autoattribute:: ItemSearchSession.item_search_order

   .. automethod:: ItemSearchSession.get_items_by_search

   .. automethod:: ItemSearchSession.get_item_query_from_inspector



Item Admin Methods
------------------

   .. autoattribute:: ItemAdminSession.bank_id

   .. autoattribute:: ItemAdminSession.bank

   .. automethod:: ItemAdminSession.can_create_items

   .. automethod:: ItemAdminSession.can_create_item_with_record_types

   .. automethod:: ItemAdminSession.get_item_form_for_create

   .. automethod:: ItemAdminSession.create_item

   .. automethod:: ItemAdminSession.can_update_items

   .. automethod:: ItemAdminSession.get_item_form_for_update

   .. automethod:: ItemAdminSession.update_item

   .. automethod:: ItemAdminSession.can_delete_items

   .. automethod:: ItemAdminSession.delete_item

   .. automethod:: ItemAdminSession.can_manage_item_aliases

   .. automethod:: ItemAdminSession.alias_item

   .. automethod:: ItemAdminSession.can_create_questions

   .. automethod:: ItemAdminSession.can_create_question_with_record_types

   .. automethod:: ItemAdminSession.get_question_form_for_create

   .. automethod:: ItemAdminSession.create_question

   .. automethod:: ItemAdminSession.can_update_questions

   .. automethod:: ItemAdminSession.get_question_form_for_update

   .. automethod:: ItemAdminSession.update_question

   .. automethod:: ItemAdminSession.can_delete_questions

   .. automethod:: ItemAdminSession.delete_question

   .. automethod:: ItemAdminSession.can_create_answers

   .. automethod:: ItemAdminSession.can_create_answers_with_record_types

   .. automethod:: ItemAdminSession.get_answer_form_for_create

   .. automethod:: ItemAdminSession.create_answer

   .. automethod:: ItemAdminSession.can_update_answers

   .. automethod:: ItemAdminSession.get_answer_form_for_update

   .. automethod:: ItemAdminSession.update_answer

   .. automethod:: ItemAdminSession.can_delete_answers

   .. automethod:: ItemAdminSession.delete_answer



Item Notification Methods
-------------------------

   .. autoattribute:: ItemNotificationSession.bank_id

   .. autoattribute:: ItemNotificationSession.bank

   .. automethod:: ItemNotificationSession.can_register_for_item_notifications

   .. automethod:: ItemNotificationSession.use_federated_bank_view

   .. automethod:: ItemNotificationSession.use_isolated_bank_view

   .. automethod:: ItemNotificationSession.reliable_item_notifications

   .. automethod:: ItemNotificationSession.unreliable_item_notifications

   .. automethod:: ItemNotificationSession.acknowledge_item_notification

   .. automethod:: ItemNotificationSession.register_for_new_items

   .. automethod:: ItemNotificationSession.register_for_changed_items

   .. automethod:: ItemNotificationSession.register_for_changed_item

   .. automethod:: ItemNotificationSession.register_for_deleted_items

   .. automethod:: ItemNotificationSession.register_for_deleted_item



Assessment Lookup Methods
-------------------------

   .. autoattribute:: AssessmentLookupSession.bank_id

   .. autoattribute:: AssessmentLookupSession.bank

   .. automethod:: AssessmentLookupSession.can_lookup_assessments

   .. automethod:: AssessmentLookupSession.use_comparative_assessment_view

   .. automethod:: AssessmentLookupSession.use_plenary_assessment_view

   .. automethod:: AssessmentLookupSession.use_federated_bank_view

   .. automethod:: AssessmentLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentLookupSession.get_assessment

   .. automethod:: AssessmentLookupSession.get_assessments_by_ids

   .. automethod:: AssessmentLookupSession.get_assessments_by_genus_type

   .. automethod:: AssessmentLookupSession.get_assessments_by_parent_genus_type

   .. automethod:: AssessmentLookupSession.get_assessments_by_record_type

   .. autoattribute:: AssessmentLookupSession.assessments



Assessment Query Methods
------------------------

   .. autoattribute:: AssessmentQuerySession.bank_id

   .. autoattribute:: AssessmentQuerySession.bank

   .. automethod:: AssessmentQuerySession.can_search_assessments

   .. automethod:: AssessmentQuerySession.use_federated_bank_view

   .. automethod:: AssessmentQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentQuerySession.assessment_query

   .. automethod:: AssessmentQuerySession.get_assessments_by_query



Assessment Admin Methods
------------------------

   .. autoattribute:: AssessmentAdminSession.bank_id

   .. autoattribute:: AssessmentAdminSession.bank

   .. automethod:: AssessmentAdminSession.can_create_assessments

   .. automethod:: AssessmentAdminSession.can_create_assessment_with_record_types

   .. automethod:: AssessmentAdminSession.get_assessment_form_for_create

   .. automethod:: AssessmentAdminSession.create_assessment

   .. automethod:: AssessmentAdminSession.can_update_assessments

   .. automethod:: AssessmentAdminSession.get_assessment_form_for_update

   .. automethod:: AssessmentAdminSession.update_assessment

   .. automethod:: AssessmentAdminSession.can_delete_assessments

   .. automethod:: AssessmentAdminSession.delete_assessment

   .. automethod:: AssessmentAdminSession.can_manage_assessment_aliases

   .. automethod:: AssessmentAdminSession.alias_assessment



Assessment Basic Authoring Methods
----------------------------------

   .. autoattribute:: AssessmentBasicAuthoringSession.bank_id

   .. autoattribute:: AssessmentBasicAuthoringSession.bank

   .. automethod:: AssessmentBasicAuthoringSession.can_author_assessments

   .. automethod:: AssessmentBasicAuthoringSession.get_items

   .. automethod:: AssessmentBasicAuthoringSession.add_item

   .. automethod:: AssessmentBasicAuthoringSession.remove_item

   .. automethod:: AssessmentBasicAuthoringSession.move_item

   .. automethod:: AssessmentBasicAuthoringSession.order_items



Assessment Offered Lookup Methods
---------------------------------

   .. autoattribute:: AssessmentOfferedLookupSession.bank_id

   .. autoattribute:: AssessmentOfferedLookupSession.bank

   .. automethod:: AssessmentOfferedLookupSession.can_lookup_assessments_offered

   .. automethod:: AssessmentOfferedLookupSession.use_comparative_assessment_offered_view

   .. automethod:: AssessmentOfferedLookupSession.use_plenary_assessment_offered_view

   .. automethod:: AssessmentOfferedLookupSession.use_federated_bank_view

   .. automethod:: AssessmentOfferedLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentOfferedLookupSession.get_assessment_offered

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_ids

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_genus_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_parent_genus_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_record_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_date

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_for_assessment

   .. autoattribute:: AssessmentOfferedLookupSession.assessments_offered



Assessment Offered Query Methods
--------------------------------

   .. autoattribute:: AssessmentOfferedQuerySession.bank_id

   .. autoattribute:: AssessmentOfferedQuerySession.bank

   .. automethod:: AssessmentOfferedQuerySession.can_search_assessments_offered

   .. automethod:: AssessmentOfferedQuerySession.use_federated_bank_view

   .. automethod:: AssessmentOfferedQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentOfferedQuerySession.assessment_offered_query

   .. automethod:: AssessmentOfferedQuerySession.get_assessments_offered_by_query



Assessment Offered Admin Methods
--------------------------------

   .. autoattribute:: AssessmentOfferedAdminSession.bank_id

   .. autoattribute:: AssessmentOfferedAdminSession.bank

   .. automethod:: AssessmentOfferedAdminSession.can_create_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.can_create_assessment_offered_with_record_types

   .. automethod:: AssessmentOfferedAdminSession.get_assessment_offered_form_for_create

   .. automethod:: AssessmentOfferedAdminSession.create_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_update_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.get_assessment_offered_form_for_update

   .. automethod:: AssessmentOfferedAdminSession.update_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_delete_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.delete_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_manage_assessment_offered_aliases

   .. automethod:: AssessmentOfferedAdminSession.alias_assessment_offered



Assessment Taken Lookup Methods
-------------------------------

   .. autoattribute:: AssessmentTakenLookupSession.bank_id

   .. autoattribute:: AssessmentTakenLookupSession.bank

   .. automethod:: AssessmentTakenLookupSession.can_lookup_assessments_taken

   .. automethod:: AssessmentTakenLookupSession.use_comparative_assessment_taken_view

   .. automethod:: AssessmentTakenLookupSession.use_plenary_assessment_taken_view

   .. automethod:: AssessmentTakenLookupSession.use_federated_bank_view

   .. automethod:: AssessmentTakenLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentTakenLookupSession.get_assessment_taken

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_ids

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_genus_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_parent_genus_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_record_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker_and_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker_and_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker_and_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker_and_assessment_offered

   .. autoattribute:: AssessmentTakenLookupSession.assessments_taken



Assessment Taken Query Methods
------------------------------

   .. autoattribute:: AssessmentTakenQuerySession.bank_id

   .. autoattribute:: AssessmentTakenQuerySession.bank

   .. automethod:: AssessmentTakenQuerySession.can_search_assessments_taken

   .. automethod:: AssessmentTakenQuerySession.use_federated_bank_view

   .. automethod:: AssessmentTakenQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentTakenQuerySession.assessment_taken_query

   .. automethod:: AssessmentTakenQuerySession.get_assessments_taken_by_query



Assessment Taken Admin Methods
------------------------------

   .. autoattribute:: AssessmentTakenAdminSession.bank_id

   .. autoattribute:: AssessmentTakenAdminSession.bank

   .. automethod:: AssessmentTakenAdminSession.can_create_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.can_create_assessment_taken_with_record_types

   .. automethod:: AssessmentTakenAdminSession.get_assessment_taken_form_for_create

   .. automethod:: AssessmentTakenAdminSession.create_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_update_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.get_assessment_taken_form_for_update

   .. automethod:: AssessmentTakenAdminSession.update_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_delete_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.delete_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_manage_assessment_taken_aliases

   .. automethod:: AssessmentTakenAdminSession.alias_assessment_taken



Item Query
----------

.. autoclass:: ItemQuery
   :show-inheritance:

   .. automethod:: ItemQuery.match_learning_objective_id

   .. autoattribute:: ItemQuery.learning_objective_id_terms

   .. automethod:: ItemQuery.supports_learning_objective_query

   .. autoattribute:: ItemQuery.learning_objective_query

   .. automethod:: ItemQuery.match_any_learning_objective

   .. autoattribute:: ItemQuery.learning_objective_terms

   .. automethod:: ItemQuery.match_question_id

   .. autoattribute:: ItemQuery.question_id_terms

   .. automethod:: ItemQuery.supports_question_query

   .. autoattribute:: ItemQuery.question_query

   .. automethod:: ItemQuery.match_any_question

   .. autoattribute:: ItemQuery.question_terms

   .. automethod:: ItemQuery.match_answer_id

   .. autoattribute:: ItemQuery.answer_id_terms

   .. automethod:: ItemQuery.supports_answer_query

   .. autoattribute:: ItemQuery.answer_query

   .. automethod:: ItemQuery.match_any_answer

   .. autoattribute:: ItemQuery.answer_terms

   .. automethod:: ItemQuery.match_assessment_id

   .. autoattribute:: ItemQuery.assessment_id_terms

   .. automethod:: ItemQuery.supports_assessment_query

   .. autoattribute:: ItemQuery.assessment_query

   .. automethod:: ItemQuery.match_any_assessment

   .. autoattribute:: ItemQuery.assessment_terms

   .. automethod:: ItemQuery.match_bank_id

   .. autoattribute:: ItemQuery.bank_id_terms

   .. automethod:: ItemQuery.supports_bank_query

   .. autoattribute:: ItemQuery.bank_query

   .. autoattribute:: ItemQuery.bank_terms

   .. automethod:: ItemQuery.get_item_query_record



Item Bank Methods
-----------------

   .. automethod:: ItemBankSession.can_lookup_item_bank_mappings

   .. automethod:: ItemBankSession.use_comparative_bank_view

   .. automethod:: ItemBankSession.use_plenary_bank_view

   .. automethod:: ItemBankSession.get_item_ids_by_bank

   .. automethod:: ItemBankSession.get_items_by_bank

   .. automethod:: ItemBankSession.get_item_ids_by_banks

   .. automethod:: ItemBankSession.get_items_by_banks

   .. automethod:: ItemBankSession.get_bank_ids_by_item

   .. automethod:: ItemBankSession.get_banks_by_item



Item Bank Assignment Methods
----------------------------

   .. automethod:: ItemBankAssignmentSession.can_assign_items

   .. automethod:: ItemBankAssignmentSession.can_assign_items_to_bank

   .. automethod:: ItemBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: ItemBankAssignmentSession.get_assignable_bank_ids_for_item

   .. automethod:: ItemBankAssignmentSession.assign_item_to_bank

   .. automethod:: ItemBankAssignmentSession.unassign_item_from_bank

   .. automethod:: ItemBankAssignmentSession.reassign_item_to_billing



Assessment Bank Methods
-----------------------

   .. automethod:: AssessmentBankSession.can_lookup_assessment_bank_mappings

   .. automethod:: AssessmentBankSession.use_comparative_bank_view

   .. automethod:: AssessmentBankSession.use_plenary_bank_view

   .. automethod:: AssessmentBankSession.get_assessment_ids_by_bank

   .. automethod:: AssessmentBankSession.get_assessments_by_bank

   .. automethod:: AssessmentBankSession.get_assessment_ids_by_banks

   .. automethod:: AssessmentBankSession.get_assessments_by_banks

   .. automethod:: AssessmentBankSession.get_bank_ids_by_assessment

   .. automethod:: AssessmentBankSession.get_banks_by_assessment



Assessment Bank Assignment Methods
----------------------------------

   .. automethod:: AssessmentBankAssignmentSession.can_assign_assessments

   .. automethod:: AssessmentBankAssignmentSession.can_assign_assessments_to_bank

   .. automethod:: AssessmentBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentBankAssignmentSession.get_assignable_bank_ids_for_assessment

   .. automethod:: AssessmentBankAssignmentSession.assign_assessment_to_bank

   .. automethod:: AssessmentBankAssignmentSession.unassign_assessment_from_bank

   .. automethod:: AssessmentBankAssignmentSession.reassign_assessment_to_billing



Assessment Offered Bank Methods
-------------------------------

   .. automethod:: AssessmentOfferedBankSession.can_lookup_assessment_offered_bank_mappings

   .. automethod:: AssessmentOfferedBankSession.use_comparative_bank_view

   .. automethod:: AssessmentOfferedBankSession.use_plenary_bank_view

   .. automethod:: AssessmentOfferedBankSession.get_assessment_offered_ids_by_bank

   .. automethod:: AssessmentOfferedBankSession.get_assessments_offered_by_bank

   .. automethod:: AssessmentOfferedBankSession.get_assessment_offered_ids_by_banks

   .. automethod:: AssessmentOfferedBankSession.get_assessments_offered_by_banks

   .. automethod:: AssessmentOfferedBankSession.get_bank_ids_by_assessment_offered

   .. automethod:: AssessmentOfferedBankSession.get_banks_by_assessment_offered



Assessment Offered Bank Assignment Methods
------------------------------------------

   .. automethod:: AssessmentOfferedBankAssignmentSession.can_assign_assessments_offered

   .. automethod:: AssessmentOfferedBankAssignmentSession.can_assign_assessments_offered_to_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentOfferedBankAssignmentSession.get_assignable_bank_ids_for_assessment_offered

   .. automethod:: AssessmentOfferedBankAssignmentSession.assign_assessment_offered_to_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.unassign_assessment_offered_from_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.reassign_assessment_offered_to_billing



Assessment Taken Bank Methods
-----------------------------

   .. automethod:: AssessmentTakenBankSession.can_lookup_assessment_taken_bank_mappings

   .. automethod:: AssessmentTakenBankSession.use_comparative_bank_view

   .. automethod:: AssessmentTakenBankSession.use_plenary_bank_view

   .. automethod:: AssessmentTakenBankSession.get_assessment_taken_ids_by_bank

   .. automethod:: AssessmentTakenBankSession.get_assessments_taken_by_bank

   .. automethod:: AssessmentTakenBankSession.get_assessment_taken_ids_by_banks

   .. automethod:: AssessmentTakenBankSession.get_assessments_taken_by_banks

   .. automethod:: AssessmentTakenBankSession.get_bank_ids_by_assessment_taken

   .. automethod:: AssessmentTakenBankSession.get_banks_by_assessment_taken



Assessment Taken Bank Assignment Methods
----------------------------------------

   .. automethod:: AssessmentTakenBankAssignmentSession.can_assign_assessments_taken

   .. automethod:: AssessmentTakenBankAssignmentSession.can_assign_assessments_taken_to_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentTakenBankAssignmentSession.get_assignable_bank_ids_for_assessment_taken

   .. automethod:: AssessmentTakenBankAssignmentSession.assign_assessment_taken_to_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.unassign_assessment_taken_from_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.reassign_assessment_taken_to_billing



Bank Lookup Methods
-------------------

   .. automethod:: BankLookupSession.can_lookup_banks

   .. automethod:: BankLookupSession.use_comparative_bank_view

   .. automethod:: BankLookupSession.use_plenary_bank_view

   .. automethod:: BankLookupSession.get_bank

   .. automethod:: BankLookupSession.get_banks_by_ids

   .. automethod:: BankLookupSession.get_banks_by_genus_type

   .. automethod:: BankLookupSession.get_banks_by_parent_genus_type

   .. automethod:: BankLookupSession.get_banks_by_record_type

   .. automethod:: BankLookupSession.get_banks_by_provider

   .. autoattribute:: BankLookupSession.banks



Bank Query Methods
------------------

   .. automethod:: BankQuerySession.can_search_banks

   .. autoattribute:: BankQuerySession.bank_query

   .. automethod:: BankQuerySession.get_banks_by_query



Bank Admin Methods
------------------

   .. automethod:: BankAdminSession.can_create_banks

   .. automethod:: BankAdminSession.can_create_bank_with_record_types

   .. automethod:: BankAdminSession.get_bank_form_for_create

   .. automethod:: BankAdminSession.create_bank

   .. automethod:: BankAdminSession.can_update_banks

   .. automethod:: BankAdminSession.get_bank_form_for_update

   .. automethod:: BankAdminSession.update_bank

   .. automethod:: BankAdminSession.can_delete_banks

   .. automethod:: BankAdminSession.delete_bank

   .. automethod:: BankAdminSession.can_manage_bank_aliases

   .. automethod:: BankAdminSession.alias_bank



Bank Hierarchy Methods
----------------------

   .. autoattribute:: BankHierarchySession.bank_hierarchy_id

   .. autoattribute:: BankHierarchySession.bank_hierarchy

   .. automethod:: BankHierarchySession.can_access_bank_hierarchy

   .. automethod:: BankHierarchySession.use_comparative_bank_view

   .. automethod:: BankHierarchySession.use_plenary_bank_view

   .. autoattribute:: BankHierarchySession.root_bank_ids

   .. autoattribute:: BankHierarchySession.root_banks

   .. automethod:: BankHierarchySession.has_parent_banks

   .. automethod:: BankHierarchySession.is_parent_of_bank

   .. automethod:: BankHierarchySession.get_parent_bank_ids

   .. automethod:: BankHierarchySession.get_parent_banks

   .. automethod:: BankHierarchySession.is_ancestor_of_bank

   .. automethod:: BankHierarchySession.has_child_banks

   .. automethod:: BankHierarchySession.is_child_of_bank

   .. automethod:: BankHierarchySession.get_child_bank_ids

   .. automethod:: BankHierarchySession.get_child_banks

   .. automethod:: BankHierarchySession.is_descendant_of_bank

   .. automethod:: BankHierarchySession.get_bank_node_ids

   .. automethod:: BankHierarchySession.get_bank_nodes



Bank Hierarchy Design Methods
-----------------------------

   .. autoattribute:: BankHierarchyDesignSession.bank_hierarchy_id

   .. autoattribute:: BankHierarchyDesignSession.bank_hierarchy

   .. automethod:: BankHierarchyDesignSession.can_modify_bank_hierarchy

   .. automethod:: BankHierarchyDesignSession.add_root_bank

   .. automethod:: BankHierarchyDesignSession.remove_root_bank

   .. automethod:: BankHierarchyDesignSession.add_child_bank

   .. automethod:: BankHierarchyDesignSession.remove_child_bank

   .. automethod:: BankHierarchyDesignSession.remove_child_banks



Assessment Methods
------------------

   .. autoattribute:: AssessmentSession.bank_id

   .. autoattribute:: AssessmentSession.bank

   .. automethod:: AssessmentSession.can_take_assessments

   .. automethod:: AssessmentSession.has_assessment_begun

   .. automethod:: AssessmentSession.is_assessment_over

   .. automethod:: AssessmentSession.requires_synchronous_sections

   .. automethod:: AssessmentSession.get_first_assessment_section

   .. automethod:: AssessmentSession.has_next_assessment_section

   .. automethod:: AssessmentSession.get_next_assessment_section

   .. automethod:: AssessmentSession.has_previous_assessment_section

   .. automethod:: AssessmentSession.get_previous_assessment_section

   .. automethod:: AssessmentSession.get_assessment_section

   .. automethod:: AssessmentSession.get_assessment_sections

   .. automethod:: AssessmentSession.is_assessment_section_complete

   .. automethod:: AssessmentSession.get_incomplete_assessment_sections

   .. automethod:: AssessmentSession.has_assessment_section_begun

   .. automethod:: AssessmentSession.is_assessment_section_over

   .. automethod:: AssessmentSession.requires_synchronous_responses

   .. automethod:: AssessmentSession.get_first_question

   .. automethod:: AssessmentSession.has_next_question

   .. automethod:: AssessmentSession.get_next_question

   .. automethod:: AssessmentSession.has_previous_question

   .. automethod:: AssessmentSession.get_previous_question

   .. automethod:: AssessmentSession.get_question

   .. automethod:: AssessmentSession.get_questions

   .. automethod:: AssessmentSession.get_response_form

   .. automethod:: AssessmentSession.submit_response

   .. automethod:: AssessmentSession.skip_item

   .. automethod:: AssessmentSession.is_question_answered

   .. automethod:: AssessmentSession.get_unanswered_questions

   .. automethod:: AssessmentSession.has_unanswered_questions

   .. automethod:: AssessmentSession.get_first_unanswered_question

   .. automethod:: AssessmentSession.has_next_unanswered_question

   .. automethod:: AssessmentSession.get_next_unanswered_question

   .. automethod:: AssessmentSession.has_previous_unanswered_question

   .. automethod:: AssessmentSession.get_previous_unanswered_question

   .. automethod:: AssessmentSession.get_response

   .. automethod:: AssessmentSession.get_responses

   .. automethod:: AssessmentSession.clear_response

   .. automethod:: AssessmentSession.finish_assessment_section

   .. automethod:: AssessmentSession.is_answer_available

   .. automethod:: AssessmentSession.get_answers

   .. automethod:: AssessmentSession.finish_assessment



Item Lookup Methods
-------------------

   .. autoattribute:: ItemLookupSession.bank_id

   .. autoattribute:: ItemLookupSession.bank

   .. automethod:: ItemLookupSession.can_lookup_items

   .. automethod:: ItemLookupSession.use_comparative_item_view

   .. automethod:: ItemLookupSession.use_plenary_item_view

   .. automethod:: ItemLookupSession.use_federated_bank_view

   .. automethod:: ItemLookupSession.use_isolated_bank_view

   .. automethod:: ItemLookupSession.get_item

   .. automethod:: ItemLookupSession.get_items_by_ids

   .. automethod:: ItemLookupSession.get_items_by_genus_type

   .. automethod:: ItemLookupSession.get_items_by_parent_genus_type

   .. automethod:: ItemLookupSession.get_items_by_record_type

   .. automethod:: ItemLookupSession.get_items_by_question

   .. automethod:: ItemLookupSession.get_items_by_answer

   .. automethod:: ItemLookupSession.get_items_by_learning_objective

   .. automethod:: ItemLookupSession.get_items_by_learning_objectives

   .. autoattribute:: ItemLookupSession.items



Item Query Methods
------------------

   .. autoattribute:: ItemQuerySession.bank_id

   .. autoattribute:: ItemQuerySession.bank

   .. automethod:: ItemQuerySession.can_search_items

   .. automethod:: ItemQuerySession.use_federated_bank_view

   .. automethod:: ItemQuerySession.use_isolated_bank_view

   .. autoattribute:: ItemQuerySession.item_query

   .. automethod:: ItemQuerySession.get_items_by_query



Item Search Methods
-------------------

   .. autoattribute:: ItemSearchSession.item_search

   .. autoattribute:: ItemSearchSession.item_search_order

   .. automethod:: ItemSearchSession.get_items_by_search

   .. automethod:: ItemSearchSession.get_item_query_from_inspector



Item Admin Methods
------------------

   .. autoattribute:: ItemAdminSession.bank_id

   .. autoattribute:: ItemAdminSession.bank

   .. automethod:: ItemAdminSession.can_create_items

   .. automethod:: ItemAdminSession.can_create_item_with_record_types

   .. automethod:: ItemAdminSession.get_item_form_for_create

   .. automethod:: ItemAdminSession.create_item

   .. automethod:: ItemAdminSession.can_update_items

   .. automethod:: ItemAdminSession.get_item_form_for_update

   .. automethod:: ItemAdminSession.update_item

   .. automethod:: ItemAdminSession.can_delete_items

   .. automethod:: ItemAdminSession.delete_item

   .. automethod:: ItemAdminSession.can_manage_item_aliases

   .. automethod:: ItemAdminSession.alias_item

   .. automethod:: ItemAdminSession.can_create_questions

   .. automethod:: ItemAdminSession.can_create_question_with_record_types

   .. automethod:: ItemAdminSession.get_question_form_for_create

   .. automethod:: ItemAdminSession.create_question

   .. automethod:: ItemAdminSession.can_update_questions

   .. automethod:: ItemAdminSession.get_question_form_for_update

   .. automethod:: ItemAdminSession.update_question

   .. automethod:: ItemAdminSession.can_delete_questions

   .. automethod:: ItemAdminSession.delete_question

   .. automethod:: ItemAdminSession.can_create_answers

   .. automethod:: ItemAdminSession.can_create_answers_with_record_types

   .. automethod:: ItemAdminSession.get_answer_form_for_create

   .. automethod:: ItemAdminSession.create_answer

   .. automethod:: ItemAdminSession.can_update_answers

   .. automethod:: ItemAdminSession.get_answer_form_for_update

   .. automethod:: ItemAdminSession.update_answer

   .. automethod:: ItemAdminSession.can_delete_answers

   .. automethod:: ItemAdminSession.delete_answer



Item Notification Methods
-------------------------

   .. autoattribute:: ItemNotificationSession.bank_id

   .. autoattribute:: ItemNotificationSession.bank

   .. automethod:: ItemNotificationSession.can_register_for_item_notifications

   .. automethod:: ItemNotificationSession.use_federated_bank_view

   .. automethod:: ItemNotificationSession.use_isolated_bank_view

   .. automethod:: ItemNotificationSession.reliable_item_notifications

   .. automethod:: ItemNotificationSession.unreliable_item_notifications

   .. automethod:: ItemNotificationSession.acknowledge_item_notification

   .. automethod:: ItemNotificationSession.register_for_new_items

   .. automethod:: ItemNotificationSession.register_for_changed_items

   .. automethod:: ItemNotificationSession.register_for_changed_item

   .. automethod:: ItemNotificationSession.register_for_deleted_items

   .. automethod:: ItemNotificationSession.register_for_deleted_item



Assessment Lookup Methods
-------------------------

   .. autoattribute:: AssessmentLookupSession.bank_id

   .. autoattribute:: AssessmentLookupSession.bank

   .. automethod:: AssessmentLookupSession.can_lookup_assessments

   .. automethod:: AssessmentLookupSession.use_comparative_assessment_view

   .. automethod:: AssessmentLookupSession.use_plenary_assessment_view

   .. automethod:: AssessmentLookupSession.use_federated_bank_view

   .. automethod:: AssessmentLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentLookupSession.get_assessment

   .. automethod:: AssessmentLookupSession.get_assessments_by_ids

   .. automethod:: AssessmentLookupSession.get_assessments_by_genus_type

   .. automethod:: AssessmentLookupSession.get_assessments_by_parent_genus_type

   .. automethod:: AssessmentLookupSession.get_assessments_by_record_type

   .. autoattribute:: AssessmentLookupSession.assessments



Assessment Query Methods
------------------------

   .. autoattribute:: AssessmentQuerySession.bank_id

   .. autoattribute:: AssessmentQuerySession.bank

   .. automethod:: AssessmentQuerySession.can_search_assessments

   .. automethod:: AssessmentQuerySession.use_federated_bank_view

   .. automethod:: AssessmentQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentQuerySession.assessment_query

   .. automethod:: AssessmentQuerySession.get_assessments_by_query



Assessment Admin Methods
------------------------

   .. autoattribute:: AssessmentAdminSession.bank_id

   .. autoattribute:: AssessmentAdminSession.bank

   .. automethod:: AssessmentAdminSession.can_create_assessments

   .. automethod:: AssessmentAdminSession.can_create_assessment_with_record_types

   .. automethod:: AssessmentAdminSession.get_assessment_form_for_create

   .. automethod:: AssessmentAdminSession.create_assessment

   .. automethod:: AssessmentAdminSession.can_update_assessments

   .. automethod:: AssessmentAdminSession.get_assessment_form_for_update

   .. automethod:: AssessmentAdminSession.update_assessment

   .. automethod:: AssessmentAdminSession.can_delete_assessments

   .. automethod:: AssessmentAdminSession.delete_assessment

   .. automethod:: AssessmentAdminSession.can_manage_assessment_aliases

   .. automethod:: AssessmentAdminSession.alias_assessment



Assessment Basic Authoring Methods
----------------------------------

   .. autoattribute:: AssessmentBasicAuthoringSession.bank_id

   .. autoattribute:: AssessmentBasicAuthoringSession.bank

   .. automethod:: AssessmentBasicAuthoringSession.can_author_assessments

   .. automethod:: AssessmentBasicAuthoringSession.get_items

   .. automethod:: AssessmentBasicAuthoringSession.add_item

   .. automethod:: AssessmentBasicAuthoringSession.remove_item

   .. automethod:: AssessmentBasicAuthoringSession.move_item

   .. automethod:: AssessmentBasicAuthoringSession.order_items



Assessment Offered Lookup Methods
---------------------------------

   .. autoattribute:: AssessmentOfferedLookupSession.bank_id

   .. autoattribute:: AssessmentOfferedLookupSession.bank

   .. automethod:: AssessmentOfferedLookupSession.can_lookup_assessments_offered

   .. automethod:: AssessmentOfferedLookupSession.use_comparative_assessment_offered_view

   .. automethod:: AssessmentOfferedLookupSession.use_plenary_assessment_offered_view

   .. automethod:: AssessmentOfferedLookupSession.use_federated_bank_view

   .. automethod:: AssessmentOfferedLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentOfferedLookupSession.get_assessment_offered

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_ids

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_genus_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_parent_genus_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_record_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_date

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_for_assessment

   .. autoattribute:: AssessmentOfferedLookupSession.assessments_offered



Assessment Offered Query Methods
--------------------------------

   .. autoattribute:: AssessmentOfferedQuerySession.bank_id

   .. autoattribute:: AssessmentOfferedQuerySession.bank

   .. automethod:: AssessmentOfferedQuerySession.can_search_assessments_offered

   .. automethod:: AssessmentOfferedQuerySession.use_federated_bank_view

   .. automethod:: AssessmentOfferedQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentOfferedQuerySession.assessment_offered_query

   .. automethod:: AssessmentOfferedQuerySession.get_assessments_offered_by_query



Assessment Offered Admin Methods
--------------------------------

   .. autoattribute:: AssessmentOfferedAdminSession.bank_id

   .. autoattribute:: AssessmentOfferedAdminSession.bank

   .. automethod:: AssessmentOfferedAdminSession.can_create_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.can_create_assessment_offered_with_record_types

   .. automethod:: AssessmentOfferedAdminSession.get_assessment_offered_form_for_create

   .. automethod:: AssessmentOfferedAdminSession.create_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_update_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.get_assessment_offered_form_for_update

   .. automethod:: AssessmentOfferedAdminSession.update_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_delete_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.delete_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_manage_assessment_offered_aliases

   .. automethod:: AssessmentOfferedAdminSession.alias_assessment_offered



Assessment Taken Lookup Methods
-------------------------------

   .. autoattribute:: AssessmentTakenLookupSession.bank_id

   .. autoattribute:: AssessmentTakenLookupSession.bank

   .. automethod:: AssessmentTakenLookupSession.can_lookup_assessments_taken

   .. automethod:: AssessmentTakenLookupSession.use_comparative_assessment_taken_view

   .. automethod:: AssessmentTakenLookupSession.use_plenary_assessment_taken_view

   .. automethod:: AssessmentTakenLookupSession.use_federated_bank_view

   .. automethod:: AssessmentTakenLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentTakenLookupSession.get_assessment_taken

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_ids

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_genus_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_parent_genus_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_record_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker_and_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker_and_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker_and_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker_and_assessment_offered

   .. autoattribute:: AssessmentTakenLookupSession.assessments_taken



Assessment Taken Query Methods
------------------------------

   .. autoattribute:: AssessmentTakenQuerySession.bank_id

   .. autoattribute:: AssessmentTakenQuerySession.bank

   .. automethod:: AssessmentTakenQuerySession.can_search_assessments_taken

   .. automethod:: AssessmentTakenQuerySession.use_federated_bank_view

   .. automethod:: AssessmentTakenQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentTakenQuerySession.assessment_taken_query

   .. automethod:: AssessmentTakenQuerySession.get_assessments_taken_by_query



Assessment Taken Admin Methods
------------------------------

   .. autoattribute:: AssessmentTakenAdminSession.bank_id

   .. autoattribute:: AssessmentTakenAdminSession.bank

   .. automethod:: AssessmentTakenAdminSession.can_create_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.can_create_assessment_taken_with_record_types

   .. automethod:: AssessmentTakenAdminSession.get_assessment_taken_form_for_create

   .. automethod:: AssessmentTakenAdminSession.create_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_update_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.get_assessment_taken_form_for_update

   .. automethod:: AssessmentTakenAdminSession.update_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_delete_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.delete_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_manage_assessment_taken_aliases

   .. automethod:: AssessmentTakenAdminSession.alias_assessment_taken



Assessment Query
----------------

.. autoclass:: AssessmentQuery
   :show-inheritance:

   .. automethod:: AssessmentQuery.match_level_id

   .. autoattribute:: AssessmentQuery.level_id_terms

   .. automethod:: AssessmentQuery.supports_level_query

   .. autoattribute:: AssessmentQuery.level_query

   .. automethod:: AssessmentQuery.match_any_level

   .. autoattribute:: AssessmentQuery.level_terms

   .. automethod:: AssessmentQuery.match_rubric_id

   .. autoattribute:: AssessmentQuery.rubric_id_terms

   .. automethod:: AssessmentQuery.supports_rubric_query

   .. autoattribute:: AssessmentQuery.rubric_query

   .. automethod:: AssessmentQuery.match_any_rubric

   .. autoattribute:: AssessmentQuery.rubric_terms

   .. automethod:: AssessmentQuery.match_item_id

   .. autoattribute:: AssessmentQuery.item_id_terms

   .. automethod:: AssessmentQuery.supports_item_query

   .. autoattribute:: AssessmentQuery.item_query

   .. automethod:: AssessmentQuery.match_any_item

   .. autoattribute:: AssessmentQuery.item_terms

   .. automethod:: AssessmentQuery.match_assessment_offered_id

   .. autoattribute:: AssessmentQuery.assessment_offered_id_terms

   .. automethod:: AssessmentQuery.supports_assessment_offered_query

   .. autoattribute:: AssessmentQuery.assessment_offered_query

   .. automethod:: AssessmentQuery.match_any_assessment_offered

   .. autoattribute:: AssessmentQuery.assessment_offered_terms

   .. automethod:: AssessmentQuery.match_assessment_taken_id

   .. autoattribute:: AssessmentQuery.assessment_taken_id_terms

   .. automethod:: AssessmentQuery.supports_assessment_taken_query

   .. autoattribute:: AssessmentQuery.assessment_taken_query

   .. automethod:: AssessmentQuery.match_any_assessment_taken

   .. autoattribute:: AssessmentQuery.assessment_taken_terms

   .. automethod:: AssessmentQuery.match_bank_id

   .. autoattribute:: AssessmentQuery.bank_id_terms

   .. automethod:: AssessmentQuery.supports_bank_query

   .. autoattribute:: AssessmentQuery.bank_query

   .. autoattribute:: AssessmentQuery.bank_terms

   .. automethod:: AssessmentQuery.get_assessment_query_record



Item Bank Methods
-----------------

   .. automethod:: ItemBankSession.can_lookup_item_bank_mappings

   .. automethod:: ItemBankSession.use_comparative_bank_view

   .. automethod:: ItemBankSession.use_plenary_bank_view

   .. automethod:: ItemBankSession.get_item_ids_by_bank

   .. automethod:: ItemBankSession.get_items_by_bank

   .. automethod:: ItemBankSession.get_item_ids_by_banks

   .. automethod:: ItemBankSession.get_items_by_banks

   .. automethod:: ItemBankSession.get_bank_ids_by_item

   .. automethod:: ItemBankSession.get_banks_by_item



Item Bank Assignment Methods
----------------------------

   .. automethod:: ItemBankAssignmentSession.can_assign_items

   .. automethod:: ItemBankAssignmentSession.can_assign_items_to_bank

   .. automethod:: ItemBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: ItemBankAssignmentSession.get_assignable_bank_ids_for_item

   .. automethod:: ItemBankAssignmentSession.assign_item_to_bank

   .. automethod:: ItemBankAssignmentSession.unassign_item_from_bank

   .. automethod:: ItemBankAssignmentSession.reassign_item_to_billing



Assessment Bank Methods
-----------------------

   .. automethod:: AssessmentBankSession.can_lookup_assessment_bank_mappings

   .. automethod:: AssessmentBankSession.use_comparative_bank_view

   .. automethod:: AssessmentBankSession.use_plenary_bank_view

   .. automethod:: AssessmentBankSession.get_assessment_ids_by_bank

   .. automethod:: AssessmentBankSession.get_assessments_by_bank

   .. automethod:: AssessmentBankSession.get_assessment_ids_by_banks

   .. automethod:: AssessmentBankSession.get_assessments_by_banks

   .. automethod:: AssessmentBankSession.get_bank_ids_by_assessment

   .. automethod:: AssessmentBankSession.get_banks_by_assessment



Assessment Bank Assignment Methods
----------------------------------

   .. automethod:: AssessmentBankAssignmentSession.can_assign_assessments

   .. automethod:: AssessmentBankAssignmentSession.can_assign_assessments_to_bank

   .. automethod:: AssessmentBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentBankAssignmentSession.get_assignable_bank_ids_for_assessment

   .. automethod:: AssessmentBankAssignmentSession.assign_assessment_to_bank

   .. automethod:: AssessmentBankAssignmentSession.unassign_assessment_from_bank

   .. automethod:: AssessmentBankAssignmentSession.reassign_assessment_to_billing



Assessment Offered Bank Methods
-------------------------------

   .. automethod:: AssessmentOfferedBankSession.can_lookup_assessment_offered_bank_mappings

   .. automethod:: AssessmentOfferedBankSession.use_comparative_bank_view

   .. automethod:: AssessmentOfferedBankSession.use_plenary_bank_view

   .. automethod:: AssessmentOfferedBankSession.get_assessment_offered_ids_by_bank

   .. automethod:: AssessmentOfferedBankSession.get_assessments_offered_by_bank

   .. automethod:: AssessmentOfferedBankSession.get_assessment_offered_ids_by_banks

   .. automethod:: AssessmentOfferedBankSession.get_assessments_offered_by_banks

   .. automethod:: AssessmentOfferedBankSession.get_bank_ids_by_assessment_offered

   .. automethod:: AssessmentOfferedBankSession.get_banks_by_assessment_offered



Assessment Offered Bank Assignment Methods
------------------------------------------

   .. automethod:: AssessmentOfferedBankAssignmentSession.can_assign_assessments_offered

   .. automethod:: AssessmentOfferedBankAssignmentSession.can_assign_assessments_offered_to_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentOfferedBankAssignmentSession.get_assignable_bank_ids_for_assessment_offered

   .. automethod:: AssessmentOfferedBankAssignmentSession.assign_assessment_offered_to_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.unassign_assessment_offered_from_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.reassign_assessment_offered_to_billing



Assessment Taken Bank Methods
-----------------------------

   .. automethod:: AssessmentTakenBankSession.can_lookup_assessment_taken_bank_mappings

   .. automethod:: AssessmentTakenBankSession.use_comparative_bank_view

   .. automethod:: AssessmentTakenBankSession.use_plenary_bank_view

   .. automethod:: AssessmentTakenBankSession.get_assessment_taken_ids_by_bank

   .. automethod:: AssessmentTakenBankSession.get_assessments_taken_by_bank

   .. automethod:: AssessmentTakenBankSession.get_assessment_taken_ids_by_banks

   .. automethod:: AssessmentTakenBankSession.get_assessments_taken_by_banks

   .. automethod:: AssessmentTakenBankSession.get_bank_ids_by_assessment_taken

   .. automethod:: AssessmentTakenBankSession.get_banks_by_assessment_taken



Assessment Taken Bank Assignment Methods
----------------------------------------

   .. automethod:: AssessmentTakenBankAssignmentSession.can_assign_assessments_taken

   .. automethod:: AssessmentTakenBankAssignmentSession.can_assign_assessments_taken_to_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentTakenBankAssignmentSession.get_assignable_bank_ids_for_assessment_taken

   .. automethod:: AssessmentTakenBankAssignmentSession.assign_assessment_taken_to_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.unassign_assessment_taken_from_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.reassign_assessment_taken_to_billing



Bank Lookup Methods
-------------------

   .. automethod:: BankLookupSession.can_lookup_banks

   .. automethod:: BankLookupSession.use_comparative_bank_view

   .. automethod:: BankLookupSession.use_plenary_bank_view

   .. automethod:: BankLookupSession.get_bank

   .. automethod:: BankLookupSession.get_banks_by_ids

   .. automethod:: BankLookupSession.get_banks_by_genus_type

   .. automethod:: BankLookupSession.get_banks_by_parent_genus_type

   .. automethod:: BankLookupSession.get_banks_by_record_type

   .. automethod:: BankLookupSession.get_banks_by_provider

   .. autoattribute:: BankLookupSession.banks



Bank Query Methods
------------------

   .. automethod:: BankQuerySession.can_search_banks

   .. autoattribute:: BankQuerySession.bank_query

   .. automethod:: BankQuerySession.get_banks_by_query



Bank Admin Methods
------------------

   .. automethod:: BankAdminSession.can_create_banks

   .. automethod:: BankAdminSession.can_create_bank_with_record_types

   .. automethod:: BankAdminSession.get_bank_form_for_create

   .. automethod:: BankAdminSession.create_bank

   .. automethod:: BankAdminSession.can_update_banks

   .. automethod:: BankAdminSession.get_bank_form_for_update

   .. automethod:: BankAdminSession.update_bank

   .. automethod:: BankAdminSession.can_delete_banks

   .. automethod:: BankAdminSession.delete_bank

   .. automethod:: BankAdminSession.can_manage_bank_aliases

   .. automethod:: BankAdminSession.alias_bank



Bank Hierarchy Methods
----------------------

   .. autoattribute:: BankHierarchySession.bank_hierarchy_id

   .. autoattribute:: BankHierarchySession.bank_hierarchy

   .. automethod:: BankHierarchySession.can_access_bank_hierarchy

   .. automethod:: BankHierarchySession.use_comparative_bank_view

   .. automethod:: BankHierarchySession.use_plenary_bank_view

   .. autoattribute:: BankHierarchySession.root_bank_ids

   .. autoattribute:: BankHierarchySession.root_banks

   .. automethod:: BankHierarchySession.has_parent_banks

   .. automethod:: BankHierarchySession.is_parent_of_bank

   .. automethod:: BankHierarchySession.get_parent_bank_ids

   .. automethod:: BankHierarchySession.get_parent_banks

   .. automethod:: BankHierarchySession.is_ancestor_of_bank

   .. automethod:: BankHierarchySession.has_child_banks

   .. automethod:: BankHierarchySession.is_child_of_bank

   .. automethod:: BankHierarchySession.get_child_bank_ids

   .. automethod:: BankHierarchySession.get_child_banks

   .. automethod:: BankHierarchySession.is_descendant_of_bank

   .. automethod:: BankHierarchySession.get_bank_node_ids

   .. automethod:: BankHierarchySession.get_bank_nodes



Bank Hierarchy Design Methods
-----------------------------

   .. autoattribute:: BankHierarchyDesignSession.bank_hierarchy_id

   .. autoattribute:: BankHierarchyDesignSession.bank_hierarchy

   .. automethod:: BankHierarchyDesignSession.can_modify_bank_hierarchy

   .. automethod:: BankHierarchyDesignSession.add_root_bank

   .. automethod:: BankHierarchyDesignSession.remove_root_bank

   .. automethod:: BankHierarchyDesignSession.add_child_bank

   .. automethod:: BankHierarchyDesignSession.remove_child_bank

   .. automethod:: BankHierarchyDesignSession.remove_child_banks



Assessment Methods
------------------

   .. autoattribute:: AssessmentSession.bank_id

   .. autoattribute:: AssessmentSession.bank

   .. automethod:: AssessmentSession.can_take_assessments

   .. automethod:: AssessmentSession.has_assessment_begun

   .. automethod:: AssessmentSession.is_assessment_over

   .. automethod:: AssessmentSession.requires_synchronous_sections

   .. automethod:: AssessmentSession.get_first_assessment_section

   .. automethod:: AssessmentSession.has_next_assessment_section

   .. automethod:: AssessmentSession.get_next_assessment_section

   .. automethod:: AssessmentSession.has_previous_assessment_section

   .. automethod:: AssessmentSession.get_previous_assessment_section

   .. automethod:: AssessmentSession.get_assessment_section

   .. automethod:: AssessmentSession.get_assessment_sections

   .. automethod:: AssessmentSession.is_assessment_section_complete

   .. automethod:: AssessmentSession.get_incomplete_assessment_sections

   .. automethod:: AssessmentSession.has_assessment_section_begun

   .. automethod:: AssessmentSession.is_assessment_section_over

   .. automethod:: AssessmentSession.requires_synchronous_responses

   .. automethod:: AssessmentSession.get_first_question

   .. automethod:: AssessmentSession.has_next_question

   .. automethod:: AssessmentSession.get_next_question

   .. automethod:: AssessmentSession.has_previous_question

   .. automethod:: AssessmentSession.get_previous_question

   .. automethod:: AssessmentSession.get_question

   .. automethod:: AssessmentSession.get_questions

   .. automethod:: AssessmentSession.get_response_form

   .. automethod:: AssessmentSession.submit_response

   .. automethod:: AssessmentSession.skip_item

   .. automethod:: AssessmentSession.is_question_answered

   .. automethod:: AssessmentSession.get_unanswered_questions

   .. automethod:: AssessmentSession.has_unanswered_questions

   .. automethod:: AssessmentSession.get_first_unanswered_question

   .. automethod:: AssessmentSession.has_next_unanswered_question

   .. automethod:: AssessmentSession.get_next_unanswered_question

   .. automethod:: AssessmentSession.has_previous_unanswered_question

   .. automethod:: AssessmentSession.get_previous_unanswered_question

   .. automethod:: AssessmentSession.get_response

   .. automethod:: AssessmentSession.get_responses

   .. automethod:: AssessmentSession.clear_response

   .. automethod:: AssessmentSession.finish_assessment_section

   .. automethod:: AssessmentSession.is_answer_available

   .. automethod:: AssessmentSession.get_answers

   .. automethod:: AssessmentSession.finish_assessment



Item Lookup Methods
-------------------

   .. autoattribute:: ItemLookupSession.bank_id

   .. autoattribute:: ItemLookupSession.bank

   .. automethod:: ItemLookupSession.can_lookup_items

   .. automethod:: ItemLookupSession.use_comparative_item_view

   .. automethod:: ItemLookupSession.use_plenary_item_view

   .. automethod:: ItemLookupSession.use_federated_bank_view

   .. automethod:: ItemLookupSession.use_isolated_bank_view

   .. automethod:: ItemLookupSession.get_item

   .. automethod:: ItemLookupSession.get_items_by_ids

   .. automethod:: ItemLookupSession.get_items_by_genus_type

   .. automethod:: ItemLookupSession.get_items_by_parent_genus_type

   .. automethod:: ItemLookupSession.get_items_by_record_type

   .. automethod:: ItemLookupSession.get_items_by_question

   .. automethod:: ItemLookupSession.get_items_by_answer

   .. automethod:: ItemLookupSession.get_items_by_learning_objective

   .. automethod:: ItemLookupSession.get_items_by_learning_objectives

   .. autoattribute:: ItemLookupSession.items



Item Query Methods
------------------

   .. autoattribute:: ItemQuerySession.bank_id

   .. autoattribute:: ItemQuerySession.bank

   .. automethod:: ItemQuerySession.can_search_items

   .. automethod:: ItemQuerySession.use_federated_bank_view

   .. automethod:: ItemQuerySession.use_isolated_bank_view

   .. autoattribute:: ItemQuerySession.item_query

   .. automethod:: ItemQuerySession.get_items_by_query



Item Search Methods
-------------------

   .. autoattribute:: ItemSearchSession.item_search

   .. autoattribute:: ItemSearchSession.item_search_order

   .. automethod:: ItemSearchSession.get_items_by_search

   .. automethod:: ItemSearchSession.get_item_query_from_inspector



Item Admin Methods
------------------

   .. autoattribute:: ItemAdminSession.bank_id

   .. autoattribute:: ItemAdminSession.bank

   .. automethod:: ItemAdminSession.can_create_items

   .. automethod:: ItemAdminSession.can_create_item_with_record_types

   .. automethod:: ItemAdminSession.get_item_form_for_create

   .. automethod:: ItemAdminSession.create_item

   .. automethod:: ItemAdminSession.can_update_items

   .. automethod:: ItemAdminSession.get_item_form_for_update

   .. automethod:: ItemAdminSession.update_item

   .. automethod:: ItemAdminSession.can_delete_items

   .. automethod:: ItemAdminSession.delete_item

   .. automethod:: ItemAdminSession.can_manage_item_aliases

   .. automethod:: ItemAdminSession.alias_item

   .. automethod:: ItemAdminSession.can_create_questions

   .. automethod:: ItemAdminSession.can_create_question_with_record_types

   .. automethod:: ItemAdminSession.get_question_form_for_create

   .. automethod:: ItemAdminSession.create_question

   .. automethod:: ItemAdminSession.can_update_questions

   .. automethod:: ItemAdminSession.get_question_form_for_update

   .. automethod:: ItemAdminSession.update_question

   .. automethod:: ItemAdminSession.can_delete_questions

   .. automethod:: ItemAdminSession.delete_question

   .. automethod:: ItemAdminSession.can_create_answers

   .. automethod:: ItemAdminSession.can_create_answers_with_record_types

   .. automethod:: ItemAdminSession.get_answer_form_for_create

   .. automethod:: ItemAdminSession.create_answer

   .. automethod:: ItemAdminSession.can_update_answers

   .. automethod:: ItemAdminSession.get_answer_form_for_update

   .. automethod:: ItemAdminSession.update_answer

   .. automethod:: ItemAdminSession.can_delete_answers

   .. automethod:: ItemAdminSession.delete_answer



Item Notification Methods
-------------------------

   .. autoattribute:: ItemNotificationSession.bank_id

   .. autoattribute:: ItemNotificationSession.bank

   .. automethod:: ItemNotificationSession.can_register_for_item_notifications

   .. automethod:: ItemNotificationSession.use_federated_bank_view

   .. automethod:: ItemNotificationSession.use_isolated_bank_view

   .. automethod:: ItemNotificationSession.reliable_item_notifications

   .. automethod:: ItemNotificationSession.unreliable_item_notifications

   .. automethod:: ItemNotificationSession.acknowledge_item_notification

   .. automethod:: ItemNotificationSession.register_for_new_items

   .. automethod:: ItemNotificationSession.register_for_changed_items

   .. automethod:: ItemNotificationSession.register_for_changed_item

   .. automethod:: ItemNotificationSession.register_for_deleted_items

   .. automethod:: ItemNotificationSession.register_for_deleted_item



Assessment Lookup Methods
-------------------------

   .. autoattribute:: AssessmentLookupSession.bank_id

   .. autoattribute:: AssessmentLookupSession.bank

   .. automethod:: AssessmentLookupSession.can_lookup_assessments

   .. automethod:: AssessmentLookupSession.use_comparative_assessment_view

   .. automethod:: AssessmentLookupSession.use_plenary_assessment_view

   .. automethod:: AssessmentLookupSession.use_federated_bank_view

   .. automethod:: AssessmentLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentLookupSession.get_assessment

   .. automethod:: AssessmentLookupSession.get_assessments_by_ids

   .. automethod:: AssessmentLookupSession.get_assessments_by_genus_type

   .. automethod:: AssessmentLookupSession.get_assessments_by_parent_genus_type

   .. automethod:: AssessmentLookupSession.get_assessments_by_record_type

   .. autoattribute:: AssessmentLookupSession.assessments



Assessment Query Methods
------------------------

   .. autoattribute:: AssessmentQuerySession.bank_id

   .. autoattribute:: AssessmentQuerySession.bank

   .. automethod:: AssessmentQuerySession.can_search_assessments

   .. automethod:: AssessmentQuerySession.use_federated_bank_view

   .. automethod:: AssessmentQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentQuerySession.assessment_query

   .. automethod:: AssessmentQuerySession.get_assessments_by_query



Assessment Admin Methods
------------------------

   .. autoattribute:: AssessmentAdminSession.bank_id

   .. autoattribute:: AssessmentAdminSession.bank

   .. automethod:: AssessmentAdminSession.can_create_assessments

   .. automethod:: AssessmentAdminSession.can_create_assessment_with_record_types

   .. automethod:: AssessmentAdminSession.get_assessment_form_for_create

   .. automethod:: AssessmentAdminSession.create_assessment

   .. automethod:: AssessmentAdminSession.can_update_assessments

   .. automethod:: AssessmentAdminSession.get_assessment_form_for_update

   .. automethod:: AssessmentAdminSession.update_assessment

   .. automethod:: AssessmentAdminSession.can_delete_assessments

   .. automethod:: AssessmentAdminSession.delete_assessment

   .. automethod:: AssessmentAdminSession.can_manage_assessment_aliases

   .. automethod:: AssessmentAdminSession.alias_assessment



Assessment Basic Authoring Methods
----------------------------------

   .. autoattribute:: AssessmentBasicAuthoringSession.bank_id

   .. autoattribute:: AssessmentBasicAuthoringSession.bank

   .. automethod:: AssessmentBasicAuthoringSession.can_author_assessments

   .. automethod:: AssessmentBasicAuthoringSession.get_items

   .. automethod:: AssessmentBasicAuthoringSession.add_item

   .. automethod:: AssessmentBasicAuthoringSession.remove_item

   .. automethod:: AssessmentBasicAuthoringSession.move_item

   .. automethod:: AssessmentBasicAuthoringSession.order_items



Assessment Offered Lookup Methods
---------------------------------

   .. autoattribute:: AssessmentOfferedLookupSession.bank_id

   .. autoattribute:: AssessmentOfferedLookupSession.bank

   .. automethod:: AssessmentOfferedLookupSession.can_lookup_assessments_offered

   .. automethod:: AssessmentOfferedLookupSession.use_comparative_assessment_offered_view

   .. automethod:: AssessmentOfferedLookupSession.use_plenary_assessment_offered_view

   .. automethod:: AssessmentOfferedLookupSession.use_federated_bank_view

   .. automethod:: AssessmentOfferedLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentOfferedLookupSession.get_assessment_offered

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_ids

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_genus_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_parent_genus_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_record_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_date

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_for_assessment

   .. autoattribute:: AssessmentOfferedLookupSession.assessments_offered



Assessment Offered Query Methods
--------------------------------

   .. autoattribute:: AssessmentOfferedQuerySession.bank_id

   .. autoattribute:: AssessmentOfferedQuerySession.bank

   .. automethod:: AssessmentOfferedQuerySession.can_search_assessments_offered

   .. automethod:: AssessmentOfferedQuerySession.use_federated_bank_view

   .. automethod:: AssessmentOfferedQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentOfferedQuerySession.assessment_offered_query

   .. automethod:: AssessmentOfferedQuerySession.get_assessments_offered_by_query



Assessment Offered Admin Methods
--------------------------------

   .. autoattribute:: AssessmentOfferedAdminSession.bank_id

   .. autoattribute:: AssessmentOfferedAdminSession.bank

   .. automethod:: AssessmentOfferedAdminSession.can_create_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.can_create_assessment_offered_with_record_types

   .. automethod:: AssessmentOfferedAdminSession.get_assessment_offered_form_for_create

   .. automethod:: AssessmentOfferedAdminSession.create_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_update_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.get_assessment_offered_form_for_update

   .. automethod:: AssessmentOfferedAdminSession.update_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_delete_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.delete_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_manage_assessment_offered_aliases

   .. automethod:: AssessmentOfferedAdminSession.alias_assessment_offered



Assessment Taken Lookup Methods
-------------------------------

   .. autoattribute:: AssessmentTakenLookupSession.bank_id

   .. autoattribute:: AssessmentTakenLookupSession.bank

   .. automethod:: AssessmentTakenLookupSession.can_lookup_assessments_taken

   .. automethod:: AssessmentTakenLookupSession.use_comparative_assessment_taken_view

   .. automethod:: AssessmentTakenLookupSession.use_plenary_assessment_taken_view

   .. automethod:: AssessmentTakenLookupSession.use_federated_bank_view

   .. automethod:: AssessmentTakenLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentTakenLookupSession.get_assessment_taken

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_ids

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_genus_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_parent_genus_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_record_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker_and_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker_and_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker_and_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker_and_assessment_offered

   .. autoattribute:: AssessmentTakenLookupSession.assessments_taken



Assessment Taken Query Methods
------------------------------

   .. autoattribute:: AssessmentTakenQuerySession.bank_id

   .. autoattribute:: AssessmentTakenQuerySession.bank

   .. automethod:: AssessmentTakenQuerySession.can_search_assessments_taken

   .. automethod:: AssessmentTakenQuerySession.use_federated_bank_view

   .. automethod:: AssessmentTakenQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentTakenQuerySession.assessment_taken_query

   .. automethod:: AssessmentTakenQuerySession.get_assessments_taken_by_query



Assessment Taken Admin Methods
------------------------------

   .. autoattribute:: AssessmentTakenAdminSession.bank_id

   .. autoattribute:: AssessmentTakenAdminSession.bank

   .. automethod:: AssessmentTakenAdminSession.can_create_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.can_create_assessment_taken_with_record_types

   .. automethod:: AssessmentTakenAdminSession.get_assessment_taken_form_for_create

   .. automethod:: AssessmentTakenAdminSession.create_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_update_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.get_assessment_taken_form_for_update

   .. automethod:: AssessmentTakenAdminSession.update_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_delete_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.delete_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_manage_assessment_taken_aliases

   .. automethod:: AssessmentTakenAdminSession.alias_assessment_taken



Assessment Offered Query
------------------------

.. autoclass:: AssessmentOfferedQuery
   :show-inheritance:

   .. automethod:: AssessmentOfferedQuery.match_assessment_id

   .. autoattribute:: AssessmentOfferedQuery.assessment_id_terms

   .. automethod:: AssessmentOfferedQuery.supports_assessment_query

   .. autoattribute:: AssessmentOfferedQuery.assessment_query

   .. autoattribute:: AssessmentOfferedQuery.assessment_terms

   .. automethod:: AssessmentOfferedQuery.match_level_id

   .. autoattribute:: AssessmentOfferedQuery.level_id_terms

   .. automethod:: AssessmentOfferedQuery.supports_level_query

   .. autoattribute:: AssessmentOfferedQuery.level_query

   .. automethod:: AssessmentOfferedQuery.match_any_level

   .. autoattribute:: AssessmentOfferedQuery.level_terms

   .. automethod:: AssessmentOfferedQuery.match_items_sequential

   .. autoattribute:: AssessmentOfferedQuery.items_sequential_terms

   .. automethod:: AssessmentOfferedQuery.match_items_shuffled

   .. autoattribute:: AssessmentOfferedQuery.items_shuffled_terms

   .. automethod:: AssessmentOfferedQuery.match_start_time

   .. automethod:: AssessmentOfferedQuery.match_any_start_time

   .. autoattribute:: AssessmentOfferedQuery.start_time_terms

   .. automethod:: AssessmentOfferedQuery.match_deadline

   .. automethod:: AssessmentOfferedQuery.match_any_deadline

   .. autoattribute:: AssessmentOfferedQuery.deadline_terms

   .. automethod:: AssessmentOfferedQuery.match_duration

   .. automethod:: AssessmentOfferedQuery.match_any_duration

   .. autoattribute:: AssessmentOfferedQuery.duration_terms

   .. automethod:: AssessmentOfferedQuery.match_score_system_id

   .. autoattribute:: AssessmentOfferedQuery.score_system_id_terms

   .. automethod:: AssessmentOfferedQuery.supports_score_system_query

   .. autoattribute:: AssessmentOfferedQuery.score_system_query

   .. automethod:: AssessmentOfferedQuery.match_any_score_system

   .. autoattribute:: AssessmentOfferedQuery.score_system_terms

   .. automethod:: AssessmentOfferedQuery.match_grade_system_id

   .. autoattribute:: AssessmentOfferedQuery.grade_system_id_terms

   .. automethod:: AssessmentOfferedQuery.supports_grade_system_query

   .. autoattribute:: AssessmentOfferedQuery.grade_system_query

   .. automethod:: AssessmentOfferedQuery.match_any_grade_system

   .. autoattribute:: AssessmentOfferedQuery.grade_system_terms

   .. automethod:: AssessmentOfferedQuery.match_rubric_id

   .. autoattribute:: AssessmentOfferedQuery.rubric_id_terms

   .. automethod:: AssessmentOfferedQuery.supports_rubric_query

   .. autoattribute:: AssessmentOfferedQuery.rubric_query

   .. automethod:: AssessmentOfferedQuery.match_any_rubric

   .. autoattribute:: AssessmentOfferedQuery.rubric_terms

   .. automethod:: AssessmentOfferedQuery.match_assessment_taken_id

   .. autoattribute:: AssessmentOfferedQuery.assessment_taken_id_terms

   .. automethod:: AssessmentOfferedQuery.supports_assessment_taken_query

   .. autoattribute:: AssessmentOfferedQuery.assessment_taken_query

   .. automethod:: AssessmentOfferedQuery.match_any_assessment_taken

   .. autoattribute:: AssessmentOfferedQuery.assessment_taken_terms

   .. automethod:: AssessmentOfferedQuery.match_bank_id

   .. autoattribute:: AssessmentOfferedQuery.bank_id_terms

   .. automethod:: AssessmentOfferedQuery.supports_bank_query

   .. autoattribute:: AssessmentOfferedQuery.bank_query

   .. autoattribute:: AssessmentOfferedQuery.bank_terms

   .. automethod:: AssessmentOfferedQuery.get_assessment_offered_query_record



Item Bank Methods
-----------------

   .. automethod:: ItemBankSession.can_lookup_item_bank_mappings

   .. automethod:: ItemBankSession.use_comparative_bank_view

   .. automethod:: ItemBankSession.use_plenary_bank_view

   .. automethod:: ItemBankSession.get_item_ids_by_bank

   .. automethod:: ItemBankSession.get_items_by_bank

   .. automethod:: ItemBankSession.get_item_ids_by_banks

   .. automethod:: ItemBankSession.get_items_by_banks

   .. automethod:: ItemBankSession.get_bank_ids_by_item

   .. automethod:: ItemBankSession.get_banks_by_item



Item Bank Assignment Methods
----------------------------

   .. automethod:: ItemBankAssignmentSession.can_assign_items

   .. automethod:: ItemBankAssignmentSession.can_assign_items_to_bank

   .. automethod:: ItemBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: ItemBankAssignmentSession.get_assignable_bank_ids_for_item

   .. automethod:: ItemBankAssignmentSession.assign_item_to_bank

   .. automethod:: ItemBankAssignmentSession.unassign_item_from_bank

   .. automethod:: ItemBankAssignmentSession.reassign_item_to_billing



Assessment Bank Methods
-----------------------

   .. automethod:: AssessmentBankSession.can_lookup_assessment_bank_mappings

   .. automethod:: AssessmentBankSession.use_comparative_bank_view

   .. automethod:: AssessmentBankSession.use_plenary_bank_view

   .. automethod:: AssessmentBankSession.get_assessment_ids_by_bank

   .. automethod:: AssessmentBankSession.get_assessments_by_bank

   .. automethod:: AssessmentBankSession.get_assessment_ids_by_banks

   .. automethod:: AssessmentBankSession.get_assessments_by_banks

   .. automethod:: AssessmentBankSession.get_bank_ids_by_assessment

   .. automethod:: AssessmentBankSession.get_banks_by_assessment



Assessment Bank Assignment Methods
----------------------------------

   .. automethod:: AssessmentBankAssignmentSession.can_assign_assessments

   .. automethod:: AssessmentBankAssignmentSession.can_assign_assessments_to_bank

   .. automethod:: AssessmentBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentBankAssignmentSession.get_assignable_bank_ids_for_assessment

   .. automethod:: AssessmentBankAssignmentSession.assign_assessment_to_bank

   .. automethod:: AssessmentBankAssignmentSession.unassign_assessment_from_bank

   .. automethod:: AssessmentBankAssignmentSession.reassign_assessment_to_billing



Assessment Offered Bank Methods
-------------------------------

   .. automethod:: AssessmentOfferedBankSession.can_lookup_assessment_offered_bank_mappings

   .. automethod:: AssessmentOfferedBankSession.use_comparative_bank_view

   .. automethod:: AssessmentOfferedBankSession.use_plenary_bank_view

   .. automethod:: AssessmentOfferedBankSession.get_assessment_offered_ids_by_bank

   .. automethod:: AssessmentOfferedBankSession.get_assessments_offered_by_bank

   .. automethod:: AssessmentOfferedBankSession.get_assessment_offered_ids_by_banks

   .. automethod:: AssessmentOfferedBankSession.get_assessments_offered_by_banks

   .. automethod:: AssessmentOfferedBankSession.get_bank_ids_by_assessment_offered

   .. automethod:: AssessmentOfferedBankSession.get_banks_by_assessment_offered



Assessment Offered Bank Assignment Methods
------------------------------------------

   .. automethod:: AssessmentOfferedBankAssignmentSession.can_assign_assessments_offered

   .. automethod:: AssessmentOfferedBankAssignmentSession.can_assign_assessments_offered_to_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentOfferedBankAssignmentSession.get_assignable_bank_ids_for_assessment_offered

   .. automethod:: AssessmentOfferedBankAssignmentSession.assign_assessment_offered_to_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.unassign_assessment_offered_from_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.reassign_assessment_offered_to_billing



Assessment Taken Bank Methods
-----------------------------

   .. automethod:: AssessmentTakenBankSession.can_lookup_assessment_taken_bank_mappings

   .. automethod:: AssessmentTakenBankSession.use_comparative_bank_view

   .. automethod:: AssessmentTakenBankSession.use_plenary_bank_view

   .. automethod:: AssessmentTakenBankSession.get_assessment_taken_ids_by_bank

   .. automethod:: AssessmentTakenBankSession.get_assessments_taken_by_bank

   .. automethod:: AssessmentTakenBankSession.get_assessment_taken_ids_by_banks

   .. automethod:: AssessmentTakenBankSession.get_assessments_taken_by_banks

   .. automethod:: AssessmentTakenBankSession.get_bank_ids_by_assessment_taken

   .. automethod:: AssessmentTakenBankSession.get_banks_by_assessment_taken



Assessment Taken Bank Assignment Methods
----------------------------------------

   .. automethod:: AssessmentTakenBankAssignmentSession.can_assign_assessments_taken

   .. automethod:: AssessmentTakenBankAssignmentSession.can_assign_assessments_taken_to_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentTakenBankAssignmentSession.get_assignable_bank_ids_for_assessment_taken

   .. automethod:: AssessmentTakenBankAssignmentSession.assign_assessment_taken_to_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.unassign_assessment_taken_from_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.reassign_assessment_taken_to_billing



Bank Lookup Methods
-------------------

   .. automethod:: BankLookupSession.can_lookup_banks

   .. automethod:: BankLookupSession.use_comparative_bank_view

   .. automethod:: BankLookupSession.use_plenary_bank_view

   .. automethod:: BankLookupSession.get_bank

   .. automethod:: BankLookupSession.get_banks_by_ids

   .. automethod:: BankLookupSession.get_banks_by_genus_type

   .. automethod:: BankLookupSession.get_banks_by_parent_genus_type

   .. automethod:: BankLookupSession.get_banks_by_record_type

   .. automethod:: BankLookupSession.get_banks_by_provider

   .. autoattribute:: BankLookupSession.banks



Bank Query Methods
------------------

   .. automethod:: BankQuerySession.can_search_banks

   .. autoattribute:: BankQuerySession.bank_query

   .. automethod:: BankQuerySession.get_banks_by_query



Bank Admin Methods
------------------

   .. automethod:: BankAdminSession.can_create_banks

   .. automethod:: BankAdminSession.can_create_bank_with_record_types

   .. automethod:: BankAdminSession.get_bank_form_for_create

   .. automethod:: BankAdminSession.create_bank

   .. automethod:: BankAdminSession.can_update_banks

   .. automethod:: BankAdminSession.get_bank_form_for_update

   .. automethod:: BankAdminSession.update_bank

   .. automethod:: BankAdminSession.can_delete_banks

   .. automethod:: BankAdminSession.delete_bank

   .. automethod:: BankAdminSession.can_manage_bank_aliases

   .. automethod:: BankAdminSession.alias_bank



Bank Hierarchy Methods
----------------------

   .. autoattribute:: BankHierarchySession.bank_hierarchy_id

   .. autoattribute:: BankHierarchySession.bank_hierarchy

   .. automethod:: BankHierarchySession.can_access_bank_hierarchy

   .. automethod:: BankHierarchySession.use_comparative_bank_view

   .. automethod:: BankHierarchySession.use_plenary_bank_view

   .. autoattribute:: BankHierarchySession.root_bank_ids

   .. autoattribute:: BankHierarchySession.root_banks

   .. automethod:: BankHierarchySession.has_parent_banks

   .. automethod:: BankHierarchySession.is_parent_of_bank

   .. automethod:: BankHierarchySession.get_parent_bank_ids

   .. automethod:: BankHierarchySession.get_parent_banks

   .. automethod:: BankHierarchySession.is_ancestor_of_bank

   .. automethod:: BankHierarchySession.has_child_banks

   .. automethod:: BankHierarchySession.is_child_of_bank

   .. automethod:: BankHierarchySession.get_child_bank_ids

   .. automethod:: BankHierarchySession.get_child_banks

   .. automethod:: BankHierarchySession.is_descendant_of_bank

   .. automethod:: BankHierarchySession.get_bank_node_ids

   .. automethod:: BankHierarchySession.get_bank_nodes



Bank Hierarchy Design Methods
-----------------------------

   .. autoattribute:: BankHierarchyDesignSession.bank_hierarchy_id

   .. autoattribute:: BankHierarchyDesignSession.bank_hierarchy

   .. automethod:: BankHierarchyDesignSession.can_modify_bank_hierarchy

   .. automethod:: BankHierarchyDesignSession.add_root_bank

   .. automethod:: BankHierarchyDesignSession.remove_root_bank

   .. automethod:: BankHierarchyDesignSession.add_child_bank

   .. automethod:: BankHierarchyDesignSession.remove_child_bank

   .. automethod:: BankHierarchyDesignSession.remove_child_banks



Assessment Methods
------------------

   .. autoattribute:: AssessmentSession.bank_id

   .. autoattribute:: AssessmentSession.bank

   .. automethod:: AssessmentSession.can_take_assessments

   .. automethod:: AssessmentSession.has_assessment_begun

   .. automethod:: AssessmentSession.is_assessment_over

   .. automethod:: AssessmentSession.requires_synchronous_sections

   .. automethod:: AssessmentSession.get_first_assessment_section

   .. automethod:: AssessmentSession.has_next_assessment_section

   .. automethod:: AssessmentSession.get_next_assessment_section

   .. automethod:: AssessmentSession.has_previous_assessment_section

   .. automethod:: AssessmentSession.get_previous_assessment_section

   .. automethod:: AssessmentSession.get_assessment_section

   .. automethod:: AssessmentSession.get_assessment_sections

   .. automethod:: AssessmentSession.is_assessment_section_complete

   .. automethod:: AssessmentSession.get_incomplete_assessment_sections

   .. automethod:: AssessmentSession.has_assessment_section_begun

   .. automethod:: AssessmentSession.is_assessment_section_over

   .. automethod:: AssessmentSession.requires_synchronous_responses

   .. automethod:: AssessmentSession.get_first_question

   .. automethod:: AssessmentSession.has_next_question

   .. automethod:: AssessmentSession.get_next_question

   .. automethod:: AssessmentSession.has_previous_question

   .. automethod:: AssessmentSession.get_previous_question

   .. automethod:: AssessmentSession.get_question

   .. automethod:: AssessmentSession.get_questions

   .. automethod:: AssessmentSession.get_response_form

   .. automethod:: AssessmentSession.submit_response

   .. automethod:: AssessmentSession.skip_item

   .. automethod:: AssessmentSession.is_question_answered

   .. automethod:: AssessmentSession.get_unanswered_questions

   .. automethod:: AssessmentSession.has_unanswered_questions

   .. automethod:: AssessmentSession.get_first_unanswered_question

   .. automethod:: AssessmentSession.has_next_unanswered_question

   .. automethod:: AssessmentSession.get_next_unanswered_question

   .. automethod:: AssessmentSession.has_previous_unanswered_question

   .. automethod:: AssessmentSession.get_previous_unanswered_question

   .. automethod:: AssessmentSession.get_response

   .. automethod:: AssessmentSession.get_responses

   .. automethod:: AssessmentSession.clear_response

   .. automethod:: AssessmentSession.finish_assessment_section

   .. automethod:: AssessmentSession.is_answer_available

   .. automethod:: AssessmentSession.get_answers

   .. automethod:: AssessmentSession.finish_assessment



Item Lookup Methods
-------------------

   .. autoattribute:: ItemLookupSession.bank_id

   .. autoattribute:: ItemLookupSession.bank

   .. automethod:: ItemLookupSession.can_lookup_items

   .. automethod:: ItemLookupSession.use_comparative_item_view

   .. automethod:: ItemLookupSession.use_plenary_item_view

   .. automethod:: ItemLookupSession.use_federated_bank_view

   .. automethod:: ItemLookupSession.use_isolated_bank_view

   .. automethod:: ItemLookupSession.get_item

   .. automethod:: ItemLookupSession.get_items_by_ids

   .. automethod:: ItemLookupSession.get_items_by_genus_type

   .. automethod:: ItemLookupSession.get_items_by_parent_genus_type

   .. automethod:: ItemLookupSession.get_items_by_record_type

   .. automethod:: ItemLookupSession.get_items_by_question

   .. automethod:: ItemLookupSession.get_items_by_answer

   .. automethod:: ItemLookupSession.get_items_by_learning_objective

   .. automethod:: ItemLookupSession.get_items_by_learning_objectives

   .. autoattribute:: ItemLookupSession.items



Item Query Methods
------------------

   .. autoattribute:: ItemQuerySession.bank_id

   .. autoattribute:: ItemQuerySession.bank

   .. automethod:: ItemQuerySession.can_search_items

   .. automethod:: ItemQuerySession.use_federated_bank_view

   .. automethod:: ItemQuerySession.use_isolated_bank_view

   .. autoattribute:: ItemQuerySession.item_query

   .. automethod:: ItemQuerySession.get_items_by_query



Item Search Methods
-------------------

   .. autoattribute:: ItemSearchSession.item_search

   .. autoattribute:: ItemSearchSession.item_search_order

   .. automethod:: ItemSearchSession.get_items_by_search

   .. automethod:: ItemSearchSession.get_item_query_from_inspector



Item Admin Methods
------------------

   .. autoattribute:: ItemAdminSession.bank_id

   .. autoattribute:: ItemAdminSession.bank

   .. automethod:: ItemAdminSession.can_create_items

   .. automethod:: ItemAdminSession.can_create_item_with_record_types

   .. automethod:: ItemAdminSession.get_item_form_for_create

   .. automethod:: ItemAdminSession.create_item

   .. automethod:: ItemAdminSession.can_update_items

   .. automethod:: ItemAdminSession.get_item_form_for_update

   .. automethod:: ItemAdminSession.update_item

   .. automethod:: ItemAdminSession.can_delete_items

   .. automethod:: ItemAdminSession.delete_item

   .. automethod:: ItemAdminSession.can_manage_item_aliases

   .. automethod:: ItemAdminSession.alias_item

   .. automethod:: ItemAdminSession.can_create_questions

   .. automethod:: ItemAdminSession.can_create_question_with_record_types

   .. automethod:: ItemAdminSession.get_question_form_for_create

   .. automethod:: ItemAdminSession.create_question

   .. automethod:: ItemAdminSession.can_update_questions

   .. automethod:: ItemAdminSession.get_question_form_for_update

   .. automethod:: ItemAdminSession.update_question

   .. automethod:: ItemAdminSession.can_delete_questions

   .. automethod:: ItemAdminSession.delete_question

   .. automethod:: ItemAdminSession.can_create_answers

   .. automethod:: ItemAdminSession.can_create_answers_with_record_types

   .. automethod:: ItemAdminSession.get_answer_form_for_create

   .. automethod:: ItemAdminSession.create_answer

   .. automethod:: ItemAdminSession.can_update_answers

   .. automethod:: ItemAdminSession.get_answer_form_for_update

   .. automethod:: ItemAdminSession.update_answer

   .. automethod:: ItemAdminSession.can_delete_answers

   .. automethod:: ItemAdminSession.delete_answer



Item Notification Methods
-------------------------

   .. autoattribute:: ItemNotificationSession.bank_id

   .. autoattribute:: ItemNotificationSession.bank

   .. automethod:: ItemNotificationSession.can_register_for_item_notifications

   .. automethod:: ItemNotificationSession.use_federated_bank_view

   .. automethod:: ItemNotificationSession.use_isolated_bank_view

   .. automethod:: ItemNotificationSession.reliable_item_notifications

   .. automethod:: ItemNotificationSession.unreliable_item_notifications

   .. automethod:: ItemNotificationSession.acknowledge_item_notification

   .. automethod:: ItemNotificationSession.register_for_new_items

   .. automethod:: ItemNotificationSession.register_for_changed_items

   .. automethod:: ItemNotificationSession.register_for_changed_item

   .. automethod:: ItemNotificationSession.register_for_deleted_items

   .. automethod:: ItemNotificationSession.register_for_deleted_item



Assessment Lookup Methods
-------------------------

   .. autoattribute:: AssessmentLookupSession.bank_id

   .. autoattribute:: AssessmentLookupSession.bank

   .. automethod:: AssessmentLookupSession.can_lookup_assessments

   .. automethod:: AssessmentLookupSession.use_comparative_assessment_view

   .. automethod:: AssessmentLookupSession.use_plenary_assessment_view

   .. automethod:: AssessmentLookupSession.use_federated_bank_view

   .. automethod:: AssessmentLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentLookupSession.get_assessment

   .. automethod:: AssessmentLookupSession.get_assessments_by_ids

   .. automethod:: AssessmentLookupSession.get_assessments_by_genus_type

   .. automethod:: AssessmentLookupSession.get_assessments_by_parent_genus_type

   .. automethod:: AssessmentLookupSession.get_assessments_by_record_type

   .. autoattribute:: AssessmentLookupSession.assessments



Assessment Query Methods
------------------------

   .. autoattribute:: AssessmentQuerySession.bank_id

   .. autoattribute:: AssessmentQuerySession.bank

   .. automethod:: AssessmentQuerySession.can_search_assessments

   .. automethod:: AssessmentQuerySession.use_federated_bank_view

   .. automethod:: AssessmentQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentQuerySession.assessment_query

   .. automethod:: AssessmentQuerySession.get_assessments_by_query



Assessment Admin Methods
------------------------

   .. autoattribute:: AssessmentAdminSession.bank_id

   .. autoattribute:: AssessmentAdminSession.bank

   .. automethod:: AssessmentAdminSession.can_create_assessments

   .. automethod:: AssessmentAdminSession.can_create_assessment_with_record_types

   .. automethod:: AssessmentAdminSession.get_assessment_form_for_create

   .. automethod:: AssessmentAdminSession.create_assessment

   .. automethod:: AssessmentAdminSession.can_update_assessments

   .. automethod:: AssessmentAdminSession.get_assessment_form_for_update

   .. automethod:: AssessmentAdminSession.update_assessment

   .. automethod:: AssessmentAdminSession.can_delete_assessments

   .. automethod:: AssessmentAdminSession.delete_assessment

   .. automethod:: AssessmentAdminSession.can_manage_assessment_aliases

   .. automethod:: AssessmentAdminSession.alias_assessment



Assessment Basic Authoring Methods
----------------------------------

   .. autoattribute:: AssessmentBasicAuthoringSession.bank_id

   .. autoattribute:: AssessmentBasicAuthoringSession.bank

   .. automethod:: AssessmentBasicAuthoringSession.can_author_assessments

   .. automethod:: AssessmentBasicAuthoringSession.get_items

   .. automethod:: AssessmentBasicAuthoringSession.add_item

   .. automethod:: AssessmentBasicAuthoringSession.remove_item

   .. automethod:: AssessmentBasicAuthoringSession.move_item

   .. automethod:: AssessmentBasicAuthoringSession.order_items



Assessment Offered Lookup Methods
---------------------------------

   .. autoattribute:: AssessmentOfferedLookupSession.bank_id

   .. autoattribute:: AssessmentOfferedLookupSession.bank

   .. automethod:: AssessmentOfferedLookupSession.can_lookup_assessments_offered

   .. automethod:: AssessmentOfferedLookupSession.use_comparative_assessment_offered_view

   .. automethod:: AssessmentOfferedLookupSession.use_plenary_assessment_offered_view

   .. automethod:: AssessmentOfferedLookupSession.use_federated_bank_view

   .. automethod:: AssessmentOfferedLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentOfferedLookupSession.get_assessment_offered

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_ids

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_genus_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_parent_genus_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_record_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_date

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_for_assessment

   .. autoattribute:: AssessmentOfferedLookupSession.assessments_offered



Assessment Offered Query Methods
--------------------------------

   .. autoattribute:: AssessmentOfferedQuerySession.bank_id

   .. autoattribute:: AssessmentOfferedQuerySession.bank

   .. automethod:: AssessmentOfferedQuerySession.can_search_assessments_offered

   .. automethod:: AssessmentOfferedQuerySession.use_federated_bank_view

   .. automethod:: AssessmentOfferedQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentOfferedQuerySession.assessment_offered_query

   .. automethod:: AssessmentOfferedQuerySession.get_assessments_offered_by_query



Assessment Offered Admin Methods
--------------------------------

   .. autoattribute:: AssessmentOfferedAdminSession.bank_id

   .. autoattribute:: AssessmentOfferedAdminSession.bank

   .. automethod:: AssessmentOfferedAdminSession.can_create_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.can_create_assessment_offered_with_record_types

   .. automethod:: AssessmentOfferedAdminSession.get_assessment_offered_form_for_create

   .. automethod:: AssessmentOfferedAdminSession.create_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_update_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.get_assessment_offered_form_for_update

   .. automethod:: AssessmentOfferedAdminSession.update_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_delete_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.delete_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_manage_assessment_offered_aliases

   .. automethod:: AssessmentOfferedAdminSession.alias_assessment_offered



Assessment Taken Lookup Methods
-------------------------------

   .. autoattribute:: AssessmentTakenLookupSession.bank_id

   .. autoattribute:: AssessmentTakenLookupSession.bank

   .. automethod:: AssessmentTakenLookupSession.can_lookup_assessments_taken

   .. automethod:: AssessmentTakenLookupSession.use_comparative_assessment_taken_view

   .. automethod:: AssessmentTakenLookupSession.use_plenary_assessment_taken_view

   .. automethod:: AssessmentTakenLookupSession.use_federated_bank_view

   .. automethod:: AssessmentTakenLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentTakenLookupSession.get_assessment_taken

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_ids

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_genus_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_parent_genus_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_record_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker_and_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker_and_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker_and_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker_and_assessment_offered

   .. autoattribute:: AssessmentTakenLookupSession.assessments_taken



Assessment Taken Query Methods
------------------------------

   .. autoattribute:: AssessmentTakenQuerySession.bank_id

   .. autoattribute:: AssessmentTakenQuerySession.bank

   .. automethod:: AssessmentTakenQuerySession.can_search_assessments_taken

   .. automethod:: AssessmentTakenQuerySession.use_federated_bank_view

   .. automethod:: AssessmentTakenQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentTakenQuerySession.assessment_taken_query

   .. automethod:: AssessmentTakenQuerySession.get_assessments_taken_by_query



Assessment Taken Admin Methods
------------------------------

   .. autoattribute:: AssessmentTakenAdminSession.bank_id

   .. autoattribute:: AssessmentTakenAdminSession.bank

   .. automethod:: AssessmentTakenAdminSession.can_create_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.can_create_assessment_taken_with_record_types

   .. automethod:: AssessmentTakenAdminSession.get_assessment_taken_form_for_create

   .. automethod:: AssessmentTakenAdminSession.create_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_update_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.get_assessment_taken_form_for_update

   .. automethod:: AssessmentTakenAdminSession.update_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_delete_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.delete_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_manage_assessment_taken_aliases

   .. automethod:: AssessmentTakenAdminSession.alias_assessment_taken



Assessment Taken Query
----------------------

.. autoclass:: AssessmentTakenQuery
   :show-inheritance:

   .. automethod:: AssessmentTakenQuery.match_assessment_offered_id

   .. autoattribute:: AssessmentTakenQuery.assessment_offered_id_terms

   .. automethod:: AssessmentTakenQuery.supports_assessment_offered_query

   .. autoattribute:: AssessmentTakenQuery.assessment_offered_query

   .. autoattribute:: AssessmentTakenQuery.assessment_offered_terms

   .. automethod:: AssessmentTakenQuery.match_taker_id

   .. autoattribute:: AssessmentTakenQuery.taker_id_terms

   .. automethod:: AssessmentTakenQuery.supports_taker_query

   .. autoattribute:: AssessmentTakenQuery.taker_query

   .. autoattribute:: AssessmentTakenQuery.taker_terms

   .. automethod:: AssessmentTakenQuery.match_taking_agent_id

   .. autoattribute:: AssessmentTakenQuery.taking_agent_id_terms

   .. automethod:: AssessmentTakenQuery.supports_taking_agent_query

   .. autoattribute:: AssessmentTakenQuery.taking_agent_query

   .. autoattribute:: AssessmentTakenQuery.taking_agent_terms

   .. automethod:: AssessmentTakenQuery.match_actual_start_time

   .. automethod:: AssessmentTakenQuery.match_any_actual_start_time

   .. autoattribute:: AssessmentTakenQuery.actual_start_time_terms

   .. automethod:: AssessmentTakenQuery.match_completion_time

   .. automethod:: AssessmentTakenQuery.match_any_completion_time

   .. autoattribute:: AssessmentTakenQuery.completion_time_terms

   .. automethod:: AssessmentTakenQuery.match_time_spent

   .. autoattribute:: AssessmentTakenQuery.time_spent_terms

   .. automethod:: AssessmentTakenQuery.match_score_system_id

   .. autoattribute:: AssessmentTakenQuery.score_system_id_terms

   .. automethod:: AssessmentTakenQuery.supports_score_system_query

   .. autoattribute:: AssessmentTakenQuery.score_system_query

   .. automethod:: AssessmentTakenQuery.match_any_score_system

   .. autoattribute:: AssessmentTakenQuery.score_system_terms

   .. automethod:: AssessmentTakenQuery.match_score

   .. automethod:: AssessmentTakenQuery.match_any_score

   .. autoattribute:: AssessmentTakenQuery.score_terms

   .. automethod:: AssessmentTakenQuery.match_grade_id

   .. autoattribute:: AssessmentTakenQuery.grade_id_terms

   .. automethod:: AssessmentTakenQuery.supports_grade_query

   .. autoattribute:: AssessmentTakenQuery.grade_query

   .. automethod:: AssessmentTakenQuery.match_any_grade

   .. autoattribute:: AssessmentTakenQuery.grade_terms

   .. automethod:: AssessmentTakenQuery.match_feedback

   .. automethod:: AssessmentTakenQuery.match_any_feedback

   .. autoattribute:: AssessmentTakenQuery.feedback_terms

   .. automethod:: AssessmentTakenQuery.match_rubric_id

   .. autoattribute:: AssessmentTakenQuery.rubric_id_terms

   .. automethod:: AssessmentTakenQuery.supports_rubric_query

   .. autoattribute:: AssessmentTakenQuery.rubric_query

   .. automethod:: AssessmentTakenQuery.match_any_rubric

   .. autoattribute:: AssessmentTakenQuery.rubric_terms

   .. automethod:: AssessmentTakenQuery.match_bank_id

   .. autoattribute:: AssessmentTakenQuery.bank_id_terms

   .. automethod:: AssessmentTakenQuery.supports_bank_query

   .. autoattribute:: AssessmentTakenQuery.bank_query

   .. autoattribute:: AssessmentTakenQuery.bank_terms

   .. automethod:: AssessmentTakenQuery.get_assessment_taken_query_record



Item Bank Methods
-----------------

   .. automethod:: ItemBankSession.can_lookup_item_bank_mappings

   .. automethod:: ItemBankSession.use_comparative_bank_view

   .. automethod:: ItemBankSession.use_plenary_bank_view

   .. automethod:: ItemBankSession.get_item_ids_by_bank

   .. automethod:: ItemBankSession.get_items_by_bank

   .. automethod:: ItemBankSession.get_item_ids_by_banks

   .. automethod:: ItemBankSession.get_items_by_banks

   .. automethod:: ItemBankSession.get_bank_ids_by_item

   .. automethod:: ItemBankSession.get_banks_by_item



Item Bank Assignment Methods
----------------------------

   .. automethod:: ItemBankAssignmentSession.can_assign_items

   .. automethod:: ItemBankAssignmentSession.can_assign_items_to_bank

   .. automethod:: ItemBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: ItemBankAssignmentSession.get_assignable_bank_ids_for_item

   .. automethod:: ItemBankAssignmentSession.assign_item_to_bank

   .. automethod:: ItemBankAssignmentSession.unassign_item_from_bank

   .. automethod:: ItemBankAssignmentSession.reassign_item_to_billing



Assessment Bank Methods
-----------------------

   .. automethod:: AssessmentBankSession.can_lookup_assessment_bank_mappings

   .. automethod:: AssessmentBankSession.use_comparative_bank_view

   .. automethod:: AssessmentBankSession.use_plenary_bank_view

   .. automethod:: AssessmentBankSession.get_assessment_ids_by_bank

   .. automethod:: AssessmentBankSession.get_assessments_by_bank

   .. automethod:: AssessmentBankSession.get_assessment_ids_by_banks

   .. automethod:: AssessmentBankSession.get_assessments_by_banks

   .. automethod:: AssessmentBankSession.get_bank_ids_by_assessment

   .. automethod:: AssessmentBankSession.get_banks_by_assessment



Assessment Bank Assignment Methods
----------------------------------

   .. automethod:: AssessmentBankAssignmentSession.can_assign_assessments

   .. automethod:: AssessmentBankAssignmentSession.can_assign_assessments_to_bank

   .. automethod:: AssessmentBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentBankAssignmentSession.get_assignable_bank_ids_for_assessment

   .. automethod:: AssessmentBankAssignmentSession.assign_assessment_to_bank

   .. automethod:: AssessmentBankAssignmentSession.unassign_assessment_from_bank

   .. automethod:: AssessmentBankAssignmentSession.reassign_assessment_to_billing



Assessment Offered Bank Methods
-------------------------------

   .. automethod:: AssessmentOfferedBankSession.can_lookup_assessment_offered_bank_mappings

   .. automethod:: AssessmentOfferedBankSession.use_comparative_bank_view

   .. automethod:: AssessmentOfferedBankSession.use_plenary_bank_view

   .. automethod:: AssessmentOfferedBankSession.get_assessment_offered_ids_by_bank

   .. automethod:: AssessmentOfferedBankSession.get_assessments_offered_by_bank

   .. automethod:: AssessmentOfferedBankSession.get_assessment_offered_ids_by_banks

   .. automethod:: AssessmentOfferedBankSession.get_assessments_offered_by_banks

   .. automethod:: AssessmentOfferedBankSession.get_bank_ids_by_assessment_offered

   .. automethod:: AssessmentOfferedBankSession.get_banks_by_assessment_offered



Assessment Offered Bank Assignment Methods
------------------------------------------

   .. automethod:: AssessmentOfferedBankAssignmentSession.can_assign_assessments_offered

   .. automethod:: AssessmentOfferedBankAssignmentSession.can_assign_assessments_offered_to_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentOfferedBankAssignmentSession.get_assignable_bank_ids_for_assessment_offered

   .. automethod:: AssessmentOfferedBankAssignmentSession.assign_assessment_offered_to_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.unassign_assessment_offered_from_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.reassign_assessment_offered_to_billing



Assessment Taken Bank Methods
-----------------------------

   .. automethod:: AssessmentTakenBankSession.can_lookup_assessment_taken_bank_mappings

   .. automethod:: AssessmentTakenBankSession.use_comparative_bank_view

   .. automethod:: AssessmentTakenBankSession.use_plenary_bank_view

   .. automethod:: AssessmentTakenBankSession.get_assessment_taken_ids_by_bank

   .. automethod:: AssessmentTakenBankSession.get_assessments_taken_by_bank

   .. automethod:: AssessmentTakenBankSession.get_assessment_taken_ids_by_banks

   .. automethod:: AssessmentTakenBankSession.get_assessments_taken_by_banks

   .. automethod:: AssessmentTakenBankSession.get_bank_ids_by_assessment_taken

   .. automethod:: AssessmentTakenBankSession.get_banks_by_assessment_taken



Assessment Taken Bank Assignment Methods
----------------------------------------

   .. automethod:: AssessmentTakenBankAssignmentSession.can_assign_assessments_taken

   .. automethod:: AssessmentTakenBankAssignmentSession.can_assign_assessments_taken_to_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentTakenBankAssignmentSession.get_assignable_bank_ids_for_assessment_taken

   .. automethod:: AssessmentTakenBankAssignmentSession.assign_assessment_taken_to_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.unassign_assessment_taken_from_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.reassign_assessment_taken_to_billing



Bank Lookup Methods
-------------------

   .. automethod:: BankLookupSession.can_lookup_banks

   .. automethod:: BankLookupSession.use_comparative_bank_view

   .. automethod:: BankLookupSession.use_plenary_bank_view

   .. automethod:: BankLookupSession.get_bank

   .. automethod:: BankLookupSession.get_banks_by_ids

   .. automethod:: BankLookupSession.get_banks_by_genus_type

   .. automethod:: BankLookupSession.get_banks_by_parent_genus_type

   .. automethod:: BankLookupSession.get_banks_by_record_type

   .. automethod:: BankLookupSession.get_banks_by_provider

   .. autoattribute:: BankLookupSession.banks



Bank Query Methods
------------------

   .. automethod:: BankQuerySession.can_search_banks

   .. autoattribute:: BankQuerySession.bank_query

   .. automethod:: BankQuerySession.get_banks_by_query



Bank Admin Methods
------------------

   .. automethod:: BankAdminSession.can_create_banks

   .. automethod:: BankAdminSession.can_create_bank_with_record_types

   .. automethod:: BankAdminSession.get_bank_form_for_create

   .. automethod:: BankAdminSession.create_bank

   .. automethod:: BankAdminSession.can_update_banks

   .. automethod:: BankAdminSession.get_bank_form_for_update

   .. automethod:: BankAdminSession.update_bank

   .. automethod:: BankAdminSession.can_delete_banks

   .. automethod:: BankAdminSession.delete_bank

   .. automethod:: BankAdminSession.can_manage_bank_aliases

   .. automethod:: BankAdminSession.alias_bank



Bank Hierarchy Methods
----------------------

   .. autoattribute:: BankHierarchySession.bank_hierarchy_id

   .. autoattribute:: BankHierarchySession.bank_hierarchy

   .. automethod:: BankHierarchySession.can_access_bank_hierarchy

   .. automethod:: BankHierarchySession.use_comparative_bank_view

   .. automethod:: BankHierarchySession.use_plenary_bank_view

   .. autoattribute:: BankHierarchySession.root_bank_ids

   .. autoattribute:: BankHierarchySession.root_banks

   .. automethod:: BankHierarchySession.has_parent_banks

   .. automethod:: BankHierarchySession.is_parent_of_bank

   .. automethod:: BankHierarchySession.get_parent_bank_ids

   .. automethod:: BankHierarchySession.get_parent_banks

   .. automethod:: BankHierarchySession.is_ancestor_of_bank

   .. automethod:: BankHierarchySession.has_child_banks

   .. automethod:: BankHierarchySession.is_child_of_bank

   .. automethod:: BankHierarchySession.get_child_bank_ids

   .. automethod:: BankHierarchySession.get_child_banks

   .. automethod:: BankHierarchySession.is_descendant_of_bank

   .. automethod:: BankHierarchySession.get_bank_node_ids

   .. automethod:: BankHierarchySession.get_bank_nodes



Bank Hierarchy Design Methods
-----------------------------

   .. autoattribute:: BankHierarchyDesignSession.bank_hierarchy_id

   .. autoattribute:: BankHierarchyDesignSession.bank_hierarchy

   .. automethod:: BankHierarchyDesignSession.can_modify_bank_hierarchy

   .. automethod:: BankHierarchyDesignSession.add_root_bank

   .. automethod:: BankHierarchyDesignSession.remove_root_bank

   .. automethod:: BankHierarchyDesignSession.add_child_bank

   .. automethod:: BankHierarchyDesignSession.remove_child_bank

   .. automethod:: BankHierarchyDesignSession.remove_child_banks



Assessment Methods
------------------

   .. autoattribute:: AssessmentSession.bank_id

   .. autoattribute:: AssessmentSession.bank

   .. automethod:: AssessmentSession.can_take_assessments

   .. automethod:: AssessmentSession.has_assessment_begun

   .. automethod:: AssessmentSession.is_assessment_over

   .. automethod:: AssessmentSession.requires_synchronous_sections

   .. automethod:: AssessmentSession.get_first_assessment_section

   .. automethod:: AssessmentSession.has_next_assessment_section

   .. automethod:: AssessmentSession.get_next_assessment_section

   .. automethod:: AssessmentSession.has_previous_assessment_section

   .. automethod:: AssessmentSession.get_previous_assessment_section

   .. automethod:: AssessmentSession.get_assessment_section

   .. automethod:: AssessmentSession.get_assessment_sections

   .. automethod:: AssessmentSession.is_assessment_section_complete

   .. automethod:: AssessmentSession.get_incomplete_assessment_sections

   .. automethod:: AssessmentSession.has_assessment_section_begun

   .. automethod:: AssessmentSession.is_assessment_section_over

   .. automethod:: AssessmentSession.requires_synchronous_responses

   .. automethod:: AssessmentSession.get_first_question

   .. automethod:: AssessmentSession.has_next_question

   .. automethod:: AssessmentSession.get_next_question

   .. automethod:: AssessmentSession.has_previous_question

   .. automethod:: AssessmentSession.get_previous_question

   .. automethod:: AssessmentSession.get_question

   .. automethod:: AssessmentSession.get_questions

   .. automethod:: AssessmentSession.get_response_form

   .. automethod:: AssessmentSession.submit_response

   .. automethod:: AssessmentSession.skip_item

   .. automethod:: AssessmentSession.is_question_answered

   .. automethod:: AssessmentSession.get_unanswered_questions

   .. automethod:: AssessmentSession.has_unanswered_questions

   .. automethod:: AssessmentSession.get_first_unanswered_question

   .. automethod:: AssessmentSession.has_next_unanswered_question

   .. automethod:: AssessmentSession.get_next_unanswered_question

   .. automethod:: AssessmentSession.has_previous_unanswered_question

   .. automethod:: AssessmentSession.get_previous_unanswered_question

   .. automethod:: AssessmentSession.get_response

   .. automethod:: AssessmentSession.get_responses

   .. automethod:: AssessmentSession.clear_response

   .. automethod:: AssessmentSession.finish_assessment_section

   .. automethod:: AssessmentSession.is_answer_available

   .. automethod:: AssessmentSession.get_answers

   .. automethod:: AssessmentSession.finish_assessment



Item Lookup Methods
-------------------

   .. autoattribute:: ItemLookupSession.bank_id

   .. autoattribute:: ItemLookupSession.bank

   .. automethod:: ItemLookupSession.can_lookup_items

   .. automethod:: ItemLookupSession.use_comparative_item_view

   .. automethod:: ItemLookupSession.use_plenary_item_view

   .. automethod:: ItemLookupSession.use_federated_bank_view

   .. automethod:: ItemLookupSession.use_isolated_bank_view

   .. automethod:: ItemLookupSession.get_item

   .. automethod:: ItemLookupSession.get_items_by_ids

   .. automethod:: ItemLookupSession.get_items_by_genus_type

   .. automethod:: ItemLookupSession.get_items_by_parent_genus_type

   .. automethod:: ItemLookupSession.get_items_by_record_type

   .. automethod:: ItemLookupSession.get_items_by_question

   .. automethod:: ItemLookupSession.get_items_by_answer

   .. automethod:: ItemLookupSession.get_items_by_learning_objective

   .. automethod:: ItemLookupSession.get_items_by_learning_objectives

   .. autoattribute:: ItemLookupSession.items



Item Query Methods
------------------

   .. autoattribute:: ItemQuerySession.bank_id

   .. autoattribute:: ItemQuerySession.bank

   .. automethod:: ItemQuerySession.can_search_items

   .. automethod:: ItemQuerySession.use_federated_bank_view

   .. automethod:: ItemQuerySession.use_isolated_bank_view

   .. autoattribute:: ItemQuerySession.item_query

   .. automethod:: ItemQuerySession.get_items_by_query



Item Search Methods
-------------------

   .. autoattribute:: ItemSearchSession.item_search

   .. autoattribute:: ItemSearchSession.item_search_order

   .. automethod:: ItemSearchSession.get_items_by_search

   .. automethod:: ItemSearchSession.get_item_query_from_inspector



Item Admin Methods
------------------

   .. autoattribute:: ItemAdminSession.bank_id

   .. autoattribute:: ItemAdminSession.bank

   .. automethod:: ItemAdminSession.can_create_items

   .. automethod:: ItemAdminSession.can_create_item_with_record_types

   .. automethod:: ItemAdminSession.get_item_form_for_create

   .. automethod:: ItemAdminSession.create_item

   .. automethod:: ItemAdminSession.can_update_items

   .. automethod:: ItemAdminSession.get_item_form_for_update

   .. automethod:: ItemAdminSession.update_item

   .. automethod:: ItemAdminSession.can_delete_items

   .. automethod:: ItemAdminSession.delete_item

   .. automethod:: ItemAdminSession.can_manage_item_aliases

   .. automethod:: ItemAdminSession.alias_item

   .. automethod:: ItemAdminSession.can_create_questions

   .. automethod:: ItemAdminSession.can_create_question_with_record_types

   .. automethod:: ItemAdminSession.get_question_form_for_create

   .. automethod:: ItemAdminSession.create_question

   .. automethod:: ItemAdminSession.can_update_questions

   .. automethod:: ItemAdminSession.get_question_form_for_update

   .. automethod:: ItemAdminSession.update_question

   .. automethod:: ItemAdminSession.can_delete_questions

   .. automethod:: ItemAdminSession.delete_question

   .. automethod:: ItemAdminSession.can_create_answers

   .. automethod:: ItemAdminSession.can_create_answers_with_record_types

   .. automethod:: ItemAdminSession.get_answer_form_for_create

   .. automethod:: ItemAdminSession.create_answer

   .. automethod:: ItemAdminSession.can_update_answers

   .. automethod:: ItemAdminSession.get_answer_form_for_update

   .. automethod:: ItemAdminSession.update_answer

   .. automethod:: ItemAdminSession.can_delete_answers

   .. automethod:: ItemAdminSession.delete_answer



Item Notification Methods
-------------------------

   .. autoattribute:: ItemNotificationSession.bank_id

   .. autoattribute:: ItemNotificationSession.bank

   .. automethod:: ItemNotificationSession.can_register_for_item_notifications

   .. automethod:: ItemNotificationSession.use_federated_bank_view

   .. automethod:: ItemNotificationSession.use_isolated_bank_view

   .. automethod:: ItemNotificationSession.reliable_item_notifications

   .. automethod:: ItemNotificationSession.unreliable_item_notifications

   .. automethod:: ItemNotificationSession.acknowledge_item_notification

   .. automethod:: ItemNotificationSession.register_for_new_items

   .. automethod:: ItemNotificationSession.register_for_changed_items

   .. automethod:: ItemNotificationSession.register_for_changed_item

   .. automethod:: ItemNotificationSession.register_for_deleted_items

   .. automethod:: ItemNotificationSession.register_for_deleted_item



Assessment Lookup Methods
-------------------------

   .. autoattribute:: AssessmentLookupSession.bank_id

   .. autoattribute:: AssessmentLookupSession.bank

   .. automethod:: AssessmentLookupSession.can_lookup_assessments

   .. automethod:: AssessmentLookupSession.use_comparative_assessment_view

   .. automethod:: AssessmentLookupSession.use_plenary_assessment_view

   .. automethod:: AssessmentLookupSession.use_federated_bank_view

   .. automethod:: AssessmentLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentLookupSession.get_assessment

   .. automethod:: AssessmentLookupSession.get_assessments_by_ids

   .. automethod:: AssessmentLookupSession.get_assessments_by_genus_type

   .. automethod:: AssessmentLookupSession.get_assessments_by_parent_genus_type

   .. automethod:: AssessmentLookupSession.get_assessments_by_record_type

   .. autoattribute:: AssessmentLookupSession.assessments



Assessment Query Methods
------------------------

   .. autoattribute:: AssessmentQuerySession.bank_id

   .. autoattribute:: AssessmentQuerySession.bank

   .. automethod:: AssessmentQuerySession.can_search_assessments

   .. automethod:: AssessmentQuerySession.use_federated_bank_view

   .. automethod:: AssessmentQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentQuerySession.assessment_query

   .. automethod:: AssessmentQuerySession.get_assessments_by_query



Assessment Admin Methods
------------------------

   .. autoattribute:: AssessmentAdminSession.bank_id

   .. autoattribute:: AssessmentAdminSession.bank

   .. automethod:: AssessmentAdminSession.can_create_assessments

   .. automethod:: AssessmentAdminSession.can_create_assessment_with_record_types

   .. automethod:: AssessmentAdminSession.get_assessment_form_for_create

   .. automethod:: AssessmentAdminSession.create_assessment

   .. automethod:: AssessmentAdminSession.can_update_assessments

   .. automethod:: AssessmentAdminSession.get_assessment_form_for_update

   .. automethod:: AssessmentAdminSession.update_assessment

   .. automethod:: AssessmentAdminSession.can_delete_assessments

   .. automethod:: AssessmentAdminSession.delete_assessment

   .. automethod:: AssessmentAdminSession.can_manage_assessment_aliases

   .. automethod:: AssessmentAdminSession.alias_assessment



Assessment Basic Authoring Methods
----------------------------------

   .. autoattribute:: AssessmentBasicAuthoringSession.bank_id

   .. autoattribute:: AssessmentBasicAuthoringSession.bank

   .. automethod:: AssessmentBasicAuthoringSession.can_author_assessments

   .. automethod:: AssessmentBasicAuthoringSession.get_items

   .. automethod:: AssessmentBasicAuthoringSession.add_item

   .. automethod:: AssessmentBasicAuthoringSession.remove_item

   .. automethod:: AssessmentBasicAuthoringSession.move_item

   .. automethod:: AssessmentBasicAuthoringSession.order_items



Assessment Offered Lookup Methods
---------------------------------

   .. autoattribute:: AssessmentOfferedLookupSession.bank_id

   .. autoattribute:: AssessmentOfferedLookupSession.bank

   .. automethod:: AssessmentOfferedLookupSession.can_lookup_assessments_offered

   .. automethod:: AssessmentOfferedLookupSession.use_comparative_assessment_offered_view

   .. automethod:: AssessmentOfferedLookupSession.use_plenary_assessment_offered_view

   .. automethod:: AssessmentOfferedLookupSession.use_federated_bank_view

   .. automethod:: AssessmentOfferedLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentOfferedLookupSession.get_assessment_offered

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_ids

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_genus_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_parent_genus_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_record_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_date

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_for_assessment

   .. autoattribute:: AssessmentOfferedLookupSession.assessments_offered



Assessment Offered Query Methods
--------------------------------

   .. autoattribute:: AssessmentOfferedQuerySession.bank_id

   .. autoattribute:: AssessmentOfferedQuerySession.bank

   .. automethod:: AssessmentOfferedQuerySession.can_search_assessments_offered

   .. automethod:: AssessmentOfferedQuerySession.use_federated_bank_view

   .. automethod:: AssessmentOfferedQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentOfferedQuerySession.assessment_offered_query

   .. automethod:: AssessmentOfferedQuerySession.get_assessments_offered_by_query



Assessment Offered Admin Methods
--------------------------------

   .. autoattribute:: AssessmentOfferedAdminSession.bank_id

   .. autoattribute:: AssessmentOfferedAdminSession.bank

   .. automethod:: AssessmentOfferedAdminSession.can_create_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.can_create_assessment_offered_with_record_types

   .. automethod:: AssessmentOfferedAdminSession.get_assessment_offered_form_for_create

   .. automethod:: AssessmentOfferedAdminSession.create_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_update_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.get_assessment_offered_form_for_update

   .. automethod:: AssessmentOfferedAdminSession.update_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_delete_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.delete_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_manage_assessment_offered_aliases

   .. automethod:: AssessmentOfferedAdminSession.alias_assessment_offered



Assessment Taken Lookup Methods
-------------------------------

   .. autoattribute:: AssessmentTakenLookupSession.bank_id

   .. autoattribute:: AssessmentTakenLookupSession.bank

   .. automethod:: AssessmentTakenLookupSession.can_lookup_assessments_taken

   .. automethod:: AssessmentTakenLookupSession.use_comparative_assessment_taken_view

   .. automethod:: AssessmentTakenLookupSession.use_plenary_assessment_taken_view

   .. automethod:: AssessmentTakenLookupSession.use_federated_bank_view

   .. automethod:: AssessmentTakenLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentTakenLookupSession.get_assessment_taken

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_ids

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_genus_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_parent_genus_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_record_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker_and_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker_and_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker_and_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker_and_assessment_offered

   .. autoattribute:: AssessmentTakenLookupSession.assessments_taken



Assessment Taken Query Methods
------------------------------

   .. autoattribute:: AssessmentTakenQuerySession.bank_id

   .. autoattribute:: AssessmentTakenQuerySession.bank

   .. automethod:: AssessmentTakenQuerySession.can_search_assessments_taken

   .. automethod:: AssessmentTakenQuerySession.use_federated_bank_view

   .. automethod:: AssessmentTakenQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentTakenQuerySession.assessment_taken_query

   .. automethod:: AssessmentTakenQuerySession.get_assessments_taken_by_query



Assessment Taken Admin Methods
------------------------------

   .. autoattribute:: AssessmentTakenAdminSession.bank_id

   .. autoattribute:: AssessmentTakenAdminSession.bank

   .. automethod:: AssessmentTakenAdminSession.can_create_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.can_create_assessment_taken_with_record_types

   .. automethod:: AssessmentTakenAdminSession.get_assessment_taken_form_for_create

   .. automethod:: AssessmentTakenAdminSession.create_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_update_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.get_assessment_taken_form_for_update

   .. automethod:: AssessmentTakenAdminSession.update_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_delete_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.delete_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_manage_assessment_taken_aliases

   .. automethod:: AssessmentTakenAdminSession.alias_assessment_taken



Bank Query
----------

.. autoclass:: BankQuery
   :show-inheritance:

   .. automethod:: BankQuery.match_item_id

   .. autoattribute:: BankQuery.item_id_terms

   .. automethod:: BankQuery.supports_item_query

   .. autoattribute:: BankQuery.item_query

   .. automethod:: BankQuery.match_any_item

   .. autoattribute:: BankQuery.item_terms

   .. automethod:: BankQuery.match_assessment_id

   .. autoattribute:: BankQuery.assessment_id_terms

   .. automethod:: BankQuery.supports_assessment_query

   .. autoattribute:: BankQuery.assessment_query

   .. automethod:: BankQuery.match_any_assessment

   .. autoattribute:: BankQuery.assessment_terms

   .. automethod:: BankQuery.match_assessment_offered_id

   .. autoattribute:: BankQuery.assessment_offered_id_terms

   .. automethod:: BankQuery.supports_assessment_offered_query

   .. autoattribute:: BankQuery.assessment_offered_query

   .. automethod:: BankQuery.match_any_assessment_offered

   .. autoattribute:: BankQuery.assessment_offered_terms

   .. automethod:: BankQuery.match_ancestor_bank_id

   .. autoattribute:: BankQuery.ancestor_bank_id_terms

   .. automethod:: BankQuery.supports_ancestor_bank_query

   .. autoattribute:: BankQuery.ancestor_bank_query

   .. automethod:: BankQuery.match_any_ancestor_bank

   .. autoattribute:: BankQuery.ancestor_bank_terms

   .. automethod:: BankQuery.match_descendant_bank_id

   .. autoattribute:: BankQuery.descendant_bank_id_terms

   .. automethod:: BankQuery.supports_descendant_bank_query

   .. autoattribute:: BankQuery.descendant_bank_query

   .. automethod:: BankQuery.match_any_descendant_bank

   .. autoattribute:: BankQuery.descendant_bank_terms

   .. automethod:: BankQuery.get_bank_query_record



Item Bank Methods
-----------------

   .. automethod:: ItemBankSession.can_lookup_item_bank_mappings

   .. automethod:: ItemBankSession.use_comparative_bank_view

   .. automethod:: ItemBankSession.use_plenary_bank_view

   .. automethod:: ItemBankSession.get_item_ids_by_bank

   .. automethod:: ItemBankSession.get_items_by_bank

   .. automethod:: ItemBankSession.get_item_ids_by_banks

   .. automethod:: ItemBankSession.get_items_by_banks

   .. automethod:: ItemBankSession.get_bank_ids_by_item

   .. automethod:: ItemBankSession.get_banks_by_item



Item Bank Assignment Methods
----------------------------

   .. automethod:: ItemBankAssignmentSession.can_assign_items

   .. automethod:: ItemBankAssignmentSession.can_assign_items_to_bank

   .. automethod:: ItemBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: ItemBankAssignmentSession.get_assignable_bank_ids_for_item

   .. automethod:: ItemBankAssignmentSession.assign_item_to_bank

   .. automethod:: ItemBankAssignmentSession.unassign_item_from_bank

   .. automethod:: ItemBankAssignmentSession.reassign_item_to_billing



Assessment Bank Methods
-----------------------

   .. automethod:: AssessmentBankSession.can_lookup_assessment_bank_mappings

   .. automethod:: AssessmentBankSession.use_comparative_bank_view

   .. automethod:: AssessmentBankSession.use_plenary_bank_view

   .. automethod:: AssessmentBankSession.get_assessment_ids_by_bank

   .. automethod:: AssessmentBankSession.get_assessments_by_bank

   .. automethod:: AssessmentBankSession.get_assessment_ids_by_banks

   .. automethod:: AssessmentBankSession.get_assessments_by_banks

   .. automethod:: AssessmentBankSession.get_bank_ids_by_assessment

   .. automethod:: AssessmentBankSession.get_banks_by_assessment



Assessment Bank Assignment Methods
----------------------------------

   .. automethod:: AssessmentBankAssignmentSession.can_assign_assessments

   .. automethod:: AssessmentBankAssignmentSession.can_assign_assessments_to_bank

   .. automethod:: AssessmentBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentBankAssignmentSession.get_assignable_bank_ids_for_assessment

   .. automethod:: AssessmentBankAssignmentSession.assign_assessment_to_bank

   .. automethod:: AssessmentBankAssignmentSession.unassign_assessment_from_bank

   .. automethod:: AssessmentBankAssignmentSession.reassign_assessment_to_billing



Assessment Offered Bank Methods
-------------------------------

   .. automethod:: AssessmentOfferedBankSession.can_lookup_assessment_offered_bank_mappings

   .. automethod:: AssessmentOfferedBankSession.use_comparative_bank_view

   .. automethod:: AssessmentOfferedBankSession.use_plenary_bank_view

   .. automethod:: AssessmentOfferedBankSession.get_assessment_offered_ids_by_bank

   .. automethod:: AssessmentOfferedBankSession.get_assessments_offered_by_bank

   .. automethod:: AssessmentOfferedBankSession.get_assessment_offered_ids_by_banks

   .. automethod:: AssessmentOfferedBankSession.get_assessments_offered_by_banks

   .. automethod:: AssessmentOfferedBankSession.get_bank_ids_by_assessment_offered

   .. automethod:: AssessmentOfferedBankSession.get_banks_by_assessment_offered



Assessment Offered Bank Assignment Methods
------------------------------------------

   .. automethod:: AssessmentOfferedBankAssignmentSession.can_assign_assessments_offered

   .. automethod:: AssessmentOfferedBankAssignmentSession.can_assign_assessments_offered_to_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentOfferedBankAssignmentSession.get_assignable_bank_ids_for_assessment_offered

   .. automethod:: AssessmentOfferedBankAssignmentSession.assign_assessment_offered_to_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.unassign_assessment_offered_from_bank

   .. automethod:: AssessmentOfferedBankAssignmentSession.reassign_assessment_offered_to_billing



Assessment Taken Bank Methods
-----------------------------

   .. automethod:: AssessmentTakenBankSession.can_lookup_assessment_taken_bank_mappings

   .. automethod:: AssessmentTakenBankSession.use_comparative_bank_view

   .. automethod:: AssessmentTakenBankSession.use_plenary_bank_view

   .. automethod:: AssessmentTakenBankSession.get_assessment_taken_ids_by_bank

   .. automethod:: AssessmentTakenBankSession.get_assessments_taken_by_bank

   .. automethod:: AssessmentTakenBankSession.get_assessment_taken_ids_by_banks

   .. automethod:: AssessmentTakenBankSession.get_assessments_taken_by_banks

   .. automethod:: AssessmentTakenBankSession.get_bank_ids_by_assessment_taken

   .. automethod:: AssessmentTakenBankSession.get_banks_by_assessment_taken



Assessment Taken Bank Assignment Methods
----------------------------------------

   .. automethod:: AssessmentTakenBankAssignmentSession.can_assign_assessments_taken

   .. automethod:: AssessmentTakenBankAssignmentSession.can_assign_assessments_taken_to_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.get_assignable_bank_ids

   .. automethod:: AssessmentTakenBankAssignmentSession.get_assignable_bank_ids_for_assessment_taken

   .. automethod:: AssessmentTakenBankAssignmentSession.assign_assessment_taken_to_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.unassign_assessment_taken_from_bank

   .. automethod:: AssessmentTakenBankAssignmentSession.reassign_assessment_taken_to_billing



Bank Lookup Methods
-------------------

   .. automethod:: BankLookupSession.can_lookup_banks

   .. automethod:: BankLookupSession.use_comparative_bank_view

   .. automethod:: BankLookupSession.use_plenary_bank_view

   .. automethod:: BankLookupSession.get_bank

   .. automethod:: BankLookupSession.get_banks_by_ids

   .. automethod:: BankLookupSession.get_banks_by_genus_type

   .. automethod:: BankLookupSession.get_banks_by_parent_genus_type

   .. automethod:: BankLookupSession.get_banks_by_record_type

   .. automethod:: BankLookupSession.get_banks_by_provider

   .. autoattribute:: BankLookupSession.banks



Bank Query Methods
------------------

   .. automethod:: BankQuerySession.can_search_banks

   .. autoattribute:: BankQuerySession.bank_query

   .. automethod:: BankQuerySession.get_banks_by_query



Bank Admin Methods
------------------

   .. automethod:: BankAdminSession.can_create_banks

   .. automethod:: BankAdminSession.can_create_bank_with_record_types

   .. automethod:: BankAdminSession.get_bank_form_for_create

   .. automethod:: BankAdminSession.create_bank

   .. automethod:: BankAdminSession.can_update_banks

   .. automethod:: BankAdminSession.get_bank_form_for_update

   .. automethod:: BankAdminSession.update_bank

   .. automethod:: BankAdminSession.can_delete_banks

   .. automethod:: BankAdminSession.delete_bank

   .. automethod:: BankAdminSession.can_manage_bank_aliases

   .. automethod:: BankAdminSession.alias_bank



Bank Hierarchy Methods
----------------------

   .. autoattribute:: BankHierarchySession.bank_hierarchy_id

   .. autoattribute:: BankHierarchySession.bank_hierarchy

   .. automethod:: BankHierarchySession.can_access_bank_hierarchy

   .. automethod:: BankHierarchySession.use_comparative_bank_view

   .. automethod:: BankHierarchySession.use_plenary_bank_view

   .. autoattribute:: BankHierarchySession.root_bank_ids

   .. autoattribute:: BankHierarchySession.root_banks

   .. automethod:: BankHierarchySession.has_parent_banks

   .. automethod:: BankHierarchySession.is_parent_of_bank

   .. automethod:: BankHierarchySession.get_parent_bank_ids

   .. automethod:: BankHierarchySession.get_parent_banks

   .. automethod:: BankHierarchySession.is_ancestor_of_bank

   .. automethod:: BankHierarchySession.has_child_banks

   .. automethod:: BankHierarchySession.is_child_of_bank

   .. automethod:: BankHierarchySession.get_child_bank_ids

   .. automethod:: BankHierarchySession.get_child_banks

   .. automethod:: BankHierarchySession.is_descendant_of_bank

   .. automethod:: BankHierarchySession.get_bank_node_ids

   .. automethod:: BankHierarchySession.get_bank_nodes



Bank Hierarchy Design Methods
-----------------------------

   .. autoattribute:: BankHierarchyDesignSession.bank_hierarchy_id

   .. autoattribute:: BankHierarchyDesignSession.bank_hierarchy

   .. automethod:: BankHierarchyDesignSession.can_modify_bank_hierarchy

   .. automethod:: BankHierarchyDesignSession.add_root_bank

   .. automethod:: BankHierarchyDesignSession.remove_root_bank

   .. automethod:: BankHierarchyDesignSession.add_child_bank

   .. automethod:: BankHierarchyDesignSession.remove_child_bank

   .. automethod:: BankHierarchyDesignSession.remove_child_banks



Assessment Methods
------------------

   .. autoattribute:: AssessmentSession.bank_id

   .. autoattribute:: AssessmentSession.bank

   .. automethod:: AssessmentSession.can_take_assessments

   .. automethod:: AssessmentSession.has_assessment_begun

   .. automethod:: AssessmentSession.is_assessment_over

   .. automethod:: AssessmentSession.requires_synchronous_sections

   .. automethod:: AssessmentSession.get_first_assessment_section

   .. automethod:: AssessmentSession.has_next_assessment_section

   .. automethod:: AssessmentSession.get_next_assessment_section

   .. automethod:: AssessmentSession.has_previous_assessment_section

   .. automethod:: AssessmentSession.get_previous_assessment_section

   .. automethod:: AssessmentSession.get_assessment_section

   .. automethod:: AssessmentSession.get_assessment_sections

   .. automethod:: AssessmentSession.is_assessment_section_complete

   .. automethod:: AssessmentSession.get_incomplete_assessment_sections

   .. automethod:: AssessmentSession.has_assessment_section_begun

   .. automethod:: AssessmentSession.is_assessment_section_over

   .. automethod:: AssessmentSession.requires_synchronous_responses

   .. automethod:: AssessmentSession.get_first_question

   .. automethod:: AssessmentSession.has_next_question

   .. automethod:: AssessmentSession.get_next_question

   .. automethod:: AssessmentSession.has_previous_question

   .. automethod:: AssessmentSession.get_previous_question

   .. automethod:: AssessmentSession.get_question

   .. automethod:: AssessmentSession.get_questions

   .. automethod:: AssessmentSession.get_response_form

   .. automethod:: AssessmentSession.submit_response

   .. automethod:: AssessmentSession.skip_item

   .. automethod:: AssessmentSession.is_question_answered

   .. automethod:: AssessmentSession.get_unanswered_questions

   .. automethod:: AssessmentSession.has_unanswered_questions

   .. automethod:: AssessmentSession.get_first_unanswered_question

   .. automethod:: AssessmentSession.has_next_unanswered_question

   .. automethod:: AssessmentSession.get_next_unanswered_question

   .. automethod:: AssessmentSession.has_previous_unanswered_question

   .. automethod:: AssessmentSession.get_previous_unanswered_question

   .. automethod:: AssessmentSession.get_response

   .. automethod:: AssessmentSession.get_responses

   .. automethod:: AssessmentSession.clear_response

   .. automethod:: AssessmentSession.finish_assessment_section

   .. automethod:: AssessmentSession.is_answer_available

   .. automethod:: AssessmentSession.get_answers

   .. automethod:: AssessmentSession.finish_assessment



Item Lookup Methods
-------------------

   .. autoattribute:: ItemLookupSession.bank_id

   .. autoattribute:: ItemLookupSession.bank

   .. automethod:: ItemLookupSession.can_lookup_items

   .. automethod:: ItemLookupSession.use_comparative_item_view

   .. automethod:: ItemLookupSession.use_plenary_item_view

   .. automethod:: ItemLookupSession.use_federated_bank_view

   .. automethod:: ItemLookupSession.use_isolated_bank_view

   .. automethod:: ItemLookupSession.get_item

   .. automethod:: ItemLookupSession.get_items_by_ids

   .. automethod:: ItemLookupSession.get_items_by_genus_type

   .. automethod:: ItemLookupSession.get_items_by_parent_genus_type

   .. automethod:: ItemLookupSession.get_items_by_record_type

   .. automethod:: ItemLookupSession.get_items_by_question

   .. automethod:: ItemLookupSession.get_items_by_answer

   .. automethod:: ItemLookupSession.get_items_by_learning_objective

   .. automethod:: ItemLookupSession.get_items_by_learning_objectives

   .. autoattribute:: ItemLookupSession.items



Item Query Methods
------------------

   .. autoattribute:: ItemQuerySession.bank_id

   .. autoattribute:: ItemQuerySession.bank

   .. automethod:: ItemQuerySession.can_search_items

   .. automethod:: ItemQuerySession.use_federated_bank_view

   .. automethod:: ItemQuerySession.use_isolated_bank_view

   .. autoattribute:: ItemQuerySession.item_query

   .. automethod:: ItemQuerySession.get_items_by_query



Item Search Methods
-------------------

   .. autoattribute:: ItemSearchSession.item_search

   .. autoattribute:: ItemSearchSession.item_search_order

   .. automethod:: ItemSearchSession.get_items_by_search

   .. automethod:: ItemSearchSession.get_item_query_from_inspector



Item Admin Methods
------------------

   .. autoattribute:: ItemAdminSession.bank_id

   .. autoattribute:: ItemAdminSession.bank

   .. automethod:: ItemAdminSession.can_create_items

   .. automethod:: ItemAdminSession.can_create_item_with_record_types

   .. automethod:: ItemAdminSession.get_item_form_for_create

   .. automethod:: ItemAdminSession.create_item

   .. automethod:: ItemAdminSession.can_update_items

   .. automethod:: ItemAdminSession.get_item_form_for_update

   .. automethod:: ItemAdminSession.update_item

   .. automethod:: ItemAdminSession.can_delete_items

   .. automethod:: ItemAdminSession.delete_item

   .. automethod:: ItemAdminSession.can_manage_item_aliases

   .. automethod:: ItemAdminSession.alias_item

   .. automethod:: ItemAdminSession.can_create_questions

   .. automethod:: ItemAdminSession.can_create_question_with_record_types

   .. automethod:: ItemAdminSession.get_question_form_for_create

   .. automethod:: ItemAdminSession.create_question

   .. automethod:: ItemAdminSession.can_update_questions

   .. automethod:: ItemAdminSession.get_question_form_for_update

   .. automethod:: ItemAdminSession.update_question

   .. automethod:: ItemAdminSession.can_delete_questions

   .. automethod:: ItemAdminSession.delete_question

   .. automethod:: ItemAdminSession.can_create_answers

   .. automethod:: ItemAdminSession.can_create_answers_with_record_types

   .. automethod:: ItemAdminSession.get_answer_form_for_create

   .. automethod:: ItemAdminSession.create_answer

   .. automethod:: ItemAdminSession.can_update_answers

   .. automethod:: ItemAdminSession.get_answer_form_for_update

   .. automethod:: ItemAdminSession.update_answer

   .. automethod:: ItemAdminSession.can_delete_answers

   .. automethod:: ItemAdminSession.delete_answer



Item Notification Methods
-------------------------

   .. autoattribute:: ItemNotificationSession.bank_id

   .. autoattribute:: ItemNotificationSession.bank

   .. automethod:: ItemNotificationSession.can_register_for_item_notifications

   .. automethod:: ItemNotificationSession.use_federated_bank_view

   .. automethod:: ItemNotificationSession.use_isolated_bank_view

   .. automethod:: ItemNotificationSession.reliable_item_notifications

   .. automethod:: ItemNotificationSession.unreliable_item_notifications

   .. automethod:: ItemNotificationSession.acknowledge_item_notification

   .. automethod:: ItemNotificationSession.register_for_new_items

   .. automethod:: ItemNotificationSession.register_for_changed_items

   .. automethod:: ItemNotificationSession.register_for_changed_item

   .. automethod:: ItemNotificationSession.register_for_deleted_items

   .. automethod:: ItemNotificationSession.register_for_deleted_item



Assessment Lookup Methods
-------------------------

   .. autoattribute:: AssessmentLookupSession.bank_id

   .. autoattribute:: AssessmentLookupSession.bank

   .. automethod:: AssessmentLookupSession.can_lookup_assessments

   .. automethod:: AssessmentLookupSession.use_comparative_assessment_view

   .. automethod:: AssessmentLookupSession.use_plenary_assessment_view

   .. automethod:: AssessmentLookupSession.use_federated_bank_view

   .. automethod:: AssessmentLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentLookupSession.get_assessment

   .. automethod:: AssessmentLookupSession.get_assessments_by_ids

   .. automethod:: AssessmentLookupSession.get_assessments_by_genus_type

   .. automethod:: AssessmentLookupSession.get_assessments_by_parent_genus_type

   .. automethod:: AssessmentLookupSession.get_assessments_by_record_type

   .. autoattribute:: AssessmentLookupSession.assessments



Assessment Query Methods
------------------------

   .. autoattribute:: AssessmentQuerySession.bank_id

   .. autoattribute:: AssessmentQuerySession.bank

   .. automethod:: AssessmentQuerySession.can_search_assessments

   .. automethod:: AssessmentQuerySession.use_federated_bank_view

   .. automethod:: AssessmentQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentQuerySession.assessment_query

   .. automethod:: AssessmentQuerySession.get_assessments_by_query



Assessment Admin Methods
------------------------

   .. autoattribute:: AssessmentAdminSession.bank_id

   .. autoattribute:: AssessmentAdminSession.bank

   .. automethod:: AssessmentAdminSession.can_create_assessments

   .. automethod:: AssessmentAdminSession.can_create_assessment_with_record_types

   .. automethod:: AssessmentAdminSession.get_assessment_form_for_create

   .. automethod:: AssessmentAdminSession.create_assessment

   .. automethod:: AssessmentAdminSession.can_update_assessments

   .. automethod:: AssessmentAdminSession.get_assessment_form_for_update

   .. automethod:: AssessmentAdminSession.update_assessment

   .. automethod:: AssessmentAdminSession.can_delete_assessments

   .. automethod:: AssessmentAdminSession.delete_assessment

   .. automethod:: AssessmentAdminSession.can_manage_assessment_aliases

   .. automethod:: AssessmentAdminSession.alias_assessment



Assessment Basic Authoring Methods
----------------------------------

   .. autoattribute:: AssessmentBasicAuthoringSession.bank_id

   .. autoattribute:: AssessmentBasicAuthoringSession.bank

   .. automethod:: AssessmentBasicAuthoringSession.can_author_assessments

   .. automethod:: AssessmentBasicAuthoringSession.get_items

   .. automethod:: AssessmentBasicAuthoringSession.add_item

   .. automethod:: AssessmentBasicAuthoringSession.remove_item

   .. automethod:: AssessmentBasicAuthoringSession.move_item

   .. automethod:: AssessmentBasicAuthoringSession.order_items



Assessment Offered Lookup Methods
---------------------------------

   .. autoattribute:: AssessmentOfferedLookupSession.bank_id

   .. autoattribute:: AssessmentOfferedLookupSession.bank

   .. automethod:: AssessmentOfferedLookupSession.can_lookup_assessments_offered

   .. automethod:: AssessmentOfferedLookupSession.use_comparative_assessment_offered_view

   .. automethod:: AssessmentOfferedLookupSession.use_plenary_assessment_offered_view

   .. automethod:: AssessmentOfferedLookupSession.use_federated_bank_view

   .. automethod:: AssessmentOfferedLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentOfferedLookupSession.get_assessment_offered

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_ids

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_genus_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_parent_genus_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_record_type

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_by_date

   .. automethod:: AssessmentOfferedLookupSession.get_assessments_offered_for_assessment

   .. autoattribute:: AssessmentOfferedLookupSession.assessments_offered



Assessment Offered Query Methods
--------------------------------

   .. autoattribute:: AssessmentOfferedQuerySession.bank_id

   .. autoattribute:: AssessmentOfferedQuerySession.bank

   .. automethod:: AssessmentOfferedQuerySession.can_search_assessments_offered

   .. automethod:: AssessmentOfferedQuerySession.use_federated_bank_view

   .. automethod:: AssessmentOfferedQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentOfferedQuerySession.assessment_offered_query

   .. automethod:: AssessmentOfferedQuerySession.get_assessments_offered_by_query



Assessment Offered Admin Methods
--------------------------------

   .. autoattribute:: AssessmentOfferedAdminSession.bank_id

   .. autoattribute:: AssessmentOfferedAdminSession.bank

   .. automethod:: AssessmentOfferedAdminSession.can_create_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.can_create_assessment_offered_with_record_types

   .. automethod:: AssessmentOfferedAdminSession.get_assessment_offered_form_for_create

   .. automethod:: AssessmentOfferedAdminSession.create_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_update_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.get_assessment_offered_form_for_update

   .. automethod:: AssessmentOfferedAdminSession.update_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_delete_assessments_offered

   .. automethod:: AssessmentOfferedAdminSession.delete_assessment_offered

   .. automethod:: AssessmentOfferedAdminSession.can_manage_assessment_offered_aliases

   .. automethod:: AssessmentOfferedAdminSession.alias_assessment_offered



Assessment Taken Lookup Methods
-------------------------------

   .. autoattribute:: AssessmentTakenLookupSession.bank_id

   .. autoattribute:: AssessmentTakenLookupSession.bank

   .. automethod:: AssessmentTakenLookupSession.can_lookup_assessments_taken

   .. automethod:: AssessmentTakenLookupSession.use_comparative_assessment_taken_view

   .. automethod:: AssessmentTakenLookupSession.use_plenary_assessment_taken_view

   .. automethod:: AssessmentTakenLookupSession.use_federated_bank_view

   .. automethod:: AssessmentTakenLookupSession.use_isolated_bank_view

   .. automethod:: AssessmentTakenLookupSession.get_assessment_taken

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_ids

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_genus_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_parent_genus_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_record_type

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker_and_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker_and_assessment

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_for_taker_and_assessment_offered

   .. automethod:: AssessmentTakenLookupSession.get_assessments_taken_by_date_for_taker_and_assessment_offered

   .. autoattribute:: AssessmentTakenLookupSession.assessments_taken



Assessment Taken Query Methods
------------------------------

   .. autoattribute:: AssessmentTakenQuerySession.bank_id

   .. autoattribute:: AssessmentTakenQuerySession.bank

   .. automethod:: AssessmentTakenQuerySession.can_search_assessments_taken

   .. automethod:: AssessmentTakenQuerySession.use_federated_bank_view

   .. automethod:: AssessmentTakenQuerySession.use_isolated_bank_view

   .. autoattribute:: AssessmentTakenQuerySession.assessment_taken_query

   .. automethod:: AssessmentTakenQuerySession.get_assessments_taken_by_query



Assessment Taken Admin Methods
------------------------------

   .. autoattribute:: AssessmentTakenAdminSession.bank_id

   .. autoattribute:: AssessmentTakenAdminSession.bank

   .. automethod:: AssessmentTakenAdminSession.can_create_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.can_create_assessment_taken_with_record_types

   .. automethod:: AssessmentTakenAdminSession.get_assessment_taken_form_for_create

   .. automethod:: AssessmentTakenAdminSession.create_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_update_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.get_assessment_taken_form_for_update

   .. automethod:: AssessmentTakenAdminSession.update_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_delete_assessments_taken

   .. automethod:: AssessmentTakenAdminSession.delete_assessment_taken

   .. automethod:: AssessmentTakenAdminSession.can_manage_assessment_taken_aliases

   .. automethod:: AssessmentTakenAdminSession.alias_assessment_taken



