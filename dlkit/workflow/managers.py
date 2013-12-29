from ..osid import managers as osid_managers


class WorkflowProfile(osid_managers.OsidProfile):
    """The workflow profile describes the interoperability among workflow services."""
    def supports_visible_federation(self):
        """Tests if any office federation is exposed.

        Federation is exposed when a specific office may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of offices appears as a
        single office.

        :return: ``true`` if visible federation is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_process_lookup(self):
        """Tests if looking up process is supported.

        :return: ``true`` if process lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_process_query(self):
        """Tests if querying process is supported.

        :return: ``true`` if process query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_process_search(self):
        """Tests if searching process is supported.

        :return: ``true`` if process search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_process_admin(self):
        """Tests if process administrative service is supported.

        :return: ``true`` if process administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_process_notification(self):
        """Tests if a process notification service is supported.

        :return: ``true`` if process notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_process_office(self):
        """Tests if a process office lookup service is supported.

        :return: ``true`` if a process office lookup service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_process_office_assignment(self):
        """Tests if a process office service is supported.

        :return: ``true`` if process to office assignment service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_process_smart_office(self):
        """Tests if a process smart office lookup service is supported.

        :return: ``true`` if a process smart office service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_step_lookup(self):
        """Tests if looking up steps is supported.

        :return: ``true`` if step lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_step_query(self):
        """Tests if querying steps is supported.

        :return: ``true`` if step query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_step_search(self):
        """Tests if searching steps is supported.

        :return: ``true`` if step search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_step_admin(self):
        """Tests if a step administrative service is supported.

        :return: ``true`` if step administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_step_notification(self):
        """Tests if a stepnotification service is supported.

        :return: ``true`` if step notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_step_office(self):
        """Tests if a step office lookup service is supported.

        :return: ``true`` if a step office lookup service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_step_office_assignment(self):
        """Tests if a step office assignment service is supported.

        :return: ``true`` if a step to office assignment service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_step_smart_office(self):
        """Tests if a step smart office service is supported.

        :return: ``true`` if a step smart office service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_work_lookup(self):
        """Tests if looking up work is supported.

        :return: ``true`` if work lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_work_query(self):
        """Tests if querying work is supported.

        :return: ``true`` if work query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_work_search(self):
        """Tests if searching work is supported.

        :return: ``true`` if work search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_work_admin(self):
        """Tests if work administrative service is supported.

        :return: ``true`` if work administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_work_notification(self):
        """Tests if a work notification service is supported.

        :return: ``true`` if work notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_work_office(self):
        """Tests if a work office lookup service is supported.

        :return: ``true`` if a work office lookup service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_work_office_assignment(self):
        """Tests if a work office service is supported.

        :return: ``true`` if work to office assignment service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_work_smart_office(self):
        """Tests if a work smart office lookup service is supported.

        :return: ``true`` if a work smart office service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_workflow(self):
        """Tests if a workflow service is supported.

        :return: ``true`` if workflow is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_workflow_initiation(self):
        """Tests if a workflow initiation service is supported.

        :return: ``true`` if workflow initiation is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_workflow_management(self):
        """Tests if a workflow management service is supported.

        :return: ``true`` if workflow management is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_manual_workflow(self):
        """Tests if a manual workflow service is supported.

        :return: ``true`` if manual workflow is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_workflow_event_lookup(self):
        """Tests if a workflowevent lookup service is supported.

        :return: ``true`` if workflow event lookup service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_workflow_event_notification(self):
        """Tests if a workflow event notification service is supported.

        :return: ``true`` if a workflow event notification service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_office_lookup(self):
        """Tests if looking up offices is supported.

        :return: ``true`` if office lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_office_query(self):
        """Tests if querying offices is supported.

        :return: ``true`` if a office query service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_office_search(self):
        """Tests if searching offices is supported.

        :return: ``true`` if office search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_office_admin(self):
        """Tests if office administrative service is supported.

        :return: ``true`` if office administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_office_notification(self):
        """Tests if a officenotification service is supported.

        :return: ``true`` if office notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_office_hierarchy(self):
        """Tests for the availability of a office hierarchy traversal service.

        :return: ``true`` if office hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_office_hierarchy_design(self):
        """Tests for the availability of a office hierarchy design service.

        :return: ``true`` if office hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_workflow_batch(self):
        """Tests for the availability of a workflow batch service.

        :return: ``true`` if a workflow batch service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_workflow_rules(self):
        """Tests for the availability of a workflow rules service.

        :return: ``true`` if a workflow rules service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_process_record_types(self):
        """Gets the supported ``Process`` record types.

        :return: a list containing the supported ``Process`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    process_record_types = property(fget=get_process_record_types)

    def supports_process_record_type(self, process_record_type):
        """Tests if the given ``Process`` record type is supported.

        :param process_record_type: a ``Type`` indicating a ``Process`` record type
        :type process_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``process_record_type`` is ``null``

        """
        return # boolean

    def get_process_search_record_types(self):
        """Gets the supported ``Process`` search record types.

        :return: a list containing the supported ``Process`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    process_search_record_types = property(fget=get_process_search_record_types)

    def supports_process_search_record_type(self, process_search_record_type):
        """Tests if the given ``Process`` search record type is supported.

        :param process_search_record_type: a ``Type`` indicating a ``Process`` search record type
        :type process_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``process_search_record_type`` is ``null``

        """
        return # boolean

    def get_step_record_types(self):
        """Gets the supported ``Step`` record types.

        :return: a list containing the supported ``Step`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    step_record_types = property(fget=get_step_record_types)

    def supports_step_record_type(self, step_record_type):
        """Tests if the given ``Step`` record type is supported.

        :param step_record_type: a ``Type`` indicating a ``Step`` record type
        :type step_record_type: ``osid.type.Type``
        :return: ``true`` if the given record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``step_record_type`` is ``null``

        """
        return # boolean

    def get_step_search_record_types(self):
        """Gets the supported ``Step`` search types.

        :return: a list containing the supported ``Step`` search types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    step_search_record_types = property(fget=get_step_search_record_types)

    def supports_step_search_record_type(self, step_search_record_type):
        """Tests if the given ``Step`` search type is supported.

        :param step_search_record_type: a ``Type`` indicating a ``Step`` search type
        :type step_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``effiort_search_record_type`` is ``null``

        """
        return # boolean

    def get_work_record_types(self):
        """Gets the supported ``Work`` record types.

        :return: a list containing the supported ``Work`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    work_record_types = property(fget=get_work_record_types)

    def supports_work_record_type(self, work_record_type):
        """Tests if the given ``Work`` record type is supported.

        :param work_record_type: a ``Type`` indicating a ``Work`` record type
        :type work_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``work_record_type`` is ``null``

        """
        return # boolean

    def get_work_search_record_types(self):
        """Gets the supported ``Work`` search record types.

        :return: a list containing the supported ``Work`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    work_search_record_types = property(fget=get_work_search_record_types)

    def supports_work_search_record_type(self, work_search_record_type):
        """Tests if the given ``Work`` search record type is supported.

        :param work_search_record_type: a ``Type`` indicating a ``Work`` search record type
        :type work_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``work_search_record_type`` is ``null``

        """
        return # boolean

    def get_workflow_event_record_types(self):
        """Gets the supported ``WorkflowEvent`` record types.

        :return: a list containing the supported ``WorkflowEvent`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    workflow_event_record_types = property(fget=get_workflow_event_record_types)

    def supports_workflow_event_record_type(self, workflow_event_record_type):
        """Tests if the given ``WorkflowEvent`` record type is supported.

        :param workflow_event_record_type: a ``Type`` indicating a ``WorkflowEvent`` record type
        :type workflow_event_record_type: ``osid.type.Type``
        :return: ``true`` if the given record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``workflow_event_record_type`` is ``null``

        """
        return # boolean

    def get_office_record_types(self):
        """Gets the supported ``Office`` record types.

        :return: a list containing the supported ``Office`` types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    office_record_types = property(fget=get_office_record_types)

    def supports_office_record_type(self, office_record_type):
        """Tests if the given ``Office`` record type is supported.

        :param office_record_type: a ``Type`` indicating a ``Office`` record type
        :type office_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``office_record_type`` is ``null``

        """
        return # boolean

    def get_office_search_record_types(self):
        """Gets the supported ``Office`` search record types.

        :return: a list containing the supported ``Office`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    office_search_record_types = property(fget=get_office_search_record_types)

    def supports_office_search_record_type(self, office_search_record_type):
        """Tests if the given ``Office`` search record type is supported.

        :param office_search_record_type: a ``Type`` indicating a ``Office`` search record type
        :type office_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``office_search_record_type`` is ``null``

        """
        return # boolean


class WorkflowManager(osid_managers.OsidManager, WorkflowProfile):
    """The workflow manager provides access to rules sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``ProcessLookupSession:`` a session to retrieve processs
      * ``ProcessQuerySession:`` a session to query for processs
      * ``ProcessSearchSession:`` a session to search for processs
      * ``ProcessAdminSession:`` a session to create and delete processs
      * ``ProcessNotificationSession:`` a session to receive
        notifications pertaining to process changes
      * ``ProcessOfficeSession:`` a session to looking mappings of
        process to offices
      * ``ProcessOfficeAssignmentSession:`` a session to manage process
        to office workflows
      * ``ProcessSmartOfficeSession:`` a session to manage dynamic
        offices of processs
    
      * ``StepLookupSession:`` a session to retrieve steps
      * ``StepQuerySession:`` a session to query for steps
      * ``StepSearchSession:`` a session to search for steps
      * ``StepAdminSession:`` a session to create and delete steps
      * ``StepNotificationSession:`` a session to receive notifications
        pertaining to step changes
      * ``StepOfficeSession:`` a session to look up step office mappings
      * ``StepOfficeAssignmentSession:`` a session to manage steps to
        office mappings
      * ``StepSmartOfficeSession:`` a session to manage dynamic offices
        of stepss
    
      * ``WorkLookupSession:`` a session to retrieve work
      * ``WorkQuerySession:`` a session to query for work
      * ``WorkSearchSession:`` a session to search for work
      * ``WorkAdminSession:`` a session to create and delete work
      * ``WorkNotificationSession:`` a session to receive notifications
        pertaining to work changes
      * ``WorkOfficeSession:`` a session to look up work office mappings
      * ``WorkOfficeAssignmentSession:`` a session to manage
        availability to office mappings
      * ``WorkSmartOfficeSession:`` a session to manage dynamic offices
        of work
    
      * ``WorkflowSession:`` a session to examine work in a process
      * ``WorkflowInitiationSession:`` a session to start work through a
        process
      * ``WorkflowManagementSession:`` a session to enable and disable
        work in a process
      * ``ManualWorkflowSession:`` a session to manuall assign work to
        steps in a process
      * ``WorkflowLogSession:`` a session to look up changes in a
        workflow
      * ``WorkflowEventNotificationSession:`` a session to receive
        notifications of workflow changes
    
      * ``OfficeLookupSession:`` a session to retrieve offices
      * ``OfficeQuerySession:`` a session to search for offices
      * ``OfficeSearchSession:`` a session to search for offices
      * ``OfficeAdminSession:`` a session to create and delete offices
      * ``OfficeNotificationSession:`` a session to receive
        notifications pertaining to office changes
      * ``OfficeHierarchySession:`` a session to traverse a hierarchy of
        office
      * ``OfficeHierarchyDesignSession:`` a session to manage a office
        hierarchy


    """
    def get_process_lookup_session(self):
        """Gets the ``OsidSession`` associated with the process lookup service.

        :return: a ``ProcessLookupSession``
        :rtype: ``osid.workflow.ProcessLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_lookup()`` is ``false``

        """
        return # osid.workflow.ProcessLookupSession

    process_lookup_session = property(fget=get_process_lookup_session)

    def get_process_lookup_session_for_office(self, office_id):
        """Gets the ``OsidSession`` associated with the process lookup service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``ProcessLookupSession``
        :rtype: ``osid.workflow.ProcessLookupSession``
        :raise: ``NotFound`` -- no ``Office`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.ProcessLookupSession

    def get_process_query_session(self):
        """Gets the ``OsidSession`` associated with the process query service.

        :return: a ``ProcessQuerySession``
        :rtype: ``osid.workflow.ProcessQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_query()`` is ``false``

        """
        return # osid.workflow.ProcessQuerySession

    process_query_session = property(fget=get_process_query_session)

    def get_process_query_session_for_office(self, office_id):
        """Gets the ``OsidSession`` associated with the process query service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``ProcessQuerySession``
        :rtype: ``osid.workflow.ProcessQuerySession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.ProcessQuerySession

    def get_process_search_session(self):
        """Gets the ``OsidSession`` associated with the process search service.

        :return: a ``ProcessSearchSession``
        :rtype: ``osid.workflow.ProcessSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_search()`` is ``false``

        """
        return # osid.workflow.ProcessSearchSession

    process_search_session = property(fget=get_process_search_session)

    def get_process_search_session_for_office(self, office_id):
        """Gets the ``OsidSession`` associated with the process search service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``ProcessSearchSession``
        :rtype: ``osid.workflow.ProcessSearchSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.ProcessSearchSession

    def get_process_admin_session(self):
        """Gets the ``OsidSession`` associated with the process administration service.

        :return: a ``ProcessAdminSession``
        :rtype: ``osid.workflow.ProcessAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_admin()`` is ``false``

        """
        return # osid.workflow.ProcessAdminSession

    process_admin_session = property(fget=get_process_admin_session)

    def get_process_admin_session_for_office(self, office_id):
        """Gets the ``OsidSession`` associated with the process administration service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``ProcessAdminSession``
        :rtype: ``osid.workflow.ProcessAdminSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.ProcessAdminSession

    def get_process_notification_session(self, process_receiver):
        """Gets the ``OsidSession`` associated with the process notification service.

        :param process_receiver: the notification callback
        :type process_receiver: ``osid.workflow.ProcessReceiver``
        :return: a ``ProcessNotificationSession``
        :rtype: ``osid.workflow.ProcessNotificationSession``
        :raise: ``NullArgument`` -- ``process_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_notification()`` is ``false``

        """
        return # osid.workflow.ProcessNotificationSession

    def get_process_notification_session_for_office(self, process_receiver, office_id):
        """Gets the ``OsidSession`` associated with the process notification service for the given office.

        :param process_receiver: the notification callback
        :type process_receiver: ``osid.workflow.ProcessReceiver``
        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``ProcessNotificationSession``
        :rtype: ``osid.workflow.ProcessNotificationSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``process_receiver`` or ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.ProcessNotificationSession

    def get_process_office_session(self):
        """Gets the ``OsidSession`` to lookup process/office mappings.

        :return: a ``ProcessOfficeSession``
        :rtype: ``osid.workflow.ProcessOfficeSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_office()`` is ``false``

        """
        return # osid.workflow.ProcessOfficeSession

    process_office_session = property(fget=get_process_office_session)

    def get_process_office_assignment_session(self):
        """Gets the ``OsidSession`` associated with assigning process to offices.

        :return: a ``ProcessOfficeAssignmentSession``
        :rtype: ``osid.workflow.ProcessOfficeAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_office_assignment()`` is ``false``

        """
        return # osid.workflow.ProcessOfficeAssignmentSession

    process_office_assignment_session = property(fget=get_process_office_assignment_session)

    def get_process_smart_office_session(self, office_id):
        """Gets the ``OsidSession`` to manage process smart offices.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``ProcessSmartOfficeSession``
        :rtype: ``osid.workflow.ProcessSmartOfficeSession``
        :raise: ``NotFound`` -- no ``Office`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_smart_office()`` is ``false``

        """
        return # osid.workflow.ProcessSmartOfficeSession

    def get_step_lookup_session(self):
        """Gets the ``OsidSession`` associated with the step lookup service.

        :return: a ``StepLookupSession``
        :rtype: ``osid.workflow.StepLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_lookup()`` is ``false``

        """
        return # osid.workflow.StepLookupSession

    step_lookup_session = property(fget=get_step_lookup_session)

    def get_step_lookup_session_for_office(self, office_id):
        """Gets the ``OsidSession`` associated with the step lookup service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``StepLookupSession``
        :rtype: ``osid.workflow.StepLookupSession``
        :raise: ``NotFound`` -- no ``Office`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.StepLookupSession

    def get_step_query_session(self):
        """Gets the ``OsidSession`` associated with the step query service.

        :return: a ``StepQuerySession``
        :rtype: ``osid.workflow.StepQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_query()`` is ``false``

        """
        return # osid.workflow.StepQuerySession

    step_query_session = property(fget=get_step_query_session)

    def get_step_query_session_for_office(self, office_id):
        """Gets the ``OsidSession`` associated with the step query service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``StepQuerySession``
        :rtype: ``osid.workflow.StepQuerySession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.StepQuerySession

    def get_step_search_session(self):
        """Gets the ``OsidSession`` associated with the step search service.

        :return: a ``StepSearchSession``
        :rtype: ``osid.workflow.StepSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_search()`` is ``false``

        """
        return # osid.workflow.StepSearchSession

    step_search_session = property(fget=get_step_search_session)

    def get_step_search_session_for_office(self, office_id):
        """Gets the ``OsidSession`` associated with the step search service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``StepSearchSession``
        :rtype: ``osid.workflow.StepSearchSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.StepSearchSession

    def get_step_admin_session(self):
        """Gets the ``OsidSession`` associated with the step administration service.

        :return: a ``StepAdminSession``
        :rtype: ``osid.workflow.StepAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_admin()`` is ``false``

        """
        return # osid.workflow.StepAdminSession

    step_admin_session = property(fget=get_step_admin_session)

    def get_step_admin_session_for_office(self, office_id):
        """Gets the ``OsidSession`` associated with the step administration service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``StepAdminSession``
        :rtype: ``osid.workflow.StepAdminSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.StepAdminSession

    def get_step_notification_session(self, step_receiver):
        """Gets the ``OsidSession`` associated with the step notification service.

        :param step_receiver: the notification callback
        :type step_receiver: ``osid.workflow.StepReceiver``
        :return: a ``StepNotificationSession``
        :rtype: ``osid.workflow.StepNotificationSession``
        :raise: ``NullArgument`` -- ``step_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_notification()`` is ``false``

        """
        return # osid.workflow.StepNotificationSession

    def get_step_notification_session_for_office(self, step_receiver, office_id):
        """Gets the ``OsidSession`` associated with the step notification service for the given office.

        :param step_receiver: the notification callback
        :type step_receiver: ``osid.workflow.StepReceiver``
        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``StepNotificationSession``
        :rtype: ``osid.workflow.StepNotificationSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``step_receiver`` or ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.StepNotificationSession

    def get_step_office_session(self):
        """Gets the ``OsidSession`` to lookup step/office mappings.

        :return: a ``StepOfficeSession``
        :rtype: ``osid.workflow.StepOfficeSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_office()`` is ``false``

        """
        return # osid.workflow.StepOfficeSession

    step_office_session = property(fget=get_step_office_session)

    def get_step_office_assignment_session(self):
        """Gets the ``OsidSession`` associated with assigning steps to offices.

        :return: a ``StepOfficeAssignmentSession``
        :rtype: ``osid.workflow.StepOfficeAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_office_assignment()`` is ``false``

        """
        return # osid.workflow.StepOfficeAssignmentSession

    step_office_assignment_session = property(fget=get_step_office_assignment_session)

    def get_step_smart_office_session(self, office_id):
        """Gets the ``OsidSession`` to manage step smart offices.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``StepSmartOfficeSession``
        :rtype: ``osid.workflow.StepOfficeSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_smart_office()`` is ``false``

        """
        return # osid.workflow.StepOfficeSession

    def get_work_lookup_session(self):
        """Gets the ``OsidSession`` associated with the work lookup service.

        :return: a ``WorkLookupSession``
        :rtype: ``osid.workflow.WorkLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_lookup()`` is ``false``

        """
        return # osid.workflow.WorkLookupSession

    work_lookup_session = property(fget=get_work_lookup_session)

    def get_work_lookup_session_for_office(self, office_id):
        """Gets the ``OsidSession`` associated with the work lookup service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``WorkLookupSession``
        :rtype: ``osid.workflow.WorkLookupSession``
        :raise: ``NotFound`` -- no ``Office`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkLookupSession

    def get_work_query_session(self):
        """Gets the ``OsidSession`` associated with the work query service.

        :return: a ``WorkQuerySession``
        :rtype: ``osid.workflow.WorkQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_query()`` is ``false``

        """
        return # osid.workflow.WorkQuerySession

    work_query_session = property(fget=get_work_query_session)

    def get_work_query_session_for_office(self, office_id):
        """Gets the ``OsidSession`` associated with the work query service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``WorkQuerySession``
        :rtype: ``osid.workflow.WorkQuerySession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkQuerySession

    def get_work_search_session(self):
        """Gets the ``OsidSession`` associated with the work search service.

        :return: a ``WorkSearchSession``
        :rtype: ``osid.workflow.WorkSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_search()`` is ``false``

        """
        return # osid.workflow.WorkSearchSession

    work_search_session = property(fget=get_work_search_session)

    def get_work_search_session_for_office(self, office_id):
        """Gets the ``OsidSession`` associated with the work search service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``WorkSearchSession``
        :rtype: ``osid.workflow.WorkSearchSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkSearchSession

    def get_work_admin_session(self):
        """Gets the ``OsidSession`` associated with the work administration service.

        :return: a ``WorkAdminSession``
        :rtype: ``osid.workflow.WorkAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_admin()`` is ``false``

        """
        return # osid.workflow.WorkAdminSession

    work_admin_session = property(fget=get_work_admin_session)

    def get_work_admin_session_for_office(self, office_id):
        """Gets the ``OsidSession`` associated with the work administration service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``WorkAdminSession``
        :rtype: ``osid.workflow.WorkAdminSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkAdminSession

    def get_work_notification_session(self, work_receiver):
        """Gets the ``OsidSession`` associated with the work notification service.

        :param work_receiver: the notification callback
        :type work_receiver: ``osid.workflow.WorkReceiver``
        :return: a ``WorkNotificationSession``
        :rtype: ``osid.workflow.WorkNotificationSession``
        :raise: ``NullArgument`` -- ``work_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_notification()`` is ``false``

        """
        return # osid.workflow.WorkNotificationSession

    def get_work_notification_session_for_office(self, work_receiver, office_id):
        """Gets the ``OsidSession`` associated with the work notification service for the given office.

        :param work_receiver: the notification callback
        :type work_receiver: ``osid.workflow.WorkReceiver``
        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``WorkNotificationSession``
        :rtype: ``osid.workflow.WorkNotificationSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``work_receiver`` or ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkNotificationSession

    def get_work_office_session(self):
        """Gets the ``OsidSession`` to lookup work/office mappings.

        :return: a ``WorkOfficeSession``
        :rtype: ``osid.workflow.WorkOfficeSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_office()`` is ``false``

        """
        return # osid.workflow.WorkOfficeSession

    work_office_session = property(fget=get_work_office_session)

    def get_work_office_assignment_session(self):
        """Gets the ``OsidSession`` associated with assigning work to offices.

        :return: a ``WorkOfficeAssignmentSession``
        :rtype: ``osid.workflow.WorkOfficeAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workb_office_assignment()`` is ``false``

        """
        return # osid.workflow.WorkOfficeAssignmentSession

    work_office_assignment_session = property(fget=get_work_office_assignment_session)

    def get_work_smart_office_session(self, office_id):
        """Gets the ``OsidSession`` to manage work smart offices.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``WorkSmartOfficeSession``
        :rtype: ``osid.workflow.WorkSmartOfficeSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_smart_office()`` is ``false``

        """
        return # osid.workflow.WorkSmartOfficeSession

    def get_workflow_session(self):
        """Gets the ``OsidSession`` for a workflow service.

        :return: a ``WorkflowSession``
        :rtype: ``osid.workflow.WorkflowSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow()`` is ``false``

        """
        return # osid.workflow.WorkflowSession

    workflow_session = property(fget=get_workflow_session)

    def get_workflow_session_for_office(self, office_id):
        """Gets the ``OsidSession`` for a workflow service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``WorkflowSession``
        :rtype: ``osid.workflow.WorkflowSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkflowSession

    def get_workflow_initiation_session(self):
        """Gets the ``OsidSession`` for a workflow initiation service.

        :return: a ``WorkflowInitiationSession``
        :rtype: ``osid.workflow.WorkflowInitiationSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_initiation()`` is ``false``

        """
        return # osid.workflow.WorkflowInitiationSession

    workflow_initiation_session = property(fget=get_workflow_initiation_session)

    def get_workflow_initiation_session_for_office(self, office_id):
        """Gets the ``OsidSession`` for a workflow initiation service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``WorkflowInitiationSession``
        :rtype: ``osid.workflow.WorkflowInitiationSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``offiec_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_initiation()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkflowInitiationSession

    def get_workflow_management_session(self):
        """Gets the ``OsidSession`` for a workflow management service.

        :return: a ``WorkflowManagementSession``
        :rtype: ``osid.workflow.WorkflowManagementSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_management()`` is ``false``

        """
        return # osid.workflow.WorkflowManagementSession

    workflow_management_session = property(fget=get_workflow_management_session)

    def get_workflow_management_session_for_office(self, office_id):
        """Gets the ``OsidSession`` for a workflow management service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``WorkflowManagementSession``
        :rtype: ``osid.workflow.WorkflowManagementSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_management() or supports_visible_federation() is false``

        """
        return # osid.workflow.WorkflowManagementSession

    def get_manual_workflow_session(self):
        """Gets the ``OsidSession`` for a manual workflow service.

        :return: a ``ManualWorkflowSession``
        :rtype: ``osid.workflow.ManualWorkflowSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_manual_workflow()`` is ``false``

        """
        return # osid.workflow.ManualWorkflowSession

    manual_workflow_session = property(fget=get_manual_workflow_session)

    def get_manual_workflow_session_for_office(self, office_id):
        """Gets the ``OsidSession`` for a manual workflow service for the given office.

        :param office_id: the ``Id`` of the ``office``
        :type office_id: ``osid.id.Id``
        :return: a ``ManualWorkflowSession``
        :rtype: ``osid.workflow.ManualWorkflowSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_manual_workflow() or supports_visible_federation() is false``

        """
        return # osid.workflow.ManualWorkflowSession

    def get_workflow_event_lookup_session(self):
        """Gets the ``OsidSession`` for a workflow event lookup service.

        :return: a ``WorkflowLogSession``
        :rtype: ``osid.workflow.WorkflowEventLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_event_lookup()`` is ``false``

        """
        return # osid.workflow.WorkflowEventLookupSession

    workflow_event_lookup_session = property(fget=get_workflow_event_lookup_session)

    def get_workflow_event_lookup_session_for_office(self, office_id):
        """Gets the ``OsidSession`` for a workflow event lookup service for the given office.

        :param office_id: the ``Id`` of the ``office``
        :type office_id: ``osid.id.Id``
        :return: a ``WorkflowEventLookupSession``
        :rtype: ``osid.workflow.WorkflowEventLookupSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_event_lookup() or supports_visible_federation() is false``

        """
        return # osid.workflow.WorkflowEventLookupSession

    def get_workflow_event_notification_session(self, workflow_event_receiver):
        """Gets the ``OsidSession`` associated with the workflow event notification service.

        :param workflow_event_receiver: the notification callback
        :type workflow_event_receiver: ``osid.workflow.WorkflowEventReceiver``
        :return: a ``WorkflowEventNotificationSession``
        :rtype: ``osid.workflow.WorkflowEventNotificationSession``
        :raise: ``NullArgument`` -- ``workflow_event_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_event_notification()`` is ``false``

        """
        return # osid.workflow.WorkflowEventNotificationSession

    def get_workflow_event_notification_session_for_office(self, workflow_event_receiver, office_id):
        """Gets the ``OsidSession`` associated with the workflow event notification service for the given office.

        :param workflow_event_receiver: the notification callback
        :type workflow_event_receiver: ``osid.workflow.WorkflowEventReceiver``
        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: a ``WorkflowEventNotificationSession``
        :rtype: ``osid.workflow.WorkflowEventNotificationSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``workflow_event_receiver`` or ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_event_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkflowEventNotificationSession

    def get_office_lookup_session(self):
        """Gets the ``OsidSession`` associated with the office lookup service.

        :return: a ``OfficeLookupSession``
        :rtype: ``osid.workflow.OfficeLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_office_lookup()`` is ``false``

        """
        return # osid.workflow.OfficeLookupSession

    office_lookup_session = property(fget=get_office_lookup_session)

    def get_office_query_session(self):
        """Gets the ``OsidSession`` associated with the office query service.

        :return: a ``OfficeQuerySession``
        :rtype: ``osid.workflow.OfficeQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_office_query()`` is ``false``

        """
        return # osid.workflow.OfficeQuerySession

    office_query_session = property(fget=get_office_query_session)

    def get_office_search_session(self):
        """Gets the ``OsidSession`` associated with the office search service.

        :return: a ``OfficeSearchSession``
        :rtype: ``osid.workflow.OfficeSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_office_search()`` is ``false``

        """
        return # osid.workflow.OfficeSearchSession

    office_search_session = property(fget=get_office_search_session)

    def get_office_admin_session(self):
        """Gets the ``OsidSession`` associated with the office administrative service.

        :return: a ``OfficeAdminSession``
        :rtype: ``osid.workflow.OfficeAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_office_admin()`` is ``false``

        """
        return # osid.workflow.OfficeAdminSession

    office_admin_session = property(fget=get_office_admin_session)

    def get_office_notification_session(self, office_receiver):
        """Gets the ``OsidSession`` associated with the office notification service.

        :param office_receiver: the notification callback
        :type office_receiver: ``osid.workflow.OfficeReceiver``
        :return: a ``OfficeNotificationSession``
        :rtype: ``osid.workflow.OfficeNotificationSession``
        :raise: ``NullArgument`` -- ``office_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_office_notification()`` is ``false``

        """
        return # osid.workflow.OfficeNotificationSession

    def get_office_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the office hierarchy service.

        :return: a ``OfficeHierarchySession`` for offices
        :rtype: ``osid.workflow.OfficeHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_office_hierarchy()`` is ``false``

        """
        return # osid.workflow.OfficeHierarchySession

    office_hierarchy_session = property(fget=get_office_hierarchy_session)

    def get_office_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the office hierarchy design service.

        :return: a ``HierarchyDesignSession`` for offices
        :rtype: ``osid.workflow.OfficeHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_office_hierarchy_design()`` is ``false``

        """
        return # osid.workflow.OfficeHierarchyDesignSession

    office_hierarchy_design_session = property(fget=get_office_hierarchy_design_session)

    def get_workflow_batch_manager(self):
        """Gets a ``WorkflowBatchManager``.

        :return: a ``WorkflowbatchManager``
        :rtype: ``osid.workflow.batch.WorkflowBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_batch()`` is ``false``

        """
        return # osid.workflow.batch.WorkflowBatchManager

    workflow_batch_manager = property(fget=get_workflow_batch_manager)

    def get_workflow_rules_manager(self):
        """Gets a ``WorkflowRulesManager``.

        :return: a ``WorkflowRulesManager``
        :rtype: ``osid.workflow.rules.WorkflowRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_rules()`` is ``false``

        """
        return # osid.workflow.rules.WorkflowRulesManager

    workflow_rules_manager = property(fget=get_workflow_rules_manager)


class WorkflowProxyManager(osid_managers.OsidProxyManager, WorkflowProfile):
    """The workflow proxy manager provides access to rules sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager pass a ``Proxy`` for passing information
    from server environments. The sessions included in this manager are:

      * ``ProcessLookupSession:`` a session to retrieve processs
      * ``ProcessQuerySession:`` a session to query for processs
      * ``ProcessSearchSession:`` a session to search for processs
      * ``ProcessAdminSession:`` a session to create and delete processs
      * ``ProcessNotificationSession:`` a session to receive
        notifications pertaining to process changes
      * ``ProcessOfficeSession:`` a session to looking mappings of
        process to offices
      * ``ProcessOfficeAssignmentSession:`` a session to manage process
        to office workflows
      * ``ProcessSmartOfficeSession:`` a session to manage dynamic
        offices of processs
    
      * ``StepLookupSession:`` a session to retrieve steps
      * ``StepQuerySession:`` a session to query for steps
      * ``StepSearchSession:`` a session to search for steps
      * ``StepAdminSession:`` a session to create and delete steps
      * ``StepNotificationSession:`` a session to receive notifications
        pertaining to step changes
      * ``StepOfficeSession:`` a session to look up step office mappings
      * ``StepOfficeAssignmentSession:`` a session to manage steps to
        office mappings
      * ``StepSmartOfficeSession:`` a session to manage dynamic offices
        of stepss
    
      * ``WorkLookupSession:`` a session to retrieve work
      * ``WorkQuerySession:`` a session to query for work
      * ``WorkSearchSession:`` a session to search for work
      * ``WorkAdminSession:`` a session to create and delete work
      * ``WorkNotificationSession:`` a session to receive notifications
        pertaining to work changes
      * ``WorkOfficeSession:`` a session to look up work office mappings
      * ``WorkOfficeAssignmentSession:`` a session to manage
        availability to office mappings
      * ``WorkSmartOfficeSession:`` a session to manage dynamic offices
        of work
    
      * ``WorkflowSession:`` a session to examine work in a process
      * ``WorkflowInitiationSession:`` a session to start work through a
        process
      * ``WorkflowManagementSession:`` a session to enable and disable
        work in a process
      * ``ManualWorkflowSession:`` a session to manuall assign work to
        steps in a process
      * ``WorkflowLogSession:`` a session to look up changes in a
        workflow
      * ``WorkflowEventNotificationSession:`` a session to receive
        notifications of workflow changes
    
      * ``OfficeLookupSession:`` a session to retrieve offices
      * ``OfficeQuerySession:`` a session to search for offices
      * ``OfficeSearchSession:`` a session to search for offices
      * ``OfficeAdminSession:`` a session to create and delete offices
      * ``OfficeNotificationSession:`` a session to receive
        notifications pertaining to office changes
      * ``OfficeHierarchySession:`` a session to traverse a hierarchy of
        office
      * ``OfficeHierarchyDesignSession:`` a session to manage a office
        hierarchy


    """
    def get_process_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the process lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProcessLookupSession``
        :rtype: ``osid.workflow.ProcessLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_lookup()`` is ``false``

        """
        return # osid.workflow.ProcessLookupSession

    def get_process_lookup_session_for_office(self, office_id, proxy):
        """Gets the ``OsidSession`` associated with the process lookup service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProcessLookupSession``
        :rtype: ``osid.workflow.ProcessLookupSession``
        :raise: ``NotFound`` -- no ``Office`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.ProcessLookupSession

    def get_process_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the process query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProcessQuerySession``
        :rtype: ``osid.workflow.ProcessQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_query()`` is ``false``

        """
        return # osid.workflow.ProcessQuerySession

    def get_process_query_session_for_office(self, office_id, proxy):
        """Gets the ``OsidSession`` associated with the process query service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProcessQuerySession``
        :rtype: ``osid.workflow.ProcessQuerySession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.ProcessQuerySession

    def get_process_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the process search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProcessSearchSession``
        :rtype: ``osid.workflow.ProcessSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_search()`` is ``false``

        """
        return # osid.workflow.ProcessSearchSession

    def get_process_search_session_for_office(self, office_id, proxy):
        """Gets the ``OsidSession`` associated with the process search service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProcessSearchSession``
        :rtype: ``osid.workflow.ProcessSearchSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.ProcessSearchSession

    def get_process_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the process administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProcessAdminSession``
        :rtype: ``osid.workflow.ProcessAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_admin()`` is ``false``

        """
        return # osid.workflow.ProcessAdminSession

    def get_process_admin_session_for_office(self, office_id, proxy):
        """Gets the ``OsidSession`` associated with the process administration service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProcessAdminSession``
        :rtype: ``osid.workflow.ProcessAdminSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.ProcessAdminSession

    def get_process_notification_session(self, process_receiver, proxy):
        """Gets the ``OsidSession`` associated with the process notification service.

        :param process_receiver: the notification callback
        :type process_receiver: ``osid.workflow.ProcessReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProcessNotificationSession``
        :rtype: ``osid.workflow.ProcessNotificationSession``
        :raise: ``NullArgument`` -- ``process_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_notification()`` is ``false``

        """
        return # osid.workflow.ProcessNotificationSession

    def get_process_notification_session_for_office(self, process_receiver, office_id, proxy):
        """Gets the ``OsidSession`` associated with the process notification service for the given office.

        :param process_receiver: the notification callback
        :type process_receiver: ``osid.workflow.ProcessReceiver``
        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProcessNotificationSession``
        :rtype: ``osid.workflow.ProcessNotificationSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``process_receiver, office_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.ProcessNotificationSession

    def get_process_office_session(self, proxy):
        """Gets the ``OsidSession`` to lookup process/office mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProcessOfficeSession``
        :rtype: ``osid.workflow.ProcessOfficeSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_office()`` is ``false``

        """
        return # osid.workflow.ProcessOfficeSession

    def get_process_office_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with assigning process to offices.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProcessOfficeAssignmentSession``
        :rtype: ``osid.workflow.ProcessOfficeAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_office_assignment()`` is ``false``

        """
        return # osid.workflow.ProcessOfficeAssignmentSession

    def get_process_smart_office_session(self, office_id, proxy):
        """Gets the ``OsidSession`` to manage process smart offices.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProcessSmartOfficeSession``
        :rtype: ``osid.workflow.ProcessSmartOfficeSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_process_smart_office()`` is ``false``

        """
        return # osid.workflow.ProcessSmartOfficeSession

    def get_step_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the step lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``StepLookupSession``
        :rtype: ``osid.workflow.StepLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_lookup()`` is ``false``

        """
        return # osid.workflow.StepLookupSession

    def get_step_lookup_session_for_office(self, office_id, proxy):
        """Gets the ``OsidSession`` associated with the step lookup service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``StepLookupSession``
        :rtype: ``osid.workflow.StepLookupSession``
        :raise: ``NotFound`` -- no ``Office`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.StepLookupSession

    def get_step_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the step query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``StepQuerySession``
        :rtype: ``osid.workflow.StepQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_query()`` is ``false``

        """
        return # osid.workflow.StepQuerySession

    def get_step_query_session_for_office(self, office_id, proxy):
        """Gets the ``OsidSession`` associated with the step query service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``StepQuerySession``
        :rtype: ``osid.workflow.StepQuerySession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.StepQuerySession

    def get_step_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the step search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``StepSearchSession``
        :rtype: ``osid.workflow.StepSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_search()`` is ``false``

        """
        return # osid.workflow.StepSearchSession

    def get_step_search_session_for_office(self, office_id, proxy):
        """Gets the ``OsidSession`` associated with the step search service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``StepSearchSession``
        :rtype: ``osid.workflow.StepSearchSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.StepSearchSession

    def get_step_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the step administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``StepAdminSession``
        :rtype: ``osid.workflow.StepAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_admin()`` is ``false``

        """
        return # osid.workflow.StepAdminSession

    def get_step_admin_session_for_office(self, office_id, proxy):
        """Gets the ``OsidSession`` associated with the step administration service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``StepAdminSession``
        :rtype: ``osid.workflow.StepAdminSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.StepAdminSession

    def get_step_notification_session(self, step_receiver, proxy):
        """Gets the ``OsidSession`` associated with the step notification service.

        :param step_receiver: the notification callback
        :type step_receiver: ``osid.workflow.StepReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``StepNotificationSession``
        :rtype: ``osid.workflow.StepNotificationSession``
        :raise: ``NullArgument`` -- ``step_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_notification()`` is ``false``

        """
        return # osid.workflow.StepNotificationSession

    def get_step_notification_session_for_office(self, step_receiver, office_id, proxy):
        """Gets the ``OsidSession`` associated with the step notification service for the given office.

        :param step_receiver: the notification callback
        :type step_receiver: ``osid.workflow.StepReceiver``
        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``StepNotificationSession``
        :rtype: ``osid.workflow.StepNotificationSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``step_receiver, office_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.StepNotificationSession

    def get_step_office_session(self, proxy):
        """Gets the ``OsidSession`` to lookup step/office mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``StepOfficeSession``
        :rtype: ``osid.workflow.StepOfficeSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_office()`` is ``false``

        """
        return # osid.workflow.StepOfficeSession

    def get_step_office_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with assigning steps to offices.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``StepOfficeAssignmentSession``
        :rtype: ``osid.workflow.StepOfficeAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_office_assignment()`` is ``false``

        """
        return # osid.workflow.StepOfficeAssignmentSession

    def get_step_smart_office_session(self, office_id, proxy):
        """Gets the ``OsidSession`` to manage step smart offices.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``StepSmartOfficeSession``
        :rtype: ``osid.workflow.StepOfficeSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_step_smart_office()`` is ``false``

        """
        return # osid.workflow.StepOfficeSession

    def get_work_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the work lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkLookupSession``
        :rtype: ``osid.workflow.WorkLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_lookup()`` is ``false``

        """
        return # osid.workflow.WorkLookupSession

    def get_work_lookup_session_for_office(self, office_id, proxy):
        """Gets the ``OsidSession`` associated with the work lookup service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkLookupSession``
        :rtype: ``osid.workflow.WorkLookupSession``
        :raise: ``NotFound`` -- no ``Office`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkLookupSession

    def get_work_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the work query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkQuerySession``
        :rtype: ``osid.workflow.WorkQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_query()`` is ``false``

        """
        return # osid.workflow.WorkQuerySession

    def get_work_query_session_for_office(self, office_id, proxy):
        """Gets the ``OsidSession`` associated with the work query service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkQuerySession``
        :rtype: ``osid.workflow.WorkQuerySession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkQuerySession

    def get_work_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the work search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkSearchSession``
        :rtype: ``osid.workflow.WorkSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_search()`` is ``false``

        """
        return # osid.workflow.WorkSearchSession

    def get_work_search_session_for_office(self, office_id, proxy):
        """Gets the ``OsidSession`` associated with the work search service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkSearchSession``
        :rtype: ``osid.workflow.WorkSearchSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkSearchSession

    def get_work_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the work administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkAdminSession``
        :rtype: ``osid.workflow.WorkAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_admin()`` is ``false``

        """
        return # osid.workflow.WorkAdminSession

    def get_work_admin_session_for_office(self, office_id, proxy):
        """Gets the ``OsidSession`` associated with the work administration service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkAdminSession``
        :rtype: ``osid.workflow.WorkAdminSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkAdminSession

    def get_work_notification_session(self, work_receiver, proxy):
        """Gets the ``OsidSession`` associated with the work notification service.

        :param work_receiver: the notification callback
        :type work_receiver: ``osid.workflow.WorkReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkNotificationSession``
        :rtype: ``osid.workflow.WorkNotificationSession``
        :raise: ``NullArgument`` -- ``work_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_notification()`` is ``false``

        """
        return # osid.workflow.WorkNotificationSession

    def get_work_notification_session_for_office(self, work_receiver, office_id, proxy):
        """Gets the ``OsidSession`` associated with the work notification service for the given office.

        :param work_receiver: the notification callback
        :type work_receiver: ``osid.workflow.WorkReceiver``
        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkNotificationSession``
        :rtype: ``osid.workflow.WorkNotificationSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``work_receiver, office_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkNotificationSession

    def get_work_office_session(self, proxy):
        """Gets the ``OsidSession`` to lookup work/office mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkOfficeSession``
        :rtype: ``osid.workflow.WorkOfficeSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_office()`` is ``false``

        """
        return # osid.workflow.WorkOfficeSession

    def get_work_office_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with assigning work to offices.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkOfficeAssignmentSession``
        :rtype: ``osid.workflow.WorkOfficeAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workb_office_assignment()`` is ``false``

        """
        return # osid.workflow.WorkOfficeAssignmentSession

    def get_work_smart_office_session(self, office_id, proxy):
        """Gets the ``OsidSession`` to manage work smart offices.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkSmartOfficeSession``
        :rtype: ``osid.workflow.WorkSmartOfficeSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- no ``Office`` found by the given ``Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_work_smart_office()`` is ``false``

        """
        return # osid.workflow.WorkSmartOfficeSession

    def get_workflow_session(self, proxy):
        """Gets the ``OsidSession`` for a workflow service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkflowSession``
        :rtype: ``osid.workflow.WorkflowSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow()`` is ``false``

        """
        return # osid.workflow.WorkflowSession

    def get_workflow_session_for_office(self, office_id, proxy):
        """Gets the ``OsidSession`` for a workflow service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkflowSession``
        :rtype: ``osid.workflow.WorkflowSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkflowSession

    def get_workflow_initiation_session(self, proxy):
        """Gets the ``OsidSession`` for a workflow initiation service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkflowInitiationSession``
        :rtype: ``osid.workflow.WorkflowInitiationSession``
        :raise: ``NullArgument`` -- ``proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_initiation()`` is ``false``

        """
        return # osid.workflow.WorkflowInitiationSession

    def get_workflow_initiation_session_for_office(self, office_id, proxy):
        """Gets the ``OsidSession`` for a workflow initiation service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkflowInitiationSession``
        :rtype: ``osid.workflow.WorkflowInitiationSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_initiation()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkflowInitiationSession

    def get_workflow_management_session(self, proxy):
        """Gets the ``OsidSession`` for a workflow management service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkflowManagementSession``
        :rtype: ``osid.workflow.WorkflowManagementSession``
        :raise: ``NullArgument`` -- ``proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_management()`` is ``false``

        """
        return # osid.workflow.WorkflowManagementSession

    def get_workflow_management_session_for_office(self, office_id, proxy):
        """Gets the ``OsidSession`` for a workflow management service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkflowManagementSession``
        :rtype: ``osid.workflow.WorkflowManagementSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_management()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkflowManagementSession

    def get_manual_workflow_session(self, proxy):
        """Gets the ``OsidSession`` for a manual workflow service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ManualWorkflowSession``
        :rtype: ``osid.workflow.ManualWorkflowSession``
        :raise: ``NullArgument`` -- ``proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_manual_workflow()`` is ``false``

        """
        return # osid.workflow.ManualWorkflowSession

    def get_manual_workflow_session_for_office(self, office_id, proxy):
        """Gets the ``OsidSession`` for a manual workflow service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ManualWorkflowSession``
        :rtype: ``osid.workflow.ManualWorkflowSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_manual_workflow()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.ManualWorkflowSession

    def get_workflow_event_lookup_session(self, proxy):
        """Gets the ``OsidSession`` for a workflow event lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkflowEventLookupSession``
        :rtype: ``osid.workflow.WorkflowEventLookupSession``
        :raise: ``NullArgument`` -- ``proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_event_lookup()`` is ``false``

        """
        return # osid.workflow.WorkflowEventLookupSession

    def get_workflow_event_lookup_session_for_office(self, office_id, proxy):
        """Gets the ``OsidSession`` for a workflow event lookup service for the given office.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkflowEventLookupSession``
        :rtype: ``osid.workflow.WorkflowEventLookupSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``office_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_event_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkflowEventLookupSession

    def get_workflow_event_notification_session(self, workflow_event_receiver, proxy):
        """Gets the ``OsidSession`` associated with the workflow event notification service.

        :param workflow_event_receiver: the notification callback
        :type workflow_event_receiver: ``osid.workflow.WorkflowEventReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkflowEventNotificationSession``
        :rtype: ``osid.workflow.WorkflowEventNotificationSession``
        :raise: ``NullArgument`` -- ``workflow_event_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_event_notification()`` is ``false``

        """
        return # osid.workflow.WorkflowEventNotificationSession

    def get_workflow_event_notification_session_for_office(self, workflow_event_receiver, office_id, proxy):
        """Gets the ``OsidSession`` associated with the workflow event notification service for the given office.

        :param workflow_event_receiver: the notification callback
        :type workflow_event_receiver: ``osid.workflow.WorkflowEventReceiver``
        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``WorkflowEventNotificationSession``
        :rtype: ``osid.workflow.WorkflowEventNotificationSession``
        :raise: ``NotFound`` -- no office found by the given ``Id``
        :raise: ``NullArgument`` -- ``workflow_event_receiver, office_id,`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_event_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.workflow.WorkflowEventNotificationSession

    def get_office_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the office lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``OfficeLookupSession``
        :rtype: ``osid.workflow.OfficeLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_office_lookup()`` is ``false``

        """
        return # osid.workflow.OfficeLookupSession

    def get_office_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the office query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``OfficeQuerySession``
        :rtype: ``osid.workflow.OfficeQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_office_query()`` is ``false``

        """
        return # osid.workflow.OfficeQuerySession

    def get_office_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the office search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``OfficeSearchSession``
        :rtype: ``osid.workflow.OfficeSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_office_search()`` is ``false``

        """
        return # osid.workflow.OfficeSearchSession

    def get_office_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the office administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``OfficeAdminSession``
        :rtype: ``osid.workflow.OfficeAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_office_admin()`` is ``false``

        """
        return # osid.workflow.OfficeAdminSession

    def get_office_notification_session(self, office_receiver, proxy):
        """Gets the ``OsidSession`` associated with the office notification service.

        :param office_receiver: the notification callback
        :type office_receiver: ``osid.workflow.OfficeReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``OfficeNotificationSession``
        :rtype: ``osid.workflow.OfficeNotificationSession``
        :raise: ``NullArgument`` -- ``office_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_office_notification()`` is ``false``

        """
        return # osid.workflow.OfficeNotificationSession

    def get_office_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the office hierarchy service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``OfficeHierarchySession`` for offices
        :rtype: ``osid.workflow.OfficeHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_office_hierarchy()`` is ``false``

        """
        return # osid.workflow.OfficeHierarchySession

    def get_office_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the office hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyDesignSession`` for offices
        :rtype: ``osid.workflow.OfficeHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_office_hierarchy_design()`` is ``false``

        """
        return # osid.workflow.OfficeHierarchyDesignSession

    def get_workflow_batch_proxy_manager(self):
        """Gets a ``WorkflowBatchProxyManager``.

        :return: a ``WorkflowbatchProxyManager``
        :rtype: ``osid.workflow.batch.WorkflowBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_batch()`` is ``false``

        """
        return # osid.workflow.batch.WorkflowBatchProxyManager

    workflow_batch_proxy_manager = property(fget=get_workflow_batch_proxy_manager)

    def get_workflow_rules_proxy_manager(self):
        """Gets a ``WorkflowRulesProxyManager``.

        :return: a ``WorkflowRulesProxyManager`` for offices
        :rtype: ``osid.workflow.rules.WorkflowRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_workflow_rules()`` is ``false``

        """
        return # osid.workflow.rules.WorkflowRulesProxyManager

    workflow_rules_proxy_manager = property(fget=get_workflow_rules_proxy_manager)


