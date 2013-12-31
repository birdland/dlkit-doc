# -*- coding: utf-8 -*-
"""Commenting Open Service Interface Definitions
commenting version 3.0.0

The Commenting OSID provides a means of relating user comments and
ratings to OSID Objects.

The Commenting OSID may be used as an auxiliary service orchestrated
with other OSIDs to either provide administrative comments as well as
create a social network-esque comment and rating service to various
``OsidObjects``.

Comments

``Comments`` contain text entries logged by date and ``Agent``. A
``Comment`` may also include a rating represented by a ``Grade`` defined
in a ``GradeSystem``. The ``RatingLookupSession`` may be used to query
cumulative scores across an object reference or the entire ``Book``.

``Comments`` are ``OsidRelationships`` between a commentor and a
reference Id. The relationship defines dates for which the comment
and/or rating is effective.

Commentors

An ``Agent`` comments on something. As a person is represented by a
``Resource`` in the Resource OSID, the Comments provide access to both
the commenting ``Agent`` and the related ``Resource`` to avoid the need
of an additional service orchestration for resolving the ``Agent``.

Cataloging

``Comments`` are cataloged in ``Books`` which may also be grouped
hierarchically to federate multiple collections of comments.

Sub Packages

The Commenting OSID includes a Commenting Batch OSID for managing
``Comments`` and ``Books`` in bulk.

"""
from . import osid
from .osid_errors import Unimplemented, IllegalState, OperationFailed


class CommentingProfile(osid.OsidProfile):

    def supports_visible_federation(self):
        """Tests if any book federation is exposed.
        Federation is exposed when a specific book may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of books appears as a
        single book.

        :return: ``true`` if visible federation is supproted, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_comment_lookup(self):
        """Tests for the availability of a comment lookup service.

        :return: ``true`` if comment lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_rating_lookup(self):
        """Tests for the availability of a rating lookup service.

        :return: ``true`` if rating lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_comment_query(self):
        """Tests if querying comments is available.

        :return: ``true`` if comment query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_comment_search(self):
        """Tests if searching for comments is available.

        :return: ``true`` if comment search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_comment_admin(self):
        """Tests if managing comments is available.

        :return: ``true`` if comment admin is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_comment_notification(self):
        """Tests if comment notification is available.

        :return: ``true`` if comment notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_comment_book(self):
        """Tests if a comment to book lookup session is available.

        :return: ``true`` if comment book lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_comment_book_assignment(self):
        """Tests if a comment to book assignment session is available.

        :return: ``true`` if comment book assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_comment_smart_book(self):
        """Tests if a comment smart booking session is available.

        :return: ``true`` if comment smart booking is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_book_lookup(self):
        """Tests for the availability of an book lookup service.

        :return: ``true`` if book lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_book_query(self):
        """Tests if querying books is available.

        :return: ``true`` if book query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_book_search(self):
        """Tests if searching for books is available.

        :return: ``true`` if book search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_book_admin(self):
        """Tests for the availability of a book administrative service for creating and deleting books.

        :return: ``true`` if book administration is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_book_notification(self):
        """Tests for the availability of a book notification service.

        :return: ``true`` if book notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_book_hierarchy(self):
        """Tests for the availability of a book hierarchy traversal service.

        :return: ``true`` if book hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_book_hierarchy_design(self):
        """Tests for the availability of a book hierarchy design service.

        :return: ``true`` if book hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_commenting_batch(self):
        """Tests for the availability of a commenting batch service.

        :return: ``true`` if commenting batch service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_comment_record_types(self):
        """Gets the supported ``Comment`` record types.

        :return: a list containing the supported comment record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    comment_record_types = property(fget=get_comment_record_types)

    def supports_comment_record_type(self, comment_record_type):
        """Tests if the given ``Comment`` record type is supported.

        :param comment_record_type: a ``Type`` indicating a ``Comment`` record type
        :type comment_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``comment_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_comment_search_record_types(self):
        """Gets the supported comment search record types.

        :return: a list containing the supported comment search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    comment_search_record_types = property(fget=get_comment_search_record_types)

    def supports_comment_search_record_type(self, comment_search_record_type):
        """Tests if the given comment search record type is supported.

        :param comment_search_record_type: a ``Type`` indicating a comment record type
        :type comment_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``comment_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_book_record_types(self):
        """Gets the supported ``Book`` record types.

        :return: a list containing the supported book record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    book_record_types = property(fget=get_book_record_types)

    def supports_book_record_type(self, book_record_type):
        """Tests if the given ``Book`` record type is supported.

        :param book_record_type: a ``Type`` indicating a ``Book`` record type
        :type book_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``book_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_book_search_record_types(self):
        """Gets the supported book search record types.

        :return: a list containing the supported book search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    book_search_record_types = property(fget=get_book_search_record_types)

    def supports_book_search_record_type(self, book_search_record_type):
        """Tests if the given book search record type is supported.

        :param book_search_record_type: a ``Type`` indicating a book record type
        :type book_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``book_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class CommentingManager(osid.OsidManager, osid.OsidSession, CommentingProfile):

    def get_comment_lookup_session(self):
        """Gets the ``OsidSession`` associated with the comment lookup service.

        :return: a ``CommentLookupSession``
        :rtype: ``osid.commenting.CommentLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    comment_lookup_session = property(fget=get_comment_lookup_session)

    def get_comment_lookup_session_for_book(self, book_id):
        """Gets the ``OsidSession`` associated with the comment lookup service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: a ``CommentLookupSession``
        :rtype: ``osid.commenting.CommentLookupSession``
        :raise: ``NotFound`` -- no ``Book`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_rating_lookup_session(self):
        """Gets the ``OsidSession`` associated with the rating lookup service.

        :return: a ``RatingLookupSession``
        :rtype: ``osid.commenting.RatingLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rating_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    rating_lookup_session = property(fget=get_rating_lookup_session)

    def get_rating_lookup_session_for_book(self, book_id):
        """Gets the ``OsidSession`` associated with the rating lookup service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: a ``RatingLookupSession``
        :rtype: ``osid.commenting.RatingLookupSession``
        :raise: ``NotFound`` -- no ``Book`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rating_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_query_session(self):
        """Gets the ``OsidSession`` associated with the comment query service.

        :return: a ``CommentQuerySession``
        :rtype: ``osid.commenting.CommentQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    comment_query_session = property(fget=get_comment_query_session)

    def get_comment_query_session_for_book(self, book_id):
        """Gets the ``OsidSession`` associated with the comment query service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: a ``CommentQuerySession``
        :rtype: ``osid.commenting.CommentQuerySession``
        :raise: ``NotFound`` -- no ``Book`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_search_session(self):
        """Gets the ``OsidSession`` associated with the comment search service.

        :return: a ``CommentSearchSession``
        :rtype: ``osid.commenting.CommentSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    comment_search_session = property(fget=get_comment_search_session)

    def get_comment_search_session_for_book(self, book_id):
        """Gets the ``OsidSession`` associated with the comment search service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: a ``CommentSearchSession``
        :rtype: ``osid.commenting.CommentSearchSession``
        :raise: ``NotFound`` -- no ``Book`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_admin_session(self):
        """Gets the ``OsidSession`` associated with the comment administration service.

        :return: a ``CommentAdminSession``
        :rtype: ``osid.commenting.CommentAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    comment_admin_session = property(fget=get_comment_admin_session)

    def get_comment_admin_session_for_book(self, book_id):
        """Gets the ``OsidSession`` associated with the comment administration service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: a ``CommentAdminSession``
        :rtype: ``osid.commenting.CommentAdminSession``
        :raise: ``NotFound`` -- no ``Book`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_notification_session(self, comment_receiver):
        """Gets the ``OsidSession`` associated with the comment notification service.

        :param comment_receiver: the receiver
        :type comment_receiver: ``osid.commenting.CommentReceiver``
        :return: a ``CommentNotificationSession``
        :rtype: ``osid.commenting.CommentNotificationSession``
        :raise: ``NullArgument`` -- ``comment_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_notification_session_for_book(self, comment_receiver, book_id):
        """Gets the ``OsidSession`` associated with the comment notification service for the given book.

        :param comment_receiver: the receiver
        :type comment_receiver: ``osid.commenting.CommentReceiver``
        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: a ``CommentNotificationSession``
        :rtype: ``osid.commenting.CommentNotificationSession``
        :raise: ``NotFound`` -- no ``Book`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``comment_receiver`` or ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_book_session(self):
        """Gets the session for retrieving comment to book mappings.

        :return: a ``CommentBookSession``
        :rtype: ``osid.commenting.CommentBookSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_book()`` is ``false``

        """
        raise UNIMPLEMENTED()

    comment_book_session = property(fget=get_comment_book_session)

    def get_comment_book_assignment_session(self):
        """Gets the session for assigning comment to book mappings.

        :return: a ``CommentBookAssignmentSession``
        :rtype: ``osid.commenting.CommentBookAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_book_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    comment_book_assignment_session = property(fget=get_comment_book_assignment_session)

    def get_comment_smart_book_session(self, book_id):
        """Gets the session associated with the comment smart book for the given book.

        :param book_id: the ``Id`` of the book
        :type book_id: ``osid.id.Id``
        :return: a ``CommentSmartBookSession``
        :rtype: ``osid.commenting.CommentSmartBookSession``
        :raise: ``NotFound`` -- ``book_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_smart_book()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_book_lookup_session(self):
        """Gets the ``OsidSession`` associated with the book lookup service.

        :return: a ``BookLookupSession``
        :rtype: ``osid.commenting.BookLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    book_lookup_session = property(fget=get_book_lookup_session)

    def get_book_query_session(self):
        """Gets the ``OsidSession`` associated with the book query service.

        :return: a ``BookQuerySession``
        :rtype: ``osid.commenting.BookQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    book_query_session = property(fget=get_book_query_session)

    def get_book_search_session(self):
        """Gets the ``OsidSession`` associated with the book search service.

        :return: a ``BookSearchSession``
        :rtype: ``osid.commenting.BookSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    book_search_session = property(fget=get_book_search_session)

    def get_book_admin_session(self):
        """Gets the ``OsidSession`` associated with the book administrative service.

        :return: a ``BookAdminSession``
        :rtype: ``osid.commenting.BookAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    book_admin_session = property(fget=get_book_admin_session)

    def get_book_notification_session(self, book_receiver):
        """Gets the ``OsidSession`` associated with the book notification service.

        :param book_receiver: the receiver
        :type book_receiver: ``osid.commenting.BookReceiver``
        :return: a ``BookNotificationSession``
        :rtype: ``osid.commenting.BookNotificationSession``
        :raise: ``NullArgument`` -- ``book_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_book_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the book hierarchy service.

        :return: a ``BookHierarchySession``
        :rtype: ``osid.commenting.BookHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    book_hierarchy_session = property(fget=get_book_hierarchy_session)

    def get_book_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the book hierarchy design service.

        :return: a ``BookHierarchyDesignSession``
        :rtype: ``osid.commenting.BookHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    book_hierarchy_design_session = property(fget=get_book_hierarchy_design_session)

    def get_commenting_batch_manager(self):
        """Gets a ``CommentingBatchManager``.

        :return: a ``CommentingBatchManager``
        :rtype: ``osid.commenting.batch.CommentingBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commenting_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    commenting_batch_manager = property(fget=get_commenting_batch_manager)


