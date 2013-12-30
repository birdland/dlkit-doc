.. currentmodule:: dlkit.services.forum
.. automodule:: dlkit.services.forum

Services
========


Forum Manager
-------------

.. autoclass:: ForumManager
   :show-inheritance:

.. autoattribute:: ForumManager.forum_batch_manager



Forum Profile Methods
_____________

.. automethod:: ForumManager.supports_visible_federation

.. automethod:: ForumManager.supports_post_lookup

.. automethod:: ForumManager.supports_post_query

.. automethod:: ForumManager.supports_post_search

.. automethod:: ForumManager.supports_post_admin

.. automethod:: ForumManager.supports_post_notification

.. automethod:: ForumManager.supports_post_forum

.. automethod:: ForumManager.supports_post_forum_assignment

.. automethod:: ForumManager.supports_post_smart_forum

.. automethod:: ForumManager.supports_reply_lookup

.. automethod:: ForumManager.supports_reply_admin

.. automethod:: ForumManager.supports_reply_notification

.. automethod:: ForumManager.supports_forum_lookup

.. automethod:: ForumManager.supports_forum_query

.. automethod:: ForumManager.supports_forum_search

.. automethod:: ForumManager.supports_forum_admin

.. automethod:: ForumManager.supports_forum_notification

.. automethod:: ForumManager.supports_forum_hierarchy

.. automethod:: ForumManager.supports_forum_hierarchy_design

.. automethod:: ForumManager.supports_forum_batch

.. autoattribute:: ForumManager.post_record_types

.. automethod:: ForumManager.supports_post_record_type

.. autoattribute:: ForumManager.post_search_record_types

.. automethod:: ForumManager.supports_post_search_record_type

.. autoattribute:: ForumManager.reply_record_types

.. automethod:: ForumManager.supports_reply_record_type

.. autoattribute:: ForumManager.reply_search_record_types

.. automethod:: ForumManager.supports_reply_search_record_type

.. autoattribute:: ForumManager.forum_record_types

.. automethod:: ForumManager.supports_forum_record_type

.. autoattribute:: ForumManager.forum_search_record_types

.. automethod:: ForumManager.supports_forum_search_record_type



Forum Lookup
____________

.. automethod:: ForumManager.can_lookup_forums

.. automethod:: ForumManager.use_comparative_forum_view

.. automethod:: ForumManager.use_plenary_forum_view

.. automethod:: ForumManager.get_forum

.. automethod:: ForumManager.get_forums_by_ids

.. automethod:: ForumManager.get_forums_by_genus_type

.. automethod:: ForumManager.get_forums_by_parent_genus_type

.. automethod:: ForumManager.get_forums_by_record_type

.. automethod:: ForumManager.get_forums_by_provider

.. autoattribute:: ForumManager.forums



Forum Query
___________

.. automethod:: ForumManager.can_search_forums

.. autoattribute:: ForumManager.forum_query

.. automethod:: ForumManager.get_forums_by_query



Forum Search
____________

.. autoattribute:: ForumManager.forum_search

.. autoattribute:: ForumManager.forum_search_order

.. automethod:: ForumManager.get_forums_by_search

.. automethod:: ForumManager.get_forum_query_from_inspector



Forum Admin
___________

.. automethod:: ForumManager.can_create_forums

.. automethod:: ForumManager.can_create_forum_with_record_types

.. automethod:: ForumManager.get_forum_form_for_create

.. automethod:: ForumManager.create_forum

.. automethod:: ForumManager.can_update_forums

.. automethod:: ForumManager.get_forum_form_for_update

.. automethod:: ForumManager.update_forum

.. automethod:: ForumManager.can_delete_forums

.. automethod:: ForumManager.delete_forum

.. automethod:: ForumManager.can_manage_forum_aliases

.. automethod:: ForumManager.alias_forum



Forum Notification
__________________

.. automethod:: ForumManager.can_register_for_forum_notifications

.. automethod:: ForumManager.register_for_new_forums

.. automethod:: ForumManager.register_for_new_forum_ancestors

