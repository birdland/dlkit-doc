from ..osid import query_inspectors as osid_query_inspectors


class DirectoryEntryQueryInspector(osid_query_inspectors.OsidObjectQueryInspector):
    """``DirectoryEntryQueryInspector`` defines methods in common to both ``FileQueryInspector`` and ``DirectoryQueryInspector``."""
    def get_name_terms(self):
        """Gets the name query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.StringTerm``

        """
        return # osid.search.terms.StringTerm

    name_terms = property(fget=get_name_terms)

    def get_path_terms(self):
        """Gets the path query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.StringTerm``

        """
        return # osid.search.terms.StringTerm

    path_terms = property(fget=get_path_terms)

    def get_directory_terms(self):
        """Gets the directory query terms.

        :return: the query terms
        :rtype: ``osid.filing.DirectoryQueryInspector``

        """
        return # osid.filing.DirectoryQueryInspector

    directory_terms = property(fget=get_directory_terms)

    def get_aliases_terms(self):
        """Gets the aliases query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``

        """
        return # osid.search.terms.BooleanTerm

    aliases_terms = property(fget=get_aliases_terms)

    def get_owner_id_terms(self):
        """Gets the owner ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    owner_id_terms = property(fget=get_owner_id_terms)

    def get_owner_terms(self):
        """Gets the owner query terms.

        :return: the query terms
        :rtype: ``osid.authentication.AgentQueryInspector``

        """
        return # osid.authentication.AgentQueryInspector

    owner_terms = property(fget=get_owner_terms)

    def get_created_time_terms(self):
        """Gets the created time query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``

        """
        return # osid.search.terms.DateTimeRangeTerm

    created_time_terms = property(fget=get_created_time_terms)

    def get_modified_time_terms(self):
        """Gets the modified time query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``

        """
        return # osid.search.terms.DateTimeRangeTerm

    modified_time_terms = property(fget=get_modified_time_terms)

    def get_last_access_time_terms(self):
        """Gets the last access time query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``

        """
        return # osid.search.terms.DateTimeRangeTerm

    last_access_time_terms = property(fget=get_last_access_time_terms)


class FileQueryInspector(DirectoryEntryQueryInspector):
    """This is the query inspector for examining file queries."""
    def get_size_terms(self):
        """Gets the size query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.CardinalRangeTerm``

        """
        return # osid.search.terms.CardinalRangeTerm

    size_terms = property(fget=get_size_terms)

    def get_data_string_terms(self):
        """Gets the data string query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.StringTerm``

        """
        return # osid.search.terms.StringTerm

    data_string_terms = property(fget=get_data_string_terms)

    def get_data_terms(self):
        """Gets the data query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BytesTerm``

        """
        return # osid.search.terms.BytesTerm

    data_terms = property(fget=get_data_terms)

    def get_file_query_inspector_record(self, file_record_type):
        """Gets the file query inspector record corresponding to the given ``File`` record ``Type``.

        :param file_record_type: a file record type
        :type file_record_type: ``osid.type.Type``
        :return: the file query inspector record
        :rtype: ``osid.filing.records.FileQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``file_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(file_record_type)`` is ``false``

        """
        return # osid.filing.records.FileQueryInspectorRecord


class DirectoryQueryInspector(osid_query_inspectors.OsidCatalogQueryInspector, DirectoryEntryQueryInspector):
    """This is the query inspector for examining directory queries."""
    def get_file_name_terms(self):
        """Gets the file name query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.StringTerm``

        """
        return # osid.search.terms.StringTerm

    file_name_terms = property(fget=get_file_name_terms)

    def get_file_terms(self):
        """Gets the file query terms.

        :return: the query terms
        :rtype: ``osid.filing.FileQueryInspector``

        """
        return # osid.filing.FileQueryInspector

    file_terms = property(fget=get_file_terms)

    def get_directory_query_inspector_record(self, directory_record_type):
        """Gets the directory query inspector record corresponding to the given ``Directory`` record ``Type``.

        :param directory_record_type: a directory record type
        :type directory_record_type: ``osid.type.Type``
        :return: the directory query inspector record
        :rtype: ``osid.filing.records.DirectoryQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``directory_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(directory_record_type)`` is ``false``

        """
        return # osid.filing.records.DirectoryQueryInspectorRecord


