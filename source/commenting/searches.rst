

Searches
========


Comment Search
--------------

.. py:class:: CommentSearch(abc_commenting_searches.CommentSearch, osid_searches.OsidSearch)
    The search interface for governing comment searches.

    .. py:method:: search_among_comments(comment_ids):
        :noindex:


    .. py:method:: order_comment_results(comment_search_order):
        :noindex:


    .. py:method:: get_comment_search_record(comment_search_record_type):
        :noindex:


Comment Search Results
----------------------

.. py:class:: CommentSearchResults(abc_commenting_searches.CommentSearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_comments():
        :noindex:


    .. py:attribute:: comments
        :noindex:


    .. py:method:: get_comment_query_inspector():
        :noindex:


    .. py:attribute:: comment_query_inspector
        :noindex:


    .. py:method:: get_comment_search_results_record(comment_search_record_type):
        :noindex:


Book Search
-----------

.. py:class:: BookSearch(abc_commenting_searches.BookSearch, osid_searches.OsidSearch)
    The search interface for governing book searches.

    .. py:method:: search_among_books(book_ids):
        :noindex:


    .. py:method:: order_book_results(book_search_order):
        :noindex:


    .. py:method:: get_book_search_record(book_search_record_type):
        :noindex:


Book Search Results
-------------------

.. py:class:: BookSearchResults(abc_commenting_searches.BookSearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_books():
        :noindex:


    .. py:attribute:: books
        :noindex:


    .. py:method:: get_book_query_inspector():
        :noindex:


    .. py:attribute:: book_query_inspector
        :noindex:


    .. py:method:: get_book_search_results_record(book_search_record_type):
        :noindex:


