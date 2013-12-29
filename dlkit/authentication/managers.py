from ..osid import managers as osid_managers


class AuthenticationProfile(osid_managers.OsidProfile):
    """The ``AuthenticationProfile`` describes the interoperability among authentication services."""
    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_authentication_acquisition(self):
        """Tests is authentication acquisition is supported.

        Authentication acquisition is responsible for acquiring client
        side authentication credentials.

        :return: ``true`` if authentication acquisiiton is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_authentication_validation(self):
        """Tests if authentication validation is supported.

        Authentication validation verifies given authentication
        credentials and maps to an agent identity.

        :return: ``true`` if authentication validation is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_agent_lookup(self):
        """Tests if an agent lookup service is supported.

        An agent lookup service defines methods to access agents.

        :return: ``true`` if agent lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_agent_query(self):
        """Tests if an agent query service is supported.

        :return: ``true`` if agent query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_agent_search(self):
        """Tests if an agent search service is supported.

        :return: ``true`` if agent search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_agent_admin(self):
        """Tests if an agent administrative service is supported.

        :return: ``true`` if agent admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_agent_notification(self):
        """Tests if agent notification is supported.

        Messages may be sent when agents are created, modified, or
        deleted.

        :return: ``true`` if agent notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_agent_agency(self):
        """Tests if retrieving mappings of agents and agencies is supported.

        :return: ``true`` if agent agency mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_agent_agency_assignment(self):
        """Tests if managing mappings of agents and agencies is supported.

        :return: ``true`` if agent agency assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_agent_smart_agency(self):
        """Tests if agent smart agency is available.

        :return: ``true`` if agent smart agency is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_agency_lookup(self):
        """Tests if an agency lookup service is supported.

        An agency lookup service defines methods to access agencies.

        :return: ``true`` if agency lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_agency_query(self):
        """Tests if an agency query service is supported.

        :return: ``true`` if agency query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_agency_search(self):
        """Tests if an agency search service is supported.

        :return: ``true`` if agency search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_agency_admin(self):
        """Tests if an agency administrative service is supported.

        :return: ``true`` if agency admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_agency_notification(self):
        """Tests if agency notification is supported.

        Messages may be sent when agencies are created, modified, or
        deleted.

        :return: ``true`` if agency notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_agency_hierarchy(self):
        """Tests if an agency hierarchy traversal is supported.

        :return: ``true`` if an agency hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_agency_hierarchy_design(self):
        """Tests if an agency hierarchy design is supported.

        :return: ``true`` if an agency hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_authentication_keys(self):
        """Tests if an authentication key service is available.

        :return: ``true`` if an authentication key service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_authentication_process(self):
        """Tests if an authentication process service is available.

        :return: ``true`` if an authentication process service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_agent_record_types(self):
        """Gets the supported ``Agent`` record types.

        :return: a list containing the supported ``Agent`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    agent_record_types = property(fget=get_agent_record_types)

    def supports_agent_record_type(self, agent_record_type):
        """Tests if the given ``Agent`` record type is supported.

        :param agent_record_type: a ``Type`` indicating an ``Agent`` record type
        :type agent_record_type: ``osid.type.Type``
        :return: ``true`` if the given record Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agent_record_type`` is ``null``

        """
        return # boolean

    def get_agent_search_record_types(self):
        """Gets the supported ``Agent`` search record types.

        :return: a list containing the supported ``Agent`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    agent_search_record_types = property(fget=get_agent_search_record_types)

    def supports_agent_search_record_type(self, agent_search_record_type):
        """Tests if the given ``Agent`` search record type is supported.

        :param agent_search_record_type: a ``Type`` indicating an ``Agent`` search record type
        :type agent_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agent_search_record_type`` is ``null``

        """
        return # boolean

    def get_agency_record_types(self):
        """Gets the supported ``Agency`` record types.

        :return: a list containing the supported ``Agency`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    agency_record_types = property(fget=get_agency_record_types)

    def supports_agency_record_type(self, agency_record_type):
        """Tests if the given ``Agency`` record type is supported.

        :param agency_record_type: a ``Type`` indicating an ``Agency`` record type
        :type agency_record_type: ``osid.type.Type``
        :return: ``true`` if the given record Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agency_record_type`` is ``null``

        """
        return # boolean

    def get_agency_search_record_types(self):
        """Gets the supported ``Agency`` search record types.

        :return: a list containing the supported ``Agency`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    agency_search_record_types = property(fget=get_agency_search_record_types)

    def supports_agency_search_record_type(self, agency_search_record_type):
        """Tests if the given ``Agency`` search record type is supported.

        :param agency_search_record_type: a ``Type`` indicating an ``Agency`` search record type
        :type agency_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agency_search_record_type`` is ``null``

        """
        return # boolean


class AuthenticationManager(osid_managers.OsidManager, AuthenticationProfile):
    """The authentication manager provides access to authentication sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``AgentLookupSession:`` a session to look up ``Agents``
      * ``AgentQuerySession:`` a session to query ``Agents``
      * ``AgentSearchSession:`` a session to search ``Agents``
      * ``AgentAdminSession:`` a session to create, modify and delete
        ``Agents``
      * ``AgentNotificationSession: a`` session to receive messages
        pertaining to ``Agent`` changes
    
      * ``AgentAgencySession:`` a session to retrieve ``Agent`` to
        ``Agency`` mappings
      * ``AgentAgencyAssignmentSession:`` a session to manage ``Agent``
        to ``Agency`` mappings
      * ``AgentSmartAgencySession:`` a session to create dynamic
        agencies
      * ``AgencyLookupSession:`` a session to lookup agencies
      * ``AgencyQuerySession:`` a session to query agencies
      * ``AgencySearchSession`` : a session to search agencies
      * ``AgencyAdminSession`` : a session to create, modify and delete
        agencies
      * ``AgencyNotificationSession`` : a session to receive messages
        pertaining to ``Agency`` changes
      * ``AgencyHierarchySession`` : a session to traverse the
        ``Agency`` hierarchy
      * ``AgencyHierarchyDesignSession`` : a session to manage the
        ``Agency`` hierarchy


    """
    def get_agent_lookup_session(self):
        """Gets the ``OsidSession`` associated with the agent lookup service.

        :return: an ``AgentLookupSession``
        :rtype: ``osid.authentication.AgentLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_lookup()`` is ``false``

        """
        return # osid.authentication.AgentLookupSession

    agent_lookup_session = property(fget=get_agent_lookup_session)

    def get_agent_lookup_session_for_agency(self, agency_id):
        """Gets the ``OsidSession`` associated with the agent lookup service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :return: ``an _agent_lookup_session``
        :rtype: ``osid.authentication.AgentLookupSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.authentication.AgentLookupSession

    def get_agent_query_session(self):
        """Gets the ``OsidSession`` associated with the agent query service.

        :return: an ``AgentQuerySession``
        :rtype: ``osid.authentication.AgentQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_query()`` is ``false``

        """
        return # osid.authentication.AgentQuerySession

    agent_query_session = property(fget=get_agent_query_session)

    def get_agent_query_session_for_agency(self, agency_id):
        """Gets the ``OsidSession`` associated with the agent query service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :return: ``an _agent_query_session``
        :rtype: ``osid.authentication.AgentQuerySession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.authentication.AgentQuerySession

    def get_agent_search_session(self):
        """Gets the ``OsidSession`` associated with the agent search service.

        :return: an ``AgentSearchSession``
        :rtype: ``osid.authentication.AgentSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_search()`` is ``false``

        """
        return # osid.authentication.AgentSearchSession

    agent_search_session = property(fget=get_agent_search_session)

    def get_agent_search_session_for_agency(self, agency_id):
        """Gets the ``OsidSession`` associated with the agent search service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :return: ``an _agent_search_session``
        :rtype: ``osid.authentication.AgentSearchSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.authentication.AgentSearchSession

    def get_agent_admin_session(self):
        """Gets the ``OsidSession`` associated with the agent administration service.

        :return: an ``AgentAdminSession``
        :rtype: ``osid.authentication.AgentAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_admin()`` is ``false``

        """
        return # osid.authentication.AgentAdminSession

    agent_admin_session = property(fget=get_agent_admin_session)

    def get_agent_admin_session_for_agency(self, agency_id):
        """Gets the ``OsidSession`` associated with the agent admin service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :return: ``an _agent_admin_session``
        :rtype: ``osid.authentication.AgentAdminSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.authentication.AgentAdminSession

    def get_agent_notification_session(self, agent_receiver):
        """Gets the notification session for notifications pertaining to service changes.

        :param agent_receiver: the agent receiver
        :type agent_receiver: ``osid.authentication.AgentReceiver``
        :return: an ``AgentNotificationSession``
        :rtype: ``osid.authentication.AgentNotificationSession``
        :raise: ``NullArgument`` -- ``agent_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_notification()`` is ``false``

        """
        return # osid.authentication.AgentNotificationSession

    def get_agent_notification_session_for_agency(self, agent_receiver, agency_id):
        """Gets the ``OsidSession`` associated with the agent notification service for the given agency.

        :param agent_receiver: the agent receiver
        :type agent_receiver: ``osid.authentication.AgentReceiver``
        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :return: ``an _agent_notification_session``
        :rtype: ``osid.authentication.AgentNotificationSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agent_receiver`` or ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.authentication.AgentNotificationSession

    def get_agent_agency_session(self):
        """Gets the session for retrieving agent to agency mappings.

        :return: an ``AgentAgencySession``
        :rtype: ``osid.authentication.AgentAgencySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_agency()`` is ``false``

        """
        return # osid.authentication.AgentAgencySession

    agent_agency_session = property(fget=get_agent_agency_session)

    def get_agent_agency_assignment_session(self):
        """Gets the session for assigning agent to agency mappings.

        :return: a ``AgentAgencyAsignmentSession``
        :rtype: ``osid.authentication.AgentAgencyAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_agency_assignment()`` is ``false``

        """
        return # osid.authentication.AgentAgencyAssignmentSession

    agent_agency_assignment_session = property(fget=get_agent_agency_assignment_session)

    def get_agent_smart_agency_session(self, agency_id):
        """Gets the ``OsidSession`` associated with the agent smart agency service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :return: an ``AgentSmartAgencySession``
        :rtype: ``osid.authentication.AgentSmartAgencySession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_smart_agency()`` is ``false``

        """
        return # osid.authentication.AgentSmartAgencySession

    def get_agency_lookup_session(self):
        """Gets the ``OsidSession`` associated with the agency lookup service.

        :return: an ``AgencyLookupSession``
        :rtype: ``osid.authentication.AgencyLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_lookup()`` is ``false``

        """
        return # osid.authentication.AgencyLookupSession

    agency_lookup_session = property(fget=get_agency_lookup_session)

    def get_agency_search_session(self):
        """Gets the ``OsidSession`` associated with the agency search service.

        :return: an ``AgencySearchSession``
        :rtype: ``osid.authentication.AgencySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_search()`` is ``false``

        """
        return # osid.authentication.AgencySearchSession

    agency_search_session = property(fget=get_agency_search_session)

    def get_agency_admin_session(self):
        """Gets the ``OsidSession`` associated with the agency administration service.

        :return: an ``AgencyAdminSession``
        :rtype: ``osid.authentication.AgencyAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_admin()`` is ``false``

        """
        return # osid.authentication.AgencyAdminSession

    agency_admin_session = property(fget=get_agency_admin_session)

    def get_agency_notification_session(self, agency_receiver):
        """Gets the notification session for notifications pertaining to agency service changes.

        :param agency_receiver: the agency receiver
        :type agency_receiver: ``osid.authentication.AgencyReceiver``
        :return: an ``AgencyNotificationSession``
        :rtype: ``osid.authentication.AgencyNotificationSession``
        :raise: ``NullArgument`` -- ``agency_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_notification()`` is ``false``

        """
        return # osid.authentication.AgencyNotificationSession

    def get_agency_hierarchy_session(self):
        """Gets the session traversing agency hierarchies.

        :return: an ``AgencyHierarchySession``
        :rtype: ``osid.authentication.AgencyHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_hierarchy()`` is ``false``

        """
        return # osid.authentication.AgencyHierarchySession

    agency_hierarchy_session = property(fget=get_agency_hierarchy_session)

    def get_agency_hierarchy_design_session(self):
        """Gets the session designing agency hierarchies.

        :return: an ``AgencyHierarchyDesignSession``
        :rtype: ``osid.authentication.AgencyHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_hierarchy_design()`` is ``false``

        """
        return # osid.authentication.AgencyHierarchyDesignSession

    agency_hierarchy_design_session = property(fget=get_agency_hierarchy_design_session)

    def get_authentication_batch_manager(self):
        """Gets an ``AuthenticationBatchManager``.

        :return: an ``AuthenticationBatchManager``.
        :rtype: ``osid.authentication.batch.AuthenticationBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_batch()`` is ``false``

        """
        return # osid.authentication.batch.AuthenticationBatchManager

    authentication_batch_manager = property(fget=get_authentication_batch_manager)

    def get_authentication_keys_manager(self):
        """Gets an ``AuthenticationKeysManager``.

        :return: an ``AuthenticationKeysManager``.
        :rtype: ``osid.authentication.keys.AuthenticationKeysManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_keys()`` is ``false``

        """
        return # osid.authentication.keys.AuthenticationKeysManager

    authentication_keys_manager = property(fget=get_authentication_keys_manager)

    def get_authentication_process_manager(self):
        """Gets an ``AuthenticationProcessManager``.

        :return: an ``AuthenticationProcessManager``.
        :rtype: ``osid.authentication.process.AuthenticationProcessManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_process()`` is ``false``

        """
        return # osid.authentication.process.AuthenticationProcessManager

    authentication_process_manager = property(fget=get_authentication_process_manager)


class AuthenticationProxyManager(osid_managers.OsidProxyManager, AuthenticationProfile):
    """The authentication proxy manager provides access to authentication sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` object.
    The sessions included in this manager are:

      * ``AgentLookupSession:`` session to look up ``Agents``
      * ``AgentQuerySession`` : a session to query ``Agents``
      * ``AgentSearchSession:`` session to search ``Agents``
      * ``AgentAdminSession:`` session to create, modify and delete
        ``Agents``
      * Agent ``NotificationSession:`` session to receive messages
        pertaining to ``Agent`` changes
    
      * ``AgentAgencySession:`` a session to retrieve ``Agent`` to
        ``Agency`` mappings
      * ``AgentAgencyAssignmentSession:`` a session to manage ``Agent``
        to ``Agency`` mappings
      * ``AgentSmartAgencySession:`` a session to create dynamic
        agencies
      * ``AgencyLookupSession:`` a session to lookup agencies
      * ``AgencyQuerySession:`` a session to query agencies
      * ``AgencySearchSession`` : a session to search agencies
      * ``AgencyAdminSession`` : a session to create, modify and delete
        agencies
      * ``AgencyNotificationSession`` : a session to receive messages
        pertaining to ``Agency`` changes
      * ``AgencyHierarchySession`` : a session to traverse the
        ``Agency`` hierarchy
      * ``AgencyHierarchyDesignSession`` : a session to manage the
        ``Agency`` hierarchy


    """
    def get_agent_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the agent lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentLookupSession``
        :rtype: ``osid.authentication.AgentLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_lookup()`` is ``false``

        """
        return # osid.authentication.AgentLookupSession

    def get_agent_lookup_session_for_agency(self, agency_id, proxy):
        """Gets the ``OsidSession`` associated with the agent lookup service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _agent_lookup_session``
        :rtype: ``osid.authentication.AgentLookupSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.authentication.AgentLookupSession

    def get_agent_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the agent query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentQuerySession``
        :rtype: ``osid.authentication.AgentQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_query()`` is ``false``

        """
        return # osid.authentication.AgentQuerySession

    def get_agent_query_session_for_agency(self, agency_id, proxy):
        """Gets the ``OsidSession`` associated with the agent query service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentQuerySession``
        :rtype: ``osid.authentication.AgentQuerySession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.authentication.AgentQuerySession

    def get_agent_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the agent search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentSearchSession``
        :rtype: ``osid.authentication.AgentSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_search()`` is ``false``

        """
        return # osid.authentication.AgentSearchSession

    def get_agent_search_session_for_agency(self, agency_id, proxy):
        """Gets the ``OsidSession`` associated with the agent search service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _agent_search_session``
        :rtype: ``osid.authentication.AgentSearchSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.authentication.AgentSearchSession

    def get_agent_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the agent administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentAdminSession``
        :rtype: ``osid.authentication.AgentAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_admin()`` is ``false``

        """
        return # osid.authentication.AgentAdminSession

    def get_agent_admin_session_for_agency(self, agency_id, proxy):
        """Gets the ``OsidSession`` associated with the agent admin service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _agent_admin_session``
        :rtype: ``osid.authentication.AgentAdminSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.authentication.AgentAdminSession

    def get_agent_notification_session(self, agent_receiver, proxy):
        """Gets the messaging receiver session for notifications pertaining to agent changes.

        :param agent_receiver: the agent receiver
        :type agent_receiver: ``osid.authentication.AgentReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentNotificationSession``
        :rtype: ``osid.authentication.AgentNotificationSession``
        :raise: ``NullArgument`` -- ``proxy`` or ``agent_receiver`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_notification()`` is ``false``

        """
        return # osid.authentication.AgentNotificationSession

    def get_agent_notification_session_for_agency(self, agent_receiver, agency_id, proxy):
        """Gets the ``OsidSession`` associated with the agent notification service for the given agency.

        :param agent_receiver: the agent receiver
        :type agent_receiver: ``osid.authentication.AgentReceiver``
        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _agent_notification_session``
        :rtype: ``osid.authentication.AgentNotificationSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agent_receiver, agency_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.authentication.AgentNotificationSession

    def get_agent_agency_session(self, proxy):
        """Gets the session for retrieving agent to agency mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentAgencySession``
        :rtype: ``osid.authentication.AgentAgencySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_agency()`` is ``false``

        """
        return # osid.authentication.AgentAgencySession

    def get_agent_agency_assignment_session(self, proxy):
        """Gets the session for assigning agent to agency mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentAgencyAssignmentSession``
        :rtype: ``osid.authentication.AgentAgencyAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_agency_assignment()`` is ``false``

        """
        return # osid.authentication.AgentAgencyAssignmentSession

    def get_agent_smart_agency_session(self, agency_id, proxy):
        """Gets the ``OsidSession`` associated with the agent smart agency service for the given agency.

        :param agency_id: the ``Id`` of the bank
        :type agency_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentSmartAgencySession``
        :rtype: ``osid.authentication.AgentSmartAgencySession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_smart_agency()`` is ``false``

        """
        return # osid.authentication.AgentSmartAgencySession

    def get_agency_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the agency lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgencyLookupSession``
        :rtype: ``osid.authentication.AgencyLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_lookup()`` is ``false``

        """
        return # osid.authentication.AgencyLookupSession

    def get_agency_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the agency search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgencySearchSession``
        :rtype: ``osid.authentication.AgencySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_search()`` is ``false``

        """
        return # osid.authentication.AgencySearchSession

    def get_agency_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the agency administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgencyAdminSession``
        :rtype: ``osid.authentication.AgencyAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_admin()`` is ``false``

        """
        return # osid.authentication.AgencyAdminSession

    def get_agency_notification_session(self, agency_receiver, proxy):
        """Gets the messaging receiver session for notifications pertaining to agency changes.

        :param agency_receiver: the agency receiver
        :type agency_receiver: ``osid.authentication.AgencyReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgencyNotificationSession``
        :rtype: ``osid.authentication.AgencyNotificationSession``
        :raise: ``NullArgument`` -- ``agency_receiver`` or ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_notification()`` is ``false``

        """
        return # osid.authentication.AgencyNotificationSession

    def get_agency_hierarchy_session(self, proxy):
        """Gets the session traversing agency hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgencyHierarchySession``
        :rtype: ``osid.authentication.AgencyHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_hierarchy()`` is ``false``

        """
        return # osid.authentication.AgencyHierarchySession

    def get_agency_hierarchy_design_session(self, proxy):
        """Gets the session designing agency hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgencyHierarchyDesignSession``
        :rtype: ``osid.authentication.AgencyHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_hierarchy_design()`` is ``false``

        """
        return # osid.authentication.AgencyHierarchyDesignSession

    def get_authentication_batch_proxy_manager(self):
        """Gets an ``AuthenticationBatchProxyManager``.

        :return: an ``AuthenticationBatchProxyManager``.
        :rtype: ``osid.authentication.batch.AuthenticationBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_batch()`` is ``false``

        """
        return # osid.authentication.batch.AuthenticationBatchProxyManager

    authentication_batch_proxy_manager = property(fget=get_authentication_batch_proxy_manager)

    def get_authentication_keys_proxy_manager(self):
        """Gets an ``AuthenticationKeysProxyManager``.

        :return: an ``AuthenticationKeysProxyManager``.
        :rtype: ``osid.authentication.keys.AuthenticationKeysProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_keys()`` is ``false``

        """
        return # osid.authentication.keys.AuthenticationKeysProxyManager

    authentication_keys_proxy_manager = property(fget=get_authentication_keys_proxy_manager)

    def get_authentication_process_proxy_manager(self):
        """Gets an ``AuthenticationProcessProxyManager``.

        :return: an ``AuthenticationProcessproxyManager``.
        :rtype: ``osid.authentication.process.AuthenticationProcessProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_process()`` is ``false``

        """
        return # osid.authentication.process.AuthenticationProcessProxyManager

    authentication_process_proxy_manager = property(fget=get_authentication_process_proxy_manager)


