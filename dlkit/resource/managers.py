
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class ResourceProfile(osid_managers.OsidProfile):
    """The resource profile describes interoperability among resource services."""

    def supports_resource_lookup(self):
        """Tests if resource lookup is supported.

        :return: ``true`` if resource lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_resource_query(self):
        """Tests if resource query is supported.

        :return: ``true`` if resource query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_resource_search(self):
        """Tests if resource search is supported.

        :return: ``true`` if resource search is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_resource_admin(self):
        """Tests if resource administration is supported.

        :return: ``true`` if resource administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_resource_notification(self):
        """Tests if resource notification is supported.

        Messages may be sent when resources are created, modified, or
        deleted.

        :return: ``true`` if resource notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_resource_bin(self):
        """Tests if retrieving mappings of resource and bins is supported.

        :return: ``true`` if resource bin mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_resource_bin_assignment(self):
        """Tests if managing mappings of resource and bins is supported.

        :return: ``true`` if resource bin assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_resource_agent(self):
        """Tests if retrieving mappings of resource and agents is supported.

        :return: ``true`` if resource agent mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_resource_agent_assignment(self):
        """Tests if managing mappings of resources and agents is supported.

        :return: ``true`` if resource agent assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_bin_lookup(self):
        """Tests if bin lookup is supported.

        :return: ``true`` if bin lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_bin_query(self):
        """Tests if bin query is supported.

        :return: ``true`` if bin query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_bin_admin(self):
        """Tests if bin administration is supported.

        :return: ``true`` if bin administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_bin_hierarchy(self):
        """Tests if a bin hierarchy traversal is supported.

        :return: ``true`` if a bin hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_bin_hierarchy_design(self):
        """Tests if a bin hierarchy design is supported.

        :return: ``true`` if a bin hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_resource_record_types(self):
        """Gets all the resource record types supported.

        :return: the list of supported resource record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    resource_record_types = property(fget=get_resource_record_types)

    def get_resource_search_record_types(self):
        """Gets all the resource search record types supported.

        :return: the list of supported resource search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    resource_search_record_types = property(fget=get_resource_search_record_types)

    def get_resource_relationship_record_types(self):
        """Gets the supported ``ResourceRelationship`` record types.

        :return: a list containing the supported ``ResourceRelationship`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    resource_relationship_record_types = property(fget=get_resource_relationship_record_types)

    def get_resource_relationship_search_record_types(self):
        """Gets the supported ``ResourceRelationship`` search record types.

        :return: a list containing the supported ``ResourceRelationship`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    resource_relationship_search_record_types = property(fget=get_resource_relationship_search_record_types)

    def get_bin_record_types(self):
        """Gets all the bin record types supported.

        :return: the list of supported bin record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    bin_record_types = property(fget=get_bin_record_types)

    def get_bin_search_record_types(self):
        """Gets all the bin search record types supported.

        :return: the list of supported bin search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    bin_search_record_types = property(fget=get_bin_search_record_types)


class ResourceManager(osid_managers.OsidManager, osid_sessions.OsidSession, ResourceProfile):
    """The resource manager provides access to resource lookup and creation sessions and provides interoperability tests for various aspects of this service.

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

    def get_resource_batch_manager(self):
        """Gets the ``ResourceBatchManager``.

        :return: a ``ResourceBatchManager``
        :rtype: ``osid.resource.batch.ResourceBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_batch()`` is ``true``.*

        """
        return # osid.resource.batch.ResourceBatchManager

    resource_batch_manager = property(fget=get_resource_batch_manager)

    def get_resource_demographic_manager(self):
        """Gets the ``ResourceDemographicManager``.

        :return: a ``ResourceDemographicManager``
        :rtype: ``osid.resource.demographic.ResourceDemographicManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_demographic()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_demographic()`` is ``true``.*

        """
        return # osid.resource.demographic.ResourceDemographicManager

    resource_demographic_manager = property(fget=get_resource_demographic_manager)


class ResourceProxyManager(osid_managers.OsidProxyManager, ResourceProfile):
    """The resource manager provides access to resource lookup and creation session and provides interoperability tests for various aspects of this service.

    Methods in this manager accept a ``Proxy``. The sessions included in
    this manager are:

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

    def get_resource_batch_proxy_manager(self):
        """Gets the ``ResourceBatchProxyManager``.

        :return: a ``ResourceBatchProxyManager``
        :rtype: ``osid.resource.batch.ResourceBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_batch()`` is ``true``.*

        """
        return # osid.resource.batch.ResourceBatchProxyManager

    resource_batch_proxy_manager = property(fget=get_resource_batch_proxy_manager)

    def get_resource_demographic_proxy_manager(self):
        """Gets the ``ResourceDemographicProxyManager``.

        :return: a ``ResourceDemographicProxyManager``
        :rtype: ``osid.resource.demographic.ResourceDemographicProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_demographic()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_demographic()`` is ``true``.*

        """
        return # osid.resource.demographic.ResourceDemographicProxyManager

    resource_demographic_proxy_manager = property(fget=get_resource_demographic_proxy_manager)


