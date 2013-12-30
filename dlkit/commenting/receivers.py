from ..osid import receivers as osid_receivers


class CommentReceiver(osid_receivers.OsidReceiver):
    """The comment receiver is the consumer supplied interface for receiving notifications pertaining to new or deleted comments."""
    def new_comment(self, comment_id):
        """The callback for notifications of new comments.

        :param comment_id: the ``Id`` of the new comment
        :type comment_id: ``osid.id.Id``

        """
        pass

    def changed_comment(self, comment_id):
        """The callback for notifications of updated comments.

        :param comment_id: the ``Id`` of the updated comment
        :type comment_id: ``osid.id.Id``

        """
        pass

    def deleted_comment(self, comment_id):
        """the callback for notification of deleted comments.

        :param comment_id: the ``Id`` of the deleted comment
        :type comment_id: ``osid.id.Id``

        """
        pass


class BookReceiver(osid_receivers.OsidReceiver):
    """The book receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Book`` objects."""
    def new_book(self, book_id):
        """The callback for notifications of new books.

        :param book_id: the ``Id`` of the new ``Book``
        :type book_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_book(self, book_id, ancestor_id):
        """The callback for notifications of new ancestors of a book.

        :param book_id: the ``Id`` of the registered ``Book``
        :type book_id: ``osid.id.Id``
        :param ancestor_id: the Id of the new ancestor book
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_book(self, book_id, descendant_id):
        """The callback for notifications of new descendant of a book.

        :param book_id: the ``Id`` of the registered ``Book``
        :type book_id: ``osid.id.Id``
        :param descendant_id: the Id of the new descendant book
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_book(self, book_id):
        """The callback for notification of updated books.

        :param book_id: the ``Id`` of the updated ``Book``
        :type book_id: ``osid.id.Id``

        """
        pass

    def deleted_book(self, book_id):
        """the callback for notification of deleted books.

        :param book_id: the ``Id`` of the registered ``Book``
        :type book_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_book(self, book_id, ancestor_id):
        """The callback for notifications of deleted ancestors of a book.

        :param book_id: the ``Id`` of the registered ``Book``
        :type book_id: ``osid.id.Id``
        :param ancestor_id: the Id of the removed ancestor book
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_book(self, book_id, descendant_id):
        """The callback for notifications of deleted descendants of a book.

        :param book_id: the ``Id`` of the registered ``Book``
        :type book_id: ``osid.id.Id``
        :param descendant_id: the Id of the deleted descendant book
        :type descendant_id: ``osid.id.Id``

        """
        pass


