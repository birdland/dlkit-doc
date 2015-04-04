.. currentmodule:: dlkit.dictionary.query_inspectors
.. automodule:: dlkit.dictionary.query_inspectors

Query_Inspectors
================


Entry Query Inspector
---------------------

.. autoclass:: EntryQueryInspector
   :show-inheritance:

   .. autoattribute:: EntryQueryInspector.key_type_terms

   .. autoattribute:: EntryQueryInspector.key_terms

   .. autoattribute:: EntryQueryInspector.value_type_terms

   .. autoattribute:: EntryQueryInspector.value_terms

   .. autoattribute:: EntryQueryInspector.dictionary_id_terms

   .. autoattribute:: EntryQueryInspector.dictionary_terms

   .. automethod:: EntryQueryInspector.get_entry_query_inspector_record



Dictionary Query Inspector
--------------------------

.. autoclass:: DictionaryQueryInspector
   :show-inheritance:

   .. autoattribute:: DictionaryQueryInspector.entry_id_terms

   .. autoattribute:: DictionaryQueryInspector.entry_terms

   .. autoattribute:: DictionaryQueryInspector.ancestor_dictionary_id_terms

   .. autoattribute:: DictionaryQueryInspector.ancestor_dictionary_terms

   .. autoattribute:: DictionaryQueryInspector.descendant_dictionary_id_terms

   .. autoattribute:: DictionaryQueryInspector.descendant_dictionary_terms

   .. automethod:: DictionaryQueryInspector.get_dictionary_query_inspector_record



