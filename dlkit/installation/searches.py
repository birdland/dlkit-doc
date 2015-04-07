from ..osid import searches as osid_searches


class PackageSearch(osid_searches.OsidSearch):
    """``PackageSearch`` defines the interface for specifying package search options."""
    def search_among_packages(self, package_ids):
        """Execute this search among the given list of packages.

        :param package_ids: list of packages
        :type package_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``package_ids`` is ``null``

        """
        pass

    def order_package_results(self, package_search_order):
        """Specify an ordering to the search results.

        :param package_search_order: package search order
        :type package_search_order: ``osid.installation.PackageSearchOrder``
        :raise: ``NullArgument`` -- ``package_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``package_search_order`` is not of this service

        """
        pass

    def get_package_search_record(self, package_search_record_type):
        """Gets the package search record corresponding to the given package search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param package_search_record_type: a package search record type
        :type package_search_record_type: ``osid.type.Type``
        :return: the package search record
        :rtype: ``osid.installation.records.PackageSearchRecord``
        :raise: ``NullArgument`` -- ``package_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(package_search_record_type)`` is ``false``

        """
        return # osid.installation.records.PackageSearchRecord


class PackageSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_packages(self):
        """Gets the package list resulting from the search.

        :return: the package list
        :rtype: ``osid.installation.PackageList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.installation.PackageList

    packages = property(fget=get_packages)

    def get_package_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the package query inspector
        :rtype: ``osid.installation.PackageQueryInspector``

        """
        return # osid.installation.PackageQueryInspector

    package_query_inspector = property(fget=get_package_query_inspector)

    def get_package_search_results_record(self, package_search_record_type):
        """Gets the package search results record corresponding to the given package search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param package_search_record_type: a package search record type
        :type package_search_record_type: ``osid.type.Type``
        :return: the package search results record
        :rtype: ``osid.installation.records.PackageSearchResultsRecord``
        :raise: ``NullArgument`` -- ``package_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(package_search_record_type)`` is ``false``

        """
        return # osid.installation.records.PackageSearchResultsRecord


class DepotSearch(osid_searches.OsidSearch):
    """The interface for governing depot searches."""
    def search_among_depots(self, depot_ids):
        """Execute this search among the given list of depots.

        :param depot_ids: list of depots
        :type depot_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``depot_ids`` is ``null``

        """
        pass

    def order_depot_results(self, depot_search_order):
        """Specify an ordering to the search results.

        :param depot_search_order: depot search order
        :type depot_search_order: ``osid.installation.DepotSearchOrder``
        :raise: ``NullArgument`` -- ``depot_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``depot_search_order`` is not of this service

        """
        pass

    def get_depot_search_record(self, depot_search_record_type):
        """Gets the depot search record corresponding to the given depot search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param depot_search_record_type: a depot search record type
        :type depot_search_record_type: ``osid.type.Type``
        :return: the depot search record
        :rtype: ``osid.installation.records.DepotSearchRecord``
        :raise: ``NullArgument`` -- ``depot_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(depot_search_record_type)`` is ``false``

        """
        return # osid.installation.records.DepotSearchRecord


class DepotSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_depots(self):
        """Gets the depot list resulting from the search.

        :return: the depot list
        :rtype: ``osid.installation.DepotList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.installation.DepotList

    depots = property(fget=get_depots)

    def get_depot_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the depot query inspector
        :rtype: ``osid.installation.DepotQueryInspector``

        """
        return # osid.installation.DepotQueryInspector

    depot_query_inspector = property(fget=get_depot_query_inspector)

    def get_depot_search_results_record(self, depot_search_record_type):
        """Gets the depot search results record corresponding to the given depot search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param depot_search_record_type: a depot search record type
        :type depot_search_record_type: ``osid.type.Type``
        :return: the depot search results record
        :rtype: ``osid.installation.records.DepotSearchResultsRecord``
        :raise: ``NullArgument`` -- ``depot_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(depot_search_record_type)`` is ``false``

        """
        return # osid.installation.records.DepotSearchResultsRecord


class InstallationSearch(osid_searches.OsidSearch):
    """``InstallationSearch`` defines the interface for specifying installation search options."""
    def search_among_installations(self, installation_ids):
        """Execute this search among the given list of installations.

        :param installation_ids: list of installations
        :type installation_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``installation_ids`` is ``null``

        """
        pass

    def order_installation_results(self, installation_search_order):
        """Specify an ordering to the search results.

        :param installation_search_order: installation search order
        :type installation_search_order: ``osid.installation.InstallationSearchOrder``
        :raise: ``NullArgument`` -- ``installation_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``installation_search_order`` is not of this service

        """
        pass

    def get_installation_search_record(self, installation_search_record_type):
        """Gets the installation search record corresponding to the given installation search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param installation_search_record_type: an installation search record type
        :type installation_search_record_type: ``osid.type.Type``
        :return: the installation search record
        :rtype: ``osid.installation.records.InstallationSearchRecord``
        :raise: ``NullArgument`` -- ``installation_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(installation_search_record_type)`` is ``false``

        """
        return # osid.installation.records.InstallationSearchRecord


class InstallationSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_installations(self):
        """Gets the installation list resulting from the search.

        :return: the installation list
        :rtype: ``osid.installation.InstallationList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.installation.InstallationList

    installations = property(fget=get_installations)

    def get_installation_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the installation query inspector
        :rtype: ``osid.installation.InstallationQueryInspector``

        """
        return # osid.installation.InstallationQueryInspector

    installation_query_inspector = property(fget=get_installation_query_inspector)

    def get_installation_search_results_record(self, installation_search_record_type):
        """Gets the installation search results record corresponding to the given installation search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param installation_search_record_type: an installation search record type
        :type installation_search_record_type: ``osid.type.Type``
        :return: the installation search results record
        :rtype: ``osid.installation.records.InstallationSearchResultsRecord``
        :raise: ``NullArgument`` -- ``installation_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(installation_search_record_type)`` is ``false``

        """
        return # osid.installation.records.InstallationSearchResultsRecord


