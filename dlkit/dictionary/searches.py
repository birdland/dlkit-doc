from ..osid import searches as osid_searches


class EntrySearch(osid_searches.OsidSearch):
    """This interface specifies options for governing entry searches."""
    def search_among_entries(self, entry_ids):
        """Execute this search among the given list of entries.

        :param entry_ids: list of entry ``Ids``
        :type entry_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``entry_ids`` is ``null``

        """
        pass

    def order_entry_results(self, entry_search_order):
        """Specify an ordering to the search results.

        :param entry_search_order: entry searcgh order
        :type entry_search_order: ``osid.dictionary.EntrySearchOrder``
        :raise: ``NullArgument`` -- ``entry_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``entry_search_order`` is not of this service

        """
        pass

    def get_entry_search_record(self, entry_search_record_type):
        """Gets the entry search record corresponding to the given entry search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param entry_search_record_type: an entry search record type
        :type entry_search_record_type: ``osid.type.Type``
        :return: the entry search record
        :rtype: ``osid.dictionary.records.EntrySearchRecord``
        :raise: ``NullArgument`` -- ``entry_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(entry_search_record_type)`` is ``false``

        """
        return # osid.dictionary.records.EntrySearchRecord


class EntrySearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_entries(self):
        """Gets the entry list resulting from the search.

        :return: the entry list
        :rtype: ``osid.dictionary.EntryList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.dictionary.EntryList

    entries = property(fget=get_entries)

    def get_entry_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the entry query inspector
        :rtype: ``osid.dictionary.EntryQueryInspector``

        """
        return # osid.dictionary.EntryQueryInspector

    entry_query_inspector = property(fget=get_entry_query_inspector)

    def get_entry_search_results_record(self, entry_search_record_type):
        """Gets the entry search results record corresponding to the given entry search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record interface.

        :param entry_search_record_type: an entry search record type
        :type entry_search_record_type: ``osid.type.Type``
        :return: the entry search results record
        :rtype: ``osid.dictionary.records.EntrySearchResultsRecord``
        :raise: ``NullArgument`` -- ``entry_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(entry_search_record_type)`` is ``false``

        """
        return # osid.dictionary.records.EntrySearchResultsRecord


class DictionarySearch(osid_searches.OsidSearch):
    """This interface defines search options."""
    def search_among_dictionaries(self, dictionary_ids):
        """Execute this search among the given list of dictionaries.

        :param dictionary_ids: list of dictionaries
        :type dictionary_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``dictionary_ids`` is ``null``

        """
        pass

    def order_dictionary_results(self, dictionary_search_order):
        """Specify an ordering to the search results.

        :param dictionary_search_order: dictionary search order
        :type dictionary_search_order: ``osid.dictionary.DictionarySearchOrder``
        :raise: ``NullArgument`` -- ``dictionary_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``dictionary_search_order`` is not of this service

        """
        pass

    def get_dictionary_search_record(self, dictionary_search_record_type):
        """Gets the dictionary search record corresponding to the given dictionary search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record interface.

        :param dictionary_search_record_type: a dictionary search record type
        :type dictionary_search_record_type: ``osid.type.Type``
        :return: the dictionary search record
        :rtype: ``osid.dictionary.records.DictionarySearchRecord``
        :raise: ``NullArgument`` -- ``dictionary_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(dictionary_search_record_type)`` is ``false``

        """
        return # osid.dictionary.records.DictionarySearchRecord


class DictionarySearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_dictionaries(self):
        """Gets the dictionary list resulting from the search.

        :return: the dictionary list
        :rtype: ``osid.dictionary.DictionaryList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.dictionary.DictionaryList

    dictionaries = property(fget=get_dictionaries)

    def get_dictionary_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the dictionary query inspector
        :rtype: ``osid.dictionary.DictionaryQueryInspector``

        """
        return # osid.dictionary.DictionaryQueryInspector

    dictionary_query_inspector = property(fget=get_dictionary_query_inspector)

    def get_dictionary_search_results_record(self, dictionary_search_record_type):
        """Gets the dictionary search results record corresponding to the given dictionary search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param dictionary_search_record_type: a dictionary search record type
        :type dictionary_search_record_type: ``osid.type.Type``
        :return: the dictionary search results record
        :rtype: ``osid.dictionary.records.DictionarySearchResultsRecord``
        :raise: ``NullArgument`` -- ``dictionary_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(dictionary_search_record_type)`` is ``false``

        """
        return # osid.dictionary.records.DictionarySearchResultsRecord


