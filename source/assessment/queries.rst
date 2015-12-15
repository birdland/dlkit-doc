

Queries
=======


Question Query
--------------

.. py:class:: QuestionQuery(abc_assessment_queries.QuestionQuery, osid_queries.OsidObjectQuery)
    This is the query for searching questions.


    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.





    .. py:method:: get_question_query_record(question_record_type):
        :noindex:


Answer Query
------------

.. py:class:: AnswerQuery(abc_assessment_queries.AnswerQuery, osid_queries.OsidObjectQuery)
    This is the query for searching answers.


    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.





    .. py:method:: get_answer_query_record(answer_record_type):
        :noindex:


Item Query
----------

.. py:class:: ItemQuery(abc_assessment_queries.ItemQuery, osid_queries.OsidObjectQuery, osid_queries.OsidAggregateableQuery)
    This is the query for searching items.


    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.





    .. py:method:: match_learning_objective_id(objective_id, match):
        :noindex:


    .. py:method:: clear_learning_objective_id_terms():
        :noindex:


    .. py:attribute:: learning_objective_id_terms
        :noindex:


    .. py:method:: supports_learning_objective_query():
        :noindex:


    .. py:method:: get_learning_objective_query():
        :noindex:


    .. py:attribute:: learning_objective_query
        :noindex:


    .. py:method:: match_any_learning_objective(match):
        :noindex:


    .. py:method:: clear_learning_objective_terms():
        :noindex:


    .. py:attribute:: learning_objective_terms
        :noindex:


    .. py:method:: match_question_id(question_id, match):
        :noindex:


    .. py:method:: clear_question_id_terms():
        :noindex:


    .. py:attribute:: question_id_terms
        :noindex:


    .. py:method:: supports_question_query():
        :noindex:


    .. py:method:: get_question_query():
        :noindex:


    .. py:attribute:: question_query
        :noindex:


    .. py:method:: match_any_question(match):
        :noindex:


    .. py:method:: clear_question_terms():
        :noindex:


    .. py:attribute:: question_terms
        :noindex:


    .. py:method:: match_answer_id(answer_id, match):
        :noindex:


    .. py:method:: clear_answer_id_terms():
        :noindex:


    .. py:attribute:: answer_id_terms
        :noindex:


    .. py:method:: supports_answer_query():
        :noindex:


    .. py:method:: get_answer_query():
        :noindex:


    .. py:attribute:: answer_query
        :noindex:


    .. py:method:: match_any_answer(match):
        :noindex:


    .. py:method:: clear_answer_terms():
        :noindex:


    .. py:attribute:: answer_terms
        :noindex:


    .. py:method:: match_assessment_id(assessment_id, match):
        :noindex:


    .. py:method:: clear_assessment_id_terms():
        :noindex:


    .. py:attribute:: assessment_id_terms
        :noindex:


    .. py:method:: supports_assessment_query():
        :noindex:


    .. py:method:: get_assessment_query():
        :noindex:


    .. py:attribute:: assessment_query
        :noindex:


    .. py:method:: match_any_assessment(match):
        :noindex:


    .. py:method:: clear_assessment_terms():
        :noindex:


    .. py:attribute:: assessment_terms
        :noindex:


    .. py:method:: match_bank_id(bank_id, match):
        :noindex:


    .. py:method:: clear_bank_id_terms():
        :noindex:


    .. py:attribute:: bank_id_terms
        :noindex:


    .. py:method:: supports_bank_query():
        :noindex:


    .. py:method:: get_bank_query():
        :noindex:


    .. py:attribute:: bank_query
        :noindex:


    .. py:method:: clear_bank_terms():
        :noindex:


    .. py:attribute:: bank_terms
        :noindex:


    .. py:method:: get_item_query_record(item_record_type):
        :noindex:


Assessment Query
----------------

.. py:class:: AssessmentQuery(abc_assessment_queries.AssessmentQuery, osid_queries.OsidObjectQuery)
    This is the query for searching assessments.


    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.





    .. py:method:: match_level_id(grade_id, match):
        :noindex:


    .. py:method:: clear_level_id_terms():
        :noindex:


    .. py:attribute:: level_id_terms
        :noindex:


    .. py:method:: supports_level_query():
        :noindex:


    .. py:method:: get_level_query():
        :noindex:


    .. py:attribute:: level_query
        :noindex:


    .. py:method:: match_any_level(match):
        :noindex:


    .. py:method:: clear_level_terms():
        :noindex:


    .. py:attribute:: level_terms
        :noindex:


    .. py:method:: match_rubric_id(assessment_id, match):
        :noindex:


    .. py:method:: clear_rubric_id_terms():
        :noindex:


    .. py:attribute:: rubric_id_terms
        :noindex:


    .. py:method:: supports_rubric_query():
        :noindex:


    .. py:method:: get_rubric_query():
        :noindex:


    .. py:attribute:: rubric_query
        :noindex:


    .. py:method:: match_any_rubric(match):
        :noindex:


    .. py:method:: clear_rubric_terms():
        :noindex:


    .. py:attribute:: rubric_terms
        :noindex:


    .. py:method:: match_item_id(item_id, match):
        :noindex:


    .. py:method:: clear_item_id_terms():
        :noindex:


    .. py:attribute:: item_id_terms
        :noindex:


    .. py:method:: supports_item_query():
        :noindex:


    .. py:method:: get_item_query():
        :noindex:


    .. py:attribute:: item_query
        :noindex:


    .. py:method:: match_any_item(match):
        :noindex:


    .. py:method:: clear_item_terms():
        :noindex:


    .. py:attribute:: item_terms
        :noindex:


    .. py:method:: match_assessment_offered_id(assessment_offered_id, match):
        :noindex:


    .. py:method:: clear_assessment_offered_id_terms():
        :noindex:


    .. py:attribute:: assessment_offered_id_terms
        :noindex:


    .. py:method:: supports_assessment_offered_query():
        :noindex:


    .. py:method:: get_assessment_offered_query():
        :noindex:


    .. py:attribute:: assessment_offered_query
        :noindex:


    .. py:method:: match_any_assessment_offered(match):
        :noindex:


    .. py:method:: clear_assessment_offered_terms():
        :noindex:


    .. py:attribute:: assessment_offered_terms
        :noindex:


    .. py:method:: match_assessment_taken_id(assessment_taken_id, match):
        :noindex:


    .. py:method:: clear_assessment_taken_id_terms():
        :noindex:


    .. py:attribute:: assessment_taken_id_terms
        :noindex:


    .. py:method:: supports_assessment_taken_query():
        :noindex:


    .. py:method:: get_assessment_taken_query():
        :noindex:


    .. py:attribute:: assessment_taken_query
        :noindex:


    .. py:method:: match_any_assessment_taken(match):
        :noindex:


    .. py:method:: clear_assessment_taken_terms():
        :noindex:


    .. py:attribute:: assessment_taken_terms
        :noindex:


    .. py:method:: match_bank_id(bank_id, match):
        :noindex:


    .. py:method:: clear_bank_id_terms():
        :noindex:


    .. py:attribute:: bank_id_terms
        :noindex:


    .. py:method:: supports_bank_query():
        :noindex:


    .. py:method:: get_bank_query():
        :noindex:


    .. py:attribute:: bank_query
        :noindex:


    .. py:method:: clear_bank_terms():
        :noindex:


    .. py:attribute:: bank_terms
        :noindex:


    .. py:method:: get_assessment_query_record(assessment_record_type):
        :noindex:


Assessment Offered Query
------------------------

.. py:class:: AssessmentOfferedQuery(abc_assessment_queries.AssessmentOfferedQuery, osid_queries.OsidObjectQuery, osid_queries.OsidSubjugateableQuery)
    This is the query for searching assessments.


    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.





    .. py:method:: match_assessment_id(assessment_id, match):
        :noindex:


    .. py:method:: clear_assessment_id_terms():
        :noindex:


    .. py:attribute:: assessment_id_terms
        :noindex:


    .. py:method:: supports_assessment_query():
        :noindex:


    .. py:method:: get_assessment_query():
        :noindex:


    .. py:attribute:: assessment_query
        :noindex:


    .. py:method:: clear_assessment_terms():
        :noindex:


    .. py:attribute:: assessment_terms
        :noindex:


    .. py:method:: match_level_id(grade_id, match):
        :noindex:


    .. py:method:: clear_level_id_terms():
        :noindex:


    .. py:attribute:: level_id_terms
        :noindex:


    .. py:method:: supports_level_query():
        :noindex:


    .. py:method:: get_level_query():
        :noindex:


    .. py:attribute:: level_query
        :noindex:


    .. py:method:: match_any_level(match):
        :noindex:


    .. py:method:: clear_level_terms():
        :noindex:


    .. py:attribute:: level_terms
        :noindex:


    .. py:method:: match_items_sequential(match):
        :noindex:


    .. py:method:: clear_items_sequential_terms():
        :noindex:


    .. py:attribute:: items_sequential_terms
        :noindex:


    .. py:method:: match_items_shuffled(match):
        :noindex:


    .. py:method:: clear_items_shuffled_terms():
        :noindex:


    .. py:attribute:: items_shuffled_terms
        :noindex:


    .. py:method:: match_start_time(start, end, match):
        :noindex:


    .. py:method:: match_any_start_time(match):
        :noindex:


    .. py:method:: clear_start_time_terms():
        :noindex:


    .. py:attribute:: start_time_terms
        :noindex:


    .. py:method:: match_deadline(start, end, match):
        :noindex:


    .. py:method:: match_any_deadline(match):
        :noindex:


    .. py:method:: clear_deadline_terms():
        :noindex:


    .. py:attribute:: deadline_terms
        :noindex:


    .. py:method:: match_duration(low, high, match):
        :noindex:


    .. py:method:: match_any_duration(match):
        :noindex:


    .. py:method:: clear_duration_terms():
        :noindex:


    .. py:attribute:: duration_terms
        :noindex:


    .. py:method:: match_score_system_id(grade_system_id, match):
        :noindex:


    .. py:method:: clear_score_system_id_terms():
        :noindex:


    .. py:attribute:: score_system_id_terms
        :noindex:


    .. py:method:: supports_score_system_query():
        :noindex:


    .. py:method:: get_score_system_query():
        :noindex:


    .. py:attribute:: score_system_query
        :noindex:


    .. py:method:: match_any_score_system(match):
        :noindex:


    .. py:method:: clear_score_system_terms():
        :noindex:


    .. py:attribute:: score_system_terms
        :noindex:


    .. py:method:: match_grade_system_id(grade_system_id, match):
        :noindex:


    .. py:method:: clear_grade_system_id_terms():
        :noindex:


    .. py:attribute:: grade_system_id_terms
        :noindex:


    .. py:method:: supports_grade_system_query():
        :noindex:


    .. py:method:: get_grade_system_query():
        :noindex:


    .. py:attribute:: grade_system_query
        :noindex:


    .. py:method:: match_any_grade_system(match):
        :noindex:


    .. py:method:: clear_grade_system_terms():
        :noindex:


    .. py:attribute:: grade_system_terms
        :noindex:


    .. py:method:: match_rubric_id(assessment_offered_id, match):
        :noindex:


    .. py:method:: clear_rubric_id_terms():
        :noindex:


    .. py:attribute:: rubric_id_terms
        :noindex:


    .. py:method:: supports_rubric_query():
        :noindex:


    .. py:method:: get_rubric_query():
        :noindex:


    .. py:attribute:: rubric_query
        :noindex:


    .. py:method:: match_any_rubric(match):
        :noindex:


    .. py:method:: clear_rubric_terms():
        :noindex:


    .. py:attribute:: rubric_terms
        :noindex:


    .. py:method:: match_assessment_taken_id(assessment_taken_id, match):
        :noindex:


    .. py:method:: clear_assessment_taken_id_terms():
        :noindex:


    .. py:attribute:: assessment_taken_id_terms
        :noindex:


    .. py:method:: supports_assessment_taken_query():
        :noindex:


    .. py:method:: get_assessment_taken_query():
        :noindex:


    .. py:attribute:: assessment_taken_query
        :noindex:


    .. py:method:: match_any_assessment_taken(match):
        :noindex:


    .. py:method:: clear_assessment_taken_terms():
        :noindex:


    .. py:attribute:: assessment_taken_terms
        :noindex:


    .. py:method:: match_bank_id(bank_id, match):
        :noindex:


    .. py:method:: clear_bank_id_terms():
        :noindex:


    .. py:attribute:: bank_id_terms
        :noindex:


    .. py:method:: supports_bank_query():
        :noindex:


    .. py:method:: get_bank_query():
        :noindex:


    .. py:attribute:: bank_query
        :noindex:


    .. py:method:: clear_bank_terms():
        :noindex:


    .. py:attribute:: bank_terms
        :noindex:


    .. py:method:: get_assessment_offered_query_record(assessment_offered_record_type):
        :noindex:


Assessment Taken Query
----------------------

.. py:class:: AssessmentTakenQuery(abc_assessment_queries.AssessmentTakenQuery, osid_queries.OsidObjectQuery)
    This is the query for searching assessments.


    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.





    .. py:method:: match_assessment_offered_id(assessment_offered_id, match):
        :noindex:


    .. py:method:: clear_assessment_offered_id_terms():
        :noindex:


    .. py:attribute:: assessment_offered_id_terms
        :noindex:


    .. py:method:: supports_assessment_offered_query():
        :noindex:


    .. py:method:: get_assessment_offered_query():
        :noindex:


    .. py:attribute:: assessment_offered_query
        :noindex:


    .. py:method:: clear_assessment_offered_terms():
        :noindex:


    .. py:attribute:: assessment_offered_terms
        :noindex:


    .. py:method:: match_taker_id(resource_id, match):
        :noindex:


    .. py:method:: clear_taker_id_terms():
        :noindex:


    .. py:attribute:: taker_id_terms
        :noindex:


    .. py:method:: supports_taker_query():
        :noindex:


    .. py:method:: get_taker_query():
        :noindex:


    .. py:attribute:: taker_query
        :noindex:


    .. py:method:: clear_taker_terms():
        :noindex:


    .. py:attribute:: taker_terms
        :noindex:


    .. py:method:: match_taking_agent_id(agent_id, match):
        :noindex:


    .. py:method:: clear_taking_agent_id_terms():
        :noindex:


    .. py:attribute:: taking_agent_id_terms
        :noindex:


    .. py:method:: supports_taking_agent_query():
        :noindex:


    .. py:method:: get_taking_agent_query():
        :noindex:


    .. py:attribute:: taking_agent_query
        :noindex:


    .. py:method:: clear_taking_agent_terms():
        :noindex:


    .. py:attribute:: taking_agent_terms
        :noindex:


    .. py:method:: match_actual_start_time(start, end, match):
        :noindex:


    .. py:method:: match_any_actual_start_time(match):
        :noindex:


    .. py:method:: clear_actual_start_time_terms():
        :noindex:


    .. py:attribute:: actual_start_time_terms
        :noindex:


    .. py:method:: match_completion_time(start, end, match):
        :noindex:


    .. py:method:: match_any_completion_time(match):
        :noindex:


    .. py:method:: clear_completion_time_terms():
        :noindex:


    .. py:attribute:: completion_time_terms
        :noindex:


    .. py:method:: match_time_spent(low, high, match):
        :noindex:


    .. py:method:: clear_time_spent_terms():
        :noindex:


    .. py:attribute:: time_spent_terms
        :noindex:


    .. py:method:: match_score_system_id(grade_system_id, match):
        :noindex:


    .. py:method:: clear_score_system_id_terms():
        :noindex:


    .. py:attribute:: score_system_id_terms
        :noindex:


    .. py:method:: supports_score_system_query():
        :noindex:


    .. py:method:: get_score_system_query():
        :noindex:


    .. py:attribute:: score_system_query
        :noindex:


    .. py:method:: match_any_score_system(match):
        :noindex:


    .. py:method:: clear_score_system_terms():
        :noindex:


    .. py:attribute:: score_system_terms
        :noindex:


    .. py:method:: match_score(low, high, match):
        :noindex:


    .. py:method:: match_any_score(match):
        :noindex:


    .. py:method:: clear_score_terms():
        :noindex:


    .. py:attribute:: score_terms
        :noindex:


    .. py:method:: match_grade_id(grade_id, match):
        :noindex:


    .. py:method:: clear_grade_id_terms():
        :noindex:


    .. py:attribute:: grade_id_terms
        :noindex:


    .. py:method:: supports_grade_query():
        :noindex:


    .. py:method:: get_grade_query():
        :noindex:


    .. py:attribute:: grade_query
        :noindex:


    .. py:method:: match_any_grade(match):
        :noindex:


    .. py:method:: clear_grade_terms():
        :noindex:


    .. py:attribute:: grade_terms
        :noindex:


    .. py:method:: match_feedback(comments, string_match_type, match):
        :noindex:


    .. py:method:: match_any_feedback(match):
        :noindex:


    .. py:method:: clear_feedback_terms():
        :noindex:


    .. py:attribute:: feedback_terms
        :noindex:


    .. py:method:: match_rubric_id(assessment_taken_id, match):
        :noindex:


    .. py:method:: clear_rubric_id_terms():
        :noindex:


    .. py:attribute:: rubric_id_terms
        :noindex:


    .. py:method:: supports_rubric_query():
        :noindex:


    .. py:method:: get_rubric_query():
        :noindex:


    .. py:attribute:: rubric_query
        :noindex:


    .. py:method:: match_any_rubric(match):
        :noindex:


    .. py:method:: clear_rubric_terms():
        :noindex:


    .. py:attribute:: rubric_terms
        :noindex:


    .. py:method:: match_bank_id(bank_id, match):
        :noindex:


    .. py:method:: clear_bank_id_terms():
        :noindex:


    .. py:attribute:: bank_id_terms
        :noindex:


    .. py:method:: supports_bank_query():
        :noindex:


    .. py:method:: get_bank_query():
        :noindex:


    .. py:attribute:: bank_query
        :noindex:


    .. py:method:: clear_bank_terms():
        :noindex:


    .. py:attribute:: bank_terms
        :noindex:


    .. py:method:: get_assessment_taken_query_record(assessment_taken_record_type):
        :noindex:


