# -*- coding: utf-8 -*-
"""Filing Open Service Interface Definitions
filing version 3.0.0

The Filing OSID provides a means for managing and accessing files and
directories. The Filing OSID is used to abstract assumptions made about
using a specific file system, or can be used to provide a file-based
application a file system oriented view of other OSIDs.

Files

The Filing OSID defines a file access session that maps to a single
``File``. This is the simplest application of the Filing OSID can be
used in circumstances when it is desirable to confine knowledge of
directories within a provider.

Directories

``Directories`` are hierarchical ``OsidCatalogs`` of Files.

Differences from OSID Patterns

The Filing OSID assumes the pathname and filename of a ``File`` or
``Directory`` is globally unique. Typically, only the ``Id`` field is
unique in an ``OsidObject``. In the Filing OSID, there are two unique
identifiers for identifying ``Files`` and Directories.

The ``Id`` is used to conform to existing OSID patterns and more easily
create relationships to other auxiliary services such as the Journaling
OSID, Relationship OSID, or the Ontology OSID. However, in a file system
one is accustomed to traversing a file system using path names.

The standard ``OsidSessions`` refer to ``Files`` and ``Directories``
using their ``Ids``. The file system-oriented and content sessions
access and manipulate the file system using path names. Access to these
sessions via the ``OsidManagers`` provide for both a path name and
``Directory``  ``Id``.

The cataloging in the file system and content sessions behave
differently than that in other OsidSessions. Typically, one is
constrained to ``OsidObjects`` within the ``OsidCatalog,`` and its
children in a federated view. In these sessions which use the path name
as a key, ``Files`` and ``Directories`` outside the local Directory may
be accessed with the use of absolute path names.

Finally, there are no hierarchical service patterns in the ``Directory``
``OsidCatalog`` and a ``File`` or sub-directory may belong to one and
only one ``Directory`` .

Example
  FilieSession session = filingManager.getFileContentSession();
  DataInputStream dis = session.getInputStream("/etc/passwd");



Sub Packages

The Filing OSID contains a Filing Allocation OSID for examining and
managing file system utilization and user quotas.

"""
from ..osid import managers as osid_managers
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class FilingProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if directory federation is exposed.
        Federation is exposed when a specific directory may be
        identified, selected and used to access a session. Federation is
        not exposed when a set of directories appears as a single
        directory.

        :return: ``true`` if federation is visible ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_file_system(self):
        """Tests if a ``FileSystemSession`` is supported.

        :return: ``true`` if a ``FileSystemSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_file_system_management(self):
        """Tests if a ``FileSystemManagementSession`` is supported.

        :return: ``true`` if a ``FileSystemManagementSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_file_content(self):
        """Tests if a ``FileContentSession`` is supported.

        :return: ``true`` if a ``FileContentSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_file_lookup(self):
        """Tests if file lookup is supported.

        :return: ``true`` if a ``FileLookupSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_file_query(self):
        """Tests if file querying is supported.

        :return: ``true`` if a ``FileQuerySession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_file_search(self):
        """Tests if file searching is supported.

        :return: ``true`` if a ``FileSearchSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_file_notification(self):
        """Tests if file notification is supported.

        :return: ``true`` if a ``FileNotificationSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_file_smart_directory(self):
        """Tests if managing smart directories is supported.

        :return: ``true`` if a ``FileSmartDirectorySession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_directory_lookup(self):
        """Tests if a ``DirectoryLookupSession`` is supported.

        :return: ``true`` if a ``DirectoryLookupSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_directory_query(self):
        """Tests if directory querying is supported.

        :return: ``true`` if a ``DirectoryQuerySession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_directory_search(self):
        """Tests if directory searching is supported.

        :return: ``true`` if a ``DirectorySearchSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_directory_admin(self):
        """Tests if directory administration is supported.

        :return: ``true`` if a ``DirectoryAdminSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_directory_notification(self):
        """Tests if a directorynotification service is supported.

        :return: ``true`` if a ``DirectoryNotificationSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_filing_management(self):
        """Tests if a file management service is supported.

        :return: ``true`` if a ``FileManagementSession`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_filing_allocation(self):
        """Tests if a filing allocation service is supported.

        :return: ``true`` if a ``FilingAllocationManager`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_file_record_types(self):
        """Gets the supported file record types.

        :return: a list containing the supported ``File`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    file_record_types = property(fget=get_file_record_types)

    def supports_file_record_type(self, file_record_type):
        """Tests if the given file record type is supported.

        :param file_record_type: a ``Type`` indicating a file record type
        :type file_record_type: ``osid.type.Type``
        :return: ``true`` if the given record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``file_record_type`` is null

        """
        raise UNIMPLEMENTED()

    def get_file_search_record_types(self):
        """Gets the supported file search record types.

        :return: a list containing the supported ``File`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    file_search_record_types = property(fget=get_file_search_record_types)

    def supports_file_search_record_type(self, file_search_record_type):
        """Tests if the given file search record type is supported.

        :param file_search_record_type: a ``Type`` indicating a file search record type
        :type file_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``file_search_record_type`` is null

        """
        raise UNIMPLEMENTED()

    def get_directory_record_types(self):
        """Gets the supported directory record types.

        :return: a list containing the supported ``Directory`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    directory_record_types = property(fget=get_directory_record_types)

    def supports_directory_record_type(self, directory_record_type):
        """Tests if the given directory record type is supported.

        :param directory_record_type: a ``Type`` indicating a directory record type
        :type directory_record_type: ``osid.type.Type``
        :return: ``true`` if the given record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``directory_record_type`` is null

        """
        raise UNIMPLEMENTED()

    def get_directory_search_record_types(self):
        """Gets the supported directory search record types.

        :return: a list containing the supported ``Directory`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    directory_search_record_types = property(fget=get_directory_search_record_types)

    def supports_directory_search_record_type(self, directory_search_record_type):
        """Tests if the given directory search record type is supported.

        :param directory_search_record_type: a ``Type`` indicating a directory search record type
        :type directory_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``directory_search_record_type`` is null

        """
        raise UNIMPLEMENTED()



class FilingManager(osid_managers.OsidManager, osid_sessions.OsidSession, FilingProfile):

    def get_file_system_session(self):
        """Gets the session for examining file systems.

        :return: a ``FileSystemSession``
        :rtype: ``osid.filing.FileSystemSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_system()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_file_system_management_session(self):
        """Gets the session for manipulating file systems.

        :return: a ``FileSystemManagementSession``
        :rtype: ``osid.filing.FileSystemManagementSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_system_management()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_file_content_session(self):
        """Gets the session for reading and writing files.

        :return: a ``FileContentSession``
        :rtype: ``osid.filing.FileContentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_content()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_file_lookup_session(self):
        """Gets the session for looking up files.

        :return: the ``FileLookupSession``
        :rtype: ``osid.filing.FileLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_file_query_session(self):
        """Gets the session for querying files.

        :return: the ``FileQuerySession``
        :rtype: ``osid.filing.FileQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_file_search_session(self):
        """Gets the session for searching for files.

        :return: the ``FileSearchSession``
        :rtype: ``osid.filing.FileSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_file_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_directory_lookup_session(self):
        """Gets the session for examining directories.

        :return: a ``DirectoryLookupSession``
        :rtype: ``osid.filing.DirectoryLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_directory_query_session(self):
        """Gets the session for querying directories.

        :return: a ``DirectoryQuerySession``
        :rtype: ``osid.filing.DirectoryQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_directory_search_session(self):
        """Gets the session for searching for directories.

        :return: a ``DirectorySearchSession``
        :rtype: ``osid.filing.DirectorySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_directory_admin_session(self):
        """Gets the session for creating and removing files.

        :return: a ``DirectoryAdminSession``
        :rtype: ``osid.filing.DirectoryAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_directory_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_filing_allocation_manager(self):
        """Gets the ``FilingAllocationManager``.

        :return: a ``FilingAllocationManager``
        :rtype: ``osid.filing.allocation.FilingAllocationManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_filing_allocation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    filing_allocation_manager = property(fget=get_filing_allocation_manager)


##
# The following methods are from osid.filing.DirectoryLookupSession

    def get_directory_id(self):
        """Gets the ``Id`` of this directory.

        :return: the ``Id`` of this directory
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    directory_id = property(fget=get_directory_id)

    def get_directory(self):
        """Gets the directory associated with this session.

        :return: the directory associated with this session
        :rtype: ``osid.filing.Directory``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    directory = property(fget=get_directory)

    def can_lookup_directories(self):
        """Tests if this user can perform entry lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_directory_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_directory_view(self):
        """A complete view of the directory returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_directory_view(self):
        """Federates the view for methods in this session.
        A federated view will include entries in directories which are
        children of this directory.



        """
        raise UNIMPLEMENTED()

    def use_isolated_directory_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this directory only.



        """
        raise UNIMPLEMENTED()

    def get_directories_by_ids(self, directory_ids):
        """Gets a ``DirectoryList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the
        directories specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Directories`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param directory_ids: the list of ``Ids`` to retrieve
        :type directory_ids: ``osid.id.IdList``
        :return: the returned ``Directory`` list
        :rtype: ``osid.filing.DirectoryList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``directory_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_directories_by_genus_type(self, dircetory_genus_type):
        """Gets a ``DirectoryList`` corresponding to the given directory genus ``Type`` which does not include directories of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        directories or an error results. Otherwise, the returned list
        may contain only those directories that are accessible through
        this session.

        :param dircetory_genus_type: a directory genus type
        :type dircetory_genus_type: ``osid.type.Type``
        :return: the returned ``Directory list``
        :rtype: ``osid.filing.DirectoryList``
        :raise: ``NullArgument`` -- ``directory_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_directories_by_parent_genus_type(self, directory_genus_type):
        """Gets a ``DirectoryList`` corresponding to the given directory genus ``Type`` and include any additional directories with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        directories or an error results. Otherwise, the returned list
        may contain only those directories that are accessible through
        this session.

        :param directory_genus_type: a directory genus type
        :type directory_genus_type: ``osid.type.Type``
        :return: the returned ``Directory`` list
        :rtype: ``osid.filing.DirectoryList``
        :raise: ``NullArgument`` -- ``directory_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_directories_by_record_type(self, directory_record_type):
        """Gets a ``DirectoryList`` corresponding to the given directory record ``Type``.
        The set of directories implementing the given record type is
        returned.In plenary mode, the returned list contains all known
        directories or an error results. Otherwise, the returned list
        may contain only those directories that are accessible through
        this session.

        :param directory_record_type: a directory record type
        :type directory_record_type: ``osid.type.Type``
        :return: the returned ``Directory`` list
        :rtype: ``osid.filing.DirectoryList``
        :raise: ``NullArgument`` -- ``directory_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_directories_by_provider(self, resource_id):
        """Gets a ``DirectoryList`` for the given provider.
        In plenary mode, the returned list contains all known
        directories or an error results. Otherwise, the returned list
        may contain only those directories that are accessible through
        this session.

        :param resource_id: a resource Id
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Directory`` list
        :rtype: ``osid.filing.DirectoryList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_directories(self):
        """Gets the list of directories inthis directory.
        In a federated view, this method returns all directories in
        descendant directories. In plenary mode, the returned list
        contains all known directories or an error results. Otherwise,
        the returned list may contain only those directories that are
        accessible through this session.

        :return: the list of directories in this directory
        :rtype: ``osid.filing.DirectoryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    directories = property(fget=get_directories)


##
# The following methods are from osid.filing.DirectoryQuerySession

    def can_search_directories(self):
        """Tests if this user can perform ``Directory`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_directory_query(self):
        """Gets a directory query.

        :return: the directory query
        :rtype: ``osid.filing.DirectoryQuery``

        """
        raise UNIMPLEMENTED()

    directory_query = property(fget=get_directory_query)

    def get_directories_by_query(self, directory_query):
        """Gets a list of ``Directory`` objects matching the given directory query.

        :param directory_query: the directory query
        :type directory_query: ``osid.filing.DirectoryQuery``
        :return: the returned ``DirectoryList``
        :rtype: ``osid.filing.DirectoryList``
        :raise: ``NullArgument`` -- ``directory_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``directory_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.filing.DirectorySearchSession

    def get_directory_search(self):
        """Gets a diectory search.

        :return: the directory search
        :rtype: ``osid.filing.DirectorySearch``

        """
        raise UNIMPLEMENTED()

    directory_search = property(fget=get_directory_search)

    def get_directory_search_order(self):
        """Gets a directory search order.
        The ``DirectorySearchOrder`` is supplied to a
        ``DirectorySearch`` to specify the ordering of results.

        :return: the directory search order
        :rtype: ``osid.filing.DirectorySearchOrder``

        """
        raise UNIMPLEMENTED()

    directory_search_order = property(fget=get_directory_search_order)

    def get_directories_by_search(self, directory_query, directory_search):
        """Gets the search results matching the given search.

        :param directory_query: the directory query
        :type directory_query: ``osid.filing.DirectoryQuery``
        :param directory_search: the directory search
        :type directory_search: ``osid.filing.DirectorySearch``
        :return: the directory search results
        :rtype: ``osid.filing.DirectorySearchResults``
        :raise: ``NullArgument`` -- ``directory_query`` or ``directory_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``directory_query`` or ``directory_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_directory_query_from_inspector(self, directory_query_inspector):
        """Gets a directory query from an inspector.
        The inspector is available from an ``DirectorySearchResults``.

        :param directory_query_inspector: a query inspector
        :type directory_query_inspector: ``osid.filing.DirectoryQueryInspector``
        :return: the directory query
        :rtype: ``osid.filing.DirectoryQuery``
        :raise: ``NullArgument`` -- ``directory_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``directory_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.filing.DirectoryAdminSession

    def can_modify_directory(self):
        """Tests if this user can create or remove entries in this directory.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known modifying this
        directory will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if modifying this directory is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def overwrite(self):
        """Overwrite files if a destination pathname exists and is a file."""
        raise UNIMPLEMENTED()

    def can_create_file_with_record_types(self, file_record_types):
        """Tests if this user can create a single ``File`` using the desired record types.
        While ``FilingManager.getFileRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``File``.
        Providing an empty array tests if a ``File`` can be created with
        no records.

        :param file_record_types: array of file record types
        :type file_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``File`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``file_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_file_form_for_create(self, name, file_record_types):
        """Gets the file form for creating new files.
        A new form should be requested for each create transaction.

        :param name: name of a file
        :type name: ``string``
        :param file_record_types: array of file record types
        :type file_record_types: ``osid.type.Type[]``
        :return: the file form
        :rtype: ``osid.filing.FileForm``
        :raise: ``AlreadyExists`` -- ``name`` already exists as a file in this direrctory and ``overwrite()`` is ``false``
        :raise: ``InvalidArgument`` -- ``name`` is invalid
        :raise: ``NullArgument`` -- ``name`` or ``file_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_file(self, file_form):
        """Creates a new file in this directory.

        :param file_form: the file form
        :type file_form: ``osid.filing.FileForm``
        :return: the new file
        :rtype: ``osid.filing.File``
        :raise: ``IllegalState`` -- ``file_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``file_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``file_form`` did not originate from ``get_file_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def get_file_form_for_update(self, file_id):
        """Gets the file form for updating an existing files.
        A new file form should be requested for each update transaction.

        :param file_id: ``Id`` of the file to update
        :type file_id: ``osid.id.Id``
        :return: the file form
        :rtype: ``osid.filing.FileForm``
        :raise: ``NotFound`` -- ``file_id`` is not found
        :raise: ``NullArgument`` -- ``file_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_file(self, file_form):
        """Updates an existing file.

        :param file_form: the form containing the elements to be updated
        :type file_form: ``osid.filing.FileForm``
        :raise: ``IllegalState`` -- ``file_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``file_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``file_form`` did not originate from ``get_file_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def delete_file(self, file_id):
        """Deletes a file.

        :param file_id: the ``Id`` of the file to delete
        :type file_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``file_id`` is not found
        :raise: ``NullArgument`` -- ``file_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_create_directory_with_record_types(self, directory_record_types):
        """Tests if this user can create a single ``Directory`` using the desired record types.
        While ``FilingManager.getDiectoryRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Directory``.
        Providing an empty array tests if a ``Directory`` can be created
        with no records.

        :param directory_record_types: array of directory record types
        :type directory_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Directory`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``directory_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_directory_form_for_create(self, name, directory_record_types):
        """Gets the file form for creating new directories.
        A new form should be requested for each create transaction. This
        method is used for creating new ``Directories`` where only the
        ``Directory`` ``Type`` is known.

        :param name: the name of a subdirectory in this directory
        :type name: ``string``
        :param directory_record_types: array of directory record types
        :type directory_record_types: ``osid.type.Type[]``
        :return: the directory form
        :rtype: ``osid.filing.DirectoryForm``
        :raise: ``AlreadyExists`` -- directory already exists and ``overwrite()`` is false
        :raise: ``InvalidArgument`` -- ``name`` is invalid
        :raise: ``NullArgument`` -- ``name`` or ``directory_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_directory(self, directory_form):
        """Creates a new directory.

        :param directory_form: the directory form
        :type directory_form: ``osid.filing.DirectoryForm``
        :return: the new directory
        :rtype: ``osid.filing.Directory``
        :raise: ``IllegalState`` -- ``directory_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``directory_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``directory_form`` did not originate from ``get_directory_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def get_directory_form_for_update(self, directory_id):
        """Gets the directory form for updating an existing files.
        A new directory form should be requested for each update
        transaction. This method is used when the ``Directory`` to be
        updated is known and is desired to access any metadata specific
        to the ``Directory`` being updated.

        :param directory_id: ``Id`` of the directory to update
        :type directory_id: ``osid.id.Id``
        :return: the directory form
        :rtype: ``osid.filing.DirectoryForm``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_directory(self, directory_form):
        """Updates an existing directory.

        :param directory_form: the form containing the elements to be updated
        :type directory_form: ``osid.filing.DirectoryForm``
        :raise: ``IllegalState`` -- ``directory_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``directory_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``directory_form`` did not originate from ``get_directory_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def delete_directory(self, directory_id):
        """Deletes a directory in this directory.
        The directory to remove must be empty.

        :param directory_id: the ``Id`` of the directory to delete
        :type directory_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def clear_directory(self, directory_id):
        """Deletes all files and subdirectories within the given directory.

        :param directory_id: the ``Id`` of the directory to delete
        :type directory_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.filing.DirectoryNotificationSession

    def can_register_for_directory_notifications(self):
        """Tests if this user can register for ``Directory`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_directories(self):
        """Register for notifications of new directories.
        ``DirectoryReceiver.newDirectory()`` is invoked when a new
        ``Directory`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_directories(self):
        """Registers for notification of updated directories.
        ``DirectoryReceiver.changedDirectory()`` is invoked when a file
        is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_directory(self, directory_id):
        """Registers for notification of an updated file.
        ``DirectoryReceiver.changedDirectory()`` is invoked when the
        specified directory is changed.

        :param directory_id: the ``Id`` of the directory to monitor
        :type directory_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``directory_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_directories(self):
        """Registers for notification of deleted directories.
        ``DirectoryReceiver.deletedDirectory()`` is invoked when a
        directory is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_directory(self, directory_id):
        """Registers for notification of a deleted directory.
        ``DirectoryReceiver.changedDirectory()`` is invoked when the
        specified directory is deleted.

        :param directory_id: the ``Id`` of the directory to monitor
        :type directory_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``directory_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class FilingProxyManager(osid_managers.OsidProxyManager, FilingProfile):

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_filing_allocation_proxy_manager(self):
        """Gets the ``FilingAllocationProxyManager``.

        :return: a ``FilingAllocationProxyManager``
        :rtype: ``osid.filing.allocation.FilingAllocationProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_filing_allocation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    filing_allocation_proxy_manager = property(fget=get_filing_allocation_proxy_manager)


##
# The following methods are from osid.filing.DirectoryLookupSession

    def get_directory_id(self):
        """Gets the ``Id`` of this directory.

        :return: the ``Id`` of this directory
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    directory_id = property(fget=get_directory_id)

    def get_directory(self):
        """Gets the directory associated with this session.

        :return: the directory associated with this session
        :rtype: ``osid.filing.Directory``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    directory = property(fget=get_directory)

    def can_lookup_directories(self):
        """Tests if this user can perform entry lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.


        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_directory_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.




        """
        raise UNIMPLEMENTED()

    def use_plenary_directory_view(self):
        """A complete view of the directory returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.




        """
        raise UNIMPLEMENTED()

    def use_federated_directory_view(self):
        """Federates the view for methods in this session.
        A federated view will include entries in directories which are
        children of this directory.




        """
        raise UNIMPLEMENTED()

    def use_isolated_directory_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this directory only.




        """
        raise UNIMPLEMENTED()

    def get_directories_by_ids(self, directory_ids):
        """Gets a ``DirectoryList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the
        directories specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Directories`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.


        :param directory_ids: the list of ``Ids`` to retrieve
        :type directory_ids: ``osid.id.IdList``
        :return: the returned ``Directory`` list
        :rtype: ``osid.filing.DirectoryList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``directory_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_directories_by_genus_type(self, dircetory_genus_type):
        """Gets a ``DirectoryList`` corresponding to the given directory genus ``Type`` which does not include directories of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        directories or an error results. Otherwise, the returned list
        may contain only those directories that are accessible through
        this session.


        :param dircetory_genus_type: a directory genus type
        :type dircetory_genus_type: ``osid.type.Type``
        :return: the returned ``Directory list``
        :rtype: ``osid.filing.DirectoryList``
        :raise: ``NullArgument`` -- ``directory_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_directories_by_parent_genus_type(self, directory_genus_type):
        """Gets a ``DirectoryList`` corresponding to the given directory genus ``Type`` and include any additional directories with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        directories or an error results. Otherwise, the returned list
        may contain only those directories that are accessible through
        this session.


        :param directory_genus_type: a directory genus type
        :type directory_genus_type: ``osid.type.Type``
        :return: the returned ``Directory`` list
        :rtype: ``osid.filing.DirectoryList``
        :raise: ``NullArgument`` -- ``directory_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_directories_by_record_type(self, directory_record_type):
        """Gets a ``DirectoryList`` corresponding to the given directory record ``Type``.
        The set of directories implementing the given record type is
        returned.In plenary mode, the returned list contains all known
        directories or an error results. Otherwise, the returned list
        may contain only those directories that are accessible through
        this session.


        :param directory_record_type: a directory record type
        :type directory_record_type: ``osid.type.Type``
        :return: the returned ``Directory`` list
        :rtype: ``osid.filing.DirectoryList``
        :raise: ``NullArgument`` -- ``directory_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_directories_by_provider(self, resource_id):
        """Gets a ``DirectoryList`` for the given provider.
        In plenary mode, the returned list contains all known
        directories or an error results. Otherwise, the returned list
        may contain only those directories that are accessible through
        this session.


        :param resource_id: a resource Id
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Directory`` list
        :rtype: ``osid.filing.DirectoryList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_directories(self):
        """Gets the list of directories inthis directory.
        In a federated view, this method returns all directories in
        descendant directories. In plenary mode, the returned list
        contains all known directories or an error results. Otherwise,
        the returned list may contain only those directories that are
        accessible through this session.


        :return: the list of directories in this directory
        :rtype: ``osid.filing.DirectoryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    directories = property(fget=get_directories)


