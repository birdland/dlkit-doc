
from ..osid import searches as osid_searches


class GradeSystemSearch(osid_searches.OsidSearch):
    """The interface for governing grade system searches."""
    



    def search_among_grade_systems(self, grade_system_ids):
        """Execute this search among the given list of grade systems.

        arg:    grade_system_ids (osid.id.IdList): list of grade systems
        raise:  NullArgument - ``grade_system_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def order_grade_system_results(self, grade_system_search_order):
        """Specify an ordering to the search results.

        arg:    grade_system_search_order
                (osid.grading.GradeSystemSearchOrder): grade system
                search order
        raise:  NullArgument - ``grade_system_search_order`` is ``null``
        raise:  Unsupported - ``grade_system_search_order`` is not of
                this service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def get_grade_system_search_record(self, grade_system_search_record_type):
        """Gets the grade system search record corresponding to the given grade system search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    grade_system_search_record_type (osid.type.Type): a
                grade system search record type
        return: (osid.grading.records.GradeSystemSearchRecord) - the
                grade system search record
        raise:  NullArgument - ``grade_system_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(grade_system_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradeSystemSearchRecord


class GradeSystemSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    



    def get_grade_systems(self):
        """Gets the grade system list resulting from the search.

        return: (osid.grading.GradeSystemList) - the grade system list
        raise:  IllegalState - list already retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystemList

    grade_systems = property(fget=get_grade_systems)


    def get_grade_system_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.grading.GradeSystemQueryInspector) - the grade
                system query inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystemQueryInspector

    grade_system_query_inspector = property(fget=get_grade_system_query_inspector)


    def get_grade_system_search_results_record(self, grade_system_search_record_type):
        """Gets the grade system search results record corresponding to the given grade system search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    grade_system_search_record_type (osid.type.Type): a
                grade system search record type
        return: (osid.grading.records.GradeSystemSearchResultsRecord) -
                the grade system search results record
        raise:  NullArgument - ``grade_system_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(grade_system_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradeSystemSearchResultsRecord


class GradeEntrySearch(osid_searches.OsidSearch):
    """``GradeEntrySearch`` defines the interface for specifying package search options."""
    



    def search_among_grade_entries(self, grade_entry_ids):
        """Execute this search among the given list of grade entries.

        arg:    grade_entry_ids (osid.id.IdList): list of grade entries
        raise:  NullArgument - ``grade_entry_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def order_grade_entry_results(self, grade_entry_search_order):
        """Specify an ordering to the search results.

        arg:    grade_entry_search_order
                (osid.grading.GradeEntrySearchOrder): package search
                order
        raise:  NullArgument - ``grade_entry_search_order`` is ``null``
        raise:  Unsupported - ``grade_entry_search_order`` is not of
                this service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def get_grade_entry_search_record(self, grade_entry_search_record_type):
        """Gets the grade entry search record corresponding to the given package search record ``Type``.

        This method ie used to retrieve an object implementing the
        requested record.

        arg:    grade_entry_search_record_type (osid.type.Type): a grade
                entry search record type
        return: (osid.grading.records.GradeEntrySearchRecord) - the
                grade entry search record
        raise:  NullArgument - ``grade_entry_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(grade_entry_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradeEntrySearchRecord


class GradeEntrySearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    



    def get_grade_entries(self):
        """Gets the package list resulting from the search.

        return: (osid.grading.GradeEntryList) - the grade entry list
        raise:  IllegalState - list already retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryList

    grade_entries = property(fget=get_grade_entries)


    def get_grade_entry_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.grading.GradeEntryQueryInspector) - the grade
                entry query inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryQueryInspector

    grade_entry_query_inspector = property(fget=get_grade_entry_query_inspector)


    def get_grade_entry_search_results_record(self, grade_entry_search_record_type):
        """Gets the grade entry search results record corresponding to the given grade entry search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    grade_entry_search_record_type (osid.type.Type): a grade
                entry search record type
        return: (osid.grading.records.GradeEntrySearchResultsRecord) -
                the grade entry search results record
        raise:  NullArgument - ``grade_entry_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(grade_entry_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradeEntrySearchResultsRecord


class GradebookColumnSearch(osid_searches.OsidSearch):
    """``GradebookColumnSearch`` defines the interface for specifying grading search options."""
    



    def search_among_gradebook_columns(self, gradebook_column_ids):
        """Execute this search among the given list of gradebook columns.

        arg:    gradebook_column_ids (osid.id.IdList): list of gradebook
                columns
        raise:  NullArgument - ``gradebook_column_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def order_gradebook_column_results(self, gradebook_column_search_order):
        """Specify an ordering to the search results.

        arg:    gradebook_column_search_order
                (osid.grading.GradebookColumnSearchOrder): gradebook
                column search order
        raise:  NullArgument - ``gradebook_column_search_order`` is
                ``null``
        raise:  Unsupported - ``gradebook_column_search_order`` is not
                of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def get_gradebook_column_search_record(self, gradebook_column_search_record_type):
        """Gets the gradebook column search record corresponding to the given gradebook column search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    gradebook_column_search_record_type (osid.type.Type): a
                gradebook column search record type
        return: (osid.grading.records.GradebookColumnSearchRecord) - the
                gradebook column search record
        raise:  NullArgument - ``gradebook_column_search_record_type``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(gradebook_column_search_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradebookColumnSearchRecord


class GradebookColumnSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    



    def get_gradebook_columns(self):
        """Gets the gradebook column list resulting from the search.

        return: (osid.grading.GradebookColumnList) - the gradebook
                column list
        raise:  IllegalState - list already retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookColumnList

    gradebook_columns = property(fget=get_gradebook_columns)


    def get_gradebook_column_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.grading.GradebookColumnQueryInspector) - the
                gradebook column query inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookColumnQueryInspector

    gradebook_column_query_inspector = property(fget=get_gradebook_column_query_inspector)


    def get_gradebook_column_search_results_record(self, gradebook_column_search_record_type):
        """Gets the gradebook column search results record corresponding to the given gradebook column search record
        ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    gradebook_column_search_record_type (osid.type.Type): a
                gradebook column search record type
        return:
                (osid.grading.records.GradebookColumnSearchResultsRecord
                ) - the gradebook column search results record
        raise:  NullArgument - ``gradebook_column_search_record_type``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(gradebook_column_search_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradebookColumnSearchResultsRecord


class GradebookSearch(osid_searches.OsidSearch):
    """The interface for governing gradebook searches."""
    



    def search_among_gradebooks(self, gradebook_ids):
        """Execute this search among the given list of gradebooks.

        arg:    gradebook_ids (osid.id.IdList): list of gradebooks
        raise:  NullArgument - ``gradebook_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def order_gradebook_results(self, gradebook_search_order):
        """Specify an ordering to the search results.

        arg:    gradebook_search_order
                (osid.grading.GradebookSearchOrder): gradebook search
                order
        raise:  NullArgument - ``gradebook_search_order`` is ``null``
        raise:  Unsupported - ``gradebook_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def get_gradebook_search_record(self, gradebook_search_record_type):
        """Gets the gradebook search record corresponding to the given gradebook search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    gradebook_search_record_type (osid.type.Type): a
                gradebook search record type
        return: (osid.grading.records.GradebookSearchRecord) - the
                gradebook search record
        raise:  NullArgument - ``gradebook_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(gradebook_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradebookSearchRecord


class GradebookSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    



    def get_gradebooks(self):
        """Gets the gradebook list resulting from the search.

        return: (osid.grading.GradebookList) - the gradebook list
        raise:  IllegalState - list already retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

    gradebooks = property(fget=get_gradebooks)


    def get_gradebook_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.grading.GradebookQueryInspector) - the gradebook
                query inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookQueryInspector

    gradebook_query_inspector = property(fget=get_gradebook_query_inspector)


    def get_gradebook_search_results_record(self, gradebook_search_record_type):
        """Gets the gradebook search results record corresponding to the given gradebook search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    gradebook_search_record_type (osid.type.Type): a
                gradebook search record type
        return: (osid.grading.records.GradebookSearchResultsRecord) -
                the gradebook search results record
        raise:  NullArgument - ``gradebook_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(gradebook_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradebookSearchResultsRecord


