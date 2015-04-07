from ..osid import queries as osid_queries


class EntryQuery(osid_queries.OsidObjectQuery):
    """This is the query for searching dictionary entries.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def match_key_type(self, key_type, match):
        """Sets the ``Type`` for querying keys of a given type.

        :param key_type: the key ``Type``
        :type key_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``key_type`` is ``null``

        """
        pass

    def clear_key_type_terms(self):
        """Clears the key type terms."""
        pass

    key_type_terms = property(fdel=clear_key_type_terms)

    def match_key(self, key, key_type, match):
        """Matches entries of this key.

        :param key: the key
        :type key: ``object``
        :param key_type: the key ``Type``
        :type key_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``key`` or ``key_type`` is ``null``

        """
        pass

    def clear_key_terms(self):
        """Clears the key terms."""
        pass

    key_terms = property(fdel=clear_key_terms)

    def match_value_type(self, value_type, match):
        """Sets the ``Type`` of this entry value.

        :param value_type: the value ``Type``
        :type value_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``value_type`` is ``null``

        """
        pass

    def clear_value_type_terms(self):
        """Clears the value type terms."""
        pass

    value_type_terms = property(fdel=clear_value_type_terms)

    def match_value(self, value, value_type, match):
        """Sets the value in this entry.

        :param value: the value
        :type value: ``object``
        :param value_type: the value ``Type``
        :type value_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``value`` or ``value_type`` is ``null``

        """
        pass

    def clear_value_terms(self):
        """Clears the value terms."""
        pass

    value_terms = property(fdel=clear_value_terms)

    def match_dictionary_id(self, dictionary_id, match):
        """Sets the dictionary ``Id`` for this query.

        :param dictionary_id: a dictionary ``Id``
        :type dictionary_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``

        """
        pass

    def clear_dictionary_id_terms(self):
        """Clears the dictionary ``Id`` terms."""
        pass

    dictionary_id_terms = property(fdel=clear_dictionary_id_terms)

    def supports_dictionary_query(self):
        """Tests if a ``DictionaryQuery`` is available.

        :return: ``true`` if a dictionary query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_dictionary_query(self):
        """Gets the query for a dictionary.

        Multiple retrievals produce a nested boolean ``OR`` term.

        :return: the dictionary query
        :rtype: ``osid.dictionary.DictionaryQuery``
        :raise: ``Unimplemented`` -- ``supports_dictionary_query()`` is ``false``

        """
        return # osid.dictionary.DictionaryQuery

    dictionary_query = property(fget=get_dictionary_query)

    def clear_dictionary_terms(self):
        """Clears the dictionary terms."""
        pass

    dictionary_terms = property(fdel=clear_dictionary_terms)

    def get_entry_query_record(self, entry_record_type):
        """Gets the entry query record corresponding to the given ``Dictionary`` record ``Type``.

        Multiple retrievale produce a nested boolean ``OR`` term.

        :param entry_record_type: an entry record type
        :type entry_record_type: ``osid.type.Type``
        :return: the entry query record
        :rtype: ``osid.dictionary.records.EntryQueryRecord``
        :raise: ``NullArgument`` -- ``entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(entry_record_type)`` is ``false``

        """
        return # osid.dictionary.records.EntryQueryRecord


