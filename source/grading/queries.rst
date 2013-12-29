.. currentmodule:: dlkit.abstract_osid.grading.queries
.. automodule:: dlkit.abstract_osid.grading.queries

Queries
=======


Grade Query
-----------

.. autoclass:: GradeQuery
   :show-inheritance:

.. automethod:: GradeQuery.match_grade_system_id

.. autoattribute:: GradeQuery.grade_system_id_terms

.. automethod:: GradeQuery.supports_grade_system_query

.. autoattribute:: GradeQuery.grade_system_query

.. autoattribute:: GradeQuery.grade_system_terms

.. automethod:: GradeQuery.match_input_score_start_range

.. autoattribute:: GradeQuery.input_score_start_range_terms

.. automethod:: GradeQuery.match_input_score_end_range

.. autoattribute:: GradeQuery.input_score_end_range_terms

.. automethod:: GradeQuery.match_input_score_range

.. autoattribute:: GradeQuery.input_score_range_terms

.. automethod:: GradeQuery.match_output_score

.. autoattribute:: GradeQuery.output_score_terms

.. automethod:: GradeQuery.match_grade_entry_id

.. autoattribute:: GradeQuery.grade_entry_id_terms

.. automethod:: GradeQuery.supports_grade_entry_query

.. autoattribute:: GradeQuery.grade_entry_query

.. automethod:: GradeQuery.match_any_grade_entry

.. autoattribute:: GradeQuery.grade_entry_terms

.. automethod:: GradeQuery.match_gradebook_id

.. autoattribute:: GradeQuery.gradebook_id_terms

.. automethod:: GradeQuery.supports_gradebook_query

.. autoattribute:: GradeQuery.gradebook_query

.. autoattribute:: GradeQuery.gradebook_terms

.. automethod:: GradeQuery.get_grade_query_record



Grade System Query
------------------

.. autoclass:: GradeSystemQuery
   :show-inheritance:

.. automethod:: GradeSystemQuery.match_grade_based_systems

.. autoattribute:: GradeSystemQuery.grade_based_terms

.. automethod:: GradeSystemQuery.match_grade_id

.. autoattribute:: GradeSystemQuery.grade_id_terms

.. automethod:: GradeSystemQuery.supports_grade_query

.. autoattribute:: GradeSystemQuery.grade_query

.. automethod:: GradeSystemQuery.match_any_grade

.. autoattribute:: GradeSystemQuery.grade_terms

.. automethod:: GradeSystemQuery.match_lowest_numeric_score

.. autoattribute:: GradeSystemQuery.lowest_numeric_score_terms

.. automethod:: GradeSystemQuery.match_numeric_score_increment

.. autoattribute:: GradeSystemQuery.numeric_score_increment_terms

.. automethod:: GradeSystemQuery.match_highest_numeric_score

.. autoattribute:: GradeSystemQuery.highest_numeric_score_terms

.. automethod:: GradeSystemQuery.match_gradebook_column_id

.. autoattribute:: GradeSystemQuery.gradebook_column_id_terms

.. automethod:: GradeSystemQuery.supports_gradebook_column_query

.. autoattribute:: GradeSystemQuery.gradebook_column_query

.. automethod:: GradeSystemQuery.match_any_gradebook_column

.. autoattribute:: GradeSystemQuery.gradebook_column_terms

.. automethod:: GradeSystemQuery.match_gradebook_id

.. autoattribute:: GradeSystemQuery.gradebook_id_terms

.. automethod:: GradeSystemQuery.supports_gradebook_query

.. autoattribute:: GradeSystemQuery.gradebook_query

.. autoattribute:: GradeSystemQuery.gradebook_terms

.. automethod:: GradeSystemQuery.get_grade_system_query_record



Grade Entry Query
-----------------

.. autoclass:: GradeEntryQuery
   :show-inheritance:

.. automethod:: GradeEntryQuery.match_gradebook_column_id

.. autoattribute:: GradeEntryQuery.gradebook_column_id_terms

.. automethod:: GradeEntryQuery.supports_gradebook_column_query

.. autoattribute:: GradeEntryQuery.gradebook_column_query

.. autoattribute:: GradeEntryQuery.gradebook_column_terms

.. automethod:: GradeEntryQuery.match_key_resource_id

.. autoattribute:: GradeEntryQuery.key_resource_id_terms

.. automethod:: GradeEntryQuery.supports_key_resource_query

.. autoattribute:: GradeEntryQuery.key_resource_query

.. automethod:: GradeEntryQuery.match_any_key_resource

.. autoattribute:: GradeEntryQuery.key_resource_terms

.. automethod:: GradeEntryQuery.match_derived

.. autoattribute:: GradeEntryQuery.derived_terms

.. automethod:: GradeEntryQuery.match_overridden_grade_entry_id

.. autoattribute:: GradeEntryQuery.overridden_grade_entry_id_terms

.. automethod:: GradeEntryQuery.supports_overridden_grade_entry_query

.. autoattribute:: GradeEntryQuery.overridden_grade_entry_query

.. automethod:: GradeEntryQuery.match_any_overridden_grade_entry

.. autoattribute:: GradeEntryQuery.overridden_grade_entry_terms

.. automethod:: GradeEntryQuery.match_ignored_for_calculation_entries

.. autoattribute:: GradeEntryQuery.ignored_for_calculation_terms

.. automethod:: GradeEntryQuery.match_grade_id

.. autoattribute:: GradeEntryQuery.grade_id_terms

.. automethod:: GradeEntryQuery.supports_grade_query

.. autoattribute:: GradeEntryQuery.grade_query

.. automethod:: GradeEntryQuery.match_any_grade

.. autoattribute:: GradeEntryQuery.grade_terms

.. automethod:: GradeEntryQuery.match_score

.. automethod:: GradeEntryQuery.match_any_score

.. autoattribute:: GradeEntryQuery.score_terms

.. automethod:: GradeEntryQuery.match_time_graded

.. autoattribute:: GradeEntryQuery.time_graded_terms

.. automethod:: GradeEntryQuery.match_grader_id

.. autoattribute:: GradeEntryQuery.grader_id_terms

.. automethod:: GradeEntryQuery.supports_grader_query

.. autoattribute:: GradeEntryQuery.grader_query

.. automethod:: GradeEntryQuery.match_any_grader

.. autoattribute:: GradeEntryQuery.grader_terms

.. automethod:: GradeEntryQuery.match_grading_agent_id

.. autoattribute:: GradeEntryQuery.grading_agent_id_terms

.. automethod:: GradeEntryQuery.supports_grading_agent_query

.. autoattribute:: GradeEntryQuery.grading_agent_query

.. automethod:: GradeEntryQuery.match_any_grading_agent

.. autoattribute:: GradeEntryQuery.grading_agent_terms

.. automethod:: GradeEntryQuery.match_gradebook_id

.. autoattribute:: GradeEntryQuery.gradebook_id_terms

.. automethod:: GradeEntryQuery.supports_gradebook_query

.. autoattribute:: GradeEntryQuery.gradebook_query

.. autoattribute:: GradeEntryQuery.gradebook_terms

.. automethod:: GradeEntryQuery.get_grade_entry_query_record



Gradebook Column Query
----------------------

.. autoclass:: GradebookColumnQuery
   :show-inheritance:

.. automethod:: GradebookColumnQuery.match_grade_system_id

.. autoattribute:: GradebookColumnQuery.grade_system_id_terms

.. automethod:: GradebookColumnQuery.supports_grade_system_query

.. autoattribute:: GradebookColumnQuery.grade_system_query

.. automethod:: GradebookColumnQuery.match_any_grade_system

.. autoattribute:: GradebookColumnQuery.grade_system_terms

.. automethod:: GradebookColumnQuery.match_grade_entry_id

.. autoattribute:: GradebookColumnQuery.grade_entry_id_terms

.. automethod:: GradebookColumnQuery.supports_grade_entry_query

.. autoattribute:: GradebookColumnQuery.grade_entry_query

.. automethod:: GradebookColumnQuery.match_any_grade_entry

.. autoattribute:: GradebookColumnQuery.grade_entry_terms

.. automethod:: GradebookColumnQuery.supports_gradebook_column_summary_query

.. autoattribute:: GradebookColumnQuery.gradebook_column_summary_query

.. autoattribute:: GradebookColumnQuery.gradebook_column_summary_terms

.. automethod:: GradebookColumnQuery.match_gradebook_id

.. autoattribute:: GradebookColumnQuery.gradebook_id_terms

.. automethod:: GradebookColumnQuery.supports_gradebook_query

.. autoattribute:: GradebookColumnQuery.gradebook_query

.. autoattribute:: GradebookColumnQuery.gradebook_terms

.. automethod:: GradebookColumnQuery.get_gradebook_column_query_record



Gradebook Column Summary Query
------------------------------

.. autoclass:: GradebookColumnSummaryQuery
   :show-inheritance:

.. automethod:: GradebookColumnSummaryQuery.match_gradebook_column_id

.. autoattribute:: GradebookColumnSummaryQuery.gradebook_column_id_terms

.. automethod:: GradebookColumnSummaryQuery.supports_gradebook_column_query

.. autoattribute:: GradebookColumnSummaryQuery.gradebook_column_query

.. automethod:: GradebookColumnSummaryQuery.match_any_gradebook_column

.. autoattribute:: GradebookColumnSummaryQuery.gradebook_column_terms

.. automethod:: GradebookColumnSummaryQuery.match_mean

.. autoattribute:: GradebookColumnSummaryQuery.mean_terms

.. automethod:: GradebookColumnSummaryQuery.match_minimum_mean

.. autoattribute:: GradebookColumnSummaryQuery.minimum_mean_terms

.. automethod:: GradebookColumnSummaryQuery.match_median

.. autoattribute:: GradebookColumnSummaryQuery.median_terms

.. automethod:: GradebookColumnSummaryQuery.match_minimum_median

.. autoattribute:: GradebookColumnSummaryQuery.minimum_median_terms

.. automethod:: GradebookColumnSummaryQuery.match_mode

.. autoattribute:: GradebookColumnSummaryQuery.mode_terms

.. automethod:: GradebookColumnSummaryQuery.match_minimum_mode

.. autoattribute:: GradebookColumnSummaryQuery.minimum_mode_terms

.. automethod:: GradebookColumnSummaryQuery.match_rms

.. autoattribute:: GradebookColumnSummaryQuery.rms_terms

.. automethod:: GradebookColumnSummaryQuery.match_minimum_rms

.. autoattribute:: GradebookColumnSummaryQuery.minimum_rms_terms

.. automethod:: GradebookColumnSummaryQuery.match_standard_deviation

.. autoattribute:: GradebookColumnSummaryQuery.standard_deviation_terms

.. automethod:: GradebookColumnSummaryQuery.match_minimum_standard_deviation

.. autoattribute:: GradebookColumnSummaryQuery.minimum_standard_deviation_terms

.. automethod:: GradebookColumnSummaryQuery.match_sum

.. autoattribute:: GradebookColumnSummaryQuery.sum_terms

.. automethod:: GradebookColumnSummaryQuery.match_minimum_sum

.. autoattribute:: GradebookColumnSummaryQuery.minimum_sum_terms

.. automethod:: GradebookColumnSummaryQuery.match_gradebook_id

.. autoattribute:: GradebookColumnSummaryQuery.gradebook_id_terms

.. automethod:: GradebookColumnSummaryQuery.supports_gradebook_query

.. autoattribute:: GradebookColumnSummaryQuery.gradebook_query

.. autoattribute:: GradebookColumnSummaryQuery.gradebook_terms

.. automethod:: GradebookColumnSummaryQuery.get_gradebook_column_summary_query_record



Gradebook Query
---------------

.. autoclass:: GradebookQuery
   :show-inheritance:

.. automethod:: GradebookQuery.match_grade_system_id

.. autoattribute:: GradebookQuery.grade_system_id_terms

.. automethod:: GradebookQuery.supports_grade_system_query

.. autoattribute:: GradebookQuery.grade_system_query

.. automethod:: GradebookQuery.match_any_grade_system_query

.. autoattribute:: GradebookQuery.grade_system_terms

.. automethod:: GradebookQuery.match_grade_entry_id

.. autoattribute:: GradebookQuery.grade_entry_id_terms

.. automethod:: GradebookQuery.supports_grade_entry_query

.. autoattribute:: GradebookQuery.grade_entry_query

.. automethod:: GradebookQuery.match_any_grade_entry_query

.. autoattribute:: GradebookQuery.grade_entry_terms

.. automethod:: GradebookQuery.match_gradebook_column_id

.. autoattribute:: GradebookQuery.gradebook_column_id_terms

.. automethod:: GradebookQuery.supports_gradebook_column_query

.. autoattribute:: GradebookQuery.gradebook_column_query

.. automethod:: GradebookQuery.match_any_gradebook_column

.. autoattribute:: GradebookQuery.gradebook_column_terms

.. automethod:: GradebookQuery.match_ancestor_gradebook_id

.. autoattribute:: GradebookQuery.ancestor_gradebook_id_terms

.. automethod:: GradebookQuery.supports_ancestor_gradebook_query

.. autoattribute:: GradebookQuery.ancestor_gradebook_query

.. automethod:: GradebookQuery.match_any_ancestor_gradebook

.. autoattribute:: GradebookQuery.ancestor_gradebook_terms

.. automethod:: GradebookQuery.match_descendant_gradebook_id

.. autoattribute:: GradebookQuery.descendant_gradebook_id_terms

.. automethod:: GradebookQuery.supports_descendant_gradebook_query

.. autoattribute:: GradebookQuery.descendant_gradebook_query

.. automethod:: GradebookQuery.match_any_descendant_gradebook

.. autoattribute:: GradebookQuery.descendant_gradebook_terms

.. automethod:: GradebookQuery.get_gradebook_query_record



