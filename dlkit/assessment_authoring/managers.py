
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class AssessmentAuthoringProfile(osid_managers.OsidProfile):
    """The ``AssessmentAuthoringProfile`` describes the interoperability among assessment authoring services."""

    def supports_assessment_part_lookup(self):
        """Tests if looking up assessment part is supported.

        :return: ``true`` if assessment part lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_assessment_part_query(self):
        """Tests if querying assessment part is supported.

        :return: ``true`` if assessment part query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_assessment_part_admin(self):
        """Tests if an assessment part administrative service is supported.

        :return: ``true`` if assessment part administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_assessment_part_item(self):
        """Tests if an assessment part item service is supported for looking up assessment part and item mappings.

        :return: ``true`` if assessment part item service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_assessment_part_item_design(self):
        """Tests if an assessment part item design session is supported.

        :return: ``true`` if an assessment part item design service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_sequence_rule_lookup(self):
        """Tests if looking up sequence rule is supported.

        :return: ``true`` if sequence rule lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_sequence_rule_admin(self):
        """Tests if a sequence rule administrative service is supported.

        :return: ``true`` if sequence rule administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_assessment_part_record_types(self):
        """Gets the supported ``AssessmentPart`` record types.

        :return: a list containing the supported ``AssessmentPart`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    assessment_part_record_types = property(fget=get_assessment_part_record_types)

    def get_assessment_part_search_record_types(self):
        """Gets the supported ``AssessmentPart`` search record types.

        :return: a list containing the supported ``AssessmentPart`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    assessment_part_search_record_types = property(fget=get_assessment_part_search_record_types)

    def get_sequence_rule_record_types(self):
        """Gets the supported ``SequenceRule`` record types.

        :return: a list containing the supported ``SequenceRule`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    sequence_rule_record_types = property(fget=get_sequence_rule_record_types)

    def get_sequence_rule_search_record_types(self):
        """Gets the supported ``SequenceRule`` search record types.

        :return: a list containing the supported ``SequenceRule`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    sequence_rule_search_record_types = property(fget=get_sequence_rule_search_record_types)

    def get_sequence_rule_enabler_record_types(self):
        """Gets the supported ``SequenceRuleEnabler`` record types.

        :return: a list containing the supported ``SequenceRuleEnabler`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    sequence_rule_enabler_record_types = property(fget=get_sequence_rule_enabler_record_types)

    def get_sequence_rule_enabler_search_record_types(self):
        """Gets the supported ``SequenceRuleEnabler`` search record types.

        :return: a list containing the supported ``SequenceRuleEnabler`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    sequence_rule_enabler_search_record_types = property(fget=get_sequence_rule_enabler_search_record_types)


class AssessmentAuthoringManager(osid_managers.OsidManager, osid_sessions.OsidSession, AssessmentAuthoringProfile):
    """The assessment authoring manager provides access to assessment authoring sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``AssessmentPartLookupSession:`` a session to retrieve
        assessment part
      * ``AssessmentPartQuerySession:`` a session to query for
        assessment part
      * ``AssessmentPartSearchSession:`` a session to search for
        assessment part
      * ``AssessmentPartAdminSession:`` a session to create and delete
        assessment part
      * ``AssessmentPartNotificationSession:`` a session to receive
        notifications pertaining to assessment part changes
      * ``AssessmentPartBankSession:`` a session to look up assessment
        part bank mappings
      * ``AssessmentPartBankAssignmentSession:`` a session to manage
        assessment part to bank mappings
      * ``AssessmentPartSmartBankSession:`` a session to manage dynamic
        bank of assessment part
      * ``AssessmentPartItemSession:`` a session to look up assessment
        part to item mappings
      * ``AssessmentPartItemDesignSession:`` a session to map items to
        assessment parts

      * ``SequenceRuleLookupSession:`` a session to retrieve sequence
        rule
      * ``SequenceRuleQuerySession:`` a session to query for sequence
        rule
      * ``SequenceRuleSearchSession:`` a session to search for sequence
        rule
      * ``SequenceRuleAdminSession:`` a session to create and delete
        sequence rule
      * ``SequenceRuleNotificationSession:`` a session to receive
        notifications pertaining to sequence rule changes
      * ``SequenceRuleBankSession:`` a session to look up sequence rule
        bank mappings
      * ``SequenceRuleBankAssignmentSession:`` a session to manage
        sequence rule to bank mappings
      * ``SequenceRuleSmartBankSession:`` a session to manage dynamic
        bank of sequence rule

      * ``SequenceRuleEnablerLookupSession:`` a session to retrieve
        sequence rule enablers
      * ``SequenceRuleEnablerQuerySession:`` a session to query for
        sequence rule enablers
      * ``SequenceRuleEnablerSearchSession:`` a session to search for
        sequence rule enablers
      * ``SequenceRuleEnablerAdminSession:`` a session to create and
        delete sequence rule enablers
      * ``SequenceRuleEnablerNotificationSession:`` a session to receive
        notifications pertaining to sequence rule enabler changes
      * ``SequenceRuleEnablerBankSession:`` a session to look up
        sequence rule enabler bank mappings
      * ``SequenceRuleEnablerBankAssignmentSession:`` a session to
        manage sequence rule enabler to bank mappings
      * ``SequenceRuleEnablerSmartBankSession:`` a session to manage
        dynamic bank of sequence rule enablers
      * ``SequenceRuleEnableRuleLookupSession:`` a session to look up
        sequence rule enabler mappings
      * ``SequenceRuleEnablerRuleApplicationSession:`` a session to
        apply sequence rule enablers

    """




class AssessmentAuthoringProxyManager(osid_managers.OsidProxyManager, AssessmentAuthoringProfile):
    """The assessment authoring manager provides access to assessment authoring sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` object.
    The sessions included in this manager are:

      * ``AssessmentPartLookupSession:`` a session to retrieve
        assessment part
      * ``AssessmentPartQuerySession:`` a session to query for
        assessment part
      * ``AssessmentPartSearchSession:`` a session to search for
        assessment part
      * ``AssessmentPartAdminSession:`` a session to create and delete
        assessment part
      * ``AssessmentPartNotificationSession:`` a session to receive
        notifications pertaining to assessment part changes
      * ``AssessmentPartBankSession:`` a session to look up assessment
        part bank mappings
      * ``AssessmentPartBankAssignmentSession:`` a session to manage
        assessment part to bank mappings
      * ``AssessmentPartSmartBankSession:`` a session to manage dynamic
        bank of assessment part
      * ``AssessmentPartItemSession:`` a session to look up assessment
        part to item mappings
      * ``AssessmentPartItemDesignSession:`` a session to map items to
        assessment parts

      * ``SequenceRuleLookupSession:`` a session to retrieve sequence
        rule
      * ``SequenceRuleQuerySession:`` a session to query for sequence
        rule
      * ``SequenceRuleSearchSession:`` a session to search for sequence
        rule
      * ``SequenceRuleAdminSession:`` a session to create and delete
        sequence rule
      * ``SequenceRuleNotificationSession:`` a session to receive
        notifications pertaining to sequence rule changes
      * ``SequenceRuleBankSession:`` a session to look up sequence rule
        bank mappings
      * ``SequenceRuleBankAssignmentSession:`` a session to manage
        sequence rule to bank mappings
      * ``SequenceRuleSmartBankSession:`` a session to manage dynamic
        bank of sequence rule

      * ``SequenceRuleEnablerLookupSession:`` a session to retrieve
        sequence rule enablers
      * ``SequenceRuleEnablerQuerySession:`` a session to query for
        sequence rule enablers
      * ``SequenceRuleEnablerSearchSession:`` a session to search for
        sequence rule enablers
      * ``SequenceRuleEnablerAdminSession:`` a session to create and
        delete sequence rule enablers
      * ``SequenceRuleEnablerNotificationSession:`` a session to receive
        notifications pertaining to sequence rule enabler changes
      * ``SequenceRuleEnablerBankSession:`` a session to look up
        sequence rule enabler bank mappings
      * ``SequenceRuleEnablerBankAssignmentSession:`` a session to
        manage sequence rule enabler to bank mappings
      * ``SequenceRuleEnablerSmartBankSession:`` a session to manage
        dynamic bank of sequence rule enablers
      * ``SequenceRuleEnableRuleLookupSession:`` a session to look up
        sequence rule enabler mappings
      * ``SequenceRuleEnablerRuleApplicationSession:`` a session to
        apply sequence rule enablers

    """