##
# The following methods are from osid.commenting.BookLookupSession

    def can_lookup_books(self):
        """Tests if this user can perform ``Book`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_book_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_book_view(self):
        """A complete view of the ``Book`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_book(self, book_id):
        """Gets the ``Book`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Book`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Book`` and retained for compatibility.

        :param book_id: ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: the book
        :rtype: ``osid.commenting.Book``
        :raise: ``NotFound`` -- ``book_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_books_by_ids(self, book_ids):
        """Gets a ``BookList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the books
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Books`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param book_ids: the list of ``Ids`` to retrieve
        :type book_ids: ``osid.id.IdList``
        :return: the returned ``Book`` list
        :rtype: ``osid.commenting.BookList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``book_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_books_by_genus_type(self, book_genus_type):
        """Gets a ``BookList`` corresponding to the given book genus ``Type`` which does not include books of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :param book_genus_type: a book genus type
        :type book_genus_type: ``osid.type.Type``
        :return: the returned ``Book`` list
        :rtype: ``osid.commenting.BookList``
        :raise: ``NullArgument`` -- ``book_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_books_by_parent_genus_type(self, book_genus_type):
        """Gets a ``BookList`` corresponding to the given book genus ``Type`` and include any additional books with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :param book_genus_type: a book genus type
        :type book_genus_type: ``osid.type.Type``
        :return: the returned ``Book`` list
        :rtype: ``osid.commenting.BookList``
        :raise: ``NullArgument`` -- ``book_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_books_by_record_type(self, book_record_type):
        """Gets a ``BookList`` containing the given book record ``Type``.
        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :param book_record_type: a book record type
        :type book_record_type: ``osid.type.Type``
        :return: the returned ``Book`` list
        :rtype: ``osid.commenting.BookList``
        :raise: ``NullArgument`` -- ``book_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_books_by_provider(self, resource_id):
        """Gets a ``BookList`` from the given provider ````.
        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Book`` list
        :rtype: ``osid.commenting.BookList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_books(self):
        """Gets all ``Books``.
        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :return: a list of ``Books``
        :rtype: ``osid.commenting.BookList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    books = property(fget=get_books)


##
# The following methods are from osid.commenting.BookQuerySession

    def can_search_books(self):
        """Tests if this user can perform ``Book`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_book_query(self):
        """Gets a book query.

        :return: the book query
        :rtype: ``osid.commenting.BookQuery``

        """
        raise UNIMPLEMENTED()

    book_query = property(fget=get_book_query)

    def get_books_by_query(self, book_query):
        """Gets a list of ``Books`` matching the given search.

        :param book_query: the book query
        :type book_query: ``osid.commenting.BookQuery``
        :return: the returned ``BookList``
        :rtype: ``osid.commenting.BookList``
        :raise: ``NullArgument`` -- ``book_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``book_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.commenting.BookSearchSession

    def get_book_search(self):
        """Gets a book search.

        :return: the book search
        :rtype: ``osid.commenting.BookSearch``

        """
        raise UNIMPLEMENTED()

    book_search = property(fget=get_book_search)

    def get_book_search_order(self):
        """Gets a book search order.
        The ``BookSearchOrder`` is supplied to a ``BookSearch`` to
        specify the ordering of results.

        :return: the book search order
        :rtype: ``osid.commenting.BookSearchOrder``

        """
        raise UNIMPLEMENTED()

    book_search_order = property(fget=get_book_search_order)

    def get_books_by_search(self, book_query, book_search):
        """Gets the search results matching the given search.

        :param book_query: the book query
        :type book_query: ``osid.commenting.BookQuery``
        :param book_search: the book search
        :type book_search: ``osid.commenting.BookSearch``
        :return: the search results
        :rtype: ``osid.commenting.BookSearchResults``
        :raise: ``NullArgument`` -- ``book_query`` or ``book_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``book_query`` or ``book_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_book_query_from_inspector(self, book_query_inspector):
        """Gets an entry query from an inspector.
        The inspector is available from an ``BookSearchResults``.

        :param book_query_inspector: a book query inspector
        :type book_query_inspector: ``osid.commenting.BookQueryInspector``
        :return: the book query
        :rtype: ``osid.commenting.BookQuery``
        :raise: ``NullArgument`` -- ``book_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``book_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.commenting.BookAdminSession

    def can_create_books(self):
        """Tests if this user can create ``Books``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Book`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_book_with_record_types(self, book_record_types):
        """Tests if this user can create a single ``Book`` using the desired record types.
        While ``CommentingManager.getBookRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Book``.
        Providing an empty array tests if a ``Book`` can be created with
        no records.

        :param book_record_types: array of book record types
        :type book_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Book`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``book_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_book_form_for_create(self, book_record_types):
        """Gets the book form for creating new books.
        A new form should be requested for each create transaction.

        :param book_record_types: array of book record types
        :type book_record_types: ``osid.type.Type[]``
        :return: the book form
        :rtype: ``osid.commenting.BookForm``
        :raise: ``NullArgument`` -- ``book_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_book(self, book_form):
        """Creates a new ``Book``.

        :param book_form: the form for this ``Book``
        :type book_form: ``osid.commenting.BookForm``
        :return: the new ``Book``
        :rtype: ``osid.commenting.Book``
        :raise: ``IllegalState`` -- ``book_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``book_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``book_form`` did not originte from ``get_book_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_books(self):
        """Tests if this user can update ``Books``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Book`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_book_form_for_update(self, book_id):
        """Gets the book form for updating an existing book.
        A new book form should be requested for each update transaction.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: the book form
        :rtype: ``osid.commenting.BookForm``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_book(self, book_form):
        """Updates an existing book.

        :param book_form: the form containing the elements to be updated
        :type book_form: ``osid.commenting.BookForm``
        :raise: ``IllegalState`` -- ``book_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``book_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``book_form`` did not originte from ``get_book_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_books(self):
        """Tests if this user can delete ``Books`` A return of true does not guarantee successful authorization.
        A return of false indicates that it is known deleting a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Book`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_book(self, book_id):
        """Deletes a ``Book``.

        :param book_id: the ``Id`` of the ``Book`` to remove
        :type book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``book_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_book_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Books``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Book`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_book(self, book_id, alias_id):
        """Adds an ``Id`` to a ``Book`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Book`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another book, it is
        reassigned to the given book ``Id``.

        :param book_id: the ``Id`` of a ``Book``
        :type book_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``book_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.commenting.BookNotificationSession

    def can_register_for_book_notifications(self):
        """Tests if this user can register for ``Book`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_books(self):
        """Register for notifications of new books.
        ``BookReceiver.newBook()`` is invoked when a new ``Book`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_book_ancestors(self, book_id):
        """Registers for notification of an updated hierarchy structure that introduces a new ancestor of the specified book.
        ``BookReceiver.newAncestorBook()`` is invoked when the specified
        book node gets a new ancestor.

        :param book_id: the ``Id`` of the ``Book`` node to monitor
        :type book_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_book_descendants(self, book_id):
        """Registers for notification of an updated hierarchy structure that introduces a new descendant of the specified book.
        ``BookReceiver.newDescendantBook()`` is invoked when the
        specified book node gets a new descendant.

        :param book_id: the ``Id`` of the ``Book`` node to monitor
        :type book_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_books(self):
        """Registers for notification of updated books.
        ``BookReceiver.changedBook()`` is invoked when a book is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_book(self, book_id):
        """Registers for notification of an updated book.
        ``BookReceiver.changedBook()`` is invoked when the specified
        book is changed.

        :param book_id: the ``Id`` of the ``Book`` to monitor
        :type book_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_books(self):
        """Registers for notification of deleted books.
        ``BookReceiver.deletedBook()`` is invoked when a book is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_book(self, book_id):
        """Registers for notification of a deleted book.
        ``BookReceiver.deletedBook()`` is invoked when the specified
        book is deleted.

        :param book_id: the ``Id`` of the ``Book`` to monitor
        :type book_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_book_ancestors(self, book_id):
        """Registers for notification of an updated hierarchy structure that removes an ancestor of the specified book ``BookReceiver.
        deletedAncestor()`` is invoked when the specified book node
        loses an ancestor.

        :param book_id: the ``Id`` of the ``Book`` to monitor
        :type book_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_book_descendants(self, book_id):
        """Registers for notification of an updated hierarchy structure that removes a descendant of the specified book.
        ``BookReceiver.deletedDescendant()`` is invoked when the
        specified book node loses a descendant.

        :param book_id: the ``Id`` of the ``Book`` to monitor
        :type book_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.commenting.BookHierarchySession

    def get_book_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    book_hierarchy_id = property(fget=get_book_hierarchy_id)

    def get_book_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    book_hierarchy = property(fget=get_book_hierarchy)

    def can_access_book_hierarchy(self):
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

    def get_root_book_ids(self):
        """Gets the root book ``Ids`` in this hierarchy.

        :return: the root book ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_book_ids = property(fget=get_root_book_ids)

    def get_root_books(self):
        """Gets the root books in the book hierarchy.
        A node with no parents is an orphan. While all book ``Ids`` are
        known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        :return: the root books
        :rtype: ``osid.commenting.BookList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_books = property(fget=get_root_books)

    def has_parent_books(self, book_id):
        """Tests if the ``Book`` has any parents.

        :param book_id: a book ``Id``
        :type book_id: ``osid.id.Id``
        :return: ``true`` if the book has parents, f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_book(self, id_, book_id):
        """Tests if an ``Id`` is a direct parent of book.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``book_id,`` f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_book_ids(self, book_id):
        """Gets the parent ``Ids`` of the given book.

        :param book_id: a book ``Id``
        :type book_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the book
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_books(self, book_id):
        """Gets the parent books of the given ``id``.

        :param book_id: the ``Id`` of the ``Book`` to query
        :type book_id: ``osid.id.Id``
        :return: the parent books of the ``id``
        :rtype: ``osid.commenting.BookList``
        :raise: ``NotFound`` -- a ``Book`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_book(self, id_, book_id):
        """Tests if an ``Id`` is an ancestor of a book.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :return: ``tru`` e if this ``id`` is an ancestor of ``book_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_books(self, book_id):
        """Tests if a book has any children.

        :param book_id: a book ``Id``
        :type book_id: ``osid.id.Id``
        :return: ``true`` if the ``book_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_book(self, id_, book_id):
        """Tests if a book is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``book_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_book_ids(self, book_id):
        """Gets the child ``Ids`` of the given book.

        :param book_id: the ``Id`` to query
        :type book_id: ``osid.id.Id``
        :return: the children of the book
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_books(self, book_id):
        """Gets the child books of the given ``id``.

        :param book_id: the ``Id`` of the ``Book`` to query
        :type book_id: ``osid.id.Id``
        :return: the child books of the ``id``
        :rtype: ``osid.commenting.BookList``
        :raise: ``NotFound`` -- a ``Book`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_book(self, id_, book_id):
        """Tests if an ``Id`` is a descendant of a book.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``book_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_book_node_ids(self, book_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given book.

        :param book_id: the ``Id`` to query
        :type book_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a book node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_book_nodes(self, book_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given book.

        :param book_id: the ``Id`` to query
        :type book_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a book node
        :rtype: ``osid.commenting.BookNode``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.commenting.BookHierarchyDesignSession

    def can_modify_book_hierarchy(self):
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

    def add_root_book(self, book_id):
        """Adds a root book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``book_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_book(self, book_id):
        """Removes a root book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``book_id`` is not a root
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_book(self, book_id, child_id):
        """Adds a child to a book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``book_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``book_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_book(self, book_id, child_id):
        """Removes a child from a book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``book_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``book_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_books(self, book_id):
        """Removes all children from a book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``book_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class CommentingProxyManager(osid.OsidProxyManager, CommentingProfile):

    def get_comment_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the comment lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentLookupSession``
        :rtype: ``osid.commenting.CommentLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_lookup_session_for_book(self, book_id, proxy):
        """Gets the ``OsidSession`` associated with the comment lookup service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentLookupSession``
        :rtype: ``osid.commenting.CommentLookupSession``
        :raise: ``NotFound`` -- no ``Book`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_rating_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the rating lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RatingLookupSession``
        :rtype: ``osid.commenting.RatingLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rating_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_rating_lookup_session_for_book(self, book_id, proxy):
        """Gets the ``OsidSession`` associated with the rating lookup service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RatingLookupSession``
        :rtype: ``osid.commenting.RatingLookupSession``
        :raise: ``NotFound`` -- no ``Book`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rating_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the comment query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentQuerySession``
        :rtype: ``osid.commenting.CommentQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_query_session_for_book(self, book_id, proxy):
        """Gets the ``OsidSession`` associated with the comment query service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentQuerySession``
        :rtype: ``osid.commenting.CommentQuerySession``
        :raise: ``NotFound`` -- no ``Comment`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the comment search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentSearchSession``
        :rtype: ``osid.commenting.CommentSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_search_session_for_book(self, book_id, proxy):
        """Gets the ``OsidSession`` associated with the comment search service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentSearchSession``
        :rtype: ``osid.commenting.CommentSearchSession``
        :raise: ``NotFound`` -- no ``Comment`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the comment administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentAdminSession``
        :rtype: ``osid.commenting.CommentAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_admin_session_for_book(self, book_id, proxy):
        """Gets the ``OsidSession`` associated with the comment administration service for the given book.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentAdminSession``
        :rtype: ``osid.commenting.CommentAdminSession``
        :raise: ``NotFound`` -- no ``Comment`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``book_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_notification_session(self, comment_receiver, proxy):
        """Gets the ``OsidSession`` associated with the comment notification service.

        :param comment_receiver: the receiver
        :type comment_receiver: ``osid.commenting.CommentReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentNotificationSession``
        :rtype: ``osid.commenting.CommentNotificationSession``
        :raise: ``NullArgument`` -- ``comment_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_notification_session_for_book(self, comment_receiver, book_id, proxy):
        """Gets the ``OsidSession`` associated with the comment notification service for the given book.

        :param comment_receiver: the receiver
        :type comment_receiver: ``osid.commenting.CommentReceiver``
        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentNotificationSession``
        :rtype: ``osid.commenting.CommentNotificationSession``
        :raise: ``NotFound`` -- no ``Comment`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``comment_receiver, book_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_book_session(self, proxy):
        """Gets the session for retrieving comment to book mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentBookSession``
        :rtype: ``osid.commenting.CommentBookSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_book()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_book_assignment_session(self, proxy):
        """Gets the session for assigning comment to book mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommentBookAssignmentSession``
        :rtype: ``osid.commenting.CommentBookAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_book_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_comment_smart_book_session(self, book_id, proxy):
        """Gets the session for managing dynamic comment books for the given book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``book_id`` not found
        :rtype: ``osid.commenting.CommentSmartBookSession``
        :raise: ``NotFound`` -- ``book_id`` or ``proxy`` is ``null``
        :raise: ``NullArgument`` -- ``book_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_smart_book()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_book_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the book lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BookLookupSession``
        :rtype: ``osid.commenting.BookLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_book_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the book query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BookQuerySession``
        :rtype: ``osid.commenting.BookQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_queryh()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_book_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the book search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BookSearchSession``
        :rtype: ``osid.commenting.BookSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_book_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the book administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BookAdminSession``
        :rtype: ``osid.commenting.BookAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_book_notification_session(self, book_receiver, proxy):
        """Gets the ``OsidSession`` associated with the book notification service.

        :param book_receiver: the receiver
        :type book_receiver: ``osid.commenting.BookReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BookNotificationSession``
        :rtype: ``osid.commenting.BookNotificationSession``
        :raise: ``NullArgument`` -- ``book_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_book_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the book hierarchy service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BookHierarchySession``
        :rtype: ``osid.commenting.BookHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_book_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the book hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BookHierarchyDesignSession``
        :rtype: ``osid.commenting.BookHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commenting_batch_proxy_manager(self):
        """Gets a ``CommentingBatchProxyManager``.

        :return: a ``CommentingBatchProxyManager``
        :rtype: ``osid.commenting.batch.CommentingBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commenting_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    commenting_batch_proxy_manager = property(fget=get_commenting_batch_proxy_manager)



class Book(osid.OsidCatalog, osid.OsidSession):

    def get_book_record(self, book_record_type):
        """Gets the book record corresponding to the given ``Book`` record ``Type``.
        This method is used to retrieve an object implementing the
        requested record. The ``book_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(book_record_type)``
        is ``true`` .

        :param book_record_type: the type of book record to retrieve
        :type book_record_type: ``osid.type.Type``
        :return: the book record
        :rtype: ``osid.commenting.records.BookRecord``
        :raise: ``NullArgument`` -- ``book_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(book_record_type)`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.commenting.CommentLookupSession

    def get_book_id(self):
        """Gets the ``Book``  ``Id`` associated with this session.

        :return: the ``Book Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    book_id = property(fget=get_book_id)

    def get_book(self):
        """Gets the ``Book`` associated with this session.

        :return: the book
        :rtype: ``osid.commenting.Book``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    book = property(fget=get_book)

    def can_lookup_comments(self):
        """Tests if this user can examine this book.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer these
        operations.

        :return: ``false`` if book reading methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_comment_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_comment_view(self):
        """A complete view of the ``Comment`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_book_view(self):
        """Federates the view for methods in this session.
        A federated view will include comments in books which are
        children of this book in the book hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_book_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts retrievals to this book only.



        """
        raise UNIMPLEMENTED()

    def use_effective_comment_view(self):
        """Only comments whose effective dates are current are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_any_effective_comment_view(self):
        """All comments of any effective dates are returned by all methods in this session."""
        raise UNIMPLEMENTED()

    def get_comment(self, comment_id):
        """Gets the ``Comment`` specified by its ``Id``.

        :param comment_id: the ``Id`` of the ``Comment`` to retrieve
        :type comment_id: ``osid.id.Id``
        :return: the returned ``Comment``
        :rtype: ``osid.commenting.Comment``
        :raise: ``NotFound`` -- no ``Comment`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``comment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_by_ids(self, comment_ids):
        """Gets a ``CommentList`` corresponding to the given ``IdList``.

        :param comment_ids: the list of ``Ids`` to retrieve
        :type comment_ids: ``osid.id.IdList``
        :return: the returned ``Comment list``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``comment_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_by_genus_type(self, comment_genus_type):
        """Gets a ``CommentList`` corresponding to the given comment genus ``Type`` which does not include comments of genus types derived from the specified ``Type``.

        :param comment_genus_type: a comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :return: the returned ``Comment`` list
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``comment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_by_parent_genus_type(self, comment_genus_type):
        """Gets a ``CommentList`` corresponding to the given comment genus ``Type`` and include any additional comments with genus types derived from the specified ``Type``.

        :param comment_genus_type: a comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :return: the returned ``Comment`` list
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``comment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_by_record_type(self, comment_record_type):
        """Gets a ``CommentList`` containing the given comment record ``Type``.

        :param comment_record_type: a comment record type
        :type comment_record_type: ``osid.type.Type``
        :return: the returned ``Comment`` list
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``comment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_on_date(self, from_, to):
        """Gets a ``CommentList`` effective during the entire given date range inclusive but not confined to the date range.

        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Comment`` list
        :rtype: ``osid.commenting.CommentList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_by_genus_type_on_date(self, comment_genus_type, from_, to):
        """Gets a ``CommentList`` of a given genus type and effective during the entire given date range inclusive but not confined to the date range.

        :param comment_genus_type: a comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Comment`` list
        :rtype: ``osid.commenting.CommentList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``comment_genus_type, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_for_commentor(self, resource_id):
        """Gets a list of comments corresponding to a resource ``Id``.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_for_commentor_on_date(self, resource_id, from_, to):
        """Gets a list of all comments corresponding to a resource ``Id`` and effective during the entire given date range inclusive but not confined to the date range.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``resource_id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_by_genus_type_for_commentor(self, resource_id, comment_genus_type):
        """Gets a list of comments of the given genus type corresponding to a resource ``Id``.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param comment_genus_type: the comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``resource_id`` or ``comment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_by_genus_type_for_commentor_on_date(self, resource_id, comment_genus_type, from_, to):
        """Gets a list of all comments of the given genus type corresponding to a resource ``Id`` and effective during the entire given date range inclusive but not confined to the date range.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param comment_genus_type: the comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``resource_id, comment_genus_type, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_for_reference(self, reference_id):
        """Gets a list of comments corresponding to a reference ``Id``.

        :param reference_id: the ``Id`` of the reference
        :type reference_id: ``osid.id.Id``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_for_reference_on_date(self, reference_id, from_, to):
        """Gets a list of all comments corresponding to a reference ``Id`` and effective during the entire given date range inclusive but not confined to the date range.

        :param reference_id: a reference ``Id``
        :type reference_id: ``osid.id.Id``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``reference_id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_by_genus_type_for_reference(self, reference_id, comment_genus_type):
        """Gets a list of comments of the given genus type corresponding to a reference ``Id``.

        :param reference_id: the ``Id`` of the reference
        :type reference_id: ``osid.id.Id``
        :param comment_genus_type: the comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``reference_id`` or ``comment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_by_genus_type_for_reference_on_date(self, reference_id, comment_genus_type, from_, to):
        """Gets a list of all comments of the given genus type corresponding to a reference ``Id`` and effective during the entire given date range inclusive but not confined to the date range.

        :param reference_id: a reference ``Id``
        :type reference_id: ``osid.id.Id``
        :param comment_genus_type: the comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``reference_id, comment_genus_type, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_for_commentor_and_reference(self, resource_id, reference_id):
        """Gets a list of comments corresponding to a resource and reference ``Id``.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param reference_id: the ``Id`` of the reference
        :type reference_id: ``osid.id.Id``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``resource_id`` or ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_for_commentor_and_reference_on_date(self, resource_id, reference_id, from_, to):
        """Gets a list of all comments corresponding to a resource and reference ``Id`` and effective during the entire given date range inclusive but not confined to the date range.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param reference_id: a reference ``Id``
        :type reference_id: ``osid.id.Id``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``resource_id, reference_id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_by_genus_type_for_commentor_and_reference(self, resource_id, reference_id, comment_genus_type):
        """Gets a list of comments of the given genus type corresponding to a resource and reference ``Id``.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param reference_id: the ``Id`` of the reference
        :type reference_id: ``osid.id.Id``
        :param comment_genus_type: the comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``resource_id, reference_id`` or ``comment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_by_genus_type_for_commentor_and_reference_on_date(self, resource_id, reference_id, comment_genus_type, from_, to):
        """Gets a list of all comments corresponding to a resource and reference ``Id`` and effective during the entire given date range inclusive but not confined to the date range.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :param reference_id: a reference ``Id``
        :type reference_id: ``osid.id.Id``
        :param comment_genus_type: the comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :param from: from date
        :type from: ``osid.calendaring.DateTime``
        :param to: to date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``resource_id, reference_id, comment_genus_type, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments(self):
        """Gets all comments.

        :return: a list of comments
        :rtype: ``osid.commenting.CommentList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    comments = property(fget=get_comments)


##
# The following methods are from osid.commenting.RatingLookupSession

    def can_lookup_ratings(self):
        """Tests if this user can examine this book.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer these
        operations.

        :return: ``false`` if book reading methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_cumulative_rating(self):
        """Gets the cumulative rating for all the references in this book.

        :return: the cumulative rating
        :rtype: ``osid.grading.Grade``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    cumulative_rating = property(fget=get_cumulative_rating)

    def get_cumulative_rating_for_reference(self, reference_id):
        """Gets the cumulative rating for a reference.

        :param reference_id: the ``Id`` of the reference
        :type reference_id: ``osid.id.Id``
        :return: the cumulative rating
        :rtype: ``osid.grading.Grade``
        :raise: ``NotFound`` -- no reference found with the given ``Id``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_cumulative_rating_for_commentor(self, resource_id):
        """Gets the cumulative rating for a commentor.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :return: the cumulative rating
        :rtype: ``osid.grading.Grade``
        :raise: ``NotFound`` -- no resource found with the given ``Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_top_references(self, max):
        """Gets the top rated references in this book.

        :param max: the maximum number to return
        :type max: ``cardinal``
        :return: the top references
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_references(self, grade_id):
        """Gets the references with ratings equal to or higher than the given grade.

        :param grade_id: the ``Id`` of the grade
        :type grade_id: ``osid.id.Id``
        :return: the cumulative rating
        :rtype: ``osid.grading.Grade``
        :raise: ``NotFound`` -- no reference found with the given ``Id``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.commenting.CommentQuerySession

    def can_search_comments(self):
        """Tests if this user can perform comment searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not wish to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_comment_query(self):
        """Gets a comment query.

        :return: the comment query
        :rtype: ``osid.commenting.CommentQuery``

        """
        raise UNIMPLEMENTED()

    comment_query = property(fget=get_comment_query)

    def get_comments_by_query(self, comment_query):
        """Gets a list of comments matching the given search.

        :param comment_query: the search query array
        :type comment_query: ``osid.commenting.CommentQuery``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``comment_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``comment_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.commenting.CommentSearchSession

    def get_comment_search(self):
        """Gets a comment search.

        :return: the comment search
        :rtype: ``osid.commenting.CommentSearch``

        """
        raise UNIMPLEMENTED()

    comment_search = property(fget=get_comment_search)

    def get_comment_search_order(self):
        """Gets a comment search order.
        The ``CommentSearchOrder`` is supplied to a ``CommentSearch`` to
        specify the ordering of results.

        :return: the comment search order
        :rtype: ``osid.commenting.CommentSearchOrder``

        """
        raise UNIMPLEMENTED()

    comment_search_order = property(fget=get_comment_search_order)

    def get_comments_by_search(self, comment_query, comment_search):
        """Gets the search results matching the given search.

        :param comment_query: the comment query
        :type comment_query: ``osid.commenting.CommentQuery``
        :param comment_search: the comment search
        :type comment_search: ``osid.commenting.CommentSearch``
        :return: the search results
        :rtype: ``osid.commenting.CommentSearchResults``
        :raise: ``NullArgument`` -- ``comment_query`` or ``comment_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``comment_query`` or ``comment_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_comment_query_from_inspector(self, comment_query_inspector):
        """Gets an entry query from an inspector.
        The inspector is available from an ``CommentSearchResults``.

        :param comment_query_inspector: a comment query inspector
        :type comment_query_inspector: ``osid.commenting.CommentQueryInspector``
        :return: the entry query
        :rtype: ``osid.commenting.CommentQuery``
        :raise: ``NullArgument`` -- ``comment_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``comment_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.commenting.CommentAdminSession

    def can_create_comments(self):
        """Tests if this user can create comments.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Comment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Comment`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_comment_with_record_types(self, comment_record_types):
        """Tests if this user can create a single ``Comment`` using the desired record types.
        While ``CommentingManager.getCommentRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Comment``.
        Providing an empty array tests if a ``Comment`` can be created
        with no records.

        :param comment_record_types: array of comment record types
        :type comment_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Comment`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``comment_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_comment_form_for_create(self, reference_id, comment_record_types):
        """Gets the comment form for creating new comments.
        A new form should be requested for each create transaction.

        :param reference_id: the ``Id`` for the reference object
        :type reference_id: ``osid.id.Id``
        :param comment_record_types: array of comment record types
        :type comment_record_types: ``osid.type.Type[]``
        :return: the comment form
        :rtype: ``osid.commenting.CommentForm``
        :raise: ``NullArgument`` -- ``reference_id or comment_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_comment(self, comment_form):
        """Creates a new ``Comment``.

        :param comment_form: the form for this ``Comment``
        :type comment_form: ``osid.commenting.CommentForm``
        :return: the new ``Comment``
        :rtype: ``osid.commenting.Comment``
        :raise: ``IllegalState`` -- ``comment_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``comment_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``comment_form`` did not originate from ``get_comment_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_comments(self):
        """Tests if this user can update comments.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Comment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Comment`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_comment_form_for_update(self, comment_id):
        """Gets the comment form for updating an existing comment.
        A new comment form should be requested for each update
        transaction.

        :param comment_id: the ``Id`` of the ``Comment``
        :type comment_id: ``osid.id.Id``
        :return: the comment form
        :rtype: ``osid.commenting.CommentForm``
        :raise: ``NotFound`` -- ``comment_id`` is not found
        :raise: ``NullArgument`` -- ``comment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_comment(self, comment_form):
        """Updates an existing comment.

        :param comment_form: the form containing the elements to be updated
        :type comment_form: ``osid.commenting.CommentForm``
        :raise: ``IllegalState`` -- ``comment_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``comment_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``comment_form`` did not originate from ``get_comment_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_comments(self):
        """Tests if this user can delete comments.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Comment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Comment`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_comment(self, comment_id):
        """Deletes a ``Comment``.

        :param comment_id: the ``Id`` of the ``Comment`` to remove
        :type comment_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``comment_id`` not found
        :raise: ``NullArgument`` -- ``comment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_comment_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Comnents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Comment`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_comment(self, comment_id, alias_id):
        """Adds an ``Id`` to a ``Comment`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Comment`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another comment, it is
        reassigned to the given comment ``Id``.

        :param comment_id: the ``Id`` of a ``Comment``
        :type comment_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``comment_id`` not found
        :raise: ``NullArgument`` -- ``comment_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.commenting.CommentNotificationSession

    def can_register_for_comment_notifications(self):
        """Tests if this user can register for ``Comment`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_comments(self):
        """Register for notifications of new comments.
        ``CommentReceiver.newComment()`` is invoked when a new
        ``Comment`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_comments_for_commentor(self, resource_id):
        """Register for notifications of new comments by the given resource ``Id``.
        ``CommentReceiver.newComment()`` is invoked when a new
        ``Comment`` is created.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_comments_for_reference(self, reference_id):
        """Register for notifications of new comments for the given reference ``Id``.
        ``CommentReceiver.newComment()`` is invoked when a new
        ``Comment`` is created.

        :param reference_id: the ``Id`` of the reference to monitor
        :type reference_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_comments(self):
        """Registers for notification of updated comments.
        ``CommentReceiver.changedComment()`` is invoked when a comment
        is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_comments_for_commentor(self, resource_id):
        """Register for notifications of changed comments by the given resource ``Id``.
        ``CommentReceiver.changedComment()`` is invoked when a
        ``Comment`` by the resource is changed.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_comments_for_reference(self, reference_id):
        """Register for notifications of changed comments for the given reference ``Id``.
        ``CommentReceiver.changedComment()`` is invoked when a
        ``Comment`` for the reference is changed.

        :param reference_id: the ``Id`` of the reference to monitor
        :type reference_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_comment(self, comment_id):
        """Registers for notification of an updated comment.
        ``CommentReceiver.changedComment()`` is invoked when the
        specified comment is changed.

        :param comment_id: the ``Id`` of the ``Comment`` to monitor
        :type comment_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a comment was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``comment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_comments(self):
        """Registers for notification of deleted comments.
        ``CommentReceiver.deletedComment()`` is invoked when a comment
        is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_comments_for_commentor(self, resource_id):
        """Register for notifications of deleted comments by the given resource ``Id``.
        ``CommentReceiver.deletedComment()`` is invoked when a
        ``Comment`` by the resource is deleted.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_comments_for_reference(self, reference_id):
        """Register for notifications of deleted comments for the given reference ``Id``.
        ``CommentReceiver.deletedComment()`` is invoked when a
        ``Comment`` for the reference is deleted.

        :param reference_id: the ``Id`` of the reference to monitor
        :type reference_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_comment(self, comment_id):
        """Registers for notification of a deleted comment.
        ``CommentReceiver.deletedComment()`` is invoked when the
        specified comment is deleted.

        :param comment_id: the ``Id`` of the ``Comment`` to monitor
        :type comment_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a comment was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``comment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.commenting.CommentBookSession

    def can_lookup_comment_book_mappings(self):
        """Tests if this user can perform lookups of comment/book mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intendedas a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_book_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_book_view(self):
        """A complete view of the ``Comment`` and ``Book`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_comment_ids_by_book(self, book_id):
        """Gets the list of Comment Ids associated with a ``Book``.

        :param book_id: ``Id`` of a ``Book``.
        :type book_id: ``osid.id.Id``
        :return: list of related comment ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_by_book(self, book_id):
        """Gets the list of ``Comments`` associated with a ``Book``.

        :param book_id: ``Id`` of a ``Book``
        :type book_id: ``osid.id.Id``
        :return: list of related comments
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comment_ids_by_books(self, book_ids):
        """Gets the list of ``Comment Ids`` corresponding to a list of ``Book`` objects.

        :param book_ids: list of book ``Ids``
        :type book_ids: ``osid.id.IdList``
        :return: list of comment ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``book_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_comments_by_books(self, book_ids):
        """Gets the list of ``Comments`` corresponding to a list of ``Books``.

        :param book_ids: list of book ``Ids``
        :type book_ids: ``osid.id.IdList``
        :return: list of comments
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``book_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_book_ids_by_comment(self, comment_id):
        """Gets the list of ``Book``  ``Ids`` mapped to a ``Comment``.

        :param comment_id: ``Id`` of a ``Comment``
        :type comment_id: ``osid.id.Id``
        :return: list of book ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``comment_id`` is not found
        :raise: ``NullArgument`` -- ``comment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_books_by_comment(self, comment_id):
        """Gets the list of ``Book`` objects mapped to a ``Comment``.

        :param comment_id: ``Id`` of a ``Comment``
        :type comment_id: ``osid.id.Id``
        :return: list of books
        :rtype: ``osid.commenting.BookList``
        :raise: ``NotFound`` -- ``comment_id`` is not found
        :raise: ``NullArgument`` -- ``comment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.commenting.CommentBookAssignmentSession

    def can_assign_comments(self):
        """Tests if this user can alter comment/book mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_comments_to_book(self, book_id):
        """Tests if this user can alter comment/book mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_book_ids(self, book_id):
        """Gets a list of books including and under the given book node in which any comment can be assigned.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :return: list of assignable book ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_book_ids_for_comment(self, book_id, comment_id):
        """Gets a list of books including and under the given book node in which a specific comment can be assigned.

        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :param comment_id: the ``Id`` of the ``Comment``
        :type comment_id: ``osid.id.Id``
        :return: list of assignable book ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``book_id`` or ``comment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_comment_to_book(self, comment_id, book_id):
        """Adds an existing ``Comment`` to a ``Book``.

        :param comment_id: the ``Id`` of the ``Comment``
        :type comment_id: ``osid.id.Id``
        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``comment_id`` is already assigned to ``book_id``
        :raise: ``NotFound`` -- ``comment_id`` or ``book_id`` not found
        :raise: ``NullArgument`` -- ``comment_id`` or ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_comment_from_book(self, comment_id, book_id):
        """Removes a ``Comment`` from a ``Book``.

        :param comment_id: the ``Id`` of the ``Comment``
        :type comment_id: ``osid.id.Id``
        :param book_id: the ``Id`` of the ``Book``
        :type book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``comment_id`` or ``book_id`` not found or ``comment_id`` not assigned to ``book_id``
        :raise: ``NullArgument`` -- ``comment_id`` or ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.commenting.CommentSmartBookSession

    def can_manage_smart_books(self):
        """Tests if this user can manage smart books.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart book management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_comment_query(self, comment_query):
        """Applies a comment query to this book.

        :param comment_query: the comment query
        :type comment_query: ``osid.commenting.CommentQuery``
        :raise: ``NullArgument`` -- ``comment_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``comment_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_comment_query(self):
        """Gets a comment query inspector for this book.

        :return: the comment query inspector
        :rtype: ``osid.commenting.CommentQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_comment_sequencing(self, comment_search_order):
        """Applies a comment search order to this book.

        :param comment_search_order: the comment search order
        :type comment_search_order: ``osid.commenting.CommentSearchOrder``
        :raise: ``NullArgument`` -- ``comment_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``comment_search_order`` not of this service

        """
        raise UNIMPLEMENTED()



class BookList(osid.OsidList):

    def get_next_book(self):
        """Gets the next ``Book`` in this list.

        :return: the next ``Book`` in this list. The ``has_next()`` method should be used to test that a next ``Book`` is available before calling this method.
        :rtype: ``osid.commenting.Book``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    next_book = property(fget=get_next_book)

    def get_next_books(self, n):
        """Gets the next set of ``Book`` elements in this list.
        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Book`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Book`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.commenting.Book``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()



class Books(CommentingManager):
    pass

