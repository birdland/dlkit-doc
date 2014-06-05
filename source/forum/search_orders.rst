.. currentmodule:: dlkit.forum.search_orders
.. automodule:: dlkit.forum.search_orders

Search_Orders
=============


Post Search Order
-----------------

.. autoclass:: PostSearchOrder
   :show-inheritance:

   .. automethod:: PostSearchOrder.order_by_timestamp

   .. automethod:: PostSearchOrder.order_by_poster

   .. automethod:: PostSearchOrder.supports_poster_search_order

   .. autoattribute:: PostSearchOrder.poster_search_order

   .. automethod:: PostSearchOrder.order_by_posting_agent

   .. automethod:: PostSearchOrder.supports_posting_agent_search_order

   .. autoattribute:: PostSearchOrder.posting_agent_search_order

   .. automethod:: PostSearchOrder.order_by_subject

   .. automethod:: PostSearchOrder.order_by_text

   .. automethod:: PostSearchOrder.get_post_search_order_record



Reply Search Order
------------------

.. autoclass:: ReplySearchOrder
   :show-inheritance:

   .. automethod:: ReplySearchOrder.order_by_timestamp

   .. automethod:: ReplySearchOrder.order_by_poster

   .. automethod:: ReplySearchOrder.supports_poster_search_order

   .. autoattribute:: ReplySearchOrder.poster_search_order

   .. automethod:: ReplySearchOrder.order_by_posting_agent

   .. automethod:: ReplySearchOrder.supports_posting_agent_search_order

   .. autoattribute:: ReplySearchOrder.posting_agent_search_order

   .. automethod:: ReplySearchOrder.order_by_subject_line

   .. automethod:: ReplySearchOrder.order_by_text

   .. automethod:: ReplySearchOrder.get_reply_search_order_record



Forum Search Order
------------------

.. autoclass:: ForumSearchOrder
   :show-inheritance:

   .. automethod:: ForumSearchOrder.get_forum_search_order_record



