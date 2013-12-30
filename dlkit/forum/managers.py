from ..osid import managers as osid_managers


class ForumProfile(osid_managers.OsidProfile):
    """The reply profile describes the interoperability among forum services."""
    def supports_visible_federation(self):
        """Tests if any post federation is exposed.

        Federation is exposed when a specific post may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of posts appears as a
        single post.

        :return: ``true`` if visible federation is supproted, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_post_lookup(self):
        """Tests for the availability of an post lookup service.

        :return: ``true`` if post lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_post_query(self):
        """Tests if querying posts is available.

        :return: ``true`` if post query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_post_search(self):
        """Tests if searching for posts is available.

        :return: ``true`` if post search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_post_admin(self):
        """Tests for the availability of a post administrative service for creating and deleting posts.

        :return: ``true`` if post administration is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_post_notification(self):
        """Tests for the availability of a post notification service.

        :return: ``true`` if post notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_post_forum(self):
        """Tests if a post to forum lookup session is available.

        :return: ``true`` if post forum lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_post_forum_assignment(self):
        """Tests if a post to forum assignment session is available.

        :return: ``true`` if post forum assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_post_smart_forum(self):
        """Tests if a post smart foruming session is available.

        :return: ``true`` if post smart foruming is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_reply_lookup(self):
        """Tests for the availability of a reply lookup service.

        :return: ``true`` if reply lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_reply_admin(self):
        """Tests if searching for replies is available.

        :return: ``true`` if reply search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_reply_notification(self):
        """Tests if reply notification is available.

        :return: ``true`` if reply notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_forum_lookup(self):
        """Tests for the availability of an forum lookup service.

        :return: ``true`` if forum lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_forum_query(self):
        """Tests if querying forums is available.

        :return: ``true`` if forum query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_forum_search(self):
        """Tests if searching for forums is available.

        :return: ``true`` if forum search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_forum_admin(self):
        """Tests for the availability of a forum administrative service for creating and deleting forums.

        :return: ``true`` if forum administration is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_forum_notification(self):
        """Tests for the availability of a forum notification service.

        :return: ``true`` if forum notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_forum_hierarchy(self):
        """Tests for the availability of a forum hierarchy traversal service.

        :return: ``true`` if forum hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_forum_hierarchy_design(self):
        """Tests for the availability of a forum hierarchy design service.

        :return: ``true`` if forum hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_forum_batch(self):
        """Tests if forum batch service is available.

        :return: ``true`` if forum batch service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_post_record_types(self):
        """Gets the supported ``Post`` record types.

        :return: a list containing the supported post record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    post_record_types = property(fget=get_post_record_types)

    def supports_post_record_type(self, post_record_type):
        """Tests if the given ``Post`` record type is supported.

        :param post_record_type: a ``Type`` indicating a ``Post`` record type
        :type post_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``post_record_type`` is ``null``

        """
        return # boolean

    def get_post_search_record_types(self):
        """Gets the supported post search record types.

        :return: a list containing the supported post search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    post_search_record_types = property(fget=get_post_search_record_types)

    def supports_post_search_record_type(self, post_search_record_type):
        """Tests if the given post search record type is supported.

        :param post_search_record_type: a ``Type`` indicating a post record type
        :type post_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``post_search_record_type`` is ``null``

        """
        return # boolean

    def get_reply_record_types(self):
        """Gets the supported ``Reply`` record types.

        :return: a list containing the supported reply record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    reply_record_types = property(fget=get_reply_record_types)

    def supports_reply_record_type(self, reply_record_type):
        """Tests if the given ``Reply`` record type is supported.

        :param reply_record_type: a ``Type`` indicating a ``Reply`` record type
        :type reply_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``reply_record_type`` is ``null``

        """
        return # boolean

    def get_reply_search_record_types(self):
        """Gets the supported reply search record types.

        :return: a list containing the supported reply search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    reply_search_record_types = property(fget=get_reply_search_record_types)

    def supports_reply_search_record_type(self, reply_search_record_type):
        """Tests if the given reply search record type is supported.

        :param reply_search_record_type: a ``Type`` indicating a reply record type
        :type reply_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``reply_search_record_type`` is ``null``

        """
        return # boolean

    def get_forum_record_types(self):
        """Gets the supported ``Forum`` record types.

        :return: a list containing the supported forum record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    forum_record_types = property(fget=get_forum_record_types)

    def supports_forum_record_type(self, forum_record_type):
        """Tests if the given ``Forum`` record type is supported.

        :param forum_record_type: a ``Type`` indicating a ``Forum`` record type
        :type forum_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``forum_record_type`` is ``null``

        """
        return # boolean

    def get_forum_search_record_types(self):
        """Gets the supported forum search record types.

        :return: a list containing the supported forum search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    forum_search_record_types = property(fget=get_forum_search_record_types)

    def supports_forum_search_record_type(self, forum_search_record_type):
        """Tests if the given forum search record type is supported.

        :param forum_search_record_type: a ``Type`` indicating a forum record type
        :type forum_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``forum_search_record_type`` is ``null``

        """
        return # boolean


