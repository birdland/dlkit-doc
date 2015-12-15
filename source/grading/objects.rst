

Objects
=======


Grade
-----

.. py:class:: Grade(abc_grading_objects.Grade, osid_objects.OsidObject, osid_markers.Subjugateable)
    A ``Grade``.


    Grades represent qualified performance levels defined within some
    grading system.





    .. py:method:: get_grade_system_id():
        :noindex:


    .. py:attribute:: grade_system_id
        :noindex:


    .. py:method:: get_grade_system():
        :noindex:


    .. py:attribute:: grade_system
        :noindex:


    .. py:method:: get_input_score_start_range():
        :noindex:


    .. py:attribute:: input_score_start_range
        :noindex:


    .. py:method:: get_input_score_end_range():
        :noindex:


    .. py:attribute:: input_score_end_range
        :noindex:


    .. py:method:: get_output_score():
        :noindex:


    .. py:attribute:: output_score
        :noindex:


    .. py:method:: get_grade_record(grade_record_type):
        :noindex:


Grade Form
----------

.. py:class:: GradeForm(abc_grading_objects.GradeForm, osid_objects.OsidObjectForm, osid_objects.OsidSubjugateableForm)
    This is the form for creating and updating ``Grades``.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``GradeAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_input_score_start_range_metadata():
        :noindex:


    .. py:attribute:: input_score_start_range_metadata
        :noindex:


    .. py:method:: set_input_score_start_range(score):
        :noindex:


    .. py:method:: clear_input_score_start_range():
        :noindex:


    .. py:attribute:: input_score_start_range
        :noindex:


    .. py:method:: get_input_score_end_range_metadata():
        :noindex:


    .. py:attribute:: input_score_end_range_metadata
        :noindex:


    .. py:method:: set_input_score_end_range(score):
        :noindex:


    .. py:method:: clear_input_score_end_range():
        :noindex:


    .. py:attribute:: input_score_end_range
        :noindex:


    .. py:method:: get_output_score_metadata():
        :noindex:


    .. py:attribute:: output_score_metadata
        :noindex:


    .. py:method:: set_output_score(score):
        :noindex:


    .. py:method:: clear_output_score():
        :noindex:


    .. py:attribute:: output_score
        :noindex:


    .. py:method:: get_grade_form_record(grade_record_type):
        :noindex:


Grade List
----------

