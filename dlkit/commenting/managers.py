
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class CommentingProfile(osid_managers.OsidProfile):
    """The commenting profile describes the interoperability among commenting services."""

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


class CommentingManager(osid_managers.OsidManager, osid_sessions.OsidSession, CommentingProfile):
    """The commenting manager provides access to commenting sessions and provides interoperability tests for various aspects of
    this service.

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


class CommentingProxyManager(osid_managers.OsidProxyManager, CommentingProfile):
    """The commenting manager provides access to commenting sessions and provides interoperability tests for various aspects of
    this service.

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


