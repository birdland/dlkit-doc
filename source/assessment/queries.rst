.. currentmodule:: dlkit.assessment.queries
.. automodule:: dlkit.assessment.queries

Queries
=======


Question Query
--------------

.. autoclass:: QuestionQuery
   :show-inheritance:

.. automethod:: QuestionQuery.get_question_query_record



Answer Query
------------

.. autoclass:: AnswerQuery
   :show-inheritance:

.. automethod:: AnswerQuery.get_answer_query_record



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



