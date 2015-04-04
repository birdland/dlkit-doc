.. currentmodule:: dlkit.dictionary.receivers
.. automodule:: dlkit.dictionary.receivers

Receivers
=========


Entry Receiver
--------------

.. autoclass:: EntryReceiver
   :show-inheritance:

   .. automethod:: EntryReceiver.new_entry

   .. automethod:: EntryReceiver.changed_entry

   .. automethod:: EntryReceiver.deleted_entry



Dictionary Receiver
-------------------

.. autoclass:: DictionaryReceiver
   :show-inheritance:

   .. automethod:: DictionaryReceiver.new_dictionary

   .. automethod:: DictionaryReceiver.new_ancestor_endpoint

   .. automethod:: DictionaryReceiver.new_descendant_dictionary

   .. automethod:: DictionaryReceiver.changed_dictionary

   .. automethod:: DictionaryReceiver.deleted_dictionary

   .. automethod:: DictionaryReceiver.deleted_ancestor_dictionary

   .. automethod:: DictionaryReceiver.deleted_descendant_dictionary



