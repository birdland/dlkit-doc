from ..osid import objects as osid_objects
from ..osid import markers as osid_markers


class Post(osid_objects.OsidObject):
    """A ``Post`` represents a blob of text posted to a forum by a poster.

    Like all OSID objects, a ``Post`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """
    def get_timestamp(self):
        """Gets the time of this post.

        :return: the time
        :rtype: ``osid.calendaring.DateTime``

        """
        return # osid.calendaring.DateTime

    timestamp = property(fget=get_timestamp)

    def get_poster_id(self):
        """Gets the poster ``Id`` of this post.

        :return: the poster resource ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    poster_id = property(fget=get_poster_id)

    def get_poster(self):
        """Gets the poster of this post.

        :return: the poster resource
        :rtype: ``osid.resource.Resource``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.resource.Resource

    poster = property(fget=get_poster)

    def get_posting_agent_id(self):
        """Gets the posting agent ``Id`` of this post.

        :return: the posting agent ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    posting_agent_id = property(fget=get_posting_agent_id)

    def get_posting_agent(self):
        """Gets the posting agent of this post.

        :return: the posting agent
        :rtype: ``osid.authentication.Agent``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.authentication.Agent

    posting_agent = property(fget=get_posting_agent)

    def get_subject_line(self):
        """Gets the subject line of this post.

        :return: the subject
        :rtype: ``osid.locale.DisplayText``

        """
        return # osid.locale.DisplayText

    subject_line = property(fget=get_subject_line)

    def get_text(self):
        """Gets the text of the post.

        :return: the entry text
        :rtype: ``osid.locale.DisplayText``

        """
        return # osid.locale.DisplayText

    text = property(fget=get_text)

    def get_post_record(self, post_record_type):
        """Gets the post record corresponding to the given ``Post`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``post_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(post_record_type)``
        is ``true`` .

        :param post_record_type: the type of post record to retrieve
        :type post_record_type: ``osid.type.Type``
        :return: the post record
        :rtype: ``osid.forum.records.PostRecord``
        :raise: ``NullArgument`` -- ``post_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(post_record_type)`` is ``false``

        """
        return # osid.forum.records.PostRecord


