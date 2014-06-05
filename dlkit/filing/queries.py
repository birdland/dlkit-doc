from ..osid import queries as osid_queries


class DirectoryEntryQuery(osid_queries.OsidObjectQuery):
    """``DirectoryEntryQuery`` defines methods in common to both ``FileQuery`` and ``DirectoryQuery``."""
    def match_name(self, name, string_match_type, match):
        """Matches entry names.

        Supplying multiple strings behaves like a boolean ``AND`` among
        the elements each which must correspond to the
        ``stringMatchType``. An ``OR`` can be performed with multiple
        queries.

        :param name: name to match
        :type name: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``name`` not of ``string_match_type``
        :raise: ``NullArgument`` -- ``name`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        """
        pass

    def clear_name_terms(self):
        """Clears the name terms."""
        pass

    name_terms = property(fdel=clear_name_terms)

    def match_path(self, path, string_match_type, match):
        """Matches an absolute pathname of a directory entry.

        Supplying multiple strings behaves like a boolean ``AND`` among
        the elements each which must correspond to the
        ``stringMatchType``. An ``OR`` can be performed with multiple
        queries.

        :param path: path to match
        :type path: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``name`` not of ``string_match_type``
        :raise: ``NullArgument`` -- ``path`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        """
        pass

    def clear_path_terms(self):
        """Clears the path terms."""
        pass

    path_terms = property(fdel=clear_path_terms)

    def supports_directory_query(self):
        """Tests if a ``DirectoryQuery`` is available.

        :return: ``true`` if a directory query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_directory_query(self):
        """Gets the query for a directory to match the parent directory.

        There is only one ``DirectoryQuery`` per
        ``DifrectoryEntryQuery``. Multiple retrievals return the same
        object.

        :return: the directory query
        :rtype: ``osid.filing.DirectoryQuery``
        :raise: ``Unimplemented`` -- ``supports_directory_query()`` is ``false``

        """
        return # osid.filing.DirectoryQuery

    directory_query = property(fget=get_directory_query)

    def clear_directory_terms(self):
        """Clears the directory terms."""
        pass

    directory_terms = property(fdel=clear_directory_terms)

    def match_aliases(self, match):
        """Matches aliases only.

        :param match: ``true`` to match aliases, ``false`` to match target files
        :type match: ``boolean``

        """
        pass

    def match_any_aliases(self, match):
        """Matches a file that has any aliases.

        :param match: ``true`` to match any alias, ``false`` to match objects with no aliases
        :type match: ``boolean``

        """
        pass

    def clear_aliases_terms(self):
        """Clears the aliases terms."""
        pass

    aliases_terms = property(fdel=clear_aliases_terms)

    def match_owner_id(self, agent_id, match):
        """Matches files whose entries are owned by the given agent id.

        :param agent_id: the agent ``Id``
        :type agent_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        """
        pass

    def clear_owner_id_terms(self):
        """Clears the owner ``Id`` terms."""
        pass

    owner_id_terms = property(fdel=clear_owner_id_terms)

    def supports_owner_query(self):
        """Tests if an ``AgentQuery`` is available for querying agents.

        :return: ``true`` if an agent query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_owner_query(self):
        """Gets the query for an agent.

        :return: the agent query
        :rtype: ``osid.authentication.AgentQuery``
        :raise: ``Unimplemented`` -- ``supports_agent_query()`` is ``false``

        """
        return # osid.authentication.AgentQuery

    owner_query = property(fget=get_owner_query)

    def clear_owner_terms(self):
        """Clears the owner terms."""
        pass

    owner_terms = property(fdel=clear_owner_terms)

    def match_created_time(self, start, end, match):
        """Match directory entries that are created between the specified time period inclusive.

        :param start: start time of the query
        :type start: ``osid.calendaring.DateTime``
        :param end: end time of the query
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is les than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``

        """
        pass

    def clear_created_time_terms(self):
        """Clears the created time terms."""
        pass

    created_time_terms = property(fdel=clear_created_time_terms)

    def match_modified_time(self, start, end, match):
        """Match directory entries that are modified between the specified time period inclusive.

        :param start: start time of the query
        :type start: ``osid.calendaring.DateTime``
        :param end: end time of the query
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is les than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``

        """
        pass

    def clear_modified_time_terms(self):
        """Clears the modified time terms."""
        pass

    modified_time_terms = property(fdel=clear_modified_time_terms)

    def match_last_access_time(self, start, end, match):
        """Match directory entries that were last accessed between the specified time period.

        :param start: start time of the query
        :type start: ``osid.calendaring.DateTime``
        :param end: end time of the query
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is les than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``

        """
        pass

    def clear_last_access_time_terms(self):
        """Clears the last access time terms."""
        pass

    last_access_time_terms = property(fdel=clear_last_access_time_terms)


class FileQuery(DirectoryEntryQuery):
    """This is the query for searching files.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produces a nested ``OR``.

    """
    def match_size(self, from_, to, match):
        """Matches files whose size is within and including the given range.

        :param from: low file size
        :type from: ``cardinal``
        :param to: high file size
        :type to: ``cardinal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``to`` is les than ``from``

        """
        pass

    def match_any_size(self, match):
        """Matches a file that has any known size.

        :param match: ``true`` to match any size, ``false`` to match files with no known size
        :type match: ``boolean``

        """
        pass

    def clear_size_terms(self):
        """Clears all file size terms."""
        pass

    size_terms = property(fdel=clear_size_terms)

    def match_data_string(self, data, string_match_type, match):
        """Adds data strings to this query to match files whose content contains these strings.

        Supplying multiple strings behaves like a boolean AND among the
        elements each which must correspond to the ``stringMatchType``.
        An OR can be performed with multiple queries.

        :param data: string to match
        :type data: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``data`` not of ``string_match_type``
        :raise: ``NullArgument`` -- ``data`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        """
        pass

    def clear_data_string_terms(self):
        """Clears all file data string terms."""
        pass

    data_string_terms = property(fdel=clear_data_string_terms)

    def match_data(self, data, match, partial):
        """Matches files who data contains the given bytes.

        :param data: data to match
        :type data: ``byte[]``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :param partial: ``true`` for a partial match, ``false`` for a complete match
        :type partial: ``boolean``
        :raise: ``NullArgument`` -- ``data`` is ``null``

        """
        pass

    def match_any_data(self, match):
        """Matches a file that has any data.

        :param match: ``true`` to match any data, ``false`` to match files with no data
        :type match: ``boolean``

        """
        pass

    def clear_data_terms(self):
        """Clears all file data terms."""
        pass

    data_terms = property(fdel=clear_data_terms)

    def get_file_query_record(self, file_record_type):
        """Gets the file query record corresponding to the given ``File`` record ``Type``.

        Multiple record retrievals produce a nested boolean ``OR`` term.

        :param file_record_type: a file record type
        :type file_record_type: ``osid.type.Type``
        :return: the file query record
        :rtype: ``osid.filing.records.FileQueryRecord``
        :raise: ``NullArgument`` -- ``file_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(file_record_type)`` is ``false``

        """
        return # osid.filing.records.FileQueryRecord


class DirectoryQuery(osid_queries.OsidCatalogQuery, DirectoryEntryQuery):
    """This is the query for searching directories.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    An example to find directories whose name is "Library".
      DirectoryQuery query = session.getDirectoryQuery();
      query.matchName("Library", wordStringMatchType, true);
      
      DirectoryList list = session.getDirectoriesByQuery(query);
    


    """
    def match_file_name(self, name, string_match_type, match):
        """Matches directories that contain the specified file name.

        :param name: a file name
        :type name: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``name`` not of ``string_match_type``
        :raise: ``NullArgument`` -- ``name`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        """
        pass

    def clear_file_name_terms(self):
        """Clears all file name terms."""
        pass

    file_name_terms = property(fdel=clear_file_name_terms)

    def supports_file_query(self):
        """Tests if a ``FileQuery`` is available.

        :return: ``true`` if a file query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_file_query(self, match):
        """Gets the query for a file contained within the directory.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :return: the directory query
        :rtype: ``osid.filing.FileQuery``
        :raise: ``Unimplemented`` -- ``supports_file_query()`` is ``false``

        """
        return # osid.filing.FileQuery

    def match_any_file(self, match):
        """Matches directories with any file.

        :param match: ``true`` to match directories with any file,, ``false`` to match directories with no file.
        :type match: ``boolean``

        """
        pass

    def clear_file_terms(self):
        """Clears all file terms."""
        pass

    file_terms = property(fdel=clear_file_terms)

    def get_directory_query_record(self, directory_record_type):
        """Gets the directory query record corresponding to the given ``Directory`` record ``Type``.

        Multiple record retrievals produce a nested boolean ``OR`` term.

        :param directory_record_type: a directory record type
        :type directory_record_type: ``osid.type.Type``
        :return: the directory query record
        :rtype: ``osid.filing.records.DirectoryQueryRecord``
        :raise: ``NullArgument`` -- ``directory_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(directory_record_type)`` is ``false``

        """
        return # osid.filing.records.DirectoryQueryRecord