.. automethod:: ForumManager.register_for_new_forum_descendants

.. automethod:: ForumManager.register_for_changed_forums

.. automethod:: ForumManager.register_for_changed_forum

.. automethod:: ForumManager.register_for_deleted_forums

.. automethod:: ForumManager.register_for_deleted_forum

.. automethod:: ForumManager.register_for_deleted_forum_ancestors

.. automethod:: ForumManager.register_for_deleted_forum_descendants



Forum Hierarchy
_______________

.. autoattribute:: ForumManager.forum_hierarchy_id

.. autoattribute:: ForumManager.forum_hierarchy

.. automethod:: ForumManager.can_access_forum_hierarchy

.. automethod:: ForumManager.use_comparative_forum_view

.. automethod:: ForumManager.use_plenary_forum_view

.. autoattribute:: ForumManager.root_forum_ids

.. autoattribute:: ForumManager.root_forums

.. automethod:: ForumManager.has_parent_forums

.. automethod:: ForumManager.is_parent_of_forum

.. automethod:: ForumManager.get_parent_forum_ids

.. automethod:: ForumManager.get_parent_forums

.. automethod:: ForumManager.is_ancestor_of_forum

.. automethod:: ForumManager.has_child_forums

.. automethod:: ForumManager.is_child_of_forum

.. automethod:: ForumManager.get_child_forum_ids

.. automethod:: ForumManager.get_child_forums

.. automethod:: ForumManager.is_descendant_of_forum

.. automethod:: ForumManager.get_forum_node_ids

.. automethod:: ForumManager.get_forum_nodes



Forum Hierarchy Design
______________________

.. autoattribute:: ForumManager.forum_hierarchy_id

.. autoattribute:: ForumManager.forum_hierarchy

.. automethod:: ForumManager.can_modify_forum_hierarchy

.. automethod:: ForumManager.add_root_forum

.. automethod:: ForumManager.remove_root_forum

.. automethod:: ForumManager.add_child_forum

.. automethod:: ForumManager.remove_child_forum

.. automethod:: ForumManager.remove_child_forums



Forum Proxy Manager
-------------------

.. autoclass:: ForumProxyManager
   :show-inheritance:

.. automethod:: ForumProxyManager.get_post_lookup_session

.. automethod:: ForumProxyManager.get_post_lookup_session_for_forum

.. automethod:: ForumProxyManager.get_post_query_session

.. automethod:: ForumProxyManager.get_post_query_session_for_forum

.. automethod:: ForumProxyManager.get_post_search_session

.. automethod:: ForumProxyManager.get_post_search_session_for_forum

.. automethod:: ForumProxyManager.get_post_admin_session

.. automethod:: ForumProxyManager.get_post_admin_session_for_forum

.. automethod:: ForumProxyManager.get_post_notification_session

.. automethod:: ForumProxyManager.get_post_notification_session_for_forum

.. automethod:: ForumProxyManager.get_post_forum_session

.. automethod:: ForumProxyManager.get_post_forum_assignment_session

.. automethod:: ForumProxyManager.get_post_smart_forum_session

.. automethod:: ForumProxyManager.get_reply_lookup_session

.. automethod:: ForumProxyManager.get_reply_lookup_session_for_forum

.. automethod:: ForumProxyManager.get_reply_admin_session

.. automethod:: ForumProxyManager.get_reply_admin_session_for_forum

.. automethod:: ForumProxyManager.get_reply_notification_session

.. automethod:: ForumProxyManager.get_reply_notification_session_for_forum

.. automethod:: ForumProxyManager.get_forum_lookup_session

.. automethod:: ForumProxyManager.get_forum_query_session

.. automethod:: ForumProxyManager.get_forum_search_session

.. automethod:: ForumProxyManager.get_forum_admin_session

.. automethod:: ForumProxyManager.get_forum_notification_session

.. automethod:: ForumProxyManager.get_forum_hierarchy_session

.. automethod:: ForumProxyManager.get_forum_hierarchy_design_session

.. autoattribute:: ForumProxyManager.forum_batch_proxy_manager



