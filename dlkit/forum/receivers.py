from ..osid import receivers as osid_receivers


class PostReceiver(osid_receivers.OsidReceiver):
    """The post receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Post`` objects."""
    def new_post(self, post_id):
        """The callback for notifications of new posts.

        :param post_id: the ``Id`` of the new ``Post``
        :type post_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_post(self, post_id, ancestor_id):
        """The callback for notifications of new ancestors of a post.

        :param post_id: the ``Id`` of the registered ``Post``
        :type post_id: ``osid.id.Id``
        :param ancestor_id: the Id of the new ancestor post
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_post(self, post_id, descendant_id):
        """The callback for notifications of new descendant of a post.

        :param post_id: the ``Id`` of the registered ``Post``
        :type post_id: ``osid.id.Id``
        :param descendant_id: the Id of the new descendant post
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_post(self, post_id):
        """The callback for notification of updated posts.

        :param post_id: the ``Id`` of the updated ``Post``
        :type post_id: ``osid.id.Id``

        """
        pass

    def deleted_post(self, post_id):
        """the callback for notification of deleted posts.

        :param post_id: the ``Id`` of the registered ``Post``
        :type post_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_post(self, post_id, ancestor_id):
        """The callback for notifications of deleted ancestors of a post.

        :param post_id: the ``Id`` of the registered ``Post``
        :type post_id: ``osid.id.Id``
        :param ancestor_id: the Id of the removed ancestor post
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_post(self, post_id, descendant_id):
        """The callback for notifications of deleted descendants of a post.

        :param post_id: the ``Id`` of the registered ``Post``
        :type post_id: ``osid.id.Id``
        :param descendant_id: the Id of the deleted descendant post
        :type descendant_id: ``osid.id.Id``

        """
        pass


class ReplyReceiver(osid_receivers.OsidReceiver):
    """The reply receiver is the consumer supplied interface for receiving notifications pertaining to new or deleted replies."""
    def new_reply(self, reply_id):
        """The callback for notifications of new replies.

        :param reply_id: the ``Id`` of the new reply
        :type reply_id: ``osid.id.Id``

        """
        pass

    def changed_reply(self, reply_id):
        """The callback for notifications of updated replies.

        :param reply_id: the ``Id`` of the updated reply
        :type reply_id: ``osid.id.Id``

        """
        pass

    def deleted_reply(self, reply_id):
        """the callback for notification of deleted replies.

        :param reply_id: the ``Id`` of the deleted reply
        :type reply_id: ``osid.id.Id``

        """
        pass


class ForumReceiver(osid_receivers.OsidReceiver):
    """The forum receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Forum`` objects."""
    def new_forum(self, forum_id):
        """The callback for notifications of new forums.

        :param forum_id: the ``Id`` of the new ``Forum``
        :type forum_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_forum(self, forum_id, ancestor_id):
        """The callback for notifications of new ancestors of a forum.

        :param forum_id: the ``Id`` of the registered ``Forum``
        :type forum_id: ``osid.id.Id``
        :param ancestor_id: the Id of the new ancestor forum
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_forum(self, forum_id, descendant_id):
        """The callback for notifications of new descendant of a forum.

        :param forum_id: the ``Id`` of the registered ``Forum``
        :type forum_id: ``osid.id.Id``
        :param descendant_id: the Id of the new descendant forum
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_forum(self, forum_id):
        """The callback for notification of updated forums.

        :param forum_id: the ``Id`` of the updated ``Forum``
        :type forum_id: ``osid.id.Id``

        """
        pass

    def deleted_forum(self, forum_id):
        """the callback for notification of deleted forums.

        :param forum_id: the ``Id`` of the registered ``Forum``
        :type forum_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_forum(self, forum_id, ancestor_id):
        """The callback for notifications of deleted ancestors of a forum.

        :param forum_id: the ``Id`` of the registered ``Forum``
        :type forum_id: ``osid.id.Id``
        :param ancestor_id: the Id of the removed ancestor forum
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_forum(self, forum_id, descendant_id):
        """The callback for notifications of deleted descendants of a forum.

        :param forum_id: the ``Id`` of the registered ``Forum``
        :type forum_id: ``osid.id.Id``
        :param descendant_id: the Id of the deleted descendant forum
        :type descendant_id: ``osid.id.Id``

        """
        pass


