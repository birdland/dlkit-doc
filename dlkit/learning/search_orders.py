
from ..osid import search_orders as osid_search_orders


class ObjectiveSearchOrder(osid_search_orders.OsidObjectSearchOrder, osid_search_orders.OsidFederateableSearchOrder):
    """An interface for specifying the ordering of search results."""

    def order_by_assessment(self, style):
        """Specified a preference for ordering results by the assessment.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def supports_assessment_search_order(self):
        """Tests if an ``AssessmentSearchOrder`` is available.

        :return: ``true`` if an assessment search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_assessment_search_order(self):
        """Gets the search order for an assessment.

        :return: the assessment search order
        :rtype: ``osid.assessment.AssessmentSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_assessment_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_assessment_search_order()`` is ``true``.*

        """
        return # osid.assessment.AssessmentSearchOrder

    assessment_search_order = property(fget=get_assessment_search_order)

    def order_by_knowledge_category(self, style):
        """Specifies a preference for ordering the result set by the knowledge category.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def supports_knowledge_category_search_order(self):
        """Tests if a grade search order is available.

        :return: ``true`` if a grade search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_knowledge_category_search_order(self):
        """Gets a grade search order to order on knolwgedge category.

        :return: a grade search order
        :rtype: ``osid.grading.GradeSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_knowledge_category_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_knowledge_category_search_order()`` is ``true``.*

        """
        return # osid.grading.GradeSearchOrder

    knowledge_category_search_order = property(fget=get_knowledge_category_search_order)

    def order_by_cognitive_process(self, style):
        """Specifies a preference for ordering the result set by the cognitive process.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def supports_cognitive_process_search_order(self):
        """Tests if a grade search order is available.

        :return: ``true`` if a grade search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_cognitive_process_search_order(self):
        """Gets a grade search order to order on cognitive process.

        :return: a grade search order
        :rtype: ``osid.grading.GradeSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_cognitive_process_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_cognitive_process_search_order()`` is ``true``.*

        """
        return # osid.grading.GradeSearchOrder

    cognitive_process_search_order = property(fget=get_cognitive_process_search_order)

    def get_objective_search_order_record(self, objective_record_type):
        """Gets the objective search order record corresponding to the given objective record ``Type``.

        Multiple retrievals return the same underlying object.

        :param objective_record_type: an objective record type
        :type objective_record_type: ``osid.type.Type``
        :return: the objective search order record
        :rtype: ``osid.learning.records.ObjectiveSearchOrderRecord``
        :raise: ``NullArgument`` -- ``objective_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(objective_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.records.ObjectiveSearchOrderRecord


class ActivitySearchOrder(osid_search_orders.OsidObjectSearchOrder, osid_search_orders.OsidSubjugateableSearchOrder):
    """An interface for specifying the ordering of search results."""

    def order_by_objective(self, style):
        """Specifies a preference for ordering the result set by the objective.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def supports_objective_search_order(self):
        """Tests if an objective search order is available.

        :return: ``true`` if an objective search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_objective_search_order(self):
        """Gets an objective search order.

        :return: an objective search order
        :rtype: ``osid.learning.ObjectiveSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_objective_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_search_order()`` is ``true``.*

        """
        return # osid.learning.ObjectiveSearchOrder

    objective_search_order = property(fget=get_objective_search_order)

    def get_activity_search_order_record(self, activity_record_type):
        """Gets the activity search order record corresponding to the given activity record ``Type``.

        Multiple retrievals return the same underlying object.

        :param activity_record_type: an activity record type
        :type activity_record_type: ``osid.type.Type``
        :return: the activity search order record
        :rtype: ``osid.learning.records.ActivitySearchOrderRecord``
        :raise: ``NullArgument`` -- ``activity_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(activity_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.records.ActivitySearchOrderRecord


class ProficiencySearchOrder(osid_search_orders.OsidRelationshipSearchOrder):
    """An interface for specifying the ordering of search results."""

    def order_by_resource(self, style):
        """Specifies a preference for ordering the result set by the resource.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def supports_resource_search_order(self):
        """Tests if a resource search order is available.

        :return: ``true`` if a resource search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_resource_search_order(self):
        """Gets a resource search order.

        :return: a resource search order
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_resource_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_search_order()`` is ``true``.*

        """
        return # osid.resource.ResourceSearchOrder

    resource_search_order = property(fget=get_resource_search_order)

    def order_by_objective(self, style):
        """Specifies a preference for ordering the result set by the objective.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def supports_objective_search_order(self):
        """Tests if an objective search order is available.

        :return: ``true`` if an objective search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_objective_search_order(self):
        """Gets an objective search order.

        :return: an objective search order
        :rtype: ``osid.learning.ObjectiveSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_objective_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_search_order()`` is ``true``.*

        """
        return # osid.learning.ObjectiveSearchOrder

    objective_search_order = property(fget=get_objective_search_order)

    def order_by_completion(self, style):
        """Specifies a preference for ordering the result set by the completion.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_by_level(self, style):
        """Specifies a preference for ordering the result set by the level.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def supports_level_search_order(self):
        """Tests if a grade search order is available.

        :return: ``true`` if a grade search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_level_search_order(self):
        """Gets a grade search order.

        :return: a grade search order
        :rtype: ``osid.grading.GradeSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_level_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_level_search_order()`` is ``true``.*

        """
        return # osid.grading.GradeSearchOrder

    level_search_order = property(fget=get_level_search_order)

    def get_proficiency_search_order_record(self, proficiency_record_type):
        """Gets the proficiency search order record corresponding to the given proficiency record ``Type``.

        Multiple retrievals return the same underlying object.

        :param proficiency_record_type: a proficiency record type
        :type proficiency_record_type: ``osid.type.Type``
        :return: the proficiency search order record
        :rtype: ``osid.learning.records.ProficiencySearchOrderRecord``
        :raise: ``NullArgument`` -- ``proficiency_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(proficiency_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.records.ProficiencySearchOrderRecord


class ObjectiveBankSearchOrder(osid_search_orders.OsidCatalogSearchOrder):
    """An interface for specifying the ordering of search results."""

    def get_objective_bank_search_order_record(self, objective_bank_record_type):
        """Gets the objective bank search order record corresponding to the given objective bank record ``Type``.

        Multiple retrievals return the same underlying object.

        :param objective_bank_record_type: an objective bank record type
        :type objective_bank_record_type: ``osid.type.Type``
        :return: the objective bank search order record
        :rtype: ``osid.learning.records.ObjectiveBankSearchOrderRecord``
        :raise: ``NullArgument`` -- ``objective_bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(objective_bank_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.records.ObjectiveBankSearchOrderRecord


