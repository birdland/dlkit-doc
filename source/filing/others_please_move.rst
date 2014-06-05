.. currentmodule:: dlkit.filing.others_please_move
.. automodule:: dlkit.filing.others_please_move

Others_Please_Move
==================


File
----

.. autoclass:: File
   :show-inheritance:

   .. automethod:: File.has_size

   .. autoattribute:: File.size

   .. automethod:: File.get_file_record



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



File Query Inspector
--------------------

.. autoclass:: FileQueryInspector
   :show-inheritance:

   .. autoattribute:: FileQueryInspector.size_terms

   .. autoattribute:: FileQueryInspector.data_string_terms

   .. autoattribute:: FileQueryInspector.data_terms

   .. automethod:: FileQueryInspector.get_file_query_inspector_record



File Form
---------

.. autoclass:: FileForm
   :show-inheritance:

   .. automethod:: FileForm.get_file_form_record



File Search Order
-----------------

.. autoclass:: FileSearchOrder
   :show-inheritance:

   .. automethod:: FileSearchOrder.order_by_size

   .. automethod:: FileSearchOrder.get_file_search_order_record



