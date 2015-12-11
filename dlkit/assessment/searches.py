
from ..osid import searches as osid_searches


class ItemSearch(osid_searches.OsidSearch):
    """``ItemSearch`` defines the interface for specifying item search options."""
    



    def search_among_items(self, item_ids):
        """Execute this search among the given list of items.

        arg:    item_ids (osid.id.IdList): list of items
        raise:  NullArgument - ``item_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def order_item_results(self, item_search_order):
        """Specify an ordering to the search results.

        arg:    item_search_order (osid.assessment.ItemSearchOrder):
                item search order
        raise:  NullArgument - ``item_search_order`` is ``null``
        raise:  Unsupported - ``item_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def get_item_search_record(self, item_search_record_type):
        """Gets the item search record corresponding to the given item search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    item_search_record_type (osid.type.Type): an item search
                record type
        return: (osid.assessment.records.ItemSearchRecord) - the item
                search record
        raise:  NullArgument - ``item_search_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(item_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.ItemSearchRecord


class ItemSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    



    def get_items(self):
        """Gets the item list resulting from the search.

        return: (osid.assessment.ItemList) - the item list
        raise:  IllegalState - the item list has already been retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.ItemList

    items = property(fget=get_items)


    def get_item_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.assessment.ItemQueryInspector) - the query
                inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.ItemQueryInspector

    item_query_inspector = property(fget=get_item_query_inspector)


    def get_item_search_results_record(self, item_search_record_type):
        """Gets the record corresponding to the given item search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    item_search_record_type (osid.type.Type): an item search
                record type
        return: (osid.assessment.records.ItemSearchResultsRecord) - the
                item search results record
        raise:  NullArgument - ``item_search_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(item_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.ItemSearchResultsRecord


class AssessmentSearch(osid_searches.OsidSearch):
    """``AssessmentSearch`` defines the interface for specifying assessment search options."""
    



    def search_among_assessments(self, assessment_ids):
        """Execute this search among the given list of assessments.

        arg:    assessment_ids (osid.id.IdList): list of assessments
        raise:  NullArgument - ``assessment_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def order_assessment_results(self, assessment_search_order):
        """Specify an ordering to the search results.

        arg:    assessment_search_order
                (osid.assessment.AssessmentSearchOrder): assessment
                search order
        raise:  NullArgument - ``assessment_search_order`` is ``null``
        raise:  Unsupported - ``assessment_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def get_assessment_search_record(self, assessment_search_record_type):
        """Gets the assessment search record corresponding to the given assessment search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    assessment_search_record_type (osid.type.Type): an
                assessment search record type
        return: (osid.assessment.records.AssessmentSearchRecord) - the
                assessment search record
        raise:  NullArgument - ``assessment_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.AssessmentSearchRecord


class AssessmentSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    



    def get_assessments(self):
        """Gets the assessment list resulting from the search.

        return: (osid.assessment.AssessmentList) - the assessment list
        raise:  IllegalState - the assessment list has already been
                retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.AssessmentList

    assessments = property(fget=get_assessments)


    def get_assessment_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.assessment.AssessmentQueryInspector) - the query
                inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.AssessmentQueryInspector

    assessment_query_inspector = property(fget=get_assessment_query_inspector)


    def get_assessment_search_results_record(self, assessment_search_record_type):
        """Gets the assessment search order record corresponding to the given assessment search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    assessment_search_record_type (osid.type.Type): an
                assessment search record type
        return: (osid.assessment.records.AssessmentSearchResultsRecord)
                - the assessment search results record
        raise:  NullArgument - ``assessment_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.AssessmentSearchResultsRecord


class AssessmentOfferedSearch(osid_searches.OsidSearch):
    """``AssessmentOfferedSearch`` defines the interface for specifying assessment search options."""
    



    def search_among_assessments_offered(self, assessment_offrered_ids):
        """Execute this search among the given list of assessments.

        arg:    assessment_offrered_ids (osid.id.IdList): list of
                assessments offered
        raise:  NullArgument - ``assessment_offered_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def order_assessment_offered_results(self, assessment_offered_search_order):
        """Specify an ordering to the search results.

        arg:    assessment_offered_search_order
                (osid.assessment.AssessmentOfferedSearchOrder):
                assessment offered search order
        raise:  NullArgument - ``assessment_offered_search_order`` is
                ``null``
        raise:  Unsupported - ``assessment_offered_search_order`` is not
                of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def get_assessment_offered_search_record(self, assessment_offered_search_record_type):
        """Gets the assessment search record corresponding to the given assessment offered search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    assessment_offered_search_record_type (osid.type.Type):
                an assessment offered search record type
        return: (osid.assessment.records.AssessmentOfferedSearchRecord)
                - the assessment offered search
        raise:  NullArgument - ``assessment_offered_search_record_type``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_offered_search_record_type)
                `` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.AssessmentOfferedSearchRecord


class AssessmentOfferedSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    



    def get_assessments_offered(self):
        """Gets the assessment offered list resulting from the search.

        return: (osid.assessment.AssessmentOfferedList) - the assessment
                offered list
        raise:  IllegalState - the assessment offered list has already
                been retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.AssessmentOfferedList

    assessments_offered = property(fget=get_assessments_offered)


    def get_assessment_offered_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.assessment.AssessmentOfferedQueryInspector) - the
                query inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.AssessmentOfferedQueryInspector

    assessment_offered_query_inspector = property(fget=get_assessment_offered_query_inspector)


    def get_assessment_offered_search_results_record(self, assessment_offered_search_record_type):
        """Gets the assessment offered search results record corresponding to the given assessment offered search record
        ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    assessment_offered_search_record_type (osid.type.Type):
                an assessment offered search record type
        return:
                (osid.assessment.records.AssessmentOfferedSearchResultsR
                ecord) - the assessment offered search results record
        raise:  NullArgument - ``assessment_offered_search_record_type``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_offered_search_record_type)
                `` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.AssessmentOfferedSearchResultsRecord


class AssessmentTakenSearch(osid_searches.OsidSearch):
    """``AssessmentTakenSearch`` defines the interface for specifying assessment search options."""
    



    def search_among_assessments_taken(self, assessment_taken_ids):
        """Execute this search among the given list of assessments.

        arg:    assessment_taken_ids (osid.id.IdList): list of
                assessments taken
        raise:  NullArgument - ``assessment_taken_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def order_assessment_taken_results(self, assessment_taken_search_order):
        """Specify an ordering to the search results.

        arg:    assessment_taken_search_order
                (osid.assessment.AssessmentTakenSearchOrder): assessment
                offered search order
        raise:  NullArgument - ``assessment_taken_search_order`` is
                ``null``
        raise:  Unsupported - ``assessment_taken_search_order`` is not
                of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def get_assessment_taken_search_record(self, assessment_taken_search_record_type):
        """Gets the assessment taken search record corresponding to the given assessment taken search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    assessment_taken_search_record_type (osid.type.Type): an
                assessment taken search record type
        return: (osid.assessment.records.AssessmentTakenSearchRecord) -
                the assessment taken search record
        raise:  NullArgument - ``assessment_taken_search_record_type``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_taken_search_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.AssessmentTakenSearchRecord


class AssessmentTakenSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    



    def get_assessments_taken(self):
        """Gets the assessment taken list resulting from the search.

        return: (osid.assessment.AssessmentTakenList) - the assessment
                taken list
        raise:  IllegalState - the assessment taken list has already
                been retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.AssessmentTakenList

    assessments_taken = property(fget=get_assessments_taken)


    def get_assessment_taken_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.assessment.AssessmentTakenQueryInspector) - the
                query inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.AssessmentTakenQueryInspector

    assessment_taken_query_inspector = property(fget=get_assessment_taken_query_inspector)


    def get_assessment_taken_search_results_record(self, assessment_taken_search_record_type):
        """Gets the assessment taken record corresponding to the given assessment taken search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    assessment_taken_search_record_type (osid.type.Type): an
                assessment taken search record type
        return:
                (osid.assessment.records.AssessmentTakenSearchResultsRec
                ord) - the assessment taken search results record
        raise:  NullArgument - ``assessment_taken_search_record_type``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_taken_search_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.AssessmentTakenSearchResultsRecord


class BankSearch(osid_searches.OsidSearch):
    """The interface for governing bank searches."""
    



    def search_among_banks(self, bank_ids):
        """Execute this search among the given list of banks.

        arg:    bank_ids (osid.id.IdList): list of banks
        raise:  NullArgument - ``bank_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def order_bank_results(self, bank_search_order):
        """Specify an ordering to the search results.

        arg:    bank_search_order (osid.assessment.BankSearchOrder):
                bank search order
        raise:  NullArgument - ``bank_search_order`` is ``null``
        raise:  Unsupported - ``bank_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def get_bank_search_record(self, bank_search_record_type):
        """Gets the bank search record corresponding to the given bank search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    bank_search_record_type (osid.type.Type): a bank search
                record type
        return: (osid.assessment.records.BankSearchRecord) - the bank
                search record
        raise:  NullArgument - ``bank_search_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(bank_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.BankSearchRecord


class BankSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    



    def get_banks(self):
        """Gets the bank list resulting from a search.

        return: (osid.assessment.BankList) - the bank list
        raise:  IllegalState - the bank list has already been retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.BankList

    banks = property(fget=get_banks)


    def get_bank_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.assessment.BankQueryInspector) - the query
                inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.BankQueryInspector

    bank_query_inspector = property(fget=get_bank_query_inspector)


    def get_bank_search_results_record(self, bank_search_record_type):
        """Gets the bank search results record corresponding to the given bank search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    bank_search_record_type (osid.type.Type): a bank search
                record type
        return: (osid.assessment.records.BankSearchResultsRecord) - the
                bank search results record
        raise:  NullArgument - ``bank_search_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(bank_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.BankSearchResultsRecord


