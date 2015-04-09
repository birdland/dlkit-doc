.. currentmodule:: dlkit.commenting.search_orders
.. automodule:: dlkit.commenting.search_orders

Search Orders
=============


Comment Search Order
--------------------

.. autoclass:: CommentSearchOrder
   :show-inheritance:

   .. automethod:: CommentSearchOrder.order_by_reference

   .. automethod:: CommentSearchOrder.order_by_commentor

   .. automethod:: CommentSearchOrder.supports_commentor_search_order

   .. autoattribute:: CommentSearchOrder.commentor_search_order

   .. automethod:: CommentSearchOrder.order_by_commenting_agent

   .. automethod:: CommentSearchOrder.supports_commenting_agent_search_order

   .. autoattribute:: CommentSearchOrder.commenting_agent_search_order

   .. automethod:: CommentSearchOrder.order_by_text

   .. automethod:: CommentSearchOrder.order_by_rating

   .. automethod:: CommentSearchOrder.supports_rating_search_order

   .. autoattribute:: CommentSearchOrder.rating_search_order

   .. automethod:: CommentSearchOrder.get_comment_search_order_record



Book Search Order
-----------------

.. autoclass:: BookSearchOrder
   :show-inheritance:

   .. automethod:: BookSearchOrder.get_book_search_order_record



