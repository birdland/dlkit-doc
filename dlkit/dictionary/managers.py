from ..osid import managers as osid_managers


class DictionaryProfile(osid_managers.OsidProfile):
    """The ``DictionaryProfile`` describes the interoperability among dictionary services."""
    def supports_visible_federation(self):
        """Tests if any dictionary federation is exposed.

        Federation is exposed when a specific dictionary may be
        identified, selected and used to create a lookup or admin
        session. Federation is not exposed when a set of dictionaries
        appears as a single dictionary.

        :return: ``true`` if federation is visible ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_entry_retrieval(self):
        """Tests if retrieving dictionary entries are supported.

        :return: ``true`` if entry retrieval is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_entry_lookup(self):
        """Tests if looking up dictionary entries are supported.

        :return: ``true`` if entry lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_entry_query(self):
        """Tests if querying dictionary entries are supported.

        :return: ``true`` if entry query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_entry_search(self):
        """Tests if searching dictionary entries are supported.

        :return: ``true`` if entry search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_entry_admin(self):
        """Tests if a dictionary entry administrative service is supported.

        :return: ``true`` if dictionary entry administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_entry_notification(self):
        """Tests if a dictionary entry notification service is supported.

        :return: ``true`` if dictionary entry notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_entry_dictionary(self):
        """Tests if retrieving mappings of entry and dictionarys is supported.

        :return: ``true`` if entry dictionary mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_entry_dictionary_assignment(self):
        """Tests if managing mappings of entry and dictionarys is supported.

        :return: ``true`` if entry dictionary assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_entry_smart_dictionary(self):
        """Tests if entry smart dictionarys are available.

        :return: ``true`` if entry smart dictionarys are supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_dictionary_lookup(self):
        """Tests if a dictionary lookup service is supported.

        :return: ``true`` if dictionary lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_dictionary_query(self):
        """Tests if a dictionary query service is supported.

        :return: ``true`` if dictionary query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_dictionary_search(self):
        """Tests if a dictionary search service is supported.

        :return: ``true`` if dictionary search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_dictionary_admin(self):
        """Tests if a dictionary administrative service is supported.

        :return: ``true`` if dictionary administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_dictionary_notification(self):
        """Tests if a dictionary notification service is supported.

        :return: ``true`` if dictionary notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_dictionary_hierachy_traversal(self):
        """Tests if a dictionary hierarchy traversal service is supported.

        :return: ``true`` if dictionary hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_dictionary_hierachy_design(self):
        """Tests if a dictionary hierarchy design service is supported.

        :return: ``true`` if dictionary hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_dictionary_batch(self):
        """Tests if a dictionary batch service is supported.

        :return: ``true`` if dictionary batch service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_entry_key_types(self):
        """Gets the supported ``Entry`` key types.

        :return: a list containing the supported ``Entry`` key types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    entry_key_types = property(fget=get_entry_key_types)

    def supports_entry_key_type(self, entry_key_type):
        """Tests if the given ``Entry`` key type is supported.

        :param entry_key_type: a ``Type`` indicating an ``Entry`` key type
        :type entry_key_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``entry_key_type`` is ``null``

        """
        return # boolean

    def get_entry_value_types(self):
        """Gets the supported ``Entry`` value types.

        :return: a list containing the supported ``Entry`` value types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    entry_value_types = property(fget=get_entry_value_types)

    def supports_entry_value_type(self, entry_value_type):
        """Tests if the given ``Entry`` value type is supported.

        :param entry_value_type: a ``Type`` indicating an ``Entry`` value type
        :type entry_value_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``entry_record_type`` is ``null``

        """
        return # boolean

    def get_entry_value_types_for_key_type(self, entry_key_type):
        """Gets the list of value types supported for the given key type.

        :param entry_key_type: a ``Type`` indicating an ``Entry`` key type
        :type entry_key_type: ``osid.type.Type``
        :return: a list of value types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``entry_key_type`` is ``null``

        """
        return # osid.type.TypeList

    def supports_entry_types(self, entry_key_type, entry_value_type):
        """Tests if the given ``Entry`` key and value types are supported.

        :param entry_key_type: a ``Type`` indicating an ``Entry`` key type
        :type entry_key_type: ``osid.type.Type``
        :param entry_value_type: a ``Type`` indicating an ``Entry`` value type
        :type entry_value_type: ``osid.type.Type``
        :return: ``true`` if the given Types are supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``entry_key_type`` or ``entry_value_type`` is ``null``

        """
        return # boolean

    def get_entry_record_types(self):
        """Gets the supported ``Entry`` record types.

        :return: a list containing the supported ``Entry`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    entry_record_types = property(fget=get_entry_record_types)

    def supports_entry_record_type(self, entry_record_type):
        """Tests if the given ``Entry`` record type is supported.

        :param entry_record_type: a ``Type`` indicating an ``Entry`` record type
        :type entry_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``entry_record_type`` is ``null``

        """
        return # boolean

    def get_entry_search_record_types(self):
        """Gets the supported ``Entry`` search record types.

        :return: a list containing the supported ``Entry`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    entry_search_record_types = property(fget=get_entry_search_record_types)

    def supports_entry_search_record_type(self, entry_search_record_type):
        """Tests if the given ``Entry`` search record type is supported.

        :param entry_search_record_type: a ``Type`` indicating an ``Entry`` search record type
        :type entry_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``entry_search_record_type`` is ``null``

        """
        return # boolean

    def get_dictionary_record_types(self):
        """Gets the supported ``Dictionary`` record types.

        :return: a list containing the supported ``Dictionary`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    dictionary_record_types = property(fget=get_dictionary_record_types)

    def supports_dictionary_record_type(self, dictionary_record_type):
        """Tests if the given ``Dictionary`` record type is supported.

        :param dictionary_record_type: a ``Type`` indicating a ``Dictionary`` record type
        :type dictionary_record_type: ``osid.type.Type``
        :return: ``true`` if the given record Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``dictionary_record_type`` is ``null``

        """
        return # boolean

    def get_dictionary_search_record_types(self):
        """Gets the supported ``Dictionary`` search record types.

        :return: a list containing the supported ``Dictionary`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    dictionary_search_record_types = property(fget=get_dictionary_search_record_types)

    def supports_dictionary_search_record_type(self, dictionary_search_record_type):
        """Tests if the given ``Dictionary`` search record type is supported.

        :param dictionary_search_record_type: a ``Type`` indicating a ``Dictionary`` search record type
        :type dictionary_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``dictionary_search_record_type`` is ``null``

        """
        return # boolean


class DictionaryManager(osid_managers.OsidManager, DictionaryProfile):
    """The dictionary manager provides access to dictionary sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``EntryRetrievalSession:`` a basic session for retrieving
        dictoonary entries
      * ``EntryLookupSession:`` a session for looking up dictionary
        entries
      * ``EntryQuerySession:`` a session for querying dictionary entries
      * ``EntrySearchSession:`` a session for searching for dictionary
        entries
      * ``EntryAdminSession:`` a session for creating, updating, and
        delting dictionary entries
      * ``EntryNotificationSession:`` a session for subscribing to
        notifications about dictionary entries
      * ``EntryDictionarySession:`` a session to look up entry to
        dictionary mappings
      * ``EntryDictionaryAssignmentSession:`` a session to manage entry
        to dictionary mappings
      * ``EntrySmartDictionarySession:`` a session to manage smart entry
        dictionaries
      * ``DictionaryLookupSession`` a session for looking up
        dictionaries
      * ``DictionaryQuerySession`` a session for querying dictionaries
      * ``DictionarySearchSession`` a session for searchin gamong
        dictionaries
      * ``DictionaryAdminSession`` a session creating, updating or
        deleting dictionaries
      * ``DictionaryNotificationSession:`` a session for subscribing to
        adds and changes of dictionaries
      * ``DictionaryHierarchySession:`` a session for traversing the
        hierarchy of dictionaries
      * ``DictionaryHierarchyDesignSession:`` a session for managing the
        dictionary hierarchy


    """
    def get_entry_retrieval_session(self):
        """Gets the ``OsidSession`` used to retrieve dictionary entries.

        :return: the new ``EntryRetrievalSession``
        :rtype: ``osid.dictionary.EntryRetrievalSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_retrieval()`` is ``false``

        """
        return # osid.dictionary.EntryRetrievalSession

    entry_retrieval_session = property(fget=get_entry_retrieval_session)

    def get_entry_retrieval_session_for_dictionary(self, dictionary_id):
        """Gets the ``OsidSession`` used to retrieve dictionary entries for the specified ``Dictionary``.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to use
        :type dictionary_id: ``osid.id.Id``
        :return: an ``EntryRetrievalSession``
        :rtype: ``osid.dictionary.EntryRetrievalSession``
        :raise: ``NotFound`` -- no ``Dictionary`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_retrieval()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.dictionary.EntryRetrievalSession

    def get_entry_lookup_session(self):
        """Gets the ``OsidSession`` used to retrieve dictionary entries.

        :return: an ``EntryLookupSession``
        :rtype: ``osid.dictionary.EntryLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_lookup()`` is ``false``

        """
        return # osid.dictionary.EntryLookupSession

    entry_lookup_session = property(fget=get_entry_lookup_session)

    def get_entry_lookup_session_for_dictionary(self, dictionary_id):
        """Gets the ``OsidSession`` used to lookup dictionary entries for the specified ``Dictionary``.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to use
        :type dictionary_id: ``osid.id.Id``
        :return: an ``EntryLookupSession``
        :rtype: ``osid.dictionary.EntryLookupSession``
        :raise: ``NotFound`` -- no ``Dictionary`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.dictionary.EntryLookupSession

    def get_entry_query_session(self):
        """Gets the ``OsidSession`` used to query dictionary entries.

        :return: an ``EntryQuerySession``
        :rtype: ``osid.dictionary.EntryQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_query()`` is ``false``

        """
        return # osid.dictionary.EntryQuerySession

    entry_query_session = property(fget=get_entry_query_session)

    def get_entry_query_session_for_dictionary(self, dictionary_id):
        """Gets the ``OsidSession`` used to query dictionary entries for the specified ``Dictionary``.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to use
        :type dictionary_id: ``osid.id.Id``
        :return: an ``EntryQuerySession``
        :rtype: ``osid.dictionary.EntryQuerySession``
        :raise: ``NotFound`` -- no ``Dictionary`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.dictionary.EntryQuerySession

    def get_entry_search_session(self):
        """Gets the ``OsidSession`` used to search dictionary entries.

        :return: an ``EntrySearchSession``
        :rtype: ``osid.dictionary.EntrySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_search()`` is ``false``

        """
        return # osid.dictionary.EntrySearchSession

    entry_search_session = property(fget=get_entry_search_session)

    def get_entry_search_session_for_dictionary(self, dictionary_id):
        """Gets the ``OsidSession`` used to search dictionary entries for the specified ``Dictionary``.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to use
        :type dictionary_id: ``osid.id.Id``
        :return: an ``EntrySearchSession``
        :rtype: ``osid.dictionary.EntrySearchSession``
        :raise: ``NotFound`` -- no ``Dictionary`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.dictionary.EntrySearchSession

    def get_entry_admin_session(self):
        """Gets the ``OsidSession`` used to administer dictionary entries.

        :return: an ``EntryAdminSession``
        :rtype: ``osid.dictionary.EntryAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_admin()`` is ``false``

        """
        return # osid.dictionary.EntryAdminSession

    entry_admin_session = property(fget=get_entry_admin_session)

    def get_entry_admin_session_for_dictionary(self, dictionary_id):
        """Gets the ``OsidSession`` used to administer dictionary entries for the specified ``Dictionary``.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to use
        :type dictionary_id: ``osid.id.Id``
        :return: an ``EntryAdminSession``
        :rtype: ``osid.dictionary.EntryAdminSession``
        :raise: ``NotFound`` -- no ``Dictionary`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_admin()`` os ``supports_visible_federration()`` is ``false``

        """
        return # osid.dictionary.EntryAdminSession

    def get_entry_notification_session(self, entry_receiver):
        """Gets an ``EntryNotificationSession`` which is responsible for subscribing to entry changes within a default ``Dictionary``.

        :param entry_receiver: the notification callback
        :type entry_receiver: ``osid.dictionary.EntryReceiver``
        :return: an ``EntryNotificationSession``
        :rtype: ``osid.dictionary.EntryNotificationSession``
        :raise: ``NullArgument`` -- ``entry_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_notification()`` is ``false``

        """
        return # osid.dictionary.EntryNotificationSession

    def get_entry_notification_session_for_dictionary(self, entry_receiver, dictionary_id):
        """Gets an ``EntryNotificationSession`` which is responsible for subscribing to entry changes for a specified ``Dictionary``.

        :param entry_receiver: the notification callback
        :type entry_receiver: ``osid.dictionary.EntryReceiver``
        :param dictionary_id: the ``Id`` of the ``Dictionary`` to use
        :type dictionary_id: ``osid.id.Id``
        :return: an ``EntryNotificationSession``
        :rtype: ``osid.dictionary.EntryNotificationSession``
        :raise: ``NotFound`` -- no ``Dictionary`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``entry_receiver`` or ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.dictionary.EntryNotificationSession

    def get_entry_dictionary_session(self):
        """Gets the session for retrieving entry to dictionary mappings.

        :return: a ``EntryDictionarySession``
        :rtype: ``osid.dictionary.EntryDictionarySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_dictionary()`` is ``false``

        """
        return # osid.dictionary.EntryDictionarySession

    entry_dictionary_session = property(fget=get_entry_dictionary_session)

    def get_entry_dictionary_assignment_session(self):
        """Gets the session for assigning entry to dictionary mappings.

        :return: a ``EntryDictionaryAssignmentSession``
        :rtype: ``osid.dictionary.EntryDictionaryAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_dictionary_assignment()`` is ``false``

        """
        return # osid.dictionary.EntryDictionaryAssignmentSession

    entry_dictionary_assignment_session = property(fget=get_entry_dictionary_assignment_session)

    def get_entry_smart_dictionary_session(self, dictionary_id):
        """Gets the session for managing dynamic entry dictionarys.

        :param dictionary_id: the ``Id`` of the dictionary
        :type dictionary_id: ``osid.id.Id``
        :return: a ``EntrySmartDictionarySession``
        :rtype: ``osid.dictionary.EntrySmartDictionarySession``
        :raise: ``NotFound`` -- ``dictionary_id`` not found
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_smart_dictionary()`` is ``false``

        """
        return # osid.dictionary.EntrySmartDictionarySession

    def get_dictionary_lookup_session(self):
        """Gets the ``OsidSession`` used to lookup dictionaries.

        :return: a ``DictionaryLookupSession``
        :rtype: ``osid.dictionary.DictionaryLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_lookup()`` is ``false``

        """
        return # osid.dictionary.DictionaryLookupSession

    dictionary_lookup_session = property(fget=get_dictionary_lookup_session)

    def get_dictionary_query_session(self):
        """Gets the ``OsidSession`` used to query dictionaries.

        :return: a ``DictionaryQuerySession``
        :rtype: ``osid.dictionary.DictionaryQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_query()`` is ``false``

        """
        return # osid.dictionary.DictionaryQuerySession

    dictionary_query_session = property(fget=get_dictionary_query_session)

    def get_dictionary_search_session(self):
        """Gets the ``OsidSession`` used to search dictionaries.

        :return: a ``DictionarySearchSession``
        :rtype: ``osid.dictionary.DictionarySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_search()`` is ``false``

        """
        return # osid.dictionary.DictionarySearchSession

    dictionary_search_session = property(fget=get_dictionary_search_session)

    def get_dictionary_admin_session(self):
        """Gets the ``OsidSession`` used to administer dictionaries.

        :return: a ``DictionaryAdminSession``
        :rtype: ``osid.dictionary.DictionaryAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_admin()`` is ``false``

        """
        return # osid.dictionary.DictionaryAdminSession

    dictionary_admin_session = property(fget=get_dictionary_admin_session)

    def get_dictionary_notification_session(self, dictionary_receiver):
        """Gets the ``OsidSession`` used to receive notifications of dictionary changes.

        :param dictionary_receiver: the notification callback
        :type dictionary_receiver: ``osid.dictionary.DictionaryReceiver``
        :return: a ``DictionaryNotificationSession``
        :rtype: ``osid.dictionary.DictionaryNotificationSession``
        :raise: ``NullArgument`` -- ``dictionary_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_notification()`` is ``false``

        """
        return # osid.dictionary.DictionaryNotificationSession

    def get_dictionary_hierarchy_session(self):
        """Gets hierarchy service for traversing the ``Dictionary`` hierarchy.

        A parent includes all the dictionary entries of its children.

        :return: a Dictionary ``HierarchySession``
        :rtype: ``osid.dictionary.DictionaryHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_hierarchy_traversal()`` is ``false``

        """
        return # osid.dictionary.DictionaryHierarchySession

    dictionary_hierarchy_session = property(fget=get_dictionary_hierarchy_session)

    def get_dictionary_hierarchy_design_session(self):
        """Gets hierarchy service for structuring ``Dictionary`` objects.

        :return: a ``DictionaryHierarchyDesignSession``
        :rtype: ``osid.dictionary.DictionaryHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_hierarchy_design()`` is ``false``

        """
        return # osid.dictionary.DictionaryHierarchyDesignSession

    dictionary_hierarchy_design_session = property(fget=get_dictionary_hierarchy_design_session)

    def get_dictionary_batch_manager(self):
        """Gets a ``DictionaryBatchManager``.

        :return: a ``DictionaryBatchManager``
        :rtype: ``osid.dictionary.batch.DictionaryBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_batch()`` is ``false``

        """
        return # osid.dictionary.batch.DictionaryBatchManager

    dictionary_batch_manager = property(fget=get_dictionary_batch_manager)


class DictionaryProxyManager(osid_managers.OsidProxyManager, DictionaryProfile):
    """The dictionary manager provides access to dictionary sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support a ``Proxy`` to pass information from
    server environments. The sessions included in this manager are:

      * ``EntryRetrievalSession:`` a basic session for retrieving
        dictoonary entries
      * ``EntryLookupSession:`` a session for looking up dictionary
        entries
      * ``EntryQuerySession:`` a session for querying dictionary entries
      * ``EntrySearchSession:`` a session for searching for dictionary
        entries
      * ``EntryAdminSession:`` a session for creating, updating, and
        delting dictionary entries
      * ``EntryNotificationSession:`` a session for subscribing to
        notifications about dictionary entries
      * ``EntryDictionarySession:`` a session to look up entry to
        dictionary mappings
      * ``EntryDictionaryAssignmentSession:`` a session to manage entry
        to dictionary mappings
      * ``EntrySmartDictionarySession:`` a session to manage smart entry
        dictionaries
      * ``DictionaryLookupSession`` a session for looking up
        dictionaries
      * ``DictionaryQuerySession`` a session for querying dictionaries
      * ``DictionarySearchSession`` a session for searchin gamong
        dictionaries
      * ``DictionaryAdminSession`` a session creating, updating or
        deleting dictionaries
      * ``DictionaryNotificationSession:`` a session for subscribing to
        adds and changes of dictionaries
      * ``DictionaryHierarchySession:`` a session for traversing the
        hierarchy of dictionaries
      * ``DictionaryHierarchyDesignSession:`` a session for managing the
        dictionary hierarchy


    """
    def get_entry_retrieval_session(self, proxy):
        """Gets the ``OsidSession`` used to retrieve dictionary entries.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EntryRetrievalSession``
        :rtype: ``osid.dictionary.EntryRetrievalSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_retrieval()`` is ``false``

        """
        return # osid.dictionary.EntryRetrievalSession

    def get_entry_retrieval_session_for_dictionary(self, dictionary_id, proxy):
        """Gets the ``OsidSession`` used to retrieve dictionary entries for the specified ``Dictionary``.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to use
        :type dictionary_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EntryRetrievalSession``
        :rtype: ``osid.dictionary.EntryRetrievalSession``
        :raise: ``NotFound`` -- no ``Dictionary`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``dictionary_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_retrieval()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.dictionary.EntryRetrievalSession

    def get_entry_lookup_session(self, proxy):
        """Gets the ``OsidSession`` used to lookup dictionary entries.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EntryLookupSession``
        :rtype: ``osid.dictionary.EntryLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_lookup()`` is ``false``

        """
        return # osid.dictionary.EntryLookupSession

    def get_entry_lookup_session_for_dictionary(self, dictionary_id, proxy):
        """Gets the ``OsidSession`` used to lookup dictionary entries for the specified ``Dictionary``.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to use
        :type dictionary_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EntryLookupSession``
        :rtype: ``osid.dictionary.EntryLookupSession``
        :raise: ``NotFound`` -- no ``Dictionary`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``dictionary_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.dictionary.EntryLookupSession

    def get_entry_query_session(self, proxy):
        """Gets the ``OsidSession`` used to query dictionary entries.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EntryQuerySession``
        :rtype: ``osid.dictionary.EntryQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_query()`` is ``false``

        """
        return # osid.dictionary.EntryQuerySession

    def get_entry_query_session_for_dictionary(self, dictionary_id, proxy):
        """Gets the ``OsidSession`` used to query dictionary entries for the specified ``Dictionary``.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to use
        :type dictionary_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EntryQuerySession``
        :rtype: ``osid.dictionary.EntryQuerySession``
        :raise: ``NotFound`` -- no ``Dictionary`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``dictionary_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.dictionary.EntryQuerySession

    def get_entry_search_session(self, proxy):
        """Gets the ``OsidSession`` used to search among dictionary entries.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EntrySearchSession``
        :rtype: ``osid.dictionary.EntrySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_search()`` is ``false``

        """
        return # osid.dictionary.EntrySearchSession

    def get_entry_search_session_for_dictionary(self, dictionary_id, proxy):
        """Gets the ``OsidSession`` used to search among dictionary entries for the specified ``Dictionary``.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to use
        :type dictionary_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EntrySearchSession``
        :rtype: ``osid.dictionary.EntrySearchSession``
        :raise: ``NotFound`` -- no ``Dictionary`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``dictionary_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.dictionary.EntrySearchSession

    def get_entry_admin_session(self, proxy):
        """Gets the ``OsidSession`` used to administer dictionary entries.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EntryAdminSession``
        :rtype: ``osid.dictionary.EntryAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_admin()`` is ``false``

        """
        return # osid.dictionary.EntryAdminSession

    def get_entry_admin_session_for_dictionary(self, dictionary_id, proxy):
        """Gets the ``OsidSession`` used to administer dictionary entries for the specified ``Dictionary``.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to use
        :type dictionary_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EntryAdminSession``
        :rtype: ``osid.dictionary.EntryAdminSession``
        :raise: ``NotFound`` -- no ``Dictionary`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``dictionary_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_admin()`` os ``supports_visible_federration()`` is ``false``

        """
        return # osid.dictionary.EntryAdminSession

    def get_entry_notification_session(self, entry_receiver, proxy):
        """Gets an ``EntryNotificationSession`` which is responsible for subscribing to entry changes within a default ``Dictionary``.

        :param entry_receiver: the notification callback
        :type entry_receiver: ``osid.dictionary.EntryReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EntryNotificationSession``
        :rtype: ``osid.dictionary.EntryNotificationSession``
        :raise: ``NullArgument`` -- ``entry_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_notification()`` is ``false``

        """
        return # osid.dictionary.EntryNotificationSession

    def get_entry_notification_session_for_dictionary(self, entry_receiver, dictionary_id, proxy):
        """Gets an ``EntryNotificationSession`` which is responsible for subscribing to entry changes for a specified ``Dictionary``.

        :param entry_receiver: the notification callback
        :type entry_receiver: ``osid.dictionary.EntryReceiver``
        :param dictionary_id: the ``Id`` of the ``Dictionary`` to use
        :type dictionary_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EntryNotificationSession``
        :rtype: ``osid.dictionary.EntryNotificationSession``
        :raise: ``NotFound`` -- no ``Dictionary`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``entry_receiver, dictionary_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.dictionary.EntryNotificationSession

    def get_entry_dictionary_session(self, proxy):
        """Gets the session for retrieving entry to dictionary mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``EntryDictionarySession``
        :rtype: ``osid.dictionary.EntryDictionarySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_dictionary()`` is ``false``

        """
        return # osid.dictionary.EntryDictionarySession

    def get_entry_dictionary_assignment_session(self, proxy):
        """Gets the session for assigning entry to dictionary mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``EntryDictionaryAssignmentSession``
        :rtype: ``osid.dictionary.EntryDictionaryAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_dictionary_assignment()`` is ``false``

        """
        return # osid.dictionary.EntryDictionaryAssignmentSession

    def get_entry_smart_dictionary_session(self, dictionary_id, proxy):
        """Gets the session for managing dynamic entry dictionarys.

        :param dictionary_id: the ``Id`` of the dictionary
        :type dictionary_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``EntrySmartDictionarySession``
        :rtype: ``osid.dictionary.EntrySmartDictionarySession``
        :raise: ``NotFound`` -- ``dictionary_id`` not found
        :raise: ``NullArgument`` -- ``dictionary_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_smart_dictionary()`` is ``false``

        """
        return # osid.dictionary.EntrySmartDictionarySession

    def get_dictionary_lookup_session(self, proxy):
        """Gets the ``OsidSession`` used to lookup dictionaries.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DictionaryLookupSession``
        :rtype: ``osid.dictionary.DictionaryLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_lookup()`` is ``false``

        """
        return # osid.dictionary.DictionaryLookupSession

    def get_dictionary_query_session(self, proxy):
        """Gets the ``OsidSession`` used to query dictionaries.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DictionaryQuerySession``
        :rtype: ``osid.dictionary.DictionaryQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_query()`` is ``false``

        """
        return # osid.dictionary.DictionaryQuerySession

    def get_dictionary_search_session(self, proxy):
        """Gets the ``OsidSession`` used to search for dictionaries.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DictionarySearchSession``
        :rtype: ``osid.dictionary.DictionarySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_search()`` is ``false``

        """
        return # osid.dictionary.DictionarySearchSession

    def get_dictionary_admin_session(self, proxy):
        """Gets the ``OsidSession`` used to administer dictionaries.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DictionaryAdminSession``
        :rtype: ``osid.dictionary.DictionaryAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_admin()`` is ``false``

        """
        return # osid.dictionary.DictionaryAdminSession

    def get_dictionary_notification_session(self, dictionary_receiver, proxy):
        """Gets the ``OsidSession`` used to subscribe to notifications of new, updated or deleted dictionaries dictionaries.

        :param dictionary_receiver: the notification callback
        :type dictionary_receiver: ``osid.dictionary.DictionaryReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DictionaryNotificationSession``
        :rtype: ``osid.dictionary.DictionaryNotificationSession``
        :raise: ``NullArgument`` -- ``dictionary_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_notification()`` is ``false``

        """
        return # osid.dictionary.DictionaryNotificationSession

    def get_dictionary_hierarchy_session(self, proxy):
        """Gets the hierarchy traversing the ``Dictionary`` hierarchy.

        The parent includes all dictionary elements of its children.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DictionaryHierarchySession``
        :rtype: ``osid.dictionary.DictionaryHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_dictionary_hierarchy()`` is ``false``

        """
        return # osid.dictionary.DictionaryHierarchySession

    def get_dictionary_hierarchy_design_session(self, proxy):
        """Gets the hierarchy managing the ``Dictionary`` hierarchy.

        The parent includes all dictionary elements of its children.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DictionaryHierarchyDesignSession``
        :rtype: ``osid.dictionary.DictionaryHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_dictionary_hierarchy_design()`` is ``false``

        """
        return # osid.dictionary.DictionaryHierarchyDesignSession

    def get_dictionary_batch_proxy_manager(self):
        """Gets a ``DictionaryBatchProxyManager``.

        :return: a ``DictionaryBatchProxyManager``
        :rtype: ``osid.dictionary.batch.DictionaryBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_batch()`` is ``false``

        """
        return # osid.dictionary.batch.DictionaryBatchProxyManager

    dictionary_batch_proxy_manager = property(fget=get_dictionary_batch_proxy_manager)


