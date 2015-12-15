

Service Managers
================


Assessment Manager
------------------

.. py:class:: AssessmentManager(osid_managers.OsidManager, AssessmentProfile, assessment_managers.AssessmentManager)
    The assessment manager provides access to assessment sessions and provides interoperability
        tests
    for various aspects of this service.


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





    .. py:method:: get_my_assessment_taken_session():
        :noindex:


    .. py:attribute:: my_assessment_taken_session
        :noindex:


    .. py:method:: get_my_assessment_taken_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_session():
        :noindex:


    .. py:attribute:: assessment_session
        :noindex:


    .. py:method:: get_assessment_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_results_session():
        :noindex:


    .. py:attribute:: assessment_results_session
        :noindex:


    .. py:method:: get_assessment_results_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_item_lookup_session():
        :noindex:


    .. py:attribute:: item_lookup_session
        :noindex:


    .. py:method:: get_item_lookup_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_item_query_session():
        :noindex:


    .. py:attribute:: item_query_session
        :noindex:


    .. py:method:: get_item_query_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_item_search_session():
        :noindex:


    .. py:attribute:: item_search_session
        :noindex:


    .. py:method:: get_item_search_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_item_admin_session():
        :noindex:


    .. py:attribute:: item_admin_session
        :noindex:


    .. py:method:: get_item_admin_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_item_notification_session(item_receiver):
        :noindex:


    .. py:method:: get_item_notification_session_for_bank(item_receiver, bank_id):
        :noindex:


    .. py:method:: get_item_bank_session():
        :noindex:


    .. py:attribute:: item_bank_session
        :noindex:


    .. py:method:: get_item_bank_assignment_session():
        :noindex:


    .. py:attribute:: item_bank_assignment_session
        :noindex:


    .. py:method:: get_item_smart_bank_session(bank_id):
        :noindex:


    .. py:method:: get_assessment_lookup_session():
        :noindex:


    .. py:attribute:: assessment_lookup_session
        :noindex:


    .. py:method:: get_assessment_lookup_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_query_session():
        :noindex:


    .. py:attribute:: assessment_query_session
        :noindex:


    .. py:method:: get_assessment_query_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_search_session():
        :noindex:


    .. py:attribute:: assessment_search_session
        :noindex:


    .. py:method:: get_assessment_search_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_admin_session():
        :noindex:


    .. py:attribute:: assessment_admin_session
        :noindex:


    .. py:method:: get_assessment_admin_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_notification_session(assessment_receiver):
        :noindex:


    .. py:method:: get_assessment_notification_session_for_bank(assessment_receiver, bank_id):
        :noindex:


    .. py:method:: get_assessment_bank_session():
        :noindex:


    .. py:attribute:: assessment_bank_session
        :noindex:


    .. py:method:: get_assessment_bank_assignment_session():
        :noindex:


    .. py:attribute:: assessment_bank_assignment_session
        :noindex:


    .. py:method:: get_assessment_smart_bank_session(bank_id):
        :noindex:


    .. py:method:: get_assessment_basic_authoring_session():
        :noindex:


    .. py:attribute:: assessment_basic_authoring_session
        :noindex:


    .. py:method:: get_assessment_basic_authoring_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_offered_lookup_session():
        :noindex:


    .. py:attribute:: assessment_offered_lookup_session
        :noindex:


    .. py:method:: get_assessment_offered_lookup_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_offered_query_session():
        :noindex:


    .. py:attribute:: assessment_offered_query_session
        :noindex:


    .. py:method:: get_assessment_offered_query_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_offered_search_session():
        :noindex:


    .. py:attribute:: assessment_offered_search_session
        :noindex:


    .. py:method:: get_assessment_offered_search_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_offered_admin_session():
        :noindex:


    .. py:attribute:: assessment_offered_admin_session
        :noindex:


    .. py:method:: get_assessment_offered_admin_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_offered_notification_session(assessment_offered_receiver):
        :noindex:


    .. py:method:: get_assessment_offered_notification_session_for_bank(assessment_offered_receiver, bank_id):
        :noindex:


    .. py:method:: get_assessment_offered_bank_session():
        :noindex:


    .. py:attribute:: assessment_offered_bank_session
        :noindex:


    .. py:method:: get_assessment_offered_bank_assignment_session():
        :noindex:


    .. py:attribute:: assessment_offered_bank_assignment_session
        :noindex:


    .. py:method:: get_assessment_offered_smart_bank_session(bank_id):
        :noindex:


    .. py:method:: get_assessment_taken_lookup_session():
        :noindex:


    .. py:attribute:: assessment_taken_lookup_session
        :noindex:


    .. py:method:: get_assessment_taken_lookup_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_taken_query_session():
        :noindex:


    .. py:attribute:: assessment_taken_query_session
        :noindex:


    .. py:method:: get_assessment_taken_query_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_taken_search_session():
        :noindex:


    .. py:attribute:: assessment_taken_search_session
        :noindex:


    .. py:method:: get_assessment_taken_search_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_taken_admin_session():
        :noindex:


    .. py:attribute:: assessment_taken_admin_session
        :noindex:


    .. py:method:: get_assessment_taken_admin_session_for_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_taken_notification_session(assessment_taken_receiver):
        :noindex:


    .. py:method:: get_assessment_taken_notification_session_for_bank(assessment_taken_receiver, bank_id):
        :noindex:


    .. py:method:: get_assessment_taken_bank_session():
        :noindex:


    .. py:attribute:: assessment_taken_bank_session
        :noindex:


    .. py:method:: get_assessment_taken_bank_assignment_session():
        :noindex:


    .. py:attribute:: assessment_taken_bank_assignment_session
        :noindex:


    .. py:method:: get_assessment_taken_smart_bank_session(bank_id):
        :noindex:


    .. py:method:: get_bank_lookup_session():
        :noindex:


    .. py:attribute:: bank_lookup_session
        :noindex:


    .. py:method:: get_bank_query_session():
        :noindex:


    .. py:attribute:: bank_query_session
        :noindex:


    .. py:method:: get_bank_search_session():
        :noindex:


    .. py:attribute:: bank_search_session
        :noindex:


    .. py:method:: get_bank_admin_session():
        :noindex:


    .. py:attribute:: bank_admin_session
        :noindex:


    .. py:method:: get_bank_notification_session(bankreceiver):
        :noindex:


    .. py:method:: get_bank_hierarchy_session():
        :noindex:


    .. py:attribute:: bank_hierarchy_session
        :noindex:


    .. py:method:: get_bank_hierarchy_design_session():
        :noindex:


    .. py:attribute:: bank_hierarchy_design_session
        :noindex:


    .. py:method:: get_assessment_authoring_manager():
        :noindex:


    .. py:attribute:: assessment_authoring_manager
        :noindex:


    .. py:method:: get_assessment_batch_manager():
        :noindex:


    .. py:attribute:: assessment_batch_manager
        :noindex:




Item Bank Methods
-----------------

    .. py:method:: can_lookup_item_bank_mappings():
        Tests if this user can perform lookups of item/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_bank_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bank_view():
        A complete view of the ``Item`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_item_ids_by_bank(bank_id):
        Gets the list of ``Item``  ``Ids`` associated with a ``Bank``.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.id.IdList) - list of related item ``Ids``
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_items_by_bank(bank_id):
        Gets the list of ``Items`` associated with a ``Bank``.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.assessment.ItemList) - list of related items
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_item_ids_by_banks(bank_ids):
        Gets the list of ``Item Ids`` corresponding to a list of ``Banks``.

        :arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        :return: (osid.id.IdList) - list of bank ``Ids``
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_items_by_banks(bank_ids):
        Gets the list of ``Items`` corresponding to a list of ``Banks``.

        :arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        :return: (osid.assessment.ItemList) - list of items
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bank_ids_by_item(item_id):
        Gets the list of ``Bank``  ``Ids`` mapped to an ``Item``.

        :arg:    item_id (osid.id.Id): ``Id`` of an ``Item``
        :return: (osid.id.IdList) - list of bank ``Ids``
        :raises:  NotFound - ``item_id`` is not found
        :raises:  NullArgument - ``item_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks_by_item(item_id):
        Gets the list of ``Banks`` mapped to an ``Item``.

        :arg:    item_id (osid.id.Id): ``Id`` of an ``Item``
        :return: (osid.assessment.BankList) - list of banks
        :raises:  NotFound - ``item_id`` is not found
        :raises:  NullArgument - ``item_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*






Item Bank Assignment Methods
----------------------------

    .. py:method:: can_assign_items():
        Tests if this user can alter item/bank mappings.

        A return of true does not guarantee successful assessment. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_items_to_bank(bank_id):
        Tests if this user can alter item/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bank_ids(bank_id):
        Gets a list of banks including and under the given bank node in which any item can be
            assigned.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (osid.id.IdList) - list of assignable bank ``Ids``
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bank_ids_for_item(bank_id, item_id):
        Gets a list of banks including and under the given bank node in which a specific item can be
            assigned.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        :return: (osid.id.IdList) - list of assignable bank ``Ids``
        :raises:  NullArgument - ``bank_id`` or ``item_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_item_to_bank(item_id, bank_id):
        Adds an existing ``Item`` to a ``Bank``.

        :arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :raises:  AlreadyExists - ``item_id`` is already assigned to
                ``bank_id``
        :raises:  NotFound - ``item_id`` or ``bank_id`` not found
        :raises:  NullArgument - ``item_id`` or ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_item_from_bank(item_id, bank_id):
        Removes an ``Item`` from a ``Bank``.

        :arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :raises:  NotFound - ``item_id`` or ``bank_id`` not found or
                ``item_id`` not assigned to ``bank_id``
        :raises:  NullArgument - ``item_id`` or ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: reassign_item_to_billing(item_id, from_bank_id, to_bank_id):
        Moves an ``Item`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        :arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        :arg:    from_bank_id (osid.id.Id): the ``Id`` of the current
                ``Bank``
        :arg:    to_bank_id (osid.id.Id): the ``Id`` of the destination
                ``Bank``
        :raises:  NotFound - ``item_id, from_bank_id,`` or ``to_bank_id``
                not found or ``item_id`` not mapped to ``from_bank_id``
        :raises:  NullArgument - ``item_id, from_bank_id,`` or
                ``to_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Assessment Bank Methods
-----------------------

    .. py:method:: can_lookup_assessment_bank_mappings():
        Tests if this user can perform lookups of assessment/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_bank_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bank_view():
        A complete view of the ``Assessment`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_assessment_ids_by_bank(bank_id):
        Gets the list of ``Assessment``  ``Ids`` associated with a ``Bank``.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.id.IdList) - list of related assessment ``Ids``
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_by_bank(bank_id):
        Gets the list of ``Assessments`` associated with a ``Bank``.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.assessment.AssessmentList) - list of related
                assessments
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessment_ids_by_banks(bank_ids):
        Gets the list of ``Assessment Ids`` corresponding to a list of ``Banks``.

        :arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        :return: (osid.id.IdList) - list of bank ``Ids``
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_by_banks(bank_ids):
        Gets the list of ``Assessments`` corresponding to a list of ``Banks``.

        :arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        :return: (osid.assessment.AssessmentList) - list of assessments
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bank_ids_by_assessment(assessment_id):
        Gets the list of ``Bank``  ``Ids`` mapped to an ``Assessment``.

        :arg:    assessment_id (osid.id.Id): ``Id`` of an ``Assessment``
        :return: (osid.id.IdList) - list of bank ``Ids``
        :raises:  NotFound - ``assessment_id`` is not found
        :raises:  NullArgument - ``assessment_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks_by_assessment(assessment_id):
        Gets the list of ``Banks`` mapped to an ``Assessment``.

        :arg:    assessment_id (osid.id.Id): ``Id`` of an ``Assessment``
        :return: (osid.assessment.BankList) - list of banks
        :raises:  NotFound - ``assessment_id`` is not found
        :raises:  NullArgument - ``assessment_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*






Assessment Bank Assignment Methods
----------------------------------

    .. py:method:: can_assign_assessments():
        Tests if this user can alter assessment/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_assessments_to_bank(bank_id):
        Tests if this user can alter assessment/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bank_ids(bank_id):
        Gets a list of banks including and under the given banks node in which any assessment can be
            assigned.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (osid.id.IdList) - list of assignable bank ``Ids``
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bank_ids_for_assessment(bank_id, assessment_id):
        Gets a list of bank including and under the given bank node in which a specific assessment
            can be assigned.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        :return: (osid.id.IdList) - list of assignable bank ``Ids``
        :raises:  NullArgument - ``bank_id`` or ``assessment_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_assessment_to_bank(assessment_id, bank_id):
        Adds an existing ``Assessment`` to a ``Bank``.

        :arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :raises:  AlreadyExists - ``assessment_id`` is already assigned to
                ``bank_id``
        :raises:  NotFound - ``assessment_id`` or ``bank_id`` not found
        :raises:  NullArgument - ``assessment_id`` or ``bank_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_assessment_from_bank(assessment_id, bank_id):
        Removes an ``Assessment`` from a ``Bank``.

        :arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :raises:  NotFound - ``assessment_id`` or ``bank_id`` not found or
                ``assessment_id`` not assigned to ``bank_id``
        :raises:  NullArgument - ``assessment_id`` or ``bank_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: reassign_assessment_to_billing(assessment_id, from_bank_id, to_bank_id):
        Moves an ``Assessment`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        :arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        :arg:    from_bank_id (osid.id.Id): the ``Id`` of the current
                ``Bank``
        :arg:    to_bank_id (osid.id.Id): the ``Id`` of the destination
                ``Bank``
        :raises:  NotFound - ``assessment_id, from_bank_id,`` or
                ``to_bank_id`` not found or ``assessment_id`` not mapped
                to ``from_bank_id``
        :raises:  NullArgument - ``assessment_id, from_bank_id,`` or
                ``to_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Assessment Offered Bank Methods
