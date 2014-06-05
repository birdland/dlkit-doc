from ..osid import managers as osid_managers


class JournalingProfile(osid_managers.OsidProfile):
    """The journaling profile describes the interoperability among journaling services."""
    def supports_visible_federation(self):
        """Tests if any journal federation is exposed.

        Federation is exposed when a specific journal may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of journals appears as a
        single journal.

        :return: ``true`` if visible federation is supproted, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_journal_entry_lookup(self):
        """Tests for the availability of a journal entry lookup service.

        :return: ``true`` if journal entry lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_journal_entry_query(self):
        """Tests if querying journal entries is available.

        :return: ``true`` if journal entry query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_journal_entry_search(self):
        """Tests if searching for journal entries is available.

        :return: ``true`` if journal entry search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_journal_entry_admin(self):
        """Tests if searching for journal entries is available.

        :return: ``true`` if journal entry search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_journal_entry_notification(self):
        """Tests if journal entry notification is available.

        :return: ``true`` if journal entry notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_branch_lookup(self):
        """Tests if branch lookup is supported.

        :return: ``true`` if branch lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_branch_query(self):
        """Tests if branch query is supported.

        :return: ``true`` if branch query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_branch_search(self):
        """Tests if branch search is supported.

        :return: ``true`` if branch search is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_branch_admin(self):
        """Tests if branch administration is supported.

        :return: ``true`` if branch administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_branch_notification(self):
        """Tests if branch notification is supported.

        Messages may be sent when branches are created, modified, or
        deleted.

        :return: ``true`` if branch notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_branch_smart_journal(self):
        """Tests if branch smart journals are available.

        :return: ``true`` if branch smart journals are supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_journal_lookup(self):
        """Tests for the availability of an journal lookup service.

        :return: ``true`` if journal lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_journal_query(self):
        """Tests if querying journals is available.

        :return: ``true`` if journal query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_journal_search(self):
        """Tests if searching for journals is available.

        :return: ``true`` if journal search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_journal_admin(self):
        """Tests for the availability of a journal administrative service for creating and deleting journals.

        :return: ``true`` if journal administration is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_journal_notification(self):
        """Tests for the availability of a journal notification service.

        :return: ``true`` if journal notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_journal_hierarchy(self):
        """Tests for the availability of a journal hierarchy traversal service.

        :return: ``true`` if journal hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_journal_hierarchy_design(self):
        """Tests for the availability of a journal hierarchy design service.

        :return: ``true`` if journal hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_journalng_batch(self):
        """Tests for the availability of a journaling batch service.

        :return: ``true`` if journaling batch service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_journal_entry_record_types(self):
        """Gets the supported ``JournalEntry`` record types.

        :return: a list containing the supported journal entry record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    journal_entry_record_types = property(fget=get_journal_entry_record_types)

    def supports_journal_entry_record_type(self, journal_entry_record_type):
        """Tests if the given ``JournalEntry`` record type is supported.

        :param journal_entry_record_type: a ``Type`` indicating a ``JournalEntry`` record type
        :type journal_entry_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``journal_entry_record_type`` is ``null``

        """
        return # boolean

    def get_journal_entry_search_record_types(self):
        """Gets the supported journal entry search record types.

        :return: a list containing the supported journal entry search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    journal_entry_search_record_types = property(fget=get_journal_entry_search_record_types)

    def supports_journal_entry_search_record_type(self, journal_entry_search_record_type):
        """Tests if the given journal entry search record type is supported.

        :param journal_entry_search_record_type: a ``Type`` indicating a journal entry record type
        :type journal_entry_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``journal_entry_search_record_type`` is ``null``

        """
        return # boolean

    def get_branch_record_types(self):
        """Gets all the branch record types supported.

        :return: the list of supported branch record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    branch_record_types = property(fget=get_branch_record_types)

    def supports_branch_record_type(self, branch_record_type):
        """Tests if a given branch record type is supported.

        :param branch_record_type: the branch type
        :type branch_record_type: ``osid.type.Type``
        :return: ``true`` if the branch record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``branch_record_type`` is ``null``

        """
        return # boolean

    def get_branch_search_record_types(self):
        """Gets all the branch search record types supported.

        :return: the list of supported branch search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    branch_search_record_types = property(fget=get_branch_search_record_types)

    def supports_branch_search_record_type(self, branch_search_record_type):
        """Tests if a given branch search type is supported.

        :param branch_search_record_type: the branch search type
        :type branch_search_record_type: ``osid.type.Type``
        :return: ``true`` if the branch search record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``branch_search_record_type`` is ``null``

        """
        return # boolean

    def get_journal_record_types(self):
        """Gets the supported ``Journal`` record types.

        :return: a list containing the supported journal record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    journal_record_types = property(fget=get_journal_record_types)

    def supports_journal_record_type(self, journal_record_type):
        """Tests if the given ``Journal`` record type is supported.

        :param journal_record_type: a ``Type`` indicating a ``Journal`` record type
        :type journal_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``journal_record_type`` is ``null``

        """
        return # boolean

    def get_journal_search_record_types(self):
        """Gets the supported journal search record types.

        :return: a list containing the supported journal search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    journal_search_record_types = property(fget=get_journal_search_record_types)

    def supports_journal_search_record_type(self, journal_search_record_type):
        """Tests if the given journal search record type is supported.

        :param journal_search_record_type: a ``Type`` indicating a journal record type
        :type journal_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``journal_entry_search_record_type`` is ``null``

        """
        return # boolean


