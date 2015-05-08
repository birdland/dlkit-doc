from ..osid import queries as osid_queries


class GradeQuery(osid_queries.OsidObjectQuery, osid_queries.OsidSubjugateableQuery):
    """This is the query for searching gradings.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    def match_grade_system_id(self, grade_system_id, match):
        """Sets the grade system ``Id`` for this query.

        :param grade_system_id: a grade system ``Id``
        :type grade_system_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``

        """
        pass

    def clear_grade_system_id_terms(self):
        """Clears the grade system ``Id`` terms."""
        pass

    grade_system_id_terms = property(fdel=clear_grade_system_id_terms)

    def supports_grade_system_query(self):
        """Tests if a ``GradeSystemQuery`` is available for querying grade systems.

        :return: ``true`` if a grade system query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_grade_system_query(self):
        """Gets the query for a grade system.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade system query
        :rtype: ``osid.grading.GradeSystemQuery``
        :raise: ``Unimplemented`` -- ``supports_grade_system_query()`` is ``false``

        """
        return # osid.grading.GradeSystemQuery

    grade_system_query = property(fget=get_grade_system_query)

    def clear_grade_system_terms(self):
        """Clears the grade system terms."""
        pass

    grade_system_terms = property(fdel=clear_grade_system_terms)

    def match_input_score_start_range(self, start, end, match):
        """Matches grades with the start input score inclusive.

        :param start: start of range
        :type start: ``decimal``
        :param end: end of range
        :type end: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``

        """
        pass

    def clear_input_score_start_range_terms(self):
        """Clears the nput score start range terms."""
        pass

    input_score_start_range_terms = property(fdel=clear_input_score_start_range_terms)

    def match_input_score_end_range(self, start, end, match):
        """Matches grades with the end input score inclusive.

        :param start: start of range
        :type start: ``decimal``
        :param end: end of range
        :type end: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``

        """
        pass

    def clear_input_score_end_range_terms(self):
        """Clears the nput score start range terms."""
        pass

    input_score_end_range_terms = property(fdel=clear_input_score_end_range_terms)

    def match_input_score(self, start, end, match):
        """Matches grades with the input score range contained within the given range inclusive.

        :param start: start of range
        :type start: ``decimal``
        :param end: end of range
        :type end: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``

        """
        pass

    def clear_input_score_terms(self):
        """Clears the input score start range terms."""
        pass

    input_score_terms = property(fdel=clear_input_score_terms)

    def match_output_score(self, start, end, match):
        """Matches grades with the output score contained within the given range inclusive.

        :param start: start of range
        :type start: ``decimal``
        :param end: end of range
        :type end: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``

        """
        pass

    def clear_output_score_terms(self):
        """Clears the output score terms."""
        pass

    output_score_terms = property(fdel=clear_output_score_terms)

    def match_grade_entry_id(self, grade_entry_id, match):
        """Sets the grade entry ``Id`` for this query.

        :param grade_entry_id: a grade entry ``Id``
        :type grade_entry_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_entry_id`` is ``null``

        """
        pass

    def clear_grade_entry_id_terms(self):
        """Clears the grade entry ``Id`` terms."""
        pass

    grade_entry_id_terms = property(fdel=clear_grade_entry_id_terms)

    def supports_grade_entry_query(self):
        """Tests if a ``GradeEntryQuery`` is available for querying grade entries.

        :return: ``true`` if a grade entry query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_grade_entry_query(self):
        """Gets the query for a grade entry.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade entry query
        :rtype: ``osid.grading.GradeEntryQuery``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_query()`` is ``false``

        """
        return # osid.grading.GradeEntryQuery

    grade_entry_query = property(fget=get_grade_entry_query)

    def match_any_grade_entry(self, match):
        """Matches grades that are assigned to any grade entry.

        :param match: ``true`` to match grades used in any grade entry, ``false`` to match grades that are not used in any grade entries
        :type match: ``boolean``

        """
        pass

    def clear_grade_entry_terms(self):
        """Clears the grade entry terms."""
        pass

    grade_entry_terms = property(fdel=clear_grade_entry_terms)

    def match_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query.

        :param gradebook_id: a gradebook ``Id``
        :type gradebook_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``

        """
        pass

    def clear_gradebook_id_terms(self):
        """Clears the gradebook ``Id`` terms."""
        pass

    gradebook_id_terms = property(fdel=clear_gradebook_id_terms)

    def supports_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available.

        :return: ``true`` if a gradebook query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_gradebook_query(self):
        """Gets the query for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook query
        :rtype: ``osid.grading.GradebookQuery``
        :raise: ``Unimplemented`` -- ``supports_gradebook_query()`` is ``false``

        """
        return # osid.grading.GradebookQuery

    gradebook_query = property(fget=get_gradebook_query)

    def clear_gradebook_terms(self):
        """Clears the gradebook terms."""
        pass

    gradebook_terms = property(fdel=clear_gradebook_terms)

    def get_grade_query_record(self, grade_record_type):
        """Gets the grade query record corresponding to the given ``Grade`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param grade_record_type: a grade record type
        :type grade_record_type: ``osid.type.Type``
        :return: the grade query record
        :rtype: ``osid.grading.records.GradeQueryRecord``
        :raise: ``NullArgument`` -- ``grade_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_record_type)`` is ``false``

        """
        return # osid.grading.records.GradeQueryRecord


class GradeSystemQuery(osid_queries.OsidObjectQuery, osid_queries.OsidAggregateableQuery):
    """This is the query for searching grade systems.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    def match_based_on_grades(self, match):
        """Matches grade systems based on grades.

        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``

        """
        pass

    def clear_based_on_grades_terms(self):
        """Clears the grade ``based`` terms."""
        pass

    based_on_grades_terms = property(fdel=clear_based_on_grades_terms)

    def match_grade_id(self, grade_id, match):
        """Sets the grade ``Id`` for this query.

        :param grade_id: a grade ``Id``
        :type grade_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        """
        pass

    def clear_grade_id_terms(self):
        """Clears the grade ``Id`` terms."""
        pass

    grade_id_terms = property(fdel=clear_grade_id_terms)

    def supports_grade_query(self):
        """Tests if a ``GradeQuery`` is available for querying grades.

        :return: ``true`` if a grade query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_grade_query(self):
        """Gets the query for a grade.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade query
        :rtype: ``osid.grading.GradeQuery``
        :raise: ``Unimplemented`` -- ``supports_grade_query()`` is ``false``

        """
        return # osid.grading.GradeQuery

    grade_query = property(fget=get_grade_query)

    def match_any_grade(self, match):
        """Matches grade systems with any grade.

        :param match: ``true`` to match grade systems with any grade, ``false`` to match systems with no grade
        :type match: ``boolean``

        """
        pass

    def clear_grade_terms(self):
        """Clears the grade terms."""
        pass

    grade_terms = property(fdel=clear_grade_terms)

    def match_lowest_numeric_score(self, start, end, match):
        """Matches grade systems whose low end score falls in the specified range inclusive.

        :param start: low end of range
        :type start: ``decimal``
        :param end: high end of range
        :type end: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        """
        pass

    def clear_lowest_numeric_score_terms(self):
        """Clears the lowest numeric score terms."""
        pass

    lowest_numeric_score_terms = property(fdel=clear_lowest_numeric_score_terms)

    def match_numeric_score_increment(self, start, end, match):
        """Matches grade systems numeric score increment is between the specified range inclusive.

        :param start: low end of range
        :type start: ``decimal``
        :param end: high end of range
        :type end: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        """
        pass

    def clear_numeric_score_increment_terms(self):
        """Clears the numeric score increment terms."""
        pass

    numeric_score_increment_terms = property(fdel=clear_numeric_score_increment_terms)

    def match_highest_numeric_score(self, start, end, match):
        """Matches grade systems whose high end score falls in the specified range inclusive.

        :param start: low end of range
        :type start: ``decimal``
        :param end: high end of range
        :type end: ``decimal``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``

        """
        pass

    def clear_highest_numeric_score_terms(self):
        """Clears the highest numeric score terms."""
        pass

    highest_numeric_score_terms = property(fdel=clear_highest_numeric_score_terms)

    def match_gradebook_column_id(self, gradebook_column_id, match):
        """Sets the gradebook column ``Id`` for this query.

        :param gradebook_column_id: a gradebook column ``Id``
        :type gradebook_column_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``

        """
        pass

    def clear_gradebook_column_id_terms(self):
        """Clears the gradebook column ``Id`` terms."""
        pass

    gradebook_column_id_terms = property(fdel=clear_gradebook_column_id_terms)

    def supports_gradebook_column_query(self):
        """Tests if a ``GradebookColumnQuery`` is available.

        :return: ``true`` if a gradebook column query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_gradebook_column_query(self):
        """Gets the query for a gradebook column.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook column query
        :rtype: ``osid.grading.GradebookColumnQuery``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` is ``false``

        """
        return # osid.grading.GradebookColumnQuery

    gradebook_column_query = property(fget=get_gradebook_column_query)

    def match_any_gradebook_column(self, match):
        """Matches grade systems assigned to any gradebook column.

        :param match: ``true`` to match grade systems mapped to any column, ``false`` to match systems mapped to no columns
        :type match: ``boolean``

        """
        pass

    def clear_gradebook_column_terms(self):
        """Clears the gradebook column terms."""
        pass

    gradebook_column_terms = property(fdel=clear_gradebook_column_terms)

    def match_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query.

        :param gradebook_id: a gradebook ``Id``
        :type gradebook_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``

        """
        pass

    def clear_gradebook_id_terms(self):
        """Clears the gradebook ``Id`` terms."""
        pass

    gradebook_id_terms = property(fdel=clear_gradebook_id_terms)

    def supports_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available.

        :return: ``true`` if a gradebook query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_gradebook_query(self):
        """Gets the query for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook query
        :rtype: ``osid.grading.GradebookQuery``
        :raise: ``Unimplemented`` -- ``supports_gradebook_query()`` is ``false``

        """
        return # osid.grading.GradebookQuery

    gradebook_query = property(fget=get_gradebook_query)

    def clear_gradebook_terms(self):
        """Clears the gradebook terms."""
        pass

    gradebook_terms = property(fdel=clear_gradebook_terms)

    def get_grade_system_query_record(self, grade_system_record_type):
        """Gets the grade system query record corresponding to the given ``GradeSystem`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param grade_system_record_type: a grade system record type
        :type grade_system_record_type: ``osid.type.Type``
        :return: the grade system query record
        :rtype: ``osid.grading.records.GradeSystemQueryRecord``
        :raise: ``NullArgument`` -- ``grade_system_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(grade_system_record_type)`` is ``false``

        """
        return # osid.grading.records.GradeSystemQueryRecord


class GradebookQuery(osid_queries.OsidCatalogQuery):
    """This is the query for searching gradebooks.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def match_grade_system_id(self, grade_system_id, match):
        """Sets the grade system ``Id`` for this query.

        :param grade_system_id: a grade system ``Id``
        :type grade_system_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``

        """
        pass

    def clear_grade_system_id_terms(self):
        """Clears the grade system ``Id`` terms."""
        pass

    grade_system_id_terms = property(fdel=clear_grade_system_id_terms)

    def supports_grade_system_query(self):
        """Tests if a ``GradeSystemQuery`` is available.

        :return: ``true`` if a grade system query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_grade_system_query(self):
        """Gets the query for a grade system.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade system query
        :rtype: ``osid.grading.GradeSystemQuery``
        :raise: ``Unimplemented`` -- ``supports_grade_system_query()`` is ``false``

        """
        return # osid.grading.GradeSystemQuery

    grade_system_query = property(fget=get_grade_system_query)

    def match_any_grade_system(self, match):
        """Matches gradebooks that have any grade system.

        :param match: ``true`` to match gradebooks with any grade system, ``false`` to match gradebooks with no grade system
        :type match: ``boolean``

        """
        pass

    def clear_grade_system_terms(self):
        """Clears the grade system terms."""
        pass

    grade_system_terms = property(fdel=clear_grade_system_terms)

    def match_grade_entry_id(self, grade_entry_id, match):
        """Sets the grade entry ``Id`` for this query.

        :param grade_entry_id: a grade entry ``Id``
        :type grade_entry_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``grade_entry_id`` is ``null``

        """
        pass

    def clear_grade_entry_id_terms(self):
        """Clears the grade entry ``Id`` terms."""
        pass

    grade_entry_id_terms = property(fdel=clear_grade_entry_id_terms)

    def supports_grade_entry_query(self):
        """Tests if a ``GradeEntryQuery`` is available.

        :return: ``true`` if a grade entry query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_grade_entry_query(self):
        """Gets the query for a grade entry.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the grade entry query
        :rtype: ``osid.grading.GradeEntryQuery``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_query()`` is ``false``

        """
        return # osid.grading.GradeEntryQuery

    grade_entry_query = property(fget=get_grade_entry_query)

    def match_any_grade_entry(self, match):
        """Matches gradebooks that have any grade entry.

        :param match: ``true`` to match gradebooks with any grade entry, ``false`` to match gradebooks with no grade entry
        :type match: ``boolean``

        """
        pass

    def clear_grade_entry_terms(self):
        """Clears the grade entry terms."""
        pass

    grade_entry_terms = property(fdel=clear_grade_entry_terms)

    def match_gradebook_column_id(self, gradebook_column_id, match):
        """Sets the gradebook column ``Id`` for this query.

        :param gradebook_column_id: a gradebook column ``Id``
        :type gradebook_column_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``

        """
        pass

    def clear_gradebook_column_id_terms(self):
        """Clears the gradebook column ``Id`` terms."""
        pass

    gradebook_column_id_terms = property(fdel=clear_gradebook_column_id_terms)

    def supports_gradebook_column_query(self):
        """Tests if a ``GradebookColumnQuery`` is available.

        :return: ``true`` if a gradebook column query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_gradebook_column_query(self):
        """Gets the query for a gradebook column.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook column query
        :rtype: ``osid.grading.GradebookColumnQuery``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` is ``false``

        """
        return # osid.grading.GradebookColumnQuery

    gradebook_column_query = property(fget=get_gradebook_column_query)

    def match_any_gradebook_column(self, match):
        """Matches gradebooks that have any column.

        :param match: ``true`` to match gradebooks with any column, ``false`` to match gradebooks with no column
        :type match: ``boolean``

        """
        pass

    def clear_gradebook_column_terms(self):
        """Clears the gradebook column terms."""
        pass

    gradebook_column_terms = property(fdel=clear_gradebook_column_terms)

    def match_ancestor_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query to match gradebooks that have the specified gradebook as an ancestor.

        :param gradebook_id: a gradebook ``Id``
        :type gradebook_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``

        """
        pass

    def clear_ancestor_gradebook_id_terms(self):
        """Clears the ancestor gradebook ``Id`` terms."""
        pass

    ancestor_gradebook_id_terms = property(fdel=clear_ancestor_gradebook_id_terms)

    def supports_ancestor_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available.

        :return: ``true`` if a gradebook query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_ancestor_gradebook_query(self):
        """Gets the query for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook query
        :rtype: ``osid.grading.GradebookQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_gradebook_query()`` is ``false``

        """
        return # osid.grading.GradebookQuery

    ancestor_gradebook_query = property(fget=get_ancestor_gradebook_query)

    def match_any_ancestor_gradebook(self, match):
        """Matches gradebook with any ancestor.

        :param match: ``true`` to match gradebooks with any ancestor, ``false`` to match root gradebooks
        :type match: ``boolean``

        """
        pass

    def clear_ancestor_gradebook_terms(self):
        """Clears the ancestor gradebook terms."""
        pass

    ancestor_gradebook_terms = property(fdel=clear_ancestor_gradebook_terms)

    def match_descendant_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query to match gradebooks that have the specified gradebook as a descendant.

        :param gradebook_id: a gradebook ``Id``
        :type gradebook_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``

        """
        pass

    def clear_descendant_gradebook_id_terms(self):
        """Clears the descendant gradebook ``Id`` terms."""
        pass

    descendant_gradebook_id_terms = property(fdel=clear_descendant_gradebook_id_terms)

    def supports_descendant_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available.

        :return: ``true`` if a gradebook query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_descendant_gradebook_query(self):
        """Gets the query for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the gradebook query
        :rtype: ``osid.grading.GradebookQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_gradebook_query()`` is ``false``

        """
        return # osid.grading.GradebookQuery

    descendant_gradebook_query = property(fget=get_descendant_gradebook_query)

    def match_any_descendant_gradebook(self, match):
        """Matches gradebook with any descendant.

        :param match: ``true`` to match gradebooks with any descendant, ``false`` to match leaf gradebooks
        :type match: ``boolean``

        """
        pass

    def clear_descendant_gradebook_terms(self):
        """Clears the descendant gradebook terms."""
        pass

    descendant_gradebook_terms = property(fdel=clear_descendant_gradebook_terms)

    def get_gradebook_query_record(self, gradebook_record_type):
        """Gets the gradebook query record corresponding to the given ``Gradebook`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param gradebook_record_type: a gradebook record type
        :type gradebook_record_type: ``osid.type.Type``
        :return: the gradebook query record
        :rtype: ``osid.grading.records.GradebookQueryRecord``
        :raise: ``NullArgument`` -- ``gradebook_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_record_type)`` is ``false``

        """
        return # osid.grading.records.GradebookQueryRecord


