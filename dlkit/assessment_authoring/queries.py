from ..osid import queries as osid_queries


class AssessmentPartQuery(osid_queries.OsidObjectQuery, osid_queries.OsidContainableQuery, osid_queries.OsidOperableQuery):
    """This is the query for searching assessment parts.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    def match_assessment_id(self, assessment_id, match):
        """Sets the assessment ``Id`` for this query.

        :param assessment_id: an assessment ``Id``
        :type assessment_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``

        """
        pass

    def clear_assessment_id_terms(self):
        """Clears all assessment ``Id`` terms."""
        pass

    assessment_id_terms = property(fdel=clear_assessment_id_terms)

    def supports_assessment_query(self):
        """Tests if an ``AssessmentQuery`` is available.

        :return: ``true`` if an assessment query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_assessment_query(self):
        """Gets the query for an assessment.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment query
        :rtype: ``osid.assessment.AssessmentQuery``
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` is ``false``

        """
        return # osid.assessment.AssessmentQuery

    assessment_query = property(fget=get_assessment_query)

    def clear_assessment_terms(self):
        """Clears all assessment terms."""
        pass

    assessment_terms = property(fdel=clear_assessment_terms)

    def match_parent_assessment_part_id(self, assessment_part_id, match):
        """Sets the assessment part ``Id`` for this query.

        :param assessment_part_id: an assessment part ``Id``
        :type assessment_part_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``

        """
        pass

    def clear_parent_assessment_part_id_terms(self):
        """Clears all assessment part ``Id`` terms."""
        pass

    parent_assessment_part_id_terms = property(fdel=clear_parent_assessment_part_id_terms)

    def supports_parent_assessment_part_query(self):
        """Tests if an ``AssessmentPartQuery`` is available.

        :return: ``true`` if an assessment part query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_parent_assessment_part_query(self):
        """Gets the query for an assessment part.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment part query
        :rtype: ``osid.assessment.authoring.AssessmentPartQuery``
        :raise: ``Unimplemented`` -- ``supports_parent_assessment_part_query()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartQuery

    parent_assessment_part_query = property(fget=get_parent_assessment_part_query)

    def match_any_parent_assessment_part(self, match):
        """Matches assessment parts with any parent assessment part.

        :param match: ``true`` to match assessment parts with any parent, ``false`` to match assessment parts with no parents
        :type match: ``boolean``

        """
        pass

    def clear_parent_assessment_part_terms(self):
        """Clears all assessment part terms."""
        pass

    parent_assessment_part_terms = property(fdel=clear_parent_assessment_part_terms)

    def match_section(self, match):
        """Matches assessment parts that are also used as sections.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def clear_section_terms(self):
        """Clears all section terms."""
        pass

    section_terms = property(fdel=clear_section_terms)

    def match_weight(self, low, high, match):
        """Matches assessment parts that fall in between the given weights inclusive.

        :param low: low end of range
        :type low: ``cardinal``
        :param high: high end of range
        :type high: ``cardinal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``high`` is less than ``low``

        """
        pass

    def match_any_weight(self, match):
        """Matches assessment parts with any weight assigned.

        :param match: ``true`` to match assessment parts with any wieght, ``false`` to match assessment parts with no weight
        :type match: ``boolean``

        """
        pass

    def clear_weight_terms(self):
        """Clears all weight terms."""
        pass

    weight_terms = property(fdel=clear_weight_terms)

    def match_allocated_time(self, low, high, match):
        """Matches assessment parts hose allocated time falls in between the given times inclusive.

        :param low: low end of range
        :type low: ``osid.calendaring.Duration``
        :param high: high end of range
        :type high: ``osid.calendaring.Duration``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``high`` is less than ``low``

        """
        pass

    def match_any_allocated_time(self, match):
        """Matches assessment parts with any time assigned.

        :param match: ``true`` to match assessment parts with any alloocated time, ``false`` to match assessment parts with no allocated time
        :type match: ``boolean``

        """
        pass

    def clear_allocated_time_terms(self):
        """Clears all allocated time terms."""
        pass

    allocated_time_terms = property(fdel=clear_allocated_time_terms)

    def match_child_assessment_part_id(self, assessment_part_id, match):
        """Sets the assessment part ``Id`` for this query.

        :param assessment_part_id: an assessment part ``Id``
        :type assessment_part_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``

        """
        pass

    def clear_child_assessment_part_id_terms(self):
        """Clears all assessment part ``Id`` terms."""
        pass

    child_assessment_part_id_terms = property(fdel=clear_child_assessment_part_id_terms)

    def supports_child_assessment_part_query(self):
        """Tests if an ``AssessmentPartQuery`` is available.

        :return: ``true`` if an assessment part query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_child_assessment_part_query(self):
        """Gets the query for an assessment part.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment part query
        :rtype: ``osid.assessment.authoring.AssessmentPartQuery``
        :raise: ``Unimplemented`` -- ``supports_child_assessment_part_query()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartQuery

    child_assessment_part_query = property(fget=get_child_assessment_part_query)

    def match_any_child_assessment_part(self, match):
        """Matches assessment parts with any child assessment part.

        :param match: ``true`` to match assessment parts with any children, ``false`` to match assessment parts with no children
        :type match: ``boolean``

        """
        pass

    def clear_child_assessment_part_terms(self):
        """Clears all assessment part terms."""
        pass

    child_assessment_part_terms = property(fdel=clear_child_assessment_part_terms)

    def match_bank_id(self, bank_id, match):
        """Matches constrainers mapped to the bank.

        :param bank_id: the bank ``Id``
        :type bank_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        """
        pass

    def clear_bank_id_terms(self):
        """Clears the bank ``Id`` query terms."""
        pass

    bank_id_terms = property(fdel=clear_bank_id_terms)

    def supports_bank_query(self):
        """Tests if an ``BankQuery`` is available.

        :return: ``true`` if a bank query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_bank_query(self):
        """Gets the query for a bank.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the bank query
        :rtype: ``osid.assessment.BankQuery``
        :raise: ``Unimplemented`` -- ``supports_bank_query()`` is ``false``

        """
        return # osid.assessment.BankQuery

    bank_query = property(fget=get_bank_query)

    def clear_bank_terms(self):
        """Clears the bank query terms."""
        pass

    bank_terms = property(fdel=clear_bank_terms)

    def get_assessment_part_query_record(self, assessment_part_record_type):
        """Gets the assessment part query record corresponding to the given ``AssessmentPart`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param assessment_part_record_type: an assessment part record type
        :type assessment_part_record_type: ``osid.type.Type``
        :return: the assessment part query record
        :rtype: ``osid.assessment.authoring.records.AssessmentPartQueryRecord``
        :raise: ``NullArgument`` -- ``assessment_part_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(assessment_part_record_type)`` is ``false``

        """
        return # osid.assessment.authoring.records.AssessmentPartQueryRecord


class SequenceRuleQuery(osid_queries.OsidRuleQuery):
    """This is the query for searching sequence rules.

    Each method match specifies a ``AND`` term while multiple
    invocations of the same method produce a nested ``OR``.

    """
    def match_assessment_part_id(self, assessment_part_id, match):
        """Sets the assessment part ``Id`` for this query.

        :param assessment_part_id: an assessment part ``Id``
        :type assessment_part_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``

        """
        pass

    def clear_assessment_part_id_terms(self):
        """Clears all assessment part ``Id`` terms."""
        pass

    assessment_part_id_terms = property(fdel=clear_assessment_part_id_terms)

    def supports_assessment_part_query(self):
        """Tests if an ``AssessmentPartQuery`` is available.

        :return: ``true`` if an assessment part query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_assessment_part_query(self):
        """Gets the query for an assessment part.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment part query
        :rtype: ``osid.assessment.authoring.AssessmentPartQuery``
        :raise: ``Unimplemented`` -- ``supports_assessment_part_query()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartQuery

    assessment_part_query = property(fget=get_assessment_part_query)

    def clear_assessment_part_terms(self):
        """Clears all assessment part terms."""
        pass

    assessment_part_terms = property(fdel=clear_assessment_part_terms)

    def match_next_assessment_part_id(self, assessment_part_id, match):
        """Sets the assessment part ``Id`` for this query.

        :param assessment_part_id: an assessment part ``Id``
        :type assessment_part_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``

        """
        pass

    def clear_next_assessment_part_id_terms(self):
        """Clears all assessment part ``Id`` terms."""
        pass

    next_assessment_part_id_terms = property(fdel=clear_next_assessment_part_id_terms)

    def supports_next_assessment_part_query(self):
        """Tests if an ``AssessmentPartQuery`` is available.

        :return: ``true`` if an assessment part query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_next_assessment_part_query(self):
        """Gets the query for an assessment part.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment part query
        :rtype: ``osid.assessment.authoring.AssessmentPartQuery``
        :raise: ``Unimplemented`` -- ``supports_next_assessment_part_query()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartQuery

    next_assessment_part_query = property(fget=get_next_assessment_part_query)

    def clear_next_assessment_part_terms(self):
        """Clears all assessment part terms."""
        pass

    next_assessment_part_terms = property(fdel=clear_next_assessment_part_terms)

    def match_minimum_score(self, low, high, match):
        """Matches minimum scores that fall in between the given scores inclusive.

        :param low: low end of range
        :type low: ``cardinal``
        :param high: high end of range
        :type high: ``cardinal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``high`` is less than ``low``

        """
        pass

    def match_any_minimum_score(self, match):
        """Matches assessment parts with any minimum score assigned.

        :param match: ``true`` to match assessment parts with any minimum score, ``false`` to match assessment parts with no minimum score
        :type match: ``boolean``

        """
        pass

    def clear_minimum_score_terms(self):
        """Clears all minimum score terms."""
        pass

    minimum_score_terms = property(fdel=clear_minimum_score_terms)

    def match_maximum_score(self, low, high, match):
        """Matches maximum scores that fall in between the given scores inclusive.

        :param low: low end of range
        :type low: ``cardinal``
        :param high: high end of range
        :type high: ``cardinal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``high`` is less than ``low``

        """
        pass

    def match_any_maximum_score(self, match):
        """Matches assessment parts with any maximum score assigned.

        :param match: ``true`` to match assessment parts with any maximum score, ``false`` to match assessment parts with no maximum score
        :type match: ``boolean``

        """
        pass

    def clear_maximum_score_terms(self):
        """Clears all maximum score terms."""
        pass

    maximum_score_terms = property(fdel=clear_maximum_score_terms)

    def match_cumulative(self, match):
        """Matches cumulative rules.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def clear_cumulative_terms(self):
        """Clears all cumulative terms."""
        pass

    cumulative_terms = property(fdel=clear_cumulative_terms)

    def match_applied_assessment_part_id(self, assessment_part_id, match):
        """Sets the assessment part ``Id`` for this query.

        :param assessment_part_id: an assessment part ``Id``
        :type assessment_part_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``

        """
        pass

    def clear_applied_assessment_part_id_terms(self):
        """Clears all assessment part ``Id`` terms."""
        pass

    applied_assessment_part_id_terms = property(fdel=clear_applied_assessment_part_id_terms)

    def supports_applied_assessment_part_query(self):
        """Tests if an ``AssessmentPartQuery`` is available.

        :return: ``true`` if an assessment part query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_applied_assessment_part_query(self):
        """Gets the query for an assessment part.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the assessment part query
        :rtype: ``osid.assessment.authoring.AssessmentPartQuery``
        :raise: ``Unimplemented`` -- ``supports_applied_assessment_part_query()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartQuery

    applied_assessment_part_query = property(fget=get_applied_assessment_part_query)

    def match_any_applied_assessment_part(self, match):
        """Matches assessment parts with any applied assessment part.

        :param match: ``true`` to match assessment parts with any applied assessment part, ``false`` to match assessment parts with no applied assessment parts
        :type match: ``boolean``

        """
        pass

    def clear_applied_assessment_part_terms(self):
        """Clears all assessment part terms."""
        pass

    applied_assessment_part_terms = property(fdel=clear_applied_assessment_part_terms)

    def match_bank_id(self, bank_id, match):
        """Matches constrainers mapped to the bank.

        :param bank_id: the bank ``Id``
        :type bank_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        """
        pass

    def clear_bank_id_terms(self):
        """Clears the bank ``Id`` query terms."""
        pass

    bank_id_terms = property(fdel=clear_bank_id_terms)

    def supports_bank_query(self):
        """Tests if an ``BankQuery`` is available.

        :return: ``true`` if a bank query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_bank_query(self):
        """Gets the query for a bank.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the bank query
        :rtype: ``osid.assessment.BankQuery``
        :raise: ``Unimplemented`` -- ``supports_bank_query()`` is ``false``

        """
        return # osid.assessment.BankQuery

    bank_query = property(fget=get_bank_query)

    def clear_bank_terms(self):
        """Clears the bank query terms."""
        pass

    bank_terms = property(fdel=clear_bank_terms)

    def get_sequence_rule_query_record(self, sequence_rule_record_type):
        """Gets the sequence rule query record corresponding to the given ``SequenceRule`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param sequence_rule_record_type: a sequence rule record type
        :type sequence_rule_record_type: ``osid.type.Type``
        :return: the sequence rule query record
        :rtype: ``osid.assessment.authoring.records.SequenceRuleQueryRecord``
        :raise: ``NullArgument`` -- ``sequence_rule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(sequence_rule_record_type)`` is ``false``

        """
        return # osid.assessment.authoring.records.SequenceRuleQueryRecord


class SequenceRuleEnablerQuery(osid_queries.OsidEnablerQuery):
    """This is the query for searching sequence rule enablers.

    Each method match specifies a ``AND`` term while multiple
    invocations of the same method produce a nested ``OR``.

    """
    def match_ruled_sequence_rule_id(self, sequence_rule_id, match):
        """Matches enablers mapped to the sequence rule.

        :param sequence_rule_id: the sequence rule ``Id``
        :type sequence_rule_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``

        """
        pass

    def clear_ruled_sequence_rule_id_terms(self):
        """Clears the sequence rule ``Id`` query terms."""
        pass

    ruled_sequence_rule_id_terms = property(fdel=clear_ruled_sequence_rule_id_terms)

    def supports_ruled_sequence_rule_query(self):
        """Tests if a ``SequenceRuleQuery`` is available.

        :return: ``true`` if a sequence rule query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_ruled_sequence_rule_query(self):
        """Gets the query for a sequence rule.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the sequence rule query
        :rtype: ``osid.assessment.authoring.SequenceRuleQuery``
        :raise: ``Unimplemented`` -- ``supports_ruled_sequence_rule_query()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleQuery

    ruled_sequence_rule_query = property(fget=get_ruled_sequence_rule_query)

    def match_any_ruled_sequence_rule(self, match):
        """Matches enablers mapped to any sequence rule.

        :param match: ``true`` for enablers mapped to any sequence rule, ``false`` to match enablers mapped to no sequence rules
        :type match: ``boolean``

        """
        pass

    def clear_ruled_sequence_rule_terms(self):
        """Clears the sequence rule query terms."""
        pass

    ruled_sequence_rule_terms = property(fdel=clear_ruled_sequence_rule_terms)

    def match_bank_id(self, bank_id, match):
        """Matches enablers mapped to the bank.

        :param bank_id: the bank ``Id``
        :type bank_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        """
        pass

    def clear_bank_id_terms(self):
        """Clears the bank ``Id`` query terms."""
        pass

    bank_id_terms = property(fdel=clear_bank_id_terms)

    def supports_bank_query(self):
        """Tests if an ``BankQuery`` is available.

        :return: ``true`` if a bank query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_bank_query(self):
        """Gets the query for a bank.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the bank query
        :rtype: ``osid.assessment.BankQuery``
        :raise: ``Unimplemented`` -- ``supports_bank_query()`` is ``false``

        """
        return # osid.assessment.BankQuery

    bank_query = property(fget=get_bank_query)

    def clear_bank_terms(self):
        """Clears the bank query terms."""
        pass

    bank_terms = property(fdel=clear_bank_terms)

    def get_sequence_rule_enabler_query_record(self, sequence_rule_enabler_record_type):
        """Gets the sequence rule enabler query record corresponding to the given ``SequenceRuleEnabler`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param sequence_rule_enabler_record_type: a sequence rule enabler record type
        :type sequence_rule_enabler_record_type: ``osid.type.Type``
        :return: the sequence rule enabler query record
        :rtype: ``osid.assessment.authoring.records.SequenceRuleEnablerQueryRecord``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(sequence_rule_enabler_record_type)`` is ``false``

        """
        return # osid.assessment.authoring.records.SequenceRuleEnablerQueryRecord


