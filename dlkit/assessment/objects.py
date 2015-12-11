
from ..osid import objects as osid_objects
from ..osid import markers as osid_markers
from ..osid import sessions as osid_sessions


class Question(osid_objects.OsidObject):
    """A ``Question`` represents the question portion of an assessment item.

    Like all OSID objects, a ``Question`` is identified by its ``Id``
    and any persisted references should use the ``Id``.

    """
    



    def get_question_record(self, question_record_type):
        """Gets the item record corresponding to the given ``Question`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``question_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(question_record_type)`` is ``true`` .

        arg:    question_record_type (osid.type.Type): the type of the
                record to retrieve
        return: (osid.assessment.records.QuestionRecord) - the question
                record
        raise:  NullArgument - ``question_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(question_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.QuestionRecord


class QuestionForm(osid_objects.OsidObjectForm):
    """This is the form for creating and updating ``Questions``."""
    



    def get_question_form_record(self, question_record_type):
        """Gets the ``QuestionFormRecord`` corresponding to the given question record ``Type``.

        arg:    question_record_type (osid.type.Type): the question
                record type
        return: (osid.assessment.records.QuestionFormRecord) - the
                question record
        raise:  NullArgument - ``question_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(question_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.QuestionFormRecord


class QuestionList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``QuestionList`` provides a means for accessing ``Question`` elements sequentially either one
        at a time or many at a time.

    Examples: while (ql.hasNext()) { Question question =
    ql.getNextQuestion(); }

    or
      while (ql.hasNext()) {
           Question[] question = al.getNextQuestions(ql.available());
      }


    """
    



    def get_next_question(self):
        """Gets the next ``Question`` in this list.

        return: (osid.assessment.Question) - the next ``Question`` in
                this list. The ``has_next()`` method should be used to
                test that a next ``Question`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Question

    next_question = property(fget=get_next_question)


    def get_next_questions(self, n):
        """Gets the next set of ``Question`` elements in this list which must be less than or equal to the number
        returned from ``available()``.

        arg:    n (cardinal): the number of ``Question`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.assessment.Question) - an array of ``Question``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Question


class Answer(osid_objects.OsidObject):
    """An ``Answer`` represents the question portion of an assessment item.

    Like all OSID objects, an ``Answer`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """
    



    def get_answer_record(self, answer_record_type):
        """Gets the answer record corresponding to the given ``Answer`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested records. The ``answer_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(answer_record_type)`` is ``true`` .

        arg:    answer_record_type (osid.type.Type): the type of the
                record to retrieve
        return: (osid.assessment.records.AnswerRecord) - the answer
                record
        raise:  NullArgument - ``answer_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(answer_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.AnswerRecord


class AnswerForm(osid_objects.OsidObjectForm):
    """This is the form for creating and updating ``Answers``."""
    



    def get_answer_form_record(self, answer_record_type):
        """Gets the ``AnswerFormRecord`` corresponding to the given answer record ``Type``.

        arg:    answer_record_type (osid.type.Type): the answer record
                type
        return: (osid.assessment.records.AnswerFormRecord) - the answer
                record
        raise:  NullArgument - ``answer_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(answer_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.AnswerFormRecord


class AnswerList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``AnswerList`` provides a means for accessing ``Answer`` elements sequentially either one at a
        time or many at a time.

    Examples: while (al.hasNext()) { Answer answer = al.getNextAnswer();
    }

    or
      while (al.hasNext()) {
           Answer[] answer = al.getNextAnswers(al.available());
      }


    """
    



    def get_next_answer(self):
        """Gets the next ``Answer`` in this list.

        return: (osid.assessment.Answer) - the next ``Answer`` in this
                list. The ``has_next()`` method should be used to test
                that a next ``Answer`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Answer

    next_answer = property(fget=get_next_answer)


    def get_next_answers(self, n):
        """Gets the next set of ``Answer`` elements in this list which must be less than or equal to the number returned
        from ``available()``.

        arg:    n (cardinal): the number of ``Answer`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.assessment.Answer) - an array of ``Answer``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Answer


class Item(osid_objects.OsidObject, osid_markers.Aggregateable):
    """An ``Item`` represents an individual assessment item such as a question.

    Like all OSID objects, a ``Item`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    An ``Item`` is composed of a ``Question`` and an ``Answer``.

    """
    



    def get_learning_objective_ids(self):
        """Gets the ``Ids`` of any ``Objectives`` corresponding to this item.

        return: (osid.id.IdList) - the learning objective ``Ids``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    learning_objective_ids = property(fget=get_learning_objective_ids)


    def get_learning_objectives(self):
        """Gets the any ``Objectives`` corresponding to this item.

        return: (osid.learning.ObjectiveList) - the learning objectives
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList

    learning_objectives = property(fget=get_learning_objectives)


    def get_question_id(self):
        """Gets the ``Id`` of the ``Question``.

        return: (osid.id.Id) - the question ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    question_id = property(fget=get_question_id)


    def get_question(self):
        """Gets the question.

        return: (osid.assessment.Question) - the question
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Question

    question = property(fget=get_question)


    def get_answer_ids(self):
        """Gets the ``Ids`` of the answers.

        Questions may have more than one acceptable answer.

        return: (osid.id.IdList) - the answer ``Ids``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    answer_ids = property(fget=get_answer_ids)


    def get_answers(self):
        """Gets the answers.

        return: (osid.assessment.AnswerList) - the answers
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.AnswerList

    answers = property(fget=get_answers)


    def get_item_record(self, item_record_type):
        """Gets the item record corresponding to the given ``Item`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested records. The ``item_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(item_record_type)``
        is ``true`` .

        arg:    item_record_type (osid.type.Type): the type of the
                record to retrieve
        return: (osid.assessment.records.ItemRecord) - the item record
        raise:  NullArgument - ``item_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(item_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.ItemRecord


class ItemForm(osid_objects.OsidObjectForm, osid_objects.OsidAggregateableForm):
    """This is the form for creating and updating ``Items``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ItemAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    



    def get_learning_objectives_metadata(self):
        """Gets the metadata for learning objectives.

        return: (osid.Metadata) - metadata for the learning objectives
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    learning_objectives_metadata = property(fget=get_learning_objectives_metadata)


    def set_learning_objectives(self, objective_ids):
        """Sets the learning objectives.

        arg:    objective_ids (osid.id.Id[]): the learning objective
                ``Ids``
        raise:  InvalidArgument - ``objective_ids`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_learning_objectives(self):
        """Clears the learning objectives.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    learning_objectives = property(fset=set_learning_objectives, fdel=clear_learning_objectives)


    def get_item_form_record(self, item_record_type):
        """Gets the ``ItemnFormRecord`` corresponding to the given item record ``Type``.

        arg:    item_record_type (osid.type.Type): the item record type
        return: (osid.assessment.records.ItemFormRecord) - the item
                record
        raise:  NullArgument - ``item_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(item_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.ItemFormRecord


class ItemList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ItemList`` provides a means for accessing ``Item`` elements sequentially either one at a time
        or many at a time.

    Examples: while (il.hasNext()) { Item item = il.getNextItem(); }

    or
      while (il.hasNext()) {
           Item[] items = il.getNextItems(il.available());
      }


    """
    



    def get_next_item(self):
        """Gets the next ``Item`` in this list.

        return: (osid.assessment.Item) - the next ``Item`` in this list.
                The ``has_next()`` method should be used to test that a
                next ``Item`` is available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Item

    next_item = property(fget=get_next_item)


    def get_next_items(self, n):
        """Gets the next set of ``Item`` elements in this list which must be less than or equal to the number returned
        from ``available()``.

        arg:    n (cardinal): the number of ``Item`` elements requested
                which should be less than or equal to ``available()``
        return: (osid.assessment.Item) - an array of ``Item``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Item


class Assessment(osid_objects.OsidObject):
    """An ``Assessment`` represents a sequence of assessment items.

    Like all OSID objects, an ``Assessment`` is identified by its ``Id``
    and any persisted references should use the ``Id``.

    An ``Assessment`` may have an accompanying rubric used for assessing
    performance. The rubric assessment is established canonically in
    this ``Assessment``.

    """
    



    def get_level_id(self):
        """Gets the ``Id`` of a ``Grade`` corresponding to the assessment difficulty.

        return: (osid.id.Id) - a grade ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    level_id = property(fget=get_level_id)


    def get_level(self):
        """Gets the ``Grade`` corresponding to the assessment difficulty.

        return: (osid.grading.Grade) - the level
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Grade

    level = property(fget=get_level)


    def has_rubric(self):
        """Tests if a rubric assessment is associated with this assessment.

        return: (boolean) - ``true`` if a rubric is available, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_rubric_id(self):
        """Gets the ``Id`` of the rubric.

        return: (osid.id.Id) - an assessment ``Id``
        raise:  IllegalState - ``has_rubric()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    rubric_id = property(fget=get_rubric_id)


    def get_rubric(self):
        """Gets the rubric.

        return: (osid.assessment.Assessment) - the assessment
        raise:  IllegalState - ``has_rubric()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Assessment

    rubric = property(fget=get_rubric)


    def get_assessment_record(self, assessment_record_type):
        """Gets the assessment record corresponding to the given ``Assessment`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``assessment_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(assessment_record_type)`` is ``true`` .

        arg:    assessment_record_type (osid.type.Type): the type of the
                record to retrieve
        return: (osid.assessment.records.AssessmentRecord) - the
                assessment record
        raise:  NullArgument - ``assessment_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_record_type)`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.AssessmentRecord


class AssessmentForm(osid_objects.OsidObjectForm):
    """This is the form for creating and updating ``Assessments``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssessmentAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    



    def get_level_metadata(self):
        """Gets the metadata for a grade level.

        return: (osid.Metadata) - metadata for the grade level
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    level_metadata = property(fget=get_level_metadata)


    def set_level(self, grade_id):
        """Sets the level of difficulty expressed as a ``Grade``.

        arg:    grade_id (osid.id.Id): the grade level
        raise:  InvalidArgument - ``grade_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``grade_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_level(self):
        """Clears the grade level.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    level = property(fset=set_level, fdel=clear_level)


    def get_rubric_metadata(self):
        """Gets the metadata for a rubric assessment.

        return: (osid.Metadata) - metadata for the assesment
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    rubric_metadata = property(fget=get_rubric_metadata)


    def set_rubric(self, assessment_id):
        """Sets the rubric expressed as another assessment.

        arg:    assessment_id (osid.id.Id): the assessment ``Id``
        raise:  InvalidArgument - ``assessment_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``assessment_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_rubric(self):
        """Clears the rubric.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rubric = property(fset=set_rubric, fdel=clear_rubric)


    def get_assessment_form_record(self, assessment_record_type):
        """Gets the ``AssessmentFormRecord`` corresponding to the given assessment record ``Type``.

        arg:    assessment_record_type (osid.type.Type): the assessment
                record type
        return: (osid.assessment.records.AssessmentFormRecord) - the
                assessment record
        raise:  NullArgument - ``assessment_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_record_type)`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.AssessmentFormRecord


