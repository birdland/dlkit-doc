# -*- coding: utf-8 -*-
"""Assessment Open Service Interface Definitions
assessment version 3.0.0

The Assessment OSID provides the means to create, access, and take
assessments. An ``Assessment`` may represent a quiz, survey, or other
evaluation that includes assessment ``Items``. The OSID defines methods
to describe the flow of control and the relationships among the objects.
Assessment ``Items`` are extensible objects to capture various types of
questions, such as a multiple choice or an asset submission.

The Assessment service can br broken down into several distinct
services:

  * Assessment Taking
  * Assessment and Item authoring
  * Accessing and managing banks of assessments and items


Each of these service areas are covered by different session and object
interfaces. The object interfaces describe both the structure of the
assessment and follow an assessment management workflow of first
defining assessment items and then authoring assessments based on those
items. They are:

  * ``Item`` : a question and answer pair
  * ``Response:`` a response to an ``Item`` question
  * ``Assessment`` : a set of ``Items``
  * ``AssessmentSection:`` A grouped set of ``Items``
  * ``AssessmentOffering:`` An ``Assessment`` available for taking
  * ``AssessmentTaken:`` An ``AssessmentOffering`` that has been
    completed or in progress


Taking Assessments

The ``AssessmentSession`` is used to take an assessment. It captures
various ways an assessment can be taken which may include time
constraints, the ability to suspend and resume, and the availability of
an answer.

Taking an ``Assessment`` involves first navigating through
``AssessmentSections``. An ``AssessmentSection`` is an advanced
authoring construct used to both visually divide an ``Assessment`` and
impose additional constraints. Basic assessments are assumed to always
have one ``AssessmentSection`` even if not explicitly created.

Authoring

A basic authoring session is available in this package to map ``Items``
to ``Assessments``. More sophisticated authoring using
``AssessmentParts`` and sequencing is available in the Assessment
Authoring OSID.

Bank Cataloging

``Assessments,``  ``AssessmentsOffered,``  ``AssessmentsTaken,`` and
``Items`` may be organized into federateable catalogs called ``Banks`` .

Sub Packages

The Assessment OSID includes an Assessment Authoring OSID for more
advanced authoring and sequencing options.

"""
from ..osid import managers as osid_managers
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class AssessmentProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_my_assessment_taken(self):
        """Tests if a session is available to lookup taken assessments for the authenticated agent.

        :return: ``true`` if my assessment taken session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment(self):
        """Tests for the availability of a assessment service which is the service for taking and examining assessments taken.

        :return: ``true`` if assessment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_results(self):
        """Tests for the availability of an assessment rsults service.

        :return: ``true`` if assessment results is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_item_lookup(self):
        """Tests if an item lookup service is supported.

        :return: true if item lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_item_query(self):
        """Tests if an item query service is supported.

        :return: ``true`` if item query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_item_search(self):
        """Tests if an item search service is supported.

        :return: ``true`` if item search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_item_admin(self):
        """Tests if an item administrative service is supported.

        :return: ``true`` if item admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_item_notification(self):
        """Tests if item notification is supported.
        Messages may be sent when items are created, modified, or
        deleted.

        :return: ``true`` if item notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_item_bank(self):
        """Tests if an item to bank lookup session is available.

        :return: ``true`` if item bank lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_item_bank_assignment(self):
        """Tests if an item to bank assignment session is available.

        :return: ``true`` if item bank assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_item_smart_bank(self):
        """Tests if an item smart bank session is available.

        :return: ``true`` if item smart bank session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_lookup(self):
        """Tests if an assessment lookup service is supported.
        An assessment lookup service defines methods to access
        assessments.

        :return: true if assessment lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_query(self):
        """Tests if an assessment query service is supported.

        :return: ``true`` if assessment query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_search(self):
        """Tests if an assessment search service is supported.

        :return: ``true`` if assessment search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_admin(self):
        """Tests if an assessment administrative service is supported.

        :return: ``true`` if assessment admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_notification(self):
        """Tests if assessment notification is supported.
        Messages may be sent when assessments are created, modified, or
        deleted.

        :return: ``true`` if assessment notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_bank(self):
        """Tests if an assessment to bank lookup session is available.

        :return: ``true`` if assessment bank lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_bank_assignment(self):
        """Tests if an assessment to bank assignment session is available.

        :return: ``true`` if assessment bank assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_smart_bank(self):
        """Tests if an assessment smart bank session is available.

        :return: ``true`` if assessment smart bank session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_basic_authoring(self):
        """Tests if an assessment basic authoring session is available.

        :return: ``true`` if assessment basic authoring is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_offered_lookup(self):
        """Tests if an assessment offered lookup service is supported.

        :return: true if assessment offered lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_offered_query(self):
        """Tests if an assessment offered query service is supported.

        :return: ``true`` if assessment offered query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_offered_search(self):
        """Tests if an assessment offered search service is supported.

        :return: ``true`` if assessment offered search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_offered_admin(self):
        """Tests if an assessment offered administrative service is supported.

        :return: ``true`` if assessment offered admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_offered_notification(self):
        """Tests if assessment offered notification is supported.
        Messages may be sent when offered assessments are created,
        modified, or deleted.

        :return: ``true`` if assessment offered notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_offered_bank(self):
        """Tests if an assessment offered to bank lookup session is available.

        :return: ``true`` if assessment offered bank lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_offered_bank_assignment(self):
        """Tests if an assessment offered to bank assignment session is available.

        :return: ``true`` if assessment offered bank assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_offered_smart_bank(self):
        """Tests if an assessment offered smart bank session is available.

        :return: ``true`` if assessment offered smart bank session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_taken_lookup(self):
        """Tests if an assessment taken lookup service is supported.

        :return: ``true`` if assessment taken lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_taken_query(self):
        """Tests if an assessment taken query service is supported.

        :return: ``true`` if assessment taken query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_taken_search(self):
        """Tests if an assessment taken search service is supported.

        :return: ``true`` if assessment taken search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_taken_admin(self):
        """Tests if an assessment taken administrative service is supported which is used to instantiate an assessment offered.

        :return: ``true`` if assessment taken admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_taken_notification(self):
        """Tests if assessment taken notification is supported.
        Messages may be sent when items are created, modified, or
        deleted.

        :return: ``true`` if assessment taken notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_taken_bank(self):
        """Tests if an assessment taken to bank lookup session is available.

        :return: ``true`` if assessment taken bank lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_taken_bank_assignment(self):
        """Tests if an assessment taken to bank assignment session is available.

        :return: ``true`` if assessment taken bank assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_taken_smart_bank(self):
        """Tests if an assessment taken smart bank session is available.

        :return: ``true`` if assessment taken smart bank session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_bank_lookup(self):
        """Tests if a bank lookup service is supported.
        A bank lookup service defines methods to access assessment
        banks.

        :return: ``true`` if bank lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_bank_query(self):
        """Tests if a bank query service is supported.

        :return: ``true`` if bank query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_bank_search(self):
        """Tests if a bank search service is supported.

        :return: ``true`` if bank search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_bank_admin(self):
        """Tests if a banlk administrative service is supported.

        :return: ``true`` if bank admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_bank_notification(self):
        """Tests if bank notification is supported.
        Messages may be sent when items are created, modified, or
        deleted.

        :return: ``true`` if bank notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_bank_hierarchy(self):
        """Tests if a bank hierarchy traversal is supported.

        :return: ``true`` if a bank hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_bank_hierarchy_design(self):
        """Tests if bank hierarchy design is supported.

        :return: ``true`` if a bank hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_authoring(self):
        """Tests if an assessment authoring service is supported.

        :return: ``true`` if an assessment authoring is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_assessment_batch(self):
        """Tests if an assessment batch service is supported.

        :return: ``true`` if an assessment batch service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_item_record_types(self):
        """Gets the supported ``Item`` record types.

        :return: a list containing the supported ``Item`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    item_record_types = property(fget=get_item_record_types)

    def supports_item_record_type(self, item_record_type):
        """Tests if the given ``Item`` record type is supported.

        :param item_record_type: a ``Type`` indicating a ``Item`` record type
        :type item_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``item_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_item_search_record_types(self):
        """Gets the supported ``Item`` search record types.

        :return: a list containing the supported ``Item`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    item_search_record_types = property(fget=get_item_search_record_types)

    def supports_item_search_record_type(self, item_search_record_type):
        """Tests if the given ``Item`` search record type is supported.

        :param item_search_record_type: a ``Type`` indicating an ``Item`` search record type
        :type item_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``item_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assessment_record_types(self):
        """Gets the supported ``Assessment`` record types.

        :return: a list containing the supported ``Assessment`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    assessment_record_types = property(fget=get_assessment_record_types)

    def supports_assessment_record_type(self, assessment_record_type):
        """Tests if the given ``Assessment`` record type is supported.

        :param assessment_record_type: a ``Type`` indicating an ``Assessment`` record type
        :type assessment_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assessment_search_record_types(self):
        """Gets the supported ``Assessment`` search record types.

        :return: a list containing the supported assessment search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    assessment_search_record_types = property(fget=get_assessment_search_record_types)

    def supports_assessment_search_record_type(self, assessment_search_record_type):
        """Tests if the given assessment search record type is supported.

        :param assessment_search_record_type: a ``Type`` indicating an assessment search record type
        :type assessment_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_record_types(self):
        """Gets the supported ``AssessmentOffered`` record types.

        :return: a list containing the supported ``AssessmentOffered`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    assessment_offered_record_types = property(fget=get_assessment_offered_record_types)

    def supports_assessment_offered_record_type(self, assessment_offered_record_type):
        """Tests if the given ``AssessmentOffered`` record type is supported.

        :param assessment_offered_record_type: a ``Type`` indicating an ``AssessmentOffered`` record type
        :type assessment_offered_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_offered_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_search_record_types(self):
        """Gets the supported ``AssessmentOffered`` search record types.

        :return: a list containing the supported ``AssessmentOffered`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    assessment_offered_search_record_types = property(fget=get_assessment_offered_search_record_types)

    def supports_assessment_offered_search_record_type(self, assessment_offered_search_record_type):
        """Tests if the given ``AssessmentOffered`` search record type is supported.

        :param assessment_offered_search_record_type: a ``Type`` indicating an ``AssessmentOffered`` search record type
        :type assessment_offered_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_offered_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_record_types(self):
        """Gets the supported ``AssessmentTaken`` record types.

        :return: a list containing the supported ``AssessmentTaken`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    assessment_taken_record_types = property(fget=get_assessment_taken_record_types)

    def supports_assessment_taken_record_type(self, assessment_taken_record_type):
        """Tests if the given ``AssessmentTaken`` record type is supported.

        :param assessment_taken_record_type: a ``Type`` indicating an ``AssessmentTaken`` record type
        :type assessment_taken_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_taken_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_search_record_types(self):
        """Gets the supported ``AssessmentTaken`` search record types.

        :return: a list containing the supported ``AssessmentTaken`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    assessment_taken_search_record_types = property(fget=get_assessment_taken_search_record_types)

    def supports_assessment_taken_search_record_type(self, assessment_taken_search_record_type):
        """Tests if the given ``AssessmentTaken`` search record type is supported.

        :param assessment_taken_search_record_type: a ``Type`` indicating an ``AssessmentTaken`` search record type
        :type assessment_taken_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_taken_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assessment_section_record_types(self):
        """Gets the supported ``AssessmentSection`` record types.

        :return: a list containing the supported ``AssessmentSection`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    assessment_section_record_types = property(fget=get_assessment_section_record_types)

    def supports_assessment_section_record_type(self, assessment_section_record_type):
        """Tests if the given ``AssessmentSection`` record type is supported.

        :param assessment_section_record_type: a ``Type`` indicating an ``AssessmentSection`` record type
        :type assessment_section_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_section_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_bank_record_types(self):
        """Gets the supported ``Bank`` record types.

        :return: a list containing the supported ``Bank`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    bank_record_types = property(fget=get_bank_record_types)

    def supports_bank_record_type(self, bank_record_type):
        """Tests if the given ``Bank`` record type is supported.

        :param bank_record_type: a ``Type`` indicating a ``Bank`` type
        :type bank_record_type: ``osid.type.Type``
        :return: ``true`` if the given key record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_bank_search_record_types(self):
        """Gets the supported bank search record types.

        :return: a list containing the supported ``Bank`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    bank_search_record_types = property(fget=get_bank_search_record_types)

    def supports_bank_search_record_type(self, bank_search_record_type):
        """Tests if the given bank search record type is supported.

        :param bank_search_record_type: a ``Type`` indicating a ``Bank`` search record type
        :type bank_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class AssessmentManager(osid_managers.OsidManager, osid_sessions.OsidSession, AssessmentProfile):

    def get_my_assessment_taken_session(self):
        """Gets a ``MyAssessmentTakenSession`` to retrieve assessments taken for the current agent.

        :return: a ``MyAssessmentTakenSession``
        :rtype: ``osid.assessment.MyAssessmentTakenSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_assessment_taken()`` is ``false``

        """
        raise UNIMPLEMENTED()

    my_assessment_taken_session = property(fget=get_my_assessment_taken_session)

    def get_my_assessment_taken_session_for_bank(self, bank_id):
        """Gets a ``MyAssessmentTakenSession`` to retrieve assessments taken for the current agent for the given bank ``Id``.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: a ``MyAssessmentTakenSession``
        :rtype: ``osid.assessment.MyAssessmentTakenSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_assessment_taken()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_session(self):
        """Gets an ``AssessmentSession`` which is responsible for taking assessments and examining responses from assessments taken.

        :return: an assessment session for this service
        :rtype: ``osid.assessment.AssessmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_session = property(fget=get_assessment_session)

    def get_assessment_session_for_bank(self, bank_id):
        """Gets an ``AssessmentSession`` which is responsible for performing assessments for the given bank ``Id``.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: an assessment session for this service
        :rtype: ``osid.assessment.AssessmentSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_results_session(self):
        """Gets an ``AssessmentResultsSession`` to retrieve assessment results.

        :return: an assessment results session for this service
        :rtype: ``osid.assessment.AssessmentResultsSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_results()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_results_session = property(fget=get_assessment_results_session)

    def get_assessment_results_session_for_bank(self, bank_id):
        """Gets an ``AssessmentResultsSession`` to retrieve assessment results for the given bank.

        :param bank_id: the ``Id`` of the assessment taken
        :type bank_id: ``osid.id.Id``
        :return: an assessment results session for this service
        :rtype: ``osid.assessment.AssessmentResultsSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_results()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_lookup_session(self):
        """Gets the ``OsidSession`` associated with the item lookup service.

        :return: an ``ItemLookupSession``
        :rtype: ``osid.assessment.ItemLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    item_lookup_session = property(fget=get_item_lookup_session)

    def get_item_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the item lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _item_lookup_session``
        :rtype: ``osid.assessment.ItemLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_query_session(self):
        """Gets the ``OsidSession`` associated with the item query service.

        :return: an ``ItemQuerySession``
        :rtype: ``osid.assessment.ItemQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    item_query_session = property(fget=get_item_query_session)

    def get_item_query_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the item query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _item_query_session``
        :rtype: ``osid.assessment.ItemQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_search_session(self):
        """Gets the ``OsidSession`` associated with the item search service.

        :return: an ``ItemSearchSession``
        :rtype: ``osid.assessment.ItemSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    item_search_session = property(fget=get_item_search_session)

    def get_item_search_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the item search service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _item_search_session``
        :rtype: ``osid.assessment.ItemSearchSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_admin_session(self):
        """Gets the ``OsidSession`` associated with the item administration service.

        :return: an ``ItemAdminSession``
        :rtype: ``osid.assessment.ItemAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    item_admin_session = property(fget=get_item_admin_session)

    def get_item_admin_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the item admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _item_admin_session``
        :rtype: ``osid.assessment.ItemAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_notification_session(self, item_receiver):
        """Gets the notification session for notifications pertaining to item changes.

        :param item_receiver: the item receiver interface
        :type item_receiver: ``osid.assessment.ItemReceiver``
        :return: an ``ItemNotificationSession``
        :rtype: ``osid.assessment.ItemNotificationSession``
        :raise: ``NullArgument`` -- ``item_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_notification_session_for_bank(self, item_receiver, bank_id):
        """Gets the ``OsidSession`` associated with the item notification service for the given bank.

        :param item_receiver: the item receiver interface
        :type item_receiver: ``osid.assessment.ItemReceiver``
        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _item_notification_session``
        :rtype: ``osid.assessment.AssessmentNotificationSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``item_receiver`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_bank_session(self):
        """Gets the ``OsidSession`` associated with the item banking service.

        :return: an ``ItemBankSession``
        :rtype: ``osid.assessment.ItemBankSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_bank()`` is ``false``

        """
        raise UNIMPLEMENTED()

    item_bank_session = property(fget=get_item_bank_session)

    def get_item_bank_assignment_session(self):
        """Gets the ``OsidSession`` associated with the item bank assignment service.

        :return: an ``ItemBankAssignmentSession``
        :rtype: ``osid.assessment.ItemBankAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_bank_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    item_bank_assignment_session = property(fget=get_item_bank_assignment_session)

    def get_item_smart_bank_session(self, bank_id):
        """Gets the ``OsidSession`` associated with the item smart banking service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``ItemSmartBankSession``
        :rtype: ``osid.assessment.ItemSmartBankSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_smart_bank()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_lookup_session(self):
        """Gets the ``OsidSession`` associated with the assessment lookup service.

        :return: an ``AssessmentLookupSession``
        :rtype: ``osid.assessment.AssessmentLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_lookup_session = property(fget=get_assessment_lookup_session)

    def get_assessment_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _assessment_lookup_session``
        :rtype: ``osid.assessment.AssessmentLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_query_session(self):
        """Gets the ``OsidSession`` associated with the assessment query service.

        :return: an ``AssessmentQuerySession``
        :rtype: ``osid.assessment.AssessmentQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_query_session = property(fget=get_assessment_query_session)

    def get_assessment_query_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _assessment_query_session``
        :rtype: ``osid.assessment.AssessmentQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_search_session(self):
        """Gets the ``OsidSession`` associated with the assessment search service.

        :return: an ``AssessmentSearchSession``
        :rtype: ``osid.assessment.AssessmentSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_search_session = property(fget=get_assessment_search_session)

    def get_assessment_search_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment search service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _assessment_search_session``
        :rtype: ``osid.assessment.AssessmentSearchSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_admin_session(self):
        """Gets the ``OsidSession`` associated with the assessment administration service.

        :return: an ``AssessmentAdminSession``
        :rtype: ``osid.assessment.AssessmentAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_admin_session = property(fget=get_assessment_admin_session)

    def get_assessment_admin_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _assessment_admin_session``
        :rtype: ``osid.assessment.AssessmentAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_notification_session(self, assessment_receiver):
        """Gets the notification session for notifications pertaining to assessment changes.

        :param assessment_receiver: the assessment receiver interface
        :type assessment_receiver: ``osid.assessment.AssessmentReceiver``
        :return: an ``AssessmentNotificationSession``
        :rtype: ``osid.assessment.AssessmentNotificationSession``
        :raise: ``NullArgument`` -- ``assessment_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_notification_session_for_bank(self, assessment_receiver, bank_id):
        """Gets the ``OsidSession`` associated with the assessment notification service for the given bank.

        :param assessment_receiver: the assessment receiver interface
        :type assessment_receiver: ``osid.assessment.AssessmentReceiver``
        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: ``an _assessment_notification_session``
        :rtype: ``osid.assessment.AssessmentNotificationSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``assessment_receiver`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_bank_session(self):
        """Gets the ``OsidSession`` associated with the assessment banking service.

        :return: an ``AssessmentBankSession``
        :rtype: ``osid.assessment.AssessmentBankSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_bank()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_bank_session = property(fget=get_assessment_bank_session)

    def get_assessment_bank_assignment_session(self):
        """Gets the ``OsidSession`` associated with the assessment bank assignment service.

        :return: an ``AssessmentBankAssignmentSession``
        :rtype: ``osid.assessment.AssessmentBankAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_bank_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_bank_assignment_session = property(fget=get_assessment_bank_assignment_session)

    def get_assessment_smart_bank_session(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment smart banking service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentSmartBankSession``
        :rtype: ``osid.assessment.AssessmentSmartBankSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_smart_bank()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_basic_authoring_session(self):
        """Gets the ``OsidSession`` associated with the assessment authoring service.

        :return: an ``AssessmentBasicAuthoringSession``
        :rtype: ``osid.assessment.AssessmentBasicAuthoringSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_basic_authoring()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_basic_authoring_session = property(fget=get_assessment_basic_authoring_session)

    def get_assessment_basic_authoring_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment authoring service for the given bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentBasicAuthoringSession``
        :rtype: ``osid.assessment.AssessmentBasicAuthoringSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_basic_authoring()`` or ``supports_visibe_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_lookup_session(self):
        """Gets the ``OsidSession`` associated with the assessment offered lookup service.

        :return: an ``AssessmentOfferedLookupSession``
        :rtype: ``osid.assessment.AssessmentOfferedLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_offered_lookup_session = property(fget=get_assessment_offered_lookup_session)

    def get_assessment_offered_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment offered lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentOfferedLookupSession``
        :rtype: ``osid.assessment.AssessmentOfferedLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_query_session(self):
        """Gets the ``OsidSession`` associated with the assessment offered query service.

        :return: an ``AssessmentOfferedQuerySession``
        :rtype: ``osid.assessment.AssessmentOfferedQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_offered_query_session = property(fget=get_assessment_offered_query_session)

    def get_assessment_offered_query_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment offered query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentOfferedQuerySession``
        :rtype: ``osid.assessment.AssessmentOfferedQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_search_session(self):
        """Gets the ``OsidSession`` associated with the assessment offered search service.

        :return: an ``AssessmentOfferedSearchSession``
        :rtype: ``osid.assessment.AssessmentOfferedSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_offered_search_session = property(fget=get_assessment_offered_search_session)

    def get_assessment_offered_search_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment offered search service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentOfferedSearchSession``
        :rtype: ``osid.assessment.AssessmentOfferedSearchSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_admin_session(self):
        """Gets the ``OsidSession`` associated with the assessment offered administration service.

        :return: an ``AssessmentOfferedAdminSession``
        :rtype: ``osid.assessment.AssessmentOfferedAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_offered_admin_session = property(fget=get_assessment_offered_admin_session)

    def get_assessment_offered_admin_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment offered admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentOfferedAdminSession``
        :rtype: ``osid.assessment.AssessmentOfferedAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_notification_session(self, assessment_offered_receiver):
        """Gets the notification session for notifications pertaining to offered assessment changes.

        :param assessment_offered_receiver: the assessment offered receiver interface
        :type assessment_offered_receiver: ``osid.assessment.AssessmentOfferedReceiver``
        :return: an ``AssessmentOfferedNotificationSession``
        :rtype: ``osid.assessment.AssessmentOfferedNotificationSession``
        :raise: ``NullArgument`` -- ``assessment_offered_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_notification_session_for_bank(self, assessment_offered_receiver, bank_id):
        """Gets the ``OsidSession`` associated with the offered assessment notification service for the given bank.

        :param assessment_offered_receiver: the assessment offered receiver interface
        :type assessment_offered_receiver: ``osid.assessment.AssessmentOfferedReceiver``
        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: a ``AssessmentOfferedNotificationSession``
        :rtype: ``osid.assessment.AssessmentOfferedNotificationSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``assessment_offered_receiver`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_bank_session(self):
        """Gets the session for retrieving offered assessments to bank mappings.

        :return: an ``AssessmentOfferedBankSession``
        :rtype: ``osid.assessment.AssessmentOfferedBankSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_bank()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_offered_bank_session = property(fget=get_assessment_offered_bank_session)

    def get_assessment_offered_bank_assignment_session(self):
        """Gets the session for assigning offered assessments to bank mappings.

        :return: an ``AssessmentOfferedBankAssignmentSession``
        :rtype: ``osid.assessment.AssessmentOfferedBankAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_bank_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_offered_bank_assignment_session = property(fget=get_assessment_offered_bank_assignment_session)

    def get_assessment_offered_smart_bank_session(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment offered smart banking service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentOfferedSmartBankSession``
        :rtype: ``osid.assessment.AssessmentOfferedSmartBankSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_smart_bank()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_lookup_session(self):
        """Gets the ``OsidSession`` associated with the assessment taken lookup service.

        :return: an ``AssessmentTakenLookupSession``
        :rtype: ``osid.assessment.AssessmentTakenLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_taken_lookup_session = property(fget=get_assessment_taken_lookup_session)

    def get_assessment_taken_lookup_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment taken lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentTakenLookupSession``
        :rtype: ``osid.assessment.AssessmentTakenLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_query_session(self):
        """Gets the ``OsidSession`` associated with the assessment taken query service.

        :return: an ``AssessmentTakenQuerySession``
        :rtype: ``osid.assessment.AssessmentTakenQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_taken_query_session = property(fget=get_assessment_taken_query_session)

    def get_assessment_taken_query_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment taken query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentTakenQuerySession``
        :rtype: ``osid.assessment.AssessmentTakenQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_search_session(self):
        """Gets the ``OsidSession`` associated with the assessment taken search service.

        :return: an ``AssessmentTakenSearchSession``
        :rtype: ``osid.assessment.AssessmentTakenSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    assessment_taken_search_session = property(fget=get_assessment_taken_search_session)

    def get_assessment_taken_search_session_for_bank(self, bank_id):
        """Gets the ``OsidSession`` associated with the assessment taken search service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentTakenSearchSession``
        :rtype: ``osid.assessment.AssessmentTakenSearchSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_notification_session(self, assessment_taken_receiver):
        """Gets the notification session for notifications pertaining to taken assessment changes.

        :param assessment_taken_receiver: the assessment taken receiver interface
        :type assessment_taken_receiver: ``osid.assessment.AssessmentTakenReceiver``
        :return: an ``AssessmentTakenNotificationSession``
        :rtype: ``osid.assessment.AssessmentTakenNotificationSession``
        :raise: ``NullArgument`` -- ``assessment_taken_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_notification_session_for_bank(self, assessment_taken_receiver, bank_id):
        """Gets the ``OsidSession`` associated with the taken assessment notification service for the given bank.

        :param assessment_taken_receiver: the assessment taken receiver interface
        :type assessment_taken_receiver: ``osid.assessment.AssessmentTakenReceiver``
        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :return: an ``AssessmentTakenNotificationSession``
        :rtype: ``osid.assessment.AssessmentTakenNotificationSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``assessment_taken_receiver`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_bank_lookup_session(self):
        """Gets the OsidSession associated with the bank lookup service.

        :return: a ``BankLookupSession``
        :rtype: ``osid.assessment.BankLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_lookup() is false``

        """
        raise UNIMPLEMENTED()

    bank_lookup_session = property(fget=get_bank_lookup_session)

    def get_bank_query_session(self):
        """Gets the OsidSession associated with the bank query service.

        :return: a ``BankQuerySession``
        :rtype: ``osid.assessment.BankQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_query() is false``

        """
        raise UNIMPLEMENTED()

    bank_query_session = property(fget=get_bank_query_session)

    def get_bank_search_session(self):
        """Gets the OsidSession associated with the bank search service.

        :return: a ``BankSearchSession``
        :rtype: ``osid.assessment.BankSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_search() is false``

        """
        raise UNIMPLEMENTED()

    bank_search_session = property(fget=get_bank_search_session)

    def get_bank_admin_session(self):
        """Gets the OsidSession associated with the bank administration service.

        :return: a ``BankAdminSession``
        :rtype: ``osid.assessment.BankAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_admin() is false``

        """
        raise UNIMPLEMENTED()

    bank_admin_session = property(fget=get_bank_admin_session)

    def get_bank_notification_session(self, bankreceiver):
        """Gets the notification session for notifications pertaining to bank service changes.

        :param bankreceiver: the bank receiver interface
        :type bankreceiver: ``osid.assessment.BankReceiver``
        :return: a ``BankNotificationSession``
        :rtype: ``osid.assessment.BankNotificationSession``
        :raise: ``NullArgument`` -- ``bank_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_notification() is false``

        """
        raise UNIMPLEMENTED()

    def get_bank_hierarchy_session(self):
        """Gets the session traversing bank hierarchies.

        :return: a ``BankHierarchySession``
        :rtype: ``osid.assessment.BankHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_hierarchy() is false``

        """
        raise UNIMPLEMENTED()

    bank_hierarchy_session = property(fget=get_bank_hierarchy_session)

    def get_bank_hierarchy_design_session(self):
        """Gets the session designing bank hierarchies.

        :return: a ``BankHierarchySession``
        :rtype: ``osid.assessment.BankHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_hierarchy_design() is false``

        """
        raise UNIMPLEMENTED()

    bank_hierarchy_design_session = property(fget=get_bank_hierarchy_design_session)

    def get_assessment_authoring_manager(self):
        """Gets an ``AssessmentAuthoringManager``.

        :return: an ``AssessmentAuthoringManager``
        :rtype: ``osid.assessment.authoring.AssessmentAuthoringManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_authoring() is false``

        """
        raise UNIMPLEMENTED()

    assessment_authoring_manager = property(fget=get_assessment_authoring_manager)

    def get_assessment_batch_manager(self):
        """Gets an ``AssessmentBatchManager``.

        :return: an ``AssessmentBatchManager``
        :rtype: ``osid.assessment.batch.AssessmentBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_batch() is false``

        """
        raise UNIMPLEMENTED()

    assessment_batch_manager = property(fget=get_assessment_batch_manager)


##
# The following methods are from osid.assessment.BankLookupSession

    def can_lookup_banks(self):
        """Tests if this user can perform ``Bank`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_bank_view(self):
        """A complete view of the ``Bank`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_bank(self, bank_id):
        """Gets the ``Bank`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Bank`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Bank`` and retained for compatibility.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_banks_by_ids(self, bank_ids):
        """Gets a ``BankList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the banks
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Bank`` objects may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param bank_ids: the list of ``Ids`` to retrieve
        :type bank_ids: ``osid.id.IdList``
        :return: the returned ``Bank`` list
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_banks_by_genus_type(self, bank_genus_type):
        """Gets a ``BankList`` corresponding to the given bank genus ``Type`` which does not include banks of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :param bank_genus_type: a bank genus type
        :type bank_genus_type: ``osid.type.Type``
        :return: the returned ``Bank`` list
        :rtype: ``osid.assessment.BankList``
        :raise: ``NullArgument`` -- ``bank_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_banks_by_parent_genus_type(self, bank_genus_type):
        """Gets a ``BankList`` corresponding to the given bank genus ``Type`` and include any additional banks with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :param bank_genus_type: a bank genus type
        :type bank_genus_type: ``osid.type.Type``
        :return: the returned ``Bank`` list
        :rtype: ``osid.assessment.BankList``
        :raise: ``NullArgument`` -- ``bank_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_banks_by_record_type(self, bank_record_type):
        """Gets a ``BankList`` containing the given bank record ``Type``.
        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :param bank_record_type: a bank record type
        :type bank_record_type: ``osid.type.Type``
        :return: the returned ``Bank`` list
        :rtype: ``osid.assessment.BankList``
        :raise: ``NullArgument`` -- ``bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_banks_by_provider(self, resource_id):
        """Gets a ``BankList`` from the given provider ````.
        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Bank`` list
        :rtype: ``osid.assessment.BankList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_banks(self):
        """Gets all ``Banks``.
        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.

        :return: a ``BankList``
        :rtype: ``osid.assessment.BankList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    banks = property(fget=get_banks)


##
# The following methods are from osid.assessment.BankQuerySession

    def can_search_banks(self):
        """Tests if this user can perform ``Bank`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_bank_query(self):
        """Gets a bank query.

        :return: a bank query
        :rtype: ``osid.assessment.BankQuery``

        """
        raise UNIMPLEMENTED()

    bank_query = property(fget=get_bank_query)

    def get_banks_by_query(self, bank_query):
        """Gets a list of ``Bank`` objects matching the given bank query.

        :param bank_query: the bank query
        :type bank_query: ``osid.assessment.BankQuery``
        :return: the returned ``BankList``
        :rtype: ``osid.assessment.BankList``
        :raise: ``NullArgument`` -- ``bank_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``bank_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.BankSearchSession

    def get_bank_search(self):
        """Gets a bank search.

        :return: a bank search
        :rtype: ``osid.assessment.BankSearch``

        """
        raise UNIMPLEMENTED()

    bank_search = property(fget=get_bank_search)

    def get_bank_search_order(self):
        """Gets a bank search order.
        The ``BankSearchOrder`` is supplied to a ``BankSearch`` to
        specify the ordering of results.

        :return: the bank search order
        :rtype: ``osid.assessment.BankSearchOrder``

        """
        raise UNIMPLEMENTED()

    bank_search_order = property(fget=get_bank_search_order)

    def get_banks_by_search(self, bank_query, bank_search):
        """Gets the search results matching the given search query using the given search.

        :param bank_query: the bank query
        :type bank_query: ``osid.assessment.BankQuery``
        :param bank_search: the bank search
        :type bank_search: ``osid.assessment.BankSearch``
        :return: the bank search results
        :rtype: ``osid.assessment.BankSearchResults``
        :raise: ``NullArgument`` -- ``bank_query`` or ``bank_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``bank_query`` or ``bank_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_bank_query_from_inspector(self, bank_query_inspector):
        """Gets a bank query from an inspector.
        The inspector is available from a ``BankSearchResults``.

        :param bank_query_inspector: a bank query inspector
        :type bank_query_inspector: ``osid.assessment.BankQueryInspector``
        :return: the bank query
        :rtype: ``osid.assessment.BankQuery``
        :raise: ``NullArgument`` -- ``bank_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``bank_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.BankAdminSession

    def can_create_banks(self):
        """Tests if this user can create ``Banks``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Bank`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_bank_with_record_types(self, bank_record_types):
        """Tests if this user can create a single ``Bank`` using the desired record types.
        While ``AssessmentManager.getBankRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Bank``.
        Providing an empty array tests if a ``Bank`` can be created with
        no records.

        :param bank_record_types: array of bank record types
        :type bank_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Bank`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_bank_form_for_create(self, bank_record_types):
        """Gets the bank form for creating new banks.
        A new form should be requested for each create transaction.

        :param bank_record_types: array of bank record types to be included in the create operation or an empty list if none
        :type bank_record_types: ``osid.type.Type[]``
        :return: the bank form
        :rtype: ``osid.assessment.BankForm``
        :raise: ``NullArgument`` -- ``bank_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_bank(self, bank_form):
        """Creates a new ``Bank``.

        :param bank_form: the form for this ``Bank``
        :type bank_form: ``osid.assessment.BankForm``
        :return: the new ``Bank``
        :rtype: ``osid.assessment.Bank``
        :raise: ``IllegalState`` -- ``bank_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``bank_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``bank_form`` did not originate from ``get_bank_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_banks(self):
        """Tests if this user can update ``Banks``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Bank`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_bank_form_for_update(self, bank_id):
        """Gets the bank form for updating an existing bank.
        A new bank form should be requested for each update transaction.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: the bank form
        :rtype: ``osid.assessment.BankForm``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def update_bank(self, bank_form):
        """Updates an existing bank.

        :param bank_form: the form containing the elements to be updated
        :type bank_form: ``osid.assessment.BankForm``
        :raise: ``IllegalState`` -- ``bank_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``bank_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``bank_form`` did not originate from ``get_bank_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_banks(self):
        """Tests if this user can delete banks.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Bank`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_bank(self, bank_id):
        """Deletes a ``Bank``.

        :param bank_id: the ``Id`` of the ``Bank`` to remove
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def can_manage_bank_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Banks``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Bank`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_bank(self, bank_id, alias_id):
        """Adds an ``Id`` to a ``Bank`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Bank`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another bank, it is reassigned to the
        given bank ``Id``.

        :param bank_id: the ``Id`` of a ``Bank``
        :type bank_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.BankNotificationSession

    def can_register_for_bank_notifications(self):
        """Tests if this user can register for ``Bank`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def reliable_bank_notifications(self):
        """Reliable notifications are desired.
        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_bank_notification()`` .



        """
        raise UNIMPLEMENTED()

    def unreliable_bank_notifications(self):
        """Unreliable notifications are desired.
        In unreliable mode, notifications do not need to be
        acknowledged.



        """
        raise UNIMPLEMENTED()

    def acknowledge_bank_notification(self, notification_id):
        """Acknowledge a bank notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_banks(self):
        """Register for notifications of new banks.
        ``BankReceiver.newBanks()`` is invoked when a new Bank is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_banks(self):
        """Registers for notification of updated banks.
        ``BankReceiver.changedBanks()`` is invoked when a bank is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_bank(self, bank_id):
        """Registers for notification of an updated bank.
        ``BankReceiver.changedBanks()`` is invoked when the specified
        bank is changed.

        :param bank_id: the Id of the bank to monitor
        :type bank_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bank_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_banks(self):
        """Registers for notification of deleted banks.
        ``BankReceiver.deletedBanks()`` is invoked when a bank is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_bank(self, bank_id):
        """Registers for notification of a deleted bank.
        ``BankReceiver.deletedBanks()`` is invoked when the specified
        bank is deleted.

        :param bank_id: the Id of the bank to monitor
        :type bank_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bank_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_bank_hierarchy(self):
        """Registers for notification of an updated bank hierarchy structure.
        ``BankReceiver.changedChildOfBanks()`` is invoked when a node
        experiences a change in its children.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_bank_hierarchy_for_ancestors(self, bank_id):
        """Registers for notification of an updated bank hierarchy structure.
        ``BankReceiver.changedChildOfBanks()`` is invoked when the
        specified node or any of its ancestors experiences a change in
        its children.

        :param bank_id: the ``Id`` of the ``Bank`` node to monitor
        :type bank_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_bank_hierarchy_for_descendants(self, bank_id):
        """Registers for notification of an updated bank hierarchy structure.
        ``BankReceiver.changedChildOfBanks()`` is invoked when the
        specified node or any of its descendants experiences a change in
        its children.

        :param bank_id: the ``Id`` of the ``Bank`` node to monitor
        :type bank_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.BankHierarchySession

    def get_bank_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    bank_hierarchy_id = property(fget=get_bank_hierarchy_id)

    def get_bank_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        """
        raise UNIMPLEMENTED()

    bank_hierarchy = property(fget=get_bank_hierarchy)

    def can_access_bank_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_bank_ids(self):
        """Gets the root bank ``Ids`` in this hierarchy.

        :return: the root bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    root_bank_ids = property(fget=get_root_bank_ids)

    def get_root_banks(self):
        """Gets the root banks in this bank hierarchy.

        :return: the root banks
        :rtype: ``osid.assessment.BankList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    root_banks = property(fget=get_root_banks)

    def has_parent_banks(self, bank_id):
        """Tests if the ``Bank`` has any parents.

        :param bank_id: a bank ``Id``
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if the bank has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def is_parent_of_bank(self, id_, bank_id):
        """Tests if an ``Id`` is a direct parent of a bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_parent_bank_ids(self, bank_id):
        """Gets the parent ``Ids`` of the given bank.

        :param bank_id: a bank ``Id``
        :type bank_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the bank
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_parent_banks(self, bank_id):
        """Gets the parents of the given bank.

        :param bank_id: a bank ``Id``
        :type bank_id: ``osid.id.Id``
        :return: the parents of the bank
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_bank(self, id_, bank_id):
        """Tests if an ``Id`` is an ancestor of a bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_banks(self, bank_id):
        """Tests if a bank has any children.

        :param bank_id: a ``bank_id``
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if the ``bank_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_bank(self, id_, bank_id):
        """Tests if a bank is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_bank_ids(self, bank_id):
        """Gets the child ``Ids`` of the given bank.

        :param bank_id: the ``Id`` to query
        :type bank_id: ``osid.id.Id``
        :return: the children of the bank
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_banks(self, bank_id):
        """Gets the children of the given bank.

        :param bank_id: the ``Id`` to query
        :type bank_id: ``osid.id.Id``
        :return: the children of the bank
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_bank(self, id_, bank_id):
        """Tests if an ``Id`` is a descendant of a bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bank_node_ids(self, bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given bank.

        :param bank_id: the ``Id`` to query
        :type bank_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a bank node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bank_nodes(self, bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given bank.

        :param bank_id: the ``Id`` to query
        :type bank_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a bank node
        :rtype: ``osid.assessment.BankNode``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.BankHierarchyDesignSession

    def can_modify_bank_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_bank(self, bank_id):
        """Adds a root bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``bank_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def remove_root_bank(self, bank_id):
        """Removes a root bank from this hierarchy.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bank_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``bank_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_bank(self, bank_id, child_id):
        """Adds a child to a bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``bank_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``bank_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def remove_child_bank(self, bank_id, child_id):
        """Removes a child from a bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bank_id`` not parent of ``child_id``
        :raise: ``NullArgument`` -- ``bank_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def remove_child_banks(self, bank_id):
        """Removes all children from a bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bank_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()



class AssessmentProxyManager(osid_managers.OsidProxyManager, AssessmentProfile):

    def get_my_assessment_taken_session(self, proxy):
        """Gets a ``MyAssessmentTakenSession`` to retrieve assessments taken for the current agent.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MyAssessmentTakenSession``
        :rtype: ``osid.assessment.MyAssessmentTakenSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_assessment_taken()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_my_assessment_taken_session_for_bank(self, bank_id, proxy):
        """Gets a ``MyAssessmentTakenSession`` to retrieve assessments taken for the current agent for the given bank ``Id``.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MyAssessmentTakenSession``
        :rtype: ``osid.assessment.MyAssessmentTakenSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_assessment_taken()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_session(self, proxy):
        """Gets an ``AssessmentSession`` which is responsible for taking assessments and examining responses from assessments taken.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an assessment session for this service
        :rtype: ``osid.assessment.AssessmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_session_for_bank(self, bank_id, proxy):
        """Gets an ``AssessmentSession`` which is responsible for performing assessments for the given bank ``Id``.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an assessment session for this service
        :rtype: ``osid.assessment.AssessmentSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_results_session(self, proxy):
        """Gets an ``AssessmentResultsSession`` to retrieve assessment results.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an assessment results session for this service
        :rtype: ``osid.assessment.AssessmentResultsSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_results()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_results_session_for_bank(self, bank_id, proxy):
        """Gets an ``AssessmentResultsSession`` to retrieve assessment results for the given bank.

        :param bank_id: the ``Id`` of the assessment taken
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an assessment results session for this service
        :rtype: ``osid.assessment.AssessmentResultsSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_results()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the item lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemLookupSession``
        :rtype: ``osid.assessment.ItemLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the item lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _item_lookup_session``
        :rtype: ``osid.assessment.ItemLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the item query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemQuerySession``
        :rtype: ``osid.assessment.ItemQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_query_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the item query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _item_query_session``
        :rtype: ``osid.assessment.ItemQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the item search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemSearchSession``
        :rtype: ``osid.assessment.ItemSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_search_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the item search service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _item_search_session``
        :rtype: ``osid.assessment.ItemSearchSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``porxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the item administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemAdminSession``
        :rtype: ``osid.assessment.ItemAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_admin_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the item admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _item_admin_session``
        :rtype: ``osid.assessment.ItemAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_notification_session(self, item_receiver, proxy):
        """Gets the notification session for notifications pertaining to item changes.

        :param item_receiver: the item receiver interface
        :type item_receiver: ``osid.assessment.ItemReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemNotificationSession``
        :rtype: ``osid.assessment.ItemNotificationSession``
        :raise: ``NullArgument`` -- ``item_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_notification_session_for_bank(self, item_receiver, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the item notification service for the given bank.

        :param item_receiver: the item receiver interface
        :type item_receiver: ``osid.assessment.ItemReceiver``
        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _item_notification_session``
        :rtype: ``osid.assessment.AssessmentNotificationSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``item_receiver, bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_item_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_bank_session(self, proxy):
        """Gets the ``OsidSession`` associated with the item banking service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemBankSession``
        :rtype: ``osid.assessment.ItemBankSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_bank()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_bank_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with the item bank assignment service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemBankAssignmentSession``
        :rtype: ``osid.assessment.ItemBankAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_bank_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_item_smart_bank_session(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the item smart banking service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ItemSmartBankSession``
        :rtype: ``osid.assessment.ItemSmartBankSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_item_smart_bank()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentLookupSession``
        :rtype: ``osid.assessment.AssessmentLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _assessment_lookup_session``
        :rtype: ``osid.assessment.AssessmentLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentQuerySession``
        :rtype: ``osid.assessment.AssessmentQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_query_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _assessment_query_session``
        :rtype: ``osid.assessment.AssessmentQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentSearchSession``
        :rtype: ``osid.assessment.AssessmentSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_search_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment search service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _assessment_search_session``
        :rtype: ``osid.assessment.AssessmentSearchSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentAdminSession``
        :rtype: ``osid.assessment.AssessmentAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_admin_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _assessment_admin_session``
        :rtype: ``osid.assessment.AssessmentAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_notification_session(self, assessment_receiver, proxy):
        """Gets the notification session for notifications pertaining to assessment changes.

        :param assessment_receiver: the assessment receiver interface
        :type assessment_receiver: ``osid.assessment.AssessmentReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentNotificationSession``
        :rtype: ``osid.assessment.AssessmentNotificationSession``
        :raise: ``NullArgument`` -- ``assessment_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_notification_session_for_bank(self, assessment_receiver, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment notification service for the given bank.

        :param assessment_receiver: the assessment receiver interface
        :type assessment_receiver: ``osid.assessment.AssessmentReceiver``
        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _assessment_notification_session``
        :rtype: ``osid.assessment.AssessmentNotificationSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``assessment_receiver, bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_bank_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment banking service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentBankSession``
        :rtype: ``osid.assessment.AssessmentBankSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_bank()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_bank_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment bank assignment service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentBankAssignmentSession``
        :rtype: ``osid.assessment.AssessmentBankAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_bank_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_smart_bank_session(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment smart banking service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentSmartBankSession``
        :rtype: ``osid.assessment.AssessmentSmartBankSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_smart_bank()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_basic_authoring_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment authoring service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentBasicAuthoringSession``
        :rtype: ``osid.assessment.AssessmentBasicAuthoringSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_basic_authoring()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_basic_authoring_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment authoring service for the given bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentBasicAuthoringSession``
        :rtype: ``osid.assessment.AssessmentBasicAuthoringSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_basic_authoring()`` or ``supports_visibe_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedLookupSession``
        :rtype: ``osid.assessment.AssessmentOfferedLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedLookupSession``
        :rtype: ``osid.assessment.AssessmentOfferedLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedQuerySession``
        :rtype: ``osid.assessment.AssessmentOfferedQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_query_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedQuerySession``
        :rtype: ``osid.assessment.AssessmentOfferedQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedSearchSession``
        :rtype: ``osid.assessment.AssessmentOfferedSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_search_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered search service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedSearchSession``
        :rtype: ``osid.assessment.AssessmentOfferedSearchSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or proxy is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedAdminSession``
        :rtype: ``osid.assessment.AssessmentOfferedAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_admin_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered admin service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedAdminSession``
        :rtype: ``osid.assessment.AssessmentOfferedAdminSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_notification_session(self, assessment_offered_receiver, proxy):
        """Gets the notification session for notifications pertaining to offered assessment changes.

        :param assessment_offered_receiver: the assessment offered receiver interface
        :type assessment_offered_receiver: ``osid.assessment.AssessmentOfferedReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedNotificationSession``
        :rtype: ``osid.assessment.AssessmentOfferedNotificationSession``
        :raise: ``NullArgument`` -- ``assessment_offered_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_notification_session_for_bank(self, assessment_offered_receiver, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the offered assessment notification service for the given bank.

        :param assessment_offered_receiver: the assessment offered receiver interface
        :type assessment_offered_receiver: ``osid.assessment.AssessmentOfferedReceiver``
        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``AssessmentOfferedNotificationSession``
        :rtype: ``osid.assessment.AssessmentOfferedNotificationSession``
        :raise: ``NotFound`` -- ``bank_id`` or ``proxy`` not found
        :raise: ``NullArgument`` -- ``assessment_offered_receiver, bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_bank_session(self, proxy):
        """Gets the session for retrieving offered assessments to bank mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedBankSession``
        :rtype: ``osid.assessment.AssessmentOfferedBankSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_bank()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_bank_assignment_session(self, proxy):
        """Gets the session for assigning offered assessments to bank mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedBankAssignmentSession``
        :rtype: ``osid.assessment.AssessmentOfferedBankAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_bank_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_smart_bank_session(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment offered smart banking service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentOfferedSmartBankSession``
        :rtype: ``osid.assessment.AssessmentOfferedSmartBankSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_offered_smart_bank()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenLookupSession``
        :rtype: ``osid.assessment.AssessmentTakenLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_lookup_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken lookup service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenLookupSession``
        :rtype: ``osid.assessment.AssessmentTakenLookupSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenQuerySession``
        :rtype: ``osid.assessment.AssessmentTakenQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_query_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken query service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenQuerySession``
        :rtype: ``osid.assessment.AssessmentTakenQuerySession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenSearchSession``
        :rtype: ``osid.assessment.AssessmentTakenSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_search_session_for_bank(self, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the assessment taken search service for the given bank.

        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenSearchSession``
        :rtype: ``osid.assessment.AssessmentTakenSearchSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_notification_session(self, assessment_taken_receiver, proxy):
        """Gets the notification session for notifications pertaining to taken assessment changes.

        :param assessment_taken_receiver: the assessment taken receiver interface
        :type assessment_taken_receiver: ``osid.assessment.AssessmentTakenReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenNotificationSession``
        :rtype: ``osid.assessment.AssessmentTakenNotificationSession``
        :raise: ``NullArgument`` -- ``assessment_taken_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_notification_session_for_bank(self, assessment_taken_receiver, bank_id, proxy):
        """Gets the ``OsidSession`` associated with the taken assessment notification service for the given bank.

        :param assessment_taken_receiver: the assessment taken receiver interface
        :type assessment_taken_receiver: ``osid.assessment.AssessmentTakenReceiver``
        :param bank_id: the ``Id`` of the bank
        :type bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssessmentTakenNotificationSession``
        :rtype: ``osid.assessment.AssessmentTakenNotificationSession``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``assessment_taken_receiver, bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_assessment_taken_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_bank_lookup_session(self, proxy):
        """Gets the OsidSession associated with the bank lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankLookupSession``
        :rtype: ``osid.assessment.BankLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_lookup() is false``

        """
        raise UNIMPLEMENTED()

    def get_bank_query_session(self, proxy):
        """Gets the OsidSession associated with the bank query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankQuerySession``
        :rtype: ``osid.assessment.BankQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_query() is false``

        """
        raise UNIMPLEMENTED()

    def get_bank_search_session(self, proxy):
        """Gets the OsidSession associated with the bank search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankSearchSession``
        :rtype: ``osid.assessment.BankSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_search() is false``

        """
        raise UNIMPLEMENTED()

    def get_bank_admin_session(self, proxy):
        """Gets the OsidSession associated with the bank administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankAdminSession``
        :rtype: ``osid.assessment.BankAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_admin() is false``

        """
        raise UNIMPLEMENTED()

    def get_bank_notification_session(self, bank_receiver, proxy):
        """Gets the notification session for notifications pertaining to bank service changes.

        :param bank_receiver: the bank receiver interface
        :type bank_receiver: ``osid.assessment.BankReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankNotificationSession``
        :rtype: ``osid.assessment.BankNotificationSession``
        :raise: ``NullArgument`` -- ``bank_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_notification() is false``

        """
        raise UNIMPLEMENTED()

    def get_bank_hierarchy_session(self, proxy):
        """Gets the session traversing bank hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankHierarchySession``
        :rtype: ``osid.assessment.BankHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_hierarchy() is false``

        """
        raise UNIMPLEMENTED()

    def get_bank_hierarchy_design_session(self, proxy):
        """Gets the session designing bank hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BankHierarchySession``
        :rtype: ``osid.assessment.BankHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_bank_hierarchy_design() is false``

        """
        raise UNIMPLEMENTED()

    def get_assessment_authoring_proxy_manager(self):
        """Gets an ``AssessmentAuthoringProxyManager``.

        :return: an ``AssessmentAuthoringProxyManager``
        :rtype: ``osid.assessment.authoring.AssessmentAuthoringProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_authoring() is false``

        """
        raise UNIMPLEMENTED()

    assessment_authoring_proxy_manager = property(fget=get_assessment_authoring_proxy_manager)

    def get_assessment_batch_proxy_manager(self):
        """Gets an ``AssessmentBatchProxyManager``.

        :return: an ``AssessmentBatchProxyManager``
        :rtype: ``osid.assessment.batch.AssessmentBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_assessment_batch() is false``

        """
        raise UNIMPLEMENTED()

    assessment_batch_proxy_manager = property(fget=get_assessment_batch_proxy_manager)


##
# The following methods are from osid.assessment.BankLookupSession

    def can_lookup_banks(self):
        """Tests if this user can perform ``Bank`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.


        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.




        """
        raise UNIMPLEMENTED()

    def use_plenary_bank_view(self):
        """A complete view of the ``Bank`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.




        """
        raise UNIMPLEMENTED()

    def get_bank(self, bank_id):
        """Gets the ``Bank`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Bank`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Bank`` and retained for compatibility.


        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_banks_by_ids(self, bank_ids):
        """Gets a ``BankList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the banks
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Bank`` objects may be omitted from the list and
        may present the elements in any order including returning a
        unique set.


        :param bank_ids: the list of ``Ids`` to retrieve
        :type bank_ids: ``osid.id.IdList``
        :return: the returned ``Bank`` list
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_banks_by_genus_type(self, bank_genus_type):
        """Gets a ``BankList`` corresponding to the given bank genus ``Type`` which does not include banks of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.


        :param bank_genus_type: a bank genus type
        :type bank_genus_type: ``osid.type.Type``
        :return: the returned ``Bank`` list
        :rtype: ``osid.assessment.BankList``
        :raise: ``NullArgument`` -- ``bank_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_banks_by_parent_genus_type(self, bank_genus_type):
        """Gets a ``BankList`` corresponding to the given bank genus ``Type`` and include any additional banks with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.


        :param bank_genus_type: a bank genus type
        :type bank_genus_type: ``osid.type.Type``
        :return: the returned ``Bank`` list
        :rtype: ``osid.assessment.BankList``
        :raise: ``NullArgument`` -- ``bank_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_banks_by_record_type(self, bank_record_type):
        """Gets a ``BankList`` containing the given bank record ``Type``.
        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.


        :param bank_record_type: a bank record type
        :type bank_record_type: ``osid.type.Type``
        :return: the returned ``Bank`` list
        :rtype: ``osid.assessment.BankList``
        :raise: ``NullArgument`` -- ``bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_banks_by_provider(self, resource_id):
        """Gets a ``BankList`` from the given provider ````.
        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Bank`` list
        :rtype: ``osid.assessment.BankList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_banks(self):
        """Gets all ``Banks``.
        In plenary mode, the returned list contains all known banks or
        an error results. Otherwise, the returned list may contain only
        those banks that are accessible through this session.


        :return: a ``BankList``
        :rtype: ``osid.assessment.BankList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    banks = property(fget=get_banks)


##
# The following methods are from osid.assessment.BankQuerySession

    def can_search_banks(self):
        """Tests if this user can perform ``Bank`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_bank_query(self):
        """Gets a bank query.

        :return: a bank query
        :rtype: ``osid.assessment.BankQuery``

        """
        raise UNIMPLEMENTED()

    bank_query = property(fget=get_bank_query)

    def get_banks_by_query(self, bank_query):
        """Gets a list of ``Bank`` objects matching the given bank query.

        :param bank_query: the bank query
        :type bank_query: ``osid.assessment.BankQuery``
        :return: the returned ``BankList``
        :rtype: ``osid.assessment.BankList``
        :raise: ``NullArgument`` -- ``bank_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``bank_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.BankSearchSession

    def get_bank_search(self):
        """Gets a bank search.

        :return: a bank search
        :rtype: ``osid.assessment.BankSearch``

        """
        raise UNIMPLEMENTED()

    bank_search = property(fget=get_bank_search)

    def get_bank_search_order(self):
        """Gets a bank search order.
        The ``BankSearchOrder`` is supplied to a ``BankSearch`` to
        specify the ordering of results.


        :return: the bank search order
        :rtype: ``osid.assessment.BankSearchOrder``

        """
        raise UNIMPLEMENTED()

    bank_search_order = property(fget=get_bank_search_order)

    def get_banks_by_search(self, bank_query, bank_search):
        """Gets the search results matching the given search query using the given search.

        :param bank_query: the bank query
        :type bank_query: ``osid.assessment.BankQuery``
        :param bank_search: the bank search
        :type bank_search: ``osid.assessment.BankSearch``
        :return: the bank search results
        :rtype: ``osid.assessment.BankSearchResults``
        :raise: ``NullArgument`` -- ``bank_query`` or ``bank_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``bank_query`` or ``bank_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_bank_query_from_inspector(self, bank_query_inspector):
        """Gets a bank query from an inspector.
        The inspector is available from a ``BankSearchResults``.


        :param bank_query_inspector: a bank query inspector
        :type bank_query_inspector: ``osid.assessment.BankQueryInspector``
        :return: the bank query
        :rtype: ``osid.assessment.BankQuery``
        :raise: ``NullArgument`` -- ``bank_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``bank_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.BankAdminSession

    def can_create_banks(self):
        """Tests if this user can create ``Banks``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.


        :return: ``false`` if ``Bank`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_bank_with_record_types(self, bank_record_types):
        """Tests if this user can create a single ``Bank`` using the desired record types.
        While ``AssessmentManager.getBankRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Bank``.
        Providing an empty array tests if a ``Bank`` can be created with
        no records.


        :param bank_record_types: array of bank record types
        :type bank_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Bank`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_bank_form_for_create(self, bank_record_types):
        """Gets the bank form for creating new banks.
        A new form should be requested for each create transaction.


        :param bank_record_types: array of bank record types to be included in the create operation or an empty list if none
        :type bank_record_types: ``osid.type.Type[]``
        :return: the bank form
        :rtype: ``osid.assessment.BankForm``
        :raise: ``NullArgument`` -- ``bank_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_bank(self, bank_form):
        """Creates a new ``Bank``.

        :param bank_form: the form for this ``Bank``
        :type bank_form: ``osid.assessment.BankForm``
        :return: the new ``Bank``
        :rtype: ``osid.assessment.Bank``
        :raise: ``IllegalState`` -- ``bank_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``bank_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``bank_form`` did not originate from ``get_bank_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_banks(self):
        """Tests if this user can update ``Banks``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.


        :return: ``false`` if ``Bank`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_bank_form_for_update(self, bank_id):
        """Gets the bank form for updating an existing bank.
        A new bank form should be requested for each update transaction.


        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: the bank form
        :rtype: ``osid.assessment.BankForm``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def update_bank(self, bank_form):
        """Updates an existing bank.

        :param bank_form: the form containing the elements to be updated
        :type bank_form: ``osid.assessment.BankForm``
        :raise: ``IllegalState`` -- ``bank_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``bank_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``bank_form`` did not originate from ``get_bank_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_banks(self):
        """Tests if this user can delete banks.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Bank``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.


        :return: ``false`` if ``Bank`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_bank(self, bank_id):
        """Deletes a ``Bank``.

        :param bank_id: the ``Id`` of the ``Bank`` to remove
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def can_manage_bank_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Banks``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``Bank`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_bank(self, bank_id, alias_id):
        """Adds an ``Id`` to a ``Bank`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Bank`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another bank, it is reassigned to the
        given bank ``Id``.


        :param bank_id: the ``Id`` of a ``Bank``
        :type bank_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.BankNotificationSession

    def can_register_for_bank_notifications(self):
        """Tests if this user can register for ``Bank`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.


        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def reliable_bank_notifications(self):
        """Reliable notifications are desired.
        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_bank_notification()`` .




        """
        raise UNIMPLEMENTED()

    def unreliable_bank_notifications(self):
        """Unreliable notifications are desired.
        In unreliable mode, notifications do not need to be
        acknowledged.




        """
        raise UNIMPLEMENTED()

    def acknowledge_bank_notification(self, notification_id):
        """Acknowledge a bank notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_banks(self):
        """Register for notifications of new banks.
        ``BankReceiver.newBanks()`` is invoked when a new Bank is
        created.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_banks(self):
        """Registers for notification of updated banks.
        ``BankReceiver.changedBanks()`` is invoked when a bank is
        changed.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_bank(self, bank_id):
        """Registers for notification of an updated bank.
        ``BankReceiver.changedBanks()`` is invoked when the specified
        bank is changed.


        :param bank_id: the Id of the bank to monitor
        :type bank_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bank_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_banks(self):
        """Registers for notification of deleted banks.
        ``BankReceiver.deletedBanks()`` is invoked when a bank is
        deleted.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_bank(self, bank_id):
        """Registers for notification of a deleted bank.
        ``BankReceiver.deletedBanks()`` is invoked when the specified
        bank is deleted.


        :param bank_id: the Id of the bank to monitor
        :type bank_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bank_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_bank_hierarchy(self):
        """Registers for notification of an updated bank hierarchy structure.
        ``BankReceiver.changedChildOfBanks()`` is invoked when a node
        experiences a change in its children.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_bank_hierarchy_for_ancestors(self, bank_id):
        """Registers for notification of an updated bank hierarchy structure.
        ``BankReceiver.changedChildOfBanks()`` is invoked when the
        specified node or any of its ancestors experiences a change in
        its children.


        :param bank_id: the ``Id`` of the ``Bank`` node to monitor
        :type bank_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_bank_hierarchy_for_descendants(self, bank_id):
        """Registers for notification of an updated bank hierarchy structure.
        ``BankReceiver.changedChildOfBanks()`` is invoked when the
        specified node or any of its descendants experiences a change in
        its children.


        :param bank_id: the ``Id`` of the ``Bank`` node to monitor
        :type bank_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.BankHierarchySession

    def get_bank_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    bank_hierarchy_id = property(fget=get_bank_hierarchy_id)

    def get_bank_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        """
        raise UNIMPLEMENTED()

    bank_hierarchy = property(fget=get_bank_hierarchy)

    def can_access_bank_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.


        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_bank_ids(self):
        """Gets the root bank ``Ids`` in this hierarchy.

        :return: the root bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    root_bank_ids = property(fget=get_root_bank_ids)

    def get_root_banks(self):
        """Gets the root banks in this bank hierarchy.

        :return: the root banks
        :rtype: ``osid.assessment.BankList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    root_banks = property(fget=get_root_banks)

    def has_parent_banks(self, bank_id):
        """Tests if the ``Bank`` has any parents.

        :param bank_id: a bank ``Id``
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if the bank has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def is_parent_of_bank(self, id_, bank_id):
        """Tests if an ``Id`` is a direct parent of a bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_parent_bank_ids(self, bank_id):
        """Gets the parent ``Ids`` of the given bank.

        :param bank_id: a bank ``Id``
        :type bank_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the bank
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_parent_banks(self, bank_id):
        """Gets the parents of the given bank.

        :param bank_id: a bank ``Id``
        :type bank_id: ``osid.id.Id``
        :return: the parents of the bank
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_bank(self, id_, bank_id):
        """Tests if an ``Id`` is an ancestor of a bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_banks(self, bank_id):
        """Tests if a bank has any children.

        :param bank_id: a ``bank_id``
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if the ``bank_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_bank(self, id_, bank_id):
        """Tests if a bank is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_bank_ids(self, bank_id):
        """Gets the child ``Ids`` of the given bank.

        :param bank_id: the ``Id`` to query
        :type bank_id: ``osid.id.Id``
        :return: the children of the bank
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_banks(self, bank_id):
        """Gets the children of the given bank.

        :param bank_id: the ``Id`` to query
        :type bank_id: ``osid.id.Id``
        :return: the children of the bank
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_bank(self, id_, bank_id):
        """Tests if an ``Id`` is a descendant of a bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bank_node_ids(self, bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given bank.

        :param bank_id: the ``Id`` to query
        :type bank_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a bank node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_bank_nodes(self, bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given bank.

        :param bank_id: the ``Id`` to query
        :type bank_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a bank node
        :rtype: ``osid.assessment.BankNode``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.BankHierarchyDesignSession

    def can_modify_bank_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.


        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_bank(self, bank_id):
        """Adds a root bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``bank_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``bank_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def remove_root_bank(self, bank_id):
        """Removes a root bank from this hierarchy.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bank_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``bank_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_bank(self, bank_id, child_id):
        """Adds a child to a bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``bank_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``bank_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``bank_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def remove_child_bank(self, bank_id, child_id):
        """Removes a child from a bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bank_id`` not parent of ``child_id``
        :raise: ``NullArgument`` -- ``bank_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def remove_child_banks(self, bank_id):
        """Removes all children from a bank.

        :param bank_id: the ``Id`` of a bank
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bank_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()



class Bank(osid_objects.OsidCatalog, osid_sessions.OsidSession):

    def get_bank_record(self, bank_record_type):
        """Gets the bank record corresponding to the given ``Bank`` record ``Type``.
        This method is used to retrieve an object implementing the
        requested record. The ``bank_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(bank_record_type)``
        is ``true`` .

        :param bank_record_type: a bank record type
        :type bank_record_type: ``osid.type.Type``
        :return: the bank record
        :rtype: ``osid.assessment.records.BankRecord``
        :raise: ``NullArgument`` -- ``bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(bank_record_type)`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.MyAssessmentTakenSession

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    bank = property(fget=get_bank)

    def can_get_my_taken_assessments(self):
        """Tests if this user can perform ``AssessmentOffered`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_assessments_started_during(self, start, end):
        """Gets all the assessments started by this agent during the given period of time inclusive.

        :param start: start time
        :type start: ``osid.calendaring.DateTime``
        :param end: end time
        :type end: ``osid.calendaring.DateTime``
        :return: the started assessments
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_started(self):
        """Gets all the assessments started by this agent.

        :return: the started assessments
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    assessments_started = property(fget=get_assessments_started)

    def get_assessments_in_progress_during(self, start, end):
        """Gets all the assessments in progress by this agent overlapping with the given period of time inclusive.

        :param start: start time
        :type start: ``osid.calendaring.DateTime``
        :param end: end time
        :type end: ``osid.calendaring.DateTime``
        :return: the in progress assessments
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_in_progress(self):
        """Gets all the assessments started but not completed by this agent.

        :return: the assessments in progress
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    assessments_in_progress = property(fget=get_assessments_in_progress)

    def get_assessments_completed(self):
        """Gets all the assessments completed by this agent.

        :return: the completed assessments
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    assessments_completed = property(fget=get_assessments_completed)


##
# The following methods are from osid.assessment.AssessmentSession

    def can_take_assessments(self):
        """Tests if this user can take this assessment section.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer assessment
        operations to unauthorized users.

        :return: ``false`` if assessment methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def has_assessment_begun(self, assessment_taken_id):
        """Tests if this assessment has started.
        An assessment begins from the designated start time if a start
        time is defined. If no start time is defined the assessment may
        begin at any time. Assessment sections cannot be accessed if the
        return for this method is ``false``.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: ``true`` if this assessment has begun, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def is_assessment_over(self, assessment_taken_id):
        """Tests if this assessment is over.
        An assessment is over if ``finished_assessment()`` is invoked or
        the designated finish time has expired.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: ``true`` if this assessment is over, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def finished_assessment(self, assessment_taken_id):
        """Indicates the entire assessment is complete.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_begun()`` is ``false or is_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def requires_synchronous_sections(self):
        """Tests if synchronous sections are required.
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

        :return: ``true`` if this synchronous sections are required, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_first_assessment_section(self, assessment_taken_id):
        """Gets the first assessment section in this assesment.
        All assessments have at least one ``AssessmentSection``.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: the first assessment section
        :rtype: ``osid.assessment.AssessmentSection``
        :raise: ``IllegalState`` -- ``has_assessment_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def has_next_assessment_section(self, assessment_section_id):
        """Tests if there is a next assessment section in the assessment following the given assessment section ``Id``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: ``true`` if there is a next section, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_next_assessment_section(self, assessment_section_id):
        """Gets the next assessemnt section following the given assesment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: the next section
        :rtype: ``osid.assessment.AssessmentSection``
        :raise: ``IllegalState`` -- ``has_next_assessment_section()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def has_previous_assessment_section(self, assessment_section_id):
        """Tests if there is a previous assessment section in the assessment following the given assessment section ``Id``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: ``true`` if there is a previous assessment section, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_previous_assessment_section(self, assessment_section_id):
        """Gets the next assessemnt section following the given assesment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: the previous assessment section
        :rtype: ``osid.assessment.AssessmentSection``
        :raise: ``IllegalState`` -- ``has_next_assessment_section()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessment_section(self, assessment_section_id):
        """Gets an assessemnts section by ``Id``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: the assessment section
        :rtype: ``osid.assessment.AssessmentSection``
        :raise: ``IllegalState`` -- ``has_assessment_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessment_sections(self, assessment_taken_id):
        """Gets the assessment sections of this assessment.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: the list of assessment sections
        :rtype: ``osid.assessment.AssessmentSectionList``
        :raise: ``IllegalState`` -- ``has_assessment_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def is_assessment_section_complete(self, assessment_section_id):
        """Tests if the given assessment section is complete.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: ``true`` if this assessment section is complete, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``is_assessment_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_incomplete_assessment_sections(self, assessment_taken_id):
        """Gets the incomplete assessment sections of this assessment.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: the list of incomplete assessment sections
        :rtype: ``osid.assessment.AssessmentSectionList``
        :raise: ``IllegalState`` -- ``has_assessment_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def has_assessment_section_begun(self, assessment_section_id):
        """Tests if this assessment section has started.
        A section begins from the designated start time if a start time
        is defined. If no start time is defined the section may begin at
        any time. Assessment items cannot be accessed or submitted if
        the return for this method is ``false``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: ``true`` if this assessment section has begun, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_begun()`` is ``false or is_assessment_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_assessment_section_over(self, assessment_section_id):
        """Tests if this assessment section is over.
        An assessment section is over if
        ``finished_assessment_section()`` is invoked or the designated
        finish time has expired.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: ``true`` if this assessment is over, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessmen_sectiont_begun()`` is ``false or is_assessment_section_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def finished_assessment_section(self, assessment_section_id):
        """Indicates an assessment section is complete.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false or is_assessment_section_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def requires_synchronous_responses(self, assessment_section_id):
        """Tests if synchronous responses are required in this assessment section.
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

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: ``true`` if this synchronous responses are required, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_begun()`` is ``false or is_assessment_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_first_question(self, assessment_section_id):
        """Gets the first question in this assesment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: the first question
        :rtype: ``osid.assessment.Question``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def has_next_question(self, assessment_section_id, item_id):
        """Tests if there is a next question following the given question ``Id``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: ``true`` if there is a next question, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` or ``item_id`` is not found, or ``item_id`` not part of ``assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_next_question(self, assessment_section_id, item_id):
        """Gets the next question in this assesment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the next question
        :rtype: ``osid.assessment.Question``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` or ``has_next_question()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` or ``item_id`` is not found, or ``item_id`` not part of ``assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def has_previous_question(self, assessment_section_id, item_id):
        """Tests if there is a previous question preceeding the given question ``Id``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: ``true`` if there is a previous question, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` or ``item_id`` is not found, or ``item_id`` not part of ``assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_previous_question(self, assessment_section_id, item_id):
        """Gets the previous question in this assesment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the previous question
        :rtype: ``osid.assessment.Question``
        :raise: ``IllegalState`` -- ``has_begun()`` or ``has_previous_question()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` or ``item_id`` is not found, or ``item_id`` not part of ``assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_question(self, assessment_section_id, item_id):
        """Gets the ``Question`` specified by its ``Id``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the returned ``Question``
        :rtype: ``osid.assessment.Question``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` or ``item_id`` is not found, or ``item_id`` not part of ``assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_questions(self, assessment_section_id):
        """Gets the questions of this assessment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: the list of assessment questions
        :rtype: ``osid.assessment.QuestionList``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_response_form(self, assessment_section_id, item_id):
        """Gets the response form for submitting an answer.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: an answer form
        :rtype: ``osid.assessment.AnswerForm``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false or is_assessment_section_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id`` or ``item_id`` is not found, or ``item_id`` not part of ``assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def submit_response(self, assessment_section_id, item_id, answer_form):
        """Submits an answer to an item.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :param answer_form: the response
        :type answer_form: ``osid.assessment.AnswerForm``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false or is_assessment_section_over()`` is ``true``
        :raise: ``InvalidArgument`` -- one or more of the elements in the form is invalid
        :raise: ``NotFound`` -- ``assessment_section_id`` or ``item_id`` is not found, or ``item_id`` not part of ``assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id, item_id,`` or ``answer_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``answer_form`` is not of this service

        """
        raise UNIMPLEMENTED()

    def skip_item(self, assessment_section_id, item_id):
        """Skips an item.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false or is_assessment_section_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id`` or ``item_id`` is not found, or ``item_id`` not part of ``assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_question_answered(self, assessment_section_id, item_id):
        """Tests if the given item has a response.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: ``true`` if this item has a response, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false or is_assessment_section_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_unanswered_questions(self, assessment_section_id):
        """Gets the unanswered questions of this assessment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: the list of questions with no rsponses
        :rtype: ``osid.assessment.QuestionList``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def has_unanswered_questions(self, assessment_section_id):
        """Tests if there are unanswered questions in this assessment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: ``true`` if there are unanswered questions, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_first_unanswered_question(self, assessment_section_id):
        """Gets the first unanswered question in this assesment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: the first unanswered question
        :rtype: ``osid.assessment.Question``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` or ``has_unanswered_questions()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def has_next_unanswered_question(self, assessment_section_id, item_id):
        """Tests if there is a next unanswered question following the given question ``Id``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: ``true`` if there is a next unanswered question, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_next_unanswered_question(self, assessment_section_id, item_id):
        """Gets the next unanswered question in this assesment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the next unanswered question
        :rtype: ``osid.assessment.Question``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` or ``has_next_unanswered_question()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def has_previous_unanswered_question(self, assessment_section_id, item_id):
        """Tests if there is a previous unanswered question preceeding the given question ``Id``.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: ``true`` if there is a previous unanswered question, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_previous_unanswered_question(self, assessment_section_id, item_id):
        """Gets the previous unanswered question in this assesment section.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the previous unanswered question
        :rtype: ``osid.assessment.Question``
        :raise: ``IllegalState`` -- ``has_assessmnet_section_begun()`` or ``has_previous_unanswered_question()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_response(self, assessment_section_id, item_id):
        """Gets the submitted response to the associated item.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the response
        :rtype: ``osid.assessment.Response``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false or is_assessment_section_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_responses(self, assessment_section_id):
        """Gets all submitted responses.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :return: the list of responses
        :rtype: ``osid.assessment.ResponseList``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun()`` is ``false or is_assessment_section_over()`` is ``true``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def clear_response(self, assessment_section_id, item_id):
        """Clears the response to an item The item appears as unanswered.
        If no response exists, the method simply returns.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun() is false or is_assessment_section_over() is true``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def finish(self, assessment_section_id):
        """Indicates the assessment section is complete.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_assessment_section_begun() is false or is_assessment_section_over() is true``
        :raise: ``NotFound`` -- ``assessment_section_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_section_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_answer_available(self, assessment_section_id, item_id):
        """Tests if an answer is available for the given item.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: ``true`` if an answer are available, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_answers(self, assessment_section_id, item_id):
        """Gets the acceptable answers to the associated item.

        :param assessment_section_id: ``Id`` of the ``AssessmentSection``
        :type assessment_section_id: ``osid.id.Id``
        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the answers
        :rtype: ``osid.assessment.AnswerList``
        :raise: ``IllegalState`` -- ``is_answer_available()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_section_id or item_id is not found, or item_id not part of assessment_section_id``
        :raise: ``NullArgument`` -- ``assessment_section_id or item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentResultsSession

    def can_access_assessment_results(self):
        """Tests if this user can take this assessment.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer assessment
        operations to unauthorized users.

        :return: ``false`` if assessment methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_items(self, assessment_taken_id):
        """Gets the items questioned in a assessment.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: the list of assessment questions
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def are_results_available(self, assessment_taken_id):
        """Tests if the results are available for this assessment.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: ``true`` if results are available, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_entries(self, assessment_taken_id):
        """Gets a list of grade entries for this assessment.
        Each grade entry may indicate a grade or score input by multiple
        graders.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: a list of grade entries
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``IllegalState`` -- ``are_results_available()`` is ``false``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.ItemLookupSession

    def can_lookup_items(self):
        """Tests if this user can perform ``Item`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_item_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_item_view(self):
        """A complete view of the ``Item`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.
        A federated view will include assessment items in assessment
        banks which are children of this assessment bank in the
        assessment bank hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this assessment bank only.



        """
        raise UNIMPLEMENTED()

    def get_item(self, item_id):
        """Gets the ``Item`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Item`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Item`` and retained for compatibility.

        :param item_id: the ``Id`` of the ``Item`` to retrieve
        :type item_id: ``osid.id.Id``
        :return: the returned ``Item``
        :rtype: ``osid.assessment.Item``
        :raise: ``NotFound`` -- no ``Item`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_items_by_ids(self, item_ids):
        """Gets an ``ItemList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the items
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Items`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param item_ids: the list of ``Ids`` to retrieve
        :type item_ids: ``osid.id.IdList``
        :return: the returned ``Item`` list
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``item_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_items_by_genus_type(self, item_genus_type):
        """Gets an ``ItemList`` corresponding to the given assessment item genus ``Type`` which does not include assessment items of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known assessment
        items or an error results. Otherwise, the returned list may
        contain only those assessment items that are accessible through
        this session.

        :param item_genus_type: an assessment item genus type
        :type item_genus_type: ``osid.type.Type``
        :return: the returned ``Item`` list
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``item_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_items_by_parent_genus_type(self, item_genus_type):
        """Gets an ``ItemList`` corresponding to the given assessment item genus ``Type`` and include any additional assessment items with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known assessment
        items or an error results. Otherwise, the returned list may
        contain only those assessment items that are accessible through
        this session.

        :param item_genus_type: an assessment item genus type
        :type item_genus_type: ``osid.type.Type``
        :return: the returned ``Item`` list
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``item_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_items_by_record_type(self, item_record_type):
        """Gets an ``ItemList`` containing the given assessment item record ``Type``.
        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        :param item_record_type: an item record type
        :type item_record_type: ``osid.type.Type``
        :return: the returned ``Item`` list
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``item_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_items_by_question(self, question_id):
        """Gets an ``ItemList`` containing the given question.
        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        :param question_id: a question ``Id``
        :type question_id: ``osid.id.Id``
        :return: the returned ``Item`` list
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``question_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_items_by_answer(self, answer_id):
        """Gets an ``ItemList`` containing the given answer.
        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        :param answer_id: an answer ``Id``
        :type answer_id: ``osid.id.Id``
        :return: the returned ``Item`` list
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``answer_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_items_by_learning_objective(self, objective_id):
        """Gets an ``ItemList`` containing the given learning objective.
        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        :param objective_id: a learning objective ``Id``
        :type objective_id: ``osid.id.Id``
        :return: the returned ``Item`` list
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_items_by_learning_objectives(self, objective_ids):
        """Gets an ``ItemList`` containing the given learning objectives.
        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those assessment items that are accessible through this session.

        :param objective_ids: a list of learning objective ``Ids``
        :type objective_ids: ``osid.id.IdList``
        :return: the returned ``Item`` list
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``objective_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.ItemQuerySession

    def can_search_items(self):
        """Tests if this user can perform ``Item`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an pplication that may wish not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_item_query(self):
        """Gets an assessment item query.

        :return: the assessment item query
        :rtype: ``osid.assessment.ItemQuery``

        """
        raise UNIMPLEMENTED()

    item_query = property(fget=get_item_query)

    def get_items_by_query(self, item_query):
        """Gets a list of ``Items`` matching the given item query.

        :param item_query: the item query
        :type item_query: ``osid.assessment.ItemQuery``
        :return: the returned ``ItemList``
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``item_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``item_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.ItemSearchSession

    def get_item_search(self):
        """Gets an assessment item search.

        :return: the assessment item search
        :rtype: ``osid.assessment.ItemSearch``

        """
        raise UNIMPLEMENTED()

    item_search = property(fget=get_item_search)

    def get_item_search_order(self):
        """Gets an assessment item search order.
        The ``ItemSearchOrder`` is supplied to an ``ItemSearch`` to
        specify the ordering of results.

        :return: the assessment item search order
        :rtype: ``osid.assessment.ItemSearchOrder``

        """
        raise UNIMPLEMENTED()

    item_search_order = property(fget=get_item_search_order)

    def get_items_by_search(self, item_query, item_search):
        """Gets the search results matching the given search query using the given search.

        :param item_query: the item query
        :type item_query: ``osid.assessment.ItemQuery``
        :param item_search: the item search
        :type item_search: ``osid.assessment.ItemSearch``
        :return: the returned search results
        :rtype: ``osid.assessment.ItemSearchResults``
        :raise: ``NullArgument`` -- ``item_query`` or ``item_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``item_search`` or ``item_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_item_query_from_inspector(self, item_query_inspector):
        """Gets an item query from an inspector.
        The inspector is available from an ``ItemSearchResults``.

        :param item_query_inspector: a query inspector
        :type item_query_inspector: ``osid.assessment.ItemQueryInspector``
        :return: the item query
        :rtype: ``osid.assessment.ItemQuery``
        :raise: ``NullArgument`` -- ``item_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``item_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.ItemAdminSession

    def can_create_items(self):
        """Tests if this user can create ``Items``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an ``Item``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Item`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_item_with_record_types(self, item_record_types):
        """Tests if this user can create a single ``Item`` using the desired record types.
        While ``AssessmentManager.getItemRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Item``.
        Providing an empty array tests if an ``Item`` can be created
        with no records.

        :param item_record_types: array of item record types
        :type item_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Item`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``item_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_item_form_for_create(self, item_record_types):
        """Gets the assessment item form for creating new assessment items.
        A new form should be requested for each create transaction.

        :param item_record_types: array of item record types to be included in the create operation or an empty list if none
        :type item_record_types: ``osid.type.Type[]``
        :return: the assessment item form
        :rtype: ``osid.assessment.ItemForm``
        :raise: ``NullArgument`` -- ``item_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_item(self, item_form):
        """Creates a new ``Item``.

        :param item_form: the form for this ``Item``
        :type item_form: ``osid.assessment.ItemForm``
        :return: the new ``Item``
        :rtype: ``osid.assessment.Item``
        :raise: ``IllegalState`` -- ``item_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``item_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``item_form`` did not originate from ``get_item_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_items(self):
        """Tests if this user can update ``Items``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an ``Item``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if assessment item modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_item_form_for_update(self, item_id):
        """Gets the assessment item form for updating an existing item.
        A new item form should be requested for each update transaction.

        :param item_id: the ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the assessment item form
        :rtype: ``osid.assessment.ItemForm``
        :raise: ``NotFound`` -- ``item_id`` is not found
        :raise: ``NullArgument`` -- ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def update_item(self, item_form):
        """Updates an existing item.

        :param item_form: the form containing the elements to be updated
        :type item_form: ``osid.assessment.ItemForm``
        :raise: ``IllegalState`` -- ``item_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``item_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``item_form`` did not originate from ``get_item_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_items(self):
        """Tests if this user can delete ``Items``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an ``Item``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Item`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_item(self, item_id):
        """Deletes the ``Item`` identified by the given ``Id``.

        :param item_id: the ``Id`` of the ``Item`` to delete
        :type item_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``Item`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def can_manage_item_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Items``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Item`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_item(self, item_id, alias_id):
        """Adds an ``Id`` to an ``Item`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Item`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another item, it is reassigned to the
        given item ``Id``.

        :param item_id: the ``Id`` of an ``Item``
        :type item_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``item_id`` not found
        :raise: ``NullArgument`` -- ``item_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def can_create_questions(self):
        """Tests if this user can create ``Questions``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Question`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Question`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_question_with_record_types(self, question_record_types):
        """Tests if this user can create a single ``Question`` using the desired record types.
        While ``AssessmentManager.getQuestionRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Question``.
        Providing an empty array tests if a ``Question`` can be created
        with no records.

        :param question_record_types: array of question record types
        :type question_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Question`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``question_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_question_form_for_create(self, item_id, question_record_types):
        """Gets the question form for creating new questions.
        A new form should be requested for each create transaction.

        :param item_id: an assessment item ``Id``
        :type item_id: ``osid.id.Id``
        :param question_record_types: array of question record types to be included in the create operation or an empty list if none
        :type question_record_types: ``osid.type.Type[]``
        :return: the question form
        :rtype: ``osid.assessment.QuestionForm``
        :raise: ``NullArgument`` -- ``question_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_question(self, question_form):
        """Creates a new ``Question``.

        :param question_form: the form for this ``Question``
        :type question_form: ``osid.assessment.QuestionForm``
        :return: the new ``Question``
        :rtype: ``osid.assessment.Question``
        :raise: ``AlreadyExists`` -- a question already exists for this item
        :raise: ``IllegalState`` -- ``question_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``question_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``question_form`` did not originate from ``get_question_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_questions(self):
        """Tests if this user can update ``Questions``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Question`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if question modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_question_form_for_update(self, question_id):
        """Gets the question form for updating an existing question.
        A new question form should be requested for each update
        transaction.

        :param question_id: the ``Id`` of the ``Question``
        :type question_id: ``osid.id.Id``
        :return: the question form
        :rtype: ``osid.assessment.QuestionForm``
        :raise: ``NotFound`` -- ``question_id`` is not found
        :raise: ``NullArgument`` -- ``question_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def update_question(self, question_form):
        """Updates an existing question.

        :param question_form: the form containing the elements to be updated
        :type question_form: ``osid.assessment.QuestionForm``
        :raise: ``IllegalState`` -- ``question_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``question_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``question_form`` did not originate from ``get_question_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_questions(self):
        """Tests if this user can delete ``Questions``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Question`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Question`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_question(self, question_id):
        """Deletes the ``Question`` identified by the given ``Id``.

        :param question_id: the ``Id`` of the ``Question`` to delete
        :type question_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Question`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``question_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def can_create_answers(self):
        """Tests if this user can create ``Answers``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Answer``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Answer`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_answers_with_record_types(self, answer_record_types):
        """Tests if this user can create a single ``Answer`` using the desired record types.
        While ``AssessmentManager.getAnswerRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Answer``.
        Providing an empty array tests if an ``Answer`` can be created
        with no records.

        :param answer_record_types: array of answer record types
        :type answer_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Answer`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``answern_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_answer_form_for_create(self, item_id, answer_record_types):
        """Gets the answer form for creating new answers.
        A new form should be requested for each create transaction.

        :param item_id: an assessment item ``Id``
        :type item_id: ``osid.id.Id``
        :param answer_record_types: array of answer record types to be included in the create operation or an empty list if none
        :type answer_record_types: ``osid.type.Type[]``
        :return: the answer form
        :rtype: ``osid.assessment.AnswerForm``
        :raise: ``NullArgument`` -- ``answer_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_answer(self, answer_form):
        """Creates a new ``Answer``.

        :param answer_form: the form for this ``Answer``
        :type answer_form: ``osid.assessment.AnswerForm``
        :return: the new ``Answer``
        :rtype: ``osid.assessment.Answer``
        :raise: ``IllegalState`` -- ``answer_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``answer_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``answer_form`` did not originate from ``get_answer_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_answers(self):
        """Tests if this user can update ``Answers``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Answer`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if answer modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_answer_form_for_update(self, answer_id):
        """Gets the answer form for updating an existing answer.
        A new answer form should be requested for each update
        transaction.

        :param answer_id: the ``Id`` of the ``Answer``
        :type answer_id: ``osid.id.Id``
        :return: the answer form
        :rtype: ``osid.assessment.AnswerForm``
        :raise: ``NotFound`` -- ``answer_id`` is not found
        :raise: ``NullArgument`` -- ``answer_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def update_answer(self, answer_form):
        """Updates an existing answer.

        :param answer_form: the form containing the elements to be updated
        :type answer_form: ``osid.assessment.AnswerForm``
        :raise: ``IllegalState`` -- ``answer_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``answer_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``answer_form`` did not originate from ``get_answer_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_answers(self):
        """Tests if this user can delete ``Answers``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Answer`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Answer`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_answer(self, answer_id):
        """Deletes the ``Answer`` identified by the given ``Id``.

        :param answer_id: the ``Id`` of the ``Answer`` to delete
        :type answer_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``Answer`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``answer_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.ItemNotificationSession

    def can_register_for_item_notifications(self):
        """Tests if this user can register for ``Item`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def reliable_item_notifications(self):
        """Reliable notifications are desired.
        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        """
        raise UNIMPLEMENTED()

    def unreliable_item_notifications(self):
        """Unreliable notifications are desired.
        In unreliable mode, notifications do not need to be
        acknowledged.



        """
        raise UNIMPLEMENTED()

    def acknowledge_item_notification(self, notification_id):
        """Acknowledge an item notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_items(self):
        """Register for notifications of new assessment items.
        ``ItemReceiver.newItems()`` is invoked when a new ``Item`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_items(self):
        """Registers for notification of updated assessment items.
        ``ItemReceiver.changedItems()`` is invoked when an assessment
        item is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_item(self, item_id):
        """Registers for notification of an updated assessment item.
        ``ItemReceiver.changedItems()`` is invoked when the specified
        assessment item is changed.

        :param item_id: the ``Id`` of the ``Assessment`` to monitor
        :type item_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``item`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_items(self):
        """Registers for notification of deleted assessment items.
        ``ItemReceiver.deletedItems()`` is invoked when an assessment
        item is removed from the assessment bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_item(self, item_id):
        """Registers for notification of a deleted assessment item.
        ``ItemReceiver.deletedItems()`` is invoked when the specified
        assessment item is removed from the assessment bank.

        :param item_id: the ``Id`` of the ``Item`` to monitor
        :type item_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``Item`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``item_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.ItemBankSession

    def can_lookup_item_bank_mappings(self):
        """Tests if this user can perform lookups of item/bank mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_bank_view(self):
        """A complete view of the ``Item`` and ``Bank`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_item_ids_by_bank(self, bank_id):
        """Gets the list of ``Item``  ``Ids`` associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related item ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_items_by_bank(self, bank_id):
        """Gets the list of ``Items`` associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related items
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_item_ids_by_banks(self, bank_ids):
        """Gets the list of ``Item Ids`` corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        """
        raise UNIMPLEMENTED()

    def get_items_by_banks(self, bank_ids):
        """Gets the list of ``Items`` corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of items
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        """
        raise UNIMPLEMENTED()

    def get_bank_ids_by_item(self, item_id):
        """Gets the list of ``Bank``  ``Ids`` mapped to an ``Item``.

        :param item_id: ``Id`` of an ``Item``
        :type item_id: ``osid.id.Id``
        :return: list of bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``item_id`` is not found
        :raise: ``NullArgument`` -- ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        """
        raise UNIMPLEMENTED()

    def get_banks_by_item(self, item_id):
        """Gets the list of ``Banks`` mapped to an ``Item``.

        :param item_id: ``Id`` of an ``Item``
        :type item_id: ``osid.id.Id``
        :return: list of banks
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- ``item_id`` is not found
        :raise: ``NullArgument`` -- ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.ItemBankAssignmentSession

    def can_assign_items(self):
        """Tests if this user can alter item/bank mappings.
        A return of true does not guarantee successful assessment. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_items_to_bank(self, bank_id):
        """Tests if this user can alter item/bank mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_bank_ids(self, bank_id):
        """Gets a list of banks including and under the given bank node in which any item can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_bank_ids_for_item(self, bank_id, item_id):
        """Gets a list of banks including and under the given bank node in which a specific item can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param item_id: the ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_item_to_bank(self, item_id, bank_id):
        """Adds an existing ``Item`` to a ``Bank``.

        :param item_id: the ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``item_id`` is already assigned to ``bank_id``
        :raise: ``NotFound`` -- ``item_id`` or ``bank_id`` not found
        :raise: ``NullArgument`` -- ``item_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def unassign_item_from_bank(self, item_id, bank_id):
        """Removes an ``Item`` from a ``Bank``.

        :param item_id: the ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``item_id`` or ``bank_id`` not found or ``item_id`` not assigned to ``bank_id``
        :raise: ``NullArgument`` -- ``item_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def reassign_item_to_billing(self, item_id, from_bank_id, to_bank_id):
        """Moves an ``Item`` from one ``Bank`` to another.
        Mappings to other ``Banks`` are unaffected.

        :param item_id: the ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :param from_bank_id: the ``Id`` of the current ``Bank``
        :type from_bank_id: ``osid.id.Id``
        :param to_bank_id: the ``Id`` of the destination ``Bank``
        :type to_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``item_id, from_bank_id,`` or ``to_bank_id`` not found or ``item_id`` not mapped to ``from_bank_id``
        :raise: ``NullArgument`` -- ``item_id, from_bank_id,`` or ``to_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.ItemSmartBankSession

    def can_manage_smart_banks(self):
        """Tests if this user can manage smart banks.
        A return of true does not guarantee successful assessment. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart bank management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_item_query(self, item_query):
        """Applies an item query to this bank.

        :param item_query: the item query
        :type item_query: ``osid.assessment.ItemQuery``
        :raise: ``NullArgument`` -- ``item_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``item_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_item_query(self):
        """Gets an item query inspector for this bank.

        :return: the item query inspector
        :rtype: ``osid.assessment.ItemQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_item_sequencing(self, item_search_order):
        """Applies an item search order to this bank.

        :param item_search_order: the item search order
        :type item_search_order: ``osid.assessment.ItemSearchOrder``
        :raise: ``NullArgument`` -- ``item_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``item_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentLookupSession

    def can_lookup_assessments(self):
        """Tests if this user can perform ``Assessment`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_assessment_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_assessment_view(self):
        """A complete view of the ``Assessment`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_assessment(self, assessment_id):
        """Gets the ``Assessment`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Assessment`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Assessment`` and retained
        for compatibility.

        :param assessment_id: ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :return: the assessment
        :rtype: ``osid.assessment.Assessment``
        :raise: ``NotFound`` -- ``assessment_id`` not found
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_by_ids(self, assessment_ids):
        """Gets an ``AssessmentList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the
        assessments specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Assessments`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param assessment_ids: the list of ``Ids`` to retrieve
        :type assessment_ids: ``osid.id.IdList``
        :return: the returned ``Assessment`` list
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``assessment_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        """
        raise UNIMPLEMENTED()

    def get_assessments_by_genus_type(self, assessment_genus_type):
        """Gets an ``AssessmentList`` corresponding to the given assessment genus ``Type`` which does not include assessments of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments that are accessible through
        this session.

        :param assessment_genus_type: an assessment genus type
        :type assessment_genus_type: ``osid.type.Type``
        :return: the returned ``Assessment`` list
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``NullArgument`` -- ``assessment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_by_parent_genus_type(self, assessment_genus_type):
        """Gets an ``AssessmentList`` corresponding to the given assessment genus ``Type`` and include any additional assessments with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments that are accessible through
        this session.

        :param assessment_genus_type: an assessment genus type
        :type assessment_genus_type: ``osid.type.Type``
        :return: the returned ``Assessment`` list
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``NullArgument`` -- ``assessment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_by_record_type(self, assessment_record_type):
        """Gets an ``AssessmentList`` corresponding to the given assessment record ``Type``.
        The set of assessments implementing the given record type is
        returned. In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments that are accessible through
        this session.

        :param assessment_record_type: an assessment record type
        :type assessment_record_type: ``osid.type.Type``
        :return: the returned ``Assessment`` list
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``NullArgument`` -- ``assessment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments(self):
        """Gets all ``Assessments``.
        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments that are accessible through
        this session.

        :return: a list of ``Assessments``
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    assessments = property(fget=get_assessments)


##
# The following methods are from osid.assessment.AssessmentQuerySession

    def can_search_assessments(self):
        """Tests if this user can perform ``Assessment`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an pplication that may wish not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_assessment_query(self):
        """Gets an assessment query.

        :return: the assessment query
        :rtype: ``osid.assessment.AssessmentQuery``

        """
        raise UNIMPLEMENTED()

    assessment_query = property(fget=get_assessment_query)

    def get_assessments_by_query(self, assessment_query):
        """Gets a list of ``Assessments`` matching the given assessment query.

        :param assessment_query: the assessment query
        :type assessment_query: ``osid.assessment.AssessmentQuery``
        :return: the returned ``AssessmentList``
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``NullArgument`` -- ``assessment_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentSearchSession

    def get_assessment_search(self):
        """Gets an assessment search.

        :return: the assessment search
        :rtype: ``osid.assessment.AssessmentSearch``

        """
        raise UNIMPLEMENTED()

    assessment_search = property(fget=get_assessment_search)

    def get_assessment_search_order(self):
        """Gets an assessment search order.
        The ``AssessmentSearchOrder`` is supplied to an
        ``AssessmentSearch`` to specify the ordering of results.

        :return: the assessment search order
        :rtype: ``osid.assessment.AssessmentSearchOrder``

        """
        raise UNIMPLEMENTED()

    assessment_search_order = property(fget=get_assessment_search_order)

    def get_assessments_by_search(self, assessment_query, assessment_search):
        """Gets the search results matching the given search query using the given search.

        :param assessment_query: the assessment query
        :type assessment_query: ``osid.assessment.AssessmentQuery``
        :param assessment_search: the assessment search
        :type assessment_search: ``osid.assessment.AssessmentSearch``
        :return: the search results
        :rtype: ``osid.assessment.AssessmentSearchResults``
        :raise: ``NullArgument`` -- ``assessment_query`` or ``assessment_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_query`` or ``assessment_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_assessment_query_from_inspector(self, assessment_query_inspector):
        """Gets an assessment query from an inspector.
        The inspector is available from an ``AssessmentSearchResults``.

        :param assessment_query_inspector: an assessment query inspector
        :type assessment_query_inspector: ``osid.assessment.AssessmentQueryInspector``
        :return: the assessment query
        :rtype: ``osid.assessment.AssessmentQuery``
        :raise: ``NullArgument`` -- ``assessment_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``assessment_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentAdminSession

    def can_create_assessments(self):
        """Tests if this user can create ``Assessments``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``Assessment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Assessment`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_assessment_with_record_types(self, assessment_record_types):
        """Tests if this user can create a single ``Assessment`` using the desired record interface types.
        While ``AssessmentManager.getAssessmentRecordTypes()`` can be
        used to examine which record interfaces are supported, this
        method tests which record(s) are required for creating a
        specific ``Assessment``. Providing an empty array tests if an
        ``Assessment`` can be created with no records.

        :param assessment_record_types: array of assessment record types
        :type assessment_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Assessment`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assessment_form_for_create(self, assessment_record_types):
        """Gets the assessment form for creating new assessments.
        A new form should be requested for each create transaction.

        :param assessment_record_types: array of assessment record types to be included in the create operation or an empty list if none
        :type assessment_record_types: ``osid.type.Type[]``
        :return: the assessment form
        :rtype: ``osid.assessment.AssessmentForm``
        :raise: ``NullArgument`` -- ``assessment_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_assessment(self, assessment_form):
        """Creates a new ``Assessment``.

        :param assessment_form: the form for this ``Assessment``
        :type assessment_form: ``osid.assessment.AssessmentForm``
        :return: the new ``Assessment``
        :rtype: ``osid.assessment.Assessment``
        :raise: ``IllegalState`` -- ``assessment_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``assessment_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_form`` did not originate from ``get_assessment_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_assessments(self):
        """Tests if this user can update ``Assessments``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Assessment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``Assessment`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_assessment_form_for_update(self, assessment_id):
        """Gets the assessment form for updating an existing assessment.
        A new assessment form should be requested for each update
        transaction.

        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :return: the assessment form
        :rtype: ``osid.assessment.AssessmentForm``
        :raise: ``NotFound`` -- ``assessment_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def update_assessment(self, assessment_form):
        """Updates an existing assessment.

        :param assessment_form: the form containing the elements to be updated
        :type assessment_form: ``osid.assessment.AssessmentForm``
        :raise: ``IllegalState`` -- ``assessment_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``assessment_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_form did not originate from get_assessment_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_assessments(self):
        """Tests if this user can delete ``Assessments``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Assessment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Assessment`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_assessment(self, assessment_id):
        """Deletes an ``Assessment``.

        :param assessment_id: the ``Id`` of the ``Assessment`` to remove
        :type assessment_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_id`` not found
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def can_manage_assessment_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Assessments``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Assessment`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_assessment(self, assessment_id, alias_id):
        """Adds an ``Id`` to an ``Assessment`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Assessment`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another assessment, it is reassigned
        to the given assessment ``Id``.

        :param assessment_id: the ``Id`` of an ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``assessment_id`` not found
        :raise: ``NullArgument`` -- ``assessment_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentNotificationSession

    def can_register_for_assessment_notifications(self):
        """Tests if this user can register for ``Assessment`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def reliable_assessment_notifications(self):
        """Reliable notifications are desired.
        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_assessment_notification()`` .



        """
        raise UNIMPLEMENTED()

    def unreliable_assessment_notifications(self):
        """Unreliable notifications are desired.
        In unreliable mode, notifications do not need to be
        acknowledged.



        """
        raise UNIMPLEMENTED()

    def acknowledge_assessment_notification(self, notification_id):
        """Acknowledge an assessment notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_assessments(self):
        """Register for notifications of new assessments.
        ``AssessmentReceiver.newAssessments()`` is invoked when a new
        ``Assessment`` appears in this assessment bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_assessments(self):
        """Registers for notification of updated assessments.
        ``AssessmentReceiver.changedAssessments()`` is invoked when an
        assessment in this assessment bank is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_assessment(self, assessment_id):
        """Registers for notification of an updated assessment.
        ``AssessmentReceiver.changedAssessments()`` is invoked when the
        specified assessment in this assessment bank is changed.

        :param assessment_id: the ``Id`` of the ``Assessment`` to monitor
        :type assessment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_assessments(self):
        """Registers for notification of deleted assessments.
        ``AssessmentReceiver.deletedAssessments()`` is invoked when an
        assessment is removed from this assessment bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_assessment(self, assessment_id):
        """Registers for notification of a deleted assessment.
        ``AssessmentReceiver.deletedAssessments()`` is invoked when the
        specified assessment is removed from this assessment bank.

        :param assessment_id: the ``Id`` of the ``Assessment`` to monitor
        :type assessment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentBankSession

    def can_lookup_assessment_bank_mappings(self):
        """Tests if this user can perform lookups of assessment/bank mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_assessment_ids_by_bank(self, bank_id):
        """Gets the list of ``Assessment``  ``Ids`` associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related assessment ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_by_bank(self, bank_id):
        """Gets the list of ``Assessments`` associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related assessments
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessment_ids_by_banks(self, bank_ids):
        """Gets the list of ``Assessment Ids`` corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_by_banks(self, bank_ids):
        """Gets the list of ``Assessments`` corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of assessments
        :rtype: ``osid.assessment.AssessmentList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_bank_ids_by_assessment(self, assessment_id):
        """Gets the list of ``Bank``  ``Ids`` mapped to an ``Assessment``.

        :param assessment_id: ``Id`` of an ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :return: list of bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``assessment_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_banks_by_assessment(self, assessment_id):
        """Gets the list of ``Banks`` mapped to an ``Assessment``.

        :param assessment_id: ``Id`` of an ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :return: list of banks
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- ``assessment_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentBankAssignmentSession

    def can_assign_assessments(self):
        """Tests if this user can alter assessment/bank mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_assessments_to_bank(self, bank_id):
        """Tests if this user can alter assessment/bank mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_bank_ids_for_assessment(self, bank_id, assessment_id):
        """Gets a list of bank including and under the given bank node in which a specific assessment can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` or ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_assessment_to_bank(self, assessment_id, bank_id):
        """Adds an existing ``Assessment`` to a ``Bank``.

        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``assessment_id`` is already assigned to ``bank_id``
        :raise: ``NotFound`` -- ``assessment_id`` or ``bank_id`` not found
        :raise: ``NullArgument`` -- ``assessment_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def unassign_assessment_from_bank(self, assessment_id, bank_id):
        """Removes an ``Assessment`` from a ``Bank``.

        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_id`` or ``bank_id`` not found or ``assessment_id`` not assigned to ``bank_id``
        :raise: ``NullArgument`` -- ``assessment_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def reassign_assessment_to_billing(self, assessment_id, from_bank_id, to_bank_id):
        """Moves an ``Assessment`` from one ``Bank`` to another.
        Mappings to other ``Banks`` are unaffected.

        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param from_bank_id: the ``Id`` of the current ``Bank``
        :type from_bank_id: ``osid.id.Id``
        :param to_bank_id: the ``Id`` of the destination ``Bank``
        :type to_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_id, from_bank_id,`` or ``to_bank_id`` not found or ``assessment_id`` not mapped to ``from_bank_id``
        :raise: ``NullArgument`` -- ``assessment_id, from_bank_id,`` or ``to_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentSmartBankSession

    def apply_assessment_query(self, assessment_query):
        """Applies an assessment query to this bank.

        :param assessment_query: the assessment query
        :type assessment_query: ``osid.assessment.AssessmentQuery``
        :raise: ``NullArgument`` -- ``assessment_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_assessment_query(self):
        """Gets an assessment query inspector for this bank.

        :return: the assessment query inspector
        :rtype: ``osid.assessment.AssessmentQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_assessment_sequencing(self, assessment_search_order):
        """Applies an assessment search order to this bank.

        :param assessment_search_order: the assessment search order
        :type assessment_search_order: ``osid.assessment.AssessmentSearchOrder``
        :raise: ``NullArgument`` -- ``assessment_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentBasicAuthoringSession

    def can_author_assessments(self):
        """Tests if this user can author assessments.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        authoring operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_item(self, assessment_id, item_id):
        """Adds an existing ``Item`` to an assessment.

        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param item_id: the ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_id`` or ``item_id`` not found
        :raise: ``NullArgument`` -- ``assessment_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def remove_item(self, assessment_id, item_id):
        """Removes an ``Item`` from this assessment.

        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param item_id: the ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_id`` or ``item_id`` not found or ``item_id`` not on ``assessmentid``
        :raise: ``NullArgument`` -- ``assessment_id`` or ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def move_item(self, assessment_id, item_id, preceeding_item_id):
        """Moves an existing item to follow another item in an assessment.

        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param item_id: the ``Id`` of an ``Item``
        :type item_id: ``osid.id.Id``
        :param preceeding_item_id: the ``Id`` of a preceeding ``Item`` in the sequence
        :type preceeding_item_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_id`` is not found, or ``item_id`` or ``preceeding_item_id`` not on ``assessment_id``
        :raise: ``NullArgument`` -- ``assessment_id, item_id`` or ``preceeding_item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def order_items(self, item_ids, assessment_id):
        """Sequences existing items in an assessment.

        :param item_ids: the ``Id`` of the ``Items``
        :type item_ids: ``osid.id.Id[]``
        :param assessment_id: the ``Id`` of the ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_id`` is not found or an ``item_id`` is not on ``assessment_id``
        :raise: ``NullArgument`` -- ``assessment_id`` or ``item_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentOfferedLookupSession

    def can_lookup_assessments_offered(self):
        """Tests if this user can perform ``AssessmentOffered`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_assessment_offered_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_assessment_offered_view(self):
        """A complete view of the ``AssessmentOffered`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_assessment_offered(self, assessment_offered_id):
        """Gets the ``AssessmentOffered`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``AssessmentOffered`` may have
        a different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``AssessmentOffered`` and
        retained for compatibility.

        :param assessment_offered_id: ``Id`` of the ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :return: the assessment offered
        :rtype: ``osid.assessment.AssessmentOffered``
        :raise: ``NotFound`` -- ``assessment_offered_id`` not found
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_offered_by_ids(self, assessment_offered_ids):
        """Gets an ``AssessmentOfferedList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the
        assessments specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``AssessmentOffered`` objects may be omitted from
        the list and may present the elements in any order including
        returning a unique set.

        :param assessment_offered_ids: the list of ``Ids`` to retrieve
        :type assessment_offered_ids: ``osid.id.IdList``
        :return: the returned ``AssessmentOffered`` list
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``assessment_offered_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        """
        raise UNIMPLEMENTED()

    def get_assessments_offered_by_genus_type(self, assessment_offered_genus_type):
        """Gets an ``AssessmentOfferedList`` corresponding to the given assessment offered genus ``Type`` which does not include assessments of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        :param assessment_offered_genus_type: an assessment offered genus type
        :type assessment_offered_genus_type: ``osid.type.Type``
        :return: the returned ``AssessmentOffered`` list
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``NullArgument`` -- ``assessment_offered_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_offered_by_parent_genus_type(self, assessment_offered_genus_type):
        """Gets an ``AssessmentOfferedList`` corresponding to the given assessment offered genus ``Type`` and include any additional assessments with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments offered that are accessible
        through this session.

        :param assessment_offered_genus_type: an assessment offered genus type
        :type assessment_offered_genus_type: ``osid.type.Type``
        :return: the returned ``AssessmentOffered`` list
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``NullArgument`` -- ``assessment_offered_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_offered_by_record_type(self, assessment_record_type):
        """Gets an ``AssessmentOfferedList`` corresponding to the given assessment offered record ``Type``.
        The set of assessments implementing the given record type is
        returned. In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        :param assessment_record_type: an assessment offered record type
        :type assessment_record_type: ``osid.type.Type``
        :return: the returned ``AssessmentOffered`` list
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``NullArgument`` -- ``assessment_offered_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_offered_by_date(self, start, end):
        """Gets an ``AssessmentOfferedList`` that have designated start times where the start times fall in the given range inclusive.
        In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        :param start: start of time range
        :type start: ``osid.calendaring.DateTime``
        :param end: end of time range
        :type end: ``osid.calendaring.DateTime``
        :return: the returned ``AssessmentOffered`` list
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_offered_for_assessment(self, assessment_id):
        """Gets an ``AssessmentOfferedList`` by the given assessment.
        In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        :param assessment_id: ``Id`` of an ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :return: the returned ``AssessmentOffered`` list
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_offered(self):
        """Gets all ``AssessmentOffered`` elements.
        In plenary mode, the returned list contains all known
        assessments offered or an error results. Otherwise, the returned
        list may contain only those assessments offered that are
        accessible through this session.

        :return: a list of ``AssessmentOffered`` elements
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    assessments_offered = property(fget=get_assessments_offered)


##
# The following methods are from osid.assessment.AssessmentOfferedQuerySession

    def can_search_assessments_offered(self):
        """Tests if this user can perform ``AssessmentOffered`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may wish not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_query(self):
        """Gets an assessment offered query.

        :return: the assessment offered query
        :rtype: ``osid.assessment.AssessmentOfferedQuery``

        """
        raise UNIMPLEMENTED()

    assessment_offered_query = property(fget=get_assessment_offered_query)

    def get_assessments_offered_by_query(self, assessment_offered_query):
        """Gets a list of ``AssessmentOffered`` elements matching the given assessment offered query.

        :param assessment_offered_query: the assessment offered query
        :type assessment_offered_query: ``osid.assessment.AssessmentOfferedQuery``
        :return: the returned ``AssessmentOfferedList``
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``NullArgument`` -- ``assessment_offered_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_offered_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentOfferedSearchSession

    def get_assessment_offered_search(self):
        """Gets an assessment offered search.

        :return: the assessment offered search
        :rtype: ``osid.assessment.AssessmentOfferedSearch``

        """
        raise UNIMPLEMENTED()

    assessment_offered_search = property(fget=get_assessment_offered_search)

    def get_assessment_offered_search_order(self):
        """Gets an assessment offered search order.
        The ``AssessmentOfferedSearchOrder`` is supplied to an
        ``AssessmentOfferedSearch`` to specify the ordering of results.

        :return: the assessment offered search order
        :rtype: ``osid.assessment.AssessmentOfferedSearchOrder``

        """
        raise UNIMPLEMENTED()

    assessment_offered_search_order = property(fget=get_assessment_offered_search_order)

    def get_assessments_offered_by_search(self, assessment_offered_query, assessment_offered_search):
        """Gets the search results matching the given search query using the given search.

        :param assessment_offered_query: the assessment offered query
        :type assessment_offered_query: ``osid.assessment.AssessmentOfferedQuery``
        :param assessment_offered_search: the assessment offered search
        :type assessment_offered_search: ``osid.assessment.AssessmentOfferedSearch``
        :return: the assessment offered search results
        :rtype: ``osid.assessment.AssessmentOfferedSearchResults``
        :raise: ``NullArgument`` -- ``assessment_offered_query`` or ``assessment_offered_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_offered_query`` or ``assessment_offered_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_query_from_inspector(self, assessment_offered_query_inspector):
        """Gets an assessment offered query from an inspector.
        The inspector is available from an
        ``AssessmentOfferedSearchResults``.

        :param assessment_offered_query_inspector: an assessment offered query inspector
        :type assessment_offered_query_inspector: ``osid.assessment.AssessmentOfferedQueryInspector``
        :return: the assessment offered query
        :rtype: ``osid.assessment.AssessmentOfferedQuery``
        :raise: ``NullArgument`` -- ``assessment_offered_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``assessment_offered_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentOfferedAdminSession

    def can_create_assessments_offered(self):
        """Tests if this user can create ``AssessmentOffered`` objects.
        A return of true does not guarantee successful authoriization. A
        return of false indicates that it is known creating an
        ``AssessmentOffered`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer create operations to an unauthorized user.

        :return: ``false`` if ``AssessmentOffered`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_assessment_offered_with_record_types(self, assessment_offered_record_types):
        """Tests if this user can create a single ``AssessmentOffered`` using the desired record types.
        While ``AssessmentManager.getAssessmentOfferedRecordTypes()``
        can be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``AssessmentOffered``. Providing an empty array tests if an
        ``AssessmentOffered`` can be created with no records.

        :param assessment_offered_record_types: array of assessment offered record types
        :type assessment_offered_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``AssessmentOffered`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_offered_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_form_for_create(self, assessment_id, assessment_offered_record_types):
        """Gets the assessment offered form for creating new assessments offered.
        A new form should be requested for each create transaction.

        :param assessment_id: the ``Id`` of the related ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param assessment_offered_record_types: array of assessment offered record types to be included in the create operation or an empty list if none
        :type assessment_offered_record_types: ``osid.type.Type[]``
        :return: the assessment offered form
        :rtype: ``osid.assessment.AssessmentOfferedForm``
        :raise: ``NotFound`` -- ``assessment_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_id`` or ``assessment_offered_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_assessment_offered(self, assessment_offered_form):
        """Creates a new ``AssessmentOffered``.

        :param assessment_offered_form: the form for this ``AssessmentOffered``
        :type assessment_offered_form: ``osid.assessment.AssessmentOfferedForm``
        :return: the new ``AssessmentOffered``
        :rtype: ``osid.assessment.AssessmentOffered``
        :raise: ``IllegalState`` -- ``assessment_offrered_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``assessment_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_form`` did not originate from ``get_assessment_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_assessments_offered(self):
        """Tests if this user can update ``AssessmentOffered`` objects.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``AssessmentOffered`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: ``false`` if ``Assessment`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_form_for_update(self, assessment_offered_id):
        """Gets the assessment offered form for updating an existing assessment offered.
        A new assessment offered form should be requested for each
        update transaction.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :return: the assessment offered form
        :rtype: ``osid.assessment.AssessmentOfferedForm``
        :raise: ``NotFound`` -- ``assessment_offered_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def update_assessment_offered(self, assessment_offered_form):
        """Updates an existing assessment offered.

        :param assessment_offered_form: the form containing the elements to be updated
        :type assessment_offered_form: ``osid.assessment.AssessmentOfferedForm``
        :raise: ``IllegalState`` -- ``assessment_offrered_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``assessment_offered_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_form`` did not originate from ``get_assessment_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_assessments_offered(self):
        """Tests if this user can delete ``AssessmentsOffered``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``AssessmentOffered`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer a delete operations to unauthorized users.

        :return: ``false`` if ``AssessmentOffered`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_assessment_offered(self, assessment_offered_id):
        """Deletes an ``AssessmentOffered``.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered`` to remove
        :type assessment_offered_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_offered_id`` not found
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def can_manage_assessment_offered_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``AssessmentsOffered``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``AssessmentOffered`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_assessment_offered(self, assessment_offered_id, alias_id):
        """Adds an ``Id`` to an ``AssessmentOffered`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``AssessmentOffered`` is determined by
        the provider. The new ``Id`` is an alias to the primary ``Id``.
        If the alias is a pointer to another assessment offered, it is
        reassigned to the given assessment offered ``Id``.

        :param assessment_offered_id: the ``Id`` of an ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``assessment_offered_id`` not found
        :raise: ``NullArgument`` -- ``assessment_offered_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentOfferedNotificationSession

    def can_register_for_assessment_offered_notifications(self):
        """Tests if this user can register for ``AssessmentOffered`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def reliable_assessment_offered_notifications(self):
        """Reliable notifications are desired.
        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_assessment_offered_notification()`` .



        """
        raise UNIMPLEMENTED()

    def unreliable_assessment_offered_notifications(self):
        """Unreliable notifications are desired.
        In unreliable mode, notifications do not need to be
        acknowledged.



        """
        raise UNIMPLEMENTED()

    def acknowledge_assessment_offered_notification(self, notification_id):
        """Acknowledge an assessment offered notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_assessments_offered(self):
        """Register for notifications of new assessments offered.
        ``AssessmentOfferedReceiver.newAssessmentsOffered()`` is invoked
        when a new ``AssessmentOffered`` appears in this assessmen
        tbank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_new_assessments_offered_for_assessment(self, assessment_id):
        """Register for notifications of new assessments offered by assessment.
        ``AssessmentOfferedReceiver.newAssessmentsOffered()`` is invoked
        when a new ``AssessmentOffered`` appears in this assessment
        bank.

        :param assessment_id: ``Id`` of an assessment to monitor
        :type assessment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_assessments_offered(self):
        """Registers for notification of updated assessments offered.
        ``AssessmentOfferedReceiver.changedAssessmentsOffered()`` is
        invoked when an assessment offered in this assessment bank is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_assessments_offered_for_assessment(self, assessment_id):
        """Register for notifications of updated assessments offered by assessment.
        ``AssessmentOfferedReceiver.changedAssessmentsOffered()`` is
        invoked when an ``AssessmentOffered`` in this assessment bank is
        changed.

        :param assessment_id: ``Id`` of an assessment to monitor
        :type assessment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_assessment_offered(self, assessment_offered_id):
        """Registers for notification of an updated assessment offered.
        ``AssessmentOfferedReceiver.changedAssessmentsOffered()`` is
        invoked when the specified assessment offered in this assessment
        bank is changed.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered`` to monitor
        :type assessment_offered_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_assessments_offered(self):
        """Registers for notification of deleted assessments offered.
        ``AssessmentOfferedReceiver.deletedAssessmentsOffered()`` is
        invoked when an assessment offered is removed from the
        assessment bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_assessments_offered_for_assessment(self, assessment_id):
        """Register for notifications of deleted assessments offered by assessment.
        ``AssessmentOfferedReceiver.deletedAssessmenstOffered()`` is
        invoked when an ``AssessmentOffered`` is removed form the
        assessment bank.

        :param assessment_id: ``Id`` of an assessment to monitor
        :type assessment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_assessment_offered(self, assessment_offered_id):
        """Registers for notification of a deleted assessment offered.
        ``AssessmentOfferedReceiver.deletedAssessmentsOffered()`` is
        invoked when the specified assessment offered is removed from
        the assessment bank.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered`` to monitor
        :type assessment_offered_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentOfferedBankSession

    def can_lookup_assessment_offered_bank_mappings(self):
        """Tests if this user can perform lookups of assessment offered/bank mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_ids_by_bank(self, bank_id):
        """Gets the list of ``AssessmentOffered``  ``Ids`` associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related assessment offered ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_offered_by_bank(self, bank_id):
        """Gets the list of ``AssessmentOffereds`` associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related assessments offered
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessment_offered_ids_by_banks(self, bank_ids):
        """Gets the list of ``AssessmentOffered Ids`` corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_offered_by_banks(self, bank_ids):
        """Gets the list of ``AssessmentOffered`` objects corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of assessments offered
        :rtype: ``osid.assessment.AssessmentOfferedList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_bank_ids_by_assessment_offered(self, assessment_offered_id):
        """Gets the list of ``Bank``  ``Ids`` mapped to an ``AssessmentOffered``.

        :param assessment_offered_id: ``Id`` of an ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :return: list of bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``assessment_offered_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_banks_by_assessment_offered(self, assessment_offered_id):
        """Gets the list of ``Banks`` mapped to an ``AssessmentOffered``.

        :param assessment_offered_id: ``Id`` of an ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :return: list of banks
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- ``assessment_offered_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentOfferedBankAssignmentSession

    def can_assign_assessments_offered(self):
        """Tests if this user can alter assessment offered/bank mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_assessments_offered_to_bank(self, bank_id):
        """Tests if this user can alter assessment offered/bank mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_bank_ids_for_assessment_offered(self, bank_id, assessment_offered_id):
        """Gets a list of bank including and under the given bank node in which a specific assessment offered can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` or ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_assessment_offered_to_bank(self, assessment_offered_id, bank_id):
        """Adds an existing ``AssessmentOffered`` to a ``Bank``.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``assessment_offered_id`` is already assigned to ``bank_id``
        :raise: ``NotFound`` -- ``assessment_offered_id`` or ``bank_id`` not found
        :raise: ``NullArgument`` -- ``assessment_offered_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def unassign_assessment_offered_from_bank(self, assessment_offered_id, bank_id):
        """Removes an ``AssessmentOffered`` from a ``Bank``.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_offered_id`` or ``bank_id`` not found or ``assessment_offered_id`` not assigned to ``bank_id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def reassign_assessment_offered_to_billing(self, assessment_offered_id, from_bank_id, to_bank_id):
        """Moves an ``AssessmentOffered`` from one ``Bank`` to another.
        Mappings to other ``Banks`` are unaffected.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :param from_bank_id: the ``Id`` of the current ``Bank``
        :type from_bank_id: ``osid.id.Id``
        :param to_bank_id: the ``Id`` of the destination ``Bank``
        :type to_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_offered_id, from_bank_id,`` or ``to_bank_id`` not found or ``assessment_offered_id`` not mapped to ``from_bank_id``
        :raise: ``NullArgument`` -- ``assessment_offered_id, from_bank_id,`` or ``to_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentOfferedSmartBankSession

    def apply_assessment_offered_query(self, assessment_offered_query):
        """Applies an assessment offered query to this bank.

        :param assessment_offered_query: the assessment offered query
        :type assessment_offered_query: ``osid.assessment.AssessmentOfferedQuery``
        :raise: ``NullArgument`` -- ``assessment_offered_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_offered_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_assessment_offered_query(self):
        """Gets an assessment offered query inspector for this bank.

        :return: the assessment offered query inspector
        :rtype: ``osid.assessment.AssessmentOfferedQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_assessment_offered_sequencing(self, assessment_offered_search_order):
        """Applies an assessment offered search order to this bank.

        :param assessment_offered_search_order: the assessment offered search order
        :type assessment_offered_search_order: ``osid.assessment.AssessmentOfferedSearchOrder``
        :raise: ``NullArgument`` -- ``assessment_offered_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_offered_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentTakenLookupSession

    def can_lookup_assessments_taken(self):
        """Tests if this user can perform ``AssessmentTaken`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_assessment_taken_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as assessment, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_assessment_taken_view(self):
        """A complete view of the ``AssessmentTaken`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_assessment_taken(self, assessment_taken_id):
        """Gets the ``AssessmentTaken`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``AssessmentTaken`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``AssessmentTaken`` and
        retained for compatibility.

        :param assessment_taken_id: ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: the assessment taken
        :rtype: ``osid.assessment.AssessmentTaken``
        :raise: ``NotFound`` -- ``assessment_taken_id`` not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken_by_ids(self, assessment_taken_ids):
        """Gets an ``AssessmentTakenList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the
        assessments specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``AssessmentTaken`` objects may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :param assessment_taken_ids: the list of ``Ids`` to retrieve
        :type assessment_taken_ids: ``osid.id.IdList``
        :return: the returned ``AssessmentTaken list``
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``assessment_taken_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- assessment failure

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken_by_genus_type(self, assessment_taken_genus_type):
        """Gets an ``AssessmentTakenList`` corresponding to the given assessment taken genus ``Type`` which does not include assessments of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param assessment_taken_genus_type: an assessment taken genus type
        :type assessment_taken_genus_type: ``osid.type.Type``
        :return: the returned ``AssessmentTaken list``
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``assessment_taken_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken_by_parent_genus_type(self, assessment_taken_genus_type):
        """Gets an ``AssessmentTakenList`` corresponding to the given assessment taken genus ``Type`` and include any additional assessments with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        assessments or an error results. Otherwise, the returned list
        may contain only those assessments taken that are accessible
        through this session.

        :param assessment_taken_genus_type: an assessment taken genus type
        :type assessment_taken_genus_type: ``osid.type.Type``
        :return: the returned ``AssessmentTaken list``
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``assessment_taken_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken_by_record_type(self, assessment_taken_record_type):
        """Gets an ``AssessmentTakenList`` corresponding to the given assessment taken record ``Type``.
        The set of assessments implementing the given record type is
        returned. In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session. In both cases, the order of the
        set is not specified.

        :param assessment_taken_record_type: an assessment taken record type
        :type assessment_taken_record_type: ``osid.type.Type``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``assessment_taken_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken_by_date(self, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive.
        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session. In both cases, the order of the
        set is not specified.

        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken_for_taker(self, resource_id):
        """Gets an ``AssessmentTakenList`` for the given resource.
        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken_by_date_for_taker(self, resource_id, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given resource.
        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken_for_assessment(self, assessment_id):
        """Gets an ``AssessmentTakenList`` for the given assessment.
        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param assessment_id: ``Id`` of an ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken_by_date_for_assessment(self, assessment_id, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given assessment.
        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param assessment_id: ``Id`` of an ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``assessment_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken_for_taker_and_assessment(self, resource_id, assessment_id):
        """Gets an ``AssessmentTakenList`` for the given resource and assessment.
        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :param assessment_id: ``Id`` of an ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``resource_id`` or ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken_by_date_for_taker_and_assessment(self, resource_id, assessment_id, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given resource and assessment.
        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :param assessment_id: ``Id`` of an ``Assessment``
        :type assessment_id: ``osid.id.Id``
        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, assessment_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken_for_assessment_offered(self, assessment_offered_id):
        """Gets an ``AssessmentTakenList`` by the given assessment offered.
        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param assessment_offered_id: ``Id`` of an ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken_by_date_for_assessment_offered(self, assessment_offered_id, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given assessment offered.
        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param assessment_offered_id: ``Id`` of an ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``assessment_offered_id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken_for_taker_and_assessment_offered(self, resource_id, assessment_offered_id):
        """Gets an ``AssessmentTakenList`` for the given resource and assessment offered.
        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :param assessment_offered_id: ``Id`` of an ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``resource_id`` or ``assessmen_offeredt_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken_by_date_for_taker_and_assessment_offered(self, resource_id, assessment_offered_id, from_, to):
        """Gets an ``AssessmentTakenList`` started in the given date range inclusive for the given resource and assessment offered.
        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :param assessment_offered_id: ``Id`` of an ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``AssessmentTaken`` list
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, assessment_offered_id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken(self):
        """Gets all ``AssessmentTaken`` elements.
        In plenary mode, the returned list contains all known
        assessments taken or an error results. Otherwise, the returned
        list may contain only those assessments taken that are
        accessible through this session.

        :return: a list of ``AssessmentTaken`` elements
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    assessments_taken = property(fget=get_assessments_taken)


##
# The following methods are from osid.assessment.AssessmentTakenQuerySession

    def can_search_assessments_taken(self):
        """Tests if this user can perform ``AssessmentTaken`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_query(self):
        """Gets an assessment taken query.

        :return: the assessment taken query
        :rtype: ``osid.assessment.AssessmentTakenQuery``

        """
        raise UNIMPLEMENTED()

    assessment_taken_query = property(fget=get_assessment_taken_query)

    def get_assessments_taken_by_query(self, assessment_taken_query):
        """Gets a list of ``AssessmentTaken`` elements matching the given assessment taken query.

        :param assessment_taken_query: the assessment taken query
        :type assessment_taken_query: ``osid.assessment.AssessmentTakenQuery``
        :return: the returned ``AssessmentTakenList``
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``assessment_taken_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_taken_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentTakenSearchSession

    def get_assessment_taken_search(self):
        """Gets an assessment taken search.

        :return: the assessment taken search
        :rtype: ``osid.assessment.AssessmentTakenSearch``

        """
        raise UNIMPLEMENTED()

    assessment_taken_search = property(fget=get_assessment_taken_search)

    def get_assessment_taken_search_order(self):
        """Gets an assessment taken search order.
        The ``AssessmentTakenSearchOrder`` is supplied to an
        ``AssessmentTakenSearch`` to specify the ordering of results.

        :return: the assessment taken search order
        :rtype: ``osid.assessment.AssessmentTakenSearchOrder``

        """
        raise UNIMPLEMENTED()

    assessment_taken_search_order = property(fget=get_assessment_taken_search_order)

    def get_assessments_taken_by_search(self, assessment_taken_query, assessment_taken_search):
        """Gets the search results matching the given search query using the given assessment taken query.

        :param assessment_taken_query: the assessment taken query
        :type assessment_taken_query: ``osid.assessment.AssessmentTakenQuery``
        :param assessment_taken_search: the assessment taken search
        :type assessment_taken_search: ``osid.assessment.AssessmentTakenSearch``
        :return: the assessment taken search results
        :rtype: ``osid.assessment.AssessmentTakenSearchResults``
        :raise: ``NullArgument`` -- ``assessment_taken_query`` or ``assessment_taken_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_taken_query`` or ``assessment_taken_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_query_from_inspector(self, assessment_taken_query_inspector):
        """Gets an assessment taken query from an inspector.
        The inspector is available from an
        ``AssessmentTakenSearchResults``.

        :param assessment_taken_query_inspector: an assessment taken query inspector
        :type assessment_taken_query_inspector: ``osid.assessment.AssessmentTakenQueryInspector``
        :return: the assessment taken query
        :rtype: ``osid.assessment.AssessmentTakenQuery``
        :raise: ``NullArgument`` -- ``assessment_taken_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``assessment_taken_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentTakenAdminSession

    def can_create_assessments_taken(self):
        """Tests if this user can create ``AssessmentTaken`` objects.
        A return of true does not guarantee successful authoriization. A
        return of false indicates that it is known creating an
        ``AssessmentTaken`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer create operations to an unauthorized user.

        :return: ``false`` if ``AssessmentTaken`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_assessment_taken_with_record_types(self, assessment_taken_record_types):
        """Tests if this user can create a single ``AssessmentTaken`` using the desired record types.
        While ``AssessmentManager.getAssessmentTakenRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``AssessmentTaken``. Providing an empty array tests if an
        ``AssessmentTaken`` can be created with no records.

        :param assessment_taken_record_types: array of assessment taken record types
        :type assessment_taken_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``AssessmentTaken`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_taken_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_form_for_create(self, assessment_offered_id, assessment_taken_record_types):
        """Gets the assessment taken form for creating new assessments taken.
        A new form should be requested for each create transaction.

        :param assessment_offered_id: the ``Id`` of the related ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``
        :param assessment_taken_record_types: array of assessment taken record types to be included in the create operation or an empty list if none
        :type assessment_taken_record_types: ``osid.type.Type[]``
        :return: the assessment taken form
        :rtype: ``osid.assessment.AssessmentTakenForm``
        :raise: ``NotFound`` -- ``assessment_offered_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_offered_id`` or ``assessment_taken_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_assessment_taken(self, assessment_taken_form):
        """Creates a new ``AssessmentTaken``.

        :param assessment_taken_form: the form for this ``AssessmentTaken``
        :type assessment_taken_form: ``osid.assessment.AssessmentForm``
        :return: the new ``AssessmentTaken``
        :rtype: ``osid.assessment.AssessmentTaken``
        :raise: ``IllegalState`` -- ``assessment_taken_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``assessment_taken_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_offered_form`` did not originate from ``get_assessment_taken_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_assessments_taken(self):
        """Tests if this user can update ``AssessmentTaken`` objects.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``AssessmentTaken`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: ``false`` if ``AssessmentTaken`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_form_for_update(self, assessment_taken_id):
        """Gets the assessment taken form for updating an existing assessment taken.
        A new assessment taken form should be requested for each update
        transaction.

        :param assessment_taken_id: the ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: the assessment taken form
        :rtype: ``osid.assessment.AssessmentTakenForm``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def update_assessment_taken(self, assessment_taken_form):
        """Updates an existing assessment taken.

        :param assessment_taken_form: the form containing the elements to be updated
        :type assessment_taken_form: ``osid.assessment.AssessmentTakenForm``
        :raise: ``IllegalState`` -- ``assessment_taken_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``assessment_taken_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_offered_form`` did not originate from ``get_assessment_taken_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_assessments_taken(self):
        """Tests if this user can delete ``AssessmentsTaken``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``AssessmentTaken`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer a delete operations to unauthorized users.

        :return: ``false`` if ``AssessmentTaken`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_assessment_taken(self, assessment_taken_id):
        """Deletes an ``AssessmentTaken``.

        :param assessment_taken_id: the ``Id`` of the ``AssessmentTaken`` to remove
        :type assessment_taken_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_taken_id`` not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def can_manage_assessment_taken_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``AssessmentsTaken``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``AssessmentTaken`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_assessment_taken(self, assessment_taken_id, alias_id):
        """Adds an ``Id`` to an ``AssessmentTaken`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``AssessmentTaken`` is determined by
        the provider. The new ``Id`` is an alias to the primary ``Id``.
        If the alias is a pointer to another assessment taken, it is
        reassigned to the given assessment taken ``Id``.

        :param assessment_taken_id: the ``Id`` of an ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``assessment_taken_id`` not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentTakenNotificationSession

    def can_register_for_assessment_taken_notifications(self):
        """Tests if this user can register for ``AssessmentTaken`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def reliable_assessment_taken_notifications(self):
        """Reliable notifications are desired.
        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_assessment_taken_notification()`` .



        """
        raise UNIMPLEMENTED()

    def unreliable_assessment_taken_notifications(self):
        """Unreliable notifications are desired.
        In unreliable mode, notifications do not need to be
        acknowledged.



        """
        raise UNIMPLEMENTED()

    def acknowledge_assessment_taken_notification(self, notification_id):
        """Acknowledge an assessment taken notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_assessments_taken(self):
        """Register for notifications of new assessments taken in this assessment bank.
        ``AssessmentTakenReceiver.newAssessmentsTaken()`` is invoked
        when a new ``AssessmentTaken`` appears in this assessment bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_new_assessments_taken_for_taker(self, resource_id):
        """Register for notifications of new assessments taken for a resource.
        ``AssessmentTakenReceiver.newAssessmenstTaken()`` is invoked
        when a new ``AssessmentTaken`` appears in this assessment bank.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_new_assessments_taken_for_assessment_offered(self, assessment_offered_id):
        """Register for notifications of new assessments taken for an assessment offered.
        ``AssessmentTakenReceiver.newAssessmentsTaken()`` is invoked
        when a new ``AssessmentTaken`` appears in this assessment bank.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered`` to monitor
        :type assessment_offered_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_new_assessments_taken_for_assessment(self, assessment_id):
        """Register for notifications of new assessments taken for an assessment.
        ``AssessmentTakenReceiver.newAssessmentsTaken()`` is invoked
        when a new ``AssessmentTaken`` appears in this assessment bank.

        :param assessment_id: the ``Id`` of the ``Assessment`` to monitor
        :type assessment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_assessments_taken(self):
        """Registers for notification of updated assessments taken.
        ``AssessmentTakenReceiver.changedAssessmentsTaken()`` is invoked
        when an assessment taken in this assessment bank is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_assessments_taken_for_taker(self, resource_id):
        """Register for notifications of changed assessments taken for a resource.
        ``AssessmentTakenReceiver.changedAssessmentsTaken()`` is invoked
        when an ``AssessmentTaken`` is changed in this assessment bank.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_assessments_taken_for_assessment_offered(self, assessment_offered_id):
        """Register for notifications of changed assessments taken for an assessment offered.
        ``AssessmentTakenReceiver.changedAssessmentsTaken()`` is invoked
        when an ``AssessmentTaken`` is changed in this assessment bank.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered`` to monitor
        :type assessment_offered_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_assessments_taken_for_assessment(self, assessment_id):
        """Register for notifications of changed assessments taken for an assessment.
        ``AssessmentTakenReceiver.changedAssessmentsTaken()`` is invoked
        when an ``AssessmentTaken`` is changed in this assessment bank.

        :param assessment_id: the ``Id`` of the ``Assessment`` to monitor
        :type assessment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_changed_assessment_taken(self, assessment_taken_id):
        """Registers for notification of an updated assessment taken.
        ``AssessmentTakenReceiver.changedAssessmentsTaken()`` is invoked
        when the specified assessment taken in this assessment bank is
        changed.

        :param assessment_taken_id: the ``Id`` of the ``AssessmentTaken`` to monitor
        :type assessment_taken_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_assessments_taken(self):
        """Registers for notification of deleted assessments taken.
        ``AssessmentTakenReceiver.deletedAssessmentsTaken()`` is invoked
        when an assessment taken is removed from this assessment bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_assessments_taken_for_taker(self, resource_id):
        """Register for notifications of deleted assessments taken for a resource.
        ``AssessmentTakenReceiver.deletedAssessmentsTaken()`` is invoked
        when an ``AssessmentTaken`` is removed from this assessment
        bank.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_assessments_taken_for_assessment_offered(self, assessment_offered_id):
        """Register for notifications of deleted assessments taken for an assessment offered.
        ``AssessmentTakenReceiver.deletedAssessmentsTaken()`` is invoked
        when an ``AssessmentTaken`` is removed from this assessment
        bank.

        :param assessment_offered_id: the ``Id`` of the ``AssessmentOffered`` to monitor
        :type assessment_offered_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_offered_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_assessments_taken_for_assessment(self, assessment_id):
        """Register for notifications of deleted assessments taken for an assessment.
        ``AssessmentTakenReceiver.deletedAssessmentsTaken()`` is invoked
        when an ``AssessmentTaken`` is removed from this assessment
        bank.

        :param assessment_id: the ``Id`` of the ``Assessment`` to monitor
        :type assessment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_assessment_taken(self, assessment_taken_id):
        """Registers for notification of a deleted assessment taken.
        ``AssessmentTakenReceiver.deletedAssessmentsTaken()`` is invoked
        when the specified assessment taken is removed from this
        assessment bank.

        :param assessment_taken_id: the ``Id`` of the ``AssessmentTaken`` to monitor
        :type assessment_taken_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentTakenBankSession

    def can_lookup_assessment_taken_bank_mappings(self):
        """Tests if this user can perform lookups of assessment taken/bank mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_ids_by_bank(self, bank_id):
        """Gets the list of ``AssessmentTaken``  ``Ids`` associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related assessment taken ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken_by_bank(self, bank_id):
        """Gets the list of ``AssessmentTakens`` associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related assessments taken
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessment_taken_ids_by_banks(self, bank_ids):
        """Gets the list of ``AssessmentTaken Ids`` corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_assessments_taken_by_banks(self, bank_ids):
        """Gets the list of ``AssessmentTaken`` objects corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of assessments taken
        :rtype: ``osid.assessment.AssessmentTakenList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_bank_ids_by_assessment_taken(self, assessment_taken_id):
        """Gets the list of ``Bank``  ``Ids`` mapped to an ``AssessmentTaken``.

        :param assessment_taken_id: ``Id`` of an ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: list of bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def get_banks_by_assessment_taken(self, assessment_taken_id):
        """Gets the list of ``Banks`` mapped to an ``AssessmentTaken``.

        :param assessment_taken_id: ``Id`` of an ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: list of banks
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- ``assessment_taken_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentTakenBankAssignmentSession

    def can_assign_assessments_taken(self):
        """Tests if this user can alter assessment taken/bank mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_assessments_taken_to_bank(self, bank_id):
        """Tests if this user can alter assessment taken/bank mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_bank_ids_for_assessment_taken(self, bank_id, assessment_taken_id):
        """Gets a list of bank including and under the given bank node in which a specific assessment taken can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param assessment_taken_id: the ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` or ``assessment_taken_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_assessment_taken_to_bank(self, assessment_taken_id, bank_id):
        """Adds an existing ``AssessmentTaken`` to a ``Bank``.

        :param assessment_taken_id: the ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``assessment_taken_id`` is already assigned to ``bank_id``
        :raise: ``NotFound`` -- ``assessment_taken_id`` or ``bank_id`` not found
        :raise: ``NullArgument`` -- ``assessment_taken_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def unassign_assessment_taken_from_bank(self, assessment_taken_id, bank_id):
        """Removes an ``AssessmentTaken`` from a ``Bank``.

        :param assessment_taken_id: the ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_taken_id`` or ``bank_id`` not found or ``assessment_taken_id`` not assigned to ``bank_id``
        :raise: ``NullArgument`` -- ``assessment_taken_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def reassign_assessment_taken_to_billing(self, assessment_taken_id, from_bank_id, to_bank_id):
        """Moves an ``AssessmentTaken`` from one ``Bank`` to another.
        Mappings to other ``Banks`` are unaffected.

        :param assessment_taken_id: the ``Id`` of the ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``
        :param from_bank_id: the ``Id`` of the current ``Bank``
        :type from_bank_id: ``osid.id.Id``
        :param to_bank_id: the ``Id`` of the destination ``Bank``
        :type to_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_taken_id, from_bank_id,`` or ``to_bank_id`` not found or ``assessment_taken_id`` not mapped to ``from_bank_id``
        :raise: ``NullArgument`` -- ``assessment_taken_id, from_bank_id,`` or ``to_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.assessment.AssessmentTakenSmartBankSession

    def apply_assessment_taken_query(self, assessment_taken_query):
        """Applies an assessment taken query to this bank.

        :param assessment_taken_query: the assessment taken query
        :type assessment_taken_query: ``osid.assessment.AssessmentTakenQuery``
        :raise: ``NullArgument`` -- ``assessment_taken_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_taken_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_assessment_taken_query(self):
        """Gets an assessment taken query inspector for this bank.

        :return: the assessment taken query inspector
        :rtype: ``osid.assessment.AssessmentTakenQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_assessment_taken_sequencing(self, assessment_taken_search_order):
        """Applies an assessment taken search order to this bank.

        :param assessment_taken_search_order: the assessment taken search order
        :type assessment_taken_search_order: ``osid.assessment.AssessmentTakenSearchOrder``
        :raise: ``NullArgument`` -- ``assessment_taken_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_taken_search_order`` not of this service

        """
        raise UNIMPLEMENTED()



class BankList(osid_objects.OsidList):

    def get_next_bank(self):
        """Gets the next ``Bank`` in this list.

        :return: the next ``Bank`` in this list. The ``has_next()`` method should be used to test that a next ``Bank`` is available before calling this method.
        :rtype: ``osid.assessment.Bank``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    next_bank = property(fget=get_next_bank)

    def get_next_banks(self, n):
        """Gets the next set of ``Bank`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Bank`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Bank`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.assessment.Bank``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()



class Banks(AssessmentManager):
    pass


