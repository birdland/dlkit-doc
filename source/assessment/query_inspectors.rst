.. currentmodule:: dlkit.assessment.query_inspectors
.. automodule:: dlkit.assessment.query_inspectors

Query Inspectors
================


Question Query Inspector
------------------------

.. autoclass:: QuestionQueryInspector
   :show-inheritance:

   .. automethod:: QuestionQueryInspector.get_question_query_inspector_record



Answer Query Inspector
----------------------

.. autoclass:: AnswerQueryInspector
   :show-inheritance:

   .. automethod:: AnswerQueryInspector.get_answer_query_inspector_record



Item Query Inspector
--------------------

.. autoclass:: ItemQueryInspector
   :show-inheritance:

   .. autoattribute:: ItemQueryInspector.learning_objective_id_terms

   .. autoattribute:: ItemQueryInspector.learning_objective_terms

   .. autoattribute:: ItemQueryInspector.question_id_terms

   .. autoattribute:: ItemQueryInspector.question_terms

   .. autoattribute:: ItemQueryInspector.answer_id_terms

   .. autoattribute:: ItemQueryInspector.answer_terms

   .. autoattribute:: ItemQueryInspector.assessment_id_terms

   .. autoattribute:: ItemQueryInspector.assessment_terms

   .. autoattribute:: ItemQueryInspector.bank_id_terms

   .. autoattribute:: ItemQueryInspector.bank_terms

   .. automethod:: ItemQueryInspector.get_item_query_inspector_record



Assessment Query Inspector
--------------------------

.. autoclass:: AssessmentQueryInspector
   :show-inheritance:

   .. autoattribute:: AssessmentQueryInspector.level_id_terms

   .. autoattribute:: AssessmentQueryInspector.level_terms

   .. autoattribute:: AssessmentQueryInspector.rubric_id_terms

   .. autoattribute:: AssessmentQueryInspector.rubric_terms

   .. autoattribute:: AssessmentQueryInspector.item_id_terms

   .. autoattribute:: AssessmentQueryInspector.item_terms

   .. autoattribute:: AssessmentQueryInspector.assessment_offered_id_terms

   .. autoattribute:: AssessmentQueryInspector.assessment_offered_terms

   .. autoattribute:: AssessmentQueryInspector.assessment_taken_id_terms

   .. autoattribute:: AssessmentQueryInspector.assessment_taken_terms

   .. autoattribute:: AssessmentQueryInspector.bank_id_terms

   .. autoattribute:: AssessmentQueryInspector.bank_terms

   .. automethod:: AssessmentQueryInspector.get_assessment_query_inspector_record



Assessment Offered Query Inspector
----------------------------------

.. autoclass:: AssessmentOfferedQueryInspector
   :show-inheritance:

   .. autoattribute:: AssessmentOfferedQueryInspector.assessment_id_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.assessment_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.level_id_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.level_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.items_sequential_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.items_shuffled_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.start_time_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.deadline_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.duration_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.score_system_id_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.score_system_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.grade_system_id_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.grade_system_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.rubric_id_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.rubric_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.assessment_taken_id_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.assessment_taken_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.bank_id_terms

   .. autoattribute:: AssessmentOfferedQueryInspector.bank_terms

   .. automethod:: AssessmentOfferedQueryInspector.get_assessment_offered_query_inspector_record



Assessment Taken Query Inspector
--------------------------------

.. autoclass:: AssessmentTakenQueryInspector
   :show-inheritance:

   .. autoattribute:: AssessmentTakenQueryInspector.assessment_offered_id_terms

   .. autoattribute:: AssessmentTakenQueryInspector.assessment_offered_terms

   .. autoattribute:: AssessmentTakenQueryInspector.taker_id_terms

   .. autoattribute:: AssessmentTakenQueryInspector.taker_terms

   .. autoattribute:: AssessmentTakenQueryInspector.taking_agent_id_terms

   .. autoattribute:: AssessmentTakenQueryInspector.taking_agent_terms

   .. autoattribute:: AssessmentTakenQueryInspector.actual_start_time_terms

   .. autoattribute:: AssessmentTakenQueryInspector.completion_time_terms

   .. autoattribute:: AssessmentTakenQueryInspector.time_spent_terms

   .. autoattribute:: AssessmentTakenQueryInspector.score_system_id_terms

   .. autoattribute:: AssessmentTakenQueryInspector.score_system_terms

   .. autoattribute:: AssessmentTakenQueryInspector.score_terms

   .. autoattribute:: AssessmentTakenQueryInspector.grade_id_terms

   .. autoattribute:: AssessmentTakenQueryInspector.grade_terms

   .. autoattribute:: AssessmentTakenQueryInspector.feedback_terms

   .. autoattribute:: AssessmentTakenQueryInspector.rubric_id_terms

   .. autoattribute:: AssessmentTakenQueryInspector.rubric_terms

   .. autoattribute:: AssessmentTakenQueryInspector.bank_id_terms

   .. autoattribute:: AssessmentTakenQueryInspector.bank_terms

   .. automethod:: AssessmentTakenQueryInspector.get_assessment_taken_query_inspector_record



Bank Query Inspector
--------------------

.. autoclass:: BankQueryInspector
   :show-inheritance:

   .. autoattribute:: BankQueryInspector.item_id_terms

   .. autoattribute:: BankQueryInspector.item_terms

   .. autoattribute:: BankQueryInspector.assessment_id_terms

   .. autoattribute:: BankQueryInspector.assessment_terms

   .. autoattribute:: BankQueryInspector.assessment_offered_id_terms

   .. autoattribute:: BankQueryInspector.assessment_offered_terms

   .. autoattribute:: BankQueryInspector.ancestor_bank_id_terms

   .. autoattribute:: BankQueryInspector.ancestor_bank_terms

   .. autoattribute:: BankQueryInspector.descendant_bank_id_terms

   .. autoattribute:: BankQueryInspector.descendant_bank_terms

   .. automethod:: BankQueryInspector.get_bank_query_inspector_record



