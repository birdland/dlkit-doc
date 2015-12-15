

Objects
=======


Objective
---------

.. py:class:: Objective(abc_learning_objects.Objective, osid_objects.OsidObject, osid_markers.Federateable)
    An ``Objective`` is a statable learning objective.

    .. py:method:: has_assessment():
        :noindex:


    .. py:method:: get_assessment_id():
        :noindex:


    .. py:attribute:: assessment_id
        :noindex:


    .. py:method:: get_assessment():
        :noindex:


    .. py:attribute:: assessment
        :noindex:


    .. py:method:: has_knowledge_category():
        :noindex:


    .. py:method:: get_knowledge_category_id():
        :noindex:


    .. py:attribute:: knowledge_category_id
        :noindex:


    .. py:method:: get_knowledge_category():
        :noindex:


    .. py:attribute:: knowledge_category
        :noindex:


    .. py:method:: has_cognitive_process():
        :noindex:


    .. py:method:: get_cognitive_process_id():
        :noindex:


    .. py:attribute:: cognitive_process_id
        :noindex:


    .. py:method:: get_cognitive_process():
        :noindex:


    .. py:attribute:: cognitive_process
        :noindex:


    .. py:method:: get_objective_record(objective_record_type):
        :noindex:


Objective Form
--------------

.. py:class:: ObjectiveForm(abc_learning_objects.ObjectiveForm, osid_objects.OsidObjectForm, osid_objects.OsidFederateableForm)
    This is the form for creating and updating ``Objectives``.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ObjectiveAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_assessment_metadata():
        :noindex:


    .. py:attribute:: assessment_metadata
        :noindex:


    .. py:method:: set_assessment(assessment_id):
        :noindex:


    .. py:method:: clear_assessment():
        :noindex:


    .. py:attribute:: assessment
        :noindex:


    .. py:method:: get_knowledge_category_metadata():
        :noindex:


    .. py:attribute:: knowledge_category_metadata
        :noindex:


    .. py:method:: set_knowledge_category(grade_id):
        :noindex:


    .. py:method:: clear_knowledge_category():
        :noindex:


    .. py:attribute:: knowledge_category
        :noindex:


    .. py:method:: get_cognitive_process_metadata():
        :noindex:


    .. py:attribute:: cognitive_process_metadata
        :noindex:


    .. py:method:: set_cognitive_process(grade_id):
        :noindex:


    .. py:method:: clear_cognitive_process():
        :noindex:


    .. py:attribute:: cognitive_process
        :noindex:


    .. py:method:: get_objective_form_record(objective_record_type):
        :noindex:


Objective List
--------------

.. py:class:: ObjectiveList(abc_learning_objects.ObjectiveList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``ObjectiveList`` provides a means for accessing ``Objective`` elements
    sequentially either one at a time or many at a time.


    Examples: while (ol.hasNext()) { Objective objective =
    ol.getNextObjective(); }




    or
      while (ol.hasNext()) {
           Objective[] objectives = ol.getNextObjectives(ol.available());
      }









    .. py:method:: get_next_objective():
        :noindex:


    .. py:attribute:: next_objective
        :noindex:


    .. py:method:: get_next_objectives(n):
        :noindex:


Objective Node
--------------

.. py:class:: ObjectiveNode(abc_learning_objects.ObjectiveNode, osid_objects.OsidNode)
    This interface is a container for a partial hierarchy retrieval.


    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``ObjectiveHierarchySession``.





    .. py:method:: get_objective():
        :noindex:


    .. py:attribute:: objective
        :noindex:


    .. py:method:: get_parent_objective_nodes():
        :noindex:


    .. py:attribute:: parent_objective_nodes
        :noindex:


    .. py:method:: get_child_objective_nodes():
        :noindex:


    .. py:attribute:: child_objective_nodes
        :noindex:


Objective Node List
-------------------

.. py:class:: ObjectiveNodeList(abc_learning_objects.ObjectiveNodeList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``ObjectiveNodeList`` provides a means for accessing ``ObjectiveNode``
    elements sequentially either one at a time or many at a time.


    Examples: while (onl.hasNext()) { ObjectiveNode node =
    onl.getNextObjectiveNode(); }




    or
      while (onl.hasNext()) {
           ObjectiveNode[] nodes = onl.getNextObjectiveNodes(onl.available());
      }









    .. py:method:: get_next_objective_node():
        :noindex:


    .. py:attribute:: next_objective_node
        :noindex:


    .. py:method:: get_next_objective_nodes(n):
        :noindex:


Activity
--------

.. py:class:: Activity(abc_learning_objects.Activity, osid_objects.OsidObject, osid_markers.Subjugateable)
    An ``Activity`` represents learning material or other learning activities to meet an objective.


    An Activity has may relate to a set of ``Asssts`` for self learning,
    recommended ``Courses`` to take, or a learning ``Assessment``. The
    learning ``Assessment`` differs from the ``Objective``
    ``Assessment`` in that the latter used to test for proficiency in
    the ``Objective``.




    Generally, an ``Activity`` should focus on one of assets, courses,
    assessments, or some other specific activity related to the
    objective described or related in the ``ActivityRecord``.





    .. py:method:: get_objective_id():
        :noindex:


    .. py:attribute:: objective_id
        :noindex:


    .. py:method:: get_objective():
        :noindex:


    .. py:attribute:: objective
        :noindex:


    .. py:method:: is_asset_based_activity():
        :noindex:


    .. py:method:: get_asset_ids():
        :noindex:


    .. py:attribute:: asset_ids
        :noindex:


    .. py:method:: get_assets():
        :noindex:


    .. py:attribute:: assets
        :noindex:


    .. py:method:: is_course_based_activity():
        :noindex:


    .. py:method:: get_course_ids():
        :noindex:


    .. py:attribute:: course_ids
        :noindex:


    .. py:method:: get_courses():
        :noindex:


    .. py:attribute:: courses
        :noindex:


    .. py:method:: is_assessment_based_activity():
        :noindex:


    .. py:method:: get_assessment_ids():
        :noindex:


    .. py:attribute:: assessment_ids
        :noindex:


    .. py:method:: get_assessments():
        :noindex:


    .. py:attribute:: assessments
        :noindex:


    .. py:method:: get_activity_record(activity_record_type):
        :noindex:


Activity Form
-------------

.. py:class:: ActivityForm(abc_learning_objects.ActivityForm, osid_objects.OsidObjectForm, osid_objects.OsidSubjugateableForm)
    This is the form for creating and updating ``Activities``.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ActivityAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_assets_metadata():
        :noindex:


    .. py:attribute:: assets_metadata
        :noindex:


    .. py:method:: set_assets(asset_ids):
        :noindex:


    .. py:method:: clear_assets():
        :noindex:


    .. py:attribute:: assets
        :noindex:


    .. py:method:: get_courses_metadata():
        :noindex:


    .. py:attribute:: courses_metadata
        :noindex:


    .. py:method:: set_courses(course_ids):
        :noindex:


    .. py:method:: clear_courses():
        :noindex:


    .. py:attribute:: courses
        :noindex:


    .. py:method:: get_assessments_metadata():
        :noindex:


    .. py:attribute:: assessments_metadata
        :noindex:


    .. py:method:: set_assessments(assessment_ids):
        :noindex:


    .. py:method:: clear_assessments():
        :noindex:


    .. py:attribute:: assessments
        :noindex:


    .. py:method:: get_activity_form_record(activity_record_type):
        :noindex:


Activity List
-------------

.. py:class:: ActivityList(abc_learning_objects.ActivityList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``ActivityList`` provides a means for accessing ``Activity`` elements
    sequentially either one at a time or many at a time.


    Examples: while (al.hasNext()) { Activity activity =
    al.getNextActivity(); }




    or
      while (al.hasNext()) {
           Activity[] activities = al.getNextActivities(al.available());
      }









    .. py:method:: get_next_activity():
        :noindex:


    .. py:attribute:: next_activity
        :noindex:


    .. py:method:: get_next_activities(n):
        :noindex:


Objective Bank
--------------

.. py:class:: ObjectiveBank(abc_learning_objects.ObjectiveBank, osid_objects.OsidCatalog)
        :noindex:

    .. py:method:: get_objective_bank_record(objective_bank_record_type):
        :noindex:


Objective Bank Form
-------------------

.. py:class:: ObjectiveBankForm(abc_learning_objects.ObjectiveBankForm, osid_objects.OsidCatalogForm)
    This is the form for creating and updating objective banks.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ObjectiveBankAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_objective_bank_form_record(objective_bank_record_type):
        :noindex:


Objective Bank List
-------------------

.. py:class:: ObjectiveBankList(abc_learning_objects.ObjectiveBankList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``ObjectiveBankList`` provides a means for accessing ``ObjectiveBank``
    elements sequentially either one at a time or many at a time.


    Examples: while (obl.hasNext()) { ObjectiveBank objectiveBanks =
    obl.getNextObjectiveBank(); }




    or
      while (obl.hasNext()) {
           ObjectiveBank[] objectivBanks = obl.getNextObjectiveBanks(obl.available());
      }









    .. py:method:: get_next_objective_bank():
        :noindex:


    .. py:attribute:: next_objective_bank
        :noindex:


    .. py:method:: get_next_objective_banks(n):
        :noindex:


Objective Bank Node
-------------------

.. py:class:: ObjectiveBankNode(abc_learning_objects.ObjectiveBankNode, osid_objects.OsidNode)
    This interface is a container for a partial hierarchy retrieval.


    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``ObjectiveBankHierarchySession``.





    .. py:method:: get_objective_bank():
        :noindex:


    .. py:attribute:: objective_bank
        :noindex:


    .. py:method:: get_parent_objective_bank_nodes():
        :noindex:


    .. py:attribute:: parent_objective_bank_nodes
        :noindex:


    .. py:method:: get_child_objective_bank_nodes():
        :noindex:


    .. py:attribute:: child_objective_bank_nodes
        :noindex:


Objective Bank Node List
------------------------

.. py:class:: ObjectiveBankNodeList(abc_learning_objects.ObjectiveBankNodeList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``ObjectiveBankNodeList`` provides a means for accessing
    ``ObjectiveBankNode`` elements sequentially either one at a time or many at a time.


    Examples: while (obnl.hasNext()) { ObjectiveBankNode node bank =
    obnl.getNextObjectiveBankNode(); }




    or
      while (obnl.hasNext()) {
           ObjectiveBankNode[] nodes = obnl.getNextObjectiveBankNodes(obnl.available());
      }









    .. py:method:: get_next_objective_bank_node():
        :noindex:


    .. py:attribute:: next_objective_bank_node
        :noindex:


    .. py:method:: get_next_objective_bank_nodes(n):
        :noindex:


