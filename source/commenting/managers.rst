
.. currentmodule:: dlkit.commenting.managers
.. automodule:: dlkit.commenting.managers

Managers
========


Commenting Profile
------------------

.. autoclass:: CommentingProfile
   :show-inheritance:

   .. automethod:: CommentingProfile.supports_visible_federation

   .. automethod:: CommentingProfile.supports_comment_lookup

   .. automethod:: CommentingProfile.supports_rating_lookup

   .. automethod:: CommentingProfile.supports_comment_query

   .. automethod:: CommentingProfile.supports_comment_search

   .. automethod:: CommentingProfile.supports_comment_admin

   .. automethod:: CommentingProfile.supports_comment_notification

   .. automethod:: CommentingProfile.supports_comment_book

   .. automethod:: CommentingProfile.supports_comment_book_assignment

   .. automethod:: CommentingProfile.supports_comment_smart_book

   .. automethod:: CommentingProfile.supports_book_lookup

   .. automethod:: CommentingProfile.supports_book_query

   .. automethod:: CommentingProfile.supports_book_search

   .. automethod:: CommentingProfile.supports_book_admin

   .. automethod:: CommentingProfile.supports_book_notification

   .. automethod:: CommentingProfile.supports_book_hierarchy

   .. automethod:: CommentingProfile.supports_book_hierarchy_design

   .. automethod:: CommentingProfile.supports_commenting_batch

   .. autoattribute:: CommentingProfile.comment_record_types

   .. automethod:: CommentingProfile.supports_comment_record_type

   .. autoattribute:: CommentingProfile.comment_search_record_types

   .. automethod:: CommentingProfile.supports_comment_search_record_type

   .. autoattribute:: CommentingProfile.book_record_types

   .. automethod:: CommentingProfile.supports_book_record_type

   .. autoattribute:: CommentingProfile.book_search_record_types

   .. automethod:: CommentingProfile.supports_book_search_record_type

Commenting Manager
------------------

.. autoclass:: CommentingManager
   :show-inheritance:

   .. autoattribute:: CommentingManager.comment_lookup_session

   .. automethod:: CommentingManager.get_comment_lookup_session_for_book

   .. autoattribute:: CommentingManager.rating_lookup_session

   .. automethod:: CommentingManager.get_rating_lookup_session_for_book

   .. autoattribute:: CommentingManager.comment_query_session

   .. automethod:: CommentingManager.get_comment_query_session_for_book

   .. autoattribute:: CommentingManager.comment_search_session

   .. automethod:: CommentingManager.get_comment_search_session_for_book

   .. autoattribute:: CommentingManager.comment_admin_session

   .. automethod:: CommentingManager.get_comment_admin_session_for_book

   .. automethod:: CommentingManager.get_comment_notification_session

   .. automethod:: CommentingManager.get_comment_notification_session_for_book

   .. autoattribute:: CommentingManager.comment_book_session

   .. autoattribute:: CommentingManager.comment_book_assignment_session

   .. automethod:: CommentingManager.get_comment_smart_book_session

   .. autoattribute:: CommentingManager.book_lookup_session

   .. autoattribute:: CommentingManager.book_query_session

   .. autoattribute:: CommentingManager.book_search_session

   .. autoattribute:: CommentingManager.book_admin_session

   .. automethod:: CommentingManager.get_book_notification_session

   .. autoattribute:: CommentingManager.book_hierarchy_session

   .. autoattribute:: CommentingManager.book_hierarchy_design_session

   .. autoattribute:: CommentingManager.commenting_batch_manager

Commenting Proxy Manager
------------------------

.. autoclass:: CommentingProxyManager
   :show-inheritance:

   .. automethod:: CommentingProxyManager.get_comment_lookup_session

   .. automethod:: CommentingProxyManager.get_comment_lookup_session_for_book

   .. automethod:: CommentingProxyManager.get_rating_lookup_session

   .. automethod:: CommentingProxyManager.get_rating_lookup_session_for_book

   .. automethod:: CommentingProxyManager.get_comment_query_session

   .. automethod:: CommentingProxyManager.get_comment_query_session_for_book

   .. automethod:: CommentingProxyManager.get_comment_search_session

   .. automethod:: CommentingProxyManager.get_comment_search_session_for_book

   .. automethod:: CommentingProxyManager.get_comment_admin_session

   .. automethod:: CommentingProxyManager.get_comment_admin_session_for_book

   .. automethod:: CommentingProxyManager.get_comment_notification_session

   .. automethod:: CommentingProxyManager.get_comment_notification_session_for_book

   .. automethod:: CommentingProxyManager.get_comment_book_session

   .. automethod:: CommentingProxyManager.get_comment_book_assignment_session

   .. automethod:: CommentingProxyManager.get_comment_smart_book_session

   .. automethod:: CommentingProxyManager.get_book_lookup_session

   .. automethod:: CommentingProxyManager.get_book_query_session

   .. automethod:: CommentingProxyManager.get_book_search_session

   .. automethod:: CommentingProxyManager.get_book_admin_session

   .. automethod:: CommentingProxyManager.get_book_notification_session

   .. automethod:: CommentingProxyManager.get_book_hierarchy_session

   .. automethod:: CommentingProxyManager.get_book_hierarchy_design_session

   .. autoattribute:: CommentingProxyManager.commenting_batch_proxy_manager

