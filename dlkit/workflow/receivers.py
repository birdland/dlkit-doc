from ..osid import receivers as osid_receivers


class ProcessReceiver(osid_receivers.OsidReceiver):
    """The process receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Process`` objects."""
    def new_process(self, process_id):
        """The callback for notifications of new process.

        :param process_id: the ``Id`` of the new ``Process``
        :type process_id: ``osid.id.Id``

        """
        pass

    def changed_process(self, process_id):
        """The callback for notification of updated process.

        :param process_id: the ``Id`` of the updated ``Process``
        :type process_id: ``osid.id.Id``

        """
        pass

    def deleted_process(self, process_id):
        """The callback for notification of deleted process.

        :param process_id: the ``Id`` of the deleted ``Process``
        :type process_id: ``osid.id.Id``

        """
        pass


class StepReceiver(osid_receivers.OsidReceiver):
    """The step receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Step`` objects."""
    def new_step(self, step_id):
        """The callback for notifications of new steps.

        :param step_id: the ``Id`` of the new ``Step``
        :type step_id: ``osid.id.Id``

        """
        pass

    def changed_step(self, step_id):
        """The callback for notification of updated steps.

        :param step_id: the ``Id`` of the updated ``Step``
        :type step_id: ``osid.id.Id``

        """
        pass

    def deleted_step(self, step_id):
        """The callback for notification of deleted steps.

        :param step_id: the ``Id`` of the deleted ``Step``
        :type step_id: ``osid.id.Id``

        """
        pass


class WorkReceiver(osid_receivers.OsidReceiver):
    """The work receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Work`` objects."""
    def new_work(self, work_id):
        """The callback for notifications of new works.

        :param work_id: the ``Id`` of the new ``Work``
        :type work_id: ``osid.id.Id``

        """
        pass

    def changed_work(self, work_id):
        """The callback for notification of updated works.

        :param work_id: the ``Id`` of the updated ``Work``
        :type work_id: ``osid.id.Id``

        """
        pass

    def deleted_work(self, work_id):
        """The callback for notification of deleted works.

        :param work_id: the ``Id`` of the deleted ``Work``
        :type work_id: ``osid.id.Id``

        """
        pass


class WorkflowEventReceiver(osid_receivers.OsidReceiver):
    """The workflow event receiver is the consumer supplied interface for receiving notifications pertaining to new ``WorkflowEvents``."""
    def new_workflow_event(self, workflow_event_id):
        """The callback for notifications of new workflow events.

        :param workflow_event_id: the ``Id`` of the new ``WorkflowEvent``
        :type workflow_event_id: ``osid.id.Id``

        """
        pass


class OfficeReceiver(osid_receivers.OsidReceiver):
    """The office receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Office`` objects."""
    def new_office(self, office_id):
        """The callback for notifications of new offices.

        :param office_id: the ``Id`` of the new ``Office``
        :type office_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_office(self, office_id, ancestor_id):
        """The callback for notifications of new office ancestors.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ``Office`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_office(self, office_id, descendant_id):
        """The callback for notifications of new office descendants.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Office`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_office(self, office_id):
        """The callback for notification of updated office.

        :param office_id: the ``Id`` of the updated ``Office``
        :type office_id: ``osid.id.Id``

        """
        pass

    def deleted_office(self, office_id):
        """The callback for notification of deleted offices.

        :param office_id: the ``Id`` of the deleted ``Office``
        :type office_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_office(self, office_id, ancestor_id):
        """The callback for notifications of deleted office ancestors.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Office`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_office(self, office_id, descendant_id):
        """The callback for notifications of deleted office descendants.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Office`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass


