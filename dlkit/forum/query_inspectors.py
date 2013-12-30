from ..osid import query_inspectors as osid_query_inspectors


class PostQueryInspector(osid_query_inspectors.OsidObjectQueryInspector):
    """This is the query inspector for examining for post queries.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def get_timestamp_terms(self):
        """Gets the timestamp terms.

        :return: the timestamp terms
        :rtype: ``osid.search.terms.DateTimeTerm``

        """
        return # osid.search.terms.DateTimeTerm

    timestamp_terms = property(fget=get_timestamp_terms)

    def get_poster_id_terms(self):
        """Gets the poster ``Id`` terms.

        :return: the resource ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    poster_id_terms = property(fget=get_poster_id_terms)

    def get_poster_terms(self):
        """Gets the poster terms.

        :return: the query terms
        :rtype: ``osid.resource.ResourceQueryInspector``

        """
        return # osid.resource.ResourceQueryInspector

    poster_terms = property(fget=get_poster_terms)

    def get_posting_agent_id_terms(self):
        """Gets the poster ``Id`` terms.

        :return: the agent ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    posting_agent_id_terms = property(fget=get_posting_agent_id_terms)

    def get_posting_agent_terms(self):
        """Gets the poster terms.

        :return: the query terms
        :rtype: ``osid.authentication.AgentQueryInspector``

        """
        return # osid.authentication.AgentQueryInspector

    posting_agent_terms = property(fget=get_posting_agent_terms)

    def get_subject_line_terms(self):
        """Gets the subject line terms.

        :return: the query terms
        :rtype: ``osid.search.terms.StringTerm``

        """
        return # osid.search.terms.StringTerm

    subject_line_terms = property(fget=get_subject_line_terms)

    def get_text_terms(self):
        """Gets the text terms.

        :return: the query terms
        :rtype: ``osid.search.terms.StringTerm``

        """
        return # osid.search.terms.StringTerm

    text_terms = property(fget=get_text_terms)

    def get_reply_id_terms(self):
        """Gets the reply ``Id`` terms.

        :return: the reply ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    reply_id_terms = property(fget=get_reply_id_terms)

    def get_reply_terms(self):
        """Gets the reply terms.

        :return: the reply terms
        :rtype: ``osid.forum.ReplyQueryInspector``

        """
        return # osid.forum.ReplyQueryInspector

    reply_terms = property(fget=get_reply_terms)

    def get_forum_id_terms(self):
        """Gets the forum ``Id`` terms.

        :return: the forum ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    forum_id_terms = property(fget=get_forum_id_terms)

    def get_forum_terms(self):
        """Gets the forum terms.

        :return: the forum terms
        :rtype: ``osid.forum.ForumQueryInspector``

        """
        return # osid.forum.ForumQueryInspector

    forum_terms = property(fget=get_forum_terms)

    def get_post_query_inspector_record(self, post_record_type):
        """Gets the query inspector record corresponding to the given ``Post`` record ``Type``.

        :param post_record_type: a post record type
        :type post_record_type: ``osid.type.Type``
        :return: the post query inspector record
        :rtype: ``osid.forum.records.PostQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``post_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(post_record_type)`` is ``false``

        """
        return # osid.forum.records.PostQueryInspectorRecord


class ReplyQueryInspector(osid_query_inspectors.OsidObjectQueryInspector, osid_query_inspectors.OsidContainableQueryInspector, osid_query_inspectors.OsidSubjugateableQueryInspector):
    """This is the query inspector for examining reply queries.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def get_post_id_terms(self):
        """Gets the post ``Id`` terms.

        :return: the post ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    post_id_terms = property(fget=get_post_id_terms)

    def get_post_terms(self):
        """Gets the post terms.

        :return: the post terms
        :rtype: ``osid.forum.ReplyQueryInspector``

        """
        return # osid.forum.ReplyQueryInspector

    post_terms = property(fget=get_post_terms)

    def get_timestamp_terms(self):
        """Gets the timestamp terms.

        :return: the timestamp terms
        :rtype: ``osid.search.terms.DateTimeTerm``

        """
        return # osid.search.terms.DateTimeTerm

    timestamp_terms = property(fget=get_timestamp_terms)

    def get_poster_id_terms(self):
        """Gets the poster ``Id`` terms.

        :return: the resource ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    poster_id_terms = property(fget=get_poster_id_terms)

    def get_poster_terms(self):
        """Gets the poster terms.

        :return: the query terms
        :rtype: ``osid.resource.ResourceQueryInspector``

        """
        return # osid.resource.ResourceQueryInspector

    poster_terms = property(fget=get_poster_terms)

    def get_posting_agent_id_terms(self):
        """Gets the posting agent ``Id`` terms.

        :return: the agent ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    posting_agent_id_terms = property(fget=get_posting_agent_id_terms)

    def get_posting_agent_terms(self):
        """Gets the posting agent terms.

        :return: the query terms
        :rtype: ``osid.authentication.AgentQueryInspector``

        """
        return # osid.authentication.AgentQueryInspector

    posting_agent_terms = property(fget=get_posting_agent_terms)

    def get_subject_line_terms(self):
        """Gets the subject line terms.

        :return: the query terms
        :rtype: ``osid.search.terms.StringTerm``

        """
        return # osid.search.terms.StringTerm

    subject_line_terms = property(fget=get_subject_line_terms)

    def get_text_terms(self):
        """Gets the text terms.

        :return: the query terms
        :rtype: ``osid.search.terms.StringTerm``

        """
        return # osid.search.terms.StringTerm

    text_terms = property(fget=get_text_terms)

    def get_containing_reply_id_terms(self):
        """Gets the containing reply ``Id`` terms.

        :return: the containing reply ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    containing_reply_id_terms = property(fget=get_containing_reply_id_terms)

    def get_containing_reply_terms(self):
        """Gets the containing reply terms.

        :return: the containing reply terms
        :rtype: ``osid.forum.ReplyQueryInspector``

        """
        return # osid.forum.ReplyQueryInspector

    containing_reply_terms = property(fget=get_containing_reply_terms)

    def get_contained_reply_id_terms(self):
        """Gets the contained reply ``Id`` terms.

        :return: the contained reply ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    contained_reply_id_terms = property(fget=get_contained_reply_id_terms)

    def get_contained_reply_terms(self):
        """Gets the contained reply terms.

        :return: the contained reply terms
        :rtype: ``osid.forum.ReplyQueryInspector``

        """
        return # osid.forum.ReplyQueryInspector

    contained_reply_terms = property(fget=get_contained_reply_terms)

    def get_forum_id_terms(self):
        """Gets the forum ``Id`` terms.

        :return: the forum ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    forum_id_terms = property(fget=get_forum_id_terms)

    def get_forum_terms(self):
        """Gets the forum terms.

        :return: the forum terms
        :rtype: ``osid.forum.ForumQueryInspector``

        """
        return # osid.forum.ForumQueryInspector

    forum_terms = property(fget=get_forum_terms)

    def get_reply_query_inspector_record(self, reply_record_type):
        """Gets the reply query inspector record corresponding to the given ``Reply`` record ``Type``.

        :param reply_record_type: a reply record type
        :type reply_record_type: ``osid.type.Type``
        :return: the reply query inspector record
        :rtype: ``osid.forum.records.ReplyQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``reply_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(reply_record_type)`` is ``false``

        """
        return # osid.forum.records.ReplyQueryInspectorRecord


class ForumQueryInspector(osid_query_inspectors.OsidCatalogQueryInspector):
    """This is the query inspector for examining forum queries.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def get_reply_id_terms(self):
        """Gets the reply ``Id`` terms.

        :return: the reply ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    reply_id_terms = property(fget=get_reply_id_terms)

    def get_reply_terms(self):
        """Gets the reply terms.

        :return: the reply terms
        :rtype: ``osid.forum.ReplyQueryInspector``

        """
        return # osid.forum.ReplyQueryInspector

    reply_terms = property(fget=get_reply_terms)

    def get_post_id_terms(self):
        """Gets the post ``Id`` terms.

        :return: the post ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    post_id_terms = property(fget=get_post_id_terms)

    def get_post_terms(self):
        """Gets the post terms.

        :return: the post terms
        :rtype: ``osid.forum.PostQueryInspector``

        """
        return # osid.forum.PostQueryInspector

    post_terms = property(fget=get_post_terms)

    def get_ancestor_forum_id_terms(self):
        """Gets the ancestor forum ``Id`` terms.

        :return: the ancestor forum ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    ancestor_forum_id_terms = property(fget=get_ancestor_forum_id_terms)

    def get_ancestor_forum_terms(self):
        """Gets the ancestor forum terms.

        :return: the ancestor forum terms
        :rtype: ``osid.forum.ForumQueryInspector``

        """
        return # osid.forum.ForumQueryInspector

    ancestor_forum_terms = property(fget=get_ancestor_forum_terms)

    def get_descendant_forum_id_terms(self):
        """Gets the descendant forum ``Id`` terms.

        :return: the descendant forum ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    descendant_forum_id_terms = property(fget=get_descendant_forum_id_terms)

    def get_descendant_forum_terms(self):
        """Gets the descendant forum terms.

        :return: the descendant forum terms
        :rtype: ``osid.forum.ForumQueryInspector``

        """
        return # osid.forum.ForumQueryInspector

    descendant_forum_terms = property(fget=get_descendant_forum_terms)

    def get_forum_query_inspector_record(self, forum_record_type):
        """Gets the forum query inspector record corresponding to the given ``Forum`` record ``Type``.

        :param forum_record_type: a forum record type
        :type forum_record_type: ``osid.type.Type``
        :return: the forum query inspector record
        :rtype: ``osid.forum.records.ForumQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``forum_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(forum_record_type)`` is ``false``

        """
        return # osid.forum.records.ForumQueryInspectorRecord


