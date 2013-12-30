from ..osid import search_orders as osid_search_orders


class PostSearchOrder(osid_search_orders.OsidObjectSearchOrder):
    """An interface for specifying the ordering of search results."""
    def order_by_timestamp(self, style):
        """Specifies a preference for ordering the result set by the timestamp.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_poster(self, style):
        """Specifies a preference for ordering the result set by the poster.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_poster_search_order(self):
        """Tests if a resource order interface is available.

        :return: ``true`` if a poster order interface is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_poster_search_order(self):
        """Gets the poster order interface.

        :return: the poster search order interface
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_poster_search_order()`` is ``false``

        """
        return # osid.resource.ResourceSearchOrder

    poster_search_order = property(fget=get_poster_search_order)

    def order_by_posting_agent(self, style):
        """Specifies a preference for ordering the result set by the posting agent.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_posting_agent_search_order(self):
        """Tests if a posting agent order interface is available.

        :return: ``true`` if a posting agent order interface is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_posting_agent_search_order(self):
        """Gets the posting agent search order interface.

        :return: the posting agent search order interface
        :rtype: ``osid.authentication.AgentSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_posting_agent_search_order()`` is ``false``

        """
        return # osid.authentication.AgentSearchOrder

    posting_agent_search_order = property(fget=get_posting_agent_search_order)

    def order_by_subject_line(self, style):
        """Specifies a preference for ordering the result set by the subject.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_text(self, style):
        """Specifies a preference for ordering the result set by the text.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def get_post_search_order_record(self, post_record_type):
        """Gets the post search record order corresponding to the given post record Type.

        Multiple retrievals return the same underlying object.

        :param post_record_type: a post record type
        :type post_record_type: ``osid.type.Type``
        :return: the post search order record
        :rtype: ``osid.forum.records.PostSearchOrderRecord``
        :raise: ``NullArgument`` -- ``post_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(post_record_type)`` is ``false``

        """
        return # osid.forum.records.PostSearchOrderRecord


class ReplySearchOrder(osid_search_orders.OsidObjectSearchOrder, osid_search_orders.OsidContainableSearchOrder, osid_search_orders.OsidSubjugateableSearchOrder):
    """An interface for specifying the ordering of search results."""
    def order_by_timestamp(self, style):
        """Specifies a preference for ordering the result set by the timestamp.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_poster(self, style):
        """Specifies a preference for ordering the result set by the poster.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_poster_search_order(self):
        """Tests if a poster resource search order interface is available.

        :return: ``true`` if a resource search order interface is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_poster_search_order(self):
        """Gets the resource search order interface.

        :return: the resource search order interface
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_poster_search_order()`` is ``false``

        """
        return # osid.resource.ResourceSearchOrder

    poster_search_order = property(fget=get_poster_search_order)

    def order_by_posting_agent(self, style):
        """Specifies a preference for ordering the result set by the posting agent.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_posting_agent_search_order(self):
        """Tests if a posting agent search order interface is available.

        :return: ``true`` if a agent search order interface is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_posting_agent_search_order(self):
        """Gets the posting agent search order interface.

        :return: the agent search order interface
        :rtype: ``osid.authentication.AgentSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_posting_agent_search_order()`` is ``false``

        """
        return # osid.authentication.AgentSearchOrder

    posting_agent_search_order = property(fget=get_posting_agent_search_order)

    def order_by_subject_line(self, style):
        """Specifies a preference for ordering the result set by the subject.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_text(self, style):
        """Specifies a preference for ordering the result set by the text.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def get_reply_search_order_record(self, reply_record_type):
        """Gets the reply search order record corresponding to the given reply record ``Type``.

        Multiple retrievals return the same underlying object.

        :param reply_record_type: a reply record type
        :type reply_record_type: ``osid.type.Type``
        :return: the reply search order record
        :rtype: ``osid.forum.records.ReplySearchOrderRecord``
        :raise: ``NullArgument`` -- ``reply_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(reply_record_type)`` is ``false``

        """
        return # osid.forum.records.ReplySearchOrderRecord


class ForumSearchOrder(osid_search_orders.OsidCatalogSearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_forum_search_order_record(self, forum_record_type):
        """Gets the forum search order record corresponding to the given forum record Type.

        Multiple retrievals return the same underlying object.

        :param forum_record_type: a forum record type
        :type forum_record_type: ``osid.type.Type``
        :return: the forum search order record
        :rtype: ``osid.forum.records.ForumSearchOrderRecord``
        :raise: ``NullArgument`` -- ``forum_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(forum_record_type)`` is ``false``

        """
        return # osid.forum.records.ForumSearchOrderRecord