.. py:class:: GradeList(abc_grading_objects.GradeList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``GradeList`` provides a means for accessing ``Grade`` elements
        sequentially
    either one at a time or many at a time.


    Examples: while (gl.hasNext()) { Grade grade = gl.getNextGrade(); }




    or
      while (gl.hasNext()) {
           Grade[] grades = gl.getNextGrades(gl.available());
      }









    .. py:method:: get_next_grade():
        :noindex:


    .. py:attribute:: next_grade
        :noindex:


    .. py:method:: get_next_grades(n):
        :noindex:


Grade System
------------

.. py:class:: GradeSystem(abc_grading_objects.GradeSystem, osid_objects.OsidObject, osid_markers.Aggregateable)
    A ``GradeSystem`` represents a grading system.


    The system can be based on assigned Grades or based on a numeric
    scale.





    .. py:method:: is_based_on_grades():
        :noindex:


    .. py:method:: get_grade_ids():
        :noindex:


    .. py:attribute:: grade_ids
        :noindex:


    .. py:method:: get_grades():
        :noindex:


    .. py:attribute:: grades
        :noindex:


    .. py:method:: get_lowest_numeric_score():
        :noindex:


    .. py:attribute:: lowest_numeric_score
        :noindex:


    .. py:method:: get_numeric_score_increment():
        :noindex:


    .. py:attribute:: numeric_score_increment
        :noindex:


    .. py:method:: get_highest_numeric_score():
        :noindex:


    .. py:attribute:: highest_numeric_score
        :noindex:


    .. py:method:: get_grade_system_record(grade_system_record_type):
        :noindex:


Grade System Form
-----------------

.. py:class:: GradeSystemForm(abc_grading_objects.GradeSystemForm, osid_objects.OsidObjectForm, osid_objects.OsidAggregateableForm)
    This is the form for creating and updating ``GradeSystems``.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``GradeSystemAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_based_on_grades_metadata():
        :noindex:


    .. py:attribute:: based_on_grades_metadata
        :noindex:


    .. py:method:: set_based_on_grades(grades):
        :noindex:


    .. py:method:: clear_based_on_grades():
        :noindex:


    .. py:attribute:: based_on_grades
        :noindex:


    .. py:method:: get_lowest_numeric_score_metadata():
        :noindex:


    .. py:attribute:: lowest_numeric_score_metadata
        :noindex:


    .. py:method:: set_lowest_numeric_score(score):
        :noindex:


    .. py:method:: clear_lowest_numeric_score():
        :noindex:


    .. py:attribute:: lowest_numeric_score
        :noindex:


    .. py:method:: get_numeric_score_increment_metadata():
        :noindex:


    .. py:attribute:: numeric_score_increment_metadata
        :noindex:


    .. py:method:: set_numeric_score_increment(increment):
        :noindex:


    .. py:method:: clear_numeric_score_increment():
        :noindex:


    .. py:attribute:: numeric_score_increment
        :noindex:


    .. py:method:: get_highest_numeric_score_metadata():
        :noindex:


    .. py:attribute:: highest_numeric_score_metadata
        :noindex:


    .. py:method:: set_highest_numeric_score(score):
        :noindex:


    .. py:method:: clear_highest_numeric_score():
        :noindex:


    .. py:attribute:: highest_numeric_score
        :noindex:


    .. py:method:: get_grade_system_form_record(grade_system_record_type):
        :noindex:


Grade System List
-----------------

.. py:class:: GradeSystemList(abc_grading_objects.GradeSystemList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``GradeSystemList`` provides a means for accessing ``GradeSystem``
        elements
    sequentially either one at a time or many at a time.


    Examples: while (gsl.hasNext()) { GradeSystem system =
    gsl.getNextGradeSystem(); }




    or
      while (gsl.hasNext()) {
           GradeSystem[] systems = gsl.getNextGradeSystems(gsl.available());
      }









    .. py:method:: get_next_grade_system():
        :noindex:


    .. py:attribute:: next_grade_system
        :noindex:


    .. py:method:: get_next_grade_systems(n):
        :noindex:


Grade Entry
-----------

.. py:class:: GradeEntry(abc_grading_objects.GradeEntry, osid_objects.OsidRelationship)
    A ``GradeEntry`` represents an entry in a ``Gradebook``.

    .. py:method:: get_gradebook_column_id():
        :noindex:


    .. py:attribute:: gradebook_column_id
        :noindex:


    .. py:method:: get_gradebook_column():
        :noindex:


    .. py:attribute:: gradebook_column
        :noindex:


    .. py:method:: get_key_resource_id():
        :noindex:


    .. py:attribute:: key_resource_id
        :noindex:


    .. py:method:: get_key_resource():
        :noindex:


    .. py:attribute:: key_resource
        :noindex:


    .. py:method:: is_derived():
        :noindex:


    .. py:method:: overrides_calculated_entry():
        :noindex:


    .. py:method:: get_overridden_calculated_entry_id():
        :noindex:


    .. py:attribute:: overridden_calculated_entry_id
        :noindex:


    .. py:method:: get_overridden_calculated_entry():
        :noindex:


    .. py:attribute:: overridden_calculated_entry
        :noindex:


    .. py:method:: is_ignored_for_calculations():
        :noindex:


    .. py:method:: is_graded():
        :noindex:


    .. py:method:: get_grade_id():
        :noindex:


    .. py:attribute:: grade_id
        :noindex:


    .. py:method:: get_grade():
        :noindex:


    .. py:attribute:: grade
        :noindex:


    .. py:method:: get_score():
        :noindex:


    .. py:attribute:: score
        :noindex:


    .. py:method:: get_time_graded():
        :noindex:


    .. py:attribute:: time_graded
        :noindex:


    .. py:method:: get_grader_id():
        :noindex:


    .. py:attribute:: grader_id
        :noindex:


    .. py:method:: get_grader():
        :noindex:


    .. py:attribute:: grader
        :noindex:


    .. py:method:: get_grading_agent_id():
        :noindex:


    .. py:attribute:: grading_agent_id
        :noindex:


    .. py:method:: get_grading_agent():
        :noindex:


    .. py:attribute:: grading_agent
        :noindex:


    .. py:method:: get_grade_entry_record(grade_entry_record_type):
        :noindex:


Grade Entry Form
----------------

.. py:class:: GradeEntryForm(abc_grading_objects.GradeEntryForm, osid_objects.OsidRelationshipForm)
    This is the form for creating and updating ``GradeEntries``.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``GradeEntryAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_ignored_for_calculations_metadata():
        :noindex:


    .. py:attribute:: ignored_for_calculations_metadata
        :noindex:


    .. py:method:: set_ignored_for_calculations(ignore):
        :noindex:


    .. py:method:: clear_ignored_for_calculations():
        :noindex:


    .. py:attribute:: ignored_for_calculations
        :noindex:


    .. py:method:: get_grade_metadata():
        :noindex:


    .. py:attribute:: grade_metadata
        :noindex:


    .. py:method:: set_grade(grade_id):
        :noindex:


    .. py:method:: clear_grade():
        :noindex:


    .. py:attribute:: grade
        :noindex:


    .. py:method:: get_score_metadata():
        :noindex:


    .. py:attribute:: score_metadata
        :noindex:


    .. py:method:: set_score(score):
        :noindex:


    .. py:method:: clear_score():
        :noindex:


    .. py:attribute:: score
        :noindex:


    .. py:method:: get_grade_entry_form_record(grade_entry_record_type):
        :noindex:


Grade Entry List
----------------

.. py:class:: GradeEntryList(abc_grading_objects.GradeEntryList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``GradeEntryList`` provides a means for accessing ``GradeEntry``
        elements
    sequentially either one at a time or many at a time.


    Examples: while (gel.hasNext()) { GradeEntry entry =
    gel.getNextGradeEntry(); }




    or
      while (gel.hasNext()) {
           GradeEntry[] entries = gel.getNextGradeEntries(gel.available());
      }









    .. py:method:: get_next_grade_entry():
        :noindex:


    .. py:attribute:: next_grade_entry
        :noindex:


    .. py:method:: get_next_grade_entries(n):
        :noindex:


Gradebook Column
----------------

.. py:class:: GradebookColumn(abc_grading_objects.GradebookColumn, osid_objects.OsidObject)
    A ``GradebookColumn`` represents a series of grade entries in a gradebook.


    Each GradeEntry in a column share the same ``GradeSystem``.





    .. py:method:: get_grade_system_id():
        :noindex:


    .. py:attribute:: grade_system_id
        :noindex:


    .. py:method:: get_grade_system():
        :noindex:


    .. py:attribute:: grade_system
        :noindex:


    .. py:method:: get_gradebook_column_record(gradebook_column_record_type):
        :noindex:


Gradebook Column Form
---------------------

.. py:class:: GradebookColumnForm(abc_grading_objects.GradebookColumnForm, osid_objects.OsidObjectForm)
    This is the form for creating and updating ``GradebookColumns``.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``GradebookAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_grade_system_metadata():
        :noindex:


    .. py:attribute:: grade_system_metadata
        :noindex:


    .. py:method:: set_grade_system(grade_system_id):
        :noindex:


    .. py:method:: clear_grade_system():
        :noindex:


    .. py:attribute:: grade_system
        :noindex:


    .. py:method:: get_gradebook_column_form_record(gradebook_column_record_type):
        :noindex:


Gradebook Column List
---------------------

.. py:class:: GradebookColumnList(abc_grading_objects.GradebookColumnList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``GradebookColumnList`` provides a means for accessing
        ``GradebookColumn``
    elements sequentially either one at a time or many at a time.


    Examples: while (gcl.hasNext()) { GradebookColumn column =
    gcl.getNextGradebookColumn(); }




    or
      while (gcl.hasNext()) {
           GradebookColumn[] columns = gcl.getNextGradebookColumns(gcl.available());
      }









    .. py:method:: get_next_gradebook_column():
        :noindex:


    .. py:attribute:: next_gradebook_column
        :noindex:


    .. py:method:: get_next_gradebook_columns(n):
        :noindex:


Gradebook Column Summary
------------------------

.. py:class:: GradebookColumnSummary(abc_grading_objects.GradebookColumnSummary, osid_objects.OsidObject)
    A ``GradebookColumnSummary`` is a summary of all entries within a gradebook column.

    .. py:method:: get_gradebook_column_id():
        :noindex:


    .. py:attribute:: gradebook_column_id
        :noindex:


    .. py:method:: get_gradebook_column():
        :noindex:


    .. py:attribute:: gradebook_column
        :noindex:


    .. py:method:: get_mean():
        :noindex:


    .. py:attribute:: mean
        :noindex:


    .. py:method:: get_median():
        :noindex:


    .. py:attribute:: median
        :noindex:


    .. py:method:: get_mode():
        :noindex:


    .. py:attribute:: mode
        :noindex:


    .. py:method:: get_rms():
        :noindex:


    .. py:attribute:: rms
        :noindex:


    .. py:method:: get_standard_deviation():
        :noindex:


    .. py:attribute:: standard_deviation
        :noindex:


    .. py:method:: get_sum():
        :noindex:


    .. py:attribute:: sum
        :noindex:


    .. py:method:: get_gradebook_column_summary_record(gradebook_column_summary_record_type):
        :noindex:


Gradebook
---------

.. py:class:: Gradebook(abc_grading_objects.Gradebook, osid_objects.OsidCatalog)
        :noindex:

    .. py:method:: get_gradebook_record(gradebook_record_type):
        :noindex:


Gradebook Form
--------------

.. py:class:: GradebookForm(abc_grading_objects.GradebookForm, osid_objects.OsidCatalogForm)
    This is the form for creating and updating ``Gradebooks``.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``GradebookAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_gradebook_form_record(gradebook_record_type):
        :noindex:


Gradebook List
--------------

.. py:class:: GradebookList(abc_grading_objects.GradebookList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``GradebookList`` provides a means for accessing ``Gradebook`` elements
    sequentially either one at a time or many at a time.


    Examples: while (gl.hasNext()) { Gradebook gradebook =
    gl.getNextGradebook(); }




    or
      while (gl.hasNext()) {
           Gradebook[] gradebooks = gl.getNextGradebooks(gl.available());
      }









    .. py:method:: get_next_gradebook():
        :noindex:


    .. py:attribute:: next_gradebook
        :noindex:


    .. py:method:: get_next_gradebooks(n):
        :noindex:


Gradebook Node
--------------

.. py:class:: GradebookNode(abc_grading_objects.GradebookNode, osid_objects.OsidNode)
    This interface is a container for a partial hierarchy retrieval.


    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``GradebookHierarchySession``.





    .. py:method:: get_gradebook():
        :noindex:


    .. py:attribute:: gradebook
        :noindex:


    .. py:method:: get_parent_gradebook_nodes():
        :noindex:


    .. py:attribute:: parent_gradebook_nodes
        :noindex:


    .. py:method:: get_child_gradebook_nodes():
        :noindex:


    .. py:attribute:: child_gradebook_nodes
        :noindex:


Gradebook Node List
-------------------

.. py:class:: GradebookNodeList(abc_grading_objects.GradebookNodeList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``GradebookNodeList`` provides a means for accessing ``GradebookNode``
    elements sequentially either one at a time or many at a time.


    Examples: while (gnl.hasNext()) { GradebookNode node =
    gnl.getNextGradebookNode(); }




    or
      while (gnl.hasNext()) {
           GradebookNode[] nodes = gnl.getNextGradebookNodes(gnl.available());
      }









    .. py:method:: get_next_gradebook_node():
        :noindex:


    .. py:attribute:: next_gradebook_node
        :noindex:


    .. py:method:: get_next_gradebook_nodes(n):
        :noindex:


