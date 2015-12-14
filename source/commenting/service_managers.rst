
.. currentmodule:: dlkit.services.commenting
.. automodule:: dlkit.services.commenting

Service Managers
================


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



Book Lookup Methods
-------------------

   .. automethod:: CommentingManager.can_lookup_books

   .. automethod:: CommentingManager.use_comparative_book_view

   .. automethod:: CommentingManager.use_plenary_book_view

   .. automethod:: CommentingManager.get_book

   .. automethod:: CommentingManager.get_books_by_ids

   .. automethod:: CommentingManager.get_books_by_genus_type

   .. automethod:: CommentingManager.get_books_by_parent_genus_type

   .. automethod:: CommentingManager.get_books_by_record_type

   .. automethod:: CommentingManager.get_books_by_provider

   .. autoattribute:: CommentingManager.books



Book Admin Methods
------------------

   .. automethod:: CommentingManager.can_create_books

   .. automethod:: CommentingManager.can_create_book_with_record_types

   .. automethod:: CommentingManager.get_book_form_for_create

   .. automethod:: CommentingManager.create_book

   .. automethod:: CommentingManager.can_update_books

   .. automethod:: CommentingManager.get_book_form_for_update

   .. automethod:: CommentingManager.update_book

   .. automethod:: CommentingManager.can_delete_books

   .. automethod:: CommentingManager.delete_book

   .. automethod:: CommentingManager.can_manage_book_aliases

   .. automethod:: CommentingManager.alias_book



Book Hierarchy Methods
----------------------

   .. autoattribute:: CommentingManager.book_hierarchy_id

   .. autoattribute:: CommentingManager.book_hierarchy

   .. automethod:: CommentingManager.can_access_book_hierarchy

   .. automethod:: CommentingManager.use_comparative_book_view

   .. automethod:: CommentingManager.use_plenary_book_view

   .. autoattribute:: CommentingManager.root_book_ids

   .. autoattribute:: CommentingManager.root_books

   .. automethod:: CommentingManager.has_parent_books

   .. automethod:: CommentingManager.is_parent_of_book

   .. automethod:: CommentingManager.get_parent_book_ids

   .. automethod:: CommentingManager.get_parent_books

   .. automethod:: CommentingManager.is_ancestor_of_book

   .. automethod:: CommentingManager.has_child_books

   .. automethod:: CommentingManager.is_child_of_book

   .. automethod:: CommentingManager.get_child_book_ids

   .. automethod:: CommentingManager.get_child_books

   .. automethod:: CommentingManager.is_descendant_of_book

   .. automethod:: CommentingManager.get_book_node_ids

   .. automethod:: CommentingManager.get_book_nodes



Book Hierarchy Design Methods
-----------------------------

   .. autoattribute:: CommentingManager.book_hierarchy_id

   .. autoattribute:: CommentingManager.book_hierarchy

   .. automethod:: CommentingManager.can_modify_book_hierarchy

   .. automethod:: CommentingManager.add_root_book

   .. automethod:: CommentingManager.remove_root_book

   .. automethod:: CommentingManager.add_child_book

   .. automethod:: CommentingManager.remove_child_book

   .. automethod:: CommentingManager.remove_child_books



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



Book Lookup Methods
-------------------

   .. automethod:: CommentingProxyManager.can_lookup_books

   .. automethod:: CommentingProxyManager.use_comparative_book_view

   .. automethod:: CommentingProxyManager.use_plenary_book_view

   .. automethod:: CommentingProxyManager.get_book

   .. automethod:: CommentingProxyManager.get_books_by_ids

   .. automethod:: CommentingProxyManager.get_books_by_genus_type

   .. automethod:: CommentingProxyManager.get_books_by_parent_genus_type

   .. automethod:: CommentingProxyManager.get_books_by_record_type

   .. automethod:: CommentingProxyManager.get_books_by_provider

   .. autoattribute:: CommentingProxyManager.books



Book Admin Methods
------------------

   .. automethod:: CommentingProxyManager.can_create_books

   .. automethod:: CommentingProxyManager.can_create_book_with_record_types

   .. automethod:: CommentingProxyManager.get_book_form_for_create

   .. automethod:: CommentingProxyManager.create_book

   .. automethod:: CommentingProxyManager.can_update_books

   .. automethod:: CommentingProxyManager.get_book_form_for_update

   .. automethod:: CommentingProxyManager.update_book

   .. automethod:: CommentingProxyManager.can_delete_books

   .. automethod:: CommentingProxyManager.delete_book

   .. automethod:: CommentingProxyManager.can_manage_book_aliases

   .. automethod:: CommentingProxyManager.alias_book



Book Hierarchy Methods
----------------------

   .. autoattribute:: CommentingProxyManager.book_hierarchy_id

   .. autoattribute:: CommentingProxyManager.book_hierarchy

   .. automethod:: CommentingProxyManager.can_access_book_hierarchy

   .. automethod:: CommentingProxyManager.use_comparative_book_view

   .. automethod:: CommentingProxyManager.use_plenary_book_view

   .. autoattribute:: CommentingProxyManager.root_book_ids

   .. autoattribute:: CommentingProxyManager.root_books

   .. automethod:: CommentingProxyManager.has_parent_books

   .. automethod:: CommentingProxyManager.is_parent_of_book

   .. automethod:: CommentingProxyManager.get_parent_book_ids

   .. automethod:: CommentingProxyManager.get_parent_books

   .. automethod:: CommentingProxyManager.is_ancestor_of_book

   .. automethod:: CommentingProxyManager.has_child_books

   .. automethod:: CommentingProxyManager.is_child_of_book

   .. automethod:: CommentingProxyManager.get_child_book_ids

   .. automethod:: CommentingProxyManager.get_child_books

   .. automethod:: CommentingProxyManager.is_descendant_of_book

   .. automethod:: CommentingProxyManager.get_book_node_ids

   .. automethod:: CommentingProxyManager.get_book_nodes



Book Hierarchy Design Methods
-----------------------------

   .. autoattribute:: CommentingProxyManager.book_hierarchy_id

   .. autoattribute:: CommentingProxyManager.book_hierarchy

   .. automethod:: CommentingProxyManager.can_modify_book_hierarchy

   .. automethod:: CommentingProxyManager.add_root_book

   .. automethod:: CommentingProxyManager.remove_root_book

   .. automethod:: CommentingProxyManager.add_child_book

   .. automethod:: CommentingProxyManager.remove_child_book

   .. automethod:: CommentingProxyManager.remove_child_books



