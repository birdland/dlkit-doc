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

from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects
from ..osid import records as osid_records
from ..osid import queries as osid_queries
from ..osid import searches as osid_searches


class CommentingProfile(osid_managers.OsidProfile):
    """The commenting profile describes the interoperability among commenting services."""

    def __init__(self):
        self._provider_manager = None


    def supports_comment_lookup(self):
        """Tests for the availability of a comment lookup service.

        :return: ``true`` if comment lookup is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_comment_query(self):
        """Tests if querying comments is available.

        :return: ``true`` if comment query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_comment_admin(self):
        """Tests if managing comments is available.

        :return: ``true`` if comment admin is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_book_lookup(self):
        """Tests for the availability of an book lookup service.

        :return: ``true`` if book lookup is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_book_admin(self):
        """Tests for the availability of a book administrative service for creating and deleting books.

        :return: ``true`` if book administration is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_book_hierarchy(self):
        """Tests for the availability of a book hierarchy traversal service.

        :return: ``true`` if book hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_book_hierarchy_design(self):
        """Tests for the availability of a book hierarchy design service.

        :return: ``true`` if book hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return # boolean

    def get_comment_record_types(self):
        """Gets the supported ``Comment`` record types.

        :return: a list containing the supported comment record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    comment_record_types = property(fget=get_comment_record_types)

    def get_comment_search_record_types(self):
        """Gets the supported comment search record types.

        :return: a list containing the supported comment search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    comment_search_record_types = property(fget=get_comment_search_record_types)

    def get_book_record_types(self):
        """Gets the supported ``Book`` record types.

        :return: a list containing the supported book record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    book_record_types = property(fget=get_book_record_types)

    def get_book_search_record_types(self):
        """Gets the supported book search record types.

        :return: a list containing the supported book search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    book_search_record_types = property(fget=get_book_search_record_types)
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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_book_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_book_view(self):
        """A complete view of the ``Book`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.commenting.Book

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

    def get_books(self):
        """Gets all ``Books``.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :return: a list of ``Books``
        :rtype: ``osid.commenting.BookList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

    books = property(fget=get_books)


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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.Book

    def can_update_books(self):
        """Tests if this user can update ``Books``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Book`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_books(self):
        """Tests if this user can delete ``Books`` A return of true does not guarantee successful authorization.

        A return of false indicates that it is known deleting a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Book`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_book(self, book_id):
        """Deletes a ``Book``.

        :param book_id: the ``Id`` of the ``Book`` to remove
        :type book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``book_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_book_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Books``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Book`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.commenting.BookHierarchySession

    def get_book_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    book_hierarchy_id = property(fget=get_book_hierarchy_id)

    def get_book_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_book_view(self):
        """The returns from the book methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_book_view(self):
        """A complete view of the ``Book`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_root_book_ids(self):
        """Gets the root book ``Ids`` in this hierarchy.

        :return: the root book ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Node

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookNode


##
# The following methods are from osid.commenting.BookHierarchyDesignSession

    def get_book_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    book_hierarchy_id = property(fget=get_book_hierarchy_id)

    def get_book_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    book_hierarchy = property(fget=get_book_hierarchy)

    def can_modify_book_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def add_root_book(self, book_id):
        """Adds a root book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``book_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_root_book(self, book_id):
        """Removes a root book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``book_id`` is not a root
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_books(self, book_id):
        """Removes all children from a book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``book_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




class CommentingManager(osid_managers.OsidManager, osid_sessions.OsidSession, CommentingProfile):
    """The commenting manager provides access to commenting sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``CommentLookupSession:`` a session to lookup comments
      * ``RatingLookupSession:`` a session to lookup comments
      * ``CommentQuerySession:`` a session to query comments
      * ``CommentSearchSession:`` a session to search comments
      * ``CommentAdminSession:`` a session to manage comments
      * ``CommentNotificationSession:`` a session to subscribe to
        notifications of comment changes
      * ``CommentBookSession:`` a session for looking up comment and
        book mappings
      * ``CommentBookAssignmentSession:`` a session for managing comment
        and book mappings
      * ``CommentSmartBookSession:`` a session to manage dynamic comment
        books
      * ``BookLookupSession:`` a session to retrieve books
      * ``BookQuerySession:`` a session to query books
      * ``BookSearchSession:`` a session to search for books
      * ``BookAdminSession:`` a session to create, update and delete
        books
      * ``BookNotificationSession:`` a session to receive notifications
        for changes in books
      * ``BookHierarchyTraversalSession:`` a session to traverse
        hierarchies of books
      * ``BookHierarchyDesignSession:`` a session to manage hierarchies
        of books


    The commenting manager also provides a profile for determing the
    supported search types supported by this service.

    """

    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._book_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)
        self._sub_package_provider_managers = dict()

    def _set_book_view(self, session):
        """Sets the underlying book view to match current view"""
        if self._book_view == COMPARATIVE:
            try:
                session.use_comparative_book_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_book_view()
            except AttributeError:
                pass

    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_book_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _get_sub_package_provider_manager(self, sub_package_name):
        if sub_package_name in self._sub_package_provider_managers:
            return self._sub_package_provider_managers[sub_package_name]
        config = self._runtime.get_configuration()
        parameter_id = Id('parameter:{0}ProviderImpl@dlkit_service'.format(sub_package_name))
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            sub_package = self._runtime.get_manager(sub_package_name.upper(), provider_impl)
        else:
            # need to add version argument
            sub_package = self._runtime.get_proxy_manager(sub_package_name.upper(), provider_impl)
        self._sub_package_provider_managers[sub_package_name] = sub_package
        return sub_package

    def _get_sub_package_provider_session(self, sub_package, session_name, proxy=None):
        """Gets the session from a sub-package"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            manager = self._get_sub_package_provider_manager(sub_package)
            session = self._instantiate_session('get_' + session_name + '_for_bank',
                                                proxy=self._proxy,
                                                manager=manager)
            self._set_bank_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _instantiate_session(self, method_name, proxy=None, *args, **kwargs):
        """Instantiates a provider session"""
        session_class = getattr(self._provider_manager, method_name)
        if proxy is None:
            try:
                return session_class(bank_id=self._catalog_id, *args, **kwargs)
            except AttributeError:
                return session_class(*args, **kwargs)
        else:
            try:
                return session_class(bank_id=self._catalog_id, proxy=proxy, *args, **kwargs)
            except AttributeError:
                return session_class(proxy=proxy, *args, **kwargs)

    def initialize(self, runtime):
        """OSID Manager initialize"""
        from .primitives import Id
        if self._runtime is not None:
            raise IllegalState('Manager has already been initialized')
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:commentingProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('COMMENTING', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('COMMENTING', provider_impl)

    def close_sessions(self):
        """Close all sessions, unless session management is set to MANDATORY"""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()

    def use_automatic_session_management(self):
        """Session state will be saved unless closed by consumers"""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will be saved and can not be closed by consumers"""
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved"""
        self._session_management = DISABLED
        self.close_sessions()

    def get_commenting_batch_manager(self):
        """Gets a ``CommentingBatchManager``.

        :return: a ``CommentingBatchManager``
        :rtype: ``osid.commenting.batch.CommentingBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commenting_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commenting_batch()`` is ``true``.*

        """
        return # osid.commenting.batch.CommentingBatchManager

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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_book_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_book_view(self):
        """A complete view of the ``Book`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.commenting.Book

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

    def get_books(self):
        """Gets all ``Books``.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :return: a list of ``Books``
        :rtype: ``osid.commenting.BookList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

    books = property(fget=get_books)


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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.Book

    def can_update_books(self):
        """Tests if this user can update ``Books``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Book`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_books(self):
        """Tests if this user can delete ``Books`` A return of true does not guarantee successful authorization.

        A return of false indicates that it is known deleting a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Book`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_book(self, book_id):
        """Deletes a ``Book``.

        :param book_id: the ``Id`` of the ``Book`` to remove
        :type book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``book_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_book_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Books``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Book`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.commenting.BookHierarchySession

    def get_book_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    book_hierarchy_id = property(fget=get_book_hierarchy_id)

    def get_book_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_book_view(self):
        """The returns from the book methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_book_view(self):
        """A complete view of the ``Book`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_root_book_ids(self):
        """Gets the root book ``Ids`` in this hierarchy.

        :return: the root book ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Node

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookNode


##
# The following methods are from osid.commenting.BookHierarchyDesignSession

    def get_book_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    book_hierarchy_id = property(fget=get_book_hierarchy_id)

    def get_book_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    book_hierarchy = property(fget=get_book_hierarchy)

    def can_modify_book_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def add_root_book(self, book_id):
        """Adds a root book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``book_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_root_book(self, book_id):
        """Removes a root book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``book_id`` is not a root
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_books(self, book_id):
        """Removes all children from a book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``book_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




class CommentingProxyManager(osid_managers.OsidProxyManager, CommentingProfile):
    """The commenting manager provides access to commenting sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager accept a ``Proxy`` for passing information
    from a server environment. The sessions included in this manager
    are:

      * ``CommentLookupSession:`` a session to lookup comments
      * ``RatingLookupSession:`` a session to lookup comments
      * ``CommentQuerySession:`` a session to query comments
      * ``CommentSearchSession:`` a session to search comments
      * ``CommentAdminSession:`` a session to manage comments
      * ``CommentNotificationSession:`` a session to subscribe to
        notifications of comment changes
      * ``CommentBookSession:`` a session for looking up comment and
        book mappings
      * ``CommentBookAssignmentSession:`` a session for managing comment
        and book mappings
      * ``CommentSmartBookSession:`` a session to manage dynamic comment
        books
      * ``BookLookupSession:`` a session to retrieve books
      * ``BookQuerySession:`` a session to query books
      * ``BookSearchSession:`` a session to search for books
      * ``BookAdminSession:`` a session to create, update and delete
        books
      * ``BookNotificationSession:`` a session to receive notifications
        for changes in books
      * ``BookHierarchyTraversalSession:`` a session to traverse
        hierarchies of books
      * ``BookHierarchyDesignSession:`` a session to manage hierarchies
        of books


    The commenting manager also provides a profile for determing the
    supported search types supported by this service.

    """

    def get_commenting_batch_proxy_manager(self):
        """Gets a ``CommentingBatchProxyManager``.

        :return: a ``CommentingBatchProxyManager``
        :rtype: ``osid.commenting.batch.CommentingBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commenting_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_commenting_batch()`` is ``true``.*

        """
        return # osid.commenting.batch.CommentingBatchProxyManager

    commenting_batch_proxy_manager = property(fget=get_commenting_batch_proxy_manager)
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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_book_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_book_view(self):
        """A complete view of the ``Book`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.commenting.Book

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

    def get_books(self):
        """Gets all ``Books``.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :return: a list of ``Books``
        :rtype: ``osid.commenting.BookList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

    books = property(fget=get_books)


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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.Book

    def can_update_books(self):
        """Tests if this user can update ``Books``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Book`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_books(self):
        """Tests if this user can delete ``Books`` A return of true does not guarantee successful authorization.

        A return of false indicates that it is known deleting a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Book`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_book(self, book_id):
        """Deletes a ``Book``.

        :param book_id: the ``Id`` of the ``Book`` to remove
        :type book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``book_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_book_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Books``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Book`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.commenting.BookHierarchySession

    def get_book_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    book_hierarchy_id = property(fget=get_book_hierarchy_id)

    def get_book_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_book_view(self):
        """The returns from the book methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_book_view(self):
        """A complete view of the ``Book`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_root_book_ids(self):
        """Gets the root book ``Ids`` in this hierarchy.

        :return: the root book ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Node

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookNode


##
# The following methods are from osid.commenting.BookHierarchyDesignSession

    def get_book_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    book_hierarchy_id = property(fget=get_book_hierarchy_id)

    def get_book_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    book_hierarchy = property(fget=get_book_hierarchy)

    def can_modify_book_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def add_root_book(self, book_id):
        """Adds a root book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``book_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``book_id`` is not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_root_book(self, book_id):
        """Removes a root book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``book_id`` is not a root
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_books(self, book_id):
        """Removes all children from a book.

        :param book_id: the ``Id`` of a book
        :type book_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``book_id`` not found
        :raise: ``NullArgument`` -- ``book_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




class Book(osid_objects.OsidCatalog, osid_sessions.OsidSession):
    """A ``Book`` represents a collection of comments.

    Like all OSID objects, a ``Book`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """

    # WILL THIS EVER BE CALLED DIRECTLY - OUTSIDE OF A MANAGER?
    def __init__(self, provider_manager, catalog, runtime, proxy, **kwargs):
        self._provider_manager = provider_manager
        self._catalog = catalog
        self._runtime = runtime
        osid.OsidObject.__init__(self, self._catalog)  # This is to initialize self._object
        osid.OsidSession.__init__(self, proxy)  # This is to initialize self._proxy
        self._catalog_id = catalog.get_id()
        self._provider_sessions = kwargs
        self._session_management = AUTOMATIC
        self._book_view = DEFAULT
        self._object_views = dict()
        self._operable_views = dict()
        self._containable_views = dict()

    def _set_book_view(self, session):
        """Sets the underlying book view to match current view"""
        if self._book_view == FEDERATED:
            try:
                session.use_federated_book_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_book_view()
            except AttributeError:
                pass

    def _set_object_view(self, session):
        """Sets the underlying object views to match current view"""
        for obj_name in self._object_views:
            if self._object_views[obj_name] == PLENARY:
                try:
                    getattr(session, 'use_plenary_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_comparative_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _set_operable_view(self, session):
        """Sets the underlying operable views to match current view"""
        for obj_name in self._operable_views:
            if self._operable_views[obj_name] == ACTIVE:
                try:
                    getattr(session, 'use_active_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_any_status_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _set_containable_view(self, session):
        """Sets the underlying containable views to match current view"""
        for obj_name in self._containable_views:
            if self._containable_views[obj_name] == SEQUESTERED:
                try:
                    getattr(session, 'use_sequestered_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_unsequestered_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _get_provider_session(self, session_name):
        """Returns the requested provider session.

        Instantiates a new one if the named session is not already known.

        """
        agent_key = self._get_agent_key()
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_book')
            if self._proxy is None:
                session = session_class(self._catalog.get_id())
            else:
                session = session_class(self._catalog.get_id(), self._proxy)
            self._set_book_view(session)
            self._set_object_view(session)
            self._set_operable_view(session)
            self._set_containable_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def get_book_id(self):
        """Gets the Id of this book."""
        return self._catalog_id

    def get_book(self):
        """Strange little method to assure conformance for inherited Sessions."""
        return self

    def get_objective_hierarchy_id(self):
        """WHAT am I doing here?"""
        return self._catalog_id

    def get_objective_hierarchy(self):
        """WHAT am I doing here?"""
        return self

    def __getattr__(self, name):
        if '_catalog' in self.__dict__:
            try:
                return self._catalog[name]
            except AttributeError:
                pass
        raise AttributeError

    def close_sessions(self):
        """Close all sessions currently being managed by this Manager to save memory."""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()
        else:
            raise IllegalState()

    def use_automatic_session_management(self):
        """Session state will be saved until closed by consumers."""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will always be saved and can not be closed by consumers."""
        # Session state will be saved and can not be closed by consumers
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved."""
        self._session_management = DISABLED
        self.close_sessions()

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.records.BookRecord
##
# The following methods are from osid.commenting.CommentLookupSession

    def get_book_id(self):
        """Gets the ``Book``  ``Id`` associated with this session.

        :return: the ``Book Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    book_id = property(fget=get_book_id)

    def get_book(self):
        """Gets the ``Book`` associated with this session.

        :return: the book
        :rtype: ``osid.commenting.Book``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.Book

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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_comment_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_comment_view(self):
        """A complete view of the ``Comment`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_book_view(self):
        """Federates the view for methods in this session.

        A federated view will include comments in books which are
        children of this book in the book hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_book_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this book only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_effective_comment_view(self):
        """Only comments whose effective dates are current are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_any_effective_comment_view(self):
        """All comments of any effective dates are returned by all methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.Comment

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

    def get_comments_by_genus_type(self, comment_genus_type):
        """Gets a ``CommentList`` corresponding to the given comment genus ``Type`` which does not include comments of genus types derived from the specified ``Type``.

        :param comment_genus_type: a comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :return: the returned ``Comment`` list
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``comment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

    def get_comments_by_parent_genus_type(self, comment_genus_type):
        """Gets a ``CommentList`` corresponding to the given comment genus ``Type`` and include any additional comments with genus types derived from the specified ``Type``.

        :param comment_genus_type: a comment genus type
        :type comment_genus_type: ``osid.type.Type``
        :return: the returned ``Comment`` list
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``comment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

    def get_comments_by_record_type(self, comment_record_type):
        """Gets a ``CommentList`` containing the given comment record ``Type``.

        :param comment_record_type: a comment record type
        :type comment_record_type: ``osid.type.Type``
        :return: the returned ``Comment`` list
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``comment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

    def get_comments_for_commentor(self, resource_id):
        """Gets a list of comments corresponding to a resource ``Id``.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

    def get_comments_for_reference(self, reference_id):
        """Gets a list of comments corresponding to a reference ``Id``.

        :param reference_id: the ``Id`` of the reference
        :type reference_id: ``osid.id.Id``
        :return: the returned ``CommentList``
        :rtype: ``osid.commenting.CommentList``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

    def get_comments(self):
        """Gets all comments.

        :return: a list of comments
        :rtype: ``osid.commenting.CommentList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

    comments = property(fget=get_comments)


##
# The following methods are from osid.commenting.CommentQuerySession

    def get_book_id(self):
        """Gets the ``Book``  ``Id`` associated with this session.

        :return: the ``Book Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    book_id = property(fget=get_book_id)

    def get_book(self):
        """Gets the ``Book`` associated with this session.

        :return: the book
        :rtype: ``osid.commenting.Book``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.Book

    book = property(fget=get_book)

    def can_search_comments(self):
        """Tests if this user can perform comment searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not wish to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_federated_book_view(self):
        """Federates the view for methods in this session.

        A federated view will include comments in books which are
        children of this book in the book hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_book_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this book only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_comment_query(self):
        """Gets a comment query.

        :return: the comment query
        :rtype: ``osid.commenting.CommentQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentQuery

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList


##
# The following methods are from osid.commenting.CommentAdminSession

    def get_book_id(self):
        """Gets the ``Book``  ``Id`` associated with this session.

        :return: the ``Book Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    book_id = property(fget=get_book_id)

    def get_book(self):
        """Gets the ``Book`` associated with this session.

        :return: the book
        :rtype: ``osid.commenting.Book``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.Book

    book = property(fget=get_book)

    def can_create_comments(self):
        """Tests if this user can create comments.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Comment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Comment`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.Comment

    def can_update_comments(self):
        """Tests if this user can update comments.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Comment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Comment`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_comments(self):
        """Tests if this user can delete comments.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Comment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Comment`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_comment(self, comment_id):
        """Deletes a ``Comment``.

        :param comment_id: the ``Id`` of the ``Comment`` to remove
        :type comment_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``comment_id`` not found
        :raise: ``NullArgument`` -- ``comment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_comment_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Comnents``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Comment`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




class BookList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``BookList`` provides a means for accessing ``Book`` elements sequentially either one at a time or many at a time.

    Examples: while (bl.hasNext()) { Book book = bl.getNextBook(); }

    or
      while (bl.hasNext()) {
           Book[] books = bl.getNextBooks(bl.available());
      }

    """

    def get_next_book(self):
        """Gets the next ``Book`` in this list.

        :return: the next ``Book`` in this list. The ``has_next()`` method should be used to test that a next ``Book`` is available before calling this method.
        :rtype: ``osid.commenting.Book``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.Book

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.Book


