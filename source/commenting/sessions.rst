

Sessions
========


Comment Lookup Session
----------------------

.. py:class:: CommentLookupSession(abc_commenting_sessions.CommentLookupSession, osid_sessions.OsidSession)
    This session defines methods for retrieving comments.

    .. py:method:: get_book_id():
        :noindex:


    .. py:attribute:: book_id
        :noindex:


    .. py:method:: get_book():
        :noindex:


    .. py:attribute:: book
        :noindex:


    .. py:method:: can_lookup_comments():
        :noindex:


    .. py:method:: use_comparative_comment_view():
        :noindex:


    .. py:method:: use_plenary_comment_view():
        :noindex:


    .. py:method:: use_federated_book_view():
        :noindex:


    .. py:method:: use_isolated_book_view():
        :noindex:


    .. py:method:: use_effective_comment_view():
        :noindex:


    .. py:method:: use_any_effective_comment_view():
        :noindex:


    .. py:method:: get_comment(comment_id):
        :noindex:


    .. py:method:: get_comments_by_ids(comment_ids):
        :noindex:


    .. py:method:: get_comments_by_genus_type(comment_genus_type):
        :noindex:


    .. py:method:: get_comments_by_parent_genus_type(comment_genus_type):
        :noindex:


    .. py:method:: get_comments_by_record_type(comment_record_type):
        :noindex:


    .. py:method:: get_comments_on_date(from_, to):
        :noindex:


    .. py:method:: get_comments_by_genus_type_on_date(comment_genus_type, from_, to):
        :noindex:


    .. py:method:: get_comments_for_commentor(resource_id):
        :noindex:


    .. py:method:: get_comments_for_commentor_on_date(resource_id, from_, to):
        :noindex:


    .. py:method:: get_comments_by_genus_type_for_commentor(resource_id, comment_genus_type):
        :noindex:


    .. py:method:: get_comments_by_genus_type_for_commentor_on_date(resource_id, comment_genus_type, from_, to):
        :noindex:


    .. py:method:: get_comments_for_reference(reference_id):
        :noindex:


    .. py:method:: get_comments_for_reference_on_date(reference_id, from_, to):
        :noindex:


    .. py:method:: get_comments_by_genus_type_for_reference(reference_id, comment_genus_type):
        :noindex:


    .. py:method:: get_comments_by_genus_type_for_reference_on_date(reference_id, comment_genus_type, from_, to):
        :noindex:


    .. py:method:: get_comments_for_commentor_and_reference(resource_id, reference_id):
        :noindex:


    .. py:method:: get_comments_for_commentor_and_reference_on_date(resource_id, reference_id, from_, to):
        :noindex:


    .. py:method:: get_comments_by_genus_type_for_commentor_and_reference(resource_id, reference_id, comment_genus_type):
        :noindex:


    .. py:method:: get_comments_by_genus_type_for_commentor_and_reference_on_date(resource_id, reference_id, comment_genus_type, from_, to):
        :noindex:


    .. py:method:: get_comments():
        :noindex:


    .. py:attribute:: comments
        :noindex:


Comment Query Session
---------------------

.. py:class:: CommentQuerySession(abc_commenting_sessions.CommentQuerySession, osid_sessions.OsidSession)
    This session provides methods for searching ``Comment`` objects.


    The search query is constructed using the ``CommentQuery``. The book
    record ``Type`` also specifies the record for the book query.




    Comments may have a query record indicated by their respective
    record types. The query record is accessed via the ``CommentQuery``.
    The returns in this session may not be cast directly to these
    interfaces.





    .. py:method:: get_book_id():
        :noindex:


    .. py:attribute:: book_id
        :noindex:


    .. py:method:: get_book():
        :noindex:


    .. py:attribute:: book
        :noindex:


    .. py:method:: can_search_comments():
        :noindex:


    .. py:method:: use_federated_book_view():
        :noindex:


    .. py:method:: use_isolated_book_view():
        :noindex:


    .. py:method:: get_comment_query():
        :noindex:


    .. py:attribute:: comment_query
        :noindex:


    .. py:method:: get_comments_by_query(comment_query):
        :noindex:


Comment Admin Session
---------------------

.. py:class:: CommentAdminSession(abc_commenting_sessions.CommentAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``Comments``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create a
    ``Comment,`` a ``CommentForm`` is requested using
    ``get_comment_form_for_create()`` specifying the desired
    relationship peers and record ``Types`` or none if no record
    ``Types`` are needed. The returned ``CommentForm`` will indicate
    that it is to be used with a create operation and can be used to
    examine metdata or validate data prior to creation. Once the
    ``CommentForm`` is submiited to a create operation, it cannot be
    reused with another create operation unless the first operation was
    unsuccessful. Each ``CommentForm`` corresponds to an attempted
    transaction.




    For updates, ``CommentForms`` are requested to the ``Comment``
    ``Id`` that is to be updated using ``getCommentFormForUpdate()``.
    Similarly, the ``CommentForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``CommentForm`` can only be used once for a successful
    update and cannot be reused.




    The delete operations delete ``Comments``. To unmap a ``Comment``
    from the current ``Book,`` the ``CommentBookAssignmentSession``
    should be used. These delete operations attempt to remove the
    ``Comment`` itself thus removing it from all known ``Book``
    catalogs.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: get_book_id():
        :noindex:


    .. py:attribute:: book_id
        :noindex:


    .. py:method:: get_book():
        :noindex:


    .. py:attribute:: book
        :noindex:


    .. py:method:: can_create_comments():
        :noindex:


    .. py:method:: can_create_comment_with_record_types(comment_record_types):
        :noindex:


    .. py:method:: get_comment_form_for_create(reference_id, comment_record_types):
        :noindex:


    .. py:method:: create_comment(comment_form):
        :noindex:


    .. py:method:: can_update_comments():
        :noindex:


    .. py:method:: get_comment_form_for_update(comment_id):
        :noindex:


    .. py:method:: update_comment(comment_form):
        :noindex:


    .. py:method:: can_delete_comments():
        :noindex:


    .. py:method:: delete_comment(comment_id):
        :noindex:


    .. py:method:: can_manage_comment_aliases():
        :noindex:


    .. py:method:: alias_comment(comment_id, alias_id):
        :noindex:


Book Lookup Session
-------------------

.. py:class:: BookLookupSession(abc_commenting_sessions.BookLookupSession, osid_sessions.OsidSession)
    This session provides methods for retrieving ``Book`` objects.


    The ``Book`` represents a collection of comments.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition





    .. py:method:: can_lookup_books():
        :noindex:


    .. py:method:: use_comparative_book_view():
        :noindex:


    .. py:method:: use_plenary_book_view():
        :noindex:


    .. py:method:: get_book(book_id):
        :noindex:


    .. py:method:: get_books_by_ids(book_ids):
        :noindex:


    .. py:method:: get_books_by_genus_type(book_genus_type):
        :noindex:


    .. py:method:: get_books_by_parent_genus_type(book_genus_type):
        :noindex:


    .. py:method:: get_books_by_record_type(book_record_type):
        :noindex:


    .. py:method:: get_books_by_provider(resource_id):
        :noindex:


    .. py:method:: get_books():
        :noindex:


    .. py:attribute:: books
        :noindex:


Book Admin Session
------------------

.. py:class:: BookAdminSession(abc_commenting_sessions.BookAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``Books``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create a
    ``Book,`` a ``BookForm`` is requested using
    ``get_book_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``BookForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``BookForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``BookForm`` corresponds
    to an attempted transaction.




    For updates, ``BookForms`` are requested to the ``Book``  ``Id``
    that is to be updated using ``getBookFormForUpdate()``. Similarly,
    the ``BookForm`` has metadata about the data that can be updated and
    it can perform validation before submitting the update. The
    ``BookForm`` can only be used once for a successful update and
    cannot be reused.




    The delete operations delete ``Books``.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: can_create_books():
        :noindex:


    .. py:method:: can_create_book_with_record_types(book_record_types):
        :noindex:


    .. py:method:: get_book_form_for_create(book_record_types):
        :noindex:


    .. py:method:: create_book(book_form):
        :noindex:


    .. py:method:: can_update_books():
        :noindex:


    .. py:method:: get_book_form_for_update(book_id):
        :noindex:


    .. py:method:: update_book(book_form):
        :noindex:


    .. py:method:: can_delete_books():
        :noindex:


    .. py:method:: delete_book(book_id):
        :noindex:


    .. py:method:: can_manage_book_aliases():
        :noindex:


    .. py:method:: alias_book(book_id, alias_id):
        :noindex:


Book Hierarchy Session
----------------------

.. py:class:: BookHierarchySession(abc_commenting_sessions.BookHierarchySession, osid_sessions.OsidSession)
    This session defines methods for traversing a hierarchy of ``Book`` objects.


    Each node in the hierarchy is a unique ``Book``. The hierarchy may
    be traversed recursively to establish the tree structure through
    ``get_parent_books()`` and ``getChildBooks()``. To relate these
    ``Ids`` to another OSID, ``get_book_nodes()`` can be used for
    retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Book`` available in the Commenting OSID is known to this hierarchy
    but does not appear in the hierarchy traversal until added as a root
    node or a child of another node.




    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_books()`` or ``get_child_books()`` in lieu
    of a ``PermissionDenied`` error that may disrupt the traversal
    through authorized pathways.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: book elements may be silently omitted or re-
        ordered
      * plenary view: provides a complete set or is an error condition





    .. py:method:: get_book_hierarchy_id():
        :noindex:


    .. py:attribute:: book_hierarchy_id
        :noindex:


    .. py:method:: get_book_hierarchy():
        :noindex:


    .. py:attribute:: book_hierarchy
        :noindex:


    .. py:method:: can_access_book_hierarchy():
        :noindex:


    .. py:method:: use_comparative_book_view():
        :noindex:


    .. py:method:: use_plenary_book_view():
        :noindex:


    .. py:method:: get_root_book_ids():
        :noindex:


    .. py:attribute:: root_book_ids
        :noindex:


    .. py:method:: get_root_books():
        :noindex:


    .. py:attribute:: root_books
        :noindex:


    .. py:method:: has_parent_books(book_id):
        :noindex:


    .. py:method:: is_parent_of_book(id_, book_id):
        :noindex:


    .. py:method:: get_parent_book_ids(book_id):
        :noindex:


    .. py:method:: get_parent_books(book_id):
        :noindex:


    .. py:method:: is_ancestor_of_book(id_, book_id):
        :noindex:


    .. py:method:: has_child_books(book_id):
        :noindex:


    .. py:method:: is_child_of_book(id_, book_id):
        :noindex:


    .. py:method:: get_child_book_ids(book_id):
        :noindex:


    .. py:method:: get_child_books(book_id):
        :noindex:


    .. py:method:: is_descendant_of_book(id_, book_id):
        :noindex:


    .. py:method:: get_book_node_ids(book_id, ancestor_levels, descendant_levels, include_siblings):
        :noindex:


    .. py:method:: get_book_nodes(book_id, ancestor_levels, descendant_levels, include_siblings):
        :noindex:


Book Hierarchy Design Session
-----------------------------

.. py:class:: BookHierarchyDesignSession(abc_commenting_sessions.BookHierarchyDesignSession, osid_sessions.OsidSession)
    This session manages a hierarchy of books.


    Books may be organized into a hierarchy for organizing or
    federating. A parent ``Book`` includes all of the comments of its
    children such that a single root node contains all of the comments
    of the federation.





    .. py:method:: get_book_hierarchy_id():
        :noindex:


    .. py:attribute:: book_hierarchy_id
        :noindex:


    .. py:method:: get_book_hierarchy():
        :noindex:


    .. py:attribute:: book_hierarchy
        :noindex:


    .. py:method:: can_modify_book_hierarchy():
        :noindex:


    .. py:method:: add_root_book(book_id):
        :noindex:


    .. py:method:: remove_root_book(book_id):
        :noindex:


    .. py:method:: add_child_book(book_id, child_id):
        :noindex:


    .. py:method:: remove_child_book(book_id, child_id):
        :noindex:


    .. py:method:: remove_child_books(book_id):
        :noindex:


