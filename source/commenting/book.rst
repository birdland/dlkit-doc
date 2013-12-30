.. currentmodule:: dlkit.services.commenting
.. automodule:: dlkit.services.commenting

Book
====


Book
----

.. autoclass:: Book
   :show-inheritance:

.. automethod:: Book.get_book_record



Comment Lookup Methods
----------------------

.. autoattribute:: Book.book_id

.. autoattribute:: Book.book

.. automethod:: Book.can_lookup_comments

.. automethod:: Book.use_comparative_comment_view

.. automethod:: Book.use_plenary_comment_view

.. automethod:: Book.use_federated_book_view

.. automethod:: Book.use_isolated_book_view

.. automethod:: Book.use_effective_comment_view

.. automethod:: Book.use_any_effective_comment_view

.. automethod:: Book.get_comment

.. automethod:: Book.get_comments_by_ids

.. automethod:: Book.get_comments_by_genus_type

.. automethod:: Book.get_comments_by_parent_genus_type

.. automethod:: Book.get_comments_by_record_type

.. automethod:: Book.get_comments_on_date

.. automethod:: Book.get_comments_by_genus_type_on_date

.. automethod:: Book.get_comments_for_commentor

.. automethod:: Book.get_comments_for_commentor_on_date

.. automethod:: Book.get_comments_by_genus_type_for_commentor

.. automethod:: Book.get_comments_by_genus_type_for_commentor_on_date

.. automethod:: Book.get_comments_for_reference

.. automethod:: Book.get_comments_for_reference_on_date

.. automethod:: Book.get_comments_by_genus_type_for_reference

.. automethod:: Book.get_comments_by_genus_type_for_reference_on_date

.. automethod:: Book.get_comments_for_commentor_and_reference

.. automethod:: Book.get_comments_for_commentor_and_reference_on_date

.. automethod:: Book.get_comments_by_genus_type_for_commentor_and_reference

.. automethod:: Book.get_comments_by_genus_type_for_commentor_and_reference_on_date

.. autoattribute:: Book.comments



Rating Lookup Methods
---------------------

.. autoattribute:: Book.book_id

.. autoattribute:: Book.book

.. automethod:: Book.can_lookup_ratings

.. automethod:: Book.use_comparative_comment_view

.. automethod:: Book.use_plenary_comment_view

.. automethod:: Book.use_federated_book_view

.. automethod:: Book.use_isolated_book_view

.. autoattribute:: Book.cumulative_rating

.. automethod:: Book.get_cumulative_rating_for_reference

.. automethod:: Book.get_cumulative_rating_for_commentor

.. automethod:: Book.get_top_references

.. automethod:: Book.get_references



Comment Query Methods
---------------------

.. autoattribute:: Book.book_id

.. autoattribute:: Book.book

.. automethod:: Book.can_search_comments

.. automethod:: Book.use_federated_book_view

.. automethod:: Book.use_isolated_book_view

.. autoattribute:: Book.comment_query

.. automethod:: Book.get_comments_by_query



Comment Search Methods
----------------------

.. autoattribute:: Book.comment_search

.. autoattribute:: Book.comment_search_order

.. automethod:: Book.get_comments_by_search

.. automethod:: Book.get_comment_query_from_inspector



Comment Admin Methods
---------------------

.. autoattribute:: Book.book_id

.. autoattribute:: Book.book

.. automethod:: Book.can_create_comments

.. automethod:: Book.can_create_comment_with_record_types

.. automethod:: Book.get_comment_form_for_create

.. automethod:: Book.create_comment

.. automethod:: Book.can_update_comments

.. automethod:: Book.get_comment_form_for_update

.. automethod:: Book.update_comment

.. automethod:: Book.can_delete_comments

.. automethod:: Book.delete_comment

.. automethod:: Book.can_manage_comment_aliases

.. automethod:: Book.alias_comment



Comment Notification Methods
----------------------------

.. autoattribute:: Book.book_id

.. autoattribute:: Book.book

.. automethod:: Book.can_register_for_comment_notifications

.. automethod:: Book.use_federated_book_view

.. automethod:: Book.use_isolated_book_view

.. automethod:: Book.register_for_new_comments

.. automethod:: Book.register_for_new_comments_for_commentor

.. automethod:: Book.register_for_new_comments_for_reference

.. automethod:: Book.register_for_changed_comments

.. automethod:: Book.register_for_changed_comments_for_commentor

.. automethod:: Book.register_for_changed_comments_for_reference

.. automethod:: Book.register_for_changed_comment

.. automethod:: Book.register_for_deleted_comments

.. automethod:: Book.register_for_deleted_comments_for_commentor

.. automethod:: Book.register_for_deleted_comments_for_reference

.. automethod:: Book.register_for_deleted_comment



Comment Book Methods
--------------------

.. automethod:: Book.can_lookup_comment_book_mappings

.. automethod:: Book.use_comparative_book_view

.. automethod:: Book.use_plenary_book_view

.. automethod:: Book.get_comment_ids_by_book

.. automethod:: Book.get_comments_by_book

.. automethod:: Book.get_comment_ids_by_books

.. automethod:: Book.get_comments_by_books

.. automethod:: Book.get_book_ids_by_comment

.. automethod:: Book.get_books_by_comment



Comment Book Assignment Methods
-------------------------------

.. automethod:: Book.can_assign_comments

.. automethod:: Book.can_assign_comments_to_book

.. automethod:: Book.get_assignable_book_ids

.. automethod:: Book.get_assignable_book_ids_for_comment

.. automethod:: Book.assign_comment_to_book

.. automethod:: Book.unassign_comment_from_book



Comment Smart Book Methods
--------------------------

.. autoattribute:: Book.book_id

.. autoattribute:: Book.book

.. automethod:: Book.can_manage_smart_books

.. autoattribute:: Book.comment_query

.. autoattribute:: Book.comment_search_order

.. automethod:: Book.apply_comment_query

.. automethod:: Book.inspect_comment_query

.. automethod:: Book.apply_comment_sequencing

.. automethod:: Book.get_comment_query_from_inspector



