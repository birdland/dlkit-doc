

Service Catalog
===============


Bank
----

.. py:class:: Bank(abc_assessment_objects.Bank, osid_objects.OsidCatalog)
    A bank defines a collection of assessments and items.

    .. py:method:: get_bank_record(bank_record_type):
        :noindex:




Assessment Methods
------------------

    .. py:method:: get_bank_id():
        Gets the ``Bank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_id


    .. py:method:: get_bank():
        Gets the ``Bank`` associated with this session.

        :return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank


    .. py:method:: can_take_assessments():
        Tests if this user can take this assessment section.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer assessment
        operations to unauthorized users.

        :return: (boolean) - ``false`` if assessment methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: has_assessment_begun(assessment_taken_id):
        Tests if this assessment has started.

        An assessment begins from the designated start time if a start
        time is defined. If no start time is defined the assessment may
        begin at any time. Assessment sections cannot be accessed if the
        return for this method is ``false``.

        :arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        :return: (boolean) - ``true`` if this assessment has begun,
                ``false`` otherwise
        :raises:  NotFound - ``assessment_taken_id`` is not found
        :raises:  NullArgument - ``assessment_taken_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_assessment_over(assessment_taken_id):
        Tests if this assessment is over.

        An assessment is over if ``finished_assessment()`` is invoked or
        the designated finish time has expired.

        :arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        :return: (boolean) - ``true`` if this assessment is over,
                ``false`` otherwise
        :raises:  NotFound - ``assessment_taken_id`` is not found
        :raises:  NullArgument - ``assessment_taken_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: requires_synchronous_sections(assessment_taken_id):
        Tests if synchronous sections are required.

        This method should be checked to determine if all sections are
        available when requested, or the next sections becomes available
        only after the previous section is complete.


        There are two methods for retrieving sections. One is using the
        built-in hasNextSection() and getNextSection() methods. In
        synchronous mode, hasNextSection() is false until the current
        section is completed. In asynchronous mode,
        ``has_next_section()`` returns true until the end of the
        assessment.


        ``AssessmentSections`` may also be accessed via an
        ``AssessmentSectionList``. If syncronous sections are required,
        ``AssessmentSectionList.available() == 0`` and
        ``AssessmentSectionList.getNextQuestion()`` blocks until the
        section is complete. ``AssessmentSectionList.hasNext()`` is
        always true until the end of the assessment is reached.

        :arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        :return: (boolean) - ``true`` if this synchronous sections are
                required, ``false`` otherwise
        :raises:  NotFound - ``assessment_taken_id`` is not found
        :raises:  NullArgument - ``assessment_taken_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_first_assessment_section(assessment_taken_id):
        Gets the first assessment section in this assesment.

        All assessments have at least one ``AssessmentSection``.

        :arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        :return: (osid.assessment.AssessmentSection) - the first
                assessment section
        :raises:  IllegalState - ``has_assessment_begun()`` is ``false``
        :raises:  NotFound - ``assessment_taken_id`` is not found
        :raises:  NullArgument - ``assessment_taken_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: has_next_assessment_section(assessment_section_id):
        Tests if there is a next assessment section in the assessment following the given assessment
            section ``Id``.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :return: (boolean) - ``true`` if there is a next section,
                ``false`` otherwise
        :raises:  IllegalState - ``has_assessment_begun()`` is ``false``
        :raises:  NotFound - ``assessment_taken_id`` is not found
        :raises:  NullArgument - ``assessment_taken_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_next_assessment_section(assessment_section_id):
        Gets the next assessemnt section following the given assesment section.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :return: (osid.assessment.AssessmentSection) - the next section
        :raises:  IllegalState - ``has_next_assessment_section()`` is
                ``false``
        :raises:  NotFound - ``assessment_section_id`` is not found
        :raises:  NullArgument - ``assessment_section_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: has_previous_assessment_section(assessment_section_id):
        Tests if there is a previous assessment section in the assessment following the given
            assessment section ``Id``.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :return: (boolean) - ``true`` if there is a previous assessment
                section, ``false`` otherwise
        :raises:  IllegalState - ``has_assessment_begun()`` is ``false``
        :raises:  NotFound - ``assessment_section_id`` is not found
        :raises:  NullArgument - ``assessment_section_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_previous_assessment_section(assessment_section_id):
        Gets the next assessemnt section following the given assesment section.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :return: (osid.assessment.AssessmentSection) - the previous
                assessment section
        :raises:  IllegalState - ``has_next_assessment_section()`` is
                ``false``
        :raises:  NotFound - ``assessment_section_id`` is not found
        :raises:  NullArgument - ``assessment_section_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessment_section(assessment_section_id):
        Gets an assessemnts section by ``Id``.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :return: (osid.assessment.AssessmentSection) - the assessment
                section
        :raises:  IllegalState - ``has_assessment_begun()`` is ``false``
        :raises:  NotFound - ``assessment_section_id`` is not found
        :raises:  NullArgument - ``assessment_section_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessment_sections(assessment_taken_id):
        Gets the assessment sections of this assessment.

        :arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        :return: (osid.assessment.AssessmentSectionList) - the list of
                assessment sections
        :raises:  IllegalState - ``has_assessment_begun()`` is ``false``
        :raises:  NotFound - ``assessment_taken_id`` is not found
        :raises:  NullArgument - ``assessment_taken_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_assessment_section_complete(assessment_section_id):
        Tests if the all responses have been submitted to this assessment section.

        If ``is_assessment_section_complete()`` is false, then
        ``get_unanswered_questions()`` may return a list of questions
        that can be submitted.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :return: (boolean) - ``true`` if this assessment section is
                complete, ``false`` otherwise
        :raises:  IllegalState - ``is_assessment_over()`` is ``true``
        :raises:  NotFound - ``assessment_section_id`` is not found
        :raises:  NullArgument - ``assessment_section_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_incomplete_assessment_sections(assessment_taken_id):
        Gets the incomplete assessment sections of this assessment.

        :arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        :return: (osid.assessment.AssessmentSectionList) - the list of
                incomplete assessment sections
        :raises:  IllegalState - ``has_assessment_begun()`` is ``false``
        :raises:  NotFound - ``assessment_taken_id`` is not found
        :raises:  NullArgument - ``assessment_taken_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: has_assessment_section_begun(assessment_section_id):
        Tests if this assessment section has started.

        A section begins from the designated start time if a start time
        is defined. If no start time is defined the section may begin at
        any time. Assessment items cannot be accessed or submitted if
        the return for this method is ``false``.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :return: (boolean) - ``true`` if this assessment section has
                begun, ``false`` otherwise
        :raises:  IllegalState - ``has_assessment_begun()`` is ``false or
                is_assessment_over()`` is ``true``
        :raises:  NotFound - ``assessment_section_id`` is not found
        :raises:  NullArgument - ``assessment_section_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_assessment_section_over(assessment_section_id):
        Tests if this assessment section is over.

        An assessment section is over if new or updated responses can
        not be submitted such as the designated finish time has expired.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :return: (boolean) - ``true`` if this assessment is over,
                ``false`` otherwise
        :raises:  IllegalState - ``has_assessmen_sectiont_begun()`` is
                ``false or is_assessment_section_over()`` is ``true``
        :raises:  NotFound - ``assessment_section_id`` is not found
        :raises:  NullArgument - ``assessment_section_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: requires_synchronous_responses(assessment_section_id):
        Tests if synchronous responses are required in this assessment section.

        This method should be checked to determine if all items are
        available when requested, or the next item becomes available
        only after the response to the current item is submitted.


        There are two methods for retrieving questions. One is using the
        built-in ``has_next_question()`` and ``get_next_question()``
        methods. In synchronous mode, ``has_next_question()`` is
        ``false`` until the response for the current question is
        submitted. In asynchronous mode, ``has_next_question()`` returns
        ``true`` until the end of the assessment.


        ``Questions`` may also be accessed via a ``QuestionList``. If
        syncronous responses are required, ``QuestionList.available() ==
        0`` and ``QuestionList.getNextQuestion()`` blocks until the
        response is submitted. ``QuestionList.hasNext()`` is always true
        until the end of the assessment is reached.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :return: (boolean) - ``true`` if this synchronous responses are
                required, ``false`` otherwise
        :raises:  IllegalState - ``has_assessment_begun()`` is ``false or
                is_assessment_over()`` is ``true``
        :raises:  NotFound - ``assessment_section_id`` is not found
        :raises:  NullArgument - ``assessment_section_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_first_question(assessment_section_id):
        Gets the first question in this assesment section.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :return: (osid.assessment.Question) - the first question
        :raises:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        :raises:  NotFound - ``assessment_section_id`` is not found
        :raises:  NullArgument - ``assessment_section_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: has_next_question(assessment_section_id, item_id):
        Tests if there is a next question following the given question ``Id``.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        :return: (boolean) - ``true`` if there is a next question,
                ``false`` otherwise
        :raises:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        :raises:  NotFound - ``assessment_section_id`` or ``item_id`` is
                not found, or ``item_id`` not part of
                ``assessment_section_id``
        :raises:  NullArgument - ``assessment_section_id`` or ``item_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_next_question(assessment_section_id, item_id):
        Gets the next question in this assesment section.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        :return: (osid.assessment.Question) - the next question
        :raises:  IllegalState - ``has_next_question()`` is ``false``
        :raises:  NotFound - ``assessment_section_id`` or ``item_id`` is
                not found, or ``item_id`` not part of
                ``assessment_section_id``
        :raises:  NullArgument - ``assessment_section_id`` or ``item_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: has_previous_question(assessment_section_id, item_id):
        Tests if there is a previous question preceeding the given question ``Id``.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        :return: (boolean) - ``true`` if there is a previous question,
                ``false`` otherwise
        :raises:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        :raises:  NotFound - ``assessment_section_id`` or ``item_id`` is
                not found, or ``item_id`` not part of
                ``assessment_section_id``
        :raises:  NullArgument - ``assessment_section_id`` or ``item_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_previous_question(assessment_section_id, item_id):
        Gets the previous question in this assesment section.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        :return: (osid.assessment.Question) - the previous question
        :raises:  IllegalState - ``has_previous_question()`` is ``false``
        :raises:  NotFound - ``assessment_section_id`` or ``item_id`` is
                not found, or ``item_id`` not part of
                ``assessment_section_id``
        :raises:  NullArgument - ``assessment_section_id`` or ``item_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_question(assessment_section_id, item_id):
        Gets the ``Question`` specified by its ``Id``.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        :return: (osid.assessment.Question) - the returned ``Question``
        :raises:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        :raises:  NotFound - ``assessment_section_id`` or ``item_id`` is
                not found, or ``item_id`` not part of
                ``assessment_section_id``
        :raises:  NullArgument - ``assessment_section_id`` or ``item_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_questions(assessment_section_id):
        Gets the questions of this assessment section.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :return: (osid.assessment.QuestionList) - the list of assessment
                questions
        :raises:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        :raises:  NotFound - ``assessment_section_id`` is not found
        :raises:  NullArgument - ``assessment_section_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_response_form(assessment_section_id, item_id):
        Gets the response form for submitting an answer.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        :return: (osid.assessment.AnswerForm) - an answer form
        :raises:  IllegalState - ``has_assessment_section_begun()`` is
                ``false or is_assessment_section_over()`` is ``true``
        :raises:  NotFound - ``assessment_section_id`` or ``item_id`` is
                not found, or ``item_id`` not part of
                ``assessment_section_id``
        :raises:  NullArgument - ``assessment_section_id`` or ``item_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: submit_response(assessment_section_id, item_id, answer_form):
        Submits an answer to an item.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        :arg:    answer_form (osid.assessment.AnswerForm): the response
        :raises:  IllegalState - ``has_assessment_section_begun()`` is
                ``false or is_assessment_section_over()`` is ``true``
        :raises:  InvalidArgument - one or more of the elements in the
                form is invalid
        :raises:  NotFound - ``assessment_section_id`` or ``item_id`` is
                not found, or ``item_id`` not part of
                ``assessment_section_id``
        :raises:  NullArgument - ``assessment_section_id, item_id,`` or
                ``answer_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``answer_form`` is not of this service
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: skip_item(assessment_section_id, item_id):
        Skips an item.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        :raises:  IllegalState - ``has_assessment_section_begun()`` is
                ``false or is_assessment_section_over()`` is ``true``
        :raises:  NotFound - ``assessment_section_id`` or ``item_id`` is
                not found, or ``item_id`` not part of
                ``assessment_section_id``
        :raises:  NullArgument - ``assessment_section_id`` or ``item_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_question_answered(assessment_section_id, item_id):
        Tests if the given item has a response.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        :return: (boolean) - ``true`` if this item has a response,
                ``false`` otherwise
        :raises:  IllegalState - ``has_assessment_section_begun()`` is
                ``false or is_assessment_section_over()`` is ``true``
        :raises:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        :raises:  NullArgument - ``assessment_section_id or item_id is
                null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_unanswered_questions(assessment_section_id):
        Gets the unanswered questions of this assessment section.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :return: (osid.assessment.QuestionList) - the list of questions
                with no rsponses
        :raises:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        :raises:  NotFound - ``assessment_section_id`` is not found
        :raises:  NullArgument - ``assessment_section_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: has_unanswered_questions(assessment_section_id):
        Tests if there are unanswered questions in this assessment section.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :return: (boolean) - ``true`` if there are unanswered questions,
                ``false`` otherwise
        :raises:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        :raises:  NotFound - ``assessment_section_id`` is not found
        :raises:  NullArgument - ``assessment_section_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_first_unanswered_question(assessment_section_id):
        Gets the first unanswered question in this assesment section.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :return: (osid.assessment.Question) - the first unanswered
                question
        :raises:  IllegalState - ``has_unanswered_questions()`` is
                ``false``
        :raises:  NotFound - ``assessment_section_id`` is not found
        :raises:  NullArgument - ``assessment_section_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: has_next_unanswered_question(assessment_section_id, item_id):
        Tests if there is a next unanswered question following the given question ``Id``.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        :return: (boolean) - ``true`` if there is a next unanswered
                question, ``false`` otherwise
        :raises:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        :raises:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        :raises:  NullArgument - ``assessment_section_id or item_id is
                null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_next_unanswered_question(assessment_section_id, item_id):
        Gets the next unanswered question in this assesment section.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        :return: (osid.assessment.Question) - the next unanswered
                question
        :raises:  IllegalState - ``has_next_unanswered_question()`` is
                ``false``
        :raises:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        :raises:  NullArgument - ``assessment_section_id or item_id is
                null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: has_previous_unanswered_question(assessment_section_id, item_id):
        Tests if there is a previous unanswered question preceeding the given question ``Id``.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        :return: (boolean) - ``true`` if there is a previous unanswered
                question, ``false`` otherwise
        :raises:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        :raises:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        :raises:  NullArgument - ``assessment_section_id or item_id is
                null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_previous_unanswered_question(assessment_section_id, item_id):
        Gets the previous unanswered question in this assesment section.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        :return: (osid.assessment.Question) - the previous unanswered
                question
        :raises:  IllegalState - ``has_previous_unanswered_question()`` is
                ``false``
        :raises:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        :raises:  NullArgument - ``assessment_section_id or item_id is
                null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_response(assessment_section_id, item_id):
        Gets the submitted response to the associated item.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        :return: (osid.assessment.Response) - the response
        :raises:  IllegalState - ``has_assessment_section_begun()`` is
                ``false or is_assessment_section_over()`` is ``true``
        :raises:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        :raises:  NullArgument - ``assessment_section_id or item_id is
                null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_responses(assessment_section_id):
        Gets all submitted responses.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :return: (osid.assessment.ResponseList) - the list of responses
        :raises:  IllegalState - ``has_assessment_section_begun()`` is
                ``false or is_assessment_section_over()`` is ``true``
        :raises:  NotFound - ``assessment_section_id`` is not found
        :raises:  NullArgument - ``assessment_section_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: clear_response(assessment_section_id, item_id):
        Clears the response to an item The item appears as unanswered.

        If no response exists, the method simply returns.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        :raises:  IllegalState - ``has_assessment_section_begun() is false
                or is_assessment_section_over() is true``
        :raises:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        :raises:  NullArgument - ``assessment_section_id or item_id is
                null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: finish_assessment_section(assessment_section_id):
        Indicates an assessment section is complete.

        Finished sections may or may not allow new or updated responses.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :raises:  IllegalState - ``has_assessment_section_begun()`` is
                ``false or is_assessment_section_over()`` is ``true``
        :raises:  NotFound - ``assessment_section_id`` is not found
        :raises:  NullArgument - ``assessment_section_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_answer_available(assessment_section_id, item_id):
        Tests if an answer is available for the given item.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        :return: (boolean) - ``true`` if an answer are available,
                ``false`` otherwise
        :raises:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        :raises:  NullArgument - ``assessment_section_id or item_id is
                null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_answers(assessment_section_id, item_id):
        Gets the acceptable answers to the associated item.

        :arg:    assessment_section_id (osid.id.Id): ``Id`` of the
                ``AssessmentSection``
        :arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        :return: (osid.assessment.AnswerList) - the answers
        :raises:  IllegalState - ``is_answer_available()`` is ``false``
        :raises:  NotFound - ``assessment_section_id or item_id is not
                found, or item_id not part of assessment_section_id``
        :raises:  NullArgument - ``assessment_section_id or item_id is
                null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: finish_assessment(assessment_taken_id):
        Indicates the entire assessment is complete.

        :arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        :raises:  IllegalState - ``has_begun()`` is ``false or is_over()``
                is ``true``
        :raises:  NotFound - ``assessment_taken_id`` is not found
        :raises:  NullArgument - ``assessment_taken_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Item Lookup Methods
-------------------

    .. py:method:: get_bank_id():
        Gets the ``Bank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_id


    .. py:method:: get_bank():
        Gets the ``Bank`` associated with this session.

        :return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank


    .. py:method:: can_lookup_items():
        Tests if this user can perform ``Item`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_item_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_item_view():
        A complete view of the ``Item`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_bank_view():
        Federates the view for methods in this session.

        A federated view will include assessment items in assessment
        banks which are children of this assessment bank in the
        assessment bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_bank_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this assessment bank only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_item(item_id):
        Gets the ``Item`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Item`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Item`` and retained for compatibility.

        :arg:    item_id (osid.id.Id): the ``Id`` of the ``Item`` to
                retrieve
        :return: (osid.assessment.Item) - the returned ``Item``
        :raises:  NotFound - no ``Item`` found with the given ``Id``
        :raises:  NullArgument - ``item_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_items_by_ids(item_ids):
        Gets an ``ItemList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the items
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Items`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :arg:    item_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.assessment.ItemList) - the returned ``Item`` list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``item_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_items_by_genus_type(item_genus_type):
        Gets an ``ItemList`` corresponding to the given assessment item genus ``Type`` which does
            not include assessment items of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known assessment
        items or an error results. Otherwise, the returned list may
        contain only those assessment items that are accessible through
        this session.

        :arg:    item_genus_type (osid.type.Type): an assessment item
                genus type
        :return: (osid.assessment.ItemList) - the returned ``Item`` list
        :raises:  NullArgument - ``item_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_items_by_parent_genus_type(item_genus_type):
        Gets an ``ItemList`` corresponding to the given assessment item genus ``Type`` and include
            any additional assessment items with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known assessment
        items or an error results. Otherwise, the returned list may
        contain only those assessment items that are accessible through
        this session.

        :arg:    item_genus_type (osid.type.Type): an assessment item
                genus type
        :return: (osid.assessment.ItemList) - the returned ``Item`` list
        :raises:  NullArgument - ``item_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_items_by_record_type(item_record_type):
        Gets an ``ItemList`` containing the given assessment item record ``Type``.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        :arg:    item_record_type (osid.type.Type): an item record type
        :return: (osid.assessment.ItemList) - the returned ``Item`` list
        :raises:  NullArgument - ``item_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_items_by_question(question_id):
        Gets an ``ItemList`` containing the given question.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        :arg:    question_id (osid.id.Id): a question ``Id``
        :return: (osid.assessment.ItemList) - the returned ``Item`` list
        :raises:  NullArgument - ``question_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_items_by_answer(answer_id):
        Gets an ``ItemList`` containing the given answer.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        :arg:    answer_id (osid.id.Id): an answer ``Id``
        :return: (osid.assessment.ItemList) - the returned ``Item`` list
        :raises:  NullArgument - ``answer_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_items_by_learning_objective(objective_id):
        Gets an ``ItemList`` containing the given learning objective.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        :arg:    objective_id (osid.id.Id): a learning objective ``Id``
        :return: (osid.assessment.ItemList) - the returned ``Item`` list
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_items_by_learning_objectives(objective_ids):
        Gets an ``ItemList`` containing the given learning objectives.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        :arg:    objective_ids (osid.id.IdList): a list of learning
                objective ``Ids``
        :return: (osid.assessment.ItemList) - the returned ``Item`` list
        :raises:  NullArgument - ``objective_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_items():
        Gets all ``Items``.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those items that are accessible through this session.

        :return: (osid.assessment.ItemList) - a list of ``Items``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: items




Item Query Methods
------------------

    .. py:method:: get_bank_id():
        Gets the ``Bank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_id


    .. py:method:: get_bank():
        Gets the ``Bank`` associated with this session.

        :return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank


    .. py:method:: can_search_items():
        Tests if this user can perform ``Item`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an pplication that may wish not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_federated_bank_view():
        Federates the view for methods in this session.

        A federated view will include assessment items in assessment
        banks which are children of this assessment bank in the
        assessment bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_bank_view():
        Isolates the view for methods in this session.

        An isolated view restricts searches to this assessment bank
        only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_item_query():
        Gets an assessment item query.

        :return: (osid.assessment.ItemQuery) - the assessment item query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: item_query


    .. py:method:: get_items_by_query(item_query):
        Gets a list of ``Items`` matching the given item query.

        :arg:    item_query (osid.assessment.ItemQuery): the item query
        :return: (osid.assessment.ItemList) - the returned ``ItemList``
        :raises:  NullArgument - ``item_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``item_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*






Item Search Methods
-------------------

    .. py:method:: get_item_search():
        Gets an assessment item search.

        :return: (osid.assessment.ItemSearch) - the assessment item
                search
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: item_search


    .. py:method:: get_item_search_order():
        Gets an assessment item search order.

        The ``ItemSearchOrder`` is supplied to an ``ItemSearch`` to
        specify the ordering of results.

        :return: (osid.assessment.ItemSearchOrder) - the assessment item
                search order
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: item_search_order


    .. py:method:: get_items_by_search(item_query, item_search):
        Gets the search results matching the given search query using the given search.

        :arg:    item_query (osid.assessment.ItemQuery): the item query
        :arg:    item_search (osid.assessment.ItemSearch): the item
                search
        :return: (osid.assessment.ItemSearchResults) - the returned
                search results
        :raises:  NullArgument - ``item_query`` or ``item_search`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``item_search`` or ``item_query`` is not
                of this service
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_item_query_from_inspector(item_query_inspector):
        Gets an item query from an inspector.

        The inspector is available from an ``ItemSearchResults``.

        :arg:    item_query_inspector
                (osid.assessment.ItemQueryInspector): a query inspector
        :return: (osid.assessment.ItemQuery) - the item query
        :raises:  NullArgument - ``item_query_inspector`` is ``null``
        :raises:  Unsupported - ``item_query_inspector`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*






Item Admin Methods
------------------

    .. py:method:: get_bank_id():
        Gets the ``Bank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_id


    .. py:method:: get_bank():
        Gets the ``Bank`` associated with this session.

        :return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank


    .. py:method:: can_create_items():
        Tests if this user can create ``Items``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an ``Item``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Item`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_item_with_record_types(item_record_types):
        Tests if this user can create a single ``Item`` using the desired record types.

        While ``AssessmentManager.getItemRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Item``.
        Providing an empty array tests if an ``Item`` can be created
        with no records.

        :arg:    item_record_types (osid.type.Type[]): array of item
                record types
        :return: (boolean) - ``true`` if ``Item`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``item_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_item_form_for_create(item_record_types):
        Gets the assessment item form for creating new assessment items.

        A new form should be requested for each create transaction.

        :arg:    item_record_types (osid.type.Type[]): array of item
                record types to be included in the create operation or
                an empty list if none
        :return: (osid.assessment.ItemForm) - the assessment item form
        :raises:  NullArgument - ``item_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_item(item_form):
        Creates a new ``Item``.

        :arg:    item_form (osid.assessment.ItemForm): the form for this
                ``Item``
        :return: (osid.assessment.Item) - the new ``Item``
        :raises:  IllegalState - ``item_form`` already used in a create
                transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``item_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``item_form`` did not originate from
                ``get_item_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_items():
        Tests if this user can update ``Items``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an ``Item``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if assessment item modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_item_form_for_update(item_id):
        Gets the assessment item form for updating an existing item.

        A new item form should be requested for each update transaction.

        :arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        :return: (osid.assessment.ItemForm) - the assessment item form
        :raises:  NotFound - ``item_id`` is not found
        :raises:  NullArgument - ``item_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_item(item_form):
        Updates an existing item.

        :arg:    item_form (osid.assessment.ItemForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``item_form`` already used in an update
                transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``item_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``item_form`` did not originate from
                ``get_item_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_items():
        Tests if this user can delete ``Items``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an ``Item``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Item`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_item(item_id):
        Deletes the ``Item`` identified by the given ``Id``.

        :arg:    item_id (osid.id.Id): the ``Id`` of the ``Item`` to
                delete
        :raises:  NotFound - an ``Item`` was not found identified by the
                given ``Id``
        :raises:  NullArgument - ``item_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_item_aliases():
        Tests if this user can manage ``Id`` aliases for ``Items``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Item`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_item(item_id, alias_id):
        Adds an ``Id`` to an ``Item`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Item`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another item, it is reassigned to the
        given item ``Id``.

        :arg:    item_id (osid.id.Id): the ``Id`` of an ``Item``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is in use as a primary
                ``Id``
        :raises:  NotFound - ``item_id`` not found
        :raises:  NullArgument - ``item_id`` or ``alias_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_questions():
        Tests if this user can create ``Questions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Question`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Question`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_question_with_record_types(question_record_types):
        Tests if this user can create a single ``Question`` using the desired record types.

        While ``AssessmentManager.getQuestionRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Question``.
        Providing an empty array tests if a ``Question`` can be created
        with no records.

        :arg:    question_record_types (osid.type.Type[]): array of
                question record types
        :return: (boolean) - ``true`` if ``Question`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``question_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_question_form_for_create(item_id, question_record_types):
        Gets the question form for creating new questions.

        A new form should be requested for each create transaction.

        :arg:    item_id (osid.id.Id): an assessment item ``Id``
        :arg:    question_record_types (osid.type.Type[]): array of
                question record types to be included in the create
                operation or an empty list if none
        :return: (osid.assessment.QuestionForm) - the question form
        :raises:  NullArgument - ``question_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_question(question_form):
        Creates a new ``Question``.

        :arg:    question_form (osid.assessment.QuestionForm): the form
                for this ``Question``
        :return: (osid.assessment.Question) - the new ``Question``
        :raises:  AlreadyExists - a question already exists for this item
        :raises:  IllegalState - ``question_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``question_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``question_form`` did not originate from
                ``get_question_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_questions():
        Tests if this user can update ``Questions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Question`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: (boolean) - ``false`` if question modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_question_form_for_update(question_id):
        Gets the question form for updating an existing question.

        A new question form should be requested for each update
        transaction.

        :arg:    question_id (osid.id.Id): the ``Id`` of the ``Question``
        :return: (osid.assessment.QuestionForm) - the question form
        :raises:  NotFound - ``question_id`` is not found
        :raises:  NullArgument - ``question_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_question(question_form):
        Updates an existing question.

        :arg:    question_form (osid.assessment.QuestionForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``question_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``question_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``question_form`` did not originate from
                ``get_question_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_questions():
        Tests if this user can delete ``Questions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Question`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Question`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_question(question_id):
        Deletes the ``Question`` identified by the given ``Id``.

        :arg:    question_id (osid.id.Id): the ``Id`` of the ``Question``
                to delete
        :raises:  NotFound - a ``Question`` was not found identified by
                the given ``Id``
        :raises:  NullArgument - ``question_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_answers():
        Tests if this user can create ``Answers``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Answer``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Answer`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_answers_with_record_types(answer_record_types):
        Tests if this user can create a single ``Answer`` using the desired record types.

        While ``AssessmentManager.getAnswerRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Answer``.
        Providing an empty array tests if an ``Answer`` can be created
        with no records.

        :arg:    answer_record_types (osid.type.Type[]): array of answer
                record types
        :return: (boolean) - ``true`` if ``Answer`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``answern_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_answer_form_for_create(item_id, answer_record_types):
        Gets the answer form for creating new answers.

        A new form should be requested for each create transaction.

        :arg:    item_id (osid.id.Id): an assessment item ``Id``
        :arg:    answer_record_types (osid.type.Type[]): array of answer
                record types to be included in the create operation or
                an empty list if none
        :return: (osid.assessment.AnswerForm) - the answer form
        :raises:  NullArgument - ``answer_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_answer(answer_form):
        Creates a new ``Answer``.

        :arg:    answer_form (osid.assessment.AnswerForm): the form for
                this ``Answer``
        :return: (osid.assessment.Answer) - the new ``Answer``
        :raises:  IllegalState - ``answer_form`` already used in a create
                transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``answer_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``answer_form`` did not originate from
                ``get_answer_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_answers():
        Tests if this user can update ``Answers``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Answer`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: (boolean) - ``false`` if answer modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_answer_form_for_update(answer_id):
        Gets the answer form for updating an existing answer.

        A new answer form should be requested for each update
        transaction.

        :arg:    answer_id (osid.id.Id): the ``Id`` of the ``Answer``
        :return: (osid.assessment.AnswerForm) - the answer form
        :raises:  NotFound - ``answer_id`` is not found
        :raises:  NullArgument - ``answer_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_answer(answer_form):
        Updates an existing answer.

        :arg:    answer_form (osid.assessment.AnswerForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``answer_form`` already used in an update
                transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``answer_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``answer_form`` did not originate from
                ``get_answer_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_answers():
        Tests if this user can delete ``Answers``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Answer`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Answer`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_answer(answer_id):
        Deletes the ``Answer`` identified by the given ``Id``.

        :arg:    answer_id (osid.id.Id): the ``Id`` of the ``Answer`` to
                delete
        :raises:  NotFound - an ``Answer`` was not found identified by the
                given ``Id``
        :raises:  NullArgument - ``answer_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*






Item Notification Methods
-------------------------

    .. py:method:: get_bank_id():
        Gets the ``Bank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_id


    .. py:method:: get_bank():
        Gets the ``Bank`` associated with this session.

        :return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank


    .. py:method:: can_register_for_item_notifications():
        Tests if this user can register for ``Item`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: (boolean) - ``false`` if notification methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_federated_bank_view():
        Federates the view for methods in this session.

        A federated view will include notifications for assessment items
        in assessment banks which are children of this assessment bank
        in the assessment bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_bank_view():
        Isolates the view for methods in this session.

        An isolated view restricts notifications to this assessment bank
        only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: reliable_item_notifications():
        Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: unreliable_item_notifications():
        Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: acknowledge_item_notification(notification_id):
        Acknowledge an item notification.

        :arg:    notification_id (osid.id.Id): the ``Id`` of the
                notification
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_new_items():
        Register for notifications of new assessment items.

        ``ItemReceiver.newItems()`` is invoked when a new ``Item`` is
        created.

        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_changed_items():
        Registers for notification of updated assessment items.

        ``ItemReceiver.changedItems()`` is invoked when an assessment
        item is changed.

        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_changed_item(item_id):
        Registers for notification of an updated assessment item.

        ``ItemReceiver.changedItems()`` is invoked when the specified
        assessment item is changed.

        :arg:    item_id (osid.id.Id): the ``Id`` of the ``Assessment``
                to monitor
        :raises:  NotFound - an ``item`` was not found identified by the
                given ``Id``
        :raises:  NullArgument - ``item_id is null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_deleted_items():
        Registers for notification of deleted assessment items.

        ``ItemReceiver.deletedItems()`` is invoked when an assessment
        item is removed from the assessment bank.

        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_deleted_item(item_id):
        Registers for notification of a deleted assessment item.

        ``ItemReceiver.deletedItems()`` is invoked when the specified
        assessment item is removed from the assessment bank.

        :arg:    item_id (osid.id.Id): the ``Id`` of the ``Item`` to
                monitor
        :raises:  NotFound - an ``Item`` was not found identified by the
                given ``Id``
        :raises:  NullArgument - ``item_id is null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: reliable_item_notifications():
        Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: unreliable_item_notifications():
        Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: acknowledge_item_notification(notification_id):
        Acknowledge an item notification.

        :arg:    notification_id (osid.id.Id): the ``Id`` of the
                notification
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Assessment Lookup Methods
-------------------------

    .. py:method:: get_bank_id():
        Gets the ``Bank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_id


    .. py:method:: get_bank():
        Gets the ``Bank`` associated with this session.

        :return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank


    .. py:method:: can_lookup_assessments():
        Tests if this user can perform ``Assessment`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_assessment_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_assessment_view():
        A complete view of the ``Assessment`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_bank_view():
        Federates the view for methods in this session.

        A federated view will include assessments in banks which are
        children of this bank in the bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_bank_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_assessment(assessment_id):
        Gets the ``Assessment`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Assessment`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Assessment`` and retained
        for compatibility.

        :arg:    assessment_id (osid.id.Id): ``Id`` of the ``Assessment``
        :return: (osid.assessment.Assessment) - the assessment
        :raises:  NotFound - ``assessment_id`` not found
        :raises:  NullArgument - ``assessment_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_assessments_by_ids(assessment_ids):
        Gets an ``AssessmentList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        assessments specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Assessments`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :arg:    assessment_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.assessment.AssessmentList) - the returned
                ``Assessment`` list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``assessment_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_by_genus_type(assessment_genus_type):
        Gets an ``AssessmentList`` corresponding to the given assessment genus ``Type`` which does
            not include assessments of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments that are accessible through
        this session.

        :arg:    assessment_genus_type (osid.type.Type): an assessment
                genus type
        :return: (osid.assessment.AssessmentList) - the returned
                ``Assessment`` list
        :raises:  NullArgument - ``assessment_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_by_parent_genus_type(assessment_genus_type):
        Gets an ``AssessmentList`` corresponding to the given assessment genus ``Type`` and include
            any additional assessments with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments that are accessible through
        this session.

        :arg:    assessment_genus_type (osid.type.Type): an assessment
                genus type
        :return: (osid.assessment.AssessmentList) - the returned
                ``Assessment`` list
        :raises:  NullArgument - ``assessment_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_by_record_type(assessment_record_type):
        Gets an ``AssessmentList`` corresponding to the given assessment record ``Type``.

        The set of assessments implementing the given record type is
        returned. In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments that are accessible through
        this session.

        :arg:    assessment_record_type (osid.type.Type): an assessment
                record type
        :return: (osid.assessment.AssessmentList) - the returned
                ``Assessment`` list
        :raises:  NullArgument - ``assessment_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments():
        Gets all ``Assessments``.

        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments that are accessible through
        this session.

        :return: (osid.assessment.AssessmentList) - a list of
                ``Assessments``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: assessments




Assessment Query Methods
------------------------

    .. py:method:: get_bank_id():
        Gets the ``Bank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_id


    .. py:method:: get_bank():
        Gets the ``Bank`` associated with this session.

        :return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank


    .. py:method:: can_search_assessments():
        Tests if this user can perform ``Assessment`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an pplication that may wish not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_federated_bank_view():
        Federates the view for methods in this session.

        A federated view will include assessments in banks which are
        children of this bank in the bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_bank_view():
        Isolates the view for methods in this session.

        An isolated view restricts searches to this bank only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_assessment_query():
        Gets an assessment query.

        :return: (osid.assessment.AssessmentQuery) - the assessment query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: assessment_query


    .. py:method:: get_assessments_by_query(assessment_query):
        Gets a list of ``Assessments`` matching the given assessment query.

        :arg:    assessment_query (osid.assessment.AssessmentQuery): the
                assessment query
        :return: (osid.assessment.AssessmentList) - the returned
                ``AssessmentList``
        :raises:  NullArgument - ``assessment_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``assessment_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*






Assessment Admin Methods
------------------------

    .. py:method:: get_bank_id():
        Gets the ``Bank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_id


    .. py:method:: get_bank():
        Gets the ``Bank`` associated with this session.

        :return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank


    .. py:method:: can_create_assessments():
        Tests if this user can create ``Assessments``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``Assessment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Assessment`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_assessment_with_record_types(assessment_record_types):
        Tests if this user can create a single ``Assessment`` using the desired record interface
            types.

        While ``AssessmentManager.getAssessmentRecordTypes()`` can be
        used to examine which record interfaces are supported, this
        method tests which record(s) are required for creating a
        specific ``Assessment``. Providing an empty array tests if an
        ``Assessment`` can be created with no records.

        :arg:    assessment_record_types (osid.type.Type[]): array of
                assessment record types
        :return: (boolean) - ``true`` if ``Assessment`` creation using
                the specified record ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``assessment_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessment_form_for_create(assessment_record_types):
        Gets the assessment form for creating new assessments.

        A new form should be requested for each create transaction.

        :arg:    assessment_record_types (osid.type.Type[]): array of
                assessment record types to be included in the create
                operation or an empty list if none
        :return: (osid.assessment.AssessmentForm) - the assessment form
        :raises:  NullArgument - ``assessment_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_assessment(assessment_form):
        Creates a new ``Assessment``.

        :arg:    assessment_form (osid.assessment.AssessmentForm): the
                form for this ``Assessment``
        :return: (osid.assessment.Assessment) - the new ``Assessment``
        :raises:  IllegalState - ``assessment_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``assessment_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``assessment_form`` did not originate from
                ``get_assessment_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_assessments():
        Tests if this user can update ``Assessments``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Assessment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Assessment`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessment_form_for_update(assessment_id):
        Gets the assessment form for updating an existing assessment.

        A new assessment form should be requested for each update
        transaction.

        :arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        :return: (osid.assessment.AssessmentForm) - the assessment form
        :raises:  NotFound - ``assessment_id`` is not found
        :raises:  NullArgument - ``assessment_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_assessment(assessment_form):
        Updates an existing assessment.

        :arg:    assessment_form (osid.assessment.AssessmentForm): the
                form containing the elements to be updated
        :raises:  IllegalState - ``assessment_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``assessment_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``assessment_form did not originate from
                get_assessment_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_assessments():
        Tests if this user can delete ``Assessments``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Assessment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Assessment`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_assessment(assessment_id):
        Deletes an ``Assessment``.

        :arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment`` to remove
        :raises:  NotFound - ``assessment_id`` not found
        :raises:  NullArgument - ``assessment_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_assessment_aliases():
        Tests if this user can manage ``Id`` aliases for ``Assessments``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Assessment`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_assessment(assessment_id, alias_id):
        Adds an ``Id`` to an ``Assessment`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Assessment`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another assessment, it is reassigned
        to the given assessment ``Id``.

        :arg:    assessment_id (osid.id.Id): the ``Id`` of an
                ``Assessment``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is in use as a primary
                ``Id``
        :raises:  NotFound - ``assessment_id`` not found
        :raises:  NullArgument - ``assessment_id`` or ``alias_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*






Assessment Basic Authoring Methods
----------------------------------

    .. py:method:: get_bank_id():
        Gets the ``Bank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_id


    .. py:method:: get_bank():
        Gets the ``Bank`` associated with this session.

        :return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank


    .. py:method:: can_author_assessments():
        Tests if this user can author assessments.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        authoring operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessment_items(assessment_id):
        Gets the items in sequence from an assessment.

        :arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        :return: (osid.assessment.ItemList) - list of items
        :raises:  NotFound - ``assessmentid`` not found
        :raises:  NullArgument - ``assessment_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_item(assessment_id, item_id):
        Adds an existing ``Item`` to an assessment.

        :arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        :arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        :raises:  NotFound - ``assessment_id`` or ``item_id`` not found
        :raises:  NullArgument - ``assessment_id`` or ``item_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_item(assessment_id, item_id):
        Removes an ``Item`` from this assessment.

        :arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        :arg:    item_id (osid.id.Id): the ``Id`` of the ``Item``
        :raises:  NotFound - ``assessment_id`` or ``item_id`` not found or
                ``item_id`` not on ``assessmentid``
        :raises:  NullArgument - ``assessment_id`` or ``item_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: move_item(assessment_id, item_id, preceeding_item_id):
        Moves an existing item to follow another item in an assessment.

        :arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        :arg:    item_id (osid.id.Id): the ``Id`` of an ``Item``
        :arg:    preceeding_item_id (osid.id.Id): the ``Id`` of a
                preceeding ``Item`` in the sequence
        :raises:  NotFound - ``assessment_id`` is not found, or
                ``item_id`` or ``preceeding_item_id`` not on
                ``assessment_id``
        :raises:  NullArgument - ``assessment_id, item_id`` or
                ``preceeding_item_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: order_items(item_ids, assessment_id):
        Sequences existing items in an assessment.

        :arg:    item_ids (osid.id.Id[]): the ``Id`` of the ``Items``
        :arg:    assessment_id (osid.id.Id): the ``Id`` of the
                ``Assessment``
        :raises:  NotFound - ``assessment_id`` is not found or an
                ``item_id`` is not on ``assessment_id``
        :raises:  NullArgument - ``assessment_id`` or ``item_ids`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*






Assessment Offered Lookup Methods
---------------------------------

    .. py:method:: get_bank_id():
        Gets the ``Bank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_id


    .. py:method:: get_bank():
        Gets the ``Bank`` associated with this session.

        :return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank


    .. py:method:: can_lookup_assessments_offered():
        Tests if this user can perform ``AssessmentOffered`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_assessment_offered_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_assessment_offered_view():
        A complete view of the ``AssessmentOffered`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_bank_view():
        Federates the view for methods in this session.

        A federated view will include assessments in banks which are
        children of this bank in the bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_bank_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_assessment_offered(assessment_offered_id):
        Gets the ``AssessmentOffered`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``AssessmentOffered`` may have
        a different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``AssessmentOffered`` and
        retained for compatibility.

        :arg:    assessment_offered_id (osid.id.Id): ``Id`` of the
                ``AssessmentOffered``
        :return: (osid.assessment.AssessmentOffered) - the assessment
                offered
        :raises:  NotFound - ``assessment_offered_id`` not found
        :raises:  NullArgument - ``assessment_offered_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_assessments_offered_by_ids(assessment_offered_ids):
        Gets an ``AssessmentOfferedList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        assessments specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``AssessmentOffered`` objects may be omitted from
        the list and may present the elements in any order including
        returning a unique set.

        :arg:    assessment_offered_ids (osid.id.IdList): the list of
                ``Ids`` to retrieve
        :return: (osid.assessment.AssessmentOfferedList) - the returned
                ``AssessmentOffered`` list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``assessment_offered_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_offered_by_genus_type(assessment_offered_genus_type):
        Gets an ``AssessmentOfferedList`` corresponding to the given assessment offered genus
            ``Type`` which does not include assessments of types derived from the specified
            ``Type``.

        In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        :arg:    assessment_offered_genus_type (osid.type.Type): an
                assessment offered genus type
        :return: (osid.assessment.AssessmentOfferedList) - the returned
                ``AssessmentOffered`` list
        :raises:  NullArgument - ``assessment_offered_genus_type`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_offered_by_parent_genus_type(assessment_offered_genus_type):
        Gets an ``AssessmentOfferedList`` corresponding to the given assessment offered genus
            ``Type`` and include any additional assessments with genus types derived from the
            specified ``Type``.

        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments offered that are accessible
        through this session.

        :arg:    assessment_offered_genus_type (osid.type.Type): an
                assessment offered genus type
        :return: (osid.assessment.AssessmentOfferedList) - the returned
                ``AssessmentOffered`` list
        :raises:  NullArgument - ``assessment_offered_genus_type`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_offered_by_record_type(assessment_record_type):
        Gets an ``AssessmentOfferedList`` corresponding to the given assessment offered record
            ``Type``.

        The set of assessments implementing the given record type is
        returned. In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        :arg:    assessment_record_type (osid.type.Type): an assessment
                offered record type
        :return: (osid.assessment.AssessmentOfferedList) - the returned
                ``AssessmentOffered`` list
        :raises:  NullArgument - ``assessment_offered_record_type`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_offered_by_date(start, end):
        Gets an ``AssessmentOfferedList`` that have designated start times where the start times
            fall in the given range inclusive.

        In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        :arg:    start (osid.calendaring.DateTime): start of time range
        :arg:    end (osid.calendaring.DateTime): end of time range
        :return: (osid.assessment.AssessmentOfferedList) - the returned
                ``AssessmentOffered`` list
        :raises:  InvalidArgument - ``end`` is less than ``start``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_offered_for_assessment(assessment_id):
        Gets an ``AssessmentOfferedList`` by the given assessment.

        In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        :arg:    assessment_id (osid.id.Id): ``Id`` of an ``Assessment``
        :return: (osid.assessment.AssessmentOfferedList) - the returned
                ``AssessmentOffered`` list
        :raises:  NullArgument - ``assessment_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_offered():
        Gets all ``AssessmentOffered`` elements.

        In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        :return: (osid.assessment.AssessmentOfferedList) - a list of
                ``AssessmentOffered`` elements
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: assessments_offered




Assessment Offered Query Methods
--------------------------------

    .. py:method:: get_bank_id():
        Gets the ``Bank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_id


    .. py:method:: get_bank():
        Gets the ``Bank`` associated with this session.

        :return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank


    .. py:method:: can_search_assessments_offered():
        Tests if this user can perform ``AssessmentOffered`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may wish not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_federated_bank_view():
        Federates the view for methods in this session.

        A federated view will include assessments offered in banks which
        are children of this bank in the bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_bank_view():
        Isolates the view for methods in this session.

        An isolated view restricts searches to this bank only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_assessment_offered_query():
        Gets an assessment offered query.

        :return: (osid.assessment.AssessmentOfferedQuery) - the
                assessment offered query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: assessment_offered_query


    .. py:method:: get_assessments_offered_by_query(assessment_offered_query):
        Gets a list of ``AssessmentOffered`` elements matching the given assessment offered query.

        :arg:    assessment_offered_query
                (osid.assessment.AssessmentOfferedQuery): the assessment
                offered query
        :return: (osid.assessment.AssessmentOfferedList) - the returned
                ``AssessmentOfferedList``
        :raises:  NullArgument - ``assessment_offered_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``assessment_offered_query`` is not of
                this service
        *compliance: mandatory -- This method must be implemented.*






Assessment Offered Admin Methods
--------------------------------

    .. py:method:: get_bank_id():
        Gets the ``Bank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_id


    .. py:method:: get_bank():
        Gets the ``Bank`` associated with this session.

        :return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank


    .. py:method:: can_create_assessments_offered():
        Tests if this user can create ``AssessmentOffered`` objects.

        A return of true does not guarantee successful authoriization. A
        return of false indicates that it is known creating an
        ``AssessmentOffered`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer create operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``AssessmentOffered`` creation
                is not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_assessment_offered_with_record_types(assessment_offered_record_types):
        Tests if this user can create a single ``AssessmentOffered`` using the desired record types.

        While ``AssessmentManager.getAssessmentOfferedRecordTypes()``
        can be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``AssessmentOffered``. Providing an empty array tests if an
        ``AssessmentOffered`` can be created with no records.

        :arg:    assessment_offered_record_types (osid.type.Type[]):
                array of assessment offered record types
        :return: (boolean) - ``true`` if ``AssessmentOffered`` creation
                using the specified record ``Types`` is supported,
                ``false`` otherwise
        :raises:  NullArgument - ``assessment_offered_record_types`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessment_offered_form_for_create(assessment_id, assessment_offered_record_types):
        Gets the assessment offered form for creating new assessments offered.

        A new form should be requested for each create transaction.

        :arg:    assessment_id (osid.id.Id): the ``Id`` of the related
                ``Assessment``
        :arg:    assessment_offered_record_types (osid.type.Type[]):
                array of assessment offered record types to be included
                in the create operation or an empty list if none
        :return: (osid.assessment.AssessmentOfferedForm) - the assessment
                offered form
        :raises:  NotFound - ``assessment_id`` is not found
        :raises:  NullArgument - ``assessment_id`` or
                ``assessment_offered_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_assessment_offered(assessment_offered_form):
        Creates a new ``AssessmentOffered``.

        :arg:    assessment_offered_form
                (osid.assessment.AssessmentOfferedForm): the form for
                this ``AssessmentOffered``
        :return: (osid.assessment.AssessmentOffered) - the new
                ``AssessmentOffered``
        :raises:  IllegalState - ``assessment_offrered_form`` already used
                in a create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``assessment_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``assessment_form`` did not originate from
                ``get_assessment_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_assessments_offered():
        Tests if this user can update ``AssessmentOffered`` objects.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``AssessmentOffered`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Assessment`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessment_offered_form_for_update(assessment_offered_id):
        Gets the assessment offered form for updating an existing assessment offered.

        A new assessment offered form should be requested for each
        update transaction.

        :arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                ``AssessmentOffered``
        :return: (osid.assessment.AssessmentOfferedForm) - the assessment
                offered form
        :raises:  NotFound - ``assessment_offered_id`` is not found
        :raises:  NullArgument - ``assessment_offered_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_assessment_offered(assessment_offered_form):
        Updates an existing assessment offered.

        :arg:    assessment_offered_form
                (osid.assessment.AssessmentOfferedForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``assessment_offrered_form`` already used
                in an update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``assessment_offered_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``assessment_form`` did not originate from
                ``get_assessment_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_assessments_offered():
        Tests if this user can delete ``AssessmentsOffered``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``AssessmentOffered`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer a delete operations to unauthorized users.

        :return: (boolean) - ``false`` if ``AssessmentOffered`` deletion
                is not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_assessment_offered(assessment_offered_id):
        Deletes an ``AssessmentOffered``.

        :arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                ``AssessmentOffered`` to remove
        :raises:  NotFound - ``assessment_offered_id`` not found
        :raises:  NullArgument - ``assessment_offered_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_assessment_offered_aliases():
        Tests if this user can manage ``Id`` aliases for ``AssessmentsOffered``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``AssessmentOffered`` aliasing
                is not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_assessment_offered(assessment_offered_id, alias_id):
        Adds an ``Id`` to an ``AssessmentOffered`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``AssessmentOffered`` is determined by
        the provider. The new ``Id`` is an alias to the primary ``Id``.
        If the alias is a pointer to another assessment offered, it is
        reassigned to the given assessment offered ``Id``.

        :arg:    assessment_offered_id (osid.id.Id): the ``Id`` of an
                ``AssessmentOffered``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is in use as a primary
                ``Id``
        :raises:  NotFound - ``assessment_offered_id`` not found
        :raises:  NullArgument - ``assessment_offered_id`` or ``alias_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*






Assessment Taken Lookup Methods
-------------------------------

    .. py:method:: get_bank_id():
        Gets the ``Bank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_id


    .. py:method:: get_bank():
        Gets the ``Bank`` associated with this session.

        :return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank


    .. py:method:: can_lookup_assessments_taken():
        Tests if this user can perform ``AssessmentTaken`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_assessment_taken_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as assessment, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_assessment_taken_view():
        A complete view of the ``AssessmentTaken`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_bank_view():
        Federates the view for methods in this session.

        A federated view will include assessments in banks which are
        children of this bank in the bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_bank_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_assessment_taken(assessment_taken_id):
        Gets the ``AssessmentTaken`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``AssessmentTaken`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``AssessmentTaken`` and
        retained for compatibility.

        :arg:    assessment_taken_id (osid.id.Id): ``Id`` of the
                ``AssessmentTaken``
        :return: (osid.assessment.AssessmentTaken) - the assessment taken
        :raises:  NotFound - ``assessment_taken_id`` not found
        :raises:  NullArgument - ``assessment_taken_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_assessments_taken_by_ids(assessment_taken_ids):
        Gets an ``AssessmentTakenList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        assessments specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``AssessmentTaken`` objects may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :arg:    assessment_taken_ids (osid.id.IdList): the list of
                ``Ids`` to retrieve
        :return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken list``
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``assessment_taken_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_by_genus_type(assessment_taken_genus_type):
        Gets an ``AssessmentTakenList`` corresponding to the given assessment taken genus ``Type``
            which does not include assessments of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :arg:    assessment_taken_genus_type (osid.type.Type): an
                assessment taken genus type
        :return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken list``
        :raises:  NullArgument - ``assessment_taken_genus_type`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_by_parent_genus_type(assessment_taken_genus_type):
        Gets an ``AssessmentTakenList`` corresponding to the given assessment taken genus ``Type``
            and include any additional assessments with genus types derived from the specified
            ``Type``.

        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments taken that are accessible
        through this session.

        :arg:    assessment_taken_genus_type (osid.type.Type): an
                assessment taken genus type
        :return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken list``
        :raises:  NullArgument - ``assessment_taken_genus_type`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_by_record_type(assessment_taken_record_type):
        Gets an ``AssessmentTakenList`` corresponding to the given assessment taken record ``Type``.

        The set of assessments implementing the given record type is
        returned. In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session. In both cases, the order of the
        set is not specified.

        :arg:    assessment_taken_record_type (osid.type.Type): an
                assessment taken record type
        :return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        :raises:  NullArgument - ``assessment_taken_record_type`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_by_date(from_, to):
        Gets an ``AssessmentTakenList`` started in the given date range inclusive.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session. In both cases, the order of the
        set is not specified.

        :arg:    from (osid.calendaring.DateTime): start date
        :arg:    to (osid.calendaring.DateTime): end date
        :return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        :raises:  InvalidArgument - ``from`` is greater than ``to``
        :raises:  NullArgument - ``from`` or ``to`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_for_taker(resource_id):
        Gets an ``AssessmentTakenList`` for the given resource.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        :return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_by_date_for_taker(resource_id, from_, to):
        Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given
            resource.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        :arg:    from (osid.calendaring.DateTime): start date
        :arg:    to (osid.calendaring.DateTime): end date
        :return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        :raises:  InvalidArgument - ``from`` is greater than ``to``
        :raises:  NullArgument - ``resource_id, from`` or ``to`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_for_assessment(assessment_id):
        Gets an ``AssessmentTakenList`` for the given assessment.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :arg:    assessment_id (osid.id.Id): ``Id`` of an ``Assessment``
        :return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        :raises:  NullArgument - ``assessment_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_by_date_for_assessment(assessment_id, from_, to):
        Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given
            assessment.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :arg:    assessment_id (osid.id.Id): ``Id`` of an ``Assessment``
        :arg:    from (osid.calendaring.DateTime): start date
        :arg:    to (osid.calendaring.DateTime): end date
        :return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        :raises:  InvalidArgument - ``from`` is greater than ``to``
        :raises:  NullArgument - ``assessment_id, from`` or ``to`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_for_taker_and_assessment(resource_id, assessment_id):
        Gets an ``AssessmentTakenList`` for the given resource and assessment.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        :arg:    assessment_id (osid.id.Id): ``Id`` of an ``Assessment``
        :return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        :raises:  NullArgument - ``resource_id`` or ``assessment_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_by_date_for_taker_and_assessment(resource_id, assessment_id, from_, to):
        Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given
            resource and assessment.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        :arg:    assessment_id (osid.id.Id): ``Id`` of an ``Assessment``
        :arg:    from (osid.calendaring.DateTime): start date
        :arg:    to (osid.calendaring.DateTime): end date
        :return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        :raises:  InvalidArgument - ``from`` is greater than ``to``
        :raises:  NullArgument - ``resource_id, assessment_id, from`` or
                ``to`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_for_assessment_offered(assessment_offered_id):
        Gets an ``AssessmentTakenList`` by the given assessment offered.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :arg:    assessment_offered_id (osid.id.Id): ``Id`` of an
                ``AssessmentOffered``
        :return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        :raises:  NullArgument - ``assessment_offered_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_by_date_for_assessment_offered(assessment_offered_id, from_, to):
        Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given
            assessment offered.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :arg:    assessment_offered_id (osid.id.Id): ``Id`` of an
                ``AssessmentOffered``
        :arg:    from (osid.calendaring.DateTime): start date
        :arg:    to (osid.calendaring.DateTime): end date
        :return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        :raises:  InvalidArgument - ``from`` is greater than ``to``
        :raises:  NullArgument - ``assessment_offered_id, from,`` or
                ``to`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_for_taker_and_assessment_offered(resource_id, assessment_offered_id):
        Gets an ``AssessmentTakenList`` for the given resource and assessment offered.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        :arg:    assessment_offered_id (osid.id.Id): ``Id`` of an
                ``AssessmentOffered``
        :return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        :raises:  NullArgument - ``resource_id`` or
                ``assessmen_offeredt_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken_by_date_for_taker_and_assessment_offered(resource_id, assessment_offered_id, from_, to):
        Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given
            resource and assessment offered.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        :arg:    assessment_offered_id (osid.id.Id): ``Id`` of an
                ``AssessmentOffered``
        :arg:    from (osid.calendaring.DateTime): start date
        :arg:    to (osid.calendaring.DateTime): end date
        :return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTaken`` list
        :raises:  InvalidArgument - ``from`` is greater than ``to``
        :raises:  NullArgument - ``resource_id, assessment_offered_id,
                from,`` or ``to`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessments_taken():
        Gets all ``AssessmentTaken`` elements.

        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :return: (osid.assessment.AssessmentTakenList) - a list of
                ``AssessmentTaken`` elements
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: assessments_taken




Assessment Taken Query Methods
------------------------------

    .. py:method:: get_bank_id():
        Gets the ``Bank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_id


    .. py:method:: get_bank():
        Gets the ``Bank`` associated with this session.

        :return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank


    .. py:method:: can_search_assessments_taken():
        Tests if this user can perform ``AssessmentTaken`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_federated_bank_view():
        Federates the view for methods in this session.

        A federated view will include assessments taken in banks which
        are children of this bank in the bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_bank_view():
        Isolates the view for methods in this session.

        An isolated view restricts searches to this bank only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_assessment_taken_query():
        Gets an assessment taken query.

        :return: (osid.assessment.AssessmentTakenQuery) - the assessment
                taken query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: assessment_taken_query


    .. py:method:: get_assessments_taken_by_query(assessment_taken_query):
        Gets a list of ``AssessmentTaken`` elements matching the given assessment taken query.

        :arg:    assessment_taken_query
                (osid.assessment.AssessmentTakenQuery): the assessment
                taken query
        :return: (osid.assessment.AssessmentTakenList) - the returned
                ``AssessmentTakenList``
        :raises:  NullArgument - ``assessment_taken_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``assessment_taken_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*






Assessment Taken Admin Methods
------------------------------

    .. py:method:: get_bank_id():
        Gets the ``Bank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank_id


    .. py:method:: get_bank():
        Gets the ``Bank`` associated with this session.

        :return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bank


    .. py:method:: can_create_assessments_taken():
        Tests if this user can create ``AssessmentTaken`` objects.

        A return of true does not guarantee successful authoriization. A
        return of false indicates that it is known creating an
        ``AssessmentTaken`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer create operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``AssessmentTaken`` creation is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_assessment_taken_with_record_types(assessment_taken_record_types):
        Tests if this user can create a single ``AssessmentTaken`` using the desired record types.

        While ``AssessmentManager.getAssessmentTakenRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``AssessmentTaken``. Providing an empty array tests if an
        ``AssessmentTaken`` can be created with no records.

        :arg:    assessment_taken_record_types (osid.type.Type[]): array
                of assessment taken record types
        :return: (boolean) - ``true`` if ``AssessmentTaken`` creation
                using the specified record ``Types`` is supported,
                ``false`` otherwise
        :raises:  NullArgument - ``assessment_taken_record_types`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessment_taken_form_for_create(assessment_offered_id, assessment_taken_record_types):
        Gets the assessment taken form for creating new assessments taken.

        A new form should be requested for each create transaction.

        :arg:    assessment_offered_id (osid.id.Id): the ``Id`` of the
                related ``AssessmentOffered``
        :arg:    assessment_taken_record_types (osid.type.Type[]): array
                of assessment taken record types to be included in the
                create operation or an empty list if none
        :return: (osid.assessment.AssessmentTakenForm) - the assessment
                taken form
        :raises:  NotFound - ``assessment_offered_id`` is not found
        :raises:  NullArgument - ``assessment_offered_id`` or
                ``assessment_taken_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_assessment_taken(assessment_taken_form):
        Creates a new ``AssessmentTaken``.

        :arg:    assessment_taken_form
                (osid.assessment.AssessmentTakenForm): the form for this
                ``AssessmentTaken``
        :return: (osid.assessment.AssessmentTaken) - the new
                ``AssessmentTaken``
        :raises:  IllegalState - ``assessment_taken_form`` already used in
                a create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``assessment_taken_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``assessment_offered_form`` did not
                originate from
                ``get_assessment_taken_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_assessments_taken():
        Tests if this user can update ``AssessmentTaken`` objects.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``AssessmentTaken`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``AssessmentTaken``
                modification is not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assessment_taken_form_for_update(assessment_taken_id):
        Gets the assessment taken form for updating an existing assessment taken.

        A new assessment taken form should be requested for each update
        transaction.

        :arg:    assessment_taken_id (osid.id.Id): the ``Id`` of the
                ``AssessmentTaken``
        :return: (osid.assessment.AssessmentTakenForm) - the assessment
                taken form
        :raises:  NotFound - ``assessment_taken_id`` is not found
        :raises:  NullArgument - ``assessment_taken_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_assessment_taken(assessment_taken_form):
        Updates an existing assessment taken.

        :arg:    assessment_taken_form
                (osid.assessment.AssessmentTakenForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``assessment_taken_form`` already used in
                an update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``assessment_taken_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        :raises:  Unsupported - ``assessment_offered_form`` did not
                originate from
                ``get_assessment_taken_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_assessments_taken():
        Tests if this user can delete ``AssessmentsTaken``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``AssessmentTaken`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer a delete operations to unauthorized users.

        :return: (boolean) - ``false`` if ``AssessmentTaken`` deletion is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_assessment_taken(assessment_taken_id):
        Deletes an ``AssessmentTaken``.

        :arg:    assessment_taken_id (osid.id.Id): the ``Id`` of the
                ``AssessmentTaken`` to remove
        :raises:  NotFound - ``assessment_taken_id`` not found
        :raises:  NullArgument - ``assessment_taken_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_assessment_taken_aliases():
        Tests if this user can manage ``Id`` aliases for ``AssessmentsTaken``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``AssessmentTaken`` aliasing is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_assessment_taken(assessment_taken_id, alias_id):
        Adds an ``Id`` to an ``AssessmentTaken`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``AssessmentTaken`` is determined by
        the provider. The new ``Id`` is an alias to the primary ``Id``.
        If the alias is a pointer to another assessment taken, it is
        reassigned to the given assessment taken ``Id``.

        :arg:    assessment_taken_id (osid.id.Id): the ``Id`` of an
                ``AssessmentTaken``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is in use as a primary
                ``Id``
        :raises:  NotFound - ``assessment_taken_id`` not found
        :raises:  NullArgument - ``assessment_taken_id`` or ``alias_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*






