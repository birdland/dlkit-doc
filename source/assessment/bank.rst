.. currentmodule:: dlkit.services.assessment
.. automodule:: dlkit.services.assessment

Bank
====


Bank
----

.. autoclass:: Bank
   :show-inheritance:

.. automethod:: Bank.get_bank_record



My Assessment Taken Methods
---------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_get_my_taken_assessments

.. automethod:: Bank.get_assessments_started_during

.. autoattribute:: Bank.assessments_started

.. automethod:: Bank.get_assessments_in_progress_during

.. autoattribute:: Bank.assessments_in_progress

.. autoattribute:: Bank.assessments_completed



Assessment Methods
------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_take_assessments

.. automethod:: Bank.has_assessment_begun

.. automethod:: Bank.is_assessment_over

.. automethod:: Bank.finished_assessment

.. automethod:: Bank.requires_synchronous_sections

.. automethod:: Bank.get_first_assessment_section

.. automethod:: Bank.has_next_assessment_section

.. automethod:: Bank.get_next_assessment_section

.. automethod:: Bank.has_previous_assessment_section

.. automethod:: Bank.get_previous_assessment_section

.. automethod:: Bank.get_assessment_section

.. automethod:: Bank.get_assessment_sections

.. automethod:: Bank.is_assessment_section_complete

.. autoattribute:: Bank.incomplete_assessment_sections

.. automethod:: Bank.has_assessment_section_begun

.. automethod:: Bank.is_assessment_section_over

.. automethod:: Bank.finished_assessment_section

.. automethod:: Bank.requires_synchronous_responses

.. autoattribute:: Bank.first_question

.. automethod:: Bank.has_next_question

.. automethod:: Bank.get_next_question

.. automethod:: Bank.has_previous_question

.. automethod:: Bank.get_previous_question

.. automethod:: Bank.get_question

.. autoattribute:: Bank.questions

.. automethod:: Bank.get_response_form

.. automethod:: Bank.submit_response

.. automethod:: Bank.skip_item

.. automethod:: Bank.is_question_answered

.. autoattribute:: Bank.unanswered_questions

.. automethod:: Bank.has_unanswered_questions

.. autoattribute:: Bank.first_unanswered_question

.. automethod:: Bank.has_next_unanswered_question

.. automethod:: Bank.get_next_unanswered_question

.. automethod:: Bank.has_previous_unanswered_question

.. automethod:: Bank.get_previous_unanswered_question

.. automethod:: Bank.get_response

.. autoattribute:: Bank.responses

.. automethod:: Bank.clear_response

.. automethod:: Bank.finish

.. automethod:: Bank.is_answer_available

.. automethod:: Bank.get_answers



Assessment Results Methods
--------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_access_assessment_results

.. automethod:: Bank.get_items

.. automethod:: Bank.get_responses

.. automethod:: Bank.are_results_available

.. automethod:: Bank.get_grade_entries



Item Lookup Methods
-------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_lookup_items

.. automethod:: Bank.use_comparative_item_view

.. automethod:: Bank.use_plenary_item_view

.. automethod:: Bank.use_federated_bank_view

.. automethod:: Bank.use_isolated_bank_view

.. automethod:: Bank.get_item

.. automethod:: Bank.get_items_by_ids

.. automethod:: Bank.get_items_by_genus_type

.. automethod:: Bank.get_items_by_parent_genus_type

.. automethod:: Bank.get_items_by_record_type

.. automethod:: Bank.get_items_by_learning_objective

.. automethod:: Bank.get_items_by_learning_objectives

.. autoattribute:: Bank.items



Item Query Methods
------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_search_items

.. automethod:: Bank.use_federated_bank_view

.. automethod:: Bank.use_isolated_bank_view

.. autoattribute:: Bank.item_query

.. automethod:: Bank.get_items_by_query



Item Search Methods
-------------------

.. autoattribute:: Bank.item_search

.. autoattribute:: Bank.item_search_order

.. automethod:: Bank.get_items_by_search

.. automethod:: Bank.get_item_query_from_inspector



Item Admin Methods
------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_create_items

.. automethod:: Bank.can_create_item_with_record_types

.. automethod:: Bank.get_item_form_for_create

.. automethod:: Bank.create_item

.. automethod:: Bank.can_update_items

.. automethod:: Bank.get_item_form_for_update

.. automethod:: Bank.update_item

.. automethod:: Bank.can_delete_items

.. automethod:: Bank.delete_item

.. automethod:: Bank.can_manage_item_aliases

.. automethod:: Bank.alias_item

.. automethod:: Bank.can_create_questions

.. automethod:: Bank.can_create_question_with_record_types

.. automethod:: Bank.get_question_form_for_create

.. automethod:: Bank.create_question

.. automethod:: Bank.can_update_questions

.. automethod:: Bank.get_question_form_for_update

.. automethod:: Bank.update_question

.. automethod:: Bank.can_delete_questions

.. automethod:: Bank.delete_question

.. automethod:: Bank.can_create_answers

.. automethod:: Bank.can_create_answers_with_record_types

.. automethod:: Bank.get_answer_form_for_create

.. automethod:: Bank.create_answer

.. automethod:: Bank.can_update_answers

.. automethod:: Bank.get_answer_form_for_update

.. automethod:: Bank.update_answer

.. automethod:: Bank.can_delete_answers

.. automethod:: Bank.delete_answer



Item Notification Methods
-------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_register_for_item_notifications

.. automethod:: Bank.use_federated_bank_view

.. automethod:: Bank.use_isolated_bank_view

.. automethod:: Bank.register_for_new_items

.. automethod:: Bank.register_for_changed_items

.. automethod:: Bank.register_for_changed_item

.. automethod:: Bank.register_for_deleted_items

.. automethod:: Bank.register_for_deleted_item



Item Bank Methods
-----------------

.. automethod:: Bank.can_lookup_item_bank_mappings

.. automethod:: Bank.use_comparative_bank_view

.. automethod:: Bank.use_plenary_bank_view

.. automethod:: Bank.get_item_ids_by_bank

.. automethod:: Bank.get_items_by_bank

.. automethod:: Bank.get_item_ids_by_banks

.. automethod:: Bank.get_items_by_banks

.. automethod:: Bank.get_bank_ids_by_item

.. automethod:: Bank.get_banks_by_item



Item Bank Assignment Methods
----------------------------

.. automethod:: Bank.can_assign_items

.. automethod:: Bank.can_assign_items_to_bank

.. automethod:: Bank.get_assignable_bank_ids

.. automethod:: Bank.get_assignable_bank_ids_for_item

.. automethod:: Bank.assign_item_to_bank

.. automethod:: Bank.unassign_item_from_bank



Item Smart Bank Methods
-----------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_manage_smart_banks

.. autoattribute:: Bank.item_query

.. autoattribute:: Bank.item_search_order

.. automethod:: Bank.apply_item_query

.. automethod:: Bank.inspect_item_query

.. automethod:: Bank.apply_item_sequencing

.. automethod:: Bank.get_item_query_from_inspector



Assessment Lookup Methods
-------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_lookup_assessments

.. automethod:: Bank.use_comparative_assessment_view

.. automethod:: Bank.use_plenary_assessment_view

.. automethod:: Bank.use_federated_bank_view

.. automethod:: Bank.use_isolated_bank_view

.. automethod:: Bank.get_assessment

.. automethod:: Bank.get_assessments_by_ids

.. automethod:: Bank.get_assessments_by_genus_type

.. automethod:: Bank.get_assessments_by_parent_genus_type

.. automethod:: Bank.get_assessments_by_record_type

.. autoattribute:: Bank.assessments



Assessment Query Methods
------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_search_assessments

.. automethod:: Bank.use_federated_bank_view

.. automethod:: Bank.use_isolated_bank_view

.. autoattribute:: Bank.assessment_query

.. automethod:: Bank.get_assessments_by_query



Assessment Search Methods
-------------------------

.. autoattribute:: Bank.assessment_search

.. autoattribute:: Bank.assessment_search_order

.. automethod:: Bank.get_assessments_by_search

.. automethod:: Bank.get_assessment_query_from_inspector



Assessment Admin Methods
------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_create_assessments

.. automethod:: Bank.can_create_assessment_with_record_types

.. automethod:: Bank.get_assessment_form_for_create

.. automethod:: Bank.create_assessment

.. automethod:: Bank.can_update_assessments

.. automethod:: Bank.get_assessment_form_for_update

.. automethod:: Bank.update_assessment

.. automethod:: Bank.can_delete_assessments

.. automethod:: Bank.delete_assessment

.. automethod:: Bank.can_manage_assessment_aliases

.. automethod:: Bank.alias_assessment



Assessment Notification Methods
-------------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_register_for_assessment_notifications

.. automethod:: Bank.use_federated_bank_view

.. automethod:: Bank.use_isolated_bank_view

.. automethod:: Bank.register_for_new_assessments

.. automethod:: Bank.register_for_changed_assessments

.. automethod:: Bank.register_for_changed_assessment

.. automethod:: Bank.register_for_deleted_assessments

.. automethod:: Bank.register_for_deleted_assessment



Assessment Bank Methods
-----------------------

.. automethod:: Bank.can_lookup_assessment_bank_mappings

.. automethod:: Bank.use_comparative_bank_view

.. automethod:: Bank.use_plenary_bank_view

.. automethod:: Bank.get_assessment_ids_by_bank

.. automethod:: Bank.get_assessments_by_bank

.. automethod:: Bank.get_assessment_ids_by_banks

.. automethod:: Bank.get_assessments_by_banks

.. automethod:: Bank.get_bank_ids_by_assessment

.. automethod:: Bank.get_banks_by_assessment



Assessment Bank Assignment Methods
----------------------------------

.. automethod:: Bank.can_assign_assessments

.. automethod:: Bank.can_assign_assessments_to_bank

.. automethod:: Bank.get_assignable_bank_ids

.. automethod:: Bank.get_assignable_bank_ids_for_assessment

.. automethod:: Bank.assign_assessment_to_bank

.. automethod:: Bank.unassign_assessment_from_bank



Assessment Smart Bank Methods
-----------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_manage_smart_banks

.. autoattribute:: Bank.assessment_query

.. autoattribute:: Bank.assessment_search_order

.. automethod:: Bank.apply_assessment_query

.. automethod:: Bank.inspect_assessment_query

.. automethod:: Bank.apply_assessment_sequencing

.. automethod:: Bank.get_assessment_query_from_inspector



Assessment Basic Authoring Methods
----------------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_author_assessment

.. automethod:: Bank.get_items

.. automethod:: Bank.add_item

.. automethod:: Bank.remove_item

.. automethod:: Bank.move_item

.. automethod:: Bank.order_items



Assessment Offered Lookup Methods
---------------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_lookup_assessments_offered

.. automethod:: Bank.use_comparative_assessment_offered_view

.. automethod:: Bank.use_plenary_assessment_offered_view

.. automethod:: Bank.use_federated_bank_view

.. automethod:: Bank.use_isolated_bank_view

.. automethod:: Bank.get_assessment_offered

.. automethod:: Bank.get_assessments_offered_by_ids

.. automethod:: Bank.get_assessments_offered_by_genus_type

.. automethod:: Bank.get_assessments_offered_by_parent_genus_type

.. automethod:: Bank.get_assessments_offered_by_record_type

.. automethod:: Bank.get_assessments_offered_by_date

.. automethod:: Bank.get_assessments_offered_for_assessment

.. autoattribute:: Bank.assessments_offered



Assessment Offered Query Methods
--------------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_search_assessments_offered

.. automethod:: Bank.use_federated_bank_view

.. automethod:: Bank.use_isolated_bank_view

.. autoattribute:: Bank.assessment_offered_query

.. automethod:: Bank.get_assessments_offered_by_query



Assessment Offered Search Methods
---------------------------------

.. autoattribute:: Bank.assessment_offered_search

.. autoattribute:: Bank.assessment_offered_search_order

.. automethod:: Bank.get_assessments_offered_by_search

.. automethod:: Bank.get_assessment_offered_query_from_inspector



Assessment Offered Admin Methods
--------------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_create_assessments_offered

.. automethod:: Bank.can_create_assessment_offered_with_record_types

.. automethod:: Bank.get_assessment_offered_form_for_create

.. automethod:: Bank.create_assessment_offered

