
.. currentmodule:: dlkit.services.commenting

Service Catalog
===============


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



Comment Query Methods
---------------------

   .. autoattribute:: Book.book_id

   .. autoattribute:: Book.book

   .. automethod:: Book.can_search_comments

   .. automethod:: Book.use_federated_book_view

   .. automethod:: Book.use_isolated_book_view

   .. autoattribute:: Book.comment_query

   .. automethod:: Book.get_comments_by_query



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



