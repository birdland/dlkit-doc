.. currentmodule:: dlkit.filing.objects
.. automodule:: dlkit.filing.objects

Objects
=======


Directory Entry
---------------

.. autoclass:: DirectoryEntry
   :show-inheritance:

   .. autoattribute:: DirectoryEntry.name

   .. automethod:: DirectoryEntry.is_alias

   .. autoattribute:: DirectoryEntry.path

   .. autoattribute:: DirectoryEntry.real_path

   .. autoattribute:: DirectoryEntry.owner_id

   .. autoattribute:: DirectoryEntry.owner

   .. autoattribute:: DirectoryEntry.created_time

   .. autoattribute:: DirectoryEntry.last_modified_time

   .. autoattribute:: DirectoryEntry.last_access_time



Directory Entry Form
--------------------

.. autoclass:: DirectoryEntryForm
   :show-inheritance:

   .. autoattribute:: DirectoryEntryForm.owner_metadata

   .. autoattribute:: DirectoryEntryForm.owner



File
----

.. autoclass:: File
   :show-inheritance:

   .. automethod:: File.has_size

   .. autoattribute:: File.size

   .. automethod:: File.get_file_record



File Form
---------

.. autoclass:: FileForm
   :show-inheritance:

   .. automethod:: FileForm.get_file_form_record



File List
---------

.. autoclass:: FileList
   :show-inheritance:

   .. autoattribute:: FileList.next_file

   .. automethod:: FileList.get_next_files



Directory Form
--------------

.. autoclass:: DirectoryForm
   :show-inheritance:

   .. automethod:: DirectoryForm.get_directory_form_record



Directory List
--------------

.. autoclass:: DirectoryList
   :show-inheritance:

   .. autoattribute:: DirectoryList.next_directory

   .. automethod:: DirectoryList.get_next_directories