class ForumManager(osid_managers.OsidManager, ForumProfile):
    """The reply manager provides access to forum sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``PostLookupSession:`` a session to retrieve posts
      * ``PostQuerySession:`` a session to query posts
      * ``PostSearchSession:`` a session to search for posts
      * ``PostAdminSession:`` a session to create, update and delete
        posts
      * ``PostNotificationSession:`` a session to receive notifications
        for changes in posts
      * ``PostForumSession:`` a session to lookup post forum mappings
      * ``PostForumAssignmentSession:`` a session to manage post forum
        mappings
      * ``PostSmartForumSession:`` a session to manage smart forums of
        posts
    
      * ``ReplyLookupSession:`` a session to lookup replies
      * ``ReplyAdminSession:`` a session to manage replies
      * ``ReplyNotificationSession:`` a session to subscribe to
        notifications of reply changes
    
      * ``ForumLookupSession:`` a session to retrieve forums
      * ``ForumQuerySession:`` a session to query forums
      * ``ForumSearchSession:`` a session to search for forums
      * ``ForumAdminSession:`` a session to create, update and delete
        forums
      * ``ForumNotificationSession:`` a session to receive notifications
        for changes in forums
      * ``ForumHierarchySession:`` a session to traverse hierarchies of
        forums
      * ``ForumHierarchyDesignSession:`` a session to manage hierarchies
        of forums

    
    The forum manager also provides a profile for determing the
    supported search types supported by this service.

    """
    def get_post_lookup_session(self):
        """Gets the ``OsidSession`` associated with the post lookup service.

        :return: a ``PostLookupSession``
        :rtype: ``osid.forum.PostLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_lookup()`` is ``false``

        """
        return # osid.forum.PostLookupSession

    post_lookup_session = property(fget=get_post_lookup_session)

    def get_post_lookup_session_for_forum(self, forum_id):
        """Gets the ``OsidSession`` associated with the post lookup service for the given forum.

        :param forum_id: the ``Id`` of the ``Post``
        :type forum_id: ``osid.id.Id``
        :return: a ``PostLookupSession``
        :rtype: ``osid.forum.PostLookupSession``
        :raise: ``NotFound`` -- no ``Forum`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.forum.PostLookupSession

    def get_post_query_session(self):
        """Gets the ``OsidSession`` associated with the post query service.

        :return: a ``PostQuerySession``
        :rtype: ``osid.forum.PostQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_query()`` is ``false``

        """
        return # osid.forum.PostQuerySession

    post_query_session = property(fget=get_post_query_session)

    def get_post_query_session_for_forum(self, forum_id):
        """Gets the ``OsidSession`` associated with the post query service for the given forum.

        :param forum_id: the ``Id`` of the ``Post``
        :type forum_id: ``osid.id.Id``
        :return: a ``PostQuerySession``
        :rtype: ``osid.forum.PostQuerySession``
        :raise: ``NotFound`` -- no ``Forum`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.forum.PostQuerySession

    def get_post_search_session(self):
        """Gets the ``OsidSession`` associated with the post search service.

        :return: a ``PostSearchSession``
        :rtype: ``osid.forum.PostSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_search()`` is ``false``

        """
        return # osid.forum.PostSearchSession

    post_search_session = property(fget=get_post_search_session)

    def get_post_search_session_for_forum(self, forum_id):
        """Gets the ``OsidSession`` associated with the post search service for the given forum.

        :param forum_id: the ``Id`` of the ``Post``
        :type forum_id: ``osid.id.Id``
        :return: a ``PostSearchSession``
        :rtype: ``osid.forum.PostSearchSession``
        :raise: ``NotFound`` -- no ``Forum`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.forum.PostSearchSession

    def get_post_admin_session(self):
        """Gets the ``OsidSession`` associated with the post administrative service.

        :return: a ``PostAdminSession``
        :rtype: ``osid.forum.PostAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_admin()`` is ``false``

        """
        return # osid.forum.PostAdminSession

    post_admin_session = property(fget=get_post_admin_session)

    def get_post_admin_session_for_forum(self, forum_id):
        """Gets the ``OsidSession`` associated with the post administrative service for the given forum.

        :param forum_id: the ``Id`` of the ``Post``
        :type forum_id: ``osid.id.Id``
        :return: a ``PostAdminSession``
        :rtype: ``osid.forum.PostAdminSession``
        :raise: ``NotFound`` -- no ``Forum`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.forum.PostAdminSession

    def get_post_notification_session(self, post_receiver):
        """Gets the ``OsidSession`` associated with the post notification service.

        :param post_receiver: the receiver
        :type post_receiver: ``osid.forum.PostReceiver``
        :return: a ``PostNotificationSession``
        :rtype: ``osid.forum.PostNotificationSession``
        :raise: ``NullArgument`` -- ``post_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_notification()`` is ``false``

        """
        return # osid.forum.PostNotificationSession

    def get_post_notification_session_for_forum(self, post_receiver, forum_id):
        """Gets the ``OsidSession`` associated with the post notification service for the given forum.

        :param post_receiver: the receiver
        :type post_receiver: ``osid.forum.PostReceiver``
        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :return: a ``PostNotificationSession``
        :rtype: ``osid.forum.PostNotificationSession``
        :raise: ``NotFound`` -- no ``Forum`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``post_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.forum.PostNotificationSession

    def get_post_forum_session(self):
        """Gets the session for retrieving post to forum mappings.

        :return: a ``PostForumSession``
        :rtype: ``osid.forum.PostForumSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_forum()`` is ``false``

        """
        return # osid.forum.PostForumSession

    post_forum_session = property(fget=get_post_forum_session)

    def get_post_forum_assignment_session(self):
        """Gets the session for assigning post to forum mappings.

        :return: a ``PostForumAssignmentSession``
        :rtype: ``osid.forum.PostForumAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_forum_assignment()`` is ``false``

        """
        return # osid.forum.PostForumAssignmentSession

    post_forum_assignment_session = property(fget=get_post_forum_assignment_session)

    def get_post_smart_forum_session(self, forum_id):
        """Gets the session associated with the post smart forum for the given forum.

        :param forum_id: the ``Id`` of the forum
        :type forum_id: ``osid.id.Id``
        :return: a ``PostSmartForumSession``
        :rtype: ``osid.forum.PostSmartForumSession``
        :raise: ``NotFound`` -- ``forum_id`` not found
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_smart_forum()`` is ``false``

        """
        return # osid.forum.PostSmartForumSession

    def get_reply_lookup_session(self):
        """Gets the ``OsidSession`` associated with the reply lookup service.

        :return: a ``ReplyLookupSession``
        :rtype: ``osid.forum.ReplyLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_reply_lookup()`` is ``false``

        """
        return # osid.forum.ReplyLookupSession

    reply_lookup_session = property(fget=get_reply_lookup_session)

    def get_reply_lookup_session_for_forum(self, forum_id):
        """Gets the ``OsidSession`` associated with the reply lookup service for the given forum.

        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :return: a ``ReplyLookupSession``
        :rtype: ``osid.forum.ReplyLookupSession``
        :raise: ``NotFound`` -- no ``Forum`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_reply_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.forum.ReplyLookupSession

    def get_reply_admin_session(self):
        """Gets the ``OsidSession`` associated with the reply administration service.

        :return: a ``ReplyAdminSession``
        :rtype: ``osid.forum.ReplyAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_reply_admin()`` is ``false``

        """
        return # osid.forum.ReplyAdminSession

    reply_admin_session = property(fget=get_reply_admin_session)

    def get_reply_admin_session_for_forum(self, forum_id):
        """Gets the ``OsidSession`` associated with the reply administration service for the given forum.

        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :return: a ``ReplyAdminSession``
        :rtype: ``osid.forum.ReplyAdminSession``
        :raise: ``NotFound`` -- no ``Forum`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_reply_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.forum.ReplyAdminSession

    def get_reply_notification_session(self, reply_receiver):
        """Gets the ``OsidSession`` associated with the reply notification service.

        :param reply_receiver: the receiver
        :type reply_receiver: ``osid.forum.ReplyReceiver``
        :return: a ``ReplyNotificationSession``
        :rtype: ``osid.forum.ReplyNotificationSession``
        :raise: ``NullArgument`` -- ``reply_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_reply_notification()`` is ``false``

        """
        return # osid.forum.ReplyNotificationSession

    def get_reply_notification_session_for_forum(self, reply_receiver, forum_id):
        """Gets the ``OsidSession`` associated with the reply notification service for the given forum.

        :param reply_receiver: the receiver
        :type reply_receiver: ``osid.forum.ReplyReceiver``
        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :return: a ``ReplyNotificationSession``
        :rtype: ``osid.forum.ReplyNotificationSession``
        :raise: ``NotFound`` -- no ``Forum`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``reply_receiver`` or ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_reply_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.forum.ReplyNotificationSession

    def get_forum_lookup_session(self):
        """Gets the ``OsidSession`` associated with the forum lookup service.

        :return: a ``ForumLookupSession``
        :rtype: ``osid.forum.ForumLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_lookup()`` is ``false``

        """
        return # osid.forum.ForumLookupSession

    forum_lookup_session = property(fget=get_forum_lookup_session)

    def get_forum_query_session(self):
        """Gets the ``OsidSession`` associated with the forum query service.

        :return: a ``ForumQuerySession``
        :rtype: ``osid.forum.ForumQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_query()`` is ``false``

        """
        return # osid.forum.ForumQuerySession

    forum_query_session = property(fget=get_forum_query_session)

    def get_forum_search_session(self):
        """Gets the ``OsidSession`` associated with the forum search service.

        :return: a ``ForumSearchSession``
        :rtype: ``osid.forum.ForumSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_search()`` is ``false``

        """
        return # osid.forum.ForumSearchSession

    forum_search_session = property(fget=get_forum_search_session)

    def get_forum_admin_session(self):
        """Gets the ``OsidSession`` associated with the forum administrative service.

        :return: a ``ForumAdminSession``
        :rtype: ``osid.forum.ForumAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_admin()`` is ``false``

        """
        return # osid.forum.ForumAdminSession

    forum_admin_session = property(fget=get_forum_admin_session)

    def get_forum_notification_session(self, forum_receiver):
        """Gets the ``OsidSession`` associated with the forum notification service.

        :param forum_receiver: the receiver
        :type forum_receiver: ``osid.forum.ForumReceiver``
        :return: a ``ForumNotificationSession``
        :rtype: ``osid.forum.ForumNotificationSession``
        :raise: ``NullArgument`` -- ``forum_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_notification()`` is ``false``

        """
        return # osid.forum.ForumNotificationSession

    def get_forum_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the forum hierarchy service.

        :return: a ``ForumHierarchySession``
        :rtype: ``osid.forum.ForumHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_hierarchy()`` is ``false``

        """
        return # osid.forum.ForumHierarchySession

    forum_hierarchy_session = property(fget=get_forum_hierarchy_session)

    def get_forum_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the forum hierarchy design service.

        :return: a ``ForumHierarchyDesignSession``
        :rtype: ``osid.forum.ForumHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_hierarchy_design()`` is ``false``

        """
        return # osid.forum.ForumHierarchyDesignSession

    forum_hierarchy_design_session = property(fget=get_forum_hierarchy_design_session)

    def get_forum_batch_manager(self):
        """Gets a ``ForumBatchManager``.

        :return: a ``ForumBatchManager``
        :rtype: ``osid.forum.batch.ForumBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_batch()`` is ``false``

        """
        return # osid.forum.batch.ForumBatchManager

    forum_batch_manager = property(fget=get_forum_batch_manager)


class ForumProxyManager(osid_managers.OsidProxyManager, ForumProfile):
    """The reply manager provides access to forum sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager accept a ``Proxy`` for passing information
    from a server environment. The sessions included in this manager
    are:

      * ``PostLookupSession:`` a session to retrieve posts
      * ``PostQuerySession:`` a session to query posts
      * ``PostSearchSession:`` a session to search for posts
      * ``PostAdminSession:`` a session to create, update and delete
        posts
      * ``PostNotificationSession:`` a session to receive notifications
        for changes in posts
      * ``PostForumSession:`` a session to lookup post forum mappings
      * ``PostForumAssignmentSession:`` a session to manage post forum
        mappings
      * ``PostSmartForumSession:`` a session to manage smart forums of
        posts
    
      * ``ReplyLookupSession:`` a session to lookup replies
      * ``ReplyAdminSession:`` a session to manage replies
      * ``ReplyNotificationSession:`` a session to subscribe to
        notifications of reply changes
    
      * ``ForumLookupSession:`` a session to retrieve forums
      * ``ForumQuerySession:`` a session to query forums
      * ``ForumSearchSession:`` a session to search for forums
      * ``ForumAdminSession:`` a session to create, update and delete
        forums
      * ``ForumNotificationSession:`` a session to receive notifications
        for changes in forums
      * ``ForumHierarchySession:`` a session to traverse hierarchies of
        forums
      * ``ForumHierarchyDesignSession:`` a session to manage hierarchies
        of forums

    
    The forum manager also provides a profile for determing the
    supported search types supported by this service.

    """
    def get_post_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the post lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PostLookupSession``
        :rtype: ``osid.forum.PostLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_lookup()`` is ``false``

        """
        return # osid.forum.PostLookupSession

    def get_post_lookup_session_for_forum(self, forum_id, proxy):
        """Gets the ``OsidSession`` associated with the post lookup service for the given forum.

        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PostLookupSession``
        :rtype: ``osid.forum.PostLookupSession``
        :raise: ``NotFound`` -- no ``Forum`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``forum_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.forum.PostLookupSession

    def get_post_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the post query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PostQuerySession``
        :rtype: ``osid.forum.PostQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_query()`` is ``false``

        """
        return # osid.forum.PostQuerySession

    def get_post_query_session_for_forum(self, forum_id, proxy):
        """Gets the ``OsidSession`` associated with the post query service for the given forum.

        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PostQuerySession``
        :rtype: ``osid.forum.PostQuerySession``
        :raise: ``NotFound`` -- no ``Post`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``forum_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.forum.PostQuerySession

    def get_post_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the post search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PostSearchSession``
        :rtype: ``osid.forum.PostSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_search()`` is ``false``

        """
        return # osid.forum.PostSearchSession

    def get_post_search_session_for_forum(self, forum_id, proxy):
        """Gets the ``OsidSession`` associated with the post search service for the given forum.

        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PostSearchSession``
        :rtype: ``osid.forum.PostSearchSession``
        :raise: ``NotFound`` -- no ``Post`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``forum_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.forum.PostSearchSession

    def get_post_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the post administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PostAdminSession``
        :rtype: ``osid.forum.PostAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_admin()`` is ``false``

        """
        return # osid.forum.PostAdminSession

    def get_post_admin_session_for_forum(self, forum_id, proxy):
        """Gets the ``OsidSession`` associated with the post administration service for the given forum.

        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PostAdminSession``
        :rtype: ``osid.forum.PostAdminSession``
        :raise: ``NotFound`` -- no ``Post`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``forum_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.forum.PostAdminSession

    def get_post_notification_session(self, post_receiver, proxy):
        """Gets the ``OsidSession`` associated with the post notification service.

        :param post_receiver: the receiver
        :type post_receiver: ``osid.forum.PostReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PostNotificationSession``
        :rtype: ``osid.forum.PostNotificationSession``
        :raise: ``NullArgument`` -- ``post_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_notification()`` is ``false``

        """
        return # osid.forum.PostNotificationSession

    def get_post_notification_session_for_forum(self, post_receiver, forum_id, proxy):
        """Gets the ``OsidSession`` associated with the post notification service for the given forum.

        :param post_receiver: the receiver
        :type post_receiver: ``osid.forum.PostReceiver``
        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PostNotificationSession``
        :rtype: ``osid.forum.PostNotificationSession``
        :raise: ``NotFound`` -- no ``Post`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``post_receiver, forum_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.forum.PostNotificationSession

    def get_post_forum_session(self, proxy):
        """Gets the session for retrieving post to forum mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PostForumSession``
        :rtype: ``osid.forum.PostForumSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_forum()`` is ``false``

        """
        return # osid.forum.PostForumSession

    def get_post_forum_assignment_session(self, proxy):
        """Gets the session for assigning post to forum mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PostForumAssignmentSession``
        :rtype: ``osid.forum.PostForumAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_forum_assignment()`` is ``false``

        """
        return # osid.forum.PostForumAssignmentSession

    def get_post_smart_forum_session(self, forum_id, proxy):
        """Gets the session for managing dynamic post forums for the given forum.

        :param forum_id: the ``Id`` of a forum
        :type forum_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``forum_id`` not found
        :rtype: ``osid.forum.PostSmartForumSession``
        :raise: ``NotFound`` -- ``forum_id`` or ``proxy`` is ``null``
        :raise: ``NullArgument`` -- ``forum_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_smart_forum()`` is ``false``

        """
        return # osid.forum.PostSmartForumSession

    def get_reply_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the reply lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ReplyLookupSession``
        :rtype: ``osid.forum.ReplyLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_reply_lookup()`` is ``false``

        """
        return # osid.forum.ReplyLookupSession

    def get_reply_lookup_session_for_forum(self, forum_id, proxy):
        """Gets the ``OsidSession`` associated with the reply lookup service for the given forum.

        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ReplyLookupSession``
        :rtype: ``osid.forum.ReplyLookupSession``
        :raise: ``NotFound`` -- no ``Forum`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``forum_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_reply_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.forum.ReplyLookupSession

    def get_reply_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the reply administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ReplyAdminSession``
        :rtype: ``osid.forum.ReplyAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_reply_admin()`` is ``false``

        """
        return # osid.forum.ReplyAdminSession

    def get_reply_admin_session_for_forum(self, forum_id, proxy):
        """Gets the ``OsidSession`` associated with the reply administration service for the given forum.

        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ReplyAdminSession``
        :rtype: ``osid.forum.ReplyAdminSession``
        :raise: ``NotFound`` -- no ``Forum`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``forum_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_reply_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.forum.ReplyAdminSession

    def get_reply_notification_session(self, reply_receiver, proxy):
        """Gets the ``OsidSession`` associated with the reply notification service.

        :param reply_receiver: the receiver
        :type reply_receiver: ``osid.forum.ReplyReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ReplyNotificationSession``
        :rtype: ``osid.forum.ReplyNotificationSession``
        :raise: ``NullArgument`` -- ``reply_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_reply_notification()`` is ``false``

        """
        return # osid.forum.ReplyNotificationSession

    def get_reply_notification_session_for_forum(self, reply_receiver, forum_id, proxy):
        """Gets the ``OsidSession`` associated with the reply notification service for the given forum.

        :param reply_receiver: the receiver
        :type reply_receiver: ``osid.forum.ReplyReceiver``
        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ReplyNotificationSession``
        :rtype: ``osid.forum.ReplyNotificationSession``
        :raise: ``NotFound`` -- no ``Forum`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``reply_receiver, forum_id,`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_reply_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.forum.ReplyNotificationSession

    def get_forum_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the forum lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ForumLookupSession``
        :rtype: ``osid.forum.ForumLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_lookup()`` is ``false``

        """
        return # osid.forum.ForumLookupSession

    def get_forum_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the forum query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ForumQuerySession``
        :rtype: ``osid.forum.ForumQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_query()`` is ``false``

        """
        return # osid.forum.ForumQuerySession

    def get_forum_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the forum search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ForumSearchSession``
        :rtype: ``osid.forum.ForumSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_search()`` is ``false``

        """
        return # osid.forum.ForumSearchSession

    def get_forum_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the forum administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ForumAdminSession``
        :rtype: ``osid.forum.ForumAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_admin()`` is ``false``

        """
        return # osid.forum.ForumAdminSession

    def get_forum_notification_session(self, forum_receiver, proxy):
        """Gets the ``OsidSession`` associated with the forum notification service.

        :param forum_receiver: the receiver
        :type forum_receiver: ``osid.forum.ForumReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ForumNotificationSession``
        :rtype: ``osid.forum.ForumNotificationSession``
        :raise: ``NullArgument`` -- ``forum_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_notification()`` is ``false``

        """
        return # osid.forum.ForumNotificationSession

    def get_forum_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the forum hierarchy service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ForumHierarchySession``
        :rtype: ``osid.forum.ForumHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_hierarchy()`` is ``false``

        """
        return # osid.forum.ForumHierarchySession

    def get_forum_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the forum hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ForumHierarchyDesignSession``
        :rtype: ``osid.forum.ForumHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_hierarchy_design()`` is ``false``

        """
        return # osid.forum.ForumHierarchyDesignSession

    def get_forum_batch_proxy_manager(self):
        """Gets a ``ForumBatchProxyManager``.

        :return: a ``ForumBatchProxyManager``
        :rtype: ``osid.forum.batch.ForumBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_batch()`` is ``false``

        """
        return # osid.forum.batch.ForumBatchProxyManager

    forum_batch_proxy_manager = property(fget=get_forum_batch_proxy_manager)


