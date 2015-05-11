.. currentmodule:: dlkit.services.commenting
.. automodule:: dlkit.services.commenting

Service Managers
================


Commenting Manager
------------------

.. autoclass:: CommentingManager
   :show-inheritance:

   .. autoattribute:: CommentingManager.commenting_batch_manager



Commenting Profile Methods
--------------------------

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



