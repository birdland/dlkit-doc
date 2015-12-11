
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class HierarchyProfile(osid_managers.OsidProfile):
    """The hierarchy profile describes the interoperability among hierarchy services."""
    



    def supports_visible_federation(self):
        """Tests if federation is visible.

        Visible federation allows for selecting among multiple
        hierarchies.

        return: (boolean) - ``true`` if visible federation is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_hierarchy_traversal(self):
        """Tests if hierarchy traversal is supported.

        return: (boolean) - ``true`` if hierarchy traversal is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_hierarchy_design(self):
        """Tests if hierarchy design is supported.

        return: (boolean) - ``true`` if hierarchy design is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_hierarchy_sequencing(self):
        """Tests if hierarchy sequencing is supported.

        return: (boolean) - ``true`` if hierarchy sequencing is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_hierarchy_structure_notification(self):
        """Tests if hierarchy structure notification is supported.

        return: (boolean) - ``true`` if hierarchy structure notification
                is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_hierarchy_lookup(self):
        """Tests if a hierarchy lookup is supported.

        return: (boolean) - ``true`` if hierarchy lookup is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_hierarchy_query(self):
        """Tests if a hierarchy query is supported.

        return: (boolean) - ``true`` if hierarchy query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_hierarchy_search(self):
        """Tests if a hierarchy search is supported.

        return: (boolean) - ``true`` if hierarchy search is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_hierarchy_admin(self):
        """Tests if a hierarchy administration is supported.

        return: (boolean) - ``true`` if hierarchy administration is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_hierarchy_notification(self):
        """Tests if hierarchy notification is supported.

        Messages may be sent when hierarchies are created, modified, or
        deleted.

        return: (boolean) - ``true`` if hierarchy notification is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_hierarchy_record_types(self):
        """Gets the supported ``Hierarchy`` types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Hierarchy`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    hierarchy_record_types = property(fget=get_hierarchy_record_types)


    def supports_hierarchy_record_type(self, hierarchy_record_type):
        """Tests if the given ``Hierarchy`` record type is supported.

        arg:    hierarchy_record_type (osid.type.Type): a ``Type``
                indicating a ``Hierarchy`` record type
        return: (boolean) - ``true`` if the given record Type is
                supported, ``false`` otherwise
        raise:  NullArgument - ``hierarchy_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_hierarchy_search_record_types(self):
        """Gets the supported ``Hierarchy`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Hierarchy`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    hierarchy_search_record_types = property(fget=get_hierarchy_search_record_types)


    def supports_hierarchy_search_record_type(self, hierarchy_search_record_type):
        """Tests if the given ``Hierarchy`` search record type is supported.

        arg:    hierarchy_search_record_type (osid.type.Type): a
                ``Type`` indicating a ``Hierarchy`` search record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``hierarchy_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


class HierarchyManager(osid_managers.OsidManager, osid_sessions.OsidSession, HierarchyProfile):
    """The hierarchy manager provides access sessions to traverse and manage hierrachies of ``Ids``.

    The sessions included in this manager are:

      * ``HierarchyTraversalSession:`` a basic session traversing a
        hierarchy
      * ``HierarchyDesignSession:`` a session to design a hierarchy
      * ``HierarchySequencingSession:`` a session to sequence nodes in a
        hierarchy
      * ``HierarchyStructureNotificationSession:`` a session for
        notififcations within a hierarchy structure
      * ``HierarchyLookupSession:`` a session looking up hiererachies
      * ``HierarchyQuerySession:`` a session querying hiererachies
      * ``HierarchySearchSession:`` a session for searching for
        hierarchies
      * ``HierarchyAdminSession:`` a session for creating and deleting
        hierarchies
      * ``HierarchyNotificationSession:`` a session for subscribing to
        changes in hierarchies

    """
    



    def get_hierarchy_traversal_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service.

        return: (osid.hierarchy.HierarchyTraversalSession) - a
                ``HierarchyTraversalSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_traversal()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_traversal()`` is ``true``.*

        """
        return # osid.hierarchy.HierarchyTraversalSession

    hierarchy_traversal_session = property(fget=get_hierarchy_traversal_session)


    def get_hierarchy_traversal_session_for_hierarchy(self, hierarchy_id):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service for the given hierarchy.

        arg:    hierarchy_id (osid.id.Id): the ``Id`` of the hierarchy
        return: (osid.hierarchy.HierarchyTraversalSession) - the new
                ``HierarchyTraversalSession``
        raise:  NotFound - ``hierarchy_id`` not found
        raise:  NullArgument - ``hierarchyid`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_hierarchy_traversal()`` or
                ``supports_visible_fedaration()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_traversal()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.hierarchy.HierarchyTraversalSession


    def get_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy design service.

        return: (osid.hierarchy.HierarchyDesignSession) - a
                ``HierarchyDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_design()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_design()`` is ``true``.*

        """
        return # osid.hierarchy.HierarchyDesignSession

    hierarchy_design_session = property(fget=get_hierarchy_design_session)


    def get_hierarchy_design_session_for_hierarchy(self, hierarchy_id):
        """Gets the ``OsidSession`` associated with the topology design service using for the given hierarchy.

        arg:    hierarchy_id (osid.id.Id): the ``Id`` of the graph
        return: (osid.hierarchy.HierarchyDesignSession) - a
                ``HierarchyDesignSession``
        raise:  NotFound - ``hierarchy_id`` is not found
        raise:  NullArgument - ``hierarchy_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_design()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_design()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.hierarchy.HierarchyDesignSession


    def get_hierarchy_sequencing_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy sequencing service.

        return: (osid.hierarchy.HierarchySequencingSession) - a
                ``HierarchySequencingSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_sequencing()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_sequencing()`` is ``true``.*

        """
        return # osid.hierarchy.HierarchySequencingSession

    hierarchy_sequencing_session = property(fget=get_hierarchy_sequencing_session)


    def get_hierarchy_sequencing_session_for_hierarchy(self, hierarchy_id):
        """Gets the ``OsidSession`` associated with the sequencing design service using for the given hierarchy.

        arg:    hierarchy_id (osid.id.Id): the ``Id`` of the graph
        return: (osid.hierarchy.HierarchySequencingSession) - a
                ``HierarchySequencingSession``
        raise:  NotFound - ``hierarchy_id`` is not found
        raise:  NullArgument - ``hierarchy_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_sequencing()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_sequencing()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.hierarchy.HierarchySequencingSession


    def get_hierarchy_structure_notification_session(self, hierarchy_structure_receiver):
        """Gets the session for subscribing to notifications of changes within a hierarchy structure.

        arg:    hierarchy_structure_receiver
                (osid.hierarchy.HierarchyStructureReceiver): a receiver
        return: (osid.hierarchy.HierarchyStructureNotificationSession) -
                a ``HierarchyStructureNotificationSession``
        raise:  NullArgument - ``hierarchy_structure_receiver`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_hierarchy_structure_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_structure_notification()`` is ``true``.*

        """
        return # osid.hierarchy.HierarchyStructureNotificationSession


    def get_hierarchy_structure_notification_session_for_hierarchy(self, hierarchy_structure_receiver, hierarchy_id):
        """Gets the session for subscribing to notifications of changes within a hierarchy structure for the given
        hierarchy.

        arg:    hierarchy_structure_receiver
                (osid.hierarchy.HierarchyStructureReceiver): a receiver
        arg:    hierarchy_id (osid.id.Id): the ``Id`` of the graph
        return: (osid.hierarchy.HierarchyStructureNotificationSession) -
                a ``HierarchyStructureNotificationSession``
        raise:  NotFound - ``hierarchy_id`` is not found
        raise:  NullArgument - ``hierarchy_structure_receiver`` or
                ``hierarchy_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_hierarchy_structure_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_structure_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.hierarchy.HierarchyStructureNotificationSession


    def get_hierarchy_lookup_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy lookup service.

        return: (osid.hierarchy.HierarchyLookupSession) - a
                ``HierarchyLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_lookup()`` is ``true``.*

        """
        return # osid.hierarchy.HierarchyLookupSession

    hierarchy_lookup_session = property(fget=get_hierarchy_lookup_session)


    def get_hierarchy_query_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy query service.

        return: (osid.hierarchy.HierarchyQuerySession) - a
                ``HierarchyQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_query()`` is ``true``.*

        """
        return # osid.hierarchy.HierarchyQuerySession

    hierarchy_query_session = property(fget=get_hierarchy_query_session)


    def get_hierarchy_search_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy search service.

        return: (osid.hierarchy.HierarchySearchSession) - a
                ``HierarchySearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_search()`` is ``true``.*

        """
        return # osid.hierarchy.HierarchySearchSession

    hierarchy_search_session = property(fget=get_hierarchy_search_session)


    def get_hierarchy_admin_session(self):
        """Gets the hierarchy administrative session.

        return: (osid.hierarchy.HierarchyAdminSession) - a
                ``HierarchyAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_admin()`` is ``true``.*

        """
        return # osid.hierarchy.HierarchyAdminSession

    hierarchy_admin_session = property(fget=get_hierarchy_admin_session)


    def get_hierarchy_notification_session(self, hierarchy_receiver):
        """Gets a hierarchy notification session.

        arg:    hierarchy_receiver (osid.hierarchy.HierarchyReceiver):
                notification callback
        return: (osid.hierarchy.HierarchyNotificationSession) - a
                ``HierarchyNotificationSession``
        raise:  NullArgument - ``hierarchy_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_hierarchy_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_hierarchy_notification()`` is ``true``.*

        """
        return # osid.hierarchy.HierarchyNotificationSession