class DictionaryQuery(osid_queries.OsidCatalogQuery):
    """This is the query for searching dictionaries.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def match_entry_id(self, entry_id, match):
        """Sets the entry ``Id``.

        :param entry_id: an entry ``Id``
        :type entry_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``entry_id`` is ``null``

        """
        pass

    def clear_entry_id_terms(self):
        """Clears the entry ``Id`` terms."""
        pass

    entry_id_terms = property(fdel=clear_entry_id_terms)

    def supports_entry_query(self):
        """Tests if an ``EntryQuery`` is available.

        :return: ``true`` if an entry query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_entry_query(self):
        """Gets the query for an entry.

        Multiple retrievale produce a nested boolean ``OR`` term.

        :return: the entry query
        :rtype: ``osid.dictionary.EntryQuery``
        :raise: ``Unimplemented`` -- ``supports_entry_query()`` is ``false``

        """
        return # osid.dictionary.EntryQuery

    entry_query = property(fget=get_entry_query)

    def match_any_entry(self, match):
        """Matches dictionaries with any entry.

        :param match: ``true`` to match dictionaries with any entry, ``false`` to match dictionaries with no entry
        :type match: ``boolean``

        """
        pass

    def clear_entry_terms(self):
        """Clears the entry terms."""
        pass

    entry_terms = property(fdel=clear_entry_terms)

    def match_ancestor_dictionary_id(self, dictionary_id, match):
        """Sets the dictionary ``Id`` for to match dictionaries in which the specified dictionary is an acestor.

        :param dictionary_id: a dictionary ``Id``
        :type dictionary_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``

        """
        pass

    def clear_ancestor_dictionary_id_terms(self):
        """Clears the ancestor dictionary ``Id`` terms."""
        pass

    ancestor_dictionary_id_terms = property(fdel=clear_ancestor_dictionary_id_terms)

    def supports_ancestor_dictionary_query(self):
        """Tests if a ``DictionaryQuery`` is available.

        :return: ``true`` if a dictionary query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_ancestor_dictionary_query(self):
        """Gets the query for an ancestor dictionary.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the dictionary query
        :rtype: ``osid.dictionary.DictionaryQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_dictionary_query()`` is ``false``

        """
        return # osid.dictionary.DictionaryQuery

    ancestor_dictionary_query = property(fget=get_ancestor_dictionary_query)

    def match_any_ancestor_dictionary(self, match):
        """Matches a dictionary that has any ancestor.

        :param match: ``true`` to match dictionaries with any ancestor dictionaries, ``false`` to match root dictionaries
        :type match: ``boolean``

        """
        pass

    def clear_ancestor_dictionary_terms(self):
        """Clears the ancestor dictionary terms."""
        pass

    ancestor_dictionary_terms = property(fdel=clear_ancestor_dictionary_terms)

    def match_descendant_dictionary_id(self, dictionary_id, match):
        """Sets the dictionary ``Id`` for to match dictionaries in which the specified dictionary is a descendant.

        :param dictionary_id: a dictionary ``Id``
        :type dictionary_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``

        """
        pass

    def clear_descendant_dictionary_id_terms(self):
        """Clears the dictionary ``Id`` terms."""
        pass

    descendant_dictionary_id_terms = property(fdel=clear_descendant_dictionary_id_terms)

    def supports_descendant_dictionary_query(self):
        """Tests if a ``DictionaryQuery`` is available.

        :return: ``true`` if a dictionary query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_descendant_dictionary_query(self):
        """Gets the query for a descendant dictioonary.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the dictionary query
        :rtype: ``osid.dictionary.DictionaryQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_dictionary_query()`` is ``false``

        """
        return # osid.dictionary.DictionaryQuery

    descendant_dictionary_query = property(fget=get_descendant_dictionary_query)

    def match_any_descendant_dictionary(self, match):
        """Matches a dictionary that has any descendant.

        :param match: ``true`` to match dictionaries with any descendant dictionaries, ``false`` to match leaf dictionaries
        :type match: ``boolean``

        """
        pass

    def clear_descendant_dictionary_terms(self):
        """Clears the dictionary terms."""
        pass

    descendant_dictionary_terms = property(fdel=clear_descendant_dictionary_terms)

    def get_dictionary_query_record(self, dictionary_record_type):
        """Gets the dictionary query record corresponding to the given ``Dictionary`` record ``Type``.

        Multiple retrievale produce a nested boolean ``OR`` term.

        :param dictionary_record_type: a dictionary record type
        :type dictionary_record_type: ``osid.type.Type``
        :return: the dictionary query record
        :rtype: ``osid.dictionary.records.DictionaryQueryRecord``
        :raise: ``NullArgument`` -- ``dictionary_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(dictionary_record_type)`` is ``false``

        """
        return # osid.dictionary.records.DictionaryQueryRecord


