from ..osid import receivers as osid_receivers


class GradeSystemReceiver(osid_receivers.OsidReceiver):
    """The vault receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``GradeSystem`` objects."""
    def new_grade_system(self, grade_system_id):
        """The callback for notifications of new grade systems.

        :param grade_system_id: the ``Id`` of the new ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``

        """
        pass

    def changed_grade_system(self, grade_system_id):
        """The callback for notification of updated grade systems.

        :param grade_system_id: the ``Id`` of the updated ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``

        """
        pass

    def deleted_grade_system(self, grade_system_id):
        """The callback for notification of deleted grade systems.

        :param grade_system_id: the ``Id`` of the deleted ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``

        """
        pass


class GradeEntryReceiver(osid_receivers.OsidReceiver):
    """The grade entry receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted grade entries."""
    def new_grade_entry(self, grade_entry_id):
        """The callback for notifications of new grade entries.

        :param grade_entry_id: the ``Id`` of the new ``GradeEntry``
        :type grade_entry_id: ``osid.id.Id``

        """
        pass

    def changed_grade_entry(self, grade_entry_id):
        """The callback for notification of updated grade entries.

        :param grade_entry_id: the ``Id`` of the updated ``GradeEntry``
        :type grade_entry_id: ``osid.id.Id``

        """
        pass

    def deleted_grade_entry(self, grade_entry_id):
        """The callback for notification of deleted grade entries.

        :param grade_entry_id: the ``Id`` of the deleted ``GradeEntry``
        :type grade_entry_id: ``osid.id.Id``

        """
        pass


class GradebookColumnReceiver(osid_receivers.OsidReceiver):
    """The grade receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``GradebookColumns``."""
    def new_gradebook_column(self, gradebook_column_id):
        """The callback for notifications of new gradebook columns.

        :param gradebook_column_id: the ``Id`` of the new ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``

        """
        pass

    def chaneged_gradebook_column(self, gradebook_column_id):
        """The callback for notifications of new gradebook columns.

        :param gradebook_column_id: the ``Id`` of the new ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``

        """
        pass

    def deleted_gradebook_column(self, gradebook_column_id):
        """The callback for notification of deleted gradebook columns.

        :param gradebook_column_id: the ``Id`` of the deleted ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``

        """
        pass


class GradebookReceiver(osid_receivers.OsidReceiver):
    """The vault receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Gradebook`` objects."""
    def new_gradebook(self, gradebook_id):
        """The callback for notifications of new gradebooks.

        :param gradebook_id: the ``Id`` of the new ``Gradebook``
        :type gradebook_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_gradebook(self, gradebook_id, ancestor_id):
        """The callback for notifications of new gradebook ancestors.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :param ancestor_id: ``has_record_type(gradebook_record_type) is false``
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_gradebook(self, gradebook_id, descendant_id):
        """The callback for notifications of new gradebook descendants.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Gradebook`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_gradebook(self, gradebook_id):
        """The callback for notification of updated gradebooks.

        :param gradebook_id: the ``Id`` of the updated ``Gradebook``
        :type gradebook_id: ``osid.id.Id``

        """
        pass

    def deleted_gradebook(self, gradebook_id):
        """The callback for notification of deleted gradebooks.

        :param gradebook_id: the ``Id`` of the deleted ``Gradebook``
        :type gradebook_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_gradebook(self, gradebook_id, ancestor_id):
        """The callback for notifications of deleted gradebook ancestors.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Gradebook`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_gradebook(self, gradebook_id, descendant_id):
        """The callback for notifications of deleted gradebook descendants.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Gradebook`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass


