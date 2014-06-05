.. currentmodule:: dlkit.rules.objects
.. automodule:: dlkit.rules.objects

Objects
=======


Rule
----

.. autoclass:: Rule
   :show-inheritance:

   .. automethod:: Rule.get_rule_record



Rule Form
---------

.. autoclass:: RuleForm
   :show-inheritance:

   .. automethod:: RuleForm.get_rule_form_record



Rule List
---------

.. autoclass:: RuleList
   :show-inheritance:

   .. autoattribute:: RuleList.next_rule

   .. automethod:: RuleList.get_next_rules



Engine Form
-----------

.. autoclass:: EngineForm
   :show-inheritance:

   .. automethod:: EngineForm.get_engine_form_record



Engine List
-----------

.. autoclass:: EngineList
   :show-inheritance:

   .. autoattribute:: EngineList.next_engine

   .. automethod:: EngineList.get_next_engines



Engine Node
-----------

.. autoclass:: EngineNode
   :show-inheritance:

   .. autoattribute:: EngineNode.engine

   .. autoattribute:: EngineNode.parent_engine_nodes

   .. autoattribute:: EngineNode.child_engine_nodes



Engine Node List
----------------

.. autoclass:: EngineNodeList
   :show-inheritance:

   .. autoattribute:: EngineNodeList.next_engine_node

   .. automethod:: EngineNodeList.get_next_engine_nodes



