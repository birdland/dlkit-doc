
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class AssessmentProfile(osid_managers.OsidProfile):
    """The ``AssessmentProfile`` describes the interoperability among assessment services."""

    def supports_assessment(self):
        """Tests for the availability of a assessment service which is the service for taking and examining assessments
            taken.


        :return: ``true`` if assessment is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_item_lookup(self):
        """Tests if an item lookup service is supported.


        :return: true if item lookup is supported, false otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_item_query(self):
        """Tests if an item query service is supported.


        :return: ``true`` if item query is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_item_search(self):
        """Tests if an item search service is supported.


        :return: ``true`` if item search is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_item_admin(self):
        """Tests if an item administrative service is supported.


        :return: ``true`` if item admin is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_item_notification(self):
        """Tests if item notification is supported.


        Messages may be sent when items are created, modified, or
        deleted.


        :return: ``true`` if item notification is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_item_bank(self):
        """Tests if an item to bank lookup session is available.


        :return: ``true`` if item bank lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_item_bank_assignment(self):
        """Tests if an item to bank assignment session is available.


        :return: ``true`` if item bank assignment is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_assessment_lookup(self):
        """Tests if an assessment lookup service is supported.


        An assessment lookup service defines methods to access
        assessments.


        :return: true if assessment lookup is supported, false otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_assessment_query(self):
        """Tests if an assessment query service is supported.


        :return: ``true`` if assessment query is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_assessment_admin(self):
        """Tests if an assessment administrative service is supported.


        :return: ``true`` if assessment admin is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_assessment_bank(self):
        """Tests if an assessment to bank lookup session is available.


        :return: ``true`` if assessment bank lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_assessment_bank_assignment(self):
        """Tests if an assessment to bank assignment session is available.


        :return: ``true`` if assessment bank assignment is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_assessment_basic_authoring(self):
        """Tests if an assessment basic authoring session is available.


        :return: ``true`` if assessment basic authoring is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_assessment_offered_lookup(self):
        """Tests if an assessment offered lookup service is supported.


        :return: true if assessment offered lookup is supported, false otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_assessment_offered_query(self):
        """Tests if an assessment offered query service is supported.


        :return: ``true`` if assessment offered query is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_assessment_offered_admin(self):
        """Tests if an assessment offered administrative service is supported.


        :return: ``true`` if assessment offered admin is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_assessment_offered_bank(self):
        """Tests if an assessment offered to bank lookup session is available.


        :return: ``true`` if assessment offered bank lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_assessment_offered_bank_assignment(self):
        """Tests if an assessment offered to bank assignment session is available.


        :return: ``true`` if assessment offered bank assignment is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_assessment_taken_lookup(self):
        """Tests if an assessment taken lookup service is supported.


        :return: ``true`` if assessment taken lookup is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_assessment_taken_query(self):
        """Tests if an assessment taken query service is supported.


        :return: ``true`` if assessment taken query is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_assessment_taken_admin(self):
        """Tests if an assessment taken administrative service is supported which is used to instantiate an assessment
            offered.


        :return: ``true`` if assessment taken admin is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_assessment_taken_bank(self):
        """Tests if an assessment taken to bank lookup session is available.


        :return: ``true`` if assessment taken bank lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_assessment_taken_bank_assignment(self):
        """Tests if an assessment taken to bank assignment session is available.


        :return: ``true`` if assessment taken bank assignment is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_bank_lookup(self):
        """Tests if a bank lookup service is supported.


        A bank lookup service defines methods to access assessment
        banks.


        :return: ``true`` if bank lookup is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_bank_query(self):
        """Tests if a bank query service is supported.


        :return: ``true`` if bank query is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_bank_admin(self):
        """Tests if a banlk administrative service is supported.


        :return: ``true`` if bank admin is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_bank_hierarchy(self):
        """Tests if a bank hierarchy traversal is supported.


        :return: ``true`` if a bank hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_bank_hierarchy_design(self):
        """Tests if bank hierarchy design is supported.


        :return: ``true`` if a bank hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_item_record_types(self):
        """Gets the supported ``Item`` record types.


        :return: a list containing the supported ``Item`` record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    item_record_types = property(fget=get_item_record_types)

    def get_item_search_record_types(self):
        """Gets the supported ``Item`` search record types.


        :return: a list containing the supported ``Item`` search record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    item_search_record_types = property(fget=get_item_search_record_types)

    def get_assessment_record_types(self):
        """Gets the supported ``Assessment`` record types.


        :return: a list containing the supported ``Assessment`` record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    assessment_record_types = property(fget=get_assessment_record_types)

    def get_assessment_search_record_types(self):
        """Gets the supported ``Assessment`` search record types.


        :return: a list containing the supported assessment search record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    assessment_search_record_types = property(fget=get_assessment_search_record_types)

    def get_assessment_offered_record_types(self):
        """Gets the supported ``AssessmentOffered`` record types.


        :return: a list containing the supported ``AssessmentOffered`` record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    assessment_offered_record_types = property(fget=get_assessment_offered_record_types)

    def get_assessment_offered_search_record_types(self):
        """Gets the supported ``AssessmentOffered`` search record types.


        :return: a list containing the supported ``AssessmentOffered`` search record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    assessment_offered_search_record_types = property(fget=get_assessment_offered_search_record_types)

    def get_assessment_taken_record_types(self):
        """Gets the supported ``AssessmentTaken`` record types.


        :return: a list containing the supported ``AssessmentTaken`` record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    assessment_taken_record_types = property(fget=get_assessment_taken_record_types)

    def get_assessment_taken_search_record_types(self):
        """Gets the supported ``AssessmentTaken`` search record types.


        :return: a list containing the supported ``AssessmentTaken`` search record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    assessment_taken_search_record_types = property(fget=get_assessment_taken_search_record_types)

    def get_assessment_section_record_types(self):
        """Gets the supported ``AssessmentSection`` record types.


        :return: a list containing the supported ``AssessmentSection`` record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    assessment_section_record_types = property(fget=get_assessment_section_record_types)

    def get_bank_record_types(self):
        """Gets the supported ``Bank`` record types.


        :return: a list containing the supported ``Bank`` record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    bank_record_types = property(fget=get_bank_record_types)

    def get_bank_search_record_types(self):
        """Gets the supported bank search record types.


        :return: a list containing the supported ``Bank`` search record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    bank_search_record_types = property(fget=get_bank_search_record_types)


class AssessmentManager(osid_managers.OsidManager, osid_sessions.OsidSession, AssessmentProfile):
    """The assessment manager provides access to assessment sessions and provides interoperability tests for various
        aspects of
    this service.


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

    def get_assessment_authoring_manager(self):
        """Gets an ``AssessmentAuthoringManager``.


        :return: an ``AssessmentAuthoringManager``
        :rtype: ``osid.assessment.authoring.AssessmentAuthoringManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_authoring() is false``


        *compliance: optional -- This method must be implemented if
        ``supports_assessment_authoring()`` is true.*


        """
        return # osid.assessment.authoring.AssessmentAuthoringManager

    assessment_authoring_manager = property(fget=get_assessment_authoring_manager)

    def get_assessment_batch_manager(self):
        """Gets an ``AssessmentBatchManager``.


        :return: an ``AssessmentBatchManager``
        :rtype: ``osid.assessment.batch.AssessmentBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_batch() is false``


        *compliance: optional -- This method must be implemented if
        ``supports_assessment_batch()`` is true.*


        """
        return # osid.assessment.batch.AssessmentBatchManager

    assessment_batch_manager = property(fget=get_assessment_batch_manager)


class AssessmentProxyManager(osid_managers.OsidProxyManager, AssessmentProfile):
    """The assessment manager provides access to assessment sessions and provides interoperability tests for various
        aspects of
    this service.


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

    def get_assessment_authoring_proxy_manager(self):
        """Gets an ``AssessmentAuthoringProxyManager``.


        :return: an ``AssessmentAuthoringProxyManager``
        :rtype: ``osid.assessment.authoring.AssessmentAuthoringProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_authoring() is false``


        *compliance: optional -- This method must be implemented if
        ``supports_assessment_authoring()`` is true.*


        """
        return # osid.assessment.authoring.AssessmentAuthoringProxyManager

    assessment_authoring_proxy_manager = property(fget=get_assessment_authoring_proxy_manager)

    def get_assessment_batch_proxy_manager(self):
        """Gets an ``AssessmentBatchProxyManager``.


        :return: an ``AssessmentBatchProxyManager``
        :rtype: ``osid.assessment.batch.AssessmentBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_batch() is false``


        *compliance: optional -- This method must be implemented if
        ``supports_assessment_batch()`` is true.*


        """
        return # osid.assessment.batch.AssessmentBatchProxyManager

    assessment_batch_proxy_manager = property(fget=get_assessment_batch_proxy_manager)


