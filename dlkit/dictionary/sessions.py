from ..osid import sessions as osid_sessions


class EntryRetrievalSession(osid_sessions.OsidSession):
    """``EntryRetrievalSession`` is used to query dictionary entries.

    A dictionary entry contains a key and a value. The uniqeness of the
    entry depends on the key, the key type and the value type.

    This session defines two views which offer differing behaviors when
    retrieving multiple objects.
    
      * federated view: entries are accessible from the ``Dictionary``
        associated with this session and any descedant dictionaries in
        the ``Dictionary`` hierarchy
      * isolated view: entries are accessible from this ``Dictionary``
        only


    """
    def get_dictionary_id(self):
        """Gets the ``Dictionary``  ``Id`` associated with this session.

        :return: the ``Dictionary``  ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    dictionary_id = property(fget=get_dictionary_id)

    def get_dictionary(self):
        """Gets the ``Dictionary`` associated with this session.

        :return: the ``Dictionary`` associated with this session
        :rtype: ``osid.dictionary.Dictionary``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.Dictionary

    dictionary = property(fget=get_dictionary)

    def can_lookup_entries(self):
        """Tests if this user can perform ``Entry`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_federated_dictionary_view(self):
        """Federates the view for methods in this session.

        A federated view will include entries from descendant
        dictionaries in the dictionary hierarchy.



        """
        pass

    def use_isolated_dictionary_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this dictionary only.



        """
        pass

    def retrieve_entry(self, key, key_type, value_type):
        """Gets the ``Dictionary`` entry associated with the given key and types.

        The ``key_type`` indicates the key object type and the
        ``value_type`` indicates the value object return.

        :param key: the key of the entry to retrieve
        :type key: ``object``
        :param key_type: the key type of the entry to retrieve
        :type key_type: ``osid.type.Type``
        :param value_type: the value type of the entry to retrieve
        :type value_type: ``osid.type.Type``
        :return: the returned ``object``
        :rtype: ``object``
        :raise: ``InvalidArgument`` -- ``key`` is not of ``key_type``
        :raise: ``NotFound`` -- no entry found
        :raise: ``NullArgument`` -- ``key, key_type,`` or ``value_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # object


class EntryLookupSession(EntryRetrievalSession):
    """``EntryLookupSession`` is used to look up dictionary entries.

    This session includes the methods defined in the
    ``EntryRetrievalSession``.

    This session defines two views which offer differing behaviors when
    retrieving multiple objects.
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete and ordered result set or is
        an error condition

    
    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data out of sync or there
    is an authorization block in a particular element.

    """
    def use_comparative_entry_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_entry_view(self):
        """A complete view of the ``Entry`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def get_entry(self, entry_id):
        """Gets the ``Entry`` specified by its ``Id``.

        The identifier represents the union of the key, keyType and
        valueType.In plenary mode, the exact ``Id`` is found or a
        ``NotFound`` results. Otherwise, the returned ``Entry`` may have
        a different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``Agency`` and retained for
        compatibility.

        :param entry_id: ``Id`` of the ``Entry``
        :type entry_id: ``osid.id.Id``
        :return: the entry
        :rtype: ``osid.dictionary.Entry``
        :raise: ``NotFound`` -- ``entry_id`` not found
        :raise: ``NullArgument`` -- ``entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.Entry

    def get_entries_by_ids(self, entry_ids):
        """Gets an ``EntryList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the entries
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Entry`` elements may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param entry_ids: a list of ``Entry Ids``
        :type entry_ids: ``osid.id.IdList``
        :return: the entry list
        :rtype: ``osid.dictionary.EntryList``
        :raise: ``NotFound`` -- ``entry_id`` not found
        :raise: ``NullArgument`` -- ``entry_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.EntryList

    def get_entries_by_genus_type(self, entry_genus_type):
        """Gets an ``EntryList`` corresponding to the given entry genus ``Type`` which does not include entries of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :param entry_genus_type: an entry genus type
        :type entry_genus_type: ``osid.type.Type``
        :return: the returned ``Entry list``
        :rtype: ``osid.dictionary.EntryList``
        :raise: ``NullArgument`` -- ``entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.EntryList

    def get_entries_by_parent_genus_type(self, entry_genus_type):
        """Gets an ``EntryList`` corresponding to the given entry genus ``Type`` and include any additional entries with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :param entry_genus_type: an entry genus type
        :type entry_genus_type: ``osid.type.Type``
        :return: the returned ``Entry list``
        :rtype: ``osid.dictionary.EntryList``
        :raise: ``NullArgument`` -- ``entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.EntryList

    def get_entries_by_record_type(self, entryy_record_type):
        """Gets an ``EntryList`` containing the given entry record ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :param entryy_record_type: an entry record type
        :type entryy_record_type: ``osid.type.Type``
        :return: the returned ``Entry`` list
        :rtype: ``osid.dictionary.EntryList``
        :raise: ``NullArgument`` -- ``entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.EntryList

    def get_entries_by_key_type(self, key_type):
        """Gets all the ``Dictionary`` entries matching the given key ``Type``.

        In plenary mode, the returned list contains all of the entries
        specified in the Id list, in the order of the list, including
        duplicates, or an error results if an Id in the supplied list is
        not found or inaccessible. Otherwise, inaccessible Entry
        elements may be omitted from the list and may present the
        elements in any order including returning a unique set.

        :param key_type: the type of the key to match
        :type key_type: ``osid.type.Type``
        :return: the list of entries matching ``key_type``
        :rtype: ``osid.dictionary.EntryList``
        :raise: ``NullArgument`` -- ``key_type`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.EntryList

    def get_entries_by_key_type_and_value_type(self, key_type, value_type):
        """Gets all the ``Dictionary`` entries matching the given key and value ``Type``.

        In plenary mode, the returned list contains all of the entries
        specified in the Id list, in the order of the list, including
        duplicates, or an error results if an Id in the supplied list is
        not found or inaccessible. Otherwise, inaccessible Entry
        elements may be omitted from the list and may present the
        elements in any order including returning a unique set.

        :param key_type: the type of the key to match
        :type key_type: ``osid.type.Type``
        :param value_type: the type of the value to match
        :type value_type: ``osid.type.Type``
        :return: the list of entries matching ``key_type``
        :rtype: ``osid.dictionary.EntryList``
        :raise: ``NullArgument`` -- ``key_type`` or ``value_type`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.EntryList

    def get_entries_by_key_and_key_type(self, key, key_type):
        """Gets all the ``Dictionary`` entries matching the given key and key ``Type``.

        In plenary mode, the returned list contains all of the entries
        specified in the Id list, in the order of the list, including
        duplicates, or an error results if an Id in the supplied list is
        not found or inaccessible. Otherwise, inaccessible Entry
        elements may be omitted from the list and may present the
        elements in any order including returning a unique set.

        :param key: the key to match
        :type key: ``object``
        :param key_type: the type of the value to match
        :type key_type: ``osid.type.Type``
        :return: the list of entries matching ``key_type``
        :rtype: ``osid.dictionary.EntryList``
        :raise: ``NullArgument`` -- ``key`` or ``key_type`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.EntryList

    def get_entries(self):
        """Gets all the ``Dictionary`` entries.

        In plenary mode, the returned list contains all of the entries
        specified in the Id list, in the order of the list, including
        duplicates, or an error results if an Id in the supplied list is
        not found or inaccessible. Otherwise, inaccessible Entry
        elements may be omitted from the list and may present the
        elements in any order including returning a unique set.

        :return: the list of entries
        :rtype: ``osid.dictionary.EntryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.EntryList

    entries = property(fget=get_entries)


class EntryQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among entries.

    The search query is constructed using the ``EntryQuery``.

    """
    def get_dictionary_id(self):
        """Gets the ``Dictionary``  ``Id`` associated with this session.

        :return: the ``Dictionary``  ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    dictionary_id = property(fget=get_dictionary_id)

    def get_dictionary(self):
        """Gets the ``Dictionary`` associated with this session.

        :return: the ``Dictionary`` associated with this session
        :rtype: ``osid.dictionary.Dictionary``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.Dictionary

    dictionary = property(fget=get_dictionary)

    def can_search_entries(self):
        """Tests if this user can perform dictionary entry searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_federated_dictionary_view(self):
        """Federates the view for methods in this session.

        A federated view will include entries from descendant
        dictionaries in the catalog hierarchy.



        """
        pass

    def use_isolated_dictionary_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications for entries to this
        dictionary only.



        """
        pass

    def get_entry_query(self):
        """Gets an entry query.

        :return: the entry query
        :rtype: ``osid.dictionary.EntryQuery``

        """
        return # osid.dictionary.EntryQuery

    entry_query = property(fget=get_entry_query)

    def get_entries_by_query(self, entry_query):
        """Gets a list of ``Entry`` elements matching the given search.

        :param entry_query: the entry query
        :type entry_query: ``osid.dictionary.EntryQuery``
        :return: the returned ``EntryList``
        :rtype: ``osid.dictionary.EntryList``
        :raise: ``NullArgument`` -- ``entry_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``entry_query`` is not of this service

        """
        return # osid.dictionary.EntryList


class EntrySearchSession(EntryQuerySession):
    """This session provides methods for searching among entries.

    The search query is constructed using the ``EntryQuery``.

    ``get_entry_by_query()`` is the basic search method and returns a
    list of ``Entries``. A more advanced search may be performed with
    ``getEntriesBySearch()``. It accepts an ``EntrySearch`` in addition
    to the query for the purpose of specifying additional options
    affecting the entire search, such as ordering.
    ``get_entries_by_search()`` returns a ``EntrySearchResult`` that can
    be used to access the resulting ``EntryList`` or be used to perform
    a search within the result set through ``EntrySearch``.

    """
    def get_entry_search(self):
        """Gets an entry search.

        :return: the entry search
        :rtype: ``osid.dictionary.EntrySearch``

        """
        return # osid.dictionary.EntrySearch

    entry_search = property(fget=get_entry_search)

    def get_entry_search_order(self):
        """Gets an entry search order.

        The ``EntrySearchOrder`` is supplied to a ``EntrySearch`` to
        specify the ordering of results.

        :return: the entry search order
        :rtype: ``osid.dictionary.EntrySearchOrder``

        """
        return # osid.dictionary.EntrySearchOrder

    entry_search_order = property(fget=get_entry_search_order)

    def get_entries_by_search(self, entry_query, entry_search):
        """Gets a list of ``Entry`` elements matching the given search.

        :param entry_query: the entry query
        :type entry_query: ``osid.dictionary.EntryQuery``
        :param entry_search: the entry search
        :type entry_search: ``osid.dictionary.EntrySearch``
        :return: the returned search results
        :rtype: ``osid.dictionary.EntrySearchResults``
        :raise: ``NullArgument`` -- ``entry_query`` or ``entry_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``entry_search`` or ``entry_query`` is not of this service

        """
        return # osid.dictionary.EntrySearchResults

    def get_entry_query_from_inspector(self, entry_query_inspector):
        """Gets an entry query from an inspector.

        The inspector is available from an ``EntrySearchResults``.

        :param entry_query_inspector: an entry query inspector
        :type entry_query_inspector: ``osid.dictionary.EntryQueryInspector``
        :return: the entry query
        :rtype: ``osid.dictionary.EntryQuery``
        :raise: ``NullArgument`` -- ``entry_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``entry_query_inspector`` is not of this service

        """
        return # osid.dictionary.EntryQuery


class EntryAdminSession(osid_sessions.OsidSession):
    """``EntryAdminSession`` creates, updates and deletes dictionary entries."""
    def get_dictionary_id(self):
        """Gets the ``Dictionary``  ``Id`` associated with this session.

        :return: the ``Dictionary``  ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    dictionary_id = property(fget=get_dictionary_id)

    def get_dictionary(self):
        """Gets the ``Dictionary`` associated with this session.

        :return: the ``Dictionary`` associated with this session
        :rtype: ``osid.dictionary.Dictionary``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.Dictionary

    dictionary = property(fget=get_dictionary)

    def can_create_entries(self):
        """Tests if this user can create entries A return of true does not guarantee successful authorization.

        A return of false indicates that it is known creating an
        ``Entry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if entry creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_create_entry_with_record_types(self, entry_record_types):
        """Tests if this user can create a single ``Entry`` using the desired record types.

        While ``DictionaryManager.getEntryRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Entry``.
        Providing an empty array tests if an ``Entry`` can be created
        with no records.

        :param entry_record_types: array of entry record types
        :type entry_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Entry`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``entry_record_types`` is ``null``

        """
        return # boolean

    def get_entry_form_for_create(self, key_type, key, value_type, entry_record_types):
        """Gets the entry form for creating new inquiries.

        A new form should be requested for each create transaction.

        :param key_type: the ``Type`` of the key
        :type key_type: ``osid.type.Type``
        :param key: the key
        :type key: ``object``
        :param value_type: the ``Type`` of the value
        :type value_type: ``osid.type.Type``
        :param entry_record_types: array of entry record types
        :type entry_record_types: ``osid.type.Type[]``
        :return: the entry form
        :rtype: ``osid.dictionary.EntryForm``
        :raise: ``AlreadyExists`` -- an entry by this ``key,``  ``key_type,`` and ``value_type`` already exists
        :raise: ``NullArgument`` -- ``key_type, key, value_type,`` or ``entry_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested key/value or record types

        """
        return # osid.dictionary.EntryForm

    def create_entry(self, entry_form):
        """Creates a new ``Entry``.

        :param entry_form: the form for this entry
        :type entry_form: ``osid.dictionary.EntryForm``
        :return: the created entry
        :rtype: ``osid.dictionary.Entry``
        :raise: ``IllegalState`` -- ``entry_form`` already used in a create transaction.
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``entry_form`` did not originate from ``get_entry_form_for_create()``

        """
        return # osid.dictionary.Entry

    def can_update_entries(self):
        """Tests if this user can update entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an ``Entry``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if entry modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_entry_form_for_update(self, entry_id):
        """Gets the entry form for updating an existing entry.

        A new entry form should be requested for each update
        transaction.

        :param entry_id: the ``Id`` of the ``Entry``
        :type entry_id: ``osid.id.Id``
        :return: the entry form
        :rtype: ``osid.dictionary.EntryForm``
        :raise: ``NotFound`` -- ``entry_id`` is not found
        :raise: ``NullArgument`` -- ``entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.EntryForm

    def update_entry(self, entry_form):
        """Updates an existing ``Entry``.

        :param entry_form: the form containing the elements to be updated
        :type entry_form: ``osid.dictionary.EntryForm``
        :raise: ``IllegalState`` -- ``entry_form`` already used in an update transatcion
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``entryy_form`` did not originate from ``get_entry_form_for_update()``

        """
        pass

    def can_delete_entries(self):
        """Tests if this user can delete ``Entries``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an ``Entry``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Entry`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def delete_entry(self, entry_id):
        """Updates an existing ``Dictionary`` entry identified with the specified key with the given value.

        :param entry_id: the ``Id`` of the entry
        :type entry_id: ``osid.id.Id``
        :raise: ``NotFound`` -- entry is not found
        :raise: ``NullArgument`` -- ``entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_manage_entry_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Entries``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Entry`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def alias_entry(self, entry_id, alias_id):
        """Adds an ``Id`` to an ``Entry`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Entry`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another entry, it is
        reassigned to the given entry ``Id``.

        :param entry_id: the ``Id`` of an ``Entry``
        :type entry_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``entry_id`` not found
        :raise: ``NullArgument`` -- ``entry_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class EntryNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``Entry`` objects within a ``Dictionary``.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    """
    def get_dictionary_id(self):
        """Gets the ``Dictionary``  ``Id`` associated with this session.

        :return: the ``Dictionary``  ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    dictionary_id = property(fget=get_dictionary_id)

    def get_dictionary(self):
        """Gets the ``Dictionary`` associated with this session.

        :return: the ``Dictionary`` associated with this session
        :rtype: ``osid.dictionary.Dictionary``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.Dictionary

    dictionary = property(fget=get_dictionary)

    def can_register_for_entry_notifications(self):
        """Tests if this user can register for ``Entry`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_federated_dictionary_view(self):
        """Federates the view for methods in this session.

        A federated view will include entries from parent dictionaries
        in the dictionary hierarchy.



        """
        pass

    def use_isolated_dictionary_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications for entries to this
        dictionary only.



        """
        pass

    def register_for_new_entries(self):
        """Registers for notifications of new entries.

        ``EntryReceiver.newEntry(key, keyType)`` is invoked when a new
        ``Entry`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_entries_by_key_type_and_value_type(self, key_type, value_type):
        """Registers for notifications of new entries by key and value types.

        ``EntryReceiver.newEntry(key, keyType)`` is invoked when a new
        ``Entry`` is created.

        :param key_type: the entry key type
        :type key_type: ``osid.type.Type``
        :param value_type: the entry key type
        :type value_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``key_type`` or ``value_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_entries(self):
        """Regsiters for notification of updated entries.

        ``EntryReceiver.changedEntry(key, keyType)`` is invoked when an
        ``Entry`` is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_entries_by_key_type_and_value_type(self, key_type, value_type):
        """Registers for notifications of an update to entries by key and value type ````.

        ``EntryReceiver.changedEntry(key, keyType)`` is invoked when the
        specified ``Entry`` is changed.

        :param key_type: the entry key type
        :type key_type: ``osid.type.Type``
        :param value_type: the entry key type
        :type value_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``key_type`` or ``value_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_entry(self, entry_id):
        """Registers for notifications of an update to an ``Entry``.

        ``EntryReceiver.changedEntry(key, keyType)`` is invoked when the
        specified ``Entry`` is changed.

        :param entry_id: the entry ``Id``
        :type entry_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_entries(self):
        """Registers for notification of deleted dictionaries.

        ``EntryReceiver.deletedEntry(key, keyType)`` is invoked when the
        specified ``Entry`` is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_entries_by_key_type_and_value_type(self, key_type, value_t_ype):
        """Registers for notifications of a deleted entries by key and value type.

        ``EntryReceiver.deletedEntry(key, keyType)`` is invoked when the
        specified ``Entry`` is removed from this dictionary.

        :param key_type: the entry key type
        :type key_type: ``osid.type.Type``
        :param value_t_ype: the entry key type
        :type value_t_ype: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``key_type or value_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_entry(self, entry_id):
        """Registers for notifications of a deleted ``Entry``.

        ``EntryReceiver.deletedEntry(key, keyType)`` is invoked when the
        specified ``Entry`` is removed from this dictionary.

        :param entry_id: the entry ``Id``
        :type entry_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class EntryDictionarySession(osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Entry`` to ``Dictionary`` mappings.

    A ``Entry`` may appear in multiple dictionaries ````. Each
    ``Dictionary`` may have its own authorizations governing who is
    allowed to look at it.

    This lookup session defines several views:
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition


    """
    def use_comparative_dictionary_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_dictionary_view(self):
        """A complete view of the ``Entry`` and ``Dictionary`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def can_lookup_entry_dictionary_mappings(self):
        """Tests if this user can perform lookups of entry/dictionary mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_entry_ids_by_dictionary(self, dictionary_id):
        """Gets the list of ``Entry``  ``Ids`` associated with a ``Dictionary``.

        :param dictionary_id: ``Id`` of a ``Dictionary``
        :type dictionary_id: ``osid.id.Id``
        :return: list of related entry ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``dictionary_id`` is not found
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_entries_by_dictionary(self, dictionary_id):
        """Gets the list of dictionary entries associated with a ``Dictionary``.

        :param dictionary_id: ``Id`` of a ``Dictionary``
        :type dictionary_id: ``osid.id.Id``
        :return: list of related entries
        :rtype: ``osid.dictionary.EntryList``
        :raise: ``NotFound`` -- ``dictionary_id`` is not found
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.EntryList

    def get_entry_ids_by_dictionaries(self, dictionary_ids):
        """Gets the list of ``Entry Ids`` corresponding to a list of ``Dictionary`` objects.

        :param dictionary_ids: list of dictionary ``Ids``
        :type dictionary_ids: ``osid.id.IdList``
        :return: list of entry ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``dictionary_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_entries_by_dictionaries(self, dictionary_ids):
        """Gets the list of entries corresponding to a list of dictioanries.

        :param dictionary_ids: list of dictionary ``Ids``
        :type dictionary_ids: ``osid.id.IdList``
        :return: list of entries
        :rtype: ``osid.dictionary.EntryList``
        :raise: ``NullArgument`` -- ``dictionary_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.EntryList

    def get_dictionary_ids_by_entry(self, entry_id):
        """Gets the list of ``Dictionary``  ``Ids`` mapped to a ``Entry``.

        :param entry_id: ``Id`` of a ``Entry``
        :type entry_id: ``osid.id.Id``
        :return: list of dictionary ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``entry_id`` is not found
        :raise: ``NullArgument`` -- ``entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_dictionaries_by_entry(self, entry_id):
        """Gets the list of ``Dictionary`` objects mapped to a ``Entry``.

        :param entry_id: ``Id`` of a ``Entry``
        :type entry_id: ``osid.id.Id``
        :return: list of dictionaries
        :rtype: ``osid.dictionary.DictionaryList``
        :raise: ``NotFound`` -- ``entry_id`` is not found
        :raise: ``NullArgument`` -- ``entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.DictionaryList


class EntryDictionaryAssignmentSession(osid_sessions.OsidSession):
    """This session provides methods to re-assign enrties to dictionaries.

    A ``Entry`` may map to multiple ``Dictionary`` objects and removing
    the last reference to a ``Entry`` is the equivalent of deleting it.
    Each ``Dictionary`` may have its own authorizations governing who is
    allowed to operate on it.

    Moving or adding a reference of a ``Entry`` to another
    ``Dictionary`` is not a copy operation (eg: does not change its
    ``Id`` ).

    """
    def can_assign_entries(self):
        """Tests if this user can alter entry/dictionary mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_assign_entries_to_dictionary(self, dictionary_id):
        """Tests if this user can alter entry/dictionary mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied`` . This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param dictionary_id: the ``Id`` of the ``Dictionary``
        :type dictionary_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``

        """
        return # boolean

    def get_assignable_dictionary_ids(self, dictionary_id):
        """Gets a list of dictionaries including and under the given dictionary node in which any entry can be assigned.

        :param dictionary_id: the ``Id`` of the ``Dictionary``
        :type dictionary_id: ``osid.id.Id``
        :return: list of assignable dictionary ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.IdList

    def get_assignable_dictionary_ids_for_entry(self, dictionary_id, entry_id):
        """Gets a list of dictionaries including and under the given dictionary node in which a specific entry can be assigned.

        :param dictionary_id: the ``Id`` of the ``Dictionary``
        :type dictionary_id: ``osid.id.Id``
        :param entry_id: the ``Id`` of the ``Entry``
        :type entry_id: ``osid.id.Id``
        :return: list of assignable dictionary ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``dictionary_id`` or ``entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.IdList

    def assign_entry_to_dictionary(self, entry_id, dictionary_id):
        """Adds an existing ``Entry`` to a ``Dictionary``.

        :param entry_id: the ``Id`` of the ``Entry``
        :type entry_id: ``osid.id.Id``
        :param dictionary_id: the ``Id`` of the ``Dictionary``
        :type dictionary_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``entry_id`` is already assigned to ``dictionary_id``
        :raise: ``NotFound`` -- ``entry_id`` or ``dictionary_id`` not found
        :raise: ``NullArgument`` -- ``entry_id`` or ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def unassign_entry_from_dictionary(self, entry_id, dictionary_id):
        """Removes a ``Entry`` from a ``Dictionary``.

        :param entry_id: the ``Id`` of the ``Entry``
        :type entry_id: ``osid.id.Id``
        :param dictionary_id: the ``Id`` of the ``Dictionary``
        :type dictionary_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``entry_id`` or ``dictionary_id`` not found or ``entry_id`` not assigned to ``dictionary_id``
        :raise: ``NullArgument`` -- ``entry_id`` or ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class EntrySmartDictionarySession(osid_sessions.OsidSession):
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``EntryQuery`` can be retrieved from this session and mapped to
    this ``Dictionary`` to create a virtual collection of ``Entries``.
    The entries may be sequenced using the ``EntrySearchOrder`` from
    this session.

    This ``Dictionary`` has a default query that matches any entry and a
    default search order that specifies no sequencing. The queries may
    be examined using a ``EntryQueryInspector``. The query may be
    modified by converting the inspector back to a ``EntryQuery``.

    """
    def get_dictionary_id(self):
        """Gets the ``Dictionary``  ``Id`` associated with this session.

        :return: the ``Dictionary Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    dictionary_id = property(fget=get_dictionary_id)

    def get_dictionary(self):
        """Gets the ``Dictionary`` associated with this session.

        :return: the ``Dictionary`` associated with this session
        :rtype: ``osid.dictionary.Dictionary``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.Dictionary

    dictionary = property(fget=get_dictionary)

    def can_manage_smart_dictionaries(self):
        """Tests if this user can manage smart dictionarys.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart dictionary management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_entry_query(self):
        """Gets a entry query.

        :return: the entry query
        :rtype: ``osid.dictionary.EntryQuery``

        """
        return # osid.dictionary.EntryQuery

    entry_query = property(fget=get_entry_query)

    def get_entry_search_order(self):
        """Gets a entry search order.

        :return: the entry search order
        :rtype: ``osid.dictionary.EntrySearchOrder``

        """
        return # osid.dictionary.EntrySearchOrder

    entry_search_order = property(fget=get_entry_search_order)

    def apply_entry_query(self, entry_query):
        """Applies a entry query to this dictionary.

        :param entry_query: the entry query
        :type entry_query: ``osid.dictionary.EntryQuery``
        :raise: ``NullArgument`` -- ``entry_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``entry_query`` not of this service

        """
        pass

    def inspect_entry_query(self):
        """Gets a entry query inspector for this dictionary.

        :return: the entry query inspector
        :rtype: ``osid.dictionary.EntryQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        return # osid.dictionary.EntryQueryInspector

    def apply_entry_sequencing(self, entry_search_order):
        """Applies a entry search order to this dictionary.

        :param entry_search_order: the entry search order
        :type entry_search_order: ``osid.dictionary.EntrySearchOrder``
        :raise: ``NullArgument`` -- ``entry_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``entry_search_order`` not of this service

        """
        pass

    def get_entry_query_from_inspector(self, entry_query_inspector):
        """Gets a entry query from an inspector.

        :param entry_query_inspector: a entry query inspector
        :type entry_query_inspector: ``osid.dictionary.EntryQueryInspector``
        :return: the entry query
        :rtype: ``osid.dictionary.EntryQuery``
        :raise: ``NullArgument`` -- ``entry_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``entry_query_inspector`` is not of this service

        """
        return # osid.dictionary.EntryQuery


class DictionaryLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Dictionary`` objects.

    The ``Dictionary represents a`` collection of key/value entries.

    This session defines two views which offer differing behaviors when
    retrieving multiple objects.
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete and ordered result set or is
        an error condition

    
    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data out of sync. For
    example, a hierarchy output can be plugged into a lookup method to
    retrieve all objects known to a hierarchy, but it may not be
    necessary to break execution if a node from the hierarchy no longer
    exists. However, some administrative applications may need to know
    whether it had retrieved an entire set of objects and may sacrifice
    some interoperability for the sake of precision.

    """
    def can_lookup_dictionaries(self):
        """Tests if this user can perform ``Dictionary`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_dictionary_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_dictionary_view(self):
        """A complete view of the ``Dictionary`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def get_dictionary(self, dictionary_id):
        """Gets the ``Dictionary`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Dictionary`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Dictionary`` and retained
        for compatibility.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to retrieve
        :type dictionary_id: ``osid.id.Id``
        :return: the ``Dictionary``
        :rtype: ``osid.dictionary.Dictionary``
        :raise: ``NotFound`` -- no ``Dictionary`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``Id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.Dictionary

    def get_dictionaries_by_ids(self, dictionary_ids):
        """Gets a ``DictionaryList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        dictionaries specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Dictionary`` elements may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :param dictionary_ids: the list of ``Ids`` to retrieve
        :type dictionary_ids: ``osid.id.IdList``
        :return: the returned ``Dictionary`` list
        :rtype: ``osid.dictionary.DictionaryList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``dictionary_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.DictionaryList

    def get_dictionaries_by_genus_type(self, dictionary_genus_type):
        """Gets a ``DictionaryList`` corresponding to the given dictionary genus ``Type`` which does not include dictionaries of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        dictionaries or an error results. Otherwise, the returned list
        may contain only those dictionaries that are accessible through
        this session.

        :param dictionary_genus_type: a dictionary genus type
        :type dictionary_genus_type: ``osid.type.Type``
        :return: the returned ``Dictionary list``
        :rtype: ``osid.dictionary.DictionaryList``
        :raise: ``NullArgument`` -- ``dictionary_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.DictionaryList

    def get_dictionaries_by_parent_genus_type(self, dictionary_genus_type):
        """Gets a ``DictionaryList`` corresponding to the given dictionary genus ``Type`` and include any additional dictionaries with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        dictionaries or an error results. Otherwise, the returned list
        may contain only those dictionaries that are accessible through
        this session.

        :param dictionary_genus_type: a dictionary genus type
        :type dictionary_genus_type: ``osid.type.Type``
        :return: the returned ``Dictionary`` list
        :rtype: ``osid.dictionary.DictionaryList``
        :raise: ``NullArgument`` -- ``dictionary_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.DictionaryList

    def get_dictionaries_by_record_type(self, dictionary_record_type):
        """Gets a ``DictionaryList`` containing the given dictionary record ``Type``.

        In plenary mode, the returned list contains all known
        dictionaries or an error results. Otherwise, the returned list
        may contain only those dictionaries that are accessible through
        this session.

        :param dictionary_record_type: a dictionary record type
        :type dictionary_record_type: ``osid.type.Type``
        :return: the returned ``Dictionary`` list
        :rtype: ``osid.dictionary.DictionaryList``
        :raise: ``NullArgument`` -- ``dictionary_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.DictionaryList

    def get_dictionaries_by_provider(self, resource_id):
        """Gets a ``DictionaryList`` for the given provider ````.

        In plenary mode, the returned list contains all known
        dictionaries or an error results. Otherwise, the returned list
        may contain only those dictionaries that are accessible through
        this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Dictionary`` list
        :rtype: ``osid.dictionary.DictionaryList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.DictionaryList

    def get_dictionaries(self):
        """Gets all ``Dictionary`` elements.

        In plenary mode, the returned list contains all known
        dictionaries or an error results. Otherwise, the returned list
        may contain only those dictionaries that are accessible through
        this session.

        :return: a list of dictionaries
        :rtype: ``osid.dictionary.DictionaryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.DictionaryList

    dictionaries = property(fget=get_dictionaries)


class DictionaryQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching ``Dictionary`` objects.

    The search query is constructed using the ``DictionaryQuery``. The
    dictionary record ``Type`` also specifies the record for the
    dictionary query.

    Dictionaries may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``DictionaryQuery``.

    """
    def can_search_dictionaries(self):
        """Tests if this user can perform ``Dictionary`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_dictionary_query(self):
        """Gets a dictionary query.

        :return: the dictionary query
        :rtype: ``osid.dictionary.DictionaryQuery``

        """
        return # osid.dictionary.DictionaryQuery

    dictionary_query = property(fget=get_dictionary_query)

    def get_dictionaries_by_query(self, dictionary_query):
        """Gets a list of ``Dictionary`` elements matching the given query.

        :param dictionary_query: the dictionary query
        :type dictionary_query: ``osid.dictionary.DictionaryQuery``
        :return: the returned ``DictionaryList``
        :rtype: ``osid.dictionary.DictionaryList``
        :raise: ``NullArgument`` -- ``dictionary_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``dictionary_query`` is not of this service

        """
        return # osid.dictionary.DictionaryList


class DictionarySearchSession(DictionaryQuerySession):
    """This session provides methods for searching ``Dictionary`` objects.

    The search query is constructed using the ``DictionaryQuery. The``
    dictionary record ``Type`` also specifies the record for the
    dictionary query.

    ``get_dictionaries_by_query()`` is the basic search method and
    returns a list of ``Dictionary`` elements. A more advanced search
    may be performed with ``getDictionaresBySearch()``. It accepts a
    ``DictionarySearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_dictionaries_by_search()`` returns a
    ``DictionarySearchResults`` that can be used to access the resulting
    ``DictionaryList`` or be used to perform a search within the result
    set through ``DictionarySearch``.
    
    Dictionaries may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``DictionaryQuery``.

    """
    def get_dictionary_search(self):
        """Gets a dictionary search.

        :return: the dictionary search
        :rtype: ``osid.dictionary.DictionarySearch``

        """
        return # osid.dictionary.DictionarySearch

    dictionary_search = property(fget=get_dictionary_search)

    def get_dictionary_search_order(self):
        """Gets a dictionary search order.

        The ``DictionarySearchOrder`` is supplied to a
        ``DictionarySearch`` to specify the ordering of results.

        :return: the dictionary search order
        :rtype: ``osid.dictionary.DictionarySearchOrder``

        """
        return # osid.dictionary.DictionarySearchOrder

    dictionary_search_order = property(fget=get_dictionary_search_order)

    def get_dictionaries_by_search(self, dictionary_query, dictionary_search):
        """Gets the search results matching the given search query using the given search.

        :param dictionary_query: the dictionary search query
        :type dictionary_query: ``osid.dictionary.DictionaryQuery``
        :param dictionary_search: the dictionary search
        :type dictionary_search: ``osid.dictionary.DictionarySearch``
        :return: the returned search results
        :rtype: ``osid.dictionary.DictionarySearchResults``
        :raise: ``NullArgument`` -- ``dictionary_query`` or ``dictionary_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``dictionary_search`` or ``dictionary_query`` is not of this service

        """
        return # osid.dictionary.DictionarySearchResults

    def get_dictionary_query_from_inspector(self, dictionary_query_inspector):
        """Gets a dictionary query from an inspector.

        The inspector is available from a ``DictionarySearchResults``.

        :param dictionary_query_inspector: a dictionary query inspector
        :type dictionary_query_inspector: ``osid.dictionary.DictionaryQueryInspector``
        :return: the dictionary query
        :rtype: ``osid.dictionary.DictionaryQuery``
        :raise: ``NullArgument`` -- ``dictionary_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``dictionary_query_inspector`` is not of this service

        """
        return # osid.dictionary.DictionaryQuery


class DictionaryAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Dictionaries``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Dictionary,`` a ``DictionaryForm`` is requested using
    ``get_dictionary_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``DictionaryForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``DictionaryForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``DictionaryForm``
    corresponds to an attempted transaction.
    
    For updates, ``DictionaryForms`` are requested to the ``Dictionary``
    ``Id`` that is to be updated using ``getDictionaryFormForUpdate()``.
    Similarly, the ``DictionaryForm`` has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ``DictionaryForm`` can only be used once for a
    successful update and cannot be reused.
    
    The delete operations delete ``Dictionaries``.
    
    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def can_create_dictionaries(self):
        """Tests if this user can create ``Dictionaries``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Dictionary`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Dictionary`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_create_dictionary_with_record_types(self, dictionary_record_types):
        """Tests if this user can create a single ``Dictionary`` using the desired record types.

        While ``DictionaryManager.getDictionaryRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Dictionary``. Providing an empty array tests if a
        ``Dictionary`` can be created with no records.

        :param dictionary_record_types: array of dictionary record types
        :type dictionary_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Dictionary`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``dictionary_record_types`` is ``null``

        """
        return # boolean

    def get_dictionary_form_for_create(self, dictionary_record_types):
        """Gets the dictionary form for creating new dictionaries.

        A new form should be requested for each create transaction.

        :param dictionary_record_types: array of dictionary record types
        :type dictionary_record_types: ``osid.type.Type[]``
        :return: the dictionary form
        :rtype: ``osid.dictionary.DictionaryForm``
        :raise: ``NullArgument`` -- ``dictionary_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        return # osid.dictionary.DictionaryForm

    def create_dictionary(self, dictionary_form):
        """Creates a new ``Dictionary``.

        :param dictionary_form: the form for the new ``Dictionary``
        :type dictionary_form: ``osid.dictionary.DictionaryForm``
        :return: the new ``Dictionary``
        :rtype: ``osid.dictionary.Dictionary``
        :raise: ``IllegalState`` -- ``dictionary_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``dictionary_forms`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``dictionary_form`` did not originate from ``get_dictionary_form_for_create()``

        """
        return # osid.dictionary.Dictionary

    def can_update_dictionaries(self):
        """Tests if this user can update ``Dictionaries``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a Dictionary
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if ``Dictionary`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_dictionary_form_for_update(self, dictionary_id):
        """Gets the dictionary form for updating an existing dictionary.

        A new dictionary form should be requested for each update
        transaction.

        :param dictionary_id: the ``Id`` of the ``Dictionary``
        :type dictionary_id: ``osid.id.Id``
        :return: the dictionary form
        :rtype: ``osid.dictionary.DictionaryForm``
        :raise: ``NotFound`` -- ``dictionary_id`` is not found
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.DictionaryForm

    def update_dictionary(self, dictionary_form):
        """Updates an existing dictionary.

        :param dictionary_form: the form containing the elements to be updated
        :type dictionary_form: ``osid.dictionary.DictionaryForm``
        :raise: ``IllegalState`` -- ``dictionary_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``dictionary_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- a ``dictionary_form`` did not originate from ``get_dictionary_form_for_update()``

        """
        pass

    def can_delete_dictionaries(self):
        """Tests if this user can delete ``Dictionaries``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Dictionary`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Dictionary`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def delete_dictionary(self, dictionary_id):
        """Deletes a ``Dictionary``.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to delete
        :type dictionary_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``dictionary_id`` not found
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_manage_dictionary_aliases(self):
        """Tests if this user can manage ``Id`` aliases for dictionaries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Dictionary`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def alias_dictionary(self, dictionary_id, alias_id):
        """Adds an ``Id`` to a ``Dictionary`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Dictionary`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another dictionary it is
        reassigned to the given dictionary ``Id``.

        :param dictionary_id: the ``Id`` of an ``Dictionary``
        :type dictionary_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``dictionary_id`` not found
        :raise: ``NullArgument`` -- ``dictionary_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class DictionaryNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``Dictionary`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    """
    def can_register_for_dictionary_notifications(self):
        """Tests if this user can register for ``Dictionary`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def register_for_new_dictionaries(self):
        """Register for notifications of new dictionaries.

        ``DictionaryReceiver.newDictionary()`` is invoked when a new
        ``Dictionary`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_dictionary_ancestors(self, dictionary_id):
        """Registers for notification of an updated hierarchy structure that introduces a new ancestor of the specified dictionary.

        ``DictionaryReceiver.newAncestorDictionary()`` is invoked when
        the specified dictionary node gets a new ancestor.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` node to monitor
        :type dictionary_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_dictionary_descendants(self, dictionary_id):
        """Registers for notification of an updated hierarchy structure that introduces a new descendant of the specified dictionary.

        ``DictionaryReceiver.newDescendantDictionary()`` is invoked when
        the specified dictionary node gets a new descendant.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` node to monitor
        :type dictionary_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_dictionaries(self):
        """Registers for notification of updated dictionaries.

        ``DictionaryReceiver.changedDictionary()`` is invoked when a
        dictionary is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_dictionary(self, dictionary_id):
        """Registers for notification of an updated dictionary.

        ``DictionaryReceiver.changedDictionary()`` is invoked when the
        specified dictionary is changed. A notification may be triggered
        for any updated, deleted or new dictionary the specified
        dictionary inherits data from.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to monitor
        :type dictionary_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_dictionaries(self):
        """Registers for notification of deleted dictionaries.

        ``DictionaryReceiver.deletedDictionary()`` is invoked when a
        dictionary is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_dictionary(self, dictionary_id):
        """Registers for notification of a deleted dictionary.

        ``DictionaryReceiver.changedDictionary()`` is invoked when the
        specified dictionary is changed.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to monitor
        :type dictionary_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_dictionary_ancestors(self, dictionary_id):
        """Registers for notification of an updated hierarchy structure that removes an ancestor of the specified dictionary.

        ``DictionaryReceiver.deletedAncestor()`` is invoked when the
        specified dictionary node loses an ancestor.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to monitor
        :type dictionary_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_dictionary_descendants(self, dictionary_id):
        """Registers for notification of an updated hierarchy structure that removes a descendant of the specified dictionary.

        ``DictionaryReceiver.deletedDescendant()`` is invoked when the
        specified dictionary node loses a descendant.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to monitor
        :type dictionary_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class DictionaryHierarchySession(osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of ``Dictionary`` objects.

    Each node in the hierarchy is a unique ``Dictionary``. The hierarchy
    may be traversed recursively to establish the tree structure through
    ``get_parent_d_ictionaries()`` and ``getChildDictionaries()``. To
    relate these ``Ids`` to another OSID, ``get_dictionary_nodes()`` can
    be used for retrievals that can be used for bulk lookups in other
    OSIDs. Any ``Dictionary`` available in the Dictionary OSID is known
    to this hierarchy but does not appear in the hierarchy traversal
    until added as a root node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_dictionaries()`` or
    ``get_child_dictionaries()`` in lieu of a ``PermissionDenied`` error
    that may disrupt the traversal through authorized pathways.
    
    This session defines views that offer differing behaviors when
    retrieving multiple objects.
    
      * comparative view: dictionary elements may be silently omitted or
        re-ordered
      * plenary view: provides a complete set or is an error condition


    """
    def get_dictionary_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    dictionary_hierarchy_id = property(fget=get_dictionary_hierarchy_id)

    def get_dictionary_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

    dictionary_hierarchy = property(fget=get_dictionary_hierarchy)

    def can_access_dictionary_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_dictionary_view(self):
        """The returns from the dictionary methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_dictionary_view(self):
        """A complete view of the ``Dictionary`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def get_root_dictionary_ids(self):
        """Gets the root dictionary ``Ids`` in this hierarchy.

        :return: the root dictionary ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    root_dictionary_ids = property(fget=get_root_dictionary_ids)

    def get_root_dictionaries(self):
        """Gets the root subjects in the dictionary hierarchy.

        A node with no parents is an orphan. While all dictionary
        ``Ids`` are known to the hierarchy, an orphan does not appear in
        the hierarchy unless explicitly added as a root node or child of
        another node.

        :return: the root dictionaries
        :rtype: ``osid.dictionary.DictionaryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.DictionaryList

    root_dictionaries = property(fget=get_root_dictionaries)

    def has_parent_dictionaries(self, dictionary_id):
        """Tests if the ``Dictionary`` has any parents.

        :param dictionary_id: a dictionary ``Id``
        :type dictionary_id: ``osid.id.Id``
        :return: ``true`` if the dictionary has parents, f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``dictionary_id`` is not found
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def is_parent_of_dictionary(self, id_, dictionary_id):
        """Tests if an ``Id`` is a direct parent of dictionary.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param dictionary_id: the ``Id`` of a dictionary
        :type dictionary_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``dictionary_id,`` f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``dictionary_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_parent_dictionary_ids(self, dictionary_id):
        """Gets the parent ``Ids`` of the given dictionary.

        :param dictionary_id: a dictionary ``Id``
        :type dictionary_id: ``osid.id.Id``
        :return: the parent Ids of the dictionary
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``dictionary_id`` is not found
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_parent_dictionaries(self, dictionary_id):
        """Gets the parent dictionaries of the given ``id``.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to query
        :type dictionary_id: ``osid.id.Id``
        :return: the parent dictionaries of the ``id``
        :rtype: ``osid.dictionary.DictionaryList``
        :raise: ``NotFound`` -- a ``Dictionary`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.DictionaryList

    def is_ancestor_of_dictionary(self, id_, dictionary_id):
        """Tests if an ``Id`` is an ancestor of a dictionary.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param dictionary_id: the ``Id`` of a dictionary
        :type dictionary_id: ``osid.id.Id``
        :return: ``tru`` e if this ``id`` is an ancestor of ``dictionary_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``dictionary_id`` is not found
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def has_child_dictionaries(self, dictionary_id):
        """Tests if a dictionary has any children.

        :param dictionary_id: a dictionary ``Id``
        :type dictionary_id: ``osid.id.Id``
        :return: ``true`` if the ``dictionary_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``dictionary_id`` is not found
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def is_child_of_dictionary(self, id_, dictionary_id):
        """Tests if a dictionary is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param dictionary_id: the ``Id`` of a dictionary
        :type dictionary_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``dictionary_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``dictionary_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_child_dictionary_ids(self, dictionary_id):
        """Gets the child ``Ids`` of the given dictionary.

        :param dictionary_id: the ``Id`` to query
        :type dictionary_id: ``osid.id.Id``
        :return: the children of the dictionary
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``dictionary_id`` is not found
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_child_dictionaries(self, dictionary_id):
        """Gets the child dictionaries of the given ``id``.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to query
        :type dictionary_id: ``osid.id.Id``
        :return: the child dictionaries of the ``id``
        :rtype: ``osid.dictionary.DictionaryList``
        :raise: ``NotFound`` -- a ``Dictionary`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.DictionaryList

    def is_descendant_of_dictionary(self, id_, dictionary_id):
        """Tests if an ``Id`` is a descendant of a dictionary.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param dictionary_id: the ``Id`` of a dictionary
        :type dictionary_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``dictionary_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``dictionary_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_dictionary_node_ids(self, dictionary_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given dictionary.

        :param dictionary_id: the ``Id`` to query
        :type dictionary_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a dictionary node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``dictionary_id`` is not found
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Node

    def get_dictionary_nodes(self, dictionary_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given dictionary.

        :param dictionary_id: the ``Id`` to query
        :type dictionary_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a dictionary node
        :rtype: ``osid.dictionary.DictionaryNode``
        :raise: ``NotFound`` -- ``dictionary_id`` is not found
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.dictionary.DictionaryNode


class DictionaryHierarchyDesignSession(osid_sessions.OsidSession):
    """This session manages a hierarchy of dictionaries.

    ``Dictionary`` objects may be organized into a hierarchy for
    organizing or federating. A parent ``Dictionary`` includes all of
    the entries of its children such that a single root node contains
    all of the entries of the federation.

    """
    def get_dictionary_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    dictionary_hierarchy_id = property(fget=get_dictionary_hierarchy_id)

    def get_dictionary_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

    dictionary_hierarchy = property(fget=get_dictionary_hierarchy)

    def can_modify_dictionary_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def add_root_dictionary(self, dictionary_id):
        """Adds a root dictionary.

        :param dictionary_id: the ``Id`` of a dicrtionary
        :type dictionary_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``dictionary_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``dictionary_id`` not found
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_root_dictionary(self, dictionary_id):
        """Removes a root dictionary.

        :param dictionary_id: the ``Id`` of a dicrtionary
        :type dictionary_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``dictionary_id`` is not a root
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def add_child_dictionary(self, dictionary_id, child_id):
        """Adds a child to a dictionary.

        :param dictionary_id: the ``Id`` of a dictionary
        :type dictionary_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``dictionary_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``dictionary_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``dictionary_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_child_dictionary(self, dictionary_id, child_id):
        """Removes a child from a dictionary.

        :param dictionary_id: the ``Id`` of a dictionary
        :type dictionary_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``dictionary_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``dictionary_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_child_dictionaries(self, dictionary_id):
        """Removes all children from a dictionary.

        :param dictionary_id: the ``Id`` of a dictionary
        :type dictionary_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``dictionary_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


