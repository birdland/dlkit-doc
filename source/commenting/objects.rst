
.. currentmodule:: dlkit.commenting.objects
.. automodule:: dlkit.commenting.objects

Objects
=======


Comment
-------

.. autoclass:: Comment
   :show-inheritance:

   .. autoattribute:: Comment.reference_id

   .. autoattribute:: Comment.commentor_id

   .. autoattribute:: Comment.commentor

   .. autoattribute:: Comment.commenting_agent_id

   .. autoattribute:: Comment.commenting_agent

   .. autoattribute:: Comment.text

   .. automethod:: Comment.has_rating

   .. autoattribute:: Comment.rating_id

   .. autoattribute:: Comment.rating

   .. automethod:: Comment.get_comment_record



Book Lookup Methods
-------------------

   .. automethod:: BookLookupSession.can_lookup_books

   .. automethod:: BookLookupSession.use_comparative_book_view

   .. automethod:: BookLookupSession.use_plenary_book_view

   .. automethod:: BookLookupSession.get_book

   .. automethod:: BookLookupSession.get_books_by_ids

   .. automethod:: BookLookupSession.get_books_by_genus_type

   .. automethod:: BookLookupSession.get_books_by_parent_genus_type

   .. automethod:: BookLookupSession.get_books_by_record_type

   .. automethod:: BookLookupSession.get_books_by_provider

   .. autoattribute:: BookLookupSession.books



Book Admin Methods
------------------

   .. automethod:: BookAdminSession.can_create_books

   .. automethod:: BookAdminSession.can_create_book_with_record_types

   .. automethod:: BookAdminSession.get_book_form_for_create

   .. automethod:: BookAdminSession.create_book

   .. automethod:: BookAdminSession.can_update_books

   .. automethod:: BookAdminSession.get_book_form_for_update

   .. automethod:: BookAdminSession.update_book

   .. automethod:: BookAdminSession.can_delete_books

   .. automethod:: BookAdminSession.delete_book

   .. automethod:: BookAdminSession.can_manage_book_aliases

   .. automethod:: BookAdminSession.alias_book



Book Hierarchy Methods
----------------------

   .. autoattribute:: BookHierarchySession.book_hierarchy_id

   .. autoattribute:: BookHierarchySession.book_hierarchy

   .. automethod:: BookHierarchySession.can_access_book_hierarchy

   .. automethod:: BookHierarchySession.use_comparative_book_view

   .. automethod:: BookHierarchySession.use_plenary_book_view

   .. autoattribute:: BookHierarchySession.root_book_ids

   .. autoattribute:: BookHierarchySession.root_books

   .. automethod:: BookHierarchySession.has_parent_books

   .. automethod:: BookHierarchySession.is_parent_of_book

   .. automethod:: BookHierarchySession.get_parent_book_ids

   .. automethod:: BookHierarchySession.get_parent_books

   .. automethod:: BookHierarchySession.is_ancestor_of_book

   .. automethod:: BookHierarchySession.has_child_books

   .. automethod:: BookHierarchySession.is_child_of_book

   .. automethod:: BookHierarchySession.get_child_book_ids

   .. automethod:: BookHierarchySession.get_child_books

   .. automethod:: BookHierarchySession.is_descendant_of_book

   .. automethod:: BookHierarchySession.get_book_node_ids

   .. automethod:: BookHierarchySession.get_book_nodes



Book Hierarchy Design Methods
-----------------------------

   .. autoattribute:: BookHierarchyDesignSession.book_hierarchy_id

   .. autoattribute:: BookHierarchyDesignSession.book_hierarchy

   .. automethod:: BookHierarchyDesignSession.can_modify_book_hierarchy

   .. automethod:: BookHierarchyDesignSession.add_root_book

   .. automethod:: BookHierarchyDesignSession.remove_root_book

   .. automethod:: BookHierarchyDesignSession.add_child_book

   .. automethod:: BookHierarchyDesignSession.remove_child_book

   .. automethod:: BookHierarchyDesignSession.remove_child_books



Comment Lookup Methods
----------------------

   .. autoattribute:: CommentLookupSession.book_id

   .. autoattribute:: CommentLookupSession.book

   .. automethod:: CommentLookupSession.can_lookup_comments

   .. automethod:: CommentLookupSession.use_comparative_comment_view

   .. automethod:: CommentLookupSession.use_plenary_comment_view

   .. automethod:: CommentLookupSession.use_federated_book_view

   .. automethod:: CommentLookupSession.use_isolated_book_view

   .. automethod:: CommentLookupSession.use_effective_comment_view

   .. automethod:: CommentLookupSession.use_any_effective_comment_view

   .. automethod:: CommentLookupSession.get_comment

   .. automethod:: CommentLookupSession.get_comments_by_ids

   .. automethod:: CommentLookupSession.get_comments_by_genus_type

   .. automethod:: CommentLookupSession.get_comments_by_parent_genus_type

   .. automethod:: CommentLookupSession.get_comments_by_record_type

   .. automethod:: CommentLookupSession.get_comments_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_on_date

   .. automethod:: CommentLookupSession.get_comments_for_commentor

   .. automethod:: CommentLookupSession.get_comments_for_commentor_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_on_date

   .. automethod:: CommentLookupSession.get_comments_for_reference

   .. automethod:: CommentLookupSession.get_comments_for_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_reference

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_for_commentor_and_reference

   .. automethod:: CommentLookupSession.get_comments_for_commentor_and_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_and_reference

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_and_reference_on_date

   .. autoattribute:: CommentLookupSession.comments



Comment Query Methods
---------------------

   .. autoattribute:: CommentQuerySession.book_id

   .. autoattribute:: CommentQuerySession.book

   .. automethod:: CommentQuerySession.can_search_comments

   .. automethod:: CommentQuerySession.use_federated_book_view

   .. automethod:: CommentQuerySession.use_isolated_book_view

   .. autoattribute:: CommentQuerySession.comment_query

   .. automethod:: CommentQuerySession.get_comments_by_query



Comment Admin Methods
---------------------

   .. autoattribute:: CommentAdminSession.book_id

   .. autoattribute:: CommentAdminSession.book

   .. automethod:: CommentAdminSession.can_create_comments

   .. automethod:: CommentAdminSession.can_create_comment_with_record_types

   .. automethod:: CommentAdminSession.get_comment_form_for_create

   .. automethod:: CommentAdminSession.create_comment

   .. automethod:: CommentAdminSession.can_update_comments

   .. automethod:: CommentAdminSession.get_comment_form_for_update

   .. automethod:: CommentAdminSession.update_comment

   .. automethod:: CommentAdminSession.can_delete_comments

   .. automethod:: CommentAdminSession.delete_comment

   .. automethod:: CommentAdminSession.can_manage_comment_aliases

   .. automethod:: CommentAdminSession.alias_comment



Comment Form
------------

.. autoclass:: CommentForm
   :show-inheritance:

   .. autoattribute:: CommentForm.text_metadata

   .. autoattribute:: CommentForm.text

   .. autoattribute:: CommentForm.rating_metadata

   .. autoattribute:: CommentForm.rating

   .. automethod:: CommentForm.get_comment_form_record



Book Lookup Methods
-------------------

   .. automethod:: BookLookupSession.can_lookup_books

   .. automethod:: BookLookupSession.use_comparative_book_view

   .. automethod:: BookLookupSession.use_plenary_book_view

   .. automethod:: BookLookupSession.get_book

   .. automethod:: BookLookupSession.get_books_by_ids

   .. automethod:: BookLookupSession.get_books_by_genus_type

   .. automethod:: BookLookupSession.get_books_by_parent_genus_type

   .. automethod:: BookLookupSession.get_books_by_record_type

   .. automethod:: BookLookupSession.get_books_by_provider

   .. autoattribute:: BookLookupSession.books



Book Admin Methods
------------------

   .. automethod:: BookAdminSession.can_create_books

   .. automethod:: BookAdminSession.can_create_book_with_record_types

   .. automethod:: BookAdminSession.get_book_form_for_create

   .. automethod:: BookAdminSession.create_book

   .. automethod:: BookAdminSession.can_update_books

   .. automethod:: BookAdminSession.get_book_form_for_update

   .. automethod:: BookAdminSession.update_book

   .. automethod:: BookAdminSession.can_delete_books

   .. automethod:: BookAdminSession.delete_book

   .. automethod:: BookAdminSession.can_manage_book_aliases

   .. automethod:: BookAdminSession.alias_book



Book Hierarchy Methods
----------------------

   .. autoattribute:: BookHierarchySession.book_hierarchy_id

   .. autoattribute:: BookHierarchySession.book_hierarchy

   .. automethod:: BookHierarchySession.can_access_book_hierarchy

   .. automethod:: BookHierarchySession.use_comparative_book_view

   .. automethod:: BookHierarchySession.use_plenary_book_view

   .. autoattribute:: BookHierarchySession.root_book_ids

   .. autoattribute:: BookHierarchySession.root_books

   .. automethod:: BookHierarchySession.has_parent_books

   .. automethod:: BookHierarchySession.is_parent_of_book

   .. automethod:: BookHierarchySession.get_parent_book_ids

   .. automethod:: BookHierarchySession.get_parent_books

   .. automethod:: BookHierarchySession.is_ancestor_of_book

   .. automethod:: BookHierarchySession.has_child_books

   .. automethod:: BookHierarchySession.is_child_of_book

   .. automethod:: BookHierarchySession.get_child_book_ids

   .. automethod:: BookHierarchySession.get_child_books

   .. automethod:: BookHierarchySession.is_descendant_of_book

   .. automethod:: BookHierarchySession.get_book_node_ids

   .. automethod:: BookHierarchySession.get_book_nodes



Book Hierarchy Design Methods
-----------------------------

   .. autoattribute:: BookHierarchyDesignSession.book_hierarchy_id

   .. autoattribute:: BookHierarchyDesignSession.book_hierarchy

   .. automethod:: BookHierarchyDesignSession.can_modify_book_hierarchy

   .. automethod:: BookHierarchyDesignSession.add_root_book

   .. automethod:: BookHierarchyDesignSession.remove_root_book

   .. automethod:: BookHierarchyDesignSession.add_child_book

   .. automethod:: BookHierarchyDesignSession.remove_child_book

   .. automethod:: BookHierarchyDesignSession.remove_child_books



Comment Lookup Methods
----------------------

   .. autoattribute:: CommentLookupSession.book_id

   .. autoattribute:: CommentLookupSession.book

   .. automethod:: CommentLookupSession.can_lookup_comments

   .. automethod:: CommentLookupSession.use_comparative_comment_view

   .. automethod:: CommentLookupSession.use_plenary_comment_view

   .. automethod:: CommentLookupSession.use_federated_book_view

   .. automethod:: CommentLookupSession.use_isolated_book_view

   .. automethod:: CommentLookupSession.use_effective_comment_view

   .. automethod:: CommentLookupSession.use_any_effective_comment_view

   .. automethod:: CommentLookupSession.get_comment

   .. automethod:: CommentLookupSession.get_comments_by_ids

   .. automethod:: CommentLookupSession.get_comments_by_genus_type

   .. automethod:: CommentLookupSession.get_comments_by_parent_genus_type

   .. automethod:: CommentLookupSession.get_comments_by_record_type

   .. automethod:: CommentLookupSession.get_comments_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_on_date

   .. automethod:: CommentLookupSession.get_comments_for_commentor

   .. automethod:: CommentLookupSession.get_comments_for_commentor_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_on_date

   .. automethod:: CommentLookupSession.get_comments_for_reference

   .. automethod:: CommentLookupSession.get_comments_for_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_reference

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_for_commentor_and_reference

   .. automethod:: CommentLookupSession.get_comments_for_commentor_and_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_and_reference

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_and_reference_on_date

   .. autoattribute:: CommentLookupSession.comments



Comment Query Methods
---------------------

   .. autoattribute:: CommentQuerySession.book_id

   .. autoattribute:: CommentQuerySession.book

   .. automethod:: CommentQuerySession.can_search_comments

   .. automethod:: CommentQuerySession.use_federated_book_view

   .. automethod:: CommentQuerySession.use_isolated_book_view

   .. autoattribute:: CommentQuerySession.comment_query

   .. automethod:: CommentQuerySession.get_comments_by_query



Comment Admin Methods
---------------------

   .. autoattribute:: CommentAdminSession.book_id

   .. autoattribute:: CommentAdminSession.book

   .. automethod:: CommentAdminSession.can_create_comments

   .. automethod:: CommentAdminSession.can_create_comment_with_record_types

   .. automethod:: CommentAdminSession.get_comment_form_for_create

   .. automethod:: CommentAdminSession.create_comment

   .. automethod:: CommentAdminSession.can_update_comments

   .. automethod:: CommentAdminSession.get_comment_form_for_update

   .. automethod:: CommentAdminSession.update_comment

   .. automethod:: CommentAdminSession.can_delete_comments

   .. automethod:: CommentAdminSession.delete_comment

   .. automethod:: CommentAdminSession.can_manage_comment_aliases

   .. automethod:: CommentAdminSession.alias_comment



Comment List
------------

.. autoclass:: CommentList
   :show-inheritance:

   .. autoattribute:: CommentList.next_comment

   .. automethod:: CommentList.get_next_comments



Book Lookup Methods
-------------------

   .. automethod:: BookLookupSession.can_lookup_books

   .. automethod:: BookLookupSession.use_comparative_book_view

   .. automethod:: BookLookupSession.use_plenary_book_view

   .. automethod:: BookLookupSession.get_book

   .. automethod:: BookLookupSession.get_books_by_ids

   .. automethod:: BookLookupSession.get_books_by_genus_type

   .. automethod:: BookLookupSession.get_books_by_parent_genus_type

   .. automethod:: BookLookupSession.get_books_by_record_type

   .. automethod:: BookLookupSession.get_books_by_provider

   .. autoattribute:: BookLookupSession.books



Book Admin Methods
------------------

   .. automethod:: BookAdminSession.can_create_books

   .. automethod:: BookAdminSession.can_create_book_with_record_types

   .. automethod:: BookAdminSession.get_book_form_for_create

   .. automethod:: BookAdminSession.create_book

   .. automethod:: BookAdminSession.can_update_books

   .. automethod:: BookAdminSession.get_book_form_for_update

   .. automethod:: BookAdminSession.update_book

   .. automethod:: BookAdminSession.can_delete_books

   .. automethod:: BookAdminSession.delete_book

   .. automethod:: BookAdminSession.can_manage_book_aliases

   .. automethod:: BookAdminSession.alias_book



Book Hierarchy Methods
----------------------

   .. autoattribute:: BookHierarchySession.book_hierarchy_id

   .. autoattribute:: BookHierarchySession.book_hierarchy

   .. automethod:: BookHierarchySession.can_access_book_hierarchy

   .. automethod:: BookHierarchySession.use_comparative_book_view

   .. automethod:: BookHierarchySession.use_plenary_book_view

   .. autoattribute:: BookHierarchySession.root_book_ids

   .. autoattribute:: BookHierarchySession.root_books

   .. automethod:: BookHierarchySession.has_parent_books

   .. automethod:: BookHierarchySession.is_parent_of_book

   .. automethod:: BookHierarchySession.get_parent_book_ids

   .. automethod:: BookHierarchySession.get_parent_books

   .. automethod:: BookHierarchySession.is_ancestor_of_book

   .. automethod:: BookHierarchySession.has_child_books

   .. automethod:: BookHierarchySession.is_child_of_book

   .. automethod:: BookHierarchySession.get_child_book_ids

   .. automethod:: BookHierarchySession.get_child_books

   .. automethod:: BookHierarchySession.is_descendant_of_book

   .. automethod:: BookHierarchySession.get_book_node_ids

   .. automethod:: BookHierarchySession.get_book_nodes



Book Hierarchy Design Methods
-----------------------------

   .. autoattribute:: BookHierarchyDesignSession.book_hierarchy_id

   .. autoattribute:: BookHierarchyDesignSession.book_hierarchy

   .. automethod:: BookHierarchyDesignSession.can_modify_book_hierarchy

   .. automethod:: BookHierarchyDesignSession.add_root_book

   .. automethod:: BookHierarchyDesignSession.remove_root_book

   .. automethod:: BookHierarchyDesignSession.add_child_book

   .. automethod:: BookHierarchyDesignSession.remove_child_book

   .. automethod:: BookHierarchyDesignSession.remove_child_books



Comment Lookup Methods
----------------------

   .. autoattribute:: CommentLookupSession.book_id

   .. autoattribute:: CommentLookupSession.book

   .. automethod:: CommentLookupSession.can_lookup_comments

   .. automethod:: CommentLookupSession.use_comparative_comment_view

   .. automethod:: CommentLookupSession.use_plenary_comment_view

   .. automethod:: CommentLookupSession.use_federated_book_view

   .. automethod:: CommentLookupSession.use_isolated_book_view

   .. automethod:: CommentLookupSession.use_effective_comment_view

   .. automethod:: CommentLookupSession.use_any_effective_comment_view

   .. automethod:: CommentLookupSession.get_comment

   .. automethod:: CommentLookupSession.get_comments_by_ids

   .. automethod:: CommentLookupSession.get_comments_by_genus_type

   .. automethod:: CommentLookupSession.get_comments_by_parent_genus_type

   .. automethod:: CommentLookupSession.get_comments_by_record_type

   .. automethod:: CommentLookupSession.get_comments_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_on_date

   .. automethod:: CommentLookupSession.get_comments_for_commentor

   .. automethod:: CommentLookupSession.get_comments_for_commentor_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_on_date

   .. automethod:: CommentLookupSession.get_comments_for_reference

   .. automethod:: CommentLookupSession.get_comments_for_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_reference

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_for_commentor_and_reference

   .. automethod:: CommentLookupSession.get_comments_for_commentor_and_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_and_reference

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_and_reference_on_date

   .. autoattribute:: CommentLookupSession.comments



Comment Query Methods
---------------------

   .. autoattribute:: CommentQuerySession.book_id

   .. autoattribute:: CommentQuerySession.book

   .. automethod:: CommentQuerySession.can_search_comments

   .. automethod:: CommentQuerySession.use_federated_book_view

   .. automethod:: CommentQuerySession.use_isolated_book_view

   .. autoattribute:: CommentQuerySession.comment_query

   .. automethod:: CommentQuerySession.get_comments_by_query



Comment Admin Methods
---------------------

   .. autoattribute:: CommentAdminSession.book_id

   .. autoattribute:: CommentAdminSession.book

   .. automethod:: CommentAdminSession.can_create_comments

   .. automethod:: CommentAdminSession.can_create_comment_with_record_types

   .. automethod:: CommentAdminSession.get_comment_form_for_create

   .. automethod:: CommentAdminSession.create_comment

   .. automethod:: CommentAdminSession.can_update_comments

   .. automethod:: CommentAdminSession.get_comment_form_for_update

   .. automethod:: CommentAdminSession.update_comment

   .. automethod:: CommentAdminSession.can_delete_comments

   .. automethod:: CommentAdminSession.delete_comment

   .. automethod:: CommentAdminSession.can_manage_comment_aliases

   .. automethod:: CommentAdminSession.alias_comment



Book Form
---------

.. autoclass:: BookForm
   :show-inheritance:

   .. automethod:: BookForm.get_book_form_record



Book Lookup Methods
-------------------

   .. automethod:: BookLookupSession.can_lookup_books

   .. automethod:: BookLookupSession.use_comparative_book_view

   .. automethod:: BookLookupSession.use_plenary_book_view

   .. automethod:: BookLookupSession.get_book

   .. automethod:: BookLookupSession.get_books_by_ids

   .. automethod:: BookLookupSession.get_books_by_genus_type

   .. automethod:: BookLookupSession.get_books_by_parent_genus_type

   .. automethod:: BookLookupSession.get_books_by_record_type

   .. automethod:: BookLookupSession.get_books_by_provider

   .. autoattribute:: BookLookupSession.books



Book Admin Methods
------------------

   .. automethod:: BookAdminSession.can_create_books

   .. automethod:: BookAdminSession.can_create_book_with_record_types

   .. automethod:: BookAdminSession.get_book_form_for_create

   .. automethod:: BookAdminSession.create_book

   .. automethod:: BookAdminSession.can_update_books

   .. automethod:: BookAdminSession.get_book_form_for_update

   .. automethod:: BookAdminSession.update_book

   .. automethod:: BookAdminSession.can_delete_books

   .. automethod:: BookAdminSession.delete_book

   .. automethod:: BookAdminSession.can_manage_book_aliases

   .. automethod:: BookAdminSession.alias_book



Book Hierarchy Methods
----------------------

   .. autoattribute:: BookHierarchySession.book_hierarchy_id

   .. autoattribute:: BookHierarchySession.book_hierarchy

   .. automethod:: BookHierarchySession.can_access_book_hierarchy

   .. automethod:: BookHierarchySession.use_comparative_book_view

   .. automethod:: BookHierarchySession.use_plenary_book_view

   .. autoattribute:: BookHierarchySession.root_book_ids

   .. autoattribute:: BookHierarchySession.root_books

   .. automethod:: BookHierarchySession.has_parent_books

   .. automethod:: BookHierarchySession.is_parent_of_book

   .. automethod:: BookHierarchySession.get_parent_book_ids

   .. automethod:: BookHierarchySession.get_parent_books

   .. automethod:: BookHierarchySession.is_ancestor_of_book

   .. automethod:: BookHierarchySession.has_child_books

   .. automethod:: BookHierarchySession.is_child_of_book

   .. automethod:: BookHierarchySession.get_child_book_ids

   .. automethod:: BookHierarchySession.get_child_books

   .. automethod:: BookHierarchySession.is_descendant_of_book

   .. automethod:: BookHierarchySession.get_book_node_ids

   .. automethod:: BookHierarchySession.get_book_nodes



Book Hierarchy Design Methods
-----------------------------

   .. autoattribute:: BookHierarchyDesignSession.book_hierarchy_id

   .. autoattribute:: BookHierarchyDesignSession.book_hierarchy

   .. automethod:: BookHierarchyDesignSession.can_modify_book_hierarchy

   .. automethod:: BookHierarchyDesignSession.add_root_book

   .. automethod:: BookHierarchyDesignSession.remove_root_book

   .. automethod:: BookHierarchyDesignSession.add_child_book

   .. automethod:: BookHierarchyDesignSession.remove_child_book

   .. automethod:: BookHierarchyDesignSession.remove_child_books



Comment Lookup Methods
----------------------

   .. autoattribute:: CommentLookupSession.book_id

   .. autoattribute:: CommentLookupSession.book

   .. automethod:: CommentLookupSession.can_lookup_comments

   .. automethod:: CommentLookupSession.use_comparative_comment_view

   .. automethod:: CommentLookupSession.use_plenary_comment_view

   .. automethod:: CommentLookupSession.use_federated_book_view

   .. automethod:: CommentLookupSession.use_isolated_book_view

   .. automethod:: CommentLookupSession.use_effective_comment_view

   .. automethod:: CommentLookupSession.use_any_effective_comment_view

   .. automethod:: CommentLookupSession.get_comment

   .. automethod:: CommentLookupSession.get_comments_by_ids

   .. automethod:: CommentLookupSession.get_comments_by_genus_type

   .. automethod:: CommentLookupSession.get_comments_by_parent_genus_type

   .. automethod:: CommentLookupSession.get_comments_by_record_type

   .. automethod:: CommentLookupSession.get_comments_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_on_date

   .. automethod:: CommentLookupSession.get_comments_for_commentor

   .. automethod:: CommentLookupSession.get_comments_for_commentor_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_on_date

   .. automethod:: CommentLookupSession.get_comments_for_reference

   .. automethod:: CommentLookupSession.get_comments_for_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_reference

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_for_commentor_and_reference

   .. automethod:: CommentLookupSession.get_comments_for_commentor_and_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_and_reference

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_and_reference_on_date

   .. autoattribute:: CommentLookupSession.comments



Comment Query Methods
---------------------

   .. autoattribute:: CommentQuerySession.book_id

   .. autoattribute:: CommentQuerySession.book

   .. automethod:: CommentQuerySession.can_search_comments

   .. automethod:: CommentQuerySession.use_federated_book_view

   .. automethod:: CommentQuerySession.use_isolated_book_view

   .. autoattribute:: CommentQuerySession.comment_query

   .. automethod:: CommentQuerySession.get_comments_by_query



Comment Admin Methods
---------------------

   .. autoattribute:: CommentAdminSession.book_id

   .. autoattribute:: CommentAdminSession.book

   .. automethod:: CommentAdminSession.can_create_comments

   .. automethod:: CommentAdminSession.can_create_comment_with_record_types

   .. automethod:: CommentAdminSession.get_comment_form_for_create

   .. automethod:: CommentAdminSession.create_comment

   .. automethod:: CommentAdminSession.can_update_comments

   .. automethod:: CommentAdminSession.get_comment_form_for_update

   .. automethod:: CommentAdminSession.update_comment

   .. automethod:: CommentAdminSession.can_delete_comments

   .. automethod:: CommentAdminSession.delete_comment

   .. automethod:: CommentAdminSession.can_manage_comment_aliases

   .. automethod:: CommentAdminSession.alias_comment



Book List
---------

.. autoclass:: BookList
   :show-inheritance:

   .. autoattribute:: BookList.next_book

   .. automethod:: BookList.get_next_books



Book Lookup Methods
-------------------

   .. automethod:: BookLookupSession.can_lookup_books

   .. automethod:: BookLookupSession.use_comparative_book_view

   .. automethod:: BookLookupSession.use_plenary_book_view

   .. automethod:: BookLookupSession.get_book

   .. automethod:: BookLookupSession.get_books_by_ids

   .. automethod:: BookLookupSession.get_books_by_genus_type

   .. automethod:: BookLookupSession.get_books_by_parent_genus_type

   .. automethod:: BookLookupSession.get_books_by_record_type

   .. automethod:: BookLookupSession.get_books_by_provider

   .. autoattribute:: BookLookupSession.books



Book Admin Methods
------------------

   .. automethod:: BookAdminSession.can_create_books

   .. automethod:: BookAdminSession.can_create_book_with_record_types

   .. automethod:: BookAdminSession.get_book_form_for_create

   .. automethod:: BookAdminSession.create_book

   .. automethod:: BookAdminSession.can_update_books

   .. automethod:: BookAdminSession.get_book_form_for_update

   .. automethod:: BookAdminSession.update_book

   .. automethod:: BookAdminSession.can_delete_books

   .. automethod:: BookAdminSession.delete_book

   .. automethod:: BookAdminSession.can_manage_book_aliases

   .. automethod:: BookAdminSession.alias_book



Book Hierarchy Methods
----------------------

   .. autoattribute:: BookHierarchySession.book_hierarchy_id

   .. autoattribute:: BookHierarchySession.book_hierarchy

   .. automethod:: BookHierarchySession.can_access_book_hierarchy

   .. automethod:: BookHierarchySession.use_comparative_book_view

   .. automethod:: BookHierarchySession.use_plenary_book_view

   .. autoattribute:: BookHierarchySession.root_book_ids

   .. autoattribute:: BookHierarchySession.root_books

   .. automethod:: BookHierarchySession.has_parent_books

   .. automethod:: BookHierarchySession.is_parent_of_book

   .. automethod:: BookHierarchySession.get_parent_book_ids

   .. automethod:: BookHierarchySession.get_parent_books

   .. automethod:: BookHierarchySession.is_ancestor_of_book

   .. automethod:: BookHierarchySession.has_child_books

   .. automethod:: BookHierarchySession.is_child_of_book

   .. automethod:: BookHierarchySession.get_child_book_ids

   .. automethod:: BookHierarchySession.get_child_books

   .. automethod:: BookHierarchySession.is_descendant_of_book

   .. automethod:: BookHierarchySession.get_book_node_ids

   .. automethod:: BookHierarchySession.get_book_nodes



Book Hierarchy Design Methods
-----------------------------

   .. autoattribute:: BookHierarchyDesignSession.book_hierarchy_id

   .. autoattribute:: BookHierarchyDesignSession.book_hierarchy

   .. automethod:: BookHierarchyDesignSession.can_modify_book_hierarchy

   .. automethod:: BookHierarchyDesignSession.add_root_book

   .. automethod:: BookHierarchyDesignSession.remove_root_book

   .. automethod:: BookHierarchyDesignSession.add_child_book

   .. automethod:: BookHierarchyDesignSession.remove_child_book

   .. automethod:: BookHierarchyDesignSession.remove_child_books



Comment Lookup Methods
----------------------

   .. autoattribute:: CommentLookupSession.book_id

   .. autoattribute:: CommentLookupSession.book

   .. automethod:: CommentLookupSession.can_lookup_comments

   .. automethod:: CommentLookupSession.use_comparative_comment_view

   .. automethod:: CommentLookupSession.use_plenary_comment_view

   .. automethod:: CommentLookupSession.use_federated_book_view

   .. automethod:: CommentLookupSession.use_isolated_book_view

   .. automethod:: CommentLookupSession.use_effective_comment_view

   .. automethod:: CommentLookupSession.use_any_effective_comment_view

   .. automethod:: CommentLookupSession.get_comment

   .. automethod:: CommentLookupSession.get_comments_by_ids

   .. automethod:: CommentLookupSession.get_comments_by_genus_type

   .. automethod:: CommentLookupSession.get_comments_by_parent_genus_type

   .. automethod:: CommentLookupSession.get_comments_by_record_type

   .. automethod:: CommentLookupSession.get_comments_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_on_date

   .. automethod:: CommentLookupSession.get_comments_for_commentor

   .. automethod:: CommentLookupSession.get_comments_for_commentor_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_on_date

   .. automethod:: CommentLookupSession.get_comments_for_reference

   .. automethod:: CommentLookupSession.get_comments_for_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_reference

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_for_commentor_and_reference

   .. automethod:: CommentLookupSession.get_comments_for_commentor_and_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_and_reference

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_and_reference_on_date

   .. autoattribute:: CommentLookupSession.comments



Comment Query Methods
---------------------

   .. autoattribute:: CommentQuerySession.book_id

   .. autoattribute:: CommentQuerySession.book

   .. automethod:: CommentQuerySession.can_search_comments

   .. automethod:: CommentQuerySession.use_federated_book_view

   .. automethod:: CommentQuerySession.use_isolated_book_view

   .. autoattribute:: CommentQuerySession.comment_query

   .. automethod:: CommentQuerySession.get_comments_by_query



Comment Admin Methods
---------------------

   .. autoattribute:: CommentAdminSession.book_id

   .. autoattribute:: CommentAdminSession.book

   .. automethod:: CommentAdminSession.can_create_comments

   .. automethod:: CommentAdminSession.can_create_comment_with_record_types

   .. automethod:: CommentAdminSession.get_comment_form_for_create

   .. automethod:: CommentAdminSession.create_comment

   .. automethod:: CommentAdminSession.can_update_comments

   .. automethod:: CommentAdminSession.get_comment_form_for_update

   .. automethod:: CommentAdminSession.update_comment

   .. automethod:: CommentAdminSession.can_delete_comments

   .. automethod:: CommentAdminSession.delete_comment

   .. automethod:: CommentAdminSession.can_manage_comment_aliases

   .. automethod:: CommentAdminSession.alias_comment



Book Node
---------

.. autoclass:: BookNode
   :show-inheritance:

   .. autoattribute:: BookNode.book

   .. autoattribute:: BookNode.parent_book_nodes

   .. autoattribute:: BookNode.child_book_nodes



Book Lookup Methods
-------------------

   .. automethod:: BookLookupSession.can_lookup_books

   .. automethod:: BookLookupSession.use_comparative_book_view

   .. automethod:: BookLookupSession.use_plenary_book_view

   .. automethod:: BookLookupSession.get_book

   .. automethod:: BookLookupSession.get_books_by_ids

   .. automethod:: BookLookupSession.get_books_by_genus_type

   .. automethod:: BookLookupSession.get_books_by_parent_genus_type

   .. automethod:: BookLookupSession.get_books_by_record_type

   .. automethod:: BookLookupSession.get_books_by_provider

   .. autoattribute:: BookLookupSession.books



Book Admin Methods
------------------

   .. automethod:: BookAdminSession.can_create_books

   .. automethod:: BookAdminSession.can_create_book_with_record_types

   .. automethod:: BookAdminSession.get_book_form_for_create

   .. automethod:: BookAdminSession.create_book

   .. automethod:: BookAdminSession.can_update_books

   .. automethod:: BookAdminSession.get_book_form_for_update

   .. automethod:: BookAdminSession.update_book

   .. automethod:: BookAdminSession.can_delete_books

   .. automethod:: BookAdminSession.delete_book

   .. automethod:: BookAdminSession.can_manage_book_aliases

   .. automethod:: BookAdminSession.alias_book



Book Hierarchy Methods
----------------------

   .. autoattribute:: BookHierarchySession.book_hierarchy_id

   .. autoattribute:: BookHierarchySession.book_hierarchy

   .. automethod:: BookHierarchySession.can_access_book_hierarchy

   .. automethod:: BookHierarchySession.use_comparative_book_view

   .. automethod:: BookHierarchySession.use_plenary_book_view

   .. autoattribute:: BookHierarchySession.root_book_ids

   .. autoattribute:: BookHierarchySession.root_books

   .. automethod:: BookHierarchySession.has_parent_books

   .. automethod:: BookHierarchySession.is_parent_of_book

   .. automethod:: BookHierarchySession.get_parent_book_ids

   .. automethod:: BookHierarchySession.get_parent_books

   .. automethod:: BookHierarchySession.is_ancestor_of_book

   .. automethod:: BookHierarchySession.has_child_books

   .. automethod:: BookHierarchySession.is_child_of_book

   .. automethod:: BookHierarchySession.get_child_book_ids

   .. automethod:: BookHierarchySession.get_child_books

   .. automethod:: BookHierarchySession.is_descendant_of_book

   .. automethod:: BookHierarchySession.get_book_node_ids

   .. automethod:: BookHierarchySession.get_book_nodes



Book Hierarchy Design Methods
-----------------------------

   .. autoattribute:: BookHierarchyDesignSession.book_hierarchy_id

   .. autoattribute:: BookHierarchyDesignSession.book_hierarchy

   .. automethod:: BookHierarchyDesignSession.can_modify_book_hierarchy

   .. automethod:: BookHierarchyDesignSession.add_root_book

   .. automethod:: BookHierarchyDesignSession.remove_root_book

   .. automethod:: BookHierarchyDesignSession.add_child_book

   .. automethod:: BookHierarchyDesignSession.remove_child_book

   .. automethod:: BookHierarchyDesignSession.remove_child_books



Comment Lookup Methods
----------------------

   .. autoattribute:: CommentLookupSession.book_id

   .. autoattribute:: CommentLookupSession.book

   .. automethod:: CommentLookupSession.can_lookup_comments

   .. automethod:: CommentLookupSession.use_comparative_comment_view

   .. automethod:: CommentLookupSession.use_plenary_comment_view

   .. automethod:: CommentLookupSession.use_federated_book_view

   .. automethod:: CommentLookupSession.use_isolated_book_view

   .. automethod:: CommentLookupSession.use_effective_comment_view

   .. automethod:: CommentLookupSession.use_any_effective_comment_view

   .. automethod:: CommentLookupSession.get_comment

   .. automethod:: CommentLookupSession.get_comments_by_ids

   .. automethod:: CommentLookupSession.get_comments_by_genus_type

   .. automethod:: CommentLookupSession.get_comments_by_parent_genus_type

   .. automethod:: CommentLookupSession.get_comments_by_record_type

   .. automethod:: CommentLookupSession.get_comments_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_on_date

   .. automethod:: CommentLookupSession.get_comments_for_commentor

   .. automethod:: CommentLookupSession.get_comments_for_commentor_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_on_date

   .. automethod:: CommentLookupSession.get_comments_for_reference

   .. automethod:: CommentLookupSession.get_comments_for_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_reference

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_for_commentor_and_reference

   .. automethod:: CommentLookupSession.get_comments_for_commentor_and_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_and_reference

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_and_reference_on_date

   .. autoattribute:: CommentLookupSession.comments



Comment Query Methods
---------------------

   .. autoattribute:: CommentQuerySession.book_id

   .. autoattribute:: CommentQuerySession.book

   .. automethod:: CommentQuerySession.can_search_comments

   .. automethod:: CommentQuerySession.use_federated_book_view

   .. automethod:: CommentQuerySession.use_isolated_book_view

   .. autoattribute:: CommentQuerySession.comment_query

   .. automethod:: CommentQuerySession.get_comments_by_query



Comment Admin Methods
---------------------

   .. autoattribute:: CommentAdminSession.book_id

   .. autoattribute:: CommentAdminSession.book

   .. automethod:: CommentAdminSession.can_create_comments

   .. automethod:: CommentAdminSession.can_create_comment_with_record_types

   .. automethod:: CommentAdminSession.get_comment_form_for_create

   .. automethod:: CommentAdminSession.create_comment

   .. automethod:: CommentAdminSession.can_update_comments

   .. automethod:: CommentAdminSession.get_comment_form_for_update

   .. automethod:: CommentAdminSession.update_comment

   .. automethod:: CommentAdminSession.can_delete_comments

   .. automethod:: CommentAdminSession.delete_comment

   .. automethod:: CommentAdminSession.can_manage_comment_aliases

   .. automethod:: CommentAdminSession.alias_comment



Book Node List
--------------

.. autoclass:: BookNodeList
   :show-inheritance:

   .. autoattribute:: BookNodeList.next_book_node

   .. automethod:: BookNodeList.get_next_book_nodes



Book Lookup Methods
-------------------

   .. automethod:: BookLookupSession.can_lookup_books

   .. automethod:: BookLookupSession.use_comparative_book_view

   .. automethod:: BookLookupSession.use_plenary_book_view

   .. automethod:: BookLookupSession.get_book

   .. automethod:: BookLookupSession.get_books_by_ids

   .. automethod:: BookLookupSession.get_books_by_genus_type

   .. automethod:: BookLookupSession.get_books_by_parent_genus_type

   .. automethod:: BookLookupSession.get_books_by_record_type

   .. automethod:: BookLookupSession.get_books_by_provider

   .. autoattribute:: BookLookupSession.books



