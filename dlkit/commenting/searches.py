
from ..osid import searches as osid_searches


class CommentSearch(osid_searches.OsidSearch):
    """The search interface for governing comment searches."""
    



    def search_among_comments(self, comment_ids):
        """Execute this search among the given list of comments.

        arg:    comment_ids (osid.id.IdList): list of comments
        raise:  NullArgument - ``comment_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def order_comment_results(self, comment_search_order):
        """Specify an ordering to the search results.

        arg:    comment_search_order
                (osid.commenting.CommentSearchOrder): comment search
                order
        raise:  NullArgument - ``comment_search_order`` is ``null``
        raise:  Unsupported - ``comment_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def get_comment_search_record(self, comment_search_record_type):
        """Gets the comment search record corresponding to the given comment search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    comment_search_record_type (osid.type.Type): a comment
                search record type
        return: (osid.commenting.records.CommentSearchRecord) - the
                comment search record
        raise:  NullArgument - ``comment_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(comment_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.records.CommentSearchRecord


class CommentSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    



    def get_comments(self):
        """Gets the comment list resulting from a search.

        return: (osid.commenting.CommentList) - the comment list
        raise:  IllegalState - list has already been retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentList

    comments = property(fget=get_comments)


    def get_comment_query_inspector(self):
        """Gets the inspector for the query to examine the terns used in the search.

        return: (osid.commenting.CommentQueryInspector) - the query
                inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentQueryInspector

    comment_query_inspector = property(fget=get_comment_query_inspector)


    def get_comment_search_results_record(self, comment_search_record_type):
        """Gets the comment search results record corresponding to the given comment search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    comment_search_record_type (osid.type.Type): a comment
                search record type
        return: (osid.commenting.records.CommentSearchResultsRecord) -
                the comment search results record
        raise:  NullArgument - ``comment_search_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(comment_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.records.CommentSearchResultsRecord


class BookSearch(osid_searches.OsidSearch):
    """The search interface for governing book searches."""
    



    def search_among_books(self, book_ids):
        """Execute this search among the given list of books.

        arg:    book_ids (osid.id.IdList): list of books
        raise:  NullArgument - ``book_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def order_book_results(self, book_search_order):
        """Specify an ordering to the search results.

        arg:    book_search_order (osid.commenting.BookSearchOrder):
                book search order
        raise:  NullArgument - ``book_search_order`` is ``null``
        raise:  Unsupported - ``book_search_order`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def get_book_search_record(self, book_search_record_type):
        """Gets the book search record corresponding to the given book search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    book_search_record_type (osid.type.Type): a book search
                record type
        return: (osid.commenting.records.BookSearchRecord) - the book
                search record
        raise:  NullArgument - ``book_search_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(book_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.records.BookSearchRecord


class BookSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    



    def get_books(self):
        """Gets the book list resulting from a search.

        return: (osid.commenting.BookList) - the book list
        raise:  IllegalState - list has already been retrieved
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookList

    books = property(fget=get_books)


    def get_book_query_inspector(self):
        """Gets the inspector for the query to examine the terns used in the search.

        return: (osid.commenting.BookQueryInspector) - the query
                inspector
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.BookQueryInspector

    book_query_inspector = property(fget=get_book_query_inspector)


    def get_book_search_results_record(self, book_search_record_type):
        """Gets the book search results record corresponding to the given book search record Type.

        This method is used to retrieve an object implementing the
        requested record.

        arg:    book_search_record_type (osid.type.Type): a book search
                record type
        return: (osid.commenting.records.BookSearchResultsRecord) - the
                book search results record
        raise:  NullArgument - ``BookSearchRecordType`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(book_search_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.records.BookSearchResultsRecord


