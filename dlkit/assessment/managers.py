from ..osid import managers as osid_managers


class AssessmentProfile(osid_managers.OsidProfile):
    """The ``AssessmentProfile`` describes the interoperability among assessment services."""
    def supports_assessment(self):
        """Tests for the availability of a assessment service which is the service for taking and examining assessments taken.

        :return: ``true`` if assessment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_item_lookup(self):
        """Tests if an item lookup service is supported.

        :return: true if item lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_item_query(self):
        """Tests if an item query service is supported.

        :return: ``true`` if item query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_item_admin(self):
        """Tests if an item administrative service is supported.

        :return: ``true`` if item admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_lookup(self):
        """Tests if an assessment lookup service is supported.

        An assessment lookup service defines methods to access
        assessments.

        :return: true if assessment lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_query(self):
        """Tests if an assessment query service is supported.

        :return: ``true`` if assessment query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_admin(self):
        """Tests if an assessment administrative service is supported.

        :return: ``true`` if assessment admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_basic_authoring(self):
        """Tests if an assessment basic authoring session is available.

        :return: ``true`` if assessment basic authoring is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_offered_lookup(self):
        """Tests if an assessment offered lookup service is supported.

        :return: true if assessment offered lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_offered_query(self):
        """Tests if an assessment offered query service is supported.

        :return: ``true`` if assessment offered query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_offered_admin(self):
        """Tests if an assessment offered administrative service is supported.

        :return: ``true`` if assessment offered admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_taken_lookup(self):
        """Tests if an assessment taken lookup service is supported.

        :return: ``true`` if assessment taken lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_taken_query(self):
        """Tests if an assessment taken query service is supported.

        :return: ``true`` if assessment taken query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_assessment_taken_admin(self):
        """Tests if an assessment taken administrative service is supported which is used to instantiate an assessment offered.

        :return: ``true`` if assessment taken admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_bank_lookup(self):
        """Tests if a bank lookup service is supported.

        A bank lookup service defines methods to access assessment
        banks.

        :return: ``true`` if bank lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_bank_admin(self):
        """Tests if a banlk administrative service is supported.

        :return: ``true`` if bank admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_bank_hierarchy(self):
        """Tests if a bank hierarchy traversal is supported.

        :return: ``true`` if a bank hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_bank_hierarchy_design(self):
        """Tests if bank hierarchy design is supported.

        :return: ``true`` if a bank hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_item_record_types(self):
        """Gets the supported ``Item`` record types.

        :return: a list containing the supported ``Item`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    item_record_types = property(fget=get_item_record_types)

    def get_item_search_record_types(self):
        """Gets the supported ``Item`` search record types.

        :return: a list containing the supported ``Item`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    item_search_record_types = property(fget=get_item_search_record_types)

    def get_assessment_record_types(self):
        """Gets the supported ``Assessment`` record types.

        :return: a list containing the supported ``Assessment`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    assessment_record_types = property(fget=get_assessment_record_types)

    def get_assessment_search_record_types(self):
        """Gets the supported ``Assessment`` search record types.

        :return: a list containing the supported assessment search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    assessment_search_record_types = property(fget=get_assessment_search_record_types)

    def get_assessment_offered_record_types(self):
        """Gets the supported ``AssessmentOffered`` record types.

        :return: a list containing the supported ``AssessmentOffered`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    assessment_offered_record_types = property(fget=get_assessment_offered_record_types)

    def get_assessment_offered_search_record_types(self):
        """Gets the supported ``AssessmentOffered`` search record types.

        :return: a list containing the supported ``AssessmentOffered`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    assessment_offered_search_record_types = property(fget=get_assessment_offered_search_record_types)

    def get_assessment_taken_record_types(self):
        """Gets the supported ``AssessmentTaken`` record types.

        :return: a list containing the supported ``AssessmentTaken`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    assessment_taken_record_types = property(fget=get_assessment_taken_record_types)

    def get_assessment_taken_search_record_types(self):
        """Gets the supported ``AssessmentTaken`` search record types.

        :return: a list containing the supported ``AssessmentTaken`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    assessment_taken_search_record_types = property(fget=get_assessment_taken_search_record_types)

    def get_assessment_section_record_types(self):
        """Gets the supported ``AssessmentSection`` record types.

        :return: a list containing the supported ``AssessmentSection`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    assessment_section_record_types = property(fget=get_assessment_section_record_types)

    def get_bank_record_types(self):
        """Gets the supported ``Bank`` record types.

        :return: a list containing the supported ``Bank`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    bank_record_types = property(fget=get_bank_record_types)

    def get_bank_search_record_types(self):
        """Gets the supported bank search record types.

        :return: a list containing the supported ``Bank`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    bank_search_record_types = property(fget=get_bank_search_record_types)


class AssessmentManager(osid_managers.OsidManager, AssessmentProfile):
    """The assessment manager provides access to assessment sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``MyAssessmentTakenSession:`` a session to get taken or in
        progress assessments for the current agent
      * ``AssessmentSession:`` a session to be assessed and examine
        assessments taken
      * ``AssessmentResultsSession:`` a session to retrieve assessment
        results

      * ``ItemLookupSession:`` a session to look up ``Items``
      * ``ItemQuerySession`` : a session to query ``Items``
      * ``ItemSearchSession:`` a session to search ``Items``
      * ``ItemAdminSession:`` a session to create, modify and delete
        ``Items``
      * ``ItemNotificationSession: a`` session to receive messages
        pertaining to ``Item`` changes
      * ``ItemBankSession:`` a session for looking up item and bank
        mappings
      * ``ItemBankAssignmentSession:`` a session for managing item and
        bank mappings
      * ``ItemSmartBankSession:`` a session for managing dynamic banks

      * ``AssessmentLookupSession:`` a session to look up
        ``Assessments``
      * ``AssessmentQuerySession:`` a session to query ``Assessments``
      * ``AssessmentSearchSession:`` a session to search ``Assessments``
      * ``AssessmentAdminSession:`` a session to create, modify and
        delete ``Assessments``
      * ``AssessmentNotificationSession: a`` session to receive messages
        pertaining to ``Assessment`` changes

      * ``AssessmentBankSession:`` a session for looking up assessment
        and bank mappings
      * ``AssessmentBankAssignmentSession:`` a session for managing
        assessment and bank mappings
      * ``AssessmentSmartBankSession:`` a session for managing dynamic
        banks
      * ``AssessmentBasicAuthoringSession:`` a session for making simple
        mappings of assessment items to assessments

      * ``AssessmentOfferedLookupSession:`` a session to look up
        ``AssessmentsOffered``
      * ``AssessmentOfferedQuerySession:`` a session to query
        ``AssessmentsOffered``
      * ``AssessmentOfferedSearchSession`` : a session to search
        ``AssessmentsOffered``
      * ``AssessmentOfferedAdminSession:`` a session to create, modify
        and delete ``AssessmentsOffered``
      * ``AssessmentOfferedNotificationSession: a`` session to receive
        messages pertaining to ``AssessmentOffered`` changes
      * ``AssessmentOfferedBankSession:`` a session for looking up
        assessments offered and bank mappings
      * ``AssessmentOfferedBankAssignmentSession:`` a session for
        managing assessments offered and bank mappings
      * ``AssessmentOfferedSmartBankSession`` : a session to manage
        dynamic banks of assessments offered

      * ``AssessmentTakenLookupSession:`` a session to look up
        ``Assessments``
      * ``AssessmentTakenQuerySession:`` a session to query
        ``Assessments``
      * ``AssessmentTakenSearchSession:`` a session to search
        Assessments
      * ``AssessmentTakenAdminSession:`` a session to create, modify and
        delete ``AssessmentsTaken``
      * ``AssessmentTakenNotificationSession: a`` session to receive
        messages pertaining to ``AssessmentTaken`` changes
      * ``AssessmentTakenBankSession:`` a session for looking up
        assessments taken and bank mappings
      * ``AssessmenttTakenBankAssignmentSession:`` a session for
        managing assessments taken and bank mappings
      * ``AssessmentTakenSmartBankSession:`` a session to manage dynamic
        banks of assessments taken

      * ``BankLookupSession:`` a session to lookup banks
      * ``BankQuerySession`` : a session to query banks
      * ``BankSearchSession:`` a session to search banks
      * ``BankAdminSession`` : a session to create, modify and delete
        banks
      * ``BankNotificationSession`` : a session to receive messages
        pertaining to ``Bank`` changes
      * ``BankHierarchySession`` : a session to traverse the ``Bank``
        hierarchy
      * ``BankHierarchyDesignSession`` : a session to manage the
        ``Bank`` hierarchy


    """
    def get_assessment_session(self):
        """Gets an ``AssessmentSession`` which is responsible for taking assessments and examining responses from assessments taken.

        :return: an assessment session for this service
        :rtype: ``osid.assessment.AssessmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment()`` is ``false``

        """
        return # osid.assessment.AssessmentSession

    assessment_session = property(fget=get_assessment_session)

    def get_assessment_session_for_bank(self, bank_id):
        """Gets an ``AssessmentSession`` which is responsible for performing assessments for the given bank ``Id``.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: an assessment session for this service
        :rtype: ``osid.assessment.AssessmentSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment()`` is ``false``

        """
        return # osid.assessment.AssessmentSession

    def get_item_lookup_session(self):
        """Gets the ``OsidSession`` associated with the item lookup service.

        :return: an ``ItemLookupSession``
        :rtype: ``osid.assessment.ItemLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_lookup()`` is ``false``

        """
        return # osid.assessment.ItemLookupSession

    item_lookup_session = property(fget=get_item_lookup_session)

    def get_item_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the item lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _item_lookup_session``
        :rtype: ``osid.assessment.ItemLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.ItemLookupSession

    def get_item_query_session(self):
        """Gets the ``OsidSession`` associated with the item query service.

        :return: an ``ItemQuerySession``
        :rtype: ``osid.assessment.ItemQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_query()`` is ``false``

        """
        return # osid.assessment.ItemQuerySession

    item_query_session = property(fget=get_item_query_session)

    def get_item_query_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the item query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _item_query_session``
        :rtype: ``osid.assessment.ItemQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.ItemQuerySession

    def get_item_admin_session(self):
        """Gets the ``OsidSession`` associated with the item administration service.

        :return: an ``ItemAdminSession``
        :rtype: ``osid.assessment.ItemAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_admin()`` is ``false``

        """
        return # osid.assessment.ItemAdminSession

    item_admin_session = property(fget=get_item_admin_session)

    def get_item_admin_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the item admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _item_admin_session``
        :rtype: ``osid.assessment.ItemAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.ItemAdminSession

    def get_assessment_lookup_session(self):
        """Gets the ``OsidSession`` associated with the assessment lookup service.

        :return: an ``AssessmentLookupSession``
        :rtype: ``osid.assessment.AssessmentLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_lookup()`` is ``false``

        """
        return # osid.assessment.AssessmentLookupSession

    assessment_lookup_session = property(fget=get_assessment_lookup_session)

    def get_assessment_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _assessment_lookup_session``
        :rtype: ``osid.assessment.AssessmentLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentLookupSession

    def get_assessment_query_session(self):
        """Gets the ``OsidSession`` associated with the assessment query service.

        :return: an ``AssessmentQuerySession``
        :rtype: ``osid.assessment.AssessmentQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` is ``false``

        """
        return # osid.assessment.AssessmentQuerySession

    assessment_query_session = property(fget=get_assessment_query_session)

    def get_assessment_query_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _assessment_query_session``
        :rtype: ``osid.assessment.AssessmentQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentQuerySession

    def get_assessment_admin_session(self):
        """Gets the ``OsidSession`` associated with the assessment administration service.

        :return: an ``AssessmentAdminSession``
        :rtype: ``osid.assessment.AssessmentAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_admin()`` is ``false``

        """
        return # osid.assessment.AssessmentAdminSession

    assessment_admin_session = property(fget=get_assessment_admin_session)

    def get_assessment_admin_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _assessment_admin_session``
        :rtype: ``osid.assessment.AssessmentAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentAdminSession

    def get_assessment_basic_authoring_session(self):
        """Gets the ``OsidSession`` associated with the assessment authoring service.

        :return: an ``AssessmentBasicAuthoringSession``
        :rtype: ``osid.assessment.AssessmentBasicAuthoringSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_basic_authoring()`` is ``false``

        """
        return # osid.assessment.AssessmentBasicAuthoringSession

    assessment_basic_authoring_session = property(fget=get_assessment_basic_authoring_session)

    def get_assessment_basic_authoring_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment authoring service for the given bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentBasicAuthoringSession``
        :rtype: ``osid.assessment.AssessmentBasicAuthoringSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_basic_authoring()`` or ``supports_visibe_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentBasicAuthoringSession

    def get_assessment_offered_lookup_session(self):
        """Gets the ``OsidSession`` associated with the assessment offered lookup service.

        :return: an ``AssessmentOfferedLookupSession``
        :rtype: ``osid.assessment.AssessmentOfferedLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_lookup()`` is ``false``

        """
        return # osid.assessment.AssessmentOfferedLookupSession

    assessment_offered_lookup_session = property(fget=get_assessment_offered_lookup_session)

    def get_assessment_offered_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment offered lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentOfferedLookupSession``
        :rtype: ``osid.assessment.AssessmentOfferedLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentOfferedLookupSession

    def get_assessment_offered_query_session(self):
        """Gets the ``OsidSession`` associated with the assessment offered query service.

        :return: an ``AssessmentOfferedQuerySession``
        :rtype: ``osid.assessment.AssessmentOfferedQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_query()`` is ``false``

        """
        return # osid.assessment.AssessmentOfferedQuerySession

    assessment_offered_query_session = property(fget=get_assessment_offered_query_session)

    def get_assessment_offered_query_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment offered query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentOfferedQuerySession``
        :rtype: ``osid.assessment.AssessmentOfferedQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentOfferedQuerySession

    def get_assessment_offered_admin_session(self):
        """Gets the ``OsidSession`` associated with the assessment offered administration service.

        :return: an ``AssessmentOfferedAdminSession``
        :rtype: ``osid.assessment.AssessmentOfferedAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_admin()`` is ``false``

        """
        return # osid.assessment.AssessmentOfferedAdminSession

    assessment_offered_admin_session = property(fget=get_assessment_offered_admin_session)

    def get_assessment_offered_admin_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment offered admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentOfferedAdminSession``
        :rtype: ``osid.assessment.AssessmentOfferedAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentOfferedAdminSession

    def get_assessment_taken_lookup_session(self):
        """Gets the ``OsidSession`` associated with the assessment taken lookup service.

        :return: an ``AssessmentTakenLookupSession``
        :rtype: ``osid.assessment.AssessmentTakenLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_lookup()`` is ``false``

        """
        return # osid.assessment.AssessmentTakenLookupSession

    assessment_taken_lookup_session = property(fget=get_assessment_taken_lookup_session)

    def get_assessment_taken_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment taken lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentTakenLookupSession``
        :rtype: ``osid.assessment.AssessmentTakenLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentTakenLookupSession

    def get_assessment_taken_query_session(self):
        """Gets the ``OsidSession`` associated with the assessment taken query service.

        :return: an ``AssessmentTakenQuerySession``
        :rtype: ``osid.assessment.AssessmentTakenQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_query()`` is ``false``

        """
        return # osid.assessment.AssessmentTakenQuerySession

    assessment_taken_query_session = property(fget=get_assessment_taken_query_session)

    def get_assessment_taken_query_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment taken query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentTakenQuerySession``
        :rtype: ``osid.assessment.AssessmentTakenQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentTakenQuerySession

    def get_assessment_taken_admin_session(self):
        """Gets the ``OsidSession`` associated with the assessment taken administration service.

        :return: an ``AssessmentTakenAdminSession``
        :rtype: ``osid.assessment.AssessmentTakenAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_admin()`` is ``false``

        """
        return # osid.assessment.AssessmentTakenAdminSession

    assessment_taken_admin_session = property(fget=get_assessment_taken_admin_session)

    def get_assessment_taken_admin_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment taken admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentTakenSearchSession``
        :rtype: ``osid.assessment.AssessmentTakenAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentTakenAdminSession

    def get_bank_lookup_session(self):
        """Gets the OsidSession associated with the bank lookup service.

        :return: a ``BankLookupSession``
        :rtype: ``osid.assessment.BankLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_lookup() is false``

        """
        return # osid.assessment.BankLookupSession

    bank_lookup_session = property(fget=get_bank_lookup_session)

    def get_bank_admin_session(self):
        """Gets the OsidSession associated with the bank administration service.

        :return: a ``BankAdminSession``
        :rtype: ``osid.assessment.BankAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_admin() is false``

        """
        return # osid.assessment.BankAdminSession

    bank_admin_session = property(fget=get_bank_admin_session)

    def get_bank_hierarchy_session(self):
        """Gets the session traversing bank hierarchies.

        :return: a ``BankHierarchySession``
        :rtype: ``osid.assessment.BankHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_hierarchy() is false``

        """
        return # osid.assessment.BankHierarchySession

    bank_hierarchy_session = property(fget=get_bank_hierarchy_session)

    def get_bank_hierarchy_design_session(self):
        """Gets the session designing bank hierarchies.

        :return: a ``BankHierarchySession``
        :rtype: ``osid.assessment.BankHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_hierarchy_design() is false``

        """
        return # osid.assessment.BankHierarchyDesignSession

    bank_hierarchy_design_session = property(fget=get_bank_hierarchy_design_session)

    def get_assessment_authoring_manager(self):
        """Gets an ``AssessmentAuthoringManager``.

        :return: an ``AssessmentAuthoringManager``
        :rtype: ``osid.assessment.authoring.AssessmentAuthoringManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_authoring() is false``

        """
        return # osid.assessment.authoring.AssessmentAuthoringManager

    assessment_authoring_manager = property(fget=get_assessment_authoring_manager)

    def get_assessment_batch_manager(self):
        """Gets an ``AssessmentBatchManager``.

        :return: an ``AssessmentBatchManager``
        :rtype: ``osid.assessment.batch.AssessmentBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_batch() is false``

        """
        return # osid.assessment.batch.AssessmentBatchManager

    assessment_batch_manager = property(fget=get_assessment_batch_manager)


class AssessmentProxyManager(osid_managers.OsidProxyManager, AssessmentProfile):
    """The assessment manager provides access to assessment sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` object.
    The sessions included in this manager are:

      * ``MyAssessmentTakenSession:`` a session to get taken or in
        progress assessments for the current agent
      * ``AssessmentSession:`` a session to be assessed and examine
        assessments taken
      * ``AssessmentResultsSession:`` a session to retrieve assessment
        results

      * ``ItemLookupSession:`` a session to look up ``Items``
      * ``ItemQuerySession`` : a session to query ``Items``
      * ``ItemSearchSession:`` a session to search ``Items``
      * ``ItemAdminSession:`` a session to create, modify and delete
        ``Items``
      * ``ItemNotificationSession: a`` session to receive messages
        pertaining to ``Item`` changes
      * ``ItemBankSession:`` a session for looking up item and bank
        mappings
      * ``ItemBankAssignmentSession:`` a session for managing item and
        bank mappings
      * ``ItemSmartBankSession:`` a session for managing dynamic banks

      * ``AssessmentLookupSession:`` a session to look up
        ``Assessments``
      * ``AssessmentQuerySession:`` a session to query ``Assessments``
      * ``AssessmentSearchSession:`` a session to search ``Assessments``
      * ``AssessmentAdminSession:`` a session to create, modify and
        delete ``Assessments``
      * ``AssessmentNotificationSession: a`` session to receive messages
        pertaining to ``Assessment`` changes

      * ``AssessmentBankSession:`` a session for looking up assessment
        and bank mappings
      * ``AssessmentBankAssignmentSession:`` a session for managing
        assessment and bank mappings
      * ``AssessmentSmartBankSession:`` a session for managing dynamic
        banks
      * ``AssessmentBasicAuthoringSession:`` a session for making simple
        mappings of assessment items to assessments

      * ``AssessmentOfferedLookupSession:`` a session to look up
        ``Assessments``
      * ``AssessmentOfferedQuerySession:`` a session to query
        ``Assessments``
      * ``AssessmentOfferedSearchSession`` : a session to search
        ``Assessments``
      * ``AssessmentOfferedAdminSession:`` a session to create, modify
        and delete ``Assessments``
      * ``AssessmentOfferedNotificationSession: a`` session to receive
        messages pertaining to ``Assessment`` changes
      * ``AssessmentOfferedBankSession:`` a session for looking up
        assessment and bank mappings
      * ``AssessmentOfferedBankAssignmentSession:`` a session for
        managing assessment and bank mappings
      * ``AssessmentOfferedSmartBankSession`` : a session to manage
        dynamic banks

      * ``AssessmentTakenLookupSession:`` a session to look up
        ``Assessments``
      * ``AssessmentTakenQuerySession:`` a session to query
        ``Assessments``
      * ``AssessmentTakenSearchSession:`` a session to search
        Assessments
      * ``AssessmentTakenAdminSession:`` a session to create, modify and
        delete ``AssessmentsTaken``
      * ``AssessmentTakenNotificationSession: a`` session to receive
        messages pertaining to ``AssessmentTaken`` changes
      * ``AssessmentTakenBankSession:`` a session for looking up
        assessments taken and bank mappings
      * ``AssessmenttTakenBankAssignmentSession:`` a session for
        managing assessments taken and bank mappings
      * ``AssessmentTakenSmartBankSession:`` a session to manage dynamic
        banks of assessments taken

      * ``BankLookupSession:`` a session to lookup banks
      * ``BankQuerySession`` : a session to query banks
      * ``BankSearchSession:`` a session to search banks
      * ``BankAdminSession`` : a session to create, modify and delete
        banks
      * ``BankNotificationSession`` : a session to receive messages
        pertaining to ``Bank`` changes
      * ``BankHierarchySession`` : a session to traverse the ``Bank``
        hierarchy
      * ``BankHierarchyDesignSession`` : a session to manage the
        ``Bank`` hierarchy


    """
    def get_assessment_session(self, proxy):
        """Gets an ``AssessmentSession`` which is responsible for taking assessments and examining responses from assessments taken.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an assessment session for this service
        :rtype: ``osid.assessment.AssessmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment()`` is ``false``

        """
        return # osid.assessment.AssessmentSession

    def get_assessment_session_for_bank(self, bank_id, proxy):
        """Gets an ``AssessmentSession`` which is responsible for performing assessments for the given bank ``Id``.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an assessment session for this service
        :rtype: ``osid.assessment.AssessmentSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment()`` is ``false``

        """
        return # osid.assessment.AssessmentSession

    def get_item_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the item lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemLookupSession``
        :rtype: ``osid.assessment.ItemLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_lookup()`` is ``false``

        """
        return # osid.assessment.ItemLookupSession

    def get_item_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the item lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _item_lookup_session``
        :rtype: ``osid.assessment.ItemLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.ItemLookupSession

    def get_item_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the item query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemQuerySession``
        :rtype: ``osid.assessment.ItemQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_query()`` is ``false``

        """
        return # osid.assessment.ItemQuerySession

    def get_item_query_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the item query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _item_query_session``
        :rtype: ``osid.assessment.ItemQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.ItemQuerySession

    def get_item_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the item administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemAdminSession``
        :rtype: ``osid.assessment.ItemAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_admin()`` is ``false``

        """
        return # osid.assessment.ItemAdminSession

    def get_item_admin_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the item admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _item_admin_session``
        :rtype: ``osid.assessment.ItemAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.ItemAdminSession

    def get_assessment_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentLookupSession``
        :rtype: ``osid.assessment.AssessmentLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_lookup()`` is ``false``

        """
        return # osid.assessment.AssessmentLookupSession

    def get_assessment_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _assessment_lookup_session``
        :rtype: ``osid.assessment.AssessmentLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentLookupSession

    def get_assessment_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentQuerySession``
        :rtype: ``osid.assessment.AssessmentQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` is ``false``

        """
        return # osid.assessment.AssessmentQuerySession

    def get_assessment_query_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _assessment_query_session``
        :rtype: ``osid.assessment.AssessmentQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentQuerySession

    def get_assessment_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentAdminSession``
        :rtype: ``osid.assessment.AssessmentAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_admin()`` is ``false``

        """
        return # osid.assessment.AssessmentAdminSession

    def get_assessment_admin_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _assessment_admin_session``
        :rtype: ``osid.assessment.AssessmentAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentAdminSession

    def get_assessment_basic_authoring_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment authoring service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentBasicAuthoringSession``
        :rtype: ``osid.assessment.AssessmentBasicAuthoringSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_basic_authoring()`` is ``false``

        """
        return # osid.assessment.AssessmentBasicAuthoringSession

    def get_assessment_basic_authoring_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment authoring service for the given bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentBasicAuthoringSession``
        :rtype: ``osid.assessment.AssessmentBasicAuthoringSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_basic_authoring()`` or ``supports_visibe_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentBasicAuthoringSession

    def get_assessment_offered_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedLookupSession``
        :rtype: ``osid.assessment.AssessmentOfferedLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_lookup()`` is ``false``

        """
        return # osid.assessment.AssessmentOfferedLookupSession

    def get_assessment_offered_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedLookupSession``
        :rtype: ``osid.assessment.AssessmentOfferedLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentOfferedLookupSession

    def get_assessment_offered_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedQuerySession``
        :rtype: ``osid.assessment.AssessmentOfferedQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_query()`` is ``false``

        """
        return # osid.assessment.AssessmentOfferedQuerySession

    def get_assessment_offered_query_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedQuerySession``
        :rtype: ``osid.assessment.AssessmentOfferedQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentOfferedQuerySession

    def get_assessment_offered_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedAdminSession``
        :rtype: ``osid.assessment.AssessmentOfferedAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_admin()`` is ``false``

        """
        return # osid.assessment.AssessmentOfferedAdminSession

    def get_assessment_offered_admin_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedAdminSession``
        :rtype: ``osid.assessment.AssessmentOfferedAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentOfferedAdminSession

    def get_assessment_taken_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenLookupSession``
        :rtype: ``osid.assessment.AssessmentTakenLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_lookup()`` is ``false``

        """
        return # osid.assessment.AssessmentTakenLookupSession

    def get_assessment_taken_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenLookupSession``
        :rtype: ``osid.assessment.AssessmentTakenLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentTakenLookupSession

    def get_assessment_taken_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenQuerySession``
        :rtype: ``osid.assessment.AssessmentTakenQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_query()`` is ``false``

        """
        return # osid.assessment.AssessmentTakenQuerySession

    def get_assessment_taken_query_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenQuerySession``
        :rtype: ``osid.assessment.AssessmentTakenQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentTakenQuerySession

    def get_assessment_taken_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenAdminSession``
        :rtype: ``osid.assessment.AssessmentTakenAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_admin()`` is ``false``

        """
        return # osid.assessment.AssessmentTakenAdminSession

    def get_assessment_taken_admin_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenSearchSession``
        :rtype: ``osid.assessment.AssessmentTakenAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.assessment.AssessmentTakenAdminSession

    def get_bank_lookup_session(self, proxy):
        """Gets the OsidSession associated with the bank lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankLookupSession``
        :rtype: ``osid.assessment.BankLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_lookup() is false``

        """
        return # osid.assessment.BankLookupSession

    def get_bank_admin_session(self, proxy):
        """Gets the OsidSession associated with the bank administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankAdminSession``
        :rtype: ``osid.assessment.BankAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_admin() is false``

        """
        return # osid.assessment.BankAdminSession

    def get_bank_hierarchy_session(self, proxy):
        """Gets the session traversing bank hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankHierarchySession``
        :rtype: ``osid.assessment.BankHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_hierarchy() is false``

        """
        return # osid.assessment.BankHierarchySession

    def get_bank_hierarchy_design_session(self, proxy):
        """Gets the session designing bank hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankHierarchySession``
        :rtype: ``osid.assessment.BankHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_hierarchy_design() is false``

        """
        return # osid.assessment.BankHierarchyDesignSession

    def get_assessment_authoring_proxy_manager(self):
        """Gets an ``AssessmentAuthoringProxyManager``.

        :return: an ``AssessmentAuthoringProxyManager``
        :rtype: ``osid.assessment.authoring.AssessmentAuthoringProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_authoring() is false``

        """
        return # osid.assessment.authoring.AssessmentAuthoringProxyManager

    assessment_authoring_proxy_manager = property(fget=get_assessment_authoring_proxy_manager)

    def get_assessment_batch_proxy_manager(self):
        """Gets an ``AssessmentBatchProxyManager``.

        :return: an ``AssessmentBatchProxyManager``
        :rtype: ``osid.assessment.batch.AssessmentBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_batch() is false``

        """
        return # osid.assessment.batch.AssessmentBatchProxyManager

    assessment_batch_proxy_manager = property(fget=get_assessment_batch_proxy_manager)


