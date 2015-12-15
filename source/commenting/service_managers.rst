

Service Managers
================


Commenting Manager
------------------

.. py:class:: CommentingManager(osid_managers.OsidManager, CommentingProfile, commenting_managers.CommentingManager)
    The commenting manager provides access to commenting sessions and provides interoperability
        tests
    for various aspects of this service.


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





    .. py:method:: get_comment_lookup_session():
        :noindex:


    .. py:attribute:: comment_lookup_session
        :noindex:


    .. py:method:: get_comment_lookup_session_for_book(book_id):
        :noindex:


    .. py:method:: get_rating_lookup_session():
        :noindex:


    .. py:attribute:: rating_lookup_session
        :noindex:


    .. py:method:: get_rating_lookup_session_for_book(book_id):
        :noindex:


    .. py:method:: get_comment_query_session():
        :noindex:


    .. py:attribute:: comment_query_session
        :noindex:


    .. py:method:: get_comment_query_session_for_book(book_id):
        :noindex:


    .. py:method:: get_comment_search_session():
        :noindex:


    .. py:attribute:: comment_search_session
        :noindex:


    .. py:method:: get_comment_search_session_for_book(book_id):
        :noindex:


    .. py:method:: get_comment_admin_session():
        :noindex:


    .. py:attribute:: comment_admin_session
        :noindex:


    .. py:method:: get_comment_admin_session_for_book(book_id):
        :noindex:


    .. py:method:: get_comment_notification_session(comment_receiver):
        :noindex:


    .. py:method:: get_comment_notification_session_for_book(comment_receiver, book_id):
        :noindex:


    .. py:method:: get_comment_book_session():
        :noindex:


    .. py:attribute:: comment_book_session
        :noindex:


    .. py:method:: get_comment_book_assignment_session():
        :noindex:


    .. py:attribute:: comment_book_assignment_session
        :noindex:


    .. py:method:: get_comment_smart_book_session(book_id):
        :noindex:


    .. py:method:: get_book_lookup_session():
        :noindex:


    .. py:attribute:: book_lookup_session
        :noindex:


    .. py:method:: get_book_query_session():
        :noindex:


    .. py:attribute:: book_query_session
        :noindex:


    .. py:method:: get_book_search_session():
        :noindex:


    .. py:attribute:: book_search_session
        :noindex:


    .. py:method:: get_book_admin_session():
        :noindex:


    .. py:attribute:: book_admin_session
        :noindex:


    .. py:method:: get_book_notification_session(book_receiver):
        :noindex:


    .. py:method:: get_book_hierarchy_session():
        :noindex:


    .. py:attribute:: book_hierarchy_session
        :noindex:


    .. py:method:: get_book_hierarchy_design_session():
        :noindex:


    .. py:attribute:: book_hierarchy_design_session
        :noindex:


    .. py:method:: get_commenting_batch_manager():
        :noindex:


    .. py:attribute:: commenting_batch_manager
        :noindex:




Book Lookup Methods
-------------------

    .. py:method:: can_lookup_books():
        Tests if this user can perform ``Book`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_book_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_book_view():
        A complete view of the ``Book`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_book(book_id):
        Gets the ``Book`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Book`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Book`` and retained for compatibility.

        :arg:    book_id (osid.id.Id): ``Id`` of the ``Book``
        :return: (osid.commenting.Book) - the book
        :raises:  NotFound - ``book_id`` not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_books_by_ids(book_ids):
        Gets a ``BookList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the books
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Books`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :arg:    book_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.commenting.BookList) - the returned ``Book`` list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``book_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_books_by_genus_type(book_genus_type):
        Gets a ``BookList`` corresponding to the given book genus ``Type`` which does not include
            books of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :arg:    book_genus_type (osid.type.Type): a book genus type
        :return: (osid.commenting.BookList) - the returned ``Book`` list
        :raises:  NullArgument - ``book_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_books_by_parent_genus_type(book_genus_type):
        Gets a ``BookList`` corresponding to the given book genus ``Type`` and include any
            additional books with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :arg:    book_genus_type (osid.type.Type): a book genus type
        :return: (osid.commenting.BookList) - the returned ``Book`` list
        :raises:  NullArgument - ``book_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_books_by_record_type(book_record_type):
        Gets a ``BookList`` containing the given book record ``Type``.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :arg:    book_record_type (osid.type.Type): a book record type
        :return: (osid.commenting.BookList) - the returned ``Book`` list
        :raises:  NullArgument - ``book_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_books_by_provider(resource_id):
        Gets a ``BookList`` from the given provider ````.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.commenting.BookList) - the returned ``Book`` list
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_books():
        Gets all ``Books``.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :return: (osid.commenting.BookList) - a list of ``Books``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: books




Book Admin Methods
------------------

    .. py:method:: can_create_books():
        Tests if this user can create ``Books``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Book`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_book_with_record_types(book_record_types):
        Tests if this user can create a single ``Book`` using the desired record types.

        While ``CommentingManager.getBookRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Book``.
        Providing an empty array tests if a ``Book`` can be created with
        no records.

        :arg:    book_record_types (osid.type.Type[]): array of book
                record types
        :return: (boolean) - ``true`` if ``Book`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``book_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_book_form_for_create(book_record_types):
        Gets the book form for creating new books.

        A new form should be requested for each create transaction.

        :arg:    book_record_types (osid.type.Type[]): array of book
                record types
        :return: (osid.commenting.BookForm) - the book form
        :raises:  NullArgument - ``book_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_book(book_form):
        Creates a new ``Book``.

        :arg:    book_form (osid.commenting.BookForm): the form for this
                ``Book``
        :return: (osid.commenting.Book) - the new ``Book``
        :raises:  IllegalState - ``book_form`` already used in a create
                transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``book_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``book_form`` did not originte from
                ``get_book_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_books():
        Tests if this user can update ``Books``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Book`` modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_book_form_for_update(book_id):
        Gets the book form for updating an existing book.

        A new book form should be requested for each update transaction.

        :arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        :return: (osid.commenting.BookForm) - the book form
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_book(book_form):
        Updates an existing book.

        :arg:    book_form (osid.commenting.BookForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``book_form`` already used in an update
                transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``book_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``book_form`` did not originte from
                ``get_book_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_books():
        Tests if this user can delete ``Books`` A return of true does not guarantee successful
            authorization.

        A return of false indicates that it is known deleting a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Book`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_book(book_id):
        Deletes a ``Book``.

        :arg:    book_id (osid.id.Id): the ``Id`` of the ``Book`` to
                remove
        :raises:  NotFound - ``book_id`` not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_book_aliases():
        Tests if this user can manage ``Id`` aliases for ``Books``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Book`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_book(book_id, alias_id):
        Adds an ``Id`` to a ``Book`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Book`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another book, it is
        reassigned to the given book ``Id``.

        :arg:    book_id (osid.id.Id): the ``Id`` of a ``Book``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``book_id`` not found
        :raises:  NullArgument - ``book_id`` or ``alias_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Book Hierarchy Methods
----------------------

    .. py:method:: get_book_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: book_hierarchy_id


    .. py:method:: get_book_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: book_hierarchy


    .. py:method:: can_access_book_hierarchy():
        Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_book_view():
        The returns from the book methods may omit or translate elements based on this session, such
            as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_book_view():
        A complete view of the ``Book`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_root_book_ids():
        Gets the root book ``Ids`` in this hierarchy.

        :return: (osid.id.IdList) - the root book ``Ids``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: root_book_ids


    .. py:method:: get_root_books():
        Gets the root books in the book hierarchy.

        A node with no parents is an orphan. While all book ``Ids`` are
        known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        :return: (osid.commenting.BookList) - the root books
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:attribute:: root_books


    .. py:method:: has_parent_books(book_id):
        Tests if the ``Book`` has any parents.

        :arg:    book_id (osid.id.Id): a book ``Id``
        :return: (boolean) - ``true`` if the book has parents, f ``alse``
                otherwise
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_parent_of_book(id_, book_id):
        Tests if an ``Id`` is a direct parent of book.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :return: (boolean) - ``true`` if this ``id`` is a parent of
                ``book_id,`` f ``alse`` otherwise
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``id`` or ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_parent_book_ids(book_id):
        Gets the parent ``Ids`` of the given book.

        :arg:    book_id (osid.id.Id): a book ``Id``
        :return: (osid.id.IdList) - the parent ``Ids`` of the book
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_parent_books(book_id):
        Gets the parent books of the given ``id``.

        :arg:    book_id (osid.id.Id): the ``Id`` of the ``Book`` to
                query
        :return: (osid.commenting.BookList) - the parent books of the
                ``id``
        :raises:  NotFound - a ``Book`` identified by ``Id is`` not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_ancestor_of_book(id_, book_id):
        Tests if an ``Id`` is an ancestor of a book.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :return: (boolean) - ``tru`` e if this ``id`` is an ancestor of
                ``book_id,``  ``false`` otherwise
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``id`` or ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: has_child_books(book_id):
        Tests if a book has any children.

        :arg:    book_id (osid.id.Id): a book ``Id``
        :return: (boolean) - ``true`` if the ``book_id`` has children,
                ``false`` otherwise
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_child_of_book(id_, book_id):
        Tests if a book is a direct child of another.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :return: (boolean) - ``true`` if the ``id`` is a child of
                ``book_id,``  ``false`` otherwise
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``id`` or ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_child_book_ids(book_id):
        Gets the child ``Ids`` of the given book.

        :arg:    book_id (osid.id.Id): the ``Id`` to query
        :return: (osid.id.IdList) - the children of the book
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_child_books(book_id):
        Gets the child books of the given ``id``.

        :arg:    book_id (osid.id.Id): the ``Id`` of the ``Book`` to
                query
        :return: (osid.commenting.BookList) - the child books of the
                ``id``
        :raises:  NotFound - a ``Book`` identified by ``Id is`` not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_descendant_of_book(id_, book_id):
        Tests if an ``Id`` is a descendant of a book.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``book_id,``  ``false`` otherwise
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``id`` or ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.




    .. py:method:: get_book_node_ids(book_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given book.

        :arg:    book_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.hierarchy.Node) - a book node
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_book_nodes(book_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given book.

        :arg:    book_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.commenting.BookNode) - a book node
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Book Hierarchy Design Methods
-----------------------------

    .. py:method:: get_book_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: book_hierarchy_id


    .. py:method:: get_book_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: book_hierarchy


    .. py:method:: can_modify_book_hierarchy():
        Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_root_book(book_id):
        Adds a root book.

        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :raises:  AlreadyExists - ``book_id`` is already in hierarchy
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_root_book(book_id):
        Removes a root book.

        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :raises:  NotFound - ``book_id`` is not a root
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_child_book(book_id, child_id):
        Adds a child to a book.

        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  AlreadyExists - ``book_id`` is already a parent of
                ``child_id``
        :raises:  NotFound - ``book_id`` or ``child_id`` not found
        :raises:  NullArgument - ``book_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_book(book_id, child_id):
        Removes a child from a book.

        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  NotFound - ``book_id`` not a parent of ``child_id``
        :raises:  NullArgument - ``book_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_books(book_id):
        Removes all children from a book.

        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :raises:  NotFound - ``book_id`` not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Commenting Proxy Manager
------------------------

.. py:class:: CommentingProxyManager(osid_managers.OsidProxyManager, CommentingProfile, commenting_managers.CommentingProxyManager)
    The commenting manager provides access to commenting sessions and provides interoperability
        tests
    for various aspects of this service.


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





    .. py:method:: get_comment_lookup_session(proxy):
        :noindex:


    .. py:method:: get_comment_lookup_session_for_book(book_id, proxy):
        :noindex:


    .. py:method:: get_rating_lookup_session(proxy):
        :noindex:


    .. py:method:: get_rating_lookup_session_for_book(book_id, proxy):
        :noindex:


    .. py:method:: get_comment_query_session(proxy):
        :noindex:


    .. py:method:: get_comment_query_session_for_book(book_id, proxy):
        :noindex:


    .. py:method:: get_comment_search_session(proxy):
        :noindex:


    .. py:method:: get_comment_search_session_for_book(book_id, proxy):
        :noindex:


    .. py:method:: get_comment_admin_session(proxy):
        :noindex:


    .. py:method:: get_comment_admin_session_for_book(book_id, proxy):
        :noindex:


    .. py:method:: get_comment_notification_session(comment_receiver, proxy):
        :noindex:


    .. py:method:: get_comment_notification_session_for_book(comment_receiver, book_id, proxy):
        :noindex:


    .. py:method:: get_comment_book_session(proxy):
        :noindex:


    .. py:method:: get_comment_book_assignment_session(proxy):
        :noindex:


    .. py:method:: get_comment_smart_book_session(book_id, proxy):
        :noindex:


    .. py:method:: get_book_lookup_session(proxy):
        :noindex:


    .. py:method:: get_book_query_session(proxy):
        :noindex:


    .. py:method:: get_book_search_session(proxy):
        :noindex:


    .. py:method:: get_book_admin_session(proxy):
        :noindex:


    .. py:method:: get_book_notification_session(book_receiver, proxy):
        :noindex:


    .. py:method:: get_book_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_book_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_commenting_batch_proxy_manager():
        :noindex:


    .. py:attribute:: commenting_batch_proxy_manager
        :noindex:




Book Lookup Methods
-------------------

    .. py:method:: can_lookup_books():
        Tests if this user can perform ``Book`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_book_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_book_view():
        A complete view of the ``Book`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_book(book_id):
        Gets the ``Book`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Book`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Book`` and retained for compatibility.

        :arg:    book_id (osid.id.Id): ``Id`` of the ``Book``
        :return: (osid.commenting.Book) - the book
        :raises:  NotFound - ``book_id`` not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_books_by_ids(book_ids):
        Gets a ``BookList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the books
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Books`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :arg:    book_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.commenting.BookList) - the returned ``Book`` list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``book_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_books_by_genus_type(book_genus_type):
        Gets a ``BookList`` corresponding to the given book genus ``Type`` which does not include
            books of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :arg:    book_genus_type (osid.type.Type): a book genus type
        :return: (osid.commenting.BookList) - the returned ``Book`` list
        :raises:  NullArgument - ``book_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_books_by_parent_genus_type(book_genus_type):
        Gets a ``BookList`` corresponding to the given book genus ``Type`` and include any
            additional books with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :arg:    book_genus_type (osid.type.Type): a book genus type
        :return: (osid.commenting.BookList) - the returned ``Book`` list
        :raises:  NullArgument - ``book_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_books_by_record_type(book_record_type):
        Gets a ``BookList`` containing the given book record ``Type``.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :arg:    book_record_type (osid.type.Type): a book record type
        :return: (osid.commenting.BookList) - the returned ``Book`` list
        :raises:  NullArgument - ``book_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_books_by_provider(resource_id):
        Gets a ``BookList`` from the given provider ````.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.commenting.BookList) - the returned ``Book`` list
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_books():
        Gets all ``Books``.

        In plenary mode, the returned list contains all known books or
        an error results. Otherwise, the returned list may contain only
        those books that are accessible through this session.

        :return: (osid.commenting.BookList) - a list of ``Books``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: books




Book Admin Methods
------------------

    .. py:method:: can_create_books():
        Tests if this user can create ``Books``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Book`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_book_with_record_types(book_record_types):
        Tests if this user can create a single ``Book`` using the desired record types.

        While ``CommentingManager.getBookRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Book``.
        Providing an empty array tests if a ``Book`` can be created with
        no records.

        :arg:    book_record_types (osid.type.Type[]): array of book
                record types
        :return: (boolean) - ``true`` if ``Book`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``book_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_book_form_for_create(book_record_types):
        Gets the book form for creating new books.

        A new form should be requested for each create transaction.

        :arg:    book_record_types (osid.type.Type[]): array of book
                record types
        :return: (osid.commenting.BookForm) - the book form
        :raises:  NullArgument - ``book_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_book(book_form):
        Creates a new ``Book``.

        :arg:    book_form (osid.commenting.BookForm): the form for this
                ``Book``
        :return: (osid.commenting.Book) - the new ``Book``
        :raises:  IllegalState - ``book_form`` already used in a create
                transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``book_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``book_form`` did not originte from
                ``get_book_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_books():
        Tests if this user can update ``Books``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Book`` modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_book_form_for_update(book_id):
        Gets the book form for updating an existing book.

        A new book form should be requested for each update transaction.

        :arg:    book_id (osid.id.Id): the ``Id`` of the ``Book``
        :return: (osid.commenting.BookForm) - the book form
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_book(book_form):
        Updates an existing book.

        :arg:    book_form (osid.commenting.BookForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``book_form`` already used in an update
                transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``book_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``book_form`` did not originte from
                ``get_book_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_books():
        Tests if this user can delete ``Books`` A return of true does not guarantee successful
            authorization.

        A return of false indicates that it is known deleting a ``Book``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Book`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_book(book_id):
        Deletes a ``Book``.

        :arg:    book_id (osid.id.Id): the ``Id`` of the ``Book`` to
                remove
        :raises:  NotFound - ``book_id`` not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_book_aliases():
        Tests if this user can manage ``Id`` aliases for ``Books``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Book`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_book(book_id, alias_id):
        Adds an ``Id`` to a ``Book`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Book`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another book, it is
        reassigned to the given book ``Id``.

        :arg:    book_id (osid.id.Id): the ``Id`` of a ``Book``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``book_id`` not found
        :raises:  NullArgument - ``book_id`` or ``alias_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Book Hierarchy Methods
----------------------

    .. py:method:: get_book_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: book_hierarchy_id


    .. py:method:: get_book_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: book_hierarchy


    .. py:method:: can_access_book_hierarchy():
        Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_book_view():
        The returns from the book methods may omit or translate elements based on this session, such
            as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_book_view():
        A complete view of the ``Book`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_root_book_ids():
        Gets the root book ``Ids`` in this hierarchy.

        :return: (osid.id.IdList) - the root book ``Ids``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: root_book_ids


    .. py:method:: get_root_books():
        Gets the root books in the book hierarchy.

        A node with no parents is an orphan. While all book ``Ids`` are
        known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        :return: (osid.commenting.BookList) - the root books
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:attribute:: root_books


    .. py:method:: has_parent_books(book_id):
        Tests if the ``Book`` has any parents.

        :arg:    book_id (osid.id.Id): a book ``Id``
        :return: (boolean) - ``true`` if the book has parents, f ``alse``
                otherwise
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_parent_of_book(id_, book_id):
        Tests if an ``Id`` is a direct parent of book.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :return: (boolean) - ``true`` if this ``id`` is a parent of
                ``book_id,`` f ``alse`` otherwise
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``id`` or ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_parent_book_ids(book_id):
        Gets the parent ``Ids`` of the given book.

        :arg:    book_id (osid.id.Id): a book ``Id``
        :return: (osid.id.IdList) - the parent ``Ids`` of the book
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_parent_books(book_id):
        Gets the parent books of the given ``id``.

        :arg:    book_id (osid.id.Id): the ``Id`` of the ``Book`` to
                query
        :return: (osid.commenting.BookList) - the parent books of the
                ``id``
        :raises:  NotFound - a ``Book`` identified by ``Id is`` not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_ancestor_of_book(id_, book_id):
        Tests if an ``Id`` is an ancestor of a book.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :return: (boolean) - ``tru`` e if this ``id`` is an ancestor of
                ``book_id,``  ``false`` otherwise
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``id`` or ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: has_child_books(book_id):
        Tests if a book has any children.

        :arg:    book_id (osid.id.Id): a book ``Id``
        :return: (boolean) - ``true`` if the ``book_id`` has children,
                ``false`` otherwise
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_child_of_book(id_, book_id):
        Tests if a book is a direct child of another.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :return: (boolean) - ``true`` if the ``id`` is a child of
                ``book_id,``  ``false`` otherwise
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``id`` or ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_child_book_ids(book_id):
        Gets the child ``Ids`` of the given book.

        :arg:    book_id (osid.id.Id): the ``Id`` to query
        :return: (osid.id.IdList) - the children of the book
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_child_books(book_id):
        Gets the child books of the given ``id``.

        :arg:    book_id (osid.id.Id): the ``Id`` of the ``Book`` to
                query
        :return: (osid.commenting.BookList) - the child books of the
                ``id``
        :raises:  NotFound - a ``Book`` identified by ``Id is`` not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_descendant_of_book(id_, book_id):
        Tests if an ``Id`` is a descendant of a book.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``book_id,``  ``false`` otherwise
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``id`` or ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.




    .. py:method:: get_book_node_ids(book_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given book.

        :arg:    book_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.hierarchy.Node) - a book node
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_book_nodes(book_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given book.

        :arg:    book_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.commenting.BookNode) - a book node
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Book Hierarchy Design Methods
-----------------------------

    .. py:method:: get_book_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: book_hierarchy_id


    .. py:method:: get_book_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: book_hierarchy


    .. py:method:: can_modify_book_hierarchy():
        Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_root_book(book_id):
        Adds a root book.

        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :raises:  AlreadyExists - ``book_id`` is already in hierarchy
        :raises:  NotFound - ``book_id`` is not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_root_book(book_id):
        Removes a root book.

        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :raises:  NotFound - ``book_id`` is not a root
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_child_book(book_id, child_id):
        Adds a child to a book.

        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  AlreadyExists - ``book_id`` is already a parent of
                ``child_id``
        :raises:  NotFound - ``book_id`` or ``child_id`` not found
        :raises:  NullArgument - ``book_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_book(book_id, child_id):
        Removes a child from a book.

        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  NotFound - ``book_id`` not a parent of ``child_id``
        :raises:  NullArgument - ``book_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_books(book_id):
        Removes all children from a book.

        :arg:    book_id (osid.id.Id): the ``Id`` of a book
        :raises:  NotFound - ``book_id`` not found
        :raises:  NullArgument - ``book_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






