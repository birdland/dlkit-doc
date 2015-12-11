
from ..osid import searches as osid_searches


class ObjectiveSearch(osid_searches.OsidSearch):
    """``ObjectiveSearch`` defines the interface for specifying objective search options."""
    



    def search_among_objectives(self, objective_ids):
        """Execute this search among the given list of objectives.

        arg:    objective_ids (osid.id.IdList): list of objectives
        raise:  NullArgument - ``objective_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def order_objective_results(self, objective_search_order):
        """Specify an ordering to the search results.

        arg:    objective_search_order
                (osid.learning.ObjectiveSearchOrder): objective search
                order
        raise:  NullArgument - ``objective_search_order`` is ``null``
        raise:  Unsupported - ``objective_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def get_objective_search_record(self, objective_search_record_type):
        """Gets the objective search record corresponding to the given objective search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    objective_search_record_type (osid.type.Type): an
                objective search record type
        return: (osid.learning.records.ObjectiveSearchRecord) - the
                objective search record
        raise:  NullArgument - ``objective_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_search_record_type(objective_search_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.records.ObjectiveSearchRecord


class ObjectiveSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    



    def get_objectives(self):
        """Gets the objective list resulting from the search.

        return: (osid.learning.ObjectiveList) - the objective list
        raise:  IllegalState - list already retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList

    objectives = property(fget=get_objectives)


    def get_objective_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.learning.ObjectiveQueryInspector) - the query
                inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveQueryInspector

    objective_query_inspector = property(fget=get_objective_query_inspector)


    def get_objective_search_results_record(self, objective_search_record_type):
        """Gets the objective search results record corresponding to the given objective search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    objective_search_record_type (osid.type.Type): an
                objective search record type
        return: (osid.learning.records.ObjectiveSearchResultsRecord) -
                the objective search results record
        raise:  NullArgument - ``objective_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_search_record_type(objective_search_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.records.ObjectiveSearchResultsRecord


class ActivitySearch(osid_searches.OsidSearch):
    """``ActivitySearch`` defines the interface for specifying activity search options."""
    



    def search_among_activities(self, activity_ids):
        """Execute this search among the given list of activities.

        arg:    activity_ids (osid.id.IdList): list of activities
        raise:  NullArgument - ``activity_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def order_activity_results(self, activitiesearch_order):
        """Specify an ordering to the search results.

        arg:    activitiesearch_order
                (osid.learning.ActivitySearchOrder): activity search
                order
        raise:  NullArgument - ``activitiesearch_order`` is ``null``
        raise:  Unsupported - ``activitiesearch_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def get_activity_search_record(self, activitiesearch_record_type):
        """Gets the activity record corresponding to the given activity search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    activitiesearch_record_type (osid.type.Type): an
                activity search record type
        return: (osid.learning.records.ActivitySearchRecord) - the
                activity search record
        raise:  NullArgument - ``activitiesearch_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_search_record_type(activitiesearch_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.records.ActivitySearchRecord


class ActivitySearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    



    def get_activities(self):
        """Gets the activity list resulting from the search.

        return: (osid.learning.ActivityList) - the activity list
        raise:  IllegalState - list already retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ActivityList

    activities = property(fget=get_activities)


    def get_activity_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.learning.ActivityQueryInspector) - the query
                inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ActivityQueryInspector

    activity_query_inspector = property(fget=get_activity_query_inspector)


    def get_activity_search_results_record(self, activitiesearch_record_type):
        """Gets the activity search results record corresponding to the given activity search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    activitiesearch_record_type (osid.type.Type): an
                activity search record type
        return: (osid.learning.records.ActivitySearchResultsRecord) -
                the activity search results record
        raise:  NullArgument - ``activitiesearch_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_search_record_type(activitiesearch_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.records.ActivitySearchResultsRecord


class ObjectiveBankSearch(osid_searches.OsidSearch):
    """The interface for governing objective bank searches."""
    



    def search_among_objective_banks(self, objective_bank_ids):
        """Execute this search among the given list of objective banks.

        arg:    objective_bank_ids (osid.id.IdList): list of objective
                banks
        raise:  NullArgument - ``objective bank_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def order_objective_bank_results(self, objective_bank_search_order):
        """Specify an ordering to the search results.

        arg:    objective_bank_search_order
                (osid.learning.ObjectiveBankSearchOrder): objective bank
                search order
        raise:  NullArgument - ``objective_bank_search_order`` is
                ``null``
        raise:  Unsupported - ``objective_bank_search_order`` is not of
                this service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def get_objective_bank_search_record(self, objective_bank_search_record_type):
        """Gets the objective bank search record corresponding to the given objective bank search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    objective_bank_search_record_type (osid.type.Type): an
                objective bank search record type
        return: (osid.learning.records.ObjectiveBankSearchRecord) - the
                objective bank search record
        raise:  NullArgument - ``objective_bank_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_search_record_type(objective
                bank_search_record_type)`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.records.ObjectiveBankSearchRecord


class ObjectiveBankSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    



    def get_objective_banks(self):
        """Gets the objective bank list resulting from the search.

        return: (osid.learning.ObjectiveBankList) - the objective bank
                list
        raise:  IllegalState - list already retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    objective_banks = property(fget=get_objective_banks)


    def get_objective_bank_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.learning.ObjectiveBankQueryInspector) - the query
                inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankQueryInspector

    objective_bank_query_inspector = property(fget=get_objective_bank_query_inspector)


    def get_objective_bank_search_results_record(self, objective_bank_search_record_type):
        """Gets the objective bank search results record corresponding to the given objective bank search record
        ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    objective_bank_search_record_type (osid.type.Type): an
                objective bank search record type
        return: (osid.learning.records.ObjectiveBankSearchResultsRecord)
                - the objective bank search results record
        raise:  NullArgument - ``objective_bank_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_search_record_type(objective
                bank_search_record_type)`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.records.ObjectiveBankSearchResultsRecord