Bank Query
----------

.. py:class:: BankQuery(abc_assessment_queries.BankQuery, osid_queries.OsidCatalogQuery)
    This is the query for searching banks Each method specifies an ``AND`` term while multiple
    invocations of the same method produce a nested ``OR``.

    .. py:method:: match_item_id(item_id, match):
        :noindex:


    .. py:method:: clear_item_id_terms():
        :noindex:


    .. py:attribute:: item_id_terms
        :noindex:


    .. py:method:: supports_item_query():
        :noindex:


    .. py:method:: get_item_query():
        :noindex:


    .. py:attribute:: item_query
        :noindex:


    .. py:method:: match_any_item(match):
        :noindex:


    .. py:method:: clear_item_terms():
        :noindex:


    .. py:attribute:: item_terms
        :noindex:


    .. py:method:: match_assessment_id(assessment_id, match):
        :noindex:


    .. py:method:: clear_assessment_id_terms():
        :noindex:


    .. py:attribute:: assessment_id_terms
        :noindex:


    .. py:method:: supports_assessment_query():
        :noindex:


    .. py:method:: get_assessment_query():
        :noindex:


    .. py:attribute:: assessment_query
        :noindex:


    .. py:method:: match_any_assessment(match):
        :noindex:


    .. py:method:: clear_assessment_terms():
        :noindex:


    .. py:attribute:: assessment_terms
        :noindex:


    .. py:method:: match_assessment_offered_id(assessment_offered_id, match):
        :noindex:


    .. py:method:: clear_assessment_offered_id_terms():
        :noindex:


    .. py:attribute:: assessment_offered_id_terms
        :noindex:


    .. py:method:: supports_assessment_offered_query():
        :noindex:


    .. py:method:: get_assessment_offered_query():
        :noindex:


    .. py:attribute:: assessment_offered_query
        :noindex:


    .. py:method:: match_any_assessment_offered(match):
        :noindex:


    .. py:method:: clear_assessment_offered_terms():
        :noindex:


    .. py:attribute:: assessment_offered_terms
        :noindex:


    .. py:method:: match_ancestor_bank_id(bank_id, match):
        :noindex:


    .. py:method:: clear_ancestor_bank_id_terms():
        :noindex:


    .. py:attribute:: ancestor_bank_id_terms
        :noindex:


    .. py:method:: supports_ancestor_bank_query():
        :noindex:


    .. py:method:: get_ancestor_bank_query():
        :noindex:


    .. py:attribute:: ancestor_bank_query
        :noindex:


    .. py:method:: match_any_ancestor_bank(match):
        :noindex:


    .. py:method:: clear_ancestor_bank_terms():
        :noindex:


    .. py:attribute:: ancestor_bank_terms
        :noindex:


    .. py:method:: match_descendant_bank_id(bank_id, match):
        :noindex:


    .. py:method:: clear_descendant_bank_id_terms():
        :noindex:


    .. py:attribute:: descendant_bank_id_terms
        :noindex:


    .. py:method:: supports_descendant_bank_query():
        :noindex:


    .. py:method:: get_descendant_bank_query():
        :noindex:


    .. py:attribute:: descendant_bank_query
        :noindex:


    .. py:method:: match_any_descendant_bank(match):
        :noindex:


    .. py:method:: clear_descendant_bank_terms():
        :noindex:


    .. py:attribute:: descendant_bank_terms
        :noindex:


    .. py:method:: get_bank_query_record(bank_record_type):
        :noindex:


