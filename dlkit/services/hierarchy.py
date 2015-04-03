# -*- coding: utf-8 -*-
"""Hierarchy Open Service Interface Definitions
hierarchy version 3.0.0

The Hierarchy OSID is an auxiliary service providing a means for
accessing and managing hierarchical relationships among OSID ``Ids``.

An OSID ``Id`` may have onr or more parents or children and the
hierarchy itself represents a directed acyclic graph. The hierarchy
service defines a set of interfaces used among other OSIDs that utilize
hierarchies and can also be used to abstract hierarchical data into a
standalone service.

Hierarchical queries may be performed using the
``HierarchyTraversalSession``. A set of methods exist to query parents,
children, ancestors, and decendants. A Node structure may be retrieved
to access a portion of a hierarchy in bulk. The ``Node`` provides
methods to get parents and children of the node directly.

Hierarchies are federateable by combining nodes. There is no hierarchy
service for the hierarchy catalog.

"""
from ..osid import managers as osid_managers
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class HierarchyProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if federation is visible.
        Visible federation allows for selecting among multiple
        hierarchies.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_hierarchy_traversal(self):
        """Tests if hierarchy traversal is supported.

        :return: ``true`` if hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_hierarchy_design(self):
        """Tests if hierarchy design is supported.

        :return: ``true`` if hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_hierarchy_sequencing(self):
        """Tests if hierarchy sequencing is supported.

        :return: ``true`` if hierarchy sequencing is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_hierarchy_structure_notification(self):
        """Tests if hierarchy structure notification is supported.

        :return: ``true`` if hierarchy structure notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_hierarchy_lookup(self):
        """Tests if a hierarchy lookup is supported.

        :return: ``true`` if hierarchy lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_hierarchy_query(self):
        """Tests if a hierarchy query is supported.

        :return: ``true`` if hierarchy query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_hierarchy_search(self):
        """Tests if a hierarchy search is supported.

        :return: ``true`` if hierarchy search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_hierarchy_admin(self):
        """Tests if a hierarchy administration is supported.

        :return: ``true`` if hierarchy administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_hierarchy_notification(self):
        """Tests if hierarchy notification is supported.
        Messages may be sent when hierarchies are created, modified, or
        deleted.

        :return: ``true`` if hierarchy notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_record_types(self):
        """Gets the supported ``Hierarchy`` types.

        :return: a list containing the supported ``Hierarchy`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    hierarchy_record_types = property(fget=get_hierarchy_record_types)

    def supports_hierarchy_record_type(self, hierarchy_record_type):
        """Tests if the given ``Hierarchy`` record type is supported.

        :param hierarchy_record_type: a ``Type`` indicating a ``Hierarchy`` record type
        :type hierarchy_record_type: ``osid.type.Type``
        :return: ``true`` if the given record Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``hierarchy_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_search_record_types(self):
        """Gets the supported ``Hierarchy`` search record types.

        :return: a list containing the supported ``Hierarchy`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    hierarchy_search_record_types = property(fget=get_hierarchy_search_record_types)

    def supports_hierarchy_search_record_type(self, hierarchy_search_record_type):
        """Tests if the given ``Hierarchy`` search record type is supported.

        :param hierarchy_search_record_type: a ``Type`` indicating a ``Hierarchy`` search record type
        :type hierarchy_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``hierarchy_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class HierarchyManager(osid_managers.OsidManager, osid_sessions.OsidSession, HierarchyProfile):

    def get_hierarchy_traversal_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service.

        :return: a ``HierarchyTraversalSession``
        :rtype: ``osid.hierarchy.HierarchyTraversalSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_traversal()`` is ``false``

        """
        raise UNIMPLEMENTED()

    hierarchy_traversal_session = property(fget=get_hierarchy_traversal_session)

    def get_hierarchy_traversal_session_for_hierarchy(self, hierarchy_id):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service for the given hierarchy.

        :param hierarchy_id: the ``Id`` of the hierarchy
        :type hierarchy_id: ``osid.id.Id``
        :return: the new ``HierarchyTraversalSession``
        :rtype: ``osid.hierarchy.HierarchyTraversalSession``
        :raise: ``NotFound`` -- ``hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``hierarchyid`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_hierarchy_traversal()`` or ``supports_visible_fedaration()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy design service.

        :return: a ``HierarchyDesignSession``
        :rtype: ``osid.hierarchy.HierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    hierarchy_design_session = property(fget=get_hierarchy_design_session)

    def get_hierarchy_design_session_for_hierarchy(self, hierarchy_id):
        """Gets the ``OsidSession`` associated with the topology design service using for the given hierarchy.

        :param hierarchy_id: the ``Id`` of the graph
        :type hierarchy_id: ``osid.id.Id``
        :return: a ``HierarchyDesignSession``
        :rtype: ``osid.hierarchy.HierarchyDesignSession``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_design()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_sequencing_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy sequencing service.

        :return: a ``HierarchySequencingSession``
        :rtype: ``osid.hierarchy.HierarchySequencingSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_sequencing()`` is ``false``

        """
        raise UNIMPLEMENTED()

    hierarchy_sequencing_session = property(fget=get_hierarchy_sequencing_session)

    def get_hierarchy_sequencing_session_for_hierarchy(self, hierarchy_id):
        """Gets the ``OsidSession`` associated with the sequencing design service using for the given hierarchy.

        :param hierarchy_id: the ``Id`` of the graph
        :type hierarchy_id: ``osid.id.Id``
        :return: a ``HierarchySequencingSession``
        :rtype: ``osid.hierarchy.HierarchySequencingSession``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_sequencing()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_structure_notification_session(self, hierarchy_structure_receiver):
        """Gets the session for subscribing to notifications of changes within a hierarchy structure.

        :param hierarchy_structure_receiver: a receiver
        :type hierarchy_structure_receiver: ``osid.hierarchy.HierarchyStructureReceiver``
        :return: a ``HierarchyStructureNotificationSession``
        :rtype: ``osid.hierarchy.HierarchyStructureNotificationSession``
        :raise: ``NullArgument`` -- ``hierarchy_structure_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_structure_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_structure_notification_session_for_hierarchy(self, hierarchy_structure_receiver, hierarchy_id):
        """Gets the session for subscribing to notifications of changes within a hierarchy structure for the given hierarchy.

        :param hierarchy_structure_receiver: a receiver
        :type hierarchy_structure_receiver: ``osid.hierarchy.HierarchyStructureReceiver``
        :param hierarchy_id: the ``Id`` of the graph
        :type hierarchy_id: ``osid.id.Id``
        :return: a ``HierarchyStructureNotificationSession``
        :rtype: ``osid.hierarchy.HierarchyStructureNotificationSession``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_structure_receiver`` or ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_structure_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_lookup_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy lookup service.

        :return: a ``HierarchyLookupSession``
        :rtype: ``osid.hierarchy.HierarchyLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    hierarchy_lookup_session = property(fget=get_hierarchy_lookup_session)

    def get_hierarchy_query_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy query service.

        :return: a ``HierarchyQuerySession``
        :rtype: ``osid.hierarchy.HierarchyQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    hierarchy_query_session = property(fget=get_hierarchy_query_session)

    def get_hierarchy_search_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy search service.

        :return: a ``HierarchySearchSession``
        :rtype: ``osid.hierarchy.HierarchySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    hierarchy_search_session = property(fget=get_hierarchy_search_session)

    def get_hierarchy_admin_session(self):
        """Gets the hierarchy administrative session.

        :return: a ``HierarchyAdminSession``
        :rtype: ``osid.hierarchy.HierarchyAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    hierarchy_admin_session = property(fget=get_hierarchy_admin_session)

    def get_hierarchy_notification_session(self, hierarchy_receiver):
        """Gets a hierarchy notification session.

        :param hierarchy_receiver: notification callback
        :type hierarchy_receiver: ``osid.hierarchy.HierarchyReceiver``
        :return: a ``HierarchyNotificationSession``
        :rtype: ``osid.hierarchy.HierarchyNotificationSession``
        :raise: ``NullArgument`` -- ``hierarchy_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.hierarchy.HierarchyTraversalSession

    def get_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    hierarchy_id = property(fget=get_hierarchy_id)

    def get_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    hierarchy = property(fget=get_hierarchy)

    def can_access_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_roots(self):
        """Gets the root nodes of this hierarchy.

        :return: the root nodes
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    roots = property(fget=get_roots)

    def has_parents(self, id_):
        """Tests if this ``Id`` contains any parents.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: ``true`` if this ``Id`` contains parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent(self, id_, parent_id):
        """Tests if an ``Id`` is a direct parent of another.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param parent_id: the ``Id`` of a parent
        :type parent_id: ``osid.id.Id``
        :return: ``true`` if this ``parent_id`` is a parent of ``id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``parent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parents(self, id_):
        """Gets the parents of the given ``id``.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: the parents of the ``id``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor(self, id_, ancestor_id):
        """Tests if an ``Id`` is an ancestor of another.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of an ancestor
        :type ancestor_id: ``osid.id.Id``
        :return: ``true`` if this ``ancestor_id`` is a parent of ``id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``ancestor_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_children(self, id_):
        """Tests if this ``Id`` has any children.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: ``true`` if this ``Id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child(self, id_, child_id):
        """Tests if a node is a direct child of another.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param child_id: the ``Id`` of a child
        :type child_id: ``osid.id.Id``
        :return: ``true`` if this ``child_id`` is a child of the ``Id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_children(self, id_):
        """Gets the children of the given ``Id``.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: the children of the ``id``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant(self, id_, descendant_id):
        """Tests if a node is a descendant of another.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of a descendant
        :type descendant_id: ``osid.id.Id``
        :return: ``true`` if this ``descendant_id`` is a child of the ``Id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``descendant`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_nodes(self, id_, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given ``Id``.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.hierarchy.HierarchyDesignSession

    def can_modify_hierarchy(self):
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

    def add_root(self, id_):
        """Adds a root node.

        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``id`` is already in hierarchy
        :raise: ``NotFound`` -- ``id`` not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child(self, id_, child_id):
        """Adds a child to a ``Id``.

        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``child_id`` is already a child of ``id``
        :raise: ``NotFound`` -- ``id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root(self, id_):
        """Removes a root node.

        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``id`` was not found or not in hierarchy
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child(self, id_, child_id):
        """Removes a childfrom an ``Id``.

        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :param child_id: the ``Id`` of the child to remove
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``id`` or ``child_id`` was not found or ``child_id`` is not a child of ``id``
        :raise: ``NullArgument`` -- ``id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_children(self, id_):
        """Removes all childrenfrom an ``Id``.

        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :raise: ``NotFound`` -- an node identified by the given ``Id`` was not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.hierarchy.HierarchySequencingSession

    def can_sequence_hierarchy(self):
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

    def move_node_ahead(self, parent_id, reference_id, id_):
        """Moves a node ahead of a refrence node under the given parent.

        :param parent_id: the ``Id`` of the parent node
        :type parent_id: ``osid.id.Id``
        :param reference_id: the ``Id`` of the node
        :type reference_id: ``osid.id.Id``
        :param id: the ``Id`` of the node to move ahead of ``reference_id``
        :type id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``parent_id, reference_id,`` or ``id`` not found, or ``reference_id`` or ``id`` is not a child of ``parent_id``
        :raise: ``NullArgument`` -- ``parent_id, reference_id,`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def move_node_behind(self, parent_id, reference_id, id_):
        """Moves a node behind a refrence node under the given parent.

        :param parent_id: the ``Id`` of the parent node
        :type parent_id: ``osid.id.Id``
        :param reference_id: the ``Id`` of the node
        :type reference_id: ``osid.id.Id``
        :param id: the ``Id`` of the node to move behind ``reference_id``
        :type id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``parent_id, reference_id,`` or ``id`` not found, or ``reference_id`` or ``id`` is not a child of ``parent_id``
        :raise: ``NullArgument`` -- ``parent_id, reference_id,`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def sequence_nodes(self, parent_id, ids):
        """Sequences a set of nodes under a parent.

        :param parent_id: the ``Id`` of the parent node
        :type parent_id: ``osid.id.Id``
        :param ids: the ``Id`` of the nodes
        :type ids: ``osid.id.Id[]``
        :raise: ``NotFound`` -- ``parent_id`` or an ``id`` not found, or an ``id`` is not a child of ``parent_id``
        :raise: ``NullArgument`` -- ``parent_id`` or ``ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.hierarchy.HierarchyStructureNotificationSession

    def can_register_for_hierarchy_structure_notifications(self):
        """Tests if this user can register for ``Hierarchy`` node notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_hierarchy_nodes(self):
        """Register for notifications of new hierarchy nodes.
        ``HierarchyStructureReceiver.newNode()`` is invoked when a new
        ``Hierarchy`` node is added.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_ancestor(self, node_id):
        """Registers for notification of an updated hierarchy structure that impacts the ancestors of the specified node.
        ``HierarchyStructureReceiver.newAncestor()`` or
        ``HierarchyStructureReceiver.deletedAncestor()`` is invoked when
        the specified hierarchy node experiences a change in ancestry.

        :param node_id: the ``Id`` of the ``hierarchy`` node to monitor
        :type node_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``node_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_descendant(self, node_id):
        """Registers for notification of an updated hierarchy structure that impacts the descendants of the specified node.
        ``HierarchyStructureReceiver.newDescendant()`` or
        ``HierarchyStructureReceiver.deletedDescendant()`` is invoked
        when the specified hierarchy node experiences a change in
        offspring.

        :param node_id: the ``Id`` of the ``hierarchy`` node to monitor
        :type node_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``node_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_hierarchy_nodes(self):
        """Registers for notification of deleted hierarchy nodes.
        ``HierarchyStructureReceiver.deletedNode()`` is invoked when a
        hierarchy ndoe is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_hierarchy_node(self, node_id):
        """Registers for notification of a deleted hierarchy node.
        ``HierarchyStructureReceiver.deletedNode()`` is invoked when the
        specified hierarchy node is deleted.

        :param node_id: the ``Id`` of the ``Hierarchy`` node to monitor
        :type node_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``node_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.hierarchy.HierarchyLookupSession

    def can_lookup_hierarchies(self):
        """Tests if this user can perform ``Hierarchy`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_hierarchy_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_hierarchy_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_hierarchies_by_ids(self, hierarchy_ids):
        """Gets a ``Hierarchy`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the
        hierarchies specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Hierarchy`` objects may be omitted from the list
        and may present the elements in any order including returning a
        unique set.

        :param hierarchy_ids: the list of ``Ids`` to retrieve
        :type hierarchy_ids: ``osid.id.IdList``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``hierarchy_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_hierarchies_by_genus_type(self, hierarchy_genus_type):
        """Gets a ``HierarchyList`` corresponding to the given genus ``Type`` which does not include hierarchies of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.

        :param hierarchy_genus_type: a hierarchy genus type
        :type hierarchy_genus_type: ``osid.type.Type``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``hierarchy_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_hierarchies_by_parent_genus_type(self, hierarchy_genus_type):
        """Gets a ``HierarchyList`` corresponding to the given hierarchy genus ``Type`` and include any additional hierarchies with types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.

        :param hierarchy_genus_type: a hierarchy genus type
        :type hierarchy_genus_type: ``osid.type.Type``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``hierarchy_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_hierarchies_by_record_type(self, hierarchy_record_type):
        """Gets a ``HierarchyList`` corresponding to the given hierarchy record ``Type``.
        The set of hierarchies implementing the given record type are
        returned.In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.

        :param hierarchy_record_type: a hierarchy record type
        :type hierarchy_record_type: ``osid.type.Type``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``hierarchy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_hierarchies_by_provider(self, resource_id):
        """Gets a ``HierarchyList`` for the given provider ````.
        The set of hierarchies implementing the given record type are
        returned.In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_hierarchies(self):
        """Gets all hierarchies.
        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.

        :return: a list of ``Hierarchies``
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    hierarchies = property(fget=get_hierarchies)


##
# The following methods are from osid.hierarchy.HierarchyQuerySession

    def can_search_hierarchies(self):
        """Tests if this user can perform ``Hierarchy`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_query(self):
        """Gets a hierarchy query.

        :return: the hierarchy query
        :rtype: ``osid.hierarchy.HierarchyQuery``

        """
        raise UNIMPLEMENTED()

    hierarchy_query = property(fget=get_hierarchy_query)

    def get_hierarchies_by_query(self, hierarchy_query):
        """Gets a list of ``Hierarchy`` objects matching the given hierarchy query.

        :param hierarchy_query: the hierarchy query
        :type hierarchy_query: ``osid.hierarchy.HierarchyQuery``
        :return: the returned ``HierarchyList``
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``hierarchy_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``hierarchy_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.hierarchy.HierarchySearchSession

    def get_hierarchy_search(self):
        """Gets a hierarchy search.

        :return: the hierarchy search
        :rtype: ``osid.hierarchy.HierarchySearch``

        """
        raise UNIMPLEMENTED()

    hierarchy_search = property(fget=get_hierarchy_search)

    def get_hierarchy_search_order(self):
        """Gets a hierarchy search order.
        The ``HierarchySearchOrder`` is supplied to a
        ``HierarchySearch`` to specify the ordering of results.

        :return: the hierarchy search order
        :rtype: ``osid.hierarchy.HierarchySearchOrder``

        """
        raise UNIMPLEMENTED()

    hierarchy_search_order = property(fget=get_hierarchy_search_order)

    def get_hierarchies_by_search(self, hierarchy_query, hierarchy_search):
        """Gets the search results matching the given search query using the given search.

        :param hierarchy_query: the hierarchy query
        :type hierarchy_query: ``osid.hierarchy.HierarchyQuery``
        :param hierarchy_search: the hierarchy search
        :type hierarchy_search: ``osid.hierarchy.HierarchySearch``
        :return: the hierarchy search results
        :rtype: ``osid.hierarchy.HierarchySearchResults``
        :raise: ``NullArgument`` -- ``hierarchy_query`` or ``hierarchy_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``hierarchy_query`` or ``hierarchy_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_query_from_inspector(self, hierarchy_query_inspector):
        """Gets a hierarchy query from an inspector.
        The inspector is available from a ``HierarchySearchResults``.

        :param hierarchy_query_inspector: a hierarchy query inspector
        :type hierarchy_query_inspector: ``osid.hierarchy.HierarchyQueryInspector``
        :return: the hierarchy query
        :rtype: ``osid.hierarchy.HierarchyQuery``
        :raise: ``NullArgument`` -- ``hierarchy_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``hierarchy_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.hierarchy.HierarchyAdminSession

    def can_create_hierarchies(self):
        """Tests if this user can create ``Hierarchy`` objects.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Hierarchy`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_hierarchy_with_record_types(self, hierarchy_record_types):
        """Tests if this user can create a single ``Hierarchy`` using the desired record types.
        While ``HierarchyManager.getHierarchyRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Hierarchy``.
        Providing an empty array tests if a ``Hierarchy`` can be created
        with no records.

        :param hierarchy_record_types: array of hierarchy record types
        :type hierarchy_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Hierarchy`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``hierarchy_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_form_for_create(self, hierarchy_record_types):
        """Gets the hierarchy form for creating new hierarchies.
        A new form should be requested for each create transaction. This
        method is used for creating new hierarchies, where only the
        ``Hierarchy`` ``Type`` is known.

        :param hierarchy_record_types: array of hierarchy record types
        :type hierarchy_record_types: ``osid.type.Type[]``
        :return: the hierarchy form
        :rtype: ``osid.hierarchy.HierarchyForm``
        :raise: ``NullArgument`` -- ``hierarchy_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_hierarchy(self, hierarchy_form):
        """Creates a new ``Hierarchy``.

        :param hierarchy_form: the form for this ``Hierarchy``
        :type hierarchy_form: ``osid.hierarchy.HierarchyForm``
        :return: the new ``Hierarchy``
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``IllegalState`` -- ``hierarchy_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``hierarchy_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``hierarchy_form`` did not originate from ``get_hierarchy_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_hierarchies(self):
        """Tests if this user can update ``Hierarchy`` objects.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Hierarchy`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_form_for_update(self, hierarchy_id):
        """Gets the hierarchy form for updating an existing hierarchy.
        A new hierarchy form should be requested for each update
        transaction.

        :param hierarchy_id: the ``Id`` of the ``Hierarchy``
        :type hierarchy_id: ``osid.id.Id``
        :return: the hierarchy form
        :rtype: ``osid.hierarchy.HierarchyForm``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_hierarchy(self, hierarchy_form):
        """Updates an existing hierarchy.

        :param hierarchy_form: the form containing the elements to be updated
        :type hierarchy_form: ``osid.hierarchy.HierarchyForm``
        :raise: ``IllegalState`` -- ``hierarchy_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``hierarchy_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``hierarchy_form`` did not originate from ``get_hierarchy_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_hierarchies(self):
        """Tests if this user can delete ``Hierarchy`` objects.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Hierarchy`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_hierarchy(self, hierarchy_id):
        """Deletes a ``Hierarchy``.

        :param hierarchy_id: the ``Id`` of the ``Hierarchy`` to remove
        :type hierarchy_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_hierarchy_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Hierarchy`` objects.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Hierarchy`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_hierarchy(self, hierarchy_id, alias_id):
        """Adds an ``Id`` to a ``Hierarchy`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Hierarchy`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another vault it is
        reassigned to the given vault ``Id``.

        :param hierarchy_id: the ``Id`` of an ``Hierarchy``
        :type hierarchy_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.hierarchy.HierarchyNotificationSession

    def can_register_for_hierarchy_notifications(self):
        """Tests if this user can register for ``Hierarchy`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_hierarchies(self):
        """Register for notifications of new hierarchies.
        ``HierarchyReceiver.newHierarchy()`` is invoked when a new
        ``Hierarchy`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_hierarchies(self):
        """Registers for notification of updated hierarchies.
        ``HierarchyReceiver.changedHierarchy()`` is invoked when a
        hierarchy is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_hierarchy(self, hierarchy_id):
        """Registers for notification of an updated hierarchy.
        ``HierarchyReceiver.changedHierarchy()`` is invoked when the
        specified hierarchy is changed.

        :param hierarchy_id: the ``Id`` of the ``hierarchy`` to monitor
        :type hierarchy_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_hierarchies(self):
        """Registers for notification of deleted hierarchies.
        ``HierarchyReceiver.deletedHierarchy()`` is invoked when a
        hierarchy is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_hierarchy(self, hierarchy_id):
        """Registers for notification of a deleted hierarchy.
        ``HierarchyReceiver.deletedHierarchy()`` is invoked when the
        specified hierarchy is deleted.

        :param hierarchy_id: the ``Id`` of the ``Hierarchy`` to monitor
        :type hierarchy_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class HierarchyProxyManager(osid_managers.OsidProxyManager, HierarchyProfile):

    def get_hierarchy_traversal_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyTraversalSession``
        :rtype: ``osid.hierarchy.HierarchyTraversalSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_traversal()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_traversal_session_for_hierarchy(self, hierarchy_id, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service for the given hierarchy.

        :param hierarchy_id: the ``Id`` of the hierarchy
        :type hierarchy_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyTraversalSession``
        :rtype: ``osid.hierarchy.HierarchyTraversalSession``
        :raise: ``NotFound`` -- ``hierarchyid`` not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_hierarchy_traversal()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyDesignSession``
        :rtype: ``osid.hierarchy.HierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_design_session_for_hierarchy(self, hierarchy_id, proxy):
        """Gets the ``OsidSession`` associated with the topology design service using for the given hierarchy.

        :param hierarchy_id: the ``Id`` of the hierarchy
        :type hierarchy_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyDesignSession``
        :rtype: ``osid.hierarchy.HierarchyDesignSession``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_design()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_sequencing_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy sequencing service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchySequencingSession``
        :rtype: ``osid.hierarchy.HierarchySequencingSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_sequencing()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_sequencing_session_for_hierarchy(self, hierarchy_id, proxy):
        """Gets the ``OsidSession`` associated with the sequencing design service using for the given hierarchy.

        :param hierarchy_id: the ``Id`` of the graph
        :type hierarchy_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchySequencingSession``
        :rtype: ``osid.hierarchy.HierarchySequencingSession``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_sequencing()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_structure_notification_session(self, hierarchy_structure_receiver, proxy):
        """Gets the session for subscribing to notifications of changes within a hierarchy structure.

        :param hierarchy_structure_receiver: a receiver
        :type hierarchy_structure_receiver: ``osid.hierarchy.HierarchyStructureReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyStructureNotificationSession``
        :rtype: ``osid.hierarchy.HierarchyStructureNotificationSession``
        :raise: ``NullArgument`` -- ``hierarchy_structure_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_structure_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_structure_notification_session_for_hierarchy(self, hierarchy_structure_receiver, hierarchy_id, proxy):
        """Gets the session for subscribing to notifications of changes within a hierarchy structure for the given hierarchy.

        :param hierarchy_structure_receiver: a receiver
        :type hierarchy_structure_receiver: ``osid.hierarchy.HierarchyStructureReceiver``
        :param hierarchy_id: the ``Id`` of the hierarchy
        :type hierarchy_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyStructureNotificationSession``
        :rtype: ``osid.hierarchy.HierarchyStructureNotificationSession``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_structure_receiver, hierarchy_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_structure_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyLookupSession``
        :rtype: ``osid.hierarchy.HierarchyLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyQuerySession``
        :rtype: ``osid.hierarchy.HierarchyQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchySearchSession``
        :rtype: ``osid.hierarchy.HierarchySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_admin_session(self, proxy):
        """Gets the hierarchy administrative session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyAdminSession``
        :rtype: ``osid.hierarchy.HierarchyAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_notification_session(self, hierarchy_receiver, proxy):
        """Gets the hierarchy notification session.

        :param hierarchy_receiver: notification callback
        :type hierarchy_receiver: ``osid.hierarchy.HierarchyReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyNotificationSession``
        :rtype: ``osid.hierarchy.HierarchyNotificationSession``
        :raise: ``NullArgument`` -- ``hierarchy_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.hierarchy.HierarchyTraversalSession

    def get_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    hierarchy_id = property(fget=get_hierarchy_id)

    def get_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    hierarchy = property(fget=get_hierarchy)

    def can_access_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.


        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_roots(self):
        """Gets the root nodes of this hierarchy.

        :return: the root nodes
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    roots = property(fget=get_roots)

    def has_parents(self, id_):
        """Tests if this ``Id`` contains any parents.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: ``true`` if this ``Id`` contains parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent(self, id_, parent_id):
        """Tests if an ``Id`` is a direct parent of another.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param parent_id: the ``Id`` of a parent
        :type parent_id: ``osid.id.Id``
        :return: ``true`` if this ``parent_id`` is a parent of ``id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``parent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parents(self, id_):
        """Gets the parents of the given ``id``.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: the parents of the ``id``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor(self, id_, ancestor_id):
        """Tests if an ``Id`` is an ancestor of another.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of an ancestor
        :type ancestor_id: ``osid.id.Id``
        :return: ``true`` if this ``ancestor_id`` is a parent of ``id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``ancestor_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_children(self, id_):
        """Tests if this ``Id`` has any children.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: ``true`` if this ``Id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child(self, id_, child_id):
        """Tests if a node is a direct child of another.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param child_id: the ``Id`` of a child
        :type child_id: ``osid.id.Id``
        :return: ``true`` if this ``child_id`` is a child of the ``Id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_children(self, id_):
        """Gets the children of the given ``Id``.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: the children of the ``id``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant(self, id_, descendant_id):
        """Tests if a node is a descendant of another.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of a descendant
        :type descendant_id: ``osid.id.Id``
        :return: ``true`` if this ``descendant_id`` is a child of the ``Id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``descendant`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_nodes(self, id_, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given ``Id``.

        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.hierarchy.HierarchyDesignSession

    def can_modify_hierarchy(self):
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

    def add_root(self, id_):
        """Adds a root node.

        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``id`` is already in hierarchy
        :raise: ``NotFound`` -- ``id`` not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child(self, id_, child_id):
        """Adds a child to a ``Id``.

        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``child_id`` is already a child of ``id``
        :raise: ``NotFound`` -- ``id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root(self, id_):
        """Removes a root node.

        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``id`` was not found or not in hierarchy
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child(self, id_, child_id):
        """Removes a childfrom an ``Id``.

        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :param child_id: the ``Id`` of the child to remove
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``id`` or ``child_id`` was not found or ``child_id`` is not a child of ``id``
        :raise: ``NullArgument`` -- ``id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_children(self, id_):
        """Removes all childrenfrom an ``Id``.

        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :raise: ``NotFound`` -- an node identified by the given ``Id`` was not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.hierarchy.HierarchySequencingSession

    def can_sequence_hierarchy(self):
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

    def move_node_ahead(self, parent_id, reference_id, id_):
        """Moves a node ahead of a refrence node under the given parent.

        :param parent_id: the ``Id`` of the parent node
        :type parent_id: ``osid.id.Id``
        :param reference_id: the ``Id`` of the node
        :type reference_id: ``osid.id.Id``
        :param id: the ``Id`` of the node to move ahead of ``reference_id``
        :type id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``parent_id, reference_id,`` or ``id`` not found, or ``reference_id`` or ``id`` is not a child of ``parent_id``
        :raise: ``NullArgument`` -- ``parent_id, reference_id,`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def move_node_behind(self, parent_id, reference_id, id_):
        """Moves a node behind a refrence node under the given parent.

        :param parent_id: the ``Id`` of the parent node
        :type parent_id: ``osid.id.Id``
        :param reference_id: the ``Id`` of the node
        :type reference_id: ``osid.id.Id``
        :param id: the ``Id`` of the node to move behind ``reference_id``
        :type id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``parent_id, reference_id,`` or ``id`` not found, or ``reference_id`` or ``id`` is not a child of ``parent_id``
        :raise: ``NullArgument`` -- ``parent_id, reference_id,`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def sequence_nodes(self, parent_id, ids):
        """Sequences a set of nodes under a parent.

        :param parent_id: the ``Id`` of the parent node
        :type parent_id: ``osid.id.Id``
        :param ids: the ``Id`` of the nodes
        :type ids: ``osid.id.Id[]``
        :raise: ``NotFound`` -- ``parent_id`` or an ``id`` not found, or an ``id`` is not a child of ``parent_id``
        :raise: ``NullArgument`` -- ``parent_id`` or ``ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.hierarchy.HierarchyStructureNotificationSession

    def can_register_for_hierarchy_structure_notifications(self):
        """Tests if this user can register for ``Hierarchy`` node notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.


        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_hierarchy_nodes(self):
        """Register for notifications of new hierarchy nodes.
        ``HierarchyStructureReceiver.newNode()`` is invoked when a new
        ``Hierarchy`` node is added.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_ancestor(self, node_id):
        """Registers for notification of an updated hierarchy structure that impacts the ancestors of the specified node.
        ``HierarchyStructureReceiver.newAncestor()`` or
        ``HierarchyStructureReceiver.deletedAncestor()`` is invoked when
        the specified hierarchy node experiences a change in ancestry.


        :param node_id: the ``Id`` of the ``hierarchy`` node to monitor
        :type node_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``node_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_descendant(self, node_id):
        """Registers for notification of an updated hierarchy structure that impacts the descendants of the specified node.
        ``HierarchyStructureReceiver.newDescendant()`` or
        ``HierarchyStructureReceiver.deletedDescendant()`` is invoked
        when the specified hierarchy node experiences a change in
        offspring.


        :param node_id: the ``Id`` of the ``hierarchy`` node to monitor
        :type node_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``node_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_hierarchy_nodes(self):
        """Registers for notification of deleted hierarchy nodes.
        ``HierarchyStructureReceiver.deletedNode()`` is invoked when a
        hierarchy ndoe is deleted.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_hierarchy_node(self, node_id):
        """Registers for notification of a deleted hierarchy node.
        ``HierarchyStructureReceiver.deletedNode()`` is invoked when the
        specified hierarchy node is deleted.


        :param node_id: the ``Id`` of the ``Hierarchy`` node to monitor
        :type node_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``node_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.hierarchy.HierarchyLookupSession

    def can_lookup_hierarchies(self):
        """Tests if this user can perform ``Hierarchy`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.


        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_hierarchy_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.




        """
        raise UNIMPLEMENTED()

    def use_plenary_hierarchy_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.




        """
        raise UNIMPLEMENTED()

    def get_hierarchies_by_ids(self, hierarchy_ids):
        """Gets a ``Hierarchy`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the
        hierarchies specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Hierarchy`` objects may be omitted from the list
        and may present the elements in any order including returning a
        unique set.


        :param hierarchy_ids: the list of ``Ids`` to retrieve
        :type hierarchy_ids: ``osid.id.IdList``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``hierarchy_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_hierarchies_by_genus_type(self, hierarchy_genus_type):
        """Gets a ``HierarchyList`` corresponding to the given genus ``Type`` which does not include hierarchies of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :param hierarchy_genus_type: a hierarchy genus type
        :type hierarchy_genus_type: ``osid.type.Type``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``hierarchy_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_hierarchies_by_parent_genus_type(self, hierarchy_genus_type):
        """Gets a ``HierarchyList`` corresponding to the given hierarchy genus ``Type`` and include any additional hierarchies with types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :param hierarchy_genus_type: a hierarchy genus type
        :type hierarchy_genus_type: ``osid.type.Type``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``hierarchy_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_hierarchies_by_record_type(self, hierarchy_record_type):
        """Gets a ``HierarchyList`` corresponding to the given hierarchy record ``Type``.
        The set of hierarchies implementing the given record type are
        returned.In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :param hierarchy_record_type: a hierarchy record type
        :type hierarchy_record_type: ``osid.type.Type``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``hierarchy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_hierarchies_by_provider(self, resource_id):
        """Gets a ``HierarchyList`` for the given provider ````.
        The set of hierarchies implementing the given record type are
        returned.In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_hierarchies(self):
        """Gets all hierarchies.
        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :return: a list of ``Hierarchies``
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    hierarchies = property(fget=get_hierarchies)


##
# The following methods are from osid.hierarchy.HierarchyQuerySession

    def can_search_hierarchies(self):
        """Tests if this user can perform ``Hierarchy`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_query(self):
        """Gets a hierarchy query.

        :return: the hierarchy query
        :rtype: ``osid.hierarchy.HierarchyQuery``

        """
        raise UNIMPLEMENTED()

    hierarchy_query = property(fget=get_hierarchy_query)

    def get_hierarchies_by_query(self, hierarchy_query):
        """Gets a list of ``Hierarchy`` objects matching the given hierarchy query.

        :param hierarchy_query: the hierarchy query
        :type hierarchy_query: ``osid.hierarchy.HierarchyQuery``
        :return: the returned ``HierarchyList``
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``hierarchy_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``hierarchy_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.hierarchy.HierarchySearchSession

    def get_hierarchy_search(self):
        """Gets a hierarchy search.

        :return: the hierarchy search
        :rtype: ``osid.hierarchy.HierarchySearch``

        """
        raise UNIMPLEMENTED()

    hierarchy_search = property(fget=get_hierarchy_search)

    def get_hierarchy_search_order(self):
        """Gets a hierarchy search order.
        The ``HierarchySearchOrder`` is supplied to a
        ``HierarchySearch`` to specify the ordering of results.


        :return: the hierarchy search order
        :rtype: ``osid.hierarchy.HierarchySearchOrder``

        """
        raise UNIMPLEMENTED()

    hierarchy_search_order = property(fget=get_hierarchy_search_order)

    def get_hierarchies_by_search(self, hierarchy_query, hierarchy_search):
        """Gets the search results matching the given search query using the given search.

        :param hierarchy_query: the hierarchy query
        :type hierarchy_query: ``osid.hierarchy.HierarchyQuery``
        :param hierarchy_search: the hierarchy search
        :type hierarchy_search: ``osid.hierarchy.HierarchySearch``
        :return: the hierarchy search results
        :rtype: ``osid.hierarchy.HierarchySearchResults``
        :raise: ``NullArgument`` -- ``hierarchy_query`` or ``hierarchy_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``hierarchy_query`` or ``hierarchy_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_query_from_inspector(self, hierarchy_query_inspector):
        """Gets a hierarchy query from an inspector.
        The inspector is available from a ``HierarchySearchResults``.


        :param hierarchy_query_inspector: a hierarchy query inspector
        :type hierarchy_query_inspector: ``osid.hierarchy.HierarchyQueryInspector``
        :return: the hierarchy query
        :rtype: ``osid.hierarchy.HierarchyQuery``
        :raise: ``NullArgument`` -- ``hierarchy_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``hierarchy_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.hierarchy.HierarchyAdminSession

    def can_create_hierarchies(self):
        """Tests if this user can create ``Hierarchy`` objects.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.


        :return: ``false`` if ``Hierarchy`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_hierarchy_with_record_types(self, hierarchy_record_types):
        """Tests if this user can create a single ``Hierarchy`` using the desired record types.
        While ``HierarchyManager.getHierarchyRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Hierarchy``.
        Providing an empty array tests if a ``Hierarchy`` can be created
        with no records.


        :param hierarchy_record_types: array of hierarchy record types
        :type hierarchy_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Hierarchy`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``hierarchy_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_form_for_create(self, hierarchy_record_types):
        """Gets the hierarchy form for creating new hierarchies.
        A new form should be requested for each create transaction. This
        method is used for creating new hierarchies, where only the
        ``Hierarchy`` ``Type`` is known.


        :param hierarchy_record_types: array of hierarchy record types
        :type hierarchy_record_types: ``osid.type.Type[]``
        :return: the hierarchy form
        :rtype: ``osid.hierarchy.HierarchyForm``
        :raise: ``NullArgument`` -- ``hierarchy_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_hierarchy(self, hierarchy_form):
        """Creates a new ``Hierarchy``.

        :param hierarchy_form: the form for this ``Hierarchy``
        :type hierarchy_form: ``osid.hierarchy.HierarchyForm``
        :return: the new ``Hierarchy``
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``IllegalState`` -- ``hierarchy_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``hierarchy_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``hierarchy_form`` did not originate from ``get_hierarchy_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_hierarchies(self):
        """Tests if this user can update ``Hierarchy`` objects.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.


        :return: ``false`` if ``Hierarchy`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_hierarchy_form_for_update(self, hierarchy_id):
        """Gets the hierarchy form for updating an existing hierarchy.
        A new hierarchy form should be requested for each update
        transaction.


        :param hierarchy_id: the ``Id`` of the ``Hierarchy``
        :type hierarchy_id: ``osid.id.Id``
        :return: the hierarchy form
        :rtype: ``osid.hierarchy.HierarchyForm``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_hierarchy(self, hierarchy_form):
        """Updates an existing hierarchy.

        :param hierarchy_form: the form containing the elements to be updated
        :type hierarchy_form: ``osid.hierarchy.HierarchyForm``
        :raise: ``IllegalState`` -- ``hierarchy_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``hierarchy_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``hierarchy_form`` did not originate from ``get_hierarchy_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_hierarchies(self):
        """Tests if this user can delete ``Hierarchy`` objects.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.


        :return: ``false`` if ``Hierarchy`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_hierarchy(self, hierarchy_id):
        """Deletes a ``Hierarchy``.

        :param hierarchy_id: the ``Id`` of the ``Hierarchy`` to remove
        :type hierarchy_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_hierarchy_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Hierarchy`` objects.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``Hierarchy`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_hierarchy(self, hierarchy_id, alias_id):
        """Adds an ``Id`` to a ``Hierarchy`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Hierarchy`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another vault it is
        reassigned to the given vault ``Id``.


        :param hierarchy_id: the ``Id`` of an ``Hierarchy``
        :type hierarchy_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.hierarchy.HierarchyNotificationSession

    def can_register_for_hierarchy_notifications(self):
        """Tests if this user can register for ``Hierarchy`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.


        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_hierarchies(self):
        """Register for notifications of new hierarchies.
        ``HierarchyReceiver.newHierarchy()`` is invoked when a new
        ``Hierarchy`` is created.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_hierarchies(self):
        """Registers for notification of updated hierarchies.
        ``HierarchyReceiver.changedHierarchy()`` is invoked when a
        hierarchy is changed.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_hierarchy(self, hierarchy_id):
        """Registers for notification of an updated hierarchy.
        ``HierarchyReceiver.changedHierarchy()`` is invoked when the
        specified hierarchy is changed.


        :param hierarchy_id: the ``Id`` of the ``hierarchy`` to monitor
        :type hierarchy_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_hierarchies(self):
        """Registers for notification of deleted hierarchies.
        ``HierarchyReceiver.deletedHierarchy()`` is invoked when a
        hierarchy is deleted.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_hierarchy(self, hierarchy_id):
        """Registers for notification of a deleted hierarchy.
        ``HierarchyReceiver.deletedHierarchy()`` is invoked when the
        specified hierarchy is deleted.


        :param hierarchy_id: the ``Id`` of the ``Hierarchy`` to monitor
        :type hierarchy_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class Hierarchy(osid_objects.OsidCatalog, osid_sessions.OsidSession):

    def get_hierarchy_record(self, hierarchy_record_type):
        """Gets the hierarchy record corresponding to the given ``Hierarchy`` record ``Type``.
        This method is used to retrieve an object implementing the
        requested record. The ``hierarchy_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(hierarchy_record_type)`` is ``true`` .

        :param hierarchy_record_type: the type of the record to retrieve
        :type hierarchy_record_type: ``osid.type.Type``
        :return: the hierarchy record
        :rtype: ``osid.hierarchy.records.HierarchyRecord``
        :raise: ``NullArgument`` -- ``hierarchy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(hierarchyrecord_type)`` is ``false``

        """
        raise UNIMPLEMENTED()



class HierarchyList(osid_objects.OsidList):

    def get_next_hierarchy(self):
        """Gets the next ``Hierarchy`` in this list.

        :return: the next ``Hierarchy`` in this list. The ``has_next()`` method should be used to test that a next ``Hierarchy`` is available before calling this method.
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    next_hierarchy = property(fget=get_next_hierarchy)

    def get_next_hierarchies(self, n):
        """Gets the next set of ``Hierarchy`` objects in this list.
        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Hierarchy`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Hierarchy`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()



class Hierarchies(HierarchyManager):
    pass


