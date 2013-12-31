from ..osid import objects as osid_objects
from ..osid import markers as osid_markers


class Process(osid_objects.OsidGovernator):
    """A ``Process``."""
    def is_enabled(self):
        """Tests if this process is enabled.

        :return: ``true`` if this process is enabled, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_initial_step_id(self):
        """Gets the ``Id`` of the initial step of this process.

        All work goes through an initial step.

        :return: the step ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    initial_step_id = property(fget=get_initial_step_id)

    def get_initial_step(self):
        """Gets the initial step of this process.

        :return: the step
        :rtype: ``osid.workflow.Step``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.workflow.Step

    initial_step = property(fget=get_initial_step)

    def get_initial_state_id(self):
        """Gets the ``Id`` of the initial state of the work upon entering this process.

        The initial state is used to assign the work to an initial step
        that has this state as an initial state.

        :return: the state ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    initial_state_id = property(fget=get_initial_state_id)

    def get_initial_state(self):
        """Gets the initial state of the work upon entering this process.

        The initial state is used to assign the work to an initial step
        that has this state as an initial state.

        :return: the state
        :rtype: ``osid.process.State``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.process.State

    initial_state = property(fget=get_initial_state)

    def get_process_record(self, process_record_type):
        """Gets the process record corresponding to the given ``Process`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``process_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(process_record_type)`` is ``true`` .

        :param process_record_type: the type of process record to retrieve
        :type process_record_type: ``osid.type.Type``
        :return: the process record
        :rtype: ``osid.workflow.records.ProcessRecord``
        :raise: ``NullArgument`` -- ``process_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(process_record_type)`` is ``false``

        """
        return # osid.workflow.records.ProcessRecord


class ProcessForm(osid_objects.OsidGovernatorForm):
    """This is the form for creating and updating ``Processes``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ProcessAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_enabled_metadata(self):
        """Gets the metadata for the enabled flag.

        :return: metadata for the enabled flag
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    enabled_metadata = property(fget=get_enabled_metadata)

    def set_enabled(self, enabled):
        """Sets the enabled flag.

        :param enabled: the new enabled flag
        :type enabled: ``boolean``
        :raise: ``InvalidArgument`` -- ``enabled`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    def clear_enabled(self):
        """Removes the enabled flag.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    enabled = property(fget=set_enabled, fdel=clear_enabled)

    def get_initial_step_metadata(self):
        """Gets the metadata for the initial step.

        :return: metadata for the initial step
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    initial_step_metadata = property(fget=get_initial_step_metadata)

    def set_initial_step(self, step_id):
        """Sets the initial step.

        :param step_id: the new initial step
        :type step_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``step_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``step_id`` is ``null``

        """
        pass

    def clear_initial_step(self):
        """Removes the initial step.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    initial_step = property(fget=set_initial_step, fdel=clear_initial_step)

    def get_initial_state_metadata(self):
        """Gets the metadata for the initial state.

        :return: metadata for the initial state
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    initial_state_metadata = property(fget=get_initial_state_metadata)

    def set_initial_state(self, state_id):
        """Sets the initial state.

        :param state_id: the new initial state
        :type state_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``state_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``state_id`` is ``null``

        """
        pass

    def clear_initial_state(self):
        """Removes the initial state.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    initial_state = property(fget=set_initial_state, fdel=clear_initial_state)

    def get_process_form_record(self, process_record_type):
        """Gets the ``ProcessFormRecord`` corresponding to the given process record ``Type``.

        :param process_record_type: a process record type
        :type process_record_type: ``osid.type.Type``
        :return: the process form record
        :rtype: ``osid.workflow.records.ProcessFormRecord``
        :raise: ``NullArgument`` -- ``process_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(process_record_type)`` is ``false``

        """
        return # osid.workflow.records.ProcessFormRecord


class ProcessList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ProcessList`` provides a means for accessing ``Process`` elements sequentially either one at a time or many at a time.

    Examples: while (pl.hasNext()) { Process process =
    pl.getNextProcess(); }

    or
      while (pl.hasNext()) {
           Process[] processes = pl.getNextProcesses(pl.available());
      }
    


    """
    def get_next_process(self):
        """Gets the next ``Process`` in this list.

        :return: the next ``Process`` in this list. The ``has_next()`` method should be used to test that a next ``Process`` is available before calling this method.
        :rtype: ``osid.workflow.Process``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.workflow.Process

    next_process = property(fget=get_next_process)

    def get_next_processes(self, n):
        """Gets the next set of ``Process`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Process`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Process`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.workflow.Process``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.workflow.Process


class Step(osid_objects.OsidGovernator, osid_markers.Subjugateable):
    """A ``Step`` is an element in a Process in which Work is processed.

    The workers in this ``Step`` are represented by ``Resources`` or
    ``Resource`` groups. The input ``States`` list the states of
    ``Work`` that are valid to be accepted into this ``Step``.
    Successful processing of the ``Work`` result in a single next
    ``State`` that determines the valid next ``Steps`` in the
    ``Process``.

    """
    def get_process_id(self):
        """Gets the ``Id`` of the process.

        :return: the process ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    process_id = property(fget=get_process_id)

    def get_process(self):
        """Gets the process.

        :return: the process
        :rtype: ``osid.workflow.Process``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.workflow.Process

    process = property(fget=get_process)

    def get_resource_ids(self):
        """Gets the ``Ids`` of the resources working in this step.

        :return: the resource ``Ids``
        :rtype: ``osid.id.IdList``

        """
        return # osid.id.IdList

    resource_ids = property(fget=get_resource_ids)

    def get_resources(self):
        """Gets the resources working in this step.

        :return: the resources
        :rtype: ``osid.resource.ResourceList``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.resource.ResourceList

    resources = property(fget=get_resources)

    def get_input_state_ids(self):
        """Gets the ``Ids`` of the valid states entering this step.

        :return: the state ``Ids``
        :rtype: ``osid.id.IdList``

        """
        return # osid.id.IdList

    input_state_ids = property(fget=get_input_state_ids)

    def get_input_states(self):
        """Gets the valid states to enter this step.

        :return: the states
        :rtype: ``osid.process.StateList``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.process.StateList

    input_states = property(fget=get_input_states)

    def get_next_state_id(self):
        """Gets the ``Id`` of the state of the work upon completing this step.

        :return: the state ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    next_state_id = property(fget=get_next_state_id)

    def get_next_state(self):
        """Gets the state of the work upon completing this step.

        :return: the state
        :rtype: ``osid.process.State``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.process.State

    next_state = property(fget=get_next_state)

    def get_step_record(self, step_record_type):
        """Gets the step record corresponding to the given ``Step`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``step_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(step_record_type)``
        is ``true`` .

        :param step_record_type: the type of step record to retrieve
        :type step_record_type: ``osid.type.Type``
        :return: the step record
        :rtype: ``osid.workflow.records.StepRecord``
        :raise: ``NullArgument`` -- ``step_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(step_record_type)`` is ``false``

        """
        return # osid.workflow.records.StepRecord


class StepForm(osid_objects.OsidGovernatorForm, osid_objects.OsidSubjugateableForm):
    """This is the form for creating and updating ``Steps``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``StepAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_input_states_metadata(self):
        """Gets the metadata for the input states.

        :return: metadata for the states
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    input_states_metadata = property(fget=get_input_states_metadata)

    def se_input_states(self, state_ids):
        """Sets the input states.

        :param state_ids: the new input states
        :type state_ids: ``osid.id.IdList``
        :raise: ``InvalidArgument`` -- ``state_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``state_id`` is ``null``

        """
        pass

    def clear_input_states(self):
        """Removes the input states.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    input_states = property(fdel=clear_input_states)

    def get_next_state_metadata(self):
        """Gets the metadata for the next state.

        :return: metadata for the state
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    next_state_metadata = property(fget=get_next_state_metadata)

    def set_next_state(self, state_id):
        """Sets the next state.

        :param state_id: the new next state
        :type state_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``state_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``state_id`` is ``null``

        """
        pass

    def clear_next_state(self):
        """Removes the next state.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    next_state = property(fget=set_next_state, fdel=clear_next_state)

    def get_step_form_record(self, step_record_type):
        """Gets the ``StepFormRecord`` corresponding to the given step record ``Type``.

        :param step_record_type: a step record type
        :type step_record_type: ``osid.type.Type``
        :return: the step form record
        :rtype: ``osid.workflow.records.StepFormRecord``
        :raise: ``NullArgument`` -- ``step_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(step_record_type)`` is ``false``

        """
        return # osid.workflow.records.StepFormRecord


class StepList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``StepList`` provides a means for accessing ``Step`` elements sequentially either one at a time or many at a time.

    Examples: while (sl.hasNext()) { Step step = sl.getNextStep(); }

    or
      while (sl.hasNext()) {
           Step[] steps = sl.getNextSteps(sl.available());
      }
    


    """
    def get_next_step(self):
        """Gets the next ``Step`` in this list.

        :return: the next ``Step`` in this list. The ``has_next()`` method should be used to test that a next ``Step`` is available before calling this method.
        :rtype: ``osid.workflow.Step``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.workflow.Step

    next_step = property(fget=get_next_step)

    def get_next_steps(self, n):
        """Gets the next set of ``Step`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Step`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Step`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.workflow.Step``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.workflow.Step


class Work(osid_objects.OsidObject):
    """``Work`` moves through ``Steps`` in a workflow."""
    def get_work_record(self, work_record_type):
        """Gets the work record corresponding to the given ``Work`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``work_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(work_record_type)``
        is ``true`` .

        :param work_record_type: the type of work record to retrieve
        :type work_record_type: ``osid.type.Type``
        :return: the work record
        :rtype: ``osid.workflow.records.WorkRecord``
        :raise: ``NullArgument`` -- ``work_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(work_record_type)`` is ``false``

        """
        return # osid.workflow.records.WorkRecord


class WorkForm(osid_objects.OsidObjectForm):
    """This is the form for creating and updating ``Works``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``WorkAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_work_form_record(self, work_record_type):
        """Gets the ``WorkFormRecord`` corresponding to the given work record ``Type``.

        :param work_record_type: a work record type
        :type work_record_type: ``osid.type.Type``
        :return: the work form record
        :rtype: ``osid.workflow.records.WorkFormRecord``
        :raise: ``NullArgument`` -- ``work_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(work_record_type)`` is ``false``

        """
        return # osid.workflow.records.WorkFormRecord


class WorkList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``WorkList`` provides a means for accessing ``Work`` elements sequentially either one at a time or many at a time.

    Examples: while (wl.hasNext()) { Work work = wl.getNextWork(); }

    or
      while (wl.hasNext()) {
           Work[] works = wl.getNextWorks(wl.available());
      }
    


    """
    def get_next_work(self):
        """Gets the next ``Work`` in this list.

        :return: the next ``Work`` in this list. The ``has_next()`` method should be used to test that a next ``Work`` is available before calling this method.
        :rtype: ``osid.workflow.Work``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.workflow.Work

    next_work = property(fget=get_next_work)

    def get_next_works(self, n):
        """Gets the next set of ``Work`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Work`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Work`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.workflow.Work``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.workflow.Work


class WorkflowEvent(osid_objects.OsidObject):
    """A ``WorkflowEvent`` is a change in a workflow."""
    def get_timestamp(self):
        """Gets the timestamp of this event.

        :return: the timestamp
        :rtype: ``osid.calendaring.DateTime``

        """
        return # osid.calendaring.DateTime

    timestamp = property(fget=get_timestamp)

    def get_process_id(self):
        """Gets the ``Id`` of the process.

        :return: the process ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    process_id = property(fget=get_process_id)

    def get_process(self):
        """Gets the process.

        :return: the process
        :rtype: ``osid.workflow.Process``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.workflow.Process

    process = property(fget=get_process)

    def get_worker_id(self):
        """Gets the ``Id`` of the resource that caused this event.

        :return: the resource ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    worker_id = property(fget=get_worker_id)

    def get_worker(self):
        """Gets the resource that caused this event.

        :return: the resource
        :rtype: ``osid.resource.Resource``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.resource.Resource

    worker = property(fget=get_worker)

    def get_working_agent_id(self):
        """Gets the ``Id`` of the agent that caused this event.

        :return: the agent ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    working_agent_id = property(fget=get_working_agent_id)

    def get_working_agent(self):
        """Gets the agent that caused this event.

        :return: the agent
        :rtype: ``osid.authentication.Agent``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.authentication.Agent

    working_agent = property(fget=get_working_agent)

    def get_work_id(self):
        """Gets the ``Id`` of the work.

        :return: the work ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    work_id = property(fget=get_work_id)

    def get_work(self):
        """Gets the work.

        :return: the work
        :rtype: ``osid.workflow.Work``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.workflow.Work

    work = property(fget=get_work)

    def did_cancel(self):
        """Tests if this work event indicates the work has been canceled the workflow and is not associated with a step at the time of this event.

        :return: ``true`` if the work canceled, ``false`` if the work is associated with a step in this event
        :rtype: ``boolean``

        """
        return # boolean

    def get_step_id(self):
        """Gets the ``Id`` of the step at which the work is in at the time of this event.

        :return: the step ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``did_complete()`` or ``did_cancel()`` is ``true``

        """
        return # osid.id.Id

    step_id = property(fget=get_step_id)

    def get_step(self):
        """Gets the step at which the work is in at the time of this event.

        :return: the step
        :rtype: ``osid.workflow.Step``
        :raise: ``IllegalState`` -- ``did_complete()`` or ``did_cancel()`` is ``true``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.workflow.Step

    step = property(fget=get_step)

    def get_workflow_event_record(self, work_flow_record_type):
        """Gets the workflow event record corresponding to the given ``WorkflowEvent`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``workflow_event_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(workflow_event_record_type)`` is ``true`` .

        :param work_flow_record_type: the type of workflow event record to retrieve
        :type work_flow_record_type: ``osid.type.Type``
        :return: the workflow event record
        :rtype: ``osid.workflow.records.WorkflowEventRecord``
        :raise: ``NullArgument`` -- ``work_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(workflow_event_record_type)`` is ``false``

        """
        return # osid.workflow.records.WorkflowEventRecord


class WorkflowEventList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``WorkflowEventList`` provides a means for accessing ``WorkflowEvent`` elements sequentially either one at a time or many at a time.

    Examples: while (wel.hasNext()) { WorkflowEvent event =
    wel.getNextWorkflowEvent(); }

    or
      while (wel.hasNext()) {
           WorkflowEvent[] events = wel.getNextWorkflowEvents(wel.available());
      }
    


    """
    def get_next_workflow_event(self):
        """Gets the next ``WorkflowEvent`` in this list.

        :return: the next ``WorkflowEvent`` in this list. The ``has_next()`` method should be used to test that a next ``WorkflowEvent`` is available before calling this method.
        :rtype: ``osid.workflow.WorkflowEvent``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.workflow.WorkflowEvent

    next_workflow_event = property(fget=get_next_workflow_event)

    def get_next_workflow_events(self, n):
        """Gets the next set of ``WorkflowEvent`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``WorkflowEvent`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``WorkflowEvent`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.workflow.WorkflowEvent``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.workflow.WorkflowEvent


