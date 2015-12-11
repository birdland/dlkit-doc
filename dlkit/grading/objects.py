
from ..osid import objects as osid_objects
from ..osid import markers as osid_markers
from ..osid import sessions as osid_sessions


class Grade(osid_objects.OsidObject, osid_markers.Subjugateable):
    """A ``Grade``.

    Grades represent qualified performance levels defined within some
    grading system.

    """
    



    def get_grade_system_id(self):
        """Gets the ``GradeSystem Id`` in which this grade belongs.

        return: (osid.id.Id) - the grade system ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    grade_system_id = property(fget=get_grade_system_id)


    def get_grade_system(self):
        """Gets the ``GradeSystem`` in which this grade belongs.

        return: (osid.grading.GradeSystem) - the grade system
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystem

    grade_system = property(fget=get_grade_system)


    def get_input_score_start_range(self):
        """Gets the low end of the input score range equivalent to this grade.

        return: (decimal) - the start range
        *compliance: mandatory -- This method must be implemented.*

        """
        return # decimal

    input_score_start_range = property(fget=get_input_score_start_range)


    def get_input_score_end_range(self):
        """Gets the high end of the input score range equivalent to this grade.

        return: (decimal) - the end range
        *compliance: mandatory -- This method must be implemented.*

        """
        return # decimal

    input_score_end_range = property(fget=get_input_score_end_range)


    def get_output_score(self):
        """Gets the output score for this grade used for calculating cumultives or performing articulation.

        return: (decimal) - the output score
        *compliance: mandatory -- This method must be implemented.*

        """
        return # decimal

    output_score = property(fget=get_output_score)


    def get_grade_record(self, grade_record_type):
        """Gets the grade record corresponding to the given ``Grade`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``grade_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(grade_record_type)``
        is ``true`` .

        arg:    grade_record_type (osid.type.Type): the type of the
                record to retrieve
        return: (osid.grading.records.GradeRecord) - the grade record
        raise:  NullArgument - ``grade_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(grade_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradeRecord


class GradeForm(osid_objects.OsidObjectForm, osid_objects.OsidSubjugateableForm):
    """This is the form for creating and updating ``Grades``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``GradeAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    



    def get_input_score_start_range_metadata(self):
        """Gets the metadata for the input score start range.

        return: (osid.Metadata) - metadata for the input score start
                range
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    input_score_start_range_metadata = property(fget=get_input_score_start_range_metadata)


    def set_input_score_start_range(self, score):
        """Sets the input score start range.

        arg:    score (decimal): the new start range
        raise:  InvalidArgument - ``score`` is invalid
        raise:  NoAccess - ``range`` cannot be modified
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_input_score_start_range(self):
        """Clears the input score start.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    input_score_start_range = property(fset=set_input_score_start_range, fdel=clear_input_score_start_range)


    def get_input_score_end_range_metadata(self):
        """Gets the metadata for the input score start range.

        return: (osid.Metadata) - metadata for the input score start
                range
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    input_score_end_range_metadata = property(fget=get_input_score_end_range_metadata)


    def set_input_score_end_range(self, score):
        """Sets the input score start range.

        arg:    score (decimal): the new start range
        raise:  InvalidArgument - ``score`` is invalid
        raise:  NoAccess - ``range`` cannot be modified
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_input_score_end_range(self):
        """Clears the input score start.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    input_score_end_range = property(fset=set_input_score_end_range, fdel=clear_input_score_end_range)


    def get_output_score_metadata(self):
        """Gets the metadata for the output score start range.

        return: (osid.Metadata) - metadata for the output score start
                range
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    output_score_metadata = property(fget=get_output_score_metadata)


    def set_output_score(self, score):
        """Sets the output score.

        arg:    score (decimal): the new output score
        raise:  InvalidArgument - ``score`` is invalid
        raise:  NoAccess - ``score`` cannot be modified
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_output_score(self):
        """Clears the output score.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    output_score = property(fset=set_output_score, fdel=clear_output_score)


    def get_grade_form_record(self, grade_record_type):
        """Gets the ``GradeFormRecord`` corresponding to the given grade record ``Type``.

        arg:    grade_record_type (osid.type.Type): the grade record
                type
        return: (osid.grading.records.GradeFormRecord) - the grade form
                record
        raise:  NullArgument - ``grade_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(grade_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradeFormRecord


class GradeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``GradeList`` provides a means for accessing ``Grade`` elements sequentially either one at a
        time or many at a time.

    Examples: while (gl.hasNext()) { Grade grade = gl.getNextGrade(); }

    or
      while (gl.hasNext()) {
           Grade[] grades = gl.getNextGrades(gl.available());
      }


    """
    



    def get_next_grade(self):
        """Gets the next ``Grade`` in this list.

        return: (osid.grading.Grade) - the next ``Grade`` in this list.
                The ``has_next()`` method should be used to test that a
                next ``Grade`` is available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Grade

    next_grade = property(fget=get_next_grade)


    def get_next_grades(self, n):
        """Gets the next set of ``Grade`` elements in this list which must be less than or equal to the return from
        ``available()``.

        arg:    n (cardinal): the number of ``Grade`` elements requested
                which must be less than or equal to ``available()``
        return: (osid.grading.Grade) - an array of ``Grade``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Grade


class GradeSystem(osid_objects.OsidObject, osid_markers.Aggregateable):
    """A ``GradeSystem`` represents a grading system.

    The system can be based on assigned Grades or based on a numeric
    scale.

    """
    



    def is_based_on_grades(self):
        """Tests if the grading system is based on grades.

        return: (boolean) - true if the grading system is based on
                grades, ``false`` if the system is a numeric score
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grade_ids(self):
        """Gets the grade ``Ids`` in this system ranked from highest to lowest.

        return: (osid.id.IdList) - the list of grades ``Ids``
        raise:  IllegalState - ``is_based_on_grades()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    grade_ids = property(fget=get_grade_ids)


    def get_grades(self):
        """Gets the grades in this system ranked from highest to lowest.

        return: (osid.grading.GradeList) - the list of grades
        raise:  IllegalState - ``is_based_on_grades()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeList

    grades = property(fget=get_grades)


    def get_lowest_numeric_score(self):
        """Gets the lowest number in a numeric grading system.

        return: (decimal) - the lowest number
        raise:  IllegalState - ``is_based_on_grades()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # decimal

    lowest_numeric_score = property(fget=get_lowest_numeric_score)


    def get_numeric_score_increment(self):
        """Gets the incremental step.

        return: (decimal) - the increment
        raise:  IllegalState - ``is_based_on_grades()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # decimal

    numeric_score_increment = property(fget=get_numeric_score_increment)


    def get_highest_numeric_score(self):
        """Gets the highest number in a numeric grading system.

        return: (decimal) - the highest number
        raise:  IllegalState - ``is_based_on_grades()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # decimal

    highest_numeric_score = property(fget=get_highest_numeric_score)


    def get_grade_system_record(self, grade_system_record_type):
        """Gets the grade system record corresponding to the given ``GradeSystem`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``grade_system_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(grade_system_record_type)`` is ``true`` .

        arg:    grade_system_record_type (osid.type.Type): the type of
                the record to retrieve
        return: (osid.grading.records.GradeSystemRecord) - the grade
                system record
        raise:  NullArgument - ``grade_system_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(grade_system_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradeSystemRecord


class GradeSystemForm(osid_objects.OsidObjectForm, osid_objects.OsidAggregateableForm):
    """This is the form for creating and updating ``GradeSystems``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``GradeSystemAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    



    def get_based_on_grades_metadata(self):
        """Gets the metadata for a grade-based designation.

        return: (osid.Metadata) - metadata for the grade-based
                designation
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    based_on_grades_metadata = property(fget=get_based_on_grades_metadata)


    def set_based_on_grades(self, grades):
        """Sets the grade-based designation.

        arg:    grades (boolean): the grade-based designation
        raise:  InvalidArgument - ``grades`` is invalid
        raise:  NoAccess - ``grades`` cannot be modified
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_based_on_grades(self):
        """Clears the based on grades designation.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    based_on_grades = property(fset=set_based_on_grades, fdel=clear_based_on_grades)


    def get_lowest_numeric_score_metadata(self):
        """Gets the metadata for the lowest numeric score.

        return: (osid.Metadata) - metadata for the lowest numeric score
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    lowest_numeric_score_metadata = property(fget=get_lowest_numeric_score_metadata)


    def set_lowest_numeric_score(self, score):
        """Sets the lowest numeric score.

        arg:    score (decimal): the lowest numeric score
        raise:  InvalidArgument - ``score`` is invalid
        raise:  NoAccess - ``score`` cannot be modified
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_lowest_numeric_score(self):
        """Clears the lowest score.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    lowest_numeric_score = property(fset=set_lowest_numeric_score, fdel=clear_lowest_numeric_score)


    def get_numeric_score_increment_metadata(self):
        """Gets the metadata for the lowest numeric score.

        return: (osid.Metadata) - metadata for the lowest numeric score
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    numeric_score_increment_metadata = property(fget=get_numeric_score_increment_metadata)


    def set_numeric_score_increment(self, increment):
        """Sets the numeric score increment.

        arg:    increment (decimal): the numeric score increment
        raise:  InvalidArgument - ``increment`` is invalid
        raise:  NoAccess - ``increment`` cannot be modified
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_numeric_score_increment(self):
        """Clears the numeric score increment.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    numeric_score_increment = property(fset=set_numeric_score_increment, fdel=clear_numeric_score_increment)


    def get_highest_numeric_score_metadata(self):
        """Gets the metadata for the highest numeric score.

        return: (osid.Metadata) - metadata for the highest numeric score
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    highest_numeric_score_metadata = property(fget=get_highest_numeric_score_metadata)


    def set_highest_numeric_score(self, score):
        """Sets the highest numeric score.

        arg:    score (decimal): the highest numeric score
        raise:  InvalidArgument - ``score`` is invalid
        raise:  NoAccess - ``score`` cannot be modified
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_highest_numeric_score(self):
        """Clears the highest numeric score.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    highest_numeric_score = property(fset=set_highest_numeric_score, fdel=clear_highest_numeric_score)


    def get_grade_system_form_record(self, grade_system_record_type):
        """Gets the ``GradeSystemFormRecord`` corresponding to the given grade system record ``Type``.

        arg:    grade_system_record_type (osid.type.Type): the grade
                system record type
        return: (osid.grading.records.GradeSystemFormRecord) - the grade
                system form record
        raise:  NullArgument - ``grade_system_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(grade_system_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradeSystemFormRecord


class GradeSystemList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``GradeSystemList`` provides a means for accessing ``GradeSystem`` elements sequentially either
        one at a time or many at a time.

    Examples: while (gsl.hasNext()) { GradeSystem system =
    gsl.getNextGradeSystem(); }

    or
      while (gsl.hasNext()) {
           GradeSystem[] systems = gsl.getNextGradeSystems(gsl.available());
      }


    """
    



    def get_next_grade_system(self):
        """Gets the next ``GradeSystem`` in this list.

        return: (osid.grading.GradeSystem) - the next ``GradeSystem`` in
                this list. The ``has_next()`` method should be used to
                test that a next ``GradeSystem`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystem

    next_grade_system = property(fget=get_next_grade_system)


    def get_next_grade_systems(self, n):
        """Gets the next set of ``GradeSystem`` elements in this list which must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``GradeSystem`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.grading.GradeSystem) - an array of ``GradeSystem``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystem


class GradeEntry(osid_objects.OsidRelationship):
    """A ``GradeEntry`` represents an entry in a ``Gradebook``."""
    



    def get_gradebook_column_id(self):
        """Gets the ``Id`` of the ``GradebookColumn``.

        return: (osid.id.Id) - the ``Id`` of the ``GradebookColumn``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    gradebook_column_id = property(fget=get_gradebook_column_id)


    def get_gradebook_column(self):
        """Gets the ``GradebookColumn``.

        return: (osid.grading.GradebookColumn) - the ``GradebookColumn``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookColumn

    gradebook_column = property(fget=get_gradebook_column)


    def get_key_resource_id(self):
        """Gets the ``Id`` of the key resource of this entry.

        The key resource may be a student or other applicable key to
        identify a row of grading entries.

        return: (osid.id.Id) - ``Id`` of the key resource
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    key_resource_id = property(fget=get_key_resource_id)


    def get_key_resource(self):
        """Gets the key resource of this entry.

        The key resource may be a student or other applicable key to
        identify a row of grading entries.

        return: (osid.resource.Resource) - the key resource
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Resource

    key_resource = property(fget=get_key_resource)


    def is_derived(self):
        """Tests if this is a calculated entry.

        return: (boolean) - ``true`` if this entry is a calculated
                entry, ``false`` otherwise. If ``true,`` then
                ``overrides_calculated_entry()`` must be ``false``.
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def overrides_calculated_entry(self):
        """Tests if this is a manual entry that overrides a calculated entry.

        return: (boolean) - ``true`` if this entry overrides a
                calculated entry, ``false`` otherwise. If ``true,`` then
                ``is_derived()`` must be ``false``.
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_overridden_calculated_entry_id(self):
        """Gets the calculated entry ``Id`` this entry overrides.

        return: (osid.id.Id) - the calculated entry ``Id``
        raise:  IllegalState - ``overrides_derived_entry()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    overridden_calculated_entry_id = property(fget=get_overridden_calculated_entry_id)


    def get_overridden_calculated_entry(self):
        """Gets the calculated entry this entry overrides.

        return: (osid.grading.GradeEntry) - the calculated entry
        raise:  IllegalState - ``overrides_calculated_entry()`` is
                ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntry

    overridden_calculated_entry = property(fget=get_overridden_calculated_entry)


    def is_ignored_for_calculations(self):
        """Tests if this is entry should be ignored in any averaging, scaling or curve calculation.

        return: (boolean) - ``true`` if this entry is ignored, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def is_graded(self):
        """Tests if a grade or score has been assigned to this entry.

        Generally, an entry is created with a grade or score.

        return: (boolean) - ``true`` if a grade has been assigned,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grade_id(self):
        """Gets the grade ``Id`` in this entry if the grading system is based on grades.

        return: (osid.id.Id) - the grade ``Id``
        raise:  IllegalState - ``is_graded()`` is ``false`` or
                ``GradeSystem.isBasedOnGrades()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    grade_id = property(fget=get_grade_id)


    def get_grade(self):
        """Gets the grade in this entry if the grading system is based on grades.

        return: (osid.grading.Grade) - the grade
        raise:  IllegalState - ``is_graded()`` is ``false`` or
                ``GradeSystem.isBasedOnGrades()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Grade

    grade = property(fget=get_grade)


    def get_score(self):
        """Gets the score in this entry if the grading system is not based on grades.

        return: (decimal) - the score
        raise:  IllegalState - ``is_graded()`` is ``false`` or
                ``GradeSystem.isBasedOnGrades()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # decimal

    score = property(fget=get_score)


    def get_time_graded(self):
        """Gets the time the gradeable object was graded.

        return: (osid.calendaring.DateTime) - the timestamp of the
                grading entry
        raise:  IllegalState - ``is_graded()`` is ``false`` or
                ``is_derived()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.DateTime

    time_graded = property(fget=get_time_graded)


    def get_grader_id(self):
        """Gets the ``Id`` of the ``Resource`` that created this entry.

        return: (osid.id.Id) - the ``Id`` of the ``Resource``
        raise:  IllegalState - ``is_graded()`` is ``false`` or
                ``is_derived()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    grader_id = property(fget=get_grader_id)


    def get_grader(self):
        """Gets the ``Resource`` that created this entry.

        return: (osid.resource.Resource) - the ``Resource``
        raise:  IllegalState - ``is_graded() is false or is_derived() is
                true``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Resource

    grader = property(fget=get_grader)


    def get_grading_agent_id(self):
        """Gets the ``Id`` of the ``Agent`` that created this entry.

        return: (osid.id.Id) - the ``Id`` of the ``Agent``
        raise:  IllegalState - ``is_graded()`` is ``false`` or
                ``is_derived()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    grading_agent_id = property(fget=get_grading_agent_id)


    def get_grading_agent(self):
        """Gets the ``Agent`` that created this entry.

        return: (osid.authentication.Agent) - the ``Agent``
        raise:  IllegalState - ``is_graded() is false or is_derived() is
                true``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.Agent

    grading_agent = property(fget=get_grading_agent)


    def get_grade_entry_record(self, grade_entry_record_type):
        """Gets the grade entry record corresponding to the given ``GradeEntry`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``grade_entry_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(grade_entry_record_type)`` is ``true`` .

        arg:    grade_entry_record_type (osid.type.Type): the type of
                the record to retrieve
        return: (osid.grading.records.GradeEntryRecord) - the grade
                entry record
        raise:  NullArgument - ``grade_entry_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(grade_entry_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradeEntryRecord


class GradeEntryForm(osid_objects.OsidRelationshipForm):
    """This is the form for creating and updating ``GradeEntries``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``GradeEntryAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    



    def get_ignored_for_calculations_metadata(self):
        """Gets the metadata for the ignore flag.

        return: (osid.Metadata) - metadata for the ignore flag
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    ignored_for_calculations_metadata = property(fget=get_ignored_for_calculations_metadata)


    def set_ignored_for_calculations(self, ignore):
        """Sets the ignore for calculations flag.

        arg:    ignore (boolean): the new ignore flag
        raise:  InvalidArgument - ``ignore`` is invalid
        raise:  NoAccess - ``ignore`` cannot be modified
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_ignored_for_calculations(self):
        """Clears the ignore for calculations flag.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ignored_for_calculations = property(fset=set_ignored_for_calculations, fdel=clear_ignored_for_calculations)


    def get_grade_metadata(self):
        """Gets the metadata for a grade.

        return: (osid.Metadata) - metadata for the grade
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    grade_metadata = property(fget=get_grade_metadata)


    def set_grade(self, grade_id):
        """Sets the grade.

        arg:    grade_id (osid.id.Id): the new grade
        raise:  InvalidArgument - ``grade_id`` is invalid or
                ``GradebookColumn.getGradeSystem().isBasedOnGrades()``
                is ``false``
        raise:  NoAccess - ``grade_id`` cannot be modified
        raise:  NullArgument - ``grade_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade(self):
        """Clears the grade.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade = property(fset=set_grade, fdel=clear_grade)


    def get_score_metadata(self):
        """Gets the metadata for a score.

        return: (osid.Metadata) - metadata for the score
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    score_metadata = property(fget=get_score_metadata)


    def set_score(self, score):
        """Sets the score.

        arg:    score (decimal): the new score
        raise:  InvalidArgument - ``score`` is invalid or
                ``GradebookColumn.getGradeSystem().isBasedOnGrades()``
                is ``true``
        raise:  NoAccess - ``score`` cannot be modified
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_score(self):
        """Clears the score.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    score = property(fset=set_score, fdel=clear_score)


    def get_grade_entry_form_record(self, grade_entry_record_type):
        """Gets the ``GradeEntryFormRecord`` corresponding to the given grade entry record ``Type``.

        arg:    grade_entry_record_type (osid.type.Type): the grade
                entry record type
        return: (osid.grading.records.GradeEntryFormRecord) - the grade
                entry form record
        raise:  NullArgument - ``grade_entry_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(grade_entry_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradeEntryFormRecord


class GradeEntryList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``GradeEntryList`` provides a means for accessing ``GradeEntry`` elements sequentially either
        one at a time or many at a time.

    Examples: while (gel.hasNext()) { GradeEntry entry =
    gel.getNextGradeEntry(); }

    or
      while (gel.hasNext()) {
           GradeEntry[] entries = gel.getNextGradeEntries(gel.available());
      }


    """
    



    def get_next_grade_entry(self):
        """Gets the next ``GradeEntry`` in this list.

        return: (osid.grading.GradeEntry) - the next ``GradeEntry`` in
                this list. The ``has_next()`` method should be used to
                test that a next ``GradeEntry`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntry

    next_grade_entry = property(fget=get_next_grade_entry)


    def get_next_grade_entries(self, n):
        """Gets the next set of ``GradeEntry`` elements in this list which must be less than or equal to the number
        returned from ``available()``.

        arg:    n (cardinal): the number of ``GradeEntry`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.grading.GradeEntry) - an array of ``GradeEntry``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntry


class GradebookColumn(osid_objects.OsidObject):
    """A ``GradebookColumn`` represents a series of grade entries in a gradebook.

    Each GradeEntry in a column share the same ``GradeSystem``.

    """
    



    def get_grade_system_id(self):
        """Gets the ``GradeSystem Id`` in which this grade belongs.

        return: (osid.id.Id) - the grade system ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    grade_system_id = property(fget=get_grade_system_id)


    def get_grade_system(self):
        """Gets the ``GradeSystem`` in which this grade belongs.

        return: (osid.grading.GradeSystem) - the package grade system
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystem

    grade_system = property(fget=get_grade_system)


    def get_gradebook_column_record(self, gradebook_column_record_type):
        """Gets the gradebook column record corresponding to the given ``GradeBookColumn`` record ``Type``.

        This method ie used to retrieve an object implementing the
        requested record. The ``gradebook_column_record_type`` may be
        the ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(gradebook_column_record_type)`` is ``true`` .

        arg:    gradebook_column_record_type (osid.type.Type): the type
                of the record to retrieve
        return: (osid.grading.records.GradebookColumnRecord) - the
                gradebook column record
        raise:  NullArgument - ``gradebook_column_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(gradebook_column_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradebookColumnRecord


class GradebookColumnForm(osid_objects.OsidObjectForm):
    """This is the form for creating and updating ``GradebookColumns``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``GradebookAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    



    def get_grade_system_metadata(self):
        """Gets the metadata for a grade system.

        return: (osid.Metadata) - metadata for the grade system
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    grade_system_metadata = property(fget=get_grade_system_metadata)


    def set_grade_system(self, grade_system_id):
        """Sets the grade system.

        arg:    grade_system_id (osid.id.Id): the new grade system
        raise:  InvalidArgument - ``grade_system_id`` is invalid
        raise:  NoAccess - ``grade_system_id`` cannot be modified
        raise:  NullArgument - ``grade_system_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade_system(self):
        """Clears the grade system.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system = property(fset=set_grade_system, fdel=clear_grade_system)


    def get_gradebook_column_form_record(self, gradebook_column_record_type):
        """Gets the ``GradebookColumnFormRecord`` corresponding to the given gradebook column record ``Type``.

        arg:    gradebook_column_record_type (osid.type.Type): a
                gradebook column record type
        return: (osid.grading.records.GradebookColumnFormRecord) - the
                gradebook column form record
        raise:  NullArgument - ``gradebook_column_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(gradebook_column_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradebookColumnFormRecord


class GradebookColumnList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``GradebookColumnList`` provides a means for accessing ``GradebookColumn`` elements
        sequentially either one at a time or many at a time.

    Examples: while (gcl.hasNext()) { GradebookColumn column =
    gcl.getNextGradebookColumn(); }

    or
      while (gcl.hasNext()) {
           GradebookColumn[] columns = gcl.getNextGradebookColumns(gcl.available());
      }


    """
    



    def get_next_gradebook_column(self):
        """Gets the next ``GradebookColumn`` in this list.

        return: (osid.grading.GradebookColumn) - the next
                ``GradebookColumn`` in this list. The ``has_next()``
                method should be used to test that a next
                ``GradebookColumn`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookColumn

    next_gradebook_column = property(fget=get_next_gradebook_column)


    def get_next_gradebook_columns(self, n):
        """Gets the next set of ``GradebookColumn`` elements in this list which must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``GradebookColumn`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.grading.GradebookColumn) - an array of
                ``GradebookColumn`` elements.The length of the array is
                less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookColumn


class GradebookColumnSummary(osid_objects.OsidObject):
    """A ``GradebookColumnSummary`` is a summary of all entries within a gradebook column."""
    



    def get_gradebook_column_id(self):
        """Gets the ``Id`` of the ``GradebookColumn``.

        return: (osid.id.Id) - the ``Id`` of the ``GradebookColumn``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    gradebook_column_id = property(fget=get_gradebook_column_id)


    def get_gradebook_column(self):
        """Gets the ``GradebookColumn``.

        return: (osid.grading.GradebookColumn) - the ``GradebookColumn``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookColumn

    gradebook_column = property(fget=get_gradebook_column)


    def get_mean(self):
        """Gets the mean score.

        If this system is based on grades, the mean output score is
        returned.

        return: (decimal) - the mean score
        *compliance: mandatory -- This method must be implemented.*

        """
        return # decimal

    mean = property(fget=get_mean)


    def get_median(self):
        """Gets the median score.

        If this system is based on grades, the mean output score is
        returned.

        return: (decimal) - the median score
        *compliance: mandatory -- This method must be implemented.*

        """
        return # decimal

    median = property(fget=get_median)


    def get_mode(self):
        """Gets the mode of the score.

        If this system is based on grades, the mode of the output score
        is returned.

        return: (decimal) - the median score
        *compliance: mandatory -- This method must be implemented.*

        """
        return # decimal

    mode = property(fget=get_mode)


    def get_rms(self):
        """Gets the root mean square of the score.

        If this system is based on grades, the RMS of the output score
        is returned.

        return: (decimal) - the median score
        *compliance: mandatory -- This method must be implemented.*

        """
        return # decimal

    rms = property(fget=get_rms)


    def get_standard_deviation(self):
        """Gets the standard deviation.

        If this system is based on grades, the spread of the output
        scores is returned.

        return: (decimal) - the standard deviation
        *compliance: mandatory -- This method must be implemented.*

        """
        return # decimal

    standard_deviation = property(fget=get_standard_deviation)


    def get_sum(self):
        """Gets the sum of the scores.

        If this system is based on grades, the sum of the output scores
        is returned.

        return: (decimal) - the median score
        *compliance: mandatory -- This method must be implemented.*

        """
        return # decimal

    sum = property(fget=get_sum)


    def get_gradebook_column_summary_record(self, gradebook_column_summary_record_type):
        """Gets the gradebook column summary record corresponding to the given ``GradebookColumnSummary`` record
        ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``gradebook_column_summary_record_type``
        may be the ``Type`` returned in ``get_record_types()`` or any of
        its parents in a ``Type`` hierarchy where
        ``has_record_type(gradebook_column_summary_record_type)`` is
        ``true`` .

        arg:    gradebook_column_summary_record_type (osid.type.Type):
                the type of the record to retrieve
        return: (osid.grading.records.GradebookColumnSummaryRecord) -
                the gradebook column summary record
        raise:  NullArgument - ``gradebook_column_summary_record_type``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(gradebook_column_summary_record_type)`
                ` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradebookColumnSummaryRecord


class Gradebook(osid_objects.OsidCatalog, osid_sessions.OsidSession):
    """A gradebook defines a collection of grade entries."""
    



    def get_gradebook_record(self, gradebook_record_type):
        """Gets the gradebook record corresponding to the given ``Gradebook`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``gradebook_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(gradebook_record_type)`` is ``true`` .

        arg:    gradebook_record_type (osid.type.Type): a gradebook
                record type
        return: (osid.grading.records.GradebookRecord) - the gradebook
                record
        raise:  NullArgument - ``gradebook_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(gradebook_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradebookRecord


class GradebookForm(osid_objects.OsidCatalogForm):
    """This is the form for creating and updating ``Gradebooks``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``GradebookAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    



    def get_gradebook_form_record(self, gradebook_record_type):
        """Gets the ``GradebookFormRecord`` corresponding to the given gradebook record ``Type``.

        arg:    gradebook_record_type (osid.type.Type): a gradebook
                record type
        return: (osid.grading.records.GradebookFormRecord) - the
                gradebook form record
        raise:  NullArgument - ``gradebook_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(gradebook_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradebookFormRecord


class GradebookList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``GradebookList`` provides a means for accessing ``Gradebook`` elements sequentially either one
        at a time or many at a time.

    Examples: while (gl.hasNext()) { Gradebook gradebook =
    gl.getNextGradebook(); }

    or
      while (gl.hasNext()) {
           Gradebook[] gradebooks = gl.getNextGradebooks(gl.available());
      }


    """
    



    def get_next_gradebook(self):
        """Gets the next ``Gradebook`` in this list.

        return: (osid.grading.Gradebook) - the next ``Gradebook`` in
                this list. The ``has_next()`` method should be used to
                test that a next ``Gradebook`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Gradebook

    next_gradebook = property(fget=get_next_gradebook)


    def get_next_gradebooks(self, n):
        """Gets the next set of ``Gradebook`` elements in this list which must be less than or equal to the return from
        ``available()``.

        arg:    n (cardinal): the number of ``Gradebook`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.grading.Gradebook) - an array of ``Gradebook``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Gradebook


class GradebookNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``GradebookHierarchySession``.

    """
    



    def get_gradebook(self):
        """Gets the ``Gradebook`` at this node.

        return: (osid.grading.Gradebook) - the gradebook represented by
                this node
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)


    def get_parent_gradebook_nodes(self):
        """Gets the parents of this gradebook.

        return: (osid.grading.GradebookNodeList) - the parents of the
                ``id``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookNodeList

    parent_gradebook_nodes = property(fget=get_parent_gradebook_nodes)


    def get_child_gradebook_nodes(self):
        """Gets the children of this gradebook.

        return: (osid.grading.GradebookNodeList) - the children of this
                gradebook
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookNodeList

    child_gradebook_nodes = property(fget=get_child_gradebook_nodes)


class GradebookNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``GradebookNodeList`` provides a means for accessing ``GradebookNode`` elements sequentially
        either one at a time or many at a time.

    Examples: while (gnl.hasNext()) { GradebookNode node =
    gnl.getNextGradebookNode(); }

    or
      while (gnl.hasNext()) {
           GradebookNode[] nodes = gnl.getNextGradebookNodes(gnl.available());
      }


    """
    



    def get_next_gradebook_node(self):
        """Gets the next ``GradebookNode`` in this list.

        return: (osid.grading.GradebookNode) - the next
                ``GradebookNode`` in this list. The ``has_next()``
                method should be used to test that a next
                ``GradebookNode`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookNode

    next_gradebook_node = property(fget=get_next_gradebook_node)


    def get_next_gradebook_nodes(self, n):
        """Gets the next set of ``GradebookNode`` elements in this list which must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``GradebookNode`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.grading.GradebookNode) - an array of
                ``GradebookNode`` elements.The length of the array is
                less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookNode


