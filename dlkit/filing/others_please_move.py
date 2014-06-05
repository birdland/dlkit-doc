from ..filing import objects as filing_objects
from ..filing import queries as filing_queries
from ..filing import query_inspectors as filing_query_inspectors
from ..filing import search_orders as filing_search_orders


class File(filing_objects.DirectoryEntry):
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


class FileQuery(filing_queries.DirectoryEntryQuery):
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


class FileQueryInspector(filing_query_inspectors.DirectoryEntryQueryInspector):
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


class FileForm(filing_objects.DirectoryEntryForm):
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


class FileSearchOrder(filing_search_orders.DirectoryEntrySearchOrder):
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


