
.. currentmodule:: dlkit.commenting.queries
.. automodule:: dlkit.commenting.queries

Queries
=======


Comment Query
-------------

.. autoclass:: CommentQuery
   :show-inheritance:

   .. automethod:: CommentQuery.match_reference_id

   .. autoattribute:: CommentQuery.reference_id_terms

   .. automethod:: CommentQuery.match_commentor_id

   .. autoattribute:: CommentQuery.commentor_id_terms

   .. automethod:: CommentQuery.supports_commentor_query

   .. autoattribute:: CommentQuery.commentor_query

   .. autoattribute:: CommentQuery.commentor_terms

   .. automethod:: CommentQuery.match_commenting_agent_id

   .. autoattribute:: CommentQuery.commenting_agent_id_terms

   .. automethod:: CommentQuery.supports_commenting_agent_query

   .. autoattribute:: CommentQuery.commenting_agent_query

   .. autoattribute:: CommentQuery.commenting_agent_terms

   .. automethod:: CommentQuery.match_text

   .. automethod:: CommentQuery.match_any_text

   .. autoattribute:: CommentQuery.text_terms

   .. automethod:: CommentQuery.match_rating_id

   .. autoattribute:: CommentQuery.rating_id_terms

   .. automethod:: CommentQuery.supports_rating_query

   .. autoattribute:: CommentQuery.rating_query

   .. automethod:: CommentQuery.match_any_rating

   .. autoattribute:: CommentQuery.rating_terms

   .. automethod:: CommentQuery.match_book_id

   .. autoattribute:: CommentQuery.book_id_terms

   .. automethod:: CommentQuery.supports_book_query

   .. autoattribute:: CommentQuery.book_query

   .. autoattribute:: CommentQuery.book_terms

   .. automethod:: CommentQuery.get_comment_query_record



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



Book Query
----------

.. autoclass:: BookQuery
   :show-inheritance:

   .. automethod:: BookQuery.match_comment_id

   .. autoattribute:: BookQuery.comment_id_terms

   .. automethod:: BookQuery.supports_comment_query

   .. autoattribute:: BookQuery.comment_query

   .. automethod:: BookQuery.match_any_comment

   .. autoattribute:: BookQuery.comment_terms

   .. automethod:: BookQuery.match_ancestor_book_id

   .. autoattribute:: BookQuery.ancestor_book_id_terms

   .. automethod:: BookQuery.supports_ancestor_book_query

   .. autoattribute:: BookQuery.ancestor_book_query

   .. automethod:: BookQuery.match_any_ancestor_book

   .. autoattribute:: BookQuery.ancestor_book_terms

   .. automethod:: BookQuery.match_descendant_book_id

   .. autoattribute:: BookQuery.descendant_book_id_terms

   .. automethod:: BookQuery.supports_descendant_book_query

   .. autoattribute:: BookQuery.descendant_book_query

   .. automethod:: BookQuery.match_any_descendant_book

   .. autoattribute:: BookQuery.descendant_book_terms

   .. automethod:: BookQuery.get_book_query_record



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