-------------------------------

    .. py:method:: can_lookup_assessment_offered_bank_mappings():
        Tests if this user can perform lookups of assessment offered/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_bank_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bank_view():
        A complete view of the ``AssessmentOffered`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_assessment_offered_ids_by_bank(bank_id):
        Gets the list of ``AssessmentOffered``  ``Ids`` associated with a ``Bank``.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.id.IdList) - list of related assessment offered
                ``Ids``
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_offered_by_bank(bank_id):
        Gets the list of ``AssessmentOffereds`` associated with a ``Bank``.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.assessment.AssessmentOfferedList) - list of
                related assessments offered
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessment_offered_ids_by_banks(bank_ids):
        Gets the list of ``AssessmentOffered Ids`` corresponding to a list of ``Banks``.

        :arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        :return: (osid.id.IdList) - list of bank ``Ids``
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_offered_by_banks(bank_ids):
        Gets the list of ``AssessmentOffered`` objects corresponding to a list of ``Banks``.

        :arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        :return: (osid.assessment.AssessmentOfferedList) - list of
                assessments offered
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bank_ids_by_assessment_offered(assessment_offered_id):
        Gets the list of ``Bank``  ``Ids`` mapped to an ``AssessmentOffered``.

        :arg:    assessment_offered_id (osid.id.Id): ``Id`` of an
                ``AssessmentOffered``
        :return: (osid.id.IdList) - list of bank ``Ids``
        :raises:  NotFound - ``assessment_offered_id`` is not found
        :raises:  NullArgument - ``assessment_offered_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks_by_assessment_offered(assessment_offered_id):
        Gets the list of ``Banks`` mapped to an ``AssessmentOffered``.

        :arg:    assessment_offered_id (osid.id.Id): ``Id`` of an
                ``AssessmentOffered``
        :return: (osid.assessment.BankList) - list of banks
        :raises:  NotFound - ``assessment_offered_id`` is not found
        :raises:  NullArgument - ``assessment_offered_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*






Assessment Offered Bank Assignment Methods
------------------------------------------

    .. py:method:: can_assign_assessments_offered():
        Tests if this user can alter assessment offered/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_assessments_offered_to_bank(bank_id):
        Tests if this user can alter assessment offered/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bank_ids(bank_id):
        Gets a list of banks including and under the given banks node in which any assessment
            offered can be assigned.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (osid.id.IdList) - list of assignable bank ``Ids``
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bank_ids_for_assessment_offered(bank_id, assessment_offered_id):
        Gets a list of bank including and under the given bank node in which a specific assessment
            offered can be assigned.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                ``AssessmentOffered``
        :return: (osid.id.IdList) - list of assignable bank ``Ids``
        :raises:  NullArgument - ``bank_id`` or ``assessment_offered_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_assessment_offered_to_bank(assessment_offered_id, bank_id):
        Adds an existing ``AssessmentOffered`` to a ``Bank``.

        :arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                ``AssessmentOffered``
        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :raises:  AlreadyExists - ``assessment_offered_id`` is already
                assigned to ``bank_id``
        :raises:  NotFound - ``assessment_offered_id`` or ``bank_id`` not
                found
        :raises:  NullArgument - ``assessment_offered_id`` or ``bank_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_assessment_offered_from_bank(assessment_offered_id, bank_id):
        Removes an ``AssessmentOffered`` from a ``Bank``.

        :arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                ``AssessmentOffered``
        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :raises:  NotFound - ``assessment_offered_id`` or ``bank_id`` not
                found or ``assessment_offered_id`` not assigned to
                ``bank_id``
        :raises:  NullArgument - ``assessment_offered_id`` or ``bank_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: reassign_assessment_offered_to_billing(assessment_offered_id, from_bank_id, to_bank_id):
        Moves an ``AssessmentOffered`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        :arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                ``AssessmentOffered``
        :arg:    from_bank_id (osid.id.Id): the ``Id`` of the current
                ``Bank``
        :arg:    to_bank_id (osid.id.Id): the ``Id`` of the destination
                ``Bank``
        :raises:  NotFound - ``assessment_offered_id, from_bank_id,`` or
                ``to_bank_id`` not found or ``assessment_offered_id``
                not mapped to ``from_bank_id``
        :raises:  NullArgument - ``assessment_offered_id, from_bank_id,``
                or ``to_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Assessment Taken Bank Methods
-----------------------------

    .. py:method:: can_lookup_assessment_taken_bank_mappings():
        Tests if this user can perform lookups of assessment taken/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_bank_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bank_view():
        A complete view of the ``AssessmentTaken`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_assessment_taken_ids_by_bank(bank_id):
        Gets the list of ``AssessmentTaken``  ``Ids`` associated with a ``Bank``.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.id.IdList) - list of related assessment taken
                ``Ids``
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_by_bank(bank_id):
        Gets the list of ``AssessmentTakens`` associated with a ``Bank``.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.assessment.AssessmentTakenList) - list of related
                assessments taken
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessment_taken_ids_by_banks(bank_ids):
        Gets the list of ``AssessmentTaken Ids`` corresponding to a list of ``Banks``.

        :arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        :return: (osid.id.IdList) - list of bank ``Ids``
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_by_banks(bank_ids):
        Gets the list of ``AssessmentTaken`` objects corresponding to a list of ``Banks``.

        :arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        :return: (osid.assessment.AssessmentTakenList) - list of
                assessments taken
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bank_ids_by_assessment_taken(assessment_taken_id):
        Gets the list of ``Bank``  ``Ids`` mapped to an ``AssessmentTaken``.

        :arg:    assessment_taken_id (osid.id.Id): ``Id`` of an
                ``AssessmentTaken``
        :return: (osid.id.IdList) - list of bank ``Ids``
        :raises:  NotFound - ``assessment_taken_id`` is not found
        :raises:  NullArgument - ``assessment_taken_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks_by_assessment_taken(assessment_taken_id):
        Gets the list of ``Banks`` mapped to an ``AssessmentTaken``.

        :arg:    assessment_taken_id (osid.id.Id): ``Id`` of an
                ``AssessmentTaken``
        :return: (osid.assessment.BankList) - list of banks
        :raises:  NotFound - ``assessment_taken_id`` is not found
        :raises:  NullArgument - ``assessment_taken_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*






Assessment Taken Bank Assignment Methods
----------------------------------------

    .. py:method:: can_assign_assessments_taken():
        Tests if this user can alter assessment taken/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_assessments_taken_to_bank(bank_id):
        Tests if this user can alter assessment taken/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bank_ids(bank_id):
        Gets a list of banks including and under the given banks node in which any assessment taken
            can be assigned.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (osid.id.IdList) - list of assignable bank ``Ids``
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bank_ids_for_assessment_taken(bank_id, assessment_taken_id):
        Gets a list of bank including and under the given bank node in which a specific assessment
            taken can be assigned.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :arg:    assessment_taken_id (osid.id.Id): the ``Id`` of the
                ``AssessmentTaken``
        :return: (osid.id.IdList) - list of assignable bank ``Ids``
        :raises:  NullArgument - ``bank_id`` or ``assessment_taken_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_assessment_taken_to_bank(assessment_taken_id, bank_id):
        Adds an existing ``AssessmentTaken`` to a ``Bank``.

        :arg:    assessment_taken_id (osid.id.Id): the ``Id`` of the
                ``AssessmentTaken``
        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :raises:  AlreadyExists - ``assessment_taken_id`` is already
                assigned to ``bank_id``
        :raises:  NotFound - ``assessment_taken_id`` or ``bank_id`` not
                found
        :raises:  NullArgument - ``assessment_taken_id`` or ``bank_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_assessment_taken_from_bank(assessment_taken_id, bank_id):
        Removes an ``AssessmentTaken`` from a ``Bank``.

        :arg:    assessment_taken_id (osid.id.Id): the ``Id`` of the
                ``AssessmentTaken``
        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :raises:  NotFound - ``assessment_taken_id`` or ``bank_id`` not
                found or ``assessment_taken_id`` not assigned to
                ``bank_id``
        :raises:  NullArgument - ``assessment_taken_id`` or ``bank_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: reassign_assessment_taken_to_billing(assessment_taken_id, from_bank_id, to_bank_id):
        Moves an ``AssessmentTaken`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        :arg:    assessment_taken_id (osid.id.Id): the ``Id`` of the
                ``AssessmentTaken``
        :arg:    from_bank_id (osid.id.Id): the ``Id`` of the current
                ``Bank``
        :arg:    to_bank_id (osid.id.Id): the ``Id`` of the destination
                ``Bank``
        :raises:  NotFound - ``assessment_taken_id, from_bank_id,`` or
                ``to_bank_id`` not found or ``assessment_taken_id`` not
                mapped to ``from_bank_id``
        :raises:  NullArgument - ``assessment_taken_id, from_bank_id,`` or
                ``to_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Bank Lookup Methods
-------------------

    .. py:method:: can_lookup_banks():
        Tests if this user can perform ``Bank`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_bank_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bank_view():
        A complete view of the ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_bank(bank_id):
        Gets the ``Bank`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Bank`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Bank`` and retained for compatibility.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.assessment.Bank) - the bank
        :raises:  NotFound - ``bank_id`` not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_banks_by_ids(bank_ids):
        Gets a ``BankList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the banks
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Bank`` objects may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :arg:    bank_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.assessment.BankList) - the returned ``Bank`` list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks_by_genus_type(bank_genus_type):
        Gets a ``BankList`` corresponding to the given bank genus ``Type`` which does not include
            banks of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :arg:    bank_genus_type (osid.type.Type): a bank genus type
        :return: (osid.assessment.BankList) - the returned ``Bank`` list
        :raises:  NullArgument - ``bank_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks_by_parent_genus_type(bank_genus_type):
        Gets a ``BankList`` corresponding to the given bank genus ``Type`` and include any
            additional banks with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :arg:    bank_genus_type (osid.type.Type): a bank genus type
        :return: (osid.assessment.BankList) - the returned ``Bank`` list
        :raises:  NullArgument - ``bank_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks_by_record_type(bank_record_type):
        Gets a ``BankList`` containing the given bank record ``Type``.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :arg:    bank_record_type (osid.type.Type): a bank record type
        :return: (osid.assessment.BankList) - the returned ``Bank`` list
        :raises:  NullArgument - ``bank_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks_by_provider(resource_id):
        Gets a ``BankList`` from the given provider ````.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.assessment.BankList) - the returned ``Bank`` list
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks():
        Gets all ``Banks``.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :return: (osid.assessment.BankList) - a ``BankList``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: banks




Bank Query Methods
------------------

    .. py:method:: can_search_banks():
        Tests if this user can perform ``Bank`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bank_query():
        Gets a bank query.

        :return: (osid.assessment.BankQuery) - a bank query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_query


    .. py:method:: get_banks_by_query(bank_query):
        Gets a list of ``Bank`` objects matching the given bank query.

        :arg:    bank_query (osid.assessment.BankQuery): the bank query
        :return: (osid.assessment.BankList) - the returned ``BankList``
        :raises:  NullArgument - ``bank_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``bank_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*






Bank Admin Methods
------------------

    .. py:method:: can_create_banks():
        Tests if this user can create ``Banks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Bank`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_bank_with_record_types(bank_record_types):
        Tests if this user can create a single ``Bank`` using the desired record types.

        While ``AssessmentManager.getBankRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Bank``.
        Providing an empty array tests if a ``Bank`` can be created with
        no records.

        :arg:    bank_record_types (osid.type.Type[]): array of bank
                record types
        :return: (boolean) - ``true`` if ``Bank`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        :raises:  NullArgument - ``bank_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bank_form_for_create(bank_record_types):
        Gets the bank form for creating new banks.

        A new form should be requested for each create transaction.

        :arg:    bank_record_types (osid.type.Type[]): array of bank
                record types to be included in the create operation or
                an empty list if none
        :return: (osid.assessment.BankForm) - the bank form
        :raises:  NullArgument - ``bank_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_bank(bank_form):
        Creates a new ``Bank``.

        :arg:    bank_form (osid.assessment.BankForm): the form for this
                ``Bank``
        :return: (osid.assessment.Bank) - the new ``Bank``
        :raises:  IllegalState - ``bank_form`` already used in a create
                transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``bank_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``bank_form`` did not originate from
                ``get_bank_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_banks():
        Tests if this user can update ``Banks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Bank`` modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bank_form_for_update(bank_id):
        Gets the bank form for updating an existing bank.

        A new bank form should be requested for each update transaction.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (osid.assessment.BankForm) - the bank form
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_bank(bank_form):
        Updates an existing bank.

        :arg:    bank_form (osid.assessment.BankForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``bank_form`` already used in an update
                transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``bank_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``bank_form`` did not originate from
                ``get_bank_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_banks():
        Tests if this user can delete banks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Bank`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_bank(bank_id):
        Deletes a ``Bank``.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank`` to
                remove
        :raises:  NotFound - ``bank_id`` not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_bank_aliases():
        Tests if this user can manage ``Id`` aliases for ``Banks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Bank`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_bank(bank_id, alias_id):
        Adds an ``Id`` to a ``Bank`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Bank`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another bank, it is reassigned to the
        given bank ``Id``.

        :arg:    bank_id (osid.id.Id): the ``Id`` of a ``Bank``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is in use as a primary
                ``Id``
        :raises:  NotFound - ``bank_id`` not found
        :raises:  NullArgument - ``bank_id`` or ``alias_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*






Bank Hierarchy Methods
----------------------

    .. py:method:: get_bank_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_hierarchy_id


    .. py:method:: get_bank_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_hierarchy


    .. py:method:: can_access_bank_hierarchy():
        Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_bank_view():
        The returns from the bank methods may omit or translate elements based on this session, such
            as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bank_view():
        A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_root_bank_ids():
        Gets the root bank ``Ids`` in this hierarchy.

        :return: (osid.id.IdList) - the root bank ``Ids``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: root_bank_ids


    .. py:method:: get_root_banks():
        Gets the root banks in this bank hierarchy.

        :return: (osid.assessment.BankList) - the root banks
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method is must be implemented.*




    .. py:attribute:: root_banks


    .. py:method:: has_parent_banks(bank_id):
        Tests if the ``Bank`` has any parents.

        :arg:    bank_id (osid.id.Id): a bank ``Id``
        :return: (boolean) - ``true`` if the bank has parents, ``false``
                otherwise
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_parent_of_bank(id_, bank_id):
        Tests if an ``Id`` is a direct parent of a bank.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :return: (boolean) - ``true`` if this ``id`` is a parent of
                ``bank_id,``  ``false`` otherwise
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``id`` or ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_parent_bank_ids(bank_id):
        Gets the parent ``Ids`` of the given bank.

        :arg:    bank_id (osid.id.Id): a bank ``Id``
        :return: (osid.id.IdList) - the parent ``Ids`` of the bank
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_parent_banks(bank_id):
        Gets the parents of the given bank.

        :arg:    bank_id (osid.id.Id): a bank ``Id``
        :return: (osid.assessment.BankList) - the parents of the bank
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_ancestor_of_bank(id_, bank_id):
        Tests if an ``Id`` is an ancestor of a bank.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``bank_id,``  ``false`` otherwise
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: has_child_banks(bank_id):
        Tests if a bank has any children.

        :arg:    bank_id (osid.id.Id): a ``bank_id``
        :return: (boolean) - ``true`` if the ``bank_id`` has children,
                ``false`` otherwise
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_child_of_bank(id_, bank_id):
        Tests if a bank is a direct child of another.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :return: (boolean) - ``true`` if the ``id`` is a child of
                ``bank_id,``  ``false`` otherwise
        :raises:  NotFound - ``bank_id`` not found
        :raises:  NullArgument - ``bank_id`` or ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_child_bank_ids(bank_id):
        Gets the child ``Ids`` of the given bank.

        :arg:    bank_id (osid.id.Id): the ``Id`` to query
        :return: (osid.id.IdList) - the children of the bank
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_child_banks(bank_id):
        Gets the children of the given bank.

        :arg:    bank_id (osid.id.Id): the ``Id`` to query
        :return: (osid.assessment.BankList) - the children of the bank
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_descendant_of_bank(id_, bank_id):
        Tests if an ``Id`` is a descendant of a bank.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``bank_id,``  ``false`` otherwise
        :raises:  NotFound - ``bank_id`` not found
        :raises:  NullArgument - ``bank_id`` or ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.




    .. py:method:: get_bank_node_ids(bank_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given bank.

        :arg:    bank_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.hierarchy.Node) - a bank node
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bank_nodes(bank_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given bank.

        :arg:    bank_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.assessment.BankNode) - a bank node
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Bank Hierarchy Design Methods
-----------------------------

    .. py:method:: get_bank_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_hierarchy_id


    .. py:method:: get_bank_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_hierarchy


    .. py:method:: can_modify_bank_hierarchy():
        Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_root_bank(bank_id):
        Adds a root bank.

        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :raises:  AlreadyExists - ``bank_id`` is already in hierarchy
        :raises:  NotFound - ``bank_id`` not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_root_bank(bank_id):
        Removes a root bank from this hierarchy.

        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :raises:  NotFound - ``bank_id`` not a parent of ``child_id``
        :raises:  NullArgument - ``bank_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_child_bank(bank_id, child_id):
        Adds a child to a bank.

        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  AlreadyExists - ``bank_id`` is already a parent of
                ``child_id``
        :raises:  NotFound - ``bank_id`` or ``child_id`` not found
        :raises:  NullArgument - ``bank_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_bank(bank_id, child_id):
        Removes a child from a bank.

        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  NotFound - ``bank_id`` not parent of ``child_id``
        :raises:  NullArgument - ``bank_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_banks(bank_id):
        Removes all children from a bank.

        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :raises:  NotFound - ``bank_id`` is not in hierarchy
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*






Assessment Proxy Manager
------------------------

.. py:class:: AssessmentProxyManager(osid_managers.OsidProxyManager, AssessmentProfile, assessment_managers.AssessmentProxyManager)
    The assessment manager provides access to assessment sessions and provides interoperability
        tests
    for various aspects of this service.


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





    .. py:method:: get_my_assessment_taken_session(proxy):
        :noindex:


    .. py:method:: get_my_assessment_taken_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_session(proxy):
        :noindex:


    .. py:method:: get_assessment_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_results_session(proxy):
        :noindex:


    .. py:method:: get_assessment_results_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_item_lookup_session(proxy):
        :noindex:


    .. py:method:: get_item_lookup_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_item_query_session(proxy):
        :noindex:


    .. py:method:: get_item_query_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_item_search_session(proxy):
        :noindex:


    .. py:method:: get_item_search_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_item_admin_session(proxy):
        :noindex:


    .. py:method:: get_item_admin_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_item_notification_session(item_receiver, proxy):
        :noindex:


    .. py:method:: get_item_notification_session_for_bank(item_receiver, bank_id, proxy):
        :noindex:


    .. py:method:: get_item_bank_session(proxy):
        :noindex:


    .. py:method:: get_item_bank_assignment_session(proxy):
        :noindex:


    .. py:method:: get_item_smart_bank_session(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_lookup_session(proxy):
        :noindex:


    .. py:method:: get_assessment_lookup_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_query_session(proxy):
        :noindex:


    .. py:method:: get_assessment_query_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_search_session(proxy):
        :noindex:


    .. py:method:: get_assessment_search_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_admin_session(proxy):
        :noindex:


    .. py:method:: get_assessment_admin_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_notification_session(assessment_receiver, proxy):
        :noindex:


    .. py:method:: get_assessment_notification_session_for_bank(assessment_receiver, bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_bank_session(proxy):
        :noindex:


    .. py:method:: get_assessment_bank_assignment_session(proxy):
        :noindex:


    .. py:method:: get_assessment_smart_bank_session(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_basic_authoring_session(proxy):
        :noindex:


    .. py:method:: get_assessment_basic_authoring_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_offered_lookup_session(proxy):
        :noindex:


    .. py:method:: get_assessment_offered_lookup_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_offered_query_session(proxy):
        :noindex:


    .. py:method:: get_assessment_offered_query_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_offered_search_session(proxy):
        :noindex:


    .. py:method:: get_assessment_offered_search_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_offered_admin_session(proxy):
        :noindex:


    .. py:method:: get_assessment_offered_admin_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_offered_notification_session(assessment_offered_receiver, proxy):
        :noindex:


    .. py:method:: get_assessment_offered_notification_session_for_bank(assessment_offered_receiver, bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_offered_bank_session(proxy):
        :noindex:


    .. py:method:: get_assessment_offered_bank_assignment_session(proxy):
        :noindex:


    .. py:method:: get_assessment_offered_smart_bank_session(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_taken_lookup_session(proxy):
        :noindex:


    .. py:method:: get_assessment_taken_lookup_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_taken_query_session(proxy):
        :noindex:


    .. py:method:: get_assessment_taken_query_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_taken_search_session(proxy):
        :noindex:


    .. py:method:: get_assessment_taken_search_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_taken_admin_session(proxy):
        :noindex:


    .. py:method:: get_assessment_taken_admin_session_for_bank(bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_taken_notification_session(assessment_taken_receiver, proxy):
        :noindex:


    .. py:method:: get_assessment_taken_notification_session_for_bank(assessment_taken_receiver, bank_id, proxy):
        :noindex:


    .. py:method:: get_assessment_taken_bank_session(proxy):
        :noindex:


    .. py:method:: get_assessment_taken_bank_assignment_session(proxy):
        :noindex:


    .. py:method:: get_assessment_taken_smart_bank_session(bank_id, proxy):
        :noindex:


    .. py:method:: get_bank_lookup_session(proxy):
        :noindex:


    .. py:method:: get_bank_query_session(proxy):
        :noindex:


    .. py:method:: get_bank_search_session(proxy):
        :noindex:


    .. py:method:: get_bank_admin_session(proxy):
        :noindex:


    .. py:method:: get_bank_notification_session(bank_receiver, proxy):
        :noindex:


    .. py:method:: get_bank_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_bank_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_assessment_authoring_proxy_manager():
        :noindex:


    .. py:attribute:: assessment_authoring_proxy_manager
        :noindex:


    .. py:method:: get_assessment_batch_proxy_manager():
        :noindex:


    .. py:attribute:: assessment_batch_proxy_manager
        :noindex:




Item Bank Methods
-----------------

    .. py:method:: can_lookup_item_bank_mappings():
        Tests if this user can perform lookups of item/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_bank_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bank_view():
        A complete view of the ``Item`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_item_ids_by_bank(bank_id):
        Gets the list of ``Item``  ``Ids`` associated with a ``Bank``.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.id.IdList) - list of related item ``Ids``
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_items_by_bank(bank_id):
        Gets the list of ``Items`` associated with a ``Bank``.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.assessment.ItemList) - list of related items
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_item_ids_by_banks(bank_ids):
        Gets the list of ``Item Ids`` corresponding to a list of ``Banks``.

        :arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        :return: (osid.id.IdList) - list of bank ``Ids``
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_items_by_banks(bank_ids):
        Gets the list of ``Items`` corresponding to a list of ``Banks``.

        :arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        :return: (osid.assessment.ItemList) - list of items
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bank_ids_by_item(item_id):
        Gets the list of ``Bank``  ``Ids`` mapped to an ``Item``.

        :arg:    item_id (osid.id.Id): ``Id`` of an ``Item``
        :return: (osid.id.IdList) - list of bank ``Ids``
        :raises:  NotFound - ``item_id`` is not found
        :raises:  NullArgument - ``item_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks_by_item(item_id):
        Gets the list of ``Banks`` mapped to an ``Item``.

        :arg:    item_id (osid.id.Id): ``Id`` of an ``Item``
        :return: (osid.assessment.BankList) - list of banks
        :raises:  NotFound - ``item_id`` is not found
        :raises:  NullArgument - ``item_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*






Item Bank Assignment Methods
----------------------------

    .. py:method:: can_assign_items():
        Tests if this user can alter item/bank mappings.

        A return of true does not guarantee successful assessment. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_items_to_bank(bank_id):
        Tests if this user can alter item/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bank_ids(bank_id):
        Gets a list of banks including and under the given bank node in which any item can be
            assigned.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (osid.id.IdList) - list of assignable bank ``Ids``
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bank_ids_for_item(bank_id, item_id):
        Gets a list of banks including and under the given bank node in which a specific item can be
            assigned.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        :return: (osid.id.IdList) - list of assignable bank ``Ids``
        :raises:  NullArgument - ``bank_id`` or ``item_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_item_to_bank(item_id, bank_id):
        Adds an existing ``Item`` to a ``Bank``.

        :arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :raises:  AlreadyExists - ``item_id`` is already assigned to
                ``bank_id``
        :raises:  NotFound - ``item_id`` or ``bank_id`` not found
        :raises:  NullArgument - ``item_id`` or ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_item_from_bank(item_id, bank_id):
        Removes an ``Item`` from a ``Bank``.

        :arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :raises:  NotFound - ``item_id`` or ``bank_id`` not found or
                ``item_id`` not assigned to ``bank_id``
        :raises:  NullArgument - ``item_id`` or ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: reassign_item_to_billing(item_id, from_bank_id, to_bank_id):
        Moves an ``Item`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        :arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        :arg:    from_bank_id (osid.id.Id): the ``Id`` of the current
                ``Bank``
        :arg:    to_bank_id (osid.id.Id): the ``Id`` of the destination
                ``Bank``
        :raises:  NotFound - ``item_id, from_bank_id,`` or ``to_bank_id``
                not found or ``item_id`` not mapped to ``from_bank_id``
        :raises:  NullArgument - ``item_id, from_bank_id,`` or
                ``to_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Assessment Bank Methods
-----------------------

    .. py:method:: can_lookup_assessment_bank_mappings():
        Tests if this user can perform lookups of assessment/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_bank_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bank_view():
        A complete view of the ``Assessment`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_assessment_ids_by_bank(bank_id):
        Gets the list of ``Assessment``  ``Ids`` associated with a ``Bank``.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.id.IdList) - list of related assessment ``Ids``
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_by_bank(bank_id):
        Gets the list of ``Assessments`` associated with a ``Bank``.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.assessment.AssessmentList) - list of related
                assessments
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessment_ids_by_banks(bank_ids):
        Gets the list of ``Assessment Ids`` corresponding to a list of ``Banks``.

        :arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        :return: (osid.id.IdList) - list of bank ``Ids``
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_by_banks(bank_ids):
        Gets the list of ``Assessments`` corresponding to a list of ``Banks``.

        :arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        :return: (osid.assessment.AssessmentList) - list of assessments
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bank_ids_by_assessment(assessment_id):
        Gets the list of ``Bank``  ``Ids`` mapped to an ``Assessment``.

        :arg:    assessment_id (osid.id.Id): ``Id`` of an ``Assessment``
        :return: (osid.id.IdList) - list of bank ``Ids``
        :raises:  NotFound - ``assessment_id`` is not found
        :raises:  NullArgument - ``assessment_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks_by_assessment(assessment_id):
        Gets the list of ``Banks`` mapped to an ``Assessment``.

        :arg:    assessment_id (osid.id.Id): ``Id`` of an ``Assessment``
        :return: (osid.assessment.BankList) - list of banks
        :raises:  NotFound - ``assessment_id`` is not found
        :raises:  NullArgument - ``assessment_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*






Assessment Bank Assignment Methods
----------------------------------

    .. py:method:: can_assign_assessments():
        Tests if this user can alter assessment/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_assessments_to_bank(bank_id):
        Tests if this user can alter assessment/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bank_ids(bank_id):
        Gets a list of banks including and under the given banks node in which any assessment can be
            assigned.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (osid.id.IdList) - list of assignable bank ``Ids``
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bank_ids_for_assessment(bank_id, assessment_id):
        Gets a list of bank including and under the given bank node in which a specific assessment
            can be assigned.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        :return: (osid.id.IdList) - list of assignable bank ``Ids``
        :raises:  NullArgument - ``bank_id`` or ``assessment_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_assessment_to_bank(assessment_id, bank_id):
        Adds an existing ``Assessment`` to a ``Bank``.

        :arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :raises:  AlreadyExists - ``assessment_id`` is already assigned to
                ``bank_id``
        :raises:  NotFound - ``assessment_id`` or ``bank_id`` not found
        :raises:  NullArgument - ``assessment_id`` or ``bank_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_assessment_from_bank(assessment_id, bank_id):
        Removes an ``Assessment`` from a ``Bank``.

        :arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :raises:  NotFound - ``assessment_id`` or ``bank_id`` not found or
                ``assessment_id`` not assigned to ``bank_id``
        :raises:  NullArgument - ``assessment_id`` or ``bank_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: reassign_assessment_to_billing(assessment_id, from_bank_id, to_bank_id):
        Moves an ``Assessment`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        :arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        :arg:    from_bank_id (osid.id.Id): the ``Id`` of the current
                ``Bank``
        :arg:    to_bank_id (osid.id.Id): the ``Id`` of the destination
                ``Bank``
        :raises:  NotFound - ``assessment_id, from_bank_id,`` or
                ``to_bank_id`` not found or ``assessment_id`` not mapped
                to ``from_bank_id``
        :raises:  NullArgument - ``assessment_id, from_bank_id,`` or
                ``to_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Assessment Offered Bank Methods
-------------------------------

    .. py:method:: can_lookup_assessment_offered_bank_mappings():
        Tests if this user can perform lookups of assessment offered/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_bank_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bank_view():
        A complete view of the ``AssessmentOffered`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_assessment_offered_ids_by_bank(bank_id):
        Gets the list of ``AssessmentOffered``  ``Ids`` associated with a ``Bank``.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.id.IdList) - list of related assessment offered
                ``Ids``
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_offered_by_bank(bank_id):
        Gets the list of ``AssessmentOffereds`` associated with a ``Bank``.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.assessment.AssessmentOfferedList) - list of
                related assessments offered
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessment_offered_ids_by_banks(bank_ids):
        Gets the list of ``AssessmentOffered Ids`` corresponding to a list of ``Banks``.

        :arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        :return: (osid.id.IdList) - list of bank ``Ids``
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_offered_by_banks(bank_ids):
        Gets the list of ``AssessmentOffered`` objects corresponding to a list of ``Banks``.

        :arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        :return: (osid.assessment.AssessmentOfferedList) - list of
                assessments offered
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bank_ids_by_assessment_offered(assessment_offered_id):
        Gets the list of ``Bank``  ``Ids`` mapped to an ``AssessmentOffered``.

        :arg:    assessment_offered_id (osid.id.Id): ``Id`` of an
                ``AssessmentOffered``
        :return: (osid.id.IdList) - list of bank ``Ids``
        :raises:  NotFound - ``assessment_offered_id`` is not found
        :raises:  NullArgument - ``assessment_offered_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks_by_assessment_offered(assessment_offered_id):
        Gets the list of ``Banks`` mapped to an ``AssessmentOffered``.

        :arg:    assessment_offered_id (osid.id.Id): ``Id`` of an
                ``AssessmentOffered``
        :return: (osid.assessment.BankList) - list of banks
        :raises:  NotFound - ``assessment_offered_id`` is not found
        :raises:  NullArgument - ``assessment_offered_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*






Assessment Offered Bank Assignment Methods
------------------------------------------

    .. py:method:: can_assign_assessments_offered():
        Tests if this user can alter assessment offered/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_assessments_offered_to_bank(bank_id):
        Tests if this user can alter assessment offered/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bank_ids(bank_id):
        Gets a list of banks including and under the given banks node in which any assessment
            offered can be assigned.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (osid.id.IdList) - list of assignable bank ``Ids``
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bank_ids_for_assessment_offered(bank_id, assessment_offered_id):
        Gets a list of bank including and under the given bank node in which a specific assessment
            offered can be assigned.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                ``AssessmentOffered``
        :return: (osid.id.IdList) - list of assignable bank ``Ids``
        :raises:  NullArgument - ``bank_id`` or ``assessment_offered_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_assessment_offered_to_bank(assessment_offered_id, bank_id):
        Adds an existing ``AssessmentOffered`` to a ``Bank``.

        :arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                ``AssessmentOffered``
        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :raises:  AlreadyExists - ``assessment_offered_id`` is already
                assigned to ``bank_id``
        :raises:  NotFound - ``assessment_offered_id`` or ``bank_id`` not
                found
        :raises:  NullArgument - ``assessment_offered_id`` or ``bank_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_assessment_offered_from_bank(assessment_offered_id, bank_id):
        Removes an ``AssessmentOffered`` from a ``Bank``.

        :arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                ``AssessmentOffered``
        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :raises:  NotFound - ``assessment_offered_id`` or ``bank_id`` not
                found or ``assessment_offered_id`` not assigned to
                ``bank_id``
        :raises:  NullArgument - ``assessment_offered_id`` or ``bank_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: reassign_assessment_offered_to_billing(assessment_offered_id, from_bank_id, to_bank_id):
        Moves an ``AssessmentOffered`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        :arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                ``AssessmentOffered``
        :arg:    from_bank_id (osid.id.Id): the ``Id`` of the current
                ``Bank``
        :arg:    to_bank_id (osid.id.Id): the ``Id`` of the destination
                ``Bank``
        :raises:  NotFound - ``assessment_offered_id, from_bank_id,`` or
                ``to_bank_id`` not found or ``assessment_offered_id``
                not mapped to ``from_bank_id``
        :raises:  NullArgument - ``assessment_offered_id, from_bank_id,``
                or ``to_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Assessment Taken Bank Methods
-----------------------------

    .. py:method:: can_lookup_assessment_taken_bank_mappings():
        Tests if this user can perform lookups of assessment taken/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_bank_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bank_view():
        A complete view of the ``AssessmentTaken`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_assessment_taken_ids_by_bank(bank_id):
        Gets the list of ``AssessmentTaken``  ``Ids`` associated with a ``Bank``.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.id.IdList) - list of related assessment taken
                ``Ids``
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_by_bank(bank_id):
        Gets the list of ``AssessmentTakens`` associated with a ``Bank``.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.assessment.AssessmentTakenList) - list of related
                assessments taken
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessment_taken_ids_by_banks(bank_ids):
        Gets the list of ``AssessmentTaken Ids`` corresponding to a list of ``Banks``.

        :arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        :return: (osid.id.IdList) - list of bank ``Ids``
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_by_banks(bank_ids):
        Gets the list of ``AssessmentTaken`` objects corresponding to a list of ``Banks``.

        :arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        :return: (osid.assessment.AssessmentTakenList) - list of
                assessments taken
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bank_ids_by_assessment_taken(assessment_taken_id):
        Gets the list of ``Bank``  ``Ids`` mapped to an ``AssessmentTaken``.

        :arg:    assessment_taken_id (osid.id.Id): ``Id`` of an
                ``AssessmentTaken``
        :return: (osid.id.IdList) - list of bank ``Ids``
        :raises:  NotFound - ``assessment_taken_id`` is not found
        :raises:  NullArgument - ``assessment_taken_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks_by_assessment_taken(assessment_taken_id):
        Gets the list of ``Banks`` mapped to an ``AssessmentTaken``.

        :arg:    assessment_taken_id (osid.id.Id): ``Id`` of an
                ``AssessmentTaken``
        :return: (osid.assessment.BankList) - list of banks
        :raises:  NotFound - ``assessment_taken_id`` is not found
        :raises:  NullArgument - ``assessment_taken_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*






Assessment Taken Bank Assignment Methods
----------------------------------------

    .. py:method:: can_assign_assessments_taken():
        Tests if this user can alter assessment taken/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_assessments_taken_to_bank(bank_id):
        Tests if this user can alter assessment taken/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bank_ids(bank_id):
        Gets a list of banks including and under the given banks node in which any assessment taken
            can be assigned.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (osid.id.IdList) - list of assignable bank ``Ids``
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bank_ids_for_assessment_taken(bank_id, assessment_taken_id):
        Gets a list of bank including and under the given bank node in which a specific assessment
            taken can be assigned.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :arg:    assessment_taken_id (osid.id.Id): the ``Id`` of the
                ``AssessmentTaken``
        :return: (osid.id.IdList) - list of assignable bank ``Ids``
        :raises:  NullArgument - ``bank_id`` or ``assessment_taken_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_assessment_taken_to_bank(assessment_taken_id, bank_id):
        Adds an existing ``AssessmentTaken`` to a ``Bank``.

        :arg:    assessment_taken_id (osid.id.Id): the ``Id`` of the
                ``AssessmentTaken``
        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :raises:  AlreadyExists - ``assessment_taken_id`` is already
                assigned to ``bank_id``
        :raises:  NotFound - ``assessment_taken_id`` or ``bank_id`` not
                found
        :raises:  NullArgument - ``assessment_taken_id`` or ``bank_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_assessment_taken_from_bank(assessment_taken_id, bank_id):
        Removes an ``AssessmentTaken`` from a ``Bank``.

        :arg:    assessment_taken_id (osid.id.Id): the ``Id`` of the
                ``AssessmentTaken``
        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :raises:  NotFound - ``assessment_taken_id`` or ``bank_id`` not
                found or ``assessment_taken_id`` not assigned to
                ``bank_id``
        :raises:  NullArgument - ``assessment_taken_id`` or ``bank_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: reassign_assessment_taken_to_billing(assessment_taken_id, from_bank_id, to_bank_id):
        Moves an ``AssessmentTaken`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        :arg:    assessment_taken_id (osid.id.Id): the ``Id`` of the
                ``AssessmentTaken``
        :arg:    from_bank_id (osid.id.Id): the ``Id`` of the current
                ``Bank``
        :arg:    to_bank_id (osid.id.Id): the ``Id`` of the destination
                ``Bank``
        :raises:  NotFound - ``assessment_taken_id, from_bank_id,`` or
                ``to_bank_id`` not found or ``assessment_taken_id`` not
                mapped to ``from_bank_id``
        :raises:  NullArgument - ``assessment_taken_id, from_bank_id,`` or
                ``to_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Bank Lookup Methods
-------------------

    .. py:method:: can_lookup_banks():
        Tests if this user can perform ``Bank`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_bank_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bank_view():
        A complete view of the ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_bank(bank_id):
        Gets the ``Bank`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Bank`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Bank`` and retained for compatibility.

        :arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        :return: (osid.assessment.Bank) - the bank
        :raises:  NotFound - ``bank_id`` not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_banks_by_ids(bank_ids):
        Gets a ``BankList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the banks
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Bank`` objects may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :arg:    bank_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.assessment.BankList) - the returned ``Bank`` list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks_by_genus_type(bank_genus_type):
        Gets a ``BankList`` corresponding to the given bank genus ``Type`` which does not include
            banks of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :arg:    bank_genus_type (osid.type.Type): a bank genus type
        :return: (osid.assessment.BankList) - the returned ``Bank`` list
        :raises:  NullArgument - ``bank_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks_by_parent_genus_type(bank_genus_type):
        Gets a ``BankList`` corresponding to the given bank genus ``Type`` and include any
            additional banks with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :arg:    bank_genus_type (osid.type.Type): a bank genus type
        :return: (osid.assessment.BankList) - the returned ``Bank`` list
        :raises:  NullArgument - ``bank_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks_by_record_type(bank_record_type):
        Gets a ``BankList`` containing the given bank record ``Type``.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :arg:    bank_record_type (osid.type.Type): a bank record type
        :return: (osid.assessment.BankList) - the returned ``Bank`` list
        :raises:  NullArgument - ``bank_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks_by_provider(resource_id):
        Gets a ``BankList`` from the given provider ````.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.assessment.BankList) - the returned ``Bank`` list
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_banks():
        Gets all ``Banks``.

        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :return: (osid.assessment.BankList) - a ``BankList``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: banks




Bank Query Methods
------------------

    .. py:method:: can_search_banks():
        Tests if this user can perform ``Bank`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bank_query():
        Gets a bank query.

        :return: (osid.assessment.BankQuery) - a bank query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_query


    .. py:method:: get_banks_by_query(bank_query):
        Gets a list of ``Bank`` objects matching the given bank query.

        :arg:    bank_query (osid.assessment.BankQuery): the bank query
        :return: (osid.assessment.BankList) - the returned ``BankList``
        :raises:  NullArgument - ``bank_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``bank_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*






Bank Admin Methods
------------------

    .. py:method:: can_create_banks():
        Tests if this user can create ``Banks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Bank`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_bank_with_record_types(bank_record_types):
        Tests if this user can create a single ``Bank`` using the desired record types.

        While ``AssessmentManager.getBankRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Bank``.
        Providing an empty array tests if a ``Bank`` can be created with
        no records.

        :arg:    bank_record_types (osid.type.Type[]): array of bank
                record types
        :return: (boolean) - ``true`` if ``Bank`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        :raises:  NullArgument - ``bank_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bank_form_for_create(bank_record_types):
        Gets the bank form for creating new banks.

        A new form should be requested for each create transaction.

        :arg:    bank_record_types (osid.type.Type[]): array of bank
                record types to be included in the create operation or
                an empty list if none
        :return: (osid.assessment.BankForm) - the bank form
        :raises:  NullArgument - ``bank_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_bank(bank_form):
        Creates a new ``Bank``.

        :arg:    bank_form (osid.assessment.BankForm): the form for this
                ``Bank``
        :return: (osid.assessment.Bank) - the new ``Bank``
        :raises:  IllegalState - ``bank_form`` already used in a create
                transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``bank_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``bank_form`` did not originate from
                ``get_bank_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_banks():
        Tests if this user can update ``Banks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Bank`` modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bank_form_for_update(bank_id):
        Gets the bank form for updating an existing bank.

        A new bank form should be requested for each update transaction.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        :return: (osid.assessment.BankForm) - the bank form
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_bank(bank_form):
        Updates an existing bank.

        :arg:    bank_form (osid.assessment.BankForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``bank_form`` already used in an update
                transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``bank_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``bank_form`` did not originate from
                ``get_bank_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_banks():
        Tests if this user can delete banks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Bank`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_bank(bank_id):
        Deletes a ``Bank``.

        :arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank`` to
                remove
        :raises:  NotFound - ``bank_id`` not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_bank_aliases():
        Tests if this user can manage ``Id`` aliases for ``Banks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Bank`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_bank(bank_id, alias_id):
        Adds an ``Id`` to a ``Bank`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Bank`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another bank, it is reassigned to the
        given bank ``Id``.

        :arg:    bank_id (osid.id.Id): the ``Id`` of a ``Bank``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is in use as a primary
                ``Id``
        :raises:  NotFound - ``bank_id`` not found
        :raises:  NullArgument - ``bank_id`` or ``alias_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*






Bank Hierarchy Methods
----------------------

    .. py:method:: get_bank_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_hierarchy_id


    .. py:method:: get_bank_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_hierarchy


    .. py:method:: can_access_bank_hierarchy():
        Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_bank_view():
        The returns from the bank methods may omit or translate elements based on this session, such
            as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bank_view():
        A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_root_bank_ids():
        Gets the root bank ``Ids`` in this hierarchy.

        :return: (osid.id.IdList) - the root bank ``Ids``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: root_bank_ids


    .. py:method:: get_root_banks():
        Gets the root banks in this bank hierarchy.

        :return: (osid.assessment.BankList) - the root banks
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method is must be implemented.*




    .. py:attribute:: root_banks


    .. py:method:: has_parent_banks(bank_id):
        Tests if the ``Bank`` has any parents.

        :arg:    bank_id (osid.id.Id): a bank ``Id``
        :return: (boolean) - ``true`` if the bank has parents, ``false``
                otherwise
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_parent_of_bank(id_, bank_id):
        Tests if an ``Id`` is a direct parent of a bank.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :return: (boolean) - ``true`` if this ``id`` is a parent of
                ``bank_id,``  ``false`` otherwise
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``id`` or ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_parent_bank_ids(bank_id):
        Gets the parent ``Ids`` of the given bank.

        :arg:    bank_id (osid.id.Id): a bank ``Id``
        :return: (osid.id.IdList) - the parent ``Ids`` of the bank
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_parent_banks(bank_id):
        Gets the parents of the given bank.

        :arg:    bank_id (osid.id.Id): a bank ``Id``
        :return: (osid.assessment.BankList) - the parents of the bank
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_ancestor_of_bank(id_, bank_id):
        Tests if an ``Id`` is an ancestor of a bank.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``bank_id,``  ``false`` otherwise
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: has_child_banks(bank_id):
        Tests if a bank has any children.

        :arg:    bank_id (osid.id.Id): a ``bank_id``
        :return: (boolean) - ``true`` if the ``bank_id`` has children,
                ``false`` otherwise
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_child_of_bank(id_, bank_id):
        Tests if a bank is a direct child of another.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :return: (boolean) - ``true`` if the ``id`` is a child of
                ``bank_id,``  ``false`` otherwise
        :raises:  NotFound - ``bank_id`` not found
        :raises:  NullArgument - ``bank_id`` or ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_child_bank_ids(bank_id):
        Gets the child ``Ids`` of the given bank.

        :arg:    bank_id (osid.id.Id): the ``Id`` to query
        :return: (osid.id.IdList) - the children of the bank
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_child_banks(bank_id):
        Gets the children of the given bank.

        :arg:    bank_id (osid.id.Id): the ``Id`` to query
        :return: (osid.assessment.BankList) - the children of the bank
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_descendant_of_bank(id_, bank_id):
        Tests if an ``Id`` is a descendant of a bank.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``bank_id,``  ``false`` otherwise
        :raises:  NotFound - ``bank_id`` not found
        :raises:  NullArgument - ``bank_id`` or ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.




    .. py:method:: get_bank_node_ids(bank_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given bank.

        :arg:    bank_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.hierarchy.Node) - a bank node
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bank_nodes(bank_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given bank.

        :arg:    bank_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.assessment.BankNode) - a bank node
        :raises:  NotFound - ``bank_id`` is not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Bank Hierarchy Design Methods
-----------------------------

    .. py:method:: get_bank_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_hierarchy_id


    .. py:method:: get_bank_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_hierarchy


    .. py:method:: can_modify_bank_hierarchy():
        Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_root_bank(bank_id):
        Adds a root bank.

        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :raises:  AlreadyExists - ``bank_id`` is already in hierarchy
        :raises:  NotFound - ``bank_id`` not found
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_root_bank(bank_id):
        Removes a root bank from this hierarchy.

        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :raises:  NotFound - ``bank_id`` not a parent of ``child_id``
        :raises:  NullArgument - ``bank_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_child_bank(bank_id, child_id):
        Adds a child to a bank.

        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  AlreadyExists - ``bank_id`` is already a parent of
                ``child_id``
        :raises:  NotFound - ``bank_id`` or ``child_id`` not found
        :raises:  NullArgument - ``bank_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_bank(bank_id, child_id):
        Removes a child from a bank.

        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  NotFound - ``bank_id`` not parent of ``child_id``
        :raises:  NullArgument - ``bank_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_banks(bank_id):
        Removes all children from a bank.

        :arg:    bank_id (osid.id.Id): the ``Id`` of a bank
        :raises:  NotFound - ``bank_id`` is not in hierarchy
        :raises:  NullArgument - ``bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*






