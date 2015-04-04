.. currentmodule:: dlkit.dictionary.objects
.. automodule:: dlkit.dictionary.objects

Objects
=======


Entry
-----

.. autoclass:: Entry
   :show-inheritance:

   .. autoattribute:: Entry.key_type

   .. autoattribute:: Entry.key

   .. autoattribute:: Entry.value_type

   .. autoattribute:: Entry.value

   .. automethod:: Entry.get_entry_record



Entry Form
----------

.. autoclass:: EntryForm
   :show-inheritance:

   .. autoattribute:: EntryForm.value_metadata

   .. autoattribute:: EntryForm.value

   .. automethod:: EntryForm.get_entry_form_record



Entry List
----------

.. autoclass:: EntryList
   :show-inheritance:

   .. autoattribute:: EntryList.next_entry

   .. automethod:: EntryList.get_next_entries



Dictionary Form
---------------

.. autoclass:: DictionaryForm
   :show-inheritance:

   .. automethod:: DictionaryForm.get_dictionary_form_record



Dictionary List
---------------

.. autoclass:: DictionaryList
   :show-inheritance:

   .. autoattribute:: DictionaryList.next_dictionary

   .. automethod:: DictionaryList.get_next_dictionaries



Dictionary Node
---------------

.. autoclass:: DictionaryNode
   :show-inheritance:

   .. autoattribute:: DictionaryNode.dictionary

   .. autoattribute:: DictionaryNode.parent_dictionary_nodes

   .. autoattribute:: DictionaryNode.child_dictionary_nodes



Dictionary Node List
--------------------

.. autoclass:: DictionaryNodeList
   :show-inheritance:

   .. autoattribute:: DictionaryNodeList.next_dictionary_node

   .. automethod:: DictionaryNodeList.get_next_dictionary_nodes



