

Objects
=======


Question
--------

.. py:class:: Question(abc_assessment_objects.Question, osid_objects.OsidObject)
    A ``Question`` represents the question portion of an assessment item.


    Like all OSID objects, a ``Question`` is identified by its ``Id``
    and any persisted references should use the ``Id``.





    .. py:method:: get_question_record(question_record_type):
        :noindex:


Question Form
-------------

.. py:class:: QuestionForm(abc_assessment_objects.QuestionForm, osid_objects.OsidObjectForm)
    This is the form for creating and updating ``Questions``.

    .. py:method:: get_question_form_record(question_record_type):
        :noindex:


Question List
-------------

.. py:class:: QuestionList(abc_assessment_objects.QuestionList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``QuestionList`` provides a means for accessing ``Question`` elements
    sequentially either one at a time or many at a time.


    Examples: while (ql.hasNext()) { Question question =
    ql.getNextQuestion(); }




    or
      while (ql.hasNext()) {
           Question[] question = al.getNextQuestions(ql.available());
      }









    .. py:method:: get_next_question():
        :noindex:


    .. py:attribute:: next_question
        :noindex:


    .. py:method:: get_next_questions(n):
        :noindex:


Answer
------

.. py:class:: Answer(abc_assessment_objects.Answer, osid_objects.OsidObject)
    An ``Answer`` represents the question portion of an assessment item.


    Like all OSID objects, an ``Answer`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.





    .. py:method:: get_answer_record(answer_record_type):
        :noindex:


Answer Form
-----------

.. py:class:: AnswerForm(abc_assessment_objects.AnswerForm, osid_objects.OsidObjectForm)
    This is the form for creating and updating ``Answers``.

    .. py:method:: get_answer_form_record(answer_record_type):
        :noindex:


Answer List
-----------

.. py:class:: AnswerList(abc_assessment_objects.AnswerList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``AnswerList`` provides a means for accessing ``Answer`` elements
    sequentially either one at a time or many at a time.


    Examples: while (al.hasNext()) { Answer answer = al.getNextAnswer();
    }




    or
      while (al.hasNext()) {
           Answer[] answer = al.getNextAnswers(al.available());
      }









    .. py:method:: get_next_answer():
        :noindex:


    .. py:attribute:: next_answer
        :noindex:


    .. py:method:: get_next_answers(n):
        :noindex:


Item
----

.. py:class:: Item(abc_assessment_objects.Item, osid_objects.OsidObject, osid_markers.Aggregateable)
    An ``Item`` represents an individual assessment item such as a question.


    Like all OSID objects, a ``Item`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.




    An ``Item`` is composed of a ``Question`` and an ``Answer``.





    .. py:method:: get_learning_objective_ids():
        :noindex:


    .. py:attribute:: learning_objective_ids
        :noindex:


    .. py:method:: get_learning_objectives():
        :noindex:


    .. py:attribute:: learning_objectives
        :noindex:


    .. py:method:: get_question_id():
        :noindex:


    .. py:attribute:: question_id
        :noindex:


    .. py:method:: get_question():
        :noindex:


    .. py:attribute:: question
        :noindex:


    .. py:method:: get_answer_ids():
        :noindex:


    .. py:attribute:: answer_ids
        :noindex:


    .. py:method:: get_answers():
        :noindex:


    .. py:attribute:: answers
        :noindex:


    .. py:method:: get_item_record(item_record_type):
        :noindex:


Item Form
---------

.. py:class:: ItemForm(abc_assessment_objects.ItemForm, osid_objects.OsidObjectForm, osid_objects.OsidAggregateableForm)
    This is the form for creating and updating ``Items``.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ItemAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_learning_objectives_metadata():
        :noindex:


    .. py:attribute:: learning_objectives_metadata
        :noindex:


    .. py:method:: set_learning_objectives(objective_ids):
        :noindex:


    .. py:method:: clear_learning_objectives():
        :noindex:


    .. py:attribute:: learning_objectives
        :noindex:


    .. py:method:: get_item_form_record(item_record_type):
        :noindex:


Item List
---------

.. py:class:: ItemList(abc_assessment_objects.ItemList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``ItemList`` provides a means for accessing ``Item`` elements
        sequentially
    either one at a time or many at a time.


    Examples: while (il.hasNext()) { Item item = il.getNextItem(); }




    or
      while (il.hasNext()) {
           Item[] items = il.getNextItems(il.available());
      }









    .. py:method:: get_next_item():
        :noindex:


    .. py:attribute:: next_item
        :noindex:


    .. py:method:: get_next_items(n):
        :noindex:


Assessment
----------

.. py:class:: Assessment(abc_assessment_objects.Assessment, osid_objects.OsidObject)
    An ``Assessment`` represents a sequence of assessment items.


    Like all OSID objects, an ``Assessment`` is identified by its ``Id``
    and any persisted references should use the ``Id``.




    An ``Assessment`` may have an accompanying rubric used for assessing
    performance. The rubric assessment is established canonically in
    this ``Assessment``.





    .. py:method:: get_level_id():
        :noindex:


    .. py:attribute:: level_id
        :noindex:


    .. py:method:: get_level():
        :noindex:


    .. py:attribute:: level
        :noindex:


    .. py:method:: has_rubric():
        :noindex:


    .. py:method:: get_rubric_id():
        :noindex:


    .. py:attribute:: rubric_id
        :noindex:


    .. py:method:: get_rubric():
        :noindex:


    .. py:attribute:: rubric
        :noindex:


    .. py:method:: get_assessment_record(assessment_record_type):
        :noindex:


Assessment Form
---------------

.. py:class:: AssessmentForm(abc_assessment_objects.AssessmentForm, osid_objects.OsidObjectForm)
    This is the form for creating and updating ``Assessments``.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssessmentAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_level_metadata():
        :noindex:


    .. py:attribute:: level_metadata
        :noindex:


    .. py:method:: set_level(grade_id):
        :noindex:


    .. py:method:: clear_level():
        :noindex:


    .. py:attribute:: level
        :noindex:


    .. py:method:: get_rubric_metadata():
        :noindex:


    .. py:attribute:: rubric_metadata
        :noindex:


    .. py:method:: set_rubric(assessment_id):
        :noindex:


    .. py:method:: clear_rubric():
        :noindex:


    .. py:attribute:: rubric
        :noindex:


    .. py:method:: get_assessment_form_record(assessment_record_type):
        :noindex:


Assessment List
---------------

.. py:class:: AssessmentList(abc_assessment_objects.AssessmentList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``AssessmentList`` provides a means for accessing ``Assessment``
        elements
    sequentially either one at a time or many at a time.


    Examples: while (al.hasNext()) { Assessment assessment =
    al.getNextAssessment(); }




    or
      while (al.hasNext()) {
           Assessment[] assessments = al.hetNextAssessments(al.available());
      }









    .. py:method:: get_next_assessment():
        :noindex:


    .. py:attribute:: next_assessment
        :noindex:


    .. py:method:: get_next_assessments(n):
        :noindex:


Assessment Offered
------------------

.. py:class:: AssessmentOffered(abc_assessment_objects.AssessmentOffered, osid_objects.OsidObject, osid_markers.Subjugateable)
    An ``AssessmentOffered`` represents a sequence of assessment items.


    Like all OSID objects, an ``AssessmentOffered`` is identified by its
    ``Id`` and any persisted references should use the ``Id``.





    .. py:method:: get_assessment_id():
        :noindex:


    .. py:attribute:: assessment_id
        :noindex:


    .. py:method:: get_assessment():
        :noindex:


    .. py:attribute:: assessment
        :noindex:


    .. py:method:: get_level_id():
        :noindex:


    .. py:attribute:: level_id
        :noindex:


    .. py:method:: get_level():
        :noindex:


    .. py:attribute:: level
        :noindex:


    .. py:method:: are_items_sequential():
        :noindex:


    .. py:method:: are_items_shuffled():
        :noindex:


    .. py:method:: has_start_time():
        :noindex:


    .. py:method:: get_start_time():
        :noindex:


    .. py:attribute:: start_time
        :noindex:


    .. py:method:: has_deadline():
        :noindex:


    .. py:method:: get_deadline():
        :noindex:


    .. py:attribute:: deadline
        :noindex:


    .. py:method:: has_duration():
        :noindex:


    .. py:method:: get_duration():
        :noindex:


    .. py:attribute:: duration
        :noindex:


    .. py:method:: is_scored():
        :noindex:


    .. py:method:: get_score_system_id():
        :noindex:


    .. py:attribute:: score_system_id
        :noindex:


    .. py:method:: get_score_system():
        :noindex:


    .. py:attribute:: score_system
        :noindex:


    .. py:method:: is_graded():
        :noindex:


    .. py:method:: get_grade_system_id():
        :noindex:


    .. py:attribute:: grade_system_id
        :noindex:


    .. py:method:: get_grade_system():
        :noindex:


    .. py:attribute:: grade_system
        :noindex:


    .. py:method:: has_rubric():
        :noindex:


    .. py:method:: get_rubric_id():
        :noindex:


    .. py:attribute:: rubric_id
        :noindex:


    .. py:method:: get_rubric():
        :noindex:


    .. py:attribute:: rubric
        :noindex:


    .. py:method:: get_assessment_offered_record(assessment_taken_record_type):
        :noindex:


Assessment Offered Form
-----------------------

.. py:class:: AssessmentOfferedForm(abc_assessment_objects.AssessmentOfferedForm, osid_objects.OsidObjectForm, osid_objects.OsidSubjugateableForm)
    This is the form for creating and updating an ``AssessmentOffered``.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssessmentOfferedAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_level_metadata():
        :noindex:


    .. py:attribute:: level_metadata
        :noindex:


    .. py:method:: set_level(grade_id):
        :noindex:


    .. py:method:: clear_level():
        :noindex:


    .. py:attribute:: level
        :noindex:


    .. py:method:: get_items_sequential_metadata():
        :noindex:


    .. py:attribute:: items_sequential_metadata
        :noindex:


    .. py:method:: set_items_sequential(sequential):
        :noindex:


    .. py:method:: clear_items_sequential():
        :noindex:


    .. py:attribute:: items_sequential
        :noindex:


    .. py:method:: get_items_shuffled_metadata():
        :noindex:


    .. py:attribute:: items_shuffled_metadata
        :noindex:


    .. py:method:: set_items_shuffled(shuffle):
        :noindex:


    .. py:method:: clear_items_shuffled():
        :noindex:


    .. py:attribute:: items_shuffled
        :noindex:


    .. py:method:: get_start_time_metadata():
        :noindex:


    .. py:attribute:: start_time_metadata
        :noindex:


    .. py:method:: set_start_time(start):
        :noindex:


    .. py:method:: clear_start_time():
        :noindex:


    .. py:attribute:: start_time
        :noindex:


    .. py:method:: get_deadline_metadata():
        :noindex:


    .. py:attribute:: deadline_metadata
        :noindex:


    .. py:method:: set_deadline(end):
        :noindex:


    .. py:method:: clear_deadline():
        :noindex:


    .. py:attribute:: deadline
        :noindex:


    .. py:method:: get_duration_metadata():
        :noindex:


    .. py:attribute:: duration_metadata
        :noindex:


    .. py:method:: set_duration(duration):
        :noindex:


    .. py:method:: clear_duration():
        :noindex:


    .. py:attribute:: duration
        :noindex:


    .. py:method:: get_score_system_metadata():
        :noindex:


    .. py:attribute:: score_system_metadata
        :noindex:


    .. py:method:: set_score_system(grade_system_id):
        :noindex:


    .. py:method:: clear_score_system():
        :noindex:


    .. py:attribute:: score_system
        :noindex:


    .. py:method:: get_grade_system_metadata():
        :noindex:


    .. py:attribute:: grade_system_metadata
        :noindex:


    .. py:method:: set_grade_system(grade_system_id):
        :noindex:


    .. py:method:: clear_grade_system():
        :noindex:


    .. py:attribute:: grade_system
        :noindex:


    .. py:method:: get_assessment_offered_form_record(assessment_offered_record_type):
        :noindex:


Assessment Offered List
-----------------------

.. py:class:: AssessmentOfferedList(abc_assessment_objects.AssessmentOfferedList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``AssessmentOfferedList`` provides a means for accessing
        ``AssessmentTaken``
    elements sequentially either one at a time or many at a time.


    Examples: while (aol.hasNext()) { AssessmentOffered assessment =
    aol.getNextAssessmentOffered();




    or
      while (aol.hasNext()) {
           AssessmentOffered[] assessments = aol.hetNextAssessmentsOffered(aol.available());
      }









    .. py:method:: get_next_assessment_offered():
        :noindex:


    .. py:attribute:: next_assessment_offered
        :noindex:


    .. py:method:: get_next_assessments_offered(n):
        :noindex:


Assessment Taken
----------------

.. py:class:: AssessmentTaken(abc_assessment_objects.AssessmentTaken, osid_objects.OsidObject)
    Represents a taken assessment or an assessment in progress.

    .. py:method:: get_assessment_offered_id():
        :noindex:


    .. py:attribute:: assessment_offered_id
        :noindex:


    .. py:method:: get_assessment_offered():
        :noindex:


    .. py:attribute:: assessment_offered
        :noindex:


    .. py:method:: get_taker_id():
        :noindex:


    .. py:attribute:: taker_id
        :noindex:


    .. py:method:: get_taker():
        :noindex:


    .. py:attribute:: taker
        :noindex:


    .. py:method:: get_taking_agent_id():
        :noindex:


    .. py:attribute:: taking_agent_id
        :noindex:


    .. py:method:: get_taking_agent():
        :noindex:


    .. py:attribute:: taking_agent
        :noindex:


    .. py:method:: has_started():
        :noindex:


    .. py:method:: get_actual_start_time():
        :noindex:


    .. py:attribute:: actual_start_time
        :noindex:


    .. py:method:: has_ended():
        :noindex:


    .. py:method:: get_completion_time():
        :noindex:


    .. py:attribute:: completion_time
        :noindex:


    .. py:method:: get_time_spent():
        :noindex:


    .. py:attribute:: time_spent
        :noindex:


    .. py:method:: get_completion():
        :noindex:


    .. py:attribute:: completion
        :noindex:


    .. py:method:: is_scored():
        :noindex:


    .. py:method:: get_score_system_id():
        :noindex:


    .. py:attribute:: score_system_id
        :noindex:


    .. py:method:: get_score_system():
        :noindex:


    .. py:attribute:: score_system
        :noindex:


    .. py:method:: get_score():
        :noindex:


    .. py:attribute:: score
        :noindex:


    .. py:method:: is_graded():
        :noindex:


    .. py:method:: get_grade_id():
        :noindex:


    .. py:attribute:: grade_id
        :noindex:


    .. py:method:: get_grade():
        :noindex:


    .. py:attribute:: grade
        :noindex:


    .. py:method:: get_feedback():
        :noindex:


    .. py:attribute:: feedback
        :noindex:


    .. py:method:: has_rubric():
        :noindex:


    .. py:method:: get_rubric_id():
        :noindex:


    .. py:attribute:: rubric_id
        :noindex:


    .. py:method:: get_rubric():
        :noindex:


    .. py:attribute:: rubric
        :noindex:


    .. py:method:: get_assessment_taken_record(assessment_taken_record_type):
        :noindex:


Assessment Taken Form
---------------------

.. py:class:: AssessmentTakenForm(abc_assessment_objects.AssessmentTakenForm, osid_objects.OsidObjectForm)
    This is the form for creating and updating an ``AssessmentTaken``.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssessmentTakenAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_taker_metadata():
        :noindex:


    .. py:attribute:: taker_metadata
        :noindex:


    .. py:method:: set_taker(resource_id):
        :noindex:


    .. py:method:: clear_taker():
        :noindex:


    .. py:attribute:: taker
        :noindex:


    .. py:method:: get_assessment_taken_form_record(assessment_taken_record_type):
        :noindex:


Assessment Taken List
---------------------

.. py:class:: AssessmentTakenList(abc_assessment_objects.AssessmentTakenList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``AssessmentTakenList`` provides a means for accessing
        ``AssessmentTaken``
    elements sequentially either one at a time or many at a time.


    Examples: while (atl.hasNext()) { AssessmentTaken assessment =
    atl.getNextAssessmentTaken();




    or
      while (atl.hasNext()) {
           AssessmentTaken[] assessments = atl.hetNextAssessmentsTaken(atl.available());
      }









    .. py:method:: get_next_assessment_taken():
        :noindex:


    .. py:attribute:: next_assessment_taken
        :noindex:


    .. py:method:: get_next_assessments_taken(n):
        :noindex:


Assessment Section
------------------

.. py:class:: AssessmentSection(abc_assessment_objects.AssessmentSection, osid_objects.OsidObject)
    Represents an assessment section.


    An assessment section represents a cluster of questions used to
    organize the execution of an assessment. The section is the student
    aspect of an assessment part.





    .. py:method:: get_assessment_taken_id():
        :noindex:


    .. py:attribute:: assessment_taken_id
        :noindex:


    .. py:method:: get_assessment_taken():
        :noindex:


    .. py:attribute:: assessment_taken
        :noindex:


    .. py:method:: has_allocated_time():
        :noindex:


    .. py:method:: get_allocated_time():
        :noindex:


    .. py:attribute:: allocated_time
        :noindex:


    .. py:method:: are_items_sequential():
        :noindex:


    .. py:method:: are_items_shuffled():
        :noindex:


    .. py:method:: get_assessment_section_record(assessment_section_record_type):
        :noindex:


Assessment Section List
-----------------------

.. py:class:: AssessmentSectionList(abc_assessment_objects.AssessmentSectionList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``AssessmentSectionList`` provides a means for accessing
    ``AssessmentSection`` elements sequentially either one at a time or many at a time.


    Examples: while (asl.hasNext()) { AssessmentSection section =
    asl.getNextAssessmentSection();




    or
      while (asl.hasNext()) {
           AssessmentSection[] sections = asl.hetNextAssessmentSections(asl.available());
      }









    .. py:method:: get_next_assessment_section():
        :noindex:


    .. py:attribute:: next_assessment_section
        :noindex:


    .. py:method:: get_next_assessment_sections(n):
        :noindex:


Bank
----

.. py:class:: Bank(abc_assessment_objects.Bank, osid_objects.OsidCatalog)
        :noindex:

    .. py:method:: get_bank_record(bank_record_type):
        :noindex:


Bank Form
---------

.. py:class:: BankForm(abc_assessment_objects.BankForm, osid_objects.OsidCatalogForm)
    This is the form for creating and updating banks.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``BankAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_bank_form_record(bank_record_type):
        :noindex:


Bank List
---------

.. py:class:: BankList(abc_assessment_objects.BankList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``BankList`` provides a means for accessing ``Bank`` elements
        sequentially
    either one at a time or many at a time.


    Examples: while (bl.hasNext()) { Bank bank = bl.getNextBank(); }




    or
      while (bl.hasNext()) {
           Bank[] banks = bl.getNextBanks(bl.available());
      }









    .. py:method:: get_next_bank():
        :noindex:


    .. py:attribute:: next_bank
        :noindex:


    .. py:method:: get_next_banks(n):
        :noindex:


Bank Node
---------

.. py:class:: BankNode(abc_assessment_objects.BankNode, osid_objects.OsidNode)
    This interface is a container for a partial hierarchy retrieval.


    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``BankHierarchySession``.





    .. py:method:: get_bank():
        :noindex:


    .. py:attribute:: bank
        :noindex:


    .. py:method:: get_parent_bank_nodes():
        :noindex:


    .. py:attribute:: parent_bank_nodes
        :noindex:


    .. py:method:: get_child_bank_nodes():
        :noindex:


    .. py:attribute:: child_bank_nodes
        :noindex:


Bank Node List
--------------

.. py:class:: BankNodeList(abc_assessment_objects.BankNodeList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``BankNodeList`` provides a means for accessing ``BankNode`` elements
    sequentially either one at a time or many at a time.


    Examples: while (bnl.hasNext()) { BankNode node =
    bnl.getNextBankNode(); }




    or
      while (bnl.hasNext()) {
           BankNode[] nodes = bnl.getNextBankNodes(bnl.available());
      }









    .. py:method:: get_next_bank_node():
        :noindex:


    .. py:attribute:: next_bank_node
        :noindex:


    .. py:method:: get_next_bank_nodes(n):
        :noindex:


Response List
-------------

.. py:class:: ResponseList(abc_assessment_objects.ResponseList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``ResponseList`` provides a means for accessing ``Response`` elements
    sequentially either one at a time or many at a time.


    Examples: while (rl.hasNext()) { Response response =
    rl.getNextResponse(); }




    or
      while (rl.hasNext()) {
           Response[] responses = rl.getNextResponses(rl.available());
      }









    .. py:method:: get_next_response():
        :noindex:


    .. py:attribute:: next_response
        :noindex:


    .. py:method:: get_next_responses(n):
        :noindex:


