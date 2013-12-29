.. currentmodule:: dlkit.grading.query_inspectors
.. automodule:: dlkit.grading.query_inspectors

Query_Inspectors
================


Grade Query Inspector
---------------------

.. autoclass:: GradeQueryInspector
   :show-inheritance:

.. autoattribute:: GradeQueryInspector.grade_system_id_terms

.. autoattribute:: GradeQueryInspector.grade_system_terms

.. autoattribute:: GradeQueryInspector.input_score_start_range_terms

.. autoattribute:: GradeQueryInspector.input_score_end_range_terms

.. autoattribute:: GradeQueryInspector.ouput_score_terms

.. autoattribute:: GradeQueryInspector.grade_entry_id_terms

.. autoattribute:: GradeQueryInspector.grade_entry_terms

.. autoattribute:: GradeQueryInspector.gradebook_id_terms

.. autoattribute:: GradeQueryInspector.gradebook_terms

.. automethod:: GradeQueryInspector.get_grade_query_inspector_record



Grade System Query Inspector
----------------------------

.. autoclass:: GradeSystemQueryInspector
   :show-inheritance:

.. autoattribute:: GradeSystemQueryInspector.grade_based_systems_terms

.. autoattribute:: GradeSystemQueryInspector.grade_id_terms

.. autoattribute:: GradeSystemQueryInspector.grade_terms

.. autoattribute:: GradeSystemQueryInspector.score_terms

.. autoattribute:: GradeSystemQueryInspector.lowest_numeric_score_terms

.. autoattribute:: GradeSystemQueryInspector.numeric_score_increment_terms

.. autoattribute:: GradeSystemQueryInspector.highest_numeric_score_terms

.. autoattribute:: GradeSystemQueryInspector.gradebook_column_id_terms

.. autoattribute:: GradeSystemQueryInspector.gradebook_column_terms

.. autoattribute:: GradeSystemQueryInspector.gradebook_id_terms

.. autoattribute:: GradeSystemQueryInspector.gradebook_terms

.. automethod:: GradeSystemQueryInspector.get_grade_system_query_inspector_record



Grade Entry Query Inspector
---------------------------

.. autoclass:: GradeEntryQueryInspector
   :show-inheritance:

.. autoattribute:: GradeEntryQueryInspector.gradebook_column_id_terms

.. autoattribute:: GradeEntryQueryInspector.gradebook_column_terms

.. autoattribute:: GradeEntryQueryInspector.key_resource_id_terms

.. autoattribute:: GradeEntryQueryInspector.key_resource_terms

.. autoattribute:: GradeEntryQueryInspector.derived_terms

.. autoattribute:: GradeEntryQueryInspector.overridden_grade_entry_id_terms

.. autoattribute:: GradeEntryQueryInspector.overridden_grade_entry_terms

.. autoattribute:: GradeEntryQueryInspector.ignored_for_calculation_terms

.. autoattribute:: GradeEntryQueryInspector.grade_id_terms

.. autoattribute:: GradeEntryQueryInspector.grade_terms

.. autoattribute:: GradeEntryQueryInspector.score_terms

.. autoattribute:: GradeEntryQueryInspector.time_graded_terms

.. autoattribute:: GradeEntryQueryInspector.grader_id_terms

.. autoattribute:: GradeEntryQueryInspector.grader_terms

.. autoattribute:: GradeEntryQueryInspector.grading_agent_id_terms

.. autoattribute:: GradeEntryQueryInspector.grading_agent_terms

.. autoattribute:: GradeEntryQueryInspector.gradebook_id_terms

.. autoattribute:: GradeEntryQueryInspector.gradebook_terms

.. automethod:: GradeEntryQueryInspector.get_grade_entry_query_inspector_record



Gradebook Column Query Inspector
--------------------------------

.. autoclass:: GradebookColumnQueryInspector
   :show-inheritance:

.. autoattribute:: GradebookColumnQueryInspector.grade_system_id_terms

.. autoattribute:: GradebookColumnQueryInspector.grade_system_terms

.. autoattribute:: GradebookColumnQueryInspector.grade_entry_id_terms

.. autoattribute:: GradebookColumnQueryInspector.grade_entry_terms

.. autoattribute:: GradebookColumnQueryInspector.gradebook_column_summary_terms

.. autoattribute:: GradebookColumnQueryInspector.gradebook_id_terms

.. autoattribute:: GradebookColumnQueryInspector.gradebook_terms

.. automethod:: GradebookColumnQueryInspector.get_gradebook_column_query_inspector_record



Gradebook Column Summary Query Inspector
----------------------------------------

.. autoclass:: GradebookColumnSummaryQueryInspector
   :show-inheritance:

.. autoattribute:: GradebookColumnSummaryQueryInspector.gradebook_column_id_terms

.. autoattribute:: GradebookColumnSummaryQueryInspector.gradebook_column_terms

.. autoattribute:: GradebookColumnSummaryQueryInspector.mean_terms

.. autoattribute:: GradebookColumnSummaryQueryInspector.minimum_mean_terms

.. autoattribute:: GradebookColumnSummaryQueryInspector.median_terms

.. autoattribute:: GradebookColumnSummaryQueryInspector.minimum_median_terms

.. autoattribute:: GradebookColumnSummaryQueryInspector.mode_terms

.. autoattribute:: GradebookColumnSummaryQueryInspector.minimum_mode_terms

.. autoattribute:: GradebookColumnSummaryQueryInspector.rms_terms

.. autoattribute:: GradebookColumnSummaryQueryInspector.minimum_rms_terms

.. autoattribute:: GradebookColumnSummaryQueryInspector.standard_deviation_terms

.. autoattribute:: GradebookColumnSummaryQueryInspector.minimum_standard_deviation_terms

.. autoattribute:: GradebookColumnSummaryQueryInspector.sum_terms

.. autoattribute:: GradebookColumnSummaryQueryInspector.minimum_sum_terms

.. autoattribute:: GradebookColumnSummaryQueryInspector.gradebook_id_terms

.. autoattribute:: GradebookColumnSummaryQueryInspector.gradebook_terms

.. automethod:: GradebookColumnSummaryQueryInspector.get_gradebook_column_summary_query_inspector_record



Gradebook Query Inspector
-------------------------

.. autoclass:: GradebookQueryInspector
   :show-inheritance:

.. autoattribute:: GradebookQueryInspector.grade_system_id_terms

.. autoattribute:: GradebookQueryInspector.grade_system_terms

.. autoattribute:: GradebookQueryInspector.grade_entry_id_terms

.. autoattribute:: GradebookQueryInspector.grade_entry_terms

.. autoattribute:: GradebookQueryInspector.gradebook_column_id_terms

.. autoattribute:: GradebookQueryInspector.gradebook_column_terms

.. autoattribute:: GradebookQueryInspector.ancestor_gradebook_id_terms

.. autoattribute:: GradebookQueryInspector.ancestor_gradebook_terms

.. autoattribute:: GradebookQueryInspector.descendant_gradebook_id_terms

.. autoattribute:: GradebookQueryInspector.descendant_gradebook_terms

.. automethod:: GradebookQueryInspector.get_gradebook_query_inspector_record



