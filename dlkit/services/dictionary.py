# -*- coding: utf-8 -*-
"""Dictionary Open Service Interface Definitions
dictionary version 3.0.0

The Dictionary OSID manages key/value pairs. A key and a value may be of
an arbitrary type. Dictionaries may be used to support a Locale or
Configuration OSID, or may be used to provide any dynamic translation or
conversion. The Dictionary OSID is a powerful tool for abstracting and
simplifying applications and other OSID implementations.

Entries

An ``Entry`` is indexed by a key and may contain multiple values of
different types. The key, key type, and value type must be unique. The
interpretation of the value and key are specified through the value type
and key type.

Dictionary

``Entries`` may be organized into federatable ``OsidCatalogs`` called
``Dictionaries``.

Basic Example:
  EntryLookupSession lookupSession = mgr.getEntryLookupSession();
  string definition = (string) lookupSession.getEntry("gambrel", strType, strType);



Federated Example:
  DictionaryLookupSession dictLookupSession = mgr.getDictionaryLookupSession();
  Dictionary dict = dictLookupSession.getDictionary(dict_id);
  EntryLookupSession lookupSession = mgr.getEntryLookupSessionForDictionary(dict);
  JpegImage jpg = lookupSession.getEntry(tiffImage, tiffType, jpegType);



"""
from ..osid import managers as osid_managers
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class DictionaryProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if any dictionary federation is exposed.
        Federation is exposed when a specific dictionary may be
        identified, selected and used to create a lookup or admin
        session. Federation is not exposed when a set of dictionaries
        appears as a single dictionary.

        :return: ``true`` if federation is visible ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_entry_retrieval(self):
        """Tests if retrieving dictionary entries are supported.

        :return: ``true`` if entry retrieval is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_entry_lookup(self):
        """Tests if looking up dictionary entries are supported.

        :return: ``true`` if entry lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_entry_query(self):
        """Tests if querying dictionary entries are supported.

        :return: ``true`` if entry query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_entry_search(self):
        """Tests if searching dictionary entries are supported.

        :return: ``true`` if entry search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_entry_admin(self):
        """Tests if a dictionary entry administrative service is supported.

        :return: ``true`` if dictionary entry administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_entry_notification(self):
        """Tests if a dictionary entry notification service is supported.

        :return: ``true`` if dictionary entry notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_entry_dictionary(self):
        """Tests if retrieving mappings of entry and dictionarys is supported.

        :return: ``true`` if entry dictionary mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_entry_dictionary_assignment(self):
        """Tests if managing mappings of entry and dictionarys is supported.

        :return: ``true`` if entry dictionary assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_entry_smart_dictionary(self):
        """Tests if entry smart dictionarys are available.

        :return: ``true`` if entry smart dictionarys are supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_dictionary_lookup(self):
        """Tests if a dictionary lookup service is supported.

        :return: ``true`` if dictionary lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_dictionary_query(self):
        """Tests if a dictionary query service is supported.

        :return: ``true`` if dictionary query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_dictionary_search(self):
        """Tests if a dictionary search service is supported.

        :return: ``true`` if dictionary search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_dictionary_admin(self):
        """Tests if a dictionary administrative service is supported.

        :return: ``true`` if dictionary administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_dictionary_notification(self):
        """Tests if a dictionary notification service is supported.

        :return: ``true`` if dictionary notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_dictionary_hierachy_traversal(self):
        """Tests if a dictionary hierarchy traversal service is supported.

        :return: ``true`` if dictionary hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_dictionary_hierachy_design(self):
        """Tests if a dictionary hierarchy design service is supported.

        :return: ``true`` if dictionary hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_dictionary_batch(self):
        """Tests if a dictionary batch service is supported.

        :return: ``true`` if dictionary batch service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_entry_key_types(self):
        """Gets the supported ``Entry`` key types.

        :return: a list containing the supported ``Entry`` key types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    entry_key_types = property(fget=get_entry_key_types)

    def supports_entry_key_type(self, entry_key_type):
        """Tests if the given ``Entry`` key type is supported.

        :param entry_key_type: a ``Type`` indicating an ``Entry`` key type
        :type entry_key_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``entry_key_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_entry_value_types(self):
        """Gets the supported ``Entry`` value types.

        :return: a list containing the supported ``Entry`` value types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    entry_value_types = property(fget=get_entry_value_types)

    def supports_entry_value_type(self, entry_value_type):
        """Tests if the given ``Entry`` value type is supported.

        :param entry_value_type: a ``Type`` indicating an ``Entry`` value type
        :type entry_value_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``entry_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_entry_value_types_for_key_type(self, entry_key_type):
        """Gets the list of value types supported for the given key type.

        :param entry_key_type: a ``Type`` indicating an ``Entry`` key type
        :type entry_key_type: ``osid.type.Type``
        :return: a list of value types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``entry_key_type`` is ``null``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_entry_record_types(self):
        """Gets the supported ``Entry`` record types.

        :return: a list containing the supported ``Entry`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    entry_record_types = property(fget=get_entry_record_types)

    def supports_entry_record_type(self, entry_record_type):
        """Tests if the given ``Entry`` record type is supported.

        :param entry_record_type: a ``Type`` indicating an ``Entry`` record type
        :type entry_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``entry_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_entry_search_record_types(self):
        """Gets the supported ``Entry`` search record types.

        :return: a list containing the supported ``Entry`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    entry_search_record_types = property(fget=get_entry_search_record_types)

    def supports_entry_search_record_type(self, entry_search_record_type):
        """Tests if the given ``Entry`` search record type is supported.

        :param entry_search_record_type: a ``Type`` indicating an ``Entry`` search record type
        :type entry_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``entry_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_dictionary_record_types(self):
        """Gets the supported ``Dictionary`` record types.

        :return: a list containing the supported ``Dictionary`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    dictionary_record_types = property(fget=get_dictionary_record_types)

    def supports_dictionary_record_type(self, dictionary_record_type):
        """Tests if the given ``Dictionary`` record type is supported.

        :param dictionary_record_type: a ``Type`` indicating a ``Dictionary`` record type
        :type dictionary_record_type: ``osid.type.Type``
        :return: ``true`` if the given record Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``dictionary_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_dictionary_search_record_types(self):
        """Gets the supported ``Dictionary`` search record types.

        :return: a list containing the supported ``Dictionary`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    dictionary_search_record_types = property(fget=get_dictionary_search_record_types)

    def supports_dictionary_search_record_type(self, dictionary_search_record_type):
        """Tests if the given ``Dictionary`` search record type is supported.

        :param dictionary_search_record_type: a ``Type`` indicating a ``Dictionary`` search record type
        :type dictionary_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``dictionary_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class DictionaryManager(osid_managers.OsidManager, osid_sessions.OsidSession, DictionaryProfile):

    def get_entry_retrieval_session(self):
        """Gets the ``OsidSession`` used to retrieve dictionary entries.

        :return: the new ``EntryRetrievalSession``
        :rtype: ``osid.dictionary.EntryRetrievalSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_retrieval()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_entry_lookup_session(self):
        """Gets the ``OsidSession`` used to retrieve dictionary entries.

        :return: an ``EntryLookupSession``
        :rtype: ``osid.dictionary.EntryLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_entry_query_session(self):
        """Gets the ``OsidSession`` used to query dictionary entries.

        :return: an ``EntryQuerySession``
        :rtype: ``osid.dictionary.EntryQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_entry_search_session(self):
        """Gets the ``OsidSession`` used to search dictionary entries.

        :return: an ``EntrySearchSession``
        :rtype: ``osid.dictionary.EntrySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_entry_admin_session(self):
        """Gets the ``OsidSession`` used to administer dictionary entries.

        :return: an ``EntryAdminSession``
        :rtype: ``osid.dictionary.EntryAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_entry_dictionary_session(self):
        """Gets the session for retrieving entry to dictionary mappings.

        :return: a ``EntryDictionarySession``
        :rtype: ``osid.dictionary.EntryDictionarySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_dictionary()`` is ``false``

        """
        raise UNIMPLEMENTED()

    entry_dictionary_session = property(fget=get_entry_dictionary_session)

    def get_entry_dictionary_assignment_session(self):
        """Gets the session for assigning entry to dictionary mappings.

        :return: a ``EntryDictionaryAssignmentSession``
        :rtype: ``osid.dictionary.EntryDictionaryAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_entry_dictionary_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_dictionary_lookup_session(self):
        """Gets the ``OsidSession`` used to lookup dictionaries.

        :return: a ``DictionaryLookupSession``
        :rtype: ``osid.dictionary.DictionaryLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    dictionary_lookup_session = property(fget=get_dictionary_lookup_session)

    def get_dictionary_query_session(self):
        """Gets the ``OsidSession`` used to query dictionaries.

        :return: a ``DictionaryQuerySession``
        :rtype: ``osid.dictionary.DictionaryQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    dictionary_query_session = property(fget=get_dictionary_query_session)

    def get_dictionary_search_session(self):
        """Gets the ``OsidSession`` used to search dictionaries.

        :return: a ``DictionarySearchSession``
        :rtype: ``osid.dictionary.DictionarySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    dictionary_search_session = property(fget=get_dictionary_search_session)

    def get_dictionary_admin_session(self):
        """Gets the ``OsidSession`` used to administer dictionaries.

        :return: a ``DictionaryAdminSession``
        :rtype: ``osid.dictionary.DictionaryAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_dictionary_hierarchy_session(self):
        """Gets hierarchy service for traversing the ``Dictionary`` hierarchy.
        A parent includes all the dictionary entries of its children.

        :return: a Dictionary ``HierarchySession``
        :rtype: ``osid.dictionary.DictionaryHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_hierarchy_traversal()`` is ``false``

        """
        raise UNIMPLEMENTED()

    dictionary_hierarchy_session = property(fget=get_dictionary_hierarchy_session)

    def get_dictionary_hierarchy_design_session(self):
        """Gets hierarchy service for structuring ``Dictionary`` objects.

        :return: a ``DictionaryHierarchyDesignSession``
        :rtype: ``osid.dictionary.DictionaryHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    dictionary_hierarchy_design_session = property(fget=get_dictionary_hierarchy_design_session)

    def get_dictionary_batch_manager(self):
        """Gets a ``DictionaryBatchManager``.

        :return: a ``DictionaryBatchManager``
        :rtype: ``osid.dictionary.batch.DictionaryBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    dictionary_batch_manager = property(fget=get_dictionary_batch_manager)


