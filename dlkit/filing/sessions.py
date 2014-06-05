from ..osid import sessions as osid_sessions


class FileSystemSession(osid_sessions.OsidSession):
    """This session defines methods for examining file systems.

    A ``FileSystemSession`` is associated with a directory that, unlike
    other catalogs, behaves as the current directory path for supplying
    relative path names. Absolute path names can be supplied to access
    any file or directory in the file system.

    This session defines the following views:
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition
      * federated directory view: searches include entries in
        directories of which this directory is an ancestor
      * isolated directory view: lookups are restricted to entries in
        this directory only

    
    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data out of sync. Some
    administrative applications may need to know whether it had
    retrieved an entire set of objects and may sacrifice some
    interoperability for the sake of precision using the plenary view.

    """
    def get_directory_id(self):
        """Gets the ``Id`` of this directory.

        :return: the ``Id`` of this directory
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    directory_id = property(fget=get_directory_id)

    def get_directory(self):
        """Gets the directory associated with this session.

        :return: the directory associated with this session
        :rtype: ``osid.filing.Directory``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.filing.Directory

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
        return # boolean

    def has_parent_directory(self):
        """Tests if the directory associated with this session has a parent directory.

        :return: ``true`` if a parent exists, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_parent_directory(self):
        """Gets the parent of the directory associated with this session.

        :return: the parent of the directory associated with this session
        :rtype: ``osid.filing.Directory``
        :raise: ``IllegalState`` -- ``has_parent_directory()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.filing.Directory

    parent_directory = property(fget=get_parent_directory)

    def use_comparative_directory_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_directory_view(self):
        """A complete view of the file or directory returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def use_federated_directory_view(self):
        """Federates the view for methods in this session.

        A federated view will include entries in directories which are
        children of this directory.



        """
        pass

    def use_isolated_directory_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this directory only.



        """
        pass

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
        return # boolean

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
        return # boolean

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
        return # boolean

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
        return # boolean

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
        return # osid.filing.File

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
        return # osid.filing.FileList

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
        return # osid.filing.FileList

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
        return # osid.filing.Directory

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
        return # osid.filing.DirectoryList

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
        return # osid.filing.DirectoryList

    subdirectories = property(fget=get_subdirectories)


class FileSystemManagementSession(osid_sessions.OsidSession):
    """This session defines methods for operating on files and directories.

    This session is an expanded version of the ``DirectoryAdminSession``
    that defines methods requiring path names for navigating a
    federation of directories as opposed to working within a single
    directory node.

    The directory associated with this session is the current working
    directory and any relative path names provided are with respect to
    this directory. Absolute pathnames may be supplied outside this
    directory.

    """
    def get_directory_id(self):
        """Gets the ``Id`` of this directory.

        :return: the ``Id`` of this directory
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    directory_id = property(fget=get_directory_id)

    def get_directory(self):
        """Gets the directory associated with this session.

        :return: the directory associated with this session
        :rtype: ``osid.filing.Directory``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.filing.Directory

    directory = property(fget=get_directory)

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
        return # boolean

    def overwrite(self, overwite):
        """Overwrite files if a destination pathname exists.

        :param overwite: ``true`` if files can be overwritten, ``false`` otherwise
        :type overwite: ``boolean``

        """
        pass

    def create_missing_paths(self, create):
        """Create any missing directories for a destination path that does not exist.

        :param create: ``true`` if intermediate directories should be created, ``false`` otherwise
        :type create: ``boolean``

        """
        pass

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
        pass

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
        pass

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
        return # osid.filing.File

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
        return # osid.filing.Directory

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
        return # osid.filing.File

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
        return # osid.filing.Directory


