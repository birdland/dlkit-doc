from ..osid import managers as osid_managers


class CommentingProfile(osid_managers.OsidProfile):
    """The commenting profile describes the interoperability among commenting services."""
    def supports_comment_lookup(self):
        """Tests for the availability of a comment lookup service.

        :return: ``true`` if comment lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_comment_query(self):
        """Tests if querying comments is available.

        :return: ``true`` if comment query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_comment_admin(self):
        """Tests if managing comments is available.

        :return: ``true`` if comment admin is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_book_lookup(self):
        """Tests for the availability of an book lookup service.

        :return: ``true`` if book lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_book_admin(self):
        """Tests for the availability of a book administrative service for creating and deleting books.

        :return: ``true`` if book administration is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_book_hierarchy(self):
        """Tests for the availability of a book hierarchy traversal service.

        :return: ``true`` if book hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_book_hierarchy_design(self):
        """Tests for the availability of a book hierarchy design service.

        :return: ``true`` if book hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_comment_record_types(self):
        """Gets the supported ``Comment`` record types.

        :return: a list containing the supported comment record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    comment_record_types = property(fget=get_comment_record_types)

    def get_comment_search_record_types(self):
        """Gets the supported comment search record types.

        :return: a list containing the supported comment search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    comment_search_record_types = property(fget=get_comment_search_record_types)

    def get_book_record_types(self):
        """Gets the supported ``Book`` record types.

        :return: a list containing the supported book record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    book_record_types = property(fget=get_book_record_types)

    def get_book_search_record_types(self):
        """Gets the supported book search record types.

        :return: a list containing the supported book search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    book_search_record_types = property(fget=get_book_search_record_types)


class CommentingManager(osid_managers.OsidManager, CommentingProfile):
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
    def get_comment_lookup_session(self):
        """Gets the ``OsidSession`` associated with the comment lookup service.

        :return: a ``CommentLookupSession``
        :rtype: ``osid.commenting.CommentLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_lookup()`` is ``false``

        """
        return # osid.commenting.CommentLookupSession

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
        return # osid.commenting.CommentLookupSession

    def get_comment_query_session(self):
        """Gets the ``OsidSession`` associated with the comment query service.

        :return: a ``CommentQuerySession``
        :rtype: ``osid.commenting.CommentQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_query()`` is ``false``

        """
        return # osid.commenting.CommentQuerySession

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
        return # osid.commenting.CommentQuerySession

    def get_comment_admin_session(self):
        """Gets the ``OsidSession`` associated with the comment administration service.

        :return: a ``CommentAdminSession``
        :rtype: ``osid.commenting.CommentAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_comment_admin()`` is ``false``

        """
        return # osid.commenting.CommentAdminSession

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
        return # osid.commenting.CommentAdminSession

    def get_book_lookup_session(self):
        """Gets the ``OsidSession`` associated with the book lookup service.

        :return: a ``BookLookupSession``
        :rtype: ``osid.commenting.BookLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_lookup()`` is ``false``

        """
        return # osid.commenting.BookLookupSession

    book_lookup_session = property(fget=get_book_lookup_session)

    def get_book_admin_session(self):
        """Gets the ``OsidSession`` associated with the book administrative service.

        :return: a ``BookAdminSession``
        :rtype: ``osid.commenting.BookAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_admin()`` is ``false``

        """
        return # osid.commenting.BookAdminSession

    book_admin_session = property(fget=get_book_admin_session)

    def get_book_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the book hierarchy service.

        :return: a ``BookHierarchySession``
        :rtype: ``osid.commenting.BookHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_hierarchy()`` is ``false``

        """
        return # osid.commenting.BookHierarchySession

    book_hierarchy_session = property(fget=get_book_hierarchy_session)

    def get_book_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the book hierarchy design service.

        :return: a ``BookHierarchyDesignSession``
        :rtype: ``osid.commenting.BookHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_book_hierarchy_design()`` is ``false``

        """
        return # osid.commenting.BookHierarchyDesignSession

    book_hierarchy_design_session = property(fget=get_book_hierarchy_design_session)

    def get_commenting_batch_manager(self):
        """Gets a ``CommentingBatchManager``.

        :return: a ``CommentingBatchManager``
        :rtype: ``osid.commenting.batch.CommentingBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commenting_batch()`` is ``false``

        """
        return # osid.commenting.batch.CommentingBatchManager

    commenting_batch_manager = property(fget=get_commenting_batch_manager)


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
        return # osid.commenting.CommentLookupSession

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
        return # osid.commenting.CommentLookupSession

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
        return # osid.commenting.CommentQuerySession

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
        return # osid.commenting.CommentQuerySession

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
        return # osid.commenting.CommentAdminSession

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
        return # osid.commenting.CommentAdminSession

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
        return # osid.commenting.BookLookupSession

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
        return # osid.commenting.BookAdminSession

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
        return # osid.commenting.BookHierarchySession

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
        return # osid.commenting.BookHierarchyDesignSession

    def get_commenting_batch_proxy_manager(self):
        """Gets a ``CommentingBatchProxyManager``.

        :return: a ``CommentingBatchProxyManager``
        :rtype: ``osid.commenting.batch.CommentingBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commenting_batch()`` is ``false``

        """
        return # osid.commenting.batch.CommentingBatchProxyManager

    commenting_batch_proxy_manager = property(fget=get_commenting_batch_proxy_manager)