.. automethod:: Bank.can_update_assessments_offered

.. automethod:: Bank.get_assessment_offered_form_for_update

.. automethod:: Bank.update_assessment_offered

.. automethod:: Bank.can_delete_assessments_offered

.. automethod:: Bank.delete_assessment_offered

.. automethod:: Bank.can_manage_assessment_offered_aliases

.. automethod:: Bank.alias_assessment_offered



Assessment Offered Notification Methods
---------------------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_register_for_assessment_offered_notifications

.. automethod:: Bank.use_federated_bank_view

.. automethod:: Bank.use_isolated_bank_view

.. automethod:: Bank.register_for_new_assessments_offered

.. automethod:: Bank.register_for_new_assessments_offered_for_assessment

.. automethod:: Bank.register_for_changed_assessments_offered

.. automethod:: Bank.register_for_changed_assessments_offered_for_assessment

.. automethod:: Bank.register_for_changed_assessment_offered

.. automethod:: Bank.register_for_deleted_assessments_offered

.. automethod:: Bank.register_for_deleted_assessments_offered_for_assessment

.. automethod:: Bank.register_for_deleted_assessment_offered



Assessment Offered Bank Methods
-------------------------------

.. automethod:: Bank.can_lookup_assessment_offered_bank_mappings

.. automethod:: Bank.use_comparative_bank_view

.. automethod:: Bank.use_plenary_bank_view

.. automethod:: Bank.get_assessment_offered_ids_by_bank

.. automethod:: Bank.get_assessments_offered_by_bank

.. automethod:: Bank.get_assessment_offered_ids_by_banks

.. automethod:: Bank.get_assessments_offered_by_banks

.. automethod:: Bank.get_bank_ids_by_assessment_offered

.. automethod:: Bank.get_banks_by_assessment_offered



Assessment Offered Bank Assignment Methods
------------------------------------------

.. automethod:: Bank.can_assign_assessments_offered

.. automethod:: Bank.can_assign_assessments_offered_to_bank

.. automethod:: Bank.get_assignable_bank_ids

.. automethod:: Bank.get_assignable_bank_ids_for_assessment_offered

.. automethod:: Bank.assign_assessment_offered_to_bank

.. automethod:: Bank.unassign_assessment_offered_from_bank



Assessment Offered Smart Bank Methods
-------------------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_manage_smart_banks

.. autoattribute:: Bank.assessment_offered_query

.. autoattribute:: Bank.assessment_offered_search_order

.. automethod:: Bank.apply_assessment_offered_query

.. automethod:: Bank.inspect_assessment_offered_query

.. automethod:: Bank.apply_assessment_offered_sequencing

.. automethod:: Bank.get_assessment_offered_query_from_inspector



Assessment Taken Lookup Methods
-------------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_lookup_assessments_taken

.. automethod:: Bank.use_comparative_assessment_taken_view

.. automethod:: Bank.use_plenary_assessment_taken_view

.. automethod:: Bank.use_federated_bank_view

.. automethod:: Bank.use_isolated_bank_view

.. automethod:: Bank.get_assessment_taken

.. automethod:: Bank.get_assessments_taken_by_ids

.. automethod:: Bank.get_assessments_taken_by_genus_type

.. automethod:: Bank.get_assessments_taken_by_parent_genus_type

.. automethod:: Bank.get_assessments_taken_by_record_type

.. automethod:: Bank.get_assessments_taken_by_date

.. automethod:: Bank.get_assessments_taken_for_taker

.. automethod:: Bank.get_assessments_taken_by_date_for_taker

.. automethod:: Bank.get_assessments_taken_for_assessment

.. automethod:: Bank.get_assessments_taken_by_date_for_assessment

.. automethod:: Bank.get_assessments_taken_for_taker_and_assessment

.. automethod:: Bank.get_assessments_taken_by_date_for_taker_and_assessment

.. automethod:: Bank.get_assessments_taken_for_assessment_offered

.. automethod:: Bank.get_assessments_taken_by_date_for_assessment_offered

.. automethod:: Bank.get_assessments_taken_for_taker_and_assessment_offered

.. automethod:: Bank.get_assessments_taken_by_date_for_taker_and_assessment_offered

