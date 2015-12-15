

Queries
=======


Grade Query
-----------

.. py:class:: GradeQuery(abc_grading_queries.GradeQuery, osid_queries.OsidObjectQuery, osid_queries.OsidSubjugateableQuery)
    This is the query for searching gradings.


    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.





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


    .. py:method:: clear_grade_system_terms():
        :noindex:


    .. py:attribute:: grade_system_terms
        :noindex:


    .. py:method:: match_input_score_start_range(start, end, match):
        :noindex:


    .. py:method:: clear_input_score_start_range_terms():
        :noindex:


    .. py:attribute:: input_score_start_range_terms
        :noindex:


    .. py:method:: match_input_score_end_range(start, end, match):
        :noindex:


    .. py:method:: clear_input_score_end_range_terms():
        :noindex:


    .. py:attribute:: input_score_end_range_terms
        :noindex:


    .. py:method:: match_input_score(start, end, match):
        :noindex:


    .. py:method:: clear_input_score_terms():
        :noindex:


    .. py:attribute:: input_score_terms
        :noindex:


    .. py:method:: match_output_score(start, end, match):
        :noindex:


    .. py:method:: clear_output_score_terms():
        :noindex:


    .. py:attribute:: output_score_terms
        :noindex:


    .. py:method:: match_grade_entry_id(grade_entry_id, match):
        :noindex:


    .. py:method:: clear_grade_entry_id_terms():
        :noindex:


    .. py:attribute:: grade_entry_id_terms
        :noindex:


    .. py:method:: supports_grade_entry_query():
        :noindex:


    .. py:method:: get_grade_entry_query():
        :noindex:


    .. py:attribute:: grade_entry_query
        :noindex:


    .. py:method:: match_any_grade_entry(match):
        :noindex:


    .. py:method:: clear_grade_entry_terms():
        :noindex:


    .. py:attribute:: grade_entry_terms
        :noindex:


    .. py:method:: match_gradebook_id(gradebook_id, match):
        :noindex:


    .. py:method:: clear_gradebook_id_terms():
        :noindex:


    .. py:attribute:: gradebook_id_terms
        :noindex:


    .. py:method:: supports_gradebook_query():
        :noindex:


    .. py:method:: get_gradebook_query():
        :noindex:


    .. py:attribute:: gradebook_query
        :noindex:


    .. py:method:: clear_gradebook_terms():
        :noindex:


    .. py:attribute:: gradebook_terms
        :noindex:


    .. py:method:: get_grade_query_record(grade_record_type):
        :noindex:


Grade System Query
------------------

.. py:class:: GradeSystemQuery(abc_grading_queries.GradeSystemQuery, osid_queries.OsidObjectQuery, osid_queries.OsidAggregateableQuery)
    This is the query for searching grade systems.


    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.





    .. py:method:: match_based_on_grades(match):
        :noindex:


    .. py:method:: clear_based_on_grades_terms():
        :noindex:


    .. py:attribute:: based_on_grades_terms
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


    .. py:method:: match_lowest_numeric_score(start, end, match):
        :noindex:


    .. py:method:: clear_lowest_numeric_score_terms():
        :noindex:


    .. py:attribute:: lowest_numeric_score_terms
        :noindex:


    .. py:method:: match_numeric_score_increment(start, end, match):
        :noindex:


    .. py:method:: clear_numeric_score_increment_terms():
        :noindex:


    .. py:attribute:: numeric_score_increment_terms
        :noindex:


    .. py:method:: match_highest_numeric_score(start, end, match):
        :noindex:


    .. py:method:: clear_highest_numeric_score_terms():
        :noindex:


    .. py:attribute:: highest_numeric_score_terms
        :noindex:


    .. py:method:: match_gradebook_column_id(gradebook_column_id, match):
        :noindex:


    .. py:method:: clear_gradebook_column_id_terms():
        :noindex:


    .. py:attribute:: gradebook_column_id_terms
        :noindex:


    .. py:method:: supports_gradebook_column_query():
        :noindex:


    .. py:method:: get_gradebook_column_query():
        :noindex:


    .. py:attribute:: gradebook_column_query
        :noindex:


    .. py:method:: match_any_gradebook_column(match):
        :noindex:


    .. py:method:: clear_gradebook_column_terms():
        :noindex:


    .. py:attribute:: gradebook_column_terms
        :noindex:


    .. py:method:: match_gradebook_id(gradebook_id, match):
        :noindex:


    .. py:method:: clear_gradebook_id_terms():
        :noindex:


    .. py:attribute:: gradebook_id_terms
        :noindex:


    .. py:method:: supports_gradebook_query():
        :noindex:


    .. py:method:: get_gradebook_query():
        :noindex:


    .. py:attribute:: gradebook_query
        :noindex:


    .. py:method:: clear_gradebook_terms():
        :noindex:


    .. py:attribute:: gradebook_terms
        :noindex:


    .. py:method:: get_grade_system_query_record(grade_system_record_type):
        :noindex:


Grade Entry Query
-----------------

.. py:class:: GradeEntryQuery(abc_grading_queries.GradeEntryQuery, osid_queries.OsidRelationshipQuery)
    This is the query for searching grade entries.


    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.





    .. py:method:: match_gradebook_column_id(gradebook_column_id, match):
        :noindex:


    .. py:method:: clear_gradebook_column_id_terms():
        :noindex:


    .. py:attribute:: gradebook_column_id_terms
        :noindex:


    .. py:method:: supports_gradebook_column_query():
        :noindex:


    .. py:method:: get_gradebook_column_query():
        :noindex:


    .. py:attribute:: gradebook_column_query
        :noindex:


    .. py:method:: clear_gradebook_column_terms():
        :noindex:


    .. py:attribute:: gradebook_column_terms
        :noindex:


    .. py:method:: match_key_resource_id(resource_id, match):
        :noindex:


    .. py:method:: clear_key_resource_id_terms():
        :noindex:


    .. py:attribute:: key_resource_id_terms
        :noindex:


    .. py:method:: supports_key_resource_query():
        :noindex:


    .. py:method:: get_key_resource_query():
        :noindex:


    .. py:attribute:: key_resource_query
        :noindex:


    .. py:method:: match_any_key_resource(match):
        :noindex:


    .. py:method:: clear_key_resource_terms():
        :noindex:


    .. py:attribute:: key_resource_terms
        :noindex:


    .. py:method:: match_derived(match):
        :noindex:


    .. py:method:: clear_derived_terms():
        :noindex:


    .. py:attribute:: derived_terms
        :noindex:


    .. py:method:: match_overridden_grade_entry_id(grade_entry_id, match):
        :noindex:


    .. py:method:: clear_overridden_grade_entry_id_terms():
        :noindex:


    .. py:attribute:: overridden_grade_entry_id_terms
        :noindex:


    .. py:method:: supports_overridden_grade_entry_query():
        :noindex:


    .. py:method:: get_overridden_grade_entry_query():
        :noindex:


    .. py:attribute:: overridden_grade_entry_query
        :noindex:


    .. py:method:: match_any_overridden_grade_entry(match):
        :noindex:


    .. py:method:: clear_overridden_grade_entry_terms():
        :noindex:


    .. py:attribute:: overridden_grade_entry_terms
        :noindex:


    .. py:method:: match_ignored_for_calculations(match):
        :noindex:


    .. py:method:: clear_ignored_for_calculations_terms():
        :noindex:


    .. py:attribute:: ignored_for_calculations_terms
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


    .. py:method:: match_score(start, end, match):
        :noindex:


    .. py:method:: match_any_score(match):
        :noindex:


    .. py:method:: clear_score_terms():
        :noindex:


    .. py:attribute:: score_terms
        :noindex:


    .. py:method:: match_time_graded(start, end, match):
        :noindex:


    .. py:method:: clear_time_graded_terms():
        :noindex:


    .. py:attribute:: time_graded_terms
        :noindex:


    .. py:method:: match_grader_id(resource_id, match):
        :noindex:


    .. py:method:: clear_grader_id_terms():
        :noindex:


    .. py:attribute:: grader_id_terms
        :noindex:


    .. py:method:: supports_grader_query():
        :noindex:


    .. py:method:: get_grader_query():
        :noindex:


    .. py:attribute:: grader_query
        :noindex:


    .. py:method:: match_any_grader(match):
        :noindex:


    .. py:method:: clear_grader_terms():
        :noindex:


    .. py:attribute:: grader_terms
        :noindex:


    .. py:method:: match_grading_agent_id(agent_id, match):
        :noindex:


    .. py:method:: clear_grading_agent_id_terms():
        :noindex:


    .. py:attribute:: grading_agent_id_terms
        :noindex:


    .. py:method:: supports_grading_agent_query():
        :noindex:


    .. py:method:: get_grading_agent_query():
        :noindex:


    .. py:attribute:: grading_agent_query
        :noindex:


    .. py:method:: match_any_grading_agent(match):
        :noindex:


    .. py:method:: clear_grading_agent_terms():
        :noindex:


    .. py:attribute:: grading_agent_terms
        :noindex:


    .. py:method:: match_gradebook_id(gradebook_id, match):
        :noindex:


    .. py:method:: clear_gradebook_id_terms():
        :noindex:


    .. py:attribute:: gradebook_id_terms
        :noindex:


    .. py:method:: supports_gradebook_query():
        :noindex:


    .. py:method:: get_gradebook_query():
        :noindex:


    .. py:attribute:: gradebook_query
        :noindex:


    .. py:method:: clear_gradebook_terms():
        :noindex:


    .. py:attribute:: gradebook_terms
        :noindex:


    .. py:method:: get_grade_entry_query_record(grade_entry_record_type):
        :noindex:


