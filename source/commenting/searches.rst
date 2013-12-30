.. currentmodule:: dlkit.commenting.searches
.. automodule:: dlkit.commenting.searches

Searches
========


Comment Search
--------------

.. autoclass:: CommentSearch
   :show-inheritance:

.. automethod:: CommentSearch.search_among_comments

.. automethod:: CommentSearch.order_comment_results

.. automethod:: CommentSearch.get_comment_search_record



Comment Search Results
----------------------

.. autoclass:: CommentSearchResults
   :show-inheritance:

.. autoattribute:: CommentSearchResults.comments

.. autoattribute:: CommentSearchResults.comment_query_inspector

.. automethod:: CommentSearchResults.get_comment_search_results_record



Book Search
-----------

.. autoclass:: BookSearch
   :show-inheritance:

.. automethod:: BookSearch.search_among_books

.. automethod:: BookSearch.order_book_results

.. automethod:: BookSearch.get_book_search_record



Book Search Results
-------------------

.. autoclass:: BookSearchResults
   :show-inheritance:

.. autoattribute:: BookSearchResults.books

.. autoattribute:: BookSearchResults.book_query_inspector

.. automethod:: BookSearchResults.get_book_search_results_record



