.. currentmodule:: dlkit.forum.searches
.. automodule:: dlkit.forum.searches

Searches
========


Post Search
-----------

.. autoclass:: PostSearch
   :show-inheritance:

   .. automethod:: PostSearch.search_among_posts

   .. automethod:: PostSearch.order_post_results

   .. automethod:: PostSearch.get_post_search_record



Post Search Results
-------------------

.. autoclass:: PostSearchResults
   :show-inheritance:

   .. autoattribute:: PostSearchResults.posts

   .. autoattribute:: PostSearchResults.post_query_inspector

   .. automethod:: PostSearchResults.get_post_search_results_record



Reply Search
------------

.. autoclass:: ReplySearch
   :show-inheritance:

   .. automethod:: ReplySearch.search_among_replies

   .. automethod:: ReplySearch.order_reply_results

   .. automethod:: ReplySearch.get_reply_search_record



Reply Search Results
--------------------

.. autoclass:: ReplySearchResults
   :show-inheritance:

   .. autoattribute:: ReplySearchResults.replies

   .. autoattribute:: ReplySearchResults.reply_query_inspector

   .. automethod:: ReplySearchResults.get_reply_search_results_record



Forum Search
------------

.. autoclass:: ForumSearch
   :show-inheritance:

   .. automethod:: ForumSearch.search_among_forums

   .. automethod:: ForumSearch.order_forum_results

   .. automethod:: ForumSearch.get_forum_search_record



Forum Search Results
--------------------

.. autoclass:: ForumSearchResults
   :show-inheritance:

   .. autoattribute:: ForumSearchResults.forums

   .. autoattribute:: ForumSearchResults.forum_query_inspector

   .. automethod:: ForumSearchResults.get_forum_search_results_record



