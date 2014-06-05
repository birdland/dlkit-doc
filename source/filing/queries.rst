.. currentmodule:: dlkit.filing.queries
.. automodule:: dlkit.filing.queries

Queries
=======


Directory Entry Query
---------------------

.. autoclass:: DirectoryEntryQuery
   :show-inheritance:

   .. automethod:: DirectoryEntryQuery.match_name

   .. autoattribute:: DirectoryEntryQuery.name_terms

   .. automethod:: DirectoryEntryQuery.match_path

   .. autoattribute:: DirectoryEntryQuery.path_terms

   .. automethod:: DirectoryEntryQuery.supports_directory_query

   .. autoattribute:: DirectoryEntryQuery.directory_query

   .. autoattribute:: DirectoryEntryQuery.directory_terms

   .. automethod:: DirectoryEntryQuery.match_aliases

   .. automethod:: DirectoryEntryQuery.match_any_aliases

   .. autoattribute:: DirectoryEntryQuery.aliases_terms

   .. automethod:: DirectoryEntryQuery.match_owner_id

   .. autoattribute:: DirectoryEntryQuery.owner_id_terms

   .. automethod:: DirectoryEntryQuery.supports_owner_query

   .. autoattribute:: DirectoryEntryQuery.owner_query

   .. autoattribute:: DirectoryEntryQuery.owner_terms

   .. automethod:: DirectoryEntryQuery.match_created_time

   .. autoattribute:: DirectoryEntryQuery.created_time_terms

   .. automethod:: DirectoryEntryQuery.match_modified_time

   .. autoattribute:: DirectoryEntryQuery.modified_time_terms

   .. automethod:: DirectoryEntryQuery.match_last_access_time

   .. autoattribute:: DirectoryEntryQuery.last_access_time_terms



File Query
----------

.. autoclass:: FileQuery
   :show-inheritance:

   .. automethod:: FileQuery.match_size

   .. automethod:: FileQuery.match_any_size

   .. autoattribute:: FileQuery.size_terms

   .. automethod:: FileQuery.match_data_string

   .. autoattribute:: FileQuery.data_string_terms

   .. automethod:: FileQuery.match_data

   .. automethod:: FileQuery.match_any_data

   .. autoattribute:: FileQuery.data_terms

   .. automethod:: FileQuery.get_file_query_record



Directory Query
---------------

.. autoclass:: DirectoryQuery
   :show-inheritance:

   .. automethod:: DirectoryQuery.match_file_name

   .. autoattribute:: DirectoryQuery.file_name_terms

   .. automethod:: DirectoryQuery.supports_file_query

   .. automethod:: DirectoryQuery.get_file_query

   .. automethod:: DirectoryQuery.match_any_file

   .. autoattribute:: DirectoryQuery.file_terms

   .. automethod:: DirectoryQuery.get_directory_query_record



