from ..osid import query_inspectors as osid_query_inspectors


class AssessmentPartQueryInspector(osid_query_inspectors.OsidObjectQueryInspector, osid_query_inspectors.OsidContainableQueryInspector, osid_query_inspectors.OsidOperableQueryInspector):
    """This is the query inspector for examining assessment part queries."""
    def get_assessment_id_terms(self):
        """Gets the assessment ``Id`` query terms.

        :return: the assessment ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    assessment_id_terms = property(fget=get_assessment_id_terms)

    def get_assessment_terms(self):
        """Gets the assessment query terms.

        :return: the assessment terms
        :rtype: ``osid.assessment.AssessmentQueryInspector``

        """
        return # osid.assessment.AssessmentQueryInspector

    assessment_terms = property(fget=get_assessment_terms)

    def get_parent_assessment_part_id_terms(self):
        """Gets the assessment part ``Id`` query terms.

        :return: the assessment parent ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    parent_assessment_part_id_terms = property(fget=get_parent_assessment_part_id_terms)

    def get_parent_assessment_part_terms(self):
        """Gets the assessment part query terms.

        :return: the assessment part terms
        :rtype: ``osid.assessment.authoring.AssessmentPartQueryInspector``

        """
        return # osid.assessment.authoring.AssessmentPartQueryInspector

    parent_assessment_part_terms = property(fget=get_parent_assessment_part_terms)

    def get_section_terms(self):
        """Gets the section query terms.

        :return: the section terms
        :rtype: ``osid.search.terms.BooleanTerm``

        """
        return # osid.search.terms.BooleanTerm

    section_terms = property(fget=get_section_terms)

    def get_weight_terms(self):
        """Gets the weight terms.

        :return: the resource ``Id`` terms
        :rtype: ``osid.search.terms.CardinalTerm``

        """
        return # osid.search.terms.CardinalTerm

    weight_terms = property(fget=get_weight_terms)

    def get_allocated_time_terms(self):
        """Gets the allocated time terms.

        :return: the time terms
        :rtype: ``osid.search.terms.DurationTerm``

        """
        return # osid.search.terms.DurationTerm

    allocated_time_terms = property(fget=get_allocated_time_terms)

    def get_child_assessment_part_id_terms(self):
        """Gets the assessment part ``Id`` query terms.

        :return: the assessment parent ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    child_assessment_part_id_terms = property(fget=get_child_assessment_part_id_terms)

    def get_child_assessment_part_terms(self):
        """Gets the assessment part query terms.

        :return: the assessment part terms
        :rtype: ``osid.assessment.authoring.AssessmentPartQueryInspector``

        """
        return # osid.assessment.authoring.AssessmentPartQueryInspector

    child_assessment_part_terms = property(fget=get_child_assessment_part_terms)

    def get_bank_id_terms(self):
        """Gets the bank ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    bank_id_terms = property(fget=get_bank_id_terms)

    def get_bank_terms(self):
        """Gets the bank query terms.

        :return: the query terms
        :rtype: ``osid.assessment.BankQueryInspector``

        """
        return # osid.assessment.BankQueryInspector

    bank_terms = property(fget=get_bank_terms)

    def get_assessment_part_query_inspector_record(self, assessment_part_record_type):
        """Gets the assessment part query inspector record corresponding to the given ``AssessmentPart`` record ``Type``.

        :param assessment_part_record_type: an assessment part record type
        :type assessment_part_record_type: ``osid.type.Type``
        :return: the assessment part query inspector record
        :rtype: ``osid.assessment.authoring.records.AssessmentPartQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``assessment_part_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_part_record_type)`` is ``false``

        """
        return # osid.assessment.authoring.records.AssessmentPartQueryInspectorRecord


class SequenceRuleQueryInspector(osid_query_inspectors.OsidRuleQueryInspector):
    """This is the query inspector for examining sequence rule queries."""
    def get_assessment_part_id_terms(self):
        """Gets the assessment part ``Id`` query terms.

        :return: the assessment parent ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    assessment_part_id_terms = property(fget=get_assessment_part_id_terms)

    def get_assessment_part_terms(self):
        """Gets the assessment part query terms.

        :return: the assessment part terms
        :rtype: ``osid.assessment.authoring.AssessmentPartQueryInspector``

        """
        return # osid.assessment.authoring.AssessmentPartQueryInspector

    assessment_part_terms = property(fget=get_assessment_part_terms)

    def get_next_assessment_part_id_terms(self):
        """Gets the assessment part ``Id`` query terms.

        :return: the assessment parent ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    next_assessment_part_id_terms = property(fget=get_next_assessment_part_id_terms)

    def get_next_assessment_part_terms(self):
        """Gets the assessment part query terms.

        :return: the assessment part terms
        :rtype: ``osid.assessment.authoring.AssessmentPartQueryInspector``

        """
        return # osid.assessment.authoring.AssessmentPartQueryInspector

    next_assessment_part_terms = property(fget=get_next_assessment_part_terms)

    def get_minimum_score_terms(self):
        """Gets the minimum score query terms.

        :return: the minimum score terms
        :rtype: ``osid.search.terms.CardinalRangeTerm``

        """
        return # osid.search.terms.CardinalRangeTerm

    minimum_score_terms = property(fget=get_minimum_score_terms)

    def get_maximum_score_terms(self):
        """Gets the maximum score query terms.

        :return: the maximum score terms
        :rtype: ``osid.search.terms.CardinalRangeTerm``

        """
        return # osid.search.terms.CardinalRangeTerm

    maximum_score_terms = property(fget=get_maximum_score_terms)

    def get_cumulative_terms(self):
        """Gets the minimum score query terms.

        :return: the cumulative terms
        :rtype: ``osid.search.terms.BooleanTerm``

        """
        return # osid.search.terms.BooleanTerm

    cumulative_terms = property(fget=get_cumulative_terms)

    def get_applied_assessment_part_id_terms(self):
        """Gets the assessment part ``Id`` query terms.

        :return: the assessment parent ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    applied_assessment_part_id_terms = property(fget=get_applied_assessment_part_id_terms)

    def get_applied_assessment_part_terms(self):
        """Gets the assessment part query terms.

        :return: the assessment part terms
        :rtype: ``osid.assessment.authoring.AssessmentPartQueryInspector``

        """
        return # osid.assessment.authoring.AssessmentPartQueryInspector

    applied_assessment_part_terms = property(fget=get_applied_assessment_part_terms)

    def get_bank_id_terms(self):
        """Gets the bank ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    bank_id_terms = property(fget=get_bank_id_terms)

    def get_bank_terms(self):
        """Gets the bank query terms.

        :return: the query terms
        :rtype: ``osid.assessment.BankQueryInspector``

        """
        return # osid.assessment.BankQueryInspector

    bank_terms = property(fget=get_bank_terms)

    def get_sequence_rule_query_inspector_record(self, sequence_rule_record_type):
        """Gets the sequence rule query inspector record corresponding to the given ``SequenceRule`` record ``Type``.

        :param sequence_rule_record_type: a sequence rule record type
        :type sequence_rule_record_type: ``osid.type.Type``
        :return: the sequence rule query inspector record
        :rtype: ``osid.assessment.authoring.records.SequenceRuleQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``sequence_rule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(sequence_rule_record_type)`` is ``false``

        """
        return # osid.assessment.authoring.records.SequenceRuleQueryInspectorRecord


class SequenceRuleEnablerQueryInspector(osid_query_inspectors.OsidEnablerQueryInspector):
    """This is the query inspector for examining sequence rule enabler queries."""
    def get_ruled_sequence_rule_id_terms(self):
        """Gets the sequence rule ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    ruled_sequence_rule_id_terms = property(fget=get_ruled_sequence_rule_id_terms)

    def get_ruled_sequence_rule_terms(self):
        """Gets the sequence rule query terms.

        :return: the query terms
        :rtype: ``osid.assessment.authoring.SequenceRuleQueryInspector``

        """
        return # osid.assessment.authoring.SequenceRuleQueryInspector

    ruled_sequence_rule_terms = property(fget=get_ruled_sequence_rule_terms)

    def get_bank_id_terms(self):
        """Gets the bank ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    bank_id_terms = property(fget=get_bank_id_terms)

    def get_bank_terms(self):
        """Gets the bank query terms.

        :return: the query terms
        :rtype: ``osid.assessment.BankQueryInspector``

        """
        return # osid.assessment.BankQueryInspector

    bank_terms = property(fget=get_bank_terms)

    def get_sequence_rule_enabler_query_inspector_record(self, sequence_rule_enabler_record_type):
        """Gets the sequence rule enabler query inspector record corresponding to the given ``SequenceRuleEnabler`` record ``Type``.

        :param sequence_rule_enabler_record_type: a sequence rule enabler record type
        :type sequence_rule_enabler_record_type: ``osid.type.Type``
        :return: the sequence rule enabler query inspector record
        :rtype: ``osid.assessment.authoring.records.SequenceRuleEnablerQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(sequence_rule_enabler_record_type)`` is ``false``

        """
        return # osid.assessment.authoring.records.SequenceRuleEnablerQueryInspectorRecord


