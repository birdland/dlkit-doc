
from ..osid import objects as osid_objects
from ..osid import markers as osid_markers
from ..osid import sessions as osid_sessions


class Objective(osid_objects.OsidObject, osid_markers.Federateable):
    """An ``Objective`` is a statable learning objective."""

    def has_assessment(self):
        """Tests if an assessment is associated with this objective.


        :return: ``true`` if an assessment exists, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_assessment_id(self):
        """Gets the assessment ``Id`` associated with this learning objective.


        :return: the assessment ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_assessment()`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    assessment_id = property(fget=get_assessment_id)

    def get_assessment(self):
        """Gets the assessment associated with this learning objective.


        :return: the assessment
        :rtype: ``osid.assessment.Assessment``
        :raise: ``IllegalState`` -- ``has_assessment()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.assessment.Assessment

    assessment = property(fget=get_assessment)

    def has_knowledge_category(self):
        """Tests if this objective has a knowledge dimension.


        :return: ``true`` if a knowledge category exists, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_knowledge_category_id(self):
        """Gets the grade ``Id`` associated with the knowledge dimension.


        :return: the grade ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_knowledge_category()`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    knowledge_category_id = property(fget=get_knowledge_category_id)

    def get_knowledge_category(self):
        """Gets the grade associated with the knowledge dimension.


        :return: the grade
        :rtype: ``osid.grading.Grade``
        :raise: ``IllegalState`` -- ``has_knowledge_category()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.Grade

    knowledge_category = property(fget=get_knowledge_category)

    def has_cognitive_process(self):
        """Tests if this objective has a cognitive process type.


        :return: ``true`` if a cognitive process exists, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_cognitive_process_id(self):
        """Gets the grade ``Id`` associated with the cognitive process.


        :return: the grade ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_cognitive_process()`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    cognitive_process_id = property(fget=get_cognitive_process_id)

    def get_cognitive_process(self):
        """Gets the grade associated with the cognitive process.


        :return: the grade
        :rtype: ``osid.grading.Grade``
        :raise: ``IllegalState`` -- ``has_cognitive_process()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.Grade

    cognitive_process = property(fget=get_cognitive_process)

    def get_objective_record(self, objective_record_type):
        """Gets the objective bank record corresponding to the given ``Objective`` record ``Type``.


        This method is used to retrieve an object implementing the
        requested record. The ``objective_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(objective_record_type)`` is ``true`` .


        :param objective_record_type: an objective record type
        :type objective_record_type: ``osid.type.Type``
        :return: the objective record
        :rtype: ``osid.learning.records.ObjectiveRecord``
        :raise: ``NullArgument`` -- ``objective_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(objective_record_type)`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.records.ObjectiveRecord


class ObjectiveForm(osid_objects.OsidObjectForm, osid_objects.OsidFederateableForm):
    """This is the form for creating and updating ``Objectives``.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ObjectiveAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.


    """

    def get_assessment_metadata(self):
        """Gets the metadata for an assessment.


        :return: metadata for the assessment
        :rtype: ``osid.Metadata``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.Metadata

    assessment_metadata = property(fget=get_assessment_metadata)

    def set_assessment(self, assessment_id):
        """Sets the assessment.


        :param assessment_id: the new assessment
        :type assessment_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``assessment_id`` is invalid
        :raise: ``NoAccess`` -- ``assessment_id`` cannot be modified
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def clear_assessment(self):
        """Clears the assessment.


        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    assessment = property(fset=set_assessment, fdel=clear_assessment)

    def get_knowledge_category_metadata(self):
        """Gets the metadata for a knowledge category.


        :return: metadata for the knowledge category
        :rtype: ``osid.Metadata``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.Metadata

    knowledge_category_metadata = property(fget=get_knowledge_category_metadata)

    def set_knowledge_category(self, grade_id):
        """Sets the knowledge category.


        :param grade_id: the new knowledge category
        :type grade_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``grade_id`` is invalid
        :raise: ``NoAccess`` -- ``grade_id`` cannot be modified
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def clear_knowledge_category(self):
        """Clears the knowledge category.


        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    knowledge_category = property(fset=set_knowledge_category, fdel=clear_knowledge_category)

    def get_cognitive_process_metadata(self):
        """Gets the metadata for a cognitive process.


        :return: metadata for the cognitive process
        :rtype: ``osid.Metadata``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.Metadata

    cognitive_process_metadata = property(fget=get_cognitive_process_metadata)

    def set_cognitive_process(self, grade_id):
        """Sets the cognitive process.


        :param grade_id: the new cognitive process
        :type grade_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``grade_id`` is invalid
        :raise: ``NoAccess`` -- ``grade_id`` cannot be modified
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def clear_cognitive_process(self):
        """Clears the cognitive process.


        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    cognitive_process = property(fset=set_cognitive_process, fdel=clear_cognitive_process)

    def get_objective_form_record(self, objective_record_type):
        """Gets the ``ObjectiveFormRecord`` corresponding to the given objective record ``Type``.


        :param objective_record_type: the objective record type
        :type objective_record_type: ``osid.type.Type``
        :return: the objective form record
        :rtype: ``osid.learning.records.ObjectiveFormRecord``
        :raise: ``NullArgument`` -- ``objective_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(objective_record_type)`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.records.ObjectiveFormRecord


class ObjectiveList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ObjectiveList`` provides a means for accessing ``Objective``
        elements
    sequentially either one at a time or many at a time.


    Examples: while (ol.hasNext()) { Objective objective =
    ol.getNextObjective(); }




    or
      while (ol.hasNext()) {
           Objective[] objectives = ol.getNextObjectives(ol.available());
      }






    """

    def get_next_objective(self):
        """Gets the next ``Objective`` in this list.


        :return: the next ``Objective`` in this list. The ``has_next()`` method should be used to
            test that a next ``Objective`` is available before calling this method.
        :rtype: ``osid.learning.Objective``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.Objective

    next_objective = property(fget=get_next_objective)

    def get_next_objectives(self, n):
        """Gets the next set of ``Objective`` elements in this list which must be less than or equal
            to the number returned from ``available()``.


        :param n: the number of ``Objective`` elements requested which should be less than or equal
            to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Objective`` elements.The length of the array is less than or equal to
            the number specified.
        :rtype: ``osid.learning.Objective``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.Objective


class ObjectiveNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.


    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``ObjectiveHierarchySession``.


    """

    def get_objective(self):
        """Gets the ``Objective`` at this node.


        :return: the objective represented by this node
        :rtype: ``osid.learning.Objective``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.Objective

    objective = property(fget=get_objective)

    def get_parent_objective_nodes(self):
        """Gets the parents of this objective.


        :return: the parents of the ``id``
        :rtype: ``osid.learning.ObjectiveNodeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.ObjectiveNodeList

    parent_objective_nodes = property(fget=get_parent_objective_nodes)

    def get_child_objective_nodes(self):
        """Gets the children of this objective.


        :return: the children of this objective
        :rtype: ``osid.learning.ObjectiveNodeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.ObjectiveNodeList

    child_objective_nodes = property(fget=get_child_objective_nodes)


class ObjectiveNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ObjectiveNodeList`` provides a means for accessing
        ``ObjectiveNode``
    elements sequentially either one at a time or many at a time.


    Examples: while (onl.hasNext()) { ObjectiveNode node =
    onl.getNextObjectiveNode(); }




    or
      while (onl.hasNext()) {
           ObjectiveNode[] nodes = onl.getNextObjectiveNodes(onl.available());
      }






    """

    def get_next_objective_node(self):
        """Gets the next ``ObjectiveNode`` in this list.


        :return: the next ``ObjectiveNode`` in this list. The ``has_next()`` method should be used
            to test that a next ``ObjectiveNode`` is available before calling this method.
        :rtype: ``osid.learning.ObjectiveNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.ObjectiveNode

    next_objective_node = property(fget=get_next_objective_node)

    def get_next_objective_nodes(self, n):
        """Gets the next set of ``ObjectiveNode`` elements in this list which must be less than or
            equal to the number returned from ``available()``.


        :param n: the number of ``ObjectiveNode`` elements requested which should be less than or
            equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``ObjectiveNode`` elements.The length of the array is less than or
            equal to the number specified.
        :rtype: ``osid.learning.ObjectiveNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.ObjectiveNode


class Activity(osid_objects.OsidObject, osid_markers.Subjugateable):
    """An ``Activity`` represents learning material or other learning activities to meet an
        objective.


    An Activity has may relate to a set of ``Asssts`` for self learning,
    recommended ``Courses`` to take, or a learning ``Assessment``. The
    learning ``Assessment`` differs from the ``Objective``
    ``Assessment`` in that the latter used to test for proficiency in
    the ``Objective``.




    Generally, an ``Activity`` should focus on one of assets, courses,
    assessments, or some other specific activity related to the
    objective described or related in the ``ActivityRecord``.


    """

    def get_objective_id(self):
        """Gets the ``Id`` of the related objective.


        :return: the objective ``Id``
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    objective_id = property(fget=get_objective_id)

    def get_objective(self):
        """Gets the related objective.


        :return: the related objective
        :rtype: ``osid.learning.Objective``
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.Objective

    objective = property(fget=get_objective)

    def is_asset_based_activity(self):
        """Tests if this is an asset based activity.


        :return: ``true`` if this activity is based on assets, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_asset_ids(self):
        """Gets the ``Ids`` of any assets associated with this activity.


        :return: list of asset ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``IllegalState`` -- ``is_asset_based_activity()`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    asset_ids = property(fget=get_asset_ids)

    def get_assets(self):
        """Gets any assets associated with this activity.


        :return: list of assets
        :rtype: ``osid.repository.AssetList``
        :raise: ``IllegalState`` -- ``is_asset_based_activity()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetList

    assets = property(fget=get_assets)

    def is_course_based_activity(self):
        """Tests if this is a course based activity.


        :return: ``true`` if this activity is based on courses, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_course_ids(self):
        """Gets the ``Ids`` of any courses associated with this activity.


        :return: list of course ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``IllegalState`` -- ``is_course_based_activity()`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    course_ids = property(fget=get_course_ids)

    def get_courses(self):
        """Gets any courses associated with this activity.


        :return: list of courses
        :rtype: ``osid.course.CourseList``
        :raise: ``IllegalState`` -- ``is_course_based_activity()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.course.CourseList

    courses = property(fget=get_courses)

    def is_assessment_based_activity(self):
        """Tests if this is an assessment based activity.


        These assessments are for learning the objective and not for
        assessing prodiciency in the objective.


        :return: ``true`` if this activity is based on assessments, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_assessment_ids(self):
        """Gets the ``Ids`` of any assessments associated with this activity.


        :return: list of assessment ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``IllegalState`` -- ``is_assessment_based_activity()`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    assessment_ids = property(fget=get_assessment_ids)

    def get_assessments(self):
        """Gets any assessments associated with this activity.


        :return: list of assessments
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``IllegalState`` -- ``is_assessment_based_activity()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.assessment.AssessmentList

    assessments = property(fget=get_assessments)

    def get_activity_record(self, activity_record_type):
        """Gets the activity record corresponding to the given ``Activity`` record ``Type``.


        This method is used to retrieve an object implementing the
        requested record. The ``activity_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(activity_record_type)`` is ``true`` .


        :param activity_record_type: the type of the record to retrieve
        :type activity_record_type: ``osid.type.Type``
        :return: the activity record
        :rtype: ``osid.learning.records.ActivityRecord``
        :raise: ``NullArgument`` -- ``activity_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(activity_record_type)`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.records.ActivityRecord


class ActivityForm(osid_objects.OsidObjectForm, osid_objects.OsidSubjugateableForm):
    """This is the form for creating and updating ``Activities``.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ActivityAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.


    """

    def get_assets_metadata(self):
        """Gets the metadata for the assets.


        :return: metadata for the assets
        :rtype: ``osid.Metadata``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.Metadata

    assets_metadata = property(fget=get_assets_metadata)

    def set_assets(self, asset_ids):
        """Sets the assets.


        :param asset_ids: the asset ``Ids``
        :type asset_ids: ``osid.id.Id[]``
        :raise: ``InvalidArgument`` -- ``asset_ids`` is invalid
        :raise: ``NullArgument`` -- ``asset_ids`` is ``null``
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def clear_assets(self):
        """Clears the assets.


        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    assets = property(fset=set_assets, fdel=clear_assets)

    def get_courses_metadata(self):
        """Gets the metadata for the courses.


        :return: metadata for the courses
        :rtype: ``osid.Metadata``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.Metadata

    courses_metadata = property(fget=get_courses_metadata)

    def set_courses(self, course_ids):
        """Sets the courses.


        :param course_ids: the course ``Ids``
        :type course_ids: ``osid.id.Id[]``
        :raise: ``InvalidArgument`` -- ``course_ids`` is invalid
        :raise: ``NullArgument`` -- ``course_ids`` is ``null``
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def clear_courses(self):
        """Clears the courses.


        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    courses = property(fset=set_courses, fdel=clear_courses)

    def get_assessments_metadata(self):
        """Gets the metadata for the assessments.


        :return: metadata for the assessments
        :rtype: ``osid.Metadata``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.Metadata

    assessments_metadata = property(fget=get_assessments_metadata)

    def set_assessments(self, assessment_ids):
        """Sets the assessments.


        :param assessment_ids: the assessment ``Ids``
        :type assessment_ids: ``osid.id.Id[]``
        :raise: ``InvalidArgument`` -- ``assessment_ids`` is invalid
        :raise: ``NullArgument`` -- ``assessment_ids`` is ``null``
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def clear_assessments(self):
        """Clears the assessments.


        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    assessments = property(fset=set_assessments, fdel=clear_assessments)

    def get_activity_form_record(self, activity_record_type):
        """Gets the ``ActivityFormRecord`` corresponding to the given activity record ``Type``.


        :param activity_record_type: the activity record type
        :type activity_record_type: ``osid.type.Type``
        :return: the activity form record
        :rtype: ``osid.learning.records.ActivityFormRecord``
        :raise: ``NullArgument`` -- ``activity_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(activity_record_type)`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.records.ActivityFormRecord


class ActivityList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ActivityList`` provides a means for accessing ``Activity``
        elements
    sequentially either one at a time or many at a time.


    Examples: while (al.hasNext()) { Activity activity =
    al.getNextActivity(); }




    or
      while (al.hasNext()) {
           Activity[] activities = al.getNextActivities(al.available());
      }






    """

    def get_next_activity(self):
        """Gets the next ``Activity`` in this list.


        :return: the next ``Activity`` in this list. The ``has_next()`` method should be used to
            test that a next ``Activity`` is available before calling this method.
        :rtype: ``osid.learning.Activity``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.Activity

    next_activity = property(fget=get_next_activity)

    def get_next_activities(self, n):
        """Gets the next set of ``Activity`` elements in this list which must be less than or equal
            to the number returned from ``available()``.


        :param n: the number of ``Activity`` elements requested which should be less than or equal
            to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Activity`` elements.The length of the array is less than or equal to
            the number specified.
        :rtype: ``osid.learning.Activity``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.Activity


class ObjectiveBank(osid_objects.OsidCatalog, osid_sessions.OsidSession):
    """an objective bank defines a collection of objectives."""

    def get_objective_bank_record(self, objective_bank_record_type):
        """Gets the objective bank record corresponding to the given ``ObjectiveBank`` record
            ``Type``.


        This method is used to retrieve an object implementing the
        requested record. The ``objective_bank_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(objective_bank_record_type)`` is ``true`` .


        :param objective_bank_record_type: an objective bank record type
        :type objective_bank_record_type: ``osid.type.Type``
        :return: the objective bank record
        :rtype: ``osid.learning.records.ObjectiveBankRecord``
        :raise: ``NullArgument`` -- ``objective_bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(objective_bank_record_type)`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.records.ObjectiveBankRecord


class ObjectiveBankForm(osid_objects.OsidCatalogForm):
    """This is the form for creating and updating objective banks.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ObjectiveBankAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.


    """

    def get_objective_bank_form_record(self, objective_bank_record_type):
        """Gets the ``ObjectiveBankFormRecord`` corresponding to the given objective bank record
            ``Type``.


        :param objective_bank_record_type: an objective bank record type
        :type objective_bank_record_type: ``osid.type.Type``
        :return: the objective bank form record
        :rtype: ``osid.learning.records.ObjectiveBankFormRecord``
        :raise: ``NullArgument`` -- ``objective_bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(objective_bank_record_type)`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.records.ObjectiveBankFormRecord


class ObjectiveBankList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ObjectiveBankList`` provides a means for accessing
        ``ObjectiveBank``
    elements sequentially either one at a time or many at a time.


    Examples: while (obl.hasNext()) { ObjectiveBank objectiveBanks =
    obl.getNextObjectiveBank(); }




    or
      while (obl.hasNext()) {
           ObjectiveBank[] objectivBanks = obl.getNextObjectiveBanks(obl.available());
      }






    """

    def get_next_objective_bank(self):
        """Gets the next ``ObjectiveBank`` in this list.


        :return: the next ``ObjectiveBank`` in this list. The ``has_next()`` method should be used
            to test that a next ``ObjectiveBank`` is available before calling this method.
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.ObjectiveBank

    next_objective_bank = property(fget=get_next_objective_bank)

    def get_next_objective_banks(self, n):
        """Gets the next set of ``ObjectiveBank`` elements in this list which must be less than or
            equal to the return from ``available()``.


        :param n: the number of ``ObjectiveBank`` elements requested which must be less than or
            equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``ObjectiveBank`` elements.The length of the array is less than or
            equal to the number specified.
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.ObjectiveBank


class ObjectiveBankNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.


    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``ObjectiveBankHierarchySession``.


    """

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` at this node.


        :return: the objective bank represented by this node
        :rtype: ``osid.learning.ObjectiveBank``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    def get_parent_objective_bank_nodes(self):
        """Gets the parents of this objective bank.


        :return: the parents of the ``id``
        :rtype: ``osid.learning.ObjectiveBankNodeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.ObjectiveBankNodeList

    parent_objective_bank_nodes = property(fget=get_parent_objective_bank_nodes)

    def get_child_objective_bank_nodes(self):
        """Gets the children of this objective bank.


        :return: the children of this objective bank
        :rtype: ``osid.learning.ObjectiveBankNodeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.ObjectiveBankNodeList

    child_objective_bank_nodes = property(fget=get_child_objective_bank_nodes)


class ObjectiveBankNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ObjectiveBankNodeList`` provides a means for accessing
    ``ObjectiveBankNode`` elements sequentially either one at a time or many at a time.


    Examples: while (obnl.hasNext()) { ObjectiveBankNode node bank =
    obnl.getNextObjectiveBankNode(); }




    or
      while (obnl.hasNext()) {
           ObjectiveBankNode[] nodes = obnl.getNextObjectiveBankNodes(obnl.available());
      }






    """

    def get_next_objective_bank_node(self):
        """Gets the next ``ObjectiveBankNode`` in this list.


        :return: the next ``ObjectiveBankNode`` in this list. The ``has_next()`` method should be
            used to test that a next ``ObjectiveBankNode`` is available before calling this method.
        :rtype: ``osid.learning.ObjectiveBankNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.ObjectiveBankNode

    next_objective_bank_node = property(fget=get_next_objective_bank_node)

    def get_next_objective_bank_nodes(self, n):
        """Gets the next set of ``ObjectiveBankNode`` elements in this list which must be less than
            or equal to the return from ``available()``.


        :param n: the number of ``ObjectiveBankNode`` elements requested which must be less than or
            equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``ObjectiveBankNode`` elements.The length of the array is less than or
            equal to the number specified.
        :rtype: ``osid.learning.ObjectiveBankNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.learning.ObjectiveBankNode


