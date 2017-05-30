
.. currentmodule:: dlkit.assessment_authoring.objects
.. automodule:: dlkit.assessment_authoring.objects

Objects
=======


Assessment Part
---------------

.. autoclass:: AssessmentPart
   :show-inheritance:

   .. autoattribute:: AssessmentPart.assessment_id

   .. autoattribute:: AssessmentPart.assessment

   .. automethod:: AssessmentPart.has_parent_part

   .. autoattribute:: AssessmentPart.assessment_part_id

   .. autoattribute:: AssessmentPart.assessment_part

   .. automethod:: AssessmentPart.is_section

   .. autoattribute:: AssessmentPart.weight

   .. autoattribute:: AssessmentPart.allocated_time

   .. autoattribute:: AssessmentPart.child_assessment_part_ids

   .. autoattribute:: AssessmentPart.child_assessment_parts

   .. automethod:: AssessmentPart.get_assessment_part_record

Assessment Part Form
--------------------

.. autoclass:: AssessmentPartForm
   :show-inheritance:

   .. autoattribute:: AssessmentPartForm.weight_metadata

   .. autoattribute:: AssessmentPartForm.weight

   .. autoattribute:: AssessmentPartForm.allocated_time_metadata

   .. autoattribute:: AssessmentPartForm.allocated_time

   .. automethod:: AssessmentPartForm.get_assessment_part_form_record

Assessment Part List
--------------------

.. autoclass:: AssessmentPartList
   :show-inheritance:

   .. autoattribute:: AssessmentPartList.next_assessment_part

   .. automethod:: AssessmentPartList.get_next_assessment_parts

Sequence Rule
-------------

.. autoclass:: SequenceRule
   :show-inheritance:

   .. autoattribute:: SequenceRule.assessment_part_id

   .. autoattribute:: SequenceRule.assessment_part

   .. autoattribute:: SequenceRule.next_assessment_part_id

   .. autoattribute:: SequenceRule.next_assessment_part

   .. autoattribute:: SequenceRule.minimum_score

   .. autoattribute:: SequenceRule.maximum_score

   .. automethod:: SequenceRule.is_cumulative

   .. autoattribute:: SequenceRule.applied_assessment_part_ids

   .. autoattribute:: SequenceRule.applied_assessment_parts

   .. automethod:: SequenceRule.get_sequence_rule_record

Sequence Rule Form
------------------

.. autoclass:: SequenceRuleForm
   :show-inheritance:

   .. autoattribute:: SequenceRuleForm.minimum_score_metadata

   .. autoattribute:: SequenceRuleForm.minimum_score

   .. autoattribute:: SequenceRuleForm.maximum_score_metadata

   .. autoattribute:: SequenceRuleForm.maximum_score

   .. autoattribute:: SequenceRuleForm.cumulative_metadata

   .. autoattribute:: SequenceRuleForm.cumulative

   .. autoattribute:: SequenceRuleForm.applied_assessment_parts_metadata

   .. automethod:: SequenceRuleForm.apply_assessment_parts

   .. automethod:: SequenceRuleForm.get_sequence_rule_form_record

Sequence Rule List
------------------

.. autoclass:: SequenceRuleList
   :show-inheritance:

   .. autoattribute:: SequenceRuleList.next_sequence_rule

   .. automethod:: SequenceRuleList.get_next_sequence_rules

