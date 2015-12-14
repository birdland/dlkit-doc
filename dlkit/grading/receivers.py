
from ..osid import receivers as osid_receivers


class GradeSystemReceiver(osid_receivers.OsidReceiver):
    """The vault receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted
        ``GradeSystem`` objects."""

    def new_grade_systems(self, notification_id, grade_system_ids):
        """The callback for notifications of new grade systems.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param grade_system_ids: the ``Ids`` of the new ``GradeSystems``
        :type grade_system_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def changed_grade_systems(self, notification_id, grade_system_ids):
        """The callback for notification of updated grade systems.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param grade_system_ids: the ``Ids`` of the updated ``GradeSystems``
        :type grade_system_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def deleted_grade_systems(self, notification_id, grade_system_ids):
        """The callback for notification of deleted grade systems.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param grade_system_ids: the ``Ids`` of the deleted ``GradeSystems``
        :type grade_system_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class GradeEntryReceiver(osid_receivers.OsidReceiver):
    """The grade entry receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or
        deleted grade entries."""

    def new_grade_entries(self, notification_id, grade_entry_ids):
        """The callback for notifications of new grade entries.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param grade_entry_ids: the ``Ids`` of the new ``GradeEntries``
        :type grade_entry_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def changed_grade_entries(self, notification_id, grade_entry_ids):
        """The callback for notification of updated grade entries.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param grade_entry_ids: the ``Ids`` of the updated ``GradeEntries``
        :type grade_entry_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def deleted_grade_entries(self, notification_id, grade_entry_ids):
        """The callback for notification of deleted grade entries.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param grade_entry_ids: the ``Ids`` of the deleted ``GradeEntries``
        :type grade_entry_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class GradebookColumnReceiver(osid_receivers.OsidReceiver):
    """The grade receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted
        ``GradebookColumns``."""

    def new_gradebook_columns(self, notification_id, gradebook_column_ids):
        """The callback for notifications of new gradebook columns.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param gradebook_column_ids: the ``Ids`` of the new ``GradebookColumns``
        :type gradebook_column_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def chaneged_gradebook_columns(self, gradebook_column_ids):
        """The callback for notifications of new gradebook columns.

        :param gradebook_column_ids: the ``Ids`` of the new ``GradebookColumns``
        :type gradebook_column_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def deleted_gradebook_columns(self, notification_id, gradebook_column_ids):
        """The callback for notification of deleted gradebook columns.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param gradebook_column_ids: the ``Ids`` of the deleted ``GradebookColumns``
        :type gradebook_column_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class GradebookReceiver(osid_receivers.OsidReceiver):
    """The vault receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted
        ``Gradebook`` objects."""

    def new_gradebooks(self, notification_id, gradebook_ids):
        """The callback for notifications of new gradebooks.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param gradebook_ids: the ``Ids`` of the new ``Gradebooks``
        :type gradebook_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def new_ancestor_gradebook(self, gradebook_id, ancestor_id):
        """The callback for notifications of new gradebook ancestors.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :param ancestor_id: ``has_record_type(gradebook_record_type) is false``
        :type ancestor_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def new_descendant_gradebook(self, gradebook_id, descendant_id):
        """The callback for notifications of new gradebook descendants.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Gradebook`` descendant
        :type descendant_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def changed_gradebooks(self, notification_id, gradebook_ids):
        """The callback for notification of updated gradebooks.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param gradebook_ids: the ``Ids`` of the updated ``Gradebooks``
        :type gradebook_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def deleted_gradebooks(self, notification_id, gradebook_ids):
        """The callback for notification of deleted gradebooks.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param gradebook_ids: the ``Ids`` of the deleted ``Gradebooks``
        :type gradebook_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def deleted_ancestor_gradebook(self, gradebook_id, ancestor_id):
        """The callback for notifications of deleted gradebook ancestors.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Gradebook`` ancestor
        :type ancestor_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def deleted_descendant_gradebook(self, gradebook_id, descendant_id):
        """The callback for notifications of deleted gradebook descendants.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Gradebook`` descendant
        :type descendant_id: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def restructured_gradebook_hierarchy(self):
        """The callback for notifications of changes to a gradebook hierarchy where the hierarchy needs to refreshed.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass


