from ..osid import managers as osid_managers


class FilingProfile(osid_managers.OsidProfile):
    """The filing profile describes the interoperability among filing services."""
    def supports_visible_federation(self):
        """Tests if directory federation is exposed.

        Federation is exposed when a specific directory may be
        identified, selected and used to access a session. Federation is
        not exposed when a set of directories appears as a single
        directory.

        :return: ``true`` if federation is visible ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_file_system(self):
        """Tests if a ``FileSystemSession`` is supported.

        :return: ``true`` if a ``FileSystemSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_file_system_management(self):
        """Tests if a ``FileSystemManagementSession`` is supported.

        :return: ``true`` if a ``FileSystemManagementSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_file_content(self):
        """Tests if a ``FileContentSession`` is supported.

        :return: ``true`` if a ``FileContentSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_file_lookup(self):
        """Tests if file lookup is supported.

        :return: ``true`` if a ``FileLookupSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_file_query(self):
        """Tests if file querying is supported.

        :return: ``true`` if a ``FileQuerySession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_file_search(self):
        """Tests if file searching is supported.

        :return: ``true`` if a ``FileSearchSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_file_notification(self):
        """Tests if file notification is supported.

        :return: ``true`` if a ``FileNotificationSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_file_smart_directory(self):
        """Tests if managing smart directories is supported.

        :return: ``true`` if a ``FileSmartDirectorySession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_directory_lookup(self):
        """Tests if a ``DirectoryLookupSession`` is supported.

        :return: ``true`` if a ``DirectoryLookupSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_directory_query(self):
        """Tests if directory querying is supported.

        :return: ``true`` if a ``DirectoryQuerySession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_directory_search(self):
        """Tests if directory searching is supported.

        :return: ``true`` if a ``DirectorySearchSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_directory_admin(self):
        """Tests if directory administration is supported.

        :return: ``true`` if a ``DirectoryAdminSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_directory_notification(self):
        """Tests if a directorynotification service is supported.

        :return: ``true`` if a ``DirectoryNotificationSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_filing_management(self):
        """Tests if a file management service is supported.

        :return: ``true`` if a ``FileManagementSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_filing_allocation(self):
        """Tests if a filing allocation service is supported.

        :return: ``true`` if a ``FilingAllocationManager`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_file_record_types(self):
        """Gets the supported file record types.

        :return: a list containing the supported ``File`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    file_record_types = property(fget=get_file_record_types)

    def supports_file_record_type(self, file_record_type):
        """Tests if the given file record type is supported.

        :param file_record_type: a ``Type`` indicating a file record type
        :type file_record_type: ``osid.type.Type``
        :return: ``true`` if the given record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``file_record_type`` is null

        """
        return # boolean

    def get_file_search_record_types(self):
        """Gets the supported file search record types.

        :return: a list containing the supported ``File`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    file_search_record_types = property(fget=get_file_search_record_types)

    def supports_file_search_record_type(self, file_search_record_type):
        """Tests if the given file search record type is supported.

        :param file_search_record_type: a ``Type`` indicating a file search record type
        :type file_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``file_search_record_type`` is null

        """
        return # boolean

    def get_directory_record_types(self):
        """Gets the supported directory record types.

        :return: a list containing the supported ``Directory`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    directory_record_types = property(fget=get_directory_record_types)

    def supports_directory_record_type(self, directory_record_type):
        """Tests if the given directory record type is supported.

        :param directory_record_type: a ``Type`` indicating a directory record type
        :type directory_record_type: ``osid.type.Type``
        :return: ``true`` if the given record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``directory_record_type`` is null

        """
        return # boolean

    def get_directory_search_record_types(self):
        """Gets the supported directory search record types.

        :return: a list containing the supported ``Directory`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    directory_search_record_types = property(fget=get_directory_search_record_types)

    def supports_directory_search_record_type(self, directory_search_record_type):
        """Tests if the given directory search record type is supported.

        :param directory_search_record_type: a ``Type`` indicating a directory search record type
        :type directory_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``directory_search_record_type`` is null

        """
        return # boolean


class FilingManager(osid_managers.OsidManager, FilingProfile):
    """The filing manager provides access sessions to retrieve and manage files and directories.

    Some of the federated access methods support pathnames in addition
    to directory ``Ids``. The sessions included in this manager are:

      * ``FileSystemSession:`` a session for traversing file systems
      * ``FileSystemManagementSession:`` a session for performing
        operations across directories
      * ``FileContentSession:`` a basic session for reading and writing
        a file
      * FileLookupSession: a session for looking up files
      * ``FileQuerySession:`` a session for searching for files
      * ``FileSearchSession:`` a session for searching for files
      * ``FileNotificationSession:`` a session for subscribing to
        changes in files
      * ``FileSmartDirectorySession:`` a session for managing smart
        directories of files
      * ``DirectoryLookupSession:`` a session for looking up a
        directories
      * ``DirectorQuerySession:`` a session for searching for
        directories
      * ``DirectorySearchSession:`` a session for searching for
        directories
      * ``DirectoryNotificationSession:`` a session for subscribing to
        changes in directories


    """
    def get_file_system_session(self):
        """Gets the session for examining file systems.

        :return: a ``FileSystemSession``
        :rtype: ``osid.filing.FileSystemSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_system()`` is ``false``

        """
        return # osid.filing.FileSystemSession

    file_system_session = property(fget=get_file_system_session)

    def get_file_system_session_for_path(self, path):
        """Gets the session for exmaning file systems for the given path.

        :param path: the path to a directory
        :type path: ``string``
        :return: a ``FileSystemSession``
        :rtype: ``osid.filing.FileSystemSession``
        :raise: ``NotFound`` -- ``path`` is not found or is not a directory
        :raise: ``NullArgument`` -- ``path`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_system()`` is ``false``

        """
        return # osid.filing.FileSystemSession

    def get_file_system_session_for_directory(self, directory_id):
        """Gets the session for exmaning file systems for the given directory.

        :param directory_id: the ``Id`` of a directory
        :type directory_id: ``osid.id.Id``
        :return: a ``FileSystemSession``
        :rtype: ``osid.filing.FileSystemSession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_system()`` is ``false``

        """
        return # osid.filing.FileSystemSession

    def get_file_system_management_session(self):
        """Gets the session for manipulating file systems.

        :return: a ``FileSystemManagementSession``
        :rtype: ``osid.filing.FileSystemManagementSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_system_management()`` is ``false``

        """
        return # osid.filing.FileSystemManagementSession

    file_system_management_session = property(fget=get_file_system_management_session)

    def get_file_system_management_session_for_path(self, path):
        """Gets the session for manipulating files for the given path.

        :param path: the path to a directory
        :type path: ``string``
        :return: a ``FileSystemManagementSession``
        :rtype: ``osid.filing.FileSystemManagementSession``
        :raise: ``NotFound`` -- ``path`` is not found or is not a directory
        :raise: ``NullArgument`` -- ``path`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_system_management()`` is ``false``

        """
        return # osid.filing.FileSystemManagementSession

    def get_file_system_management_session_for_directory(self, directory_id):
        """Gets the session for manipulating files for the given path.

        :param directory_id: the ``Id`` of a directory
        :type directory_id: ``osid.id.Id``
        :return: a ``FileSystemManagementSession``
        :rtype: ``osid.filing.FileSystemManagementSession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_system_management()`` is ``false``

        """
        return # osid.filing.FileSystemManagementSession

    def get_file_content_session(self):
        """Gets the session for reading and writing files.

        :return: a ``FileContentSession``
        :rtype: ``osid.filing.FileContentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_content()`` is ``false``

        """
        return # osid.filing.FileContentSession

    file_content_session = property(fget=get_file_content_session)

    def get_file_content_session_for_path(self, path):
        """Gets the session for reading and writing files for the given path.

        :param path: the path to a directory
        :type path: ``string``
        :return: a ``FileContentSession``
        :rtype: ``osid.filing.FileContentSession``
        :raise: ``NotFound`` -- ``path`` is not found or is not a directory
        :raise: ``NullArgument`` -- ``path`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_content()`` is ``false``

        """
        return # osid.filing.FileContentSession

    def get_file_content_session_for_directory(self, directory_id):
        """Gets the session for reading and writing files for the given path.

        :param directory_id: the ``Id`` of a directory
        :type directory_id: ``osid.id.Id``
        :return: a ``FileContentSession``
        :rtype: ``osid.filing.FileContentSession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_content()`` is ``false``

        """
        return # osid.filing.FileContentSession

    def get_file_lookup_session(self):
        """Gets the session for looking up files.

        :return: the ``FileLookupSession``
        :rtype: ``osid.filing.FileLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_lookup()`` is ``false``

        """
        return # osid.filing.FileLookupSession

    file_lookup_session = property(fget=get_file_lookup_session)

    def get_file_lookup_session_for_directory(self, directory_id):
        """Gets the session for manipulating files for the given path.

        :param directory_id: the ``Id`` of the directory
        :type directory_id: ``osid.id.Id``
        :return: a ``FileLookupSession``
        :rtype: ``osid.filing.FileLookupSession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_lookup()`` is ``false``

        """
        return # osid.filing.FileLookupSession

    def get_file_query_session(self):
        """Gets the session for querying files.

        :return: the ``FileQuerySession``
        :rtype: ``osid.filing.FileQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_query()`` is ``false``

        """
        return # osid.filing.FileQuerySession

    file_query_session = property(fget=get_file_query_session)

    def get_file_query_session_for_directory(self, directory_id):
        """Gets a file query session for the specified directory.

        :param directory_id: the ``Id`` of the directory
        :type directory_id: ``osid.id.Id``
        :return: a ``FileQuerySession``
        :rtype: ``osid.filing.FileQuerySession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_query()`` is ``false``

        """
        return # osid.filing.FileQuerySession

    def get_file_search_session(self):
        """Gets the session for searching for files.

        :return: the ``FileSearchSession``
        :rtype: ``osid.filing.FileSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_search()`` is ``false``

        """
        return # osid.filing.FileSearchSession

    file_search_session = property(fget=get_file_search_session)

    def get_file_search_session_for_directory(self, directory_id):
        """Gets a file search session for the specified directory.

        :param directory_id: the ``Id`` of the directory
        :type directory_id: ``osid.id.Id``
        :return: a ``FileSearchSession``
        :rtype: ``osid.filing.FileSearchSession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_search()`` is ``false``

        """
        return # osid.filing.FileSearchSession

    def get_file_notification_session(self, file_receiver):
        """Gets the session for receiving messages about changes to files.

        :param file_receiver: the notification callback
        :type file_receiver: ``osid.filing.FileReceiver``
        :return: ``a FileNotificationSession``
        :rtype: ``osid.filing.FileNotificationSession``
        :raise: ``NullArgument`` -- ``file_receiver`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_notification()`` is ``false``

        """
        return # osid.filing.FileNotificationSession

    def get_file_notification_session_for_directory(self, file_receiver, directory_id):
        """Gets a file notification session for the specified directory.

        :param file_receiver: the notification callback
        :type file_receiver: ``osid.filing.FileReceiver``
        :param directory_id: the ``Id`` of the directory
        :type directory_id: ``osid.id.Id``
        :return: a ``FileNotificationSession``
        :rtype: ``osid.filing.FileNotificationSession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``file_receiver`` or ``directory_id`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_notification()`` is ``false``

        """
        return # osid.filing.FileNotificationSession

    def get_file_smart_directory_session(self, directory_id):
        """Gets the session for managing dynamic directories.

        :param directory_id: the ``Id`` of the directory
        :type directory_id: ``osid.id.Id``
        :return: a ``FileSmartDirectorySession``
        :rtype: ``osid.filing.FileSmartDirectorySession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_smart_directory()`` is ``false``

        """
        return # osid.filing.FileSmartDirectorySession

    def get_directory_lookup_session(self):
        """Gets the session for examining directories.

        :return: a ``DirectoryLookupSession``
        :rtype: ``osid.filing.DirectoryLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_lookup()`` is ``false``

        """
        return # osid.filing.DirectoryLookupSession

    directory_lookup_session = property(fget=get_directory_lookup_session)

    def get_directory_lookup_session_for_directory(self, directory_id):
        """Gets the session for examining a given directory.

        :param directory_id: the ``Id`` of the directory
        :type directory_id: ``osid.id.Id``
        :return: a ``DirectoryLookupSession``
        :rtype: ``osid.filing.DirectoryLookupSession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_lookup()`` is ``false``

        """
        return # osid.filing.DirectoryLookupSession

    def get_directory_query_session(self):
        """Gets the session for querying directories.

        :return: a ``DirectoryQuerySession``
        :rtype: ``osid.filing.DirectoryQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_query()`` is ``false``

        """
        return # osid.filing.DirectoryQuerySession

    directory_query_session = property(fget=get_directory_query_session)

    def get_directory_query_session_for_directory(self, directory_id):
        """Gets the session for querying directories within a given directory.

        :param directory_id: the ``Id`` of the directory
        :type directory_id: ``osid.id.Id``
        :return: a ``DirectoryQuerySession``
        :rtype: ``osid.filing.DirectoryQuerySession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_query()`` is ``false``

        """
        return # osid.filing.DirectoryQuerySession

    def get_directory_search_session(self):
        """Gets the session for searching for directories.

        :return: a ``DirectorySearchSession``
        :rtype: ``osid.filing.DirectorySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_search()`` is ``false``

        """
        return # osid.filing.DirectorySearchSession

    directory_search_session = property(fget=get_directory_search_session)

    def get_directory_search_session_for_directory(self, directory_id):
        """Gets the session for searching for directories within a given directory.

        :param directory_id: the ``Id`` of the directory
        :type directory_id: ``osid.id.Id``
        :return: a ``DirectorySearchSession``
        :rtype: ``osid.filing.DirectorySearchSession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_search()`` is ``false``

        """
        return # osid.filing.DirectorySearchSession

    def get_directory_admin_session(self):
        """Gets the session for creating and removing files.

        :return: a ``DirectoryAdminSession``
        :rtype: ``osid.filing.DirectoryAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_admin()`` is ``false``

        """
        return # osid.filing.DirectoryAdminSession

    directory_admin_session = property(fget=get_directory_admin_session)

    def get_directory_admin_session_for_directory(self, directory_id):
        """Gets the session for searching for creating and removing files in the given directory.

        :param directory_id: the ``Id`` of the directory
        :type directory_id: ``osid.id.Id``
        :return: a ``DirectoryAdminSession``
        :rtype: ``osid.filing.DirectoryAdminSession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_admin()`` is ``false``

        """
        return # osid.filing.DirectoryAdminSession

    def get_directory_notification_session(self, directory_receiver):
        """Gets the session for receiving messages about changes to directories.

        :param directory_receiver: the notification callback
        :type directory_receiver: ``osid.filing.DirectoryReceiver``
        :return: a ``DirectoryNotificationSession``
        :rtype: ``osid.filing.DirectoryNotificationSession``
        :raise: ``NullArgument`` -- ``directory_receiver`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_notification()`` is ``false``

        """
        return # osid.filing.DirectoryNotificationSession

    def get_directory_notification_session_for_directory(self, directory_receiver, directory_id):
        """Gets the session for receiving messages about changes to directories in the given directory.

        :param directory_receiver: the notification callback
        :type directory_receiver: ``osid.filing.DirectoryReceiver``
        :param directory_id: the ``Id`` of the directory
        :type directory_id: ``osid.id.Id``
        :return: a ``DirectoryNotificationSession``
        :rtype: ``osid.filing.DirectoryNotificationSession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_receiver`` or ``directory_id`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_notification()`` is ``false``

        """
        return # osid.filing.DirectoryNotificationSession

    def get_filing_allocation_manager(self):
        """Gets the ``FilingAllocationManager``.

        :return: a ``FilingAllocationManager``
        :rtype: ``osid.filing.allocation.FilingAllocationManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_filing_allocation()`` is ``false``

        """
        return # osid.filing.allocation.FilingAllocationManager

    filing_allocation_manager = property(fget=get_filing_allocation_manager)


class FilingProxyManager(osid_managers.OsidProxyManager, FilingProfile):
    """The filing manager provides access sessions to retrieve and manage files and directories.

    A manager may support federation in that files and directories can
    be accessed by a specified path. Methods in this manager support the
    passing of a ``Proxy`` to pass information from server environments.
    The sessions included in this manager are:

      * ``FileSystemSession:`` a session for traversing file systems
      * ``FileSystemManagementSession:`` a session for performing
        operations across directories
      * ``FileContentSession:`` a basic session for reading and writing
        a file
      * FileLookupSession: a session for looking up files
      * ``FileQuerySession:`` a session for searching for files
      * ``FileSearchSession:`` a session for searching for files
      * ``FileNotificationSession:`` a session for subscribing to
        changes in files
      * ``FileSmartDirectorySession:`` a session for managing smart
        directories of files
      * ``DirectoryLookupSession:`` a session for looking up a
        directories
      * ``DirectorQuerySession:`` a session for searching for
        directories
      * ``DirectorySearchSession:`` a session for searching for
        directories
      * ``DirectoryNotificationSession:`` a session for subscribing to
        changes in directories


    """
    def get_file_system_session(self, proxy):
        """Gets the session for examining file systems.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FileSystemSession``
        :rtype: ``osid.filing.FileSystemSession``
        :raise: ``NullArgument`` -- ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_system()`` is ``false``

        """
        return # osid.filing.FileSystemSession

    def get_file_system_session_for_path(self, path, proxy):
        """Gets the session for exmaning file systems for the given path.

        :param path: the path to a directory
        :type path: ``string``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FileSystemSession``
        :rtype: ``osid.filing.FileSystemSession``
        :raise: ``NotFound`` -- ``path`` is not found or is not a directory
        :raise: ``NullArgument`` -- ``path`` or ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_system()`` is ``false``

        """
        return # osid.filing.FileSystemSession

    def get_file_system_session_for_directory(self, directory_id, proxy):
        """Gets the session for exmaning file systems for the given directory.

        :param directory_id: the ``Id`` of a directory
        :type directory_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FileSystemSession``
        :rtype: ``osid.filing.FileSystemSession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` or ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_system()`` is ``false``

        """
        return # osid.filing.FileSystemSession

    def get_file_system_management_session(self, proxy):
        """Gets the session for manipulating file systems.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FileSystemManagementSession``
        :rtype: ``osid.filing.FileSystemManagementSession``
        :raise: ``NullArgument`` -- ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_system_management()`` is ``false``

        """
        return # osid.filing.FileSystemManagementSession

    def get_file_system_management_session_for_path(self, path, proxy):
        """Gets the session for manipulating files for the given path.

        :param path: the path to a directory
        :type path: ``string``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FileSystemManagementSession``
        :rtype: ``osid.filing.FileSystemManagementSession``
        :raise: ``NotFound`` -- ``path`` is not found or is not a directory
        :raise: ``NullArgument`` -- ``path`` or ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_system_management()`` is ``false``

        """
        return # osid.filing.FileSystemManagementSession

    def get_file_system_management_session_for_directory(self, directory_id, proxy):
        """Gets the session for manipulating files for the given path.

        :param directory_id: the ``Id`` of a directory
        :type directory_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FileSystemManagementSession``
        :rtype: ``osid.filing.FileSystemManagementSession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` or ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_system_management()`` is ``false``

        """
        return # osid.filing.FileSystemManagementSession

    def get_file_content_session(self, proxy):
        """Gets the session for reading and writing files.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FileContentSession``
        :rtype: ``osid.filing.FileContentSession``
        :raise: ``NullArgument`` -- ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_content()`` is ``false``

        """
        return # osid.filing.FileContentSession

    def get_file_content_session_for_path(self, path, proxy):
        """Gets the session for reading and writing files for the given path.

        :param path: the path to a directory
        :type path: ``string``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FileContentSession``
        :rtype: ``osid.filing.FileContentSession``
        :raise: ``NotFound`` -- ``path`` is not found or is not a directory
        :raise: ``NullArgument`` -- ``path`` or ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_content()`` is ``false``

        """
        return # osid.filing.FileContentSession

    def get_file_content_session_for_directory(self, directory_id, proxy):
        """Gets the session for reading and writing files for the given path.

        :param directory_id: the ``Id`` of a directory
        :type directory_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FileContentSession``
        :rtype: ``osid.filing.FileContentSession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` or ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_content()`` is ``false``

        """
        return # osid.filing.FileContentSession

    def get_file_lookup_session(self, proxy):
        """Gets the session for looking up files.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: the ``FileLookupSession``
        :rtype: ``osid.filing.FileLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_lookup()`` is ``false``

        """
        return # osid.filing.FileLookupSession

    def get_file_lookup_session_for_directory(self, directory_id, proxy):
        """Gets a file lookup session for the specified directory.

        :param directory_id: the ``Id`` to the directory
        :type directory_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FileLookupSession``
        :rtype: ``osid.filing.FileLookupSession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` or ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_lookup()`` is ``false``

        """
        return # osid.filing.FileLookupSession

    def get_file_query_session(self, proxy):
        """Gets the session for querying files.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: the ``FileQuerySession``
        :rtype: ``osid.filing.FileQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_query()`` is ``false``

        """
        return # osid.filing.FileQuerySession

    def get_file_query_session_for_directory(self, directory_id, proxy):
        """Gets a file query session for the specified directory.

        :param directory_id: the ``Id`` to the directory
        :type directory_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FileQuerySession``
        :rtype: ``osid.filing.FileQuerySession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` or ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_query()`` is ``false``

        """
        return # osid.filing.FileQuerySession

    def get_file_search_session(self, proxy):
        """Gets the session for searching for files.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: the ``FileSearchSession``
        :rtype: ``osid.filing.FileSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_search()`` is ``false``

        """
        return # osid.filing.FileSearchSession

    def get_file_search_session_for_directory(self, directory_id, proxy):
        """Gets a file search session for the specified directory.

        :param directory_id: the ``Id`` to the directory
        :type directory_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FileSearchSession``
        :rtype: ``osid.filing.FileSearchSession``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` or ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_search()`` is ``false``

        """
        return # osid.filing.FileSearchSession

    def get_file_notification_session(self, file_receiver, proxy):
        """Gets the session for receiving messages about changes to files.

        :param file_receiver: the notification callback
        :type file_receiver: ``osid.filing.FileReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a FileNotificationSession``
        :rtype: ``osid.filing.FileNotificationSession``
        :raise: ``NullArgument`` -- ``file_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_notification()`` is ``false``

        """
        return # osid.filing.FileNotificationSession

    def get_file_notification_session_for_directory(self, file_receiver, directory_id, proxy):
        """Gets a file notification session for the specified directory.

        :param file_receiver: the notification callback
        :type file_receiver: ``osid.filing.FileReceiver``
        :param directory_id: the ``Id`` to the directory
        :type directory_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FileNotificationSession``
        :rtype: ``osid.filing.FileNotificationSession``
        :raise: ``NotFound`` -- ``directory_path`` is not found
        :raise: ``NullArgument`` -- ``file_receiver, directory_id,`` or ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_notification()`` is ``false``

        """
        return # osid.filing.FileNotificationSession

    def get_file_smart_directory_session(self, directory_id, proxy):
        """Gets the session for managing dynamic diectories.

        :param directory_id: the ``Id`` to the directory
        :type directory_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FileSmartDirectorySession``
        :rtype: ``osid.filing.FileSmartDirectorySession``
        :raise: ``NotFound`` -- ``directory_id is not found``
        :raise: ``NullArgument`` -- ``directory_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_smart_directory()`` is ``false``

        """
        return # osid.filing.FileSmartDirectorySession

    def get_directory_lookup_session(self, proxy):
        """Gets the session for examining directories.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DirectoryLookupSession``
        :rtype: ``osid.filing.DirectoryLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_lookup()`` is ``false``

        """
        return # osid.filing.DirectoryLookupSession

    def get_directory_lookup_session_for_directory(self, directory_id, proxy):
        """Gets the session for examining a given directory.

        If the path is an alias, the target directory is used. The path
        indicates the file alias and the real path indicates the target
        directory.

        :param directory_id: the ``Id`` to the directory
        :type directory_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DirectoryLookupSession``
        :rtype: ``osid.filing.DirectoryLookupSession``
        :raise: ``NotFound`` -- ``directory_id is not found``
        :raise: ``NullArgument`` -- ``directory_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_lookup()`` is ``false``

        """
        return # osid.filing.DirectoryLookupSession

    def get_directory_query_session(self, proxy):
        """Gets the session for querying directories.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DirectoryQuerySession``
        :rtype: ``osid.filing.DirectoryQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_query()`` is ``false``

        """
        return # osid.filing.DirectoryQuerySession

    def get_directory_query_session_for_directory(self, directory_id, proxy):
        """Gets the session for querying directories within a given directory.

        If the path is an alias, the target directory is used. The path
        indicates the file alias and the real path indicates the target
        directory.

        :param directory_id: the ``Id`` to the directory
        :type directory_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DirectoryQuerySession``
        :rtype: ``osid.filing.DirectoryQuerySession``
        :raise: ``NotFound`` -- ``directory_id is not found``
        :raise: ``NullArgument`` -- ``directory_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_query()`` is ``false``

        """
        return # osid.filing.DirectoryQuerySession

    def get_directory_search_session(self, proxy):
        """Gets the session for searching for directories.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DirectorySearchSession``
        :rtype: ``osid.filing.DirectorySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_search()`` is ``false``

        """
        return # osid.filing.DirectorySearchSession

    def get_directory_search_session_for_directory(self, directory_id, proxy):
        """Gets the session for searching for directories within a given directory.

        If the path is an alias, the target directory is used. The path
        indicates the file alias and the real path indicates the target
        directory.

        :param directory_id: the ``Id`` to the directory
        :type directory_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DirectorySearchSession``
        :rtype: ``osid.filing.DirectorySearchSession``
        :raise: ``NotFound`` -- ``directory_id is not found``
        :raise: ``NullArgument`` -- ``directory_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_search()`` is ``false``

        """
        return # osid.filing.DirectorySearchSession

    def get_directory_admin_session(self, proxy):
        """Gets the session for creating and removing files.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DirectoryAdminSession``
        :rtype: ``osid.filing.DirectoryAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_admin()`` is ``false``

        """
        return # osid.filing.DirectoryAdminSession

    def get_directory_admin_session_for_directory(self, directory_id, proxy):
        """Gets the session for searching for creating and removing files in the given directory.

        If the path is an alias, the target directory is used. The path
        indicates the file alias and the real path indicates the target
        directory.

        :param directory_id: the ``Id`` to the directory
        :type directory_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DirectoryAdminSession``
        :rtype: ``osid.filing.DirectoryAdminSession``
        :raise: ``NotFound`` -- ``directory_id is not found``
        :raise: ``NullArgument`` -- ``directory_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_admin()`` is ``false``

        """
        return # osid.filing.DirectoryAdminSession

    def get_directory_notification_session(self, directory_receiver, proxy):
        """Gets the session for receiving messages about changes to directories.

        :param directory_receiver: the notification callback
        :type directory_receiver: ``osid.filing.DirectoryReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DirectoryNotificationSession``
        :rtype: ``osid.filing.DirectoryNotificationSession``
        :raise: ``NullArgument`` -- ``directory_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_notification()`` is ``false``

        """
        return # osid.filing.DirectoryNotificationSession

    def get_directory_notification_session_for_directory(self, directory_receiver, directory_id, proxy):
        """Gets the session for receiving messages about changes to directories in the given directory.

        If the path is an alias, the target directory is used. The path
        indicates the file alias and the real path indicates the target
        directory.

        :param directory_receiver: the notification callback
        :type directory_receiver: ``osid.filing.DirectoryReceiver``
        :param directory_id: the ``Id`` to the directory
        :type directory_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DirectoryNotificationSession``
        :rtype: ``osid.filing.DirectoryNotificationSession``
        :raise: ``NotFound`` -- ``directory_path`` is not found
        :raise: ``NullArgument`` -- ``directory_receiver, directory_id,`` or ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_notification()`` is ``false``

        """
        return # osid.filing.DirectoryNotificationSession

    def get_filing_allocation_proxy_manager(self):
        """Gets the ``FilingAllocationProxyManager``.

        :return: a ``FilingAllocationProxyManager``
        :rtype: ``osid.filing.allocation.FilingAllocationProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_filing_allocation()`` is ``false``

        """
        return # osid.filing.allocation.FilingAllocationProxyManager

    filing_allocation_proxy_manager = property(fget=get_filing_allocation_proxy_manager)


