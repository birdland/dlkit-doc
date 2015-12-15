

Sessions
========


Assessment Session
------------------

.. py:class:: AssessmentSession(abc_assessment_sessions.AssessmentSession, osid_sessions.OsidSession)
    This session is used to take an assessment.


    The assessment associated with this session represents the
    "assessment taken" by an ``Agent``. This session may be created
    using an ``AssessmentOffered`` ``Id`` retrieved from an assessment
    bank, and instantiating this session represents the transaction of
    taking an assessment. Resuming an assessment, if permitted, is
    performed through instantiating this session with the
    ``AssessmentTaken`` ``Id``.




    ``Assessment Items`` are accessed via the ``Question`` interface. A
    ``Question``  ``Id`` is the same as the ``Item`` Id.




    This session manages the flow of control for the assessment taking
    process. It allows for two types of processes:




      * synchronous response: Each consecutive question is only
        available after the previous item was submitted or skipped.
      * asynchronous response: Questions may be accessed independently
        of response submission.








    It may be the case that it is allowed to suspend and resume an
    assessment. ``can_suspend()`` indicates the availability of this
    feature. ``finished()`` indicates the assessment is complete.




    This session is used in the context of an ``AssessmentSection``. An
    assessment with no sections defined is assumed to have a single
    default section that maps to the entire assessment.





    .. py:method:: get_bank_id():
        :noindex:


    .. py:attribute:: bank_id
        :noindex:


    .. py:method:: get_bank():
        :noindex:


    .. py:attribute:: bank
        :noindex:


    .. py:method:: can_take_assessments():
        :noindex:


    .. py:method:: has_assessment_begun(assessment_taken_id):
        :noindex:


    .. py:method:: is_assessment_over(assessment_taken_id):
        :noindex:


    .. py:method:: requires_synchronous_sections(assessment_taken_id):
        :noindex:


    .. py:method:: get_first_assessment_section(assessment_taken_id):
        :noindex:


    .. py:method:: has_next_assessment_section(assessment_section_id):
        :noindex:


    .. py:method:: get_next_assessment_section(assessment_section_id):
        :noindex:


    .. py:method:: has_previous_assessment_section(assessment_section_id):
        :noindex:


    .. py:method:: get_previous_assessment_section(assessment_section_id):
        :noindex:


    .. py:method:: get_assessment_section(assessment_section_id):
        :noindex:


    .. py:method:: get_assessment_sections(assessment_taken_id):
        :noindex:


    .. py:method:: is_assessment_section_complete(assessment_section_id):
        :noindex:


    .. py:method:: get_incomplete_assessment_sections(assessment_taken_id):
        :noindex:


    .. py:method:: has_assessment_section_begun(assessment_section_id):
        :noindex:


    .. py:method:: is_assessment_section_over(assessment_section_id):
        :noindex:


    .. py:method:: requires_synchronous_responses(assessment_section_id):
        :noindex:


    .. py:method:: get_first_question(assessment_section_id):
        :noindex:


    .. py:method:: has_next_question(assessment_section_id, item_id):
        :noindex:


    .. py:method:: get_next_question(assessment_section_id, item_id):
        :noindex:


    .. py:method:: has_previous_question(assessment_section_id, item_id):
        :noindex:


    .. py:method:: get_previous_question(assessment_section_id, item_id):
        :noindex:


    .. py:method:: get_question(assessment_section_id, item_id):
        :noindex:


    .. py:method:: get_questions(assessment_section_id):
        :noindex:


    .. py:method:: get_response_form(assessment_section_id, item_id):
        :noindex:


    .. py:method:: submit_response(assessment_section_id, item_id, answer_form):
        :noindex:


    .. py:method:: skip_item(assessment_section_id, item_id):
        :noindex:


    .. py:method:: is_question_answered(assessment_section_id, item_id):
        :noindex:


    .. py:method:: get_unanswered_questions(assessment_section_id):
        :noindex:


    .. py:method:: has_unanswered_questions(assessment_section_id):
        :noindex:


    .. py:method:: get_first_unanswered_question(assessment_section_id):
        :noindex:


    .. py:method:: has_next_unanswered_question(assessment_section_id, item_id):
        :noindex:


    .. py:method:: get_next_unanswered_question(assessment_section_id, item_id):
        :noindex:


    .. py:method:: has_previous_unanswered_question(assessment_section_id, item_id):
        :noindex:


    .. py:method:: get_previous_unanswered_question(assessment_section_id, item_id):
        :noindex:


    .. py:method:: get_response(assessment_section_id, item_id):
        :noindex:


    .. py:method:: get_responses(assessment_section_id):
        :noindex:


    .. py:method:: clear_response(assessment_section_id, item_id):
        :noindex:


    .. py:method:: finish_assessment_section(assessment_section_id):
        :noindex:


    .. py:method:: is_answer_available(assessment_section_id, item_id):
        :noindex:


    .. py:method:: get_answers(assessment_section_id, item_id):
        :noindex:


    .. py:method:: finish_assessment(assessment_taken_id):
        :noindex:


Item Lookup Session
-------------------

.. py:class:: ItemLookupSession(abc_assessment_sessions.ItemLookupSession, osid_sessions.OsidSession)
    This session provides methods for retrieving ``Item`` objects.

    .. py:method:: get_bank_id():
        :noindex:


    .. py:attribute:: bank_id
        :noindex:


    .. py:method:: get_bank():
        :noindex:


    .. py:attribute:: bank
        :noindex:


    .. py:method:: can_lookup_items():
        :noindex:


    .. py:method:: use_comparative_item_view():
        :noindex:


    .. py:method:: use_plenary_item_view():
        :noindex:


    .. py:method:: use_federated_bank_view():
        :noindex:


    .. py:method:: use_isolated_bank_view():
        :noindex:


    .. py:method:: get_item(item_id):
        :noindex:


    .. py:method:: get_items_by_ids(item_ids):
        :noindex:


    .. py:method:: get_items_by_genus_type(item_genus_type):
        :noindex:


    .. py:method:: get_items_by_parent_genus_type(item_genus_type):
        :noindex:


    .. py:method:: get_items_by_record_type(item_record_type):
        :noindex:


    .. py:method:: get_items_by_question(question_id):
        :noindex:


    .. py:method:: get_items_by_answer(answer_id):
        :noindex:


    .. py:method:: get_items_by_learning_objective(objective_id):
        :noindex:


    .. py:method:: get_items_by_learning_objectives(objective_ids):
        :noindex:


    .. py:method:: get_items():
        :noindex:


    .. py:attribute:: items
        :noindex:


Item Query Session
------------------

.. py:class:: ItemQuerySession(abc_assessment_sessions.ItemQuerySession, osid_sessions.OsidSession)
    This session provides methods for searching ``Item`` objects.


    The search query is constructed using the ``ItemQuery``. The
    assessment item record ``Type`` also specifies the query record for
    the assessment item query.




    This session defines views that offer differing behaviors for
    searching.




      * federated assessment bank view: searches include assessment
        items in assessment banks of which this assessment bank is a
        ancestor in the assessment bank hierarchy
      * isolated bank








    Assessment items may have a query record indicated by their
    respective record types. Thequery record is accessed via the
    ``ItemQuery``.





    .. py:method:: get_bank_id():
        :noindex:


    .. py:attribute:: bank_id
        :noindex:


    .. py:method:: get_bank():
        :noindex:


    .. py:attribute:: bank
        :noindex:


    .. py:method:: can_search_items():
        :noindex:


    .. py:method:: use_federated_bank_view():
        :noindex:


    .. py:method:: use_isolated_bank_view():
        :noindex:


    .. py:method:: get_item_query():
        :noindex:


    .. py:attribute:: item_query
        :noindex:


    .. py:method:: get_items_by_query(item_query):
        :noindex:


Item Search Session
-------------------

.. py:class:: ItemSearchSession(abc_assessment_sessions.ItemSearchSession, ItemQuerySession)
    This session provides methods for searching ``Item`` objects.


    The search query is constructed using the ``ItemQuery``. The
    assessment item record ``Type`` also specifies the query record for
    the assessment item query.




    ``get_items_by_query()`` is the basic search method and returns a
    list of ``Items``. A more advanced search may be performed with
    ``getItemsBySearch()``. It accepts an ``ItemSearch`` in addition to
    the query for the purpose of specifying additional options affecting
    the entire search, such as ordering. ``get_items_by_search()``
    returns an ``ItemSearchResults`` that can be used to access the
    resulting ``ItemList`` or be used to perform a search within the
    result set through ``ItemSearch``.




    This session defines views that offer differing behaviors for
    searching.




      * federated assessment bank view: searches include assessment
        items in assessment banks of which this assessment bank is a
        ancestor in the assessment bank hierarchy
      * isolated bank view: searches are restricted to assessment items
        in this assessment bank








    Assessment items may have a query record indicated by their
    respective record types. The query record is accessed via the
    ``ItemQuery``.





    .. py:method:: get_item_search():
        :noindex:


    .. py:attribute:: item_search
        :noindex:


    .. py:method:: get_item_search_order():
        :noindex:


    .. py:attribute:: item_search_order
        :noindex:


    .. py:method:: get_items_by_search(item_query, item_search):
        :noindex:


    .. py:method:: get_item_query_from_inspector(item_query_inspector):
        :noindex:


Item Admin Session
------------------

.. py:class:: ItemAdminSession(abc_assessment_sessions.ItemAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``Items``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create an
    ``Item,`` an ``ItemForm`` is requested using
    ``get_item_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``ItemForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``ItemForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``ItemForm`` corresponds
    to an attempted transaction.




    For updates, ``ItemForms`` are requested to the ``ItemForm``  ``Id``
    that is to be updated using ``getItemFormForUpdate()``. Similarly,
    the ``ItemForm`` has metadata about the data that can be updated and
    it can perform validation before submitting the update. The
    ``ItemForm`` can only be used once for a successful update and
    cannot be reused.




    The delete operations delete ``ItemForm``. To unmap an ``ItemForm``
    from the current ``Bank,`` the ``ItemBankAssignmentSession`` should
    be used. These delete operations attempt to remove the ``Item``
    itself thus removing it from all known ``Bank`` catalogs.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: get_bank_id():
        :noindex:


    .. py:attribute:: bank_id
        :noindex:


    .. py:method:: get_bank():
        :noindex:


    .. py:attribute:: bank
        :noindex:


    .. py:method:: can_create_items():
        :noindex:


    .. py:method:: can_create_item_with_record_types(item_record_types):
        :noindex:


    .. py:method:: get_item_form_for_create(item_record_types):
        :noindex:


    .. py:method:: create_item(item_form):
        :noindex:


    .. py:method:: can_update_items():
        :noindex:


    .. py:method:: get_item_form_for_update(item_id):
        :noindex:


    .. py:method:: update_item(item_form):
        :noindex:


    .. py:method:: can_delete_items():
        :noindex:


    .. py:method:: delete_item(item_id):
        :noindex:


    .. py:method:: can_manage_item_aliases():
        :noindex:


    .. py:method:: alias_item(item_id, alias_id):
        :noindex:


    .. py:method:: can_create_questions():
        :noindex:


    .. py:method:: can_create_question_with_record_types(question_record_types):
        :noindex:


    .. py:method:: get_question_form_for_create(item_id, question_record_types):
        :noindex:


    .. py:method:: create_question(question_form):
        :noindex:


    .. py:method:: can_update_questions():
        :noindex:


    .. py:method:: get_question_form_for_update(question_id):
        :noindex:


    .. py:method:: update_question(question_form):
        :noindex:


    .. py:method:: can_delete_questions():
        :noindex:


    .. py:method:: delete_question(question_id):
        :noindex:


    .. py:method:: can_create_answers():
        :noindex:


    .. py:method:: can_create_answers_with_record_types(answer_record_types):
        :noindex:


    .. py:method:: get_answer_form_for_create(item_id, answer_record_types):
        :noindex:


    .. py:method:: create_answer(answer_form):
        :noindex:


    .. py:method:: can_update_answers():
        :noindex:


    .. py:method:: get_answer_form_for_update(answer_id):
        :noindex:


    .. py:method:: update_answer(answer_form):
        :noindex:


    .. py:method:: can_delete_answers():
        :noindex:


    .. py:method:: delete_answer(answer_id):
        :noindex:


Item Notification Session
-------------------------

.. py:class:: ItemNotificationSession(abc_assessment_sessions.ItemNotificationSession, osid_sessions.OsidSession)
    This session defines methods to receive asynchronous notifications on adds/changes to ``Item``
    objects.


    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.




    The two views defined in this session correspond to the views in the
    ``ItemLookupSession``.





    .. py:method:: get_bank_id():
        :noindex:


    .. py:attribute:: bank_id
        :noindex:


    .. py:method:: get_bank():
        :noindex:


    .. py:attribute:: bank
        :noindex:


    .. py:method:: can_register_for_item_notifications():
        :noindex:


    .. py:method:: use_federated_bank_view():
        :noindex:


    .. py:method:: use_isolated_bank_view():
        :noindex:


    .. py:method:: reliable_item_notifications():
        :noindex:


    .. py:method:: unreliable_item_notifications():
        :noindex:


    .. py:method:: acknowledge_item_notification(notification_id):
        :noindex:


    .. py:method:: register_for_new_items():
        :noindex:


    .. py:method:: register_for_changed_items():
        :noindex:


    .. py:method:: register_for_changed_item(item_id):
        :noindex:


    .. py:method:: register_for_deleted_items():
        :noindex:


    .. py:method:: register_for_deleted_item(item_id):
        :noindex:


    .. py:method:: reliable_item_notifications():
        :noindex:


    .. py:method:: unreliable_item_notifications():
        :noindex:


    .. py:method:: acknowledge_item_notification(notification_id):
        :noindex:


Item Bank Session
-----------------

.. py:class:: ItemBankSession(abc_assessment_sessions.ItemBankSession, osid_sessions.OsidSession)
    This session provides methods to retrieve ``Item`` to ``Bank`` mappings.


    An ``Item`` may appear in multiple ``Banks``. Each ``Bank`` may have
    its own authorizations governing who is allowed to look at it.




    This lookup session defines two views:




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition





    .. py:method:: can_lookup_item_bank_mappings():
        :noindex:


    .. py:method:: use_comparative_bank_view():
        :noindex:


    .. py:method:: use_plenary_bank_view():
        :noindex:


    .. py:method:: get_item_ids_by_bank(bank_id):
        :noindex:


    .. py:method:: get_items_by_bank(bank_id):
        :noindex:


    .. py:method:: get_item_ids_by_banks(bank_ids):
        :noindex:


    .. py:method:: get_items_by_banks(bank_ids):
        :noindex:


    .. py:method:: get_bank_ids_by_item(item_id):
        :noindex:


    .. py:method:: get_banks_by_item(item_id):
        :noindex:


Item Bank Assignment Session
----------------------------

.. py:class:: ItemBankAssignmentSession(abc_assessment_sessions.ItemBankAssignmentSession, osid_sessions.OsidSession)
    This session provides methods to re-assign ``Items`` to ``Banks``.


    An ``Item`` may map to multiple ``Banks`` and removing the last
    reference to an ``Item`` is the equivalent of deleting it. Each
    ``Bank`` may have its own authorizations governing who is allowed to
    operate on it.




    Moving or adding a reference of an ``Item`` to another ``Bank`` is
    not a copy operation (eg: does not change its ``Id`` ).





    .. py:method:: can_assign_items():
        :noindex:


    .. py:method:: can_assign_items_to_bank(bank_id):
        :noindex:


    .. py:method:: get_assignable_bank_ids(bank_id):
        :noindex:


    .. py:method:: get_assignable_bank_ids_for_item(bank_id, item_id):
        :noindex:


    .. py:method:: assign_item_to_bank(item_id, bank_id):
        :noindex:


    .. py:method:: unassign_item_from_bank(item_id, bank_id):
        :noindex:


    .. py:method:: reassign_item_to_billing(item_id, from_bank_id, to_bank_id):
        :noindex:


Assessment Lookup Session
-------------------------

.. py:class:: AssessmentLookupSession(abc_assessment_sessions.AssessmentLookupSession, osid_sessions.OsidSession)
    This session defines methods for retrieving assessments.

    .. py:method:: get_bank_id():
        :noindex:


    .. py:attribute:: bank_id
        :noindex:


    .. py:method:: get_bank():
        :noindex:


    .. py:attribute:: bank
        :noindex:


    .. py:method:: can_lookup_assessments():
        :noindex:


    .. py:method:: use_comparative_assessment_view():
        :noindex:


    .. py:method:: use_plenary_assessment_view():
        :noindex:


    .. py:method:: use_federated_bank_view():
        :noindex:


    .. py:method:: use_isolated_bank_view():
        :noindex:


    .. py:method:: get_assessment(assessment_id):
        :noindex:


    .. py:method:: get_assessments_by_ids(assessment_ids):
        :noindex:


    .. py:method:: get_assessments_by_genus_type(assessment_genus_type):
        :noindex:


    .. py:method:: get_assessments_by_parent_genus_type(assessment_genus_type):
        :noindex:


    .. py:method:: get_assessments_by_record_type(assessment_record_type):
        :noindex:


    .. py:method:: get_assessments():
        :noindex:


    .. py:attribute:: assessments
        :noindex:


Assessment Query Session
------------------------

.. py:class:: AssessmentQuerySession(abc_assessment_sessions.AssessmentQuerySession, osid_sessions.OsidSession)
    This session provides methods for querying ``Assessment`` objects.


    The search query is constructed using the ``AssessmentQuery``.




    This session defines views that offer differing behaviors for
    searching.




      * federated bank view: searches include assessments in banks of
        which this bank is a ancestor in the bank hierarchy
      * isolated bank view: searches are restricted to assessments in
        this bank








    Assessments may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``AssessmentQuery``. The returns in this session may not be cast
    directly to these interfaces.





    .. py:method:: get_bank_id():
        :noindex:


    .. py:attribute:: bank_id
        :noindex:


    .. py:method:: get_bank():
        :noindex:


    .. py:attribute:: bank
        :noindex:


    .. py:method:: can_search_assessments():
        :noindex:


    .. py:method:: use_federated_bank_view():
        :noindex:


    .. py:method:: use_isolated_bank_view():
        :noindex:


    .. py:method:: get_assessment_query():
        :noindex:


    .. py:attribute:: assessment_query
        :noindex:


    .. py:method:: get_assessments_by_query(assessment_query):
        :noindex:


Assessment Admin Session
------------------------

.. py:class:: AssessmentAdminSession(abc_assessment_sessions.AssessmentAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``Assessments``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create an
    ``Assessment,`` an ``AssessmentForm`` is requested using
    ``get_assessment_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``AssessmentForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``AssessmentForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``AssessmentForm``
    corresponds to an attempted transaction.




    For updates, ``AssessmentForms`` are requested to the ``Assessment``
    ``Id`` that is to be updated using ``getAssessmentFormForUpdate()``.
    Similarly, the ``AssessmentForm`` has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ``AssessmentForm`` can only be used once for a
    successful update and cannot be reused.




    The delete operations delete ``Assessments``. To unmap an
    ``Assessment`` from the current ``Bank,`` the
    ``AssessmentBankAssignmentSession`` should be used. These delete
    operations attempt to remove the ``Assessment`` itself thus removing
    it from all known ``Bank`` catalogs.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: get_bank_id():
        :noindex:


    .. py:attribute:: bank_id
        :noindex:


    .. py:method:: get_bank():
        :noindex:


    .. py:attribute:: bank
        :noindex:


    .. py:method:: can_create_assessments():
        :noindex:


    .. py:method:: can_create_assessment_with_record_types(assessment_record_types):
        :noindex:


    .. py:method:: get_assessment_form_for_create(assessment_record_types):
        :noindex:


    .. py:method:: create_assessment(assessment_form):
        :noindex:


    .. py:method:: can_update_assessments():
        :noindex:


    .. py:method:: get_assessment_form_for_update(assessment_id):
        :noindex:


    .. py:method:: update_assessment(assessment_form):
        :noindex:


    .. py:method:: can_delete_assessments():
        :noindex:


    .. py:method:: delete_assessment(assessment_id):
        :noindex:


    .. py:method:: can_manage_assessment_aliases():
        :noindex:


    .. py:method:: alias_assessment(assessment_id, alias_id):
        :noindex:


Assessment Bank Session
-----------------------

.. py:class:: AssessmentBankSession(abc_assessment_sessions.AssessmentBankSession, osid_sessions.OsidSession)
    This session provides methods to retrieve ``Assessment`` to ``Bank`` mappings.


    An ``Assessment`` may appear in multiple ``Banks``. Each ``Bank``
    may have its own authorizations governing who is allowed to look at
    it.




    This lookup session defines two views:




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition





    .. py:method:: can_lookup_assessment_bank_mappings():
        :noindex:


    .. py:method:: use_comparative_bank_view():
        :noindex:


    .. py:method:: use_plenary_bank_view():
        :noindex:


    .. py:method:: get_assessment_ids_by_bank(bank_id):
        :noindex:


    .. py:method:: get_assessments_by_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_ids_by_banks(bank_ids):
        :noindex:


    .. py:method:: get_assessments_by_banks(bank_ids):
        :noindex:


    .. py:method:: get_bank_ids_by_assessment(assessment_id):
        :noindex:


    .. py:method:: get_banks_by_assessment(assessment_id):
        :noindex:


Assessment Bank Assignment Session
----------------------------------

.. py:class:: AssessmentBankAssignmentSession(abc_assessment_sessions.AssessmentBankAssignmentSession, osid_sessions.OsidSession)
    This session provides methods to re-assign ``Assessments`` to ``Banks``.


    An ``Assessment`` may map to multiple ``Banks`` and removing the
    last reference to an ``Assessment`` is the equivalent of deleting
    it. Each ``Bank`` may have its own authorizations governing who is
    allowed to operate on it.




    Moving or adding a reference of an ``Assessment`` to another
    ``Bank`` is not a copy operation (eg: does not change its ``Id`` ).





    .. py:method:: can_assign_assessments():
        :noindex:


    .. py:method:: can_assign_assessments_to_bank(bank_id):
        :noindex:


    .. py:method:: get_assignable_bank_ids(bank_id):
        :noindex:


    .. py:method:: get_assignable_bank_ids_for_assessment(bank_id, assessment_id):
        :noindex:


    .. py:method:: assign_assessment_to_bank(assessment_id, bank_id):
        :noindex:


    .. py:method:: unassign_assessment_from_bank(assessment_id, bank_id):
        :noindex:


    .. py:method:: reassign_assessment_to_billing(assessment_id, from_bank_id, to_bank_id):
        :noindex:


Assessment Basic Authoring Session
----------------------------------

.. py:class:: AssessmentBasicAuthoringSession(abc_assessment_sessions.AssessmentBasicAuthoringSession, osid_sessions.OsidSession)
    This session defines methods to manage assessment items in an assessment.


    This session is used for simple assessments without sections or
    parts. Updating the items on an assessment authored with sections
    and parts may result in an error.





    .. py:method:: get_bank_id():
        :noindex:


    .. py:attribute:: bank_id
        :noindex:


    .. py:method:: get_bank():
        :noindex:


    .. py:attribute:: bank
        :noindex:


    .. py:method:: can_author_assessments():
        :noindex:


    .. py:method:: get_items(assessment_id):
        :noindex:


    .. py:method:: add_item(assessment_id, item_id):
        :noindex:


    .. py:method:: remove_item(assessment_id, item_id):
        :noindex:


    .. py:method:: move_item(assessment_id, item_id, preceeding_item_id):
        :noindex:


    .. py:method:: order_items(item_ids, assessment_id):
        :noindex:


Assessment Offered Lookup Session
---------------------------------

.. py:class:: AssessmentOfferedLookupSession(abc_assessment_sessions.AssessmentOfferedLookupSession, osid_sessions.OsidSession)
    This session defines methods for retrieving assessments offered.

    .. py:method:: get_bank_id():
        :noindex:


    .. py:attribute:: bank_id
        :noindex:


    .. py:method:: get_bank():
        :noindex:


    .. py:attribute:: bank
        :noindex:


    .. py:method:: can_lookup_assessments_offered():
        :noindex:


    .. py:method:: use_comparative_assessment_offered_view():
        :noindex:


    .. py:method:: use_plenary_assessment_offered_view():
        :noindex:


    .. py:method:: use_federated_bank_view():
        :noindex:


    .. py:method:: use_isolated_bank_view():
        :noindex:


    .. py:method:: get_assessment_offered(assessment_offered_id):
        :noindex:


    .. py:method:: get_assessments_offered_by_ids(assessment_offered_ids):
        :noindex:


    .. py:method:: get_assessments_offered_by_genus_type(assessment_offered_genus_type):
        :noindex:


    .. py:method:: get_assessments_offered_by_parent_genus_type(assessment_offered_genus_type):
        :noindex:


    .. py:method:: get_assessments_offered_by_record_type(assessment_record_type):
        :noindex:


    .. py:method:: get_assessments_offered_by_date(start, end):
        :noindex:


    .. py:method:: get_assessments_offered_for_assessment(assessment_id):
        :noindex:


    .. py:method:: get_assessments_offered():
        :noindex:


    .. py:attribute:: assessments_offered
        :noindex:


Assessment Offered Query Session
--------------------------------

.. py:class:: AssessmentOfferedQuerySession(abc_assessment_sessions.AssessmentOfferedQuerySession, osid_sessions.OsidSession)
    This session provides methods for querying ``AssessmentOffered`` objects.


    The search query is constructed using the
    ``AssessmentOfferedQuery``.




    This session defines views that offer differing behaviors for
    searching.




      * federated bank view: searches include assessments offered in
        banks of which this bank is a ancestor in the bank hierarchy
      * isolated bank view: searches are restricted to assessments
        offered in this bank








    Asessments offered may have a query record indicated by their
    respective record types. The query record is accessed via the
    ``AssessmentOfferedQuery``. The returns in this session may not be
    cast directly to these interfaces.





    .. py:method:: get_bank_id():
        :noindex:


    .. py:attribute:: bank_id
        :noindex:


    .. py:method:: get_bank():
        :noindex:


    .. py:attribute:: bank
        :noindex:


    .. py:method:: can_search_assessments_offered():
        :noindex:


    .. py:method:: use_federated_bank_view():
        :noindex:


    .. py:method:: use_isolated_bank_view():
        :noindex:


    .. py:method:: get_assessment_offered_query():
        :noindex:


    .. py:attribute:: assessment_offered_query
        :noindex:


    .. py:method:: get_assessments_offered_by_query(assessment_offered_query):
        :noindex:


Assessment Offered Admin Session
--------------------------------

.. py:class:: AssessmentOfferedAdminSession(abc_assessment_sessions.AssessmentOfferedAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``AssessmentsOffered``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create an
    ``AssessmentOffered,`` an ``AssessmentOfferedForm`` is requested
    using ``get_assessment_offered_form_for_create()`` specifying the
    assessment and desired record ``Types`` or none if no record
    ``Types`` are needed. The returned ``AssessmentOfferedForm`` will
    indicate that it is to be used with a create operation and can be
    used to examine metdata or validate data prior to creation. Once the
    ``AssessmentOfferedForm`` is submiited to a create operation, it
    cannot be reused with another create operation unless the first
    operation was unsuccessful. Each ``AssessmentOfferedForm``
    corresponds to an attempted transaction.




    For updates, ``AssessmentOfferedForms`` are requested to the
    ``AssessmentOffered``  ``Id`` that is to be updated using
    ``getAssessmentOfferedFormForUpdate()``. Similarly, the
    ``AssessmentOfferedForm`` has metadata about the data that can be
    updated and it can perform validation before submitting the update.
    The ``AssessmentOfferedForm`` can only be used once for a successful
    update and cannot be reused.




    The delete operations delete ``AssessmentsOffered``. To unmap an
    ``AssessmentOffered`` from the current ``Bank,`` the
    ``AssessmentOfferedBankAssignmentSession`` should be used. These
    delete operations attempt to remove the ``AssessmentOffered`` itself
    thus removing it from all known ``Bank`` catalogs.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: get_bank_id():
        :noindex:


    .. py:attribute:: bank_id
        :noindex:


    .. py:method:: get_bank():
        :noindex:


    .. py:attribute:: bank
        :noindex:


    .. py:method:: can_create_assessments_offered():
        :noindex:


    .. py:method:: can_create_assessment_offered_with_record_types(assessment_offered_record_types):
        :noindex:


    .. py:method:: get_assessment_offered_form_for_create(assessment_id, assessment_offered_record_types):
        :noindex:


    .. py:method:: create_assessment_offered(assessment_offered_form):
        :noindex:


    .. py:method:: can_update_assessments_offered():
        :noindex:


    .. py:method:: get_assessment_offered_form_for_update(assessment_offered_id):
        :noindex:


    .. py:method:: update_assessment_offered(assessment_offered_form):
        :noindex:


    .. py:method:: can_delete_assessments_offered():
        :noindex:


    .. py:method:: delete_assessment_offered(assessment_offered_id):
        :noindex:


    .. py:method:: can_manage_assessment_offered_aliases():
        :noindex:


    .. py:method:: alias_assessment_offered(assessment_offered_id, alias_id):
        :noindex:


Assessment Offered Bank Session
-------------------------------

.. py:class:: AssessmentOfferedBankSession(abc_assessment_sessions.AssessmentOfferedBankSession, osid_sessions.OsidSession)
    This session provides methods to retrieve ``AssessmentOffered`` to ``Bank`` mappings.


    An ``AssessmentOffered`` may appear in multiple ``Banks``. Each
    ``Bank`` may have its own authorizations governing who is allowed to
    look at it.




    This lookup session defines two views:




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition





    .. py:method:: can_lookup_assessment_offered_bank_mappings():
        :noindex:


    .. py:method:: use_comparative_bank_view():
        :noindex:


    .. py:method:: use_plenary_bank_view():
        :noindex:


    .. py:method:: get_assessment_offered_ids_by_bank(bank_id):
        :noindex:


    .. py:method:: get_assessments_offered_by_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_offered_ids_by_banks(bank_ids):
        :noindex:


    .. py:method:: get_assessments_offered_by_banks(bank_ids):
        :noindex:


    .. py:method:: get_bank_ids_by_assessment_offered(assessment_offered_id):
        :noindex:


    .. py:method:: get_banks_by_assessment_offered(assessment_offered_id):
        :noindex:


Assessment Offered Bank Assignment Session
------------------------------------------

.. py:class:: AssessmentOfferedBankAssignmentSession(abc_assessment_sessions.AssessmentOfferedBankAssignmentSession, osid_sessions.OsidSession)
    This session provides methods to re-assign ``AssessmentOffered`` objects to ``Banks``.


    An ``AssessmentOffered`` may map to multiple ``Banks`` and removing
    the last reference to an ``AssessmentOffered`` is the equivalent of
    deleting it. Each ``Bank`` may have its own authorizations governing
    who is allowed to operate on it.




    Moving or adding a reference of an ``AssessmentOffered`` to another
    ``Bank`` is not a copy operation (eg: does not change its ``Id`` ).





    .. py:method:: can_assign_assessments_offered():
        :noindex:


    .. py:method:: can_assign_assessments_offered_to_bank(bank_id):
        :noindex:


    .. py:method:: get_assignable_bank_ids(bank_id):
        :noindex:


    .. py:method:: get_assignable_bank_ids_for_assessment_offered(bank_id, assessment_offered_id):
        :noindex:


    .. py:method:: assign_assessment_offered_to_bank(assessment_offered_id, bank_id):
        :noindex:


    .. py:method:: unassign_assessment_offered_from_bank(assessment_offered_id, bank_id):
        :noindex:


    .. py:method:: reassign_assessment_offered_to_billing(assessment_offered_id, from_bank_id, to_bank_id):
        :noindex:


Assessment Taken Lookup Session
-------------------------------

.. py:class:: AssessmentTakenLookupSession(abc_assessment_sessions.AssessmentTakenLookupSession, osid_sessions.OsidSession)
    This session defines methods for retrieving assessments taken.

    .. py:method:: get_bank_id():
        :noindex:


    .. py:attribute:: bank_id
        :noindex:


    .. py:method:: get_bank():
        :noindex:


    .. py:attribute:: bank
        :noindex:


    .. py:method:: can_lookup_assessments_taken():
        :noindex:


    .. py:method:: use_comparative_assessment_taken_view():
        :noindex:


    .. py:method:: use_plenary_assessment_taken_view():
        :noindex:


    .. py:method:: use_federated_bank_view():
        :noindex:


    .. py:method:: use_isolated_bank_view():
        :noindex:


    .. py:method:: get_assessment_taken(assessment_taken_id):
        :noindex:


    .. py:method:: get_assessments_taken_by_ids(assessment_taken_ids):
        :noindex:


    .. py:method:: get_assessments_taken_by_genus_type(assessment_taken_genus_type):
        :noindex:


    .. py:method:: get_assessments_taken_by_parent_genus_type(assessment_taken_genus_type):
        :noindex:


    .. py:method:: get_assessments_taken_by_record_type(assessment_taken_record_type):
        :noindex:


    .. py:method:: get_assessments_taken_by_date(from_, to):
        :noindex:


    .. py:method:: get_assessments_taken_for_taker(resource_id):
        :noindex:


    .. py:method:: get_assessments_taken_by_date_for_taker(resource_id, from_, to):
        :noindex:


    .. py:method:: get_assessments_taken_for_assessment(assessment_id):
        :noindex:


    .. py:method:: get_assessments_taken_by_date_for_assessment(assessment_id, from_, to):
        :noindex:


    .. py:method:: get_assessments_taken_for_taker_and_assessment(resource_id, assessment_id):
        :noindex:


    .. py:method:: get_assessments_taken_by_date_for_taker_and_assessment(resource_id, assessment_id, from_, to):
        :noindex:


    .. py:method:: get_assessments_taken_for_assessment_offered(assessment_offered_id):
        :noindex:


    .. py:method:: get_assessments_taken_by_date_for_assessment_offered(assessment_offered_id, from_, to):
        :noindex:


    .. py:method:: get_assessments_taken_for_taker_and_assessment_offered(resource_id, assessment_offered_id):
        :noindex:


    .. py:method:: get_assessments_taken_by_date_for_taker_and_assessment_offered(resource_id, assessment_offered_id, from_, to):
        :noindex:


    .. py:method:: get_assessments_taken():
        :noindex:


    .. py:attribute:: assessments_taken
        :noindex:


Assessment Taken Query Session
------------------------------

.. py:class:: AssessmentTakenQuerySession(abc_assessment_sessions.AssessmentTakenQuerySession, osid_sessions.OsidSession)
    This session provides methods for searching among ``AssessmentTaken`` objects.


    The search query is constructed using the ``AssessmentTakenQuery``.




    This session defines views that offer differing behaviors for
    searching.




      * federated bank view: searches include assessments taken in banks
        of which this bank is an ancestor in the bank hierarchy
      * isolated bank view: searches are restricted to assessments taken
        in this bank








    Assessments taken may have a query record indicated by their
    respective query record types. The query record is accessed via the
    ``AssessmentTakenQuery``.





    .. py:method:: get_bank_id():
        :noindex:


    .. py:attribute:: bank_id
        :noindex:


    .. py:method:: get_bank():
        :noindex:


    .. py:attribute:: bank
        :noindex:


    .. py:method:: can_search_assessments_taken():
        :noindex:


    .. py:method:: use_federated_bank_view():
        :noindex:


    .. py:method:: use_isolated_bank_view():
        :noindex:


    .. py:method:: get_assessment_taken_query():
        :noindex:


    .. py:attribute:: assessment_taken_query
        :noindex:


    .. py:method:: get_assessments_taken_by_query(assessment_taken_query):
        :noindex:


Assessment Taken Admin Session
------------------------------

.. py:class:: AssessmentTakenAdminSession(abc_assessment_sessions.AssessmentTakenAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``AssessmentsTaken``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create an
    ``AssessmentTaken,`` an ``AssessmentTakenForm`` is requested using
    ``get_assessment_taken_form_for_create()`` specifying the assessment
    offered and desired record ``Types`` or none if no record ``Types``
    are needed. The returned ``AssessmentTakenForm`` will indicate that
    it is to be used with a create operation and can be used to examine
    metdata or validate data prior to creation. Once the
    ``AssessmentTakenForm`` is submiited to a create operation, it
    cannot be reused with another create operation unless the first
    operation was unsuccessful. Each ``AssessmentTakenForm`` corresponds
    to an attempted transaction.




    For updates, ``AssessmentTakenForms`` are requested to the
    ``AssessmentTaken``  ``Id`` that is to be updated using
    ``getAssessmentTakenFormForUpdate()``. Similarly, the
    ``AssessmentTakenForm`` has metadata about the data that can be
    updated and it can perform validation before submitting the update.
    The ``AssessmentTakenForm`` can only be used once for a successful
    update and cannot be reused.




    The delete operations delete ``AssessmentsTaken``. To unmap an
    ``AssessmentTakenForm`` from the current ``Bank,`` the
    ``AssessmentTakenFormBankAssignmentSession`` should be used. These
    delete operations attempt to remove the ``AssessmentTakenForm``
    itself thus removing it from all known ``Bank`` catalogs.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: get_bank_id():
        :noindex:


    .. py:attribute:: bank_id
        :noindex:


    .. py:method:: get_bank():
        :noindex:


    .. py:attribute:: bank
        :noindex:


    .. py:method:: can_create_assessments_taken():
        :noindex:


    .. py:method:: can_create_assessment_taken_with_record_types(assessment_taken_record_types):
        :noindex:


    .. py:method:: get_assessment_taken_form_for_create(assessment_offered_id, assessment_taken_record_types):
        :noindex:


    .. py:method:: create_assessment_taken(assessment_taken_form):
        :noindex:


    .. py:method:: can_update_assessments_taken():
        :noindex:


    .. py:method:: get_assessment_taken_form_for_update(assessment_taken_id):
        :noindex:


    .. py:method:: update_assessment_taken(assessment_taken_form):
        :noindex:


    .. py:method:: can_delete_assessments_taken():
        :noindex:


    .. py:method:: delete_assessment_taken(assessment_taken_id):
        :noindex:


    .. py:method:: can_manage_assessment_taken_aliases():
        :noindex:


    .. py:method:: alias_assessment_taken(assessment_taken_id, alias_id):
        :noindex:


Assessment Taken Bank Session
-----------------------------

.. py:class:: AssessmentTakenBankSession(abc_assessment_sessions.AssessmentTakenBankSession, osid_sessions.OsidSession)
    This session provides methods to retrieve ``AssessmentTaken`` to ``Bank`` mappings.


    An ``AssessmentTaken`` may appear in multiple ``Banks``. Each
    ``Bank`` may have its own authorizations governing who is allowed to
    look at it.




    This lookup session defines two views:




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition





    .. py:method:: can_lookup_assessment_taken_bank_mappings():
        :noindex:


    .. py:method:: use_comparative_bank_view():
        :noindex:


    .. py:method:: use_plenary_bank_view():
        :noindex:


    .. py:method:: get_assessment_taken_ids_by_bank(bank_id):
        :noindex:


    .. py:method:: get_assessments_taken_by_bank(bank_id):
        :noindex:


    .. py:method:: get_assessment_taken_ids_by_banks(bank_ids):
        :noindex:


    .. py:method:: get_assessments_taken_by_banks(bank_ids):
        :noindex:


    .. py:method:: get_bank_ids_by_assessment_taken(assessment_taken_id):
        :noindex:


    .. py:method:: get_banks_by_assessment_taken(assessment_taken_id):
        :noindex:


Assessment Taken Bank Assignment Session
----------------------------------------

.. py:class:: AssessmentTakenBankAssignmentSession(abc_assessment_sessions.AssessmentTakenBankAssignmentSession, osid_sessions.OsidSession)
    This session provides methods to re-assign ``AssessmentTaken`` objects to ``Banks``.


    An ``AssessmentTaken`` may map to multiple ``Banks`` and removing
    the last reference to an ``AssessmentTaken`` is the equivalent of
    deleting it. Each ``Bank`` may have its own authorizations governing
    who is allowed to operate on it.




    Moving or adding a reference of an ``AssessmentTaken`` to another
    ``Bank`` is not a copy operation (eg: does not change its ``Id`` ).





    .. py:method:: can_assign_assessments_taken():
        :noindex:


    .. py:method:: can_assign_assessments_taken_to_bank(bank_id):
        :noindex:


    .. py:method:: get_assignable_bank_ids(bank_id):
        :noindex:


    .. py:method:: get_assignable_bank_ids_for_assessment_taken(bank_id, assessment_taken_id):
        :noindex:


    .. py:method:: assign_assessment_taken_to_bank(assessment_taken_id, bank_id):
        :noindex:


    .. py:method:: unassign_assessment_taken_from_bank(assessment_taken_id, bank_id):
        :noindex:


    .. py:method:: reassign_assessment_taken_to_billing(assessment_taken_id, from_bank_id, to_bank_id):
        :noindex:


Bank Lookup Session
-------------------

.. py:class:: BankLookupSession(abc_assessment_sessions.BankLookupSession, osid_sessions.OsidSession)
    This session provides methods for retrieving ``Bank`` objects.


    The ``Bank`` represents a collection of ``Items`` and
    ``Assessments``.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition








    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Banks`` it can access, without breaking execution.
    However, an administrative application may require all ``Bank``
    elements to be available.




    Banks may have an additional records indicated by their respective
    record types. The record may not be accessed through a cast of the
    ``Bank``.





    .. py:method:: can_lookup_banks():
        :noindex:


    .. py:method:: use_comparative_bank_view():
        :noindex:


    .. py:method:: use_plenary_bank_view():
        :noindex:


    .. py:method:: get_bank(bank_id):
        :noindex:


    .. py:method:: get_banks_by_ids(bank_ids):
        :noindex:


    .. py:method:: get_banks_by_genus_type(bank_genus_type):
        :noindex:


    .. py:method:: get_banks_by_parent_genus_type(bank_genus_type):
        :noindex:


    .. py:method:: get_banks_by_record_type(bank_record_type):
        :noindex:


    .. py:method:: get_banks_by_provider(resource_id):
        :noindex:


    .. py:method:: get_banks():
        :noindex:


    .. py:attribute:: banks
        :noindex:


Bank Query Session
------------------

.. py:class:: BankQuerySession(abc_assessment_sessions.BankQuerySession, osid_sessions.OsidSession)
    This session provides methods for searching among ``Bank`` objects.


    The search query is constructed using the ``BankQuery``.




    Banks may have aquery record indicated by their respective record
    types. The query record is accessed via the ``BankQuery``.





    .. py:method:: can_search_banks():
        :noindex:


    .. py:method:: get_bank_query():
        :noindex:


    .. py:attribute:: bank_query
        :noindex:


    .. py:method:: get_banks_by_query(bank_query):
        :noindex:


Bank Admin Session
------------------

.. py:class:: BankAdminSession(abc_assessment_sessions.BankAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``Banks``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create a
    ``Bank,`` a ``BankForm`` is requested using
    ``get_bank_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``BankForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``BankForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``BankForm`` corresponds
    to an attempted transaction.




    For updates, ``BankForms`` are requested to the ``Bank``  ``Id``
    that is to be updated using ``getBankFormForUpdate()``. Similarly,
    the ``BankForm`` has metadata about the data that can be updated and
    it can perform validation before submitting the update. The
    ``BankForm`` can only be used once for a successful update and
    cannot be reused.




    The delete operations delete ``Banks``.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: can_create_banks():
        :noindex:


    .. py:method:: can_create_bank_with_record_types(bank_record_types):
        :noindex:


    .. py:method:: get_bank_form_for_create(bank_record_types):
        :noindex:


    .. py:method:: create_bank(bank_form):
        :noindex:


    .. py:method:: can_update_banks():
        :noindex:


    .. py:method:: get_bank_form_for_update(bank_id):
        :noindex:


    .. py:method:: update_bank(bank_form):
        :noindex:


    .. py:method:: can_delete_banks():
        :noindex:


    .. py:method:: delete_bank(bank_id):
        :noindex:


    .. py:method:: can_manage_bank_aliases():
        :noindex:


    .. py:method:: alias_bank(bank_id, alias_id):
        :noindex:


Bank Hierarchy Session
----------------------

.. py:class:: BankHierarchySession(abc_assessment_sessions.BankHierarchySession, osid_sessions.OsidSession)
    This session defines methods for traversing a hierarchy of ``Bank`` objects.


    Each node in the hierarchy is a unique ``Bank``. The hierarchy may
    be traversed recursively to establish the tree structure through
    ``get_parent_banks()`` and ``getChildBanks()``. To relate these
    ``Ids`` to another OSID, ``get_bank_nodes()`` can be used for
    retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Bank`` available in the Assessment OSID is known to this hierarchy
    but does not appear in the hierarchy traversal until added as a root
    node or a child of another node.




    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_banks()`` or ``get_child_banks()`` in lieu
    of a ``PermissionDenied`` error that may disrupt the traversal
    through authorized pathways.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: bank elements may be silently omitted or re-
        ordered
      * plenary view: provides a complete set or is an error condition





    .. py:method:: get_bank_hierarchy_id():
        :noindex:


    .. py:attribute:: bank_hierarchy_id
        :noindex:


    .. py:method:: get_bank_hierarchy():
        :noindex:


    .. py:attribute:: bank_hierarchy
        :noindex:


    .. py:method:: can_access_bank_hierarchy():
        :noindex:


    .. py:method:: use_comparative_bank_view():
        :noindex:


    .. py:method:: use_plenary_bank_view():
        :noindex:


    .. py:method:: get_root_bank_ids():
        :noindex:


    .. py:attribute:: root_bank_ids
        :noindex:


    .. py:method:: get_root_banks():
        :noindex:


    .. py:attribute:: root_banks
        :noindex:


    .. py:method:: has_parent_banks(bank_id):
        :noindex:


    .. py:method:: is_parent_of_bank(id_, bank_id):
        :noindex:


    .. py:method:: get_parent_bank_ids(bank_id):
        :noindex:


    .. py:method:: get_parent_banks(bank_id):
        :noindex:


    .. py:method:: is_ancestor_of_bank(id_, bank_id):
        :noindex:


    .. py:method:: has_child_banks(bank_id):
        :noindex:


    .. py:method:: is_child_of_bank(id_, bank_id):
        :noindex:


    .. py:method:: get_child_bank_ids(bank_id):
        :noindex:


    .. py:method:: get_child_banks(bank_id):
        :noindex:


    .. py:method:: is_descendant_of_bank(id_, bank_id):
        :noindex:


    .. py:method:: get_bank_node_ids(bank_id, ancestor_levels, descendant_levels, include_siblings):
        :noindex:


    .. py:method:: get_bank_nodes(bank_id, ancestor_levels, descendant_levels, include_siblings):
        :noindex:


Bank Hierarchy Design Session
-----------------------------

.. py:class:: BankHierarchyDesignSession(abc_assessment_sessions.BankHierarchyDesignSession, osid_sessions.OsidSession)
    This session defines methods for managing a hierarchy of ``Bank`` objects.


    Each node in the hierarchy is a unique ``Bank``.





    .. py:method:: get_bank_hierarchy_id():
        :noindex:


    .. py:attribute:: bank_hierarchy_id
        :noindex:


    .. py:method:: get_bank_hierarchy():
        :noindex:


    .. py:attribute:: bank_hierarchy
        :noindex:


    .. py:method:: can_modify_bank_hierarchy():
        :noindex:


    .. py:method:: add_root_bank(bank_id):
        :noindex:


    .. py:method:: remove_root_bank(bank_id):
        :noindex:


    .. py:method:: add_child_bank(bank_id, child_id):
        :noindex:


    .. py:method:: remove_child_bank(bank_id, child_id):
        :noindex:


    .. py:method:: remove_child_banks(bank_id):
        :noindex:


