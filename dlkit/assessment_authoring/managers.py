from ..osid import managers as osid_managers


class AssessmentAuthoringProfile(osid_managers.OsidProfile):
    """The ``AssessmentAuthoringProfile`` describes the interoperability among assessment authoring services."""
    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_part_lookup(self):
        """Tests if looking up assessment part is supported.

        :return: ``true`` if assessment part lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_part_query(self):
        """Tests if querying assessment part is supported.

        :return: ``true`` if assessment part query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_part_search(self):
        """Tests if searching assessment part is supported.

        :return: ``true`` if assessment part search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_part_admin(self):
        """Tests if an assessment part administrative service is supported.

        :return: ``true`` if assessment part administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_part_notification(self):
        """Tests if an assessment part notification service is supported.

        :return: ``true`` if assessment part notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_part_bank(self):
        """Tests if an assessment part bank lookup service is supported.

        :return: ``true`` if an assessment part bank lookup service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_part_bank_assignment(self):
        """Tests if an assessment part bank service is supported.

        :return: ``true`` if assessment part bank assignment service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_part_smart_bank(self):
        """Tests if an assessment part bank lookup service is supported.

        :return: ``true`` if an assessment part bank service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_part_item(self):
        """Tests if an assessment part item service is supported for looking up assessment part and item mappings.

        :return: ``true`` if assessment part item service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_part_item_design(self):
        """Tests if an assessment part item design session is supported.

        :return: ``true`` if an assessment part item design service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_lookup(self):
        """Tests if looking up sequence rule is supported.

        :return: ``true`` if sequence rule lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_query(self):
        """Tests if querying sequence rule is supported.

        :return: ``true`` if sequence rule query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_search(self):
        """Tests if searching sequence rule is supported.

        :return: ``true`` if sequence rule search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_admin(self):
        """Tests if a sequence rule administrative service is supported.

        :return: ``true`` if sequence rule administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_notification(self):
        """Tests if a sequence rule notification service is supported.

        :return: ``true`` if sequence rule notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_bank(self):
        """Tests if a sequence rule bank lookup service is supported.

        :return: ``true`` if a sequence rule bank lookup service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_bank_assignment(self):
        """Tests if a sequence rule bank service is supported.

        :return: ``true`` if sequence rule bank assignment service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_smart_bank(self):
        """Tests if a sequence rule bank lookup service is supported.

        :return: ``true`` if a sequence rule bank service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_enabler_lookup(self):
        """Tests if looking up sequence rule enablers is supported.

        :return: ``true`` if sequence rule enabler lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_enabler_query(self):
        """Tests if querying sequence rule enablers is supported.

        :return: ``true`` if sequence rule enabler query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_enabler_search(self):
        """Tests if searching sequence rule enablers is supported.

        :return: ``true`` if sequence rule enabler search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_enabler_admin(self):
        """Tests if a sequence rule enabler administrative service is supported.

        :return: ``true`` if sequence rule enabler administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_enabler_notification(self):
        """Tests if a sequence rule enabler notification service is supported.

        :return: ``true`` if sequence rule enabler notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_enabler_bank(self):
        """Tests if a sequence rule enabler bank lookup service is supported.

        :return: ``true`` if a sequence rule enabler bank lookup service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_enabler_bank_assignment(self):
        """Tests if a sequence rule enabler bank service is supported.

        :return: ``true`` if sequence rule enabler bank assignment service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_enabler_smart_bank(self):
        """Tests if a sequence rule enabler bank lookup service is supported.

        :return: ``true`` if a sequence rule enabler bank service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_enabler_rule_lookup(self):
        """Tests if a sequence rule enabler rule lookup service is supported.

        :return: ``true`` if a sequence rule enabler rule lookup service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_sequence_rule_enabler_rule_application(self):
        """Tests if a sequence rule enabler rule application service is supported.

        :return: ``true`` if sequence rule enabler rule application service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_assessment_part_record_types(self):
        """Gets the supported ``AssessmentPart`` record types.

        :return: a list containing the supported ``AssessmentPart`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    assessment_part_record_types = property(fget=get_assessment_part_record_types)

    def supports_assessment_part_record_type(self, assessment_part_record_type):
        """Tests if the given ``AssessmentPart`` record type is supported.

        :param assessment_part_record_type: a ``Type`` indicating an ``AssessmentPart`` record type
        :type assessment_part_record_type: ``osid.type.Type``
        :return: ``true`` if the given record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_part_record_type`` is ``null``

        """
        return # boolean

    def get_assessment_part_search_record_types(self):
        """Gets the supported ``AssessmentPart`` search record types.

        :return: a list containing the supported ``AssessmentPart`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    assessment_part_search_record_types = property(fget=get_assessment_part_search_record_types)

    def supports_assessment_part_search_record_type(self, assessment_part_search_record_type):
        """Tests if the given ``AssessmentPart`` search record type is supported.

        :param assessment_part_search_record_type: a ``Type`` indicating an ``AssessmentPart`` search record type
        :type assessment_part_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_part_search_record_type`` is ``null``

        """
        return # boolean

    def get_sequence_rule_record_types(self):
        """Gets the supported ``SequenceRule`` record types.

        :return: a list containing the supported ``SequenceRule`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    sequence_rule_record_types = property(fget=get_sequence_rule_record_types)

    def supports_sequence_rule_record_type(self, sequence_rule_record_type):
        """Tests if the given ``SequenceRule`` record type is supported.

        :param sequence_rule_record_type: a ``Type`` indicating a ``SequenceRule`` record type
        :type sequence_rule_record_type: ``osid.type.Type``
        :return: ``true`` if the given record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``sequence_rule_record_type`` is ``null``

        """
        return # boolean

    def get_sequence_rule_search_record_types(self):
        """Gets the supported ``SequenceRule`` search record types.

        :return: a list containing the supported ``SequenceRule`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    sequence_rule_search_record_types = property(fget=get_sequence_rule_search_record_types)

    def supports_sequence_rule_search_record_type(self, sequence_rule_search_record_type):
        """Tests if the given ``SequenceRule`` search record type is supported.

        :param sequence_rule_search_record_type: a ``Type`` indicating a ``SequenceRule`` search record type
        :type sequence_rule_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``sequence_rule_search_record_type`` is ``null``

        """
        return # boolean

    def get_sequence_rule_enabler_record_types(self):
        """Gets the supported ``SequenceRuleEnabler`` record types.

        :return: a list containing the supported ``SequenceRuleEnabler`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    sequence_rule_enabler_record_types = property(fget=get_sequence_rule_enabler_record_types)

    def supports_sequence_rule_enabler_record_type(self, sequence_rule_enabler_record_type):
        """Tests if the given ``SequenceRuleEnabler`` record type is supported.

        :param sequence_rule_enabler_record_type: a ``Type`` indicating a ``SequenceRuleEnabler`` record type
        :type sequence_rule_enabler_record_type: ``osid.type.Type``
        :return: ``true`` if the given record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_record_type`` is ``null``

        """
        return # boolean

    def get_sequence_rule_enabler_search_record_types(self):
        """Gets the supported ``SequenceRuleEnabler`` search record types.

        :return: a list containing the supported ``SequenceRuleEnabler`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    sequence_rule_enabler_search_record_types = property(fget=get_sequence_rule_enabler_search_record_types)

    def supports_sequence_rule_enabler_search_record_type(self, sequence_rule_enabler_search_record_type):
        """Tests if the given ``SequenceRuleEnabler`` search record type is supported.

        :param sequence_rule_enabler_search_record_type: a ``Type`` indicating a ``SequenceRuleEnabler`` search record type
        :type sequence_rule_enabler_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_search_record_type`` is ``null``

        """
        return # boolean


