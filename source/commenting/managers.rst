

Managers
========


Commenting Profile
------------------

.. py:class:: CommentingProfile(osid_managers.OsidProfile, commenting_managers.CommentingProfile)
    The commenting profile describes the interoperability among commenting services.

    .. py:method:: supports_visible_federation():
        :noindex:


    .. py:method:: supports_comment_lookup():
        :noindex:


    .. py:method:: supports_rating_lookup():
        :noindex:


    .. py:method:: supports_comment_query():
        :noindex:


    .. py:method:: supports_comment_search():
        :noindex:


    .. py:method:: supports_comment_admin():
        :noindex:


    .. py:method:: supports_comment_notification():
        :noindex:


    .. py:method:: supports_comment_book():
        :noindex:


    .. py:method:: supports_comment_book_assignment():
        :noindex:


    .. py:method:: supports_comment_smart_book():
        :noindex:


    .. py:method:: supports_book_lookup():
        :noindex:


    .. py:method:: supports_book_query():
        :noindex:


    .. py:method:: supports_book_search():
        :noindex:


    .. py:method:: supports_book_admin():
        :noindex:


    .. py:method:: supports_book_notification():
        :noindex:


    .. py:method:: supports_book_hierarchy():
        :noindex:


    .. py:method:: supports_book_hierarchy_design():
        :noindex:


    .. py:method:: supports_commenting_batch():
        :noindex:


    .. py:method:: get_comment_record_types():
        :noindex:


    .. py:attribute:: comment_record_types
        :noindex:


    .. py:method:: supports_comment_record_type(comment_record_type):
        :noindex:


    .. py:method:: get_comment_search_record_types():
        :noindex:


    .. py:attribute:: comment_search_record_types
        :noindex:


    .. py:method:: supports_comment_search_record_type(comment_search_record_type):
        :noindex:


    .. py:method:: get_book_record_types():
        :noindex:


    .. py:attribute:: book_record_types
        :noindex:


    .. py:method:: supports_book_record_type(book_record_type):
        :noindex:


    .. py:method:: get_book_search_record_types():
        :noindex:


    .. py:attribute:: book_search_record_types
        :noindex:


    .. py:method:: supports_book_search_record_type(book_search_record_type):
        :noindex:


Commenting Manager
------------------

.. py:class:: CommentingManager(osid_managers.OsidManager, CommentingProfile, commenting_managers.CommentingManager)
        :noindex:

    .. py:method:: get_comment_lookup_session():
        :noindex:


    .. py:attribute:: comment_lookup_session
        :noindex:


    .. py:method:: get_comment_lookup_session_for_book(book_id):
        :noindex:


    .. py:method:: get_rating_lookup_session():
        :noindex:


    .. py:attribute:: rating_lookup_session
        :noindex:


    .. py:method:: get_rating_lookup_session_for_book(book_id):
        :noindex:


    .. py:method:: get_comment_query_session():
        :noindex:


    .. py:attribute:: comment_query_session
        :noindex:


    .. py:method:: get_comment_query_session_for_book(book_id):
        :noindex:


    .. py:method:: get_comment_search_session():
        :noindex:


    .. py:attribute:: comment_search_session
        :noindex:


    .. py:method:: get_comment_search_session_for_book(book_id):
        :noindex:


    .. py:method:: get_comment_admin_session():
        :noindex:


    .. py:attribute:: comment_admin_session
        :noindex:


    .. py:method:: get_comment_admin_session_for_book(book_id):
        :noindex:


    .. py:method:: get_comment_notification_session(comment_receiver):
        :noindex:


    .. py:method:: get_comment_notification_session_for_book(comment_receiver, book_id):
        :noindex:


    .. py:method:: get_comment_book_session():
        :noindex:


    .. py:attribute:: comment_book_session
        :noindex:


    .. py:method:: get_comment_book_assignment_session():
        :noindex:


    .. py:attribute:: comment_book_assignment_session
        :noindex:


    .. py:method:: get_comment_smart_book_session(book_id):
        :noindex:


    .. py:method:: get_book_lookup_session():
        :noindex:


    .. py:attribute:: book_lookup_session
        :noindex:


    .. py:method:: get_book_query_session():
        :noindex:


    .. py:attribute:: book_query_session
        :noindex:


    .. py:method:: get_book_search_session():
        :noindex:


    .. py:attribute:: book_search_session
        :noindex:


    .. py:method:: get_book_admin_session():
        :noindex:


    .. py:attribute:: book_admin_session
        :noindex:


    .. py:method:: get_book_notification_session(book_receiver):
        :noindex:


    .. py:method:: get_book_hierarchy_session():
        :noindex:


    .. py:attribute:: book_hierarchy_session
        :noindex:


    .. py:method:: get_book_hierarchy_design_session():
        :noindex:


    .. py:attribute:: book_hierarchy_design_session
        :noindex:


    .. py:method:: get_commenting_batch_manager():
        :noindex:


    .. py:attribute:: commenting_batch_manager
        :noindex:


Commenting Proxy Manager
------------------------

.. py:class:: CommentingProxyManager(osid_managers.OsidProxyManager, CommentingProfile, commenting_managers.CommentingProxyManager)
        :noindex:

    .. py:method:: get_comment_lookup_session(proxy):
        :noindex:


    .. py:method:: get_comment_lookup_session_for_book(book_id, proxy):
        :noindex:


    .. py:method:: get_rating_lookup_session(proxy):
        :noindex:


    .. py:method:: get_rating_lookup_session_for_book(book_id, proxy):
        :noindex:


    .. py:method:: get_comment_query_session(proxy):
        :noindex:


    .. py:method:: get_comment_query_session_for_book(book_id, proxy):
        :noindex:


    .. py:method:: get_comment_search_session(proxy):
        :noindex:


    .. py:method:: get_comment_search_session_for_book(book_id, proxy):
        :noindex:


    .. py:method:: get_comment_admin_session(proxy):
        :noindex:


    .. py:method:: get_comment_admin_session_for_book(book_id, proxy):
        :noindex:


    .. py:method:: get_comment_notification_session(comment_receiver, proxy):
        :noindex:


    .. py:method:: get_comment_notification_session_for_book(comment_receiver, book_id, proxy):
        :noindex:


    .. py:method:: get_comment_book_session(proxy):
        :noindex:


    .. py:method:: get_comment_book_assignment_session(proxy):
        :noindex:


    .. py:method:: get_comment_smart_book_session(book_id, proxy):
        :noindex:


    .. py:method:: get_book_lookup_session(proxy):
        :noindex:


    .. py:method:: get_book_query_session(proxy):
        :noindex:


    .. py:method:: get_book_search_session(proxy):
        :noindex:


    .. py:method:: get_book_admin_session(proxy):
        :noindex:


    .. py:method:: get_book_notification_session(book_receiver, proxy):
        :noindex:


    .. py:method:: get_book_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_book_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_commenting_batch_proxy_manager():
        :noindex:


    .. py:attribute:: commenting_batch_proxy_manager
        :noindex:


