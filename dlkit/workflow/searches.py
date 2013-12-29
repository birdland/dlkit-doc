from ..osid import searches as osid_searches


class ProcessSearch(osid_searches.OsidSearch):
    """The search interface for governing process searches."""
    def search_among_processes(self, process_ids):
        """Execute this search among the given list of processes.

        :param process_ids: list of processes
        :type process_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``process_ids`` is ``null``

        """
        pass

    def order_process_results(self, process_search_order):
        """Specify an ordering to the search results.

        :param process_search_order: process search order
        :type process_search_order: ``osid.workflow.ProcessSearchOrder``
        :raise: ``NullArgument`` -- ``process_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``process_search_order`` is not of this service

        """
        pass

    def get_process_search_record(self, process_search_record_type):
        """Gets the process search record corresponding to the given process search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param process_search_record_type: a process search record type
        :type process_search_record_type: ``osid.type.Type``
        :return: the process search record
        :rtype: ``osid.workflow.records.ProcessSearchRecord``
        :raise: ``NullArgument`` -- ``process_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(process_search_record_type)`` is ``false``

        """
        return # osid.workflow.records.ProcessSearchRecord


class ProcessSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_processes(self):
        """Gets the process list resulting from a search.

        :return: the process list
        :rtype: ``osid.workflow.ProcessList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.workflow.ProcessList

    processes = property(fget=get_processes)

    def get_process_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the process query inspector
        :rtype: ``osid.workflow.ProcessQueryInspector``

        """
        return # osid.workflow.ProcessQueryInspector

    process_query_inspector = property(fget=get_process_query_inspector)

    def get_process_search_results_record(self, process_search_record_type):
        """Gets the process search results record corresponding to the given process search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param process_search_record_type: a process search record type
        :type process_search_record_type: ``osid.type.Type``
        :return: the process search results record
        :rtype: ``osid.workflow.records.ProcessSearchResultsRecord``
        :raise: ``NullArgument`` -- ``process_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(process_search_record_type)`` is ``false``

        """
        return # osid.workflow.records.ProcessSearchResultsRecord


class StepSearch(osid_searches.OsidSearch):
    """The search interface for governing step searches."""
    def search_among_steps(self, step_ids):
        """Execute this search among the given list of steps.

        :param step_ids: list of steps
        :type step_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``step_ids`` is ``null``

        """
        pass

    def order_step_results(self, step_search_order):
        """Specify an ordering to the search results.

        :param step_search_order: step search order
        :type step_search_order: ``osid.workflow.StepSearchOrder``
        :raise: ``NullArgument`` -- ``step_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``step_search_order`` is not of this service

        """
        pass

    def get_step_search_record(self, step_search_record_type):
        """Gets the step search record corresponding to the given step search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param step_search_record_type: a step search record type
        :type step_search_record_type: ``osid.type.Type``
        :return: the step search record
        :rtype: ``osid.workflow.records.StepSearchRecord``
        :raise: ``NullArgument`` -- ``step_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(step_search_record_type)`` is ``false``

        """
        return # osid.workflow.records.StepSearchRecord


class StepSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_steps(self):
        """Gets the step list resulting from a search.

        :return: the step list
        :rtype: ``osid.workflow.StepList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.workflow.StepList

    steps = property(fget=get_steps)

    def get_step_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the step query inspector
        :rtype: ``osid.workflow.StepQueryInspector``

        """
        return # osid.workflow.StepQueryInspector

    step_query_inspector = property(fget=get_step_query_inspector)

    def get_step_search_results_record(self, step_search_record_type):
        """Gets the step search results record corresponding to the given step search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param step_search_record_type: a step search record type
        :type step_search_record_type: ``osid.type.Type``
        :return: the step search results record
        :rtype: ``osid.workflow.records.StepSearchResultsRecord``
        :raise: ``NullArgument`` -- ``step_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(step_search_record_type)`` is ``false``

        """
        return # osid.workflow.records.StepSearchResultsRecord


class WorkSearch(osid_searches.OsidSearch):
    """The search interface for governing work searches."""
    def search_among_works(self, work_ids):
        """Execute this search among the given list of works.

        :param work_ids: list of works
        :type work_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``work_ids`` is ``null``

        """
        pass

    def order_work_results(self, work_search_order):
        """Specify an ordering to the search results.

        :param work_search_order: work search order
        :type work_search_order: ``osid.workflow.WorkSearchOrder``
        :raise: ``NullArgument`` -- ``work_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``work_search_order`` is not of this service

        """
        pass

    def get_work_search_record(self, work_search_record_type):
        """Gets the work search record corresponding to the given work search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param work_search_record_type: a work search record type
        :type work_search_record_type: ``osid.type.Type``
        :return: the work search record
        :rtype: ``osid.workflow.records.WorkSearchRecord``
        :raise: ``NullArgument`` -- ``work_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(work_search_record_type)`` is ``false``

        """
        return # osid.workflow.records.WorkSearchRecord


class WorkSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_works(self):
        """Gets the work list resulting from a search.

        :return: the work list
        :rtype: ``osid.workflow.WorkList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.workflow.WorkList

    works = property(fget=get_works)

    def get_work_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the work query inspector
        :rtype: ``osid.workflow.WorkQueryInspector``

        """
        return # osid.workflow.WorkQueryInspector

    work_query_inspector = property(fget=get_work_query_inspector)

    def get_work_search_results_record(self, work_search_record_type):
        """Gets the work search results record corresponding to the given work search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param work_search_record_type: a work search record type
        :type work_search_record_type: ``osid.type.Type``
        :return: the work search results record
        :rtype: ``osid.workflow.records.WorkSearchResultsRecord``
        :raise: ``NullArgument`` -- ``work_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(work_search_record_type)`` is ``false``

        """
        return # osid.workflow.records.WorkSearchResultsRecord


class OfficeSearch(osid_searches.OsidSearch):
    """The search interface for governing office searches."""
    def search_among_offices(self, office_ids):
        """Execute this search among the given list of offices.

        :param office_ids: list of offices
        :type office_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``office_ids`` is ``null``

        """
        pass

    def order_office_results(self, office_search_order):
        """Specify an ordering to the search results.

        :param office_search_order: office search order
        :type office_search_order: ``osid.workflow.OfficeSearchOrder``
        :raise: ``NullArgument`` -- ``office_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``office_search_order`` is not of this service

        """
        pass

    def get_office_search_record(self, office_search_record_type):
        """Gets the office search record corresponding to the given office search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param office_search_record_type: a office search record type
        :type office_search_record_type: ``osid.type.Type``
        :return: the office search record
        :rtype: ``osid.workflow.records.OfficeSearchRecord``
        :raise: ``NullArgument`` -- ``office_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(office_search_record_type)`` is ``false``

        """
        return # osid.workflow.records.OfficeSearchRecord


class OfficeSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_offices(self):
        """Gets the office list resulting from a search.

        :return: the office list
        :rtype: ``osid.workflow.OfficeList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.workflow.OfficeList

    offices = property(fget=get_offices)

    def get_office_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the office query inspector
        :rtype: ``osid.workflow.OfficeQueryInspector``

        """
        return # osid.workflow.OfficeQueryInspector

    office_query_inspector = property(fget=get_office_query_inspector)

    def get_office_search_results_record(self, office_search_record_type):
        """Gets the office search results record corresponding to the given office search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param office_search_record_type: a office search record type
        :type office_search_record_type: ``osid.type.Type``
        :return: the office search results record
        :rtype: ``osid.workflow.records.OfficeSearchResultsRecord``
        :raise: ``NullArgument`` -- ``office_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(office_search_record_type)`` is ``false``

        """
        return # osid.workflow.records.OfficeSearchResultsRecord