class AssessmentAuthoringManager(osid_managers.OsidManager, AssessmentAuthoringProfile):
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
    def get_assessment_part_lookup_session(self):
        """Gets the ``OsidSession`` associated with the assessment part lookup service.

        :return: an ``AssessmentPartLookupSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_lookup()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartLookupSession

    assessment_part_lookup_session = property(fget=get_assessment_part_lookup_session)

    def get_assessment_part_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment part lookup service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentPartLookupSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartLookupSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartLookupSession

    def get_assessment_part_query_session(self):
        """Gets the ``OsidSession`` associated with the assessment part query service.

        :return: an ``AssessmentPartQuerySession``
        :rtype: ``osid.assessment.authoring.AssessmentPartQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_query()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartQuerySession

    assessment_part_query_session = property(fget=get_assessment_part_query_session)

    def get_assessment_part_query_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment part query service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentPartQuerySession``
        :rtype: ``osid.assessment.authoring.AssessmentPartQuerySession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartQuerySession

    def get_assessment_part_search_session(self):
        """Gets the ``OsidSession`` associated with the assessment part search service.

        :return: an ``AssessmentPartSearchSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_search()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartSearchSession

    assessment_part_search_session = property(fget=get_assessment_part_search_session)

    def get_assessment_part_search_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment part earch service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentPartSearchSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartSearchSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartSearchSession

    def get_assessment_part_admin_session(self):
        """Gets the ``OsidSession`` associated with the assessment part administration service.

        :return: an ``AssessmentPartAdminSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_admin()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartAdminSession

    assessment_part_admin_session = property(fget=get_assessment_part_admin_session)

    def get_assessment_part_admin_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment part administration service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentPartAdminSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartAdminSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartAdminSession

    def get_assessment_part_notification_session(self, assessment_part_receiver):
        """Gets the ``OsidSession`` associated with the assessment part notification service.

        :param assessment_part_receiver: the notification callback
        :type assessment_part_receiver: ``osid.assessment.authoring.AssessmentPartReceiver``
        :return: an ``AssessmentPartNotificationSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartNotificationSession``
        :raise: ``NullArgument`` -- ``assessment_part_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_notification()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartNotificationSession

    def get_assessment_part_notification_session_for_bank(self, assessment_part_receiver, bank_id):
        """Gets the ``OsidSession`` associated with the assessment part notification service for the given bank.

        :param assessment_part_receiver: the notification callback
        :type assessment_part_receiver: ``osid.assessment.authoring.AssessmentPartReceiver``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentPartNotificationSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartNotificationSession``
        :raise: ``NotFound`` -- no bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``assessment_part_receiver`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartNotificationSession

    def get_assessment_part_bank_session(self):
        """Gets the ``OsidSession`` to lookup assessment part/bank mappings for assessment parts.

        :return: an ``AssessmentPartBankSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartBankSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_bank()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartBankSession

    assessment_part_bank_session = property(fget=get_assessment_part_bank_session)

    def get_assessment_part_bank_assignment_session(self):
        """Gets the ``OsidSession`` associated with assigning assessment part to bank.

        :return: an ``AssessmentPartBankAssignmentSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartBankAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_bank_assignment()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartBankAssignmentSession

    assessment_part_bank_assignment_session = property(fget=get_assessment_part_bank_assignment_session)

    def get_assessment_part_smart_bank_session(self, bank_id):
        """Gets the ``OsidSession`` to manage assessment part smart bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentPartSmartBankSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartSmartBankSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_smart_bank()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartSmartBankSession

    def get_sequence_rule_lookup_session(self):
        """Gets the ``OsidSession`` associated with the sequence rule lookup service.

        :return: a ``SequenceRuleLookupSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_lookup()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleLookupSession

    sequence_rule_lookup_session = property(fget=get_sequence_rule_lookup_session)

    def get_sequence_rule_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the sequence rule lookup service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: a ``SequenceRuleLookupSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleLookupSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleLookupSession

    def get_sequence_rule_query_session(self):
        """Gets the ``OsidSession`` associated with the sequence rule query service.

        :return: a ``SequenceRuleQuerySession``
        :rtype: ``osid.assessment.authoring.SequenceRuleQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_query()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleQuerySession

    sequence_rule_query_session = property(fget=get_sequence_rule_query_session)

    def get_sequence_rule_query_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the sequence rule query service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: a ``SequenceRuleQuerySession``
        :rtype: ``osid.assessment.authoring.SequenceRuleQuerySession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleQuerySession

    def get_sequence_rule_search_session(self):
        """Gets the ``OsidSession`` associated with the sequence rule search service.

        :return: a ``SequenceRuleSearchSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_search()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleSearchSession

    sequence_rule_search_session = property(fget=get_sequence_rule_search_session)

    def get_sequence_rule_search_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the sequence rule earch service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: a ``SequenceRuleSearchSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleSearchSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleSearchSession

    def get_sequence_rule_admin_session(self):
        """Gets the ``OsidSession`` associated with the sequence rule administration service.

        :return: a ``SequenceRuleAdminSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_admin()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleAdminSession

    sequence_rule_admin_session = property(fget=get_sequence_rule_admin_session)

    def get_sequence_rule_admin_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the sequence rule administration service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: a ``SequenceRuleAdminSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleAdminSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleAdminSession

    def get_sequence_rule_notification_session(self, sequence_rule_receiver):
        """Gets the ``OsidSession`` associated with the sequence rule notification service.

        :param sequence_rule_receiver: the notification callback
        :type sequence_rule_receiver: ``osid.assessment.authoring.SequenceRuleReceiver``
        :return: a ``SequenceRuleNotificationSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleNotificationSession``
        :raise: ``NullArgument`` -- ``sequence_rule_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_notification()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleNotificationSession

    def get_sequence_rule_notification_session_for_bank(self, sequence_rule_receiver, bank_id):
        """Gets the ``OsidSession`` associated with the sequence rule notification service for the given bank.

        :param sequence_rule_receiver: the notification callback
        :type sequence_rule_receiver: ``osid.assessment.authoring.SequenceRuleReceiver``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: a ``SequenceRuleNotificationSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleNotificationSession``
        :raise: ``NotFound`` -- no bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``sequence_rule_receiver`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleNotificationSession

    def get_sequence_rule_bank_session(self):
        """Gets the ``OsidSession`` to lookup sequence rule/bank mappings for sequence rules.

        :return: a ``SequenceRuleBankSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleBankSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_bank()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleBankSession

    sequence_rule_bank_session = property(fget=get_sequence_rule_bank_session)

    def get_sequence_rule_bank_assignment_session(self):
        """Gets the ``OsidSession`` associated with assigning sequence rule to bank.

        :return: a ``SequenceRuleBankAssignmentSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleBankAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_bank_assignment()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleBankAssignmentSession

    sequence_rule_bank_assignment_session = property(fget=get_sequence_rule_bank_assignment_session)

    def get_sequence_rule_smart_bank_session(self, bank_id):
        """Gets the ``OsidSession`` to manage sequence rule smart bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: a ``SequenceRuleSmartBankSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleSmartBankSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_smart_bank()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleSmartBankSession

    def get_sequence_rule_enabler_lookup_session(self):
        """Gets the ``OsidSession`` associated with the sequence rule enabler lookup service.

        :return: a ``SequenceRuleEnablerLookupSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_lookup()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerLookupSession

    sequence_rule_enabler_lookup_session = property(fget=get_sequence_rule_enabler_lookup_session)

    def get_sequence_rule_enabler_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the sequence rule enabler lookup service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: a ``SequenceRuleEnablerLookupSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerLookupSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerLookupSession

    def get_sequence_rule_enabler_query_session(self):
        """Gets the ``OsidSession`` associated with the sequence rule enabler query service.

        :return: a ``SequenceRuleEnablerQuerySession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_query()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerQuerySession

    sequence_rule_enabler_query_session = property(fget=get_sequence_rule_enabler_query_session)

    def get_sequence_rule_enabler_query_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the sequence rule enabler query service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: a ``SequenceRuleEnablerQuerySession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerQuerySession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerQuerySession

    def get_sequence_rule_enabler_search_session(self):
        """Gets the ``OsidSession`` associated with the sequence rule enabler search service.

        :return: a ``SequenceRuleEnablerSearchSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_search()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerSearchSession

    sequence_rule_enabler_search_session = property(fget=get_sequence_rule_enabler_search_session)

    def get_sequence_rule_enabler_search_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the sequence rule enablers earch service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: a ``SequenceRuleEnablerSearchSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerSearchSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerSearchSession

    def get_sequence_rule_enabler_admin_session(self):
        """Gets the ``OsidSession`` associated with the sequence rule enabler administration service.

        :return: a ``SequenceRuleEnablerAdminSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_admin()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerAdminSession

    sequence_rule_enabler_admin_session = property(fget=get_sequence_rule_enabler_admin_session)

    def get_sequence_rule_enabler_admin_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the sequence rule enabler administration service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: a ``SequenceRuleEnablerAdminSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerAdminSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerAdminSession

    def get_sequence_rule_enabler_notification_session(self, sequence_rule_enabler_receiver):
        """Gets the ``OsidSession`` associated with the sequence rule enabler notification service.

        :param sequence_rule_enabler_receiver: the notification callback
        :type sequence_rule_enabler_receiver: ``osid.assessment.authoring.SequenceRuleEnablerReceiver``
        :return: a ``SequenceRuleEnablerNotificationSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerNotificationSession``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_notification()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerNotificationSession

    def get_sequence_rule_enabler_notification_session_for_bank(self, sequence_rule_enabler_receiver, bank_id):
        """Gets the ``OsidSession`` associated with the sequence rule enabler notification service for the given bank.

        :param sequence_rule_enabler_receiver: the notification callback
        :type sequence_rule_enabler_receiver: ``osid.assessment.authoring.SequenceRuleEnablerReceiver``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: a ``SequenceRuleEnablerNotificationSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerNotificationSession``
        :raise: ``NotFound`` -- no bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_receiver`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerNotificationSession

    def get_sequence_rule_enabler_bank_session(self):
        """Gets the ``OsidSession`` to lookup sequence rule enabler/bank mappings for sequence rule enablers.

        :return: a ``SequenceRuleEnablerBankSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerBankSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_bank()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerBankSession

    sequence_rule_enabler_bank_session = property(fget=get_sequence_rule_enabler_bank_session)

    def get_sequence_rule_enabler_bank_assignment_session(self):
        """Gets the ``OsidSession`` associated with assigning sequence rule enablers to bank.

        :return: a ``SequenceRuleEnablerBankAssignmentSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerBankAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_bank_assignment()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerBankAssignmentSession

    sequence_rule_enabler_bank_assignment_session = property(fget=get_sequence_rule_enabler_bank_assignment_session)

    def get_sequence_rule_enabler_smart_bank_session(self, bank_id):
        """Gets the ``OsidSession`` to manage sequence rule enabler smart bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: a ``SequenceRuleEnablerSmartBankSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerSmartBankSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_smart_bank()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerSmartBankSession

    def get_sequence_rule_enabler_rule_lookup_session(self):
        """Gets the ``OsidSession`` associated with the sequence rule enabler mapping lookup service.

        :return: a ``SequenceRuleEnablerRuleLookupSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerRuleLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_rule_lookup()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerRuleLookupSession

    sequence_rule_enabler_rule_lookup_session = property(fget=get_sequence_rule_enabler_rule_lookup_session)

    def get_sequence_rule_enabler_rule_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the sequence rule enabler mapping lookup service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: a ``SequenceRuleEnablerRuleLookupSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerRuleLookupSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_rule_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerRuleLookupSession

    def get_sequence_rule_enabler_rule_application_session(self):
        """Gets the ``OsidSession`` associated with the sequence rule enabler assignment service.

        :return: a ``SequenceRuleEnablerRuleApplicationSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerRuleApplicationSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_rule_application()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerRuleApplicationSession

    sequence_rule_enabler_rule_application_session = property(fget=get_sequence_rule_enabler_rule_application_session)

    def get_sequence_rule_enabler_rule_application_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the sequence rule enabler assignment service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: a ``SequenceRuleEnablerRuleApplicationSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerRuleApplicationSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_rule_application()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerRuleApplicationSession


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
    def get_assessment_part_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment part lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentPartLookupSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_lookup()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartLookupSession

    def get_assessment_part_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment part lookup service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentPartLookupSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartLookupSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartLookupSession

    def get_assessment_part_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment part query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentPartQuerySession``
        :rtype: ``osid.assessment.authoring.AssessmentPartQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_query()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartQuerySession

    def get_assessment_part_query_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment part query service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentPartQuerySession``
        :rtype: ``osid.assessment.authoring.AssessmentPartQuerySession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartQuerySession

    def get_assessment_part_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment part search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentPartSearchSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_search()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartSearchSession

    def get_assessment_part_search_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment part earch service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentPartSearchSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartSearchSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartSearchSession

    def get_assessment_part_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment part administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentPartAdminSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_admin()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartAdminSession

    def get_assessment_part_admin_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment part administration service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentPartAdminSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartAdminSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartAdminSession

    def get_assessment_part_notification_session(self, assessment_part_receiver, proxy):
        """Gets the ``OsidSession`` associated with the assessment part notification service.

        :param assessment_part_receiver: the notification callback
        :type assessment_part_receiver: ``osid.assessment.authoring.AssessmentPartReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentPartNotificationSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartNotificationSession``
        :raise: ``NullArgument`` -- ``assessment_part_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_notification()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartNotificationSession

    def get_assessment_part_notification_session_for_bank(self, assessment_part_receiver, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment part notification service for the given bank.

        :param assessment_part_receiver: the notification callback
        :type assessment_part_receiver: ``osid.assessment.authoring.AssessmentPartReceiver``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentPartNotificationSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartNotificationSession``
        :raise: ``NotFound`` -- no bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``assessment_part_receiver, bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartNotificationSession

    def get_assessment_part_bank_session(self, proxy):
        """Gets the ``OsidSession`` to lookup assessment part/bank mappings for assessment parts.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentPartBankSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartBankSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_bank()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartBankSession

    def get_assessment_part_bank_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with assigning assessment part to bank.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentPartBankAssignmentSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartBankAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_bank_assignment()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartBankAssignmentSession

    def get_assessment_part_smart_bank_session(self, bank_id, proxy):
        """Gets the ``OsidSession`` to manage assessment part smart bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentPartSmartBankSession``
        :rtype: ``osid.assessment.authoring.AssessmentPartSmartBankSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_part_smart_bank()`` is ``false``

        """
        return # osid.assessment.authoring.AssessmentPartSmartBankSession

    def get_sequence_rule_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleLookupSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_lookup()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleLookupSession

    def get_sequence_rule_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule lookup service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleLookupSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleLookupSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleLookupSession

    def get_sequence_rule_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleQuerySession``
        :rtype: ``osid.assessment.authoring.SequenceRuleQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_query()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleQuerySession

    def get_sequence_rule_query_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule query service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleQuerySession``
        :rtype: ``osid.assessment.authoring.SequenceRuleQuerySession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleQuerySession

    def get_sequence_rule_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleSearchSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_search()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleSearchSession

    def get_sequence_rule_search_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule earch service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleSearchSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleSearchSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleSearchSession

    def get_sequence_rule_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleAdminSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_admin()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleAdminSession

    def get_sequence_rule_admin_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule administration service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleAdminSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleAdminSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleAdminSession

    def get_sequence_rule_notification_session(self, sequence_rule_receiver, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule notification service.

        :param sequence_rule_receiver: the notification callback
        :type sequence_rule_receiver: ``osid.assessment.authoring.SequenceRuleReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleNotificationSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleNotificationSession``
        :raise: ``NullArgument`` -- ``sequence_rule_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_notification()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleNotificationSession

    def get_sequence_rule_notification_session_for_bank(self, sequence_rule_receiver, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule notification service for the given bank.

        :param sequence_rule_receiver: the notification callback
        :type sequence_rule_receiver: ``osid.assessment.authoring.SequenceRuleReceiver``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleNotificationSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleNotificationSession``
        :raise: ``NotFound`` -- no bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``sequence_rule_receiver, bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleNotificationSession

    def get_sequence_rule_bank_session(self, proxy):
        """Gets the ``OsidSession`` to lookup sequence rule/bank mappings for sequence rules.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleBankSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleBankSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_bank()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleBankSession

    def get_sequence_rule_bank_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with assigning sequence rule to bank.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleBankAssignmentSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleBankAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_bank_assignment()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleBankAssignmentSession

    def get_sequence_rule_smart_bank_session(self, bank_id, proxy):
        """Gets the ``OsidSession`` to manage sequence rule smart bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleSmartBankSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleSmartBankSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_smart_bank()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleSmartBankSession

    def get_sequence_rule_enabler_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule enabler lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleEnablerLookupSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_lookup()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerLookupSession

    def get_sequence_rule_enabler_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule enabler lookup service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleEnablerLookupSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerLookupSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerLookupSession

    def get_sequence_rule_enabler_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule enabler query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleEnablerQuerySession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_query()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerQuerySession

    def get_sequence_rule_enabler_query_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule enabler query service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleEnablerQuerySession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerQuerySession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerQuerySession

    def get_sequence_rule_enabler_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule enabler search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleEnablerSearchSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_search()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerSearchSession

    def get_sequence_rule_enabler_search_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule enablers earch service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleEnablerSearchSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerSearchSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerSearchSession

    def get_sequence_rule_enabler_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule enabler administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleEnablerAdminSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_admin()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerAdminSession

    def get_sequence_rule_enabler_admin_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule enabler administration service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleEnablerAdminSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerAdminSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerAdminSession

    def get_sequence_rule_enabler_notification_session(self, sequence_rule_enabler_receiver, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule enabler notification service.

        :param sequence_rule_enabler_receiver: the notification callback
        :type sequence_rule_enabler_receiver: ``osid.assessment.authoring.SequenceRuleEnablerReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleEnablerNotificationSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerNotificationSession``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_notification()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerNotificationSession

    def get_sequence_rule_enabler_notification_session_for_bank(self, sequence_rule_enabler_receiver, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule enabler notification service for the given bank.

        :param sequence_rule_enabler_receiver: the notification callback
        :type sequence_rule_enabler_receiver: ``osid.assessment.authoring.SequenceRuleEnablerReceiver``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleEnablerNotificationSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerNotificationSession``
        :raise: ``NotFound`` -- no bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_receiver, bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerNotificationSession

    def get_sequence_rule_enabler_bank_session(self, proxy):
        """Gets the ``OsidSession`` to lookup sequence rule enabler/bank mappings for sequence rule enablers.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleEnablerBankSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerBankSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_bank()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerBankSession

    def get_sequence_rule_enabler_bank_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with assigning sequence rule enablers to bank.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleEnablerBankAssignmentSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerBankAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_bank_assignment()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerBankAssignmentSession

    def get_sequence_rule_enabler_smart_bank_session(self, bank_id, proxy):
        """Gets the ``OsidSession`` to manage sequence rule enabler smart bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleEnablerSmartBankSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerSmartBankSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_smart_bank()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerSmartBankSession

    def get_sequence_rule_enabler_rule_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule enabler mapping lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleEnablerRuleLookupSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerRuleLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_rule_lookup()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerRuleLookupSession

    def get_sequence_rule_enabler_rule_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule enabler mapping lookup service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleEnablerRuleLookupSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerRuleLookupSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_rule_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerRuleLookupSession

    def get_sequence_rule_enabler_rule_application_session(self, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule enabler assignment service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleEnablerRuleApplicationSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerRuleApplicationSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_rule_application()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerRuleApplicationSession

    def get_sequence_rule_enabler_rule_application_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the sequence rule enabler assignment service for the given bank.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SequenceRuleEnablerRuleApplicationSession``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerRuleApplicationSession``
        :raise: ``NotFound`` -- no ``Bank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_sequence_rule_enabler_rule_application()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.authoring.SequenceRuleEnablerRuleApplicationSession


