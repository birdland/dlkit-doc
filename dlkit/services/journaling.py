# -*- coding: utf-8 -*-
"""Journaling Open Service Interface Definitions
journaling version 3.0.0

The Journaling OSID defines an auxiliary service to manage journals and
journal entries for versioining.

Journal Entries

A journal entry represents a change to an object that can be another
OSID. The journal entry contains a time, a source ``Id`` and a version
``Id``. The source ``Id`` is the principal identifier for the journaled
object while the version ``Id`` can be used to retrieve a previous
version of the object by using its respective lookup session.

Journal Cataloging

Journal entries can be categorized into ``Journals,`` which may also be
organized into hierarchies for the purpose of federating journal
entries.

Agents & Resources

An ``Agent`` creates a ``JournalEntry``. The ``JournalEntry`` directly
exposes the related ``Resource`` to manage the orchestration with a
Resourtce OSID. Multiple ``Agents`` may be acting on behalf of a
``Resource``.

Orchestration

An orchestrated journaling service is one that creates a journaling
entry for each create and update of an ``OsidObject``. The orchestration
can be tricky since there is no means for connecting a ``JournalEntry``
to a specific ``OsidObject``. other than to arrange the ``Journals``
such that each ``Journal`` contains entries for a designated
``OsidObject`` interface where multiple ``OsidObjects`` are journaled.

The Journaling OSID is designed to provide a history of the data
contained within an OSID object, such as the evolution of an ``Asset``
or a ``Resource``. OSIDs tend to offer a complex array of relationships.
To capture a history of all relationships, states, and cataloging of an
``OsidObject,`` an OSID Provider can offer a rollback of an entire OSID
to a designated point in time.

Sub Packages

The Journaling OSID contains a Journaling Batch OSID for managing
``JournalEntries,``  ``Branches,`` and ``Journals`` in bulk.

"""
from ..osid import managers as osid_managers
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class JournalingProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if any journal federation is exposed.
        Federation is exposed when a specific journal may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of journals appears as a
        single journal.

        :return: ``true`` if visible federation is supproted, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_journal_entry_lookup(self):
        """Tests for the availability of a journal entry lookup service.

        :return: ``true`` if journal entry lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_journal_entry_query(self):
        """Tests if querying journal entries is available.

        :return: ``true`` if journal entry query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_journal_entry_search(self):
        """Tests if searching for journal entries is available.

        :return: ``true`` if journal entry search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_journal_entry_admin(self):
        """Tests if searching for journal entries is available.

        :return: ``true`` if journal entry search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_journal_entry_notification(self):
        """Tests if journal entry notification is available.

        :return: ``true`` if journal entry notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_branch_lookup(self):
        """Tests if branch lookup is supported.

        :return: ``true`` if branch lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_branch_query(self):
        """Tests if branch query is supported.

        :return: ``true`` if branch query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_branch_search(self):
        """Tests if branch search is supported.

        :return: ``true`` if branch search is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_branch_admin(self):
        """Tests if branch administration is supported.

        :return: ``true`` if branch administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_branch_notification(self):
        """Tests if branch notification is supported.
        Messages may be sent when branches are created, modified, or
        deleted.

        :return: ``true`` if branch notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_branch_smart_journal(self):
        """Tests if branch smart journals are available.

        :return: ``true`` if branch smart journals are supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_journal_lookup(self):
        """Tests for the availability of an journal lookup service.

        :return: ``true`` if journal lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_journal_query(self):
        """Tests if querying journals is available.

        :return: ``true`` if journal query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_journal_search(self):
        """Tests if searching for journals is available.

        :return: ``true`` if journal search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_journal_admin(self):
        """Tests for the availability of a journal administrative service for creating and deleting journals.

        :return: ``true`` if journal administration is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_journal_notification(self):
        """Tests for the availability of a journal notification service.

        :return: ``true`` if journal notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_journal_hierarchy(self):
        """Tests for the availability of a journal hierarchy traversal service.

        :return: ``true`` if journal hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_journal_hierarchy_design(self):
        """Tests for the availability of a journal hierarchy design service.

        :return: ``true`` if journal hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_journalng_batch(self):
        """Tests for the availability of a journaling batch service.

        :return: ``true`` if journaling batch service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_journal_entry_record_types(self):
        """Gets the supported ``JournalEntry`` record types.

        :return: a list containing the supported journal entry record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    journal_entry_record_types = property(fget=get_journal_entry_record_types)

    def supports_journal_entry_record_type(self, journal_entry_record_type):
        """Tests if the given ``JournalEntry`` record type is supported.

        :param journal_entry_record_type: a ``Type`` indicating a ``JournalEntry`` record type
        :type journal_entry_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``journal_entry_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_journal_entry_search_record_types(self):
        """Gets the supported journal entry search record types.

        :return: a list containing the supported journal entry search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    journal_entry_search_record_types = property(fget=get_journal_entry_search_record_types)

    def supports_journal_entry_search_record_type(self, journal_entry_search_record_type):
        """Tests if the given journal entry search record type is supported.

        :param journal_entry_search_record_type: a ``Type`` indicating a journal entry record type
        :type journal_entry_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``journal_entry_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_branch_record_types(self):
        """Gets all the branch record types supported.

        :return: the list of supported branch record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    branch_record_types = property(fget=get_branch_record_types)

    def supports_branch_record_type(self, branch_record_type):
        """Tests if a given branch record type is supported.

        :param branch_record_type: the branch type
        :type branch_record_type: ``osid.type.Type``
        :return: ``true`` if the branch record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``branch_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_branch_search_record_types(self):
        """Gets all the branch search record types supported.

        :return: the list of supported branch search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    branch_search_record_types = property(fget=get_branch_search_record_types)

    def supports_branch_search_record_type(self, branch_search_record_type):
        """Tests if a given branch search type is supported.

        :param branch_search_record_type: the branch search type
        :type branch_search_record_type: ``osid.type.Type``
        :return: ``true`` if the branch search record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``branch_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_journal_record_types(self):
        """Gets the supported ``Journal`` record types.

        :return: a list containing the supported journal record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    journal_record_types = property(fget=get_journal_record_types)

    def supports_journal_record_type(self, journal_record_type):
        """Tests if the given ``Journal`` record type is supported.

        :param journal_record_type: a ``Type`` indicating a ``Journal`` record type
        :type journal_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``journal_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_journal_search_record_types(self):
        """Gets the supported journal search record types.

        :return: a list containing the supported journal search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    journal_search_record_types = property(fget=get_journal_search_record_types)

    def supports_journal_search_record_type(self, journal_search_record_type):
        """Tests if the given journal search record type is supported.

        :param journal_search_record_type: a ``Type`` indicating a journal record type
        :type journal_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``journal_entry_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class JournalingManager(osid_managers.OsidManager, osid_sessions.OsidSession, JournalingProfile):

    def get_journal_entry_lookup_session(self):
        """Gets the ``OsidSession`` associated with the journal entry lookup service.

        :return: a ``JournalEntryLookupSession``
        :rtype: ``osid.journaling.JournalEntryLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_journal_entry_query_session(self):
        """Gets the ``OsidSession`` associated with the journal entry query service.

        :return: a ``JournalEntryQuerySession``
        :rtype: ``osid.journaling.JournalEntryQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_journal_entry_search_session(self):
        """Gets the ``OsidSession`` associated with the journal entry search service.

        :return: a ``JournalEntrySearchSession``
        :rtype: ``osid.journaling.JournalEntrySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_journal_entry_admin_session(self):
        """Gets the ``OsidSession`` associated with the journal entry administration service.

        :return: a ``JournalEntryAdminSession``
        :rtype: ``osid.journaling.JournalEntryAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_entry_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_branch_lookup_session(self):
        """Gets the ``OsidSession`` associated with the branch lookup service.

        :return: ``a BranchLookupSession``
        :rtype: ``osid.journaling.BranchLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_branch_query_session(self):
        """Gets a branch query session.

        :return: ``a BranchQuerySession``
        :rtype: ``osid.journaling.BranchQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_branch_search_session(self):
        """Gets a branch search session.

        :return: ``a BranchSearchSession``
        :rtype: ``osid.journaling.BranchSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_branch_admin_session(self):
        """Gets a branch administration session for creating, updating and deleting branches.

        :return: ``a BranchAdminSession``
        :rtype: ``osid.journaling.BranchAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_branch_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_journal_lookup_session(self):
        """Gets the ``OsidSession`` associated with the journal lookup service.

        :return: a ``JournalLookupSession``
        :rtype: ``osid.journaling.JournalLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    journal_lookup_session = property(fget=get_journal_lookup_session)

    def get_journal_query_session(self):
        """Gets the ``OsidSession`` associated with the journal query service.

        :return: a ``JournalQuerySession``
        :rtype: ``osid.journaling.JournalQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    journal_query_session = property(fget=get_journal_query_session)

    def get_journal_search_session(self):
        """Gets the ``OsidSession`` associated with the journal search service.

        :return: a ``JournalSearchSession``
        :rtype: ``osid.journaling.JournalSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    journal_search_session = property(fget=get_journal_search_session)

    def get_journal_admin_session(self):
        """Gets the ``OsidSession`` associated with the journal administrative service.

        :return: a ``JournalAdminSession``
        :rtype: ``osid.journaling.JournalAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_journal_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the journal hierarchy service.

        :return: a ``JournalHierarchySession``
        :rtype: ``osid.journaling.JournalHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    journal_hierarchy_session = property(fget=get_journal_hierarchy_session)

    def get_journal_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the journal hierarchy design service.

        :return: a ``JournalHierarchyDesignSession``
        :rtype: ``osid.journaling.JournalHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    journal_hierarchy_design_session = property(fget=get_journal_hierarchy_design_session)

    def get_journaling_batch_manager(self):
        """Gets a ``JournalingBatchManager``.

        :return: a ``JournalingBatchManager``
        :rtype: ``osid.journaling.batch.JournalingBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journaling_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    journaling_batch_manager = property(fget=get_journaling_batch_manager)


##
# The following methods are from osid.journaling.JournalEntryLookupSession

    def get_journal_id(self):
        """Gets the ``Journal``  ``Id`` associated with this session.

        :return: the ``Journal Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    journal_id = property(fget=get_journal_id)

    def get_journal(self):
        """Gets the ``Journal`` associated with this session.

        :return: the journal
        :rtype: ``osid.journaling.Journal``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    journal = property(fget=get_journal)

    def can_read_journal(self):
        """Tests if this user can examine this journal.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer these
        operations.

        :return: ``false`` if journal reading methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_journal_entry_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_journal_entry_view(self):
        """A complete view of the ``JournalEntry`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_journal_view(self):
        """Federates the view for methods in this session.
        A federated view will include entries in journals which are
        children of this journal in the journal hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_journal_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts retrievals to this journal only.



        """
        raise UNIMPLEMENTED()

    def get_journal_entry(self, journal_entry_id):
        """Gets the ``JournalEntry`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``JournalEntry`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``JournalEntry`` and retained
        for compatibility.

        :param journal_entry_id: the ``Id`` of the ``JournalEntry`` to retrieve
        :type journal_entry_id: ``osid.id.Id``
        :return: the returned ``JournalEntry``
        :rtype: ``osid.journaling.JournalEntry``
        :raise: ``NotFound`` -- no ``JournalEntry`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``journal_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_ids(self, journal_entry_ids):
        """Gets a ``JournalEntryList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the entries
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible entries may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param journal_entry_ids: the list of ``Ids`` to retrieve
        :type journal_entry_ids: ``osid.id.IdList``
        :return: the returned ``JournalEntry list``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``journal_entry_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_genus_type(self, journal_entry_genus_type):
        """Gets a ``JournalEntryList`` corresponding to the given journal entry genus ``Type`` which does not include journal entries of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known journal
        entries or an error results. Otherwise, the returned list may
        contain only those journal entries that are accessible through
        this session.

        :param journal_entry_genus_type: a journal entry genus type
        :type journal_entry_genus_type: ``osid.type.Type``
        :return: the returned ``JournalEntry`` list
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``journal_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_parent_genus_type(self, journal_entry_genus_type):
        """Gets a ``JournalEntryList`` corresponding to the given journal entry genus ``Type`` and include any additional journal entries with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known journal
        entries or an error results. Otherwise, the returned list may
        contain only those journal entries that are accessible through
        this session.

        :param journal_entry_genus_type: a journal entry genus type
        :type journal_entry_genus_type: ``osid.type.Type``
        :return: the returned ``JournalEntry`` list
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``journal_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_record_type(self, journal_entry_record_type):
        """Gets a ``JournalEntryList`` containing the given journal entry record ``Type``.
        In plenary mode, the returned list contains all known journal
        entries or an error results. Otherwise, the returned list may
        contain only those journal entries that are accessible through
        this session.

        :param journal_entry_record_type: a journal entry record type
        :type journal_entry_record_type: ``osid.type.Type``
        :return: the returned ``JournalEntry`` list
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``journal_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_for_branch(self, branch_id):
        """Gets a list of journal entries corresponding to a branch ``Id``.
        In plenary mode, the returned list contains all known journal
        entries or an error results. Otherwise, the returned list may
        contain only those journal entries that are accessible through
        this session.

        :param branch_id: the ``Id`` of the branch
        :type branch_id: ``osid.id.Id``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_date_for_branch(self, branch_id, date):
        """Gets the journal entry corresponding to a resource ``Id`` and date.
        The entries returned have a date equal to or more recent than
        the requested date. In plenary mode, the returned list contains
        all known journal entries or an error results. Otherwise, the
        returned list may contain only those journal entries that are
        accessible through this session.

        :param branch_id: the ``Id`` of the branch
        :type branch_id: ``osid.id.Id``
        :param date: from date
        :type date: ``osid.calendaring.DateTime``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``branch_id`` or ``date`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_date_range_for_branch(self, branch_id, from_, to):
        """Gets a list of journal entries corresponding to a branch ``Id`` and date range.
        Entries are returned with dates that fall between the requested
        dates inclusive. In plenary mode, the returned list contains all
        known journal entries or an error results. Otherwise, the
        returned list may contain only those journal entries that are
        accessible through this session.

        :param branch_id: the ``Id`` of the branch
        :type branch_id: ``osid.id.Id``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``branch_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_for_source(self, source_id):
        """Gets a list of journal entries corresponding to a source ``Id``.
        A source ``Id`` of any version may be requested. In plenary
        mode, the returned list contains all known journal entries or an
        error results. Otherwise, the returned list may contain only
        those journal entries that are accessible through this session.

        :param source_id: the ``Id`` of the source
        :type source_id: ``osid.id.Id``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``source_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_date_for_source(self, source_id, date):
        """Gets the journal entry corresponding to a source ``Id`` and date.
        The entry returned has a date equal to or more recent than the
        requested date. The ``source_id`` may correspond to any version.
        In plenary mode, the returned list contains all known journal
        entries or an error results. Otherwise, the returned list may
        contain only those journal entries that are accessible through
        this session.

        :param source_id: a source ``Id``
        :type source_id: ``osid.id.Id``
        :param date: from date
        :type date: ``osid.calendaring.DateTime``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``source_id`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_date_range_for_source(self, source_id, from_, to):
        """Gets a list of journal entries corresponding to a source ``Id`` and date range.
        Entries are returned with dates that fall between the requested
        dates inclusive. The ``source_id`` may correspond to any
        version. In plenary mode, the returned list contains all known
        journal entries or an error results. Otherwise, the returned
        list may contain only those journal entries that are accessible
        through this session.

        :param source_id: a source ``Id``
        :type source_id: ``osid.id.Id``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``source_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_for_branch_and_source(self, branch_id, source_id):
        """Gets a list of journal entries corresponding to a branch and source ``Id``.
        A source ``Id`` of any version may be requested.In plenary mode,
        the returned list contains all known journal entries or an error
        results. Otherwise, the returned list may contain only those
        journal entries that are accessible through this session.

        :param branch_id: the ``Id`` of the branch
        :type branch_id: ``osid.id.Id``
        :param source_id: the ``Id`` of the source
        :type source_id: ``osid.id.Id``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``branch_id`` or ``source_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_date_for_branch_and_source(self, branch_id, source_id, date):
        """Gets the journal entry corresponding to a branch and source ``Id`` and date.
        The entry returned has a date equal to or more recent than the
        requested date. The ``source_id`` may correspond to any version.
        In plenary mode, the returned list contains all known journal
        entries or an error results. Otherwise, the returned list may
        contain only those journal entries that are accessible through
        this session.

        :param branch_id: a branch ``Id``
        :type branch_id: ``osid.id.Id``
        :param source_id: the ``Id`` of the source
        :type source_id: ``osid.id.Id``
        :param date: from date
        :type date: ``osid.calendaring.DateTime``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``branch_id, source_id`` or ``date`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_date_range_for_branch_and_source(self, branch_id, source_id, from_, to):
        """Gets a list of journal entries corresponding to a branch and source ``Id`` and date range.
        Entries are returned with dates that fall between the requested
        dates inclusive. The ``source_id`` may correspond to any version
        In plenary mode, the returned list contains all known journal
        entries or an error results. Otherwise, the returned list may
        contain only those journal entries that are accessible through
        this session.

        :param branch_id: a branch ``Id``
        :type branch_id: ``osid.id.Id``
        :param source_id: the ``Id`` of the source
        :type source_id: ``osid.id.Id``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``branch_id, source_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_for_resource(self, resource_id):
        """Gets a list of journal entries corresponding to a resource ``Id``.
        In plenary mode, the returned list contains all known journal
        entries or an error results. Otherwise, the returned list may
        contain only those journal entries that are accessible through
        this session.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_date_for_resource(self, resource_id, date):
        """Gets the journal entry corresponding to a resource ``Id`` and date.
        The entry returned has a date equal to or more recent than the
        requested date. In plenary mode, the returned list contains all
        known journal entries or an error results. Otherwise, the
        returned list may contain only those journal entries that are
        accessible through this session.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param date: from date
        :type date: ``osid.calendaring.DateTime``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``resource_id`` or ``date`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_date_range_for_resource(self, resource_id, from_, to):
        """Gets a list of journal entries corresponding to a resource ``Id`` and date range.
        Entries are returned with dates that fall between the requested
        dates inclusive. In plenary mode, the returned list contains all
        known journal entries or an error results. Otherwise, the
        returned list may contain only those journal entries that are
        accessible through this session.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``resource_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries(self):
        """Gets all journal entries.
        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session. In both
        cases, the order of the set is not specifed. In plenary mode,
        the returned list contains all known journal entries or an error
        results. Otherwise, the returned list may contain only those
        journal entries that are accessible through this session.

        :return: a list of journal entries
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    journal_entries = property(fget=get_journal_entries)


##
# The following methods are from osid.journaling.JournalEntryQuerySession

    def can_search_journal_entries(self):
        """Tests if this user can perform ``Journal`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may wish not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_journal_entry_query(self):
        """Gets a journal entry query.

        :return: the journal entry query
        :rtype: ``osid.journaling.JournalEntryQuery``

        """
        raise UNIMPLEMENTED()

    journal_entry_query = property(fget=get_journal_entry_query)

    def get_journal_entries_by_query(self, journal_entry_query):
        """Gets a list of journal entries matching the given journal entry query.

        :param journal_entry_query: the journal entry query
        :type journal_entry_query: ``osid.journaling.JournalEntryQuery``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``journal_entry_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``journal_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalEntrySearchSession

    def get_journal_entry_search(self):
        """Gets a journal entry search.

        :return: the journal entry search
        :rtype: ``osid.journaling.JournalEntrySearch``

        """
        raise UNIMPLEMENTED()

    journal_entry_search = property(fget=get_journal_entry_search)

    def get_journal_entry_search_order(self):
        """Gets a journal entry search order.
        The ``JournalEntrySearchOrder`` is supplied to a
        ``JournalEntrySearch`` to specify the ordering of results.

        :return: the journal entry search order
        :rtype: ``osid.journaling.JournalEntrySearchOrder``

        """
        raise UNIMPLEMENTED()

    journal_entry_search_order = property(fget=get_journal_entry_search_order)

    def get_journal_entries_by_search(self, journal_entry_query, journal_entry_search):
        """Gets the search results matching the given search.

        :param journal_entry_query: the journal entry query
        :type journal_entry_query: ``osid.journaling.JournalEntryQuery``
        :param journal_entry_search: the journal entry search
        :type journal_entry_search: ``osid.journaling.JournalEntrySearch``
        :return: the search results
        :rtype: ``osid.journaling.JournalEntrySearchResults``
        :raise: ``NullArgument`` -- ``journal_entry_query`` or ``journal_entry_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``journal_entry_query`` or ``journal_entry_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_journal_entry_query_from_inspector(self, journal_entry_query_inspector):
        """Gets a journal entry query from an inspector.
        The inspector is available from a ``JournalEntrySearchResults``.

        :param journal_entry_query_inspector: a journal entry query inspector
        :type journal_entry_query_inspector: ``osid.journaling.JournalEntryQueryInspector``
        :return: the journal entry query
        :rtype: ``osid.journaling.JournalEntryQuery``
        :raise: ``NullArgument`` -- ``journal_entry_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``journal_entry_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalEntryAdminSession

    def can_create_journal_entries(self):
        """Tests if this user can create journal entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``JournalEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``JournalEntry`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_journal_entry_with_record_types(self, journal_entry_record_types):
        """Tests if this user can create a single ``JournalEntry`` using the desired record interface types.
        While ``JournalingManager.getJournalEntryRecordTypes()`` can be
        used to examine which record interfaces are supported, this
        method tests which record(s) are required for creating a
        specific ``JournalEntry``. Providing an empty array tests if a
        ``JournalEntry`` can be created with no records.

        :param journal_entry_record_types: array of journal entry record types
        :type journal_entry_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``JournalEntry`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``journal_entry_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_journal_entry_form_for_create(self, branch_id, source_id, journal_entry_record_types):
        """Gets the journal entry form for creating new entries.
        A new form should be requested for each create transaction.

        :param branch_id: the ``Id`` for the branch
        :type branch_id: ``osid.id.Id``
        :param source_id: the ``Id`` for the journaled object
        :type source_id: ``osid.id.Id``
        :param journal_entry_record_types: array of journal entry record types
        :type journal_entry_record_types: ``osid.type.Type[]``
        :return: the journal entry form
        :rtype: ``osid.journaling.JournalEntryForm``
        :raise: ``NotFound`` -- ``branch_id`` is not found
        :raise: ``NullArgument`` -- ``branch_id, source_id,`` or ``journal_entry_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_journal_entry(self, journal_entry_form):
        """Creates a new ``JournalEntry``.

        :param journal_entry_form: the form for this ``JournalEntry``
        :type journal_entry_form: ``osid.journaling.JournalEntryForm``
        :return: the new ``JournalEntry``
        :rtype: ``osid.journaling.JournalEntry``
        :raise: ``IllegalState`` -- ``journal_entry_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``journal_entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``journal_entry_form`` did not originate from ``get_journal_entry_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_journal_entries(self):
        """Tests if this user can update journal entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``JournalEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``JournalEntry`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_journal_entry_form_for_update(self, journal_entry_id):
        """Gets the journal entry form for updating an existing entry.
        A new journal entry form should be requested for each update
        transaction.

        :param journal_entry_id: the ``Id`` of the ``JournalEntry``
        :type journal_entry_id: ``osid.id.Id``
        :return: the entry form
        :rtype: ``osid.journaling.JournalEntryForm``
        :raise: ``NotFound`` -- ``journal_entry_id`` is not found
        :raise: ``NullArgument`` -- ``journal_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_journal_entry(self, journal_entry_form):
        """Updates an existing journal entry.

        :param journal_entry_form: the form containing the elements to be updated
        :type journal_entry_form: ``osid.journaling.JournalEntryForm``
        :raise: ``IllegalState`` -- ``journal_entry_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``journal_entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``journal_entry_form`` did not originate from ``get_journal_entry_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_journal_entries(self):
        """Tests if this user can delete journal entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``JournalEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``JournalEntry`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_journal_entry(self, journal_entry_id):
        """Deletes a ``JournalEntry``.

        :param journal_entry_id: the ``Id`` of the ``JournalEntry`` to remove
        :type journal_entry_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``journal_entry_id`` not found
        :raise: ``NullArgument`` -- ``journal_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_journal_entry_aliases(self):
        """Tests if this user can manage ``Id`` aliases for journal entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``JournalEntry`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_journal_entry(self, journal_entry_id, alias_id):
        """Adds an ``Id`` to a ``JournalEntry`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``JournalEntry`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another journal entry it is
        reassigned to the given journal entry ``Id``.

        :param journal_entry_id: the ``Id`` of a ``JournalEntry``
        :type journal_entry_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``journal_entry_id`` not found
        :raise: ``NullArgument`` -- ``journal_entry_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalEntryNotificationSession

    def can_register_for_journal_entry_notifications(self):
        """Tests if this user can register for ``JournalEntry`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_journal_entries(self):
        """Register for notifications of new journal entries.
        ``JournalEntryReceiver.newJournalEntry()`` is invoked when a new
        ``JournalEntry`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_journal_entries_for_branch(self, branch_id):
        """Register for notifications of new journal entries for the given branch ``Id``.
        ``JournalEntryReceiver.newJournalEntry()`` is invoked when a new
        ``JournalEntry`` is created.

        :param branch_id: the ``Id`` of the branch to monitor
        :type branch_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_journal_entries_for_source(self, source_id):
        """Register for notifications of new journal entries for the given source ``Id``.
        ``JournalEntryReceiver.newJournalEntry()`` is invoked when a new
        ``JournalEntry`` is created.

        :param source_id: the ``Id`` of the source to monitor
        :type source_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``source_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_journal_entries_for_resource(self, resource_id):
        """Register for notifications of new journal entries for the given resource ``Id``.
        ``JournalEntryReceiver.newJournalEntry()`` is invoked when a new
        ``JournalEntry`` is created.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_journal_entries(self):
        """Registers for notification of updated journal entries.
        ``JournalEntryReceiver.changedJournalEntry()`` is invoked when a
        journal entry is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_journal_entries_for_branch(self, branch_id):
        """Register for notifications of changed journal entries for the given branch ``Id``.
        ``JournalEntryReceiver.changedJournalEntry()`` is invoked when a
        ``JournalEntry`` for the branch is changed.

        :param branch_id: the ``Id`` of the branch to monitor
        :type branch_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_journal_entries_for_source(self, source_id):
        """Register for notifications of changed journal entries for the given source ``Id``.
        ``JournalEntryReceiver.changedJournalEntry()`` is invoked when a
        ``JournalEntry`` for the source is changed.

        :param source_id: the ``Id`` of the source to monitor
        :type source_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``source_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_journal_entries_for_resource(self, resource_id):
        """Register for notifications of changed journal entries for the given resource ``Id``.
        ``JournalEntryReceiver.changedJournalEntry()`` is invoked when a
        ``JournalEntry`` for the source is changed.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_journal_entry(self, journal_entry_id):
        """Registers for notification of an updated journal entry.
        ``JournalEntryReceiver.changedJournalEntry()`` is invoked when
        the specified journal entry is changed.

        :param journal_entry_id: the ``Id`` of the ``JournalEntry`` to monitor
        :type journal_entry_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``journal_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journal_entries(self):
        """Registers for notification of deleted journal entries.
        ``JournalEntryReceiver.deletedJournalEntry()`` is invoked when a
        journal entry is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journal_entries_for_branch(self, branch_id):
        """Register for notifications of deleted journal entries for the given source ``Id``.
        ``JournalEntryReceiver.deletedJournalEntry()`` is invoked when a
        ``JournalEntry`` for the branch is deleted.

        :param branch_id: the ``Id`` of the branch to monitor
        :type branch_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journal_entries_for_source(self, source_id):
        """Register for notifications of deleted journal entries for the given source ``Id``.
        ``JournalEntryReceiver.deletedJournalEntry()`` is invoked when a
        ``JournalEntry`` for the source is deleted.

        :param source_id: the ``Id`` of the source to monitor
        :type source_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``source_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journal_entries_for_resource(self, resource_id):
        """Register for notifications of deleted journal entries for the given resource ``Id``.
        ``JournalEntryReceiver.deletedJournalEntry()`` is invoked when a
        ``JournalEntry`` for the source is deleted.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journal_entry(self, journal_entry_id):
        """Registers for notification of a deleted journal entry.
        ``JournalEntryReceiver.deletedJournalEntry()`` is invoked when
        the specified journal entry is deleted.

        :param journal_entry_id: the ``Id`` of the ``JournalEntry`` to monitor
        :type journal_entry_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``journal_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalLookupSession

    def can_lookup_journals(self):
        """Tests if this user can perform ``Journal`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_journal_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_journal_view(self):
        """A complete view of the ``Journal`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_journals_by_ids(self, journal_ids):
        """Gets a ``JournalList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the journals
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Journals`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param journal_ids: the list of ``Ids`` to retrieve
        :type journal_ids: ``osid.id.IdList``
        :return: the returned ``Journal`` list
        :rtype: ``osid.journaling.JournalList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``journal_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journals_by_genus_type(self, journal_genus_type):
        """Gets a ``JournalList`` corresponding to the given journal genus ``Type`` which does not include journals of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known journals
        or an error results. Otherwise, the returned list may contain
        only those journals that are accessible through this session.

        :param journal_genus_type: a journal genus type
        :type journal_genus_type: ``osid.type.Type``
        :return: the returned ``Journal`` list
        :rtype: ``osid.journaling.JournalList``
        :raise: ``NullArgument`` -- ``journal_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journals_by_parent_genus_type(self, journal_genus_type):
        """Gets a ``JournalList`` corresponding to the given journal genus ``Type`` and include any additional journals with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known journals
        or an error results. Otherwise, the returned list may contain
        only those journals that are accessible through this session.

        :param journal_genus_type: a journal genus type
        :type journal_genus_type: ``osid.type.Type``
        :return: the returned ``Journal`` list
        :rtype: ``osid.journaling.JournalList``
        :raise: ``NullArgument`` -- ``journal_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journals_by_record_type(self, journal_record_type):
        """Gets a ``JournalList`` containing the given journal record ``Type``.
        In plenary mode, the returned list contains all known journals
        or an error results. Otherwise, the returned list may contain
        only those journals that are accessible through this session.

        :param journal_record_type: a journal record type
        :type journal_record_type: ``osid.type.Type``
        :return: the returned ``Journal`` list
        :rtype: ``osid.journaling.JournalList``
        :raise: ``NullArgument`` -- ``journal_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journals_by_provider(self, resource_id):
        """Gets a ``JournalList`` for the given provider.
        In plenary mode, the returned list contains all known journals
        or an error results. Otherwise, the returned list may contain
        only those journals that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Journal`` list
        :rtype: ``osid.journaling.JournalList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journals(self):
        """Gets all ``Journals``.
        In plenary mode, the returned list contains all known journals
        or an error results. Otherwise, the returned list may contain
        only those journals that are accessible through this session.

        :return: a list of ``Journals``
        :rtype: ``osid.journaling.JournalList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    journals = property(fget=get_journals)


##
# The following methods are from osid.journaling.JournalQuerySession

    def can_search_journals(self):
        """Tests if this user can perform ``Journal`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_journal_query(self):
        """Gets a journal query.

        :return: the journal query
        :rtype: ``osid.journaling.JournalQuery``

        """
        raise UNIMPLEMENTED()

    journal_query = property(fget=get_journal_query)

    def get_journals_by_query(self, journal_query):
        """Gets a list of ``Journals`` matching the given search.

        :param journal_query: the journal query
        :type journal_query: ``osid.journaling.JournalQuery``
        :return: the returned ``JournalList``
        :rtype: ``osid.journaling.JournalList``
        :raise: ``NullArgument`` -- ``journal_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``journal_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalSearchSession

    def get_journal_search(self):
        """Gets a journal search.

        :return: the journal search
        :rtype: ``osid.journaling.JournalSearch``

        """
        raise UNIMPLEMENTED()

    journal_search = property(fget=get_journal_search)

    def get_journal_search_order(self):
        """Gets a journal search order.
        The ``JournalSearchOrder`` is supplied to a ``JournalSearch`` to
        specify the ordering of results.

        :return: the journal search order
        :rtype: ``osid.journaling.JournalSearchOrder``

        """
        raise UNIMPLEMENTED()

    journal_search_order = property(fget=get_journal_search_order)

    def get_journals_by_search(self, journal_query, journal_search):
        """Gets the search results matching the given search.

        :param journal_query: the journal query
        :type journal_query: ``osid.journaling.JournalQuery``
        :param journal_search: the journal search
        :type journal_search: ``osid.journaling.JournalSearch``
        :return: the journal search results
        :rtype: ``osid.journaling.JournalSearchResults``
        :raise: ``NullArgument`` -- ``journal_query`` or ``journal_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``journal_query`` or ``journal_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_journal_query_from_inspector(self, journal_query_inspector):
        """Gets a journal query from an inspector.
        The inspector is available from a ``JournalSearchResults``.

        :param journal_query_inspector: a journal query inspector
        :type journal_query_inspector: ``osid.journaling.JournalQueryInspector``
        :return: the journal query
        :rtype: ``osid.journaling.JournalQuery``
        :raise: ``NullArgument`` -- ``journal_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``journal_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalAdminSession

    def can_create_journals(self):
        """Tests if this user can create ``Journals``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Journal`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Journal`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_journal_with_record_types(self, journal_record_types):
        """Tests if this user can create a single ``Journal`` using the desired record interface types.
        While ``JournalingManager.getJournalRecordTypes()`` can be used
        to examine which record interfaces are supported, this method
        tests which record(s) are required for creating a specific
        ``Journal``. Providing an empty array tests if a ``Journal`` can
        be created with no records.

        :param journal_record_types: array of journal record types
        :type journal_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Journal`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``journal_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_journal_form_for_create(self, journal_record_types):
        """Gets the journal form for creating new journals.
        A new form should be requested for each create transaction.

        :param journal_record_types: array of journal record types
        :type journal_record_types: ``osid.type.Type[]``
        :return: the journal form
        :rtype: ``osid.journaling.JournalForm``
        :raise: ``NullArgument`` -- ``journal_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_journal(self, journal_form):
        """Creates a new ``Journal``.

        :param journal_form: the form for this ``Journal``
        :type journal_form: ``osid.journaling.JournalForm``
        :return: the new ``Journal``
        :rtype: ``osid.journaling.Journal``
        :raise: ``IllegalState`` -- ``journal_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``journal_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``journal_form`` did not originate from ``get_journal_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_journals(self):
        """Tests if this user can update ``Journals``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Journal`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Journal`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_journal_form_for_update(self, journal_id):
        """Gets the journal form for updating an existing journal.
        A new journal form should be requested for each update
        transaction.

        :param journal_id: the ``Id`` of the ``Journal``
        :type journal_id: ``osid.id.Id``
        :return: the journal form
        :rtype: ``osid.journaling.JournalForm``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def update_journal(self, journal_form):
        """Updates an existing journal.

        :param journal_form: the form containing the elements to be updated
        :type journal_form: ``osid.journaling.JournalForm``
        :raise: ``IllegalState`` -- ``journal_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``journal_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``journal_form`` did not originate from ``get_journal_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_journals(self):
        """Tests if this user can delete ``Journals`` A return of true does not guarantee successful authorization.
        A return of false indicates that it is known deleting a
        ``Journal`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Journal`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_journal(self, journal_id):
        """Deletes a ``Journal``.

        :param journal_id: the ``Id`` of the ``Journal`` to remove
        :type journal_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_journal_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Journals``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Journal`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_journal(self, journal_id, alias_id):
        """Adds an ``Id`` to a ``Journal`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Journal`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id`` . If the alias is a pointer to another journal it is
        reassigned to the given journal ``Id``.

        :param journal_id: the ``Id`` of a ``Journal``
        :type journal_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalNotificationSession

    def can_register_for_journal_notifications(self):
        """Tests if this user can register for ``Journal`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_journals(self):
        """Register for notifications of new journals.
        ``JournalReceiver.newJournal()`` is invoked when a new
        ``Journal`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_journal_ancestors(self, journal_id):
        """Registers for notification of an updated hierarchy structure that introduces a new ancestor of the specified journal.
        ``JournalReceiver.newAncestorJournal()`` is invoked when the
        specified journal node gets a new ancestor.

        :param journal_id: the ``Id`` of the ``Journal`` node to monitor
        :type journal_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_journal_descendants(self, journal_id):
        """Registers for notification of an updated hierarchy structure that introduces a new descendant of the specified journal.
        ``JournalReceiver.newDescendantJournal()`` is invoked when the
        specified journal node gets a new descendant.

        :param journal_id: the ``Id`` of the ``Journal`` node to monitor
        :type journal_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_journals(self):
        """Registers for notification of updated journals.
        ``JournalReceiver.changedJournal()`` is invoked when a journal
        is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_journal(self, journal_id):
        """Registers for notification of an updated journal.
        ``JournalReceiver.changedJournal()`` is invoked when the
        specified journal is changed.

        :param journal_id: the ``Id`` of the ``Journal`` to monitor
        :type journal_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journals(self):
        """Registers for notification of deleted journals.
        ``JournalReceiver.deletedJournal()`` is invoked when a journal
        is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journal(self, journal_id):
        """Registers for notification of a deleted journal.
        ``JournalReceiver.deletedJournal()`` is invoked when the
        specified journal is deleted.

        :param journal_id: the ``Id`` of the ``Journal`` to monitor
        :type journal_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journal_ancestors(self, journal_id):
        """Registers for notification of an updated hierarchy structure that removes an ancestor of the specified journal ``JournalReceiver.
        deletedAncestor()`` is invoked when the specified journal node
        loses an ancestor.

        :param journal_id: the ``Id`` of the ``Journal`` to monitor
        :type journal_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journal_descendants(self, journal_id):
        """Registers for notification of an updated hierarchy structure that removes a descendant of the specified journal.
        ``JournalReceiver.deletedDescendant()`` is invoked when the
        specified journal node loses a descendant.

        :param journal_id: the ``Id`` of the ``Journal`` to monitor
        :type journal_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalHierarchySession

    def get_journal_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    journal_hierarchy_id = property(fget=get_journal_hierarchy_id)

    def get_journal_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    journal_hierarchy = property(fget=get_journal_hierarchy)

    def can_access_journal_hierarchy(self):
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

    def get_root_journal_ids(self):
        """Gets the root journal ``Ids`` in this hierarchy.

        :return: the root journal ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_journal_ids = property(fget=get_root_journal_ids)

    def get_root_journals(self):
        """Gets the root journals in the journal hierarchy.
        A node with no parents is an orphan. While all journal ``Ids``
        are known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        :return: the root journals
        :rtype: ``osid.journaling.JournalList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_journals = property(fget=get_root_journals)

    def has_parent_journals(self, journal_id):
        """Tests if the ``Journal`` has any parents.

        :param journal_id: a journal ``Id``
        :type journal_id: ``osid.id.Id``
        :return: ``true`` if the journal has parents, f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_journal(self, id_, journal_id):
        """Tests if an ``Id`` is a direct parent of journal.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``journal_id,`` f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_journal_ids(self, journal_id):
        """Gets the parent ``Ids`` of the given journal.

        :param journal_id: a journal ``Id``
        :type journal_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the journal
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_journals(self, journal_id):
        """Gets the parent journals of the given ``id``.

        :param journal_id: the ``Id`` of the ``Journal`` to query
        :type journal_id: ``osid.id.Id``
        :return: the parent journals of the ``id``
        :rtype: ``osid.journaling.JournalList``
        :raise: ``NotFound`` -- a ``Journal`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_journal(self, id_, journal_id):
        """Tests if an ``Id`` is an ancestor of a journal.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :return: ``tru`` e if this ``id`` is an ancestor of ``journal_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_journals(self, journal_id):
        """Tests if a journal has any children.

        :param journal_id: a journal ``Id``
        :type journal_id: ``osid.id.Id``
        :return: ``true`` if the ``journal_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_journal(self, id_, journal_id):
        """Tests if a journal is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``journal_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_journal_ids(self, journal_id):
        """Gets the child ``Ids`` of the given journal.

        :param journal_id: the ``Id`` to query
        :type journal_id: ``osid.id.Id``
        :return: the children of the journal
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_journals(self, journal_id):
        """Gets the child journals of the given ``id``.

        :param journal_id: the ``Id`` of the ``Journal`` to query
        :type journal_id: ``osid.id.Id``
        :return: the child journals of the ``id``
        :rtype: ``osid.journaling.JournalList``
        :raise: ``NotFound`` -- a ``Journal`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_journal(self, id_, journal_id):
        """Tests if an ``Id`` is a descendant of a journal.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``journal_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_node_ids(self, journal_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given journal.

        :param journal_id: the ``Id`` to query
        :type journal_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a journal node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_nodes(self, journal_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given journal.

        :param journal_id: the ``Id`` to query
        :type journal_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a journal node
        :rtype: ``osid.journaling.JournalNode``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalHierarchyDesignSession

    def can_modify_journal_hierarchy(self):
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

    def add_root_journal(self, journal_id):
        """Adds a root journal.

        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``journal_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_journal(self, journal_id):
        """Removes a root journal.

        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``journal_id`` is not a root
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_journal(self, journal_id, child_id):
        """Adds a child to a journal.

        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``journal_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``journal_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_journal(self, journal_id, child_id):
        """Removes a child from a journal.

        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``journal_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``journal_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_journals(self, journal_id):
        """Removes all children from a journal.

        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class JournalingProxyManager(osid_managers.OsidProxyManager, JournalingProfile):

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_journaling_batch_proxy_manager(self):
        """Gets a ``JournalingBatchProxyManager``.

        :return: a ``JournalingBatchProxyManager``
        :rtype: ``osid.journaling.batch.JournalingBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journaling_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    journaling_batch_proxy_manager = property(fget=get_journaling_batch_proxy_manager)


##
# The following methods are from osid.journaling.JournalEntryLookupSession

    def get_journal_id(self):
        """Gets the ``Journal``  ``Id`` associated with this session.

        :return: the ``Journal Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    journal_id = property(fget=get_journal_id)

    def get_journal(self):
        """Gets the ``Journal`` associated with this session.

        :return: the journal
        :rtype: ``osid.journaling.Journal``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    journal = property(fget=get_journal)

    def can_read_journal(self):
        """Tests if this user can examine this journal.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer these
        operations.


        :return: ``false`` if journal reading methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_journal_entry_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.




        """
        raise UNIMPLEMENTED()

    def use_plenary_journal_entry_view(self):
        """A complete view of the ``JournalEntry`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.




        """
        raise UNIMPLEMENTED()

    def use_federated_journal_view(self):
        """Federates the view for methods in this session.
        A federated view will include entries in journals which are
        children of this journal in the journal hierarchy.




        """
        raise UNIMPLEMENTED()

    def use_isolated_journal_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts retrievals to this journal only.




        """
        raise UNIMPLEMENTED()

    def get_journal_entry(self, journal_entry_id):
        """Gets the ``JournalEntry`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``JournalEntry`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``JournalEntry`` and retained
        for compatibility.


        :param journal_entry_id: the ``Id`` of the ``JournalEntry`` to retrieve
        :type journal_entry_id: ``osid.id.Id``
        :return: the returned ``JournalEntry``
        :rtype: ``osid.journaling.JournalEntry``
        :raise: ``NotFound`` -- no ``JournalEntry`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``journal_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_ids(self, journal_entry_ids):
        """Gets a ``JournalEntryList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the entries
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible entries may be omitted from the list and may
        present the elements in any order including returning a unique
        set.


        :param journal_entry_ids: the list of ``Ids`` to retrieve
        :type journal_entry_ids: ``osid.id.IdList``
        :return: the returned ``JournalEntry list``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``journal_entry_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_genus_type(self, journal_entry_genus_type):
        """Gets a ``JournalEntryList`` corresponding to the given journal entry genus ``Type`` which does not include journal entries of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known journal
        entries or an error results. Otherwise, the returned list may
        contain only those journal entries that are accessible through
        this session.


        :param journal_entry_genus_type: a journal entry genus type
        :type journal_entry_genus_type: ``osid.type.Type``
        :return: the returned ``JournalEntry`` list
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``journal_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_parent_genus_type(self, journal_entry_genus_type):
        """Gets a ``JournalEntryList`` corresponding to the given journal entry genus ``Type`` and include any additional journal entries with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known journal
        entries or an error results. Otherwise, the returned list may
        contain only those journal entries that are accessible through
        this session.


        :param journal_entry_genus_type: a journal entry genus type
        :type journal_entry_genus_type: ``osid.type.Type``
        :return: the returned ``JournalEntry`` list
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``journal_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_record_type(self, journal_entry_record_type):
        """Gets a ``JournalEntryList`` containing the given journal entry record ``Type``.
        In plenary mode, the returned list contains all known journal
        entries or an error results. Otherwise, the returned list may
        contain only those journal entries that are accessible through
        this session.


        :param journal_entry_record_type: a journal entry record type
        :type journal_entry_record_type: ``osid.type.Type``
        :return: the returned ``JournalEntry`` list
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``journal_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_for_branch(self, branch_id):
        """Gets a list of journal entries corresponding to a branch ``Id``.
        In plenary mode, the returned list contains all known journal
        entries or an error results. Otherwise, the returned list may
        contain only those journal entries that are accessible through
        this session.


        :param branch_id: the ``Id`` of the branch
        :type branch_id: ``osid.id.Id``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_date_for_branch(self, branch_id, date):
        """Gets the journal entry corresponding to a resource ``Id`` and date.
        The entries returned have a date equal to or more recent than
        the requested date. In plenary mode, the returned list contains
        all known journal entries or an error results. Otherwise, the
        returned list may contain only those journal entries that are
        accessible through this session.


        :param branch_id: the ``Id`` of the branch
        :type branch_id: ``osid.id.Id``
        :param date: from date
        :type date: ``osid.calendaring.DateTime``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``branch_id`` or ``date`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_date_range_for_branch(self, branch_id, from_, to):
        """Gets a list of journal entries corresponding to a branch ``Id`` and date range.
        Entries are returned with dates that fall between the requested
        dates inclusive. In plenary mode, the returned list contains all
        known journal entries or an error results. Otherwise, the
        returned list may contain only those journal entries that are
        accessible through this session.


        :param branch_id: the ``Id`` of the branch
        :type branch_id: ``osid.id.Id``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``branch_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_for_source(self, source_id):
        """Gets a list of journal entries corresponding to a source ``Id``.
        A source ``Id`` of any version may be requested. In plenary
        mode, the returned list contains all known journal entries or an
        error results. Otherwise, the returned list may contain only
        those journal entries that are accessible through this session.


        :param source_id: the ``Id`` of the source
        :type source_id: ``osid.id.Id``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``source_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_date_for_source(self, source_id, date):
        """Gets the journal entry corresponding to a source ``Id`` and date.
        The entry returned has a date equal to or more recent than the
        requested date. The ``source_id`` may correspond to any version.
        In plenary mode, the returned list contains all known journal
        entries or an error results. Otherwise, the returned list may
        contain only those journal entries that are accessible through
        this session.


        :param source_id: a source ``Id``
        :type source_id: ``osid.id.Id``
        :param date: from date
        :type date: ``osid.calendaring.DateTime``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``source_id`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_date_range_for_source(self, source_id, from_, to):
        """Gets a list of journal entries corresponding to a source ``Id`` and date range.
        Entries are returned with dates that fall between the requested
        dates inclusive. The ``source_id`` may correspond to any
        version. In plenary mode, the returned list contains all known
        journal entries or an error results. Otherwise, the returned
        list may contain only those journal entries that are accessible
        through this session.


        :param source_id: a source ``Id``
        :type source_id: ``osid.id.Id``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``source_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_for_branch_and_source(self, branch_id, source_id):
        """Gets a list of journal entries corresponding to a branch and source ``Id``.
        A source ``Id`` of any version may be requested.In plenary mode,
        the returned list contains all known journal entries or an error
        results. Otherwise, the returned list may contain only those
        journal entries that are accessible through this session.


        :param branch_id: the ``Id`` of the branch
        :type branch_id: ``osid.id.Id``
        :param source_id: the ``Id`` of the source
        :type source_id: ``osid.id.Id``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``branch_id`` or ``source_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_date_for_branch_and_source(self, branch_id, source_id, date):
        """Gets the journal entry corresponding to a branch and source ``Id`` and date.
        The entry returned has a date equal to or more recent than the
        requested date. The ``source_id`` may correspond to any version.
        In plenary mode, the returned list contains all known journal
        entries or an error results. Otherwise, the returned list may
        contain only those journal entries that are accessible through
        this session.


        :param branch_id: a branch ``Id``
        :type branch_id: ``osid.id.Id``
        :param source_id: the ``Id`` of the source
        :type source_id: ``osid.id.Id``
        :param date: from date
        :type date: ``osid.calendaring.DateTime``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``branch_id, source_id`` or ``date`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_date_range_for_branch_and_source(self, branch_id, source_id, from_, to):
        """Gets a list of journal entries corresponding to a branch and source ``Id`` and date range.
        Entries are returned with dates that fall between the requested
        dates inclusive. The ``source_id`` may correspond to any version
        In plenary mode, the returned list contains all known journal
        entries or an error results. Otherwise, the returned list may
        contain only those journal entries that are accessible through
        this session.


        :param branch_id: a branch ``Id``
        :type branch_id: ``osid.id.Id``
        :param source_id: the ``Id`` of the source
        :type source_id: ``osid.id.Id``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``branch_id, source_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_for_resource(self, resource_id):
        """Gets a list of journal entries corresponding to a resource ``Id``.
        In plenary mode, the returned list contains all known journal
        entries or an error results. Otherwise, the returned list may
        contain only those journal entries that are accessible through
        this session.


        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_date_for_resource(self, resource_id, date):
        """Gets the journal entry corresponding to a resource ``Id`` and date.
        The entry returned has a date equal to or more recent than the
        requested date. In plenary mode, the returned list contains all
        known journal entries or an error results. Otherwise, the
        returned list may contain only those journal entries that are
        accessible through this session.


        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param date: from date
        :type date: ``osid.calendaring.DateTime``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``resource_id`` or ``date`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries_by_date_range_for_resource(self, resource_id, from_, to):
        """Gets a list of journal entries corresponding to a resource ``Id`` and date range.
        Entries are returned with dates that fall between the requested
        dates inclusive. In plenary mode, the returned list contains all
        known journal entries or an error results. Otherwise, the
        returned list may contain only those journal entries that are
        accessible through this session.


        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``resource_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_entries(self):
        """Gets all journal entries.
        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session. In both
        cases, the order of the set is not specifed. In plenary mode,
        the returned list contains all known journal entries or an error
        results. Otherwise, the returned list may contain only those
        journal entries that are accessible through this session.


        :return: a list of journal entries
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    journal_entries = property(fget=get_journal_entries)


##
# The following methods are from osid.journaling.JournalEntryQuerySession

    def can_search_journal_entries(self):
        """Tests if this user can perform ``Journal`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may wish not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_journal_entry_query(self):
        """Gets a journal entry query.

        :return: the journal entry query
        :rtype: ``osid.journaling.JournalEntryQuery``

        """
        raise UNIMPLEMENTED()

    journal_entry_query = property(fget=get_journal_entry_query)

    def get_journal_entries_by_query(self, journal_entry_query):
        """Gets a list of journal entries matching the given journal entry query.

        :param journal_entry_query: the journal entry query
        :type journal_entry_query: ``osid.journaling.JournalEntryQuery``
        :return: the returned ``JournalEntryList``
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``NullArgument`` -- ``journal_entry_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``journal_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalEntrySearchSession

    def get_journal_entry_search(self):
        """Gets a journal entry search.

        :return: the journal entry search
        :rtype: ``osid.journaling.JournalEntrySearch``

        """
        raise UNIMPLEMENTED()

    journal_entry_search = property(fget=get_journal_entry_search)

    def get_journal_entry_search_order(self):
        """Gets a journal entry search order.
        The ``JournalEntrySearchOrder`` is supplied to a
        ``JournalEntrySearch`` to specify the ordering of results.


        :return: the journal entry search order
        :rtype: ``osid.journaling.JournalEntrySearchOrder``

        """
        raise UNIMPLEMENTED()

    journal_entry_search_order = property(fget=get_journal_entry_search_order)

    def get_journal_entries_by_search(self, journal_entry_query, journal_entry_search):
        """Gets the search results matching the given search.

        :param journal_entry_query: the journal entry query
        :type journal_entry_query: ``osid.journaling.JournalEntryQuery``
        :param journal_entry_search: the journal entry search
        :type journal_entry_search: ``osid.journaling.JournalEntrySearch``
        :return: the search results
        :rtype: ``osid.journaling.JournalEntrySearchResults``
        :raise: ``NullArgument`` -- ``journal_entry_query`` or ``journal_entry_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``journal_entry_query`` or ``journal_entry_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_journal_entry_query_from_inspector(self, journal_entry_query_inspector):
        """Gets a journal entry query from an inspector.
        The inspector is available from a ``JournalEntrySearchResults``.


        :param journal_entry_query_inspector: a journal entry query inspector
        :type journal_entry_query_inspector: ``osid.journaling.JournalEntryQueryInspector``
        :return: the journal entry query
        :rtype: ``osid.journaling.JournalEntryQuery``
        :raise: ``NullArgument`` -- ``journal_entry_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``journal_entry_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalEntryAdminSession

    def can_create_journal_entries(self):
        """Tests if this user can create journal entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``JournalEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.


        :return: ``false`` if ``JournalEntry`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_journal_entry_with_record_types(self, journal_entry_record_types):
        """Tests if this user can create a single ``JournalEntry`` using the desired record interface types.
        While ``JournalingManager.getJournalEntryRecordTypes()`` can be
        used to examine which record interfaces are supported, this
        method tests which record(s) are required for creating a
        specific ``JournalEntry``. Providing an empty array tests if a
        ``JournalEntry`` can be created with no records.


        :param journal_entry_record_types: array of journal entry record types
        :type journal_entry_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``JournalEntry`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``journal_entry_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_journal_entry_form_for_create(self, branch_id, source_id, journal_entry_record_types):
        """Gets the journal entry form for creating new entries.
        A new form should be requested for each create transaction.


        :param branch_id: the ``Id`` for the branch
        :type branch_id: ``osid.id.Id``
        :param source_id: the ``Id`` for the journaled object
        :type source_id: ``osid.id.Id``
        :param journal_entry_record_types: array of journal entry record types
        :type journal_entry_record_types: ``osid.type.Type[]``
        :return: the journal entry form
        :rtype: ``osid.journaling.JournalEntryForm``
        :raise: ``NotFound`` -- ``branch_id`` is not found
        :raise: ``NullArgument`` -- ``branch_id, source_id,`` or ``journal_entry_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_journal_entry(self, journal_entry_form):
        """Creates a new ``JournalEntry``.

        :param journal_entry_form: the form for this ``JournalEntry``
        :type journal_entry_form: ``osid.journaling.JournalEntryForm``
        :return: the new ``JournalEntry``
        :rtype: ``osid.journaling.JournalEntry``
        :raise: ``IllegalState`` -- ``journal_entry_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``journal_entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``journal_entry_form`` did not originate from ``get_journal_entry_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_journal_entries(self):
        """Tests if this user can update journal entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``JournalEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.


        :return: ``false`` if ``JournalEntry`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_journal_entry_form_for_update(self, journal_entry_id):
        """Gets the journal entry form for updating an existing entry.
        A new journal entry form should be requested for each update
        transaction.


        :param journal_entry_id: the ``Id`` of the ``JournalEntry``
        :type journal_entry_id: ``osid.id.Id``
        :return: the entry form
        :rtype: ``osid.journaling.JournalEntryForm``
        :raise: ``NotFound`` -- ``journal_entry_id`` is not found
        :raise: ``NullArgument`` -- ``journal_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_journal_entry(self, journal_entry_form):
        """Updates an existing journal entry.

        :param journal_entry_form: the form containing the elements to be updated
        :type journal_entry_form: ``osid.journaling.JournalEntryForm``
        :raise: ``IllegalState`` -- ``journal_entry_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``journal_entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``journal_entry_form`` did not originate from ``get_journal_entry_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_journal_entries(self):
        """Tests if this user can delete journal entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``JournalEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.


        :return: ``false`` if ``JournalEntry`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_journal_entry(self, journal_entry_id):
        """Deletes a ``JournalEntry``.

        :param journal_entry_id: the ``Id`` of the ``JournalEntry`` to remove
        :type journal_entry_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``journal_entry_id`` not found
        :raise: ``NullArgument`` -- ``journal_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_journal_entry_aliases(self):
        """Tests if this user can manage ``Id`` aliases for journal entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``JournalEntry`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_journal_entry(self, journal_entry_id, alias_id):
        """Adds an ``Id`` to a ``JournalEntry`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``JournalEntry`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another journal entry it is
        reassigned to the given journal entry ``Id``.


        :param journal_entry_id: the ``Id`` of a ``JournalEntry``
        :type journal_entry_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``journal_entry_id`` not found
        :raise: ``NullArgument`` -- ``journal_entry_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalEntryNotificationSession

    def can_register_for_journal_entry_notifications(self):
        """Tests if this user can register for ``JournalEntry`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.


        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_journal_entries(self):
        """Register for notifications of new journal entries.
        ``JournalEntryReceiver.newJournalEntry()`` is invoked when a new
        ``JournalEntry`` is created.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_journal_entries_for_branch(self, branch_id):
        """Register for notifications of new journal entries for the given branch ``Id``.
        ``JournalEntryReceiver.newJournalEntry()`` is invoked when a new
        ``JournalEntry`` is created.


        :param branch_id: the ``Id`` of the branch to monitor
        :type branch_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_journal_entries_for_source(self, source_id):
        """Register for notifications of new journal entries for the given source ``Id``.
        ``JournalEntryReceiver.newJournalEntry()`` is invoked when a new
        ``JournalEntry`` is created.


        :param source_id: the ``Id`` of the source to monitor
        :type source_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``source_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_journal_entries_for_resource(self, resource_id):
        """Register for notifications of new journal entries for the given resource ``Id``.
        ``JournalEntryReceiver.newJournalEntry()`` is invoked when a new
        ``JournalEntry`` is created.


        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_journal_entries(self):
        """Registers for notification of updated journal entries.
        ``JournalEntryReceiver.changedJournalEntry()`` is invoked when a
        journal entry is changed.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_journal_entries_for_branch(self, branch_id):
        """Register for notifications of changed journal entries for the given branch ``Id``.
        ``JournalEntryReceiver.changedJournalEntry()`` is invoked when a
        ``JournalEntry`` for the branch is changed.


        :param branch_id: the ``Id`` of the branch to monitor
        :type branch_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_journal_entries_for_source(self, source_id):
        """Register for notifications of changed journal entries for the given source ``Id``.
        ``JournalEntryReceiver.changedJournalEntry()`` is invoked when a
        ``JournalEntry`` for the source is changed.


        :param source_id: the ``Id`` of the source to monitor
        :type source_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``source_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_journal_entries_for_resource(self, resource_id):
        """Register for notifications of changed journal entries for the given resource ``Id``.
        ``JournalEntryReceiver.changedJournalEntry()`` is invoked when a
        ``JournalEntry`` for the source is changed.


        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_journal_entry(self, journal_entry_id):
        """Registers for notification of an updated journal entry.
        ``JournalEntryReceiver.changedJournalEntry()`` is invoked when
        the specified journal entry is changed.


        :param journal_entry_id: the ``Id`` of the ``JournalEntry`` to monitor
        :type journal_entry_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``journal_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journal_entries(self):
        """Registers for notification of deleted journal entries.
        ``JournalEntryReceiver.deletedJournalEntry()`` is invoked when a
        journal entry is deleted.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journal_entries_for_branch(self, branch_id):
        """Register for notifications of deleted journal entries for the given source ``Id``.
        ``JournalEntryReceiver.deletedJournalEntry()`` is invoked when a
        ``JournalEntry`` for the branch is deleted.


        :param branch_id: the ``Id`` of the branch to monitor
        :type branch_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journal_entries_for_source(self, source_id):
        """Register for notifications of deleted journal entries for the given source ``Id``.
        ``JournalEntryReceiver.deletedJournalEntry()`` is invoked when a
        ``JournalEntry`` for the source is deleted.


        :param source_id: the ``Id`` of the source to monitor
        :type source_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``source_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journal_entries_for_resource(self, resource_id):
        """Register for notifications of deleted journal entries for the given resource ``Id``.
        ``JournalEntryReceiver.deletedJournalEntry()`` is invoked when a
        ``JournalEntry`` for the source is deleted.


        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journal_entry(self, journal_entry_id):
        """Registers for notification of a deleted journal entry.
        ``JournalEntryReceiver.deletedJournalEntry()`` is invoked when
        the specified journal entry is deleted.


        :param journal_entry_id: the ``Id`` of the ``JournalEntry`` to monitor
        :type journal_entry_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``journal_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalLookupSession

    def can_lookup_journals(self):
        """Tests if this user can perform ``Journal`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.


        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_journal_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.




        """
        raise UNIMPLEMENTED()

    def use_plenary_journal_view(self):
        """A complete view of the ``Journal`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.




        """
        raise UNIMPLEMENTED()

    def get_journals_by_ids(self, journal_ids):
        """Gets a ``JournalList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the journals
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Journals`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.


        :param journal_ids: the list of ``Ids`` to retrieve
        :type journal_ids: ``osid.id.IdList``
        :return: the returned ``Journal`` list
        :rtype: ``osid.journaling.JournalList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``journal_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journals_by_genus_type(self, journal_genus_type):
        """Gets a ``JournalList`` corresponding to the given journal genus ``Type`` which does not include journals of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known journals
        or an error results. Otherwise, the returned list may contain
        only those journals that are accessible through this session.


        :param journal_genus_type: a journal genus type
        :type journal_genus_type: ``osid.type.Type``
        :return: the returned ``Journal`` list
        :rtype: ``osid.journaling.JournalList``
        :raise: ``NullArgument`` -- ``journal_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journals_by_parent_genus_type(self, journal_genus_type):
        """Gets a ``JournalList`` corresponding to the given journal genus ``Type`` and include any additional journals with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known journals
        or an error results. Otherwise, the returned list may contain
        only those journals that are accessible through this session.


        :param journal_genus_type: a journal genus type
        :type journal_genus_type: ``osid.type.Type``
        :return: the returned ``Journal`` list
        :rtype: ``osid.journaling.JournalList``
        :raise: ``NullArgument`` -- ``journal_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journals_by_record_type(self, journal_record_type):
        """Gets a ``JournalList`` containing the given journal record ``Type``.
        In plenary mode, the returned list contains all known journals
        or an error results. Otherwise, the returned list may contain
        only those journals that are accessible through this session.


        :param journal_record_type: a journal record type
        :type journal_record_type: ``osid.type.Type``
        :return: the returned ``Journal`` list
        :rtype: ``osid.journaling.JournalList``
        :raise: ``NullArgument`` -- ``journal_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journals_by_provider(self, resource_id):
        """Gets a ``JournalList`` for the given provider.
        In plenary mode, the returned list contains all known journals
        or an error results. Otherwise, the returned list may contain
        only those journals that are accessible through this session.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Journal`` list
        :rtype: ``osid.journaling.JournalList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journals(self):
        """Gets all ``Journals``.
        In plenary mode, the returned list contains all known journals
        or an error results. Otherwise, the returned list may contain
        only those journals that are accessible through this session.


        :return: a list of ``Journals``
        :rtype: ``osid.journaling.JournalList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    journals = property(fget=get_journals)


##
# The following methods are from osid.journaling.JournalQuerySession

    def can_search_journals(self):
        """Tests if this user can perform ``Journal`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_journal_query(self):
        """Gets a journal query.

        :return: the journal query
        :rtype: ``osid.journaling.JournalQuery``

        """
        raise UNIMPLEMENTED()

    journal_query = property(fget=get_journal_query)

    def get_journals_by_query(self, journal_query):
        """Gets a list of ``Journals`` matching the given search.

        :param journal_query: the journal query
        :type journal_query: ``osid.journaling.JournalQuery``
        :return: the returned ``JournalList``
        :rtype: ``osid.journaling.JournalList``
        :raise: ``NullArgument`` -- ``journal_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``journal_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalSearchSession

    def get_journal_search(self):
        """Gets a journal search.

        :return: the journal search
        :rtype: ``osid.journaling.JournalSearch``

        """
        raise UNIMPLEMENTED()

    journal_search = property(fget=get_journal_search)

    def get_journal_search_order(self):
        """Gets a journal search order.
        The ``JournalSearchOrder`` is supplied to a ``JournalSearch`` to
        specify the ordering of results.


        :return: the journal search order
        :rtype: ``osid.journaling.JournalSearchOrder``

        """
        raise UNIMPLEMENTED()

    journal_search_order = property(fget=get_journal_search_order)

    def get_journals_by_search(self, journal_query, journal_search):
        """Gets the search results matching the given search.

        :param journal_query: the journal query
        :type journal_query: ``osid.journaling.JournalQuery``
        :param journal_search: the journal search
        :type journal_search: ``osid.journaling.JournalSearch``
        :return: the journal search results
        :rtype: ``osid.journaling.JournalSearchResults``
        :raise: ``NullArgument`` -- ``journal_query`` or ``journal_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``journal_query`` or ``journal_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_journal_query_from_inspector(self, journal_query_inspector):
        """Gets a journal query from an inspector.
        The inspector is available from a ``JournalSearchResults``.


        :param journal_query_inspector: a journal query inspector
        :type journal_query_inspector: ``osid.journaling.JournalQueryInspector``
        :return: the journal query
        :rtype: ``osid.journaling.JournalQuery``
        :raise: ``NullArgument`` -- ``journal_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``journal_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalAdminSession

    def can_create_journals(self):
        """Tests if this user can create ``Journals``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Journal`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.


        :return: ``false`` if ``Journal`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_journal_with_record_types(self, journal_record_types):
        """Tests if this user can create a single ``Journal`` using the desired record interface types.
        While ``JournalingManager.getJournalRecordTypes()`` can be used
        to examine which record interfaces are supported, this method
        tests which record(s) are required for creating a specific
        ``Journal``. Providing an empty array tests if a ``Journal`` can
        be created with no records.


        :param journal_record_types: array of journal record types
        :type journal_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Journal`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``journal_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_journal_form_for_create(self, journal_record_types):
        """Gets the journal form for creating new journals.
        A new form should be requested for each create transaction.


        :param journal_record_types: array of journal record types
        :type journal_record_types: ``osid.type.Type[]``
        :return: the journal form
        :rtype: ``osid.journaling.JournalForm``
        :raise: ``NullArgument`` -- ``journal_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_journal(self, journal_form):
        """Creates a new ``Journal``.

        :param journal_form: the form for this ``Journal``
        :type journal_form: ``osid.journaling.JournalForm``
        :return: the new ``Journal``
        :rtype: ``osid.journaling.Journal``
        :raise: ``IllegalState`` -- ``journal_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``journal_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``journal_form`` did not originate from ``get_journal_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_journals(self):
        """Tests if this user can update ``Journals``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Journal`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.


        :return: ``false`` if ``Journal`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_journal_form_for_update(self, journal_id):
        """Gets the journal form for updating an existing journal.
        A new journal form should be requested for each update
        transaction.


        :param journal_id: the ``Id`` of the ``Journal``
        :type journal_id: ``osid.id.Id``
        :return: the journal form
        :rtype: ``osid.journaling.JournalForm``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def update_journal(self, journal_form):
        """Updates an existing journal.

        :param journal_form: the form containing the elements to be updated
        :type journal_form: ``osid.journaling.JournalForm``
        :raise: ``IllegalState`` -- ``journal_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``journal_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``journal_form`` did not originate from ``get_journal_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_journals(self):
        """Tests if this user can delete ``Journals`` A return of true does not guarantee successful authorization.
        A return of false indicates that it is known deleting a
        ``Journal`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.


        :return: ``false`` if ``Journal`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_journal(self, journal_id):
        """Deletes a ``Journal``.

        :param journal_id: the ``Id`` of the ``Journal`` to remove
        :type journal_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_journal_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Journals``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``Journal`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_journal(self, journal_id, alias_id):
        """Adds an ``Id`` to a ``Journal`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Journal`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id`` . If the alias is a pointer to another journal it is
        reassigned to the given journal ``Id``.


        :param journal_id: the ``Id`` of a ``Journal``
        :type journal_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalNotificationSession

    def can_register_for_journal_notifications(self):
        """Tests if this user can register for ``Journal`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.


        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_journals(self):
        """Register for notifications of new journals.
        ``JournalReceiver.newJournal()`` is invoked when a new
        ``Journal`` is created.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_journal_ancestors(self, journal_id):
        """Registers for notification of an updated hierarchy structure that introduces a new ancestor of the specified journal.
        ``JournalReceiver.newAncestorJournal()`` is invoked when the
        specified journal node gets a new ancestor.


        :param journal_id: the ``Id`` of the ``Journal`` node to monitor
        :type journal_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_journal_descendants(self, journal_id):
        """Registers for notification of an updated hierarchy structure that introduces a new descendant of the specified journal.
        ``JournalReceiver.newDescendantJournal()`` is invoked when the
        specified journal node gets a new descendant.


        :param journal_id: the ``Id`` of the ``Journal`` node to monitor
        :type journal_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_journals(self):
        """Registers for notification of updated journals.
        ``JournalReceiver.changedJournal()`` is invoked when a journal
        is changed.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_journal(self, journal_id):
        """Registers for notification of an updated journal.
        ``JournalReceiver.changedJournal()`` is invoked when the
        specified journal is changed.


        :param journal_id: the ``Id`` of the ``Journal`` to monitor
        :type journal_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journals(self):
        """Registers for notification of deleted journals.
        ``JournalReceiver.deletedJournal()`` is invoked when a journal
        is deleted.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journal(self, journal_id):
        """Registers for notification of a deleted journal.
        ``JournalReceiver.deletedJournal()`` is invoked when the
        specified journal is deleted.


        :param journal_id: the ``Id`` of the ``Journal`` to monitor
        :type journal_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journal_ancestors(self, journal_id):
        """Registers for notification of an updated hierarchy structure that removes an ancestor of the specified journal ``JournalReceiver.
        deletedAncestor()`` is invoked when the specified journal node
        loses an ancestor.


        :param journal_id: the ``Id`` of the ``Journal`` to monitor
        :type journal_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_journal_descendants(self, journal_id):
        """Registers for notification of an updated hierarchy structure that removes a descendant of the specified journal.
        ``JournalReceiver.deletedDescendant()`` is invoked when the
        specified journal node loses a descendant.


        :param journal_id: the ``Id`` of the ``Journal`` to monitor
        :type journal_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalHierarchySession

    def get_journal_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    journal_hierarchy_id = property(fget=get_journal_hierarchy_id)

    def get_journal_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    journal_hierarchy = property(fget=get_journal_hierarchy)

    def can_access_journal_hierarchy(self):
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

    def get_root_journal_ids(self):
        """Gets the root journal ``Ids`` in this hierarchy.

        :return: the root journal ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_journal_ids = property(fget=get_root_journal_ids)

    def get_root_journals(self):
        """Gets the root journals in the journal hierarchy.
        A node with no parents is an orphan. While all journal ``Ids``
        are known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.


        :return: the root journals
        :rtype: ``osid.journaling.JournalList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_journals = property(fget=get_root_journals)

    def has_parent_journals(self, journal_id):
        """Tests if the ``Journal`` has any parents.

        :param journal_id: a journal ``Id``
        :type journal_id: ``osid.id.Id``
        :return: ``true`` if the journal has parents, f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_journal(self, id_, journal_id):
        """Tests if an ``Id`` is a direct parent of journal.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``journal_id,`` f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_journal_ids(self, journal_id):
        """Gets the parent ``Ids`` of the given journal.

        :param journal_id: a journal ``Id``
        :type journal_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the journal
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_journals(self, journal_id):
        """Gets the parent journals of the given ``id``.

        :param journal_id: the ``Id`` of the ``Journal`` to query
        :type journal_id: ``osid.id.Id``
        :return: the parent journals of the ``id``
        :rtype: ``osid.journaling.JournalList``
        :raise: ``NotFound`` -- a ``Journal`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_journal(self, id_, journal_id):
        """Tests if an ``Id`` is an ancestor of a journal.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :return: ``tru`` e if this ``id`` is an ancestor of ``journal_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_journals(self, journal_id):
        """Tests if a journal has any children.

        :param journal_id: a journal ``Id``
        :type journal_id: ``osid.id.Id``
        :return: ``true`` if the ``journal_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_journal(self, id_, journal_id):
        """Tests if a journal is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``journal_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_journal_ids(self, journal_id):
        """Gets the child ``Ids`` of the given journal.

        :param journal_id: the ``Id`` to query
        :type journal_id: ``osid.id.Id``
        :return: the children of the journal
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_journals(self, journal_id):
        """Gets the child journals of the given ``id``.

        :param journal_id: the ``Id`` of the ``Journal`` to query
        :type journal_id: ``osid.id.Id``
        :return: the child journals of the ``id``
        :rtype: ``osid.journaling.JournalList``
        :raise: ``NotFound`` -- a ``Journal`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_journal(self, id_, journal_id):
        """Tests if an ``Id`` is a descendant of a journal.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``journal_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_node_ids(self, journal_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given journal.

        :param journal_id: the ``Id`` to query
        :type journal_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a journal node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_journal_nodes(self, journal_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given journal.

        :param journal_id: the ``Id`` to query
        :type journal_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a journal node
        :rtype: ``osid.journaling.JournalNode``
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.JournalHierarchyDesignSession

    def can_modify_journal_hierarchy(self):
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

    def add_root_journal(self, journal_id):
        """Adds a root journal.

        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``journal_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``journal_id`` is not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_journal(self, journal_id):
        """Removes a root journal.

        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``journal_id`` is not a root
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_journal(self, journal_id, child_id):
        """Adds a child to a journal.

        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``journal_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``journal_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_journal(self, journal_id, child_id):
        """Removes a child from a journal.

        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``journal_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``journal_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_journals(self, journal_id):
        """Removes all children from a journal.

        :param journal_id: the ``Id`` of a journal
        :type journal_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``journal_id`` not found
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class Journal(osid_objects.OsidCatalog, osid_sessions.OsidSession):

    def get_journal_record(self, journal_record_type):
        """Gets the journal record corresponding to the given ``Journal`` record ``Type``.
        This method is used to retrieve an object implementing the
        requested record. The ``journal_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(journal_record_type)`` is ``true`` .

        :param journal_record_type: the type of journal record to retrieve
        :type journal_record_type: ``osid.type.Type``
        :return: the journal record
        :rtype: ``osid.journaling.records.JournalRecord``
        :raise: ``NullArgument`` -- ``journal_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(journal_record_type)`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.BranchLookupSession

    def get_journal_id(self):
        """Gets the ``Journal``  ``Id`` associated with this session.

        :return: the ``Journal Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    journal_id = property(fget=get_journal_id)

    def get_journal(self):
        """Gets the ``Journal`` associated with this session.

        :return: the ``Journal`` associated with this session
        :rtype: ``osid.journaling.Journal``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    journal = property(fget=get_journal)

    def can_lookup_branches(self):
        """Tests if this user can perform ``Branch`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_branch_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_branch_view(self):
        """A complete view of the ``Branch`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_journal_view(self):
        """Federates the view for methods in this session.
        A federated view will include branches in journals which are
        children of this journal in the journal hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_journal_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this journal only.



        """
        raise UNIMPLEMENTED()

    def use_active_branch_view(self):
        """Methods return only branches that are active."""
        raise UNIMPLEMENTED()

    def use_any_status_branch_view(self):
        """Actuve and inactive branches are returned from lookup methods in this session."""
        raise UNIMPLEMENTED()

    def get_branch(self, branch_id):
        """Gets the ``Branch`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Branch`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Branch`` and retained for compatibility.

        :param branch_id: the ``Id`` of the ``Branch`` to retrieve
        :type branch_id: ``osid.id.Id``
        :return: the returned ``Branch``
        :rtype: ``osid.journaling.Branch``
        :raise: ``NotFound`` -- no ``Branch`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_branches_by_ids(self, branch_ids):
        """Gets a ``BranchList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the branches
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Branches`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param branch_ids: the list of ``Ids`` to retrieve
        :type branch_ids: ``osid.id.IdList``
        :return: the returned ``Branch`` list
        :rtype: ``osid.journaling.BranchList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``branch_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_branches_by_genus_type(self, branch_genus_type):
        """Gets a ``BranchList`` corresponding to the given branch genus ``Type`` which does not include branches of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known branches
        or an error results. Otherwise, the returned list may contain
        only those branches that are accessible through this session.

        :param branch_genus_type: a branch genus type
        :type branch_genus_type: ``osid.type.Type``
        :return: the returned ``Branch`` list
        :rtype: ``osid.journaling.BranchList``
        :raise: ``NullArgument`` -- ``branch_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_branches_by_parent_genus_type(self, branch_genus_type):
        """Gets a ``BranchList`` corresponding to the given branch genus ``Type`` and include any additional branches with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known branches
        or an error results. Otherwise, the returned list may contain
        only those branches that are accessible through this session.

        :param branch_genus_type: a branch genus type
        :type branch_genus_type: ``osid.type.Type``
        :return: the returned ``Branch`` list
        :rtype: ``osid.journaling.BranchList``
        :raise: ``NullArgument`` -- ``branch_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_branches_by_record_type(self, branch_record_type):
        """Gets a ``BranchList`` containing the given branch record ``Type``.
        In plenary mode, the returned list contains all known branches
        or an error results. Otherwise, the returned list may contain
        only those branches that are accessible through this session.

        :param branch_record_type: a branch record type
        :type branch_record_type: ``osid.type.Type``
        :return: the returned ``Branch`` list
        :rtype: ``osid.journaling.BranchList``
        :raise: ``NullArgument`` -- ``branch_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_branches(self):
        """Gets all ``Branches``.
        In plenary mode, the returned list contains all known branches
        or an error results. Otherwise, the returned list may contain
        only those branches that are accessible through this session.

        :return: a list of ``Branches``
        :rtype: ``osid.journaling.BranchList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    branches = property(fget=get_branches)


##
# The following methods are from osid.journaling.BranchQuerySession

    def can_search_branches(self):
        """Tests if this user can perform ``Branch`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_branch_query(self):
        """Gets a branch query.
        The returned query will not have an extension query.

        :return: the branch query
        :rtype: ``osid.journaling.BranchQuery``

        """
        raise UNIMPLEMENTED()

    branch_query = property(fget=get_branch_query)

    def get_branches_by_query(self, branch_query):
        """Gets a list of ``Branches`` matching the given branch query.

        :param branch_query: the branch query
        :type branch_query: ``osid.journaling.BranchQuery``
        :return: the returned ``BranchList``
        :rtype: ``osid.journaling.BranchList``
        :raise: ``NullArgument`` -- ``branch_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``branch_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.BranchSearchSession

    def get_branch_search(self):
        """Gets a branch search.

        :return: the branch search
        :rtype: ``osid.journaling.BranchSearch``

        """
        raise UNIMPLEMENTED()

    branch_search = property(fget=get_branch_search)

    def get_branch_search_order(self):
        """Gets a branch search order.
        The ``BranchSearchOrder`` is supplied to a ``BranchSearch`` to
        specify the ordering of results.

        :return: the branch search order
        :rtype: ``osid.journaling.BranchSearchOrder``

        """
        raise UNIMPLEMENTED()

    branch_search_order = property(fget=get_branch_search_order)

    def get_branches_by_search(self, branch_query, branch_search):
        """Gets the search results matching the given search query using the given search.

        :param branch_query: the branch query
        :type branch_query: ``osid.journaling.BranchQuery``
        :param branch_search: the branch search
        :type branch_search: ``osid.journaling.BranchSearch``
        :return: the returned search results
        :rtype: ``osid.journaling.BranchSearchResults``
        :raise: ``NullArgument`` -- ``branch_query`` or ``branch_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``branch_query`` or ``branch_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_branch_query_from_inspector(self, branch_query_inspector):
        """Gets a branch query from an inspector.
        The inspector is available from a ``BranchSearchResults``.

        :param branch_query_inspector: a branch query inspector
        :type branch_query_inspector: ``osid.journaling.BranchQueryInspector``
        :return: the branch query
        :rtype: ``osid.journaling.BranchQuery``
        :raise: ``NullArgument`` -- ``branch_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``branch_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.BranchAdminSession

    def can_create_branches(self):
        """Tests if this user can branch a version chain.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known branching will result
        in a ``PermissionDenied``. This is intended as a hint to an
        application that may not wish to offer create operations to
        unauthorized users.

        :return: ``false`` if journal branching is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_branch(self, journal_entry_id):
        """Tests if this user can branch a specified ``JournalEntry``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known branching the
        ``JournalEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :param journal_entry_id: the ``Id`` of the ``JournalEntry``
        :type journal_entry_id: ``osid.id.Id``
        :return: ``false`` if branching is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``journal_entry_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def can_create_branch_with_record_types(self, branch_record_types):
        """Tests if this user can create a single ``Branch`` using the desired record types.
        While ``JournalingManager.getBranchRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Branch``.
        Providing an empty array tests if a ``Branch`` can be created
        with no records.

        :param branch_record_types: array of branch record types
        :type branch_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Branch`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``branchy_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_branch_form_for_create(self, journal_entry_id, branch_record_types):
        """Gets the branch form for creating new entries.
        A new form should be requested for each create transaction.

        :param journal_entry_id: the ``Id`` of the ``JournalEntry``
        :type journal_entry_id: ``osid.id.Id``
        :param branch_record_types: array of branch record types
        :type branch_record_types: ``osid.type.Type[]``
        :return: the branch form
        :rtype: ``osid.journaling.BranchForm``
        :raise: ``NotFound`` -- ``journal_entry_id`` is not found
        :raise: ``NullArgument`` -- ``journal_entry_id`` or ``branch_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_branch(self, branch_form):
        """Creates a branch.

        :param branch_form: the branch form
        :type branch_form: ``osid.journaling.BranchForm``
        :return: a the new branch
        :rtype: ``osid.journaling.Branch``
        :raise: ``IllegalState`` -- ``branch_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``branch_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``branch_form`` did not originate from ``get_branch_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_branches(self):
        """Tests if this user can update branches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Branch``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Branch`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_branch_form_for_update(self, branch_id):
        """Gets the branch form for updating an existing branch.
        A new journal entry form should be requested for each update
        transaction.

        :param branch_id: the ``Id`` of the ``Branch``
        :type branch_id: ``osid.id.Id``
        :return: the branch form
        :rtype: ``osid.journaling.BranchForm``
        :raise: ``NotFound`` -- ``branch_id`` is not found
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_branch(self, branch_form):
        """Updates an existing branch.

        :param branch_form: the form containing the elements to be updated
        :type branch_form: ``osid.journaling.BranchForm``
        :raise: ``IllegalState`` -- ``branch_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``branch_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``branch_form`` did not originate from ``get_branch_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_merge_branches(self):
        """Tests if this user can merge branches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known merging ``Branches``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer merging
        operations to unauthorized users.

        :return: ``false`` if ``Branch`` merging is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def merge_branches(self, src_branch_id, dst_branch_id):
        """Merges the source branch into the destination branch.
        A new journal entry is created to join the two branches.

        :param src_branch_id: the ``Id`` of the ``Branch`` to merge from
        :type src_branch_id: ``osid.id.Id``
        :param dst_branch_id: the ``Id`` of the ``Branch`` to merge into
        :type dst_branch_id: ``osid.id.Id``
        :return: a the new journal entry
        :rtype: ``osid.journaling.JournalEntry``
        :raise: ``NotFound`` -- ``branch_id`` not found
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_supersede_branches(self):
        """Tests if this user can supersede branches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known merging ``Branches``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer superseding
        operations to unauthorized users.

        :return: ``false`` if ``Branch`` superseding is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supersede_branch(self, src_branch_id, dst_branch_id):
        """Joins the source branch to the destination branch by creating a new journal entry.
        The most recent version of the source branch supsrsedes the most
        recent versiuon of the desitination branch.

        :param src_branch_id: the ``Id`` of the superseding ``Branch``
        :type src_branch_id: ``osid.id.Id``
        :param dst_branch_id: the ``Id`` of the ``Branch`` to override
        :type dst_branch_id: ``osid.id.Id``
        :return: a the new journal entry
        :rtype: ``osid.journaling.JournalEntry``
        :raise: ``NotFound`` -- ``branch_id`` not found
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_delete_branches(self):
        """Tests if this user can delete branches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Branch``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Branch`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_branch(self, branch_id):
        """Deletes a branch and all associated versions.

        :param branch_id: the ``Id`` of the ``Branch`` to remove
        :type branch_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``branch_id`` not found
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_branch_aliases(self):
        """Tests if this user can manage ``Id`` aliases for branches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Branch`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_branch(self, branch_id, alias_id):
        """Adds an ``Id`` to a ``Branch`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Branch`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another branch it is
        reassigned to the given branch ``Id``.

        :param branch_id: the ``Id`` of a ``Branch``
        :type branch_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``branch_id`` not found
        :raise: ``NullArgument`` -- ``branch_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.BranchNotificationSession

    def can_register_for_branch_notifications(self):
        """Tests if this user can register for ``Branch`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_branches(self):
        """Register for notifications of new branches.
        ``BranchReceiver.newBranch()`` is invoked when a new ``Branch``
        is appears in this journal.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_branches(self):
        """Registers for notification of updated branches.
        ``BranchReceiver.changedBranch()`` is invoked when a branch in
        this journal is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_branch(self, branch_id):
        """Registers for notification of an updated branch.
        ``BranchReceiver.changedBranch()`` is invoked when the specified
        branch in this journal is changed.

        :param branch_id: the ``Id`` of the ``Branch`` to monitor
        :type branch_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_branches(self):
        """Registers for notification of deleted branches.
        ``BranchReceiver.deletedBranch()`` is invoked when a branch is
        deleted or removed from this journal.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_branch(self, branch_id):
        """Registers for notification of a deleted branch.
        ``BranchReceiver.deletedBranch()`` is invoked when the specified
        branch is deleted or removed from this journal.

        :param branch_id: the ``Id`` of the ``Branch`` to monitor
        :type branch_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.journaling.BranchSmartJournalSession

    def can_manage_smart_journals(self):
        """Tests if this user can manage smart journals.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart journal management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_branch_query(self, branch_query):
        """Applies a branch query to this journal.

        :param branch_query: the branch query
        :type branch_query: ``osid.journaling.BranchQuery``
        :raise: ``NullArgument`` -- ``branch_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``branch_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_branch_query(self):
        """Gets a branch query inspector for this journal.

        :return: the branch query inspector
        :rtype: ``osid.journaling.BranchQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_branch_sequencing(self, branch_search_order):
        """Applies a branch search order to this journal.

        :param branch_search_order: the branch search order
        :type branch_search_order: ``osid.journaling.BranchSearchOrder``
        :raise: ``NullArgument`` -- ``branch_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``branch_search_order`` not of this service

        """
        raise UNIMPLEMENTED()



class JournalList(osid_objects.OsidList):

    def get_next_journal(self):
        """Gets the next ``Journal`` in this list.

        :return: the next ``Journal`` in this list. The ``has_next()`` method should be used to test that a next ``Journal`` is available before calling this method.
        :rtype: ``osid.journaling.Journal``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    next_journal = property(fget=get_next_journal)

    def get_next_journals(self, n):
        """Gets the next set of ``Journal`` elements in this list.
        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Journal`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Journal`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.journaling.Journal``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()



class Journals(JournalingManager):
    pass