##
# The following methods are from osid.filing.DirectoryQuerySession

    def can_search_directories(self):
        """Tests if this user can perform ``Directory`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_directory_query(self):
        """Gets a directory query.

        :return: the directory query
        :rtype: ``osid.filing.DirectoryQuery``

        """
        raise UNIMPLEMENTED()

    directory_query = property(fget=get_directory_query)

    def get_directories_by_query(self, directory_query):
        """Gets a list of ``Directory`` objects matching the given directory query.

        :param directory_query: the directory query
        :type directory_query: ``osid.filing.DirectoryQuery``
        :return: the returned ``DirectoryList``
        :rtype: ``osid.filing.DirectoryList``
        :raise: ``NullArgument`` -- ``directory_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``directory_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.filing.DirectorySearchSession

    def get_directory_search(self):
        """Gets a diectory search.

        :return: the directory search
        :rtype: ``osid.filing.DirectorySearch``

        """
        raise UNIMPLEMENTED()

    directory_search = property(fget=get_directory_search)

    def get_directory_search_order(self):
        """Gets a directory search order.
        The ``DirectorySearchOrder`` is supplied to a
        ``DirectorySearch`` to specify the ordering of results.


        :return: the directory search order
        :rtype: ``osid.filing.DirectorySearchOrder``

        """
        raise UNIMPLEMENTED()

    directory_search_order = property(fget=get_directory_search_order)

    def get_directories_by_search(self, directory_query, directory_search):
        """Gets the search results matching the given search.

        :param directory_query: the directory query
        :type directory_query: ``osid.filing.DirectoryQuery``
        :param directory_search: the directory search
        :type directory_search: ``osid.filing.DirectorySearch``
        :return: the directory search results
        :rtype: ``osid.filing.DirectorySearchResults``
        :raise: ``NullArgument`` -- ``directory_query`` or ``directory_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``directory_query`` or ``directory_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_directory_query_from_inspector(self, directory_query_inspector):
        """Gets a directory query from an inspector.
        The inspector is available from an ``DirectorySearchResults``.


        :param directory_query_inspector: a query inspector
        :type directory_query_inspector: ``osid.filing.DirectoryQueryInspector``
        :return: the directory query
        :rtype: ``osid.filing.DirectoryQuery``
        :raise: ``NullArgument`` -- ``directory_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``directory_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.filing.DirectoryAdminSession

    def can_modify_directory(self):
        """Tests if this user can create or remove entries in this directory.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known modifying this
        directory will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.


        :return: ``false`` if modifying this directory is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def overwrite(self):
        """Overwrite files if a destination pathname exists and is a file."""
        raise UNIMPLEMENTED()

    def can_create_file_with_record_types(self, file_record_types):
        """Tests if this user can create a single ``File`` using the desired record types.
        While ``FilingManager.getFileRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``File``.
        Providing an empty array tests if a ``File`` can be created with
        no records.


        :param file_record_types: array of file record types
        :type file_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``File`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``file_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_file_form_for_create(self, name, file_record_types):
        """Gets the file form for creating new files.
        A new form should be requested for each create transaction.


        :param name: name of a file
        :type name: ``string``
        :param file_record_types: array of file record types
        :type file_record_types: ``osid.type.Type[]``
        :return: the file form
        :rtype: ``osid.filing.FileForm``
        :raise: ``AlreadyExists`` -- ``name`` already exists as a file in this direrctory and ``overwrite()`` is ``false``
        :raise: ``InvalidArgument`` -- ``name`` is invalid
        :raise: ``NullArgument`` -- ``name`` or ``file_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_file(self, file_form):
        """Creates a new file in this directory.

        :param file_form: the file form
        :type file_form: ``osid.filing.FileForm``
        :return: the new file
        :rtype: ``osid.filing.File``
        :raise: ``IllegalState`` -- ``file_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``file_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``file_form`` did not originate from ``get_file_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def get_file_form_for_update(self, file_id):
        """Gets the file form for updating an existing files.
        A new file form should be requested for each update transaction.


        :param file_id: ``Id`` of the file to update
        :type file_id: ``osid.id.Id``
        :return: the file form
        :rtype: ``osid.filing.FileForm``
        :raise: ``NotFound`` -- ``file_id`` is not found
        :raise: ``NullArgument`` -- ``file_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_file(self, file_form):
        """Updates an existing file.

        :param file_form: the form containing the elements to be updated
        :type file_form: ``osid.filing.FileForm``
        :raise: ``IllegalState`` -- ``file_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``file_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``file_form`` did not originate from ``get_file_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def delete_file(self, file_id):
        """Deletes a file.

        :param file_id: the ``Id`` of the file to delete
        :type file_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``file_id`` is not found
        :raise: ``NullArgument`` -- ``file_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_create_directory_with_record_types(self, directory_record_types):
        """Tests if this user can create a single ``Directory`` using the desired record types.
        While ``FilingManager.getDiectoryRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Directory``.
        Providing an empty array tests if a ``Directory`` can be created
        with no records.


        :param directory_record_types: array of directory record types
        :type directory_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Directory`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``directory_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_directory_form_for_create(self, name, directory_record_types):
        """Gets the file form for creating new directories.
        A new form should be requested for each create transaction. This
        method is used for creating new ``Directories`` where only the
        ``Directory`` ``Type`` is known.


        :param name: the name of a subdirectory in this directory
        :type name: ``string``
        :param directory_record_types: array of directory record types
        :type directory_record_types: ``osid.type.Type[]``
        :return: the directory form
        :rtype: ``osid.filing.DirectoryForm``
        :raise: ``AlreadyExists`` -- directory already exists and ``overwrite()`` is false
        :raise: ``InvalidArgument`` -- ``name`` is invalid
        :raise: ``NullArgument`` -- ``name`` or ``directory_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_directory(self, directory_form):
        """Creates a new directory.

        :param directory_form: the directory form
        :type directory_form: ``osid.filing.DirectoryForm``
        :return: the new directory
        :rtype: ``osid.filing.Directory``
        :raise: ``IllegalState`` -- ``directory_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``directory_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``directory_form`` did not originate from ``get_directory_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def get_directory_form_for_update(self, directory_id):
        """Gets the directory form for updating an existing files.
        A new directory form should be requested for each update
        transaction. This method is used when the ``Directory`` to be
        updated is known and is desired to access any metadata specific
        to the ``Directory`` being updated.


        :param directory_id: ``Id`` of the directory to update
        :type directory_id: ``osid.id.Id``
        :return: the directory form
        :rtype: ``osid.filing.DirectoryForm``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_directory(self, directory_form):
        """Updates an existing directory.

        :param directory_form: the form containing the elements to be updated
        :type directory_form: ``osid.filing.DirectoryForm``
        :raise: ``IllegalState`` -- ``directory_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``directory_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``directory_form`` did not originate from ``get_directory_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def delete_directory(self, directory_id):
        """Deletes a directory in this directory.
        The directory to remove must be empty.


        :param directory_id: the ``Id`` of the directory to delete
        :type directory_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def clear_directory(self, directory_id):
        """Deletes all files and subdirectories within the given directory.

        :param directory_id: the ``Id`` of the directory to delete
        :type directory_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.filing.DirectoryNotificationSession

    def can_register_for_directory_notifications(self):
        """Tests if this user can register for ``Directory`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.


        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_directories(self):
        """Register for notifications of new directories.
        ``DirectoryReceiver.newDirectory()`` is invoked when a new
        ``Directory`` is created.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_directories(self):
        """Registers for notification of updated directories.
        ``DirectoryReceiver.changedDirectory()`` is invoked when a file
        is changed.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_directory(self, directory_id):
        """Registers for notification of an updated file.
        ``DirectoryReceiver.changedDirectory()`` is invoked when the
        specified directory is changed.


        :param directory_id: the ``Id`` of the directory to monitor
        :type directory_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``directory_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_directories(self):
        """Registers for notification of deleted directories.
        ``DirectoryReceiver.deletedDirectory()`` is invoked when a
        directory is deleted.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_directory(self, directory_id):
        """Registers for notification of a deleted directory.
        ``DirectoryReceiver.changedDirectory()`` is invoked when the
        specified directory is deleted.


        :param directory_id: the ``Id`` of the directory to monitor
        :type directory_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``directory_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class Directory(osid_objects.OsidCatalog, osid_sessions.OsidSession, DirectoryEntry):

    def get_directory_record(self, directory_record_type):
        """Gets the directory record corresponding to the given ``Directory`` record ``Type``.
        This method is used to retrieve an object implementing the
        requested record. The ``directory_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(directory_record_type)`` is ``true`` .

        :param directory_record_type: the directory record type
        :type directory_record_type: ``osid.type.Type``
        :return: the directory record
        :rtype: ``osid.filing.records.DirectoryRecord``
        :raise: ``NullArgument`` -- ``directory_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(directory_record_type)`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.filing.FileSystemSession

    def get_directory_id(self):
        """Gets the ``Id`` of this directory.

        :return: the ``Id`` of this directory
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    directory_id = property(fget=get_directory_id)

    def get_directory(self):
        """Gets the directory associated with this session.

        :return: the directory associated with this session
        :rtype: ``osid.filing.Directory``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    directory = property(fget=get_directory)

    def can_lookup_directory_entries(self):
        """Tests if this user can perform entry lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def has_parent_directory(self):
        """Tests if the directory associated with this session has a parent directory.

        :return: ``true`` if a parent exists, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_parent_directory(self):
        """Gets the parent of the directory associated with this session.

        :return: the parent of the directory associated with this session
        :rtype: ``osid.filing.Directory``
        :raise: ``IllegalState`` -- ``has_parent_directory()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    parent_directory = property(fget=get_parent_directory)

    def use_comparative_directory_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_directory_view(self):
        """A complete view of the file or directory returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_directory_view(self):
        """Federates the view for methods in this session.
        A federated view will include entries in directories which are
        children of this directory.



        """
        raise UNIMPLEMENTED()

    def use_isolated_directory_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this directory only.



        """
        raise UNIMPLEMENTED()

    def exists(self, name):
        """Tests if a file, directory or alias name exists.
        In a federated view, the existence test is performed on this
        directory and any children of this directory. In an isolated
        view, the existence test is restrcited to this directory only.

        :param name: a file or directory name
        :type name: ``string``
        :return: ``true`` if the name exists, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``name`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_file(self, name):
        """Tests if a name exists and is a file or an alias to a file.
        In a federated view, the exietence test is performed on this
        directory and any children of this directory. In an isolated
        view, the existence test is restrcited to this directory only.

        :param name: a file name
        :type name: ``string``
        :return: ``true`` if the name is a file, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``name`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_directory(self, name):
        """Tests if a name exists and is a directory or an alias to a directory.
        In a federated view, the exietence test is performed on this
        directory and any children of this directory. In an isolated
        view, the existence test is restrcited to this directory only.

        :param name: a file or directory name
        :type name: ``string``
        :return: ``true`` if the path is a directory, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``name`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_alias(self, name):
        """Tests if a name exists and is an alias.
        In a federated view, the exietence test is performed on this
        directory and any children of this directory. In an isolated
        view, the existence test is restrcited to this directory only.

        :param name: a file or directory name
        :type name: ``string``
        :return: ``true`` if the path is an alias, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``name`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_file(self, name):
        """Gets a specified file or alias to the file by its name in the current directory only.
        For federated views, use ``getFilesByName()``.

        :param name: the name to the file
        :type name: ``string``
        :return: the file
        :rtype: ``osid.filing.File``
        :raise: ``NotFound`` -- ``name`` is not found or is a directory
        :raise: ``NullArgument`` -- ``name`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_files_by_name(self, name):
        """Gets a specified files and aliases to files for the given file name.
        In an isolated view, this method behaves like ``getFile()``. Is
        a federated view, this method returns a list of files by the
        same name in descendant directories. In plenary mode, the
        returned list contains all known files or an error results.
        Otherwise, the returned list may contain only those files that
        are accessible through this session.

        :param name: the name of the file
        :type name: ``string``
        :return: the list of files of the given name
        :rtype: ``osid.filing.FileList``
        :raise: ``NullArgument`` -- ``name`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_files(self):
        """Gets the list of files and aliases to files in this directory.
        In a federated view, this method returns all files in descendant
        directories. In plenary mode, the returned list contains all
        known files or an error results. Otherwise, the returned list
        may contain only those files that are accessible through this
        session.

        :return: the list of files in this directory
        :rtype: ``osid.filing.FileList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    files = property(fget=get_files)

    def get_subdirectory(self, name):
        """Gets a specified directory or alias to the directory by its name in the current directory only.
        For federated views, use ``getDirectoriesByName()``.

        :param name: the name of the directory
        :type name: ``string``
        :return: the directory
        :rtype: ``osid.filing.Directory``
        :raise: ``NotFound`` -- ``name`` is not found or is a file
        :raise: ``NullArgument`` -- ``name`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_subdirectories_by_name(self, name):
        """Gets a specified directories and aliases to directories for the given directory name.
        In an isolated view, this method behaves like
        ``getDirectory()``. Is a federated view, this method returns a
        list of directories by the same name in descedent directories.
        In plenary mode, the returned list contains all known files or
        an error results. Otherwise, the returned list may contain only
        those files that are accessible through this session.

        :param name: the name of the file
        :type name: ``string``
        :return: the list of files of the given name
        :rtype: ``osid.filing.DirectoryList``
        :raise: ``NullArgument`` -- ``name`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_subdirectories(self):
        """Gets the list of directories and aliases to directories in this directory.
        In a federated view, this method returns all directories in
        descedent directories. In plenary mode, the returned list
        contains all known files or an error results. Otherwise, the
        returned list may contain only those files that are accessible
        through this session.

        :return: the list of directories in this directory
        :rtype: ``osid.filing.DirectoryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    subdirectories = property(fget=get_subdirectories)


##
# The following methods are from osid.filing.FileSystemManagementSession

    def can_manage_filing(self):
        """Tests if this user can perform functions in this session.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if filing management methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def overwrite(self, overwite):
        """Overwrite files if a destination pathname exists.

        :param overwite: ``true`` if files can be overwritten, ``false`` otherwise
        :type overwite: ``boolean``

        """
        raise UNIMPLEMENTED()

    def create_missing_paths(self, create):
        """Create any missing directories for a destination path that does not exist.

        :param create: ``true`` if intermediate directories should be created, ``false`` otherwise
        :type create: ``boolean``

        """
        raise UNIMPLEMENTED()

    def move_file(self, src, dst):
        """Moves a file to another path.
        The detination path may be a file or directory. If the
        destination is a file and exists, the destination is only
        replaced if ``overwrite()`` is ``true``. If the destination is a
        directory and does not exist, the missing directories are only
        created if ``create_missing_paths()`` is ``true``.

        :param src: the source ``Id`` of the file
        :type src: ``osid.id.Id``
        :param dst: the destination name or path of the directory or file
        :type dst: ``string``
        :raise: ``AlreadyExists`` -- ``dst`` exists and ``overwrite()`` is ``false``
        :raise: ``InvalidArgument`` -- ``src`` is not a file
        :raise: ``NotFound`` -- ``src`` is not found, or the path to ``dst`` is not found and ``create_missing_paths()`` is ``false``
        :raise: ``NullArgument`` -- ``src`` or ``dst`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def move_directory(self, src, dst):
        """Moves a directory to another path.
        The destination must be a directory and if exists, the source
        directory is placed as a child to the given directory. If a path
        component in the destination does not exist, the path is created
        is ``create_missing_paths()`` is ``true``.

        :param src: the source ``Id`` of the directory
        :type src: ``osid.id.Id``
        :param dst: the destination name or path of the directory
        :type dst: ``string``
        :raise: ``InvalidArgument`` -- ``src`` is not a directory
        :raise: ``NotFound`` -- ``src`` is not found, or the path to ``dst`` is not found and ``create_missing_paths()`` is ``false``
        :raise: ``NullArgument`` -- ``src`` or ``dst`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def copy_file(self, src, dst):
        """Copies a file to another path.
        The detination path may be a file or directory. If the
        destination is a file and exists, the destination is only
        replaced if ``overwrite()`` is ``true``. If the destination is a
        directory and does not exist, the missing directories are only
        created if ``create_missing_paths()`` is ``true``.

        :param src: the source ``Id`` of the file
        :type src: ``osid.id.Id``
        :param dst: the destination name or path of the directory or file
        :type dst: ``string``
        :return: the new file
        :rtype: ``osid.filing.File``
        :raise: ``AlreadyExists`` -- ``dst`` exists and ``overwrite()`` is ``false``
        :raise: ``InvalidArgument`` -- ``src`` is not a file
        :raise: ``NotFound`` -- ``src`` is not found, or the path to ``dst`` is not found and ``create_missing_paths()`` is ``false``
        :raise: ``NullArgument`` -- ``src`` or ``dst`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def copy_directory(self, src, dst):
        """Copies a directory and all of its contents to another path.
        The destination must be a directory and if exists, the source
        directory is placed as a child to the given directory. If a path
        component in the destination does not exist, the path is created
        is ``create_missing_paths()`` is ``true``.

        :param src: the source ``Id`` of the directory
        :type src: ``osid.id.Id``
        :param dst: the destination name or path of the directory
        :type dst: ``string``
        :return: the new file
        :rtype: ``osid.filing.Directory``
        :raise: ``InvalidArgument`` -- ``src`` is not a directory
        :raise: ``NotFound`` -- ``src`` is not found, or the path to ``dst`` is not found and ``create_missing_paths()`` is ``false``
        :raise: ``NullArgument`` -- ``src`` or ``dst`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def link_file(self, file_id, link):
        """Creates a link from one file to another.

        :param file_id: the ``Id`` of a file
        :type file_id: ``osid.id.Id``
        :param link: the link path
        :type link: ``string``
        :return: the link
        :rtype: ``osid.filing.File``
        :raise: ``AlreadyExists`` -- ``link already`` exists
        :raise: ``NotFound`` -- ``file_id`` is not found, or the path to ``link`` is not found and ``create_missing_paths()`` is ``false``
        :raise: ``NullArgument`` -- ``file_id`` or ``link`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def link_directory(self, directory_id, link):
        """Creates a link from one directory to another.

        :param directory_id: the ``Id`` of a directory
        :type directory_id: ``osid.id.Id``
        :param link: the destination path
        :type link: ``string``
        :return: the link
        :rtype: ``osid.filing.Directory``
        :raise: ``AlreadyExists`` -- ``link already`` exists
        :raise: ``NotFound`` -- ``directory_id`` is not found, or the path to ``link`` is not found and ``create_missing_paths()`` is ``false``
        :raise: ``NullArgument`` -- ``directory_id`` or ``link`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.filing.FileContentSession

    def can_read_files(self):
        """Tests if this user can access files in this directory.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known accessing this file
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer read
        operations to unauthorized users.

        :return: ``false`` if file access is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_input_stream(self, name):
        """Gets the input stream for reading a file.
        The input stream reads until the end of the file.

        :param name: the relative or absolute path name
        :type name: ``string``
        :return: the input stream for reading this file
        :rtype: ``osid.transport.DataInputStream``
        :raise: ``NotFound`` -- ``name`` is not found
        :raise: ``NullArgument`` -- ``name`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_blocking_input_stream(self, name):
        """Gets the input stream for reading this file.
        The returned input stream, once it reaches the end of the file,
        blocks for new content that may be later appended to the file.

        :param name: the relative or absolute path name
        :type name: ``string``
        :return: the input stream for reading this file
        :rtype: ``osid.transport.DataInputStream``
        :raise: ``NotFound`` -- ``name`` is not found
        :raise: ``NullArgument`` -- ``name`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_write_files(self):
        """Tests if this user can update this file.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known writing to this this
        file will result in a ``PermissionDenied``. This is intended as
        a hint to an application that may not wish to offer write
        operations to unauthorized users.

        :return: ``false`` if file writing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_output_stream(self, name):
        """Gets an output stream for writing to this file, replacing any existing contents.

        :param name: the relative or absolute path name
        :type name: ``string``
        :return: the output stream for writing to this file
        :rtype: ``osid.transport.DataOutputStream``
        :raise: ``NotFound`` -- ``name`` is not found
        :raise: ``NullArgument`` -- ``name`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_output_stream_for_append(self, name):
        """Gets an output stream for appending to this file.

        :param name: the relative or absolute path name
        :type name: ``string``
        :return: the output stream for appending to this file
        :rtype: ``osid.transport.DataOutputStream``
        :raise: ``NotFound`` -- ``name`` is not found
        :raise: ``NullArgument`` -- ``name`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def touch(self, name):
        """Updates the modified time of a file to be the current time.

        :param name: the relative or absolute path name
        :type name: ``string``
        :raise: ``NotFound`` -- ``name`` is not found
        :raise: ``NullArgument`` -- ``name`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.filing.FileLookupSession

    def can_lookup_files(self):
        """Tests if this user can perform entry lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_file_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_file_view(self):
        """A complete view of the file returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_files_by_ids(self, file_ids):
        """Gets a ``FileList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the files
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Fies`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param file_ids: the list of ``Ids`` to retrieve
        :type file_ids: ``osid.id.IdList``
        :return: the returned ``File`` list
        :rtype: ``osid.filing.FileList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``file_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_files_by_genus_type(self, file_genus_type):
        """Gets a ``FileList`` corresponding to the given file genus ``Type`` which does not include files of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known files or
        an error results. Otherwise, the returned list may contain only
        those files that are accessible through this session.

        :param file_genus_type: a file genus type
        :type file_genus_type: ``osid.type.Type``
        :return: the returned ``File list``
        :rtype: ``osid.filing.FileList``
        :raise: ``NullArgument`` -- ``file_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_files_by_parent_genus_type(self, file_genus_type):
        """Gets a ``FileList`` corresponding to the given file genus ``Type`` and include any additional files with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known files or
        an error results. Otherwise, the returned list may contain only
        those files that are accessible through this session.

        :param file_genus_type: a file genus type
        :type file_genus_type: ``osid.type.Type``
        :return: the returned ``File`` list
        :rtype: ``osid.filing.FileList``
        :raise: ``NullArgument`` -- ``file_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_files_by_record_type(self, file_record_type):
        """Gets a ``FileList`` corresponding to the given file record ``Type``.
        The set of files implementing the given record type is
        returned.In plenary mode, the returned list contains all known
        files or an error results. Otherwise, the returned list may
        contain only those files that are accessible through this
        session.

        :param file_record_type: a file record type
        :type file_record_type: ``osid.type.Type``
        :return: the returned ``File`` list
        :rtype: ``osid.filing.FileList``
        :raise: ``NullArgument`` -- ``file_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.filing.FileQuerySession

    def can_search_files(self):
        """Tests if this user can perform ``File`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_file_query(self):
        """Gets a file query.

        :return: the file query
        :rtype: ``osid.filing.FileQuery``

        """
        raise UNIMPLEMENTED()

    file_query = property(fget=get_file_query)

    def get_files_by_query(self, file_query):
        """Gets a list of ``Files`` matching the given file query.

        :param file_query: the file query
        :type file_query: ``osid.filing.FileQuery``
        :return: the returned ``FileList``
        :rtype: ``osid.filing.FileList``
        :raise: ``NullArgument`` -- ``file_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``file_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.filing.FileSearchSession

    def get_file_search(self):
        """Gets a file search.

        :return: the file search
        :rtype: ``osid.filing.FileSearch``

        """
        raise UNIMPLEMENTED()

    file_search = property(fget=get_file_search)

    def get_file_search_order(self):
        """Gets a file search order.
        The ``FileSearchOrder`` is supplied to a ``FileSearch`` to
        specify the ordering of results.

        :return: the file search order.
        :rtype: ``osid.filing.FileSearchOrder``

        """
        raise UNIMPLEMENTED()

    file_search_order = property(fget=get_file_search_order)

    def get_files_by_search(self, file_query, file_search):
        """Gets the search results matching the given search query using the given search.

        :param file_query: the file query
        :type file_query: ``osid.filing.FileQuery``
        :param file_search: the file search
        :type file_search: ``osid.filing.FileSearch``
        :return: the file search results
        :rtype: ``osid.filing.FileSearchResults``
        :raise: ``NullArgument`` -- ``file_query`` or ``file_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``file_query`` or ``file_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_file_query_from_inspector(self, file_query_inspector):
        """Gets a file query from an inspector.
        The inspector is available from a ``FileSearchResults``.

        :param file_query_inspector: a query inspector
        :type file_query_inspector: ``osid.filing.FileQueryInspector``
        :return: the file query
        :rtype: ``osid.filing.FileQuery``
        :raise: ``NullArgument`` -- ``file_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``file_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.filing.FileNotificationSession

    def can_register_for_file_notifications(self):
        """Tests if this user can register for ``File`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_files(self):
        """Register for notifications of new files.
        ``FileReceiver.newFile()`` is invoked when a new ``File`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_files(self):
        """Registers for notification of updated files.
        ``FileReceiver.changedFile()`` is invoked when a file is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_file(self, file_id):
        """Registers for notification of an updated file.
        ``FileReceiver.changedFile()`` is invoked when the specified
        file is changed.

        :param file_id: the ``Id`` of the file
        :type file_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``file_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_files(self):
        """Registers for notification of deleted files.
        ``FileReceiver.deletedFile()`` is invoked when a file is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_file(self, file_id):
        """Registers for notification of a deleted file.
        ``FileReceiver.changedFile()`` is invoked when the specified
        file is deleted.

        :param file_id: the ``Id`` of the file
        :type file_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``file_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.filing.FileSmartDirectorySession

    def can_manage_smart_directories(self):
        """Tests if this user can manage smart directories.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart directory management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_file_query(self, file_query):
        """Applies a file query to this directory.

        :param file_query: the file query
        :type file_query: ``osid.filing.FileQuery``
        :raise: ``NullArgument`` -- ``file_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``file_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_file_query(self):
        """Gets a file query inspector for this directory.

        :return: the file query inspector
        :rtype: ``osid.filing.FileQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_file_sequencing(self, file_search_order):
        """Applies a file search order to this directory.

        :param file_search_order: the file search order
        :type file_search_order: ``osid.filing.FileSearchOrder``
        :raise: ``NullArgument`` -- ``file_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``file_search_order`` not of this service

        """
        raise UNIMPLEMENTED()



class DirectoryList(osid_objects.OsidList):

    def get_next_directory(self):
        """Gets the next ``Directory`` in this list.

        :return: the next ``Directory`` in this list. The ``has_next()`` method should be used to test that a next ``Dircectory`` is available before calling this method.
        :rtype: ``osid.filing.Directory``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    next_directory = property(fget=get_next_directory)

    def get_next_directories(self, n):
        """Gets the next set of ``Directory`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Directory`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Directory`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.filing.Directory``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()



class Directorys(FilingManager):
    pass


