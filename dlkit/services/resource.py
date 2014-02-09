# -*- coding: utf-8 -*-
"""Resource Open Service Interface Definitions
resource version 3.0.0

The Resource OSID defines a service to access and manage a directory of
objects.

Resources

``Resources`` may represent people, places or a set or arbitrary
entities that are used throughout the OSIDs as references to indirect
objects. In core OSID, ``Resources`` have no other meaning other than to
provide an identifier and a relation to an authentication principal.
``Resource``  ``Types`` may define extra data to define an employee,
organizational unit or an inventory item.

``Resources`` are referenced throughout the OSIDs to and the abstraction
level of this service provides a consistent interface with which to
access and manage object references not directly pertinent to the
service in play.. For example, a Repository OSID may reference
``Resources`` as authors or a Course OSID may reference ``Resources``
for students and instructors. Each of these OSIDs may orchestrate a
Resource OSID to provide management of the set of referenced resources.

A ``Resource`` genus Type may be used to provide a label the kind of
resource. This service offers the flexibility that the producer of a
film may be a person, a production company, or a fire hydrant. While
genus ``Types`` may be used to constrain the kinds of ``Resources`` that
may be related to various ``OsidObjects`` if necessary ``,`` OSID
Consumers are expected to simply use the Resource as a reference. If an
OSID Consumer wishes to provide a mechanism for updating a ``Resource``
referenced, the OSID Consumer should use an orchestrated Resource OSID.

Agents

A ``Resource`` also provides the mapping between an authentication
``Agent`` and the entity on whose behalf the agent is acting. An
``Agent`` can only map to a single ``Resource`` while a ``Resource`` can
have multiple ``Agents``. An agent that represents the unix login of
"vijay" on server due.mit.edu can map to a ``Resource`` representing
Vijay Kumar, who may also have a campus agent of "vkumar@mit.edu."

Group

When a ``Resource`` is referenced in another OSID, it is a singular
entity. To provide groupings of multiple people or things, a
``Resource`` can also be defined as a hierarchucal group of other
resources. Whether a resource is a single entity or a group is an
attribute of the ``Resource`` itself. If a ``Resource`` is a group, then
its membership can be queried or managed in one of the group sessions.
This overloading of the object definition serves to keep the nature of
the resource separate from the other OSIDs such that a message to a
"group", for example, is referenced as a single resource receipient.
Other OSIDs are blind to whether or not a referenced ``Resource`` is a
group or a singular entity.



Resource Relationships

For kicks, ``Resources`` may have arbitrrary relationships to other
``Resources`` using the ``ResourceRelationship`` interface. Resource
relationships may also be used to provide a place to describe in more
detail, or hang data, on a member to group relationship.

Bin Cataloging

``Resources`` may be mapped into hierarchial ``Bins`` for the purpose of
cataloging or federation.

Sub Packages

The Resource OSID includes a Resource Demographic OSID for managing
dynamically generated populations of ``Resources`` and a Resource Batch
OSID for managing ``Resources`` in bulk.

"""
from ..osid import managers as osid_managers
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class ResourceProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_lookup(self):
        """Tests if resource lookup is supported.

        :return: ``true`` if resource lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_query(self):
        """Tests if resource query is supported.

        :return: ``true`` if resource query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_search(self):
        """Tests if resource search is supported.

        :return: ``true`` if resource search is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_admin(self):
        """Tests if resource administration is supported.

        :return: ``true`` if resource administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_notification(self):
        """Tests if resource notification is supported.
        Messages may be sent when resources are created, modified, or
        deleted.

        :return: ``true`` if resource notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_bin(self):
        """Tests if retrieving mappings of resource and bins is supported.

        :return: ``true`` if resource bin mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_bin_assignment(self):
        """Tests if managing mappings of resource and bins is supported.

        :return: ``true`` if resource bin assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_smart_bin(self):
        """Tests if resource smart bins are available.

        :return: ``true`` if resource smart bins are supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_membership(self):
        """Tests if membership queries are supported.

        :return: ``true`` if membership queries are supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_group(self):
        """Tests if group resources are supported.

        :return: ``true`` if group resources are supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_group_assignment(self):
        """Tests if group resource assignment is supported.

        :return: ``true`` if group resource assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_group_notification(self):
        """Tests if group resource notification is supported.

        :return: ``true`` if group resource notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_group_hierarchy(self):
        """Tests if a group resource hierarchy service is supported.

        :return: ``true`` if group resource hierarchy is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_agent(self):
        """Tests if retrieving mappings of resource and agents is supported.

        :return: ``true`` if resource agent mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_agent_assignment(self):
        """Tests if managing mappings of resources and agents is supported.

        :return: ``true`` if resource agent assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_relationship_lookup(self):
        """Tests if looking up resource relationships is supported.

        :return: ``true`` if resource relationships lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_relationship_query(self):
        """Tests if querying resource relationships is supported.

        :return: ``true`` if resource relationships query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_relationship_search(self):
        """Tests if searching resource relationships is supported.

        :return: ``true`` if resource relationships search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_relationship_admin(self):
        """Tests if a resource relationshipsadministrative service is supported.

        :return: ``true`` if resource relationships administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_relationship_notification(self):
        """Tests if a resource relationshipsnotification service is supported.

        :return: ``true`` if resource relationships notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_relationship_bin(self):
        """Tests if retrieving mappings of resource relationships and bins is supported.

        :return: ``true`` if resource relationship bin mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_relationship_bin_assignment(self):
        """Tests if managing mappings of resource relationships and bins is supported.

        :return: ``true`` if resource relationship bin assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_relationship_smart_bin(self):
        """Tests if resource relationship smart bins are available.

        :return: ``true`` if resource relationship smart bins are supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_bin_lookup(self):
        """Tests if bin lookup is supported.

        :return: ``true`` if bin lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_bin_query(self):
        """Tests if bin query is supported.

        :return: ``true`` if bin query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_bin_search(self):
        """Tests if bin search is supported.

        :return: ``true`` if bin search is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_bin_admin(self):
        """Tests if bin administration is supported.

        :return: ``true`` if bin administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_bin_notification(self):
        """Tests if bin notification is supported.
        Messages may be sent when ``Bin`` objects are created, deleted
        or updated. Notifications for resources within bins are sent via
        the resource notification session.

        :return: ``true`` if bin notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_bin_hierarchy(self):
        """Tests if a bin hierarchy traversal is supported.

        :return: ``true`` if a bin hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_bin_hierarchy_design(self):
        """Tests if a bin hierarchy design is supported.

        :return: ``true`` if a bin hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_batch(self):
        """Tests if a resource batch service is available.

        :return: ``true`` if a resource batch service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_demographic(self):
        """Tests if a resource demographic service is available.

        :return: ``true`` if a resource demographic service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_resource_record_types(self):
        """Gets all the resource record types supported.

        :return: the list of supported resource record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    resource_record_types = property(fget=get_resource_record_types)

    def supports_resource_record_type(self, resource_record_type):
        """Tests if a given resource record type is supported.

        :param resource_record_type: the resource type
        :type resource_record_type: ``osid.type.Type``
        :return: ``true`` if the resource record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``resource_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_resource_search_record_types(self):
        """Gets all the resource search record types supported.

        :return: the list of supported resource search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    resource_search_record_types = property(fget=get_resource_search_record_types)

    def supports_resource_search_record_type(self, resource_search_record_type):
        """Tests if a given resource search type is supported.

        :param resource_search_record_type: the resource search type
        :type resource_search_record_type: ``osid.type.Type``
        :return: ``true`` if the resource search record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``resource_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_record_types(self):
        """Gets the supported ``ResourceRelationship`` record types.

        :return: a list containing the supported ``ResourceRelationship`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    resource_relationship_record_types = property(fget=get_resource_relationship_record_types)

    def supports_resource_relationship_record_type(self, resource_relationship_record_type):
        """Tests if the given ``ResourceRelationship`` record type is supported.

        :param resource_relationship_record_type: a ``Type`` indicating a ``ResourceRelationship`` record type
        :type resource_relationship_record_type: ``osid.type.Type``
        :return: ``true`` if the given type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``resource_relationship_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_search_record_types(self):
        """Gets the supported ``ResourceRelationship`` search record types.

        :return: a list containing the supported ``ResourceRelationship`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    resource_relationship_search_record_types = property(fget=get_resource_relationship_search_record_types)

    def supports_resource_relationship_search_record_type(self, resource_relationship_search_record_type):
        """Tests if the given ``ResourceRelationship`` search record type is supported.

        :param resource_relationship_search_record_type: a ``Type`` indicating a ``ResourceRelationship`` search record type
        :type resource_relationship_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``resource_relationship_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_bin_record_types(self):
        """Gets all the bin record types supported.

        :return: the list of supported bin record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    bin_record_types = property(fget=get_bin_record_types)

    def supports_bin_record_type(self, bin_record_type):
        """Tests if a given bin record type is supported.

        :param bin_record_type: the bin record type
        :type bin_record_type: ``osid.type.Type``
        :return: ``true`` if the bin record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bin_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_bin_search_record_types(self):
        """Gets all the bin search record types supported.

        :return: the list of supported bin search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    bin_search_record_types = property(fget=get_bin_search_record_types)

    def supports_bin_search_record_type(self, bin_search_record_type):
        """Tests if a given bin search record type is supported.

        :param bin_search_record_type: the bin search record type
        :type bin_search_record_type: ``osid.type.Type``
        :return: ``true`` if the bin search record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bin_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class ResourceManager(osid_managers.OsidManager, osid_sessions.OsidSession, ResourceProfile):

    def get_resource_lookup_session(self):
        """Gets the ``OsidSession`` associated with the resource lookup service.

        :return: ``a ResourceLookupSession``
        :rtype: ``osid.resource.ResourceLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_lookup_session = property(fget=get_resource_lookup_session)

    def get_resource_lookup_session_for_bin(self, bin_id):
        """Gets the ``OsidSession`` associated with the resource lookup service for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: ``a ResourceLookupSession``
        :rtype: ``osid.resource.ResourceLookupSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_resource_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_query_session(self):
        """Gets a resource query session.

        :return: ``a ResourceQuerySession``
        :rtype: ``osid.resource.ResourceQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_query_session = property(fget=get_resource_query_session)

    def get_resource_query_session_for_bin(self, bin_id):
        """Gets a resource query session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: ``a ResourceQuerySession``
        :rtype: ``osid.resource.ResourceQuerySession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_search_session(self):
        """Gets a resource search session.

        :return: ``a ResourceSearchSession``
        :rtype: ``osid.resource.ResourceSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_search_session = property(fget=get_resource_search_session)

    def get_resource_search_session_for_bin(self, bin_id):
        """Gets a resource search session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: ``a ResourceSearchSession``
        :rtype: ``osid.resource.ResourceSearchSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_resource_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_admin_session(self):
        """Gets a resource administration session for creating, updating and deleting resources.

        :return: ``a ResourceAdminSession``
        :rtype: ``osid.resource.ResourceAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_admin_session = property(fget=get_resource_admin_session)

    def get_resource_admin_session_for_bin(self, bin_id):
        """Gets a resource administration session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: ``a ResourceAdminSession``
        :rtype: ``osid.resource.ResourceAdminSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_notification_session(self, resource_receiver):
        """Gets the notification session for notifications pertaining to resource changes.

        :param resource_receiver: the notification callback
        :type resource_receiver: ``osid.resource.ResourceReceiver``
        :return: ``a ResourceNotificationSession``
        :rtype: ``osid.resource.ResourceNotificationSession``
        :raise: ``NullArgument`` -- ``resource_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_notification_session_for_bin(self, resource_receiver, bin_id):
        """Gets the resource notification session for the given bin.

        :param resource_receiver: the notification callback
        :type resource_receiver: ``osid.resource.ResourceReceiver``
        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: ``a ResourceNotificationSession``
        :rtype: ``osid.resource.ResourceNotificationSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``resource_receiver`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_resource_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_bin_session(self):
        """Gets the session for retrieving resource to bin mappings.

        :return: a ``ResourceBinSession``
        :rtype: ``osid.resource.ResourceBinSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_bin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_bin_session = property(fget=get_resource_bin_session)

    def get_resource_bin_assignment_session(self):
        """Gets the session for assigning resource to bin mappings.

        :return: a ``ResourceBinAssignmentSession``
        :rtype: ``osid.resource.ResourceBinAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_bin_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_bin_assignment_session = property(fget=get_resource_bin_assignment_session)

    def get_resource_smart_bin_session(self, bin_id):
        """Gets the session for managing dynamic resource bins.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceSmartBinSession``
        :rtype: ``osid.resource.ResourceSmartBinSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_smart_bin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_membership_session(self):
        """Gets the session for querying memberships.

        :return: a ``MembershipSession``
        :rtype: ``osid.resource.MembershipSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_membership()`` is ``false``

        """
        raise UNIMPLEMENTED()

    membership_session = property(fget=get_membership_session)

    def get_membership_session_for_bin(self, bin_id):
        """Gets a resource membership session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: ``a MembershipSession``
        :rtype: ``osid.resource.MembershipSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_membership()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_group_session(self):
        """Gets the session for retrieving gropup memberships.

        :return: a ``GroupSession``
        :rtype: ``osid.resource.GroupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group()`` is ``false``

        """
        raise UNIMPLEMENTED()

    group_session = property(fget=get_group_session)

    def get_group_session_for_bin(self, bin_id):
        """Gets a group session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: a ``GroupSession``
        :rtype: ``osid.resource.GroupSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_group_assignment_session(self):
        """Gets the session for assigning resources to groups.

        :return: a ``GroupAssignmentSession``
        :rtype: ``osid.resource.GroupAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    group_assignment_session = property(fget=get_group_assignment_session)

    def get_group_assignment_session_for_bin(self, bin_id):
        """Gets a group assignment session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: a ``GroupAssignmentSession``
        :rtype: ``osid.resource.GroupAssignmentSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_assignment()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_group_notification_session(self, group_rceeiver):
        """Gets the notification session for notifications pertaining to resource changes.

        :param group_rceeiver: the notification callback
        :type group_rceeiver: ``osid.resource.GroupReceiver``
        :return: ``a GroupNotificationSession``
        :rtype: ``osid.resource.GroupNotificationSession``
        :raise: ``NullArgument`` -- ``group_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_group_notification_session_for_bin(self, group_rceeiver, bin_id):
        """Gets the group notification session for the given bin.

        :param group_rceeiver: the notification callback
        :type group_rceeiver: ``osid.resource.GroupReceiver``
        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: ``a GroupNotificationSession``
        :rtype: ``osid.resource.GroupNotificationSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``group_receiver`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_group_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_group_hierarchy_session(self):
        """Gets a session for retrieving gropup hierarchies.

        :return: ``a GroupHierarchySession``
        :rtype: ``osid.resource.GroupHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    group_hierarchy_session = property(fget=get_group_hierarchy_session)

    def get_group_hierarchy_session_for_bin(self, bin_id):
        """Gets a group hierarchy session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: a ``GroupHierarchySession``
        :rtype: ``osid.resource.GroupHierarchySession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_hierarchy()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_agent_session(self):
        """Gets the session for retrieving resource agent mappings.

        :return: a ``ResourceAgentSession``
        :rtype: ``osid.resource.ResourceAgentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_agent()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_agent_session = property(fget=get_resource_agent_session)

    def get_resource_agent_session_for_bin(self, bin_id):
        """Gets a resource agent session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceAgentSession``
        :rtype: ``osid.resource.ResourceAgentSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_agent()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_agent_assignment_session(self):
        """Gets the session for assigning agents to resources.

        :return: a ``ResourceAgentAssignmentSession``
        :rtype: ``osid.resource.ResourceAgentAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_agent_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_agent_assignment_session = property(fget=get_resource_agent_assignment_session)

    def get_resource_agent_assignment_session_for_bin(self, bin_id):
        """Gets a resource agent session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceAgentAssignmentSession``
        :rtype: ``osid.resource.ResourceAgentAssignmentSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_agent_assignment()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_lookup_session(self):
        """Gets the ``OsidSession`` associated with the resource relationship lookup service.

        :return: a ``ResourceRelationshipLookupSession``
        :rtype: ``osid.resource.ResourceRelationshipLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_relationship_lookup_session = property(fget=get_resource_relationship_lookup_session)

    def get_resource_relationship_lookup_session_for_bin(self, bin_id):
        """Gets the ``OsidSession`` associated with the resource relationship lookup service for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceRelationshipLookupSession``
        :rtype: ``osid.resource.ResourceRelationshipLookupSession``
        :raise: ``NotFound`` -- no ``Bin`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_query_session(self):
        """Gets the ``OsidSession`` associated with the resource relationship query service.

        :return: a ``ResourceRelationshipQuerySession``
        :rtype: ``osid.resource.ResourceRelationshipQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_relationship_query_session = property(fget=get_resource_relationship_query_session)

    def get_resource_relationship_query_session_for_bin(self, bin_id):
        """Gets the ``OsidSession`` associated with the resource relationship query service for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceRelationshipQuerySession``
        :rtype: ``osid.resource.ResourceRelationshipQuerySession``
        :raise: ``NotFound`` -- no ``Bin`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_search_session(self):
        """Gets the ``OsidSession`` associated with the resource relationship search service.

        :return: a ``ResourceRelationshipSearchSession``
        :rtype: ``osid.resource.ResourceRelationshipSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_relationship_search_session = property(fget=get_resource_relationship_search_session)

    def get_resource_relationship_search_session_for_bin(self, bin_id):
        """Gets the ``OsidSession`` associated with the resource relationship search service for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceRelationshipSearchSession``
        :rtype: ``osid.resource.ResourceRelationshipSearchSession``
        :raise: ``NotFound`` -- no bin found by the given ``Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_admin_session(self):
        """Gets the ``OsidSession`` associated with the resource relationship administration service.

        :return: a ``ResourceRelationshipAdminSession``
        :rtype: ``osid.resource.ResourceRelationshipAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_relationship_admin_session = property(fget=get_resource_relationship_admin_session)

    def get_resource_relationship_admin_session_for_bin(self, bin_id):
        """Gets the ``OsidSession`` associated with the resource relationship administration service for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceRelationshipAdminSession``
        :rtype: ``osid.resource.ResourceRelationshipAdminSession``
        :raise: ``NotFound`` -- no bin found by the given ``Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_notification_session(self, resource_relationship_receiver):
        """Gets the ``OsidSession`` associated with the resource relationship notification service.

        :param resource_relationship_receiver: the notification callback
        :type resource_relationship_receiver: ``osid.resource.ResourceRelationshipReceiver``
        :return: a ``ResourceRelationshipNotificationSession``
        :rtype: ``osid.resource.ResourceRelationshipNotificationSession``
        :raise: ``NullArgument`` -- ``resource_relationship_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_notification_session_for_bin(self, resource_relationship_receiver, bin_id):
        """Gets the ``OsidSession`` associated with the resource relationship notification service for the given bin.

        :param resource_relationship_receiver: the notification callback
        :type resource_relationship_receiver: ``osid.resource.ResourceRelationshipReceiver``
        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceRelationshipNotificationSession``
        :rtype: ``osid.resource.ResourceRelationshipNotificationSession``
        :raise: ``NotFound`` -- no bin found by the given ``Id``
        :raise: ``NullArgument`` -- ``resource_relationship_receiver`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationshipt_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_bin_session(self):
        """Gets the session for retrieving resource relationship to bin mappings.

        :return: a ``ResourceRelationshipBinSession``
        :rtype: ``osid.resource.ResourceRelationshipBinSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_bin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_relationship_bin_session = property(fget=get_resource_relationship_bin_session)

    def get_resource_relationship_bin_assignment_session(self):
        """Gets the session for assigning resource relationships to bin mappings.

        :return: a ``ResourceRelationshipBinAssignmentSession``
        :rtype: ``osid.resource.ResourceRelationshipBinAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_bin_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_relationship_bin_assignment_session = property(fget=get_resource_relationship_bin_assignment_session)

    def get_resource_relationship_smart_bin_session(self, bin_id):
        """Gets the session for managing dynamic resource relationship bins.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :return: a ``ResourceRelationshipSmartBinSession``
        :rtype: ``osid.resource.ResourceRelationshipSmartBinSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_smart_bin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_bin_lookup_session(self):
        """Gets the bin lookup session.

        :return: a ``BinLookupSession``
        :rtype: ``osid.resource.BinLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    bin_lookup_session = property(fget=get_bin_lookup_session)

    def get_bin_query_session(self):
        """Gets the bin query session.

        :return: a ``BinQuerySession``
        :rtype: ``osid.resource.BinQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    bin_query_session = property(fget=get_bin_query_session)

    def get_bin_search_session(self):
        """Gets the bin search session.

        :return: a ``BinSearchSession``
        :rtype: ``osid.resource.BinSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    bin_search_session = property(fget=get_bin_search_session)

    def get_bin_admin_session(self):
        """Gets the bin administrative session for creating, updating and deleteing bins.

        :return: a ``BinAdminSession``
        :rtype: ``osid.resource.BinAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    bin_admin_session = property(fget=get_bin_admin_session)

    def get_bin_notification_session(self, bin_receiver):
        """Gets the notification session for subscribing to changes to a bin.

        :param bin_receiver: the notification callback
        :type bin_receiver: ``osid.resource.BinReceiver``
        :return: a ``BinNotificationSession``
        :rtype: ``osid.resource.BinNotificationSession``
        :raise: ``NullArgument`` -- ``bin_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_bin_hierarchy_session(self):
        """Gets the bin hierarchy traversal session.

        :return: ``a BinHierarchySession``
        :rtype: ``osid.resource.BinHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    bin_hierarchy_session = property(fget=get_bin_hierarchy_session)

    def get_bin_hierarchy_design_session(self):
        """Gets the bin hierarchy design session.

        :return: a ``BinHierarchyDesignSession``
        :rtype: ``osid.resource.BinHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    bin_hierarchy_design_session = property(fget=get_bin_hierarchy_design_session)

    def get_resource_batch_manager(self):
        """Gets the ``ResourceBatchManager``.

        :return: a ``ResourceBatchManager``
        :rtype: ``osid.resource.batch.ResourceBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_batch_manager = property(fget=get_resource_batch_manager)

    def get_resource_demographic_manager(self):
        """Gets the ``ResourceDemographicManager``.

        :return: a ``ResourceDemographicManager``
        :rtype: ``osid.resource.demographic.ResourceDemographicManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_demographic()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_demographic_manager = property(fget=get_resource_demographic_manager)


##
# The following methods are from osid.resource.BinLookupSession

    def can_lookup_bins(self):
        """Tests if this user can perform ``Bin`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_bin_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_bin_view(self):
        """A complete view of the ``Bin`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_bin(self, bin_id):
        """Gets the ``Bin`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Bin`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Bin`` and retained for compatibility.

        :param bin_id: ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: the bin
        :rtype: ``osid.resource.Bin``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bins_by_ids(self, bin_ids):
        """Gets a ``BinList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the bins
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Bins`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param bin_ids: the list of ``Ids`` to retrieve
        :type bin_ids: ``osid.id.IdList``
        :return: the returned ``Bin list``
        :rtype: ``osid.resource.BinList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``bin_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bins_by_genus_type(self, bin_genus_type):
        """Gets a ``BinList`` corresponding to the given bin genus ``Type`` which does not include bins of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :param bin_genus_type: a bin genus type
        :type bin_genus_type: ``osid.type.Type``
        :return: the returned ``Bin list``
        :rtype: ``osid.resource.BinList``
        :raise: ``NullArgument`` -- ``bin_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bins_by_parent_genus_type(self, bin_genus_type):
        """Gets a ``BinList`` corresponding to the given bin genus ``Type`` and include any additional bins with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :param bin_genus_type: a bin genus type
        :type bin_genus_type: ``osid.type.Type``
        :return: the returned ``Bin list``
        :rtype: ``osid.resource.BinList``
        :raise: ``NullArgument`` -- ``bin_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bins_by_record_type(self, bin_record_type):
        """Gets a ``BinList`` containing the given bin record ``Type``.
        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :param bin_record_type: a bin record type
        :type bin_record_type: ``osid.type.Type``
        :return: the returned ``Bin list``
        :rtype: ``osid.resource.BinList``
        :raise: ``NullArgument`` -- ``bin_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bins_by_provider(self, resource_id):
        """Gets a ``BinList`` from the given provider.
        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Bin list``
        :rtype: ``osid.resource.BinList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bins(self):
        """Gets all ``Bins``.
        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :return: a list of ``Bins``
        :rtype: ``osid.resource.BinList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    bins = property(fget=get_bins)