.. autoattribute:: Bank.assessments_taken



Assessment Taken Query Methods
------------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_search_assessments_taken

.. automethod:: Bank.use_federated_bank_view

.. automethod:: Bank.use_isolated_bank_view

.. autoattribute:: Bank.assessment_taken_query

.. automethod:: Bank.get_assessments_taken_by_query



Assessment Taken Search Methods
-------------------------------

.. autoattribute:: Bank.assessment_taken_search

.. autoattribute:: Bank.assessment_taken_search_order

.. automethod:: Bank.get_assessments_taken_by_search

.. automethod:: Bank.get_assessment_taken_query_from_inspector



Assessment Taken Admin Methods
------------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_create_assessments_taken

.. automethod:: Bank.can_create_assessment_taken_with_record_types

.. automethod:: Bank.get_assessment_taken_form_for_create

.. automethod:: Bank.create_assessment_taken

.. automethod:: Bank.can_update_assessments_taken

.. automethod:: Bank.get_assessment_taken_form_for_update

.. automethod:: Bank.update_assessment_taken

.. automethod:: Bank.can_delete_assessments_taken

.. automethod:: Bank.delete_assessment_taken

.. automethod:: Bank.can_manage_assessment_taken_aliases

.. automethod:: Bank.alias_assessment_taken



Assessment Taken Notification Methods
-------------------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_register_for_assessment_taken_notifications

.. automethod:: Bank.use_federated_bank_view

.. automethod:: Bank.use_isolated_bank_view

.. automethod:: Bank.register_for_new_assessments_taken

.. automethod:: Bank.register_for_new_assessments_taken_for_taker

.. automethod:: Bank.register_for_new_assessments_taken_for_assessment_offered

.. automethod:: Bank.register_for_new_assessments_taken_for_assessment

.. automethod:: Bank.register_for_changed_assessments_taken

.. automethod:: Bank.register_for_changed_assessments_taken_for_taker

.. automethod:: Bank.register_for_changed_assessments_taken_for_assessment_offered

.. automethod:: Bank.register_for_changed_assessments_taken_for_assessment

.. automethod:: Bank.register_for_changed_assessment_taken

.. automethod:: Bank.register_for_deleted_assessments_taken

.. automethod:: Bank.register_for_deleted_assessments_taken_for_taker

.. automethod:: Bank.register_for_deleted_assessments_taken_for_assessment_offered

.. automethod:: Bank.register_for_deleted_assessments_taken_for_assessment

.. automethod:: Bank.register_for_deleted_assessment_taken



Assessment Taken Bank Methods
-----------------------------

.. automethod:: Bank.can_lookup_assessment_taken_bank_mappings

.. automethod:: Bank.use_comparative_bank_view

.. automethod:: Bank.use_plenary_bank_view

.. automethod:: Bank.get_assessment_taken_ids_by_bank

.. automethod:: Bank.get_assessments_taken_by_bank

.. automethod:: Bank.get_assessment_taken_ids_by_banks

.. automethod:: Bank.get_assessments_taken_by_banks

.. automethod:: Bank.get_bank_ids_by_assessment_taken

.. automethod:: Bank.get_banks_by_assessment_taken



Assessment Taken Bank Assignment Methods
----------------------------------------

.. automethod:: Bank.can_assign_assessments_taken

.. automethod:: Bank.can_assign_assessments_taken_to_bank

.. automethod:: Bank.get_assignable_bank_ids

.. automethod:: Bank.get_assignable_bank_ids_for_assessment_taken

.. automethod:: Bank.assign_assessment_taken_to_bank

.. automethod:: Bank.unassign_assessment_taken_from_bank



Assessment Taken Smart Bank Methods
-----------------------------------

.. autoattribute:: Bank.bank_id

.. autoattribute:: Bank.bank

.. automethod:: Bank.can_manage_smart_banks

.. autoattribute:: Bank.assessment_taken_query

.. autoattribute:: Bank.assessment_taken_search_order

.. automethod:: Bank.apply_assessment_taken_query

.. automethod:: Bank.inspect_assessment_taken_query

.. automethod:: Bank.apply_assessment_taken_sequencing

.. automethod:: Bank.get_assessment_taken_query_from_inspector


