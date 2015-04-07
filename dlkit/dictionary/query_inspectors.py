from ..osid import query_inspectors as osid_query_inspectors


class EntryQueryInspector(osid_query_inspectors.OsidObjectQueryInspector):
    """This is the query inspector for examining entry queries.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def get_key_type_terms(self):
        """Gets the key type query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.TypeTerm``

        """
        return # osid.search.terms.TypeTerm

    key_type_terms = property(fget=get_key_type_terms)

    def get_key_terms(self):
        """Gets the key query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.ObjectTerm``

        """
        return # osid.search.terms.ObjectTerm

    key_terms = property(fget=get_key_terms)

    def get_value_type_terms(self):
        """Gets the value type query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.TypeTerm``

        """
        return # osid.search.terms.TypeTerm

    value_type_terms = property(fget=get_value_type_terms)

    def get_value_terms(self):
        """Gets the value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.ObjectTerm``

        """
        return # osid.search.terms.ObjectTerm

    value_terms = property(fget=get_value_terms)

    def get_dictionary_id_terms(self):
        """Gets the dictionary ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    dictionary_id_terms = property(fget=get_dictionary_id_terms)

    def get_dictionary_terms(self):
        """Gets the dictionary query terms.

        :return: the query terms
        :rtype: ``osid.dictionary.DictionaryQueryInspector``

        """
        return # osid.dictionary.DictionaryQueryInspector

    dictionary_terms = property(fget=get_dictionary_terms)

    def get_entry_query_inspector_record(self, entry_record_type):
        """Gets the entry query inspector record corresponding to the given ``Entry`` record ``Type``.

        :param entry_record_type: an entry record type
        :type entry_record_type: ``osid.type.Type``
        :return: the entry query inspector record
        :rtype: ``osid.dictionary.records.EntryQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(entry_record_type)`` is ``false``

        """
        return # osid.dictionary.records.EntryQueryInspectorRecord


class DictionaryQueryInspector(osid_query_inspectors.OsidCatalogQueryInspector):
    """This is the query inspector for examining dictionary searches."""
    def get_entry_id_terms(self):
        """Gets the entry ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    entry_id_terms = property(fget=get_entry_id_terms)

    def get_entry_terms(self):
        """Gets the entry query terms.

        :return: the query terms
        :rtype: ``osid.dictionary.EntryQueryInspector``

        """
        return # osid.dictionary.EntryQueryInspector

    entry_terms = property(fget=get_entry_terms)

    def get_ancestor_dictionary_id_terms(self):
        """Gets the ancestor dictionary ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    ancestor_dictionary_id_terms = property(fget=get_ancestor_dictionary_id_terms)

    def get_ancestor_dictionary_terms(self):
        """Gets the ancestor dictionary query terms.

        :return: the query terms
        :rtype: ``osid.dictionary.DictionaryQueryInspector``

        """
        return # osid.dictionary.DictionaryQueryInspector

    ancestor_dictionary_terms = property(fget=get_ancestor_dictionary_terms)

    def get_descendant_dictionary_id_terms(self):
        """Gets the descendant dictionary ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    descendant_dictionary_id_terms = property(fget=get_descendant_dictionary_id_terms)

    def get_descendant_dictionary_terms(self):
        """Gets the descendant dictionary query terms.

        :return: the query terms
        :rtype: ``osid.dictionary.DictionaryQueryInspector``

        """
        return # osid.dictionary.DictionaryQueryInspector

    descendant_dictionary_terms = property(fget=get_descendant_dictionary_terms)

    def get_dictionary_query_inspector_record(self, dictionary_record_type):
        """Gets the dictionary query inspector record corresponding to the given ``Dictionary`` record ``Type``.

        :param dictionary_record_type: a dictionary record type
        :type dictionary_record_type: ``osid.type.Type``
        :return: the dictionary query inspector record
        :rtype: ``osid.dictionary.records.DictionaryQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``dictionary_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(dictionary_record_type)`` is ``false``

        """
        return # osid.dictionary.records.DictionaryQueryInspectorRecord


