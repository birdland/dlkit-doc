from ..osid import search_orders as osid_search_orders


class ProcessSearchOrder(osid_search_orders.OsidGovernatorSearchOrder):
    """An interface for specifying the ordering of search results."""
    def order_by_enabled(self, style):
        """Orders the results by enabled.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_initial_step(self, style):
        """Orders the results by initial step.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_initial_step_search_order(self):
        """Tests if an initial step search order is available.

        :return: ``true`` if a step search order is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_initial_step_search_order(self):
        """Gets the initial step search order.

        :return: the step search order
        :rtype: ``osid.workflow.StepSearchOrder``
        :raise: ``IllegalState`` -- ``supports_initial_step_search_order()`` is ``false``

        """
        return # osid.workflow.StepSearchOrder

    initial_step_search_order = property(fget=get_initial_step_search_order)

    def order_by_initial_state(self, style):
        """Orders the results by initial state.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_initial_state_search_order(self):
        """Tests if an initial state search order is available.

        :return: ``true`` if a state search order is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_initial_state_search_order(self):
        """Gets the initial state search order.

        :return: the state search order
        :rtype: ``osid.process.StateSearchOrder``
        :raise: ``IllegalState`` -- ``supports_initial_state_search_order()`` is ``false``

        """
        return # osid.process.StateSearchOrder

    initial_state_search_order = property(fget=get_initial_state_search_order)

    def get_process_search_order_record(self, process_record_type):
        """Gets the process search order record corresponding to the given process record ``Type``.

        Multiple retrievals return the same underlying object.

        :param process_record_type: a process record type
        :type process_record_type: ``osid.type.Type``
        :return: the process search order record
        :rtype: ``osid.workflow.records.ProcessSearchOrderRecord``
        :raise: ``NullArgument`` -- ``process_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(process_record_type)`` is ``false``

        """
        return # osid.workflow.records.ProcessSearchOrderRecord


class StepSearchOrder(osid_search_orders.OsidGovernatorSearchOrder, osid_search_orders.OsidSubjugateableSearchOrder):
    """An interface for specifying the ordering of search results."""
    def order_by_process(self, style):
        """Orders the results by process.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_process_search_order(self):
        """Tests if a process search order is available.

        :return: ``true`` if a process search order is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_process_search_order(self):
        """Gets the process search order.

        :return: the process search order
        :rtype: ``osid.workflow.ProcessSearchOrder``
        :raise: ``IllegalState`` -- ``supports_process_search_order()`` is ``false``

        """
        return # osid.workflow.ProcessSearchOrder

    process_search_order = property(fget=get_process_search_order)

    def order_by_initial(self, style):
        """Orders the results by initial steps.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_terminal(self, style):
        """Orders the results by terminal steps.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_next_state(self, style):
        """Orders the results by next state.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_next_state_search_order(self):
        """Tests if a next state search order is available.

        :return: ``true`` if a state search order is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_next_state_search_order(self):
        """Gets the next state search order.

        :return: the state search order
        :rtype: ``osid.process.StateSearchOrder``
        :raise: ``IllegalState`` -- ``supports_next_state_search_order()`` is ``false``

        """
        return # osid.process.StateSearchOrder

    next_state_search_order = property(fget=get_next_state_search_order)

    def get_step_search_order_record(self, step_record_type):
        """Gets the step search order record corresponding to the given step record ``Type``.

        Multiple retrievals return the same underlying object.

        :param step_record_type: a step record type
        :type step_record_type: ``osid.type.Type``
        :return: the step search order record
        :rtype: ``osid.workflow.records.StepSearchOrderRecord``
        :raise: ``NullArgument`` -- ``step_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(step_record_type)`` is ``false``

        """
        return # osid.workflow.records.StepSearchOrderRecord


class WorkSearchOrder(osid_search_orders.OsidObjectSearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_work_search_order_record(self, work_record_type):
        """Gets the work search order record corresponding to the given work record ``Type``.

        Multiple retrievals return the same underlying object.

        :param work_record_type: a work record type
        :type work_record_type: ``osid.type.Type``
        :return: the work search order record
        :rtype: ``osid.workflow.records.WorkSearchOrderRecord``
        :raise: ``NullArgument`` -- ``work_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(work_record_type)`` is ``false``

        """
        return # osid.workflow.records.WorkSearchOrderRecord


class OfficeSearchOrder(osid_search_orders.OsidCatalogSearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_office_search_order_record(self, office_record_type):
        """Gets the office search order record corresponding to the given office ``Type``.

        Multiple retrievals return the same underlying object.

        :param office_record_type: a office record type
        :type office_record_type: ``osid.type.Type``
        :return: the office search order record
        :rtype: ``osid.workflow.records.OfficeSearchOrderRecord``
        :raise: ``NullArgument`` -- ``office_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(office_record_type)`` is ``false``

        """
        return # osid.workflow.records.OfficeSearchOrderRecord


