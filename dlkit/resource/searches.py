
from ..osid import searches as osid_searches


class ResourceSearch(osid_searches.OsidSearch):
    """The search interface for governing resource searches."""
    



    def search_among_resources(self, resource_ids):
        """Execute this search among the given list of resources.

        arg:    resource_ids (osid.id.IdList): list of resource ``Ids``
        raise:  NullArgument - ``resource_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def order_resource_results(self, resource_search_order):
        """Specify an ordering to the search results.

        arg:    resource_search_order
                (osid.resource.ResourceSearchOrder): resource search
                order
        raise:  NullArgument - ``order`` is ``null``
        raise:  Unsupported - ``order`` is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def get_resource_search_record(self, resource_search_record_type):
        """Gets the resource search record corresponding to the given resource search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    resource_search_record_type (osid.type.Type): a resource
                search record type
        return: (osid.resource.records.ResourceSearchRecord) - the
                resource search record
        raise:  NullArgument - ``resource_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type_type(resource_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.records.ResourceSearchRecord


class ResourceSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    



    def get_resources(self):
        """Gets the resource list resulting from a search.

        return: (osid.resource.ResourceList) - the resource list
        raise:  IllegalState - list already retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceList

    resources = property(fget=get_resources)


    def get_resource_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.resource.ResourceQueryInspector) - the resource
                query inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceQueryInspector

    resource_query_inspector = property(fget=get_resource_query_inspector)


    def get_resource_search_results_record(self, resource_search_record_type):
        """Gets the resource search results record corresponding to the given resource search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    resource_search_record_type (osid.type.Type): a resource
                search record type
        return: (osid.resource.records.ResourceSearchResultsRecord) -
                the resource search results record
        raise:  NullArgument - ``resource_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type_type(resource_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.records.ResourceSearchResultsRecord


class BinSearch(osid_searches.OsidSearch):
    """The interface for governing bin searches."""
    



    def search_among_bins(self, bin_ids):
        """Execute this search among the given list of bins.

        arg:    bin_ids (osid.id.IdList): list of bins
        raise:  NullArgument - ``bin_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def order_bin_results(self, bin_search_order):
        """Specify an ordering to the search results.

        arg:    bin_search_order (osid.resource.BinSearchOrder): bin
                search order
        raise:  NullArgument - ``bin_search_order`` is ``null``
        raise:  Unsupported - ``bin_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def get_bin_search_record(self, bin_search_record_type):
        """Gets the bin search record corresponding to the given bin search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    bin_search_record_type (osid.type.Type): a bin search
                record type
        return: (osid.resource.records.BinSearchRecord) - the bin search
                record
        raise:  NullArgument - ``bin_search_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(bin_search_record_type)`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.records.BinSearchRecord


class BinSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    



    def get_bins(self):
        """Gets the bin list resulting from the search.

        return: (osid.resource.BinList) - the bin list
        raise:  IllegalState - list already retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinList

    bins = property(fget=get_bins)


    def get_bin_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        return: (osid.resource.BinQueryInspector) - the bin query
                inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinQueryInspector

    bin_query_inspector = property(fget=get_bin_query_inspector)


    def get_bin_search_results_record(self, bin_search_record_type):
        """Gets the bin search results record corresponding to the given bin search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    bin_search_record_type (osid.type.Type): a bin search
                record type
        return: (osid.resource.records.BinSearchResultsRecord) - the bin
                search results record
        raise:  NullArgument - ``bin_search_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(bin_search_record_type)`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.records.BinSearchResultsRecord


