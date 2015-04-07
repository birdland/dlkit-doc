from ..osid import objects as osid_objects


class Entry(osid_objects.OsidObject):
    """An ``Entry`` contains a key and a value.

    The key and value have a Type such that an entry is identified by
    the combination of the key, key type, and value type. The Type may
    indicate the key and value are simple strings or, more complex
    objects may be managed that allows for a translation from one
    arbitrary object to another.

    """
    def get_key_type(self):
        """Gets the ``Type`` of this entry key.

        :return: the key ``Type``
        :rtype: ``osid.type.Type``

        """
        return # osid.type.Type

    key_type = property(fget=get_key_type)

    def get_key(self):
        """Gets the key of this entry.

        :return: the key
        :rtype: ``object``

        """
        return # object

    key = property(fget=get_key)

    def get_value_type(self):
        """Gets the ``Type`` of this entry value.

        :return: the value ``Type``
        :rtype: ``osid.type.Type``

        """
        return # osid.type.Type

    value_type = property(fget=get_value_type)

    def get_value(self):
        """Gets the value in this entry.

        :return: the value
        :rtype: ``object``

        """
        return # object

    value = property(fget=get_value)

    def get_entry_record(self, entry_record_type):
        """Gets the entry record corresponding to the given ``Entry`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``entry_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(entry_record_type)``
        is ``true`` .

        :param entry_record_type: the type of the record to retrieve
        :type entry_record_type: ``osid.type.Type``
        :return: the entry record
        :rtype: ``osid.dictionary.records.EntryRecord``
        :raise: ``NullArgument`` -- ``entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(entry_record_type)`` is ``false``

        """
        return # osid.dictionary.records.EntryRecord


class EntryForm(osid_objects.OsidObjectForm):
    """This is the form for creating and updating an ``Entry``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``EntryAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_value_metadata(self):
        """Gets the metadata for the vakue.

        :return: metadata for the value
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    value_metadata = property(fget=get_value_metadata)

    def set_value(self, value):
        """Sets the value.

        :param value: the value
        :type value: ``object``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``value`` is ``null``

        """
        pass

    def clear_value(self):
        """Removes the value.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    value = property(fget=set_value, fdel=clear_value)

    def get_entry_form_record(self, entry_record_type):
        """Gets the ``EntryFormRecord`` corresponding to the given entry record ``Type``.

        :param entry_record_type: an entry record type
        :type entry_record_type: ``osid.type.Type``
        :return: the entry form record
        :rtype: ``osid.dictionary.records.EntryFormRecord``
        :raise: ``NullArgument`` -- ``entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(entry_record_type)`` is ``false``

        """
        return # osid.dictionary.records.EntryFormRecord


class EntryList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``EntryList`` provides a means for accessing ``Entry`` elements sequentially either one at a time or many at a time.

    Examples: while (el.hasNext()) { Entry entry = el.getNextEntry(); }

    or
      while (el.hasNext()) {
           Entry[] entries = el.getNextEntries(el.available());
      }
    


    """
    def get_next_entry(self):
        """Gets the next ``Entry`` in this list.

        :return: the next ``Entry`` in this list. The ``has_next()`` method should be used to test that a next ``Entry`` is available before calling this method.
        :rtype: ``osid.dictionary.Entry``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.dictionary.Entry

    next_entry = property(fget=get_next_entry)

    def get_next_entries(self, n):
        """Gets the next set of ``Entry`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Entry`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Entry`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.dictionary.Entry``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.dictionary.Entry


class Dictionary(osid_objects.OsidCatalog):
    """A ``Dictionary`` represents a collection of entries.

    Like all OSID objects, a ``Dictionary`` is identified by its ``Id``
    and any persisted references should use the ``Id``.

    """
    def get_dictionary_record(self, dictionary_record_type):
        """Gets the dictionary record corresponding to the given ``Dictionary`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``dictionary_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(dictionary_record_type)`` is ``true`` .

        :param dictionary_record_type: the type of the record to retrieve
        :type dictionary_record_type: ``osid.type.Type``
        :return: the dictionary record
        :rtype: ``osid.dictionary.records.DictionaryRecord``
        :raise: ``NullArgument`` -- ``dictionary_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(dictionary_record_type)`` is ``false``

        """
        return # osid.dictionary.records.DictionaryRecord


class DictionaryForm(osid_objects.OsidCatalogForm):
    """This is the form for creating and updating a ``Dictionary``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``DictionaryAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_dictionary_form_record(self, dictionary_record_type):
        """Gets the ``DictionaryFormRecord`` corresponding to the given dictionary record ``Type``.

        :param dictionary_record_type: a dictionary record type
        :type dictionary_record_type: ``osid.type.Type``
        :return: the dictionary form record
        :rtype: ``osid.dictionary.records.DictionaryFormRecord``
        :raise: ``NullArgument`` -- ``dictionary_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(dictionary_record_type)`` is ``false``

        """
        return # osid.dictionary.records.DictionaryFormRecord


class DictionaryList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``DictionaryList`` provides a means for accessing ``Dictionary`` elements sequentially either one at a time or many at a time.

    Examples: while (dl.hasNext()) { Dictionary dictionary =
    dl.getNextDictionary(); }

    or
      while (dl.hasNext()) {
           Dictionary[] dictionaries = dl.getNextDictionaries(dl.available());
      }
    


    """
    def get_next_dictionary(self):
        """Gets the next ``Dictionary`` in this list.

        :return: the next ``Dictionary`` in this list. The ``has_next()`` method should be used to test that a next ``Dictionary`` is available before calling this method.
        :rtype: ``osid.dictionary.Dictionary``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.dictionary.Dictionary

    next_dictionary = property(fget=get_next_dictionary)

    def get_next_dictionaries(self, n):
        """Gets the next set of ``Dictionary`` objects in this lis which must be less than or equal to whst is returned from ``available()``.

        :param n: the number of ``Dictionary`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Dictionary`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.dictionary.Dictionary``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.dictionary.Dictionary


class DictionaryNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``DictionaryHierarchySession``.

    """
    def get_dictionary(self):
        """Gets the ``Dictionary`` at this node.

        :return: the dictionary represented by this node
        :rtype: ``osid.dictionary.Dictionary``

        """
        return # osid.dictionary.Dictionary

    dictionary = property(fget=get_dictionary)

    def get_parent_dictionary_nodes(self):
        """Gets the parents of this dictionary.

        :return: the parents of this dictionary
        :rtype: ``osid.dictionary.DictionaryNodeList``

        """
        return # osid.dictionary.DictionaryNodeList

    parent_dictionary_nodes = property(fget=get_parent_dictionary_nodes)

    def get_child_dictionary_nodes(self):
        """Gets the children of this dictionary.

        :return: the children of this dictionary
        :rtype: ``osid.dictionary.DictionaryNodeList``

        """
        return # osid.dictionary.DictionaryNodeList

    child_dictionary_nodes = property(fget=get_child_dictionary_nodes)


class DictionaryNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``DictionaryNodeList`` provides a means for accessing ``DictionaryNode`` elements sequentially either one at a time or many at a time.

    Examples: while (dnl.hasNext()) { DictionaryNode node =
    dnl.getNextDictionaryNode(); }

    or
      while (dnl.hasNext()) {
           DictionaryNode[] nodes = dnl.getNextDictionaryNodes(dnl.available());
      }
    


    """
    def get_next_dictionary_node(self):
        """Gets the next ``DictionaryNode`` in this list.

        :return: the next ``DictionaryNode`` in this list. The ``has_next()`` method should be used to test that a next ``DictionaryNode`` is available before calling this method.
        :rtype: ``osid.dictionary.DictionaryNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.dictionary.DictionaryNode

    next_dictionary_node = property(fget=get_next_dictionary_node)

    def get_next_dictionary_nodes(self, n):
        """Gets the next set of ``DictionaryNode`` objects in this lis which must be less than or equal to whst is returned from ``available()``.

        :param n: the number of ``DictionaryNode`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``DictionaryNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.dictionary.DictionaryNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.dictionary.DictionaryNode