##
# The following methods are from osid.dictionary.DictionaryLookupSession

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
        raise UNIMPLEMENTED()

    def use_comparative_dictionary_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_dictionary_view(self):
        """A complete view of the ``Dictionary`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    dictionaries = property(fget=get_dictionaries)


##
# The following methods are from osid.dictionary.DictionaryQuerySession

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
        raise UNIMPLEMENTED()

    def get_dictionary_query(self):
        """Gets a dictionary query.

        :return: the dictionary query
        :rtype: ``osid.dictionary.DictionaryQuery``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.DictionarySearchSession

    def get_dictionary_search(self):
        """Gets a dictionary search.

        :return: the dictionary search
        :rtype: ``osid.dictionary.DictionarySearch``

        """
        raise UNIMPLEMENTED()

    dictionary_search = property(fget=get_dictionary_search)

    def get_dictionary_search_order(self):
        """Gets a dictionary search order.
        The ``DictionarySearchOrder`` is supplied to a
        ``DictionarySearch`` to specify the ordering of results.

        :return: the dictionary search order
        :rtype: ``osid.dictionary.DictionarySearchOrder``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.DictionaryAdminSession

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def delete_dictionary(self, dictionary_id):
        """Deletes a ``Dictionary``.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to delete
        :type dictionary_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``dictionary_id`` not found
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.DictionaryNotificationSession

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
        raise UNIMPLEMENTED()

    def register_for_new_dictionaries(self):
        """Register for notifications of new dictionaries.
        ``DictionaryReceiver.newDictionary()`` is invoked when a new
        ``Dictionary`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def register_for_changed_dictionaries(self):
        """Registers for notification of updated dictionaries.
        ``DictionaryReceiver.changedDictionary()`` is invoked when a
        dictionary is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def register_for_deleted_dictionaries(self):
        """Registers for notification of deleted dictionaries.
        ``DictionaryReceiver.deletedDictionary()`` is invoked when a
        dictionary is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.DictionaryHierarchySession

    def get_dictionary_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    dictionary_hierarchy_id = property(fget=get_dictionary_hierarchy_id)

    def get_dictionary_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_root_dictionary_ids(self):
        """Gets the root dictionary ``Ids`` in this hierarchy.

        :return: the root dictionary ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.DictionaryHierarchyDesignSession

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def remove_root_dictionary(self, dictionary_id):
        """Removes a root dictionary.

        :param dictionary_id: the ``Id`` of a dicrtionary
        :type dictionary_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``dictionary_id`` is not a root
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def remove_child_dictionaries(self, dictionary_id):
        """Removes all children from a dictionary.

        :param dictionary_id: the ``Id`` of a dictionary
        :type dictionary_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``dictionary_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class DictionaryProxyManager(osid_managers.OsidProxyManager, DictionaryProfile):

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_dictionary_batch_proxy_manager(self):
        """Gets a ``DictionaryBatchProxyManager``.

        :return: a ``DictionaryBatchProxyManager``
        :rtype: ``osid.dictionary.batch.DictionaryBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_dictionary_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    dictionary_batch_proxy_manager = property(fget=get_dictionary_batch_proxy_manager)


##
# The following methods are from osid.dictionary.DictionaryLookupSession

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
        raise UNIMPLEMENTED()

    def use_comparative_dictionary_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.




        """
        raise UNIMPLEMENTED()

    def use_plenary_dictionary_view(self):
        """A complete view of the ``Dictionary`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.




        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    dictionaries = property(fget=get_dictionaries)


##
# The following methods are from osid.dictionary.DictionaryQuerySession

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
        raise UNIMPLEMENTED()

    def get_dictionary_query(self):
        """Gets a dictionary query.

        :return: the dictionary query
        :rtype: ``osid.dictionary.DictionaryQuery``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.DictionarySearchSession

    def get_dictionary_search(self):
        """Gets a dictionary search.

        :return: the dictionary search
        :rtype: ``osid.dictionary.DictionarySearch``

        """
        raise UNIMPLEMENTED()

    dictionary_search = property(fget=get_dictionary_search)

    def get_dictionary_search_order(self):
        """Gets a dictionary search order.
        The ``DictionarySearchOrder`` is supplied to a
        ``DictionarySearch`` to specify the ordering of results.


        :return: the dictionary search order
        :rtype: ``osid.dictionary.DictionarySearchOrder``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.DictionaryAdminSession

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def delete_dictionary(self, dictionary_id):
        """Deletes a ``Dictionary``.

        :param dictionary_id: the ``Id`` of the ``Dictionary`` to delete
        :type dictionary_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``dictionary_id`` not found
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.DictionaryNotificationSession

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
        raise UNIMPLEMENTED()

    def register_for_new_dictionaries(self):
        """Register for notifications of new dictionaries.
        ``DictionaryReceiver.newDictionary()`` is invoked when a new
        ``Dictionary`` is created.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def register_for_changed_dictionaries(self):
        """Registers for notification of updated dictionaries.
        ``DictionaryReceiver.changedDictionary()`` is invoked when a
        dictionary is changed.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def register_for_deleted_dictionaries(self):
        """Registers for notification of deleted dictionaries.
        ``DictionaryReceiver.deletedDictionary()`` is invoked when a
        dictionary is deleted.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.DictionaryHierarchySession

    def get_dictionary_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    dictionary_hierarchy_id = property(fget=get_dictionary_hierarchy_id)

    def get_dictionary_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_root_dictionary_ids(self):
        """Gets the root dictionary ``Ids`` in this hierarchy.

        :return: the root dictionary ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.DictionaryHierarchyDesignSession

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def remove_root_dictionary(self, dictionary_id):
        """Removes a root dictionary.

        :param dictionary_id: the ``Id`` of a dicrtionary
        :type dictionary_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``dictionary_id`` is not a root
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def remove_child_dictionaries(self, dictionary_id):
        """Removes all children from a dictionary.

        :param dictionary_id: the ``Id`` of a dictionary
        :type dictionary_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``dictionary_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class Dictionary(osid_objects.OsidCatalog, osid_sessions.OsidSession):

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.EntryRetrievalSession

    def get_dictionary_id(self):
        """Gets the ``Dictionary``  ``Id`` associated with this session.

        :return: the ``Dictionary``  ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    dictionary_id = property(fget=get_dictionary_id)

    def get_dictionary(self):
        """Gets the ``Dictionary`` associated with this session.

        :return: the ``Dictionary`` associated with this session
        :rtype: ``osid.dictionary.Dictionary``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def use_federated_dictionary_view(self):
        """Federates the view for methods in this session.
        A federated view will include entries from descendant
        dictionaries in the dictionary hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_dictionary_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this dictionary only.



        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.EntryLookupSession

    def use_comparative_entry_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_entry_view(self):
        """A complete view of the ``Entry`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    entries = property(fget=get_entries)


##
# The following methods are from osid.dictionary.EntryQuerySession

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
        raise UNIMPLEMENTED()

    def get_entry_query(self):
        """Gets an entry query.

        :return: the entry query
        :rtype: ``osid.dictionary.EntryQuery``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.EntrySearchSession

    def get_entry_search(self):
        """Gets an entry search.

        :return: the entry search
        :rtype: ``osid.dictionary.EntrySearch``

        """
        raise UNIMPLEMENTED()

    entry_search = property(fget=get_entry_search)

    def get_entry_search_order(self):
        """Gets an entry search order.
        The ``EntrySearchOrder`` is supplied to a ``EntrySearch`` to
        specify the ordering of results.

        :return: the entry search order
        :rtype: ``osid.dictionary.EntrySearchOrder``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.EntryAdminSession

    def can_create_entries(self):
        """Tests if this user can create entries A return of true does not guarantee successful authorization.
        A return of false indicates that it is known creating an
        ``Entry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if entry creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def delete_entry(self, entry_id):
        """Updates an existing ``Dictionary`` entry identified with the specified key with the given value.

        :param entry_id: the ``Id`` of the entry
        :type entry_id: ``osid.id.Id``
        :raise: ``NotFound`` -- entry is not found
        :raise: ``NullArgument`` -- ``entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.EntryNotificationSession

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
        raise UNIMPLEMENTED()

    def register_for_new_entries(self):
        """Registers for notifications of new entries.
        ``EntryReceiver.newEntry(key, keyType)`` is invoked when a new
        ``Entry`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def register_for_changed_entries(self):
        """Regsiters for notification of updated entries.
        ``EntryReceiver.changedEntry(key, keyType)`` is invoked when an
        ``Entry`` is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def register_for_deleted_entries(self):
        """Registers for notification of deleted dictionaries.
        ``EntryReceiver.deletedEntry(key, keyType)`` is invoked when the
        specified ``Entry`` is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.EntryDictionarySession

    def use_comparative_dictionary_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_dictionary_view(self):
        """A complete view of the ``Entry`` and ``Dictionary`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.EntryDictionaryAssignmentSession

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_assignable_dictionary_ids(self, dictionary_id):
        """Gets a list of dictionaries including and under the given dictionary node in which any entry can be assigned.

        :param dictionary_id: the ``Id`` of the ``Dictionary``
        :type dictionary_id: ``osid.id.Id``
        :return: list of assignable dictionary ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``dictionary_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.dictionary.EntrySmartDictionarySession

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
        raise UNIMPLEMENTED()

    def apply_entry_query(self, entry_query):
        """Applies a entry query to this dictionary.

        :param entry_query: the entry query
        :type entry_query: ``osid.dictionary.EntryQuery``
        :raise: ``NullArgument`` -- ``entry_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``entry_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_entry_query(self):
        """Gets a entry query inspector for this dictionary.

        :return: the entry query inspector
        :rtype: ``osid.dictionary.EntryQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_entry_sequencing(self, entry_search_order):
        """Applies a entry search order to this dictionary.

        :param entry_search_order: the entry search order
        :type entry_search_order: ``osid.dictionary.EntrySearchOrder``
        :raise: ``NullArgument`` -- ``entry_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``entry_search_order`` not of this service

        """
        raise UNIMPLEMENTED()



class DictionaryList(osid_objects.OsidList):

    def get_next_dictionary(self):
        """Gets the next ``Dictionary`` in this list.

        :return: the next ``Dictionary`` in this list. The ``has_next()`` method should be used to test that a next ``Dictionary`` is available before calling this method.
        :rtype: ``osid.dictionary.Dictionary``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()



class Dictionarys(DictionaryManager):
    pass


