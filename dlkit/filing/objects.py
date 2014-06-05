from ..osid import objects as osid_objects


class DirectoryEntry(osid_objects.OsidObject):
    """``DirectoryEntry`` defines methods in common to both ``File`` and ``Directory``.

    The concatenated path and name are assumed to be unique.

    """
    def get_name(self):
        """Gets the name of this entry.

        The name does not include the path. If this entry represents an
        alias, the name of the alias is returned.

        :return: the entry name
        :rtype: ``string``

        """
        return # string

    name = property(fget=get_name)

    def is_alias(self):
        """Tests if this entry is an alias.

        :return: ``true`` if this is an alias, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_path(self):
        """Gets the full path of this entry.

        The path includes the name. Path components are separated by a
        /. If this entry represents an alias, the path to the alias is
        returned.

        :return: the path
        :rtype: ``string``

        """
        return # string

    path = property(fget=get_path)

    def get_real_path(self):
        """Gets the real path of this entry.

        The path includes the name. Path components are separated by a
        /. If this entry represents an alias, the full path to the
        target file or directory is returned.

        :return: the path
        :rtype: ``string``

        """
        return # string

    real_path = property(fget=get_real_path)

    def get_owner_id(self):
        """Gets the ``Id`` of the ``Agent`` that owns this entry.

        :return: the ``Agent Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    owner_id = property(fget=get_owner_id)

    def get_owner(self):
        """Gets the ``Agent`` that owns this entry.

        :return: the ``Agent``
        :rtype: ``osid.authentication.Agent``
        :raise: ``OperationFailed`` -- authentication service not available

        """
        return # osid.authentication.Agent

    owner = property(fget=get_owner)

    def get_created_time(self):
        """Gets the created time of this entry.

        :return: the created time
        :rtype: ``osid.calendaring.DateTime``

        """
        return # osid.calendaring.DateTime

    created_time = property(fget=get_created_time)

    def get_last_modified_time(self):
        """Gets the last modified time of this entry.

        :return: the last modified time
        :rtype: ``osid.calendaring.DateTime``

        """
        return # osid.calendaring.DateTime

    last_modified_time = property(fget=get_last_modified_time)

    def get_last_access_time(self):
        """Gets the last access time of this entry.

        :return: the last access time
        :rtype: ``osid.calendaring.DateTime``

        """
        return # osid.calendaring.DateTime

    last_access_time = property(fget=get_last_access_time)


class DirectoryEntryForm(osid_objects.OsidObjectForm):
    """``DirectoryEntryForm`` defines methods in common to both ``FileForm`` and ``DirectoryForm``."""
    def get_owner_metadata(self):
        """Gets the metadata for the owner.

        :return: metadata for the owner
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    owner_metadata = property(fget=get_owner_metadata)

    def set_owner(self, agent_id):
        """Sets the owner.

        :param agent_id: the new owner
        :type agent_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``agent_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        """
        pass

    def clear_owner(self):
        """Clears the owner.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    owner = property(fget=set_owner, fdel=clear_owner)


class File(DirectoryEntry):
    """``File`` represents a file in a file system."""
    def has_size(self):
        """Tests if this file has a known size.

        :return: ``true`` if this file has a size, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_size(self):
        """Gets the size of this file in bytes if ``has_size()`` is ``true``.

        :return: the size of this file
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- ``has_size()`` is ``false``

        """
        return # cardinal

    size = property(fget=get_size)

    def get_file_record(self, file_record_type):
        """Gets the file record corresponding to the given ``File`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``file_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(file_record_type)``
        is ``true`` .

        :param file_record_type: the file record type
        :type file_record_type: ``osid.type.Type``
        :return: the file record
        :rtype: ``osid.filing.records.FileRecord``
        :raise: ``NullArgument`` -- ``file_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(file_record_type)`` is ``false``

        """
        return # osid.filing.records.FileRecord


class FileForm(DirectoryEntryForm):
    """This is the form for creating and updating ``Files``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``FileAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_file_form_record(self, file_record_type):
        """Gets the ``FileFormRecord`` corresponding to the given file record ``Type``.

        :param file_record_type: the file record type
        :type file_record_type: ``osid.type.Type``
        :return: the file form record
        :rtype: ``osid.filing.records.FileFormRecord``
        :raise: ``NullArgument`` -- ``file_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(file_record_type)`` is ``false``

        """
        return # osid.filing.records.FileFormRecord


class FileList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``FileList`` provides a means for accessing ``File`` elements sequentially either one at a time or many at a time.

    Examples: while (fl.hasNext()) { File file = fl.getNextFile(); }

    or
      while (fl.hasNext()) {
           File[] files = fl.getNextFiles(fl.available());
      }
    


    """
    def get_next_file(self):
        """Gets the next ``File`` in this list.

        :return: the next ``File`` in this list. The ``has_next()`` method should be used to test that a next ``File`` is available before calling this method.
        :rtype: ``osid.filing.File``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.filing.File

    next_file = property(fget=get_next_file)

    def get_next_files(self, n):
        """Gets the next set of ``File`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``File`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``File`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.filing.File``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.filing.File


class Directory(osid_objects.OsidCatalog, DirectoryEntry):
    """``Directory`` represents a directory in a file system that may contain other files and directories."""
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
        return # osid.filing.records.DirectoryRecord


class DirectoryForm(osid_objects.OsidCatalogForm, DirectoryEntryForm):
    """This is the form for creating and updating ``Directory`` objects.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``DirectoryAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_directory_form_record(self, directory_record_type):
        """Gets the ``DirectoryFormRecord`` corresponding to the given directory record ``Type``.

        :param directory_record_type: the directory record type
        :type directory_record_type: ``osid.type.Type``
        :return: the directory form record
        :rtype: ``osid.filing.records.DirectoryFormRecord``
        :raise: ``NullArgument`` -- ``directory_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(directory_record_type)`` is ``false``

        """
        return # osid.filing.records.DirectoryFormRecord


class DirectoryList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``DirectoryList`` provides a means for accessing ``Directory`` elements sequentially either one at a time or many at a time.

    Examples: while (dl.hasNext()) { Directory directory =
    dl.getNextDirectory(); }

    or
      while (dl.hasNext()) {
           Directory[] directories = dl.getNextDirectories(dl.available());
      }
    


    """
    def get_next_directory(self):
        """Gets the next ``Directory`` in this list.

        :return: the next ``Directory`` in this list. The ``has_next()`` method should be used to test that a next ``Dircectory`` is available before calling this method.
        :rtype: ``osid.filing.Directory``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.filing.Directory

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
        return # osid.filing.Directory


