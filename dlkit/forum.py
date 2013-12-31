# -*- coding: utf-8 -*-
"""Reply Open Service Interface Definitions
forum version 3.0.0

The Forum OSID defines threaded diiscussion groups managing a set of
posts and replies.

Posts

A ``Post`` is an ``OsidObject`` that defines some text, a timestamp, and
a poster.

Replies

A ``Reply`` is similar to a ``Post`` but is in response to either a
``Post`` or another ``Reply``. A ``Reply`` is a ``Containable`` making
directly accessible any nested ``Replies`` outside of the session.

Posters

An ``Agent`` posts to a ``Forum`` or an ``Agent`` replies to a ``Post``.
The relationship between the ``Agent`` and its associated ``Resource``
is orchestrated within the Froum OSID. ``Posts`` and ``Replies`` reveal
both the posting ``Agent`` and the associated poster ``Resource``.

Forum Catalogs

Forums represent collections of ``Posts``. Forums may be created through
federation or by selecting ``Posts`` based on their attributes to create
a virtual catalog of Posts. ``Replies`` are always associated with their
``Posts`` and may not be cataloged independently.

Sub Packages

The Forum OSID contains a Forum Batch OSID for managing ``Posts`` and
``Replies`` in bulk.

"""
from . import osid
from .osid_errors import Unimplemented, IllegalState, OperationFailed


class ForumProfile(osid.OsidProfile):

    def supports_visible_federation(self):
        """Tests if any post federation is exposed.
        Federation is exposed when a specific post may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of posts appears as a
        single post.

        :return: ``true`` if visible federation is supproted, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_post_lookup(self):
        """Tests for the availability of an post lookup service.

        :return: ``true`` if post lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_post_query(self):
        """Tests if querying posts is available.

        :return: ``true`` if post query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_post_search(self):
        """Tests if searching for posts is available.

        :return: ``true`` if post search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_post_admin(self):
        """Tests for the availability of a post administrative service for creating and deleting posts.

        :return: ``true`` if post administration is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_post_notification(self):
        """Tests for the availability of a post notification service.

        :return: ``true`` if post notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_post_forum(self):
        """Tests if a post to forum lookup session is available.

        :return: ``true`` if post forum lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_post_forum_assignment(self):
        """Tests if a post to forum assignment session is available.

        :return: ``true`` if post forum assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_post_smart_forum(self):
        """Tests if a post smart foruming session is available.

        :return: ``true`` if post smart foruming is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_reply_lookup(self):
        """Tests for the availability of a reply lookup service.

        :return: ``true`` if reply lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_reply_admin(self):
        """Tests if searching for replies is available.

        :return: ``true`` if reply search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_reply_notification(self):
        """Tests if reply notification is available.

        :return: ``true`` if reply notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_forum_lookup(self):
        """Tests for the availability of an forum lookup service.

        :return: ``true`` if forum lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_forum_query(self):
        """Tests if querying forums is available.

        :return: ``true`` if forum query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_forum_search(self):
        """Tests if searching for forums is available.

        :return: ``true`` if forum search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_forum_admin(self):
        """Tests for the availability of a forum administrative service for creating and deleting forums.

        :return: ``true`` if forum administration is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_forum_notification(self):
        """Tests for the availability of a forum notification service.

        :return: ``true`` if forum notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_forum_hierarchy(self):
        """Tests for the availability of a forum hierarchy traversal service.

        :return: ``true`` if forum hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_forum_hierarchy_design(self):
        """Tests for the availability of a forum hierarchy design service.

        :return: ``true`` if forum hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_forum_batch(self):
        """Tests if forum batch service is available.

        :return: ``true`` if forum batch service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_post_record_types(self):
        """Gets the supported ``Post`` record types.

        :return: a list containing the supported post record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    post_record_types = property(fget=get_post_record_types)

    def supports_post_record_type(self, post_record_type):
        """Tests if the given ``Post`` record type is supported.

        :param post_record_type: a ``Type`` indicating a ``Post`` record type
        :type post_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``post_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_post_search_record_types(self):
        """Gets the supported post search record types.

        :return: a list containing the supported post search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    post_search_record_types = property(fget=get_post_search_record_types)

    def supports_post_search_record_type(self, post_search_record_type):
        """Tests if the given post search record type is supported.

        :param post_search_record_type: a ``Type`` indicating a post record type
        :type post_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``post_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_reply_record_types(self):
        """Gets the supported ``Reply`` record types.

        :return: a list containing the supported reply record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    reply_record_types = property(fget=get_reply_record_types)

    def supports_reply_record_type(self, reply_record_type):
        """Tests if the given ``Reply`` record type is supported.

        :param reply_record_type: a ``Type`` indicating a ``Reply`` record type
        :type reply_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``reply_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_reply_search_record_types(self):
        """Gets the supported reply search record types.

        :return: a list containing the supported reply search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    reply_search_record_types = property(fget=get_reply_search_record_types)

    def supports_reply_search_record_type(self, reply_search_record_type):
        """Tests if the given reply search record type is supported.

        :param reply_search_record_type: a ``Type`` indicating a reply record type
        :type reply_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``reply_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_forum_record_types(self):
        """Gets the supported ``Forum`` record types.

        :return: a list containing the supported forum record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    forum_record_types = property(fget=get_forum_record_types)

    def supports_forum_record_type(self, forum_record_type):
        """Tests if the given ``Forum`` record type is supported.

        :param forum_record_type: a ``Type`` indicating a ``Forum`` record type
        :type forum_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``forum_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_forum_search_record_types(self):
        """Gets the supported forum search record types.

        :return: a list containing the supported forum search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    forum_search_record_types = property(fget=get_forum_search_record_types)

    def supports_forum_search_record_type(self, forum_search_record_type):
        """Tests if the given forum search record type is supported.

        :param forum_search_record_type: a ``Type`` indicating a forum record type
        :type forum_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``forum_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class ForumManager(osid.OsidManager, osid.OsidSession, ForumProfile):

    def get_post_lookup_session(self):
        """Gets the ``OsidSession`` associated with the post lookup service.

        :return: a ``PostLookupSession``
        :rtype: ``osid.forum.PostLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_post_query_session(self):
        """Gets the ``OsidSession`` associated with the post query service.

        :return: a ``PostQuerySession``
        :rtype: ``osid.forum.PostQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_post_search_session(self):
        """Gets the ``OsidSession`` associated with the post search service.

        :return: a ``PostSearchSession``
        :rtype: ``osid.forum.PostSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_post_admin_session(self):
        """Gets the ``OsidSession`` associated with the post administrative service.

        :return: a ``PostAdminSession``
        :rtype: ``osid.forum.PostAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_post_forum_session(self):
        """Gets the session for retrieving post to forum mappings.

        :return: a ``PostForumSession``
        :rtype: ``osid.forum.PostForumSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_forum()`` is ``false``

        """
        raise UNIMPLEMENTED()

    post_forum_session = property(fget=get_post_forum_session)

    def get_post_forum_assignment_session(self):
        """Gets the session for assigning post to forum mappings.

        :return: a ``PostForumAssignmentSession``
        :rtype: ``osid.forum.PostForumAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_post_forum_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_reply_lookup_session(self):
        """Gets the ``OsidSession`` associated with the reply lookup service.

        :return: a ``ReplyLookupSession``
        :rtype: ``osid.forum.ReplyLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_reply_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_reply_admin_session(self):
        """Gets the ``OsidSession`` associated with the reply administration service.

        :return: a ``ReplyAdminSession``
        :rtype: ``osid.forum.ReplyAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_reply_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_forum_lookup_session(self):
        """Gets the ``OsidSession`` associated with the forum lookup service.

        :return: a ``ForumLookupSession``
        :rtype: ``osid.forum.ForumLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    forum_lookup_session = property(fget=get_forum_lookup_session)

    def get_forum_query_session(self):
        """Gets the ``OsidSession`` associated with the forum query service.

        :return: a ``ForumQuerySession``
        :rtype: ``osid.forum.ForumQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    forum_query_session = property(fget=get_forum_query_session)

    def get_forum_search_session(self):
        """Gets the ``OsidSession`` associated with the forum search service.

        :return: a ``ForumSearchSession``
        :rtype: ``osid.forum.ForumSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    forum_search_session = property(fget=get_forum_search_session)

    def get_forum_admin_session(self):
        """Gets the ``OsidSession`` associated with the forum administrative service.

        :return: a ``ForumAdminSession``
        :rtype: ``osid.forum.ForumAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_forum_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the forum hierarchy service.

        :return: a ``ForumHierarchySession``
        :rtype: ``osid.forum.ForumHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    forum_hierarchy_session = property(fget=get_forum_hierarchy_session)

    def get_forum_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the forum hierarchy design service.

        :return: a ``ForumHierarchyDesignSession``
        :rtype: ``osid.forum.ForumHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    forum_hierarchy_design_session = property(fget=get_forum_hierarchy_design_session)

    def get_forum_batch_manager(self):
        """Gets a ``ForumBatchManager``.

        :return: a ``ForumBatchManager``
        :rtype: ``osid.forum.batch.ForumBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    forum_batch_manager = property(fget=get_forum_batch_manager)


