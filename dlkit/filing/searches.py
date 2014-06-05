from ..osid import searches as osid_searches


class FileSearch(osid_searches.OsidSearch):
    """The search interface for governing file searches."""
    def search_among_files(self, file_ids):
        """Execute this search among the given list of files.

        :param file_ids: list of file ``Ids``
        :type file_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``file_ids`` is ``null``

        """
        pass

    def order_file_results(self, file_search_order):
        """Specify an ordering to the search results.

        :param file_search_order: file search order
        :type file_search_order: ``osid.filing.FileSearchOrder``
        :raise: ``NullArgument`` -- ``file_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``file_search_order`` is not of this service

        """
        pass

    def get_file_search_record(self, file_search_record_type):
        """Gets the file search record corresponding to the given file search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param file_search_record_type: a file search record type
        :type file_search_record_type: ``osid.type.Type``
        :return: the file search record
        :rtype: ``osid.filing.records.FileSearchRecord``
        :raise: ``NullArgument`` -- ``file_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(file_search_record_type)`` is ``false``

        """
        return # osid.filing.records.FileSearchRecord


class FileSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_files(self):
        """Gets the file list resulting from a search.

        :return: the directory list
        :rtype: ``osid.filing.FileList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.filing.FileList

    files = property(fget=get_files)

    def get_file_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.filing.FileQueryInspector``

        """
        return # osid.filing.FileQueryInspector

    file_query_inspector = property(fget=get_file_query_inspector)

    def get_file_search_results_record(self, file_search_record_type):
        """Gets the file search results record corresponding to the given file search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param file_search_record_type: a file search record type
        :type file_search_record_type: ``osid.type.Type``
        :return: the file search results record
        :rtype: ``osid.filing.records.FileSearchResultsRecord``
        :raise: ``NullArgument`` -- ``file_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(file_search_record_type)`` is ``false``

        """
        return # osid.filing.records.FileSearchResultsRecord


class DirectorySearch(osid_searches.OsidSearch):
    """The search interface for gioverning directory searches."""
    def search_among_directories(self, directory_ids):
        """Execute this search among the given list of diectories.

        :param directory_ids: list of directory ``Ids``
        :type directory_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``directory_ids`` is ``null``

        """
        pass

    def order_directory_results(self, directory_search_order):
        """Specify an ordering to the search results.

        :param directory_search_order: directory search order
        :type directory_search_order: ``osid.filing.DirectorySearchOrder``
        :raise: ``NullArgument`` -- ``directory_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``directory_search_order`` is not of this service

        """
        pass

    def get_directory_search_record(self, directory_search_record_type):
        """Gets the directory search record corresponding to the given directory search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param directory_search_record_type: a directory search record type
        :type directory_search_record_type: ``osid.type.Type``
        :return: the directory search record
        :rtype: ``osid.filing.records.DirectorySearchRecord``
        :raise: ``NullArgument`` -- ``directory_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(directory_search_record_type)`` is ``false``

        """
        return # osid.filing.records.DirectorySearchRecord


class DirectorySearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search.

    This example gets a result set from a keyword match.

    An example to find directories whose path contains "System" from a
    resulting search of directories whose name is "Library", sorted by
    the path name.
      DirectoryQuery query = session.getDirectoryQuery();
      query.addNameMatch("Library", wordStringMatchType, true);
      DirectorySearch search = session.getDirectorySearch();
      DirectorySearchResults results = session.getDirectoriesBySearch(query, search);
      
      query = session.getDirectoryQuery();
      query.addNameMatch("System", wordStringMatchType, true);
      search = session.getDirectorySearch();
      search.searchWithinDirectoryResults(results);
      DirectorySearchOrder order = session.getDirectorySearchOrder();
      order.orderByPath();
      search.orderDirectoryResults(order);
      
      results = session.getDirectoriesBySearch(query, search);
      DirectoryList directories = results.getDirectories();
    


    """
    def get_directories(self):
        """Gets the directory list resulting from a search.

        :return: the directory list
        :rtype: ``osid.filing.DirectoryList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.filing.DirectoryList

    directories = property(fget=get_directories)

    def get_directory_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.filing.DirectoryQueryInspector``

        """
        return # osid.filing.DirectoryQueryInspector

    directory_query_inspector = property(fget=get_directory_query_inspector)

    def get_directory_search_results_record(self, directory_search_record_type):
        """Gets the directory search results record corresponding to the given directory search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param directory_search_record_type: a directory search record type
        :type directory_search_record_type: ``osid.type.Type``
        :return: the directory search results record
        :rtype: ``osid.filing.records.DirectorySearchResultsRecord``
        :raise: ``NullArgument`` -- ``directory_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(directory_search_record_type)`` is ``false``

        """
        return # osid.filing.records.DirectorySearchResultsRecord


