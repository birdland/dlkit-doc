
.. currentmodule:: dlkit.assessment.objects
.. automodule:: dlkit.assessment.objects

Objects
=======


Question
--------

.. autoclass:: Question
   :show-inheritance:

   .. automethod:: Question.get_question_record

Question Form
-------------

.. autoclass:: QuestionForm
   :show-inheritance:

   .. automethod:: QuestionForm.get_question_form_record

Question List
-------------

.. autoclass:: QuestionList
   :show-inheritance:

   .. autoattribute:: QuestionList.next_question

   .. automethod:: QuestionList.get_next_questions

Answer
------

.. autoclass:: Answer
   :show-inheritance:

   .. automethod:: Answer.get_answer_record

Answer Form
-----------

.. autoclass:: AnswerForm
   :show-inheritance:

   .. automethod:: AnswerForm.get_answer_form_record

Answer List
-----------

.. autoclass:: AnswerList
   :show-inheritance:

   .. autoattribute:: AnswerList.next_answer

   .. automethod:: AnswerList.get_next_answers

Item
----

.. autoclass:: Item
   :show-inheritance:

   .. autoattribute:: Item.learning_objective_ids

   .. autoattribute:: Item.learning_objectives

   .. autoattribute:: Item.question_id

   .. autoattribute:: Item.question

   .. autoattribute:: Item.answer_ids

   .. autoattribute:: Item.answers

   .. automethod:: Item.get_item_record

Item Form
---------

.. autoclass:: ItemForm
   :show-inheritance:

   .. autoattribute:: ItemForm.learning_objectives_metadata

   .. autoattribute:: ItemForm.learning_objectives

   .. automethod:: ItemForm.get_item_form_record

Item List
---------

.. autoclass:: ItemList
   :show-inheritance:

   .. autoattribute:: ItemList.next_item

   .. automethod:: ItemList.get_next_items

Assessment
----------

.. autoclass:: Assessment
   :show-inheritance:

   .. autoattribute:: Assessment.level_id

   .. autoattribute:: Assessment.level

   .. automethod:: Assessment.has_rubric

   .. autoattribute:: Assessment.rubric_id

   .. autoattribute:: Assessment.rubric

   .. automethod:: Assessment.get_assessment_record

Assessment Form
---------------

.. autoclass:: AssessmentForm
   :show-inheritance:

   .. autoattribute:: AssessmentForm.level_metadata

   .. autoattribute:: AssessmentForm.level

   .. autoattribute:: AssessmentForm.rubric_metadata

   .. autoattribute:: AssessmentForm.rubric

   .. automethod:: AssessmentForm.get_assessment_form_record

Assessment List
---------------

.. autoclass:: AssessmentList
   :show-inheritance:

   .. autoattribute:: AssessmentList.next_assessment

   .. automethod:: AssessmentList.get_next_assessments

Assessment Offered
------------------

.. autoclass:: AssessmentOffered
   :show-inheritance:

   .. autoattribute:: AssessmentOffered.assessment_id

   .. autoattribute:: AssessmentOffered.assessment

   .. autoattribute:: AssessmentOffered.level_id

   .. autoattribute:: AssessmentOffered.level

   .. automethod:: AssessmentOffered.are_items_sequential

   .. automethod:: AssessmentOffered.are_items_shuffled

   .. automethod:: AssessmentOffered.has_start_time

   .. autoattribute:: AssessmentOffered.start_time

   .. automethod:: AssessmentOffered.has_deadline

   .. autoattribute:: AssessmentOffered.deadline

   .. automethod:: AssessmentOffered.has_duration

   .. autoattribute:: AssessmentOffered.duration

   .. automethod:: AssessmentOffered.is_scored

   .. autoattribute:: AssessmentOffered.score_system_id

   .. autoattribute:: AssessmentOffered.score_system

   .. automethod:: AssessmentOffered.is_graded

   .. autoattribute:: AssessmentOffered.grade_system_id

   .. autoattribute:: AssessmentOffered.grade_system

   .. automethod:: AssessmentOffered.has_rubric

   .. autoattribute:: AssessmentOffered.rubric_id

   .. autoattribute:: AssessmentOffered.rubric

   .. automethod:: AssessmentOffered.get_assessment_offered_record

Assessment Offered Form
-----------------------

.. autoclass:: AssessmentOfferedForm
   :show-inheritance:

   .. autoattribute:: AssessmentOfferedForm.level_metadata

   .. autoattribute:: AssessmentOfferedForm.level

   .. autoattribute:: AssessmentOfferedForm.items_sequential_metadata

   .. autoattribute:: AssessmentOfferedForm.items_sequential

   .. autoattribute:: AssessmentOfferedForm.items_shuffled_metadata

   .. autoattribute:: AssessmentOfferedForm.items_shuffled

   .. autoattribute:: AssessmentOfferedForm.start_time_metadata

   .. autoattribute:: AssessmentOfferedForm.start_time

   .. autoattribute:: AssessmentOfferedForm.deadline_metadata

   .. autoattribute:: AssessmentOfferedForm.deadline

   .. autoattribute:: AssessmentOfferedForm.duration_metadata

   .. autoattribute:: AssessmentOfferedForm.duration

   .. autoattribute:: AssessmentOfferedForm.score_system_metadata

   .. autoattribute:: AssessmentOfferedForm.score_system

   .. autoattribute:: AssessmentOfferedForm.grade_system_metadata

   .. autoattribute:: AssessmentOfferedForm.grade_system

   .. automethod:: AssessmentOfferedForm.get_assessment_offered_form_record

Assessment Offered List
-----------------------

.. autoclass:: AssessmentOfferedList
   :show-inheritance:

   .. autoattribute:: AssessmentOfferedList.next_assessment_offered

   .. automethod:: AssessmentOfferedList.get_next_assessments_offered

Assessment Taken
----------------

.. autoclass:: AssessmentTaken
   :show-inheritance:

   .. autoattribute:: AssessmentTaken.assessment_offered_id

   .. autoattribute:: AssessmentTaken.assessment_offered

   .. autoattribute:: AssessmentTaken.taker_id

   .. autoattribute:: AssessmentTaken.taker

   .. autoattribute:: AssessmentTaken.taking_agent_id

   .. autoattribute:: AssessmentTaken.taking_agent

   .. automethod:: AssessmentTaken.has_started

   .. autoattribute:: AssessmentTaken.actual_start_time

   .. automethod:: AssessmentTaken.has_ended

   .. autoattribute:: AssessmentTaken.completion_time

   .. autoattribute:: AssessmentTaken.time_spent

   .. autoattribute:: AssessmentTaken.completion

   .. automethod:: AssessmentTaken.is_scored

   .. autoattribute:: AssessmentTaken.score_system_id

   .. autoattribute:: AssessmentTaken.score_system

   .. autoattribute:: AssessmentTaken.score

   .. automethod:: AssessmentTaken.is_graded

   .. autoattribute:: AssessmentTaken.grade_id

   .. autoattribute:: AssessmentTaken.grade

   .. autoattribute:: AssessmentTaken.feedback

   .. automethod:: AssessmentTaken.has_rubric

   .. autoattribute:: AssessmentTaken.rubric_id

   .. autoattribute:: AssessmentTaken.rubric

   .. automethod:: AssessmentTaken.get_assessment_taken_record

Assessment Taken Form
---------------------

.. autoclass:: AssessmentTakenForm
   :show-inheritance:

   .. autoattribute:: AssessmentTakenForm.taker_metadata

   .. autoattribute:: AssessmentTakenForm.taker

   .. automethod:: AssessmentTakenForm.get_assessment_taken_form_record

Assessment Taken List
---------------------

.. autoclass:: AssessmentTakenList
   :show-inheritance:

   .. autoattribute:: AssessmentTakenList.next_assessment_taken

   .. automethod:: AssessmentTakenList.get_next_assessments_taken

Assessment Section
------------------

.. autoclass:: AssessmentSection
   :show-inheritance:

   .. autoattribute:: AssessmentSection.assessment_taken_id

   .. autoattribute:: AssessmentSection.assessment_taken

   .. automethod:: AssessmentSection.has_allocated_time

   .. autoattribute:: AssessmentSection.allocated_time

   .. automethod:: AssessmentSection.are_items_sequential

   .. automethod:: AssessmentSection.are_items_shuffled

   .. automethod:: AssessmentSection.get_assessment_section_record

Assessment Section List
-----------------------

.. autoclass:: AssessmentSectionList
   :show-inheritance:

   .. autoattribute:: AssessmentSectionList.next_assessment_section

   .. automethod:: AssessmentSectionList.get_next_assessment_sections

Bank
----

.. autoclass:: Bank
   :show-inheritance:

   .. automethod:: Bank.get_bank_record

Bank Form
---------

.. autoclass:: BankForm
   :show-inheritance:

   .. automethod:: BankForm.get_bank_form_record

Bank List
---------

.. autoclass:: BankList
   :show-inheritance:

   .. autoattribute:: BankList.next_bank

   .. automethod:: BankList.get_next_banks

Bank Node
---------

.. autoclass:: BankNode
   :show-inheritance:

   .. autoattribute:: BankNode.bank

   .. autoattribute:: BankNode.parent_bank_nodes

   .. autoattribute:: BankNode.child_bank_nodes

Bank Node List
--------------

.. autoclass:: BankNodeList
   :show-inheritance:

   .. autoattribute:: BankNodeList.next_bank_node

   .. automethod:: BankNodeList.get_next_bank_nodes

Response List
-------------

.. autoclass:: ResponseList
   :show-inheritance:

   .. autoattribute:: ResponseList.next_response

   .. automethod:: ResponseList.get_next_responses