class JournalingManager(osid_managers.OsidManager, JournalingProfile):
    """The journaling manager provides access to journaling sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``JournalEntryLookupSession:`` a session to lookup journal
        entries
      * ``JournalEntryQuerySession:`` a session to query journal entries
      * ``JournalEntrySearchSession:`` a session to search journal
        entries
      * ``JournalEntryAdminSession:`` a session to manage journal
        entries
      * ``JournalEntryNotificationSession:`` a session to subscribe to
        notifications of journal entry changes
    
      * ``BranchLookupSession:`` a session to retrieve branches
      * ``BranchQuerySession:`` a session to query branches
      * ``BranchSearchSession:`` a session to search for branches
      * ``BranchAdminSession:`` a session to create and delete brancehs
      * ``BranchNotificationSession:`` a session to receive
        notifications pertaining to branch changes
      * ``BranchSmartJournalSession:`` a session to manage smart branch
        journals
    
      * ``JournalLookupSession:`` a session to retrieve journals
      * ``JournalQuerySession`` : a session to query journals
      * ``JournalSearchSession:`` a session to search for journals
      * ``JournalAdminSession:`` a session to create, update and delete
        journals
      * ``JournalNotificationSession:`` a session to receive
        notifications for changes in journals
      * ``JournalHierarchyTraversalSession:`` a session to traverse
        hierarchies of journals
      * ``JournalHierarchyDesignSession:`` a session to manage
        hierarchies of journals

    
    The journaling manager also provides a profile for determing the
    supported search types supported by this service.

    """
    def get_journal_entry_lookup_session(self):
        """Gets the ``OsidSession`` associated with the journal entry lookup service.

        :return: a ``JournalEntryLookupSession``
        :rtype: ``osid.journaling.JournalEntryLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_lookup()`` is ``false``

        """
        return # osid.journaling.JournalEntryLookupSession

    journal_entry_lookup_session = property(fget=get_journal_entry_lookup_session)

    def get_journal_entry_lookup_session_for_journal(self, journal_id):
        """Gets the ``OsidSession`` associated with the journal entry lookup service for the given journal.

        :param journal_id: the ``Id`` of the ``Journal``
        :type journal_id: ``osid.id.Id``
        :return: a ``JournalEntryLookupSession``
        :rtype: ``osid.journaling.JournalEntryLookupSession``
        :raise: ``NotFound`` -- no ``Journal`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.JournalEntryLookupSession

    def get_journal_entry_query_session(self):
        """Gets the ``OsidSession`` associated with the journal entry query service.

        :return: a ``JournalEntryQuerySession``
        :rtype: ``osid.journaling.JournalEntryQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_query()`` is ``false``

        """
        return # osid.journaling.JournalEntryQuerySession

    journal_entry_query_session = property(fget=get_journal_entry_query_session)

    def get_journal_entry_query_session_for_journal(self, journal_id):
        """Gets the ``OsidSession`` associated with the journal entry query service for the given journal.

        :param journal_id: the ``Id`` of the ``Journal``
        :type journal_id: ``osid.id.Id``
        :return: a ``JournalEntryQuerySession``
        :rtype: ``osid.journaling.JournalEntryQuerySession``
        :raise: ``NotFound`` -- no ``Journal`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.JournalEntryQuerySession

    def get_journal_entry_search_session(self):
        """Gets the ``OsidSession`` associated with the journal entry search service.

        :return: a ``JournalEntrySearchSession``
        :rtype: ``osid.journaling.JournalEntrySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_search()`` is ``false``

        """
        return # osid.journaling.JournalEntrySearchSession

    journal_entry_search_session = property(fget=get_journal_entry_search_session)

    def get_journal_entry_search_session_for_journal(self, journal_id):
        """Gets the ``OsidSession`` associated with the journal entry search service for the given journal.

        :param journal_id: the ``Id`` of the ``Journal``
        :type journal_id: ``osid.id.Id``
        :return: a ``JournalEntrySearchSession``
        :rtype: ``osid.journaling.JournalEntrySearchSession``
        :raise: ``NotFound`` -- no ``Journal`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.JournalEntrySearchSession

    def get_journal_entry_admin_session(self):
        """Gets the ``OsidSession`` associated with the journal entry administration service.

        :return: a ``JournalEntryAdminSession``
        :rtype: ``osid.journaling.JournalEntryAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_admin()`` is ``false``

        """
        return # osid.journaling.JournalEntryAdminSession

    journal_entry_admin_session = property(fget=get_journal_entry_admin_session)

    def get_journal_entry_admin_session_for_journal(self, journal_id):
        """Gets the ``OsidSession`` associated with the journal entry administration service for the given journal.

        :param journal_id: the ``Id`` of the ``Journal``
        :type journal_id: ``osid.id.Id``
        :return: a ``JournalEntryAdminSession``
        :rtype: ``osid.journaling.JournalEntryAdminSession``
        :raise: ``NotFound`` -- no ``Journal`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.JournalEntryAdminSession

    def get_journal_entry_notification_session(self, journal_entry_receiver):
        """Gets the ``OsidSession`` associated with the journal entry notification service.

        :param journal_entry_receiver: the receiver
        :type journal_entry_receiver: ``osid.journaling.JournalEntryReceiver``
        :return: a ``JournalEntryNotificationSession``
        :rtype: ``osid.journaling.JournalEntryNotificationSession``
        :raise: ``NullArgument`` -- ``journal_entry_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_notification()`` is ``false``

        """
        return # osid.journaling.JournalEntryNotificationSession

    def get_journal_entry_notification_session_for_journal(self, journal_entry_receiver, journal_id):
        """Gets the ``OsidSession`` associated with the journal entry notification service for the given journal.

        :param journal_entry_receiver: the receiver
        :type journal_entry_receiver: ``osid.journaling.JournalEntryReceiver``
        :param journal_id: the ``Id`` of the ``Journal``
        :type journal_id: ``osid.id.Id``
        :return: a ``JournalEntryNotificationSession``
        :rtype: ``osid.journaling.JournalEntryNotificationSession``
        :raise: ``NotFound`` -- no ``Journal`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``journal_entry_receiver`` or ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.JournalEntryNotificationSession

    def get_branch_lookup_session(self):
        """Gets the ``OsidSession`` associated with the branch lookup service.

        :return: ``a BranchLookupSession``
        :rtype: ``osid.journaling.BranchLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_lookup()`` is ``false``

        """
        return # osid.journaling.BranchLookupSession

    branch_lookup_session = property(fget=get_branch_lookup_session)

    def get_branch_lookup_session_for_journal(self, journal_id):
        """Gets the ``OsidSession`` associated with the branch lookup service for the given journal.

        :param journal_id: the ``Id`` of the journal
        :type journal_id: ``osid.id.Id``
        :return: ``a BranchLookupSession``
        :rtype: ``osid.journaling.BranchLookupSession``
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_branch_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.BranchLookupSession

    def get_branch_query_session(self):
        """Gets a branch query session.

        :return: ``a BranchQuerySession``
        :rtype: ``osid.journaling.BranchQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_query()`` is ``false``

        """
        return # osid.journaling.BranchQuerySession

    branch_query_session = property(fget=get_branch_query_session)

    def get_branch_query_session_for_journal(self, journal_id):
        """Gets a branch query session for the given journal.

        :param journal_id: the ``Id`` of the journal
        :type journal_id: ``osid.id.Id``
        :return: ``a BranchQuerySession``
        :rtype: ``osid.journaling.BranchQuerySession``
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_branch_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.BranchQuerySession

    def get_branch_search_session(self):
        """Gets a branch search session.

        :return: ``a BranchSearchSession``
        :rtype: ``osid.journaling.BranchSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_search()`` is ``false``

        """
        return # osid.journaling.BranchSearchSession

    branch_search_session = property(fget=get_branch_search_session)

    def get_branch_search_session_for_journal(self, journal_id):
        """Gets a branch search session for the given journal.

        :param journal_id: the ``Id`` of the journal
        :type journal_id: ``osid.id.Id``
        :return: ``a BranchSearchSession``
        :rtype: ``osid.journaling.BranchSearchSession``
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_branch_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.BranchSearchSession

    def get_branch_admin_session(self):
        """Gets a branch administration session for creating, updating and deleting branches.

        :return: ``a BranchAdminSession``
        :rtype: ``osid.journaling.BranchAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_admin()`` is ``false``

        """
        return # osid.journaling.BranchAdminSession

    branch_admin_session = property(fget=get_branch_admin_session)

    def get_branch_admin_session_for_journal(self, journal_id):
        """Gets a branch administration session for the given journal.

        :param journal_id: the ``Id`` of the journal
        :type journal_id: ``osid.id.Id``
        :return: ``a BranchAdminSession``
        :rtype: ``osid.journaling.BranchAdminSession``
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.BranchAdminSession

    def get_branch_notification_session(self, branch_receiver):
        """Gets the notification session for notifications pertaining to branch changes.

        :param branch_receiver: the notification callback
        :type branch_receiver: ``osid.journaling.BranchReceiver``
        :return: ``a BranchNotificationSession``
        :rtype: ``osid.journaling.BranchNotificationSession``
        :raise: ``NullArgument`` -- ``branch_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_notification()`` is ``false``

        """
        return # osid.journaling.BranchNotificationSession

    def get_branch_notification_session_for_journal(self, branch_receiver, journal_id):
        """Gets the branch notification session for the given journal.

        :param branch_receiver: the notification callback
        :type branch_receiver: ``osid.journaling.BranchReceiver``
        :param journal_id: the ``Id`` of the journal
        :type journal_id: ``osid.id.Id``
        :return: ``a BranchNotificationSession``
        :rtype: ``osid.journaling.BranchNotificationSession``
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``branch_receiver`` or ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_branch_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.BranchNotificationSession

    def get_branch_smart_journal_session(self, journal_id):
        """Gets the session for managing dynamic branch journals.

        :param journal_id: the ``Id`` of the journal
        :type journal_id: ``osid.id.Id``
        :return: a ``BranchSmartJournalSession``
        :rtype: ``osid.journaling.BranchSmartJournalSession``
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_smart_journal()`` is ``false``

        """
        return # osid.journaling.BranchSmartJournalSession

    def get_journal_lookup_session(self):
        """Gets the ``OsidSession`` associated with the journal lookup service.

        :return: a ``JournalLookupSession``
        :rtype: ``osid.journaling.JournalLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_lookup()`` is ``false``

        """
        return # osid.journaling.JournalLookupSession

    journal_lookup_session = property(fget=get_journal_lookup_session)

    def get_journal_query_session(self):
        """Gets the ``OsidSession`` associated with the journal query service.

        :return: a ``JournalQuerySession``
        :rtype: ``osid.journaling.JournalQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_query()`` is ``false``

        """
        return # osid.journaling.JournalQuerySession

    journal_query_session = property(fget=get_journal_query_session)

    def get_journal_search_session(self):
        """Gets the ``OsidSession`` associated with the journal search service.

        :return: a ``JournalSearchSession``
        :rtype: ``osid.journaling.JournalSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_search()`` is ``false``

        """
        return # osid.journaling.JournalSearchSession

    journal_search_session = property(fget=get_journal_search_session)

    def get_journal_admin_session(self):
        """Gets the ``OsidSession`` associated with the journal administrative service.

        :return: a ``JournalAdminSession``
        :rtype: ``osid.journaling.JournalAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_admin()`` is ``false``

        """
        return # osid.journaling.JournalAdminSession

    journal_admin_session = property(fget=get_journal_admin_session)

    def get_journal_notification_session(self, journal_receiver):
        """Gets the ``OsidSession`` associated with the journal notification service.

        :param journal_receiver: the receiver
        :type journal_receiver: ``osid.journaling.JournalReceiver``
        :return: a ``JournalNotificationSession``
        :rtype: ``osid.journaling.JournalNotificationSession``
        :raise: ``NullArgument`` -- ``journal_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_notification()`` is ``false``

        """
        return # osid.journaling.JournalNotificationSession

    def get_journal_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the journal hierarchy service.

        :return: a ``JournalHierarchySession``
        :rtype: ``osid.journaling.JournalHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_hierarchy()`` is ``false``

        """
        return # osid.journaling.JournalHierarchySession

    journal_hierarchy_session = property(fget=get_journal_hierarchy_session)

    def get_journal_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the journal hierarchy design service.

        :return: a ``JournalHierarchyDesignSession``
        :rtype: ``osid.journaling.JournalHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_hierarchy_design()`` is ``false``

        """
        return # osid.journaling.JournalHierarchyDesignSession

    journal_hierarchy_design_session = property(fget=get_journal_hierarchy_design_session)

    def get_journaling_batch_manager(self):
        """Gets a ``JournalingBatchManager``.

        :return: a ``JournalingBatchManager``
        :rtype: ``osid.journaling.batch.JournalingBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journaling_batch()`` is ``false``

        """
        return # osid.journaling.batch.JournalingBatchManager

    journaling_batch_manager = property(fget=get_journaling_batch_manager)


class JournalingProxyManager(osid_managers.OsidProxyManager, JournalingProfile):
    """The journaling manager provides access to journaling sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager accept a ``Proxy`` for passing information
    from a server environment. The sessions included in this manager
    are:

      * ``JournalEntryLookupSession:`` a session to lookup journal
        entries
      * ``JournalEntryQuerySession:`` a session to query journal entries
      * ``JournalEntrySearchSession:`` a session to search journal
        entries
      * ``JournalEntryAdminSession:`` a session to manage journal
        entries
      * ``JournalEntryNotificationSession:`` a session to subscribe to
        notifications of journal entry changes
    
      * ``BranchLookupSession:`` a session to retrieve branches
      * ``BranchQuerySession:`` a session to query branches
      * ``BranchSearchSession:`` a session to search for branches
      * ``BranchAdminSession:`` a session to create and delete brancehs
      * ``BranchNotificationSession:`` a session to receive
        notifications pertaining to branch changes
      * ``BranchSmartJournalSession:`` a session to manage smart branch
        journals
    
      * ``JournalLookupSession:`` a session to retrieve journals
      * ``JournalQuerySession`` : a session to query journals
      * ``JournalSearchSession:`` a session to search for journals
      * ``JournalAdminSession:`` a session to create, update and delete
        journals
      * ``JournalNotificationSession:`` a session to receive
        notifications for changes in journals
      * ``JournalHierarchyTraversalSession:`` a session to traverse
        hierarchies of journals
      * ``JournalHierarchyDesignSession:`` a session to manage
        hierarchies of journals

    
    The journaling manager also provides a profile for determing the
    supported search types supported by this service.

    """
    def get_journal_entry_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the journal entry lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``JournalEntryLookupSession``
        :rtype: ``osid.journaling.JournalEntryLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_lookup()`` is ``false``

        """
        return # osid.journaling.JournalEntryLookupSession

    def get_journal_entry_lookup_session_for_journal(self, journal_id, proxy):
        """Gets the ``OsidSession`` associated with the journal entry lookup service for the given journal.

        :param journal_id: the ``Id`` of the ``Journal``
        :type journal_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``JournalEntryLookupSession``
        :rtype: ``osid.journaling.JournalEntryLookupSession``
        :raise: ``NotFound`` -- no ``Journal`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``journal_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.JournalEntryLookupSession

    def get_journal_entry_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the journal entry query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``JournalEntryQuerySession``
        :rtype: ``osid.journaling.JournalEntryQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_query()`` is ``false``

        """
        return # osid.journaling.JournalEntryQuerySession

    def get_journal_entry_query_session_for_journal(self, journal_id, proxy):
        """Gets the ``OsidSession`` associated with the journal entry query service for the given journal.

        :param journal_id: the ``Id`` of the ``Journal``
        :type journal_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``JournalEntryQuerySession``
        :rtype: ``osid.journaling.JournalEntryQuerySession``
        :raise: ``NotFound`` -- no ``Journal`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``journal_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.JournalEntryQuerySession

    def get_journal_entry_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the journal entry search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``JournalEntrySearchSession``
        :rtype: ``osid.journaling.JournalEntrySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_search()`` is ``false``

        """
        return # osid.journaling.JournalEntrySearchSession

    def get_journal_entry_search_session_for_journal(self, journal_id, proxy):
        """Gets the ``OsidSession`` associated with the journal entry search service for the given journal.

        :param journal_id: the ``Id`` of the ``Journal``
        :type journal_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``JournalEntrySearchSession``
        :rtype: ``osid.journaling.JournalEntrySearchSession``
        :raise: ``NotFound`` -- no ``Journal`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``journal_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.JournalEntrySearchSession

    def get_journal_entry_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the journal entry administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``JournalEntryAdminSession``
        :rtype: ``osid.journaling.JournalEntryAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_admin()`` is ``false``

        """
        return # osid.journaling.JournalEntryAdminSession

    def get_journal_entry_admin_session_for_journal(self, journal_id, proxy):
        """Gets the ``OsidSession`` associated with the journal entry administration service for the given journal.

        :param journal_id: the ``Id`` of the ``Journal``
        :type journal_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``JournalEntryAdminSession``
        :rtype: ``osid.journaling.JournalEntryAdminSession``
        :raise: ``NotFound`` -- no ``Journal`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``journal_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.JournalEntryAdminSession

    def get_journal_entry_notification_session(self, journal_entry_receiver, proxy):
        """Gets the ``OsidSession`` associated with the journal entry notification service.

        :param journal_entry_receiver: the receiver
        :type journal_entry_receiver: ``osid.journaling.JournalEntryReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``JournalEntryNotificationSession``
        :rtype: ``osid.journaling.JournalEntryNotificationSession``
        :raise: ``NullArgument`` -- ``journal_entry_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_notification()`` is ``false``

        """
        return # osid.journaling.JournalEntryNotificationSession

    def get_journal_entry_notification_session_for_journal(self, journal_entry_receiver, journal_id, proxy):
        """Gets the ``OsidSession`` associated with the journal entry notification service for the given journal.

        :param journal_entry_receiver: the receiver
        :type journal_entry_receiver: ``osid.journaling.JournalEntryReceiver``
        :param journal_id: the ``Id`` of the ``Journal``
        :type journal_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``JournalEntryNotificationSession``
        :rtype: ``osid.journaling.JournalEntryNotificationSession``
        :raise: ``NotFound`` -- no ``Journal`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``journal_entry_receiver, journal_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.JournalEntryNotificationSession

    def get_branch_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the branch lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a BranchLookupSession``
        :rtype: ``osid.journaling.BranchLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_lookup()`` is ``false``

        """
        return # osid.journaling.BranchLookupSession

    def get_branch_lookup_session_for_journal(self, journal_id, proxy):
        """Gets the ``OsidSession`` associated with the branch lookup service for the given journal.

        :param journal_id: the ``Id`` of the journal
        :type journal_id: ``osid.id.Id``
        :param proxy: ``a proxy``
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a BranchLookupSession``
        :rtype: ``osid.journaling.BranchLookupSession``
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_branch_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.BranchLookupSession

    def get_branch_query_session(self, proxy):
        """Gets a branch query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a BranchQuerySession``
        :rtype: ``osid.journaling.BranchQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_query()`` is ``false``

        """
        return # osid.journaling.BranchQuerySession

    def get_branch_query_session_for_journal(self, journal_id, proxy):
        """Gets a branch query session for the given journal.

        :param journal_id: the ``Id`` of the journal
        :type journal_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a BranchQuerySession``
        :rtype: ``osid.journaling.BranchQuerySession``
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_branch_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.BranchQuerySession

    def get_branch_search_session(self, proxy):
        """Gets a branch search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a BranchSearchSession``
        :rtype: ``osid.journaling.BranchSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_search()`` is ``false``

        """
        return # osid.journaling.BranchSearchSession

    def get_branch_search_session_for_journal(self, journal_id, proxy):
        """Gets a branch search session for the given journal.

        :param journal_id: the ``Id`` of the journal
        :type journal_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a BranchSearchSession``
        :rtype: ``osid.journaling.BranchSearchSession``
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_branch_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.BranchSearchSession

    def get_branch_admin_session(self, proxy):
        """Gets a branch administration session for creating, updating and deleting branches.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a BranchAdminSession``
        :rtype: ``osid.journaling.BranchAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_admin()`` is ``false``

        """
        return # osid.journaling.BranchAdminSession

    def get_branch_admin_session_for_journal(self, journal_id, proxy):
        """Gets a branch administration session for the given journal.

        :param journal_id: the ``Id`` of the journal
        :type journal_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a BranchAdminSession``
        :rtype: ``osid.journaling.BranchAdminSession``
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.BranchAdminSession

    def get_branch_notification_session(self, branch_receiver, proxy):
        """Gets the branch notification session for the given journal.

        :param branch_receiver: notification callback
        :type branch_receiver: ``osid.journaling.BranchReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a BranchNotificationSession``
        :rtype: ``osid.journaling.BranchNotificationSession``
        :raise: ``NullArgument`` -- ``branch_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_notification()`` is ``false``

        """
        return # osid.journaling.BranchNotificationSession

    def get_branch_notification_session_for_journal(self, branch_receiver, journal_id, proxy):
        """Gets the branch notification session for the given journal.

        :param branch_receiver: notification callback
        :type branch_receiver: ``osid.journaling.BranchReceiver``
        :param journal_id: the ``Id`` of the journal
        :type journal_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a BranchNotificationSession``
        :rtype: ``osid.journaling.BranchNotificationSession``
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``branch_receiver, journal_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_branch_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.journaling.BranchNotificationSession

    def get_branch_smart_journal_session(self, journal_id, proxy):
        """Gets the session for managing dynamic branch journals.

        :param journal_id: the ``Id`` of the journal
        :type journal_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BranchSmartJournalSession``
        :rtype: ``osid.journaling.BranchSmartJournalSession``
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_smart_journal()`` is ``false``

        """
        return # osid.journaling.BranchSmartJournalSession

    def get_journal_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the journal lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``JournalLookupSession``
        :rtype: ``osid.journaling.JournalLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_lookup()`` is ``false``

        """
        return # osid.journaling.JournalLookupSession

    def get_journal_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the journal query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``JournalQuerySession``
        :rtype: ``osid.journaling.JournalQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_query()`` is ``false``

        """
        return # osid.journaling.JournalQuerySession

    def get_journal_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the journal search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``JournalSearchSession``
        :rtype: ``osid.journaling.JournalSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_search()`` is ``false``

        """
        return # osid.journaling.JournalSearchSession

    def get_journal_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the journal administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``JournalAdminSession``
        :rtype: ``osid.journaling.JournalAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_admin()`` is ``false``

        """
        return # osid.journaling.JournalAdminSession

    def get_journal_notification_session(self, journal_receiver, proxy):
        """Gets the ``OsidSession`` associated with the journal notification service.

        :param journal_receiver: the receiver
        :type journal_receiver: ``osid.journaling.JournalReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``JournalNotificationSession``
        :rtype: ``osid.journaling.JournalNotificationSession``
        :raise: ``NullArgument`` -- ``journal_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_notification()`` is ``false``

        """
        return # osid.journaling.JournalNotificationSession

    def get_journal_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the journal hierarchy service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``JournalHierarchySession``
        :rtype: ``osid.journaling.JournalHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_hierarchy()`` is ``false``

        """
        return # osid.journaling.JournalHierarchySession

    def get_journal_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the journal hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``JournalHierarchyDesignSession``
        :rtype: ``osid.journaling.JournalHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_hierarchy_design()`` is ``false``

        """
        return # osid.journaling.JournalHierarchyDesignSession

    def get_journaling_batch_proxy_manager(self):
        """Gets a ``JournalingBatchProxyManager``.

        :return: a ``JournalingBatchProxyManager``
        :rtype: ``osid.journaling.batch.JournalingBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journaling_batch()`` is ``false``

        """
        return # osid.journaling.batch.JournalingBatchProxyManager

    journaling_batch_proxy_manager = property(fget=get_journaling_batch_proxy_manager)


