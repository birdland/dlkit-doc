.. currentmodule:: dlkit.assessment.search_orders
.. automodule:: dlkit.assessment.search_orders

Search_Orders
=============


Question Search Order
---------------------

.. autoclass:: QuestionSearchOrder
   :show-inheritance:

   .. automethod:: QuestionSearchOrder.get_question_search_order_record



Answer Search Order
-------------------

.. autoclass:: AnswerSearchOrder
   :show-inheritance:

   .. automethod:: AnswerSearchOrder.get_answer_search_order_record



Item Search Order
-----------------

.. autoclass:: ItemSearchOrder
   :show-inheritance:

   .. automethod:: ItemSearchOrder.order_by_question

   .. automethod:: ItemSearchOrder.supports_question_search_order

   .. autoattribute:: ItemSearchOrder.question_search_order

   .. automethod:: ItemSearchOrder.get_item_search_order_record



Assessment Search Order
-----------------------

.. autoclass:: AssessmentSearchOrder
   :show-inheritance:

   .. automethod:: AssessmentSearchOrder.order_by_level

   .. automethod:: AssessmentSearchOrder.supports_level_search_order

   .. autoattribute:: AssessmentSearchOrder.level_search_order

   .. automethod:: AssessmentSearchOrder.order_by_rubric

   .. automethod:: AssessmentSearchOrder.supports_rubric_search_order

   .. autoattribute:: AssessmentSearchOrder.rubric_search_order

   .. automethod:: AssessmentSearchOrder.get_assessment_search_order_record



Assessment Offered Search Order
-------------------------------

.. autoclass:: AssessmentOfferedSearchOrder
   :show-inheritance:

   .. automethod:: AssessmentOfferedSearchOrder.order_by_assessment

   .. automethod:: AssessmentOfferedSearchOrder.supports_assessment_search_order

   .. autoattribute:: AssessmentOfferedSearchOrder.assessment_search_order

   .. automethod:: AssessmentOfferedSearchOrder.order_by_level

   .. automethod:: AssessmentOfferedSearchOrder.supports_level_search_order

   .. autoattribute:: AssessmentOfferedSearchOrder.level_search_order

   .. automethod:: AssessmentOfferedSearchOrder.order_by_items_sequential

   .. automethod:: AssessmentOfferedSearchOrder.order_by_items_shuffled

   .. automethod:: AssessmentOfferedSearchOrder.order_by_start_time

   .. automethod:: AssessmentOfferedSearchOrder.order_by_deadline

   .. automethod:: AssessmentOfferedSearchOrder.order_by_duration

   .. automethod:: AssessmentOfferedSearchOrder.order_by_score_system

   .. automethod:: AssessmentOfferedSearchOrder.supports_score_system_search_order

   .. autoattribute:: AssessmentOfferedSearchOrder.score_system_search_order

   .. automethod:: AssessmentOfferedSearchOrder.order_by_grade_system

   .. automethod:: AssessmentOfferedSearchOrder.supports_grade_system_search_order

   .. autoattribute:: AssessmentOfferedSearchOrder.grade_system_search_order

   .. automethod:: AssessmentOfferedSearchOrder.order_by_rubric

   .. automethod:: AssessmentOfferedSearchOrder.supports_rubric_search_order

   .. autoattribute:: AssessmentOfferedSearchOrder.rubric_search_order

   .. automethod:: AssessmentOfferedSearchOrder.get_assessment_offered_search_order_record



Assessment Taken Search Order
-----------------------------

.. autoclass:: AssessmentTakenSearchOrder
   :show-inheritance:

   .. automethod:: AssessmentTakenSearchOrder.order_by_assessment_offered

   .. automethod:: AssessmentTakenSearchOrder.supports_assessment_offered_search_order

   .. autoattribute:: AssessmentTakenSearchOrder.assessment_offered_search_order

   .. automethod:: AssessmentTakenSearchOrder.order_by_taker

   .. automethod:: AssessmentTakenSearchOrder.supports_taker_search_order

   .. autoattribute:: AssessmentTakenSearchOrder.taker_search_order

   .. automethod:: AssessmentTakenSearchOrder.order_by_taking_agent

   .. automethod:: AssessmentTakenSearchOrder.supports_taking_agent_search_order

   .. autoattribute:: AssessmentTakenSearchOrder.taking_agent_search_order

   .. automethod:: AssessmentTakenSearchOrder.order_by_actual_start_time

   .. automethod:: AssessmentTakenSearchOrder.order_by_completion_time

   .. automethod:: AssessmentTakenSearchOrder.order_by_time_spent

   .. automethod:: AssessmentTakenSearchOrder.order_by_score_system

   .. automethod:: AssessmentTakenSearchOrder.supports_score_system_search_order

   .. autoattribute:: AssessmentTakenSearchOrder.score_system_search_order

   .. automethod:: AssessmentTakenSearchOrder.order_by_score

   .. automethod:: AssessmentTakenSearchOrder.order_by_grade

   .. automethod:: AssessmentTakenSearchOrder.supports_grade_search_order

   .. autoattribute:: AssessmentTakenSearchOrder.grade_search_order

   .. automethod:: AssessmentTakenSearchOrder.order_by_feedback

   .. automethod:: AssessmentTakenSearchOrder.order_by_rubric

   .. automethod:: AssessmentTakenSearchOrder.supports_rubric_search_order

   .. autoattribute:: AssessmentTakenSearchOrder.rubric_search_order

   .. automethod:: AssessmentTakenSearchOrder.get_assessment_taken_search_order_record



Bank Search Order
-----------------

.. autoclass:: BankSearchOrder
   :show-inheritance:

   .. automethod:: BankSearchOrder.get_bank_search_order_record