class PostForm(osid_objects.OsidObjectForm):
    """This is the form for creating and updating ``Posts``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``PostAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_subject_line_metadata(self):
        """Gets the metadata for the subject line.

        :return: metadata for the subject line
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    subject_line_metadata = property(fget=get_subject_line_metadata)

    def set_timestamp(self, subject_line):
        """Sets the subject line.

        :param subject_line: the new subject line
        :type subject_line: ``string``
        :raise: ``InvalidArgument`` -- ``subject_line`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``subject_line`` is ``null``

        """
        pass

    timestamp = property(fset=set_timestamp)

    def clear_subject_line(self):
        """Clears the subject line.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    subject_line = property(fdel=clear_subject_line)

    def get_text_metadata(self):
        """Gets the metadata for the text.

        :return: metadata for the text
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    text_metadata = property(fget=get_text_metadata)

    def set_text(self, text):
        """Sets the text.

        :param text: the new text
        :type text: ``string``
        :raise: ``InvalidArgument`` -- ``text`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``text`` is ``null``

        """
        pass

    def clear_text(self):
        """Clears the text.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    text = property(fget=set_text, fdel=clear_text)

    def get_post_form_record(self, post_record_type):
        """Gets the ``PostFormRecord`` corresponding to the given post record ``Type``.

        :param post_record_type: the post record type
        :type post_record_type: ``osid.type.Type``
        :return: the post form record
        :rtype: ``osid.forum.records.PostFormRecord``
        :raise: ``NullArgument`` -- ``post_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(post_record_type)`` is ``false``

        """
        return # osid.forum.records.PostFormRecord


class PostList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``PostList`` provides a means for accessing ``Post`` elements sequentially either one at a time or many at a time.

    Examples: while (pl.hasNext()) { Post post = pl.getNextPost(); }

    orp
      while (bl.hasNext()) {
           Post[] posts = pl.getNextPosts(pl.available());
      }
    


    """
    def get_next_post(self):
        """Gets the next ``Post`` in this list.

        :return: the next ``Post`` in this list. The ``has_next()`` method should be used to test that a next ``Post`` is available before calling this method.
        :rtype: ``osid.forum.Post``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.forum.Post

    next_post = property(fget=get_next_post)

    def get_next_posts(self, n):
        """Gets the next set of ``Post`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Post`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Post`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.forum.Post``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.forum.Post


class Reply(osid_objects.OsidObject, osid_markers.Containable, osid_markers.Subjugateable):
    """A ``Reply`` is a response to a ``Post`` or another ``Reply``."""
    def get_post_id(self):
        """Gets the ``Id`` of the original top level post for this reply.

        :return: the post ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    post_id = property(fget=get_post_id)

    def get_post(self):
        """Gets the original top level post.

        :return: the post
        :rtype: ``osid.forum.Post``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.forum.Post

    post = property(fget=get_post)

    def get_reply_ids(self):
        """Gets the ``Ids`` of the replies to this rpely.

        :return: the reply ``Ids``
        :rtype: ``osid.id.IdList``

        """
        return # osid.id.IdList

    reply_ids = property(fget=get_reply_ids)

    def get_replies(self):
        """Gets the replies to this reply.

        :return: the replies
        :rtype: ``osid.forum.ReplyList``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.forum.ReplyList

    replies = property(fget=get_replies)

    def get_timestamp(self):
        """Gets the time of this entry.

        :return: the time
        :rtype: ``osid.calendaring.DateTime``

        """
        return # osid.calendaring.DateTime

    timestamp = property(fget=get_timestamp)

    def get_poster_id(self):
        """Gets the poster resource ``Id`` of this entry.

        :return: the poster resource ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    poster_id = property(fget=get_poster_id)

    def get_poster(self):
        """Gets the posting of this entry.

        :return: the poster resource
        :rtype: ``osid.resource.Resource``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.resource.Resource

    poster = property(fget=get_poster)

    def get_posting_agent_id(self):
        """Gets the posting ``Id`` of this entry.

        :return: the posting agent ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    posting_agent_id = property(fget=get_posting_agent_id)

    def get_posting_agent(self):
        """Gets the posting of this entry.

        :return: the posting agent
        :rtype: ``osid.authentication.Agent``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.authentication.Agent

    posting_agent = property(fget=get_posting_agent)

    def get_subject_line(self):
        """Gets the subject line of this entry.

        :return: the subject
        :rtype: ``osid.locale.DisplayText``

        """
        return # osid.locale.DisplayText

    subject_line = property(fget=get_subject_line)

    def get_text(self):
        """Gets the text of the entry.

        :return: the entry text
        :rtype: ``osid.locale.DisplayText``

        """
        return # osid.locale.DisplayText

    text = property(fget=get_text)

    def get_reply_record(self, reply_record_type):
        """Gets the reply record corresponding to the given ``Reply`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``reply_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(reply_record_type)``
        is ``true`` .

        :param reply_record_type: the type of reply record to retrieve
        :type reply_record_type: ``osid.type.Type``
        :return: the reply record
        :rtype: ``osid.forum.records.ReplyRecord``
        :raise: ``NullArgument`` -- ``reply_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(reply_record_type)`` is ``false``

        """
        return # osid.forum.records.ReplyRecord


class ReplyForm(osid_objects.OsidObjectForm, osid_objects.OsidContainableForm, osid_objects.OsidSubjugateableForm):
    """This is the form for creating and updating ``Reply`` objects.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ReplyAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_subject_line_metadata(self):
        """Gets the metadata for the subject line.

        :return: metadata for the subject line
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    subject_line_metadata = property(fget=get_subject_line_metadata)

    def set_timestamp(self, subject_line):
        """Sets the subject line.

        :param subject_line: the new subject line
        :type subject_line: ``string``
        :raise: ``InvalidArgument`` -- ``subject_line`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``subject_line`` is ``null``

        """
        pass

    timestamp = property(fset=set_timestamp)

    def clear_subject_line(self):
        """Clears the subject line.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    subject_line = property(fdel=clear_subject_line)

    def get_text_metadata(self):
        """Gets the metadata for the text.

        :return: metadata for the text
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    text_metadata = property(fget=get_text_metadata)

    def set_text(self, text):
        """Sets the text.

        :param text: the new text
        :type text: ``string``
        :raise: ``InvalidArgument`` -- ``text`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``text`` is ``null``

        """
        pass

    def clear_text(self):
        """Clears the text.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    text = property(fget=set_text, fdel=clear_text)

    def get_reply_form_record(self, reply_record_type):
        """Gets the ``ReplyFormRecord`` corresponding to the given reply record ``Type``.

        :param reply_record_type: the reply record type
        :type reply_record_type: ``osid.type.Type``
        :return: the reply form record
        :rtype: ``osid.forum.records.ReplyFormRecord``
        :raise: ``NullArgument`` -- ``reply_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(reply_record_type)`` is ``false``

        """
        return # osid.forum.records.ReplyFormRecord


class ReplyList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ReplyList`` provides a means for accessing ``Reply`` elements sequentially either one at a time or many at a time.

    Examples: while (rl.hasNext()) { Reply reply = rl.getNextReply(); }

    or
      while (rl.hasNext()) {
           Reply[] replies = rl.getNextRepliess(rl.available());
      }
    


    """
    def get_next_reply(self):
        """Gets the next ``Reply`` in this list.

        :return: the next ``Reply`` in this list. The ``has_next()`` method should be used to test that a next ``Reply`` is available before calling this method.
        :rtype: ``osid.forum.Reply``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.forum.Reply

    next_reply = property(fget=get_next_reply)

    def get_next_replies(self, n):
        """Gets the next set of ``Reply`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Reply`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Reply`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.forum.Reply``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.forum.Reply


class Forum(osid_objects.OsidCatalog):
    """A ``Forum`` represents a collection of posts and replies.

    Like all OSID objects, a ``Forum`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """
    def get_forum_record(self, forum_record_type):
        """Gets the forum record corresponding to the given ``Forum`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``forum_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(forum_record_type)``
        is ``true`` .

        :param forum_record_type: the type of forum record to retrieve
        :type forum_record_type: ``osid.type.Type``
        :return: the forum record
        :rtype: ``osid.forum.records.ForumRecord``
        :raise: ``NullArgument`` -- ``forum_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(forum_record_type)`` is ``false``

        """
        return # osid.forum.records.ForumRecord


class ForumForm(osid_objects.OsidCatalogForm):
    """This is the form for creating and updating ``Forums``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ForumAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_forum_form_record(self, forum_record_type):
        """Gets the ``ForumFormRecord`` corresponding to the given forum record ``Type``.

        :param forum_record_type: the forum record type
        :type forum_record_type: ``osid.type.Type``
        :return: the forum form record
        :rtype: ``osid.forum.records.ForumFormRecord``
        :raise: ``NullArgument`` -- ``forum_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(forum_record_type)`` is ``false``

        """
        return # osid.forum.records.ForumFormRecord


class ForumList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ForumList`` provides a means for accessing ``Forum`` elements sequentially either one at a time or many at a time.

    Examples: while (fl.hasNext()) { Forum forum = fl.getNextForum(); }

    or
      while (fl.hasNext()) {
           Forum[] forums = fl.getNextForums(fl.available());
      }
    


    """
    def get_next_forum(self):
        """Gets the next ``Forum`` in this list.

        :return: the next ``Forum`` in this list. The ``has_next()`` method should be used to test that a next ``Forum`` is available before calling this method.
        :rtype: ``osid.forum.Forum``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.forum.Forum

    next_forum = property(fget=get_next_forum)

    def get_next_forums(self, n):
        """Gets the next set of ``Forum`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Forum`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Forum`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.forum.Forum``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.forum.Forum


class ForumNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``ForumHierarchySession``.

    """
    def get_forum(self):
        """Gets the ``Forum`` at this node.

        :return: the forum represented by this node
        :rtype: ``osid.forum.Forum``

        """
        return # osid.forum.Forum

    forum = property(fget=get_forum)

    def get_parent_forum_nodes(self):
        """Gets the parents of this forum.

        :return: the parents of this forum
        :rtype: ``osid.forum.ForumNodeList``

        """
        return # osid.forum.ForumNodeList

    parent_forum_nodes = property(fget=get_parent_forum_nodes)

    def get_child_forum_nodes(self):
        """Gets the children of this forum.

        :return: the children of this forum
        :rtype: ``osid.forum.ForumNodeList``

        """
        return # osid.forum.ForumNodeList

    child_forum_nodes = property(fget=get_child_forum_nodes)


class ForumNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ForumNodeList`` provides a means for accessing ``ForumNode`` elements sequentially either one at a time or many at a time.

    Examples: while (fnl.hasNext()) { ForumNode node =
    fnl.getNextForumNode(); }

    or
      while (fnl.hasNext()) {
           ForumNode[] nodes = fnl.getNextForumNodes(fnl.available());
      }
    


    """
    def get_next_forum_node(self):
        """Gets the next ``ForumNode`` in this list.

        :return: the next ``ForumNode`` in this list. The ``has_next()`` method should be used to test that a next ``ForumNode`` is available before calling this method.
        :rtype: ``osid.forum.ForumNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.forum.ForumNode

    next_forum_node = property(fget=get_next_forum_node)

    def get_next_forum_nodes(self, n):
        """Gets the next set of ``ForumNode`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``ForumNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``ForumNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.forum.ForumNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.forum.ForumNode


