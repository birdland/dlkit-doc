from ..osid import search_orders as osid_search_orders


class EntrySearchOrder(osid_search_orders.OsidObjectSearchOrder):
    """This interface specifies options for ordering search results."""
    def order_by_key_type(self, style):
        """Specifies a preference for ordering the results by key type.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_key(self, style):
        """Specifies a preference for ordering the results by key.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_value_type(self, style):
        """Specifies a preference for ordering the results by value type.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_value(self, style):
        """Specifies a preference for ordering the results by value.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def get_entry_search_order_record(self, entry_record_type):
        """Gets the entry search order record corresponding to the given entry record ``Type``.

        Multiple retrievals return the same underlying object.

        :param entry_record_type: an entry record type
        :type entry_record_type: ``osid.type.Type``
        :return: the entry search order record
        :rtype: ``osid.dictionary.records.EntrySearchOrderRecord``
        :raise: ``NullArgument`` -- ``entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(entry_record_type)`` is ``false``

        """
        return # osid.dictionary.records.EntrySearchOrderRecord


class DictionarySearchOrder(osid_search_orders.OsidCatalogSearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_dictionary_search_order_record(self, dictionary_record_type):
        """Gets the dictionary search order record corresponding to the given dictionary record ``Type``.

        Multiple retrievals return the same underlying object.

        :param dictionary_record_type: a dictionary record type
        :type dictionary_record_type: ``osid.type.Type``
        :return: the dictionary search order record
        :rtype: ``osid.dictionary.records.DictionarySearchOrderRecord``
        :raise: ``NullArgument`` -- ``dictionary_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(dictionary_record_type)`` is ``false``

        """
        return # osid.dictionary.records.DictionarySearchOrderRecord