class FileContentSession(osid_sessions.OsidSession):
    """This session defines methods forreading and writing files.

    The directory associated with this session is the current working
    directory and any relative path names provided are with respect to
    this directory.

    """
    def get_directory_id(self):
        """Gets the ``Id`` of this directory.

        :return: the ``Id`` of this directory
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    directory_id = property(fget=get_directory_id)

    def get_directory(self):
        """Gets the directory associated with this session.

        :return: the directory associated with this session
        :rtype: ``osid.filing.Directory``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.filing.Directory

    directory = property(fget=get_directory)

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
        return # boolean

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
        return # osid.transport.DataInputStream

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
        return # osid.transport.DataInputStream

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
        return # boolean

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
        return # osid.transport.DataOutputStream

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
        return # osid.transport.DataOutputStream

    def touch(self, name):
        """Updates the modified time of a file to be the current time.

        :param name: the relative or absolute path name
        :type name: ``string``
        :raise: ``NotFound`` -- ``name`` is not found
        :raise: ``NullArgument`` -- ``name`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class FileLookupSession(osid_sessions.OsidSession):
    """This session defines methods for looking up on files in the current directory."""
    def get_directory_id(self):
        """Gets the ``Id`` of this directory.

        :return: the ``Id`` of this directory
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    directory_id = property(fget=get_directory_id)

    def get_directory(self):
        """Gets the directory associated with this session.

        :return: the directory associated with this session
        :rtype: ``osid.filing.Directory``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.filing.Directory

    directory = property(fget=get_directory)

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
        return # boolean

    def use_comparative_file_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_file_view(self):
        """A complete view of the file returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def use_federated_directory_view(self):
        """Federates the view for methods in this session.

        A federated view will include entries in directories which are
        children of this directory.



        """
        pass

    def use_isolated_directory_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this directory only.



        """
        pass

    def get_file(self, file_id):
        """Gets a specified file or alias to the file.

        :param file_id: the ``Id`` to the file
        :type file_id: ``osid.id.Id``
        :return: the file
        :rtype: ``osid.filing.File``
        :raise: ``NotFound`` -- ``file_id`` is not found
        :raise: ``NullArgument`` -- ``file_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.filing.File

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
        return # osid.filing.FileList

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
        return # osid.filing.FileList

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
        return # osid.filing.FileList

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
        return # osid.filing.FileList

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
        return # osid.filing.FileList

    files = property(fget=get_files)


class FileQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among files and directories objects.

    The search query is constructed using a ``FileQuery``.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.
    
      * federated directory view: searches include entries in
        directories of which this directory is a ancestor
      * isolated directory view: searches are restricted this directory
        only


    """
    def get_directory_id(self):
        """Gets the ``Id`` of this directory.

        :return: the ``Id`` of this directory
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    directory_id = property(fget=get_directory_id)

    def get_directory(self):
        """Gets the directory associated with this session.

        :return: the directory associated with this session
        :rtype: ``osid.filing.Directory``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.filing.Directory

    directory = property(fget=get_directory)

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
        return # boolean

    def use_federated_directory_view(self):
        """Federates the view for methods in this session.

        A federated view will include entries in directories which are
        children of this directory.



        """
        pass

    def use_isolated_directory_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this directory only.



        """
        pass

    def get_file_query(self):
        """Gets a file query.

        :return: the file query
        :rtype: ``osid.filing.FileQuery``

        """
        return # osid.filing.FileQuery

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
        return # osid.filing.FileList


class FileSearchSession(FileQuerySession):
    """This session provides methods for searching among files and directories objects.

    The search query is constructed using a ``FileQuery``.

    ``get_files_by_query()`` is the basic search method and returns a
    list of ``Files``. A more advanced search may be performed with
    ``getFilesBySearch()``. It accepts a ``FileSearch`` in addition to
    the query for the purpose of specifying additional options affecting
    the entire search, such as ordering. ``get_files_by_search()``
    returns an ``FileSearchResults`` that can be used to access the
    resulting ``FileList`` or be used to perform a search within the
    result set through ``FileSearch``.
    
    This session defines views that offer differing behaviors when
    retrieving multiple objects.
    
      * federated directory view: searches include entries in
        directories of which this directory is a ancestor
      * isolated directory view: searches are restricted this directory
        only


    """
    def get_file_search(self):
        """Gets a file search.

        :return: the file search
        :rtype: ``osid.filing.FileSearch``

        """
        return # osid.filing.FileSearch

    file_search = property(fget=get_file_search)

    def get_file_search_order(self):
        """Gets a file search order.

        The ``FileSearchOrder`` is supplied to a ``FileSearch`` to
        specify the ordering of results.

        :return: the file search order.
        :rtype: ``osid.filing.FileSearchOrder``

        """
        return # osid.filing.FileSearchOrder

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
        return # osid.filing.FileSearchResults

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
        return # osid.filing.FileQuery


class FileNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``Files``.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    Two view are defined in this session:
    
    federated view: includes notifications of files located in
    subdirectories in this directory
    
    isolated view: includes notifcations of files in this directory only

    """
    def get_directory_id(self):
        """Gets the ``Id`` of this directory.

        :return: the ``Id`` of this directory
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    directory_id = property(fget=get_directory_id)

    def get_directory(self):
        """Gets the ``Directory`` associated with this session.

        :return: the ``Directory`` associated with this session
        :rtype: ``osid.filing.Directory``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.filing.Directory

    directory = property(fget=get_directory)

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
        return # boolean

    def use_federated_directory_view(self):
        """Federates the view for methods in this session.

        A federated view will include files in directories which are
        children of this directory.



        """
        pass

    def use_isolated_directory_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this diretory only.



        """
        pass

    def register_for_new_files(self):
        """Register for notifications of new files.

        ``FileReceiver.newFile()`` is invoked when a new ``File`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_files(self):
        """Registers for notification of updated files.

        ``FileReceiver.changedFile()`` is invoked when a file is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass

    def register_for_deleted_files(self):
        """Registers for notification of deleted files.

        ``FileReceiver.deletedFile()`` is invoked when a file is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass


class FileSmartDirectorySession(osid_sessions.OsidSession):
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``FileQuery`` can be retrieved from this session and mapped to
    this ``Directory`` to create a virtual collection of files. The
    files may be sequenced using the ``FileSearchOrder`` from this
    session.

    This ``Directory`` has a default query that matches any file and a
    default search order that specifies no sequencing. The queries may
    be examined using a ``FileQueryInspector``. The query may be
    modified by converting the inspector back to a ``FileQuery``.

    """
    def get_directory_id(self):
        """Gets the absolute path of this directory.

        :return: the ``Id`` of this directory
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    directory_id = property(fget=get_directory_id)

    def get_directory(self):
        """Gets the ``Directory`` associated with this session.

        :return: the ``Directory`` associated with this session
        :rtype: ``osid.filing.Directory``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.filing.Directory

    directory = property(fget=get_directory)

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
        return # boolean

    def get_file_query(self):
        """Gets a file query.

        :return: the file query
        :rtype: ``osid.filing.FileQuery``

        """
        return # osid.filing.FileQuery

    file_query = property(fget=get_file_query)

    def get_file_search_order(self):
        """Gets a file search order.

        The ``FileSearchOrder`` is supplied to a ``FileSearch`` to
        specify the ordering of results.

        :return: the file search order
        :rtype: ``osid.filing.FileSearchOrder``

        """
        return # osid.filing.FileSearchOrder

    file_search_order = property(fget=get_file_search_order)

    def apply_file_query(self, file_query):
        """Applies a file query to this directory.

        :param file_query: the file query
        :type file_query: ``osid.filing.FileQuery``
        :raise: ``NullArgument`` -- ``file_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``file_query`` not of this service

        """
        pass

    def inspect_file_query(self):
        """Gets a file query inspector for this directory.

        :return: the file query inspector
        :rtype: ``osid.filing.FileQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        return # osid.filing.FileQueryInspector

    def apply_file_sequencing(self, file_search_order):
        """Applies a file search order to this directory.

        :param file_search_order: the file search order
        :type file_search_order: ``osid.filing.FileSearchOrder``
        :raise: ``NullArgument`` -- ``file_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``file_search_order`` not of this service

        """
        pass

    def get_file_query_from_inspector(self, file_query_inspector):
        """Gets a file query from an inspector.

        :param file_query_inspector: a file query inspector
        :type file_query_inspector: ``osid.filing.FileQueryInspector``
        :return: the file query
        :rtype: ``osid.filing.FileQuery``
        :raise: ``NullArgument`` -- ``file_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``file_query_inspector`` is not of this service

        """
        return # osid.filing.FileQuery


class DirectoryLookupSession(osid_sessions.OsidSession):
    """This session defines methods for looking up directories in the current directory."""
    def get_directory_id(self):
        """Gets the ``Id`` of this directory.

        :return: the ``Id`` of this directory
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    directory_id = property(fget=get_directory_id)

    def get_directory(self):
        """Gets the directory associated with this session.

        :return: the directory associated with this session
        :rtype: ``osid.filing.Directory``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.filing.Directory

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
        return # boolean

    def use_comparative_directory_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_directory_view(self):
        """A complete view of the directory returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def use_federated_directory_view(self):
        """Federates the view for methods in this session.

        A federated view will include entries in directories which are
        children of this directory.



        """
        pass

    def use_isolated_directory_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this directory only.



        """
        pass

    def get_directory(self, directory_id):
        """Gets a specified directory.

        In plenary mode, the exact Id is found or a NOT_FOUND results.
        Otherwise, the returned ``Directory`` may have a different
        ``Id`` than requested such as with a link.

        :param directory_id: the ``Id`` to the directory
        :type directory_id: ``osid.id.Id``
        :return: the directory
        :rtype: ``osid.filing.Directory``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.filing.Directory

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
        return # osid.filing.DirectoryList

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
        return # osid.filing.DirectoryList

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
        return # osid.filing.DirectoryList

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
        return # osid.filing.DirectoryList

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
        return # osid.filing.DirectoryList

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
        return # osid.filing.DirectoryList

    directories = property(fget=get_directories)


class DirectoryQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among ``Directory`` objects.

    The search query is constructed using the ``DirectoryQuery``.

    This session defines views that offer differing behaviors for
    searching.
    
      * federated directory view: searches include directories in
        directories of which this directory is an ancestor
      * isolated directory view: searches are restricted to diectories
        in this directory only


    """
    def get_directory_id(self):
        """Gets the ``Id`` of this directory.

        :return: the ``Id`` of this directory
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    directory_id = property(fget=get_directory_id)

    def get_directory(self):
        """Gets the directory associated with this session.

        :return: the directory associated with this session
        :rtype: ``osid.filing.Directory``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.filing.Directory

    directory = property(fget=get_directory)

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
        return # boolean

    def use_federated_directory_view(self):
        """Federates the view for methods in this session.

        A federated view will include entries in directories which are
        children of this directory.



        """
        pass

    def use_isolated_directory_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this directory only.



        """
        pass

    def get_directory_query(self):
        """Gets a directory query.

        :return: the directory query
        :rtype: ``osid.filing.DirectoryQuery``

        """
        return # osid.filing.DirectoryQuery

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
        return # osid.filing.DirectoryList


class DirectorySearchSession(DirectoryQuerySession):
    """This session provides methods for searching among ``Directory`` objects.

    The search query is constructed using the ``DirectoryQuery``.

    This session defines views that offer differing behaviors for
    searching.
    
      * federated directory view: searches include directories in
        directories of which this directory is an ancestor
      * isolated directory view: searches are restricted to diectories
        in this directory only

    
    ``get_directories_by_query()`` is the basic search method and
    returns a list of ``Directories``. A more advanced search may be
    performed with ``getDirectoriesBySearch()``. It accepts a
    ``DirectorySearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_directories_by_search()`` returns an
    ``DirectorySearchResults`` that can be used to access the resulting
    ``DirectoryList`` or be used to perform a search within the result
    set through ``DirectorySearch``.

    """
    def get_directory_search(self):
        """Gets a diectory search.

        :return: the directory search
        :rtype: ``osid.filing.DirectorySearch``

        """
        return # osid.filing.DirectorySearch

    directory_search = property(fget=get_directory_search)

    def get_directory_search_order(self):
        """Gets a directory search order.

        The ``DirectorySearchOrder`` is supplied to a
        ``DirectorySearch`` to specify the ordering of results.

        :return: the directory search order
        :rtype: ``osid.filing.DirectorySearchOrder``

        """
        return # osid.filing.DirectorySearchOrder

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
        return # osid.filing.DirectorySearchResults

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
        return # osid.filing.DirectoryQuery


class DirectoryAdminSession(osid_sessions.OsidSession):
    """This session creates and removes files and directories under the directory associated with this session."""
    def get_directory_id(self):
        """Gets the ``Id`` of this directory.

        :return: the ``Id`` of this directory
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    directory_id = property(fget=get_directory_id)

    def get_directory(self):
        """Gets the directory associated with this session.

        :return: the directory associated with this session
        :rtype: ``osid.filing.Directory``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.filing.Directory

    directory = property(fget=get_directory)

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
        return # boolean

    def overwrite(self):
        """Overwrite files if a destination pathname exists and is a file."""
        pass

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
        return # boolean

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
        return # osid.filing.FileForm

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
        return # osid.filing.File

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
        return # osid.filing.FileForm

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
        pass

    def delete_file(self, file_id):
        """Deletes a file.

        :param file_id: the ``Id`` of the file to delete
        :type file_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``file_id`` is not found
        :raise: ``NullArgument`` -- ``file_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        return # boolean

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
        return # osid.filing.DirectoryForm

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
        return # osid.filing.Directory

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
        return # osid.filing.DirectoryForm

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
        pass

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
        pass

    def clear_directory(self, directory_id):
        """Deletes all files and subdirectories within the given directory.

        :param directory_id: the ``Id`` of the directory to delete
        :type directory_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``directory_id`` is not found
        :raise: ``NullArgument`` -- ``directory_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class DirectoryNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``Directories``.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    Two view are defined in this session:
    
    federated view: includes notifications of directories located in
    descendants of this directory
    
    isolated view: includes notifcations of directories in this
    directory only

    """
    def get_directory_id(self):
        """Gets the ``Id`` of this directory.

        :return: the ``Id`` of this directory
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    directory_id = property(fget=get_directory_id)

    def get_directory(self):
        """Gets the ``Directory`` associated with this session.

        :return: the ``Directory`` associated with this session
        :rtype: ``osid.filing.Directory``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.filing.Directory

    directory = property(fget=get_directory)

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
        return # boolean

    def use_federated_directory_view(self):
        """Federates the view for methods in this session.

        A federated view will include directories in directories which
        are children of this directory.



        """
        pass

    def use_isolated_directory_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this diretory only.



        """
        pass

    def register_for_new_directories(self):
        """Register for notifications of new directories.

        ``DirectoryReceiver.newDirectory()`` is invoked when a new
        ``Directory`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_directories(self):
        """Registers for notification of updated directories.

        ``DirectoryReceiver.changedDirectory()`` is invoked when a file
        is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass

    def register_for_deleted_directories(self):
        """Registers for notification of deleted directories.

        ``DirectoryReceiver.deletedDirectory()`` is invoked when a
        directory is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass


