from ..osid import query_inspectors as osid_query_inspectors


class ProcessQueryInspector(osid_query_inspectors.OsidGovernatorQueryInspector):
    """This is the query inspector for examining process queries."""
    def get_enabled_terms(self):
        """Gets the enabled query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``

        """
        return # osid.search.terms.BooleanTerm

    enabled_terms = property(fget=get_enabled_terms)

    def get_initial_step_id_terms(self):
        """Gets the initial step ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    initial_step_id_terms = property(fget=get_initial_step_id_terms)

    def get_initial_step_terms(self):
        """Gets the initial step query terms.

        :return: the query terms
        :rtype: ``osid.workflow.StepQueryInspector``

        """
        return # osid.workflow.StepQueryInspector

    initial_step_terms = property(fget=get_initial_step_terms)

    def get_initial_state_id_terms(self):
        """Gets the initial state ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    initial_state_id_terms = property(fget=get_initial_state_id_terms)

    def get_initial_state_terms(self):
        """Gets the initial state query terms.

        :return: the query terms
        :rtype: ``osid.process.StateQueryInspector``

        """
        return # osid.process.StateQueryInspector

    initial_state_terms = property(fget=get_initial_state_terms)

    def get_step_id_terms(self):
        """Gets the step ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    step_id_terms = property(fget=get_step_id_terms)

    def get_step_terms(self):
        """Gets the step query terms.

        :return: the query terms
        :rtype: ``osid.workflow.StepQueryInspector``

        """
        return # osid.workflow.StepQueryInspector

    step_terms = property(fget=get_step_terms)

    def get_work_id_terms(self):
        """Gets the work ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    work_id_terms = property(fget=get_work_id_terms)

    def get_work_terms(self):
        """Gets the work query terms.

        :return: the query terms
        :rtype: ``osid.workflow.WorkQueryInspector``

        """
        return # osid.workflow.WorkQueryInspector

    work_terms = property(fget=get_work_terms)

    def get_office_id_terms(self):
        """Gets the office ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    office_id_terms = property(fget=get_office_id_terms)

    def get_office_terms(self):
        """Gets the office query terms.

        :return: the query terms
        :rtype: ``osid.workflow.OfficeQueryInspector``

        """
        return # osid.workflow.OfficeQueryInspector

    office_terms = property(fget=get_office_terms)

    def get_process_query_inspector_record(self, process_record_type):
        """Gets the process query inspector record corresponding to the given ``Process`` record ``Type``.

        :param process_record_type: a process record type
        :type process_record_type: ``osid.type.Type``
        :return: the process query inspector record
        :rtype: ``osid.workflow.records.ProcessQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``process_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(process_record_type)`` is ``false``

        """
        return # osid.workflow.records.ProcessQueryInspectorRecord


class StepQueryInspector(osid_query_inspectors.OsidGovernatorQueryInspector, osid_query_inspectors.OsidSubjugateableQueryInspector):
    """This is the query inspector for examining step queries."""
    def get_process_id_terms(self):
        """Gets the process ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    process_id_terms = property(fget=get_process_id_terms)

    def get_process_terms(self):
        """Gets the process query terms.

        :return: the query terms
        :rtype: ``osid.workflow.ProcessQueryInspector``

        """
        return # osid.workflow.ProcessQueryInspector

    process_terms = property(fget=get_process_terms)

    def get_resource_id_terms(self):
        """Gets the resource ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    resource_id_terms = property(fget=get_resource_id_terms)

    def get_resource_terms(self):
        """Gets the resource query terms.

        :return: the query terms
        :rtype: ``osid.resource.ResourceQueryInspector``

        """
        return # osid.resource.ResourceQueryInspector

    resource_terms = property(fget=get_resource_terms)

    def get_work_id_terms(self):
        """Gets the work ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    work_id_terms = property(fget=get_work_id_terms)

    def get_work_terms(self):
        """Gets the work query terms.

        :return: the query terms
        :rtype: ``osid.workflow.WorkQueryInspector``

        """
        return # osid.workflow.WorkQueryInspector

    work_terms = property(fget=get_work_terms)

    def get_initial_terms(self):
        """Gets the initial step query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``

        """
        return # osid.search.terms.BooleanTerm

    initial_terms = property(fget=get_initial_terms)

    def get_terminal_terms(self):
        """Gets the terminal step query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``

        """
        return # osid.search.terms.BooleanTerm

    terminal_terms = property(fget=get_terminal_terms)

    def get_input_state_id_terms(self):
        """Gets the input state ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    input_state_id_terms = property(fget=get_input_state_id_terms)

    def get_input_state_terms(self):
        """Gets the input state query terms.

        :return: the query terms
        :rtype: ``osid.process.StateQueryInspector``

        """
        return # osid.process.StateQueryInspector

    input_state_terms = property(fget=get_input_state_terms)

    def get_next_state_id_terms(self):
        """Gets the next state ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    next_state_id_terms = property(fget=get_next_state_id_terms)

    def get_next_state_terms(self):
        """Gets the next state query terms.

        :return: the query terms
        :rtype: ``osid.process.StateQueryInspector``

        """
        return # osid.process.StateQueryInspector

    next_state_terms = property(fget=get_next_state_terms)

    def get_office_id_terms(self):
        """Gets the office ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    office_id_terms = property(fget=get_office_id_terms)

    def get_office_terms(self):
        """Gets the office query terms.

        :return: the query terms
        :rtype: ``osid.workflow.OfficeQueryInspector``

        """
        return # osid.workflow.OfficeQueryInspector

    office_terms = property(fget=get_office_terms)

    def get_step_query_inspector_record(self, step_record_type):
        """Gets the step query inspector record corresponding to the given ``Step`` record ``Type``.

        :param step_record_type: a step record type
        :type step_record_type: ``osid.type.Type``
        :return: the step query inspector record
        :rtype: ``osid.workflow.records.StepQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``step_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(step_record_type)`` is ``false``

        """
        return # osid.workflow.records.StepQueryInspectorRecord


class WorkQueryInspector(osid_query_inspectors.OsidObjectQueryInspector):
    """This is the query inspector for examining work queries."""
    def get_suspended_terms(self):
        """Gets the suspended query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``

        """
        return # osid.search.terms.BooleanTerm

    suspended_terms = property(fget=get_suspended_terms)

    def get_process_id_terms(self):
        """Gets the process ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    process_id_terms = property(fget=get_process_id_terms)

    def get_process_terms(self):
        """Gets the process query terms.

        :return: the query terms
        :rtype: ``osid.workflow.ProcessQueryInspector``

        """
        return # osid.workflow.ProcessQueryInspector

    process_terms = property(fget=get_process_terms)

    def get_step_id_terms(self):
        """Gets the step ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    step_id_terms = property(fget=get_step_id_terms)

    def get_step_terms(self):
        """Gets the step query terms.

        :return: the query terms
        :rtype: ``osid.workflow.StepQueryInspector``

        """
        return # osid.workflow.StepQueryInspector

    step_terms = property(fget=get_step_terms)

    def get_office_id_terms(self):
        """Gets the office ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    office_id_terms = property(fget=get_office_id_terms)

    def get_office_terms(self):
        """Gets the office query terms.

        :return: the query terms
        :rtype: ``osid.workflow.OfficeQueryInspector``

        """
        return # osid.workflow.OfficeQueryInspector

    office_terms = property(fget=get_office_terms)

    def get_work_query_inspector_record(self, work_record_type):
        """Gets the work query inspector record corresponding to the given ``Work`` record ``Type``.

        :param work_record_type: a work record type
        :type work_record_type: ``osid.type.Type``
        :return: the work query inspector record
        :rtype: ``osid.workflow.records.WorkQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``work_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(work_record_type)`` is ``false``

        """
        return # osid.workflow.records.WorkQueryInspectorRecord


class OfficeQueryInspector(osid_query_inspectors.OsidCatalogQueryInspector):
    """This is the query inspector for examining office queries."""
    def get_process_id_terms(self):
        """Gets the process ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    process_id_terms = property(fget=get_process_id_terms)

    def get_process_terms(self):
        """Gets the process query terms.

        :return: the query terms
        :rtype: ``osid.workflow.ProcessQueryInspector``

        """
        return # osid.workflow.ProcessQueryInspector

    process_terms = property(fget=get_process_terms)

    def get_step_id_terms(self):
        """Gets the step ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    step_id_terms = property(fget=get_step_id_terms)

    def get_step_terms(self):
        """Gets the step query terms.

        :return: the query terms
        :rtype: ``osid.workflow.StepQueryInspector``

        """
        return # osid.workflow.StepQueryInspector

    step_terms = property(fget=get_step_terms)

    def get_work_id_terms(self):
        """Gets the work ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    work_id_terms = property(fget=get_work_id_terms)

    def get_work_terms(self):
        """Gets the work query terms.

        :return: the query terms
        :rtype: ``osid.workflow.WorkQueryInspector``

        """
        return # osid.workflow.WorkQueryInspector

    work_terms = property(fget=get_work_terms)

    def get_ancestor_office_id_terms(self):
        """Gets the ancestor office ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    ancestor_office_id_terms = property(fget=get_ancestor_office_id_terms)

    def get_ancestor_office_terms(self):
        """Gets the ancestor office query terms.

        :return: the query terms
        :rtype: ``osid.workflow.OfficeQueryInspector``

        """
        return # osid.workflow.OfficeQueryInspector

    ancestor_office_terms = property(fget=get_ancestor_office_terms)

    def get_descendant_office_id_terms(self):
        """Gets the descendant office ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    descendant_office_id_terms = property(fget=get_descendant_office_id_terms)

    def get_descendant_office_terms(self):
        """Gets the descendant office query terms.

        :return: the query terms
        :rtype: ``osid.workflow.OfficeQueryInspector``

        """
        return # osid.workflow.OfficeQueryInspector

    descendant_office_terms = property(fget=get_descendant_office_terms)

    def get_office_query_inspector_record(self, office_record_type):
        """Gets the office query inspector record corresponding to the given ``Office`` record ``Type``.

        :param office_record_type: a office record type
        :type office_record_type: ``osid.type.Type``
        :return: the office query inspector record
        :rtype: ``osid.workflow.records.OfficeQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``office_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(office_record_type)`` is ``false``

        """
        return # osid.workflow.records.OfficeQueryInspectorRecord