Book Admin Methods
------------------

   .. automethod:: BookAdminSession.can_create_books

   .. automethod:: BookAdminSession.can_create_book_with_record_types

   .. automethod:: BookAdminSession.get_book_form_for_create

   .. automethod:: BookAdminSession.create_book

   .. automethod:: BookAdminSession.can_update_books

   .. automethod:: BookAdminSession.get_book_form_for_update

   .. automethod:: BookAdminSession.update_book

   .. automethod:: BookAdminSession.can_delete_books

   .. automethod:: BookAdminSession.delete_book

   .. automethod:: BookAdminSession.can_manage_book_aliases

   .. automethod:: BookAdminSession.alias_book



Book Hierarchy Methods
----------------------

   .. autoattribute:: BookHierarchySession.book_hierarchy_id

   .. autoattribute:: BookHierarchySession.book_hierarchy

   .. automethod:: BookHierarchySession.can_access_book_hierarchy

   .. automethod:: BookHierarchySession.use_comparative_book_view

   .. automethod:: BookHierarchySession.use_plenary_book_view

   .. autoattribute:: BookHierarchySession.root_book_ids

   .. autoattribute:: BookHierarchySession.root_books

   .. automethod:: BookHierarchySession.has_parent_books

   .. automethod:: BookHierarchySession.is_parent_of_book

   .. automethod:: BookHierarchySession.get_parent_book_ids

   .. automethod:: BookHierarchySession.get_parent_books

   .. automethod:: BookHierarchySession.is_ancestor_of_book

   .. automethod:: BookHierarchySession.has_child_books

   .. automethod:: BookHierarchySession.is_child_of_book

   .. automethod:: BookHierarchySession.get_child_book_ids

   .. automethod:: BookHierarchySession.get_child_books

   .. automethod:: BookHierarchySession.is_descendant_of_book

   .. automethod:: BookHierarchySession.get_book_node_ids

   .. automethod:: BookHierarchySession.get_book_nodes



Book Hierarchy Design Methods
-----------------------------

   .. autoattribute:: BookHierarchyDesignSession.book_hierarchy_id

   .. autoattribute:: BookHierarchyDesignSession.book_hierarchy

   .. automethod:: BookHierarchyDesignSession.can_modify_book_hierarchy

   .. automethod:: BookHierarchyDesignSession.add_root_book

   .. automethod:: BookHierarchyDesignSession.remove_root_book

   .. automethod:: BookHierarchyDesignSession.add_child_book

   .. automethod:: BookHierarchyDesignSession.remove_child_book

   .. automethod:: BookHierarchyDesignSession.remove_child_books



Comment Lookup Methods
----------------------

   .. autoattribute:: CommentLookupSession.book_id

   .. autoattribute:: CommentLookupSession.book

   .. automethod:: CommentLookupSession.can_lookup_comments

   .. automethod:: CommentLookupSession.use_comparative_comment_view

   .. automethod:: CommentLookupSession.use_plenary_comment_view

   .. automethod:: CommentLookupSession.use_federated_book_view

   .. automethod:: CommentLookupSession.use_isolated_book_view

   .. automethod:: CommentLookupSession.use_effective_comment_view

   .. automethod:: CommentLookupSession.use_any_effective_comment_view

   .. automethod:: CommentLookupSession.get_comment

   .. automethod:: CommentLookupSession.get_comments_by_ids

   .. automethod:: CommentLookupSession.get_comments_by_genus_type

   .. automethod:: CommentLookupSession.get_comments_by_parent_genus_type

   .. automethod:: CommentLookupSession.get_comments_by_record_type

   .. automethod:: CommentLookupSession.get_comments_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_on_date

   .. automethod:: CommentLookupSession.get_comments_for_commentor

   .. automethod:: CommentLookupSession.get_comments_for_commentor_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_on_date

   .. automethod:: CommentLookupSession.get_comments_for_reference

   .. automethod:: CommentLookupSession.get_comments_for_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_reference

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_for_commentor_and_reference

   .. automethod:: CommentLookupSession.get_comments_for_commentor_and_reference_on_date

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_and_reference

   .. automethod:: CommentLookupSession.get_comments_by_genus_type_for_commentor_and_reference_on_date

   .. autoattribute:: CommentLookupSession.comments



Comment Query Methods
---------------------

   .. autoattribute:: CommentQuerySession.book_id

   .. autoattribute:: CommentQuerySession.book

   .. automethod:: CommentQuerySession.can_search_comments

   .. automethod:: CommentQuerySession.use_federated_book_view

   .. automethod:: CommentQuerySession.use_isolated_book_view

   .. autoattribute:: CommentQuerySession.comment_query

   .. automethod:: CommentQuerySession.get_comments_by_query



Comment Admin Methods
---------------------

   .. autoattribute:: CommentAdminSession.book_id

   .. autoattribute:: CommentAdminSession.book

   .. automethod:: CommentAdminSession.can_create_comments

   .. automethod:: CommentAdminSession.can_create_comment_with_record_types

   .. automethod:: CommentAdminSession.get_comment_form_for_create

   .. automethod:: CommentAdminSession.create_comment

   .. automethod:: CommentAdminSession.can_update_comments

   .. automethod:: CommentAdminSession.get_comment_form_for_update

   .. automethod:: CommentAdminSession.update_comment

   .. automethod:: CommentAdminSession.can_delete_comments

   .. automethod:: CommentAdminSession.delete_comment

   .. automethod:: CommentAdminSession.can_manage_comment_aliases

   .. automethod:: CommentAdminSession.alias_comment



