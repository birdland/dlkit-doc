.. currentmodule:: dlkit.assessment.authoring.query_inspectors
.. automodule:: dlkit.assessment.authoring.query_inspectors

Query_Inspectors
================


Assessment Part Query Inspector
-------------------------------

.. autoclass:: AssessmentPartQueryInspector
   :show-inheritance:

   .. autoattribute:: AssessmentPartQueryInspector.assessment_id_terms

   .. autoattribute:: AssessmentPartQueryInspector.assessment_terms

   .. autoattribute:: AssessmentPartQueryInspector.parent_assessment_part_id_terms

   .. autoattribute:: AssessmentPartQueryInspector.parent_assessment_part_terms

   .. autoattribute:: AssessmentPartQueryInspector.section_terms

   .. autoattribute:: AssessmentPartQueryInspector.weight_terms

   .. autoattribute:: AssessmentPartQueryInspector.allocated_time_terms

   .. autoattribute:: AssessmentPartQueryInspector.child_assessment_part_id_terms

   .. autoattribute:: AssessmentPartQueryInspector.child_assessment_part_terms

   .. autoattribute:: AssessmentPartQueryInspector.bank_id_terms

   .. autoattribute:: AssessmentPartQueryInspector.bank_terms

   .. automethod:: AssessmentPartQueryInspector.get_assessment_part_query_inspector_record



Sequence Rule Query Inspector
-----------------------------

.. autoclass:: SequenceRuleQueryInspector
   :show-inheritance:

   .. autoattribute:: SequenceRuleQueryInspector.assessment_part_id_terms

   .. autoattribute:: SequenceRuleQueryInspector.assessment_part_terms

   .. autoattribute:: SequenceRuleQueryInspector.next_assessment_part_id_terms

   .. autoattribute:: SequenceRuleQueryInspector.next_assessment_part_terms

   .. autoattribute:: SequenceRuleQueryInspector.minimum_score_terms

   .. autoattribute:: SequenceRuleQueryInspector.maximum_score_terms

   .. autoattribute:: SequenceRuleQueryInspector.cumulative_terms

   .. autoattribute:: SequenceRuleQueryInspector.applied_assessment_part_id_terms

   .. autoattribute:: SequenceRuleQueryInspector.applied_assessment_part_terms

   .. autoattribute:: SequenceRuleQueryInspector.bank_id_terms

   .. autoattribute:: SequenceRuleQueryInspector.bank_terms

   .. automethod:: SequenceRuleQueryInspector.get_sequence_rule_query_inspector_record



Sequence Rule Enabler Query Inspector
-------------------------------------

.. autoclass:: SequenceRuleEnablerQueryInspector
   :show-inheritance:

   .. autoattribute:: SequenceRuleEnablerQueryInspector.ruled_sequence_rule_id_terms

   .. autoattribute:: SequenceRuleEnablerQueryInspector.ruled_sequence_rule_terms

   .. autoattribute:: SequenceRuleEnablerQueryInspector.bank_id_terms

   .. autoattribute:: SequenceRuleEnablerQueryInspector.bank_terms

   .. automethod:: SequenceRuleEnablerQueryInspector.get_sequence_rule_enabler_query_inspector_record



