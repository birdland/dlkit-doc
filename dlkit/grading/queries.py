
from ..osid import queries as osid_queries


class GradeQuery(osid_queries.OsidObjectQuery, osid_queries.OsidSubjugateableQuery):
    """This is the query for searching gradings.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    



    def match_grade_system_id(self, grade_system_id, match):
        """Sets the grade system ``Id`` for this query.

        arg:    grade_system_id (osid.id.Id): a grade system ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for negative match
        raise:  NullArgument - ``grade_system_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade_system_id_terms(self):
        """Clears the grade system ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system_id_terms = property(fdel=clear_grade_system_id_terms)


    def supports_grade_system_query(self):
        """Tests if a ``GradeSystemQuery`` is available for querying grade systems.

        return: (boolean) - ``true`` if a grade system query is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grade_system_query(self):
        """Gets the query for a grade system.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradeSystemQuery) - the grade system query
        raise:  Unimplemented - ``supports_grade_system_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` is ``true``.*

        """
        return # osid.grading.GradeSystemQuery

    grade_system_query = property(fget=get_grade_system_query)


    def clear_grade_system_terms(self):
        """Clears the grade system terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system_terms = property(fdel=clear_grade_system_terms)


    def match_input_score_start_range(self, start, end, match):
        """Matches grades with the start input score inclusive.

        arg:    start (decimal): start of range
        arg:    end (decimal): end of range
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for negative match
        raise:  InvalidArgument - ``start`` is greater than ``end``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_input_score_start_range_terms(self):
        """Clears the nput score start range terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    input_score_start_range_terms = property(fdel=clear_input_score_start_range_terms)


    def match_input_score_end_range(self, start, end, match):
        """Matches grades with the end input score inclusive.

        arg:    start (decimal): start of range
        arg:    end (decimal): end of range
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for negative match
        raise:  InvalidArgument - ``start`` is greater than ``end``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_input_score_end_range_terms(self):
        """Clears the nput score start range terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    input_score_end_range_terms = property(fdel=clear_input_score_end_range_terms)


    def match_input_score(self, start, end, match):
        """Matches grades with the input score range contained within the given range inclusive.

        arg:    start (decimal): start of range
        arg:    end (decimal): end of range
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for negative match
        raise:  InvalidArgument - ``start`` is greater than ``end``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_input_score_terms(self):
        """Clears the input score start range terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    input_score_terms = property(fdel=clear_input_score_terms)


    def match_output_score(self, start, end, match):
        """Matches grades with the output score contained within the given range inclusive.

        arg:    start (decimal): start of range
        arg:    end (decimal): end of range
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for negative match
        raise:  InvalidArgument - ``start`` is greater than ``end``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_output_score_terms(self):
        """Clears the output score terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    output_score_terms = property(fdel=clear_output_score_terms)


    def match_grade_entry_id(self, grade_entry_id, match):
        """Sets the grade entry ``Id`` for this query.

        arg:    grade_entry_id (osid.id.Id): a grade entry ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for negative match
        raise:  NullArgument - ``grade_entry_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade_entry_id_terms(self):
        """Clears the grade entry ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_entry_id_terms = property(fdel=clear_grade_entry_id_terms)


    def supports_grade_entry_query(self):
        """Tests if a ``GradeEntryQuery`` is available for querying grade entries.

        return: (boolean) - ``true`` if a grade entry query is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grade_entry_query(self):
        """Gets the query for a grade entry.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradeEntryQuery) - the grade entry query
        raise:  Unimplemented - ``supports_grade_entry_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` is ``true``.*

        """
        return # osid.grading.GradeEntryQuery

    grade_entry_query = property(fget=get_grade_entry_query)


    def match_any_grade_entry(self, match):
        """Matches grades that are assigned to any grade entry.

        arg:    match (boolean): ``true`` to match grades used in any
                grade entry, ``false`` to match grades that are not used
                in any grade entries
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade_entry_terms(self):
        """Clears the grade entry terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_entry_terms = property(fdel=clear_grade_entry_terms)


    def match_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query.

        arg:    gradebook_id (osid.id.Id): a gradebook ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for negative match
        raise:  NullArgument - ``gradebook_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_gradebook_id_terms(self):
        """Clears the gradebook ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_id_terms = property(fdel=clear_gradebook_id_terms)


    def supports_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available.

        return: (boolean) - ``true`` if a gradebook query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_gradebook_query(self):
        """Gets the query for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradebookQuery) - the gradebook query
        raise:  Unimplemented - ``supports_gradebook_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        return # osid.grading.GradebookQuery

    gradebook_query = property(fget=get_gradebook_query)


    def clear_gradebook_terms(self):
        """Clears the gradebook terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_terms = property(fdel=clear_gradebook_terms)


    def get_grade_query_record(self, grade_record_type):
        """Gets the grade query record corresponding to the given ``Grade`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        arg:    grade_record_type (osid.type.Type): a grade record type
        return: (osid.grading.records.GradeQueryRecord) - the grade
                query record
        raise:  NullArgument - ``grade_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(grade_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradeQueryRecord


class GradeSystemQuery(osid_queries.OsidObjectQuery, osid_queries.OsidAggregateableQuery):
    """This is the query for searching grade systems.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    



    def match_based_on_grades(self, match):
        """Matches grade systems based on grades.

        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for negative match
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_based_on_grades_terms(self):
        """Clears the grade ``based`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    based_on_grades_terms = property(fdel=clear_based_on_grades_terms)


    def match_grade_id(self, grade_id, match):
        """Sets the grade ``Id`` for this query.

        arg:    grade_id (osid.id.Id): a grade ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for negative match
        raise:  NullArgument - ``grade_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade_id_terms(self):
        """Clears the grade ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_id_terms = property(fdel=clear_grade_id_terms)


    def supports_grade_query(self):
        """Tests if a ``GradeQuery`` is available for querying grades.

        return: (boolean) - ``true`` if a grade query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grade_query(self):
        """Gets the query for a grade.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradeQuery) - the grade query
        raise:  Unimplemented - ``supports_grade_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_query()`` is ``true``.*

        """
        return # osid.grading.GradeQuery

    grade_query = property(fget=get_grade_query)


    def match_any_grade(self, match):
        """Matches grade systems with any grade.

        arg:    match (boolean): ``true`` to match grade systems with
                any grade, ``false`` to match systems with no grade
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade_terms(self):
        """Clears the grade terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_terms = property(fdel=clear_grade_terms)


    def match_lowest_numeric_score(self, start, end, match):
        """Matches grade systems whose low end score falls in the specified range inclusive.

        arg:    start (decimal): low end of range
        arg:    end (decimal): high end of range
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for negative match
        raise:  InvalidArgument - ``end`` is less than ``start``
        raise:  NullArgument - ``grade_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_lowest_numeric_score_terms(self):
        """Clears the lowest numeric score terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    lowest_numeric_score_terms = property(fdel=clear_lowest_numeric_score_terms)


    def match_numeric_score_increment(self, start, end, match):
        """Matches grade systems numeric score increment is between the specified range inclusive.

        arg:    start (decimal): low end of range
        arg:    end (decimal): high end of range
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for negative match
        raise:  InvalidArgument - ``end`` is less than ``start``
        raise:  NullArgument - ``grade_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_numeric_score_increment_terms(self):
        """Clears the numeric score increment terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    numeric_score_increment_terms = property(fdel=clear_numeric_score_increment_terms)


    def match_highest_numeric_score(self, start, end, match):
        """Matches grade systems whose high end score falls in the specified range inclusive.

        arg:    start (decimal): low end of range
        arg:    end (decimal): high end of range
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for negative match
        raise:  InvalidArgument - ``end`` is less than ``start``
        raise:  NullArgument - ``grade_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_highest_numeric_score_terms(self):
        """Clears the highest numeric score terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    highest_numeric_score_terms = property(fdel=clear_highest_numeric_score_terms)


    def match_gradebook_column_id(self, gradebook_column_id, match):
        """Sets the gradebook column ``Id`` for this query.

        arg:    gradebook_column_id (osid.id.Id): a gradebook column
                ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for negative match
        raise:  NullArgument - ``gradebook_column_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_gradebook_column_id_terms(self):
        """Clears the gradebook column ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_id_terms = property(fdel=clear_gradebook_column_id_terms)


    def supports_gradebook_column_query(self):
        """Tests if a ``GradebookColumnQuery`` is available.

        return: (boolean) - ``true`` if a gradebook column query is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_gradebook_column_query(self):
        """Gets the query for a gradebook column.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradebookColumnQuery) - the gradebook
                column query
        raise:  Unimplemented - ``supports_gradebook_column_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnQuery

    gradebook_column_query = property(fget=get_gradebook_column_query)


    def match_any_gradebook_column(self, match):
        """Matches grade systems assigned to any gradebook column.

        arg:    match (boolean): ``true`` to match grade systems mapped
                to any column, ``false`` to match systems mapped to no
                columns
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_gradebook_column_terms(self):
        """Clears the gradebook column terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_terms = property(fdel=clear_gradebook_column_terms)


    def match_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query.

        arg:    gradebook_id (osid.id.Id): a gradebook ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for negative match
        raise:  NullArgument - ``gradebook_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_gradebook_id_terms(self):
        """Clears the gradebook ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_id_terms = property(fdel=clear_gradebook_id_terms)


    def supports_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available.

        return: (boolean) - ``true`` if a gradebook query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_gradebook_query(self):
        """Gets the query for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradebookQuery) - the gradebook query
        raise:  Unimplemented - ``supports_gradebook_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_query()`` is ``true``.*

        """
        return # osid.grading.GradebookQuery

    gradebook_query = property(fget=get_gradebook_query)


    def clear_gradebook_terms(self):
        """Clears the gradebook terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_terms = property(fdel=clear_gradebook_terms)


    def get_grade_system_query_record(self, grade_system_record_type):
        """Gets the grade system query record corresponding to the given ``GradeSystem`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        arg:    grade_system_record_type (osid.type.Type): a grade
                system record type
        return: (osid.grading.records.GradeSystemQueryRecord) - the
                grade system query record
        raise:  NullArgument - ``grade_system_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(grade_system_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradeSystemQueryRecord


class GradeEntryQuery(osid_queries.OsidRelationshipQuery):
    """This is the query for searching grade entries.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    



    def match_gradebook_column_id(self, gradebook_column_id, match):
        """Sets the gradebook column ``Id`` for this query.

        arg:    gradebook_column_id (osid.id.Id): a gradebook column
                ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``gradebook_column_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_gradebook_column_id_terms(self):
        """Clears the gradebook column ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_id_terms = property(fdel=clear_gradebook_column_id_terms)


    def supports_gradebook_column_query(self):
        """Tests if a ``GradebookColumnQuery`` is available for querying creators.

        return: (boolean) - ``true`` if a gradebook column query is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_gradebook_column_query(self):
        """Gets the query for a gradebook column.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradebookColumnQuery) - the gradebook
                column query
        raise:  Unimplemented - ``supports_gradebook_column_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnQuery

    gradebook_column_query = property(fget=get_gradebook_column_query)


    def clear_gradebook_column_terms(self):
        """Clears the gradebook column terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_terms = property(fdel=clear_gradebook_column_terms)


    def match_key_resource_id(self, resource_id, match):
        """Sets the key resource ``Id`` for this query.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``resource_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_key_resource_id_terms(self):
        """Clears the key resource ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    key_resource_id_terms = property(fdel=clear_key_resource_id_terms)


    def supports_key_resource_query(self):
        """Tests if a ``ResourceQUery`` is available for querying key resources.

        return: (boolean) - ``true`` if a resource query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_key_resource_query(self):
        """Gets the query for a key resource.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.resource.ResourceQuery) - the resource query
        raise:  Unimplemented - ``supports_key_resource_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_key_resource_query()`` is ``true``.*

        """
        return # osid.resource.ResourceQuery

    key_resource_query = property(fget=get_key_resource_query)


    def match_any_key_resource(self, match):
        """Matches grade entries with any key resource.

        arg:    match (boolean): ``true`` to match grade entries with
                any key resource, ``false`` to match entries with no key
                resource
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_key_resource_terms(self):
        """Clears the key resource terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    key_resource_terms = property(fdel=clear_key_resource_terms)


    def match_derived(self, match):
        """Matches derived grade entries.

        arg:    match (boolean): ``true`` to match derived grade entries
                , ``false`` to match manual entries
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_derived_terms(self):
        """Clears the derived terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    derived_terms = property(fdel=clear_derived_terms)


    def match_overridden_grade_entry_id(self, grade_entry_id, match):
        """Sets the grade entry ``Id`` for an overridden calculated grade entry.

        arg:    grade_entry_id (osid.id.Id): a grade entry ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``grade_entry_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_overridden_grade_entry_id_terms(self):
        """Clears the overridden grade entry ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    overridden_grade_entry_id_terms = property(fdel=clear_overridden_grade_entry_id_terms)


    def supports_overridden_grade_entry_query(self):
        """Tests if a ``GradeEntry`` is available for querying overridden calculated grade entries.

        return: (boolean) - ``true`` if a grade entry query is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_overridden_grade_entry_query(self):
        """Gets the query for an overridden derived grade entry.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradeEntryQuery) - the grade entry query
        raise:  Unimplemented -
                ``supports_overridden_grade_entry_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_overridden_grade_entry_query()`` is ``true``.*

        """
        return # osid.grading.GradeEntryQuery

    overridden_grade_entry_query = property(fget=get_overridden_grade_entry_query)


    def match_any_overridden_grade_entry(self, match):
        """Matches grade entries overriding any calculated grade entry.

        arg:    match (boolean): ``true`` to match grade entries
                overriding any grade entry, ``false`` to match entries
                not overriding any entry
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_overridden_grade_entry_terms(self):
        """Clears the overridden grade entry terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    overridden_grade_entry_terms = property(fdel=clear_overridden_grade_entry_terms)


    def match_ignored_for_calculations(self, match):
        """Matches grade entries ignored for calculations.

        arg:    match (boolean): ``true`` to match grade entries ignored
                for calculations, ``false`` to match entries used in
                calculations
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_ignored_for_calculations_terms(self):
        """Clears the ignored for calculation entries terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ignored_for_calculations_terms = property(fdel=clear_ignored_for_calculations_terms)


    def match_grade_id(self, grade_id, match):
        """Sets the grade ``Id`` for this query.

        arg:    grade_id (osid.id.Id): a grade ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``grade_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade_id_terms(self):
        """Clears the grade ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_id_terms = property(fdel=clear_grade_id_terms)


    def supports_grade_query(self):
        """Tests if a ``GradeQuery`` is available for querying grades.

        return: (boolean) - ``true`` if a grade query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grade_query(self):
        """Gets the query for a grade.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradeQuery) - the grade query
        raise:  Unimplemented - ``supports_grade_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_query()`` is ``true``.*

        """
        return # osid.grading.GradeQuery

    grade_query = property(fget=get_grade_query)


    def match_any_grade(self, match):
        """Matches grade entries with any grade.

        arg:    match (boolean): ``true`` to match grade entries with
                any grade, ``false`` to match entries with no grade
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade_terms(self):
        """Clears the grade terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_terms = property(fdel=clear_grade_terms)


    def match_score(self, start, end, match):
        """Matches grade entries which score is between the specified score inclusive.

        arg:    start (decimal): start of range
        arg:    end (decimal): end of range
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``end`` is less than ``start``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def match_any_score(self, match):
        """Matches grade entries with any score.

        arg:    match (boolean): ``true`` to match grade entries with
                any score, ``false`` to match entries with no score
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_score_terms(self):
        """Clears the score terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    score_terms = property(fdel=clear_score_terms)


    def match_time_graded(self, start, end, match):
        """Matches grade entries which graded time is between the specified times inclusive.

        arg:    start (osid.calendaring.DateTime): start of range
        arg:    end (osid.calendaring.DateTime): end of range
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``end`` is less than ``start``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_time_graded_terms(self):
        """Clears the time graded terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    time_graded_terms = property(fdel=clear_time_graded_terms)


    def match_grader_id(self, resource_id, match):
        """Sets the agent ``Id`` for this query.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``resource_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grader_id_terms(self):
        """Clears the grader ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grader_id_terms = property(fdel=clear_grader_id_terms)


    def supports_grader_query(self):
        """Tests if a ``ResourceQuery`` is available for querying graders.

        return: (boolean) - ``true`` if a resource query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grader_query(self):
        """Gets the query for an agent.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.resource.ResourceQuery) - the resource query
        raise:  Unimplemented - ``supports_resource_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` is ``true``.*

        """
        return # osid.resource.ResourceQuery

    grader_query = property(fget=get_grader_query)


    def match_any_grader(self, match):
        """Matches grade entries with any grader.

        arg:    match (boolean): ``true`` to match grade entries with
                any grader, ``false`` to match entries with no grader
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grader_terms(self):
        """Clears the grader terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grader_terms = property(fdel=clear_grader_terms)


    def match_grading_agent_id(self, agent_id, match):
        """Sets the grading agent ``Id`` for this query.

        arg:    agent_id (osid.id.Id): an agent ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``agent_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grading_agent_id_terms(self):
        """Clears the grader ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grading_agent_id_terms = property(fdel=clear_grading_agent_id_terms)


    def supports_grading_agent_query(self):
        """Tests if an ``AgentQuery`` is available for querying grading agents.

        return: (boolean) - ``true`` if an agent query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grading_agent_query(self):
        """Gets the query for an agent.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.authentication.AgentQuery) - the agent query
        raise:  Unimplemented - ``supports_grading_agent_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grading_agent_query()`` is ``true``.*

        """
        return # osid.authentication.AgentQuery

    grading_agent_query = property(fget=get_grading_agent_query)


    def match_any_grading_agent(self, match):
        """Matches grade entries with any grading agent.

        arg:    match (boolean): ``true`` to match grade entries with
                any grading agent, ``false`` to match entries with no
                grading agent
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grading_agent_terms(self):
        """Clears the grading agent terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grading_agent_terms = property(fdel=clear_grading_agent_terms)


    def match_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query.

        arg:    gradebook_id (osid.id.Id): a gradebook ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``gradebook_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_gradebook_id_terms(self):
        """Clears the gradebook ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_id_terms = property(fdel=clear_gradebook_id_terms)


    def supports_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available for querying resources.

        return: (boolean) - ``true`` if a gradebook query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_gradebook_query(self):
        """Gets the query for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradebookQuery) - the gradebook query
        raise:  Unimplemented - ``supports_gradebook_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_query()`` is ``true``.*

        """
        return # osid.grading.GradebookQuery

    gradebook_query = property(fget=get_gradebook_query)


    def clear_gradebook_terms(self):
        """Clears the gradebook terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_terms = property(fdel=clear_gradebook_terms)


    def get_grade_entry_query_record(self, grade_entry_record_type):
        """Gets the grade entry query record corresponding to the given ``GradeEntry`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        arg:    grade_entry_record_type (osid.type.Type): a grade entry
                record type
        return: (osid.grading.records.GradeEntryQueryRecord) - the grade
                entry query record
        raise:  NullArgument - ``grade_entry_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(grade_entry_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradeEntryQueryRecord


class GradebookColumnQuery(osid_queries.OsidObjectQuery):
    """This is the query for searching gradings.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    



    def match_grade_system_id(self, grade_system_id, match):
        """Sets the grade system ``Id`` for this query.

        arg:    grade_system_id (osid.id.Id): a grade system ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``grade_system_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade_system_id_terms(self):
        """Clears the grade system ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system_id_terms = property(fdel=clear_grade_system_id_terms)


    def supports_grade_system_query(self):
        """Tests if a ``GradeSystemQuery`` is available for querying grade systems.

        return: (boolean) - ``true`` if a grade system query is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grade_system_query(self):
        """Gets the query for a grade system.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradeSystemQuery) - the grade system query
        raise:  Unimplemented - ``supports_grade_system_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` is ``true``.*

        """
        return # osid.grading.GradeSystemQuery

    grade_system_query = property(fget=get_grade_system_query)


    def match_any_grade_system(self, match):
        """Matches gradebook columns with any grade system assigned.

        arg:    match (boolean): ``true`` to match columns with any
                grade system, ``false`` to match columns with no grade
                system
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade_system_terms(self):
        """Clears the grade system terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system_terms = property(fdel=clear_grade_system_terms)


    def match_grade_entry_id(self, grade_entry_id, match):
        """Sets the grade entry ``Id`` for this query.

        arg:    grade_entry_id (osid.id.Id): a grade entry ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``grade_entry_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade_entry_id_terms(self):
        """Clears the grade entry ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_entry_id_terms = property(fdel=clear_grade_entry_id_terms)


    def supports_grade_entry_query(self):
        """Tests if a ``GradeEntryQuery`` is available for querying grade entries.

        return: (boolean) - ``true`` if a grade entry query is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grade_entry_query(self):
        """Gets the query for a grade entry.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradeEntryQuery) - the grade entry query
        raise:  Unimplemented - ``supports_grade_entry_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` is ``true``.*

        """
        return # osid.grading.GradeEntryQuery

    grade_entry_query = property(fget=get_grade_entry_query)


    def match_any_grade_entry(self, match):
        """Matches gradebook columns with any grade entry assigned.

        arg:    match (boolean): ``true`` to match columns with any
                grade entry, ``false`` to match columns with no grade
                entries
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade_entry_terms(self):
        """Clears the grade entry terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_entry_terms = property(fdel=clear_grade_entry_terms)


    def supports_gradebook_column_summary_query(self):
        """Tests if a ``GradebookColumnSummaryQuery`` is available for querying grade systems.

        return: (boolean) - ``true`` if a gradebook column summary query
                interface is available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_gradebook_column_summary_query(self):
        """Gets the query interface for a gradebook column summary.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradebookColumnSummaryQuery) - the
                gradebook column summary query
        raise:  Unimplemented -
                ``supports_gradebook_column_summary_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_summary_query()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnSummaryQuery

    gradebook_column_summary_query = property(fget=get_gradebook_column_summary_query)


    def clear_gradebook_column_summary_terms(self):
        """Clears the gradebook column summary terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_summary_terms = property(fdel=clear_gradebook_column_summary_terms)


    def match_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query.

        arg:    gradebook_id (osid.id.Id): a gradebook ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``gradebook_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_gradebook_id_terms(self):
        """Clears the gradebook ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_id_terms = property(fdel=clear_gradebook_id_terms)


    def supports_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available for querying grade systems.

        return: (boolean) - ``true`` if a gradebook query interface is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_gradebook_query(self):
        """Gets the query interface for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradebookQuery) - the gradebook query
        raise:  Unimplemented - ``supports_gradebook_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_query()`` is ``true``.*

        """
        return # osid.grading.GradebookQuery

    gradebook_query = property(fget=get_gradebook_query)


    def clear_gradebook_terms(self):
        """Clears the gradebook terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_terms = property(fdel=clear_gradebook_terms)


    def get_gradebook_column_query_record(self, gradebook_column_record_type):
        """Gets the gradebook column query record corresponding to the given ``GradebookColumn`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        arg:    gradebook_column_record_type (osid.type.Type): a
                gradebook column record type
        return: (osid.grading.records.GradebookColumnQueryRecord) - the
                gradebook column query record
        raise:  NullArgument - ``gradebook_column_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(gradebook_column_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradebookColumnQueryRecord


class GradebookColumnSummaryQuery(osid_queries.OsidRuleQuery):
    """This is the query for searching gradebook column summaries.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    



    def match_gradebook_column_id(self, gradebook_column_id, match):
        """Sets the gradebook column ``Id`` for this query.

        arg:    gradebook_column_id (osid.id.Id): a gradeboo column
                ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``gradebook_column_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_gradebook_column_id_terms(self):
        """Clears the gradebook column ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_id_terms = property(fdel=clear_gradebook_column_id_terms)


    def supports_gradebook_column_query(self):
        """Tests if a ``GradebookColumnQuery`` is available for querying gradebook column.

        return: (boolean) - ``true`` if a gradebook column query is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_gradebook_column_query(self):
        """Gets the query for a gradebook column.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradebookColumnQuery) - the gradebook
                column query
        raise:  Unimplemented - ``supports_gradebook_column_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnQuery

    gradebook_column_query = property(fget=get_gradebook_column_query)


    def match_any_gradebook_column(self, match):
        """Matches gradebook column derivations with any gradebookc olumn.

        arg:    match (boolean): ``true`` to match gradebook column
                derivations with any gradebook column, ``false`` to
                match gradebook column derivations with no gradebook
                columns
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_gradebook_column_terms(self):
        """Clears the source grade system terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_terms = property(fdel=clear_gradebook_column_terms)


    def match_mean(self, low, high, match):
        """Matches a mean between the given values inclusive.

        arg:    low (decimal): low end of range
        arg:    high (decimal): high end of range
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``low`` is greater than ``high``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_mean_terms(self):
        """Clears the mean terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    mean_terms = property(fdel=clear_mean_terms)


    def match_minimum_mean(self, value, match):
        """Matches a mean greater than or equal to the given value.

        arg:    value (decimal): minimum value
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_minimum_mean_terms(self):
        """Clears the minimum mean terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    minimum_mean_terms = property(fdel=clear_minimum_mean_terms)


    def match_median(self, low, high, match):
        """Matches a median between the given values inclusive.

        arg:    low (decimal): low end of range
        arg:    high (decimal): high end of range
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``low`` is greater than ``high``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_median_terms(self):
        """Clears the median terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    median_terms = property(fdel=clear_median_terms)


    def match_minimum_median(self, value, match):
        """Matches a median greater than or equal to the given value.

        arg:    value (decimal): minimum value
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_minimum_median_terms(self):
        """Clears the minimum median terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    minimum_median_terms = property(fdel=clear_minimum_median_terms)


    def match_mode(self, low, high, match):
        """Matches a mode between the given values inclusive.

        arg:    low (decimal): low end of range
        arg:    high (decimal): high end of range
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``low`` is greater than ``high``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_mode_terms(self):
        """Clears the mode terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    mode_terms = property(fdel=clear_mode_terms)


    def match_minimum_mode(self, value, match):
        """Matches a mode greater than or equal to the given value.

        arg:    value (decimal): minimum value
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_minimum_mode_terms(self):
        """Clears the minimum mode terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    minimum_mode_terms = property(fdel=clear_minimum_mode_terms)


    def match_rms(self, low, high, match):
        """Matches a root mean square between the given values inclusive.

        arg:    low (decimal): low end of range
        arg:    high (decimal): high end of range
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``low`` is greater than ``high``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_rms_terms(self):
        """Clears the root mean square terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rms_terms = property(fdel=clear_rms_terms)


    def match_minimum_rms(self, value, match):
        """Matches a root mean square greater than or equal to the given value.

        arg:    value (decimal): minimum value
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_minimum_rms_terms(self):
        """Clears the minimum RMS terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    minimum_rms_terms = property(fdel=clear_minimum_rms_terms)


    def match_standard_deviation(self, low, high, match):
        """Matches a standard deviation mean square between the given values inclusive.

        arg:    low (decimal): low end of range
        arg:    high (decimal): high end of range
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``low`` is greater than ``high``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_standard_deviation_terms(self):
        """Clears the standard deviation terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    standard_deviation_terms = property(fdel=clear_standard_deviation_terms)


    def match_minimum_standard_deviation(self, value, match):
        """Matches a standard deviation greater than or equal to the given value.

        arg:    value (decimal): minimum value
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_minimum_standard_deviation_terms(self):
        """Clears the minimum standard deviation terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    minimum_standard_deviation_terms = property(fdel=clear_minimum_standard_deviation_terms)


    def match_sum(self, low, high, match):
        """Matches a sum mean square between the given values inclusive.

        arg:    low (decimal): low end of range
        arg:    high (decimal): high end of range
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``low`` is greater than ``high``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_sum_terms(self):
        """Clears the sum terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    sum_terms = property(fdel=clear_sum_terms)


    def match_minimum_sum(self, value, match):
        """Matches a sum greater than or equal to the given value.

        arg:    value (decimal): minimum value
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_minimum_sum_terms(self):
        """Clears the minimum sum terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    minimum_sum_terms = property(fdel=clear_minimum_sum_terms)


    def match_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query.

        arg:    gradebook_id (osid.id.Id): a gradebook ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``gradebook_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_gradebook_id_terms(self):
        """Clears the gradebook ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_id_terms = property(fdel=clear_gradebook_id_terms)


    def supports_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available.

        return: (boolean) - ``true`` if a gradebook query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_gradebook_query(self):
        """Gets the query for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradebookQuery) - the gradebook query
        raise:  Unimplemented - ``supports_gradebook_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        return # osid.grading.GradebookQuery

    gradebook_query = property(fget=get_gradebook_query)


    def clear_gradebook_terms(self):
        """Clears the gradebook terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_terms = property(fdel=clear_gradebook_terms)


    def get_gradebook_column_summary_query_record(self, gradebook_column_summary_record_type):
        """Gets the gradebook column summary query record corresponding to the given ``GradebookColumnSummary`` record
        ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        arg:    gradebook_column_summary_record_type (osid.type.Type): a
                gradebook column summary record type
        return: (osid.grading.records.GradebookColumnSummaryQueryRecord)
                - the gradebook column summary query record
        raise:  NullArgument - ``gradebook_column_summary_record_type``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(gradebook_column_summary_record_type)`
                ` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradebookColumnSummaryQueryRecord


class GradebookQuery(osid_queries.OsidCatalogQuery):
    """This is the query for searching gradebooks.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    



    def match_grade_system_id(self, grade_system_id, match):
        """Sets the grade system ``Id`` for this query.

        arg:    grade_system_id (osid.id.Id): a grade system ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``grade_system_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade_system_id_terms(self):
        """Clears the grade system ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system_id_terms = property(fdel=clear_grade_system_id_terms)


    def supports_grade_system_query(self):
        """Tests if a ``GradeSystemQuery`` is available.

        return: (boolean) - ``true`` if a grade system query is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grade_system_query(self):
        """Gets the query for a grade system.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradeSystemQuery) - the grade system query
        raise:  Unimplemented - ``supports_grade_system_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` is ``true``.*

        """
        return # osid.grading.GradeSystemQuery

    grade_system_query = property(fget=get_grade_system_query)


    def match_any_grade_system(self, match):
        """Matches gradebooks that have any grade system.

        arg:    match (boolean): ``true`` to match gradebooks with any
                grade system, ``false`` to match gradebooks with no
                grade system
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade_system_terms(self):
        """Clears the grade system terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system_terms = property(fdel=clear_grade_system_terms)


    def match_grade_entry_id(self, grade_entry_id, match):
        """Sets the grade entry ``Id`` for this query.

        arg:    grade_entry_id (osid.id.Id): a grade entry ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``grade_entry_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade_entry_id_terms(self):
        """Clears the grade entry ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_entry_id_terms = property(fdel=clear_grade_entry_id_terms)


    def supports_grade_entry_query(self):
        """Tests if a ``GradeEntryQuery`` is available.

        return: (boolean) - ``true`` if a grade entry query is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grade_entry_query(self):
        """Gets the query for a grade entry.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradeEntryQuery) - the grade entry query
        raise:  Unimplemented - ``supports_grade_entry_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` is ``true``.*

        """
        return # osid.grading.GradeEntryQuery

    grade_entry_query = property(fget=get_grade_entry_query)


    def match_any_grade_entry(self, match):
        """Matches gradebooks that have any grade entry.

        arg:    match (boolean): ``true`` to match gradebooks with any
                grade entry, ``false`` to match gradebooks with no grade
                entry
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade_entry_terms(self):
        """Clears the grade entry terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_entry_terms = property(fdel=clear_grade_entry_terms)


    def match_gradebook_column_id(self, gradebook_column_id, match):
        """Sets the gradebook column ``Id`` for this query.

        arg:    gradebook_column_id (osid.id.Id): a gradebook column
                ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``gradebook_column_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_gradebook_column_id_terms(self):
        """Clears the gradebook column ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_id_terms = property(fdel=clear_gradebook_column_id_terms)


    def supports_gradebook_column_query(self):
        """Tests if a ``GradebookColumnQuery`` is available.

        return: (boolean) - ``true`` if a gradebook column query is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_gradebook_column_query(self):
        """Gets the query for a gradebook column.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradebookColumnQuery) - the gradebook
                column query
        raise:  Unimplemented - ``supports_gradebook_column_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnQuery

    gradebook_column_query = property(fget=get_gradebook_column_query)


    def match_any_gradebook_column(self, match):
        """Matches gradebooks that have any column.

        arg:    match (boolean): ``true`` to match gradebooks with any
                column, ``false`` to match gradebooks with no column
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_gradebook_column_terms(self):
        """Clears the gradebook column terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    gradebook_column_terms = property(fdel=clear_gradebook_column_terms)


    def match_ancestor_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query to match gradebooks that have the specified gradebook as an
        ancestor.

        arg:    gradebook_id (osid.id.Id): a gradebook ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``gradebook_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_ancestor_gradebook_id_terms(self):
        """Clears the ancestor gradebook ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_gradebook_id_terms = property(fdel=clear_ancestor_gradebook_id_terms)


    def supports_ancestor_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available.

        return: (boolean) - ``true`` if a gradebook query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_ancestor_gradebook_query(self):
        """Gets the query for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradebookQuery) - the gradebook query
        raise:  Unimplemented - ``supports_ancestor_gradebook_query()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_gradebook_query()`` is ``true``.*

        """
        return # osid.grading.GradebookQuery

    ancestor_gradebook_query = property(fget=get_ancestor_gradebook_query)


    def match_any_ancestor_gradebook(self, match):
        """Matches gradebook with any ancestor.

        arg:    match (boolean): ``true`` to match gradebooks with any
                ancestor, ``false`` to match root gradebooks
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_ancestor_gradebook_terms(self):
        """Clears the ancestor gradebook terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_gradebook_terms = property(fdel=clear_ancestor_gradebook_terms)


    def match_descendant_gradebook_id(self, gradebook_id, match):
        """Sets the gradebook ``Id`` for this query to match gradebooks that have the specified gradebook as a
        descendant.

        arg:    gradebook_id (osid.id.Id): a gradebook ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``gradebook_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_descendant_gradebook_id_terms(self):
        """Clears the descendant gradebook ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_gradebook_id_terms = property(fdel=clear_descendant_gradebook_id_terms)


    def supports_descendant_gradebook_query(self):
        """Tests if a ``GradebookQuery`` is available.

        return: (boolean) - ``true`` if a gradebook query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_descendant_gradebook_query(self):
        """Gets the query for a gradebook.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradebookQuery) - the gradebook query
        raise:  Unimplemented -
                ``supports_descendant_gradebook_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_descendant_gradebook_query()`` is ``true``.*

        """
        return # osid.grading.GradebookQuery

    descendant_gradebook_query = property(fget=get_descendant_gradebook_query)


    def match_any_descendant_gradebook(self, match):
        """Matches gradebook with any descendant.

        arg:    match (boolean): ``true`` to match gradebooks with any
                descendant, ``false`` to match leaf gradebooks
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_descendant_gradebook_terms(self):
        """Clears the descendant gradebook terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_gradebook_terms = property(fdel=clear_descendant_gradebook_terms)


    def get_gradebook_query_record(self, gradebook_record_type):
        """Gets the gradebook query record corresponding to the given ``Gradebook`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        arg:    gradebook_record_type (osid.type.Type): a gradebook
                record type
        return: (osid.grading.records.GradebookQueryRecord) - the
                gradebook query record
        raise:  NullArgument - ``gradebook_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(gradebook_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradebookQueryRecord


