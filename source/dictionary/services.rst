.. currentmodule:: dlkit.services.dictionary
.. automodule:: dlkit.services.dictionary

Services
========


Dictionary Manager
------------------

.. autoclass:: DictionaryManager
   :show-inheritance:

   .. autoattribute:: DictionaryManager.dictionary_batch_manager



Dictionary Profile Methods
__________________

   .. automethod:: DictionaryManager.supports_visible_federation

   .. automethod:: DictionaryManager.supports_entry_retrieval

   .. automethod:: DictionaryManager.supports_entry_lookup

   .. automethod:: DictionaryManager.supports_entry_query

   .. automethod:: DictionaryManager.supports_entry_search

   .. automethod:: DictionaryManager.supports_entry_admin

   .. automethod:: DictionaryManager.supports_entry_notification

   .. automethod:: DictionaryManager.supports_entry_dictionary

   .. automethod:: DictionaryManager.supports_entry_dictionary_assignment

   .. automethod:: DictionaryManager.supports_entry_smart_dictionary

   .. automethod:: DictionaryManager.supports_dictionary_lookup

   .. automethod:: DictionaryManager.supports_dictionary_query

   .. automethod:: DictionaryManager.supports_dictionary_search

   .. automethod:: DictionaryManager.supports_dictionary_admin

   .. automethod:: DictionaryManager.supports_dictionary_notification

   .. automethod:: DictionaryManager.supports_dictionary_hierachy_traversal

   .. automethod:: DictionaryManager.supports_dictionary_hierachy_design

   .. automethod:: DictionaryManager.supports_dictionary_batch

   .. autoattribute:: DictionaryManager.entry_key_types

   .. automethod:: DictionaryManager.supports_entry_key_type

   .. autoattribute:: DictionaryManager.entry_value_types

   .. automethod:: DictionaryManager.supports_entry_value_type

   .. automethod:: DictionaryManager.get_entry_value_types_for_key_type

   .. automethod:: DictionaryManager.supports_entry_types

   .. autoattribute:: DictionaryManager.entry_record_types

   .. automethod:: DictionaryManager.supports_entry_record_type

   .. autoattribute:: DictionaryManager.entry_search_record_types

   .. automethod:: DictionaryManager.supports_entry_search_record_type

   .. autoattribute:: DictionaryManager.dictionary_record_types

   .. automethod:: DictionaryManager.supports_dictionary_record_type

   .. autoattribute:: DictionaryManager.dictionary_search_record_types

   .. automethod:: DictionaryManager.supports_dictionary_search_record_type



Dictionary Lookup
_________________

   .. automethod:: DictionaryManager.can_lookup_dictionaries

   .. automethod:: DictionaryManager.use_comparative_dictionary_view

   .. automethod:: DictionaryManager.use_plenary_dictionary_view

   .. automethod:: DictionaryManager.get_dictionary

   .. automethod:: DictionaryManager.get_dictionaries_by_ids

   .. automethod:: DictionaryManager.get_dictionaries_by_genus_type

   .. automethod:: DictionaryManager.get_dictionaries_by_parent_genus_type

   .. automethod:: DictionaryManager.get_dictionaries_by_record_type

   .. automethod:: DictionaryManager.get_dictionaries_by_provider

   .. autoattribute:: DictionaryManager.dictionaries



Dictionary Query
________________

   .. automethod:: DictionaryManager.can_search_dictionaries

   .. autoattribute:: DictionaryManager.dictionary_query

   .. automethod:: DictionaryManager.get_dictionaries_by_query



Dictionary Search
_________________

   .. autoattribute:: DictionaryManager.dictionary_search

   .. autoattribute:: DictionaryManager.dictionary_search_order

   .. automethod:: DictionaryManager.get_dictionaries_by_search

   .. automethod:: DictionaryManager.get_dictionary_query_from_inspector



Dictionary Admin
________________

   .. automethod:: DictionaryManager.can_create_dictionaries

   .. automethod:: DictionaryManager.can_create_dictionary_with_record_types

   .. automethod:: DictionaryManager.get_dictionary_form_for_create

   .. automethod:: DictionaryManager.create_dictionary

   .. automethod:: DictionaryManager.can_update_dictionaries

   .. automethod:: DictionaryManager.get_dictionary_form_for_update

   .. automethod:: DictionaryManager.update_dictionary

   .. automethod:: DictionaryManager.can_delete_dictionaries

   .. automethod:: DictionaryManager.delete_dictionary

   .. automethod:: DictionaryManager.can_manage_dictionary_aliases

   .. automethod:: DictionaryManager.alias_dictionary



Dictionary Notification
_______________________

   .. automethod:: DictionaryManager.can_register_for_dictionary_notifications

   .. automethod:: DictionaryManager.register_for_new_dictionaries

   .. automethod:: DictionaryManager.register_for_new_dictionary_ancestors

   .. automethod:: DictionaryManager.register_for_new_dictionary_descendants

   .. automethod:: DictionaryManager.register_for_changed_dictionaries

   .. automethod:: DictionaryManager.register_for_changed_dictionary

   .. automethod:: DictionaryManager.register_for_deleted_dictionaries

   .. automethod:: DictionaryManager.register_for_deleted_dictionary

   .. automethod:: DictionaryManager.register_for_deleted_dictionary_ancestors

   .. automethod:: DictionaryManager.register_for_deleted_dictionary_descendants



Dictionary Hierarchy
____________________

   .. autoattribute:: DictionaryManager.dictionary_hierarchy_id

   .. autoattribute:: DictionaryManager.dictionary_hierarchy

   .. automethod:: DictionaryManager.can_access_dictionary_hierarchy

   .. automethod:: DictionaryManager.use_comparative_dictionary_view

   .. automethod:: DictionaryManager.use_plenary_dictionary_view

   .. autoattribute:: DictionaryManager.root_dictionary_ids

   .. autoattribute:: DictionaryManager.root_dictionaries

   .. automethod:: DictionaryManager.has_parent_dictionaries

   .. automethod:: DictionaryManager.is_parent_of_dictionary

   .. automethod:: DictionaryManager.get_parent_dictionary_ids

   .. automethod:: DictionaryManager.get_parent_dictionaries

   .. automethod:: DictionaryManager.is_ancestor_of_dictionary

   .. automethod:: DictionaryManager.has_child_dictionaries

   .. automethod:: DictionaryManager.is_child_of_dictionary

   .. automethod:: DictionaryManager.get_child_dictionary_ids

   .. automethod:: DictionaryManager.get_child_dictionaries

   .. automethod:: DictionaryManager.is_descendant_of_dictionary

   .. automethod:: DictionaryManager.get_dictionary_node_ids

   .. automethod:: DictionaryManager.get_dictionary_nodes



Dictionary Hierarchy Design
___________________________

   .. autoattribute:: DictionaryManager.dictionary_hierarchy_id

   .. autoattribute:: DictionaryManager.dictionary_hierarchy

   .. automethod:: DictionaryManager.can_modify_dictionary_hierarchy

   .. automethod:: DictionaryManager.add_root_dictionary

   .. automethod:: DictionaryManager.remove_root_dictionary

   .. automethod:: DictionaryManager.add_child_dictionary

   .. automethod:: DictionaryManager.remove_child_dictionary

   .. automethod:: DictionaryManager.remove_child_dictionaries



Dictionary Proxy Manager
------------------------

.. autoclass:: DictionaryProxyManager
   :show-inheritance:

   .. autoattribute:: DictionaryProxyManager.dictionary_batch_proxy_manager



Dictionary Profile Methods
__________________

   .. automethod:: DictionaryProxyManager.supports_visible_federation

   .. automethod:: DictionaryProxyManager.supports_entry_retrieval

   .. automethod:: DictionaryProxyManager.supports_entry_lookup

   .. automethod:: DictionaryProxyManager.supports_entry_query

   .. automethod:: DictionaryProxyManager.supports_entry_search

   .. automethod:: DictionaryProxyManager.supports_entry_admin

   .. automethod:: DictionaryProxyManager.supports_entry_notification

   .. automethod:: DictionaryProxyManager.supports_entry_dictionary

   .. automethod:: DictionaryProxyManager.supports_entry_dictionary_assignment

   .. automethod:: DictionaryProxyManager.supports_entry_smart_dictionary

   .. automethod:: DictionaryProxyManager.supports_dictionary_lookup

   .. automethod:: DictionaryProxyManager.supports_dictionary_query

   .. automethod:: DictionaryProxyManager.supports_dictionary_search

   .. automethod:: DictionaryProxyManager.supports_dictionary_admin

   .. automethod:: DictionaryProxyManager.supports_dictionary_notification

   .. automethod:: DictionaryProxyManager.supports_dictionary_hierachy_traversal

   .. automethod:: DictionaryProxyManager.supports_dictionary_hierachy_design

   .. automethod:: DictionaryProxyManager.supports_dictionary_batch

   .. autoattribute:: DictionaryProxyManager.entry_key_types

   .. automethod:: DictionaryProxyManager.supports_entry_key_type

   .. autoattribute:: DictionaryProxyManager.entry_value_types

   .. automethod:: DictionaryProxyManager.supports_entry_value_type

   .. automethod:: DictionaryProxyManager.get_entry_value_types_for_key_type

   .. automethod:: DictionaryProxyManager.supports_entry_types

   .. autoattribute:: DictionaryProxyManager.entry_record_types

   .. automethod:: DictionaryProxyManager.supports_entry_record_type

   .. autoattribute:: DictionaryProxyManager.entry_search_record_types

   .. automethod:: DictionaryProxyManager.supports_entry_search_record_type

   .. autoattribute:: DictionaryProxyManager.dictionary_record_types

   .. automethod:: DictionaryProxyManager.supports_dictionary_record_type

   .. autoattribute:: DictionaryProxyManager.dictionary_search_record_types

   .. automethod:: DictionaryProxyManager.supports_dictionary_search_record_type



Dictionary Lookup
_________________

   .. automethod:: DictionaryProxyManager.can_lookup_dictionaries

   .. automethod:: DictionaryProxyManager.use_comparative_dictionary_view

   .. automethod:: DictionaryProxyManager.use_plenary_dictionary_view

   .. automethod:: DictionaryProxyManager.get_dictionary

   .. automethod:: DictionaryProxyManager.get_dictionaries_by_ids

   .. automethod:: DictionaryProxyManager.get_dictionaries_by_genus_type

   .. automethod:: DictionaryProxyManager.get_dictionaries_by_parent_genus_type

   .. automethod:: DictionaryProxyManager.get_dictionaries_by_record_type

   .. automethod:: DictionaryProxyManager.get_dictionaries_by_provider

   .. autoattribute:: DictionaryProxyManager.dictionaries



Dictionary Query
________________

   .. automethod:: DictionaryProxyManager.can_search_dictionaries

   .. autoattribute:: DictionaryProxyManager.dictionary_query

   .. automethod:: DictionaryProxyManager.get_dictionaries_by_query



Dictionary Search
_________________

   .. autoattribute:: DictionaryProxyManager.dictionary_search

   .. autoattribute:: DictionaryProxyManager.dictionary_search_order

   .. automethod:: DictionaryProxyManager.get_dictionaries_by_search

   .. automethod:: DictionaryProxyManager.get_dictionary_query_from_inspector



Dictionary Admin
________________

   .. automethod:: DictionaryProxyManager.can_create_dictionaries

   .. automethod:: DictionaryProxyManager.can_create_dictionary_with_record_types

   .. automethod:: DictionaryProxyManager.get_dictionary_form_for_create

   .. automethod:: DictionaryProxyManager.create_dictionary

   .. automethod:: DictionaryProxyManager.can_update_dictionaries

   .. automethod:: DictionaryProxyManager.get_dictionary_form_for_update

   .. automethod:: DictionaryProxyManager.update_dictionary

   .. automethod:: DictionaryProxyManager.can_delete_dictionaries

   .. automethod:: DictionaryProxyManager.delete_dictionary

   .. automethod:: DictionaryProxyManager.can_manage_dictionary_aliases

   .. automethod:: DictionaryProxyManager.alias_dictionary



Dictionary Notification
_______________________

   .. automethod:: DictionaryProxyManager.can_register_for_dictionary_notifications

   .. automethod:: DictionaryProxyManager.register_for_new_dictionaries

   .. automethod:: DictionaryProxyManager.register_for_new_dictionary_ancestors

   .. automethod:: DictionaryProxyManager.register_for_new_dictionary_descendants

   .. automethod:: DictionaryProxyManager.register_for_changed_dictionaries

   .. automethod:: DictionaryProxyManager.register_for_changed_dictionary

   .. automethod:: DictionaryProxyManager.register_for_deleted_dictionaries

   .. automethod:: DictionaryProxyManager.register_for_deleted_dictionary

   .. automethod:: DictionaryProxyManager.register_for_deleted_dictionary_ancestors

   .. automethod:: DictionaryProxyManager.register_for_deleted_dictionary_descendants



Dictionary Hierarchy
____________________

   .. autoattribute:: DictionaryProxyManager.dictionary_hierarchy_id

   .. autoattribute:: DictionaryProxyManager.dictionary_hierarchy

   .. automethod:: DictionaryProxyManager.can_access_dictionary_hierarchy

   .. automethod:: DictionaryProxyManager.use_comparative_dictionary_view

   .. automethod:: DictionaryProxyManager.use_plenary_dictionary_view

   .. autoattribute:: DictionaryProxyManager.root_dictionary_ids

   .. autoattribute:: DictionaryProxyManager.root_dictionaries

   .. automethod:: DictionaryProxyManager.has_parent_dictionaries

   .. automethod:: DictionaryProxyManager.is_parent_of_dictionary

   .. automethod:: DictionaryProxyManager.get_parent_dictionary_ids

   .. automethod:: DictionaryProxyManager.get_parent_dictionaries

   .. automethod:: DictionaryProxyManager.is_ancestor_of_dictionary

   .. automethod:: DictionaryProxyManager.has_child_dictionaries

   .. automethod:: DictionaryProxyManager.is_child_of_dictionary

   .. automethod:: DictionaryProxyManager.get_child_dictionary_ids

   .. automethod:: DictionaryProxyManager.get_child_dictionaries

   .. automethod:: DictionaryProxyManager.is_descendant_of_dictionary

   .. automethod:: DictionaryProxyManager.get_dictionary_node_ids

   .. automethod:: DictionaryProxyManager.get_dictionary_nodes



Dictionary Hierarchy Design
___________________________

   .. autoattribute:: DictionaryProxyManager.dictionary_hierarchy_id

   .. autoattribute:: DictionaryProxyManager.dictionary_hierarchy

   .. automethod:: DictionaryProxyManager.can_modify_dictionary_hierarchy

   .. automethod:: DictionaryProxyManager.add_root_dictionary

   .. automethod:: DictionaryProxyManager.remove_root_dictionary

   .. automethod:: DictionaryProxyManager.add_child_dictionary

   .. automethod:: DictionaryProxyManager.remove_child_dictionary

   .. automethod:: DictionaryProxyManager.remove_child_dictionaries



