

Queries
=======


Comment Query
-------------

.. py:class:: CommentQuery(abc_commenting_queries.CommentQuery, osid_queries.OsidRelationshipQuery)
    This is the query for searching comments.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.





    .. py:method:: match_reference_id(source_id, match):
        :noindex:


    .. py:method:: clear_reference_id_terms():
        :noindex:


    .. py:attribute:: reference_id_terms
        :noindex:


    .. py:method:: match_commentor_id(resource_id, match):
        :noindex:


    .. py:method:: clear_commentor_id_terms():
        :noindex:


    .. py:attribute:: commentor_id_terms
        :noindex:


    .. py:method:: supports_commentor_query():
        :noindex:


    .. py:method:: get_commentor_query():
        :noindex:


    .. py:attribute:: commentor_query
        :noindex:


    .. py:method:: clear_commentor_terms():
        :noindex:


    .. py:attribute:: commentor_terms
        :noindex:


    .. py:method:: match_commenting_agent_id(agent_id, match):
        :noindex:


    .. py:method:: clear_commenting_agent_id_terms():
        :noindex:


    .. py:attribute:: commenting_agent_id_terms
        :noindex:


    .. py:method:: supports_commenting_agent_query():
        :noindex:


    .. py:method:: get_commenting_agent_query():
        :noindex:


    .. py:attribute:: commenting_agent_query
        :noindex:


    .. py:method:: clear_commenting_agent_terms():
        :noindex:


    .. py:attribute:: commenting_agent_terms
        :noindex:


    .. py:method:: match_text(text, string_match_type, match):
        :noindex:


    .. py:method:: match_any_text(match):
        :noindex:


    .. py:method:: clear_text_terms():
        :noindex:


    .. py:attribute:: text_terms
        :noindex:


    .. py:method:: match_rating_id(grade_id, match):
        :noindex:


    .. py:method:: clear_rating_id_terms():
        :noindex:


    .. py:attribute:: rating_id_terms
        :noindex:


    .. py:method:: supports_rating_query():
        :noindex:


    .. py:method:: get_rating_query():
        :noindex:


    .. py:attribute:: rating_query
        :noindex:


    .. py:method:: match_any_rating(match):
        :noindex:


    .. py:method:: clear_rating_terms():
        :noindex:


    .. py:attribute:: rating_terms
        :noindex:


    .. py:method:: match_book_id(book_id, match):
        :noindex:


    .. py:method:: clear_book_id_terms():
        :noindex:


    .. py:attribute:: book_id_terms
        :noindex:


    .. py:method:: supports_book_query():
        :noindex:


    .. py:method:: get_book_query():
        :noindex:


    .. py:attribute:: book_query
        :noindex:


    .. py:method:: clear_book_terms():
        :noindex:


    .. py:attribute:: book_terms
        :noindex:


    .. py:method:: get_comment_query_record(comment_record_type):
        :noindex:


Book Query
----------

.. py:class:: BookQuery(abc_commenting_queries.BookQuery, osid_queries.OsidCatalogQuery)
    This is the query for searching books.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.





    .. py:method:: match_comment_id(comment_id, match):
        :noindex:


    .. py:method:: clear_comment_id_terms():
        :noindex:


    .. py:attribute:: comment_id_terms
        :noindex:


    .. py:method:: supports_comment_query():
        :noindex:


    .. py:method:: get_comment_query():
        :noindex:


    .. py:attribute:: comment_query
        :noindex:


    .. py:method:: match_any_comment(match):
        :noindex:


    .. py:method:: clear_comment_terms():
        :noindex:


    .. py:attribute:: comment_terms
        :noindex:


    .. py:method:: match_ancestor_book_id(book_id, match):
        :noindex:


    .. py:method:: clear_ancestor_book_id_terms():
        :noindex:


    .. py:attribute:: ancestor_book_id_terms
        :noindex:


    .. py:method:: supports_ancestor_book_query():
        :noindex:


    .. py:method:: get_ancestor_book_query():
        :noindex:


    .. py:attribute:: ancestor_book_query
        :noindex:


    .. py:method:: match_any_ancestor_book(match):
        :noindex:


    .. py:method:: clear_ancestor_book_terms():
        :noindex:


    .. py:attribute:: ancestor_book_terms
        :noindex:


    .. py:method:: match_descendant_book_id(book_id, match):
        :noindex:


    .. py:method:: clear_descendant_book_id_terms():
        :noindex:


    .. py:attribute:: descendant_book_id_terms
        :noindex:


    .. py:method:: supports_descendant_book_query():
        :noindex:


    .. py:method:: get_descendant_book_query():
        :noindex:


    .. py:attribute:: descendant_book_query
        :noindex:


    .. py:method:: match_any_descendant_book(match):
        :noindex:


    .. py:method:: clear_descendant_book_terms():
        :noindex:


    .. py:attribute:: descendant_book_terms
        :noindex:


    .. py:method:: get_book_query_record(book_record_type):
        :noindex:


