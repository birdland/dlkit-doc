from ..osid import queries as osid_queries


class ProcessQuery(osid_queries.OsidGovernatorQuery):
    """This is the query for searching processes.

    Each method match specifies an ``AND`` term while multiple
    invocations of the same method produce a nested ``OR``.

    """
    def match_enabled(self, match):
        """Matches enabled processes.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def clear_enabled_terms(self):
        """Clears the enabled query terms."""
        pass

    enabled_terms = property(fdel=clear_enabled_terms)

    def match_initial_step_id(self, step_id, match):
        """Sets the initial step ``Id`` for this query.

        :param step_id: the step ``Id``
        :type step_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``step_id`` is ``null``

        """
        pass

    def clear_initial_step_id_terms(self):
        """Clears the initial stap ``Id`` query terms."""
        pass

    initial_step_id_terms = property(fdel=clear_initial_step_id_terms)

    def supports_initial_step_query(self):
        """Tests if a ``StepQuery`` is available.

        :return: ``true`` if a step query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_initial_step_query(self):
        """Gets the query for a step.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the step query
        :rtype: ``osid.workflow.StepQuery``
        :raise: ``Unimplemented`` -- ``supports_initial_step_query()`` is ``false``

        """
        return # osid.workflow.StepQuery

    initial_step_query = property(fget=get_initial_step_query)

    def clear_initial_step_terms(self):
        """Clears the initial step terms."""
        pass

    initial_step_terms = property(fdel=clear_initial_step_terms)

    def match_initial_state_id(self, state_id, match):
        """Sets the initial state ``Id`` for this query.

        :param state_id: the state ``Id``
        :type state_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``state_id`` is ``null``

        """
        pass

    def clear_initial_state_id_terms(self):
        """Clears the initial state ``Id`` query terms."""
        pass

    initial_state_id_terms = property(fdel=clear_initial_state_id_terms)

    def supports_initial_state_query(self):
        """Tests if a ``StateQuery`` is available.

        :return: ``true`` if a state query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_initial_state_query(self):
        """Gets the query for a state.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the state query
        :rtype: ``osid.process.StateQuery``
        :raise: ``Unimplemented`` -- ``supports_initial_state_query()`` is ``false``

        """
        return # osid.process.StateQuery

    initial_state_query = property(fget=get_initial_state_query)

    def clear_initial_state_terms(self):
        """Clears the state terms."""
        pass

    initial_state_terms = property(fdel=clear_initial_state_terms)

    def match_step_id(self, step_id, match):
        """Sets the step ``Id`` for this query.

        :param step_id: the step ``Id``
        :type step_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``step_id`` is ``null``

        """
        pass

    def clear_step_id_terms(self):
        """Clears the step ``Id`` query terms."""
        pass

    step_id_terms = property(fdel=clear_step_id_terms)

    def supports_step_query(self):
        """Tests if a ``StepQuery`` is available.

        :return: ``true`` if a step query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_step_query(self):
        """Gets the query for a step Multiple retrievals produce a nested ``OR`` term.

        :return: the step query
        :rtype: ``osid.workflow.StepQuery``
        :raise: ``Unimplemented`` -- ``supports_stepy_query()`` is ``false``

        """
        return # osid.workflow.StepQuery

    step_query = property(fget=get_step_query)

    def match_any_step(self, match):
        """Matches processes that have any step.

        :param match: ``true`` to match processes with any step, ``false`` to match processes with no step
        :type match: ``boolean``

        """
        pass

    def clear_step_terms(self):
        """Clears the step query terms."""
        pass

    step_terms = property(fdel=clear_step_terms)

    def match_work_id(self, work_id, match):
        """Sets the work ``Id`` for this query.

        :param work_id: the work ``Id``
        :type work_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``work_id`` is ``null``

        """
        pass

    def clear_work_id_terms(self):
        """Clears the work ``Id`` query terms."""
        pass

    work_id_terms = property(fdel=clear_work_id_terms)

    def supports_work_query(self):
        """Tests if a ``WorkQuery`` is available.

        :return: ``true`` if a work query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_work_query(self):
        """Gets the query for a work.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the work query
        :rtype: ``osid.workflow.WorkQuery``
        :raise: ``Unimplemented`` -- ``supports_work_query()`` is ``false``

        """
        return # osid.workflow.WorkQuery

    work_query = property(fget=get_work_query)

    def match_any_work(self, match):
        """Matches processs that have any work.

        :param match: ``true`` to match processes with any work, ``false`` to match processes with no work
        :type match: ``boolean``

        """
        pass

    def clear_work_terms(self):
        """Clears the work query terms."""
        pass

    work_terms = property(fdel=clear_work_terms)

    def match_office_id(self, office_id, match):
        """Sets the office ``Id`` for this query to match process assigned to offices.

        :param office_id: the office ``Id``
        :type office_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``

        """
        pass

    def clear_office_id_terms(self):
        """Clears the office ``Id`` query terms."""
        pass

    office_id_terms = property(fdel=clear_office_id_terms)

    def supports_office_query(self):
        """Tests if a ``OfficeQuery`` is available.

        :return: ``true`` if a office query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_office_query(self):
        """Gets the query for a office.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the office query
        :rtype: ``osid.workflow.OfficeQuery``
        :raise: ``Unimplemented`` -- ``supports_office_query()`` is ``false``

        """
        return # osid.workflow.OfficeQuery

    office_query = property(fget=get_office_query)

    def clear_office_terms(self):
        """Clears the office query terms."""
        pass

    office_terms = property(fdel=clear_office_terms)

    def get_process_query_record(self, process_record_type):
        """Gets the process query record corresponding to the given ``Process`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param process_record_type: a process record type
        :type process_record_type: ``osid.type.Type``
        :return: the process query record
        :rtype: ``osid.workflow.records.ProcessQueryRecord``
        :raise: ``NullArgument`` -- ``process_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(process_record_type)`` is ``false``

        """
        return # osid.workflow.records.ProcessQueryRecord


class StepQuery(osid_queries.OsidGovernatorQuery, osid_queries.OsidSubjugateableQuery):
    """This is the query for searching steps.

    Each method match specifies an ``AND`` term while multiple
    invocations of the same method produce a nested ``OR``.

    """
    def match_process_id(self, process_id, match):
        """Sets the process ``Id`` for this query.

        :param process_id: the process ``Id``
        :type process_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``process_id`` is ``null``

        """
        pass

    def clear_process_id_terms(self):
        """Clears the process ``Id`` query terms."""
        pass

    process_id_terms = property(fdel=clear_process_id_terms)

    def supports_process_query(self):
        """Tests if a ``ProcessQuery`` is available.

        :return: ``true`` if a process query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_process_query(self):
        """Gets the query for a process.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the process query
        :rtype: ``osid.workflow.ProcessQuery``
        :raise: ``Unimplemented`` -- ``supports_process_query()`` is ``false``

        """
        return # osid.workflow.ProcessQuery

    process_query = property(fget=get_process_query)

    def clear_process_terms(self):
        """Clears the process query terms."""
        pass

    process_terms = property(fdel=clear_process_terms)

    def match_resource_id(self, resource_id, match):
        """Sets the resource ``Id`` for this query.

        :param resource_id: the resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        """
        pass

    def clear_resource_id_terms(self):
        """Clears the resource ``Id`` query terms."""
        pass

    resource_id_terms = property(fdel=clear_resource_id_terms)

    def supports_resource_query(self):
        """Tests if a ``ResourceQuery`` is available.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_resource_query(self):
        """Gets the query for a resource.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` is ``false``

        """
        return # osid.resource.ResourceQuery

    resource_query = property(fget=get_resource_query)

    def match_any_resource(self, match):
        """Matches steps that have any resources.

        :param match: ``true`` to match steps with any resources, ``false`` to match steps with no resources
        :type match: ``boolean``

        """
        pass

    def clear_resource_terms(self):
        """Clears the resource query terms."""
        pass

    resource_terms = property(fdel=clear_resource_terms)

    def match_initial(self, match):
        """Matches initial steps.

        :param match: ``true`` to match initial steps, ``false`` otherwise
        :type match: ``boolean``

        """
        pass

    def clear_initial_terms(self):
        """Clears the initial step terms."""
        pass

    initial_terms = property(fdel=clear_initial_terms)

    def match_terminal(self, match):
        """Matches terminal steps.

        :param match: ``true`` to match terminal steps, ``false`` otherwise
        :type match: ``boolean``

        """
        pass

    def clear_terminal_terms(self):
        """Clears the terminal step terms."""
        pass

    terminal_terms = property(fdel=clear_terminal_terms)

    def match_input_state_id(self, state_id, match):
        """Sets the input state ``Id`` for this query.

        :param state_id: the state ``Id``
        :type state_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``state_id`` is ``null``

        """
        pass

    def clear_input_state_id_terms(self):
        """Clears the input state ``Id`` query terms."""
        pass

    input_state_id_terms = property(fdel=clear_input_state_id_terms)

    def supports_input_state_query(self):
        """Tests if a ``StateQuery`` is available.

        :return: ``true`` if a state query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_input_state_query(self):
        """Gets the query for an input state.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the state query
        :rtype: ``osid.process.StateQuery``
        :raise: ``Unimplemented`` -- ``supports_input_state_query()`` is ``false``

        """
        return # osid.process.StateQuery

    input_state_query = property(fget=get_input_state_query)

    def match_any_input_state(self, match):
        """Matches steps that have any input states.

        :param match: ``true`` to match steps with any input states, ``false`` to match steps with no input states
        :type match: ``boolean``

        """
        pass

    def clear_input_state_terms(self):
        """Clears the input state terms."""
        pass

    input_state_terms = property(fdel=clear_input_state_terms)

    def match_next_state_id(self, state_id, match):
        """Sets the next state ``Id`` for this query.

        :param state_id: the state ``Id``
        :type state_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``state_id`` is ``null``

        """
        pass

    def clear_next_state_id_terms(self):
        """Clears the next state ``Id`` query terms."""
        pass

    next_state_id_terms = property(fdel=clear_next_state_id_terms)

    def supports_next_state_query(self):
        """Tests if a ``StateQuery`` is available.

        :return: ``true`` if a state query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_next_state_query(self):
        """Gets the query for a state.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the state query
        :rtype: ``osid.process.StateQuery``
        :raise: ``Unimplemented`` -- ``supports_next_state_query()`` is ``false``

        """
        return # osid.process.StateQuery

    next_state_query = property(fget=get_next_state_query)

    def match_any_next_state(self, match):
        """Matches steps that have any next state,.

        :param match: ``true`` to match steps with any next state, ``false`` to match steps with no next state
        :type match: ``boolean``

        """
        pass

    def clear_next_state_terms(self):
        """Clears the state terms."""
        pass

    next_state_terms = property(fdel=clear_next_state_terms)

    def match_work_id(self, work_id, match):
        """Sets the work ``Id`` for this query.

        :param work_id: the work ``Id``
        :type work_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``work_id`` is ``null``

        """
        pass

    def clear_work_id_terms(self):
        """Clears the work ``Id`` query terms."""
        pass

    work_id_terms = property(fdel=clear_work_id_terms)

    def supports_work_query(self):
        """Tests if a ``WorkQuery`` is available.

        :return: ``true`` if a work query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_work_query(self):
        """Gets the query for a work.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the work query
        :rtype: ``osid.workflow.WorkQuery``
        :raise: ``Unimplemented`` -- ``supports_work_query()`` is ``false``

        """
        return # osid.workflow.WorkQuery

    work_query = property(fget=get_work_query)

    def match_any_work(self, match):
        """Matches steps that have any work.

        :param match: ``true`` to match steps with any work, ``false`` to match steps with no work
        :type match: ``boolean``

        """
        pass

    def clear_work_terms(self):
        """Clears the work query terms."""
        pass

    work_terms = property(fdel=clear_work_terms)

    def match_office_id(self, office_id, match):
        """Sets the office ``Id`` for this query to match steps assigned to offices.

        :param office_id: the office ``Id``
        :type office_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``

        """
        pass

    def clear_office_id_terms(self):
        """Clears the office ``Id`` query terms."""
        pass

    office_id_terms = property(fdel=clear_office_id_terms)

    def supports_office_query(self):
        """Tests if a ``OfficeQuery`` is available.

        :return: ``true`` if a office query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_office_query(self):
        """Gets the query for a office.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the office query
        :rtype: ``osid.workflow.OfficeQuery``
        :raise: ``Unimplemented`` -- ``supports_office_query()`` is ``false``

        """
        return # osid.workflow.OfficeQuery

    office_query = property(fget=get_office_query)

    def clear_office_terms(self):
        """Clears the office query terms."""
        pass

    office_terms = property(fdel=clear_office_terms)

    def get_step_query_record(self, step_record_type):
        """Gets the step query record corresponding to the given ``Step`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param step_record_type: a step record type
        :type step_record_type: ``osid.type.Type``
        :return: the step query record
        :rtype: ``osid.workflow.records.StepQueryRecord``
        :raise: ``NullArgument`` -- ``step_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(step_record_type)`` is ``false``

        """
        return # osid.workflow.records.StepQueryRecord


class WorkQuery(osid_queries.OsidObjectQuery):
    """This is the query for searching works.

    Each method match specifies an ``AND`` term while multiple
    invocations of the same method produce a nested ``OR``.

    """
    def match_suspended(self, match):
        """Matches suspended work.

        :param match: ``true`` to match suspended work, ``false`` otherwise
        :type match: ``boolean``

        """
        pass

    def clear_suspended_terms(self):
        """Clears the suspended query terms."""
        pass

    suspended_terms = property(fdel=clear_suspended_terms)

    def match_process_id(self, process_id, match):
        """Sets the process ``Id`` for this query.

        :param process_id: the process ``Id``
        :type process_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``process_id`` is ``null``

        """
        pass

    def clear_process_id_terms(self):
        """Clears the process ``Id`` query terms."""
        pass

    process_id_terms = property(fdel=clear_process_id_terms)

    def supports_process_query(self):
        """Tests if a ``ProcessQuery`` is available.

        :return: ``true`` if a process query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_process_query(self):
        """Gets the query for a process.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the process query
        :rtype: ``osid.workflow.ProcessQuery``
        :raise: ``Unimplemented`` -- ``supports_process_query()`` is ``false``

        """
        return # osid.workflow.ProcessQuery

    process_query = property(fget=get_process_query)

    def clear_process_terms(self):
        """Clears the process query terms."""
        pass

    process_terms = property(fdel=clear_process_terms)

    def match_step_id(self, step_id, match):
        """Sets the step ``Id`` for this query.

        :param step_id: the step ``Id``
        :type step_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``step_id`` is ``null``

        """
        pass

    def clear_step_id_terms(self):
        """Clears the step ``Id`` query terms."""
        pass

    step_id_terms = property(fdel=clear_step_id_terms)

    def supports_step_query(self):
        """Tests if a ``StepQuery`` is available.

        :return: ``true`` if a step query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_step_query(self):
        """Gets the query for a step Multiple retrievals produce a nested ``OR`` term.

        :return: the step query
        :rtype: ``osid.workflow.StepQuery``
        :raise: ``Unimplemented`` -- ``supports_stepy_query()`` is ``false``

        """
        return # osid.workflow.StepQuery

    step_query = property(fget=get_step_query)

    def match_any_step(self, match):
        """Matches processes that have any step.

        :param match: ``true`` to match processes with any step, ``false`` to match processes with no step
        :type match: ``boolean``

        """
        pass

    def clear_step_terms(self):
        """Clears the step query terms."""
        pass

    step_terms = property(fdel=clear_step_terms)

    def match_office_id(self, office_id, match):
        """Sets the office ``Id`` for this query to match works assigned to offices.

        :param office_id: the office ``Id``
        :type office_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``

        """
        pass

    def clear_office_id_terms(self):
        """Clears the office ``Id`` query terms."""
        pass

    office_id_terms = property(fdel=clear_office_id_terms)

    def supports_office_query(self):
        """Tests if a ``OfficeQuery`` is available.

        :return: ``true`` if a office query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_office_query(self):
        """Gets the query for a office.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the office query
        :rtype: ``osid.workflow.OfficeQuery``
        :raise: ``Unimplemented`` -- ``supports_office_query()`` is ``false``

        """
        return # osid.workflow.OfficeQuery

    office_query = property(fget=get_office_query)

    def clear_office_terms(self):
        """Clears the office query terms."""
        pass

    office_terms = property(fdel=clear_office_terms)

    def get_work_query_record(self, work_record_type):
        """Gets the work query record corresponding to the given ``Work`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param work_record_type: a work record type
        :type work_record_type: ``osid.type.Type``
        :return: the work query record
        :rtype: ``osid.workflow.records.WorkQueryRecord``
        :raise: ``NullArgument`` -- ``work_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(work_record_type)`` is ``false``

        """
        return # osid.workflow.records.WorkQueryRecord


class OfficeQuery(osid_queries.OsidCatalogQuery):
    """This is the query for searching offices.

    Each method match specifies an ``AND`` term while multiple
    invocations of the same method produce a nested ``OR``.

    """
    def match_process_id(self, process_id, match):
        """Sets the step ``Id`` for this query to match offices containing process.

        :param process_id: the process ``Id``
        :type process_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``process_id`` is ``null``

        """
        pass

    def clear_process_id_terms(self):
        """Clears the process query terms."""
        pass

    process_id_terms = property(fdel=clear_process_id_terms)

    def supports_process_query(self):
        """Tests if a ``ProcessQuery`` is available.

        :return: ``true`` if a process query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_process_query(self):
        """Gets the query for a process.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the process query
        :rtype: ``osid.workflow.ProcessQuery``
        :raise: ``Unimplemented`` -- ``supports_process_query()`` is ``false``

        """
        return # osid.workflow.ProcessQuery

    process_query = property(fget=get_process_query)

    def match_any_process(self, match):
        """Matches offices that have any process.

        :param match: ``true`` to match offices with any process, ``false`` to match offices with no process
        :type match: ``boolean``

        """
        pass

    def clear_process_terms(self):
        """Clears the process query terms."""
        pass

    process_terms = property(fdel=clear_process_terms)

    def match_step_id(self, step_id, match):
        """Sets the step ``Id`` for this query.

        :param step_id: the step ``Id``
        :type step_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``step_id`` is ``null``

        """
        pass

    def clear_step_id_terms(self):
        """Clears the step ``Id`` query terms."""
        pass

    step_id_terms = property(fdel=clear_step_id_terms)

    def supports_step_query(self):
        """Tests if an ``StepQuery`` is available.

        :return: ``true`` if an step query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_step_query(self):
        """Gets the query for an step.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the step query
        :rtype: ``osid.workflow.StepQuery``
        :raise: ``Unimplemented`` -- ``supports_step_query()`` is ``false``

        """
        return # osid.workflow.StepQuery

    step_query = property(fget=get_step_query)

    def match_any_step(self, match):
        """Matches offices with any step.

        :param match: ``true`` to match offices with any step, ``false`` to match offices with no step
        :type match: ``boolean``

        """
        pass

    def clear_step_terms(self):
        """Clears the step query terms."""
        pass

    step_terms = property(fdel=clear_step_terms)

    def match_work_id(self, work_id, match):
        """Sets the work ``Id`` for this query.

        :param work_id: the work ``Id``
        :type work_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``work_id`` is ``null``

        """
        pass

    def clear_work_id_terms(self):
        """Clears the work ``Id`` query terms."""
        pass

    work_id_terms = property(fdel=clear_work_id_terms)

    def supports_work_query(self):
        """Tests if a ``WorkQuery`` is available.

        :return: ``true`` if a work query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_work_query(self):
        """Gets the query for a work.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the work query
        :rtype: ``osid.workflow.WorkQuery``
        :raise: ``Unimplemented`` -- ``supports_work_query()`` is ``false``

        """
        return # osid.workflow.WorkQuery

    work_query = property(fget=get_work_query)

    def match_any_work(self, match):
        """Matches offices that have any work.

        :param match: ``true`` to match offices with any work, ``false`` to match offices with no process
        :type match: ``boolean``

        """
        pass

    def clear_work_terms(self):
        """Clears the work query terms."""
        pass

    work_terms = property(fdel=clear_work_terms)

    def match_ancestor_office_id(self, office_id, match):
        """Sets the office ``Id`` for this query to match offices that have the specified office as an ancestor.

        :param office_id: a office ``Id``
        :type office_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``

        """
        pass

    def clear_ancestor_office_id_terms(self):
        """Clears the ancestor office ``Id`` query terms."""
        pass

    ancestor_office_id_terms = property(fdel=clear_ancestor_office_id_terms)

    def supports_ancestor_office_query(self):
        """Tests if a ``OfficeQuery`` is available.

        :return: ``true`` if a office query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_ancestor_office_query(self):
        """Gets the query for a office/ Multiple retrievals produce a nested ``OR`` term.

        :return: the office query
        :rtype: ``osid.workflow.OfficeQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_office_query()`` is ``false``

        """
        return # osid.workflow.OfficeQuery

    ancestor_office_query = property(fget=get_ancestor_office_query)

    def match_any_ancestor_office(self, match):
        """Matches offices with any ancestor.

        :param match: ``true`` to match offices with any ancestor, ``false`` to match root offices
        :type match: ``boolean``

        """
        pass

    def clear_ancestor_office_terms(self):
        """Clears the ancestor office query terms."""
        pass

    ancestor_office_terms = property(fdel=clear_ancestor_office_terms)

    def match_descendant_office_id(self, office_id, match):
        """Sets the office ``Id`` for this query to match offices that have the specified office as a descendant.

        :param office_id: a office ``Id``
        :type office_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``

        """
        pass

    def clear_descendant_office_id_terms(self):
        """Clears the descendant office ``Id`` query terms."""
        pass

    descendant_office_id_terms = property(fdel=clear_descendant_office_id_terms)

    def supports_descendant_office_query(self):
        """Tests if a ``OfficeQuery`` is available.

        :return: ``true`` if a office query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_descendant_office_query(self):
        """Gets the query for a office/ Multiple retrievals produce a nested ``OR`` term.

        :return: the office query
        :rtype: ``osid.workflow.OfficeQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_office_query()`` is ``false``

        """
        return # osid.workflow.OfficeQuery

    descendant_office_query = property(fget=get_descendant_office_query)

    def match_any_descendant_office(self, match):
        """Matches offices with any descendant.

        :param match: ``true`` to match offices with any descendant, ``false`` to match leaf offices
        :type match: ``boolean``

        """
        pass

    def clear_descendant_office_terms(self):
        """Clears the descendant office query terms."""
        pass

    descendant_office_terms = property(fdel=clear_descendant_office_terms)

    def get_office_query_record(self, office_record_type):
        """Gets the office query corresponding to the given ``Office`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param office_record_type: a office record type
        :type office_record_type: ``osid.type.Type``
        :return: the office query record
        :rtype: ``osid.workflow.records.OfficeQueryRecord``
        :raise: ``NullArgument`` -- ``office_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(office_record_type)`` is ``false``

        """
        return # osid.workflow.records.OfficeQueryRecord


