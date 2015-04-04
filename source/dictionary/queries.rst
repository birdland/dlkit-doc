.. currentmodule:: dlkit.dictionary.queries
.. automodule:: dlkit.dictionary.queries

Queries
=======


Entry Query
-----------

.. autoclass:: EntryQuery
   :show-inheritance:

   .. automethod:: EntryQuery.match_key_type

   .. autoattribute:: EntryQuery.key_type_terms

   .. automethod:: EntryQuery.match_key

   .. autoattribute:: EntryQuery.key_terms

   .. automethod:: EntryQuery.match_value_type

   .. autoattribute:: EntryQuery.value_type_terms

   .. automethod:: EntryQuery.match_value

   .. autoattribute:: EntryQuery.value_terms

   .. automethod:: EntryQuery.match_dictionary_id

   .. autoattribute:: EntryQuery.dictionary_id_terms

   .. automethod:: EntryQuery.supports_dictionary_query

   .. autoattribute:: EntryQuery.dictionary_query

   .. autoattribute:: EntryQuery.dictionary_terms

   .. automethod:: EntryQuery.get_entry_query_record



Dictionary Query
----------------

.. autoclass:: DictionaryQuery
   :show-inheritance:

   .. automethod:: DictionaryQuery.match_entry_id

   .. autoattribute:: DictionaryQuery.entry_id_terms

   .. automethod:: DictionaryQuery.supports_entry_query

   .. autoattribute:: DictionaryQuery.entry_query

   .. automethod:: DictionaryQuery.match_any_entry

   .. autoattribute:: DictionaryQuery.entry_terms

   .. automethod:: DictionaryQuery.match_ancestor_dictionary_id

   .. autoattribute:: DictionaryQuery.ancestor_dictionary_id_terms

   .. automethod:: DictionaryQuery.supports_ancestor_dictionary_query

   .. autoattribute:: DictionaryQuery.ancestor_dictionary_query

   .. automethod:: DictionaryQuery.match_any_ancestor_dictionary

   .. autoattribute:: DictionaryQuery.ancestor_dictionary_terms

   .. automethod:: DictionaryQuery.match_descendant_dictionary_id

   .. autoattribute:: DictionaryQuery.descendant_dictionary_id_terms

   .. automethod:: DictionaryQuery.supports_descendant_dictionary_query

   .. autoattribute:: DictionaryQuery.descendant_dictionary_query

   .. automethod:: DictionaryQuery.match_any_descendant_dictionary

   .. autoattribute:: DictionaryQuery.descendant_dictionary_terms

   .. automethod:: DictionaryQuery.get_dictionary_query_record



