from ..osid import search_orders as osid_search_orders


class DirectoryEntrySearchOrder(osid_search_orders.OsidObjectSearchOrder):
    """An interface for specifying the order of search results."""
    def order_by_name(self, style):
        """Specifies a preference for ordering the result set by the entry name.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_path(self, style):
        """Specifies a preference for ordering the result set by the entry path.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_owner(self, style):
        """Specifies a preference for ordering the result set by the entry owner.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_owner_search_order(self):
        """Tests if an agent search order is available.

        :return: ``true`` if an agent search order interface is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_owner_search_order(self):
        """Gets an agent search order interface.

        :return: an agent search order interface
        :rtype: ``osid.authentication.AgentSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_owner_search_order()`` is ``false``

        """
        return # osid.authentication.AgentSearchOrder

    owner_search_order = property(fget=get_owner_search_order)

    def order_by_created_time(self, style):
        """Specifies a preference for ordering the result set by the entry creation time.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_modified_time(self, style):
        """Specifies a preference for ordering the result set by the entry modification time.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_last_access_time(self, style):
        """Specifies a preference for ordering the result set by the entry last access time.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass


class FileSearchOrder(DirectoryEntrySearchOrder):
    """An interface for specifying the ordering of search results."""
    def order_by_size(self, style):
        """Specifies a preference for ordering the results by file size.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def get_file_search_order_record(self, file_record_type):
        """Gets the file search order record corresponding to the given file record Type.

        Multiple retrievals return the same underlying object.

        :param file_record_type: a file record type
        :type file_record_type: ``osid.type.Type``
        :return: the file search order record
        :rtype: ``osid.filing.records.FileSearchOrderRecord``
        :raise: ``NullArgument`` -- ``file_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(file_record_type)`` is ``false``

        """
        return # osid.filing.records.FileSearchOrderRecord


class DirectorySearchOrder(osid_search_orders.OsidCatalogSearchOrder, DirectoryEntrySearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_directory_search_order_record(self, directory_record_type):
        """Gets the directory search order record corresponding to the given directory record Type.

        Multiple retrievals return the same underlying object.

        :param directory_record_type: a directory record type
        :type directory_record_type: ``osid.type.Type``
        :return: the directory search order record
        :rtype: ``osid.filing.records.DirectorySearchOrderRecord``
        :raise: ``NullArgument`` -- ``directory_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(directory_record_type)`` is ``false``

        """
        return # osid.filing.records.DirectorySearchOrderRecord


