.. currentmodule:: dlkit.services.forum
.. automodule:: dlkit.services.forum

Forum
=====


Forum
-----

.. autoclass:: Forum
   :show-inheritance:

.. automethod:: Forum.get_forum_record



Post Lookup Methods
-------------------

.. autoattribute:: Forum.forum_id

.. autoattribute:: Forum.forum

.. automethod:: Forum.can_lookup_posts

.. automethod:: Forum.use_comparative_post_view

.. automethod:: Forum.use_plenary_post_view

.. automethod:: Forum.use_federated_forum_view

.. automethod:: Forum.use_isolated_forum_view

.. automethod:: Forum.get_post

.. automethod:: Forum.get_posts_by_ids

.. automethod:: Forum.get_posts_by_genus_type

.. automethod:: Forum.get_posts_by_parent_genus_type

.. automethod:: Forum.get_posts_by_record_type

.. automethod:: Forum.get_posts_by_date

.. automethod:: Forum.get_posts_for_poster

.. automethod:: Forum.get_posts_by_date_for_poster

.. autoattribute:: Forum.posts



Post Query Methods
------------------

.. autoattribute:: Forum.forum_id

.. autoattribute:: Forum.forum

.. automethod:: Forum.use_federated_forum_view

.. automethod:: Forum.use_isolated_forum_view

.. automethod:: Forum.can_search_posts

.. autoattribute:: Forum.post_query

.. automethod:: Forum.get_posts_by_query



Post Search Methods
-------------------

.. autoattribute:: Forum.post_search

.. autoattribute:: Forum.post_search_order

.. automethod:: Forum.get_posts_by_search

.. automethod:: Forum.get_post_query_from_inspector



Post Admin Methods
------------------

.. autoattribute:: Forum.forum_id

.. autoattribute:: Forum.forum

.. automethod:: Forum.can_create_posts

.. automethod:: Forum.can_create_post_with_record_types

.. automethod:: Forum.get_post_form_for_create

.. automethod:: Forum.create_post

.. automethod:: Forum.can_update_posts

.. automethod:: Forum.get_post_form_for_update

.. automethod:: Forum.update_post

.. automethod:: Forum.can_delete_posts

.. automethod:: Forum.delete_post

.. automethod:: Forum.can_manage_post_aliases

.. automethod:: Forum.alias_post



Post Notification Methods
-------------------------

.. autoattribute:: Forum.forum_id

.. autoattribute:: Forum.forum

.. automethod:: Forum.can_register_for_post_notifications

.. automethod:: Forum.use_federated_forum_view

.. automethod:: Forum.use_isolated_forum_view

.. automethod:: Forum.register_for_new_posts

.. automethod:: Forum.register_for_new_posts_for_poster

.. automethod:: Forum.register_for_changed_posts

.. automethod:: Forum.register_for_changed_posts_for_poster

.. automethod:: Forum.register_for_changed_post

.. automethod:: Forum.register_for_deleted_posts

.. automethod:: Forum.register_for_deleted_posts_for_poster

.. automethod:: Forum.register_for_deleted_post



Post Forum Methods
------------------

.. automethod:: Forum.can_lookup_post_forum_mappings

.. automethod:: Forum.use_comparative_forum_view

.. automethod:: Forum.use_plenary_forum_view

.. automethod:: Forum.get_post_ids_by_forum

.. automethod:: Forum.get_posts_by_forum

.. automethod:: Forum.get_post_ids_by_forums

.. automethod:: Forum.get_posts_by_forums

.. automethod:: Forum.get_forum_ids_by_post

.. automethod:: Forum.get_forums_by_post



Post Forum Assignment Methods
-----------------------------

.. automethod:: Forum.can_assign_posts

.. automethod:: Forum.can_assign_posts_to_forum

.. automethod:: Forum.get_assignable_forum_ids

.. automethod:: Forum.get_assignable_forum_ids_for_post

.. automethod:: Forum.assign_post_to_forum

.. automethod:: Forum.unassign_post_from_forum



Post Smart Forum Methods
------------------------

.. autoattribute:: Forum.forum_id

.. autoattribute:: Forum.forum

.. automethod:: Forum.can_manage_smart_forums

.. autoattribute:: Forum.post_query

.. autoattribute:: Forum.post_search_order

.. automethod:: Forum.apply_post_query

.. automethod:: Forum.inspect_post_query

.. automethod:: Forum.apply_post_sequencing

.. automethod:: Forum.get_post_query_from_inspector



Reply Lookup Methods
--------------------

.. autoattribute:: Forum.forum_id

.. autoattribute:: Forum.forum

.. automethod:: Forum.can_lookup_replies

.. automethod:: Forum.use_comparative_reply_view

.. automethod:: Forum.use_plenary_reply_view

.. automethod:: Forum.use_federated_forum_view

.. automethod:: Forum.use_isolated_forum_view

.. automethod:: Forum.use_sequestered_reply_view

.. automethod:: Forum.use_unsequestered_reply_view

.. automethod:: Forum.get_reply

.. automethod:: Forum.get_replies_by_ids

.. automethod:: Forum.get_replies_by_genus_type

.. automethod:: Forum.get_replies_by_parent_genus_type

.. automethod:: Forum.get_replies_by_record_type

.. automethod:: Forum.get_replies_by_date

.. automethod:: Forum.get_replies_for_post

.. automethod:: Forum.get_replies_by_date_for_post

.. automethod:: Forum.get_replies_for_poster

.. automethod:: Forum.get_replies_by_date_for_poster

.. automethod:: Forum.get_replies_for_post_and_poster

.. automethod:: Forum.get_replies_by_date_for_post_and_poster

.. autoattribute:: Forum.replies



Reply Admin Methods
-------------------

.. autoattribute:: Forum.forum_id

.. autoattribute:: Forum.forum

.. automethod:: Forum.can_create_replies

.. automethod:: Forum.can_create_reply_with_record_types

.. automethod:: Forum.get_reply_form_for_create_to_post

.. automethod:: Forum.get_reply_form_for_create_to_reply

.. automethod:: Forum.create_reply

.. automethod:: Forum.can_update_replies

.. automethod:: Forum.get_reply_form_for_update

.. automethod:: Forum.update_reply

.. automethod:: Forum.can_delete_replies

.. automethod:: Forum.delete_reply

.. automethod:: Forum.can_manage_reply_aliases

.. automethod:: Forum.alias_reply



Reply Notification Methods
--------------------------

.. autoattribute:: Forum.forum_id

.. autoattribute:: Forum.forum

.. automethod:: Forum.can_register_for_reply_notifications

.. automethod:: Forum.use_federated_forum_view

.. automethod:: Forum.use_isolated_forum_view

.. automethod:: Forum.register_for_new_replies

.. automethod:: Forum.register_for_new_replies_for_poster

.. automethod:: Forum.register_for_new_replies_for_post

.. automethod:: Forum.register_for_changed_replies

.. automethod:: Forum.register_for_changed_replies_for_poster

.. automethod:: Forum.register_for_changed_replies_for_post

.. automethod:: Forum.register_for_changed_reply

.. automethod:: Forum.register_for_deleted_replies

.. automethod:: Forum.register_for_deleted_replies_for_poster

.. automethod:: Forum.register_for_deleted_replies_for_post

.. automethod:: Forum.register_for_deleted_reply