class AssessmentList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``AssessmentList`` provides a means for accessing ``Assessment`` elements sequentially either
        one at a time or many at a time.

    Examples: while (al.hasNext()) { Assessment assessment =
    al.getNextAssessment(); }

    or
      while (al.hasNext()) {
           Assessment[] assessments = al.hetNextAssessments(al.available());
      }


    """
    



    def get_next_assessment(self):
        """Gets the next ``Assessment`` in this list.

        return: (osid.assessment.Assessment) - the next ``Assessment``
                in this list. The ``has_next()`` method should be used
                to test that a next ``Assessment`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Assessment

    next_assessment = property(fget=get_next_assessment)


    def get_next_assessments(self, n):
        """Gets the next set of ``Assessment`` elements in this list which must be less than or equal to the number
        returned from ``available()``.

        arg:    n (cardinal): the number of ``Assessment`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.assessment.Assessment) - an array of
                ``Assessment`` elements.The length of the array is less
                than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Assessment


class AssessmentOffered(osid_objects.OsidObject, osid_markers.Subjugateable):
    """An ``AssessmentOffered`` represents a sequence of assessment items.

    Like all OSID objects, an ``AssessmentOffered`` is identified by its
    ``Id`` and any persisted references should use the ``Id``.

    """
    



    def get_assessment_id(self):
        """Gets the assessment ``Id`` corresponding to this assessment offering.

        return: (osid.id.Id) - the assessment id
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    assessment_id = property(fget=get_assessment_id)


    def get_assessment(self):
        """Gets the assessment corresponding to this assessment offereng.

        return: (osid.assessment.Assessment) - the assessment
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Assessment

    assessment = property(fget=get_assessment)


    def get_level_id(self):
        """Gets the ``Id`` of a ``Grade`` corresponding to the assessment difficulty.

        return: (osid.id.Id) - a grade id
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    level_id = property(fget=get_level_id)


    def get_level(self):
        """Gets the ``Grade`` corresponding to the assessment difficulty.

        return: (osid.grading.Grade) - the level
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Grade

    level = property(fget=get_level)


    def are_items_sequential(self):
        """Tests if the items or parts in this assessment are taken sequentially.

        return: (boolean) - ``true`` if the items are taken
                sequentially, ``false`` if the items can be skipped and
                revisited
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def are_items_shuffled(self):
        """Tests if the items or parts appear in a random order.

        return: (boolean) - ``true`` if the items appear in a random
                order, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def has_start_time(self):
        """Tests if there is a fixed start time for this assessment.

        return: (boolean) - ``true`` if there is a fixed start time,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_start_time(self):
        """Gets the start time for this assessment.

        return: (osid.calendaring.DateTime) - the designated start time
        raise:  IllegalState - ``has_start_time()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.DateTime

    start_time = property(fget=get_start_time)


    def has_deadline(self):
        """Tests if there is a fixed end time for this assessment.

        return: (boolean) - ``true`` if there is a fixed end time,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_deadline(self):
        """Gets the end time for this assessment.

        return: (osid.calendaring.DateTime) - the designated end time
        raise:  IllegalState - ``has_deadline()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.DateTime

    deadline = property(fget=get_deadline)


    def has_duration(self):
        """Tests if there is a fixed duration for this assessment.

        return: (boolean) - ``true`` if there is a fixed duration,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_duration(self):
        """Gets the duration for this assessment.

        return: (osid.calendaring.Duration) - the duration
        raise:  IllegalState - ``has_duration()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.Duration

    duration = property(fget=get_duration)


    def is_scored(self):
        """Tests if this assessment will be scored.

        return: (boolean) - ``true`` if this assessment will be scored
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_score_system_id(self):
        """Gets the grade system ``Id`` for the score.

        return: (osid.id.Id) - the grade system ``Id``
        raise:  IllegalState - ``is_scored()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    score_system_id = property(fget=get_score_system_id)


    def get_score_system(self):
        """Gets the grade system for the score.

        return: (osid.grading.GradeSystem) - the grade system
        raise:  IllegalState - ``is_scored()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystem

    score_system = property(fget=get_score_system)


    def is_graded(self):
        """Tests if this assessment will be graded.

        return: (boolean) - ``true`` if this assessment will be graded,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grade_system_id(self):
        """Gets the grade system ``Id`` for the grade.

        return: (osid.id.Id) - the grade system ``Id``
        raise:  IllegalState - ``is_graded()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    grade_system_id = property(fget=get_grade_system_id)


    def get_grade_system(self):
        """Gets the grade system for the grade.

        return: (osid.grading.GradeSystem) - the grade system
        raise:  IllegalState - ``is_graded()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystem

    grade_system = property(fget=get_grade_system)


    def has_rubric(self):
        """Tests if a rubric assessment is associated with this assessment.

        return: (boolean) - ``true`` if a rubric is available, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_rubric_id(self):
        """Gets the ``Id`` of the rubric.

        return: (osid.id.Id) - an assessment offered ``Id``
        raise:  IllegalState - ``has_rubric()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    rubric_id = property(fget=get_rubric_id)


    def get_rubric(self):
        """Gets the rubric.

        return: (osid.assessment.AssessmentOffered) - the assessment
                offered
        raise:  IllegalState - ``has_rubric()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.AssessmentOffered

    rubric = property(fget=get_rubric)


    def get_assessment_offered_record(self, assessment_taken_record_type):
        """Gets the assessment offered record corresponding to the given ``AssessmentOffered`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``assessment_offered_record_type`` may be
        the ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(assessment_offered_record_type)`` is ``true``
        .

        arg:    assessment_taken_record_type (osid.type.Type): an
                assessment offered record type
        return: (osid.assessment.records.AssessmentOfferedRecord) - the
                assessment offered record
        raise:  NullArgument - ``assessment_offered_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_offered_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.AssessmentOfferedRecord


class AssessmentOfferedForm(osid_objects.OsidObjectForm, osid_objects.OsidSubjugateableForm):
    """This is the form for creating and updating an ``AssessmentOffered``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssessmentOfferedAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.

    """
    



    def get_level_metadata(self):
        """Gets the metadata for a grade level.

        return: (osid.Metadata) - metadata for the grade level
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    level_metadata = property(fget=get_level_metadata)


    def set_level(self, grade_id):
        """Sets the level of difficulty expressed as a ``Grade``.

        arg:    grade_id (osid.id.Id): the grade level
        raise:  InvalidArgument - ``grade_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_level(self):
        """Clears the level.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    level = property(fset=set_level, fdel=clear_level)


    def get_items_sequential_metadata(self):
        """Gets the metadata for sequential operation.

        return: (osid.Metadata) - metadata for the sequential flag
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    items_sequential_metadata = property(fget=get_items_sequential_metadata)


    def set_items_sequential(self, sequential):
        """Sets the items sequential flag.

        arg:    sequential (boolean): ``true`` if the items are taken
                sequentially, ``false`` if the items can be skipped and
                revisited
        raise:  InvalidArgument - ``sequential`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_items_sequential(self):
        """Clears the items sequential flag.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    items_sequential = property(fset=set_items_sequential, fdel=clear_items_sequential)


    def get_items_shuffled_metadata(self):
        """Gets the metadata for shuffling items.

        return: (osid.Metadata) - metadata for the shuffled flag
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    items_shuffled_metadata = property(fget=get_items_shuffled_metadata)


    def set_items_shuffled(self, shuffle):
        """Sets the shuffle flag.

        The shuffle flag may be overidden by other assessment sequencing
        rules.

        arg:    shuffle (boolean): ``true`` if the items are shuffled,
                ``false`` if the items appear in the designated order
        raise:  InvalidArgument - ``shuffle`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_items_shuffled(self):
        """Clears the shuffle flag.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    items_shuffled = property(fset=set_items_shuffled, fdel=clear_items_shuffled)


    def get_start_time_metadata(self):
        """Gets the metadata for the assessment start time.

        return: (osid.Metadata) - metadata for the start time
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    start_time_metadata = property(fget=get_start_time_metadata)


    def set_start_time(self, start):
        """Sets the assessment start time.

        arg:    start (osid.calendaring.DateTime): assessment start time
        raise:  InvalidArgument - ``start`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_start_time(self):
        """Clears the start time.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    start_time = property(fset=set_start_time, fdel=clear_start_time)


    def get_deadline_metadata(self):
        """Gets the metadata for the assessment deadline.

        return: (osid.Metadata) - metadata for the end time
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    deadline_metadata = property(fget=get_deadline_metadata)


    def set_deadline(self, end):
        """Sets the assessment end time.

        arg:    end (timestamp): assessment end time
        raise:  InvalidArgument - ``end`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_deadline(self):
        """Clears the deadline.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    deadline = property(fset=set_deadline, fdel=clear_deadline)


    def get_duration_metadata(self):
        """Gets the metadata for the assessment duration.

        return: (osid.Metadata) - metadata for the duration
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    duration_metadata = property(fget=get_duration_metadata)


    def set_duration(self, duration):
        """Sets the assessment duration.

        arg:    duration (osid.calendaring.Duration): assessment
                duration
        raise:  InvalidArgument - ``duration`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_duration(self):
        """Clears the duration.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    duration = property(fset=set_duration, fdel=clear_duration)


    def get_score_system_metadata(self):
        """Gets the metadata for a score system.

        return: (osid.Metadata) - metadata for the grade system
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    score_system_metadata = property(fget=get_score_system_metadata)


    def set_score_system(self, grade_system_id):
        """Sets the scoring system.

        arg:    grade_system_id (osid.id.Id): the grade system
        raise:  InvalidArgument - ``grade_system_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_score_system(self):
        """Clears the score system.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    score_system = property(fset=set_score_system, fdel=clear_score_system)


    def get_grade_system_metadata(self):
        """Gets the metadata for a grading system.

        return: (osid.Metadata) - metadata for the grade system
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    grade_system_metadata = property(fget=get_grade_system_metadata)


    def set_grade_system(self, grade_system_id):
        """Sets the grading system.

        arg:    grade_system_id (osid.id.Id): the grade system
        raise:  InvalidArgument - ``grade_system_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_grade_system(self):
        """Clears the grading system.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    grade_system = property(fset=set_grade_system, fdel=clear_grade_system)


    def get_assessment_offered_form_record(self, assessment_offered_record_type):
        """Gets the ``AssessmentOfferedFormRecord`` corresponding to the given assessment record ``Type``.

        arg:    assessment_offered_record_type (osid.type.Type): the
                assessment offered record type
        return: (osid.assessment.records.AssessmentOfferedFormRecord) -
                the assessment offered record
        raise:  NullArgument - ``assessment_offered_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_offered_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.AssessmentOfferedFormRecord


class AssessmentOfferedList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``AssessmentOfferedList`` provides a means for accessing ``AssessmentTaken`` elements
        sequentially either one at a time or many at a time.

    Examples: while (aol.hasNext()) { AssessmentOffered assessment =
    aol.getNextAssessmentOffered();

    or
      while (aol.hasNext()) {
           AssessmentOffered[] assessments = aol.hetNextAssessmentsOffered(aol.available());
      }


    """
    



    def get_next_assessment_offered(self):
        """Gets the next ``AssessmentOffered`` in this list.

        return: (osid.assessment.AssessmentOffered) - the next
                ``AssessmentOffered`` in this list. The ``has_next()``
                method should be used to test that a next
                ``AssessmentOffered`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.AssessmentOffered

    next_assessment_offered = property(fget=get_next_assessment_offered)


    def get_next_assessments_offered(self, n):
        """Gets the next set of ``AssessmentOffered`` elements in this list which must be less than or equal to the
        number returned from ``available()``.

        arg:    n (cardinal): the number of ``AssessmentOffered``
                elements requested which should be less than or equal to
                ``available()``
        return: (osid.assessment.AssessmentOffered) - an array of
                ``AssessmentOffered`` elements.The length of the array
                is less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.AssessmentOffered


class AssessmentTaken(osid_objects.OsidObject):
    """Represents a taken assessment or an assessment in progress."""
    



    def get_assessment_offered_id(self):
        """Gets the ``Id`` of the ``AssessmentOffered``.

        return: (osid.id.Id) - the assessment offered ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    assessment_offered_id = property(fget=get_assessment_offered_id)


    def get_assessment_offered(self):
        """Gets the ``AssessmentOffered``.

        return: (osid.assessment.AssessmentOffered) - the assessment
                offered
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.AssessmentOffered

    assessment_offered = property(fget=get_assessment_offered)


    def get_taker_id(self):
        """Gets the ``Id`` of the resource who took or is taking this assessment.

        return: (osid.id.Id) - the resource ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    taker_id = property(fget=get_taker_id)


    def get_taker(self):
        """Gets the ``Resource`` taking this assessment.

        return: (osid.resource.Resource) - the resource
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Resource

    taker = property(fget=get_taker)


    def get_taking_agent_id(self):
        """Gets the ``Id`` of the ``Agent`` who took or is taking the assessment.

        return: (osid.id.Id) - the agent ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    taking_agent_id = property(fget=get_taking_agent_id)


    def get_taking_agent(self):
        """Gets the ``Agent``.

        return: (osid.authentication.Agent) - the agent
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.Agent

    taking_agent = property(fget=get_taking_agent)


    def has_started(self):
        """Tests if this assessment has begun.

        return: (boolean) - ``true`` if the assessment has begun,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_actual_start_time(self):
        """Gets the time this assessment was started.

        return: (osid.calendaring.DateTime) - the start time
        raise:  IllegalState - ``has_started()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.DateTime

    actual_start_time = property(fget=get_actual_start_time)


    def has_ended(self):
        """Tests if this assessment has ended.

        return: (boolean) - ``true`` if the assessment has ended,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_completion_time(self):
        """Gets the time of this assessment was completed.

        return: (osid.calendaring.DateTime) - the end time
        raise:  IllegalState - ``has_ended()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.DateTime

    completion_time = property(fget=get_completion_time)


    def get_time_spent(self):
        """Gets the total time spent taking this assessment.

        return: (osid.calendaring.Duration) - the total time spent
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.Duration

    time_spent = property(fget=get_time_spent)


    def get_completion(self):
        """Gets a completion percentage of the assessment.

        return: (cardinal) - the percent complete (0-100)
        *compliance: mandatory -- This method must be implemented.*

        """
        return # cardinal

    completion = property(fget=get_completion)


    def is_scored(self):
        """Tests if a score is available for this assessment.

        return: (boolean) - ``true`` if a score is available, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_score_system_id(self):
        """Gets a score system ``Id`` for the assessment.

        return: (osid.id.Id) - the grade system
        raise:  IllegalState - ``is_score()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    score_system_id = property(fget=get_score_system_id)


    def get_score_system(self):
        """Gets a grade system for the score.

        return: (osid.grading.GradeSystem) - the grade system
        raise:  IllegalState - ``is_scored()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystem

    score_system = property(fget=get_score_system)


    def get_score(self):
        """Gets a score for the assessment.

        return: (decimal) - the score
        raise:  IllegalState - ``is_scored()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # decimal

    score = property(fget=get_score)


    def is_graded(self):
        """Tests if a grade is available for this assessment.

        return: (boolean) - ``true`` if a grade is available, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grade_id(self):
        """Gets a grade ``Id`` for the assessment.

        return: (osid.id.Id) - the grade
        raise:  IllegalState - ``is_graded()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    grade_id = property(fget=get_grade_id)


    def get_grade(self):
        """Gets a grade for the assessment.

        return: (osid.grading.Grade) - the grade
        raise:  IllegalState - ``is_graded()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Grade

    grade = property(fget=get_grade)


    def get_feedback(self):
        """Gets any overall comments available for this assessment by the grader.

        return: (osid.locale.DisplayText) - comments
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    feedback = property(fget=get_feedback)


    def has_rubric(self):
        """Tests if a rubric assessment is associated with this assessment.

        return: (boolean) - ``true`` if a rubric is available, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_rubric_id(self):
        """Gets the ``Id`` of the rubric.

        return: (osid.id.Id) - an assessment taken ``Id``
        raise:  IllegalState - ``has_rubric()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    rubric_id = property(fget=get_rubric_id)


    def get_rubric(self):
        """Gets the rubric.

        return: (osid.assessment.AssessmentTaken) - the assessment taken
        raise:  IllegalState - ``has_rubric()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.AssessmentTaken

    rubric = property(fget=get_rubric)


    def get_assessment_taken_record(self, assessment_taken_record_type):
        """Gets the assessment taken record corresponding to the given ``AssessmentTaken`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``assessment_taken_record_type`` may be
        the ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(assessment_taken_record_type)`` is ``true`` .

        arg:    assessment_taken_record_type (osid.type.Type): an
                assessment taken record type
        return: (osid.assessment.records.AssessmentTakenRecord) - the
                assessment taken record
        raise:  NullArgument - ``assessment_taken_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_taken_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.AssessmentTakenRecord


class AssessmentTakenForm(osid_objects.OsidObjectForm):
    """This is the form for creating and updating an ``AssessmentTaken``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AssessmentTakenAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.

    """
    



    def get_taker_metadata(self):
        """Gets the metadata for a resource to manually set which resource will be taking the assessment.

        return: (osid.Metadata) - metadata for the resource
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    taker_metadata = property(fget=get_taker_metadata)


    def set_taker(self, resource_id):
        """Sets the resource who will be taking this assessment.

        arg:    resource_id (osid.id.Id): the resource Id
        raise:  InvalidArgument - ``resource_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_taker(self):
        """Clears the resource.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    taker = property(fset=set_taker, fdel=clear_taker)


    def get_assessment_taken_form_record(self, assessment_taken_record_type):
        """Gets the ``AssessmentTakenFormRecord`` corresponding to the given assessment taken record ``Type``.

        arg:    assessment_taken_record_type (osid.type.Type): the
                assessment taken record type
        return: (osid.assessment.records.AssessmentTakenFormRecord) -
                the assessment taken record
        raise:  NullArgument - ``assessment_taken_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_taken_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.AssessmentTakenFormRecord


class AssessmentTakenList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``AssessmentTakenList`` provides a means for accessing ``AssessmentTaken`` elements
        sequentially either one at a time or many at a time.

    Examples: while (atl.hasNext()) { AssessmentTaken assessment =
    atl.getNextAssessmentTaken();

    or
      while (atl.hasNext()) {
           AssessmentTaken[] assessments = atl.hetNextAssessmentsTaken(atl.available());
      }


    """
    



    def get_next_assessment_taken(self):
        """Gets the next ``AssessmentTaken`` in this list.

        return: (osid.assessment.AssessmentTaken) - the next
                ``AssessmentTaken`` in this list. The ``has_next()``
                method should be used to test that a next
                ``AssessmentTaken`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.AssessmentTaken

    next_assessment_taken = property(fget=get_next_assessment_taken)


    def get_next_assessments_taken(self, n):
        """Gets the next set of ``AssessmentTaken`` elements in this list which must be less than or equal to the number
        returned from ``available()``.

        arg:    n (cardinal): the number of ``AssessmentTaken`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.assessment.AssessmentTaken) - an array of
                ``AssessmentTaken`` elements.The length of the array is
                less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.AssessmentTaken


class AssessmentSection(osid_objects.OsidObject):
    """Represents an assessment section.

    An assessment section represents a cluster of questions used to
    organize the execution of an assessment. The section is the student
    aspect of an assessment part.

    """
    



    def get_assessment_taken_id(self):
        """Gets the ``Id`` of the ``AssessmentTaken``.

        return: (osid.id.Id) - the assessment taken ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    assessment_taken_id = property(fget=get_assessment_taken_id)


    def get_assessment_taken(self):
        """Gets the ``AssessmentTakeb``.

        return: (osid.assessment.AssessmentTaken) - the assessment taken
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.AssessmentTaken

    assessment_taken = property(fget=get_assessment_taken)


    def has_allocated_time(self):
        """Tests if this section must be completed within an allocated time.

        return: (boolean) - ``true`` if this section has an allocated
                time, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_allocated_time(self):
        """Gets the allocated time for this section.

        return: (osid.calendaring.Duration) - allocated time
        raise:  IllegalState - ``has_allocated_time()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.Duration

    allocated_time = property(fget=get_allocated_time)


    def are_items_sequential(self):
        """Tests if the items or parts in this section are taken sequentially.

        return: (boolean) - ``true`` if the items are taken
                sequentially, ``false`` if the items can be skipped and
                revisited
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def are_items_shuffled(self):
        """Tests if the items or parts appear in a random order.

        return: (boolean) - ``true`` if the items appear in a random
                order, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_assessment_section_record(self, assessment_section_record_type):
        """Gets the assessment section record corresponding to the given ``AssessmentSection`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``assessment_section_record_type`` may be
        the ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(assessment_section_record_type)`` is ``true``
        .

        arg:    assessment_section_record_type (osid.type.Type): an
                assessment section record type
        return: (osid.assessment.records.AssessmentSectionRecord) - the
                assessment section record
        raise:  NullArgument - ``assessment_section_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(assessment_section_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.AssessmentSectionRecord


class AssessmentSectionList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``AssessmentSectionList`` provides a means for accessing ``AssessmentSection`` elements
        sequentially either one at a time or many at a time.

    Examples: while (asl.hasNext()) { AssessmentSection section =
    asl.getNextAssessmentSection();

    or
      while (asl.hasNext()) {
           AssessmentSection[] sections = asl.hetNextAssessmentSections(asl.available());
      }


    """
    



    def get_next_assessment_section(self):
        """Gets the next ``AssessmentSection`` in this list.

        return: (osid.assessment.AssessmentSection) - the next
                ``AssessmentSection`` in this list. The ``has_next()``
                method should be used to test that a next
                ``AssessmentSection`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.AssessmentSection

    next_assessment_section = property(fget=get_next_assessment_section)


    def get_next_assessment_sections(self, n):
        """Gets the next set of ``AssessmentSection`` elements in this list which must be less than or equal to the
        number returned from ``available()``.

        arg:    n (cardinal): the number of ``AssessmentSection``
                elements requested which should be less than or equal to
                ``available()``
        return: (osid.assessment.AssessmentSection) - an array of
                ``AssessmentSection`` elements.The length of the array
                is less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.AssessmentSection


class Bank(osid_objects.OsidCatalog, osid_sessions.OsidSession):
    """A bank defines a collection of assessments and items."""
    



    def get_bank_record(self, bank_record_type):
        """Gets the bank record corresponding to the given ``Bank`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``bank_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(bank_record_type)``
        is ``true`` .

        arg:    bank_record_type (osid.type.Type): a bank record type
        return: (osid.assessment.records.BankRecord) - the bank record
        raise:  NullArgument - ``bank_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(bank_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.BankRecord


class BankForm(osid_objects.OsidCatalogForm):
    """This is the form for creating and updating banks.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``BankAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    



    def get_bank_form_record(self, bank_record_type):
        """Gets the ``BankFormRecord`` corresponding to the given bank record ``Type``.

        arg:    bank_record_type (osid.type.Type): a bank record type
        return: (osid.assessment.records.BankFormRecord) - the bank
                record
        raise:  NullArgument - ``bank_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(bank_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.records.BankFormRecord


class BankList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``BankList`` provides a means for accessing ``Bank`` elements sequentially either one at a time
        or many at a time.

    Examples: while (bl.hasNext()) { Bank bank = bl.getNextBank(); }

    or
      while (bl.hasNext()) {
           Bank[] banks = bl.getNextBanks(bl.available());
      }


    """
    



    def get_next_bank(self):
        """Gets the next ``Bank`` in this list.

        return: (osid.assessment.Bank) - the next ``Bank`` in this list.
                The ``has_next()`` method should be used to test that a
                next ``Bank`` is available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Bank

    next_bank = property(fget=get_next_bank)


    def get_next_banks(self, n):
        """Gets the next set of ``Bank`` elements in this list which must be less than or equal to the return from
        ``available()``.

        arg:    n (cardinal): the number of ``Bank`` elements requested
                which must be less than or equal to ``available()``
        return: (osid.assessment.Bank) - an array of ``Bank``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Bank


class BankNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``BankHierarchySession``.

    """
    



    def get_bank(self):
        """Gets the ``Bank`` at this node.

        return: (osid.assessment.Bank) - the bank represented by this
                node
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Bank

    bank = property(fget=get_bank)


    def get_parent_bank_nodes(self):
        """Gets the parents of this bank.

        return: (osid.assessment.BankNodeList) - the parents of this
                node
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.BankNodeList

    parent_bank_nodes = property(fget=get_parent_bank_nodes)


    def get_child_bank_nodes(self):
        """Gets the children of this bank.

        return: (osid.assessment.BankNodeList) - the children of this
                node
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.BankNodeList

    child_bank_nodes = property(fget=get_child_bank_nodes)


class BankNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``BankNodeList`` provides a means for accessing ``BankNode`` elements sequentially either one
        at a time or many at a time.

    Examples: while (bnl.hasNext()) { BankNode node =
    bnl.getNextBankNode(); }

    or
      while (bnl.hasNext()) {
           BankNode[] nodes = bnl.getNextBankNodes(bnl.available());
      }


    """
    



    def get_next_bank_node(self):
        """Gets the next ``BankNode`` in this list.

        return: (osid.assessment.BankNode) - the next ``BankNode`` in
                this list. The ``has_next()`` method should be used to
                test that a next ``BankNode`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.BankNode

    next_bank_node = property(fget=get_next_bank_node)


    def get_next_bank_nodes(self, n):
        """Gets the next set of ``BankNode`` elements in this list which must be less than or equal to the return from
        ``available()``.

        arg:    n (cardinal): the number of ``BankNode`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.assessment.BankNode) - an array of ``BanklNode``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.BankNode


class ResponseList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ResponseList`` provides a means for accessing ``Response`` elements sequentially either one
        at a time or many at a time.

    Examples: while (rl.hasNext()) { Response response =
    rl.getNextResponse(); }

    or
      while (rl.hasNext()) {
           Response[] responses = rl.getNextResponses(rl.available());
      }


    """
    



    def get_next_response(self):
        """Gets the next ``Response`` in this list.

        return: (osid.assessment.Response) - the next ``Response`` in
                this list. The ``has_next()`` method should be used to
                test that a next ``Response`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Response

    next_response = property(fget=get_next_response)


    def get_next_responses(self, n):
        """Gets the next set of ``Response`` elements in this list which must be less than or equal to the return from
        ``available()``.

        arg:    n (cardinal): the number of ``Response`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.assessment.Response) - an array of ``Response``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Response


