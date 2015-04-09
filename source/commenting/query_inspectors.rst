.. currentmodule:: dlkit.commenting.query_inspectors
.. automodule:: dlkit.commenting.query_inspectors

Query Inspectors
================


Comment Query Inspector
-----------------------

.. autoclass:: CommentQueryInspector
   :show-inheritance:

   .. autoattribute:: CommentQueryInspector.reference_id_terms

   .. autoattribute:: CommentQueryInspector.commentor_id_terms

   .. autoattribute:: CommentQueryInspector.commentor_terms

   .. autoattribute:: CommentQueryInspector.commenting_agent_id_terms

   .. autoattribute:: CommentQueryInspector.commenting_agent_terms

   .. autoattribute:: CommentQueryInspector.text_terms

   .. autoattribute:: CommentQueryInspector.rating_id_terms

   .. autoattribute:: CommentQueryInspector.rating_terms

   .. autoattribute:: CommentQueryInspector.book_id_terms

   .. autoattribute:: CommentQueryInspector.book_terms

   .. automethod:: CommentQueryInspector.get_comment_query_inspector_record



Book Query Inspector
--------------------

.. autoclass:: BookQueryInspector
   :show-inheritance:

   .. autoattribute:: BookQueryInspector.comment_id_terms

   .. autoattribute:: BookQueryInspector.comment_terms

   .. autoattribute:: BookQueryInspector.ancestor_book_id_terms

   .. autoattribute:: BookQueryInspector.ancestor_book_terms

   .. autoattribute:: BookQueryInspector.descendant_book_id_terms

   .. autoattribute:: BookQueryInspector.descendant_book_terms

   .. automethod:: BookQueryInspector.get_book_query_inspector_record



