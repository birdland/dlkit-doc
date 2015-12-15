

Service Catalog
===============


Book
----

.. py:class:: Book(abc_commenting_objects.Book, osid_objects.OsidCatalog)
    A ``Book`` represents a collection of comments.


    Like all OSID objects, a ``Book`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.





    .. py:method:: get_book_record(book_record_type):
        :noindex:




Comment Lookup Methods
----------------------

    .. py:method:: get_book_id():
        Gets the ``Book``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Book Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: book_id


    .. py:method:: get_book():
        Gets the ``Book`` associated with this session.

        :return: (osid.commenting.Book) - the book
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: book


    .. py:method:: can_lookup_comments():
        Tests if this user can examine this book.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer these
        operations.

        :return: (boolean) - ``false`` if book reading methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_comment_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_comment_view():
        A complete view of the ``Comment`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_book_view():
        Federates the view for methods in this session.

        A federated view will include comments in books which are
        children of this book in the book hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_book_view():
        Isolates the view for methods in this session.

        An isolated view restricts retrievals to this book only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_effective_comment_view():
        Only comments whose effective dates are current are returned by methods in this session.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_any_effective_comment_view():
        All comments of any effective dates are returned by all methods in this session.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_comment(comment_id):
        Gets the ``Comment`` specified by its ``Id``.

        :arg:    comment_id (osid.id.Id): the ``Id`` of the ``Comment``
                to retrieve
        :return: (osid.commenting.Comment) - the returned ``Comment``
        :raises:  NotFound - no ``Comment`` found with the given ``Id``
        :raises:  NullArgument - ``comment_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_by_ids(comment_ids):
        Gets a ``CommentList`` corresponding to the given ``IdList``.

        :arg:    comment_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.commenting.CommentList) - the returned ``Comment
                list``
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``comment_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_by_genus_type(comment_genus_type):
        Gets a ``CommentList`` corresponding to the given comment genus ``Type`` which does not
            include comments of genus types derived from the specified ``Type``.

        :arg:    comment_genus_type (osid.type.Type): a comment genus
                type
        :return: (osid.commenting.CommentList) - the returned ``Comment``
                list
        :raises:  NullArgument - ``comment_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_by_parent_genus_type(comment_genus_type):
        Gets a ``CommentList`` corresponding to the given comment genus ``Type`` and include any
            additional comments with genus types derived from the specified ``Type``.

        :arg:    comment_genus_type (osid.type.Type): a comment genus
                type
        :return: (osid.commenting.CommentList) - the returned ``Comment``
                list
        :raises:  NullArgument - ``comment_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_by_record_type(comment_record_type):
        Gets a ``CommentList`` containing the given comment record ``Type``.

        :arg:    comment_record_type (osid.type.Type): a comment record
                type
        :return: (osid.commenting.CommentList) - the returned ``Comment``
                list
        :raises:  NullArgument - ``comment_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_on_date(from_, to):
        Gets a ``CommentList`` effective during the entire given date range inclusive but not
            confined to the date range.

        :arg:    from (osid.calendaring.DateTime): starting date
        :arg:    to (osid.calendaring.DateTime): ending date
        :return: (osid.commenting.CommentList) - the returned ``Comment``
                list
        :raises:  InvalidArgument - ``from`` is greater than ``to``
        :raises:  NullArgument - ``from`` or ``to`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_by_genus_type_on_date(comment_genus_type, from_, to):
        Gets a ``CommentList`` of a given genus type and effective during the entire given date
            range inclusive but not confined to the date range.

        :arg:    comment_genus_type (osid.type.Type): a comment genus
                type
        :arg:    from (osid.calendaring.DateTime): starting date
        :arg:    to (osid.calendaring.DateTime): ending date
        :return: (osid.commenting.CommentList) - the returned ``Comment``
                list
        :raises:  InvalidArgument - ``from`` is greater than ``to``
        :raises:  NullArgument - ``comment_genus_type, from,`` or ``to``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_for_commentor(resource_id):
        Gets a list of comments corresponding to a resource ``Id``.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the resource
        :return: (osid.commenting.CommentList) - the returned
                ``CommentList``
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_for_commentor_on_date(resource_id, from_, to):
        Gets a list of all comments corresponding to a resource ``Id`` and effective during the
            entire given date range inclusive but not confined to the date range.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the resource
        :arg:    from (osid.calendaring.DateTime): from date
        :arg:    to (osid.calendaring.DateTime): to date
        :return: (osid.commenting.CommentList) - the returned
                ``CommentList``
        :raises:  InvalidArgument - ``to`` is less than ``from``
        :raises:  NullArgument - ``resource_id, from,`` or ``to`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_by_genus_type_for_commentor(resource_id, comment_genus_type):
        Gets a list of comments of the given genus type corresponding to a resource ``Id``.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the resource
        :arg:    comment_genus_type (osid.type.Type): the comment genus
                type
        :return: (osid.commenting.CommentList) - the returned
                ``CommentList``
        :raises:  NullArgument - ``resource_id`` or ``comment_genus_type``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_by_genus_type_for_commentor_on_date(resource_id, comment_genus_type, from_, to):
        Gets a list of all comments of the given genus type corresponding to a resource ``Id`` and
            effective during the entire given date range inclusive but not confined to the date
            range.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the resource
        :arg:    comment_genus_type (osid.type.Type): the comment genus
                type
        :arg:    from (osid.calendaring.DateTime): from date
        :arg:    to (osid.calendaring.DateTime): to date
        :return: (osid.commenting.CommentList) - the returned
                ``CommentList``
        :raises:  InvalidArgument - ``to`` is less than ``from``
        :raises:  NullArgument - ``resource_id, comment_genus_type,
                from,`` or ``to`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_for_reference(reference_id):
        Gets a list of comments corresponding to a reference ``Id``.

        :arg:    reference_id (osid.id.Id): the ``Id`` of the reference
        :return: (osid.commenting.CommentList) - the returned
                ``CommentList``
        :raises:  NullArgument - ``reference_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_for_reference_on_date(reference_id, from_, to):
        Gets a list of all comments corresponding to a reference ``Id`` and effective during the
            entire given date range inclusive but not confined to the date range.

        :arg:    reference_id (osid.id.Id): a reference ``Id``
        :arg:    from (osid.calendaring.DateTime): from date
        :arg:    to (osid.calendaring.DateTime): to date
        :return: (osid.commenting.CommentList) - the returned
                ``CommentList``
        :raises:  InvalidArgument - ``to`` is less than ``from``
        :raises:  NullArgument - ``reference_id, from,`` or ``to`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_by_genus_type_for_reference(reference_id, comment_genus_type):
        Gets a list of comments of the given genus type corresponding to a reference ``Id``.

        :arg:    reference_id (osid.id.Id): the ``Id`` of the reference
        :arg:    comment_genus_type (osid.type.Type): the comment genus
                type
        :return: (osid.commenting.CommentList) - the returned
                ``CommentList``
        :raises:  NullArgument - ``reference_id`` or
                ``comment_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_by_genus_type_for_reference_on_date(reference_id, comment_genus_type, from_, to):
        Gets a list of all comments of the given genus type corresponding to a reference ``Id`` and
            effective during the entire given date range inclusive but not confined to the date
            range.

        :arg:    reference_id (osid.id.Id): a reference ``Id``
        :arg:    comment_genus_type (osid.type.Type): the comment genus
                type
        :arg:    from (osid.calendaring.DateTime): from date
        :arg:    to (osid.calendaring.DateTime): to date
        :return: (osid.commenting.CommentList) - the returned
                ``CommentList``
        :raises:  InvalidArgument - ``to`` is less than ``from``
        :raises:  NullArgument - ``reference_id, comment_genus_type,
                from,`` or ``to`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_for_commentor_and_reference(resource_id, reference_id):
        Gets a list of comments corresponding to a resource and reference ``Id``.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the resource
        :arg:    reference_id (osid.id.Id): the ``Id`` of the reference
        :return: (osid.commenting.CommentList) - the returned
                ``CommentList``
        :raises:  NullArgument - ``resource_id`` or ``reference_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_for_commentor_and_reference_on_date(resource_id, reference_id, from_, to):
        Gets a list of all comments corresponding to a resource and reference ``Id`` and effective
            during the entire given date range inclusive but not confined to the date range.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the resource
        :arg:    reference_id (osid.id.Id): a reference ``Id``
        :arg:    from (osid.calendaring.DateTime): from date
        :arg:    to (osid.calendaring.DateTime): to date
        :return: (osid.commenting.CommentList) - the returned
                ``CommentList``
        :raises:  InvalidArgument - ``to`` is less than ``from``
        :raises:  NullArgument - ``resource_id, reference_id, from,`` or
                ``to`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_by_genus_type_for_commentor_and_reference(resource_id, reference_id, comment_genus_type):
        Gets a list of comments of the given genus type corresponding to a resource and reference
            ``Id``.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the resource
        :arg:    reference_id (osid.id.Id): the ``Id`` of the reference
        :arg:    comment_genus_type (osid.type.Type): the comment genus
                type
        :return: (osid.commenting.CommentList) - the returned
                ``CommentList``
        :raises:  NullArgument - ``resource_id, reference_id`` or
                ``comment_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments_by_genus_type_for_commentor_and_reference_on_date(resource_id, reference_id, comment_genus_type, from_, to):
        Gets a list of all comments corresponding to a resource and reference ``Id`` and effective
            during the entire given date range inclusive but not confined to the date range.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the resource
        :arg:    reference_id (osid.id.Id): a reference ``Id``
        :arg:    comment_genus_type (osid.type.Type): the comment genus
                type
        :arg:    from (osid.calendaring.DateTime): from date
        :arg:    to (osid.calendaring.DateTime): to date
        :return: (osid.commenting.CommentList) - the returned
                ``CommentList``
        :raises:  InvalidArgument - ``to`` is less than ``from``
        :raises:  NullArgument - ``resource_id, reference_id,
                comment_genus_type, from,`` or ``to`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comments():
        Gets all comments.

        :return: (osid.commenting.CommentList) - a list of comments
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: comments




Comment Query Methods
---------------------

    .. py:method:: get_book_id():
        Gets the ``Book``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Book Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: book_id


    .. py:method:: get_book():
        Gets the ``Book`` associated with this session.

        :return: (osid.commenting.Book) - the book
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: book


    .. py:method:: can_search_comments():
        Tests if this user can perform comment searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not wish to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_federated_book_view():
        Federates the view for methods in this session.

        A federated view will include comments in books which are
        children of this book in the book hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_book_view():
        Isolates the view for methods in this session.

        An isolated view restricts searches to this book only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_comment_query():
        Gets a comment query.

        :return: (osid.commenting.CommentQuery) - the comment query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: comment_query


    .. py:method:: get_comments_by_query(comment_query):
        Gets a list of comments matching the given search.

        :arg:    comment_query (osid.commenting.CommentQuery): the search
                query array
        :return: (osid.commenting.CommentList) - the returned
                ``CommentList``
        :raises:  NullArgument - ``comment_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``comment_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*






Comment Admin Methods
---------------------

    .. py:method:: get_book_id():
        Gets the ``Book``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Book Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: book_id


    .. py:method:: get_book():
        Gets the ``Book`` associated with this session.

        :return: (osid.commenting.Book) - the book
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: book


    .. py:method:: can_create_comments():
        Tests if this user can create comments.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Comment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Comment`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_comment_with_record_types(comment_record_types):
        Tests if this user can create a single ``Comment`` using the desired record types.

        While ``CommentingManager.getCommentRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Comment``.
        Providing an empty array tests if a ``Comment`` can be created
        with no records.

        :arg:    comment_record_types (osid.type.Type[]): array of
                comment record types
        :return: (boolean) - ``true`` if ``Comment`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``comment_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comment_form_for_create(reference_id, comment_record_types):
        Gets the comment form for creating new comments.

        A new form should be requested for each create transaction.

        :arg:    reference_id (osid.id.Id): the ``Id`` for the reference
                object
        :arg:    comment_record_types (osid.type.Type[]): array of
                comment record types
        :return: (osid.commenting.CommentForm) - the comment form
        :raises:  NullArgument - ``reference_id or comment_record_types``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_comment(comment_form):
        Creates a new ``Comment``.

        :arg:    comment_form (osid.commenting.CommentForm): the form for
                this ``Comment``
        :return: (osid.commenting.Comment) - the new ``Comment``
        :raises:  IllegalState - ``comment_form`` already used in a create
                transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``comment_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``comment_form`` did not originate from
                ``get_comment_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_comments():
        Tests if this user can update comments.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Comment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Comment`` modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_comment_form_for_update(comment_id):
        Gets the comment form for updating an existing comment.

        A new comment form should be requested for each update
        transaction.

        :arg:    comment_id (osid.id.Id): the ``Id`` of the ``Comment``
        :return: (osid.commenting.CommentForm) - the comment form
        :raises:  NotFound - ``comment_id`` is not found
        :raises:  NullArgument - ``comment_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_comment(comment_form):
        Updates an existing comment.

        :arg:    comment_form (osid.commenting.CommentForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``comment_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``comment_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``comment_form`` did not originate from
                ``get_comment_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_comments():
        Tests if this user can delete comments.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Comment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Comment`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_comment(comment_id):
        Deletes a ``Comment``.

        :arg:    comment_id (osid.id.Id): the ``Id`` of the ``Comment``
                to remove
        :raises:  NotFound - ``comment_id`` not found
        :raises:  NullArgument - ``comment_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_comment_aliases():
        Tests if this user can manage ``Id`` aliases for ``Comnents``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Comment`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_comment(comment_id, alias_id):
        Adds an ``Id`` to a ``Comment`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Comment`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another comment, it is
        reassigned to the given comment ``Id``.

        :arg:    comment_id (osid.id.Id): the ``Id`` of a ``Comment``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``comment_id`` not found
        :raises:  NullArgument - ``comment_id`` or ``alias_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






