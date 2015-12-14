
from ..osid import receivers as osid_receivers


class CommentReceiver(osid_receivers.OsidReceiver):
    """The comment receiver is the consumer supplied interface for receiving notifications pertaining to new or deleted
        comments."""

    def new_comments(self, notification_id, comment_ids):
        """The callback for notifications of new comments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param comment_ids: the ``Ids`` of the new comments
        :type comment_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def changed_comments(self, notification_id, comment_ids):
        """The callback for notifications of updated comments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param comment_ids: the ``Ids`` of the updated comments
        :type comment_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def deleted_comments(self, notification_id, comment_ids):
        """the callback for notification of deleted comments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param comment_ids: the ``Ids`` of the deleted comments
        :type comment_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class BookReceiver(osid_receivers.OsidReceiver):
    """The book receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted
        ``Book`` objects."""

    def new_books(self, notification_id, book_ids):
        """The callback for notifications of new books.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param book_ids: the ``Ids`` of the new ``Books``
        :type book_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def changed_books(self, notification_id, book_ids):
        """The callback for notification of updated books.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param book_ids: the ``Ids`` of the updated ``Books``
        :type book_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def deleted_books(self, notification_id, book_ids):
        """the callback for notification of deleted books.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param book_ids: the ``Ids`` of the registered ``Books``
        :type book_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def changed_child_of_books(self, notification_id, book_ids):
        """The callback for notifications of changes to children of book hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param book_ids: the ``Ids`` of the ``Books`` whose children have changed
        :type book_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


