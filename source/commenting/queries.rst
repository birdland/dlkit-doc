
.. currentmodule:: dlkit.commenting.queries
.. automodule:: dlkit.commenting.queries

Queries
=======


Comment Query
-------------

.. autoclass:: CommentQuery
   :show-inheritance:

   .. automethod:: CommentQuery.match_reference_id

   .. autoattribute:: CommentQuery.reference_id_terms

   .. automethod:: CommentQuery.match_commentor_id

   .. autoattribute:: CommentQuery.commentor_id_terms

   .. automethod:: CommentQuery.supports_commentor_query

   .. autoattribute:: CommentQuery.commentor_query

   .. autoattribute:: CommentQuery.commentor_terms

   .. automethod:: CommentQuery.match_commenting_agent_id

   .. autoattribute:: CommentQuery.commenting_agent_id_terms

   .. automethod:: CommentQuery.supports_commenting_agent_query

   .. autoattribute:: CommentQuery.commenting_agent_query

   .. autoattribute:: CommentQuery.commenting_agent_terms

   .. automethod:: CommentQuery.match_text

   .. automethod:: CommentQuery.match_any_text

   .. autoattribute:: CommentQuery.text_terms

   .. automethod:: CommentQuery.match_rating_id

   .. autoattribute:: CommentQuery.rating_id_terms

   .. automethod:: CommentQuery.supports_rating_query

   .. autoattribute:: CommentQuery.rating_query

   .. automethod:: CommentQuery.match_any_rating

   .. autoattribute:: CommentQuery.rating_terms

   .. automethod:: CommentQuery.match_book_id

   .. autoattribute:: CommentQuery.book_id_terms

   .. automethod:: CommentQuery.supports_book_query

   .. autoattribute:: CommentQuery.book_query

   .. autoattribute:: CommentQuery.book_terms

   .. automethod:: CommentQuery.get_comment_query_record

Book Query
----------

.. autoclass:: BookQuery
   :show-inheritance:

   .. automethod:: BookQuery.match_comment_id

   .. autoattribute:: BookQuery.comment_id_terms

   .. automethod:: BookQuery.supports_comment_query

   .. autoattribute:: BookQuery.comment_query

   .. automethod:: BookQuery.match_any_comment

   .. autoattribute:: BookQuery.comment_terms

   .. automethod:: BookQuery.match_ancestor_book_id

   .. autoattribute:: BookQuery.ancestor_book_id_terms

   .. automethod:: BookQuery.supports_ancestor_book_query

   .. autoattribute:: BookQuery.ancestor_book_query

   .. automethod:: BookQuery.match_any_ancestor_book

   .. autoattribute:: BookQuery.ancestor_book_terms

   .. automethod:: BookQuery.match_descendant_book_id

   .. autoattribute:: BookQuery.descendant_book_id_terms

   .. automethod:: BookQuery.supports_descendant_book_query

   .. autoattribute:: BookQuery.descendant_book_query

   .. automethod:: BookQuery.match_any_descendant_book

   .. autoattribute:: BookQuery.descendant_book_terms

   .. automethod:: BookQuery.get_book_query_record

