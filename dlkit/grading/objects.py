from ..osid import objects as osid_objects
from ..osid import markers as osid_markers


class Grade(osid_objects.OsidObject, osid_markers.Subjugateable):
    """A ``Grade``.

    Grades represent qualified performance levels defined within some
    grading system.

    """
    def get_grade_system_id(self):
        """Gets the ``GradeSystem Id`` in which this grade belongs.

        :return: the grade system ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    grade_system_id = property(fget=get_grade_system_id)

    def get_grade_system(self):
        """Gets the ``GradeSystem`` in which this grade belongs.

        :return: the grade system
        :rtype: ``osid.grading.GradeSystem``

        """
        return # osid.grading.GradeSystem

    grade_system = property(fget=get_grade_system)

    def get_input_score_start_range(self):
        """Gets the low end of the input score range equivalent to this grade.

        :return: the start range
        :rtype: ``decimal``

        """
        return # decimal

    input_score_start_range = property(fget=get_input_score_start_range)

    def get_input_score_end_range(self):
        """Gets the high end of the input score range equivalent to this grade.

        :return: the end range
        :rtype: ``decimal``

        """
        return # decimal

    input_score_end_range = property(fget=get_input_score_end_range)

    def get_output_score(self):
        """Gets the output score for this grade used for calculating cumultives or performing articulation.

        :return: the output score
        :rtype: ``decimal``

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

        :param grade_record_type: the type of the record to retrieve
        :type grade_record_type: ``osid.type.Type``
        :return: the grade record
        :rtype: ``osid.grading.records.GradeRecord``
        :raise: ``NullArgument`` -- ``grade_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_record_type)`` is ``false``

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

        :return: metadata for the input score start range
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    input_score_start_range_metadata = property(fget=get_input_score_start_range_metadata)

    def set_input_score_start_range(self, score):
        """Sets the input score start range.

        :param score: the new start range
        :type score: ``decimal``
        :raise: ``InvalidArgument`` -- ``score`` is invalid
        :raise: ``NoAccess`` -- ``range`` cannot be modified

        """
        pass

    input_score_start_range = property(fset=set_input_score_start_range)

    def clear_input_start_score_range(self):
        """Clears the input score start.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    input_start_score_range = property(fdel=clear_input_start_score_range)

    def get_input_score_end_range_metadata(self):
        """Gets the metadata for the input score start range.

        :return: metadata for the input score start range
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    input_score_end_range_metadata = property(fget=get_input_score_end_range_metadata)

    def set_input_score_end_range(self, score):
        """Sets the input score start range.

        :param score: the new start range
        :type score: ``decimal``
        :raise: ``InvalidArgument`` -- ``score`` is invalid
        :raise: ``NoAccess`` -- ``range`` cannot be modified

        """
        pass

    def clear_input_score_end_range(self):
        """Clears the input score start.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    input_score_end_range = property(fget=set_input_score_end_range, fdel=clear_input_score_end_range)

    def get_output_score_metadata(self):
        """Gets the metadata for the output score start range.

        :return: metadata for the output score start range
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    output_score_metadata = property(fget=get_output_score_metadata)

    def set_output_score(self, score):
        """Sets the output score.

        :param score: the new output score
        :type score: ``decimal``
        :raise: ``InvalidArgument`` -- ``score`` is invalid
        :raise: ``NoAccess`` -- ``score`` cannot be modified

        """
        pass

    def clear_output_score(self):
        """Clears the output score.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    output_score = property(fget=set_output_score, fdel=clear_output_score)

    def get_grade_form_record(self, grade_record_type):
        """Gets the ``GradeFormRecord`` corresponding to the given grade record ``Type``.

        :param grade_record_type: the grade record type
        :type grade_record_type: ``osid.type.Type``
        :return: the grade form record
        :rtype: ``osid.grading.records.GradeFormRecord``
        :raise: ``NullArgument`` -- ``grade_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_record_type)`` is ``false``

        """
        return # osid.grading.records.GradeFormRecord


class GradeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``GradeList`` provides a means for accessing ``Grade`` elements sequentially either one at a time or many at a time.

    Examples: while (gl.hasNext()) { Grade grade = gl.getNextGrade(); }

    or
      while (gl.hasNext()) {
           Grade[] grades = gl.getNextGrades(gl.available());
      }



    """
    def get_next_grade(self):
        """Gets the next ``Grade`` in this list.

        :return: the next ``Grade`` in this list. The ``has_next()`` method should be used to test that a next ``Grade`` is available before calling this method.
        :rtype: ``osid.grading.Grade``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.grading.Grade

    next_grade = property(fget=get_next_grade)

    def get_next_grades(self, n):
        """Gets the next set of ``Grade`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Grade`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Grade`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.grading.Grade``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.grading.Grade


class GradeSystem(osid_objects.OsidObject, osid_markers.Aggregateable):
    """A ``GradeSystem`` represents a grading system.

    The system can be based on assigned Grades or based on a numeric
    scale.

    """
    def is_based_on_grades(self):
        """Tests if the grading system is based on grades.

        :return: true if the grading system is based on grades, ``false`` if the system is a numeric score
        :rtype: ``boolean``

        """
        return # boolean

    def get_grade_ids(self):
        """Gets the grade ``Ids`` in this system ranked from highest to lowest.

        :return: the list of grades ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``IllegalState`` -- ``is_based_on_grades()`` is ``false``

        """
        return # osid.id.IdList

    grade_ids = property(fget=get_grade_ids)

    def get_grades(self):
        """Gets the grades in this system ranked from highest to lowest.

        :return: the list of grades
        :rtype: ``osid.grading.GradeList``
        :raise: ``IllegalState`` -- ``is_based_on_grades()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.grading.GradeList

    grades = property(fget=get_grades)

    def get_lowest_numeric_score(self):
        """Gets the lowest number in a numeric grading system.

        :return: the lowest number
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- ``is_based_on_grades()`` is ``true``

        """
        return # decimal

    lowest_numeric_score = property(fget=get_lowest_numeric_score)

    def get_numeric_score_increment(self):
        """Gets the incremental step.

        :return: the increment
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- ``is_based_on_grades()`` is ``true``

        """
        return # decimal

    numeric_score_increment = property(fget=get_numeric_score_increment)

    def get_highest_numeric_score(self):
        """Gets the highest number in a numeric grading system.

        :return: the highest number
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- ``is_based_on_grades()`` is ``true``

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

        :param grade_system_record_type: the type of the record to retrieve
        :type grade_system_record_type: ``osid.type.Type``
        :return: the grade system record
        :rtype: ``osid.grading.records.GradeSystemRecord``
        :raise: ``NullArgument`` -- ``grade_system_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_system_record_type)`` is ``false``

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

        :return: metadata for the grade-based designation
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    based_on_grades_metadata = property(fget=get_based_on_grades_metadata)

    def set_base_on_grades(self, grades):
        """Sets the grade-based designation.

        :param grades: the grade-based designation
        :type grades: ``boolean``
        :raise: ``InvalidArgument`` -- ``grades`` is invalid
        :raise: ``NoAccess`` -- ``grades`` cannot be modified

        """
        pass

    base_on_grades = property(fset=set_base_on_grades)

    def clear_based_on_grades(self):
        """Clears the based on grades designation.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    based_on_grades = property(fdel=clear_based_on_grades)

    def get_lowest_numeric_score_metadata(self):
        """Gets the metadata for the lowest numeric score.

        :return: metadata for the lowest numeric score
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    lowest_numeric_score_metadata = property(fget=get_lowest_numeric_score_metadata)

    def set_lowest_numeric_score(self, score):
        """Sets the lowest numeric score.

        :param score: the lowest numeric score
        :type score: ``decimal``
        :raise: ``InvalidArgument`` -- ``score`` is invalid
        :raise: ``NoAccess`` -- ``score`` cannot be modified

        """
        pass

    lowest_numeric_score = property(fset=set_lowest_numeric_score)

    def clear_lowest_score(self):
        """Clears the lowest score.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    lowest_score = property(fdel=clear_lowest_score)

    def get_numeric_score_increment_metadata(self):
        """Gets the metadata for the lowest numeric score.

        :return: metadata for the lowest numeric score
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    numeric_score_increment_metadata = property(fget=get_numeric_score_increment_metadata)

    def set_numeric_score_increment(self, increment):
        """Sets the numeric score increment.

        :param increment: the numeric score increment
        :type increment: ``decimal``
        :raise: ``InvalidArgument`` -- ``increment`` is invalid
        :raise: ``NoAccess`` -- ``increment`` cannot be modified

        """
        pass

    def clear_numeric_score_increment(self):
        """Clears the numeric score increment.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    numeric_score_increment = property(fget=set_numeric_score_increment, fdel=clear_numeric_score_increment)

    def get_highest_numeric_score_metadata(self):
        """Gets the metadata for the highest numeric score.

        :return: metadata for the highest numeric score
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    highest_numeric_score_metadata = property(fget=get_highest_numeric_score_metadata)

    def set_highest_numeric_score(self, score):
        """Sets the highest numeric score.

        :param score: the highest numeric score
        :type score: ``decimal``
        :raise: ``InvalidArgument`` -- ``score`` is invalid
        :raise: ``NoAccess`` -- ``score`` cannot be modified

        """
        pass

    def clear_highest_numeric_score(self):
        """Clears the highest numeric score.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    highest_numeric_score = property(fget=set_highest_numeric_score, fdel=clear_highest_numeric_score)

    def get_grade_system_form_record(self, grade_system_record_type):
        """Gets the ``GradeSystemFormRecord`` corresponding to the given grade system record ``Type``.

        :param grade_system_record_type: the grade system record type
        :type grade_system_record_type: ``osid.type.Type``
        :return: the grade system form record
        :rtype: ``osid.grading.records.GradeSystemFormRecord``
        :raise: ``NullArgument`` -- ``grade_system_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_system_record_type)`` is ``false``

        """
        return # osid.grading.records.GradeSystemFormRecord


class GradeSystemList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``GradeSystemList`` provides a means for accessing ``GradeSystem`` elements sequentially either one at a time or many at a time.

    Examples: while (gsl.hasNext()) { GradeSystem system =
    gsl.getNextGradeSystem(); }

    or
      while (gsl.hasNext()) {
           GradeSystem[] systems = gsl.getNextGradeSystems(gsl.available());
      }



    """
    def get_next_grade_system(self):
        """Gets the next ``GradeSystem`` in this list.

        :return: the next ``GradeSystem`` in this list. The ``has_next()`` method should be used to test that a next ``GradeSystem`` is available before calling this method.
        :rtype: ``osid.grading.GradeSystem``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.grading.GradeSystem

    next_grade_system = property(fget=get_next_grade_system)

    def get_next_grade_systems(self, n):
        """Gets the next set of ``GradeSystem`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``GradeSystem`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``GradeSystem`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.grading.GradeSystem``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.grading.GradeSystem


class Gradebook(osid_objects.OsidCatalog):
    """A gradebook defines a collection of grade entries."""
    def get_gradebook_record(self, gradebook_record_type):
        """Gets the gradebook record corresponding to the given ``Gradebook`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``gradebook_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(gradebook_record_type)`` is ``true`` .

        :param gradebook_record_type: a gradebook record type
        :type gradebook_record_type: ``osid.type.Type``
        :return: the gradebook record
        :rtype: ``osid.grading.records.GradebookRecord``
        :raise: ``NullArgument`` -- ``gradebook_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_record_type)`` is ``false``

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

        :param gradebook_record_type: a gradebook record type
        :type gradebook_record_type: ``osid.type.Type``
        :return: the gradebook form record
        :rtype: ``osid.grading.records.GradebookFormRecord``
        :raise: ``NullArgument`` -- ``gradebook_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_record_type)`` is ``false``

        """
        return # osid.grading.records.GradebookFormRecord


class GradebookList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``GradebookList`` provides a means for accessing ``Gradebook`` elements sequentially either one at a time or many at a time.

    Examples: while (gl.hasNext()) { Gradebook gradebook =
    gl.getNextGradebook(); }

    or
      while (gl.hasNext()) {
           Gradebook[] gradebooks = gl.getNextGradebooks(gl.available());
      }



    """
    def get_next_gradebook(self):
        """Gets the next ``Gradebook`` in this list.

        :return: the next ``Gradebook`` in this list. The ``has_next()`` method should be used to test that a next ``Gradebook`` is available before calling this method.
        :rtype: ``osid.grading.Gradebook``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.grading.Gradebook

    next_gradebook = property(fget=get_next_gradebook)

    def get_next_gradebooks(self, n):
        """Gets the next set of ``Gradebook`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Gradebook`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Gradebook`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.grading.Gradebook``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.grading.Gradebook


