from ..osid import searches as osid_searches


class PostSearch(osid_searches.OsidSearch):
    """The search interface for governing post searches."""
    def search_among_posts(self, post_ids):
        """Execute this search among the given list of posts.

        :param post_ids: list of posts
        :type post_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``post_ids`` is ``null``

        """
        pass

    def order_post_results(self, post_search_order):
        """Specify an ordering to the search results.

        :param post_search_order: post search order
        :type post_search_order: ``osid.forum.PostSearchOrder``
        :raise: ``NullArgument`` -- ``post_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``post_search_order`` is not of this service

        """
        pass

    def get_post_search_record(self, post_search_record_type):
        """Gets the post search record corresponding to the given post search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param post_search_record_type: a post search record type
        :type post_search_record_type: ``osid.type.Type``
        :return: the post search record
        :rtype: ``osid.forum.records.PostSearchRecord``
        :raise: ``NullArgument`` -- ``post_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(post_search_record_type)`` is ``false``

        """
        return # osid.forum.records.PostSearchRecord


class PostSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_posts(self):
        """Gets the post list resulting from a search.

        :return: the post list
        :rtype: ``osid.forum.PostList``
        :raise: ``IllegalState`` -- list has already been retrieved

        """
        return # osid.forum.PostList

    posts = property(fget=get_posts)

    def get_post_query_inspector(self):
        """Gets the inspector for the query to examine the terns used in the search.

        :return: the query inspector
        :rtype: ``osid.forum.PostQueryInspector``

        """
        return # osid.forum.PostQueryInspector

    post_query_inspector = property(fget=get_post_query_inspector)

    def get_post_search_results_record(self, post_search_record_type):
        """Gets the post search results record corresponding to the given post search record Type.

        This method is used to retrieve an object implementing the
        requested record.

        :param post_search_record_type: a post search record type
        :type post_search_record_type: ``osid.type.Type``
        :return: the post search results record
        :rtype: ``osid.forum.records.PostSearchResultsRecord``
        :raise: ``NullArgument`` -- ``PostSearchRecordType`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(post_search_record_type)`` is ``false``

        """
        return # osid.forum.records.PostSearchResultsRecord


class ReplySearch(osid_searches.OsidSearch):
    """The search interface for governing reply searches."""
    def search_among_replies(self, reply_ids):
        """Execute this search among the given list of replies.

        :param reply_ids: list of replies
        :type reply_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``reply_ids`` is ``null``

        """
        pass

    def order_reply_results(self, reply_search_order):
        """Specify an ordering to the search results.

        :param reply_search_order: reply search order
        :type reply_search_order: ``osid.forum.ReplySearchOrder``
        :raise: ``NullArgument`` -- ``reply_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``reply_search_order`` is not of this service

        """
        pass

    def get_reply_search_record(self, reply_search_record_type):
        """Gets the reply search record corresponding to the given reply search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record .

        :param reply_search_record_type: a reply search record type
        :type reply_search_record_type: ``osid.type.Type``
        :return: the reply search record
        :rtype: ``osid.forum.records.ReplySearchRecord``
        :raise: ``NullArgument`` -- ``reply_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(reply_search_record_type)`` is ``false``

        """
        return # osid.forum.records.ReplySearchRecord


class ReplySearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_replies(self):
        """Gets the reply list resulting from a search.

        :return: the reply list
        :rtype: ``osid.forum.ReplyList``
        :raise: ``IllegalState`` -- list has already been retrieved

        """
        return # osid.forum.ReplyList

    replies = property(fget=get_replies)

    def get_reply_query_inspector(self):
        """Gets the inspector for the query to examine the terns used in the search.

        :return: the query inspector
        :rtype: ``osid.forum.ReplyQueryInspector``

        """
        return # osid.forum.ReplyQueryInspector

    reply_query_inspector = property(fget=get_reply_query_inspector)

    def get_reply_search_results_record(self, reply_search_record_type):
        """Gets the reply search results record corresponding to the given reply search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param reply_search_record_type: a reply search record type
        :type reply_search_record_type: ``osid.type.Type``
        :return: the reply search results record
        :rtype: ``osid.forum.records.ReplySearchResultsRecord``
        :raise: ``NullArgument`` -- ``reply_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(reply_search_record_type)`` is ``false``

        """
        return # osid.forum.records.ReplySearchResultsRecord


class ForumSearch(osid_searches.OsidSearch):
    """The search interface for governing forum searches."""
    def search_among_forums(self, forum_ids):
        """Execute this search among the given list of forums.

        :param forum_ids: list of forums
        :type forum_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``forum_ids`` is ``null``

        """
        pass

    def order_forum_results(self, forumsearch_order):
        """Specify an ordering to the search results.

        :param forumsearch_order: forum search order
        :type forumsearch_order: ``osid.forum.ForumSearchOrder``
        :raise: ``NullArgument`` -- ``forumsearch_order`` is ``null``
        :raise: ``Unsupported`` -- ``forumsearch_order`` is not of this service

        """
        pass

    def get_forum_search_record(self, forum_search_record_type):
        """Gets the forum search record corresponding to the given forum search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param forum_search_record_type: a forum search record type
        :type forum_search_record_type: ``osid.type.Type``
        :return: the forum search record
        :rtype: ``osid.forum.records.ForumSearchRecord``
        :raise: ``NullArgument`` -- ``forum_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(forum_search_record_type)`` is ``false``

        """
        return # osid.forum.records.ForumSearchRecord


class ForumSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_forums(self):
        """Gets the forum list resulting from a search.

        :return: the forum list
        :rtype: ``osid.forum.ForumList``
        :raise: ``IllegalState`` -- list has already been retrieved

        """
        return # osid.forum.ForumList

    forums = property(fget=get_forums)

    def get_forum_query_inspector(self):
        """Gets the inspector for the query to examine the terns used in the search.

        :return: the query inspector
        :rtype: ``osid.forum.ForumQueryInspector``

        """
        return # osid.forum.ForumQueryInspector

    forum_query_inspector = property(fget=get_forum_query_inspector)

    def get_forum_search_results_record(self, forum_search_record_type):
        """Gets the forum search results record corresponding to the given forum search record Type.

        This method is used to retrieve an object implementing the
        requested record.

        :param forum_search_record_type: a forum search record type
        :type forum_search_record_type: ``osid.type.Type``
        :return: the forum search results record
        :rtype: ``osid.forum.records.ForumSearchResultsRecord``
        :raise: ``NullArgument`` -- ``forum_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(forum_search_record_type)`` is ``false``

        """
        return # osid.forum.records.ForumSearchResultsRecord