class Office(osid_objects.OsidCatalog):
    """A ``Office`` represents a collection of process."""
    def get_office_record(self, office_record_type):
        """Gets the office record corresponding to the given ``Office`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``office_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(office_record_type)``
        is ``true`` .

        :param office_record_type: the type of office record to retrieve
        :type office_record_type: ``osid.type.Type``
        :return: the office record
        :rtype: ``osid.workflow.records.OfficeRecord``
        :raise: ``NullArgument`` -- ``office_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(office_record_type)`` is ``false``

        """
        return # osid.workflow.records.OfficeRecord


class OfficeForm(osid_objects.OsidCatalogForm):
    """This is the form for creating and updating offices.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``OfficeAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_office_form_record(self, office_record_type):
        """Gets the ``OfficeFormRecord`` corresponding to the given office record ``Type``.

        :param office_record_type: a office record type
        :type office_record_type: ``osid.type.Type``
        :return: the office form record
        :rtype: ``osid.workflow.records.OfficeFormRecord``
        :raise: ``NullArgument`` -- ``office_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(office_record_type)`` is ``false``

        """
        return # osid.workflow.records.OfficeFormRecord


class OfficeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``OfficeList`` provides a means for accessing ``Office`` elements sequentially either one at a time or many at a time.

    Examples: while (ol.hasNext()) { Office office = ol.getNextOffice();
    }

    or
      while (ol.hasNext()) {
           Office[] offices = ol.getNextOffices(ol.available());
      }
    


    """
    def get_next_office(self):
        """Gets the next ``Office`` in this list.

        :return: the next ``Office`` in this list. The ``has_next()`` method should be used to test that a next ``Office`` is available before calling this method.
        :rtype: ``osid.workflow.Office``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.workflow.Office

    next_office = property(fget=get_next_office)

    def get_next_offices(self, n):
        """Gets the next set of ``Office`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Office`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Office`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.workflow.Office``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.workflow.Office


class OfficeNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``OfficeHierarchySession``.

    """
    def get_office(self):
        """Gets the ``Office`` at this node.

        :return: the office represented by this node
        :rtype: ``osid.workflow.Office``

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def get_parent_office_nodes(self):
        """Gets the parents of this office.

        :return: the parents of this office
        :rtype: ``osid.workflow.OfficeNodeList``

        """
        return # osid.workflow.OfficeNodeList

    parent_office_nodes = property(fget=get_parent_office_nodes)

    def get_child_office_nodes(self):
        """Gets the children of this office.

        :return: the children of this office
        :rtype: ``osid.workflow.OfficeNodeList``

        """
        return # osid.workflow.OfficeNodeList

    child_office_nodes = property(fget=get_child_office_nodes)


class OfficeNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``OfficeNodeList`` provides a means for accessing ``OfficeNode`` elements sequentially either one at a time or many at a time.

    Examples: while (onl.hasNext()) { OfficeNode node =
    onl.getNextOfficeNode(); }

    or
      while (onl.hasNext()) {
           OfficeNode[] nodes = onl.getNextOfficeNodes(onl.available());
      }
    


    """
    def get_next_office_node(self):
        """Gets the next ``OfficeNode`` in this list.

        :return: the next ``OfficeNode`` in this list. The ``has_next()`` method should be used to test that a next ``OfficeNode`` is available before calling this method.
        :rtype: ``osid.workflow.OfficeNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.workflow.OfficeNode

    next_office_node = property(fget=get_next_office_node)

    def get_next_office_nodes(self, n):
        """Gets the next set of ``OfficeNode`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``OfficeNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``OfficeNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.workflow.OfficeNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.workflow.OfficeNode


