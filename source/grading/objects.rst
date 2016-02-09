
.. currentmodule:: dlkit.grading.objects
.. automodule:: dlkit.grading.objects

Objects
=======


Grade
-----

.. autoclass:: Grade
   :show-inheritance:

   .. autoattribute:: Grade.grade_system_id

   .. autoattribute:: Grade.grade_system

   .. autoattribute:: Grade.input_score_start_range

   .. autoattribute:: Grade.input_score_end_range

   .. autoattribute:: Grade.output_score

   .. automethod:: Grade.get_grade_record

Grade Form
----------

.. autoclass:: GradeForm
   :show-inheritance:

   .. autoattribute:: GradeForm.input_score_start_range_metadata

   .. autoattribute:: GradeForm.input_score_start_range

   .. autoattribute:: GradeForm.input_score_end_range_metadata

   .. autoattribute:: GradeForm.input_score_end_range

   .. autoattribute:: GradeForm.output_score_metadata

   .. autoattribute:: GradeForm.output_score

   .. automethod:: GradeForm.get_grade_form_record

Grade List
----------

.. autoclass:: GradeList
   :show-inheritance:

   .. autoattribute:: GradeList.next_grade

   .. automethod:: GradeList.get_next_grades

Grade System
------------

.. autoclass:: GradeSystem
   :show-inheritance:

   .. automethod:: GradeSystem.is_based_on_grades

   .. autoattribute:: GradeSystem.grade_ids

   .. autoattribute:: GradeSystem.grades

   .. autoattribute:: GradeSystem.lowest_numeric_score

   .. autoattribute:: GradeSystem.numeric_score_increment

   .. autoattribute:: GradeSystem.highest_numeric_score

   .. automethod:: GradeSystem.get_grade_system_record

Grade System Form
-----------------

.. autoclass:: GradeSystemForm
   :show-inheritance:

   .. autoattribute:: GradeSystemForm.based_on_grades_metadata

   .. autoattribute:: GradeSystemForm.based_on_grades

   .. autoattribute:: GradeSystemForm.lowest_numeric_score_metadata

   .. autoattribute:: GradeSystemForm.lowest_numeric_score

   .. autoattribute:: GradeSystemForm.numeric_score_increment_metadata

   .. autoattribute:: GradeSystemForm.numeric_score_increment

   .. autoattribute:: GradeSystemForm.highest_numeric_score_metadata

   .. autoattribute:: GradeSystemForm.highest_numeric_score

   .. automethod:: GradeSystemForm.get_grade_system_form_record

Grade System List
-----------------

.. autoclass:: GradeSystemList
   :show-inheritance:

   .. autoattribute:: GradeSystemList.next_grade_system

   .. automethod:: GradeSystemList.get_next_grade_systems

Grade Entry
-----------

.. autoclass:: GradeEntry
   :show-inheritance:

   .. autoattribute:: GradeEntry.gradebook_column_id

   .. autoattribute:: GradeEntry.gradebook_column

   .. autoattribute:: GradeEntry.key_resource_id

   .. autoattribute:: GradeEntry.key_resource

   .. automethod:: GradeEntry.is_derived

   .. automethod:: GradeEntry.overrides_calculated_entry

   .. autoattribute:: GradeEntry.overridden_calculated_entry_id

   .. autoattribute:: GradeEntry.overridden_calculated_entry

   .. automethod:: GradeEntry.is_ignored_for_calculations

   .. automethod:: GradeEntry.is_graded

   .. autoattribute:: GradeEntry.grade_id

   .. autoattribute:: GradeEntry.grade

   .. autoattribute:: GradeEntry.score

   .. autoattribute:: GradeEntry.time_graded

   .. autoattribute:: GradeEntry.grader_id

   .. autoattribute:: GradeEntry.grader

   .. autoattribute:: GradeEntry.grading_agent_id

   .. autoattribute:: GradeEntry.grading_agent

   .. automethod:: GradeEntry.get_grade_entry_record

Grade Entry Form
----------------

.. autoclass:: GradeEntryForm
   :show-inheritance:

   .. autoattribute:: GradeEntryForm.ignored_for_calculations_metadata

   .. autoattribute:: GradeEntryForm.ignored_for_calculations

   .. autoattribute:: GradeEntryForm.grade_metadata

   .. autoattribute:: GradeEntryForm.grade

   .. autoattribute:: GradeEntryForm.score_metadata

   .. autoattribute:: GradeEntryForm.score

   .. automethod:: GradeEntryForm.get_grade_entry_form_record

Grade Entry List
----------------

.. autoclass:: GradeEntryList
   :show-inheritance:

   .. autoattribute:: GradeEntryList.next_grade_entry

   .. automethod:: GradeEntryList.get_next_grade_entries

Gradebook Column
----------------

.. autoclass:: GradebookColumn
   :show-inheritance:

   .. autoattribute:: GradebookColumn.grade_system_id

   .. autoattribute:: GradebookColumn.grade_system

   .. automethod:: GradebookColumn.get_gradebook_column_record

Gradebook Column Form
---------------------

.. autoclass:: GradebookColumnForm
   :show-inheritance:

   .. autoattribute:: GradebookColumnForm.grade_system_metadata

   .. autoattribute:: GradebookColumnForm.grade_system

   .. automethod:: GradebookColumnForm.get_gradebook_column_form_record

Gradebook Column List
---------------------

.. autoclass:: GradebookColumnList
   :show-inheritance:

   .. autoattribute:: GradebookColumnList.next_gradebook_column

   .. automethod:: GradebookColumnList.get_next_gradebook_columns

Gradebook Column Summary
------------------------

.. autoclass:: GradebookColumnSummary
   :show-inheritance:

   .. autoattribute:: GradebookColumnSummary.gradebook_column_id

   .. autoattribute:: GradebookColumnSummary.gradebook_column

   .. autoattribute:: GradebookColumnSummary.mean

   .. autoattribute:: GradebookColumnSummary.median

   .. autoattribute:: GradebookColumnSummary.mode

   .. autoattribute:: GradebookColumnSummary.rms

   .. autoattribute:: GradebookColumnSummary.standard_deviation

   .. autoattribute:: GradebookColumnSummary.sum

   .. automethod:: GradebookColumnSummary.get_gradebook_column_summary_record

Gradebook
---------

.. py:class:: Gradebook(abc_grading_objects.Gradebook, osid_objects.OsidCatalog)
        :noindex:

   .. automethod:: Gradebook.get_gradebook_record

Gradebook Form
--------------

.. autoclass:: GradebookForm
   :show-inheritance:

   .. automethod:: GradebookForm.get_gradebook_form_record

Gradebook List
--------------

.. autoclass:: GradebookList
   :show-inheritance:

   .. autoattribute:: GradebookList.next_gradebook

   .. automethod:: GradebookList.get_next_gradebooks

Gradebook Node
--------------

.. autoclass:: GradebookNode
   :show-inheritance:

   .. autoattribute:: GradebookNode.gradebook

   .. autoattribute:: GradebookNode.parent_gradebook_nodes

   .. autoattribute:: GradebookNode.child_gradebook_nodes

Gradebook Node List
-------------------

.. autoclass:: GradebookNodeList
   :show-inheritance:

   .. autoattribute:: GradebookNodeList.next_gradebook_node

   .. automethod:: GradebookNodeList.get_next_gradebook_nodes

