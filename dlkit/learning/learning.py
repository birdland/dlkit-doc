
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects
from ..osid import markers as osid_markers
from ..osid import records as osid_records
from ..osid import queries as osid_queries
from ..osid import searches as osid_searches


class LearningProfile(osid_managers.OsidProfile):
    """The ``LearningProfile`` describes the interoperability among learning services."""

    def __init__(self):
        self._provider_manager = None

    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_lookup(self):
        """Tests if an objective lookup service is supported.

        An objective lookup service defines methods to access
        objectives.

        :return: true if objective lookup is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_query(self):
        """Tests if an objective query service is supported.

        :return: ``true`` if objective query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_search(self):
        """Tests if an objective search service is supported.

        :return: ``true`` if objective search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_admin(self):
        """Tests if an objective administrative service is supported.

        :return: ``true`` if objective admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_notification(self):
        """Tests if objective notification is supported.

        Messages may be sent when objectives are created, modified, or
        deleted.

        :return: ``true`` if objective notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_hierarchy(self):
        """Tests if an objective hierarchy traversal is supported.

        :return: ``true`` if an objective hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_hierarchy_design(self):
        """Tests if an objective hierarchy design is supported.

        :return: ``true`` if an objective hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_sequencing(self):
        """Tests if an objective sequencing design is supported.

        :return: ``true`` if objective sequencing is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_objective_bank(self):
        """Tests if an objective to objective bank lookup session is available.

        :return: ``true`` if objective objective bank lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_objective_bank_assignment(self):
        """Tests if an objective to objective bank assignment session is available.

        :return: ``true`` if objective objective bank assignment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_smart_objective_bank(self):
        """Tests if an objective smart objective bank cataloging service is supported.

        :return: ``true`` if objective smart objective banks are supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_requisite(self):
        """Tests if an objective requisite service is supported.

        :return: ``true`` if objective requisite service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_requisite_assignment(self):
        """Tests if an objective requisite assignment service is supported.

        :return: ``true`` if objective requisite assignment service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_activity_lookup(self):
        """Tests if an activity lookup service is supported.

        :return: ``true`` if activity lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_activity_query(self):
        """Tests if an activity query service is supported.

        :return: ``true`` if activity query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_activity_search(self):
        """Tests if an activity search service is supported.

        :return: ``true`` if activity search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_activity_admin(self):
        """Tests if an activity administrative service is supported.

        :return: ``true`` if activity admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_activity_notification(self):
        """Tests if activity notification is supported.

        Messages may be sent when activities are created, modified, or
        deleted.

        :return: ``true`` if activity notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_activity_objective_bank(self):
        """Tests if an activity to objective bank lookup session is available.

        :return: ``true`` if activity objective bank lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_activity_objective_bank_assignment(self):
        """Tests if an activity to objective bank assignment session is available.

        :return: ``true`` if activity objective bank assignment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_activity_smart_objective_bank(self):
        """Tests if an activity smart objective bank cataloging service is supported.

        :return: ``true`` if activity smart objective banks are supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_proficiency_lookup(self):
        """Tests if looking up proficiencies is supported.

        :return: ``true`` if proficiency lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_proficiency_query(self):
        """Tests if querying proficiencies is supported.

        :return: ``true`` if proficiency query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_proficiency_search(self):
        """Tests if searching proficiencies is supported.

        :return: ``true`` if proficiency search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_proficiency_admin(self):
        """Tests if proficiencyadministrative service is supported.

        :return: ``true`` if proficiency administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_proficiency_notification(self):
        """Tests if a proficiencynotification service is supported.

        :return: ``true`` if proficiency notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_proficiency_objective_bank(self):
        """Tests if a proficiency objective bank mapping lookup service is supported.

        :return: ``true`` if a proficiency objective bank lookup service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_proficiency_objective_bank_assignment(self):
        """Tests if a proficiency objective bank mapping service is supported.

        :return: ``true`` if proficiency to objective bank mapping service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_proficiency_smart_objective_bank(self):
        """Tests if a proficiency smart objective bank cataloging service is supported.

        :return: ``true`` if proficiency smart objective banks are supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_my_learning_path(self):
        """Tests if a learning path service is supported for the authenticated agent.

        :return: ``true`` if learning path is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_learning_path(self):
        """Tests if a learning path service is supported.

        :return: ``true`` if learning path is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_bank_lookup(self):
        """Tests if an objective bank lookup service is supported.

        :return: ``true`` if objective bank lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_bank_query(self):
        """Tests if an objective bank query service is supported.

        :return: ``true`` if objective bank query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_bank_search(self):
        """Tests if an objective bank search service is supported.

        :return: ``true`` if objective bank search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_bank_admin(self):
        """Tests if an objective bank administrative service is supported.

        :return: ``true`` if objective bank admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_bank_notification(self):
        """Tests if objective bank notification is supported.

        Messages may be sent when objective banks are created, modified,
        or deleted.

        :return: ``true`` if objective bank notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_bank_hierarchy(self):
        """Tests if an objective bank hierarchy traversal is supported.

        :return: ``true`` if an objective bank hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_objective_bank_hierarchy_design(self):
        """Tests if objective bank hierarchy design is supported.

        :return: ``true`` if an objective bank hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_learning_batch(self):
        """Tests if a learning batch service is supported.

        :return: ``true`` if a learning batch service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_objective_record_types(self):
        """Gets the supported ``Objective`` record types.

        :return: a list containing the supported ``Objective`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    objective_record_types = property(fget=get_objective_record_types)

    def supports_objective_record_type(self, objective_record_type):
        """Tests if the given ``Objective`` record type is supported.

        :param objective_record_type: a ``Type`` indicating an ``Objective`` record type
        :type objective_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_objective_search_record_types(self):
        """Gets the supported ``Objective`` search record types.

        :return: a list containing the supported ``Objective`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    objective_search_record_types = property(fget=get_objective_search_record_types)

    def supports_objective_search_record_type(self, objective_search_record_type):
        """Tests if the given ``Objective`` search record type is supported.

        :param objective_search_record_type: a ``Type`` indicating an ``Objective`` search record type
        :type objective_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_activity_record_types(self):
        """Gets the supported ``Activity`` record types.

        :return: a list containing the supported ``Activity`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    activity_record_types = property(fget=get_activity_record_types)

    def supports_activity_record_type(self, activity_record_type):
        """Tests if the given ``Activity`` record type is supported.

        :param activity_record_type: a ``Type`` indicating a ``Activity`` record type
        :type activity_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``activity_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_activity_search_record_types(self):
        """Gets the supported ``Activity`` search record types.

        :return: a list containing the supported ``Activity`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    activity_search_record_types = property(fget=get_activity_search_record_types)

    def supports_activity_search_record_type(self, activity_search_record_type):
        """Tests if the given ``Activity`` search record type is supported.

        :param activity_search_record_type: a ``Type`` indicating a ``Activity`` search record type
        :type activity_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``activity_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_proficiency_record_types(self):
        """Gets the supported ``Proficiency`` record types.

        :return: a list containing the supported ``Proficiency`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    proficiency_record_types = property(fget=get_proficiency_record_types)

    def supports_proficiency_record_type(self, proficiency_record_type):
        """Tests if the given ``Proficiency`` record type is supported.

        :param proficiency_record_type: a ``Type`` indicating a ``Proficiency`` record type
        :type proficiency_record_type: ``osid.type.Type``
        :return: ``true`` if the given record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``proficiency_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_proficiency_search_record_types(self):
        """Gets the supported ``Proficiency`` search types.

        :return: a list containing the supported ``Proficiency`` search types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    proficiency_search_record_types = property(fget=get_proficiency_search_record_types)

    def supports_proficiency_search_record_type(self, proficiency_search_record_type):
        """Tests if the given ``Proficiency`` search type is supported.

        :param proficiency_search_record_type: a ``Type`` indicating a ``Proficiency`` search type
        :type proficiency_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``proficiency_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_objective_bank_record_types(self):
        """Gets the supported ``ObjectiveBank`` record types.

        :return: a list containing the supported ``ObjectiveBank`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    objective_bank_record_types = property(fget=get_objective_bank_record_types)

    def supports_objective_bank_record_type(self, objective_bank_record_type):
        """Tests if the given ``ObjectiveBank`` record type is supported.

        :param objective_bank_record_type: a ``Type`` indicating an ``ObjectiveBank`` type
        :type objective_bank_record_type: ``osid.type.Type``
        :return: ``true`` if the given objective bank record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_objective_bank_search_record_types(self):
        """Gets the supported objective bank search record types.

        :return: a list containing the supported ``ObjectiveBank`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    objective_bank_search_record_types = property(fget=get_objective_bank_search_record_types)

    def supports_objective_bank_search_record_type(self, objective_bank_search_record_type):
        """Tests if the given objective bank search record type is supported.

        :param objective_bank_search_record_type: a ``Type`` indicating an ``ObjectiveBank`` search record type
        :type objective_bank_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean
##
# The following methods are from osid.learning.ObjectiveObjectiveBankSession

    def can_lookup_objective_objective_bank_mappings(self):
        """Tests if this user can perform lookups of objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_objective_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_objective_bank_view(self):
        """A complete view of the ``Objective`` and ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_objective_ids_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Objective``  ``Ids`` associated with an ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related objectives
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_objectives_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Objectives`` associated with an ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related objective ``Ids``
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList

    def get_objective_ids_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Objective Ids`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objective bank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of objective ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_objectives_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Objectives`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objective bank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of objectives
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList

    def get_objective_bank_ids_by_objective(self, objective_id):
        """Gets the list of ``ObjectiveBank``  ``Ids`` mapped to an ``Objective``.

        :param objective_id: ``Id`` of an ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: list of objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_objective_banks_by_objective(self, objective_id):
        """Gets the list of ``ObjectiveBanks`` mapped to an ``Objective``.

        :param objective_id: ``Id`` of an ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: list of objective banks
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList


##
# The following methods are from osid.learning.ObjectiveObjectiveBankAssignmentSession

    def can_assign_objectives(self):
        """Tests if this user can alter objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_assign_objectives_to_objective_bank(self, objective_bank_id):
        """Tests if this user can alter objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_assignable_objective_bank_ids(self, objective_bank_id):
        """Gets a list of objective banks including and under the given objective bank node in which any objective can
        be assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of assignable objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_assignable_objective_bank_ids_for_objective(self, objective_bank_id, objective_id):
        """Gets a list of objective banks including and under the given objective bank node in which a specific
        objective can be assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: list of assignable objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def assign_objective_to_objective_bank(self, objective_id, objective_bank_id):
        """Adds an existing ``Objective`` to an ``ObjectiveBank``.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_id`` already mapped to ``objective_bank_id``
        :raise: ``NotFound`` -- ``objective_id`` or ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def unassign_objective_from_objective_bank(self, objective_id, objective_bank_id):
        """Removes an ``Objective`` from an ``ObjectiveBank``.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id`` or ``objective_bank_id`` not found or ``objective_id`` not mapped to
        ``objective_bank_id``
        :raise: ``NullArgument`` -- ``objective_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def reassign_proficiency_to_objective_bank(self, objective_id, from_objective_bank_id, to_objective_bank_id):
        """Moves an ``Objective`` from one ``ObjectiveBank`` to another.

        Mappings to other ``ObjectiveBanks`` are unaffected.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param from_objective_bank_id: the ``Id`` of the current ``ObjectiveBank``
        :type from_objective_bank_id: ``osid.id.Id``
        :param to_objective_bank_id: the ``Id`` of the destination ``ObjectiveBank``
        :type to_objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id, from_objective_bank_id,`` or ``to_objective_bank_id`` not found or
        ``objective_id`` not mapped to ``from_objective_bank_id``
        :raise: ``NullArgument`` -- ``objective_id, from_objective_bank_id,`` or ``to_objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.learning.ActivityObjectiveBankSession

    def can_lookup_activity_objective_bank_mappings(self):
        """Tests if this user can perform lookups of activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_objective_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_objective_bank_view(self):
        """A complete view of the ``Activity`` and ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_activity_ids_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Activity``  ``Ids`` associated with an ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related activity ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_activities_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Activities`` associated with an ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related activities
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ActivityList

    def get_activity_ids_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Activity Ids`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objective bank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of activity ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_activities_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Activities`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objective bank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of activities
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ActivityList

    def get_objective_bank_ids_by_activity(self, activity_id):
        """Gets the list of ``ObjectiveBank Ids`` mapped to a ``Activity``.

        :param activity_id: ``Id`` of a ``Activity``
        :type activity_id: ``osid.id.Id``
        :return: list of objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``activity_id`` is not found
        :raise: ``NullArgument`` -- ``activity_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_objective_banks_by_activity(self, activity_id):
        """Gets the list of ``ObjectiveBanks`` mapped to a ``Activity``.

        :param activity_id: ``Id`` of a ``Activity``
        :type activity_id: ``osid.id.Id``
        :return: list of objective bank ``Ids``
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- ``activity_id`` is not found
        :raise: ``NullArgument`` -- ``activity_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList


##
# The following methods are from osid.learning.ActivityObjectiveBankAssignmentSession

    def can_assign_activities(self):
        """Tests if this user can alter activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_assign_activities_to_objective_bank(self, objective_bank_id):
        """Tests if this user can alter activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_assignable_objective_bank_ids(self, objective_bank_id):
        """Gets a list of objective banks including and under the given objective bank node in which any activity can be
        assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of assignable objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_assignable_objective_bank_ids_for_activity(self, objective_bank_id, activity_id):
        """Gets a list of objective banks including and under the given objective bank node in which a specific activity
        can be assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :return: list of assignable objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``activity_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def assign_activity_to_objective_bank(self, activity_id, objective_bank_id):
        """Adds an existing ``Activity`` to a ``ObjectiveBank``.

        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``activity_id`` already mapped to ``objective_bank_id``
        :raise: ``NotFound`` -- ``activity_id`` or ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``activity_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def unassign_activity_from_objective_bank(self, activity_id, objective_bank_id):
        """Removes a ``Activity`` from a ``ObjectiveBank``.

        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``activity_id`` or ``objective_bank_id`` not found or ``activity_id`` not mapped to
        ``objective_bank_id``
        :raise: ``NullArgument`` -- ``activity_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def reassign_activity_to_objective_bank(self, activity_id, from_objective_bank_id, to_objective_bank_id):
        """Moves an ``Activity`` from one ``ObjectiveBank`` to another.

        Mappings to other ``ObjectiveBanks`` are unaffected.

        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :param from_objective_bank_id: the ``Id`` of the current ``ObjectiveBank``
        :type from_objective_bank_id: ``osid.id.Id``
        :param to_objective_bank_id: the ``Id`` of the destination ``ObjectiveBank``
        :type to_objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``activity_id, from_objective_bank_id,`` or ``to_objective_bank_id`` not found or
        ``activity_id`` not mapped to ``from_objective_bank_id``
        :raise: ``NullArgument`` -- ``activity_id, from_objective_bank_id,`` or ``to_objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.learning.ObjectiveBankLookupSession

    def can_lookup_objective_banks(self):
        """Tests if this user can perform ``ObjectiveBank`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_objective_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_objective_bank_view(self):
        """A complete view of the ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_objective_bank(self, objective_bank_id):
        """Gets the ``ObjectiveBank`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``ObjectiveBank`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``ObjectiveBank`` and
        retained for compatility.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: the objective bank
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.learning.ObjectiveBank

    def get_objective_banks_by_ids(self, objective_bank_ids):
        """Gets a ``ObjectiveBankList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the objective
        banks specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``ObjectiveBank`` objects may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :param objective_bank_ids: the list of ``Ids`` to retrieve
        :type objective_bank_ids: ``osid.id.IdList``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def get_objective_banks_by_genus_type(self, objective_bank_genus_type):
        """Gets a ``ObjectiveBankList`` corresponding to the given objective bank genus ``Type`` which does not include
        objective banks of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :param objective_bank_genus_type: an objective bank genus type
        :type objective_bank_genus_type: ``osid.type.Type``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NullArgument`` -- ``objective_bank_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def get_objective_banks_by_parent_genus_type(self, objective_bank_genus_type):
        """Gets a ``ObjectiveBankList`` corresponding to the given objective bank genus ``Type`` and include any
        additional objective banks with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :param objective_bank_genus_type: an objective bank genus type
        :type objective_bank_genus_type: ``osid.type.Type``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NullArgument`` -- ``objective_bank_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def get_objective_banks_by_record_type(self, objective_bank_record_type):
        """Gets a ``ObjectiveBankList`` containing the given objective bank record ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :param objective_bank_record_type: an objective bank record type
        :type objective_bank_record_type: ``osid.type.Type``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NullArgument`` -- ``objective_bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def get_objective_banks_by_provider(self, resource_id):
        """Gets a ``ObjectiveBankList`` for the given provider.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def get_objective_banks(self):
        """Gets all ``ObjectiveBanks``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :return: a ``ObjectiveBankList``
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    objective_banks = property(fget=get_objective_banks)


##
# The following methods are from osid.learning.ObjectiveBankAdminSession

    def can_create_objective_banks(self):
        """Tests if this user can create ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``ObjectiveBank`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_create_objective_bank_with_record_types(self, objective_bank_record_types):
        """Tests if this user can create a single ``ObjectiveBank`` using the desired record types.

        While ``LearningManager.getObjectiveBankRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``ObjectiveBank``. Providing an empty array tests if an
        ``ObjectiveBank`` can be created with no records.

        :param objective_bank_record_types: array of objective bank record types
        :type objective_bank_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``ObjectiveBank`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_objective_bank_form_for_create(self, objective_bank_record_types):
        """Gets the objective bank form for creating new objective banks.

        A new form should be requested for each create transaction.

        :param objective_bank_record_types: array of objective bank record types
        :type objective_bank_record_types: ``osid.type.Type[]``
        :return: the objective bank form
        :rtype: ``osid.learning.ObjectiveBankForm``
        :raise: ``NullArgument`` -- ``objective_bank_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types.

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankForm

    def create_objective_bank(self, objective_bank_form):
        """Creates a new ``ObjectiveBank``.

        :param objective_bank_form: the form for this ``ObjectiveBank``
        :type objective_bank_form: ``osid.learning.ObjectiveBankForm``
        :return: the new ``ObjectiveBank``
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``IllegalState`` -- ``objective_bank_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``objective_bank_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``objective_bank_form`` did not originate from
        ``get_objective_bank_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBank

    def can_update_objective_banks(self):
        """Tests if this user can update ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``ObjectiveBank`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_objective_bank_form_for_update(self, objective_bank_id):
        """Gets the objective bank form for updating an existing objective bank.

        A new objective bank form should be requested for each update
        transaction.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: the objective bank form
        :rtype: ``osid.learning.ObjectiveBankForm``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankForm

    def update_objective_bank(self, objective_bank_form):
        """Updates an existing objective bank.

        :param objective_bank_form: the form containing the elements to be updated
        :type objective_bank_form: ``osid.learning.ObjectiveBankForm``
        :raise: ``IllegalState`` -- ``objective_bank_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``objective_bank_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``objective_bank_form did not originate from get_objective_bank_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_objective_banks(self):
        """Tests if this user can delete objective banks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``ObjectiveBank`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_objective_bank(self, objective_bank_id):
        """Deletes an ``ObjectiveBank``.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank`` to remove
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_objective_bank_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``ObjectiveBank`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def alias_objective_bank(self, objective_bank_id, alias_id):
        """Adds an ``Id`` to an ``ObjectiveBank`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``ObjectiveBank`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another objective bank, it
        is reassigned to the given objective bank ``Id``.

        :param objective_bank_id: the ``Id`` of an ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.learning.ObjectiveBankHierarchySession

    def get_objective_bank_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    objective_bank_hierarchy_id = property(fget=get_objective_bank_hierarchy_id)

    def get_objective_bank_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    objective_bank_hierarchy = property(fget=get_objective_bank_hierarchy)

    def can_access_objective_bank_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer traversal
        functions to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_objective_bank_view(self):
        """The returns from the objective bank methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_objective_bank_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_root_objective_bank_ids(self):
        """Gets the root objective bank ``Ids`` in this hierarchy.

        :return: the root objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    root_objective_bank_ids = property(fget=get_root_objective_bank_ids)

    def get_root_objective_banks(self):
        """Gets the root objective banks in this objective bank hierarchy.

        :return: the root objective banks
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    root_objective_banks = property(fget=get_root_objective_banks)

    def has_parent_objective_banks(self, objective_bank_id):
        """Tests if the ``ObjectiveBank`` has any parents.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if the objective bank has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def is_parent_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an ``Id`` is a direct parent of an objective bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``objective_bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

    def get_parent_objective_bank_ids(self, objective_bank_id):
        """Gets the parent ``Ids`` of the given objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the objective bank
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_parent_objective_banks(self, objective_bank_id):
        """Gets the parents of the given objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: the parents of the objective bank
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def is_ancestor_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an ``Id`` is an ancestor of an objective bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``objective_bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

    def has_child_objective_banks(self, objective_bank_id):
        """Tests if an objective bank has any children.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if the ``objective_bank_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def is_child_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an objective bank is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``objective_bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

    def get_child_objective_bank_ids(self, objective_bank_id):
        """Gets the child ``Ids`` of the given objective bank.

        :param objective_bank_id: the ``Id`` to query
        :type objective_bank_id: ``osid.id.Id``
        :return: the children of the objective bank
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_child_objective_banks(self, objective_bank_id):
        """Gets the children of the given objective bank.

        :param objective_bank_id: the ``Id`` to query
        :type objective_bank_id: ``osid.id.Id``
        :return: the children of the objective bank
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def is_descendant_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an ``Id`` is a descendant of an objective bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``objective_bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return # boolean

    def get_objective_bank_node_ids(self, objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given objective bank.

        :param objective_bank_id: the ``Id`` to query
        :type objective_bank_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
        node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
        in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a catalog node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Node

    def get_objective_bank_nodes(self, objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given objective bank.

        :param objective_bank_id: the ``Id`` to query
        :type objective_bank_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
        node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
        in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an objective bank node
        :rtype: ``osid.learning.ObjectiveBankNode``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankNode


##
# The following methods are from osid.learning.ObjectiveBankHierarchyDesignSession

    def get_objective_bank_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    objective_bank_hierarchy_id = property(fget=get_objective_bank_hierarchy_id)

    def get_objective_bank_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    objective_bank_hierarchy = property(fget=get_objective_bank_hierarchy)

    def can_modify_objective_bank_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def add_root_objective_bank(self, objective_bank_id):
        """Adds a root objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_bank_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_root_objective_bank(self, objective_bank_id):
        """Removes a root objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not a root
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def add_child_objective_bank(self, objective_bank_id, child_id):
        """Adds a child to an objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_bank_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``objective_bank_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_objective_bank(self, objective_bank_id, child_id):
        """Removes a child from an objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_bank_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_objective_banks(self, objective_bank_id):
        """Removes all children from an objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_bank_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




class LearningManager(osid_managers.OsidManager, osid_sessions.OsidSession, LearningProfile):
    """The learning manager provides access to learning sessions and provides interoperability tests for various aspects
        of
        this service.

    The sessions included in this manager are:

      * ``ObjectiveLookupSession:`` a session to look up objectives
      * ``ObjectiveLookupSession:`` a session to query objectives
        ``None``
      * ``ObjectiveSearchSession:`` a session to search objectives
      * ``ObjectiveAdminSession:`` a session to create, modify and
        delete objectives ``None``
      * ``ObjectiveNotificationSession: a`` session to receive messages
        pertaining to objective ```` changes
      * ``ObjectiveHierarchySession:`` a session to traverse objective
        hierarchies
      * ``ObjectiveHierarchyDesignSession:`` a session to design
        objective hierarchies
      * ``ObjectiveSequencingSession:`` a session to sequence objectives
      * ``ObjectiveObjectiveBankSession:`` a session for retriieving
        objective and objective bank mappings
      * ``ObjectiveObjectiveBankAssignmentSession:`` a session for
        managing objective and objective bank mappings
      * ``ObjectiveSmartObjectiveBankSession:`` a session for managing
        dynamic objective banks
      * ``ObjectiveRequisiteSession:`` a session to examine objective
        requisites
      * ``ObjectiveRequisiteAssignmentSession:`` a session to manage
        objective requisites

      * ``ActivityLookupSession:`` a session to look up activities
      * ``ActivityQuerySession:`` a session to query activities ``None``
      * ``ActivitySearchSession:`` a session to search activities
      * ``ActivityAdminSession:`` a session to create, modify and delete
        activities ``None``
      * ``ActivityNotificationSession: a`` session to receive messages
        pertaining to activity ```` changes
      * ``ActivityObjectiveBankSession:`` a session for retriieving
        activity and objective bank mappings
      * ``ActivityObjectiveBankAssignmentSession:`` a session for
        managing activity and objective bank mappings
      * ``ActivitySmartObjectiveBankSession:`` a session for managing
        dynamic objective banks of activities

      * ``ProficiencyLookupSession:`` a session to retrieve
        proficiencies
      * ``ProficiencyQuerySession:`` a session to query proficiencies
      * ``ProficiencySearchSession:`` a session to search for
        proficiencies
      * ``ProficiencyAdminSession:`` a session to create, update, and
        delete proficiencies
      * ``ProficiencyNotificationSession:`` a session to receive
        notifications pertaining to proficiency changes
      * ``ProficiencyObjectiveBankSession:`` a session to look up
        proficiency to objective bank mappings
      * ``ProficiencyObjectiveBankAssignmentSession:`` a session to
        manage proficiency to objective bank mappings
      * ``ProficiencySmartObjectiveBankSession:`` a session to manage
        smart objective banks of proficiencies
      * ``MyLearningPathSession:`` a session to examine learning paths
        of objectives
      * ``LearningPathSession:`` a session to examine learning paths of
        objectives

      * ``ObjectiveBankLookupSession:`` a session to lookup objective
        banks
      * ``ObjectiveBankQuerySession:`` a session to query objective
        banks
      * ``ObjectiveBankSearchSession`` : a session to search objective
        banks
      * ``ObjectiveBankAdminSession`` : a session to create, modify and
        delete objective banks
      * ``ObjectiveBankNotificationSession`` : a session to receive
        messages pertaining to objective bank changes
      * ``ObjectiveBankHierarchySession:`` a session to traverse the
        objective bank hierarchy
      * ``ObjectiveBankHierarchyDesignSession:`` a session to manage the
        objective bank hierarchy

    """

    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._objective_bank_view = DEFAULT
        osid.OsidSession.__init__(self, proxy) # This is to initialize self._proxy

    # def _get_view(self, view):
    #     """Gets the currently set view"""
    #     if view in self._views:
    #         return self._views[view]
    #     else:
    #         self._views[view] = DEFAULT
    #         return DEFAULT

    def _set_objective_bank_view(self, session):
        """Sets the underlying objective_bank view to match current view"""
        if self._objective_bank_view == COMPARATIVE:
            try:
                session.use_comparative_objective_bank_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_objective_bank_view()
            except AttributeError:
                pass

    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        if self._proxy is None:
            self._proxy = proxy
        if session_name in self._provider_sessions:
            return self._provider_sessions[session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_objective_bank_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[session_name] = session
            return session

    def _instantiate_session(self, method_name, proxy=None, *args, **kwargs):
        """Instantiates a provider session"""
        session_class = getattr(self._provider_manager, method_name)
        if proxy is None:
            return session_class(*args, **kwargs)
        else:
            return session_class(proxy=proxy, *args, **kwargs)

    def initialize(self, runtime):
        """OSID Manager initialize"""
        from .primitives import Id
        if self._runtime is not None:
            raise IllegalState('Manager has already been initialized')
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:learningProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('LEARNING', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('LEARNING', provider_impl)

    def close_sessions(self):
        """Close all sessions, unless session management is set to MANDATORY"""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()

    def use_automatic_session_management(self):
        """Session state will be saved unless closed by consumers"""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will be saved and can not be closed by consumers"""
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved"""
        self._session_management = DISABLED
        self.close_sessions()

    def get_objective_lookup_session(self):
        """Gets the ``OsidSession`` associated with the objective lookup service.

        :return: an ``ObjectiveLookupSession``
        :rtype: ``osid.learning.ObjectiveLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_lookup()`` is ``true``.*

        """
        return # osid.learning.ObjectiveLookupSession

    objective_lookup_session = property(fget=get_objective_lookup_session)

    def get_objective_lookup_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective lookup service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``an _objective_lookup_session``
        :rtype: ``osid.learning.ObjectiveLookupSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveLookupSession

    def get_objective_query_session(self):
        """Gets the ``OsidSession`` associated with the objective query service.

        :return: an ``ObjectiveQuerySession``
        :rtype: ``osid.learning.ObjectiveQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_query()`` is ``true``.*

        """
        return # osid.learning.ObjectiveQuerySession

    objective_query_session = property(fget=get_objective_query_session)

    def get_objective_query_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective query service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``an _objective_query_session``
        :rtype: ``osid.learning.ObjectiveQuerySession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveQuerySession

    def get_objective_search_session(self):
        """Gets the ``OsidSession`` associated with the objective search service.

        :return: an ``ObjectiveSearchSession``
        :rtype: ``osid.learning.ObjectiveSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_search()`` is ``true``.*

        """
        return # osid.learning.ObjectiveSearchSession

    objective_search_session = property(fget=get_objective_search_session)

    def get_objective_search_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective search service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``an _objective_search_session``
        :rtype: ``osid.learning.ObjectiveSearchSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveSearchSession

    def get_objective_admin_session(self):
        """Gets the ``OsidSession`` associated with the objective administration service.

        :return: an ``ObjectiveAdminSession``
        :rtype: ``osid.learning.ObjectiveAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_admin()`` is ``true``.*

        """
        return # osid.learning.ObjectiveAdminSession

    objective_admin_session = property(fget=get_objective_admin_session)

    def get_objective_admin_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective admin service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``an _objective_admin_session``
        :rtype: ``osid.learning.ObjectiveAdminSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveAdminSession

    def get_objective_notification_session(self, objective_receiver):
        """Gets the notification session for notifications pertaining to objective changes.

        :param objective_receiver: the objective receiver
        :type objective_receiver: ``osid.learning.ObjectiveReceiver``
        :return: an ``ObjectiveNotificationSession``
        :rtype: ``osid.learning.ObjectiveNotificationSession``
        :raise: ``NullArgument`` -- ``objective_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_notification()`` is ``true``.*

        """
        return # osid.learning.ObjectiveNotificationSession

    def get_objective_notification_session_for_objective_bank(self, objective_receiver, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective notification service for the given objective bank.

        :param objective_receiver: the objective receiver
        :type objective_receiver: ``osid.learning.ObjectiveReceiver``
        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``an _objective_notification_session``
        :rtype: ``osid.learning.ObjectiveNotificationSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_receiver`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveNotificationSession

    def get_objective_hierarchy_session(self):
        """Gets the session for traversing objective hierarchies.

        :return: an ``ObjectiveHierarchySession``
        :rtype: ``osid.learning.ObjectiveHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_hierarchy()`` is ``true``.*

        """
        return # osid.learning.ObjectiveHierarchySession

    objective_hierarchy_session = property(fget=get_objective_hierarchy_session)

    def get_objective_hierarchy_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective hierarchy traversal service for the given objective
        bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ObjectiveHierarchySession``
        :rtype: ``osid.learning.ObjectiveHierarchySession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_hierarchy()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_hierarchy()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveHierarchySession

    def get_objective_hierarchy_design_session(self):
        """Gets the session for designing objective hierarchies.

        :return: an ``ObjectiveHierarchyDesignSession``
        :rtype: ``osid.learning.ObjectiveHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_hierarchy_design()`` is ``true``.*

        """
        return # osid.learning.ObjectiveHierarchyDesignSession

    objective_hierarchy_design_session = property(fget=get_objective_hierarchy_design_session)

    def get_objective_hierarchy_design_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective hierarchy design service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ObjectiveHierarchyDesignSession``
        :rtype: ``osid.learning.ObjectiveHierarchyDesignSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_hierarchy_design()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_hierarchy_design()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveHierarchyDesignSession

    def get_objective_sequencing_session(self):
        """Gets the session for sequencing objectives.

        :return: an ``ObjectiveSequencingSession``
        :rtype: ``osid.learning.ObjectiveSequencingSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_sequencing()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_sequencing()`` is ``true``.*

        """
        return # osid.learning.ObjectiveSequencingSession

    objective_sequencing_session = property(fget=get_objective_sequencing_session)

    def get_objective_sequencing_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ObjectiveSequencingSession``
        :rtype: ``osid.learning.ObjectiveSequencingSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_sequencing()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_sequencing()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveSequencingSession

    def get_objective_objective_bank_session(self):
        """Gets the session for retrieving objective to objective bank mappings.

        :return: an ``ObjectiveObjectiveBankSession``
        :rtype: ``osid.learning.ObjectiveObjectiveBankSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_objective_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_objective_bank()`` is ``true``.*

        """
        return # osid.learning.ObjectiveObjectiveBankSession

    objective_objective_bank_session = property(fget=get_objective_objective_bank_session)

    def get_objective_objective_bank_assignment_session(self):
        """Gets the session for assigning objective to objective bank mappings.

        :return: an ``ObjectiveObjectiveBankAssignmentSession``
        :rtype: ``osid.learning.ObjectiveObjectiveBankAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_objective_bank_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_objective_bank_assignment()`` is ``true``.*

        """
        return # osid.learning.ObjectiveObjectiveBankAssignmentSession

    objective_objective_bank_assignment_session = property(fget=get_objective_objective_bank_assignment_session)

    def get_objective_smart_objective_bank_session(self, objective_bank_id):
        """Gets the ``OsidSession`` to manage dynamic objective banks of objectives.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ObjectiveSmartObjectiveBankSession``
        :rtype: ``osid.learning.ObjectiveSmartObjectiveBankSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_smart_objective_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_smart_objective_bank()`` is ``true``.*

        """
        return # osid.learning.ObjectiveSmartObjectiveBankSession

    def get_objective_requisite_session(self):
        """Gets the session for examining objective requisites.

        :return: an ``ObjectiveRequisiteSession``
        :rtype: ``osid.learning.ObjectiveRequisiteSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_requisite()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_requisite()`` is ``true``.*

        """
        return # osid.learning.ObjectiveRequisiteSession

    objective_requisite_session = property(fget=get_objective_requisite_session)

    def get_objective_requisite_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ObjectiveRequisiteSession``
        :rtype: ``osid.learning.ObjectiveRequisiteSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_requisite()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_requisite()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveRequisiteSession

    def get_objective_requisite_assignment_session(self):
        """Gets the session for managing objective requisites.

        :return: an ``ObjectiveRequisiteAssignmentSession``
        :rtype: ``osid.learning.ObjectiveRequisiteAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_requisite_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_requisite_assignment()`` is ``true``.*

        """
        return # osid.learning.ObjectiveRequisiteAssignmentSession

    objective_requisite_assignment_session = property(fget=get_objective_requisite_assignment_session)

    def get_objective_requisite_assignment_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ObjectiveRequisiteAssignmentSession``
        :rtype: ``osid.learning.ObjectiveRequisiteAssignmentSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_requisite_assignment()`` or ``supports_visible_federation()``
        is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_requisite_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveRequisiteAssignmentSession

    def get_activity_lookup_session(self):
        """Gets the ``OsidSession`` associated with the activity lookup service.

        :return: an ``ActivityLookupSession``
        :rtype: ``osid.learning.ActivityLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_lookup()`` is ``true``.*

        """
        return # osid.learning.ActivityLookupSession

    activity_lookup_session = property(fget=get_activity_lookup_session)

    def get_activity_lookup_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the activity lookup service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ActivityLookupSession``
        :rtype: ``osid.learning.ActivityLookupSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ActivityLookupSession

    def get_activity_query_session(self):
        """Gets the ``OsidSession`` associated with the activity query service.

        :return: a ``ActivityQuerySession``
        :rtype: ``osid.learning.ActivityQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_query()`` is ``true``.*

        """
        return # osid.learning.ActivityQuerySession

    activity_query_session = property(fget=get_activity_query_session)

    def get_activity_query_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the activity query service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ActivityQuerySession``
        :rtype: ``osid.learning.ActivityQuerySession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ActivityQuerySession

    def get_activity_search_session(self):
        """Gets the ``OsidSession`` associated with the activity search service.

        :return: a ``ActivitySearchSession``
        :rtype: ``osid.learning.ActivitySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_search()`` is ``true``.*

        """
        return # osid.learning.ActivitySearchSession

    activity_search_session = property(fget=get_activity_search_session)

    def get_activity_search_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the activity search service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ActivitySearchSession``
        :rtype: ``osid.learning.ActivitySearchSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ActivitySearchSession

    def get_activity_admin_session(self):
        """Gets the ``OsidSession`` associated with the activity administration service.

        :return: a ``ActivityAdminSession``
        :rtype: ``osid.learning.ActivityAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_admin()`` is ``true``.*

        """
        return # osid.learning.ActivityAdminSession

    activity_admin_session = property(fget=get_activity_admin_session)

    def get_activity_admin_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the activity admin service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ActivityAdminSession``
        :rtype: ``osid.learning.ActivityAdminSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ActivityAdminSession

    def get_activity_notification_session(self, activity_receiver):
        """Gets the notification session for notifications pertaining to activity changes.

        :param activity_receiver: the activity receiver
        :type activity_receiver: ``osid.learning.ActivityReceiver``
        :return: an ``ActivityNotificationSession``
        :rtype: ``osid.learning.ActivityNotificationSession``
        :raise: ``NullArgument`` -- ``activity_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_notification()`` is ``true``.*

        """
        return # osid.learning.ActivityNotificationSession

    def get_activity_notification_session_for_objective_bank(self, activity_receiver, objective_bank_id):
        """Gets the ``OsidSession`` associated with the activity notification service for the given objective bank.

        :param activity_receiver: the activity receiver
        :type activity_receiver: ``osid.learning.ActivityReceiver``
        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``an _activity_notification_session``
        :rtype: ``osid.learning.ActivityNotificationSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``activity_receiver`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ActivityNotificationSession

    def get_activity_objective_bank_session(self):
        """Gets the session for retrieving activity to objective bank mappings.

        :return: an ``ActivityObjectiveBankSession``
        :rtype: ``osid.learning.ActivityObjectiveBankSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_objective_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_objective_bank()`` is ``true``.*

        """
        return # osid.learning.ActivityObjectiveBankSession

    activity_objective_bank_session = property(fget=get_activity_objective_bank_session)

    def get_activity_objective_bank_assignment_session(self):
        """Gets the session for assigning activity to objective bank mappings.

        :return: an ``ActivityObjectiveBankAssignmentSession``
        :rtype: ``osid.learning.ActivityObjectiveBankAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_objective_bank_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_objective_bank_assignment()`` is ``true``.*

        """
        return # osid.learning.ActivityObjectiveBankAssignmentSession

    activity_objective_bank_assignment_session = property(fget=get_activity_objective_bank_assignment_session)

    def get_activity_smart_objective_bank_session(self, objective_bank_id):
        """Gets the ``OsidSession`` to manage dynamic objective banks of activities.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ActivitySmartObjectiveBankSession``
        :rtype: ``osid.learning.ActivitySmartObjectiveBankSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_smart_objective_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_smart_objective_bank()`` is ``true``.*

        """
        return # osid.learning.ActivitySmartObjectiveBankSession

    def get_proficiency_lookup_session(self):
        """Gets the ``OsidSession`` associated with the proficiency lookup service.

        :return: a ``ProficiencyLookupSession``
        :rtype: ``osid.learning.ProficiencyLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_lookup()`` is ``true``.*

        """
        return # osid.learning.ProficiencyLookupSession

    proficiency_lookup_session = property(fget=get_proficiency_lookup_session)

    def get_proficiency_lookup_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the proficiency lookup service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the obective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: a ``ProficiencyLookupSession``
        :rtype: ``osid.learning.ProficiencyLookupSession``
        :raise: ``NotFound`` -- no ``ObjectiveBank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.learning.ProficiencyLookupSession

    def get_proficiency_query_session(self):
        """Gets the ``OsidSession`` associated with the proficiency query service.

        :return: a ``ProficiencyQuerySession``
        :rtype: ``osid.learning.ProficiencyQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_query()`` is ``true``.*

        """
        return # osid.learning.ProficiencyQuerySession

    proficiency_query_session = property(fget=get_proficiency_query_session)

    def get_proficiency_query_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the proficiency query service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the obective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: a ``ProficiencyQuerySession``
        :rtype: ``osid.learning.ProficiencyQuerySession``
        :raise: ``NotFound`` -- no ``ObjectiveBank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.learning.ProficiencyQuerySession

    def get_proficiency_search_session(self):
        """Gets the ``OsidSession`` associated with the proficiency search service.

        :return: a ``ProficiencySearchSession``
        :rtype: ``osid.learning.ProficiencySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_search()`` is ``true``.*

        """
        return # osid.learning.ProficiencySearchSession

    proficiency_search_session = property(fget=get_proficiency_search_session)

    def get_proficiency_search_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the proficiency search service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: a ``ProficiencySearchSession``
        :rtype: ``osid.learning.ProficiencySearchSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.learning.ProficiencySearchSession

    def get_proficiency_admin_session(self):
        """Gets the ``OsidSession`` associated with the proficiency administration service.

        :return: a ``ProficiencyAdminSession``
        :rtype: ``osid.learning.ProficiencyAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_admin()`` is ``true``.*

        """
        return # osid.learning.ProficiencyAdminSession

    proficiency_admin_session = property(fget=get_proficiency_admin_session)

    def get_proficiency_admin_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the proficiency administration service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: a ``ProficiencyAdminSession``
        :rtype: ``osid.learning.ProficiencyAdminSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.learning.ProficiencyAdminSession

    def get_proficiency_notification_session(self, proficiency_receiver):
        """Gets the ``OsidSession`` associated with the proficiency notification service.

        :param proficiency_receiver: the notification callback
        :type proficiency_receiver: ``osid.learning.ProficiencyReceiver``
        :return: a ``ProficiencyNotificationSession``
        :rtype: ``osid.learning.ProficiencyNotificationSession``
        :raise: ``NullArgument`` -- ``proficiency_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_notification()`` is ``true``.*

        """
        return # osid.learning.ProficiencyNotificationSession

    def get_proficiency_notification_session_for_objective_bank(self, proficiency_receiver, objective_bank_id):
        """Gets the ``OsidSession`` associated with the proficiency notification service for the given objective bank.

        :param proficiency_receiver: the notification callback
        :type proficiency_receiver: ``osid.learning.ProficiencyReceiver``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: a ``ProficiencyNotificationSession``
        :rtype: ``osid.learning.ProficiencyNotificationSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``proficiency_receiver`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.learning.ProficiencyNotificationSession

    def get_proficiency_objective_bank_session(self):
        """Gets the ``OsidSession`` to lookup proficiency/objective bank mappings.

        :return: a ``ProficiencyObjectiveBankSession``
        :rtype: ``osid.learning.ProficiencyObjectiveBankSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_objective_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_objective_bank()`` is ``true``.*

        """
        return # osid.learning.ProficiencyObjectiveBankSession

    proficiency_objective_bank_session = property(fget=get_proficiency_objective_bank_session)

    def get_proficiency_objective_bank_assignment_session(self):
        """Gets the ``OsidSession`` associated with assigning proficiencys to objective banks.

        :return: a ``ProficiencyObjectiveBankAssignmentSession``
        :rtype: ``osid.learning.ProficiencyObjectiveBankAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_objective_bank_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_objective_bank_assignment()`` is
        ``true``.*

        """
        return # osid.learning.ProficiencyObjectiveBankAssignmentSession

    proficiency_objective_bank_assignment_session = property(fget=get_proficiency_objective_bank_assignment_session)

    def get_proficiency_smart_objective_bank_session(self, objective_bank_id):
        """Gets the ``OsidSession`` to manage dynamic objective banks of objectives.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: a ``ProficiencySmartObjectiveBankSession``
        :rtype: ``osid.learning.ProficiencySmartObjectiveBankSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_smart_objective_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_smart_objective_bank()`` is ``true``.*

        """
        return # osid.learning.ProficiencySmartObjectiveBankSession

    def get_my_learning_path_session(self):
        """Gets the ``OsidSession`` associated with the my learning path service.

        :return: a ``MyLearningPathSession``
        :rtype: ``osid.learning.MyLearningPathSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_learning_path()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_my_learning_path()`` is ``true``.*

        """
        return # osid.learning.MyLearningPathSession

    my_learning_path_session = property(fget=get_my_learning_path_session)

    def get_my_learning_path_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the my learning path service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: a ``MyLearningPathSession``
        :rtype: ``osid.learning.MyLearningPathSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_learning_path()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_my_learning_path()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.learning.MyLearningPathSession

    def get_learning_path_session(self):
        """Gets the ``OsidSession`` associated with the learning path service.

        :return: a ``LearningPathSession``
        :rtype: ``osid.learning.LearningPathSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_learning_path()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_learning_path()`` is ``true``.*

        """
        return # osid.learning.LearningPathSession

    learning_path_session = property(fget=get_learning_path_session)

    def get_learning_path_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the learning path service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: a ``LearningPathSession``
        :rtype: ``osid.learning.LearningPathSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supporty_learning_path()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_learning_path()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.learning.LearningPathSession

    def get_objective_bank_lookup_session(self):
        """Gets the OsidSession associated with the objective bank lookup service.

        :return: an ``ObjectiveBankLookupSession``
        :rtype: ``osid.learning.ObjectiveBankLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_lookup() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_lookup()`` is true.*

        """
        return # osid.learning.ObjectiveBankLookupSession

    objective_bank_lookup_session = property(fget=get_objective_bank_lookup_session)

    def get_objective_bank_query_session(self):
        """Gets the OsidSession associated with the objective bank query service.

        :return: an ``ObjectiveBankQuerySession``
        :rtype: ``osid.learning.ObjectiveBankQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_query() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_query()`` is true.*

        """
        return # osid.learning.ObjectiveBankQuerySession

    objective_bank_query_session = property(fget=get_objective_bank_query_session)

    def get_objective_bank_search_session(self):
        """Gets the OsidSession associated with the objective bank search service.

        :return: an ``ObjectiveBankSearchSession``
        :rtype: ``osid.learning.ObjectiveBankSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_search() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_search()`` is true.*

        """
        return # osid.learning.ObjectiveBankSearchSession

    objective_bank_search_session = property(fget=get_objective_bank_search_session)

    def get_objective_bank_admin_session(self):
        """Gets the OsidSession associated with the objective bank administration service.

        :return: an ``ObjectiveBankAdminSession``
        :rtype: ``osid.learning.ObjectiveBankAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_admin() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_admin()`` is true.*

        """
        return # osid.learning.ObjectiveBankAdminSession

    objective_bank_admin_session = property(fget=get_objective_bank_admin_session)

    def get_objective_bank_notification_session(self, objective_bank_receiver):
        """Gets the notification session for notifications pertaining to objective bank service changes.

        :param objective_bank_receiver: the objective bank receiver
        :type objective_bank_receiver: ``osid.learning.ObjectiveBankReceiver``
        :return: an ``ObjectiveBankNotificationSession``
        :rtype: ``osid.learning.ObjectiveBankNotificationSession``
        :raise: ``NullArgument`` -- ``objective_bank_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_notification() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_notification()`` is true.*

        """
        return # osid.learning.ObjectiveBankNotificationSession

    def get_objective_bank_hierarchy_session(self):
        """Gets the session traversing objective bank hierarchies.

        :return: an ``ObjectiveBankHierarchySession``
        :rtype: ``osid.learning.ObjectiveBankHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_hierarchy() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_hierarchy()`` is true.*

        """
        return # osid.learning.ObjectiveBankHierarchySession

    objective_bank_hierarchy_session = property(fget=get_objective_bank_hierarchy_session)

    def get_objective_bank_hierarchy_design_session(self):
        """Gets the session designing objective bank hierarchies.

        :return: an ``ObjectiveBankHierarchyDesignSession``
        :rtype: ``osid.learning.ObjectiveBankHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_hierarchy_design() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_hierarchy_design()`` is true.*

        """
        return # osid.learning.ObjectiveBankHierarchyDesignSession

    objective_bank_hierarchy_design_session = property(fget=get_objective_bank_hierarchy_design_session)

    def get_learning_batch_manager(self):
        """Gets a ``LearningBatchManager``.

        :return: a ``LearningBatchManager``
        :rtype: ``osid.learning.batch.LearningBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_learning_batch() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_learning_batch()`` is true.*

        """
        return # osid.learning.batch.LearningBatchManager

    learning_batch_manager = property(fget=get_learning_batch_manager)
##
# The following methods are from osid.learning.ObjectiveObjectiveBankSession

    def can_lookup_objective_objective_bank_mappings(self):
        """Tests if this user can perform lookups of objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_objective_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_objective_bank_view(self):
        """A complete view of the ``Objective`` and ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_objective_ids_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Objective``  ``Ids`` associated with an ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related objectives
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_objectives_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Objectives`` associated with an ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related objective ``Ids``
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList

    def get_objective_ids_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Objective Ids`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objective bank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of objective ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_objectives_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Objectives`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objective bank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of objectives
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList

    def get_objective_bank_ids_by_objective(self, objective_id):
        """Gets the list of ``ObjectiveBank``  ``Ids`` mapped to an ``Objective``.

        :param objective_id: ``Id`` of an ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: list of objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_objective_banks_by_objective(self, objective_id):
        """Gets the list of ``ObjectiveBanks`` mapped to an ``Objective``.

        :param objective_id: ``Id`` of an ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: list of objective banks
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList


##
# The following methods are from osid.learning.ObjectiveObjectiveBankAssignmentSession

    def can_assign_objectives(self):
        """Tests if this user can alter objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_assign_objectives_to_objective_bank(self, objective_bank_id):
        """Tests if this user can alter objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_assignable_objective_bank_ids(self, objective_bank_id):
        """Gets a list of objective banks including and under the given objective bank node in which any objective can
        be assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of assignable objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_assignable_objective_bank_ids_for_objective(self, objective_bank_id, objective_id):
        """Gets a list of objective banks including and under the given objective bank node in which a specific
        objective can be assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: list of assignable objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def assign_objective_to_objective_bank(self, objective_id, objective_bank_id):
        """Adds an existing ``Objective`` to an ``ObjectiveBank``.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_id`` already mapped to ``objective_bank_id``
        :raise: ``NotFound`` -- ``objective_id`` or ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def unassign_objective_from_objective_bank(self, objective_id, objective_bank_id):
        """Removes an ``Objective`` from an ``ObjectiveBank``.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id`` or ``objective_bank_id`` not found or ``objective_id`` not mapped to
        ``objective_bank_id``
        :raise: ``NullArgument`` -- ``objective_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def reassign_proficiency_to_objective_bank(self, objective_id, from_objective_bank_id, to_objective_bank_id):
        """Moves an ``Objective`` from one ``ObjectiveBank`` to another.

        Mappings to other ``ObjectiveBanks`` are unaffected.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param from_objective_bank_id: the ``Id`` of the current ``ObjectiveBank``
        :type from_objective_bank_id: ``osid.id.Id``
        :param to_objective_bank_id: the ``Id`` of the destination ``ObjectiveBank``
        :type to_objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id, from_objective_bank_id,`` or ``to_objective_bank_id`` not found or
        ``objective_id`` not mapped to ``from_objective_bank_id``
        :raise: ``NullArgument`` -- ``objective_id, from_objective_bank_id,`` or ``to_objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.learning.ActivityObjectiveBankSession

    def can_lookup_activity_objective_bank_mappings(self):
        """Tests if this user can perform lookups of activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_objective_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_objective_bank_view(self):
        """A complete view of the ``Activity`` and ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_activity_ids_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Activity``  ``Ids`` associated with an ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related activity ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_activities_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Activities`` associated with an ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related activities
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ActivityList

    def get_activity_ids_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Activity Ids`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objective bank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of activity ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_activities_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Activities`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objective bank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of activities
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ActivityList

    def get_objective_bank_ids_by_activity(self, activity_id):
        """Gets the list of ``ObjectiveBank Ids`` mapped to a ``Activity``.

        :param activity_id: ``Id`` of a ``Activity``
        :type activity_id: ``osid.id.Id``
        :return: list of objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``activity_id`` is not found
        :raise: ``NullArgument`` -- ``activity_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_objective_banks_by_activity(self, activity_id):
        """Gets the list of ``ObjectiveBanks`` mapped to a ``Activity``.

        :param activity_id: ``Id`` of a ``Activity``
        :type activity_id: ``osid.id.Id``
        :return: list of objective bank ``Ids``
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- ``activity_id`` is not found
        :raise: ``NullArgument`` -- ``activity_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList


##
# The following methods are from osid.learning.ActivityObjectiveBankAssignmentSession

    def can_assign_activities(self):
        """Tests if this user can alter activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_assign_activities_to_objective_bank(self, objective_bank_id):
        """Tests if this user can alter activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_assignable_objective_bank_ids(self, objective_bank_id):
        """Gets a list of objective banks including and under the given objective bank node in which any activity can be
        assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of assignable objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_assignable_objective_bank_ids_for_activity(self, objective_bank_id, activity_id):
        """Gets a list of objective banks including and under the given objective bank node in which a specific activity
        can be assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :return: list of assignable objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``activity_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def assign_activity_to_objective_bank(self, activity_id, objective_bank_id):
        """Adds an existing ``Activity`` to a ``ObjectiveBank``.

        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``activity_id`` already mapped to ``objective_bank_id``
        :raise: ``NotFound`` -- ``activity_id`` or ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``activity_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def unassign_activity_from_objective_bank(self, activity_id, objective_bank_id):
        """Removes a ``Activity`` from a ``ObjectiveBank``.

        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``activity_id`` or ``objective_bank_id`` not found or ``activity_id`` not mapped to
        ``objective_bank_id``
        :raise: ``NullArgument`` -- ``activity_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def reassign_activity_to_objective_bank(self, activity_id, from_objective_bank_id, to_objective_bank_id):
        """Moves an ``Activity`` from one ``ObjectiveBank`` to another.

        Mappings to other ``ObjectiveBanks`` are unaffected.

        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :param from_objective_bank_id: the ``Id`` of the current ``ObjectiveBank``
        :type from_objective_bank_id: ``osid.id.Id``
        :param to_objective_bank_id: the ``Id`` of the destination ``ObjectiveBank``
        :type to_objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``activity_id, from_objective_bank_id,`` or ``to_objective_bank_id`` not found or
        ``activity_id`` not mapped to ``from_objective_bank_id``
        :raise: ``NullArgument`` -- ``activity_id, from_objective_bank_id,`` or ``to_objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.learning.ObjectiveBankLookupSession

    def can_lookup_objective_banks(self):
        """Tests if this user can perform ``ObjectiveBank`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_objective_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_objective_bank_view(self):
        """A complete view of the ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_objective_bank(self, objective_bank_id):
        """Gets the ``ObjectiveBank`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``ObjectiveBank`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``ObjectiveBank`` and
        retained for compatility.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: the objective bank
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.learning.ObjectiveBank

    def get_objective_banks_by_ids(self, objective_bank_ids):
        """Gets a ``ObjectiveBankList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the objective
        banks specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``ObjectiveBank`` objects may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :param objective_bank_ids: the list of ``Ids`` to retrieve
        :type objective_bank_ids: ``osid.id.IdList``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def get_objective_banks_by_genus_type(self, objective_bank_genus_type):
        """Gets a ``ObjectiveBankList`` corresponding to the given objective bank genus ``Type`` which does not include
        objective banks of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :param objective_bank_genus_type: an objective bank genus type
        :type objective_bank_genus_type: ``osid.type.Type``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NullArgument`` -- ``objective_bank_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def get_objective_banks_by_parent_genus_type(self, objective_bank_genus_type):
        """Gets a ``ObjectiveBankList`` corresponding to the given objective bank genus ``Type`` and include any
        additional objective banks with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :param objective_bank_genus_type: an objective bank genus type
        :type objective_bank_genus_type: ``osid.type.Type``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NullArgument`` -- ``objective_bank_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def get_objective_banks_by_record_type(self, objective_bank_record_type):
        """Gets a ``ObjectiveBankList`` containing the given objective bank record ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :param objective_bank_record_type: an objective bank record type
        :type objective_bank_record_type: ``osid.type.Type``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NullArgument`` -- ``objective_bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def get_objective_banks_by_provider(self, resource_id):
        """Gets a ``ObjectiveBankList`` for the given provider.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def get_objective_banks(self):
        """Gets all ``ObjectiveBanks``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :return: a ``ObjectiveBankList``
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    objective_banks = property(fget=get_objective_banks)


##
# The following methods are from osid.learning.ObjectiveBankAdminSession

    def can_create_objective_banks(self):
        """Tests if this user can create ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``ObjectiveBank`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_create_objective_bank_with_record_types(self, objective_bank_record_types):
        """Tests if this user can create a single ``ObjectiveBank`` using the desired record types.

        While ``LearningManager.getObjectiveBankRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``ObjectiveBank``. Providing an empty array tests if an
        ``ObjectiveBank`` can be created with no records.

        :param objective_bank_record_types: array of objective bank record types
        :type objective_bank_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``ObjectiveBank`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_objective_bank_form_for_create(self, objective_bank_record_types):
        """Gets the objective bank form for creating new objective banks.

        A new form should be requested for each create transaction.

        :param objective_bank_record_types: array of objective bank record types
        :type objective_bank_record_types: ``osid.type.Type[]``
        :return: the objective bank form
        :rtype: ``osid.learning.ObjectiveBankForm``
        :raise: ``NullArgument`` -- ``objective_bank_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types.

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankForm

    def create_objective_bank(self, objective_bank_form):
        """Creates a new ``ObjectiveBank``.

        :param objective_bank_form: the form for this ``ObjectiveBank``
        :type objective_bank_form: ``osid.learning.ObjectiveBankForm``
        :return: the new ``ObjectiveBank``
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``IllegalState`` -- ``objective_bank_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``objective_bank_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``objective_bank_form`` did not originate from
        ``get_objective_bank_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBank

    def can_update_objective_banks(self):
        """Tests if this user can update ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``ObjectiveBank`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_objective_bank_form_for_update(self, objective_bank_id):
        """Gets the objective bank form for updating an existing objective bank.

        A new objective bank form should be requested for each update
        transaction.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: the objective bank form
        :rtype: ``osid.learning.ObjectiveBankForm``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankForm

    def update_objective_bank(self, objective_bank_form):
        """Updates an existing objective bank.

        :param objective_bank_form: the form containing the elements to be updated
        :type objective_bank_form: ``osid.learning.ObjectiveBankForm``
        :raise: ``IllegalState`` -- ``objective_bank_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``objective_bank_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``objective_bank_form did not originate from get_objective_bank_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_objective_banks(self):
        """Tests if this user can delete objective banks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``ObjectiveBank`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_objective_bank(self, objective_bank_id):
        """Deletes an ``ObjectiveBank``.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank`` to remove
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_objective_bank_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``ObjectiveBank`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def alias_objective_bank(self, objective_bank_id, alias_id):
        """Adds an ``Id`` to an ``ObjectiveBank`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``ObjectiveBank`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another objective bank, it
        is reassigned to the given objective bank ``Id``.

        :param objective_bank_id: the ``Id`` of an ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.learning.ObjectiveBankHierarchySession

    def get_objective_bank_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    objective_bank_hierarchy_id = property(fget=get_objective_bank_hierarchy_id)

    def get_objective_bank_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    objective_bank_hierarchy = property(fget=get_objective_bank_hierarchy)

    def can_access_objective_bank_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer traversal
        functions to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_objective_bank_view(self):
        """The returns from the objective bank methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_objective_bank_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_root_objective_bank_ids(self):
        """Gets the root objective bank ``Ids`` in this hierarchy.

        :return: the root objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    root_objective_bank_ids = property(fget=get_root_objective_bank_ids)

    def get_root_objective_banks(self):
        """Gets the root objective banks in this objective bank hierarchy.

        :return: the root objective banks
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    root_objective_banks = property(fget=get_root_objective_banks)

    def has_parent_objective_banks(self, objective_bank_id):
        """Tests if the ``ObjectiveBank`` has any parents.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if the objective bank has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def is_parent_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an ``Id`` is a direct parent of an objective bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``objective_bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

    def get_parent_objective_bank_ids(self, objective_bank_id):
        """Gets the parent ``Ids`` of the given objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the objective bank
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_parent_objective_banks(self, objective_bank_id):
        """Gets the parents of the given objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: the parents of the objective bank
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def is_ancestor_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an ``Id`` is an ancestor of an objective bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``objective_bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

    def has_child_objective_banks(self, objective_bank_id):
        """Tests if an objective bank has any children.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if the ``objective_bank_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def is_child_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an objective bank is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``objective_bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

    def get_child_objective_bank_ids(self, objective_bank_id):
        """Gets the child ``Ids`` of the given objective bank.

        :param objective_bank_id: the ``Id`` to query
        :type objective_bank_id: ``osid.id.Id``
        :return: the children of the objective bank
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_child_objective_banks(self, objective_bank_id):
        """Gets the children of the given objective bank.

        :param objective_bank_id: the ``Id`` to query
        :type objective_bank_id: ``osid.id.Id``
        :return: the children of the objective bank
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def is_descendant_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an ``Id`` is a descendant of an objective bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``objective_bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return # boolean

    def get_objective_bank_node_ids(self, objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given objective bank.

        :param objective_bank_id: the ``Id`` to query
        :type objective_bank_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
        node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
        in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a catalog node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Node

    def get_objective_bank_nodes(self, objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given objective bank.

        :param objective_bank_id: the ``Id`` to query
        :type objective_bank_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
        node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
        in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an objective bank node
        :rtype: ``osid.learning.ObjectiveBankNode``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankNode


##
# The following methods are from osid.learning.ObjectiveBankHierarchyDesignSession

    def get_objective_bank_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    objective_bank_hierarchy_id = property(fget=get_objective_bank_hierarchy_id)

    def get_objective_bank_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    objective_bank_hierarchy = property(fget=get_objective_bank_hierarchy)

    def can_modify_objective_bank_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def add_root_objective_bank(self, objective_bank_id):
        """Adds a root objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_bank_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_root_objective_bank(self, objective_bank_id):
        """Removes a root objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not a root
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def add_child_objective_bank(self, objective_bank_id, child_id):
        """Adds a child to an objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_bank_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``objective_bank_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_objective_bank(self, objective_bank_id, child_id):
        """Removes a child from an objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_bank_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_objective_banks(self, objective_bank_id):
        """Removes all children from an objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_bank_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




class LearningProxyManager(osid_managers.OsidProxyManager, LearningProfile):
    """The learning manager provides access to learning sessions and provides interoperability tests for various aspects
        of
        this service.

    Methods in this manager support the passing of a ``Proxy``. The
    sessions included in this manager are:

      * ``ObjectiveLookupSession:`` a session to look up objectives
      * ``ObjectiveLookupSession:`` a session to query objectives
        ``None``
      * ``ObjectiveSearchSession:`` a session to search objectives
      * ``ObjectiveAdminSession:`` a session to create, modify and
        delete objectives ``None``
      * ``ObjectiveNotificationSession: a`` session to receive messages
        pertaining to objective ```` changes
      * ``ObjectiveHierarchySession:`` a session to traverse objective
        hierarchies
      * ``ObjectiveHierarchyDesignSession:`` a session to design
        objective hierarchies
      * ``ObjectiveSequencingSession:`` a session to sequence objectives
      * ``ObjectiveObjectiveBankSession:`` a session for retriieving
        objective and objective bank mappings
      * ``ObjectiveObjectiveBankAssignmentSession:`` a session for
        managing objective and objective bank mappings
      * ``ObjectiveSmartObjectiveBankSession:`` a session for managing
        dynamic objective banks
      * ``ObjectiveRequisiteSession:`` a session to examine objective
        requisites
      * ``ObjectiveRequisiteAssignmentSession:`` a session to manage
        objective requisites

      * ``ActivityLookupSession:`` a session to look up activities
      * ``ActivityQuerySession:`` a session to query activities ``None``
      * ``ActivitySearchSession:`` a session to search activities
      * ``ActivityAdminSession:`` a session to create, modify and delete
        activities ``None``
      * ``ActivityNotificationSession: a`` session to receive messages
        pertaining to activity ```` changes
      * ``ActivityObjectiveBankSession:`` a session for retriieving
        activity and objective bank mappings
      * ``ActivityObjectiveBankAssignmentSession:`` a session for
        managing activity and objective bank mappings
      * ``ActivitySmartObjectiveBankSession:`` a session for managing
        dynamic objective banks of activities

      * ``ProficiencyLookupSession:`` a session to retrieve
        proficiencies
      * ``ProficiencyQuerySession:`` a session to query proficiencies
      * ``ProficiencySearchSession:`` a session to search for
        proficiencies
      * ``ProficiencyAdminSession:`` a session to create, update, and
        delete proficiencies
      * ``ProficiencyNotificationSession:`` a session to receive
        notifications pertaining to proficiency changes
      * ``ProficiencyObjectiveBankSession:`` a session to look up
        proficiency to objective bank mappings
      * ``ProficiencyObjectiveBankAssignmentSession:`` a session to
        manage proficiency to objective bank mappings
      * ``ProficiencySmartObjectiveBankSession:`` a session to manage
        smart objective banks of proficiencies
      * ``MyLearningPathSession:`` a session to examine learning paths
        of objectives
      * ``LearningPathSession:`` a session to examine learning paths of
        objectives

      * ``ObjectiveBankLookupSession:`` a session to lookup objective
        banks
      * ``ObjectiveBankQuerySession:`` a session to query objective
        banks
      * ``ObjectiveBankSearchSession`` : a session to search objective
        banks
      * ``ObjectiveBankAdminSession`` : a session to create, modify and
        delete objective banks
      * ``ObjectiveBankNotificationSession`` : a session to receive
        messages pertaining to objective bank changes
      * ``ObjectiveBankHierarchySession:`` a session to traverse the
        objective bank hierarchy
      * ``ObjectiveBankHierarchyDesignSession:`` a session to manage the
        objective bank hierarchy

    """

    def get_objective_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the objective lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveLookupSession``
        :rtype: ``osid.learning.ObjectiveLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_lookup()`` is ``true``.*

        """
        return # osid.learning.ObjectiveLookupSession

    def get_objective_lookup_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective lookup service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _objective_lookup_session``
        :rtype: ``osid.learning.ObjectiveLookupSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveLookupSession

    def get_objective_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the objective query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveQuerySession``
        :rtype: ``osid.learning.ObjectiveQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_query()`` is ``true``.*

        """
        return # osid.learning.ObjectiveQuerySession

    def get_objective_query_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective query service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _objective_query_session``
        :rtype: ``osid.learning.ObjectiveQuerySession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveQuerySession

    def get_objective_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the objective search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveSearchSession``
        :rtype: ``osid.learning.ObjectiveSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_search()`` is ``true``.*

        """
        return # osid.learning.ObjectiveSearchSession

    def get_objective_search_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective search service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _objective_search_session``
        :rtype: ``osid.learning.ObjectiveSearchSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveSearchSession

    def get_objective_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the objective administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveAdminSession``
        :rtype: ``osid.learning.ObjectiveAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_admin()`` is ``true``.*

        """
        return # osid.learning.ObjectiveAdminSession

    def get_objective_admin_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective admin service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _objective_admin_session``
        :rtype: ``osid.learning.ObjectiveAdminSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveAdminSession

    def get_objective_notification_session(self, objective_receiver, proxy):
        """Gets the notification session for notifications pertaining to objective changes.

        :param objective_receiver: the objective receiver
        :type objective_receiver: ``osid.learning.ObjectiveReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveNotificationSession``
        :rtype: ``osid.learning.ObjectiveNotificationSession``
        :raise: ``NullArgument`` -- ``objective_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_notification()`` is ``true``.*

        """
        return # osid.learning.ObjectiveNotificationSession

    def get_objective_notification_session_for_objective_bank(self, objective_receiver, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective notification service for the given objective bank.

        :param objective_receiver: the objective receiver
        :type objective_receiver: ``osid.learning.ObjectiveReceiver``
        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _objective_notification_session``
        :rtype: ``osid.learning.ObjectiveNotificationSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_receiver, objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveNotificationSession

    def get_objective_hierarchy_session(self, proxy):
        """Gets the session for traversing objective hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveHierarchySession``
        :rtype: ``osid.learning.ObjectiveHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_hierarchy()`` is ``true``.*

        """
        return # osid.learning.ObjectiveHierarchySession

    def get_objective_hierarchy_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective hierarchy traversal service for the given objective
        bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveHierarchySession``
        :rtype: ``osid.learning.ObjectiveHierarchySession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_hierarchy()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_hierarchy()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveHierarchySession

    def get_objective_hierarchy_design_session(self, proxy):
        """Gets the session for designing objective hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveHierarchyDesignSession``
        :rtype: ``osid.learning.ObjectiveHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_hierarchy_design()`` is ``true``.*

        """
        return # osid.learning.ObjectiveHierarchyDesignSession

    def get_objective_hierarchy_design_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective hierarchy design service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveHierarchyDesignSession``
        :rtype: ``osid.learning.ObjectiveHierarchyDesignSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_hierarchy_design()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_hierarchy_design()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveHierarchyDesignSession

    def get_objective_sequencing_session(self, proxy):
        """Gets the session for sequencing objectives.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveSequencingSession``
        :rtype: ``osid.learning.ObjectiveSequencingSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_sequencing()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_sequencing()`` is ``true``.*

        """
        return # osid.learning.ObjectiveSequencingSession

    def get_objective_sequencing_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveSequencingSession``
        :rtype: ``osid.learning.ObjectiveSequencingSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_sequencing()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_sequencing()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveSequencingSession

    def get_objective_objective_bank_session(self, proxy):
        """Gets the session for retrieving objective to objective bank mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveObjectiveBankSession``
        :rtype: ``osid.learning.ObjectiveObjectiveBankSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_objective_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_objective_bank()`` is ``true``.*

        """
        return # osid.learning.ObjectiveObjectiveBankSession

    def get_objective_objective_bank_assignment_session(self, proxy):
        """Gets the session for assigning objective to objective bank mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveObjectiveBankAssignmentSession``
        :rtype: ``osid.learning.ObjectiveObjectiveBankAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_objective_bank_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_objective_bank_assignment()`` is ``true``.*

        """
        return # osid.learning.ObjectiveObjectiveBankAssignmentSession

    def get_objective_smart_objective_bank_session(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` to manage dynamic objective banks of objectives.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveSmartObjectiveBankSession``
        :rtype: ``osid.learning.ActivitySmartObjectiveBankSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_smart_objective_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_smart_objective_bank()`` is ``true``.*

        """
        return # osid.learning.ActivitySmartObjectiveBankSession

    def get_objective_requisite_session(self, proxy):
        """Gets the session for examining objective requisites.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveRequisiteSession``
        :rtype: ``osid.learning.ObjectiveRequisiteSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_requisite()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_requisite()`` is ``true``.*

        """
        return # osid.learning.ObjectiveRequisiteSession

    def get_objective_requisite_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveRequisiteSession``
        :rtype: ``osid.learning.ObjectiveRequisiteSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_requisite()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_requisite()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveRequisiteSession

    def get_objective_requisite_assignment_session(self, proxy):
        """Gets the session for managing objective requisites.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveRequisiteAssignmentSession``
        :rtype: ``osid.learning.ObjectiveRequisiteAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_requisite_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_requisite_assignment()`` is ``true``.*

        """
        return # osid.learning.ObjectiveRequisiteAssignmentSession

    def get_objective_requisite_assignment_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveRequisiteAssignmentSession``
        :rtype: ``osid.learning.ObjectiveRequisiteAssignmentSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_requisite_assignment()`` or ``supports_visible_federation()``
        is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_requisite_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ObjectiveRequisiteAssignmentSession

    def get_activity_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the activity lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivityLookupSession``
        :rtype: ``osid.learning.ActivityLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_lookup()`` is ``true``.*

        """
        return # osid.learning.ActivityLookupSession

    def get_activity_lookup_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the activity lookup service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivityLookupSession``
        :rtype: ``osid.learning.ActivityLookupSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ActivityLookupSession

    def get_activity_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the activity query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivityQuerySession``
        :rtype: ``osid.learning.ActivityQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_query()`` is ``true``.*

        """
        return # osid.learning.ActivityQuerySession

    def get_activity_query_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the activity query service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivityQuerySession``
        :rtype: ``osid.learning.ActivityQuerySession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ActivityQuerySession

    def get_activity_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the activity search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivitySearchSession``
        :rtype: ``osid.learning.ActivitySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_search()`` is ``true``.*

        """
        return # osid.learning.ActivitySearchSession

    def get_activity_search_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the activity search service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivitySearchSession``
        :rtype: ``osid.learning.ActivitySearchSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ActivitySearchSession

    def get_activity_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the activity administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivityAdminSession``
        :rtype: ``osid.learning.ActivityAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_admin()`` is ``true``.*

        """
        return # osid.learning.ActivityAdminSession

    def get_activity_admin_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the activity admin service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ActivityAdminSession``
        :rtype: ``osid.learning.ActivityAdminSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ActivityAdminSession

    def get_activity_notification_session(self, activity_receiver, proxy):
        """Gets the notification session for notifications pertaining to activity changes.

        :param activity_receiver: the activity receiver
        :type activity_receiver: ``osid.learning.ActivityReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivityNotificationSession``
        :rtype: ``osid.learning.ActivityNotificationSession``
        :raise: ``NullArgument`` -- ``activity_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_notification()`` is ``true``.*

        """
        return # osid.learning.ActivityNotificationSession

    def get_activity_notification_session_for_objective_bank(self, activity_receiver, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the activity notification service for the given objective bank.

        :param activity_receiver: the activity receiver
        :type activity_receiver: ``osid.learning.ActivityReceiver``
        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _activity_notification_session``
        :rtype: ``osid.learning.ActivityNotificationSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``activity_receiver, objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.learning.ActivityNotificationSession

    def get_activity_objective_bank_session(self, proxy):
        """Gets the session for retrieving activity to objective bank mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivityObjectiveBankSession``
        :rtype: ``osid.learning.ActivityObjectiveBankSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_objective_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_objective_bank()`` is ``true``.*

        """
        return # osid.learning.ActivityObjectiveBankSession

    def get_activity_objective_bank_assignment_session(self, proxy):
        """Gets the session for assigning activity to objective bank mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivityObjectiveBankAssignmentSession``
        :rtype: ``osid.learning.ActivityObjectiveBankAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_objective_bank_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_objective_bank_assignment()`` is ``true``.*

        """
        return # osid.learning.ActivityObjectiveBankAssignmentSession

    def get_activity_smart_objective_bank_session(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` to manage dynamic objective banks of activities.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivitySmartObjectiveBankSession``
        :rtype: ``osid.learning.ActivitySmartObjectiveBankSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_smart_objective_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_activity_smart_objective_bank()`` is ``true``.*

        """
        return # osid.learning.ActivitySmartObjectiveBankSession

    def get_proficiency_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the proficiency lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyLookupSession``
        :rtype: ``osid.learning.ProficiencyLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_lookup()`` is ``true``.*

        """
        return # osid.learning.ProficiencyLookupSession

    def get_proficiency_lookup_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the proficiency lookup service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the obective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyLookupSession``
        :rtype: ``osid.learning.ProficiencyLookupSession``
        :raise: ``NotFound`` -- no ``ObjectiveBank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.learning.ProficiencyLookupSession

    def get_proficiency_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the proficiency query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyQuerySession``
        :rtype: ``osid.learning.ProficiencyQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_query()`` is ``true``.*

        """
        return # osid.learning.ProficiencyQuerySession

    def get_proficiency_query_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the proficiency query service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the obective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyQuerySession``
        :rtype: ``osid.learning.ProficiencyQuerySession``
        :raise: ``NotFound`` -- no ``ObjectiveBank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.learning.ProficiencyQuerySession

    def get_proficiency_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the proficiency search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencySearchSession``
        :rtype: ``osid.learning.ProficiencySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_search()`` is ``true``.*

        """
        return # osid.learning.ProficiencySearchSession

    def get_proficiency_search_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the proficiency search service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencySearchSession``
        :rtype: ``osid.learning.ProficiencySearchSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.learning.ProficiencySearchSession

    def get_proficiency_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the proficiency administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyAdminSession``
        :rtype: ``osid.learning.ProficiencyAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_admin()`` is ``true``.*

        """
        return # osid.learning.ProficiencyAdminSession

    def get_proficiency_admin_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the proficiency administration service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyAdminSession``
        :rtype: ``osid.learning.ProficiencyAdminSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.learning.ProficiencyAdminSession

    def get_proficiency_notification_session(self, proficiency_receiver, proxy):
        """Gets the ``OsidSession`` associated with the proficiency notification service.

        :param proficiency_receiver: the notification callback
        :type proficiency_receiver: ``osid.learning.ProficiencyReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyNotificationSession``
        :rtype: ``osid.learning.ProficiencyNotificationSession``
        :raise: ``NullArgument`` -- ``proficiency_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_notification()`` is ``true``.*

        """
        return # osid.learning.ProficiencyNotificationSession

    def get_proficiency_notification_session_for_objective_bank(self, proficiency_receiver, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the proficiency notification service for the given objective bank.

        :param proficiency_receiver: the notification callback
        :type proficiency_receiver: ``osid.learning.ProficiencyReceiver``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyNotificationSession``
        :rtype: ``osid.learning.ProficiencyNotificationSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``proficiency_receiver, objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.learning.ProficiencyNotificationSession

    def get_proficiency_objective_bank_session(self, proxy):
        """Gets the ``OsidSession`` to lookup proficiency/objective bank mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyObjectiveBankSession``
        :rtype: ``osid.learning.ProficiencyObjectiveBankSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_objective_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_objective_bank()`` is ``true``.*

        """
        return # osid.learning.ProficiencyObjectiveBankSession

    def get_proficiency_objective_bank_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with assigning proficiencies to objective banks.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyObjectiveBankAssignmentSession``
        :rtype: ``osid.learning.ProficiencyObjectiveBankAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_objective_bank_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_objective_bank_assignment()`` is
        ``true``.*

        """
        return # osid.learning.ProficiencyObjectiveBankAssignmentSession

    def get_proficiency_smart_objective_bank_session(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` to manage dynamic objective banks of proficiencies.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencySmartObjectiveBankSession``
        :rtype: ``osid.learning.ProficiencySmartObjectiveBankSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_smart_objective_bank()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_proficiency_smart_objective_bank()`` is ``true``.*

        """
        return # osid.learning.ProficiencySmartObjectiveBankSession

    def get_my_learning_path_session(self, proxy):
        """Gets the ``OsidSession`` associated with the my learning path service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MyLearningPathSession``
        :rtype: ``osid.learning.MyLearningPathSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_learning_path()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_my_learning_path()`` is ``true``.*

        """
        return # osid.learning.MyLearningPathSession

    def get_my_learning_path_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the my learning path service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MyLearningPathSession``
        :rtype: ``osid.learning.MyLearningPathSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_learning_path()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_my_learning_path()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.learning.MyLearningPathSession

    def get_learning_path_session(self, proxy):
        """Gets the ``OsidSession`` associated with the learning path service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LearningPathSession``
        :rtype: ``osid.learning.LearningPathSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_learning_path()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_learning_path()`` is ``true``.*

        """
        return # osid.learning.LearningPathSession

    def get_learning_path_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the learning path service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LearningPathSession``
        :rtype: ``osid.learning.LearningPathSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supporty_learning_path()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_learning_path()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return # osid.learning.LearningPathSession

    def get_objective_bank_lookup_session(self, proxy):
        """Gets the OsidSession associated with the objective bank lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveBankLookupSession``
        :rtype: ``osid.learning.ObjectiveBankLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_lookup() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_lookup()`` is true.*

        """
        return # osid.learning.ObjectiveBankLookupSession

    def get_objective_bank_query_session(self, proxy):
        """Gets the OsidSession associated with the objective bank query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveBankQuerySession``
        :rtype: ``osid.learning.ObjectiveBankQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_query() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_query()`` is true.*

        """
        return # osid.learning.ObjectiveBankQuerySession

    def get_objective_bank_search_session(self, proxy):
        """Gets the OsidSession associated with the objective bank search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveBankSearchSession``
        :rtype: ``osid.learning.ObjectiveBankSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_search() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_search()`` is true.*

        """
        return # osid.learning.ObjectiveBankSearchSession

    def get_objective_bank_admin_session(self, proxy):
        """Gets the OsidSession associated with the objective bank administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveBankAdminSession``
        :rtype: ``osid.learning.ObjectiveBankAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_admin() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_admin()`` is true.*

        """
        return # osid.learning.ObjectiveBankAdminSession

    def get_objective_bank_notification_session(self, objective_bank_receiver, proxy):
        """Gets the notification session for notifications pertaining to objective bank service changes.

        :param objective_bank_receiver: the objective bank receiver
        :type objective_bank_receiver: ``osid.learning.ObjectiveBankReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveBankNotificationSession``
        :rtype: ``osid.learning.ObjectiveBankNotificationSession``
        :raise: ``NullArgument`` -- ``objective_bank_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_notification() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_notification()`` is true.*

        """
        return # osid.learning.ObjectiveBankNotificationSession

    def get_objective_bank_hierarchy_session(self, proxy):
        """Gets the session traversing objective bank hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveBankHierarchySession``
        :rtype: ``osid.learning.ObjectiveBankHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_hierarchy() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_hierarchy()`` is true.*

        """
        return # osid.learning.ObjectiveBankHierarchySession

    def get_objective_bank_hierarchy_design_session(self, proxy):
        """Gets the session designing objective bank hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveBankHierarchyDesignSession``
        :rtype: ``osid.learning.ObjectiveBankHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_hierarchy_design() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_objective_bank_hierarchy_design()`` is true.*

        """
        return # osid.learning.ObjectiveBankHierarchyDesignSession

    def get_learning_batch_proxy_manager(self):
        """Gets a ``LearningBatchProxyManager``.

        :return: a ``LearningBatchProxyManager``
        :rtype: ``osid.learning.batch.LearningBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_learning_batch() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_learning_batch()`` is true.*

        """
        return # osid.learning.batch.LearningBatchProxyManager

    learning_batch_proxy_manager = property(fget=get_learning_batch_proxy_manager)
##
# The following methods are from osid.learning.ObjectiveObjectiveBankSession

    def can_lookup_objective_objective_bank_mappings(self):
        """Tests if this user can perform lookups of objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_objective_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_objective_bank_view(self):
        """A complete view of the ``Objective`` and ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_objective_ids_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Objective``  ``Ids`` associated with an ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related objectives
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_objectives_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Objectives`` associated with an ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related objective ``Ids``
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList

    def get_objective_ids_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Objective Ids`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objective bank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of objective ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_objectives_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Objectives`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objective bank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of objectives
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList

    def get_objective_bank_ids_by_objective(self, objective_id):
        """Gets the list of ``ObjectiveBank``  ``Ids`` mapped to an ``Objective``.

        :param objective_id: ``Id`` of an ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: list of objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_objective_banks_by_objective(self, objective_id):
        """Gets the list of ``ObjectiveBanks`` mapped to an ``Objective``.

        :param objective_id: ``Id`` of an ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: list of objective banks
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList


##
# The following methods are from osid.learning.ObjectiveObjectiveBankAssignmentSession

    def can_assign_objectives(self):
        """Tests if this user can alter objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_assign_objectives_to_objective_bank(self, objective_bank_id):
        """Tests if this user can alter objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_assignable_objective_bank_ids(self, objective_bank_id):
        """Gets a list of objective banks including and under the given objective bank node in which any objective can
        be assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of assignable objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_assignable_objective_bank_ids_for_objective(self, objective_bank_id, objective_id):
        """Gets a list of objective banks including and under the given objective bank node in which a specific
        objective can be assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: list of assignable objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def assign_objective_to_objective_bank(self, objective_id, objective_bank_id):
        """Adds an existing ``Objective`` to an ``ObjectiveBank``.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_id`` already mapped to ``objective_bank_id``
        :raise: ``NotFound`` -- ``objective_id`` or ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def unassign_objective_from_objective_bank(self, objective_id, objective_bank_id):
        """Removes an ``Objective`` from an ``ObjectiveBank``.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id`` or ``objective_bank_id`` not found or ``objective_id`` not mapped to
        ``objective_bank_id``
        :raise: ``NullArgument`` -- ``objective_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def reassign_proficiency_to_objective_bank(self, objective_id, from_objective_bank_id, to_objective_bank_id):
        """Moves an ``Objective`` from one ``ObjectiveBank`` to another.

        Mappings to other ``ObjectiveBanks`` are unaffected.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param from_objective_bank_id: the ``Id`` of the current ``ObjectiveBank``
        :type from_objective_bank_id: ``osid.id.Id``
        :param to_objective_bank_id: the ``Id`` of the destination ``ObjectiveBank``
        :type to_objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id, from_objective_bank_id,`` or ``to_objective_bank_id`` not found or
        ``objective_id`` not mapped to ``from_objective_bank_id``
        :raise: ``NullArgument`` -- ``objective_id, from_objective_bank_id,`` or ``to_objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.learning.ActivityObjectiveBankSession

    def can_lookup_activity_objective_bank_mappings(self):
        """Tests if this user can perform lookups of activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_objective_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_objective_bank_view(self):
        """A complete view of the ``Activity`` and ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_activity_ids_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Activity``  ``Ids`` associated with an ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related activity ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_activities_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Activities`` associated with an ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related activities
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ActivityList

    def get_activity_ids_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Activity Ids`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objective bank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of activity ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_activities_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Activities`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objective bank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of activities
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ActivityList

    def get_objective_bank_ids_by_activity(self, activity_id):
        """Gets the list of ``ObjectiveBank Ids`` mapped to a ``Activity``.

        :param activity_id: ``Id`` of a ``Activity``
        :type activity_id: ``osid.id.Id``
        :return: list of objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``activity_id`` is not found
        :raise: ``NullArgument`` -- ``activity_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_objective_banks_by_activity(self, activity_id):
        """Gets the list of ``ObjectiveBanks`` mapped to a ``Activity``.

        :param activity_id: ``Id`` of a ``Activity``
        :type activity_id: ``osid.id.Id``
        :return: list of objective bank ``Ids``
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- ``activity_id`` is not found
        :raise: ``NullArgument`` -- ``activity_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList


##
# The following methods are from osid.learning.ActivityObjectiveBankAssignmentSession

    def can_assign_activities(self):
        """Tests if this user can alter activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_assign_activities_to_objective_bank(self, objective_bank_id):
        """Tests if this user can alter activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_assignable_objective_bank_ids(self, objective_bank_id):
        """Gets a list of objective banks including and under the given objective bank node in which any activity can be
        assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of assignable objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_assignable_objective_bank_ids_for_activity(self, objective_bank_id, activity_id):
        """Gets a list of objective banks including and under the given objective bank node in which a specific activity
        can be assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :return: list of assignable objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``activity_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def assign_activity_to_objective_bank(self, activity_id, objective_bank_id):
        """Adds an existing ``Activity`` to a ``ObjectiveBank``.

        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``activity_id`` already mapped to ``objective_bank_id``
        :raise: ``NotFound`` -- ``activity_id`` or ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``activity_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def unassign_activity_from_objective_bank(self, activity_id, objective_bank_id):
        """Removes a ``Activity`` from a ``ObjectiveBank``.

        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``activity_id`` or ``objective_bank_id`` not found or ``activity_id`` not mapped to
        ``objective_bank_id``
        :raise: ``NullArgument`` -- ``activity_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def reassign_activity_to_objective_bank(self, activity_id, from_objective_bank_id, to_objective_bank_id):
        """Moves an ``Activity`` from one ``ObjectiveBank`` to another.

        Mappings to other ``ObjectiveBanks`` are unaffected.

        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :param from_objective_bank_id: the ``Id`` of the current ``ObjectiveBank``
        :type from_objective_bank_id: ``osid.id.Id``
        :param to_objective_bank_id: the ``Id`` of the destination ``ObjectiveBank``
        :type to_objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``activity_id, from_objective_bank_id,`` or ``to_objective_bank_id`` not found or
        ``activity_id`` not mapped to ``from_objective_bank_id``
        :raise: ``NullArgument`` -- ``activity_id, from_objective_bank_id,`` or ``to_objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.learning.ObjectiveBankLookupSession

    def can_lookup_objective_banks(self):
        """Tests if this user can perform ``ObjectiveBank`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_objective_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_objective_bank_view(self):
        """A complete view of the ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_objective_bank(self, objective_bank_id):
        """Gets the ``ObjectiveBank`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``ObjectiveBank`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``ObjectiveBank`` and
        retained for compatility.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: the objective bank
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.learning.ObjectiveBank

    def get_objective_banks_by_ids(self, objective_bank_ids):
        """Gets a ``ObjectiveBankList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the objective
        banks specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``ObjectiveBank`` objects may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :param objective_bank_ids: the list of ``Ids`` to retrieve
        :type objective_bank_ids: ``osid.id.IdList``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def get_objective_banks_by_genus_type(self, objective_bank_genus_type):
        """Gets a ``ObjectiveBankList`` corresponding to the given objective bank genus ``Type`` which does not include
        objective banks of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :param objective_bank_genus_type: an objective bank genus type
        :type objective_bank_genus_type: ``osid.type.Type``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NullArgument`` -- ``objective_bank_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def get_objective_banks_by_parent_genus_type(self, objective_bank_genus_type):
        """Gets a ``ObjectiveBankList`` corresponding to the given objective bank genus ``Type`` and include any
        additional objective banks with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :param objective_bank_genus_type: an objective bank genus type
        :type objective_bank_genus_type: ``osid.type.Type``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NullArgument`` -- ``objective_bank_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def get_objective_banks_by_record_type(self, objective_bank_record_type):
        """Gets a ``ObjectiveBankList`` containing the given objective bank record ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :param objective_bank_record_type: an objective bank record type
        :type objective_bank_record_type: ``osid.type.Type``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NullArgument`` -- ``objective_bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def get_objective_banks_by_provider(self, resource_id):
        """Gets a ``ObjectiveBankList`` for the given provider.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def get_objective_banks(self):
        """Gets all ``ObjectiveBanks``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :return: a ``ObjectiveBankList``
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    objective_banks = property(fget=get_objective_banks)


##
# The following methods are from osid.learning.ObjectiveBankAdminSession

    def can_create_objective_banks(self):
        """Tests if this user can create ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``ObjectiveBank`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_create_objective_bank_with_record_types(self, objective_bank_record_types):
        """Tests if this user can create a single ``ObjectiveBank`` using the desired record types.

        While ``LearningManager.getObjectiveBankRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``ObjectiveBank``. Providing an empty array tests if an
        ``ObjectiveBank`` can be created with no records.

        :param objective_bank_record_types: array of objective bank record types
        :type objective_bank_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``ObjectiveBank`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_objective_bank_form_for_create(self, objective_bank_record_types):
        """Gets the objective bank form for creating new objective banks.

        A new form should be requested for each create transaction.

        :param objective_bank_record_types: array of objective bank record types
        :type objective_bank_record_types: ``osid.type.Type[]``
        :return: the objective bank form
        :rtype: ``osid.learning.ObjectiveBankForm``
        :raise: ``NullArgument`` -- ``objective_bank_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types.

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankForm

    def create_objective_bank(self, objective_bank_form):
        """Creates a new ``ObjectiveBank``.

        :param objective_bank_form: the form for this ``ObjectiveBank``
        :type objective_bank_form: ``osid.learning.ObjectiveBankForm``
        :return: the new ``ObjectiveBank``
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``IllegalState`` -- ``objective_bank_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``objective_bank_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``objective_bank_form`` did not originate from
        ``get_objective_bank_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBank

    def can_update_objective_banks(self):
        """Tests if this user can update ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``ObjectiveBank`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_objective_bank_form_for_update(self, objective_bank_id):
        """Gets the objective bank form for updating an existing objective bank.

        A new objective bank form should be requested for each update
        transaction.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: the objective bank form
        :rtype: ``osid.learning.ObjectiveBankForm``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankForm

    def update_objective_bank(self, objective_bank_form):
        """Updates an existing objective bank.

        :param objective_bank_form: the form containing the elements to be updated
        :type objective_bank_form: ``osid.learning.ObjectiveBankForm``
        :raise: ``IllegalState`` -- ``objective_bank_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``objective_bank_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``objective_bank_form did not originate from get_objective_bank_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_objective_banks(self):
        """Tests if this user can delete objective banks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``ObjectiveBank`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_objective_bank(self, objective_bank_id):
        """Deletes an ``ObjectiveBank``.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank`` to remove
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_objective_bank_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``ObjectiveBank`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def alias_objective_bank(self, objective_bank_id, alias_id):
        """Adds an ``Id`` to an ``ObjectiveBank`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``ObjectiveBank`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another objective bank, it
        is reassigned to the given objective bank ``Id``.

        :param objective_bank_id: the ``Id`` of an ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.learning.ObjectiveBankHierarchySession

    def get_objective_bank_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    objective_bank_hierarchy_id = property(fget=get_objective_bank_hierarchy_id)

    def get_objective_bank_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    objective_bank_hierarchy = property(fget=get_objective_bank_hierarchy)

    def can_access_objective_bank_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer traversal
        functions to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_objective_bank_view(self):
        """The returns from the objective bank methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_objective_bank_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_root_objective_bank_ids(self):
        """Gets the root objective bank ``Ids`` in this hierarchy.

        :return: the root objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    root_objective_bank_ids = property(fget=get_root_objective_bank_ids)

    def get_root_objective_banks(self):
        """Gets the root objective banks in this objective bank hierarchy.

        :return: the root objective banks
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    root_objective_banks = property(fget=get_root_objective_banks)

    def has_parent_objective_banks(self, objective_bank_id):
        """Tests if the ``ObjectiveBank`` has any parents.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if the objective bank has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def is_parent_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an ``Id`` is a direct parent of an objective bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``objective_bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

    def get_parent_objective_bank_ids(self, objective_bank_id):
        """Gets the parent ``Ids`` of the given objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the objective bank
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_parent_objective_banks(self, objective_bank_id):
        """Gets the parents of the given objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: the parents of the objective bank
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def is_ancestor_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an ``Id`` is an ancestor of an objective bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``objective_bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

    def has_child_objective_banks(self, objective_bank_id):
        """Tests if an objective bank has any children.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if the ``objective_bank_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def is_child_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an objective bank is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``objective_bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

    def get_child_objective_bank_ids(self, objective_bank_id):
        """Gets the child ``Ids`` of the given objective bank.

        :param objective_bank_id: the ``Id`` to query
        :type objective_bank_id: ``osid.id.Id``
        :return: the children of the objective bank
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_child_objective_banks(self, objective_bank_id):
        """Gets the children of the given objective bank.

        :param objective_bank_id: the ``Id`` to query
        :type objective_bank_id: ``osid.id.Id``
        :return: the children of the objective bank
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankList

    def is_descendant_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an ``Id`` is a descendant of an objective bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``objective_bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return # boolean

    def get_objective_bank_node_ids(self, objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given objective bank.

        :param objective_bank_id: the ``Id`` to query
        :type objective_bank_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
        node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
        in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a catalog node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Node

    def get_objective_bank_nodes(self, objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given objective bank.

        :param objective_bank_id: the ``Id`` to query
        :type objective_bank_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
        node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
        in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an objective bank node
        :rtype: ``osid.learning.ObjectiveBankNode``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBankNode


##
# The following methods are from osid.learning.ObjectiveBankHierarchyDesignSession

    def get_objective_bank_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    objective_bank_hierarchy_id = property(fget=get_objective_bank_hierarchy_id)

    def get_objective_bank_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    objective_bank_hierarchy = property(fget=get_objective_bank_hierarchy)

    def can_modify_objective_bank_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def add_root_objective_bank(self, objective_bank_id):
        """Adds a root objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_bank_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_root_objective_bank(self, objective_bank_id):
        """Removes a root objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not a root
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def add_child_objective_bank(self, objective_bank_id, child_id):
        """Adds a child to an objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_bank_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``objective_bank_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_objective_bank(self, objective_bank_id, child_id):
        """Removes a child from an objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_bank_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_objective_banks(self, objective_bank_id):
        """Removes all children from an objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_bank_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




class ObjectiveBank(osid_objects.OsidCatalog, osid_sessions.OsidSession):
    """an objective bank defines a collection of objectives."""

    # WILL THIS EVER BE CALLED DIRECTLY - OUTSIDE OF A MANAGER?
    def __init__(self, provider_manager, catalog, proxy, **kwargs):
        self._provider_manager = provider_manager
        self._catalog = catalog
        osid.OsidObject.__init__(self, self._catalog) # This is to initialize self._object
        osid.OsidSession.__init__(self, proxy) # This is to initialize self._proxy
        self._catalog_id = catalog.get_id()
        self._provider_sessions = kwargs
        self._session_management = AUTOMATIC
        self._objective_bank_view = DEFAULT
        self._object_views = dict()

    def _set_objective_bank_view(self, session):
        """Sets the underlying objective_bank view to match current view"""
        if self._objective_bank_view == FEDERATED:
            try:
                session.use_federated_objective_bank_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_objective_bank_view()
            except AttributeError:
                pass

    def _set_object_view(self, session):
        """Sets the underlying object views to match current view"""
        for obj_name in self._object_views:
            if self._object_views[obj_name] == PLENARY:
                try:
                    getattr(session, 'use_plenary_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_comparative_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _get_provider_session(self, session_name):
        """Returns the requested provider session."""
        if session_name in self._provider_sessions:
            return self._provider_sessions[session_name]
        else:
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_objective_bank')
            if self._proxy is None:
                session = session_class(self._catalog.get_id())
            else:
                session = session_class(self._catalog.get_id(), self._proxy)
            self._set_objective_bank_view(session)
            self._set_object_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[session_name] = session
            return session

    def get_objective_bank_id(self):
        """Gets the Id of this objective_bank."""
        return self._catalog_id

    def get_objective_bank(self):
        """Strange little method to assure conformance for inherited Sessions."""
        return self

    def get_objective_hierarchy_id(self):
        """WHAT am I doing here?"""
        return self._catalog_id

    def get_objective_hierarchy(self):
        """WHAT am I doing here?"""
        return self

    def __getattr__(self, name):
        if '_catalog' in self.__dict__:
            try:
                return self._catalog[name]
            except AttributeError:
                pass
        raise AttributeError

    def close_sessions(self):
        """Close all sessions currently being managed by this Manager to save memory."""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()
        raise IllegalState()

    def use_automatic_session_management(self):
        """Session state will be saved until closed by consumers."""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will always be saved and can not be closed by consumers."""
        # Session state will be saved and can not be closed by consumers
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved."""
        self._session_management = DISABLED
        self.close_sessions()

    def get_objective_bank_record(self, objective_bank_record_type):
        """Gets the objective bank record corresponding to the given ``ObjectiveBank`` record ``Type``.

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
##
# The following methods are from osid.learning.ObjectiveLookupSession

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    def can_lookup_objectives(self):
        """Tests if this user can perform ``Objective`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_objective_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_objective_view(self):
        """A complete view of the ``Objective`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include objectives in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this objective bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_objective(self, objective_id):
        """Gets the ``Objective`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Objective`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``Objective`` and retained
        for compatibility.

        :param objective_id: ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: the objective
        :rtype: ``osid.learning.Objective``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.learning.Objective

    def get_objectives_by_ids(self, objective_ids):
        """Gets an ``ObjectiveList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        objectives specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Objectives`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param objective_ids: the list of ``Ids`` to retrieve
        :type objective_ids: ``osid.id.IdList``
        :return: the returned ``Objective`` list
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``objective_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList

    def get_objectives_by_genus_type(self, objective_genus_type):
        """Gets an ``ObjectiveList`` corresponding to the given objective genus ``Type`` which does not include
        objectives of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session.

        :param objective_genus_type: an objective genus type
        :type objective_genus_type: ``osid.type.Type``
        :return: the returned ``Objective`` list
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NullArgument`` -- ``objective_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList

    def get_objectives_by_parent_genus_type(self, objective_genus_type):
        """Gets an ``ObjectiveList`` corresponding to the given objective genus ``Type`` and include any additional
        objective with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session

        :param objective_genus_type: an objective genus type
        :type objective_genus_type: ``osid.type.Type``
        :return: the returned ``Objective`` list
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NullArgument`` -- ``objective_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList

    def get_objectives_by_record_type(self, objective_record_type):
        """Gets an ``ObjectiveList`` containing the given objective record ``Type``.

        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session.

        :param objective_record_type: an objective record type
        :type objective_record_type: ``osid.type.Type``
        :return: the returned ``Objective`` list
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NullArgument`` -- ``objective_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList

    def get_objectives(self):
        """Gets all ``Objectives``.

        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session.

        :return: an ``ObjectiveList``
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList

    objectives = property(fget=get_objectives)


##
# The following methods are from osid.learning.ObjectiveQuerySession

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    def can_search_objectives(self):
        """Tests if this user can perform ``Objectives`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include objectives in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this objective bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_objective_query(self):
        """Gets an objective query.

        :return: the objective query
        :rtype: ``osid.learning.ObjectiveQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveQuery

    objective_query = property(fget=get_objective_query)

    def get_objectives_by_query(self, objective_query):
        """Gets a list of ``Objectives`` matching the given objective query.

        :param objective_query: the objective query
        :type objective_query: ``osid.learning.ObjectiveQuery``
        :return: the returned ``ObjectiveList``
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NullArgument`` -- ``objective_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``objective_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList


##
# The following methods are from osid.learning.ObjectiveAdminSession

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    def can_create_objectives(self):
        """Tests if this user can create ``Objectives``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an Objective
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Objective`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_create_objective_with_record_types(self, objective_record_types):
        """Tests if this user can create a single ``Objective`` using the desired record types.

        While ``LearningManager.getObjectiveRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Objective``.
        Providing an empty array tests if an ``Objective`` can be
        created with no records.

        :param objective_record_types: array of objective record types
        :type objective_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Objective`` creation using the specified record ``Types`` is supported, ``false``
        otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_objective_form_for_create(self, objective_record_types):
        """Gets the objective form for creating new objectives.

        A new form should be requested for each create transaction.

        :param objective_record_types: array of objective record types
        :type objective_record_types: ``osid.type.Type[]``
        :return: the objective form
        :rtype: ``osid.learning.ObjectiveForm``
        :raise: ``NullArgument`` -- ``objective_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveForm

    def create_objective(self, objective_form):
        """Creates a new ``Objective``.

        :param objective_form: the form for this ``Objective``
        :type objective_form: ``osid.learning.ObjectiveForm``
        :return: the new ``Objective``
        :rtype: ``osid.learning.Objective``
        :raise: ``IllegalState`` -- ``objective_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``objective_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``objective_form`` did not originate from ``get_objective_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.Objective

    def can_update_objectives(self):
        """Tests if this user can update ``Objectives``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Objective`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if objective modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_objective_form_for_update(self, objective_id):
        """Gets the objective form for updating an existing objective.

        A new objective form should be requested for each update
        transaction.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: the objective form
        :rtype: ``osid.learning.ObjectiveForm``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveForm

    def update_objective(self, objective_form):
        """Updates an existing objective.

        :param objective_form: the form containing the elements to be updated
        :type objective_form: ``osid.learning.ObjectiveForm``
        :raise: ``IllegalState`` -- ``objective_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``objective_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``objective_form`` did not originate from ``get_objective_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_objectives(self):
        """Tests if this user can delete ``Objectives``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Objective`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Objective`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_objective(self, objective_id):
        """Deletes the ``Objective`` identified by the given ``Id``.

        :param objective_id: the ``Id`` of the ``Objective`` to delete
        :type objective_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``Objective`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_objective_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Objectives``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Objective`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def alias_objective(self, objective_id, alias_id):
        """Adds an ``Id`` to an ``Objective`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Objective`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another objective, it is
        reassigned to the given objective ``Id``.

        :param objective_id: the ``Id`` of an ``Objective``
        :type objective_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.learning.ObjectiveHierarchySession

    def get_objective_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    objective_hierarchy_id = property(fget=get_objective_hierarchy_id)

    def get_objective_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    objective_hierarchy = property(fget=get_objective_hierarchy)

    def can_access_objective_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer traversal
        functions to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_objective_view(self):
        """The returns from the objective methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_objective_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_root_objective_ids(self):
        """Gets the root objective ``Ids`` in this hierarchy.

        :return: the root objective ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    root_objective_ids = property(fget=get_root_objective_ids)

    def get_root_objectives(self):
        """Gets the root objective in this objective hierarchy.

        :return: the root objective
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.learning.ObjectiveList

    root_objectives = property(fget=get_root_objectives)

    def has_parent_objectives(self, objective_id):
        """Tests if the ``Objective`` has any parents.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :return: ``true`` if the objective has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def is_parent_of_objective(self, id_, objective_id):
        """Tests if an ``Id`` is a direct parent of an objective.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``objective_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

    def get_parent_objective_ids(self, objective_id):
        """Gets the parent ``Ids`` of the given objective.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the objective
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_parent_objectives(self, objective_id):
        """Gets the parents of the given objective.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :return: the parents of the objective
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList

    def is_ancestor_of_objective(self, id_, objective_id):
        """Tests if an ``Id`` is an ancestor of an objective.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``objective_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

    def has_child_objectives(self, objective_id):
        """Tests if an objective has any children.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :return: ``true`` if the ``objective_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def is_child_of_objective(self, id_, objective_id):
        """Tests if an objective is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``objective_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

    def get_child_objective_ids(self, objective_id):
        """Gets the child ``Ids`` of the given objective.

        :param objective_id: the ``Id`` to query
        :type objective_id: ``osid.id.Id``
        :return: the children of the objective
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_child_objectives(self, objective_id):
        """Gets the children of the given objective.

        :param objective_id: the ``Id`` to query
        :type objective_id: ``osid.id.Id``
        :return: the children of the objective
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList

    def is_descendant_of_objective(self, id_, objective_id):
        """Tests if an ``Id`` is a descendant of an objective.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``objective_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return # boolean

    def get_objective_node_ids(self, objective_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given objective.

        :param objective_id: the ``Id`` to query
        :type objective_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
        node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
        in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a catalog node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Node

    def get_objective_nodes(self, objective_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given objective.

        :param objective_id: the ``Id`` to query
        :type objective_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
        node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
        in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an objective node
        :rtype: ``osid.learning.ObjectiveNode``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveNode


##
# The following methods are from osid.learning.ObjectiveHierarchyDesignSession

    def get_objective_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    objective_hierarchy_id = property(fget=get_objective_hierarchy_id)

    def get_objective_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    objective_hierarchy = property(fget=get_objective_hierarchy)

    def can_modify_objective_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def add_root_objective(self, objective_id):
        """Adds a root objective.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_root_objective(self, objective_id):
        """Removes a root objective.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def add_child_objective(self, objective_id, child_id):
        """Adds a child to an objective.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``objective_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_objective(self, objective_id, child_id):
        """Removes a child from an objective.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``objective_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_objectives(self, objective_id):
        """Removes all children from an objective.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.learning.ObjectiveSequencingSession

    def get_objective_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    objective_hierarchy_id = property(fget=get_objective_hierarchy_id)

    def get_objective_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    objective_hierarchy = property(fget=get_objective_hierarchy)

    def can_sequence_objectives(self):
        """Tests if this user can sequence objectives.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if sequencing objectives is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def move_objective_ahead(self, parent_objective_id, reference_objective_id, objective_id):
        """Moves an objective ahead of a refrence objective under the given parent.

        :param parent_objective_id: the ``Id`` of the parent objective
        :type parent_objective_id: ``osid.id.Id``
        :param reference_objective_id: the ``Id`` of the objective
        :type reference_objective_id: ``osid.id.Id``
        :param objective_id: the ``Id`` of the objective to move ahead of ``reference_objective_id``
        :type objective_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``parent_objective_id, reference_objective_id,`` or ``objective_id`` not found, or
        ``reference_objective_id`` or ``objective_id`` is not a child of ``parent_objective_id``
        :raise: ``NullArgument`` -- ``parent_objective_id, reference_objective_id,`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def move_objective_behind(self, parent_objective_id, reference_objective_id, objective_id):
        """Moves an objective behind a refrence objective under the given parent.

        :param parent_objective_id: the ``Id`` of the parent objective
        :type parent_objective_id: ``osid.id.Id``
        :param reference_objective_id: the ``Id`` of the objective
        :type reference_objective_id: ``osid.id.Id``
        :param objective_id: the ``Id`` of the objective to move behind ``reference_objective_id``
        :type objective_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``parent_objective_id, reference_objective_id,`` or ``objective_id`` not found, or
        ``reference_objective_id`` or ``objective_id`` is not a child of ``parent_objective_id``
        :raise: ``NullArgument`` -- ``parent_objective_id, reference_objective_id,`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def sequence_objectives(self, parent_objective_id, objective_ids):
        """Sequences a set of objectives under a parent.

        :param parent_objective_id: the ``Id`` of the parent objective
        :type parent_objective_id: ``osid.id.Id``
        :param objective_ids: the ``Id`` of the objectives
        :type objective_ids: ``osid.id.Id[]``
        :raise: ``NotFound`` -- ``parent_id`` or an ``objective_id`` not found, or an ``objective_id`` is not a child of
        ``parent_objective_id``
        :raise: ``NullArgument`` -- ``paren_objectivet_id`` or ``objective_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.learning.ObjectiveRequisiteSession

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    def can_lookup_objective_prerequisites(self):
        """Tests if this user can perform ``Objective`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_objective_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_objective_view(self):
        """A complete view of the ``Objective`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include objectives in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this objective bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_requisite_objectives(self, objective_id):
        """Gets a list of ``Objectives`` that are the immediate requisites for the given ``Objective``.

        In plenary mode, the returned list contains all of the immediate
        requisites, or an error results if an ``Objective`` is not found
        or inaccessible. Otherwise, inaccessible ``Objectives`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        :param objective_id: ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: the returned requisite ``Objectives``
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.learning.ObjectiveList

    def get_all_requisite_objectives(self, objective_id):
        """Gets a list of ``Objectives`` that are the requisites for the given ``Objective`` including the requistes of
        the requisites, and so on.

        In plenary mode, the returned list contains all of the immediate
        requisites, or an error results if an ``Objective`` is not found
        or inaccessible. Otherwise, inaccessible ``Objectives`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        :param objective_id: ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: the returned ``Objective`` list
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList

    def get_dependent_objectives(self, objective_id):
        """Gets a list of ``Objectives`` that require the given ``Objective``.

        In plenary mode, the returned list contains all of the immediate
        requisites, or an error results if an Objective is not found or
        inaccessible. Otherwise, inaccessible ``Objectives`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        :param objective_id: ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: the returned ``Objective`` list
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList

    def is_objective_required(self, objective_id, required_objective_id):
        """Tests if an objective is required before proceeding with an objective.

        One objective may indirectly depend on another objective by way
        of one or more other objectives.

        :param objective_id: ``Id`` of the dependent ``Objective``
        :type objective_id: ``osid.id.Id``
        :param required_objective_id: ``Id`` of the required ``Objective``
        :type required_objective_id: ``osid.id.Id``
        :return: ``true`` if ``objective_id`` depends on ``required_objective_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_equivalent_objectives(self, objective_id):
        """Gets a list of ``Objectives`` that are equivalent to the given ``Objective`` for the purpose of requisites.

        An equivalent objective can satisfy the given objective. In
        plenary mode, the returned list contains all of the equivalent
        requisites, or an error results if an Objective is not found or
        inaccessible. Otherwise, inaccessible ``Objectives`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        :param objective_id: ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: the returned ``Objective`` list
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveList


##
# The following methods are from osid.learning.ObjectiveRequisiteAssignmentSession

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    def can_assign_requisites(self):
        """Tests if this user can manage objective requisites.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def assign_objective_requisite(self, objective_id, requisite_objective_id):
        """Creates a requirement dependency between two ``Objectives``.

        :param objective_id: the ``Id`` of the dependent ``Objective``
        :type objective_id: ``osid.id.Id``
        :param requisite_objective_id: the ``Id`` of the required ``Objective``
        :type requisite_objective_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_id`` already mapped to ``requisite_objective_id``
        :raise: ``NotFound`` -- ``objective_id`` or ``requisite_objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` or ``requisite_objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def unassign_objective_requisite(self, objective_id, requisite_objective_id):
        """Removes an ``Objective`` requisite from an ``Objective``.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param requisite_objective_id: the ``Id`` of the required ``Objective``
        :type requisite_objective_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id`` or ``requisite_objective_id`` not found or ``objective_id`` not mapped
        to ``requisite_objective_id``
        :raise: ``NullArgument`` -- ``objective_id`` or ``requisite_objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def assign_equivalent_objective(self, objective_id, equivalent_objective_id):
        """Makes an objective equivalent to another objective for the purposes of satisfying a requisite.

        :param objective_id: the ``Id`` of the principal ``Objective``
        :type objective_id: ``osid.id.Id``
        :param equivalent_objective_id: the ``Id`` of the equivalent ``Objective``
        :type equivalent_objective_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_id`` already mapped to ``equiavelnt_objective_id``
        :raise: ``NotFound`` -- ``objective_id`` or ``equivalent_objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` or ``equivalent_objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def unassign_equivalent_objective(self, objective_id, equivalent_objective_id):
        """Removes an ``Objective`` requisite from an ``Objective``.

        :param objective_id: the ``Id`` of the principal ``Objective``
        :type objective_id: ``osid.id.Id``
        :param equivalent_objective_id: the ``Id`` of the equivalent ``Objective``
        :type equivalent_objective_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id`` or ``equivalent_objective_id`` not found or ``objective_id`` is already
        equivalent to ``equivalent_objective_id``
        :raise: ``NullArgument`` -- ``objective_id`` or ``equivalent_objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.learning.ActivityLookupSession

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    def can_lookup_activities(self):
        """Tests if this user can perform ``Activity`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_activity_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_activity_view(self):
        """A complete view of the ``Activity`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include activities in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this objective bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_activity(self, activity_id):
        """Gets the ``Activity`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Activity`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Activity`` and retained for
        compatibility.

        :param activity_id: ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :return: the activity
        :rtype: ``osid.learning.Activity``
        :raise: ``NotFound`` -- ``activity_id`` not found
        :raise: ``NullArgument`` -- ``activity_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.learning.Activity

    def get_activities_by_ids(self, activity_ids):
        """Gets an ``ActivityList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        activities specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Activities`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param activity_ids: the list of ``Ids`` to retrieve
        :type activity_ids: ``osid.id.IdList``
        :return: the returned ``Activity`` list
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``activity_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ActivityList

    def get_activities_by_genus_type(self, activity_genus_type):
        """Gets an ``ActivityList`` corresponding to the given activity genus ``Type`` which does not include activities
        of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known activities
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.

        :param activity_genus_type: an activity genus type
        :type activity_genus_type: ``osid.type.Type``
        :return: the returned ``Activity`` list
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NullArgument`` -- ``activity_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ActivityList

    def get_activities_by_parent_genus_type(self, activity_genus_type):
        """Gets an ``ActivityList`` corresponding to the given activity genus ``Type`` and include any additional
        activity with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known activities
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.

        :param activity_genus_type: an activity genus type
        :type activity_genus_type: ``osid.type.Type``
        :return: the returned ``Activity`` list
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NullArgument`` -- ``activity_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ActivityList

    def get_activities_by_record_type(self, activity_record_type):
        """Gets a ``ActivityList`` containing the given activity record ``Type``.

        In plenary mode, the returned list contains all known activities
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.

        :param activity_record_type: an activity record type
        :type activity_record_type: ``osid.type.Type``
        :return: the returned ``Activity`` list
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NullArgument`` -- ``activity_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ActivityList

    def get_activities_for_objective(self, objective_id):
        """Gets the activities for the given objective.

        In plenary mode, the returned list contains all of the
        activities mapped to the objective ``Id`` or an error results if
        an Id in the supplied list is not found or inaccessible.
        Otherwise, inaccessible ``Activities`` may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :param objective_id: ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: list of enrollments
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.learning.ActivityList

    def get_activities_for_objectives(self, objective_ids):
        """Gets the activities for the given objectives.

        In plenary mode, the returned list contains all of the
        activities specified in the objective ``Id`` list, in the order
        of the list, including duplicates, or an error results if a
        course offering ``Id`` in the supplied list is not found or
        inaccessible. Otherwise, inaccessible ``Activities`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        :param objective_ids: list of objective ``Ids``
        :type objective_ids: ``osid.id.IdList``
        :return: list of activities
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NotFound`` -- an ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id_list`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.learning.ActivityList

    def get_activities_by_asset(self, asset_id):
        """Gets the activities for the given asset.

        In plenary mode, the returned list contains all of the
        activities mapped to the asset ``Id`` or an error results if an
        ``Id`` in the supplied list is not found or inaccessible.
        Otherwise, inaccessible ``Activities`` may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :param asset_id: ``Id`` of an ``Asset``
        :type asset_id: ``osid.id.Id``
        :return: list of activities
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NotFound`` -- ``asset_id`` not found
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.learning.ActivityList

    def get_activities_by_assets(self, asset_ids):
        """Gets the activities for the given asset.

        In plenary mode, the returned list contains all of the
        activities mapped to the asset ``Id`` or an error results if an
        ``Id`` in the supplied list is not found or inaccessible.
        Otherwise, inaccessible ``Activities`` may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :param asset_ids: ``Ids`` of ``Assets``
        :type asset_ids: ``osid.id.IdList``
        :return: list of activities
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NotFound`` -- an ``asset_id`` not found
        :raise: ``NullArgument`` -- ``asset_id_list`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.learning.ActivityList

    def get_activities(self):
        """Gets all ``Activities``.

        In plenary mode, the returned list contains all known activites
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.

        :return: a ``ActivityList``
        :rtype: ``osid.learning.ActivityList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ActivityList

    activities = property(fget=get_activities)


##
# The following methods are from osid.learning.ActivityAdminSession

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    def can_create_activities(self):
        """Tests if this user can create ``Activities``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``Activity`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Activity`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_create_activity_with_record_types(self, activity_record_types):
        """Tests if this user can create a single ``Activity`` using the desired record types.

        While ``LearningManager.getActivityRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Activity``.
        Providing an empty array tests if an ``Activity`` can be created
        with no records.

        :param activity_record_types: array of activity record types
        :type activity_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Activity`` creation using the specified record ``Types`` is supported, ``false``
        otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``activity_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_activity_form_for_create(self, objective_id, activity_record_types):
        """Gets the activity form for creating new activities.

        A new form should be requested for each create transaction.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param activity_record_types: array of activity record types
        :type activity_record_types: ``osid.type.Type[]``
        :return: the activity form
        :rtype: ``osid.learning.ActivityForm``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` or ``activity_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ActivityForm

    def create_activity(self, activity_form):
        """Creates a new ``Activity``.

        :param activity_form: the form for this ``Activity``
        :type activity_form: ``osid.learning.ActivityForm``
        :return: the new ``Activity``
        :rtype: ``osid.learning.Activity``
        :raise: ``IllegalState`` -- ``activity_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``activity_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``activity_form`` did not originate from ``get_activity_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.Activity

    def can_update_activities(self):
        """Tests if this user can update ``Activities``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Activity`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if activity modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_activity_form_for_update(self, activity_id):
        """Gets the activity form for updating an existing activity.

        A new activity form should be requested for each update
        transaction.

        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :return: the activity form
        :rtype: ``osid.learning.ActivityForm``
        :raise: ``NotFound`` -- ``activity_id`` is not found
        :raise: ``NullArgument`` -- ``activity_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ActivityForm

    def update_activity(self, activity_form):
        """Updates an existing activity,.

        :param activity_form: the form containing the elements to be updated
        :type activity_form: ``osid.learning.ActivityForm``
        :raise: ``IllegalState`` -- ``activity_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``activity_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``activity_form`` did not originate from ``get_activity_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_activities(self):
        """Tests if this user can delete ``Activities``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Activity`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Activity`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_activity(self, activity_id):
        """Deletes the ``Activity`` identified by the given ``Id``.

        :param activity_id: the ``Id`` of the ``Activity`` to delete
        :type activity_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``Activity`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``activity_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_activity_aliases(self):
        """Tests if this user can manage ``Id`` aliases for activities.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Activity`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def alias_activity(self, activity_id, alias_id):
        """Adds an ``Id`` to an ``Activity`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Activity`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another activity, it is
        reassigned to the given activity ``Id``.

        :param activity_id: the ``Id`` of an ``Activity``
        :type activity_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``activity_id`` not found
        :raise: ``NullArgument`` -- ``activity_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




class ObjectiveBankList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ObjectiveBankList`` provides a means for accessing ``ObjectiveBank`` elements
        sequentially
        either one at a time or many at a time.

    Examples: while (obl.hasNext()) { ObjectiveBank objectiveBanks =
    obl.getNextObjectiveBank(); }

    or
      while (obl.hasNext()) {
           ObjectiveBank[] objectivBanks = obl.getNextObjectiveBanks(obl.available());
      }


    """

    def get_next_objective_bank(self):
        """Gets the next ``ObjectiveBank`` in this list.

        :return: the next ``ObjectiveBank`` in this list. The ``has_next()`` method should be used to test that a next
        ``ObjectiveBank`` is available before calling this method.
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBank

    next_objective_bank = property(fget=get_next_objective_bank)

    def get_next_objective_banks(self, n):
        """Gets the next set of ``ObjectiveBank`` elements in this list which must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``ObjectiveBank`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``ObjectiveBank`` elements.The length of the array is less than or equal to the number
        specified.
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.learning.ObjectiveBank