Gradebook Column Query
----------------------

.. py:class:: GradebookColumnQuery(abc_grading_queries.GradebookColumnQuery, osid_queries.OsidObjectQuery)
    This is the query for searching gradings.


    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.





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


    .. py:method:: match_grade_entry_id(grade_entry_id, match):
        :noindex:


    .. py:method:: clear_grade_entry_id_terms():
        :noindex:


    .. py:attribute:: grade_entry_id_terms
        :noindex:


    .. py:method:: supports_grade_entry_query():
        :noindex:


    .. py:method:: get_grade_entry_query():
        :noindex:


    .. py:attribute:: grade_entry_query
        :noindex:


    .. py:method:: match_any_grade_entry(match):
        :noindex:


    .. py:method:: clear_grade_entry_terms():
        :noindex:


    .. py:attribute:: grade_entry_terms
        :noindex:


    .. py:method:: supports_gradebook_column_summary_query():
        :noindex:


    .. py:method:: get_gradebook_column_summary_query():
        :noindex:


    .. py:attribute:: gradebook_column_summary_query
        :noindex:


    .. py:method:: clear_gradebook_column_summary_terms():
        :noindex:


    .. py:attribute:: gradebook_column_summary_terms
        :noindex:


    .. py:method:: match_gradebook_id(gradebook_id, match):
        :noindex:


    .. py:method:: clear_gradebook_id_terms():
        :noindex:


    .. py:attribute:: gradebook_id_terms
        :noindex:


    .. py:method:: supports_gradebook_query():
        :noindex:


    .. py:method:: get_gradebook_query():
        :noindex:


    .. py:attribute:: gradebook_query
        :noindex:


    .. py:method:: clear_gradebook_terms():
        :noindex:


    .. py:attribute:: gradebook_terms
        :noindex:


    .. py:method:: get_gradebook_column_query_record(gradebook_column_record_type):
        :noindex:


Gradebook Column Summary Query
------------------------------

.. py:class:: GradebookColumnSummaryQuery(abc_grading_queries.GradebookColumnSummaryQuery, osid_queries.OsidRuleQuery)
    This is the query for searching gradebook column summaries.


    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.





    .. py:method:: match_gradebook_column_id(gradebook_column_id, match):
        :noindex:


    .. py:method:: clear_gradebook_column_id_terms():
        :noindex:


    .. py:attribute:: gradebook_column_id_terms
        :noindex:


    .. py:method:: supports_gradebook_column_query():
        :noindex:


    .. py:method:: get_gradebook_column_query():
        :noindex:


    .. py:attribute:: gradebook_column_query
        :noindex:


    .. py:method:: match_any_gradebook_column(match):
        :noindex:


    .. py:method:: clear_gradebook_column_terms():
        :noindex:


    .. py:attribute:: gradebook_column_terms
        :noindex:


    .. py:method:: match_mean(low, high, match):
        :noindex:


    .. py:method:: clear_mean_terms():
        :noindex:


    .. py:attribute:: mean_terms
        :noindex:


    .. py:method:: match_minimum_mean(value, match):
        :noindex:


    .. py:method:: clear_minimum_mean_terms():
        :noindex:


    .. py:attribute:: minimum_mean_terms
        :noindex:


    .. py:method:: match_median(low, high, match):
        :noindex:


    .. py:method:: clear_median_terms():
        :noindex:


    .. py:attribute:: median_terms
        :noindex:


    .. py:method:: match_minimum_median(value, match):
        :noindex:


    .. py:method:: clear_minimum_median_terms():
        :noindex:


    .. py:attribute:: minimum_median_terms
        :noindex:


    .. py:method:: match_mode(low, high, match):
        :noindex:


    .. py:method:: clear_mode_terms():
        :noindex:


    .. py:attribute:: mode_terms
        :noindex:


    .. py:method:: match_minimum_mode(value, match):
        :noindex:


    .. py:method:: clear_minimum_mode_terms():
        :noindex:


    .. py:attribute:: minimum_mode_terms
        :noindex:


    .. py:method:: match_rms(low, high, match):
        :noindex:


    .. py:method:: clear_rms_terms():
        :noindex:


    .. py:attribute:: rms_terms
        :noindex:


    .. py:method:: match_minimum_rms(value, match):
        :noindex:


    .. py:method:: clear_minimum_rms_terms():
        :noindex:


    .. py:attribute:: minimum_rms_terms
        :noindex:


    .. py:method:: match_standard_deviation(low, high, match):
        :noindex:


    .. py:method:: clear_standard_deviation_terms():
        :noindex:


    .. py:attribute:: standard_deviation_terms
        :noindex:


    .. py:method:: match_minimum_standard_deviation(value, match):
        :noindex:


    .. py:method:: clear_minimum_standard_deviation_terms():
        :noindex:


    .. py:attribute:: minimum_standard_deviation_terms
        :noindex:


    .. py:method:: match_sum(low, high, match):
        :noindex:


    .. py:method:: clear_sum_terms():
        :noindex:


    .. py:attribute:: sum_terms
        :noindex:


    .. py:method:: match_minimum_sum(value, match):
        :noindex:


    .. py:method:: clear_minimum_sum_terms():
        :noindex:


    .. py:attribute:: minimum_sum_terms
        :noindex:


    .. py:method:: match_gradebook_id(gradebook_id, match):
        :noindex:


    .. py:method:: clear_gradebook_id_terms():
        :noindex:


    .. py:attribute:: gradebook_id_terms
        :noindex:


    .. py:method:: supports_gradebook_query():
        :noindex:


    .. py:method:: get_gradebook_query():
        :noindex:


    .. py:attribute:: gradebook_query
        :noindex:


    .. py:method:: clear_gradebook_terms():
        :noindex:


    .. py:attribute:: gradebook_terms
        :noindex:


    .. py:method:: get_gradebook_column_summary_query_record(gradebook_column_summary_record_type):
        :noindex:


Gradebook Query
---------------

.. py:class:: GradebookQuery(abc_grading_queries.GradebookQuery, osid_queries.OsidCatalogQuery)
    This is the query for searching gradebooks.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.





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


    .. py:method:: match_grade_entry_id(grade_entry_id, match):
        :noindex:


    .. py:method:: clear_grade_entry_id_terms():
        :noindex:


    .. py:attribute:: grade_entry_id_terms
        :noindex:


    .. py:method:: supports_grade_entry_query():
        :noindex:


    .. py:method:: get_grade_entry_query():
        :noindex:


    .. py:attribute:: grade_entry_query
        :noindex:


    .. py:method:: match_any_grade_entry(match):
        :noindex:


    .. py:method:: clear_grade_entry_terms():
        :noindex:


    .. py:attribute:: grade_entry_terms
        :noindex:


    .. py:method:: match_gradebook_column_id(gradebook_column_id, match):
        :noindex:


    .. py:method:: clear_gradebook_column_id_terms():
        :noindex:


    .. py:attribute:: gradebook_column_id_terms
        :noindex:


    .. py:method:: supports_gradebook_column_query():
        :noindex:


    .. py:method:: get_gradebook_column_query():
        :noindex:


    .. py:attribute:: gradebook_column_query
        :noindex:


    .. py:method:: match_any_gradebook_column(match):
        :noindex:


    .. py:method:: clear_gradebook_column_terms():
        :noindex:


    .. py:attribute:: gradebook_column_terms
        :noindex:


    .. py:method:: match_ancestor_gradebook_id(gradebook_id, match):
        :noindex:


    .. py:method:: clear_ancestor_gradebook_id_terms():
        :noindex:


    .. py:attribute:: ancestor_gradebook_id_terms
        :noindex:


    .. py:method:: supports_ancestor_gradebook_query():
        :noindex:


    .. py:method:: get_ancestor_gradebook_query():
        :noindex:


    .. py:attribute:: ancestor_gradebook_query
        :noindex:


    .. py:method:: match_any_ancestor_gradebook(match):
        :noindex:


    .. py:method:: clear_ancestor_gradebook_terms():
        :noindex:


    .. py:attribute:: ancestor_gradebook_terms
        :noindex:


    .. py:method:: match_descendant_gradebook_id(gradebook_id, match):
        :noindex:


    .. py:method:: clear_descendant_gradebook_id_terms():
        :noindex:


    .. py:attribute:: descendant_gradebook_id_terms
        :noindex:


    .. py:method:: supports_descendant_gradebook_query():
        :noindex:


    .. py:method:: get_descendant_gradebook_query():
        :noindex:


    .. py:attribute:: descendant_gradebook_query
        :noindex:


    .. py:method:: match_any_descendant_gradebook(match):
        :noindex:


    .. py:method:: clear_descendant_gradebook_terms():
        :noindex:


    .. py:attribute:: descendant_gradebook_terms
        :noindex:


    .. py:method:: get_gradebook_query_record(gradebook_record_type):
        :noindex:


