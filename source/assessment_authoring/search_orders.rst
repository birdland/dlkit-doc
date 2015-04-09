.. currentmodule:: dlkit.assessment.authoring.search_orders
.. automodule:: dlkit.assessment.authoring.search_orders

Search Orders
=============


Assessment Part Search Order
----------------------------

.. autoclass:: AssessmentPartSearchOrder
   :show-inheritance:

   .. automethod:: AssessmentPartSearchOrder.order_by_assessment

   .. automethod:: AssessmentPartSearchOrder.supports_assessment_search_order

   .. autoattribute:: AssessmentPartSearchOrder.assessment_search_order

   .. automethod:: AssessmentPartSearchOrder.order_by_section

   .. automethod:: AssessmentPartSearchOrder.order_by_weight

   .. automethod:: AssessmentPartSearchOrder.order_by_allocated_time

   .. automethod:: AssessmentPartSearchOrder.get_assessment_part_search_order_record



Sequence Rule Search Order
--------------------------

.. autoclass:: SequenceRuleSearchOrder
   :show-inheritance:

   .. automethod:: SequenceRuleSearchOrder.order_by_assessment_part

   .. automethod:: SequenceRuleSearchOrder.supports_assessment_part_search_order

   .. autoattribute:: SequenceRuleSearchOrder.assessment_part_search_order

   .. automethod:: SequenceRuleSearchOrder.order_by_next_assessment_part

   .. automethod:: SequenceRuleSearchOrder.supports_next_assessment_part_search_order

   .. autoattribute:: SequenceRuleSearchOrder.next_assessment_part_search_order

   .. automethod:: SequenceRuleSearchOrder.order_by_minimum_score

   .. automethod:: SequenceRuleSearchOrder.order_by_maximum_score

   .. automethod:: SequenceRuleSearchOrder.order_by_cumulative

   .. automethod:: SequenceRuleSearchOrder.get_sequence_rule_search_order_record



Sequence Rule Enabler Search Order
----------------------------------

.. autoclass:: SequenceRuleEnablerSearchOrder
   :show-inheritance:

   .. automethod:: SequenceRuleEnablerSearchOrder.get_sequence_rule_enabler_search_order_record



