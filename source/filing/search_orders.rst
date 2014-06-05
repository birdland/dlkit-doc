.. currentmodule:: dlkit.filing.search_orders
.. automodule:: dlkit.filing.search_orders

Search_Orders
=============


Directory Entry Search Order
----------------------------

.. autoclass:: DirectoryEntrySearchOrder
   :show-inheritance:

   .. automethod:: DirectoryEntrySearchOrder.order_by_name

   .. automethod:: DirectoryEntrySearchOrder.order_by_path

   .. automethod:: DirectoryEntrySearchOrder.order_by_owner

   .. automethod:: DirectoryEntrySearchOrder.supports_owner_search_order

   .. autoattribute:: DirectoryEntrySearchOrder.owner_search_order

   .. automethod:: DirectoryEntrySearchOrder.order_by_created_time

   .. automethod:: DirectoryEntrySearchOrder.order_by_modified_time

   .. automethod:: DirectoryEntrySearchOrder.order_by_last_access_time



File Search Order
-----------------

.. autoclass:: FileSearchOrder
   :show-inheritance:

   .. automethod:: FileSearchOrder.order_by_size

   .. automethod:: FileSearchOrder.get_file_search_order_record



Directory Search Order
----------------------

.. autoclass:: DirectorySearchOrder
   :show-inheritance:

   .. automethod:: DirectorySearchOrder.get_directory_search_order_record



