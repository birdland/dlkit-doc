.. currentmodule:: dlkit.services.commenting
.. automodule:: dlkit.services.commenting

Services
========


Commenting Manager
------------------

.. autoclass:: CommentingManager
   :show-inheritance:

   .. autoattribute:: CommentingManager.commenting_batch_manager



Commenting Profile Methods
__________________

   .. automethod:: CommentingManager.supports_visible_federation

   .. automethod:: CommentingManager.supports_comment_lookup

   .. automethod:: CommentingManager.supports_rating_lookup

   .. automethod:: CommentingManager.supports_comment_query

   .. automethod:: CommentingManager.supports_comment_search

   .. automethod:: CommentingManager.supports_comment_admin

   .. automethod:: CommentingManager.supports_comment_notification

   .. automethod:: CommentingManager.supports_comment_book

   .. automethod:: CommentingManager.supports_comment_book_assignment

   .. automethod:: CommentingManager.supports_comment_smart_book

   .. automethod:: CommentingManager.supports_book_lookup

   .. automethod:: CommentingManager.supports_book_query

   .. automethod:: CommentingManager.supports_book_search

   .. automethod:: CommentingManager.supports_book_admin

   .. automethod:: CommentingManager.supports_book_notification

   .. automethod:: CommentingManager.supports_book_hierarchy

   .. automethod:: CommentingManager.supports_book_hierarchy_design

   .. automethod:: CommentingManager.supports_commenting_batch

   .. autoattribute:: CommentingManager.comment_record_types

   .. automethod:: CommentingManager.supports_comment_record_type

   .. autoattribute:: CommentingManager.comment_search_record_types

   .. automethod:: CommentingManager.supports_comment_search_record_type

   .. autoattribute:: CommentingManager.book_record_types

   .. automethod:: CommentingManager.supports_book_record_type

   .. autoattribute:: CommentingManager.book_search_record_types

   .. automethod:: CommentingManager.supports_book_search_record_type



Book Lookup
___________

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



Book Query
__________

   .. automethod:: CommentingManager.can_search_books

   .. autoattribute:: CommentingManager.book_query

   .. automethod:: CommentingManager.get_books_by_query



Book Search
___________

   .. autoattribute:: CommentingManager.book_search

   .. autoattribute:: CommentingManager.book_search_order

   .. automethod:: CommentingManager.get_books_by_search

   .. automethod:: CommentingManager.get_book_query_from_inspector



Book Admin
__________

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



Book Notification
_________________

   .. automethod:: CommentingManager.can_register_for_book_notifications

   .. automethod:: CommentingManager.register_for_new_books

   .. automethod:: CommentingManager.register_for_new_book_ancestors

   .. automethod:: CommentingManager.register_for_new_book_descendants

   .. automethod:: CommentingManager.register_for_changed_books

   .. automethod:: CommentingManager.register_for_changed_book

   .. automethod:: CommentingManager.register_for_deleted_books

   .. automethod:: CommentingManager.register_for_deleted_book

   .. automethod:: CommentingManager.register_for_deleted_book_ancestors

   .. automethod:: CommentingManager.register_for_deleted_book_descendants



Book Hierarchy
______________

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



Book Hierarchy Design
_____________________

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

   .. autoattribute:: CommentingProxyManager.commenting_batch_proxy_manager



Commenting Profile Methods
__________________

   .. automethod:: CommentingProxyManager.supports_visible_federation

   .. automethod:: CommentingProxyManager.supports_comment_lookup

   .. automethod:: CommentingProxyManager.supports_rating_lookup

   .. automethod:: CommentingProxyManager.supports_comment_query

   .. automethod:: CommentingProxyManager.supports_comment_search

   .. automethod:: CommentingProxyManager.supports_comment_admin

   .. automethod:: CommentingProxyManager.supports_comment_notification

   .. automethod:: CommentingProxyManager.supports_comment_book

   .. automethod:: CommentingProxyManager.supports_comment_book_assignment

   .. automethod:: CommentingProxyManager.supports_comment_smart_book

   .. automethod:: CommentingProxyManager.supports_book_lookup

   .. automethod:: CommentingProxyManager.supports_book_query

   .. automethod:: CommentingProxyManager.supports_book_search

   .. automethod:: CommentingProxyManager.supports_book_admin

   .. automethod:: CommentingProxyManager.supports_book_notification

   .. automethod:: CommentingProxyManager.supports_book_hierarchy

   .. automethod:: CommentingProxyManager.supports_book_hierarchy_design

   .. automethod:: CommentingProxyManager.supports_commenting_batch

   .. autoattribute:: CommentingProxyManager.comment_record_types

   .. automethod:: CommentingProxyManager.supports_comment_record_type

   .. autoattribute:: CommentingProxyManager.comment_search_record_types

   .. automethod:: CommentingProxyManager.supports_comment_search_record_type

   .. autoattribute:: CommentingProxyManager.book_record_types

   .. automethod:: CommentingProxyManager.supports_book_record_type

   .. autoattribute:: CommentingProxyManager.book_search_record_types

   .. automethod:: CommentingProxyManager.supports_book_search_record_type



Book Lookup
___________

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



Book Query
__________

   .. automethod:: CommentingProxyManager.can_search_books

   .. autoattribute:: CommentingProxyManager.book_query

   .. automethod:: CommentingProxyManager.get_books_by_query



Book Search
___________

   .. autoattribute:: CommentingProxyManager.book_search

   .. autoattribute:: CommentingProxyManager.book_search_order

   .. automethod:: CommentingProxyManager.get_books_by_search

   .. automethod:: CommentingProxyManager.get_book_query_from_inspector



Book Admin
__________

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



Book Notification
_________________

   .. automethod:: CommentingProxyManager.can_register_for_book_notifications

   .. automethod:: CommentingProxyManager.register_for_new_books

   .. automethod:: CommentingProxyManager.register_for_new_book_ancestors

   .. automethod:: CommentingProxyManager.register_for_new_book_descendants

   .. automethod:: CommentingProxyManager.register_for_changed_books

   .. automethod:: CommentingProxyManager.register_for_changed_book

   .. automethod:: CommentingProxyManager.register_for_deleted_books

   .. automethod:: CommentingProxyManager.register_for_deleted_book

   .. automethod:: CommentingProxyManager.register_for_deleted_book_ancestors

   .. automethod:: CommentingProxyManager.register_for_deleted_book_descendants



Book Hierarchy
______________

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



Book Hierarchy Design
_____________________

   .. autoattribute:: CommentingProxyManager.book_hierarchy_id

   .. autoattribute:: CommentingProxyManager.book_hierarchy

   .. automethod:: CommentingProxyManager.can_modify_book_hierarchy

   .. automethod:: CommentingProxyManager.add_root_book

   .. automethod:: CommentingProxyManager.remove_root_book

   .. automethod:: CommentingProxyManager.add_child_book

   .. automethod:: CommentingProxyManager.remove_child_book

   .. automethod:: CommentingProxyManager.remove_child_books



