from ..osid import queries as osid_queries


class PostQuery(osid_queries.OsidObjectQuery):
    """This is the query for searching for posts.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def match_timestamp(self, start_time, end_time, match):
        """Matches entries whose sent time is between the supplied range inclusive.

        :param start_time: start time
        :type start_time: ``osid.calendaring.DateTime``
        :param end_time: end time
        :type end_time: ``osid.calendaring.DateTime``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``start_time`` is greater than ``end_time``
        :raise: ``NullArgument`` -- ``start_time`` or ``end_time`` is ``null``

        """
        pass

    def clear_timestamp_terms(self):
        """Clears the timestamp terms."""
        pass

    timestamp_terms = property(fdel=clear_timestamp_terms)

    def match_poster_id(self, resource_id, match):
        """Matches the poster of the entry.

        :param resource_id: ``Id`` to match
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        """
        pass

    def clear_poster_id_terms(self):
        """Clears the poster ``Id`` terms."""
        pass

    poster_id_terms = property(fdel=clear_poster_id_terms)

    def supports_poster_query(self):
        """Tests if a ``ResourceQuery`` is available for querying senders.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_poster_query(self):
        """Gets the query for a resource.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_poster_query()`` is ``false``

        """
        return # osid.resource.ResourceQuery

    poster_query = property(fget=get_poster_query)

    def clear_poster_terms(self):
        """Clears the poster terms."""
        pass

    poster_terms = property(fdel=clear_poster_terms)

    def match_posting_agent_id(self, agent_id, match):
        """Matches the posting agent of the entry.

        :param agent_id: ``Id`` to match
        :type agent_id: ``osid.id.Id``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        """
        pass

    def clear_posting_agent_id_terms(self):
        """Clears the posting agent ``Id`` terms."""
        pass

    posting_agent_id_terms = property(fdel=clear_posting_agent_id_terms)

    def supports_posting_agent_query(self):
        """Tests if an ``AgentQuery`` is available for querying posters.

        :return: ``true`` if an agent query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_posting_agent_query(self):
        """Gets the query for an agent.

        :return: the agent query
        :rtype: ``osid.authentication.AgentQuery``
        :raise: ``Unimplemented`` -- ``supports_posting_agent_query()`` is ``false``

        """
        return # osid.authentication.AgentQuery

    posting_agent_query = property(fget=get_posting_agent_query)

    def clear_posting_agent_terms(self):
        """Clears the posting agent terms."""
        pass

    posting_agent_terms = property(fdel=clear_posting_agent_terms)

    def match_subject_line(self, subject, string_match_type, match):
        """Adds a subject line to match.

        Multiple subject line matches can be added to perform a boolean
        ``OR`` among them.

        :param subject: display name to match
        :type subject: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``subject is`` not of ``string_match_type``
        :raise: ``NullArgument`` -- ``subject`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        """
        pass

    def match_any_subject_line(self, match):
        """Matches entries with any subject line.

        :param match: ``true`` to match entries with any subject line, ``false`` to match entries with no subject line
        :type match: ``boolean``

        """
        pass

    def clear_subject_line_terms(self):
        """Clears the subject line terms."""
        pass

    subject_line_terms = property(fdel=clear_subject_line_terms)

    def match_text(self, text, string_match_type, match):
        """Adds text to match.

        Multiple text matches can be added to perform a boolean ``OR``
        among them.

        :param text: text to match
        :type text: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``text is`` not of ``string_match_type``
        :raise: ``NullArgument`` -- ``text`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        """
        pass

    def match_any_text(self, match):
        """Matches entries with any text.

        :param match: ``true`` to match entries with any text, ``false`` to match entries with no text
        :type match: ``boolean``

        """
        pass

    def clear_text_terms(self):
        """Clears the text terms."""
        pass

    text_terms = property(fdel=clear_text_terms)

    def match_reply_id(self, reply_id, match):
        """Sets the reply ``Id`` for this query to match replies assigned to posts.

        :param reply_id: a reply ``Id``
        :type reply_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``reply_id`` is ``null``

        """
        pass

    def clear_reply_id_terms(self):
        """Clears the reply ``Id`` terms."""
        pass

    reply_id_terms = property(fdel=clear_reply_id_terms)

    def supports_reply_query(self):
        """Tests if a reply query is available.

        :return: ``true`` if a reply query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_reply_query(self):
        """Gets the query for a post.

        :return: the reply query
        :rtype: ``osid.forum.ReplyQuery``
        :raise: ``Unimplemented`` -- ``supports_reply_query()`` is ``false``

        """
        return # osid.forum.ReplyQuery

    reply_query = property(fget=get_reply_query)

    def match_any_reply(self, match):
        """Matches posts with any reply.

        :param match: ``true`` to match posts with any reply, ``false`` to match posts with no replies
        :type match: ``boolean``

        """
        pass

    def clear_reply_terms(self):
        """Clears the reply terms."""
        pass

    reply_terms = property(fdel=clear_reply_terms)

    def match_forum_id(self, forum_id, match):
        """Sets the post ``Id`` for this query to match replies assigned to forums.

        :param forum_id: a forum ``Id``
        :type forum_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``

        """
        pass

    def clear_forum_id_terms(self):
        """Clears the forum ``Id`` terms."""
        pass

    forum_id_terms = property(fdel=clear_forum_id_terms)

    def supports_forum_query(self):
        """Tests if a ``ForumQuery`` is available.

        :return: ``true`` if a forum query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_forum_query(self):
        """Gets the query for a forum query.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the forum query
        :rtype: ``osid.forum.ForumQuery``
        :raise: ``Unimplemented`` -- ``supports_forum_query()`` is ``false``

        """
        return # osid.forum.ForumQuery

    forum_query = property(fget=get_forum_query)

    def clear_forum_terms(self):
        """Clears the forum terms."""
        pass

    forum_terms = property(fdel=clear_forum_terms)

    def get_post_query_record(self, post_record_type):
        """Gets the post query record corresponding to the given ``Post`` record ``Type``.

        Multiple record retrievals produce a nested boolean ``OR`` term.

        :param post_record_type: a post record type
        :type post_record_type: ``osid.type.Type``
        :return: the post query record
        :rtype: ``osid.forum.records.PostQueryRecord``
        :raise: ``NullArgument`` -- ``post_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(post_record_type)`` is ``false``

        """
        return # osid.forum.records.PostQueryRecord


class ReplyQuery(osid_queries.OsidObjectQuery, osid_queries.OsidContainableQuery, osid_queries.OsidSubjugateableQuery):
    """This is the query for searching for replies.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def match_post_id(self, post_id, match):
        """Sets the post ``Id`` for this query to match replies to posts.

        :param post_id: a post ``Id``
        :type post_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``post_id`` is ``null``

        """
        pass

    def clear_post_id_terms(self):
        """Clears the post ``Id`` terms."""
        pass

    post_id_terms = property(fdel=clear_post_id_terms)

    def supports_post_query(self):
        """Tests if a ``PostQuery`` is available.

        :return: ``true`` if a post query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_post_query(self):
        """Gets the query for a post query.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the post query
        :rtype: ``osid.forum.PostQuery``
        :raise: ``Unimplemented`` -- ``supports_post_query()`` is ``false``

        """
        return # osid.forum.PostQuery

    post_query = property(fget=get_post_query)

    def clear_post_terms(self):
        """Clears the post terms."""
        pass

    post_terms = property(fdel=clear_post_terms)

    def match_timestamp(self, start_time, end_time, match):
        """Matches entries whose sent time is between the supplied range inclusive.

        :param start_time: start time
        :type start_time: ``osid.calendaring.DateTime``
        :param end_time: end time
        :type end_time: ``osid.calendaring.DateTime``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``start_time`` is greater than ``end_time``
        :raise: ``NullArgument`` -- ``start_time`` or ``end_time`` is ``null``

        """
        pass

    def clear_timestamp_terms(self):
        """Clears the timestamp terms."""
        pass

    timestamp_terms = property(fdel=clear_timestamp_terms)

    def match_poster_id(self, resource_id, match):
        """Matches the poster of the entry.

        :param resource_id: resource ``Id`` to match
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        """
        pass

    def clear_poster_id_terms(self):
        """Clears the poster resource ``Id`` terms."""
        pass

    poster_id_terms = property(fdel=clear_poster_id_terms)

    def supports_poster_query(self):
        """Tests if a ``ResourceQuery`` is available for querying posters.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_poster_query(self):
        """Gets the query for a resource.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_poster_query()`` is ``false``

        """
        return # osid.resource.ResourceQuery

    poster_query = property(fget=get_poster_query)

    def clear_poster_terms(self):
        """Clears the poster terms."""
        pass

    poster_terms = property(fdel=clear_poster_terms)

    def match_posting_agent_id(self, agent_id, match):
        """Matches the posting agent of the entry.

        :param agent_id: agent ``Id`` to match
        :type agent_id: ``osid.id.Id``
        :param match: ``true`` if for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        """
        pass

    def clear_posting_agent_id_terms(self):
        """Clears the posting agent ``Id`` terms."""
        pass

    posting_agent_id_terms = property(fdel=clear_posting_agent_id_terms)

    def supports_posting_agent_query(self):
        """Tests if an ``AgentQuery`` is available for querying posting agents.

        :return: ``true`` if an agent query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_posting_agent_query(self):
        """Gets the query for an agent.

        :return: the agent query
        :rtype: ``osid.authentication.AgentQuery``
        :raise: ``Unimplemented`` -- ``supports_posting_agent_query()`` is ``false``

        """
        return # osid.authentication.AgentQuery

    posting_agent_query = property(fget=get_posting_agent_query)

    def clear_posting_agent_terms(self):
        """Clears the posting agent terms."""
        pass

    posting_agent_terms = property(fdel=clear_posting_agent_terms)

    def match_subject_line(self, subject, string_match_type, match):
        """Adds a subject line to match.

        Multiple subject line matches can be added to perform a boolean
        ``OR`` among them.

        :param subject: display name to match
        :type subject: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``subject is`` not of ``string_match_type``
        :raise: ``NullArgument`` -- ``subject`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        """
        pass

    def match_any_subject_line(self, match):
        """Matches entries with any subject line.

        :param match: ``true`` to match entries with any subject line, ``false`` to match entries with no subject line
        :type match: ``boolean``

        """
        pass

    def clear_subject_line_terms(self):
        """Clears the subject line terms."""
        pass

    subject_line_terms = property(fdel=clear_subject_line_terms)

    def match_text(self, text, string_match_type, match):
        """Adds text to match.

        Multiple text matches can be added to perform a boolean ``OR``
        among them.

        :param text: text to match
        :type text: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``text is`` not of ``string_match_type``
        :raise: ``NullArgument`` -- ``text`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        """
        pass

    def match_any_text(self, match):
        """Matches entries with any text.

        :param match: ``true`` to match entries with any text, ``false`` to match entries with no text
        :type match: ``boolean``

        """
        pass

    def clear_text_terms(self):
        """Clears the text terms."""
        pass

    text_terms = property(fdel=clear_text_terms)

    def match_containing_reply_id(self, reply_id, match):
        """Sets the reply ``Id`` for this query to match replies that have the specified reply as an ancestor.

        :param reply_id: a reply ``Id``
        :type reply_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``reply_id`` is ``null``

        """
        pass

    def clear_containing_reply_id_terms(self):
        """Clears the containing reply ``Id`` terms."""
        pass

    containing_reply_id_terms = property(fdel=clear_containing_reply_id_terms)

    def supports_containing_reply_query(self):
        """Tests if a containing reply query is available.

        :return: ``true`` if a containing reply query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_containing_reply_query(self):
        """Gets the query for a containing reply.

        :return: the containing reply query
        :rtype: ``osid.forum.ReplyQuery``
        :raise: ``Unimplemented`` -- ``supports_containing_reply_query()`` is ``false``

        """
        return # osid.forum.ReplyQuery

    containing_reply_query = property(fget=get_containing_reply_query)

    def match_any_containing_reply(self, match):
        """Matches replies with any ancestor reply.

        :param match: ``true`` to match replies with any ancestor reply, ``false`` to match replies with no ancestor replies
        :type match: ``boolean``

        """
        pass

    def clear_containing_reply_terms(self):
        """Clears the containing reply terms."""
        pass

    containing_reply_terms = property(fdel=clear_containing_reply_terms)

    def match_contained_reply_id(self, reply_id, match):
        """Sets the reply ``Id`` for this query to match replies that have the specified reply as a descendant.

        :param reply_id: a reply ``Id``
        :type reply_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``reply_id`` is ``null``

        """
        pass

    def clear_contained_reply_id_terms(self):
        """Clears the contained reply ``Id`` terms."""
        pass

    contained_reply_id_terms = property(fdel=clear_contained_reply_id_terms)

    def supports_contained_reply_query(self):
        """Tests if a contained reply query is available.

        :return: ``true`` if a contained reply query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_contained_reply_query(self):
        """Gets the query for a contained reply.

        :return: the contained reply query
        :rtype: ``osid.forum.ReplyQuery``
        :raise: ``Unimplemented`` -- ``supports_contained_reply_query()`` is ``false``

        """
        return # osid.forum.ReplyQuery

    contained_reply_query = property(fget=get_contained_reply_query)

    def match_any_contained_reply(self, match):
        """Matches replies with any descednant reply.

        :param match: ``true`` to match replies with any descendant reply, ``false`` to match replies with no descendant replies
        :type match: ``boolean``

        """
        pass

    def clear_contained_reply_terms(self):
        """Clears the contained reply terms."""
        pass

    contained_reply_terms = property(fdel=clear_contained_reply_terms)

    def match_forum_id(self, forum_id, match):
        """Sets the post ``Id`` for this query to match replies assigned to forums.

        :param forum_id: a forum ``Id``
        :type forum_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``

        """
        pass

    def clear_forum_id_terms(self):
        """Clears the forum ``Id`` terms."""
        pass

    forum_id_terms = property(fdel=clear_forum_id_terms)

    def supports_forum_query(self):
        """Tests if a ``ForumQuery`` is available.

        :return: ``true`` if a forum query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_forum_query(self):
        """Gets the query for a forum query.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the forum query
        :rtype: ``osid.forum.ForumQuery``
        :raise: ``Unimplemented`` -- ``supports_forum_query()`` is ``false``

        """
        return # osid.forum.ForumQuery

    forum_query = property(fget=get_forum_query)

    def clear_forum_terms(self):
        """Clears the forum terms."""
        pass

    forum_terms = property(fdel=clear_forum_terms)

    def get_reply_query_record(self, reply_record_type):
        """Gets the reply query record corresponding to the given ``Reply`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param reply_record_type: a reply record type
        :type reply_record_type: ``osid.type.Type``
        :return: the reply query record
        :rtype: ``osid.forum.records.ReplyQueryRecord``
        :raise: ``NullArgument`` -- ``reply_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(reply_record_type)`` is ``false``

        """
        return # osid.forum.records.ReplyQueryRecord


class ForumQuery(osid_queries.OsidCatalogQuery):
    """This is the query for searching for forums.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def match_reply_id(self, reply_id, match):
        """Sets the reply ``Id`` for this query to match replies assigned to forums.

        :param reply_id: a reply ``Id``
        :type reply_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``reply_id`` is ``null``

        """
        pass

    def clear_reply_id_terms(self):
        """Clears the reply ``Id`` terms."""
        pass

    reply_id_terms = property(fdel=clear_reply_id_terms)

    def supports_reply_query(self):
        """Tests if a reply query is available.

        :return: ``true`` if a reply query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_reply_query(self):
        """Gets the query for a forum.

        :return: the reply query
        :rtype: ``osid.forum.ReplyQuery``
        :raise: ``Unimplemented`` -- ``supports_reply_query()`` is ``false``

        """
        return # osid.forum.ReplyQuery

    reply_query = property(fget=get_reply_query)

    def match_any_reply(self, match):
        """Matches forums with any reply.

        :param match: ``true`` to match forums with any reply, ``false`` to match forums with no replies
        :type match: ``boolean``

        """
        pass

    def clear_reply_terms(self):
        """Clears the reply terms."""
        pass

    reply_terms = property(fdel=clear_reply_terms)

    def match_post_id(self, post_id, match):
        """Sets the post ``Id`` for this query to match replies assigned to posts.

        :param post_id: a post ``Id``
        :type post_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``post_id`` is ``null``

        """
        pass

    def clear_post_id_terms(self):
        """Clears the post ``Id`` terms."""
        pass

    post_id_terms = property(fdel=clear_post_id_terms)

    def supports_post_query(self):
        """Tests if a ``PostQuery`` is available.

        :return: ``true`` if a post query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_post_query(self):
        """Gets the query for a post query.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the post query
        :rtype: ``osid.forum.PostQuery``
        :raise: ``Unimplemented`` -- ``supports_post_query()`` is ``false``

        """
        return # osid.forum.PostQuery

    post_query = property(fget=get_post_query)

    def match_any_post(self, match):
        """Matches forums with any post.

        :param match: ``true`` to match forums with any post, ``false`` to match forums with no posts
        :type match: ``boolean``

        """
        pass

    def clear_post_terms(self):
        """Clears the post terms."""
        pass

    post_terms = property(fdel=clear_post_terms)

    def match_ancestor_forum_id(self, forum_id, match):
        """Sets the forum ``Id`` for this query to match forums that have the specified forum as an ancestor.

        :param forum_id: a forum ``Id``
        :type forum_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``

        """
        pass

    def clear_ancestor_forum_id_terms(self):
        """Clears the ancestor forum ``Id`` terms."""
        pass

    ancestor_forum_id_terms = property(fdel=clear_ancestor_forum_id_terms)

    def supports_ancestor_forum_query(self):
        """Tests if a ``ForumQuery`` is available.

        :return: ``true`` if a forum query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_ancestor_forum_query(self):
        """Gets the query for a forum.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the forum query
        :rtype: ``osid.forum.ForumQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_forum_query()`` is ``false``

        """
        return # osid.forum.ForumQuery

    ancestor_forum_query = property(fget=get_ancestor_forum_query)

    def match_any_ancestor_forum(self, match):
        """Matches forums with any ancestor.

        :param match: ``true`` to match forums with any ancestor, ``false`` to match root forums
        :type match: ``boolean``

        """
        pass

    def clear_ancestor_forum_terms(self):
        """Clears the ancestor forum terms."""
        pass

    ancestor_forum_terms = property(fdel=clear_ancestor_forum_terms)

    def match_descendant_forum_id(self, forum_id, match):
        """Sets the forum ``Id`` for this query to match forums that have the specified forum as a descendant.

        :param forum_id: a forum ``Id``
        :type forum_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``

        """
        pass

    def clear_descendant_forum_id_terms(self):
        """Clears the descendant forum ``Id`` terms."""
        pass

    descendant_forum_id_terms = property(fdel=clear_descendant_forum_id_terms)

    def supports_descendant_forum_query(self):
        """Tests if a ``ForumQuery`` is available.

        :return: ``true`` if a forum query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_descendant_forum_query(self):
        """Gets the query for a forum.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the forum query
        :rtype: ``osid.forum.ForumQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_forum_query()`` is ``false``

        """
        return # osid.forum.ForumQuery

    descendant_forum_query = property(fget=get_descendant_forum_query)

    def match_any_descendant_forum(self, match):
        """Matches forums with any descendant.

        :param match: ``true`` to match forums with any descendant, ``false`` to match leaf forums
        :type match: ``boolean``

        """
        pass

    def clear_descendant_forum_terms(self):
        """Clears the descendant forum terms."""
        pass

    descendant_forum_terms = property(fdel=clear_descendant_forum_terms)

    def get_forum_query_record(self, forum_record_type):
        """Gets the forum query record corresponding to the given ``Forum`` record ``Type``.

        Multiple record retrievals produce a nested boolean ``OR`` term.

        :param forum_record_type: a forum record type
        :type forum_record_type: ``osid.type.Type``
        :return: the forum query record
        :rtype: ``osid.forum.records.ForumQueryRecord``
        :raise: ``NullArgument`` -- ``forum_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(forum_record_type)`` is ``false``

        """
        return # osid.forum.records.ForumQueryRecord


