.. currentmodule:: dlkit.rules.receivers
.. automodule:: dlkit.rules.receivers

Receivers
=========


Rule Receiver
-------------

.. autoclass:: RuleReceiver
   :show-inheritance:

   .. automethod:: RuleReceiver.new_rule

   .. automethod:: RuleReceiver.changed_rule

   .. automethod:: RuleReceiver.deleted_rule



Engine Receiver
---------------

.. autoclass:: EngineReceiver
   :show-inheritance:

   .. automethod:: EngineReceiver.new_engine

   .. automethod:: EngineReceiver.new_ancestor_engine

   .. automethod:: EngineReceiver.new_descendant_engine

   .. automethod:: EngineReceiver.changed_engine

   .. automethod:: EngineReceiver.deleted_engine

   .. automethod:: EngineReceiver.deleted_ancestor_engine

   .. automethod:: EngineReceiver.deleted_descendant_engine



