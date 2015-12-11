
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class ResourceProfile(osid_managers.OsidProfile):
    """The resource profile describes interoperability among resource services."""
    



    def supports_visible_federation(self):
        """Tests if federation is visible.

        return: (boolean) - ``true`` if visible federation is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_lookup(self):
        """Tests if resource lookup is supported.

        return: (boolean) - ``true`` if resource lookup is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_query(self):
        """Tests if resource query is supported.

        return: (boolean) - ``true`` if resource query is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_search(self):
        """Tests if resource search is supported.

        return: (boolean) - ``true`` if resource search is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_admin(self):
        """Tests if resource administration is supported.

        return: (boolean) - ``true`` if resource administration is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_notification(self):
        """Tests if resource notification is supported.

        Messages may be sent when resources are created, modified, or
        deleted.

        return: (boolean) - ``true`` if resource notification is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_bin(self):
        """Tests if retrieving mappings of resource and bins is supported.

        return: (boolean) - ``true`` if resource bin mapping retrieval
                is supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_bin_assignment(self):
        """Tests if managing mappings of resource and bins is supported.

        return: (boolean) - ``true`` if resource bin assignment is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_smart_bin(self):
        """Tests if resource smart bins are available.

        return: (boolean) - ``true`` if resource smart bins are
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_membership(self):
        """Tests if membership queries are supported.

        return: (boolean) - ``true`` if membership queries are supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_group(self):
        """Tests if group resources are supported.

        return: (boolean) - ``true`` if group resources are supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_group_assignment(self):
        """Tests if group resource assignment is supported.

        return: (boolean) - ``true`` if group resource assignment is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_group_notification(self):
        """Tests if group resource notification is supported.

        return: (boolean) - ``true`` if group resource notification is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_group_hierarchy(self):
        """Tests if a group resource hierarchy service is supported.

        return: (boolean) - ``true`` if group resource hierarchy is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_agent(self):
        """Tests if retrieving mappings of resource and agents is supported.

        return: (boolean) - ``true`` if resource agent mapping retrieval
                is supported ``,`` ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_agent_assignment(self):
        """Tests if managing mappings of resources and agents is supported.

        return: (boolean) - ``true`` if resource agent assignment is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_relationship_lookup(self):
        """Tests if looking up resource relationships is supported.

        return: (boolean) - ``true`` if resource relationships lookup is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_relationship_query(self):
        """Tests if querying resource relationships is supported.

        return: (boolean) - ``true`` if resource relationships query is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_relationship_search(self):
        """Tests if searching resource relationships is supported.

        return: (boolean) - ``true`` if resource relationships search is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_relationship_admin(self):
        """Tests if a resource relationshipsadministrative service is supported.

        return: (boolean) - ``true`` if resource relationships
                administration is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_relationship_notification(self):
        """Tests if a resource relationshipsnotification service is supported.

        return: (boolean) - ``true`` if resource relationships
                notification is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_relationship_bin(self):
        """Tests if retrieving mappings of resource relationships and bins is supported.

        return: (boolean) - ``true`` if resource relationship bin
                mapping retrieval is supported ``,``  ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_relationship_bin_assignment(self):
        """Tests if managing mappings of resource relationships and bins is supported.

        return: (boolean) - ``true`` if resource relationship bin
                assignment is supported ``,`` ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_relationship_smart_bin(self):
        """Tests if resource relationship smart bins are available.

        return: (boolean) - ``true`` if resource relationship smart bins
                are supported ``,`` ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_bin_lookup(self):
        """Tests if bin lookup is supported.

        return: (boolean) - ``true`` if bin lookup is supported ``,``
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_bin_query(self):
        """Tests if bin query is supported.

        return: (boolean) - ``true`` if bin query is supported ``,``
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_bin_search(self):
        """Tests if bin search is supported.

        return: (boolean) - ``true`` if bin search is supported ``,``
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_bin_admin(self):
        """Tests if bin administration is supported.

        return: (boolean) - ``true`` if bin administration is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_bin_notification(self):
        """Tests if bin notification is supported.

        Messages may be sent when ``Bin`` objects are created, deleted
        or updated. Notifications for resources within bins are sent via
        the resource notification session.

        return: (boolean) - ``true`` if bin notification is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_bin_hierarchy(self):
        """Tests if a bin hierarchy traversal is supported.

        return: (boolean) - ``true`` if a bin hierarchy traversal is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_bin_hierarchy_design(self):
        """Tests if a bin hierarchy design is supported.

        return: (boolean) - ``true`` if a bin hierarchy design is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_batch(self):
        """Tests if a resource batch service is available.

        return: (boolean) - ``true`` if a resource batch service is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_resource_demographic(self):
        """Tests if a resource demographic service is available.

        return: (boolean) - ``true`` if a resource demographic service
                is available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_resource_record_types(self):
        """Gets all the resource record types supported.

        return: (osid.type.TypeList) - the list of supported resource
                record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    resource_record_types = property(fget=get_resource_record_types)


    def supports_resource_record_type(self, resource_record_type):
        """Tests if a given resource record type is supported.

        arg:    resource_record_type (osid.type.Type): the resource type
        return: (boolean) - ``true`` if the resource record type is
                supported ``,``  ``false`` otherwise
        raise:  NullArgument - ``resource_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_resource_search_record_types(self):
        """Gets all the resource search record types supported.

        return: (osid.type.TypeList) - the list of supported resource
                search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    resource_search_record_types = property(fget=get_resource_search_record_types)


    def supports_resource_search_record_type(self, resource_search_record_type):
        """Tests if a given resource search type is supported.

        arg:    resource_search_record_type (osid.type.Type): the
                resource search type
        return: (boolean) - ``true`` if the resource search record type
                is supported ``,`` ``false`` otherwise
        raise:  NullArgument - ``resource_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_resource_relationship_record_types(self):
        """Gets the supported ``ResourceRelationship`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``ResourceRelationship`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    resource_relationship_record_types = property(fget=get_resource_relationship_record_types)


    def supports_resource_relationship_record_type(self, resource_relationship_record_type):
        """Tests if the given ``ResourceRelationship`` record type is supported.

        arg:    resource_relationship_record_type (osid.type.Type): a
                ``Type`` indicating a ``ResourceRelationship`` record
                type
        return: (boolean) - ``true`` if the given type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``resource_relationship_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_resource_relationship_search_record_types(self):
        """Gets the supported ``ResourceRelationship`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``ResourceRelationship`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    resource_relationship_search_record_types = property(fget=get_resource_relationship_search_record_types)


    def supports_resource_relationship_search_record_type(self, resource_relationship_search_record_type):
        """Tests if the given ``ResourceRelationship`` search record type is supported.

        arg:    resource_relationship_search_record_type
                (osid.type.Type): a ``Type`` indicating a
                ``ResourceRelationship`` search record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument -
                ``resource_relationship_search_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_bin_record_types(self):
        """Gets all the bin record types supported.

        return: (osid.type.TypeList) - the list of supported bin record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    bin_record_types = property(fget=get_bin_record_types)


    def supports_bin_record_type(self, bin_record_type):
        """Tests if a given bin record type is supported.

        arg:    bin_record_type (osid.type.Type): the bin record type
        return: (boolean) - ``true`` if the bin record type is supported
                ``,``  ``false`` otherwise
        raise:  NullArgument - ``bin_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_bin_search_record_types(self):
        """Gets all the bin search record types supported.

        return: (osid.type.TypeList) - the list of supported bin search
                record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    bin_search_record_types = property(fget=get_bin_search_record_types)


    def supports_bin_search_record_type(self, bin_search_record_type):
        """Tests if a given bin search record type is supported.

        arg:    bin_search_record_type (osid.type.Type): the bin search
                record type
        return: (boolean) - ``true`` if the bin search record type is
                supported ``,``  ``false`` otherwise
        raise:  NullArgument - ``bin_search_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


class ResourceManager(osid_managers.OsidManager, osid_sessions.OsidSession, ResourceProfile):
    """The resource manager provides access to resource lookup and creation sessions and provides interoperability tests for
        various aspects of this service.

    The sessions included in this manager are:

      * ``ResourceLookupSession:`` a session to retrieve resources
      * ``ResourceQuerySession:`` a session to query resources
      * ``ResourceSearchSession:`` a session to search for resources
      * ``ResourceAdminSession:`` a session to create and delete
        resources
      * ``ResourceNotificationSession:`` a session to receive
        notifications pertaining to resource changes
      * ``ResourceBinSession:`` a session to look up resource to bin
        mappings
      * ``ResourceBinAssignmentSession:`` a session to manage resource
        to bin mappings
      * ``ResourceSmartBinSession:`` a session to manage smart resource
        bins
      * ``MembershipSession:`` a session to query memberships
      * ``GroupSession:`` a session to retrieve group memberships
      * ``GroupAssignmentSession:`` a session to manage groups
      * ``GroupNotificationSession:`` a session to retrieve
        notifications on changes to group membership
      * ``GroupHierarchySession:`` a session to view a group hierarchy
      * ``RsourceAgentSession:`` a session to retrieve ``Resource`` and
        ``Agent`` mappings
      * ``ResourceAgentAssignmentSession:`` a session to manage
        ``Resource`` and ``Agent`` mappings

      * ``ResourceRelationshipLookupSession:`` a session to retrieve
        resource relationships
      * ``ResourceRelationshipQuerySession:`` a session to query for
        resource relationships
      * ``ResourceRelationshipSearchSession:`` a session to search for
        resource relationships
      * ``ResourceRelationshipAdminSession:`` a session to create and
        delete resource relationships
      * ``ResourceRelationshipNotificationSession:`` a session to
        receive notifications pertaining to resource relationshipchanges
      * ``ResourceRelationshipBinSession:`` a session to look up
        resource relationship to bin mappings
      * ``ResourceRelationshipBinAssignmentSession:`` a session to
        manage resource relationship to bin mappings
      * ``ResourceRelationshipSmartBinSession:`` a session to manage
        smart resource relationship bins

      * ``BinLookupSession: a`` session to retrieve bins
      * ``BinQuerySession:`` a session to query bins
      * ``BinSearchSession:`` a session to search for bins
      * ``BinAdminSession:`` a session to create, update and delete bins
      * ``BinNotificationSession:`` a session to receive notifications
        pertaining to changes in bins
      * ``BinHierarchySession:`` a session to traverse bin hierarchies
      * ``BinHierarchyDesignSession:`` a session to manage bin
        hierarchies

    """
    



    def get_resource_lookup_session(self):
        """Gets the ``OsidSession`` associated with the resource lookup service.

        return: (osid.resource.ResourceLookupSession) - ``a
                ResourceLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_lookup()`` is ``true``.*

        """
        return # osid.resource.ResourceLookupSession

    resource_lookup_session = property(fget=get_resource_lookup_session)


    def get_resource_lookup_session_for_bin(self, bin_id):
        """Gets the ``OsidSession`` associated with the resource lookup service for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.ResourceLookupSession) - ``a
                ResourceLookupSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_resource_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.resource.ResourceLookupSession


    def get_resource_query_session(self):
        """Gets a resource query session.

        return: (osid.resource.ResourceQuerySession) - ``a
                ResourceQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` is ``true``.*

        """
        return # osid.resource.ResourceQuerySession

    resource_query_session = property(fget=get_resource_query_session)


    def get_resource_query_session_for_bin(self, bin_id):
        """Gets a resource query session for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.ResourceQuerySession) - ``a
                ResourceQuerySession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_resource_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.resource.ResourceQuerySession


    def get_resource_search_session(self):
        """Gets a resource search session.

        return: (osid.resource.ResourceSearchSession) - ``a
                ResourceSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_search()`` is ``true``.*

        """
        return # osid.resource.ResourceSearchSession

    resource_search_session = property(fget=get_resource_search_session)


    def get_resource_search_session_for_bin(self, bin_id):
        """Gets a resource search session for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.ResourceSearchSession) - ``a
                ResourceSearchSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_resource_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.resource.ResourceSearchSession


    def get_resource_admin_session(self):
        """Gets a resource administration session for creating, updating and deleting resources.

        return: (osid.resource.ResourceAdminSession) - ``a
                ResourceAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_admin()`` is ``true``.*

        """
        return # osid.resource.ResourceAdminSession

    resource_admin_session = property(fget=get_resource_admin_session)


    def get_resource_admin_session_for_bin(self, bin_id):
        """Gets a resource administration session for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.ResourceAdminSession) - ``a
                ResourceAdminSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.resource.ResourceAdminSession


    def get_resource_notification_session(self, resource_receiver):
        """Gets the notification session for notifications pertaining to resource changes.

        arg:    resource_receiver (osid.resource.ResourceReceiver): the
                notification callback
        return: (osid.resource.ResourceNotificationSession) - ``a
                ResourceNotificationSession``
        raise:  NullArgument - ``resource_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_notification()`` is ``true``.*

        """
        return # osid.resource.ResourceNotificationSession


    def get_resource_notification_session_for_bin(self, resource_receiver, bin_id):
        """Gets the resource notification session for the given bin.

        arg:    resource_receiver (osid.resource.ResourceReceiver): the
                notification callback
        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.ResourceNotificationSession) - ``a
                ResourceNotificationSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``resource_receiver`` or ``bin_id`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_resource_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_notfication()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.resource.ResourceNotificationSession


    def get_resource_bin_session(self):
        """Gets the session for retrieving resource to bin mappings.

        return: (osid.resource.ResourceBinSession) - a
                ``ResourceBinSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_bin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_bin()`` is ``true``.*

        """
        return # osid.resource.ResourceBinSession

    resource_bin_session = property(fget=get_resource_bin_session)


    def get_resource_bin_assignment_session(self):
        """Gets the session for assigning resource to bin mappings.

        return: (osid.resource.ResourceBinAssignmentSession) - a
                ``ResourceBinAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_bin_assignment()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_bin_assignment()`` is ``true``.*

        """
        return # osid.resource.ResourceBinAssignmentSession

    resource_bin_assignment_session = property(fget=get_resource_bin_assignment_session)


    def get_resource_smart_bin_session(self, bin_id):
        """Gets the session for managing dynamic resource bins.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.ResourceSmartBinSession) - a
                ``ResourceSmartBinSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_smart_bin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_smart_bin()`` is ``true``.*

        """
        return # osid.resource.ResourceSmartBinSession


    def get_membership_session(self):
        """Gets the session for querying memberships.

        return: (osid.resource.MembershipSession) - a
                ``MembershipSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_membership()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``support_membership()`` is ``true``.*

        """
        return # osid.resource.MembershipSession

    membership_session = property(fget=get_membership_session)


    def get_membership_session_for_bin(self, bin_id):
        """Gets a resource membership session for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.MembershipSession) - ``a
                MembershipSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_membership()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_membership()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return # osid.resource.MembershipSession


    def get_group_session(self):
        """Gets the session for retrieving gropup memberships.

        return: (osid.resource.GroupSession) - a ``GroupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_group()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_group()`` is ``true``.*

        """
        return # osid.resource.GroupSession

    group_session = property(fget=get_group_session)


    def get_group_session_for_bin(self, bin_id):
        """Gets a group session for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.GroupSession) - a ``GroupSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_group()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_group()`` and ``supports_visible_federation()`` are
        ``true``.*

        """
        return # osid.resource.GroupSession


    def get_group_assignment_session(self):
        """Gets the session for assigning resources to groups.

        return: (osid.resource.GroupAssignmentSession) - a
                ``GroupAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_group_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_group_assignment()`` is ``true``.*

        """
        return # osid.resource.GroupAssignmentSession

    group_assignment_session = property(fget=get_group_assignment_session)


    def get_group_assignment_session_for_bin(self, bin_id):
        """Gets a group assignment session for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.GroupAssignmentSession) - a
                ``GroupAssignmentSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_group_assignment()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_group_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.resource.GroupAssignmentSession


    def get_group_notification_session(self, group_rceeiver):
        """Gets the notification session for notifications pertaining to resource changes.

        arg:    group_rceeiver (osid.resource.GroupReceiver): the
                notification callback
        return: (osid.resource.GroupNotificationSession) - ``a
                GroupNotificationSession``
        raise:  NullArgument - ``group_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_group_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_group_notification()`` is ``true``.*

        """
        return # osid.resource.GroupNotificationSession


    def get_group_notification_session_for_bin(self, group_rceeiver, bin_id):
        """Gets the group notification session for the given bin.

        arg:    group_rceeiver (osid.resource.GroupReceiver): the
                notification callback
        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.GroupNotificationSession) - ``a
                GroupNotificationSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``group_receiver`` or ``bin_id`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_group_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_group_notfication()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.resource.GroupNotificationSession


    def get_group_hierarchy_session(self):
        """Gets a session for retrieving gropup hierarchies.

        return: (osid.resource.GroupHierarchySession) - ``a
                GroupHierarchySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_group_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_group_hierarchy()`` is ``true``.*

        """
        return # osid.resource.GroupHierarchySession

    group_hierarchy_session = property(fget=get_group_hierarchy_session)


    def get_group_hierarchy_session_for_bin(self, bin_id):
        """Gets a group hierarchy session for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.GroupHierarchySession) - a
                ``GroupHierarchySession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_group_hierarchy()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_group_hierarchy()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.resource.GroupHierarchySession


    def get_resource_agent_session(self):
        """Gets the session for retrieving resource agent mappings.

        return: (osid.resource.ResourceAgentSession) - a
                ``ResourceAgentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_agent()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_agent()`` is ``true``.*

        """
        return # osid.resource.ResourceAgentSession

    resource_agent_session = property(fget=get_resource_agent_session)


    def get_resource_agent_session_for_bin(self, bin_id):
        """Gets a resource agent session for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.ResourceAgentSession) - a
                ``ResourceAgentSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_agent()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_agent()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.resource.ResourceAgentSession


    def get_resource_agent_assignment_session(self):
        """Gets the session for assigning agents to resources.

        return: (osid.resource.ResourceAgentAssignmentSession) - a
                ``ResourceAgentAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_agent_assignment()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_agent_assignment()`` is ``true``.*

        """
        return # osid.resource.ResourceAgentAssignmentSession

    resource_agent_assignment_session = property(fget=get_resource_agent_assignment_session)


    def get_resource_agent_assignment_session_for_bin(self, bin_id):
        """Gets a resource agent session for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.ResourceAgentAssignmentSession) - a
                ``ResourceAgentAssignmentSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_agent_assignment()``
                or ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_agent_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.resource.ResourceAgentAssignmentSession


    def get_resource_relationship_lookup_session(self):
        """Gets the ``OsidSession`` associated with the resource relationship lookup service.

        return: (osid.resource.ResourceRelationshipLookupSession) - a
                ``ResourceRelationshipLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_resource_relationship_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_lookup()`` is ``true``.*

        """
        return # osid.resource.ResourceRelationshipLookupSession

    resource_relationship_lookup_session = property(fget=get_resource_relationship_lookup_session)


    def get_resource_relationship_lookup_session_for_bin(self, bin_id):
        """Gets the ``OsidSession`` associated with the resource relationship lookup service for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        return: (osid.resource.ResourceRelationshipLookupSession) - a
                ``ResourceRelationshipLookupSession``
        raise:  NotFound - no ``Bin`` found by the given ``Id``
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_resource_relationship_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.resource.ResourceRelationshipLookupSession


    def get_resource_relationship_query_session(self):
        """Gets the ``OsidSession`` associated with the resource relationship query service.

        return: (osid.resource.ResourceRelationshipQuerySession) - a
                ``ResourceRelationshipQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_resource_relationship_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_query()`` is ``true``.*

        """
        return # osid.resource.ResourceRelationshipQuerySession

    resource_relationship_query_session = property(fget=get_resource_relationship_query_session)


    def get_resource_relationship_query_session_for_bin(self, bin_id):
        """Gets the ``OsidSession`` associated with the resource relationship query service for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        return: (osid.resource.ResourceRelationshipQuerySession) - a
                ``ResourceRelationshipQuerySession``
        raise:  NotFound - no ``Bin`` found by the given ``Id``
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_resource_relationship_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.resource.ResourceRelationshipQuerySession


    def get_resource_relationship_search_session(self):
        """Gets the ``OsidSession`` associated with the resource relationship search service.

        return: (osid.resource.ResourceRelationshipSearchSession) - a
                ``ResourceRelationshipSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_resource_relationship_search()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_search()`` is ``true``.*

        """
        return # osid.resource.ResourceRelationshipSearchSession

    resource_relationship_search_session = property(fget=get_resource_relationship_search_session)


    def get_resource_relationship_search_session_for_bin(self, bin_id):
        """Gets the ``OsidSession`` associated with the resource relationship search service for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        return: (osid.resource.ResourceRelationshipSearchSession) - a
                ``ResourceRelationshipSearchSession``
        raise:  NotFound - no bin found by the given ``Id``
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_resource_relationship_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.resource.ResourceRelationshipSearchSession


    def get_resource_relationship_admin_session(self):
        """Gets the ``OsidSession`` associated with the resource relationship administration service.

        return: (osid.resource.ResourceRelationshipAdminSession) - a
                ``ResourceRelationshipAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_resource_relationship_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_admin()`` is ``true``.*

        """
        return # osid.resource.ResourceRelationshipAdminSession

    resource_relationship_admin_session = property(fget=get_resource_relationship_admin_session)


    def get_resource_relationship_admin_session_for_bin(self, bin_id):
        """Gets the ``OsidSession`` associated with the resource relationship administration service for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        return: (osid.resource.ResourceRelationshipAdminSession) - a
                ``ResourceRelationshipAdminSession``
        raise:  NotFound - no bin found by the given ``Id``
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_resource_relationship_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.resource.ResourceRelationshipAdminSession


    def get_resource_relationship_notification_session(self, resource_relationship_receiver):
        """Gets the ``OsidSession`` associated with the resource relationship notification service.

        arg:    resource_relationship_receiver
                (osid.resource.ResourceRelationshipReceiver): the
                notification callback
        return: (osid.resource.ResourceRelationshipNotificationSession)
                - a ``ResourceRelationshipNotificationSession``
        raise:  NullArgument - ``resource_relationship_receiver`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_resource_relationship_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_notification()`` is ``true``.*

        """
        return # osid.resource.ResourceRelationshipNotificationSession


    def get_resource_relationship_notification_session_for_bin(self, resource_relationship_receiver, bin_id):
        """Gets the ``OsidSession`` associated with the resource relationship notification service for the given bin.

        arg:    resource_relationship_receiver
                (osid.resource.ResourceRelationshipReceiver): the
                notification callback
        arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        return: (osid.resource.ResourceRelationshipNotificationSession)
                - a ``ResourceRelationshipNotificationSession``
        raise:  NotFound - no bin found by the given ``Id``
        raise:  NullArgument - ``resource_relationship_receiver`` or
                ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_resource_relationshipt_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.resource.ResourceRelationshipNotificationSession


    def get_resource_relationship_bin_session(self):
        """Gets the session for retrieving resource relationship to bin mappings.

        return: (osid.resource.ResourceRelationshipBinSession) - a
                ``ResourceRelationshipBinSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_relationship_bin()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_bin()`` is ``true``.*

        """
        return # osid.resource.ResourceRelationshipBinSession

    resource_relationship_bin_session = property(fget=get_resource_relationship_bin_session)


    def get_resource_relationship_bin_assignment_session(self):
        """Gets the session for assigning resource relationships to bin mappings.

        return: (osid.resource.ResourceRelationshipBinAssignmentSession)
                - a ``ResourceRelationshipBinAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_resource_relationship_bin_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_bin_assignment()`` is
        ``true``.*

        """
        return # osid.resource.ResourceRelationshipBinAssignmentSession

    resource_relationship_bin_assignment_session = property(fget=get_resource_relationship_bin_assignment_session)


    def get_resource_relationship_smart_bin_session(self, bin_id):
        """Gets the session for managing dynamic resource relationship bins.

        arg:    bin_id (osid.id.Id): the ``Id`` of the bin
        return: (osid.resource.ResourceRelationshipSmartBinSession) - a
                ``ResourceRelationshipSmartBinSession``
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_resource_relationship_smart_bin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_relationship_smart_bin()`` is ``true``.*

        """
        return # osid.resource.ResourceRelationshipSmartBinSession


    def get_bin_lookup_session(self):
        """Gets the bin lookup session.

        return: (osid.resource.BinLookupSession) - a
                ``BinLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_bin_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_bin_lookup()`` is ``true``.*

        """
        return # osid.resource.BinLookupSession

    bin_lookup_session = property(fget=get_bin_lookup_session)


    def get_bin_query_session(self):
        """Gets the bin query session.

        return: (osid.resource.BinQuerySession) - a ``BinQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_bin_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_bin_query()`` is ``true``.*

        """
        return # osid.resource.BinQuerySession

    bin_query_session = property(fget=get_bin_query_session)


    def get_bin_search_session(self):
        """Gets the bin search session.

        return: (osid.resource.BinSearchSession) - a
                ``BinSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_bin_search()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_bin_search()`` is ``true``.*

        """
        return # osid.resource.BinSearchSession

    bin_search_session = property(fget=get_bin_search_session)


    def get_bin_admin_session(self):
        """Gets the bin administrative session for creating, updating and deleteing bins.

        return: (osid.resource.BinAdminSession) - a ``BinAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_bin_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_bin_admin()`` is ``true``.*

        """
        return # osid.resource.BinAdminSession

    bin_admin_session = property(fget=get_bin_admin_session)


    def get_bin_notification_session(self, bin_receiver):
        """Gets the notification session for subscribing to changes to a bin.

        arg:    bin_receiver (osid.resource.BinReceiver): the
                notification callback
        return: (osid.resource.BinNotificationSession) - a
                ``BinNotificationSession``
        raise:  NullArgument - ``bin_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_bin_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_bin_notification()`` is ``true``.*

        """
        return # osid.resource.BinNotificationSession


    def get_bin_hierarchy_session(self):
        """Gets the bin hierarchy traversal session.

        return: (osid.resource.BinHierarchySession) - ``a
                BinHierarchySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_bin_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_bin_hierarchy()`` is ``true``.*

        """
        return # osid.resource.BinHierarchySession

    bin_hierarchy_session = property(fget=get_bin_hierarchy_session)


    def get_bin_hierarchy_design_session(self):
        """Gets the bin hierarchy design session.

        return: (osid.resource.BinHierarchyDesignSession) - a
                ``BinHierarchyDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_bin_hierarchy_design()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_bin_hierarchy_design()`` is ``true``.*

        """
        return # osid.resource.BinHierarchyDesignSession

    bin_hierarchy_design_session = property(fget=get_bin_hierarchy_design_session)


    def get_resource_batch_manager(self):
        """Gets the ``ResourceBatchManager``.

        return: (osid.resource.batch.ResourceBatchManager) - a
                ``ResourceBatchManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_batch()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_batch()`` is ``true``.*

        """
        return # osid.resource.batch.ResourceBatchManager

    resource_batch_manager = property(fget=get_resource_batch_manager)


    def get_resource_demographic_manager(self):
        """Gets the ``ResourceDemographicManager``.

        return: (osid.resource.demographic.ResourceDemographicManager) -
                a ``ResourceDemographicManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_resource_demographic()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_resource_demographic()`` is ``true``.*

        """
        return # osid.resource.demographic.ResourceDemographicManager

    resource_demographic_manager = property(fget=get_resource_demographic_manager)