##
# The following methods are from osid.resource.BinQuerySession

    def can_search_bins(self):
        """Tests if this user can perform ``Bin`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_bin_query(self):
        """Gets a bin query.
        The returned query will not have an extension query.

        :return: the bin query
        :rtype: ``osid.resource.BinQuery``

        """
        raise UNIMPLEMENTED()

    bin_query = property(fget=get_bin_query)

    def get_bins_by_query(self, bin_query):
        """Gets a list of ``Bins`` matching the given bin query.

        :param bin_query: the bin query
        :type bin_query: ``osid.resource.BinQuery``
        :return: the returned ``BinList``
        :rtype: ``osid.resource.BinList``
        :raise: ``NullArgument`` -- ``bin_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- a ``bin_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.BinSearchSession

    def get_bin_search(self):
        """Gets a bin search.

        :return: the bin search
        :rtype: ``osid.resource.BinSearch``

        """
        raise UNIMPLEMENTED()

    bin_search = property(fget=get_bin_search)

    def get_bin_search_order(self):
        """Gets a bin search order.
        The ``BinSearchOrder`` is supplied to a ``BinSearch`` to specify
        the ordering of results.

        :return: the bin search order
        :rtype: ``osid.resource.BinSearchOrder``

        """
        raise UNIMPLEMENTED()

    bin_search_order = property(fget=get_bin_search_order)

    def get_bins_by_search(self, bin_query, bin_search):
        """Gets the search results matching the given search query using the given search.

        :param bin_query: the bin query
        :type bin_query: ``osid.resource.BinQuery``
        :param bin_search: the bin search
        :type bin_search: ``osid.resource.BinSearch``
        :return: the bin search results
        :rtype: ``osid.resource.BinSearchResults``
        :raise: ``NullArgument`` -- ``bin_query`` or ``bin_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``bin_query`` or ``bin_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_bin_query_from_inspector(self, bin_query_inspector):
        """Gets a bin query from an inspector.
        The inspector is available from a ``BinSearchResults``.

        :param bin_query_inspector: a bin query inspector
        :type bin_query_inspector: ``osid.resource.BinQueryInspector``
        :return: the bin query
        :rtype: ``osid.resource.BinQuery``
        :raise: ``NullArgument`` -- ``bin_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``bin_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.BinAdminSession

    def can_create_bins(self):
        """Tests if this user can create ``Bins``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Bin`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_bin_with_record_types(self, bin_record_types):
        """Tests if this user can create a single ``Bin`` using the desired record types.
        While ``ResourceManager.getBinRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Bin``.
        Providing an empty array tests if a ``Bin`` can be created with
        no records.

        :param bin_record_types: array of bin record types
        :type bin_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Bin`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bin_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_bin_form_for_create(self, bin_record_types):
        """Gets the bin form for creating new bins.

        :param bin_record_types: array of bin record types
        :type bin_record_types: ``osid.type.Type[]``
        :return: the bin form
        :rtype: ``osid.resource.BinForm``
        :raise: ``NullArgument`` -- ``bin_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        """
        raise UNIMPLEMENTED()

    def create_bin(self, bin_form):
        """Creates a new ``Bin``.

        :param bin_form: the form for this ``Bin``
        :type bin_form: ``osid.resource.BinForm``
        :return: the new ``Bin``
        :rtype: ``osid.resource.Bin``
        :raise: ``IllegalState`` -- ``bin_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``bin_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``bin_form`` did not originate from ``get_bin_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_bins(self):
        """Tests if this user can update ``Bins``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Bin`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_bin_form_for_update(self, bin_id):
        """Gets the bin form for updating an existing bin.
        A new bin form should be requested for each update transaction.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: the bin form
        :rtype: ``osid.resource.BinForm``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_bin(self, bin_form):
        """Updates an existing bin.

        :param bin_form: the form containing the elements to be updated
        :type bin_form: ``osid.resource.BinForm``
        :raise: ``IllegalState`` -- ``bin_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``bin_id`` or ``bin_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``bin_form`` did not originate from ``get_bin_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_bins(self):
        """Tests if this user can delete ``Bins``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Bin`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_bin(self, bin_id):
        """Deletes a ``Bin``.

        :param bin_id: the ``Id`` of the ``Bin`` to remove
        :type bin_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_bin_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Bins``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Bin`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_bin(self, bin_id, alias_id):
        """Adds an ``Id`` to a ``Bin`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Bin`` is determined by the provider.
        The new ``Id`` performs as an alias to the primary ``Id``. If
        the alias is a pointer to another bin, it is reassigned to the
        given bin ``Id``.

        :param bin_id: the ``Id`` of a ``Bin``
        :type bin_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.BinNotificationSession

    def can_register_for_bin_notifications(self):
        """Tests if this user can register for ``Bin`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_bins(self):
        """Register for notifications of new bins.
        ``BinReceiver.newBin()`` is invoked when a new ``Bin`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_bin_ancestors(self, bin_id):
        """Registers for notification if an ancestor is added to the specified bin in the bin hierarchy.
        ``BinReceiver.newBinAncestor()`` is invoked when the specified
        bin experiences an addition in ancestry.

        :param bin_id: the ``Id`` of the bin to monitor
        :type bin_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_bin_descendants(self, bin_id):
        """Registers for notification if a descendant is added to the specified bin in the bin hierarchy.
        ``BinReceiver.newBinDescendant()`` is invoked when the specified
        bin experiences an addition in descendants.

        :param bin_id: the ``Id`` of the bin to monitor
        :type bin_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_bins(self):
        """Registers for notification of updated bins.
        ``BinReceiver.changedBin()`` is invoked when a bin is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_bin(self, bin_id):
        """Registers for notification of an updated bin.
        ``BinReceiver.changedBin()`` is invoked when the specified bin
        is changed.

        :param bin_id: the Id of the Bin to monitor
        :type bin_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_bins(self):
        """Registers for notification of deleted bins.
        ``BinReceiver.deletedBin()`` is invoked when a bin is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_bin(self, bin_id):
        """Registers for notification of a deleted bin.
        ``BinReceiver.deletedBin()`` is invoked when the specified bin
        is deleted.

        :param bin_id: the ``Id`` of the ``Bin`` to monitor
        :type bin_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_bin_ancestors(self, bin_id):
        """Registers for notification if an ancestor is removed from the specified bin in the bin hierarchy.
        ``BinReceiver.deletedBinAncestor()`` is invoked when the
        specified bin experiences a removal of an ancestor.

        :param bin_id: the ``Id`` of the bin to monitor
        :type bin_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_bin_descendants(self, bin_id):
        """Registers for notification if a descendant is removed from fthe specified bin in the bin hierarchy.
        ``BinReceiver.deletedBinDescendnant()`` is invoked when the
        specified bin experiences a removal of one of its descdendents.

        :param bin_id: the ``Id`` of the bin to monitor
        :type bin_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.BinHierarchySession

    def get_bin_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    bin_hierarchy_id = property(fget=get_bin_hierarchy_id)

    def get_bin_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    bin_hierarchy = property(fget=get_bin_hierarchy)

    def can_access_bin_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer traversal
        functions to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_bin_ids(self):
        """Gets the root bin ``Ids`` in this hierarchy.

        :return: the root bin ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_bin_ids = property(fget=get_root_bin_ids)

    def get_root_bins(self):
        """Gets the root bins in the bin hierarchy.
        A node with no parents is an orphan. While all bin ``Ids`` are
        known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        :return: the root bins
        :rtype: ``osid.resource.BinList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_bins = property(fget=get_root_bins)

    def has_parent_bins(self, bin_id):
        """Tests if the ``Bin`` has any parents.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if the bin has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_bin(self, id_, bin_id):
        """Tests if an ``Id`` is a direct parent of a bin.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``bin_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_bin_ids(self, bin_id):
        """Gets the parent ``Ids`` of the given bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the bin
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_bins(self, bin_id):
        """Gets the parents of the given bin.

        :param bin_id: the ``Id`` to query
        :type bin_id: ``osid.id.Id``
        :return: the parents of the bin
        :rtype: ``osid.resource.BinList``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_bin(self, id_, bin_id):
        """Tests if an ``Id`` is an ancestor of a bin.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``bin_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_bins(self, bin_id):
        """Tests if a bin has any children.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if the ``bin_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_bin(self, id_, bin_id):
        """Tests if a bin is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``bin_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_bin_ids(self, bin_id):
        """Gets the child ``Ids`` of the given bin.

        :param bin_id: the ``Id`` to query
        :type bin_id: ``osid.id.Id``
        :return: the children of the bin
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_bins(self, bin_id):
        """Gets the children of the given bin.

        :param bin_id: the ``Id`` to query
        :type bin_id: ``osid.id.Id``
        :return: the children of the bin
        :rtype: ``osid.resource.BinList``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_bin(self, id_, bin_id):
        """Tests if an ``Id`` is a descendant of a bin.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``bin_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bin_node_ids(self, bin_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given bin.

        :param bin_id: the ``Id`` to query
        :type bin_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a bin node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bin_nodes(self, bin_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given bin.

        :param bin_id: the ``Id`` to query
        :type bin_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a bin node
        :rtype: ``osid.resource.BinNode``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.BinHierarchyDesignSession

    def can_modify_bin_hierarchy(self):
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

    def add_root_bin(self, bin_id):
        """Adds a root bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``bin_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_bin(self, bin_id):
        """Removes a root bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bin_id`` not a root
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_bin(self, bin_id, child_id):
        """Adds a child to a bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``bin_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``bin_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_bin(self, bin_id, child_id):
        """Removes a child from a bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bin_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``bin_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_bins(self, bin_id):
        """Removes all children from a bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bin_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class ResourceProxyManager(osid_managers.OsidProxyManager, ResourceProfile):

    def get_resource_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the resource lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceLookupSession``
        :rtype: ``osid.resource.ResourceLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_lookup_session_for_bin(self, bin_id, proxy):
        """Gets the ``OsidSession`` associated with the resource lookup service for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: ``a proxy``
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceLookupSession``
        :rtype: ``osid.resource.ResourceLookupSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_resource_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_query_session(self, proxy):
        """Gets a resource query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceQuerySession``
        :rtype: ``osid.resource.ResourceQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_query_session_for_bin(self, bin_id, proxy):
        """Gets a resource query session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceQuerySession``
        :rtype: ``osid.resource.ResourceQuerySession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_search_session(self, proxy):
        """Gets a resource search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceSearchSession``
        :rtype: ``osid.resource.ResourceSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_search_session_for_bin(self, bin_id, proxy):
        """Gets a resource search session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceSearchSession``
        :rtype: ``osid.resource.ResourceSearchSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_resource_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_admin_session(self, proxy):
        """Gets a resource administration session for creating, updating and deleting resources.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceAdminSession``
        :rtype: ``osid.resource.ResourceAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_admin_session_for_bin(self, bin_id, proxy):
        """Gets a resource administration session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceAdminSession``
        :rtype: ``osid.resource.ResourceAdminSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_notification_session(self, resource_receiver, proxy):
        """Gets the resource notification session for the given bin.

        :param resource_receiver: notification callback
        :type resource_receiver: ``osid.resource.ResourceReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceNotificationSession``
        :rtype: ``osid.resource.ResourceNotificationSession``
        :raise: ``NullArgument`` -- ``resource_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_notification_session_for_bin(self, resource_receiver, bin_id, proxy):
        """Gets the resource notification session for the given bin.

        :param resource_receiver: notification callback
        :type resource_receiver: ``osid.resource.ResourceReceiver``
        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a ResourceNotificationSession``
        :rtype: ``osid.resource.ResourceNotificationSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``resource_receiver, bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_resource_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_bin_session(self, proxy):
        """Gets the session for retrieving resource to bin mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceBinSession``
        :rtype: ``osid.resource.ResourceBinSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_bin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_bin_assignment_session(self, proxy):
        """Gets the session for assigning resource to bin mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceBinAssignmentSession``
        :rtype: ``osid.resource.ResourceBinAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_bin_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_smart_bin_session(self, bin_id, proxy):
        """Gets the session for managing dynamic resource bins.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceSmartBinSession``
        :rtype: ``osid.resource.ResourceSmartBinSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_smart_bin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_membership_session(self, proxy):
        """Gets the session for querying memberships.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MembershipSession``
        :rtype: ``osid.resource.MembershipSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_membership()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_membership_session_for_bin(self, bin_id, proxy):
        """Gets a resource membership session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a MembershipSession``
        :rtype: ``osid.resource.MembershipSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_membership()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_group_session(self, proxy):
        """Gets the session for retrieving gropup memberships.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GroupSession``
        :rtype: ``osid.resource.GroupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_groups()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_group_session_for_bin(self, bin_id, proxy):
        """Gets a group session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GroupSession``
        :rtype: ``osid.resource.GroupSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_group_assignment_session(self, proxy):
        """Gets the session for assigning resources to groups.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GroupAssignmentSession``
        :rtype: ``osid.resource.GroupAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_group_assignment_session_for_bin(self, bin_id, proxy):
        """Gets a group assignment session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GroupAssignmentSession``
        :rtype: ``osid.resource.GroupAssignmentSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_assignment()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_group_notification_session(self, group_rceeiver, proxy):
        """Gets the notification session for notifications pertaining to resource changes.

        :param group_rceeiver: the notification callback
        :type group_rceeiver: ``osid.resource.GroupReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GroupNotificationSession``
        :rtype: ``osid.resource.GroupNotificationSession``
        :raise: ``NullArgument`` -- ``group_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_group_notification_session_for_bin(self, group_rceeiver, bin_id, proxy):
        """Gets the group notification session for the given bin.

        :param group_rceeiver: the notification callback
        :type group_rceeiver: ``osid.resource.GroupReceiver``
        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GroupNotificationSession``
        :rtype: ``osid.resource.GroupNotificationSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``group_receiver, bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_group_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_group_hierarchy_session(self, proxy):
        """Gets the group hierarchy traversal session for the given resource group.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GroupHierarchySession``
        :rtype: ``osid.resource.BinHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_group_hierarchy_session_for_bin(self, bin_id, proxy):
        """Gets a group hierarchy session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GroupHierarchySession``
        :rtype: ``osid.resource.GroupHierarchySession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_group_hierarchy()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_agent_session(self, proxy):
        """Gets the session for retrieving resource agent mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GroupSession``
        :rtype: ``osid.resource.ResourceAgentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_agents()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_agent_session_for_bin(self, bin_id, proxy):
        """Gets a resource agent session for the given bin.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceAgentSession``
        :rtype: ``osid.resource.ResourceAgentSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_agent()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_agent_assignment_session(self, proxy):
        """Gets the session for assigning agents to resources.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceAgentAssignmentSession``
        :rtype: ``osid.resource.ResourceAgentAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_agent_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_agent_assignment_session_for_bin(self, bin_id, proxy):
        """Gets a resource agent session for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceAgentAssignmentSession``
        :rtype: ``osid.resource.ResourceAgentAssignmentSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_agent_assignment()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipLookupSession``
        :rtype: ``osid.resource.ResourceRelationshipLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_lookup_session_for_bin(self, bin_id, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship lookup service for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipLookupSession``
        :rtype: ``osid.resource.ResourceRelationshipLookupSession``
        :raise: ``NotFound`` -- no ``Bin`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipQuerySession``
        :rtype: ``osid.resource.ResourceRelationshipQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_query_session_for_bin(self, bin_id, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship query service for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipQuerySession``
        :rtype: ``osid.resource.ResourceRelationshipQuerySession``
        :raise: ``NotFound`` -- no ``Bin`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipSearchSession``
        :rtype: ``osid.resource.ResourceRelationshipSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_search_session_for_bin(self, bin_id, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship search service for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipSearchSession``
        :rtype: ``osid.resource.ResourceRelationshipSearchSession``
        :raise: ``NotFound`` -- no bin found by the given ``Id``
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipAdminSession``
        :rtype: ``osid.resource.ResourceRelationshipAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_admin_session_for_bin(self, bin_id, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship administration service for the given bin.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipAdminSession``
        :rtype: ``osid.resource.ResourceRelationshipAdminSession``
        :raise: ``NotFound`` -- no bin found by the given ``Id``
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_notification_session(self, resource_relationship_receiver, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship notification service.

        :param resource_relationship_receiver: the notification callback
        :type resource_relationship_receiver: ``osid.resource.ResourceRelationshipReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipNotificationSession``
        :rtype: ``osid.resource.ResourceRelationshipNotificationSession``
        :raise: ``NullArgument`` -- ``resource_relationship_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_notification_session_for_bin(self, resource_relationship_receiver, bin_id, proxy):
        """Gets the ``OsidSession`` associated with the resource relationship notification service for the given bin.

        :param resource_relationship_receiver: the notification callback
        :type resource_relationship_receiver: ``osid.resource.ResourceRelationshipReceiver``
        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipNotificationSession``
        :rtype: ``osid.resource.ResourceRelationshipNotificationSession``
        :raise: ``NotFound`` -- no bin found by the given ``Id``
        :raise: ``NullArgument`` -- ``resource_relationship_receiver, bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationshipt_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_bin_session(self, proxy):
        """Gets the session for retrieving resource relationship to bin mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipBinSession``
        :rtype: ``osid.resource.ResourceRelationshipBinSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_bin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_bin_assignment_session(self, proxy):
        """Gets the session for assigning resource relationship to bin mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipBinAssignmentSession``
        :rtype: ``osid.resource.ResourceRelationshipBinAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_bin_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_smart_bin_session(self, bin_id, proxy):
        """Gets the session for managing dynamic resource relationship bins.

        :param bin_id: the ``Id`` of the bin
        :type bin_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceRelationshipSmartBinSession``
        :rtype: ``osid.resource.ResourceRelationshipSmartBinSession``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_relationship_smart_bin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_bin_lookup_session(self, proxy):
        """Gets the bin lookup session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BinLookupSession``
        :rtype: ``osid.resource.BinLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_bin_query_session(self, proxy):
        """Gets the bin query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BinQuerySession``
        :rtype: ``osid.resource.BinQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_bin_search_session(self, proxy):
        """Gets the bin search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BinSearchSession``
        :rtype: ``osid.resource.BinSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_bin_admin_session(self, proxy):
        """Gets the bin administrative session for creating, updating and deleteing bins.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BinAdminSession``
        :rtype: ``osid.resource.BinAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_bin_notification_session(self, bin_receiver, proxy):
        """Gets the notification session for subscribing to changes to a bin.

        :param bin_receiver: notification callback
        :type bin_receiver: ``osid.resource.BinReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BinNotificationSession``
        :rtype: ``osid.resource.BinNotificationSession``
        :raise: ``NullArgument`` -- ``bin_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bin_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_bin_hierarchy_session(self, proxy):
        """Gets the bin hierarchy traversal session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a BinHierarchySession``
        :rtype: ``osid.resource.BinHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unimplemented`` -- ``supports_bin_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_bin_hierarchy_design_session(self, proxy):
        """Gets the bin hierarchy design session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BinHierarchyDesignSession``
        :rtype: ``osid.resource.BinHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unimplemented`` -- ``supports_bin_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_batch_proxy_manager(self):
        """Gets the ``ResourceBatchProxyManager``.

        :return: a ``ResourceBatchProxyManager``
        :rtype: ``osid.resource.batch.ResourceBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_batch_proxy_manager = property(fget=get_resource_batch_proxy_manager)

    def get_resource_demographic_proxy_manager(self):
        """Gets the ``ResourceDemographicProxyManager``.

        :return: a ``ResourceDemographicProxyManager``
        :rtype: ``osid.resource.demographic.ResourceDemographicProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_demographic()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_demographic_proxy_manager = property(fget=get_resource_demographic_proxy_manager)


##
# The following methods are from osid.resource.BinLookupSession

    def can_lookup_bins(self):
        """Tests if this user can perform ``Bin`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.


        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_bin_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.




        """
        raise UNIMPLEMENTED()

    def use_plenary_bin_view(self):
        """A complete view of the ``Bin`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.




        """
        raise UNIMPLEMENTED()

    def get_bin(self, bin_id):
        """Gets the ``Bin`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Bin`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Bin`` and retained for compatibility.


        :param bin_id: ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: the bin
        :rtype: ``osid.resource.Bin``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bins_by_ids(self, bin_ids):
        """Gets a ``BinList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the bins
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Bins`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.


        :param bin_ids: the list of ``Ids`` to retrieve
        :type bin_ids: ``osid.id.IdList``
        :return: the returned ``Bin list``
        :rtype: ``osid.resource.BinList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``bin_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bins_by_genus_type(self, bin_genus_type):
        """Gets a ``BinList`` corresponding to the given bin genus ``Type`` which does not include bins of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.


        :param bin_genus_type: a bin genus type
        :type bin_genus_type: ``osid.type.Type``
        :return: the returned ``Bin list``
        :rtype: ``osid.resource.BinList``
        :raise: ``NullArgument`` -- ``bin_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bins_by_parent_genus_type(self, bin_genus_type):
        """Gets a ``BinList`` corresponding to the given bin genus ``Type`` and include any additional bins with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.


        :param bin_genus_type: a bin genus type
        :type bin_genus_type: ``osid.type.Type``
        :return: the returned ``Bin list``
        :rtype: ``osid.resource.BinList``
        :raise: ``NullArgument`` -- ``bin_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bins_by_record_type(self, bin_record_type):
        """Gets a ``BinList`` containing the given bin record ``Type``.
        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.


        :param bin_record_type: a bin record type
        :type bin_record_type: ``osid.type.Type``
        :return: the returned ``Bin list``
        :rtype: ``osid.resource.BinList``
        :raise: ``NullArgument`` -- ``bin_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bins_by_provider(self, resource_id):
        """Gets a ``BinList`` from the given provider.
        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Bin list``
        :rtype: ``osid.resource.BinList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bins(self):
        """Gets all ``Bins``.
        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.


        :return: a list of ``Bins``
        :rtype: ``osid.resource.BinList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    bins = property(fget=get_bins)


##
# The following methods are from osid.resource.BinQuerySession

    def can_search_bins(self):
        """Tests if this user can perform ``Bin`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_bin_query(self):
        """Gets a bin query.
        The returned query will not have an extension query.


        :return: the bin query
        :rtype: ``osid.resource.BinQuery``

        """
        raise UNIMPLEMENTED()

    bin_query = property(fget=get_bin_query)

    def get_bins_by_query(self, bin_query):
        """Gets a list of ``Bins`` matching the given bin query.

        :param bin_query: the bin query
        :type bin_query: ``osid.resource.BinQuery``
        :return: the returned ``BinList``
        :rtype: ``osid.resource.BinList``
        :raise: ``NullArgument`` -- ``bin_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- a ``bin_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.BinSearchSession

    def get_bin_search(self):
        """Gets a bin search.

        :return: the bin search
        :rtype: ``osid.resource.BinSearch``

        """
        raise UNIMPLEMENTED()

    bin_search = property(fget=get_bin_search)

    def get_bin_search_order(self):
        """Gets a bin search order.
        The ``BinSearchOrder`` is supplied to a ``BinSearch`` to specify
        the ordering of results.


        :return: the bin search order
        :rtype: ``osid.resource.BinSearchOrder``

        """
        raise UNIMPLEMENTED()

    bin_search_order = property(fget=get_bin_search_order)

    def get_bins_by_search(self, bin_query, bin_search):
        """Gets the search results matching the given search query using the given search.

        :param bin_query: the bin query
        :type bin_query: ``osid.resource.BinQuery``
        :param bin_search: the bin search
        :type bin_search: ``osid.resource.BinSearch``
        :return: the bin search results
        :rtype: ``osid.resource.BinSearchResults``
        :raise: ``NullArgument`` -- ``bin_query`` or ``bin_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``bin_query`` or ``bin_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_bin_query_from_inspector(self, bin_query_inspector):
        """Gets a bin query from an inspector.
        The inspector is available from a ``BinSearchResults``.


        :param bin_query_inspector: a bin query inspector
        :type bin_query_inspector: ``osid.resource.BinQueryInspector``
        :return: the bin query
        :rtype: ``osid.resource.BinQuery``
        :raise: ``NullArgument`` -- ``bin_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``bin_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.BinAdminSession

    def can_create_bins(self):
        """Tests if this user can create ``Bins``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.


        :return: ``false`` if ``Bin`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_bin_with_record_types(self, bin_record_types):
        """Tests if this user can create a single ``Bin`` using the desired record types.
        While ``ResourceManager.getBinRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Bin``.
        Providing an empty array tests if a ``Bin`` can be created with
        no records.


        :param bin_record_types: array of bin record types
        :type bin_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Bin`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bin_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_bin_form_for_create(self, bin_record_types):
        """Gets the bin form for creating new bins.

        :param bin_record_types: array of bin record types
        :type bin_record_types: ``osid.type.Type[]``
        :return: the bin form
        :rtype: ``osid.resource.BinForm``
        :raise: ``NullArgument`` -- ``bin_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        """
        raise UNIMPLEMENTED()

    def create_bin(self, bin_form):
        """Creates a new ``Bin``.

        :param bin_form: the form for this ``Bin``
        :type bin_form: ``osid.resource.BinForm``
        :return: the new ``Bin``
        :rtype: ``osid.resource.Bin``
        :raise: ``IllegalState`` -- ``bin_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``bin_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``bin_form`` did not originate from ``get_bin_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_bins(self):
        """Tests if this user can update ``Bins``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.


        :return: ``false`` if ``Bin`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_bin_form_for_update(self, bin_id):
        """Gets the bin form for updating an existing bin.
        A new bin form should be requested for each update transaction.


        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: the bin form
        :rtype: ``osid.resource.BinForm``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_bin(self, bin_form):
        """Updates an existing bin.

        :param bin_form: the form containing the elements to be updated
        :type bin_form: ``osid.resource.BinForm``
        :raise: ``IllegalState`` -- ``bin_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``bin_id`` or ``bin_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``bin_form`` did not originate from ``get_bin_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_bins(self):
        """Tests if this user can delete ``Bins``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.


        :return: ``false`` if ``Bin`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_bin(self, bin_id):
        """Deletes a ``Bin``.

        :param bin_id: the ``Id`` of the ``Bin`` to remove
        :type bin_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_bin_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Bins``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``Bin`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_bin(self, bin_id, alias_id):
        """Adds an ``Id`` to a ``Bin`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Bin`` is determined by the provider.
        The new ``Id`` performs as an alias to the primary ``Id``. If
        the alias is a pointer to another bin, it is reassigned to the
        given bin ``Id``.


        :param bin_id: the ``Id`` of a ``Bin``
        :type bin_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.BinNotificationSession

    def can_register_for_bin_notifications(self):
        """Tests if this user can register for ``Bin`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.


        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_bins(self):
        """Register for notifications of new bins.
        ``BinReceiver.newBin()`` is invoked when a new ``Bin`` is
        created.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_bin_ancestors(self, bin_id):
        """Registers for notification if an ancestor is added to the specified bin in the bin hierarchy.
        ``BinReceiver.newBinAncestor()`` is invoked when the specified
        bin experiences an addition in ancestry.


        :param bin_id: the ``Id`` of the bin to monitor
        :type bin_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_bin_descendants(self, bin_id):
        """Registers for notification if a descendant is added to the specified bin in the bin hierarchy.
        ``BinReceiver.newBinDescendant()`` is invoked when the specified
        bin experiences an addition in descendants.


        :param bin_id: the ``Id`` of the bin to monitor
        :type bin_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_bins(self):
        """Registers for notification of updated bins.
        ``BinReceiver.changedBin()`` is invoked when a bin is changed.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_bin(self, bin_id):
        """Registers for notification of an updated bin.
        ``BinReceiver.changedBin()`` is invoked when the specified bin
        is changed.


        :param bin_id: the Id of the Bin to monitor
        :type bin_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_bins(self):
        """Registers for notification of deleted bins.
        ``BinReceiver.deletedBin()`` is invoked when a bin is deleted.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_bin(self, bin_id):
        """Registers for notification of a deleted bin.
        ``BinReceiver.deletedBin()`` is invoked when the specified bin
        is deleted.


        :param bin_id: the ``Id`` of the ``Bin`` to monitor
        :type bin_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_bin_ancestors(self, bin_id):
        """Registers for notification if an ancestor is removed from the specified bin in the bin hierarchy.
        ``BinReceiver.deletedBinAncestor()`` is invoked when the
        specified bin experiences a removal of an ancestor.


        :param bin_id: the ``Id`` of the bin to monitor
        :type bin_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_bin_descendants(self, bin_id):
        """Registers for notification if a descendant is removed from fthe specified bin in the bin hierarchy.
        ``BinReceiver.deletedBinDescendnant()`` is invoked when the
        specified bin experiences a removal of one of its descdendents.


        :param bin_id: the ``Id`` of the bin to monitor
        :type bin_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.BinHierarchySession

    def get_bin_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    bin_hierarchy_id = property(fget=get_bin_hierarchy_id)

    def get_bin_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    bin_hierarchy = property(fget=get_bin_hierarchy)

    def can_access_bin_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer traversal
        functions to unauthorized users.


        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_bin_ids(self):
        """Gets the root bin ``Ids`` in this hierarchy.

        :return: the root bin ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_bin_ids = property(fget=get_root_bin_ids)

    def get_root_bins(self):
        """Gets the root bins in the bin hierarchy.
        A node with no parents is an orphan. While all bin ``Ids`` are
        known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.


        :return: the root bins
        :rtype: ``osid.resource.BinList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_bins = property(fget=get_root_bins)

    def has_parent_bins(self, bin_id):
        """Tests if the ``Bin`` has any parents.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if the bin has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_bin(self, id_, bin_id):
        """Tests if an ``Id`` is a direct parent of a bin.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``bin_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_bin_ids(self, bin_id):
        """Gets the parent ``Ids`` of the given bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the bin
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_bins(self, bin_id):
        """Gets the parents of the given bin.

        :param bin_id: the ``Id`` to query
        :type bin_id: ``osid.id.Id``
        :return: the parents of the bin
        :rtype: ``osid.resource.BinList``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_bin(self, id_, bin_id):
        """Tests if an ``Id`` is an ancestor of a bin.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``bin_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_bins(self, bin_id):
        """Tests if a bin has any children.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if the ``bin_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_bin(self, id_, bin_id):
        """Tests if a bin is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``bin_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_bin_ids(self, bin_id):
        """Gets the child ``Ids`` of the given bin.

        :param bin_id: the ``Id`` to query
        :type bin_id: ``osid.id.Id``
        :return: the children of the bin
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_bins(self, bin_id):
        """Gets the children of the given bin.

        :param bin_id: the ``Id`` to query
        :type bin_id: ``osid.id.Id``
        :return: the children of the bin
        :rtype: ``osid.resource.BinList``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_bin(self, id_, bin_id):
        """Tests if an ``Id`` is a descendant of a bin.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``bin_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bin_node_ids(self, bin_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given bin.

        :param bin_id: the ``Id`` to query
        :type bin_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a bin node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bin_nodes(self, bin_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given bin.

        :param bin_id: the ``Id`` to query
        :type bin_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a bin node
        :rtype: ``osid.resource.BinNode``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.BinHierarchyDesignSession

    def can_modify_bin_hierarchy(self):
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

    def add_root_bin(self, bin_id):
        """Adds a root bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``bin_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_bin(self, bin_id):
        """Removes a root bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bin_id`` not a root
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_bin(self, bin_id, child_id):
        """Adds a child to a bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``bin_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``bin_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_bin(self, bin_id, child_id):
        """Removes a child from a bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bin_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``bin_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_bins(self, bin_id):
        """Removes all children from a bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bin_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class Bin(osid_objects.OsidCatalog, osid_sessions.OsidSession):

    def get_bin_record(self, bin_record_type):
        """Gets the bin record corresponding to the given ``Bin`` record ``Type``.
        This method is used to retrieve an object implementing the
        requested record. The ``bin_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(bin_record_type)`` is
        ``true`` .

        :param bin_record_type: the bin record type
        :type bin_record_type: ``osid.type.Type``
        :return: the bin record
        :rtype: ``osid.resource.records.BinRecord``
        :raise: ``NullArgument`` -- ``bin_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(bin_record_type)`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.ResourceLookupSession

    def get_bin_id(self):
        """Gets the ``Bin``  ``Id`` associated with this session.

        :return: the ``Bin Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        """Gets the ``Bin`` associated with this session.

        :return: the ``Bin`` associated with this session
        :rtype: ``osid.resource.Bin``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    bin = property(fget=get_bin)

    def can_lookup_resources(self):
        """Tests if this user can perform ``Resource`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_resource_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_resource_view(self):
        """A complete view of the ``Resource`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_bin_view(self):
        """Federates the view for methods in this session.
        A federated view will include resources in bins which are
        children of this bin in the bin hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_bin_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this bin only.



        """
        raise UNIMPLEMENTED()

    def get_resource(self, resource_id):
        """Gets the ``Resource`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Resource`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Resource`` and retained for
        compatibility.

        :param resource_id: the ``Id`` of the ``Resource`` to retrieve
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Resource``
        :rtype: ``osid.resource.Resource``
        :raise: ``NotFound`` -- no ``Resource`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resources_by_ids(self, resource_ids):
        """Gets a ``ResourceList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the resources
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Resources`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param resource_ids: the list of ``Ids`` to retrieve
        :type resource_ids: ``osid.id.IdList``
        :return: the returned ``Resource`` list
        :rtype: ``osid.resource.ResourceList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``resource_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resources_by_genus_type(self, resource_genus_type):
        """Gets a ``ResourceList`` corresponding to the given resource genus ``Type`` which does not include resources of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        :param resource_genus_type: a resource genus type
        :type resource_genus_type: ``osid.type.Type``
        :return: the returned ``Resource`` list
        :rtype: ``osid.resource.ResourceList``
        :raise: ``NullArgument`` -- ``resource_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resources_by_parent_genus_type(self, resource_genus_type):
        """Gets a ``ResourceList`` corresponding to the given resource genus ``Type`` and include any additional resources with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        :param resource_genus_type: a resource genus type
        :type resource_genus_type: ``osid.type.Type``
        :return: the returned ``Resource`` list
        :rtype: ``osid.resource.ResourceList``
        :raise: ``NullArgument`` -- ``resource_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resources_by_record_type(self, resource_record_type):
        """Gets a ``ResourceList`` containing the given resource record ``Type``.
        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        :param resource_record_type: a resource record type
        :type resource_record_type: ``osid.type.Type``
        :return: the returned ``Resource`` list
        :rtype: ``osid.resource.ResourceList``
        :raise: ``NullArgument`` -- ``resource_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resources(self):
        """Gets all ``Resources``.
        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        :return: a list of ``Resources``
        :rtype: ``osid.resource.ResourceList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    resources = property(fget=get_resources)


##
# The following methods are from osid.resource.ResourceQuerySession

    def can_search_resources(self):
        """Tests if this user can perform ``Resource`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_resource_query(self):
        """Gets a resource query.
        The returned query will not have an extension query.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``

        """
        raise UNIMPLEMENTED()

    resource_query = property(fget=get_resource_query)

    def get_resources_by_query(self, resource_query):
        """Gets a list of ``Resources`` matching the given resource query.

        :param resource_query: the resource query
        :type resource_query: ``osid.resource.ResourceQuery``
        :return: the returned ``ResourceList``
        :rtype: ``osid.resource.ResourceList``
        :raise: ``NullArgument`` -- ``resource_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``resource_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.ResourceSearchSession

    def get_resource_search(self):
        """Gets a resource search.

        :return: the resource search
        :rtype: ``osid.resource.ResourceSearch``

        """
        raise UNIMPLEMENTED()

    resource_search = property(fget=get_resource_search)

    def get_resource_search_order(self):
        """Gets a resource search order.
        The ``ResourceSearchOrder`` is supplied to a ``ResourceSearch``
        to specify the ordering of results.

        :return: the resource search order
        :rtype: ``osid.resource.ResourceSearchOrder``

        """
        raise UNIMPLEMENTED()

    resource_search_order = property(fget=get_resource_search_order)

    def get_resources_by_search(self, resource_query, resource_search):
        """Gets the search results matching the given search query using the given search.

        :param resource_query: the resource query
        :type resource_query: ``osid.resource.ResourceQuery``
        :param resource_search: the resource search
        :type resource_search: ``osid.resource.ResourceSearch``
        :return: the resource search results
        :rtype: ``osid.resource.ResourceSearchResults``
        :raise: ``NullArgument`` -- ``resource_query`` or ``resource_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``resource_query`` or ``resource_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_resource_query_from_inspector(self, resource_query_inspector):
        """Gets a resource query from an inspector.
        The inspector is available from a ``ResourceSearchResults``.

        :param resource_query_inspector: a resource query inspector
        :type resource_query_inspector: ``osid.resource.ResourceQueryInspector``
        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``NullArgument`` -- ``resource_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``resource_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.ResourceAdminSession

    def can_create_resources(self):
        """Tests if this user can create ``Resources``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Resource`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Resource`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_resource_with_record_types(self, resource_record_types):
        """Tests if this user can create a single ``Resource`` using the desired record types.
        While ``ResourceManager.getResourceRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Resource``.
        Providing an empty array tests if a ``Resource`` can be created
        with no records.

        :param resource_record_types: array of resource record types
        :type resource_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Resource`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``resource_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_resource_form_for_create(self, resource_record_types):
        """Gets the resource form for creating new resources.
        A new form should be requested for each create transaction.

        :param resource_record_types: array of resource record types
        :type resource_record_types: ``osid.type.Type[]``
        :return: the resource form
        :rtype: ``osid.resource.ResourceForm``
        :raise: ``NullArgument`` -- ``resource_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        """
        raise UNIMPLEMENTED()

    def create_resource(self, resource_form):
        """Creates a new ``Resource``.

        :param resource_form: the form for this ``Resource``
        :type resource_form: ``osid.resource.ResourceForm``
        :return: the new ``Resource``
        :rtype: ``osid.resource.Resource``
        :raise: ``IllegalState`` -- ``resource_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``resource_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``resource_form`` did not originate from ``get_resource_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_resources(self):
        """Tests if this user can update ``Resources``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Resource`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``Resource`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_resource_form_for_update(self, resource_id):
        """Gets the resource form for updating an existing resource.
        A new resource form should be requested for each update
        transaction.

        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: the resource form
        :rtype: ``osid.resource.ResourceForm``
        :raise: ``NotFound`` -- ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_resource(self, resource_form):
        """Updates an existing resource.

        :param resource_form: the form containing the elements to be updated
        :type resource_form: ``osid.resource.ResourceForm``
        :raise: ``IllegalState`` -- ``resource_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``resource_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``resource_form`` did not originate from ``get_resource_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_resources(self):
        """Tests if this user can delete ``Resources``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Resource`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Resource`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_resource(self, resource_id):
        """Deletes a ``Resource``.

        :param resource_id: the ``Id`` of the ``Resource`` to remove
        :type resource_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``resource_id`` not found
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_resource_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Resources``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Resource`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_resource(self, resource_id, alias_id):
        """Adds an ``Id`` to a ``Resource`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Resource`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another resource it is
        reassigned to the given resource ``Id``.

        :param resource_id: the ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``resource_id`` not found
        :raise: ``NullArgument`` -- ``alias_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.ResourceNotificationSession

    def can_register_for_resource_notifications(self):
        """Tests if this user can register for ``Resource`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_resources(self):
        """Register for notifications of new resources.
        ``ResourceReceiver.newResource()`` is invoked when a new
        ``Resource`` is appears in this bin.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_resources(self):
        """Registers for notification of updated resources.
        ``ResourceReceiver.changedResource()`` is invoked when a
        resource in this bin is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_resource(self, resource_id):
        """Registers for notification of an updated resource.
        ``ResourceReceiver.changedResource()`` is invoked when the
        specified resource in this bin is changed.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_resources(self):
        """Registers for notification of deleted resources.
        ``ResourceReceiver.deletedResource()`` is invoked when a
        resource is deleted or removed from this bin.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_resource(self, resource_id):
        """Registers for notification of a deleted resource.
        ``ResourceReceiver.deletedResource()`` is invoked when the
        specified resource is deleted or removed from this bin.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.ResourceBinSession

    def use_comparative_bin_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_bin_view(self):
        """A complete view of the ``Resource`` and ``Bin`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def can_lookup_resource_bin_mappings(self):
        """Tests if this user can perform lookups of resource/bin mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_resource_ids_by_bin(self, bin_id):
        """Gets the list of ``Resource``  ``Ids`` associated with a ``Bin``.

        :param bin_id: ``Id`` of a ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: list of related resource ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resources_by_bin(self, bin_id):
        """Gets the list of ``Resources`` associated with a ``Bin``.

        :param bin_id: ``Id`` of a ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: list of related resources
        :rtype: ``osid.resource.ResourceList``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_ids_by_bins(self, bin_ids):
        """Gets the list of ``Resource Ids`` corresponding to a list of ``Bin`` objects.

        :param bin_ids: list of bin ``Ids``
        :type bin_ids: ``osid.id.IdList``
        :return: list of resource ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bin_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resources_by_bins(self, bin_ids):
        """Gets the list of ``Resources`` corresponding to a list of ``Bins``.

        :param bin_ids: list of bin ``Ids``
        :type bin_ids: ``osid.id.IdList``
        :return: list of resources
        :rtype: ``osid.resource.ResourceList``
        :raise: ``NullArgument`` -- ``bin_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bin_ids_by_resource(self, resource_id):
        """Gets the list of ``Bin``  ``Ids`` mapped to a ``Resource``.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: list of bin ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bins_by_resource(self, resource_id):
        """Gets the list of ``Bin`` objects mapped to a ``Resource``.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: list of bins
        :rtype: ``osid.resource.BinList``
        :raise: ``NotFound`` -- ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.ResourceBinAssignmentSession

    def can_assign_resources(self):
        """Tests if this user can alter resource/bin mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_resources_to_bin(self, bin_id):
        """Tests if this user can alter resource/bin mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied`` . This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_bin_ids(self, bin_id):
        """Gets a list of bins including and under the given bin node in which any resource can be assigned.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: list of assignable bin ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_bin_ids_for_resource(self, bin_id, resource_id):
        """Gets a list of bins including and under the given bin node in which a specific resource can be assigned.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: list of assignable bin ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bin_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_resource_to_bin(self, resource_id, bin_id):
        """Adds an existing ``Resource`` to a ``Bin``.

        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``resource_id`` is already assigned to ``bin_id``
        :raise: ``NotFound`` -- ``resource_id`` or ``bin_id`` not found
        :raise: ``NullArgument`` -- ``resource_id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_resource_from_bin(self, resource_id, bin_id):
        """Removes a ``Resource`` from a ``Bin``.

        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``resource_id`` or ``bin_id`` not found or ``resource_id`` not assigned to ``bin_id``
        :raise: ``NullArgument`` -- ``resource_id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.ResourceSmartBinSession

    def can_manage_smart_bins(self):
        """Tests if this user can manage smart bins.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart bin management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_resource_query(self, resource_query):
        """Applies a resource query to this bin.

        :param resource_query: the resource query
        :type resource_query: ``osid.resource.ResourceQuery``
        :raise: ``NullArgument`` -- ``resource_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``resource_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_resource_query(self):
        """Gets a resource query inspector for this bin.

        :return: the resource query inspector
        :rtype: ``osid.resource.ResourceQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_resource_sequencing(self, resource_search_order):
        """Applies a resource search order to this bin.

        :param resource_search_order: the resource search order
        :type resource_search_order: ``osid.resource.ResourceSearchOrder``
        :raise: ``NullArgument`` -- ``resource_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``resource_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.MembershipSession

    def can_query_membership(self):
        """Tests if this user can perform membership queries.
        . A return of true does not guarantee successful authorization.
        A return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if membership queries are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def is_member(self, member_resource_id, resource_id):
        """Tests if a ``Resource`` is a member of another ``Resource``.

        :param member_resource_id: ``Id`` of the ``Resource`` member
        :type member_resource_id: ``osid.id.Id``
        :param resource_id: ``Id`` of the ``Resource`` representing the group or demographic
        :type resource_id: ``osid.id.Id``
        :return: true if ``member_resource_id`` is a member of the ``resource_id,`` false otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``member_resource_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.GroupSession

    def can_lookup_resource_members(self):
        """Tests if this user can perform lookups of resource members.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up members is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_federated_group_view(self):
        """Federates the view for methods in this session.
        A federated view will include resources in groups which are
        children of the specified group in the group hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_group_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to the specified group only.



        """
        raise UNIMPLEMENTED()

    def get_resource_ids_by_group(self, group_resource_id):
        """Gets the list of ``Resource``  ``Ids`` associated with a ``Resource``.
        In a federated view, resources for child groups are included.

        :param group_resource_id: ``Id`` of the ``Resource``
        :type group_resource_id: ``osid.id.Id``
        :return: list of member resource ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``group_resource_id`` is not found
        :raise: ``NullArgument`` -- ``group_resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resources_by_group(self, group_resource_id):
        """Gets the list of ``Resources`` associated with a ``Resource``.
        In a federated view, resources for child groups are included.

        :param group_resource_id: ``Id`` of the ``Resource``
        :type group_resource_id: ``osid.id.Id``
        :return: list of resourcememembers
        :rtype: ``osid.resource.ResourceList``
        :raise: ``NotFound`` -- ``group_resource_id`` is not found
        :raise: ``NullArgument`` -- ``group_resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_ids_by_groups(self, group_resource_ids):
        """Gets the list of ``Resource Ids`` corresponding to a list of ``Resource`` objects.

        :param group_resource_ids: list of resource ``Ids``
        :type group_resource_ids: ``osid.id.IdList``
        :return: list of resource ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``group_resource_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resources_by_groups(self, group_resource_ids):
        """Gets the list of ``Resources`` corresponding to a list of ``Resource`` objects.

        :param group_resource_ids: list of resource ``Ids``
        :type group_resource_ids: ``osid.id.IdList``
        :return: list of resources
        :rtype: ``osid.resource.ResourceList``
        :raise: ``NullArgument`` -- ``group_resource_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_group_ids_by_resource(self, resource_id):
        """Gets the list of ``Resource``  ``Ids`` mapped to a ``Resource``.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: list of group resource ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_groups_by_resource(self, resource_id):
        """Gets the list of ``Resource`` objects mapped to a ``Resource``.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: list of group resources
        :rtype: ``osid.resource.ResourceList``
        :raise: ``NotFound`` -- ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.GroupAssignmentSession

    def can_assign_resources_to_group(self, resource_id):
        """Tests if this user can assign members to the given group.
        . A return of true does not guarantee successful authorization.
        A return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def assign_resource_to_group(self, resource_id, resource_group_id):
        """Adds an existing ``Resource`` to a ``Resource`` group.

        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :param resource_group_id: the ``Id`` of the ``Resource`` group
        :type resource_group_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``resource_id`` is already part of ``resource_group_id``
        :raise: ``NotFound`` -- ``resource_id`` or ``resource_group_id`` not found
        :raise: ``NullArgument`` -- ``resource_id`` or ``resource_group_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_resource_from_group(self, resource_id, resource_group_id):
        """Removes a ``Resource`` from a ``Resource`` group.

        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :param resource_group_id: the ``Id`` of the ``Repository``
        :type resource_group_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``resource_id or resource_group_id`` not found or ``resource_id`` not part of ``resource_group_id``
        :raise: ``NullArgument`` -- ``resource_id or resource_group_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.GroupNotificationSession

    def can_register_for_group_notifications(self):
        """Tests if this user can register for group notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_members(self, resource_id):
        """Register for notifications of new resource memberss.
        ``GroupReceiver.newMember()`` is invoked when a new member is
        added to the specified group.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_members(self, resource_id):
        """Register for notifications of deleted resource memberss.
        ``GroupReceiver.deletedMember()`` is invoked when a new member
        is removed from the specified group.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.GroupHierarchySession

    def can_access_group_hierarchy(self):
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

    def is_member_of_group(self, group_id, resource_id):
        """Tests if a resource ``Id`` is a member of a group either directly or indirectly through nested groups.

        :param group_id: a resource group ``Id``
        :type group_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of a resource
        :type resource_id: ``osid.id.Id``
        :return: ``true`` if this ``resource_id`` is a member of ``group_id,`` f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``group_id`` is not found
        :raise: ``NullArgument`` -- ``group_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_node_ids(self, resource_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given resource group.

        :param resource_id: the ``Id`` to query
        :type resource_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a resource node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_nodes(self, resource_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given resource group.

        :param resource_id: the ``Id`` to query
        :type resource_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a resource node
        :rtype: ``osid.acknowledgement.BillingNode``
        :raise: ``NotFound`` -- ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.ResourceAgentSession

    def can_lookup_resource_agent_mappings(self):
        """Tests if this user can perform lookups of resource/agent mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_agent_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_agent_view(self):
        """A complete view of the ``Agent`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_resource_id_by_agent(self, agent_id):
        """Gets the ``Resource``  ``Id`` associated with the given agent.

        :param agent_id: ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: associated resource
        :rtype: ``osid.id.Id``
        :raise: ``NotFound`` -- ``agent_id`` is not found
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_by_agent(self, agent_id):
        """Gets the ``Resource`` associated with the given agent.

        :param agent_id: ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: associated resource
        :rtype: ``osid.resource.Resource``
        :raise: ``NotFound`` -- ``agent_id`` is not found
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agent_ids_by_resource(self, resource_id):
        """Gets the list of ``Agent``  ``Ids`` mapped to a ``Resource``.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: list of agent ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agents_by_resource(self, resource_id):
        """Gets the list of ``Agents`` mapped to a ``Resource``.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: list of agents
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NotFound`` -- ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.ResourceAgentAssignmentSession

    def can_assign_agents(self):
        """Tests if this user can alter resource/agent mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_agents_to_resource(self, resource_id):
        """Tests if this user can alter resource/agent mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known location methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def assign_agent_to_resource(self, agent_id, resource_id):
        """Adds an existing ``Agent`` to a ``Resource``.

        :param agent_id: the ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``agent_id`` is already assigned to ``resource_id``
        :raise: ``NotFound`` -- ``agent_id`` or ``resource_id`` not found
        :raise: ``NullArgument`` -- ``agent_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_agent_from_resource(self, agent_id, resource_id):
        """Removes an ``Agent`` from a ``Resource``.

        :param agent_id: the ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``agent_id`` or ``resource_id`` not found or ``agent_id`` not assigned to ``resource_id``
        :raise: ``NullArgument`` -- ``agent_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.ResourceRelationshipLookupSession

    def can_lookup_resource_relationships(self):
        """Tests if this user can access resource relationships.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        relationship operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_resource_relationship_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_resource_relationship_view(self):
        """A complete view of the resource relationship returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_effective_resource_relationship_view(self):
        """Only resource relationships whose effective dates are current are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_any_effective_resource_relationship_view(self):
        """All resource relationships of any effective dates are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def get_resource_relationship(self, resource_relationship_id):
        """Gets the ``ResourceRelationship`` specified by its ``Id``.

        :param resource_relationship_id: ``Id`` of the ``Relationship``
        :type resource_relationship_id: ``osid.id.Id``
        :return: the relationship
        :rtype: ``osid.resource.ResourceRelationship``
        :raise: ``NotFound`` -- ``resource_relationship_id`` not found
        :raise: ``NullArgument`` -- ``resource_relationship_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_by_ids(self, resource_relationship_ids):
        """Gets a ``ResourceRelationshipList`` corresponding to the given ``IdList``.

        :param resource_relationship_ids: the list of ``Ids`` to retrieve
        :type resource_relationship_ids: ``osid.id.IdList``
        :return: the returned ``ResourceRelationship`` list
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``resource_relationship_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_by_genus_type(self, relationship_genus_type):
        """Gets the resource relationships for the given resource relationship genus type.

        :param relationship_genus_type: a relationship genus type
        :type relationship_genus_type: ``osid.type.Type``
        :return: the relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``NullArgument`` -- ``relationship_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_by_parent_genus_type(self, relationship_genus_type):
        """Gets the reource relationships for the given resource relationship genus type and include any relationships with a genus type derived from the specified genus type.

        :param relationship_genus_type: a relationship genus type
        :type relationship_genus_type: ``osid.type.Type``
        :return: the relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``NullArgument`` -- ``relationship_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_by_record_type(self, relationship_record_type):
        """Gets the resource relationships for the given resource relationship record type.

        :param relationship_record_type: a relationship record type
        :type relationship_record_type: ``osid.type.Type``
        :return: the relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``NullArgument`` -- ``relationship_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_on_date(self, from_, to):
        """Gets the resource relationships effective during the entire given date range inclusive but not confined to the date range.

        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_for_source_resource(self, source_resource_id):
        """Gets the ``ResourceRelationships`` of a resource.

        :param source_resource_id: ``Id`` of a ``Resource``
        :type source_resource_id: ``osid.id.Id``
        :return: the relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``NullArgument`` -- ``source_resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_for_source_resource_on_date(self, source_resource_id, from_, to):
        """Gets a list of resource relationships for a resource and effective during the entire given date range inclusive but not confined to the date range.

        :param source_resource_id: a resource ``Id``
        :type source_resource_id: ``osid.id.Id``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``source_resource_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_by_genus_type_for_source_resource(self, source_resource_id, relationship_genus_type):
        """Gets the ``ResourceRelationships`` of a resource of relationship genus type that includes any genus type derived from the given one.

        :param source_resource_id: ``Id`` of a ``Resource``
        :type source_resource_id: ``osid.id.Id``
        :param relationship_genus_type: a relationship genus type
        :type relationship_genus_type: ``osid.type.Type``
        :return: the relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``NullArgument`` -- ``source_resource_id`` or ``relationship_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_by_genus_type_for_source_resource_on_date(self, source_resource_id, relationship_genus_type, from_, to):
        """Gets a list of resource relationships of a given genus type for a resource and effective during the entire given date range inclusive but not confined to the date range.

        :param source_resource_id: a resource ``Id``
        :type source_resource_id: ``osid.id.Id``
        :param relationship_genus_type: a relationship genus type
        :type relationship_genus_type: ``osid.type.Type``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``source_resource_id, relationship_genus_type, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_for_destination_resource(self, destination_resource_id):
        """Gets the ``ResourceRelationships`` of a resource.

        :param destination_resource_id: ``Id`` of a ``Resource``
        :type destination_resource_id: ``osid.id.Id``
        :return: the relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``NullArgument`` -- ``destination_resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_for_destination_resource_on_date(self, source_resource_id, from_, to):
        """Gets a list of resource relationships for a resource and effective during the entire given date range inclusive but not confined to the date range.

        :param source_resource_id: a resource ``Id``
        :type source_resource_id: ``osid.id.Id``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``destination_resource_id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_by_genus_type_for_destination_resource(self, destination_resource_id, relationship_genus_type):
        """Gets the ``ResourceRelationships`` of a resource of relationship genus type that includes any genus type derived from the given one.

        :param destination_resource_id: ``Id`` of a ``Resource``
        :type destination_resource_id: ``osid.id.Id``
        :param relationship_genus_type: a relationship genus type
        :type relationship_genus_type: ``osid.type.Type``
        :return: the relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``NullArgument`` -- ``destination_resource_id`` or ``relationship_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_by_genus_type_for_destination_resource_on_date(self, destination_resource_id, relationship_genus_type, from_, to):
        """Gets a list of resource relationships of a given genus type for a resource and effective during the entire given date range inclusive but not confined to the date range.

        :param destination_resource_id: a resource ``Id``
        :type destination_resource_id: ``osid.id.Id``
        :param relationship_genus_type: a relationship genus type
        :type relationship_genus_type: ``osid.type.Type``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``destination_resource_id, relationship_genus_type, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_for_resources(self, source_resource_id, destination_resource_id):
        """Gets the ``ResourceRelationships`` given two resources.

        :param source_resource_id: ``Id`` of a ``Resource``
        :type source_resource_id: ``osid.id.Id``
        :param destination_resource_id: ``Id`` of another ``Resource``
        :type destination_resource_id: ``osid.id.Id``
        :return: the relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``NullArgument`` -- ``source_relationship_id`` or ``destination_relationship_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_for_resources_on_date(self, source_resource_id, destination_resource_id, from_, to):
        """Gets a list of resource relationships for a two peer resources and effective during the entire given date range inclusive but not confined to the date range.

        :param source_resource_id: a resource ``Id``
        :type source_resource_id: ``osid.id.Id``
        :param destination_resource_id: ``Id`` of another ``Resource``
        :type destination_resource_id: ``osid.id.Id``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``source_resource_id, destination_resource_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_by_genus_type_for_resources(self, source_resource_id, destination_resource_id, relationship_genus_type):
        """Gets the ``ResourceRelationships`` given two resources and a relationship genus type which includes any genus types derived from the given genus type.

        :param source_resource_id: ``Id`` of a ``Resource``
        :type source_resource_id: ``osid.id.Id``
        :param destination_resource_id: ``Id`` of another ``Resource``
        :type destination_resource_id: ``osid.id.Id``
        :param relationship_genus_type: a relationship genus type
        :type relationship_genus_type: ``osid.type.Type``
        :return: the relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``NullArgument`` -- ``source_resource_id, destination_resource_id,`` or ``relatonship_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_by_genus_type_for_resources_on_date(self, source_resource_id, destination_resource_id, relationship_genus_type, from_, to):
        """Gets a list of resource relationships of a given genus type for a two peer resources and effective during the entire given date range inclusive but not confined to the date range.

        :param source_resource_id: a resource ``Id``
        :type source_resource_id: ``osid.id.Id``
        :param destination_resource_id: ``Id`` of another ``Resource``
        :type destination_resource_id: ``osid.id.Id``
        :param relationship_genus_type: a relationship genus type
        :type relationship_genus_type: ``osid.type.Type``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``source_resource_id, destination_resource_id, relationship_genus_type, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships(self):
        """Gets all ``ResourceRelationships``.

        :return: the relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    resource_relationships = property(fget=get_resource_relationships)


##
# The following methods are from osid.resource.ResourceRelationshipQuerySession

    def can_search_resource_relationships(self):
        """Tests if this user can perform ``ResourceRelationship`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_query(self):
        """Gets a relationship query.

        :return: the relationship query
        :rtype: ``osid.resource.ResourceRelationshipQuery``

        """
        raise UNIMPLEMENTED()

    resource_relationship_query = property(fget=get_resource_relationship_query)

    def get_resource_relationships_by_query(self, resource_relationship_query):
        """Gets a list of ``ResourceRelationship`` matching the given resource relationship query.

        :param resource_relationship_query: the resource relationship query
        :type resource_relationship_query: ``osid.resource.ResourceRelationshipQuery``
        :return: the returned ``ResourceRelationshipList``
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``NullArgument`` -- ``resource_relationship_query is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``resource_relationship_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.ResourceRelationshipSearchSession

    def get_resource_relationship_search(self):
        """Gets a relationship search.

        :return: the relationship search
        :rtype: ``osid.resource.ResourceRelationshipSearch``

        """
        raise UNIMPLEMENTED()

    resource_relationship_search = property(fget=get_resource_relationship_search)

    def get_resource_relationship_search_order(self):
        """Gets a relationship search order.
        The ``ResourceRelationshipSearchOrder`` is supplied to a
        ``ResourceRelationshipSearch`` to specify the ordering of
        results.

        :return: the relationship search order
        :rtype: ``osid.resource.ResourceRelationshipSearchOrder``

        """
        raise UNIMPLEMENTED()

    resource_relationship_search_order = property(fget=get_resource_relationship_search_order)

    def get_resource_relationships_by_search(self, resource_relationship_query, resource_relationship_search):
        """Gets the search results matching the given search query using the given search.

        :param resource_relationship_query: the resource relationship query
        :type resource_relationship_query: ``osid.resource.ResourceRelationshipQuery``
        :param resource_relationship_search: the resource relationship search
        :type resource_relationship_search: ``osid.resource.ResourceRelationshipSearch``
        :return: the returned resource relationship search results
        :rtype: ``osid.resource.ResourceRelationshipSearchResults``
        :raise: ``NullArgument`` -- ``resource_relationship_query`` or r ``esource_relationship_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``resource_relationship_search`` or r ``esource_relationship_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_query_from_inspector(self, resource_relationship_query_inspector):
        """Gets a resource relationship query from an inspector.
        The inspector is available from a
        ``ResourceRelationshipSearchResults``.

        :param resource_relationship_query_inspector: a query inspector
        :type resource_relationship_query_inspector: ``osid.resource.ResourceRelationshipQueryInspector``
        :return: the resource relationship query
        :rtype: ``osid.resource.ResourceRelationshipQuery``
        :raise: ``NullArgument`` -- ``resource_relationship_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``resource_relationship_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.ResourceRelationshipAdminSession

    def can_create_resource_relationships(self):
        """Tests if this user can create ``ResourceRelationships``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``ResourceRelationship`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer create operations to an unauthorized user.

        :return: ``false`` if ``ResourceRelationship`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_resource_relationship_with_record_types(self, resource_relationship_record_types):
        """Tests if this user can create a single ``ResourceRelationship`` using the desired record types.
        While ``ResourceManager.getResourceRelationshipRecordTypes()``
        can be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``ResourceRelationship``. Providing an empty array tests if a
        ``ResourceRelationship`` can be created with no records.

        :param resource_relationship_record_types: array of resource relationship types
        :type resource_relationship_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``ResourceRelationship`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``resource_relationship_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_form_for_create(self, source_resource_id, destination_resource_id, resource_relationship_record_types):
        """Gets the relationship form for creating new relationships.
        A new form should be requested for each create transaction.

        :param source_resource_id: the ``Id`` of the source ``Resource``
        :type source_resource_id: ``osid.id.Id``
        :param destination_resource_id: the ``Id`` of the destination ``Resource``
        :type destination_resource_id: ``osid.id.Id``
        :param resource_relationship_record_types: array of resource relationship types
        :type resource_relationship_record_types: ``osid.type.Type[]``
        :return: the relationship form
        :rtype: ``osid.resource.ResourceRelationshipForm``
        :raise: ``NotFound`` -- ``source_resource_id`` or ``destination_resource_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` or ``peer_resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        """
        raise UNIMPLEMENTED()

    def create_resource_relationship(self, resource_relationship_form):
        """Creates a new ``ResourceRelationship``.

        :param resource_relationship_form: the form for this ``ResourceRelationship``
        :type resource_relationship_form: ``osid.resource.ResourceRelationshipForm``
        :return: the new ``ResourceRelationship``
        :rtype: ``osid.resource.ResourceRelationship``
        :raise: ``IllegalState`` -- ``resource_relationship_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``resource_id, peer_resource_id`` or ``resource_relationship_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``resource_relationship_form`` did not originate from ``get_resource_relationship_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_resource_relationships(self):
        """Tests if this user can update ``ResourceRelationships``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``ResourceRelationship`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: ``false`` if relationship modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_form_for_update(self, resource_relationship_id):
        """Gets the relationship form for updating an existing relationship.
        A new relationship form should be requested for each update
        transaction.

        :param resource_relationship_id: the ``Id`` of the ``ResourceRelationship``
        :type resource_relationship_id: ``osid.id.Id``
        :return: the relationship form
        :rtype: ``osid.resource.ResourceRelationshipForm``
        :raise: ``NotFound`` -- ``resource_relationship_id`` not found
        :raise: ``NullArgument`` -- ``resource_relationship_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def update_resource_relationship(self, resource_relationship_form):
        """Updates an existing relationship.

        :param resource_relationship_form: the form containing the elements to be updated
        :type resource_relationship_form: ``osid.resource.ResourceRelationshipForm``
        :raise: ``IllegalState`` -- ``resource_relationship_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``resource_relationship_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``resource_relationship_form`` did not originate from ``get_resource_relationship_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_resource_relationships(self):
        """Tests if this user can delete ``ResourceRelationships``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``ResourceRelationship`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer delete operations to an unauthorized user.

        :return: ``false`` if ``ResourceRelationship`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_resource_relationship(self, resource_relationship_id):
        """Deletes the ``ResourceRelationship`` identified by the given ``Id``.

        :param resource_relationship_id: the ``Id`` of the ``ResourceRelationship`` to delete
        :type resource_relationship_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``ResourceRelationship`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``resource_relationship_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_resource_relationship_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``ResourceRelationships``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``ResourceRelationship`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_resource_relationship(self, resource_relationship_id, alias_id):
        """Adds an ``Id`` to a ``ResourceRelationship`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``ResourceRelationship`` is determined
        by the provider. The new ``Id`` performs as an alias to the
        primary ``Id`` . If the alias is a pointer to another resource
        relationshp, it is reassigned to the given resource relationship
        ``Id``.

        :param resource_relationship_id: the ``Id`` of a ``ResourceRelationship``
        :type resource_relationship_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``resource_relationship_id`` not found
        :raise: ``NullArgument`` -- ``resource_relationship_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.ResourceRelationshipNotificationSession

    def can_register_for_resource_relationship_notifications(self):
        """Tests if this user can register for ``ResourceRelationship`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_resource_relationships(self):
        """Register for notifications of new relationship.
        ``ResourceRelationshipReceiver.newResourceRelationship()`` is
        invoked when a new relationship is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_resource_relationships_by_genus_type(self, resource_relationship_genus_type):
        """Register for notifications of new relationships of the given genus type.
        ``ResourceRelationshipReceiver.newResourceRelationship()`` is
        invoked when a new relationship is created.

        :param resource_relationship_genus_type: the rsource relationship genus type
        :type resource_relationship_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``resource_relationship_genus_type is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_resource_relationships_for_resource(self, resource_id):
        """Register for notifications of new relationships for the given resource.
        ``ResourceRelationshipReceiver.newResourceRelationship()`` is
        invoked when a new relationship is created.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_resource_relationships(self):
        """Registers for notification of updated relationships.
        ``ResourceRelationshipReceiver.changedResourceRelationship()``
        is invoked when a relationship is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_resource_relationships_by_genus_type(self, resource_relationship_genus_type):
        """Register for notifications of changed relationshipsof the given genus type.
        ``ResourceRelationshipReceiver.changedResourceRelationship()``
        is invoked when a relationship is changed.

        :param resource_relationship_genus_type: the rsource relationship genus type
        :type resource_relationship_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``resource_relationship_genus_type is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_resource_relationships_for_resource(self, resource_id):
        """Register for notifications of changed relationships for the given resource.
        ``ResourceRelationshipReceiver.changedResourceRelationship()``
        is invoked when a relationship is changed.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_resource_relationship(self, resource_relationship_id):
        """Registers for notification of an updated relationship.
        ``ResourceRelationshipReceiver.changedResourceRelationship()``
        is invoked when the specified relationship is changed.

        :param resource_relationship_id: the ``Id`` of the ``ResourceRelationship`` to monitor
        :type resource_relationship_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_relationship_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_resource_relationships(self):
        """Registers for notification of deleted relationships.
        ``ResourceRelationshipReceiver.deletedResourceRelationship()``
        is invoked when a relationship is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_resource_relationships_for_resource(self, resource_relationship_genus_type):
        """Register for notifications of deleted relationships of the given genus type.
        ``ResourceRelationshipReceiver.deletedResourceRelationship()``
        is invoked when a relationship is deleted.

        :param resource_relationship_genus_type: the rsource relationship genus type
        :type resource_relationship_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``resource_relationship_genus_type is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_resource_relationship(self, resource_relationship_id):
        """Registers for notification of a deleted relationship.
        ``ResourceRelationshipReceiver.changedResourceRelationship()``
        is invoked when the specified relationship is deleted.

        :param resource_relationship_id: the ``Id`` of the ``ResourceRelationship`` to monitor
        :type resource_relationship_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_relationship_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.ResourceRelationshipBinSession

    def can_lookup_resource_relationship_bin_mappings(self):
        """Tests if this user can perform lookups of resource relationship/bin mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_resource_relationship_ids_by_bin(self, bin_id):
        """Gets the list of ``ResourceRelationship``  ``Ids`` associated with a ``Bin``.

        :param bin_id: ``Id`` of a ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: list of related resource relationship ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_by_bin(self, bin_id):
        """Gets the list of ``ResourceRelationships`` associated with a ``Bin``.

        :param bin_id: ``Id`` of a ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: list of related resource relationship
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_ids_by_bins(self, bin_ids):
        """Gets the list of ``ResourceRelationship Ids`` corresponding to a list of ``Bin`` objects.

        :param bin_ids: list of bin ``Ids``
        :type bin_ids: ``osid.id.IdList``
        :return: list of resource relationship ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bin_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_relationships_by_bins(self, bin_ids):
        """Gets the list of ``ResourceRelationships`` corresponding to a list of ``Bins``.

        :param bin_ids: list of bin ``Ids``
        :type bin_ids: ``osid.id.IdList``
        :return: list of resource relationships
        :rtype: ``osid.resource.ResourceRelationshipList``
        :raise: ``NullArgument`` -- ``bin_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bin_ids_by_resource_relationship(self, resource_relationship_id):
        """Gets the list of ``Bin``  ``Ids`` mapped to a ``ResourceRelationship``.

        :param resource_relationship_id: ``Id`` of a ``ResourceRelationship``
        :type resource_relationship_id: ``osid.id.Id``
        :return: list of bin ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``resource_relationship_id`` is not found
        :raise: ``NullArgument`` -- ``resource_relationship_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bins_by_resource_relationship(self, resource_relationship_id):
        """Gets the list of ``Bin`` objects mapped to a ``ResourceRelationship``.

        :param resource_relationship_id: ``Id`` of a ``ResourceRelationship``
        :type resource_relationship_id: ``osid.id.Id``
        :return: list of bins
        :rtype: ``osid.resource.BinList``
        :raise: ``NotFound`` -- ``resource_relationship_id`` is not found
        :raise: ``NullArgument`` -- ``resource_relationship_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.ResourceRelationshipBinAssignmentSession

    def can_assign_resource_relationships(self):
        """Tests if this user can alter resource relationship/bin mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_resource_relationships_to_bin(self, bin_id):
        """Tests if this user can alter resource relationship/bin mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied`` . This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_bin_ids_for_resource_relationship(self, bin_id, resource_relationship_id):
        """Gets a list of bins including and under the given bin node in which a specific resource relationship can be assigned.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param resource_relationship_id: the ``Id`` of the ``ResourceRelationship``
        :type resource_relationship_id: ``osid.id.Id``
        :return: list of assignable bin ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bin_id`` or ``resource_relationship_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_resource_relationship_to_bin(self, resource_relationship_id, bin_id):
        """Adds an existing ``ResourceRelationship`` to a ``Bin``.

        :param resource_relationship_id: the ``Id`` of the ``ResourceRelationship``
        :type resource_relationship_id: ``osid.id.Id``
        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``resource_relationship_id`` is already assigned to ``bin_id``
        :raise: ``NotFound`` -- ``resource_relationship_id`` or ``bin_id`` not found
        :raise: ``NullArgument`` -- ``resource_relationship_id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_resource_relationship_from_bin(self, resource_relationship_id, bin_id):
        """Removes a ``ResourceRelationship`` from a ``Bin``.

        :param resource_relationship_id: the ``Id`` of the ``ResourceRelationship``
        :type resource_relationship_id: ``osid.id.Id``
        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``resource_relationship_id`` or ``bin_id`` not found or ``resource_relationship_id`` not assigned to ``bin_id``
        :raise: ``NullArgument`` -- ``resource_relationship_id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.resource.ResourceRelationshipSmartBinSession

    def apply_resource_relationship_query(self, resource_query):
        """Applies a resource relationship query to this bin.

        :param resource_query: the resource relationship query
        :type resource_query: ``osid.resource.ResourceRelationshipQuery``
        :raise: ``NullArgument`` -- ``resource_relationship_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``resource_relationship_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_resource_relationship_query(self):
        """Gets a resource relationship query inspector for this bin.

        :return: the resource relationship query inspector
        :rtype: ``osid.resource.ResourceRelationshipQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_resource_relationship_sequencing(self, resource_relationship_search_order):
        """Applies a resource relationship search order to this bin.

        :param resource_relationship_search_order: the resource relationship search order
        :type resource_relationship_search_order: ``osid.resource.ResourceRelationshipSearchOrder``
        :raise: ``NullArgument`` -- ``resource_relationship_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``resource_relationship_search_order`` not of this service

        """
        raise UNIMPLEMENTED()



class BinList(osid_objects.OsidList):

    def get_next_bin(self):
        """Gets the next ``Bin`` in this list.

        :return: the next ``Bin`` in this list. The ``has_next()`` method should be used to test that a next ``Bin`` is available before calling this method.
        :rtype: ``osid.resource.Bin``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    next_bin = property(fget=get_next_bin)

    def get_next_bins(self, n):
        """Gets the next set of ``Bin`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Bin`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Bin`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.resource.Bin``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()



class Bins(ResourceManager):
    pass