##
# The following methods are from osid.forum.ForumLookupSession

    def can_lookup_forums(self):
        """Tests if this user can perform ``Forum`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_forum_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_forum_view(self):
        """A complete view of the ``Forum`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_forum(self, forum_id):
        """Gets the ``Forum`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Forum`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Forum`` and retained for compatibility.

        :param forum_id: ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :return: the forum
        :rtype: ``osid.forum.Forum``
        :raise: ``NotFound`` -- ``forum_id`` not found
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_forums_by_ids(self, forum_ids):
        """Gets a ``ForumList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the forums
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Forums`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param forum_ids: the list of ``Ids`` to retrieve
        :type forum_ids: ``osid.id.IdList``
        :return: the returned ``Forum`` list
        :rtype: ``osid.forum.ForumList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``forum_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_forums_by_genus_type(self, forum_genus_type):
        """Gets a ``ForumList`` corresponding to the given forum genus ``Type`` which does not include forums of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known forums or
        an error results. Otherwise, the returned list may contain only
        those forums that are accessible through this session.

        :param forum_genus_type: a forum genus type
        :type forum_genus_type: ``osid.type.Type``
        :return: the returned ``Forum`` list
        :rtype: ``osid.forum.ForumList``
        :raise: ``NullArgument`` -- ``forum_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_forums_by_parent_genus_type(self, forum_genus_type):
        """Gets a ``ForumList`` corresponding to the given forum genus ``Type`` and include any additional forums with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known forums or
        an error results. Otherwise, the returned list may contain only
        those forums that are accessible through this session.

        :param forum_genus_type: a forum genus type
        :type forum_genus_type: ``osid.type.Type``
        :return: the returned ``Forum`` list
        :rtype: ``osid.forum.ForumList``
        :raise: ``NullArgument`` -- ``forum_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_forums_by_record_type(self, forum_record_type):
        """Gets a ``ForumList`` containing the given forum record ``Type``.
        In plenary mode, the returned list contains all known forums or
        an error results. Otherwise, the returned list may contain only
        those forums that are accessible through this session.

        :param forum_record_type: a forum record type
        :type forum_record_type: ``osid.type.Type``
        :return: the returned ``Forum`` list
        :rtype: ``osid.forum.ForumList``
        :raise: ``NullArgument`` -- ``forum_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_forums_by_provider(self, resource_id):
        """Gets a ``ForumList`` for the given provider ````.
        In plenary mode, the returned list contains all known forums or
        an error results. Otherwise, the returned list may contain only
        those forums that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Forum`` list
        :rtype: ``osid.forum.ForumList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_forums(self):
        """Gets all ``Forums``.
        In plenary mode, the returned list contains all known forums or
        an error results. Otherwise, the returned list may contain only
        those forums that are accessible through this session.

        :return: a list of ``Forums``
        :rtype: ``osid.forum.ForumList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    forums = property(fget=get_forums)


##
# The following methods are from osid.forum.ForumQuerySession

    def can_search_forums(self):
        """Tests if this user can perform ``Forum`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_forum_query(self):
        """Gets a forum query.

        :return: the forum query
        :rtype: ``osid.forum.ForumQuery``

        """
        raise UNIMPLEMENTED()

    forum_query = property(fget=get_forum_query)

    def get_forums_by_query(self, forum_query):
        """Gets a list of ``Forums`` matching the given search.

        :param forum_query: the forum query
        :type forum_query: ``osid.forum.ForumQuery``
        :return: the returned ``ForumList``
        :rtype: ``osid.forum.ForumList``
        :raise: ``NullArgument`` -- ``forum_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``forum_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.forum.ForumSearchSession

    def get_forum_search(self):
        """Gets a forum search.

        :return: the forum search
        :rtype: ``osid.forum.ForumSearch``

        """
        raise UNIMPLEMENTED()

    forum_search = property(fget=get_forum_search)

    def get_forum_search_order(self):
        """Gets a forum search order.
        The ``ForumSearchOrder`` is supplied to a ``ForumSearch`` to
        specify the ordering of results.

        :return: the forum search order
        :rtype: ``osid.forum.ForumSearchOrder``

        """
        raise UNIMPLEMENTED()

    forum_search_order = property(fget=get_forum_search_order)

    def get_forums_by_search(self, forum_query, forum_search):
        """Gets the search results matching the given search.

        :param forum_query: the forum query
        :type forum_query: ``osid.forum.ForumQuery``
        :param forum_search: the forum search
        :type forum_search: ``osid.forum.ForumSearch``
        :return: the forum search results
        :rtype: ``osid.forum.ForumSearchResults``
        :raise: ``NullArgument`` -- ``forum_query`` or ``forum_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``forum_query`` or ``forum_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_forum_query_from_inspector(self, forum_query_inspector):
        """Gets a forum query from an inspector.
        The inspector is available from an ``ForumSearchResults``.

        :param forum_query_inspector: a query inspector
        :type forum_query_inspector: ``osid.forum.ForumQueryInspector``
        :return: the forum query
        :rtype: ``osid.forum.ForumQuery``
        :raise: ``NullArgument`` -- ``forum_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``forum_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.forum.ForumAdminSession

    def can_create_forums(self):
        """Tests if this user can create ``Forums``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Forum``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Forum`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_forum_with_record_types(self, forum_record_types):
        """Tests if this user can create a single ``Forum`` using the desired record types.
        While ``ForumManager.getForumRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Forum``.
        Providing an empty array tests if a ``Forum`` can be created
        with no records.

        :param forum_record_types: array of forum record types
        :type forum_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Forum`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``forum_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_forum_form_for_create(self, forum_record_types):
        """Gets the forum form for creating new forums.
        A new form should be requested for each create transaction.

        :param forum_record_types: array of forum record types
        :type forum_record_types: ``osid.type.Type[]``
        :return: the forum form
        :rtype: ``osid.forum.ForumForm``
        :raise: ``NullArgument`` -- ``forum_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_forum(self, forum_form):
        """Creates a new ``Forum``.

        :param forum_form: the form for this ``Forum``
        :type forum_form: ``osid.forum.ForumForm``
        :return: the new ``Forum``
        :rtype: ``osid.forum.Forum``
        :raise: ``IllegalState`` -- ``forum_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``forum_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``forum_form`` did not originate from ``get_forum_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_forums(self):
        """Tests if this user can update ``Forums``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Forum``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Forum`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_forum_form_for_update(self, forum_id):
        """Gets the forum form for updating an existing forum.
        A new forum form should be requested for each update
        transaction.

        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :return: the forum form
        :rtype: ``osid.forum.ForumForm``
        :raise: ``NotFound`` -- ``forum_id`` is not found
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_forum(self, forum_form):
        """Updates an existing forum.

        :param forum_form: the form containing the elements to be updated
        :type forum_form: ``osid.forum.ForumForm``
        :raise: ``IllegalState`` -- ``forum_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``forum_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``forum_form`` did not originate from ``get_forum_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_forums(self):
        """Tests if this user can delete ``Forums`` A return of true does not guarantee successful authorization.
        A return of false indicates that it is known deleting a
        ``Forum`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Forum`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_forum(self, forum_id):
        """Deletes a ``Forum``.

        :param forum_id: the ``Id`` of the ``Forum`` to remove
        :type forum_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``forum_id`` not found
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_forum_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Forums``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Forum`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_forum(self, forum_id, alias_id):
        """Adds an ``Id`` to a ``Forum`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Forum`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another forum, it is
        reassigned to the given forum ``Id``.

        :param forum_id: the ``Id`` of a ``Forum``
        :type forum_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``forum_id`` not found
        :raise: ``NullArgument`` -- ``forum_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.forum.ForumNotificationSession

    def can_register_for_forum_notifications(self):
        """Tests if this user can register for ``Forum`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_forums(self):
        """Register for notifications of new forums.
        ``ForumReceiver.newForum()`` is invoked when a new ``Forum`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_forum_ancestors(self, forum_id):
        """Registers for notification of an updated hierarchy structure that introduces a new ancestor of the specified forum.
        ``ForumReceiver.newAncestorForum()`` is invoked when the
        specified forum node gets a new ancestor.

        :param forum_id: the ``Id`` of the ``Forum`` node to monitor
        :type forum_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_forum_descendants(self, forum_id):
        """Registers for notification of an updated hierarchy structure that introduces a new descendant of the specified forum.
        ``ForumReceiver.newDescendantForum()`` is invoked when the
        specified forum node gets a new descendant.

        :param forum_id: the ``Id`` of the ``Forum`` node to monitor
        :type forum_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_forums(self):
        """Registers for notification of updated forums.
        ``ForumReceiver.changedForum()`` is invoked when a forum is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_forum(self, forum_id):
        """Registers for notification of an updated forum.
        ``ForumReceiver.changedForum()`` is invoked when the specified
        forum is changed.

        :param forum_id: the ``Id`` of the ``Forum`` to monitor
        :type forum_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_forums(self):
        """Registers for notification of deleted forums.
        ``ForumReceiver.deletedForum()`` is invoked when a forum is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_forum(self, forum_id):
        """Registers for notification of a deleted forum.
        ``ForumReceiver.deletedForum()`` is invoked when the specified
        forum is deleted.

        :param forum_id: the ``Id`` of the ``Forum`` to monitor
        :type forum_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_forum_ancestors(self, forum_id):
        """Registers for notification of an updated hierarchy structure that removes an ancestor of the specified forum ``ForumReceiver.
        deletedAncestor()`` is invoked when the specified forum node
        loses an ancestor.

        :param forum_id: the ``Id`` of the ``Forum`` to monitor
        :type forum_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_forum_descendants(self, forum_id):
        """Registers for notification of an updated hierarchy structure that removes a descendant of the specified forum.
        ``ForumReceiver.deletedDescendant()`` is invoked when the
        specified forum node loses a descendant.

        :param forum_id: the ``Id`` of the ``Forum`` to monitor
        :type forum_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.forum.ForumHierarchySession

    def get_forum_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    forum_hierarchy_id = property(fget=get_forum_hierarchy_id)

    def get_forum_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    forum_hierarchy = property(fget=get_forum_hierarchy)

    def can_access_forum_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_forum_ids(self):
        """Gets the root forum ``Ids`` in this hierarchy.

        :return: the root forum ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_forum_ids = property(fget=get_root_forum_ids)

    def get_root_forums(self):
        """Gets the root forums in the forum hierarchy.
        A node with no parents is an orphan. While all forum ``Ids`` are
        known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        :return: the root forums
        :rtype: ``osid.forum.ForumList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_forums = property(fget=get_root_forums)

    def has_parent_forums(self, forum_id):
        """Tests if the ``Forum`` has any parents.

        :param forum_id: a forum ``Id``
        :type forum_id: ``osid.id.Id``
        :return: ``true`` if the forum has parents, f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``forum_id`` is not found
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_forum(self, id_, forum_id):
        """Tests if an ``Id`` is a direct parent of forum.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param forum_id: the ``Id`` of a forum
        :type forum_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``forum_id,`` f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``forum_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_forum_ids(self, forum_id):
        """Gets the parent ``Ids`` of the given forum.

        :param forum_id: a forum ``Id``
        :type forum_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the forum
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``forum_id`` is not found
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_forums(self, forum_id):
        """Gets the parent forums of the given ``id``.

        :param forum_id: the ``Id`` of the ``Forum`` to query
        :type forum_id: ``osid.id.Id``
        :return: the parent forums of the ``id``
        :rtype: ``osid.forum.ForumList``
        :raise: ``NotFound`` -- a ``Forum`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_forum(self, id_, forum_id):
        """Tests if an ``Id`` is an ancestor of a forum.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param forum_id: the ``Id`` of a forum
        :type forum_id: ``osid.id.Id``
        :return: ``tru`` e if this ``id`` is an ancestor of ``forum_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``forum_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_forums(self, forum_id):
        """Tests if a forum has any children.

        :param forum_id: a forum ``Id``
        :type forum_id: ``osid.id.Id``
        :return: ``true`` if the ``forum_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``forum_id`` is not found
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_forum(self, id_, forum_id):
        """Tests if a forum is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param forum_id: the ``Id`` of a forum
        :type forum_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``forum_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``forum_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_forum_ids(self, forum_id):
        """Gets the child ``Ids`` of the given forum.

        :param forum_id: the ``Id`` to query
        :type forum_id: ``osid.id.Id``
        :return: the children of the forum
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``forum_id`` is not found
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_forums(self, forum_id):
        """Gets the child forums of the given ``id``.

        :param forum_id: the ``Id`` of the ``Forum`` to query
        :type forum_id: ``osid.id.Id``
        :return: the child forums of the ``id``
        :rtype: ``osid.forum.ForumList``
        :raise: ``NotFound`` -- a ``Forum`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_forum(self, id_, forum_id):
        """Tests if an ``Id`` is a descendant of a forum.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param forum_id: the ``Id`` of a forum
        :type forum_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``forum_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``forum_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_forum_node_ids(self, forum_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given forum.

        :param forum_id: the ``Id`` to query
        :type forum_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a forum node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``forum_id`` is not found
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_forum_nodes(self, forum_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given forum.

        :param forum_id: the ``Id`` to query
        :type forum_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a forum node
        :rtype: ``osid.forum.ForumNode``
        :raise: ``NotFound`` -- ``forum_id`` is not found
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.forum.ForumHierarchyDesignSession

    def can_modify_forum_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_forum(self, forum_id):
        """Adds a root forum.

        :param forum_id: the ``Id`` of a forum
        :type forum_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``forum_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``forum_id`` is not found
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_forum(self, forum_id):
        """Removes a root forum.

        :param forum_id: the ``Id`` of a forum
        :type forum_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``forum_id`` is not a root
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_forum(self, forum_id, child_id):
        """Adds a child to a forum.

        :param forum_id: the ``Id`` of a forum
        :type forum_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``forum_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``forum_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``forum_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_forum(self, forum_id, child_id):
        """Removes a child from a forum.

        :param forum_id: the ``Id`` of a forum
        :type forum_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``forum_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``forum_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_forums(self, forum_id):
        """Removes all children from a forum.

        :param forum_id: the ``Id`` of a forum
        :type forum_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``forum_id`` not found
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class ForumProxyManager(osid.OsidProxyManager, ForumProfile):

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_forum_batch_proxy_manager(self):
        """Gets a ``ForumBatchProxyManager``.

        :return: a ``ForumBatchProxyManager``
        :rtype: ``osid.forum.batch.ForumBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_forum_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    forum_batch_proxy_manager = property(fget=get_forum_batch_proxy_manager)



class Forum(osid.OsidCatalog, osid.OsidSession):

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.forum.PostLookupSession

    def get_forum_id(self):
        """Gets the ``Forum``  ``Id`` associated with this session.

        :return: the ``Forum Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    forum_id = property(fget=get_forum_id)

    def get_forum(self):
        """Gets the ``Forum`` associated with this session.

        :return: the forum
        :rtype: ``osid.forum.Forum``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    forum = property(fget=get_forum)

    def can_lookup_posts(self):
        """Tests if this user can perform ``Post`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_post_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_post_view(self):
        """A complete view of the ``Post`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_forum_view(self):
        """Federates the view for methods in this session.
        A federated view will include posts in forums which are children
        of this forum in the forum hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_forum_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts retrievals to this forum only.



        """
        raise UNIMPLEMENTED()

    def get_post(self, post_id):
        """Gets the ``Post`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Post`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Post`` and retained for compatibility.

        :param post_id: ``Id`` of the ``Post``
        :type post_id: ``osid.id.Id``
        :return: the post
        :rtype: ``osid.forum.Post``
        :raise: ``NotFound`` -- ``post_id`` not found
        :raise: ``NullArgument`` -- ``post_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_posts_by_ids(self, post_ids):
        """Gets a ``PostList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the posts
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Posts`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param post_ids: the list of ``Ids`` to retrieve
        :type post_ids: ``osid.id.IdList``
        :return: the returned ``Post`` list
        :rtype: ``osid.forum.PostList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``post_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_posts_by_genus_type(self, post_genus_type):
        """Gets a ``PostList`` corresponding to the given post genus ``Type`` which does not include posts of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known posts or
        an error results. Otherwise, the returned list may contain only
        those posts that are accessible through this session.

        :param post_genus_type: a post genus type
        :type post_genus_type: ``osid.type.Type``
        :return: the returned ``Post`` list
        :rtype: ``osid.forum.PostList``
        :raise: ``NullArgument`` -- ``post_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_posts_by_parent_genus_type(self, post_genus_type):
        """Gets a ``PostList`` corresponding to the given post genus ``Type`` and include any additional posts with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known posts or
        an error results. Otherwise, the returned list may contain only
        those posts that are accessible through this session.

        :param post_genus_type: a post genus type
        :type post_genus_type: ``osid.type.Type``
        :return: the returned ``Post`` list
        :rtype: ``osid.forum.PostList``
        :raise: ``NullArgument`` -- ``post_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_posts_by_record_type(self, post_record_type):
        """Gets a ``PostList`` containing the given post record ``Type``.
        In plenary mode, the returned list contains all known posts or
        an error results. Otherwise, the returned list may contain only
        those posts that are accessible through this session.

        :param post_record_type: a post record type
        :type post_record_type: ``osid.type.Type``
        :return: the returned ``Post`` list
        :rtype: ``osid.forum.PostList``
        :raise: ``NullArgument`` -- ``post_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_posts_by_date(self, from_, to):
        """Gets a ``PostList`` in the given date range inclusive.
        In plenary mode, the returned list contains all known posts or
        an error results. Otherwise, the returned list may contain only
        those posts that are accessible through this session.

        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Post`` list
        :rtype: ``osid.forum.PostList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_posts_for_poster(self, resource_id):
        """Gets a ``PostList`` for the given poster.
        In plenary mode, the returned list contains all known posts or
        an error results. Otherwise, the returned list may contain only
        those posts that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Post`` list
        :rtype: ``osid.forum.PostList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_posts_by_date_for_poster(self, resource_id, from_, to):
        """Gets a ``PostList`` by the given poster and in the given date range inclusive.
        In plenary mode, the returned list contains all known posts or
        an error results. Otherwise, the returned list may contain only
        those posts that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Post`` list
        :rtype: ``osid.forum.PostList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_posts(self):
        """Gets all ``Posts``.
        In plenary mode, the returned list contains all known posts or
        an error results. Otherwise, the returned list may contain only
        those posts that are accessible through this session.

        :return: a list of ``Posts``
        :rtype: ``osid.forum.PostList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    posts = property(fget=get_posts)


##
# The following methods are from osid.forum.PostQuerySession

    def can_search_posts(self):
        """Tests if this user can perform ``Post`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_post_query(self):
        """Gets a post query.

        :return: the post query
        :rtype: ``osid.forum.PostQuery``

        """
        raise UNIMPLEMENTED()

    post_query = property(fget=get_post_query)

    def get_posts_by_query(self, post_query):
        """Gets a list of ``Posts`` matching the given search.

        :param post_query: the post query
        :type post_query: ``osid.forum.PostQuery``
        :return: the returned ``PostList``
        :rtype: ``osid.forum.PostList``
        :raise: ``NullArgument`` -- ``post_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``post_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.forum.PostSearchSession

    def get_post_search(self):
        """Gets a post search.

        :return: the post search
        :rtype: ``osid.forum.PostSearch``

        """
        raise UNIMPLEMENTED()

    post_search = property(fget=get_post_search)

    def get_post_search_order(self):
        """Gets a post search order.
        The ``PostSearchOrder`` is supplied to a ``PostSearch`` to
        specify the ordering of results.

        :return: the post search order
        :rtype: ``osid.forum.PostSearchOrder``

        """
        raise UNIMPLEMENTED()

    post_search_order = property(fget=get_post_search_order)

    def get_posts_by_search(self, post_query, post_search):
        """Gets the search results matching the given search.

        :param post_query: the post query
        :type post_query: ``osid.forum.PostQuery``
        :param post_search: the post search
        :type post_search: ``osid.forum.PostSearch``
        :return: the post search results
        :rtype: ``osid.forum.PostSearchResults``
        :raise: ``NullArgument`` -- ``post_query`` or ``post_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``post_query`` or ``post_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_post_query_from_inspector(self, post_query_inspector):
        """Gets an entry query from an inspector.
        The inspector is available from an ``PostSearchResults``.

        :param post_query_inspector: a query inspector
        :type post_query_inspector: ``osid.forum.PostQueryInspector``
        :return: the entry query
        :rtype: ``osid.forum.PostQuery``
        :raise: ``NullArgument`` -- ``post_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``post_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.forum.PostAdminSession

    def can_create_posts(self):
        """Tests if this user can create ``Posts``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Post``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Post`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_post_with_record_types(self, post_record_types):
        """Tests if this user can create a single ``Post`` using the desired record types.
        While ``ForumManager.getPostRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Post``.
        Providing an empty array tests if a ``Post`` can be created with
        no records.

        :param post_record_types: array of post record types
        :type post_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Post`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``post_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_post_form_for_create(self, post_record_types):
        """Gets the post form for creating new posts.
        A new form should be requested for each create transaction.

        :param post_record_types: array of post record types
        :type post_record_types: ``osid.type.Type[]``
        :return: the post form
        :rtype: ``osid.forum.PostForm``
        :raise: ``NullArgument`` -- ``post_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_post(self, post_form):
        """Creates a new ``Post``.

        :param post_form: the form for this ``Post``
        :type post_form: ``osid.forum.PostForm``
        :return: the new ``Post``
        :rtype: ``osid.forum.Post``
        :raise: ``IllegalState`` -- ``post_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``post_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``post_form`` did not originate from ``get_post_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_posts(self):
        """Tests if this user can update ``Posts``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Post``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Post`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_post_form_for_update(self, post_id):
        """Gets the post form for updating an existing post.
        A new post form should be requested for each update transaction.

        :param post_id: the ``Id`` of the ``Post``
        :type post_id: ``osid.id.Id``
        :return: the post form
        :rtype: ``osid.forum.PostForm``
        :raise: ``NotFound`` -- ``post_id`` is not found
        :raise: ``NullArgument`` -- ``post_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_post(self, post_form):
        """Updates an existing post.

        :param post_form: the form containing the elements to be updated
        :type post_form: ``osid.forum.PostForm``
        :raise: ``IllegalState`` -- ``post_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``post_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``post_form`` did not originate from ``get_post_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_posts(self):
        """Tests if this user can delete ``Posts`` A return of true does not guarantee successful authorization.
        A return of false indicates that it is known deleting a ``Post``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Post`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_post(self, post_id):
        """Deletes a ``Post``.

        :param post_id: the ``Id`` of the ``Post`` to remove
        :type post_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``post_id`` not found
        :raise: ``NullArgument`` -- ``post_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_post_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Posts``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Post`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_post(self, post_id, alias_id):
        """Adds an ``Id`` to a ``Post`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Post`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another post, it is
        reassigned to the given post ``Id``.

        :param post_id: the ``Id`` of a ``Post``
        :type post_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``post_id`` not found
        :raise: ``NullArgument`` -- ``post_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.forum.PostNotificationSession

    def can_register_for_post_notifications(self):
        """Tests if this user can register for ``Post`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_posts(self):
        """Register for notifications of new posts.
        ``PostReceiver.newPost()`` is invoked when a new ``Post`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_posts_for_poster(self, resource_id):
        """Register for notifications of new posts for the given poster resource ``Id``.
        ``PostReceiver.newPost()`` is invoked when a new ``Post`` is
        created.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_posts(self):
        """Registers for notification of updated posts.
        ``PostReceiver.changedPost()`` is invoked when a post is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_posts_for_poster(self, resource_id):
        """Register for notifications of changed posts for the given poster resource ``Id``.
        ``PostReceiver.changedPost()`` is invoked when a ``Post`` for
        the given agent is updated.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_post(self, post_id):
        """Registers for notification of an updated post.
        ``PostReceiver.changedPost()`` is invoked when the specified
        post is changed.

        :param post_id: the ``Id`` of the ``Post`` to monitor
        :type post_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``post_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_posts(self):
        """Registers for notification of deleted posts.
        ``PostReceiver.deletedPost()`` is invoked when a post is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_posts_for_poster(self, resource_id):
        """Register for notifications of deleted posts for the given poster resource ``Id``.
        ``PostReceiver.deletedPost()`` is invoked when a ``Post`` for
        the given agent is removed.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_post(self, post_id):
        """Registers for notification of a deleted post.
        ``PostReceiver.deletedPost()`` is invoked when the specified
        post is deleted.

        :param post_id: the ``Id`` of the ``Post`` to monitor
        :type post_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``post_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.forum.PostForumSession

    def can_lookup_post_forum_mappings(self):
        """Tests if this user can perform lookups of post/forum mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intendedas a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_forum_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_forum_view(self):
        """A complete view of the ``Post`` and ``Forum`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_post_ids_by_forum(self, forum_id):
        """Gets the list of Post Ids associated with a ``Forum``.

        :param forum_id: ``Id`` of a ``Forum``.
        :type forum_id: ``osid.id.Id``
        :return: list of related post ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``forum_id`` is not found
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_posts_by_forum(self, forum_id):
        """Gets the list of ``Posts`` associated with a ``Forum``.

        :param forum_id: ``Id`` of a ``Forum``
        :type forum_id: ``osid.id.Id``
        :return: list of related posts
        :rtype: ``osid.forum.PostList``
        :raise: ``NotFound`` -- ``forum_id`` is not found
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_post_ids_by_forums(self, forum_ids):
        """Gets the list of ``Post Ids`` corresponding to a list of ``Forum`` objects.

        :param forum_ids: list of forum ``Ids``
        :type forum_ids: ``osid.id.IdList``
        :return: list of post ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``forum_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_posts_by_forums(self, forum_ids):
        """Gets the list of ``Posts`` corresponding to a list of ``Forums``.

        :param forum_ids: list of forum ``Ids``
        :type forum_ids: ``osid.id.IdList``
        :return: list of posts
        :rtype: ``osid.forum.PostList``
        :raise: ``NullArgument`` -- ``forum_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_forum_ids_by_post(self, post_id):
        """Gets the list of ``Forum``  ``Ids`` mapped to a ``Post``.

        :param post_id: ``Id`` of a ``Post``
        :type post_id: ``osid.id.Id``
        :return: list of forum ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``post_id`` is not found
        :raise: ``NullArgument`` -- ``post_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_forums_by_post(self, post_id):
        """Gets the list of ``Forum`` objects mapped to a ``Post``.

        :param post_id: ``Id`` of a ``Post``
        :type post_id: ``osid.id.Id``
        :return: list of forums
        :rtype: ``osid.forum.ForumList``
        :raise: ``NotFound`` -- ``post_id`` is not found
        :raise: ``NullArgument`` -- ``post_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.forum.PostForumAssignmentSession

    def can_assign_posts(self):
        """Tests if this user can alter post/forum mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_posts_to_forum(self, forum_id):
        """Tests if this user can alter post/forum mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_forum_ids(self, forum_id):
        """Gets a list of forums including and under the given forum node in which any post can be assigned.

        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :return: list of assignable forum ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_forum_ids_for_post(self, forum_id, post_id):
        """Gets a list of forums including and under the given forum node in which a specific post can be assigned.

        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :param post_id: the ``Id`` of the ``Post``
        :type post_id: ``osid.id.Id``
        :return: list of assignable forum ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``forum_id`` or ``post_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_post_to_forum(self, post_id, forum_id):
        """Adds an existing ``Post`` to a ``Forum``.

        :param post_id: the ``Id`` of the ``Post``
        :type post_id: ``osid.id.Id``
        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``post_id`` is already assigned to ``forum_id``
        :raise: ``NotFound`` -- ``post_id`` or ``forum_id`` not found
        :raise: ``NullArgument`` -- ``post_id`` or ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_post_from_forum(self, post_id, forum_id):
        """Removes a ``Post`` from a ``Forum``.

        :param post_id: the ``Id`` of the ``Post``
        :type post_id: ``osid.id.Id``
        :param forum_id: the ``Id`` of the ``Forum``
        :type forum_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``post_id`` or ``forum_id`` not found or ``post_id`` not assigned to ``forum_id``
        :raise: ``NullArgument`` -- ``post_id`` or ``forum_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.forum.PostSmartForumSession

    def can_manage_smart_forums(self):
        """Tests if this user can manage smart forums.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart forum management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_post_query(self, post_query):
        """Applies a post query to this forum.

        :param post_query: the post query
        :type post_query: ``osid.forum.PostQuery``
        :raise: ``NullArgument`` -- ``post_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``post_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_post_query(self):
        """Gets a post query inspector for this forum.

        :return: the post query inspector
        :rtype: ``osid.forum.PostQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_post_sequencing(self, post_search_order):
        """Applies a post search order to this forum.

        :param post_search_order: the post search order
        :type post_search_order: ``osid.forum.PostSearchOrder``
        :raise: ``NullArgument`` -- ``post_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``post_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.forum.ReplyLookupSession

    def can_lookup_replies(self):
        """Tests if this user can lookup replies.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer these
        operations.

        :return: ``false`` if reply lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_reply_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_reply_view(self):
        """A complete view of the ``Reply`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_sequestered_reply_view(self):
        """The returns from the lookup methods omit sequestered replies."""
        raise UNIMPLEMENTED()

    def use_unsequestered_reply_view(self):
        """All replies are returned including sequestered replies."""
        raise UNIMPLEMENTED()

    def get_reply(self, reply_id):
        """Gets the ``Reply`` specified by its ``Id``.

        :param reply_id: the ``Id`` of the ``Reply`` to retrieve
        :type reply_id: ``osid.id.Id``
        :return: the returned ``Reply``
        :rtype: ``osid.forum.Reply``
        :raise: ``NotFound`` -- no ``Reply`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``reply_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_replies_by_ids(self, reply_ids):
        """Gets a ``ReplyList`` corresponding to the given ``IdList``.

        :param reply_ids: the list of ``Ids`` to retrieve
        :type reply_ids: ``osid.id.IdList``
        :return: the returned ``Reply list``
        :rtype: ``osid.forum.ReplyList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``reply_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_replies_by_genus_type(self, reply_genus_type):
        """Gets a ``ReplyList`` corresponding to the given reply genus ``Type`` which does not include replies of genus types derived from the specified ``Type``.

        :param reply_genus_type: a reply genus type
        :type reply_genus_type: ``osid.type.Type``
        :return: the returned ``Reply`` list
        :rtype: ``osid.forum.ReplyList``
        :raise: ``NullArgument`` -- ``reply_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_replies_by_parent_genus_type(self, reply_genus_type):
        """Gets a ``ReplyList`` corresponding to the given reply genus ``Type`` and include any additional replies with genus types derived from the specified ``Type``.

        :param reply_genus_type: a reply genus type
        :type reply_genus_type: ``osid.type.Type``
        :return: the returned ``Post`` list
        :rtype: ``osid.forum.ReplyList``
        :raise: ``NullArgument`` -- ``post_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_replies_by_record_type(self, reply_record_type):
        """Gets a ``ReplyList`` containing the given reply record ``Type``.

        :param reply_record_type: a reply record type
        :type reply_record_type: ``osid.type.Type``
        :return: the returned ``Post`` list
        :rtype: ``osid.forum.ReplyList``
        :raise: ``NullArgument`` -- ``reply_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_replies_by_date(self, from_, to):
        """Gets a list of all replies corresponding to the given date range inclusive ````.

        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``ReplyList``
        :rtype: ``osid.forum.ReplyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_replies_for_post(self, post_id):
        """Gets a list of all replies corresponding to a post ``Id``.

        :param post_id: the ``Id`` of the post
        :type post_id: ``osid.id.Id``
        :return: the returned ``ReplyList``
        :rtype: ``osid.forum.ReplyList``
        :raise: ``NullArgument`` -- ``post_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_replies_by_date_for_post(self, post_id, from_, to):
        """Gets a list of all replies corresponding to post ``Id`` in the given daterange inclusive.

        :param post_id: the ``Id`` of the post
        :type post_id: ``osid.id.Id``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``ReplyList``
        :rtype: ``osid.forum.ReplyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``post_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_replies_for_poster(self, resource_id):
        """Gets a list of all replies corresponding to a poster.

        :param resource_id: the resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``ReplyList``
        :rtype: ``osid.forum.ReplyList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_replies_by_date_for_poster(self, resource_id, from_, to):
        """Gets a list of all replies corresponding to a post ``Id`` for the given poster within the date range inclusive.

        :param resource_id: the resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``ReplyList``
        :rtype: ``osid.forum.ReplyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_replies_for_post_and_poster(self, post_id, resource_id):
        """Gets a list of all replies corresponding to a post ``Id`` and poster.

        :param post_id: the ``Id`` of the post
        :type post_id: ``osid.id.Id``
        :param resource_id: the resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``ReplyList``
        :rtype: ``osid.forum.ReplyList``
        :raise: ``NullArgument`` -- ``post_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_replies_by_date_for_post_and_poster(self, post_id, resource_id, from_, to):
        """Gets a list of all replies corresponding to a post ``Id`` and poster within the given daterange incluisve.

        :param post_id: the ``Id`` of the post
        :type post_id: ``osid.id.Id``
        :param resource_id: the resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``ReplyList``
        :rtype: ``osid.forum.ReplyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``post_id, resource_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_replies(self):
        """Gets a list of all replies.

        :return: the returned ``ReplyList``
        :rtype: ``osid.forum.ReplyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    replies = property(fget=get_replies)


##
# The following methods are from osid.forum.ReplyAdminSession

    def can_create_replies(self):
        """Tests if this user can create hournal entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Reply``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Reply`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_reply_with_record_types(self, reply_record_types):
        """Tests if this user can create a single ``Reply`` using the desired record types.
        While ``ForumManager.getReplyRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Reply``.
        Providing an empty array tests if a ``Reply`` can be created
        with no records.

        :param reply_record_types: array of reply record types
        :type reply_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Reply`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``reply_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_reply_form_for_create_to_post(self, post_id, reply_record_types):
        """Gets the reply form for creating new replies to a post.
        A new form should be requested for each create transaction.

        :param post_id: the ``Id`` for the post
        :type post_id: ``osid.id.Id``
        :param reply_record_types: array of reply record types
        :type reply_record_types: ``osid.type.Type[]``
        :return: the reply form
        :rtype: ``osid.forum.ReplyForm``
        :raise: ``NotFound`` -- ``post_id`` is not found
        :raise: ``NullArgument`` -- ``post_id`` or ``reply_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def get_reply_form_for_create_to_reply(self, reply_id, reply_record_types):
        """Gets the reply form for creating new replies to another reply.
        A new form should be requested for each create transaction.

        :param reply_id: the ``Id`` for the reply
        :type reply_id: ``osid.id.Id``
        :param reply_record_types: array of reply record types
        :type reply_record_types: ``osid.type.Type[]``
        :return: the reply form
        :rtype: ``osid.forum.ReplyForm``
        :raise: ``NotFound`` -- ``reply_id`` is not found
        :raise: ``NullArgument`` -- ``reply_id`` or ``reply_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_reply(self, reply_form):
        """Creates a new ``Reply``.

        :param reply_form: the form for this ``Reply``
        :type reply_form: ``osid.forum.ReplyForm``
        :return: the new ``Reply``
        :rtype: ``osid.forum.Reply``
        :raise: ``IllegalState`` -- ``reply_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``reply_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``reply_form`` did not originate from ``get_reply_form_for_create_to_post()`` or ``get_reply_form_for_create_to_reply()``

        """
        raise UNIMPLEMENTED()

    def can_update_replies(self):
        """Tests if this user can update replies.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Reply``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Reply`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_reply_form_for_update(self, reply_id):
        """Gets the reply form for updating an existing reply.
        A new reply form should be requested for each update
        transaction.

        :param reply_id: the ``Id`` of the ``Reply``
        :type reply_id: ``osid.id.Id``
        :return: the reply form
        :rtype: ``osid.forum.ReplyForm``
        :raise: ``NotFound`` -- ``reply_id`` is not found
        :raise: ``NullArgument`` -- ``reply_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_reply(self, reply_form):
        """Updates an existing reply.

        :param reply_form: the form containing the elements to be updated
        :type reply_form: ``osid.forum.ReplyForm``
        :raise: ``IllegalState`` -- ``reply_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``reply_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``reply_form`` did not originate from ``get_reply_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_replies(self):
        """Tests if this user can delete replies.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an ``Reply``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Reply`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_reply(self, reply_id):
        """Deletes an ``Reply``.

        :param reply_id: the ``Id`` of the ``Reply`` to remove
        :type reply_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``reply_id`` not found
        :raise: ``NullArgument`` -- ``reply_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_reply_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Comnents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Reply`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_reply(self, reply_id, alias_id):
        """Adds an ``Id`` to a ``Reply`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Reply`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another reply, it is
        reassigned to the given reply ``Id``.

        :param reply_id: the ``Id`` of a ``Reply``
        :type reply_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``reply_id`` not found
        :raise: ``NullArgument`` -- ``reply_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.forum.ReplyNotificationSession

    def can_register_for_reply_notifications(self):
        """Tests if this user can register for ``Reply`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_replies(self):
        """Register for notifications of new replies.
        ``ReplyReceiver.newReply()`` is invoked when a new ``Reply`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_replies_for_poster(self, resource_id):
        """Register for notifications of new replies for the given poster resource ``Id``.
        ``ReplyReceiver.newReply()`` is invoked when a new ``Reply`` is
        created.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_replies_for_post(self, post_id):
        """Register for notifications of new replies for the given post ``Id``.
        ``ReplyReceiver.newReply()`` is invoked when a new ``Reply`` is
        created.

        :param post_id: the ``Id`` of the post to monitor
        :type post_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``post_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_replies(self):
        """Registers for notification of updated replies.
        ``ReplyReceiver.changedReply()`` is invoked when a reply is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_replies_for_poster(self, resource_id):
        """Register for notifications of changed replies for the given poster resource ``Id``.
        ``ReplyReceiver.changedReply()`` is invoked when a ``Reply`` for
        the poster is changed.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_replies_for_post(self, post_id):
        """Register for notifications of changed replies for the given post ``Id``.
        ``ReplyReceiver.changedReply()`` is invoked when a ``Reply`` for
        the post is changed.

        :param post_id: the ``Id`` of the post to monitor
        :type post_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``post_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_reply(self, reply_id):
        """Registers for notification of an updated reply.
        ``ReplyReceiver.changedReply()`` is invoked when the specified
        reply is changed.

        :param reply_id: the ``Id`` of the ``Reply`` to monitor
        :type reply_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``reply_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_replies(self):
        """Registers for notification of deleted replies.
        ``ReplyReceiver.deletedReply()`` is invoked when a reply is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_replies_for_poster(self, resource_id):
        """Register for notifications of deleted replies for the given poster resource ``Id``.
        ``ReplyReceiver.deletedReply()`` is invoked when a ``Reply`` for
        the poster is deleted.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_replies_for_post(self, post_id):
        """Register for notifications of deleted replies for the given post ``Id``.
        ``ReplyReceiver.deletedReply()`` is invoked when a ``Reply`` for
        the post is deleted.

        :param post_id: the ``Id`` of the post to monitor
        :type post_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``post_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_reply(self, reply_id):
        """Registers for notification of a deleted reply.
        ``ReplyReceiver.deletedReply()`` is invoked when the specified
        reply is deleted.

        :param reply_id: the ``Id`` of the ``Reply`` to monitor
        :type reply_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``reply_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class ForumList(osid.OsidList):

    def get_next_forum(self):
        """Gets the next ``Forum`` in this list.

        :return: the next ``Forum`` in this list. The ``has_next()`` method should be used to test that a next ``Forum`` is available before calling this method.
        :rtype: ``osid.forum.Forum``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()



class Forums(ForumManager):
    pass


