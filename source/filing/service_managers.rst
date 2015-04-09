Summary
=======
.. currentmodule:: dlkit.services.filing
.. automodule:: dlkit.services.filing

Service Managers
================


Filing Manager
--------------

.. autoclass:: FilingManager
   :show-inheritance:

   .. autoattribute:: FilingManager.filing_allocation_manager



Filing Profile Methods
______________

   .. automethod:: FilingManager.supports_visible_federation

   .. automethod:: FilingManager.supports_file_system

   .. automethod:: FilingManager.supports_file_system_management

   .. automethod:: FilingManager.supports_file_content

   .. automethod:: FilingManager.supports_file_lookup

   .. automethod:: FilingManager.supports_file_query

   .. automethod:: FilingManager.supports_file_search

   .. automethod:: FilingManager.supports_file_notification

   .. automethod:: FilingManager.supports_file_smart_directory

   .. automethod:: FilingManager.supports_directory_lookup

   .. automethod:: FilingManager.supports_directory_query

   .. automethod:: FilingManager.supports_directory_search

   .. automethod:: FilingManager.supports_directory_admin

   .. automethod:: FilingManager.supports_directory_notification

   .. automethod:: FilingManager.supports_filing_management

   .. automethod:: FilingManager.supports_filing_allocation

   .. autoattribute:: FilingManager.file_record_types

   .. automethod:: FilingManager.supports_file_record_type

   .. autoattribute:: FilingManager.file_search_record_types

   .. automethod:: FilingManager.supports_file_search_record_type

   .. autoattribute:: FilingManager.directory_record_types

   .. automethod:: FilingManager.supports_directory_record_type

   .. autoattribute:: FilingManager.directory_search_record_types

   .. automethod:: FilingManager.supports_directory_search_record_type



Directory Lookup
________________

   .. autoattribute:: FilingManager.directory_id

   .. autoattribute:: FilingManager.directory

   .. automethod:: FilingManager.can_lookup_directories

   .. automethod:: FilingManager.use_comparative_directory_view

   .. automethod:: FilingManager.use_plenary_directory_view

   .. automethod:: FilingManager.use_federated_directory_view

   .. automethod:: FilingManager.use_isolated_directory_view

   .. automethod:: FilingManager.get_directory

   .. automethod:: FilingManager.get_directories_by_ids

   .. automethod:: FilingManager.get_directories_by_genus_type

   .. automethod:: FilingManager.get_directories_by_parent_genus_type

   .. automethod:: FilingManager.get_directories_by_record_type

   .. automethod:: FilingManager.get_directories_by_provider

   .. autoattribute:: FilingManager.directories



Directory Query
_______________

   .. autoattribute:: FilingManager.directory_id

   .. autoattribute:: FilingManager.directory

   .. automethod:: FilingManager.can_search_directories

   .. automethod:: FilingManager.use_federated_directory_view

   .. automethod:: FilingManager.use_isolated_directory_view

   .. autoattribute:: FilingManager.directory_query

   .. automethod:: FilingManager.get_directories_by_query



Directory Search
________________

   .. autoattribute:: FilingManager.directory_search

   .. autoattribute:: FilingManager.directory_search_order

   .. automethod:: FilingManager.get_directories_by_search

   .. automethod:: FilingManager.get_directory_query_from_inspector



Directory Admin
_______________

   .. autoattribute:: FilingManager.directory_id

   .. autoattribute:: FilingManager.directory

   .. automethod:: FilingManager.can_modify_directory

   .. automethod:: FilingManager.overwrite

   .. automethod:: FilingManager.can_create_file_with_record_types

   .. automethod:: FilingManager.get_file_form_for_create

   .. automethod:: FilingManager.create_file

   .. automethod:: FilingManager.get_file_form_for_update

   .. automethod:: FilingManager.update_file

   .. automethod:: FilingManager.delete_file

   .. automethod:: FilingManager.can_create_directory_with_record_types

   .. automethod:: FilingManager.get_directory_form_for_create

   .. automethod:: FilingManager.create_directory

   .. automethod:: FilingManager.get_directory_form_for_update

   .. automethod:: FilingManager.update_directory

   .. automethod:: FilingManager.delete_directory

   .. automethod:: FilingManager.clear_directory



Directory Notification
______________________

   .. autoattribute:: FilingManager.directory_id

   .. autoattribute:: FilingManager.directory

   .. automethod:: FilingManager.can_register_for_directory_notifications

   .. automethod:: FilingManager.use_federated_directory_view

   .. automethod:: FilingManager.use_isolated_directory_view

   .. automethod:: FilingManager.register_for_new_directories

   .. automethod:: FilingManager.register_for_changed_directories

   .. automethod:: FilingManager.register_for_changed_directory

   .. automethod:: FilingManager.register_for_deleted_directories

   .. automethod:: FilingManager.register_for_deleted_directory



Filing Proxy Manager
--------------------

.. autoclass:: FilingProxyManager
   :show-inheritance:

   .. autoattribute:: FilingProxyManager.filing_allocation_proxy_manager



Filing Profile Methods
______________

   .. automethod:: FilingProxyManager.supports_visible_federation

   .. automethod:: FilingProxyManager.supports_file_system

   .. automethod:: FilingProxyManager.supports_file_system_management

   .. automethod:: FilingProxyManager.supports_file_content

   .. automethod:: FilingProxyManager.supports_file_lookup

   .. automethod:: FilingProxyManager.supports_file_query

   .. automethod:: FilingProxyManager.supports_file_search

   .. automethod:: FilingProxyManager.supports_file_notification

   .. automethod:: FilingProxyManager.supports_file_smart_directory

   .. automethod:: FilingProxyManager.supports_directory_lookup

   .. automethod:: FilingProxyManager.supports_directory_query

   .. automethod:: FilingProxyManager.supports_directory_search

   .. automethod:: FilingProxyManager.supports_directory_admin

   .. automethod:: FilingProxyManager.supports_directory_notification

   .. automethod:: FilingProxyManager.supports_filing_management

   .. automethod:: FilingProxyManager.supports_filing_allocation

   .. autoattribute:: FilingProxyManager.file_record_types

   .. automethod:: FilingProxyManager.supports_file_record_type

   .. autoattribute:: FilingProxyManager.file_search_record_types

   .. automethod:: FilingProxyManager.supports_file_search_record_type

   .. autoattribute:: FilingProxyManager.directory_record_types

   .. automethod:: FilingProxyManager.supports_directory_record_type

   .. autoattribute:: FilingProxyManager.directory_search_record_types

   .. automethod:: FilingProxyManager.supports_directory_search_record_type



Directory Lookup
________________

   .. autoattribute:: FilingProxyManager.directory_id

   .. autoattribute:: FilingProxyManager.directory

   .. automethod:: FilingProxyManager.can_lookup_directories

   .. automethod:: FilingProxyManager.use_comparative_directory_view

   .. automethod:: FilingProxyManager.use_plenary_directory_view

   .. automethod:: FilingProxyManager.use_federated_directory_view

   .. automethod:: FilingProxyManager.use_isolated_directory_view

   .. automethod:: FilingProxyManager.get_directory

   .. automethod:: FilingProxyManager.get_directories_by_ids

   .. automethod:: FilingProxyManager.get_directories_by_genus_type

   .. automethod:: FilingProxyManager.get_directories_by_parent_genus_type

   .. automethod:: FilingProxyManager.get_directories_by_record_type

   .. automethod:: FilingProxyManager.get_directories_by_provider

   .. autoattribute:: FilingProxyManager.directories



Directory Query
_______________

   .. autoattribute:: FilingProxyManager.directory_id

   .. autoattribute:: FilingProxyManager.directory

   .. automethod:: FilingProxyManager.can_search_directories

   .. automethod:: FilingProxyManager.use_federated_directory_view

   .. automethod:: FilingProxyManager.use_isolated_directory_view

   .. autoattribute:: FilingProxyManager.directory_query

   .. automethod:: FilingProxyManager.get_directories_by_query



Directory Search
________________

   .. autoattribute:: FilingProxyManager.directory_search

   .. autoattribute:: FilingProxyManager.directory_search_order

   .. automethod:: FilingProxyManager.get_directories_by_search

   .. automethod:: FilingProxyManager.get_directory_query_from_inspector



Directory Admin
_______________

   .. autoattribute:: FilingProxyManager.directory_id

   .. autoattribute:: FilingProxyManager.directory

   .. automethod:: FilingProxyManager.can_modify_directory

   .. automethod:: FilingProxyManager.overwrite

   .. automethod:: FilingProxyManager.can_create_file_with_record_types

   .. automethod:: FilingProxyManager.get_file_form_for_create

   .. automethod:: FilingProxyManager.create_file

   .. automethod:: FilingProxyManager.get_file_form_for_update

   .. automethod:: FilingProxyManager.update_file

   .. automethod:: FilingProxyManager.delete_file

   .. automethod:: FilingProxyManager.can_create_directory_with_record_types

   .. automethod:: FilingProxyManager.get_directory_form_for_create

   .. automethod:: FilingProxyManager.create_directory

   .. automethod:: FilingProxyManager.get_directory_form_for_update

   .. automethod:: FilingProxyManager.update_directory

   .. automethod:: FilingProxyManager.delete_directory

   .. automethod:: FilingProxyManager.clear_directory



Directory Notification
______________________

   .. autoattribute:: FilingProxyManager.directory_id

   .. autoattribute:: FilingProxyManager.directory

   .. automethod:: FilingProxyManager.can_register_for_directory_notifications

   .. automethod:: FilingProxyManager.use_federated_directory_view

   .. automethod:: FilingProxyManager.use_isolated_directory_view

   .. automethod:: FilingProxyManager.register_for_new_directories

   .. automethod:: FilingProxyManager.register_for_changed_directories

   .. automethod:: FilingProxyManager.register_for_changed_directory

   .. automethod:: FilingProxyManager.register_for_deleted_directories

   .. automethod:: FilingProxyManager.register_for_deleted_directory



