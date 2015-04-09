.. currentmodule:: dlkit.filing.query_inspectors
.. automodule:: dlkit.filing.query_inspectors

Query Inspectors
================


Directory Entry Query Inspector
-------------------------------

.. autoclass:: DirectoryEntryQueryInspector
   :show-inheritance:

   .. autoattribute:: DirectoryEntryQueryInspector.name_terms

   .. autoattribute:: DirectoryEntryQueryInspector.path_terms

   .. autoattribute:: DirectoryEntryQueryInspector.directory_terms

   .. autoattribute:: DirectoryEntryQueryInspector.aliases_terms

   .. autoattribute:: DirectoryEntryQueryInspector.owner_id_terms

   .. autoattribute:: DirectoryEntryQueryInspector.owner_terms

   .. autoattribute:: DirectoryEntryQueryInspector.created_time_terms

   .. autoattribute:: DirectoryEntryQueryInspector.modified_time_terms

   .. autoattribute:: DirectoryEntryQueryInspector.last_access_time_terms



File Query Inspector
--------------------

.. autoclass:: FileQueryInspector
   :show-inheritance:

   .. autoattribute:: FileQueryInspector.size_terms

   .. autoattribute:: FileQueryInspector.data_string_terms

   .. autoattribute:: FileQueryInspector.data_terms

   .. automethod:: FileQueryInspector.get_file_query_inspector_record



Directory Query Inspector
-------------------------

.. autoclass:: DirectoryQueryInspector
   :show-inheritance:

   .. autoattribute:: DirectoryQueryInspector.file_name_terms

   .. autoattribute:: DirectoryQueryInspector.file_terms

   .. automethod:: DirectoryQueryInspector.get_directory_query_inspector_record



