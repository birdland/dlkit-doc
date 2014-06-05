.. currentmodule:: dlkit.services.filing


Directory
=========


Directory
---------

.. autoclass:: Directory
   :show-inheritance:

   .. automethod:: Directory.get_directory_record



File System Methods
-------------------

   .. autoattribute:: Directory.directory_id

   .. autoattribute:: Directory.directory

   .. automethod:: Directory.can_lookup_directory_entries

   .. automethod:: Directory.has_parent_directory

   .. autoattribute:: Directory.parent_directory

   .. automethod:: Directory.use_comparative_directory_view

   .. automethod:: Directory.use_plenary_directory_view

   .. automethod:: Directory.use_federated_directory_view

   .. automethod:: Directory.use_isolated_directory_view

   .. automethod:: Directory.exists

   .. automethod:: Directory.is_file

   .. automethod:: Directory.is_directory

   .. automethod:: Directory.is_alias

   .. automethod:: Directory.get_file

   .. automethod:: Directory.get_files_by_name

   .. autoattribute:: Directory.files

   .. automethod:: Directory.get_subdirectory

   .. automethod:: Directory.get_subdirectories_by_name

   .. autoattribute:: Directory.subdirectories



File System Management Methods
------------------------------

   .. autoattribute:: Directory.directory_id

   .. autoattribute:: Directory.directory

   .. automethod:: Directory.can_manage_filing

   .. automethod:: Directory.overwrite

   .. automethod:: Directory.create_missing_paths

   .. automethod:: Directory.move_file

   .. automethod:: Directory.move_directory

   .. automethod:: Directory.copy_file

   .. automethod:: Directory.copy_directory

   .. automethod:: Directory.link_file

   .. automethod:: Directory.link_directory



File Content Methods
--------------------

   .. autoattribute:: Directory.directory_id

   .. autoattribute:: Directory.directory

   .. automethod:: Directory.can_read_files

   .. automethod:: Directory.get_input_stream

   .. automethod:: Directory.get_blocking_input_stream

   .. automethod:: Directory.can_write_files

   .. automethod:: Directory.get_output_stream

   .. automethod:: Directory.get_output_stream_for_append

   .. automethod:: Directory.touch



File Lookup Methods
-------------------

   .. autoattribute:: Directory.directory_id

   .. autoattribute:: Directory.directory

   .. automethod:: Directory.can_lookup_files

   .. automethod:: Directory.use_comparative_file_view

   .. automethod:: Directory.use_plenary_file_view

   .. automethod:: Directory.use_federated_directory_view

   .. automethod:: Directory.use_isolated_directory_view

   .. automethod:: Directory.get_file

   .. automethod:: Directory.get_files_by_ids

   .. automethod:: Directory.get_files_by_genus_type

   .. automethod:: Directory.get_files_by_parent_genus_type

   .. automethod:: Directory.get_files_by_record_type

   .. autoattribute:: Directory.files



File Query Methods
------------------

   .. autoattribute:: Directory.directory_id

   .. autoattribute:: Directory.directory

   .. automethod:: Directory.can_search_files

   .. automethod:: Directory.use_federated_directory_view

   .. automethod:: Directory.use_isolated_directory_view

   .. autoattribute:: Directory.file_query

   .. automethod:: Directory.get_files_by_query



File Search Methods
-------------------

   .. autoattribute:: Directory.file_search

   .. autoattribute:: Directory.file_search_order

   .. automethod:: Directory.get_files_by_search

   .. automethod:: Directory.get_file_query_from_inspector



File Notification Methods
-------------------------

   .. autoattribute:: Directory.directory_id

   .. autoattribute:: Directory.directory

   .. automethod:: Directory.can_register_for_file_notifications

   .. automethod:: Directory.use_federated_directory_view

   .. automethod:: Directory.use_isolated_directory_view

   .. automethod:: Directory.register_for_new_files

   .. automethod:: Directory.register_for_changed_files

   .. automethod:: Directory.register_for_changed_file

   .. automethod:: Directory.register_for_deleted_files

   .. automethod:: Directory.register_for_deleted_file



File Smart Directory Methods
----------------------------

   .. autoattribute:: Directory.directory_id

   .. autoattribute:: Directory.directory

   .. automethod:: Directory.can_manage_smart_directories

   .. autoattribute:: Directory.file_query

   .. autoattribute:: Directory.file_search_order

   .. automethod:: Directory.apply_file_query

   .. automethod:: Directory.inspect_file_query

   .. automethod:: Directory.apply_file_sequencing

   .. automethod:: Directory.get_file_query_from_inspector



