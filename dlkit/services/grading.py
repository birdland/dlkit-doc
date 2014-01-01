# -*- coding: utf-8 -*-
"""Grading Open Service Interface Definitions
grading version 3.0.0

The Grading OSID defines a service to apply grades or ratings.

Grade Systems

The grade system sessions provide the means to retrievs and manage
``GradeSystem`` definitions. A ``GradeSystem`` is a fixed set of
``Grades`` . ``GradeSystems`` may also take the form of a numerical
score as well as a rating based on some system. ``GradeEntries`` belong
to a single ``GradebookColumn``.

Gradebook Columns

A ``Gradebook`` is represented by a series of ``GradebookColumns``. A
``GradeBookColumn`` represents a something to be graded and is joined to
a single ``GradeSystem``. A ``GradebookColumn`` may be constrained to a
single grader.

Grade Entries

A ``GradebookColumn`` is comprised of a series of ``GradeEntry``
elements. A ``GradebookColumn`` may represent "Assignment 3" while a
``GradeEntry`` may represent the assignment turned in by a particular
student.

A ``Grade`` can be applied to a ``GradeEntry`` that relates the entry to
a grader and a key ``Resource``. In the case of a class gradebook, the
key resource represents the student. If there are multiple graders for
the same key resource, each grader gets their own ``GradebookColumn``.

Gradebooks may also be used to capture ratings about other objects. In
the case where people vote for their favorite assets, the key resource
represents the ``Asset`` .

``GradebookColumns`` may have a ``GradebookColumnSummary`` entry for
summary results and statistics across all ``GradeEntries`` in the
column.

Gradebook Cataloging

``GradebookColumns`` are organized into ``Gradebooks``.  ``Gradebooks``
also provide for a federated hierarchy of ``GradebookColumns``. Simple
reordering of ``GradebookColumns`` can be performed by moving the
``GradebookColumn`` relative to another. The relative positioning may
reference two ``GradebookColumns`` through the federation.

Sub Packages

The Grading OSID includes several subpackages. The Grading Transform
OSID provides a means of translating one ``GradeSystem`` to another. The
Grading Calculation OSID defines derived ``GradebookColumns``. The
Grading Batch OSID manages ``GradeSystems,``  ``GradeEntries,``
``Gradebooks,`` and ``GradebookColumns`` in bulk.

"""
from ..osid import managers as osid_managers
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class GradingProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_grade_system_lookup(self):
        """Tests if a grade system lookup service is supported.

        :return: true if grade system lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_grade_system_query(self):
        """Tests if a grade system query service is supported.

        :return: ``true`` if grade system query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_grade_system_search(self):
        """Tests if a grade system search service is supported.

        :return: ``true`` if grade system search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_grade_system_admin(self):
        """Tests if a grade system administrative service is supported.

        :return: ``true`` if grade system admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_grade_system_notification(self):
        """Tests if grade system notification is supported.
        Messages may be sent when grade entries are created, modified,
        or deleted.

        :return: ``true`` if grade system notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_grade_system_gradebook(self):
        """Tests if a grade system to gradebook lookup session is available.

        :return: ``true`` if grade system gradebook lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_grade_system_gradebook_assignment(self):
        """Tests if a grade system to gradebook assignment session is available.

        :return: ``true`` if grade system gradebook assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_grade_system_smart_gradebook(self):
        """Tests if a grade system smart gradebook session is available.

        :return: ``true`` if grade system smart gradebook is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_grade_entry_lookup(self):
        """Tests if a grade entry lookup service is supported.

        :return: true if grade entry lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_grade_entry_query(self):
        """Tests if a grade entry query service is supported.

        :return: true if grade entry query is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_grade_entry_search(self):
        """Tests if a grade entry search service is supported.

        :return: ``true`` if grade entry search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_grade_entry_admin(self):
        """Tests if a grade entry administrative service is supported.

        :return: ``true`` if grade entry admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_grade_entry_notification(self):
        """Tests if grade entry notification is supported.

        :return: ``true`` if grade entry notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_gradebook_column_lookup(self):
        """Tests if a gradebook column lookup service is supported.

        :return: true if gradebook column lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_gradebook_column_query(self):
        """Tests if a gradebook column query service is supported.

        :return: ``true`` if grade system query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_gradebook_column_search(self):
        """Tests if a gradebook column search service is supported.

        :return: ``true`` if grade system search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_gradebook_column_admin(self):
        """Tests if a gradebook column administrative service is supported.

        :return: ``true`` if gradebook column admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_gradebook_column_notification(self):
        """Tests if gradebook column notification is supported.
        Messages may be sent when grade entries are created, modified,
        or deleted.

        :return: ``true`` if gradebook column notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_gradebook_column_gradebook(self):
        """Tests if a gradebook column to gradebook lookup session is available.

        :return: ``true`` if gradebook column gradebook lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_gradebook_column_gradebook_assignment(self):
        """Tests if a gradebook column to gradebook assignment session is available.

        :return: ``true`` if gradebook column gradebook assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_gradebook_column_smart_gradebook(self):
        """Tests if a gradebook column smart gradebookt session is available.

        :return: ``true`` if gradebook column amsrt gradebook is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_gradebook_lookup(self):
        """Tests if a gradebook lookup service is supported.

        :return: ``true`` if gradebook lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_gradebook_query(self):
        """Tests if a gradebook query service is supported.

        :return: ``true`` if gradebook query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_gradebook_search(self):
        """Tests if a gradebook search service is supported.

        :return: ``true`` if gradebook search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_gradebook_admin(self):
        """Tests if a gradebook administrative service is supported.

        :return: ``true`` if gradebook admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_gradebook_notification(self):
        """Tests if gradebook notification is supported.
        Messages may be sent when gradebooks are created, modified, or
        deleted.

        :return: ``true`` if gradebook notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_gradebook_hierarchy(self):
        """Tests if a gradebook hierarchy traversal is supported.

        :return: ``true`` if a gradebook hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_gradebook_hierarchy_design(self):
        """Tests if gradebook hierarchy design is supported.

        :return: ``true`` if a gradebook hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_grading_batch(self):
        """Tests if a grading batch service is supported.

        :return: ``true`` if a grading batch service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_grading_calculation(self):
        """Tests if a grading calculation service is supported.

        :return: ``true`` if a grading calculation service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_grading_transform(self):
        """Tests if a grade system transform service is supported.

        :return: ``true`` if a grading transform service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_grade_record_types(self):
        """Gets the supported ``Grade`` record types.

        :return: a list containing the supported ``Grade`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    grade_record_types = property(fget=get_grade_record_types)

    def supports_grade_record_type(self, grade_record_type):
        """Tests if the given ``Grade`` record type is supported.

        :param grade_record_type: a ``Type`` indicating a ``Grade`` record type
        :type grade_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_record_types(self):
        """Gets the supported ``GradeSystem`` record types.

        :return: a list containing the supported ``GradeSystem`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    grade_system_record_types = property(fget=get_grade_system_record_types)

    def supports_grade_system_record_type(self, grade_system_record_type):
        """Tests if the given ``GradeSystem`` record type is supported.

        :param grade_system_record_type: a ``Type`` indicating a ``GradeSystem`` record type
        :type grade_system_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_search_record_types(self):
        """Gets the supported ``GradeSystem`` search record types.

        :return: a list containing the supported ``GradeSystem`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    grade_system_search_record_types = property(fget=get_grade_system_search_record_types)

    def supports_grade_system_search_record_type(self, grade_system_search_record_type):
        """Tests if the given ``GradeSystem`` search record type is supported.

        :param grade_system_search_record_type: a ``Type`` indicating a ``GradeSystem`` search record type
        :type grade_system_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_record_types(self):
        """Gets the supported ``GradeEntry`` record types.

        :return: a list containing the supported ``GradeEntry`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    grade_entry_record_types = property(fget=get_grade_entry_record_types)

    def supports_grade_entry_record_type(self, grade_entry_record_type):
        """Tests if the given ``GradeEntry`` record type is supported.

        :param grade_entry_record_type: a ``Type`` indicating a ``GradeEntry`` record type
        :type grade_entry_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_entry_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_search_record_types(self):
        """Gets the supported ``GradeEntry`` search record types.

        :return: a list containing the supported ``GradeEntry`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    grade_entry_search_record_types = property(fget=get_grade_entry_search_record_types)

    def supports_grade_entry_search_record_type(self, grade_entry_search_record_type):
        """Tests if the given ``GradeEntry`` search record type is supported.

        :param grade_entry_search_record_type: a ``Type`` indicating a ``GradeEntry`` search record type
        :type grade_entry_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_entry_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_record_types(self):
        """Gets the supported ``GradebookColumn`` record types.

        :return: a list containing the supported ``GradebookColumn`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    gradebook_column_record_types = property(fget=get_gradebook_column_record_types)

    def supports_gradebook_column_record_type(self, gradebook_column_record_type):
        """Tests if the given ``GradebookColumn`` record type is supported.

        :param gradebook_column_record_type: a ``Type`` indicating a ``GradebookColumn`` type
        :type gradebook_column_record_type: ``osid.type.Type``
        :return: ``true`` if the given gradebook column record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_search_record_types(self):
        """Gets the supported gradebook column search record types.

        :return: a list containing the supported ``GradebookColumn`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    gradebook_column_search_record_types = property(fget=get_gradebook_column_search_record_types)

    def supports_gradebook_column_search_record_type(self, gradebook_column_search_record_type):
        """Tests if the given gradebook column search record type is supported.

        :param gradebook_column_search_record_type: a ``Type`` indicating a ``GradebookColumn`` search record type
        :type gradebook_column_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_summary_record_types(self):
        """Gets the supported ``GradebookColumnSummary`` record types.

        :return: a list containing the supported ``GradebookColumnSummary`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    gradebook_column_summary_record_types = property(fget=get_gradebook_column_summary_record_types)

    def supports_gradebook_column_summary_record_type(self, gradebook_column_summary_record_type):
        """Tests if the given ``GradebookColumnSummary`` record type is supported.

        :param gradebook_column_summary_record_type: a ``Type`` indicating a ``GradebookColumnSummary`` type
        :type gradebook_column_summary_record_type: ``osid.type.Type``
        :return: ``true`` if the given gradebook column summary record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_record_types(self):
        """Gets the supported ``Gradebook`` record types.

        :return: a list containing the supported ``Gradebook`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    gradebook_record_types = property(fget=get_gradebook_record_types)

    def supports_gradebook_record_type(self, gradebook_record_type):
        """Tests if the given ``Gradebook`` record type is supported.

        :param gradebook_record_type: a ``Type`` indicating a ``Gradebook`` type
        :type gradebook_record_type: ``osid.type.Type``
        :return: ``true`` if the given gradebook record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_search_record_types(self):
        """Gets the supported gradebook search record types.

        :return: a list containing the supported ``Gradebook`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    gradebook_search_record_types = property(fget=get_gradebook_search_record_types)

    def supports_gradebook_search_record_type(self, gradebook_search_record_type):
        """Tests if the given gradebook search record type is supported.

        :param gradebook_search_record_type: a ``Type`` indicating a ``Gradebook`` search record type
        :type gradebook_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class GradingManager(osid_managers.OsidManager, osid_sessions.OsidSession, GradingProfile):

    def get_grade_system_lookup_session(self):
        """Gets the ``OsidSession`` associated with the grade system lookup service.

        :return: a ``GradeSystemLookupSession``
        :rtype: ``osid.grading.GradeSystemLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    grade_system_lookup_session = property(fget=get_grade_system_lookup_session)

    def get_grade_system_lookup_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system lookup service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradeSystemLookupSession``
        :rtype: ``osid.grading.GradeSystemLookupSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_query_session(self):
        """Gets the ``OsidSession`` associated with the grade system query service.

        :return: a ``GradeSystemQuerySession``
        :rtype: ``osid.grading.GradeSystemQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    grade_system_query_session = property(fget=get_grade_system_query_session)

    def get_grade_system_query_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system query service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradeSystemQuerySession``
        :rtype: ``osid.grading.GradeSystemQuerySession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_search_session(self):
        """Gets the ``OsidSession`` associated with the grade system search service.

        :return: a ``GradeSystemSearchSession``
        :rtype: ``osid.grading.GradeSystemSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    grade_system_search_session = property(fget=get_grade_system_search_session)

    def get_grade_system_search_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system search service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradeSystemSearchSession``
        :rtype: ``osid.grading.GradeSystemSearchSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_admin_session(self):
        """Gets the ``OsidSession`` associated with the grade system administration service.

        :return: a ``GradeSystemAdminSession``
        :rtype: ``osid.grading.GradeSystemAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    grade_system_admin_session = property(fget=get_grade_system_admin_session)

    def get_grade_system_admin_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system admin service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradeSystemAdminSession``
        :rtype: ``osid.grading.GradeSystemAdminSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_notification_session(self, grade_system_receiver):
        """Gets the notification session for notifications pertaining to grade system changes.

        :param grade_system_receiver: the grade system receiver
        :type grade_system_receiver: ``osid.grading.GradeSystemReceiver``
        :return: a ``GradeSystemNotificationSession``
        :rtype: ``osid.grading.GradeSystemNotificationSession``
        :raise: ``NullArgument`` -- ``grade_system_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_notification_session_for_gradebook(self, grade_system_receiver, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system notification service for the given gradebook.

        :param grade_system_receiver: the grade system receiver
        :type grade_system_receiver: ``osid.grading.GradeSystemReceiver``
        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a _grade_system_notification_session``
        :rtype: ``osid.grading.GradeSystemNotificationSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``grade_system_receiver`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_gradebook_session(self):
        """Gets the session for retrieving grade system to gradebook mappings.

        :return: a ``GradeSystemGradebookSession``
        :rtype: ``osid.grading.GradeSystemGradebookSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_gradebook()`` is ``false``

        """
        raise UNIMPLEMENTED()

    grade_system_gradebook_session = property(fget=get_grade_system_gradebook_session)

    def get_grade_system_gradebook_assignment_session(self):
        """Gets the session for assigning grade system to gradebook mappings.

        :return: a ``GradeSystemGradebookAssignmentSession``
        :rtype: ``osid.grading.GradeSystemGradebookSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_gradebook_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    grade_system_gradebook_assignment_session = property(fget=get_grade_system_gradebook_assignment_session)

    def get_grade_system_smart_gradebook_session(self, gradebook_id):
        """Gets the session for managing smart gradebooks of grade systems.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: a ``GradeSystemSmartGradebookSession``
        :rtype: ``osid.grading.GradeSystemSmartGradebookSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_smart_gradebook()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_lookup_session(self):
        """Gets the ``OsidSession`` associated with the grade entry lookup service.

        :return: a ``GradeEntryLookupSession``
        :rtype: ``osid.grading.GradeEntryLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    grade_entry_lookup_session = property(fget=get_grade_entry_lookup_session)

    def get_grade_entry_lookup_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry lookup service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradeEntryLookupSession``
        :rtype: ``osid.grading.GradeEntryLookupSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_query_session(self):
        """Gets the ``OsidSession`` associated with the grade entry query service.

        :return: a ``GradeEntryQuerySession``
        :rtype: ``osid.grading.GradeEntryQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    grade_entry_query_session = property(fget=get_grade_entry_query_session)

    def get_grade_entry_query_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry query service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradeEntryQuerySession``
        :rtype: ``osid.grading.GradeEntryQuerySession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_search_session(self):
        """Gets the ``OsidSession`` associated with the grade entry search service.

        :return: a ``GradeEntrySearchSession``
        :rtype: ``osid.grading.GradeEntrySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    grade_entry_search_session = property(fget=get_grade_entry_search_session)

    def get_grade_entry_search_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry search service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradeEntrySearchSession``
        :rtype: ``osid.grading.GradeEntrySearchSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_admin_session(self):
        """Gets the ``OsidSession`` associated with the grade entry administration service.

        :return: a ``GradeEntryAdminSession``
        :rtype: ``osid.grading.GradeEntryAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    grade_entry_admin_session = property(fget=get_grade_entry_admin_session)

    def get_grade_entry_admin_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry admin service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradeEntryAdminSession``
        :rtype: ``osid.grading.GradeEntryAdminSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_notification_session(self, receiver):
        """Gets the notification session for notifications pertaining to grade entry changes.

        :param receiver: the grade entry receiver
        :type receiver: ``osid.grading.GradeEntryReceiver``
        :return: a ``GradeEntryNotificationSession``
        :rtype: ``osid.grading.GradeEntryNotificationSession``
        :raise: ``NullArgument`` -- ``receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_notification_session_for_gradebook(self, receiver, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry notification service for the given gradebook.

        :param receiver: the grade entry receiver
        :type receiver: ``osid.grading.GradeEntryReceiver``
        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a _grade_entry_notification_session``
        :rtype: ``osid.grading.GradeEntryNotificationSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``receiver`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_lookup_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column lookup service.

        :return: a ``GradebookColumnLookupSession``
        :rtype: ``osid.grading.GradebookColumnLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    gradebook_column_lookup_session = property(fget=get_gradebook_column_lookup_session)

    def get_gradebook_column_lookup_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column lookup service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a _gradebook_column_lookup_session``
        :rtype: ``osid.grading.GradebookColumnLookupSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_query_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column query service.

        :return: a ``GradebookColumnQuerySession``
        :rtype: ``osid.grading.GradebookColumnQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    gradebook_column_query_session = property(fget=get_gradebook_column_query_session)

    def get_gradebook_column_query_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column query service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradebookColumnQuerySession``
        :rtype: ``osid.grading.GradebookColumnQuerySession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_search_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column search service.

        :return: a ``GradebookColumnSearchSession``
        :rtype: ``osid.grading.GradebookColumnSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    gradebook_column_search_session = property(fget=get_gradebook_column_search_session)

    def get_gradebook_column_search_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column search service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a _gradebook_column_search_session``
        :rtype: ``osid.grading.GradebookColumnSearchSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_admin_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column administration service.

        :return: a ``GradebookColumnAdminSession``
        :rtype: ``osid.grading.GradebookColumnAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    gradebook_column_admin_session = property(fget=get_gradebook_column_admin_session)

    def get_gradebook_column_admin_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column admin service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a GradebookColumnAdminSession``
        :rtype: ``osid.grading.GradebookColumnAdminSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_notification_session(self, gradebook_column_receiver):
        """Gets the notification session for notifications pertaining to gradebook column changes.

        :param gradebook_column_receiver: the grade system receiver
        :type gradebook_column_receiver: ``osid.grading.GradebookColumnReceiver``
        :return: a ``GradebookColumnNotificationSession``
        :rtype: ``osid.grading.GradebookColumnNotificationSession``
        :raise: ``NullArgument`` -- ``gradebook_column_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_notification_session_for_gradebook(self, gradebook_column_receiver, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column notification service for the given gradebook.

        :param gradebook_column_receiver: the gradebook column receiver
        :type gradebook_column_receiver: ``osid.grading.GradebookColumnReceiver``
        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``a _gradebook_column_notification_session``
        :rtype: ``osid.grading.GradebookColumnNotificationSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_column_receiver`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_gradebook_session(self):
        """Gets the session for retrieving gradebook column to gradebook mappings.

        :return: a ``GradebookColumnGradebookSession``
        :rtype: ``osid.grading.GradebookColumnGradebookSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_gradebook()`` is ``false``

        """
        raise UNIMPLEMENTED()

    gradebook_column_gradebook_session = property(fget=get_gradebook_column_gradebook_session)

    def get_gradebook_column_gradebook_assignment_session(self):
        """Gets the session for assigning gradebook column to gradebook mappings.

        :return: a ``GradebookColumnGradebookAssignmentSession``
        :rtype: ``osid.grading.GradebookColumnGradebookAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_gradebook_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    gradebook_column_gradebook_assignment_session = property(fget=get_gradebook_column_gradebook_assignment_session)

    def get_gradebook_column_smart_gradebook_session(self, gradebook_id):
        """Gets the session for managing smart gradebooks of gradebook columns.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: a ``GradebookColumnSmartGradebookSession``
        :rtype: ``osid.grading.GradebookColumnSmartGradebookSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_smart_gradebook()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_lookup_session(self):
        """Gets the OsidSession associated with the gradebook lookup service.

        :return: a ``GradebookLookupSession``
        :rtype: ``osid.grading.GradebookLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_lookup() is false``

        """
        raise UNIMPLEMENTED()

    gradebook_lookup_session = property(fget=get_gradebook_lookup_session)

    def get_gradebook_query_session(self):
        """Gets the OsidSession associated with the gradebook query service.

        :return: a ``GradebookQuerySession``
        :rtype: ``osid.grading.GradebookQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_query() is false``

        """
        raise UNIMPLEMENTED()

    gradebook_query_session = property(fget=get_gradebook_query_session)

    def get_gradebook_search_session(self):
        """Gets the OsidSession associated with the gradebook search service.

        :return: a ``GradebookSearchSession``
        :rtype: ``osid.grading.GradebookSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_search() is false``

        """
        raise UNIMPLEMENTED()

    gradebook_search_session = property(fget=get_gradebook_search_session)

    def get_gradebook_admin_session(self):
        """Gets the OsidSession associated with the gradebook administration service.

        :return: a ``GradebookAdminSession``
        :rtype: ``osid.grading.GradebookAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_admin() is false``

        """
        raise UNIMPLEMENTED()

    gradebook_admin_session = property(fget=get_gradebook_admin_session)

    def get_gradebook_notification_session(self, gradebook_receiver):
        """Gets the notification session for notifications pertaining to gradebook service changes.

        :param gradebook_receiver: the gradebook receiver
        :type gradebook_receiver: ``osid.grading.GradebookReceiver``
        :return: a ``GradebookNotificationSession``
        :rtype: ``osid.grading.GradebookNotificationSession``
        :raise: ``NullArgument`` -- ``gradebook_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_notification() is false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_hierarchy_session(self):
        """Gets the session traversing gradebook hierarchies.

        :return: a ``GradebookHierarchySession``
        :rtype: ``osid.grading.GradebookHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_hierarchy() is false``

        """
        raise UNIMPLEMENTED()

    gradebook_hierarchy_session = property(fget=get_gradebook_hierarchy_session)

    def get_gradebook_hierarchy_design_session(self):
        """Gets the session designing gradebook hierarchies.

        :return: a ``GradebookHierarchyDesignSession``
        :rtype: ``osid.grading.GradebookHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_hierarchy_design() is false``

        """
        raise UNIMPLEMENTED()

    gradebook_hierarchy_design_session = property(fget=get_gradebook_hierarchy_design_session)

    def get_grading_batch_manager(self):
        """Gets the ``GradingBatchManager``.

        :return: a ``GradingBatchManager``
        :rtype: ``osid.grading.batch.GradingBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_batch() is false``

        """
        raise UNIMPLEMENTED()

    grading_batch_manager = property(fget=get_grading_batch_manager)

    def get_grading_calculation_manager(self):
        """Gets the ``GradingCalculationManager``.

        :return: a ``GradingCalculationManager``
        :rtype: ``osid.grading.calculation.GradingCalculationManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_calculation() is false``

        """
        raise UNIMPLEMENTED()

    grading_calculation_manager = property(fget=get_grading_calculation_manager)

    def get_grading_transform_manager(self):
        """Gets the ``GradingTransformManager``.

        :return: a ``GradingTransformManager``
        :rtype: ``osid.grading.transform.GradingTransformManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_transform() is false``

        """
        raise UNIMPLEMENTED()

    grading_transform_manager = property(fget=get_grading_transform_manager)


##
# The following methods are from osid.grading.GradebookColumnLookupSession

    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    gradebook = property(fget=get_gradebook)

    def can_lookup_gradebook_columns(self):
        """Tests if this user can perform ``GradebookColumn`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_gradebook_column_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_gradebook_column_view(self):
        """A complete view of the ``GradebookColumn`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.
        A federated view will include gradebook columns in gradebooks
        which are children of this gradebook in the gradebook hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this gradebook only.



        """
        raise UNIMPLEMENTED()

    def get_gradebook_column(self, gradebook_column_id):
        """Gets the ``GradebookColumn`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``GradebookColumn`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``GradebookColumn`` and
        retained for compatibility.

        :param gradebook_column_id: ``Id`` of the ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :return: the gradebook column
        :rtype: ``osid.grading.GradebookColumn``
        :raise: ``NotFound`` -- ``gradebook_column_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebook_columns_by_ids(self, gradebook_column_ids):
        """Gets a ``GradebookColumnList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the gradebook
        columns specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if a ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible gradeboook columns may be omitted from the list.

        :param gradebook_column_ids: the list of ``Ids`` to retrieve
        :type gradebook_column_ids: ``osid.id.IdList``
        :return: the returned ``GradebookColumn`` list
        :rtype: ``osid.grading.GradebookColumnList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``grade_book_column_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebook_columns_by_genus_type(self, gradebook_column_genus_type):
        """Gets a ``GradebookColumnList`` corresponding to the given gradebook column genus ``Type`` which does not include gradebook columns of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known gradebook
        columns or an error results. Otherwise, the returned list may
        contain only those gradebook columns that are accessible through
        this session.

        :param gradebook_column_genus_type: a gradebook column genus type
        :type gradebook_column_genus_type: ``osid.type.Type``
        :return: the returned ``GradebookColumn`` list
        :rtype: ``osid.grading.GradebookColumnList``
        :raise: ``NullArgument`` -- ``gradebook_column_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebook_columns_by_parent_genus_type(self, gradebook_column_genus_type):
        """Gets a ``GradebookColumnList`` corresponding to the given gradebook column genus ``Type`` and include any additional columns with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known gradebook
        columns or an error results. Otherwise, the returned list may
        contain only those gradebook columns that are accessible through
        this session.

        :param gradebook_column_genus_type: a gradebook column genus type
        :type gradebook_column_genus_type: ``osid.type.Type``
        :return: the returned ``GradebookColumn`` list
        :rtype: ``osid.grading.GradebookColumnList``
        :raise: ``NullArgument`` -- ``gradebook_column_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebook_columns_by_record_type(self, gradebook_column_record_type):
        """Gets a ``GradebookColumnList`` containing the given gradebook column record ``Type``.
        In plenary mode, the returned list contains all known gradebook
        columns or an error results. Otherwise, the returned list may
        contain only those gradebook columns that are accessible through
        this session.

        :param gradebook_column_record_type: a gradebook column record type
        :type gradebook_column_record_type: ``osid.type.Type``
        :return: the returned ``GradebookColumn`` list
        :rtype: ``osid.grading.GradebookColumnList``
        :raise: ``NullArgument`` -- ``gradebook_column_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebook_columns(self):
        """Gets all gradebook columns.
        In plenary mode, the returned list contains all known gradebook
        columns or an error results. Otherwise, the returned list may
        contain only those gradebook columns that are accessible through
        this session.

        :return: a ``GradebookColumn``
        :rtype: ``osid.grading.GradebookColumnList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    gradebook_columns = property(fget=get_gradebook_columns)

    def supports_summary(self):
        """Tests if a summary entry is available.

        :return: ``true`` if a summary entry is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_summary(self, gradebook_column_id):
        """Gets the ``GradebookColumnSummary`` for summary results.

        :param gradebook_column_id: ``Id`` of the ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :return: the gradebook column summary
        :rtype: ``osid.grading.GradebookColumnSummary``
        :raise: ``NotFound`` -- ``gradebook_column_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unimplemented`` -- ``has_summary()`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradebookColumnQuerySession

    def can_search_gradebook_columns(self):
        """Tests if this user can perform ``GradebookColumn`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_query(self):
        """Gets a gradebook column query.

        :return: the gradebook column
        :rtype: ``osid.grading.GradebookColumnQuery``

        """
        raise UNIMPLEMENTED()

    gradebook_column_query = property(fget=get_gradebook_column_query)

    def get_gradebook_columns_by_query(self, gradebook_column_query):
        """Gets a list of gradebook columns matching the given query.

        :param gradebook_column_query: the gradebook column query
        :type gradebook_column_query: ``osid.grading.GradebookColumnQuery``
        :return: the returned ``GradebookColumnList``
        :rtype: ``osid.grading.GradebookColumnList``
        :raise: ``NullArgument`` -- ``gradebook_column_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``gradebook_column_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradebookColumnSearchSession

    def get_gradebook_column_search(self):
        """Gets a gradebook column search.

        :return: the gradebook column search
        :rtype: ``osid.grading.GradebookColumnSearch``

        """
        raise UNIMPLEMENTED()

    gradebook_column_search = property(fget=get_gradebook_column_search)

    def get_gradebook_column_search_order(self):
        """Gets a gradebook column search order.
        The ``GradebookColumnSearchOrder`` is supplied to a
        ``GradebookColumnSearch`` to specify the ordering of results.

        :return: the gradebook column search order
        :rtype: ``osid.grading.GradebookColumnSearchOrder``

        """
        raise UNIMPLEMENTED()

    gradebook_column_search_order = property(fget=get_gradebook_column_search_order)

    def get_gradebook_columns_by_search(self, gradebook_column_query, gradebook_column_search):
        """Gets the search results matching the given search query using the given search.

        :param gradebook_column_query: the gradebook column query
        :type gradebook_column_query: ``osid.grading.GradebookColumnQuery``
        :param gradebook_column_search: the gradebook column search
        :type gradebook_column_search: ``osid.grading.GradebookColumnSearch``
        :return: the gradebook column search results
        :rtype: ``osid.grading.GradebookColumnSearchResults``
        :raise: ``NullArgument`` -- ``gradebook_column_query`` or ``gradebook_column_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``gradebook_column_search`` or ``gradebook_column_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_query_from_inspector(self, gradebook_column_query_inspector):
        """Gets a gradebook column query from an inspector.
        The inspector is available from an
        ``GradebookColumnSearchResults``.

        :param gradebook_column_query_inspector: a gradebook column query inspector
        :type gradebook_column_query_inspector: ``osid.grading.GradebookColumnQueryInspector``
        :return: the gradebook column query
        :rtype: ``osid.grading.GradebookColumnQuery``
        :raise: ``NullArgument`` -- ``gradebook_column_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``gradebook_column_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradebookColumnAdminSession

    def can_create_gradebook_columns(self):
        """Tests if this user can create gradebook columns.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a gradebook
        column will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``GradebookColumn`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_gradebook_column_with_record_types(self, gradebook_column_record_types):
        """Tests if this user can create a single ``GradebookColumn`` using the desired record types.
        While ``GradingManager.getGradebookColumnRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``GradebookColumn``. Providing an empty array tests if a
        ``GradebookColumn`` can be created with no records.

        :param gradebook_column_record_types: array of gradebook column record types
        :type gradebook_column_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``GradebookColumn`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_form_for_create(self, gradebook_column_record_types):
        """Gets the gradebook column form for creating new gradebook columns.
        A new form should be requested for each create transaction.

        :param gradebook_column_record_types: array of gradebook column record types
        :type gradebook_column_record_types: ``osid.type.Type[]``
        :return: the gradebook column form
        :rtype: ``osid.grading.GradebookColumnForm``
        :raise: ``NullArgument`` -- ``gradebook_column_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_gradebook_column(self, gradebook_column_form):
        """Creates a new ``GradebookColumn``.

        :param gradebook_column_form: the form for this ``GradebookColumn``
        :type gradebook_column_form: ``osid.grading.GradebookColumnForm``
        :return: the new ``GradebookColumn``
        :rtype: ``osid.grading.GradebookColumn``
        :raise: ``IllegalState`` -- ``gradebook_column_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``gradebook_column_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``gradebook_column_form`` did not originate from ``get_gradebook_column_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_gradebook_columns(self):
        """Tests if this user can update gradebook columns.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``GradebookColumn`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: ``false`` if gradebook column modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_form_for_update(self, gradebook_column_id):
        """Gets the gradebook column form for updating an existing gradebook column.
        A new gradebook column form should be requested for each update
        transaction.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :return: the gradebook column form
        :rtype: ``osid.grading.GradebookColumnForm``
        :raise: ``NotFound`` -- ``gradebook_column_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_gradebook_column(self, gradebook_column_form):
        """Updates an existing gradebook column.

        :param gradebook_column_form: the form containing the elements to be updated
        :type gradebook_column_form: ``osid.grading.GradebookColumnForm``
        :raise: ``IllegalState`` -- ``gradebook_column_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``gradebook_column_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``gradebook_column_form`` did not originate from ``get_gradebook_column_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def sequence_gradebook_columns(self, gradebook_column_ids):
        """Resequences the gradebook columns.

        :param gradebook_column_ids: the ``Ids`` of the ``GradebookColumns``
        :type gradebook_column_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_column_id_list`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def move_gradebook_column(self, front_gradebook_column_id, back_gradebook_column_id):
        """Moves a gradebook column in front of another.

        :param front_gradebook_column_id: the ``Id`` of a ``GradebookColumn``
        :type front_gradebook_column_id: ``osid.id.Id``
        :param back_gradebook_column_id: the ``Id`` of a ``GradebookColumn``
        :type back_gradebook_column_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``front_gradebook_column_id or back_gradebook_column_id`` is not found
        :raise: ``NullArgument`` -- ``front_gradebook_column_id or back_gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def copy_gradebook_column_entries(self, source_gradebook_column_id, target_gradebook_column_id):
        """Copies gradebook column entries from one column to another.
        If the target grade column grade system differs from the source,
        the grades in the entries are transformed to the new grade
        system.

        :param source_gradebook_column_id: the ``Id`` of a ``GradebookColumn``
        :type source_gradebook_column_id: ``osid.id.Id``
        :param target_gradebook_column_id: the ``Id`` of a ``GradebookColumn``
        :type target_gradebook_column_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``source_gradebook_column_id ortarget_gradebook_column_id`` is not found
        :raise: ``NullArgument`` -- ``source_gradebook_column_id target_gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_delete_gradebook_columns(self):
        """Tests if this user can delete gradebook columns.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``GradebookColumn`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer delete operations to an unauthorized user.

        :return: ``false`` if ``GradebookColumn`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_gradebook_column(self, gradebook_column_id):
        """Deletes the ``GradebookColumn`` identified by the given ``Id``.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn`` to delete
        :type gradebook_column_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``GradebookColumn`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_gradebook_column_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``GradebookColumns``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``GradebookColumn`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_gradebook_column(self, gradebook_column_id, alias_id):
        """Adds an ``Id`` to a ``GradebookColumn`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``GradebookColumn`` is determined by
        the provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another gradebook column,
        it is reassigned to the given gradebook column ``Id``.

        :param gradebook_column_id: the ``Id`` of a ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``gradebook_column_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_column_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradebookColumnNotificationSession

    def can_register_for_gradebook_column_notifications(self):
        """Tests if this user can register for ``GradebookColumn`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_gradebook_columns(self):
        """Register for notifications of new gradebook columns.
        ``GradebookColumnReceiver.newGradebookColumny()`` is invoked
        when a new column is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_gradebook_columns(self):
        """Registers for notification of updated gradebook columns.
        ``GradebookColumnReceiver.changedGradebookColumn()`` is invoked
        when a gradebook column is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_gradebook_column(self, gradebook_column_id):
        """Registers for notification of an updated gradebook column.
        ``GradebookColumnReceiver.changedGradebookColumn()`` is invoked
        when the specified gradebook column is changed.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn`` to monitor
        :type gradebook_column_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_column_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_gradebook_columns(self):
        """Registers for notification of deleted gradebook columns.
        ``GradebookColumnReceiver.deletedGradebookColumn()`` is invoked
        when a gradebook column is removed from this gradebook.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_gradebook_column(self, gradebook_column_id):
        """Registers for notification of a deleted gradebook column.
        ``GradebookColumnReceiver.deletedGradebookColumn()`` is invoked
        when the specified column is removed from thia gradebook.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn`` to monitor
        :type gradebook_column_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_column_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradebookColumnGradebookSession

    def use_comparative_gradebook_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_gradebook_view(self):
        """A complete view of the ``GradebookColumn`` and ``Gradebook`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def can_lookup_gradebook_column_gradebook_mappings(self):
        """Tests if this user can perform lookups of gradebook/column mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_ids_by_gradebook(self, gradebook_id):
        """Gets the list of ``GradebookColumn``  ``Ids`` associated with a ``Gradebook``.

        :param gradebook_id: ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: list of related gradebook column ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebook_columns_by_gradebook(self, gradebook_id):
        """Gets the list of gradebook columns associated with a ``Gradebook``.

        :param gradebook_id: ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: list of related gradebook columns
        :rtype: ``osid.grading.GradebookColumnList``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_ids_by_gradebooks(self, gradebook_ids):
        """Gets the list of ``GradebookColumn Ids`` corresponding to a list of ``Gradebooks``.

        :param gradebook_ids: list of gradebook ``Ids``
        :type gradebook_ids: ``osid.id.IdList``
        :return: list of gradebook column ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebook_columns_by_gradebooks(self, gradebook_ids):
        """Gets the list of gradebook columns corresponding to a list of ``Gradebooks``.

        :param gradebook_ids: list of gradebook ``Ids``
        :type gradebook_ids: ``osid.id.IdList``
        :return: list of gradebook columns
        :rtype: ``osid.grading.GradebookColumnList``
        :raise: ``NullArgument`` -- ``gradebook_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebook_ids_by_gradebook_column(self, gradebook_column_id):
        """Gets the list of ``Gradebook``  ``Ids`` mapped to a ``GradebookColumn``.

        :param gradebook_column_id: ``Id`` of a ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :return: list of gradebook ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``gradebook_column_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebooks_by_gradebook_column(self, gradebook_column_id):
        """Gets the list of ``Gradebooks`` mapped to a ``GradebookColumn``.

        :param gradebook_column_id: ``Id`` of a ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :return: list of gradebooks
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NotFound`` -- ``gradebook_column_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradebookColumnGradebookAssignmentSession

    def can_assign_gradebook_columns(self):
        """Tests if this user can alter gradebook column/gradebook mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_gradebook_columns_to_gradebook(self, gradebook_id):
        """Tests if this user can alter gradebook column/gradebook mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_gradebook_ids(self, gradebook_id):
        """Gets a list of gradebook ``Ids`` including and under the given gradebook node in which any gradebook column can be assigned.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: list of assignable gradebook ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_gradebook_ids_for_gradebook_column(self, gradebook_id, gradebook_column_id):
        """Gets a list of gradebooks including and under the given gradebook node in which a specific gradebook column can be assigned.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :param gradebook_column_id: the ``Id`` of the ``GradebokColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :return: list of assignable gradebook ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_gradebook_column_to_gradebook(self, gradebook_column_id, gradebook_id):
        """Adds an existing ``GradebookColumn`` to a ``Gradebook``.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``gradebook_column_id`` is already assigned to ``gradebook_id``
        :raise: ``NotFound`` -- ``gradebook_column_id`` or ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_column_id`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_gradebook_column_from_gradebook(self, gradebook_column_id, gradebook_id):
        """Removes a ``GradebookColumn`` from a ``Gradebook``.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``gradebook_column_id`` or ``gradebook_id`` not found or ``gradebook_column_id`` not assigned to ``gradebook_id``
        :raise: ``NullArgument`` -- ``gradebook_column_id`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradebookColumnSmartGradebookSession

    def can_manage_smart_gradebooks(self):
        """Tests if this user can manage smart gradebooks.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer smart
        operations.

        :return: ``false`` if smart gradebook methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_gradebook_column_query(self, gradebook_column_query):
        """Applies a gradebook column query to this gradebook.

        :param gradebook_column_query: the gradebook column query
        :type gradebook_column_query: ``osid.grading.GradebookColumnQuery``
        :raise: ``NullArgument`` -- ``gradebook_column_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``gradebook_column_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_gradebook_column_query(self):
        """Gets a gradebook column query inspector for this gradebook.

        :return: the gradebook column query inspector
        :rtype: ``osid.grading.GradebookColumnQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_gradebook_column_sequencing(self, gradebook_column_search_order):
        """Applies a gradebook column search order to this gradebook.

        :param gradebook_column_search_order: the gradebook column search order
        :type gradebook_column_search_order: ``osid.grading.GradebookColumnSearchOrder``
        :raise: ``NullArgument`` -- ``gradebook_column_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``gradebook_column_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradebookLookupSession

    def can_lookup_gradebooks(self):
        """Tests if this user can perform ``Gradebook`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_gradebooks_by_ids(self, gradebook_ids):
        """Gets a ``GradebookList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the
        gradebooks specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Gradebook`` objects may be omitted from the list
        and may present the elements in any order including returning a
        unique set.

        :param gradebook_ids: the list of ``Ids`` to retrieve
        :type gradebook_ids: ``osid.id.IdList``
        :return: the returned ``Gradebook`` list
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``gradebook_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebooks_by_genus_type(self, gradebook_genus_type):
        """Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` which does not include gradebooks of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :param gradebook_genus_type: a gradebook genus type
        :type gradebook_genus_type: ``osid.type.Type``
        :return: the returned ``Gradebook`` list
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NullArgument`` -- ``gradebook_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebooks_by_parent_genus_type(self, gradebook_genus_type):
        """Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` and include any additional gradebooks with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :param gradebook_genus_type: a gradebook genus type
        :type gradebook_genus_type: ``osid.type.Type``
        :return: the returned ``Gradebook`` list
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NullArgument`` -- ``gradebook_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebooks_by_record_type(self, gradebook_record_type):
        """Gets a ``GradebookList`` containing the given gradebook record ``Type``.
        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :param gradebook_record_type: a gradebook record type
        :type gradebook_record_type: ``osid.type.Type``
        :return: the returned ``Gradebook`` list
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NullArgument`` -- ``gradebook_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebooks_by_provider(self, resource_id):
        """Gets a ``GradebookList`` for the given provider ````.
        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Gradebook`` list
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebooks(self):
        """Gets all ``Gradebooks``.
        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :return: a ``GradebookList``
        :rtype: ``osid.grading.GradebookList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    gradebooks = property(fget=get_gradebooks)


##
# The following methods are from osid.grading.GradebookQuerySession

    def can_search_gradebooks(self):
        """Tests if this user can perform ``Gradebook`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_query(self):
        """Gets a gradebook query.

        :return: a gradebook query
        :rtype: ``osid.grading.GradebookQuery``

        """
        raise UNIMPLEMENTED()

    gradebook_query = property(fget=get_gradebook_query)

    def get_gradebooks_by_query(self, gradebook_query):
        """Gets a list of ``Gradebook`` objects matching the given gradebook query.

        :param gradebook_query: the gradebook query
        :type gradebook_query: ``osid.grading.GradebookQuery``
        :return: the returned ``GradebookList``
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NullArgument`` -- ``gradebook_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``gradebook_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradebookSearchSession

    def get_gradebook_search(self):
        """Gets a gradebook search.

        :return: a gradebook search
        :rtype: ``osid.grading.GradebookSearch``

        """
        raise UNIMPLEMENTED()

    gradebook_search = property(fget=get_gradebook_search)

    def get_gradebook_search_order(self):
        """Gets a gradebook search order.
        The ``GradebookSearchOrder`` is supplied to a
        ``GradebookSearch`` to specify the ordering of results.

        :return: the gradebook search order
        :rtype: ``osid.grading.GradebookSearchOrder``

        """
        raise UNIMPLEMENTED()

    gradebook_search_order = property(fget=get_gradebook_search_order)

    def get_gradebooks_by_search(self, gradebook_query, gradebook_search):
        """Gets the search results matching the given search query using the given search.

        :param gradebook_query: the gradebook query
        :type gradebook_query: ``osid.grading.GradebookQuery``
        :param gradebook_search: the gradebook search
        :type gradebook_search: ``osid.grading.GradebookSearch``
        :return: the gradebook search results
        :rtype: ``osid.grading.GradebookSearchResults``
        :raise: ``NullArgument`` -- ``gradebook_query`` or ``gradebook_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``gradebook_query`` or ``gradebook_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_gradebook_query_from_inspector(self, gradebook_query_inspector):
        """Gets a gradebook query from an inspector.
        The inspector is available from an ``GradenookSearchResults``.

        :param gradebook_query_inspector: a gradebook query inspector
        :type gradebook_query_inspector: ``osid.grading.GradebookQueryInspector``
        :return: the gradebook query
        :rtype: ``osid.grading.GradebookQuery``
        :raise: ``NullArgument`` -- ``gradebook_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``gradebook_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradebookAdminSession

    def can_create_gradebooks(self):
        """Tests if this user can create ``Gradebooks``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Gradebook`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_gradebook_with_record_types(self, gradebook_record_types):
        """Tests if this user can create a single ``Gradebook`` using the desired record types.
        While ``GradingManager.getGradebookRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Gradebook``.
        Providing an empty array tests if a ``Gradebook`` can be created
        with no records.

        :param gradebook_record_types: array of gradebook record types
        :type gradebook_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Gradebook`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_form_for_create(self, gradebook_record_types):
        """Gets the gradebook form for creating new gradebooks.
        A new form should be requested for each create transaction.

        :param gradebook_record_types: array of gradebook record types
        :type gradebook_record_types: ``osid.type.Type[]``
        :return: the gradebook form
        :rtype: ``osid.grading.GradebookForm``
        :raise: ``NullArgument`` -- ``gradebook_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_gradebook(self, gradebook_form):
        """Creates a new ``Gradebook``.

        :param gradebook_form: the form for this ``Gradebook``
        :type gradebook_form: ``osid.grading.GradebookForm``
        :return: the new ``Gradebook``
        :rtype: ``osid.grading.Gradebook``
        :raise: ``IllegalState`` -- ``gradebook_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``gradebook_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``gradebook_form`` did not originate from ``get_gradebook_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_gradebooks(self):
        """Tests if this user can update ``Gradebooks``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Gradebook`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_form_for_update(self, gradebook_id):
        """Gets the gradebook form for updating an existing gradebook.
        A new gradebook form should be requested for each update
        transaction.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: the gradebook form
        :rtype: ``osid.grading.GradebookForm``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_gradebook(self, gradebook_form):
        """Updates an existing gradebook.

        :param gradebook_form: the form containing the elements to be updated
        :type gradebook_form: ``osid.grading.GradebookForm``
        :raise: ``IllegalState`` -- ``gradebook_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``gradebook_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``gradebook_form did not originate from get_gradebook_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_gradebooks(self):
        """Tests if this user can delete gradebooks.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Gradebook`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_gradebook(self, gradebook_id):
        """Deletes a ``Gradebook``.

        :param gradebook_id: the ``Id`` of the ``Gradebook`` to remove
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_gradebook_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Gradebooks``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Gradebook`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_gradebook(self, gradebook_id, alias_id):
        """Adds an ``Id`` to a ``Gradebook`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Gradebook`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id`` . If the alias is a pointer to another gradebook, it is
        reassigned to the given gradebook ``Id``.

        :param gradebook_id: the ``Id`` of a ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradebookNotificationSession

    def can_register_for_gradebook_notifications(self):
        """Tests if this user can register for ``Gradebook`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_gradebooks(self):
        """Register for notifications of new gradebooks.
        ``GradebookReceiver.newGradebook()`` is invoked when a new
        ``Gradebook`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_gradebook_ancestors(self, gradebook_id):
        """Registers for notification if an ancestor is added to the specified gradebook in the gradebook hierarchy.
        ``GradebookReceiver.newGradebookAncestor()`` is invoked when the
        specified gradebook experiences an addition in ancestry.

        :param gradebook_id: the ``Id`` of the gradebook to monitor
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_gradebook_descendants(self, gradebook_id):
        """Registers for notification if a descendant is added to the specified gradebook in the gradebook hierarchy.
        ``GradebookReceiver.newGradebookDescendant()`` is invoked when
        the specified gradebook experiences an addition in descendants.

        :param gradebook_id: the ``Id`` of the gradebook to monitor
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_gradebooks(self):
        """Registers for notification of updated gradebooks.
        ``GradebookReceiver.changedGradebook()`` is invoked when a
        gradebook is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_gradebook(self, gradebook_id):
        """Registers for notification of an updated gradebook.
        ``GradebookReceiver.changedGradebook()`` is invoked when the
        specified gradebook is changed.

        :param gradebook_id: the ``Id`` of the gradebook to monitor
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_gradebooks(self):
        """Registers for notification of deleted gradebooks.
        ``GradebookReceiver.deletedGradebook()`` is invoked when a
        calenedar is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_gradebook(self, gradebook_id):
        """Registers for notification of a deleted gradebook.
        ``GradebookReceiver.deletedGradebook()`` is invoked when the
        specified gradebook is deleted.

        :param gradebook_id: the ``Id`` of the gradebook to monitor
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_gradebook_ancestors(self, gradebook_id):
        """Registers for notification if an ancestor is removed from the specified gradebook in the gradebook hierarchy.
        ``GradebookReceiver.deletedGradebookAncestor()`` is invoked when
        the specified gradebook experiences a removal of an ancestor.

        :param gradebook_id: the ``Id`` of the gradebook to monitor
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_gradebook_descendants(self, gradebook_id):
        """Registers for notification if a descendant is removed from fthe specified gradebook in the calndar hierarchy.
        ``GradebookReceiver.deletedGradebookDescednant()`` is invoked
        when the specified gradebook experiences a removal of one of its
        descendants.

        :param gradebook_id: the ``Id`` of the gradebook to monitor
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradebookHierarchySession

    def get_gradebook_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    gradebook_hierarchy_id = property(fget=get_gradebook_hierarchy_id)

    def get_gradebook_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    gradebook_hierarchy = property(fget=get_gradebook_hierarchy)

    def can_access_gradebook_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer hierrachy
        traversal operations to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_gradebook_ids(self):
        """Gets the root gradebook ``Ids`` in this hierarchy.

        :return: the root gradebook ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_gradebook_ids = property(fget=get_root_gradebook_ids)

    def get_root_gradebooks(self):
        """Gets the root gradebooks in this gradebook hierarchy.

        :return: the root gradebooks
        :rtype: ``osid.grading.GradebookList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_gradebooks = property(fget=get_root_gradebooks)

    def has_parent_gradebooks(self, gradebook_id):
        """Tests if the ``Gradebook`` has any parents.

        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``true`` if the gradebook has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_gradebook(self, id_, gradebook_id):
        """Tests if an ``Id`` is a direct parent of a gradebook.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``gradebook_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_gradebook_ids(self, gradebook_id):
        """Gets the parent ``Ids`` of the given gradebook.

        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the gradebook
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_gradebooks(self, gradebook_id):
        """Gets the parents of the given gradebook.

        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: the parents of the gradebook
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_gradebook(self, id_, gradebook_id):
        """Tests if an ``Id`` is an ancestor of a gradebook.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``gradebook_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_gradebooks(self, gradebook_id):
        """Tests if a gradebook has any children.

        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``true`` if the ``gradebook_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_gradebook(self, id_, gradebook_id):
        """Tests if a gradebook is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``gradebook_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_gradebook_ids(self, gradebook_id):
        """Gets the child ``Ids`` of the given gradebook.

        :param gradebook_id: the ``Id`` to query
        :type gradebook_id: ``osid.id.Id``
        :return: the children of the gradebook
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_gradebooks(self, gradebook_id):
        """Gets the children of the given gradebook.

        :param gradebook_id: the ``Id`` to query
        :type gradebook_id: ``osid.id.Id``
        :return: the children of the gradebook
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_gradebook(self, id_, gradebook_id):
        """Tests if an ``Id`` is a descendant of a gradebook.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``gradebook_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebook_node_ids(self, gradebook_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given gradebook.

        :param gradebook_id: the ``Id`` to query
        :type gradebook_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a gradebook node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebook_nodes(self, gradebook_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given gradebook.

        :param gradebook_id: the ``Id`` to query
        :type gradebook_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a gradebook node
        :rtype: ``osid.grading.GradebookNode``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradebookHierarchyDesignSession

    def can_modify_gradebook_hierarchy(self):
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

    def add_root_gradebook(self, gradebook_id):
        """Adds a root gradebook.

        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``gradebook_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_gradebook(self, gradebook_id):
        """Removes a root gradebook.

        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``gradebook_id`` is not a root
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_gradebook(self, gradebook_id, child_id):
        """Adds a child to a gradebook.

        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``gradebook_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``gradebook_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_gradebook(self, gradebook_id, child_id):
        """Removes a child from a gradebook.

        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``gradebook_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class GradingProxyManager(osid_managers.OsidProxyManager, GradingProfile):

    def get_grade_system_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade system lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemLookupSession``
        :rtype: ``osid.grading.GradeSystemLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_lookup_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade system lookup service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradeSystemLookupSession``
        :rtype: ``osid.grading.GradeSystemLookupSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade system query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemQuerySession``
        :rtype: ``osid.grading.GradeSystemQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_query_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade system query service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradeSystemQuerySession``
        :rtype: ``osid.grading.GradeSystemQuerySession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade system search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemSearchSession``
        :rtype: ``osid.grading.GradeSystemSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_search_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade system search service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradeSystemSearchSession``
        :rtype: ``osid.grading.GradeSystemSearchSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade system administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemAdminSession``
        :rtype: ``osid.grading.GradeSystemAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_admin_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade system admin service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradeSystemAdminSession``
        :rtype: ``osid.grading.GradeSystemAdminSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_notification_session(self, grade_system_receiver, proxy):
        """Gets the notification session for notifications pertaining to grade system changes.

        :param grade_system_receiver: the grade system receiver
        :type grade_system_receiver: ``osid.grading.GradeSystemReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemNotificationSession``
        :rtype: ``osid.grading.GradeSystemNotificationSession``
        :raise: ``NullArgument`` -- ``grade_system_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_notification_session_for_gradebook(self, grade_system_receiver, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade system notification service for the given gradebook.

        :param grade_system_receiver: the grade system receiver
        :type grade_system_receiver: ``osid.grading.GradeSystemReceiver``
        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a _grade_system_notification_session``
        :rtype: ``osid.grading.GradeSystemNotificationSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``grade_system_receiver, gradebook_id`` or ``porxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_system_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_gradebook_session(self, proxy):
        """Gets the session for retrieving grade system to gradebook mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemGradebookSession``
        :rtype: ``osid.grading.GradeSystemGradebookSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_gradebook()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_gradebook_assignment_session(self, proxy):
        """Gets the session for assigning grade system to gradebook mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemGradebookAssignmentSession``
        :rtype: ``osid.grading.GradeSystemGradebookSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_gradebook_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_smart_gradebook_session(self, gradebook_id, proxy):
        """Gets the session for managing smart gradebooks of grade systems.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemSmartGradebookSession``
        :rtype: ``osid.grading.GradeSystemSmartGradebookSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_smart_gradebook()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade entry lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeEntryLookupSession``
        :rtype: ``osid.grading.GradeEntryLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_lookup_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade entry lookup service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradeEntryLookupSession``
        :rtype: ``osid.grading.GradeEntryLookupSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade entry query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeEntryQuerySession``
        :rtype: ``osid.grading.GradeEntryQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_query_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade entry query service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradeEntryQuerySession``
        :rtype: ``osid.grading.GradeEntryQuerySession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade entry search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeEntrySearchSession``
        :rtype: ``osid.grading.GradeEntrySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_search_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade entry search service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradeEntrySearchSession``
        :rtype: ``osid.grading.GradeEntrySearchSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade entry administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeEntryAdminSession``
        :rtype: ``osid.grading.GradeEntryAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_admin_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade entry admin service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradeEntryAdminSession``
        :rtype: ``osid.grading.GradeEntryAdminSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_notification_session(self, grade_entry_receiver, proxy):
        """Gets the notification session for notifications pertaining to grade entry changes.

        :param grade_entry_receiver: the grade entry receiver
        :type grade_entry_receiver: ``osid.grading.GradeEntryReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeEntryNotificationSession``
        :rtype: ``osid.grading.GradeEntryNotificationSession``
        :raise: ``NullArgument`` -- ``grade_entry_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_notification_session_for_gradebook(self, grade_entry_receiver, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the grade entry notification service for the given gradebook.

        :param grade_entry_receiver: the grade entry receiver
        :type grade_entry_receiver: ``osid.grading.GradeEntryReceiver``
        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a _grade_entry_notification_session``
        :rtype: ``osid.grading.GradeEntryNotificationSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``grade_entry_receiver, gradebook_id`` or ``porxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_grade_entry_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnLookupSession``
        :rtype: ``osid.grading.GradebookColumnLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_lookup_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column lookup service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a _gradebook_column_lookup_session``
        :rtype: ``osid.grading.GradebookColumnLookupSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnQuerySession``
        :rtype: ``osid.grading.GradebookColumnQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_query_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column query service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnQuerySession``
        :rtype: ``osid.grading.GradebookColumnQuerySession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnSearchSession``
        :rtype: ``osid.grading.GradebookColumnSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_search_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column search service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a _gradebook_column_search_session``
        :rtype: ``osid.grading.GradebookColumnSearchSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnAdminSession``
        :rtype: ``osid.grading.GradebookColumnAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_admin_session_for_gradebook(self, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column admin service for the given gradebook.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a GradebookColumnAdminSession``
        :rtype: ``osid.grading.GradebookColumnAdminSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_notification_session(self, gradebook_column_receiver, proxy):
        """Gets the notification session for notifications pertaining to gradebook column changes.

        :param gradebook_column_receiver: the grade system receiver
        :type gradebook_column_receiver: ``osid.grading.GradebookColumnReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnNotificationSession``
        :rtype: ``osid.grading.GradebookColumnNotificationSession``
        :raise: ``NullArgument`` -- ``gradebook_column_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_notification_session_for_gradebook(self, gradebook_column_receiver, gradebook_id, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column notification service for the given gradebook.

        :param gradebook_column_receiver: the gradebook column receiver
        :type gradebook_column_receiver: ``osid.grading.GradebookColumnReceiver``
        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a _gradebook_column_notification_session``
        :rtype: ``osid.grading.GradebookColumnNotificationSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_column_receiver, gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_gradebook_session(self, proxy):
        """Gets the session for retrieving gradebook column to gradebook mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnGradebookSession``
        :rtype: ``osid.grading.GradebookColumnGradebookSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_gradebook()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_gradebook_assignment_session(self, proxy):
        """Gets the session for assigning gradebook column to gradebook mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnGradebookAssignmentSession``
        :rtype: ``osid.grading.GradebookColumnGradebookAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_gradebook_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_column_smart_gradebook_session(self, gradebook_id, proxy):
        """Gets the session for managing smart gradebooks of gradebook columns.

        :param gradebook_id: the ``Id`` of the gradebook
        :type gradebook_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnSmartGradebookSession``
        :rtype: ``osid.grading.GradebookColumnSmartGradebookSession``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_smart_gradebook()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_lookup_session(self, proxy):
        """Gets the OsidSession associated with the gradebook lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookLookupSession``
        :rtype: ``osid.grading.GradebookLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_lookup() is false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_query_session(self, proxy):
        """Gets the OsidSession associated with the gradebook query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookQuerySession``
        :rtype: ``osid.grading.GradebookQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_query() is false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_search_session(self, proxy):
        """Gets the OsidSession associated with the gradebook search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookSearchSession``
        :rtype: ``osid.grading.GradebookSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_search() is false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_admin_session(self, proxy):
        """Gets the OsidSession associated with the gradebook administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookAdminSession``
        :rtype: ``osid.grading.GradebookAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_admin() is false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_notification_session(self, gradebook_receiver, proxy):
        """Gets the notification session for notifications pertaining to gradebook service changes.

        :param gradebook_receiver: the gradebook receiver
        :type gradebook_receiver: ``osid.grading.GradebookReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookNotificationSession``
        :rtype: ``osid.grading.GradebookNotificationSession``
        :raise: ``NullArgument`` -- ``gradebook_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_notification() is false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_hierarchy_session(self, proxy):
        """Gets the session traversing gradebook hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookHierarchySession``
        :rtype: ``osid.grading.GradebookHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_hierarchy() is false``

        """
        raise UNIMPLEMENTED()

    def get_gradebook_hierarchy_design_session(self, proxy):
        """Gets the session designing gradebook hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookHierarchyDesignSession``
        :rtype: ``osid.grading.GradebookHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_hierarchy_design() is false``

        """
        raise UNIMPLEMENTED()

    def get_grading_batch_proxy_manager(self):
        """Gets the ``GradingBatchProxyManager``.

        :return: a ``GradingBatchProxyManager``
        :rtype: ``osid.grading.batch.GradingBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_batch() is false``

        """
        raise UNIMPLEMENTED()

    grading_batch_proxy_manager = property(fget=get_grading_batch_proxy_manager)

    def get_grading_calculation_proxy_manager(self):
        """Gets the ``GradingCalculationProxyManager``.

        :return: a ``GradingCalculationProxyManager``
        :rtype: ``osid.grading.calculation.GradingCalculationProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_calculation() is false``

        """
        raise UNIMPLEMENTED()

    grading_calculation_proxy_manager = property(fget=get_grading_calculation_proxy_manager)

    def get_grading_transform_proxy_manager(self):
        """Gets the ``GradingTransformProxyManager``.

        :return: a ``GradingTransformManager``
        :rtype: ``osid.grading.transform.GradingTransformProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_transform() is false``

        """
        raise UNIMPLEMENTED()

    grading_transform_proxy_manager = property(fget=get_grading_transform_proxy_manager)



class Gradebook(osid_objects.OsidCatalog, osid_sessions.OsidSession):

    def get_gradebook_record(self, gradebook_record_type):
        """Gets the gradebook record corresponding to the given ``Gradebook`` record ``Type``.
        This method is used to retrieve an object implementing the
        requested record. The ``gradebook_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(gradebook_record_type)`` is ``true`` .

        :param gradebook_record_type: a gradebook record type
        :type gradebook_record_type: ``osid.type.Type``
        :return: the gradebook record
        :rtype: ``osid.grading.records.GradebookRecord``
        :raise: ``NullArgument`` -- ``gradebook_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(gradebook_record_type)`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradeSystemLookupSession

    def get_gradebook_id(self):
        """Gets the ``GradeSystem``  ``Id`` associated with this session.

        :return: the ``GradeSystem Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    gradebook = property(fget=get_gradebook)

    def can_lookup_grade_systems(self):
        """Tests if this user can perform ``GradeSystem`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_grade_system_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_grade_system_view(self):
        """A complete view of the ``GradeSystem`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.
        A federated view will include grade entries in gradebooks which
        are children of this gradebook in the gradebook hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this gradebook only.



        """
        raise UNIMPLEMENTED()

    def get_grade_system(self, grade_system_id):
        """Gets the ``GradeSystem`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``GradeSystem`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``GradeSystem`` and retained
        for compatibility.

        :param grade_system_id: ``Id`` of the ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :return: the grade system
        :rtype: ``osid.grading.GradeSystem``
        :raise: ``NotFound`` -- ``grade_system_id`` not found
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_system_by_grade(self, grade_id):
        """Gets the ``GradeSystem`` by a ``Grade``  ``Id``.

        :param grade_id: ``Id`` of a ``Grade``
        :type grade_id: ``osid.id.Id``
        :return: the grade system
        :rtype: ``osid.grading.GradeSystem``
        :raise: ``NotFound`` -- ``grade_id`` not found
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_systems_by_ids(self, grade_system_ids):
        """Gets a ``GradeSystemList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the systems
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``GradeSystems`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param grade_system_ids: the list of ``Ids`` to retrieve
        :type grade_system_ids: ``osid.id.IdList``
        :return: the returned ``GradeSystem`` list
        :rtype: ``osid.grading.GradeSystemList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``grade_system_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_systems_by_genus_type(self, grade_system_genus_type):
        """Gets a ``GradeSystemList`` corresponding to the given grade system genus ``Type`` which does not include systems of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known systems or
        an error results. Otherwise, the returned list may contain only
        those systems that are accessible through this session.

        :param grade_system_genus_type: a grade system genus type
        :type grade_system_genus_type: ``osid.type.Type``
        :return: the returned ``GradeSystem`` list
        :rtype: ``osid.grading.GradeSystemList``
        :raise: ``NullArgument`` -- ``grade_system_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_systems_by_parent_genus_type(self, grade_system_genus_type):
        """Gets a ``GradeSystemList`` corresponding to the given grade system genus ``Type`` and include any additional systems with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known systems or
        an error results. Otherwise, the returned list may contain only
        those systems that are accessible through this session.

        :param grade_system_genus_type: a grade system genus type
        :type grade_system_genus_type: ``osid.type.Type``
        :return: the returned ``GradeSystem`` list
        :rtype: ``osid.grading.GradeSystemList``
        :raise: ``NullArgument`` -- ``grade_system_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_systems_by_record_type(self, grade_system_record_type):
        """Gets a ``GradeSystemList`` containing the given grade record ``Type``.
        In plenary mode, the returned list contains all known systems or
        an error results. Otherwise, the returned list may contain only
        those systems that are accessible through this session.

        :param grade_system_record_type: a grade system record type
        :type grade_system_record_type: ``osid.type.Type``
        :return: the returned ``GradeSystem`` list
        :rtype: ``osid.grading.GradeSystemList``
        :raise: ``NullArgument`` -- ``grade_system_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_systems(self):
        """Gets all ``GradeSystems``.
        In plenary mode, the returned list contains all known grade
        systems or an error results. Otherwise, the returned list may
        contain only those grade systems that are accessible through
        this session.

        :return: a ``GradeSystemList``
        :rtype: ``osid.grading.GradeSystemList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    grade_systems = property(fget=get_grade_systems)


##
# The following methods are from osid.grading.GradeSystemQuerySession

    def can_search_grade_systems(self):
        """Tests if this user can perform ``GradeSystem`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_query(self):
        """Gets a grade system query.

        :return: a grade system query
        :rtype: ``osid.grading.GradeSystemQuery``

        """
        raise UNIMPLEMENTED()

    grade_system_query = property(fget=get_grade_system_query)

    def get_grade_systems_by_query(self, grade_system_query):
        """Gets a list of ``GradeSystem`` objects matching the given grade system query.

        :param grade_system_query: the grade system query
        :type grade_system_query: ``osid.grading.GradeSystemQuery``
        :return: the returned ``GradeSystemList``
        :rtype: ``osid.grading.GradeSystemList``
        :raise: ``NullArgument`` -- ``grade_system_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_system_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradeSystemSearchSession

    def get_grade_system_search(self):
        """Gets a grade system search.

        :return: a grade system search
        :rtype: ``osid.grading.GradeSystemSearch``

        """
        raise UNIMPLEMENTED()

    grade_system_search = property(fget=get_grade_system_search)

    def get_grade_system_search_order(self):
        """Gets a grade system search order.
        The ``GradeSystemSearchOrder`` is supplied to a
        ``GradeSystemSearch`` to specify the ordering of results.

        :return: the grade system search order
        :rtype: ``osid.grading.GradeSystemSearchOrder``

        """
        raise UNIMPLEMENTED()

    grade_system_search_order = property(fget=get_grade_system_search_order)

    def get_grade_systems_by_search(self, grade_system_query, grade_system_search):
        """Gets the search results matching the given search query using the given search.

        :param grade_system_query: the grade system query
        :type grade_system_query: ``osid.grading.GradeSystemQuery``
        :param grade_system_search: the grade system search
        :type grade_system_search: ``osid.grading.GradeSystemSearch``
        :return: the grade system search results
        :rtype: ``osid.grading.GradeSystemSearchResults``
        :raise: ``NullArgument`` -- ``grade_system_query`` or ``grade_system_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_system_query`` or ``grade_system_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_grade_system_query_from_inspector(self, grade_system_query_inspector):
        """Gets a grade system query from an inspector.
        The inspector is available from an ``GradeSystemSearchResults``.

        :param grade_system_query_inspector: a grade system query inspector
        :type grade_system_query_inspector: ``osid.grading.GradeSystemQueryInspector``
        :return: the grade system query
        :rtype: ``osid.grading.GradeSystemQuery``
        :raise: ``NullArgument`` -- ``grade_system_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``grade_system_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradeSystemAdminSession

    def can_create_grade_systems(self):
        """Tests if this user can create ``GradeSystems``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``GradeSystem`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_grade_system_with_record_types(self, grade_system_record_types):
        """Tests if this user can create a single ``GradeSystem`` using the desired record types.
        While ``GradingManager.getGradeSystemRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``GradeSystem``.
        Providing an empty array tests if a ``GradeSystem`` can be
        created with no records.

        :param grade_system_record_types: array of grade system types
        :type grade_system_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``GradeSystem`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_form_for_create(self, grade_system_record_types):
        """Gets the grade system form for creating new grade systems.
        A new form should be requested for each create transaction.

        :param grade_system_record_types: array of grade system types
        :type grade_system_record_types: ``osid.type.Type[]``
        :return: the grade system form
        :rtype: ``osid.grading.GradeSystemForm``
        :raise: ``NullArgument`` -- ``grade_system_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_grade_system(self, grade_system_form):
        """Creates a new ``GradeSystem``.

        :param grade_system_form: the form for this ``GradeSystem``
        :type grade_system_form: ``osid.grading.GradeSystemForm``
        :return: the new ``GradeSystem``
        :rtype: ``osid.grading.GradeSystem``
        :raise: ``IllegalState`` -- ``grade_system_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``grade_system_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_system_form`` did not originate from ``get_grade_system_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_grade_systems(self):
        """Tests if this user can update ``GradeSystems``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``GradeSystem`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_form_for_update(self, grade_system_id):
        """Gets the grade system form for updating an existing grade system.
        A new grade system form should be requested for each update
        transaction.

        :param grade_system_id: the ``Id`` of the ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :return: the grade system form
        :rtype: ``osid.grading.GradeSystemForm``
        :raise: ``NotFound`` -- ``grade_system_id`` is not found
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_grade_system(self, grade_system_form):
        """Updates an existing grade system.

        :param grade_system_form: the form containing the elements to be updated
        :type grade_system_form: ``osid.grading.GradeSystemForm``
        :raise: ``IllegalState`` -- ``grade_system_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``grade_system_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_system_form`` did not originate from ``get_grade_system_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_grade_systems(self):
        """Tests if this user can delete grade systems.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``GradeSystem`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_grade_system(self, grade_system_id):
        """Deletes a ``GradeSystem``.

        :param grade_system_id: the ``Id`` of the ``GradeSystem`` to remove
        :type grade_system_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``grade_system_id`` not found
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_grade_system_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``GradeSystems``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``GradeSystem`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_grade_system(self, grade_system_id, alias_id):
        """Adds an ``Id`` to a ``GradeSystem`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``GradeSystem`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another grade system, it is
        reassigned to the given grade system ``Id``.

        :param grade_system_id: the ``Id`` of a ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``grade_system_id`` not found
        :raise: ``NullArgument`` -- ``grade_system_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_create_grades(self, grade_system_id):
        """Tests if this user can create ``Grade`` s for a ``GradeSystem``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :param grade_system_id: the ``Id`` of a ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :return: ``false`` if ``Grade`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def can_create_grade_with_record_types(self, grade_system_id, grade_record_types):
        """Tests if this user can create a single ``Grade`` using the desired record types.
        While ``GradingManager.getGradeRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Grade``.
        Providing an empty array tests if a ``Grade`` can be created
        with no records.

        :param grade_system_id: the ``Id`` of a ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :param grade_record_types: array of grade recod types
        :type grade_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Grade`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_id`` or ``grade_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_grade_form_for_create(self, grade_system_id, grade_record_types):
        """Gets the grade form for creating new grades.
        A new form should be requested for each create transaction.

        :param grade_system_id: the ``Id`` of a ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :param grade_record_types: array of grade recod types
        :type grade_record_types: ``osid.type.Type[]``
        :return: the grade form
        :rtype: ``osid.grading.GradeForm``
        :raise: ``NotFound`` -- ``grade_system_id`` is not found
        :raise: ``NullArgument`` -- ``grade_system_id`` or ``grade_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_grade(self, grade_form):
        """Creates a new ``Grade``.

        :param grade_form: the form for this ``Grade``
        :type grade_form: ``osid.grading.GradeForm``
        :return: the new ``Grade``
        :rtype: ``osid.grading.Grade``
        :raise: ``IllegalState`` -- ``grade_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``grade_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_form`` did not originate from ``get_grade_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_grades(self, grade_system_id):
        """Tests if this user can update ``Grades``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Grade``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :param grade_system_id: the ``Id`` of a ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :return: ``false`` if ``Grade`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_grade_form_for_update(self, grade_id):
        """Gets the grade form for updating an existing grade.
        A new grade form should be requested for each update
        transaction.

        :param grade_id: the ``Id`` of the ``Grade``
        :type grade_id: ``osid.id.Id``
        :return: the grade form
        :rtype: ``osid.grading.GradeForm``
        :raise: ``NotFound`` -- ``grade_id`` is not found
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_grade(self, grade_form):
        """Updates an existing grade.

        :param grade_form: the form containing the elements to be updated
        :type grade_form: ``osid.grading.GradeForm``
        :raise: ``IllegalState`` -- ``grade_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``grade_id`` or ``grade_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_form`` did not originate from ``get_grade_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_grades(self, grade_system_id):
        """Tests if this user can delete grades.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Grade``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :param grade_system_id: the ``Id`` of a ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :return: ``false`` if ``Grade`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def delete_grade(self, grade_id):
        """Deletes a ``Grade``.

        :param grade_id: the ``Id`` of the ``Grade`` to remove
        :type grade_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``grade_id`` not found
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_grade_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Grades``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Grade`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_grade(self, grade_id, alias_id):
        """Adds an ``Id`` to a ``Grade`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Grade`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another grade, it is
        reassigned to the given grade ``Id``.

        :param grade_id: the ``Id`` of a ``Grade``
        :type grade_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``grade_id`` not found
        :raise: ``NullArgument`` -- ``grade_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradeSystemNotificationSession

    def can_register_for_grade_system_notifications(self):
        """Tests if this user can register for ``GradeSystem`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_grade_systems(self):
        """Register for notifications of new grade systems.
        ``GradeSystemReceiver.newGradeSystem()`` is invoked when a new
        ``GradeSystem`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_grade_systems(self):
        """Registers for notification of updated grade systems.
        ``GradeSystemReceiver.changedGradeSystem()`` is invoked when a
        system is changed or grades are changed within it.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_grade_system(self, grade_system_id):
        """Registers for notification of an updated grade system.
        ``GradeSystemReceiver.changedGradeSystem()`` is invoked when the
        specified grade system is changed or grades are changed within
        it.

        :param grade_system_id: the ``Id`` of the grade system to monitor
        :type grade_system_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``grade_system_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_grade_systems(self):
        """Registers for notification of deleted grade systems.
        ``GradeSystemReceiver.deletedGradeSystem()`` is invoked when a
        grade system is removed from this gradebook.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_grade_system(self, grade_system_id):
        """Registers for notification of a deleted grade system.
        ``GradeSystemReceiver.deletedGradeSystem()`` is invoked when the
        specified system is removed from this gradebook.

        :param grade_system_id: the ``Id`` of the grade system to monitor
        :type grade_system_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``grade_system_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradeSystemGradebookSession

    def use_comparative_gradebook_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_gradebook_view(self):
        """A complete view of the ``GradebookColumn`` and ``Gradebook`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def can_lookup_grade_system_gradebook_mappings(self):
        """Tests if this user can perform lookups of gradebook/grade system mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_grade_system_ids_by_gradebook(self, gradebook_id):
        """Gets the list of ``GradeSystem``  ``Ids`` associated with a ``Gradebook``.

        :param gradebook_id: ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: list of related grade system ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_systems_by_gradebook(self, gradebook_id):
        """Gets the list of grade systems associated with a ``Gradebook``.

        :param gradebook_id: ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: list of related grade systems
        :rtype: ``osid.grading.GradeSystemList``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_system_ids_by_gradebooks(self, gradebook_ids):
        """Gets the list of ``GradeSystem Ids`` corresponding to a list of ``Gradebooks``.

        :param gradebook_ids: list of gradebook ``Ids``
        :type gradebook_ids: ``osid.id.IdList``
        :return: list of grade systems ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_systems_by_gradebooks(self, gradebook_ids):
        """Gets the list of grade systems corresponding to a list of ``Gradebooks``.

        :param gradebook_ids: list of gradebook ``Ids``
        :type gradebook_ids: ``osid.id.IdList``
        :return: list of grade systems
        :rtype: ``osid.grading.GradeSystemList``
        :raise: ``NullArgument`` -- ``gradebook_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebook_ids_by_grade_system(self, grade_system_id):
        """Gets the list of ``Gradebook``  ``Ids`` mapped to a ``GradeSystem``.

        :param grade_system_id: ``Id`` of a ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :return: list of gradebook ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``grade_system_id`` is not found
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_gradebooks_by_grade_system(self, grade_system_id):
        """Gets the list of ``Gradebooks`` mapped to a ``GradeSystem``.

        :param grade_system_id: ``Id`` of a ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :return: list of gradebooks
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NotFound`` -- ``grade_system_id`` is not found
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradeSystemGradebookAssignmentSession

    def can_assign_grade_system(self):
        """Tests if this user can alter grade system/gradebook mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_grade_systems_to_gradebook(self, gradebook_id):
        """Tests if this user can alter grade system/gradebook mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_gradebook_ids(self, gradebook_id):
        """Gets a list of gradebooks including and under the given gradebook node in which any grade system can be assigned.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: list of assignable gradebook ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_gradebook_ids_for_grade_system(self, gradebook_id, grade_system_id):
        """Gets a list of gradebooks including and under the given gradebook node in which a specific grade system can be assigned.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :param grade_system_id: the ``Id`` of the ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :return: list of assignable gradebook ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``grade_system_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_grade_system_to_gradebook(self, grade_system_id, gradebook_id):
        """Adds an existing ``GradeSystem`` to a ``Gradebook``.

        :param grade_system_id: the ``Id`` of the ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``grade_system_id`` is already assigned to ``gradebook_id``
        :raise: ``NotFound`` -- ``grade_system_id`` or ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``grade_system_id`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_grade_system_from_gradebook(self, grade_system_id, gradebook_id):
        """Removes a ``GradeSystem`` from a ``Gradebook``.

        :param grade_system_id: the ``Id`` of the ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``grade_system_id`` or ``gradebook_id`` not found or ``grade_system_id`` not assigned to ``gradebook_id``
        :raise: ``NullArgument`` -- ``grade_system_id`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradeSystemSmartGradebookSession

    def can_manage_smart_gradebooks(self):
        """Tests if this user can manage smart gradebooks.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer smart
        operations.

        :return: ``false`` if smart gradebook methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_grade_system_query(self, grade_system_query):
        """Applies a grade system query to this gradebook.

        :param grade_system_query: the grade system query
        :type grade_system_query: ``osid.grading.GradeSystemQuery``
        :raise: ``NullArgument`` -- ``grade_system_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``grade_system_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_grade_system_query(self):
        """Gets a grade system query inspector for this gradebook.

        :return: the grade system query inspector
        :rtype: ``osid.grading.GradeSystemQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_grade_system_sequencing(self, grade_system_search_order):
        """Applies a grade system search order to this gradebook.

        :param grade_system_search_order: the grade system search order
        :type grade_system_search_order: ``osid.grading.GradeSystemSearchOrder``
        :raise: ``NullArgument`` -- ``grade_system_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``grade_system_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradeEntryLookupSession

    def can_lookup_grade_entries(self):
        """Tests if this user can perform ``GradeEntry`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_grade_entry_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_grade_entry_view(self):
        """A complete view of the ``GradeEntry`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_effective_grade_entry_view(self):
        """Only grade entries whose effective dates are current are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_any_effective_grade_entry_view(self):
        """All grade entries of any effective dates are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def get_grade_entry(self, grade_entry_id):
        """Gets the ``GradeEntry`` specified by its ``Id``.

        :param grade_entry_id: ``Id`` of the ``GradeEntry``
        :type grade_entry_id: ``osid.id.Id``
        :return: the grade entry
        :rtype: ``osid.grading.GradeEntry``
        :raise: ``NotFound`` -- ``grade_entry_id`` not found
        :raise: ``NullArgument`` -- ``grade_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_entries_by_ids(self, grade_entry_ids):
        """Gets a ``GradeEntryList`` corresponding to the given ``IdList``.

        :param grade_entry_ids: the list of ``Ids`` to retrieve
        :type grade_entry_ids: ``osid.id.IdList``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``grade_entry_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_entries_by_genus_type(self, grade_entry_genus_type):
        """Gets a ``GradeEntryList`` corresponding to the given grade entry genus ``Type`` which does not include grade entries of genus types derived from the specified ``Type``.

        :param grade_entry_genus_type: a grade entry genus type
        :type grade_entry_genus_type: ``osid.type.Type``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``grade_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_entries_by_parent_genus_type(self, grade_entry_genus_type):
        """Gets a ``GradeEntryList`` corresponding to the given grade entry genus ``Type`` and include any additional grade entry with genus types derived from the specified ``Type``.

        :param grade_entry_genus_type: a grade entry genus type
        :type grade_entry_genus_type: ``osid.type.Type``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``grade_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_entries_by_record_type(self, grade_entry_record_type):
        """Gets a ``GradeEntryList`` containing the given grade entry record ``Type``.

        :param grade_entry_record_type: a grade entry record type
        :type grade_entry_record_type: ``osid.type.Type``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``grade_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_entries_on_date(self, from_, to):
        """Gets a ``GradeEntryList`` effective during the entire given date range inclusive but not confined to the date range.

        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from or to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_entries_for_gradebook_column(self, gradebook_column_id):
        """Gets a ``GradeEntryList`` for the gradebook column.

        :param gradebook_column_id: a gradebook column ``Id``
        :type gradebook_column_id: ``osid.id.Id``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_entries_for_gradebook_column_on_date(self, gradebook_column_id, from_, to):
        """Gets a ``GradeEntryList`` for the given gradebook column and effective during the entire given date range inclusive but not confined to the date range.

        :param gradebook_column_id: a gradebook column ``Id``
        :type gradebook_column_id: ``osid.id.Id``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``gradebook_column_id, from, or to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_entries_for_resource(self, resource_id):
        """Gets a ``GradeEntryList`` for the given key key resource.

        :param resource_id: a key resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_entries_for_resource_on_date(self, resource_id, from_, to):
        """Gets a ``GradeEntryList`` for the given key resource and effective during the entire given date range inclusive but not confined to the date range.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, from, or to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_entries_for_gradebook_column_and_resource(self, gradebook_column_id, resource_id):
        """Gets a ``GradeEntryList`` for the gradebook column and key resource.

        :param gradebook_column_id: a gradebook column ``Id``
        :type gradebook_column_id: ``osid.id.Id``
        :param resource_id: a key resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``gradebook_column_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_entries_for_gradebook_column_and_resource_on_date(self, gradebook_column_id, resource_id, from_, to):
        """Gets a ``GradeEntryList`` for the given gradebook column, resource, and effective during the entire given date range inclusive but not confined to the date range.

        :param gradebook_column_id: a gradebook column ``Id``
        :type gradebook_column_id: ``osid.id.Id``
        :param resource_id: a key resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``gradebook_column_id, resource, from, or to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_entries_by_grader(self, resource_id):
        """Gets a ``GradeEntryList`` for the given grader.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_grade_entries(self):
        """Gets all grade entries.

        :return: a ``GradeEntryList``
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    grade_entries = property(fget=get_grade_entries)


##
# The following methods are from osid.grading.GradeEntryQuerySession

    def can_search_grade_entries(self):
        """Tests if this user can perform ``GradeEntry`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_query(self):
        """Gets a grade entry query.

        :return: the grade entry query
        :rtype: ``osid.grading.GradeEntryQuery``

        """
        raise UNIMPLEMENTED()

    grade_entry_query = property(fget=get_grade_entry_query)

    def get_grade_entries_by_query(self, grade_entry_query):
        """Gets a list of entries matching the given grade entry query.

        :param grade_entry_query: the grade entry query
        :type grade_entry_query: ``osid.grading.GradeEntryQuery``
        :return: the returned ``GradeEntryList``
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``grade_entry_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_entry_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradeEntrySearchSession

    def get_grade_entry_search(self):
        """Gets a grade entry search.

        :return: the grade entry search
        :rtype: ``osid.grading.GradeEntrySearch``

        """
        raise UNIMPLEMENTED()

    grade_entry_search = property(fget=get_grade_entry_search)

    def get_grade_entry_search_order(self):
        """Gets a grade entry search order.
        The ``GradeEntrySearchOrder`` is supplied to a
        ``GradeEntrySearch`` to specify the ordering of results.

        :return: the grade entry search order
        :rtype: ``osid.grading.GradeEntrySearchOrder``

        """
        raise UNIMPLEMENTED()

    grade_entry_search_order = property(fget=get_grade_entry_search_order)

    def get_grade_entries_by_search(self, grade_entry_query, grade_entry_search):
        """Gets the search results matching the given search query using the given search.

        :param grade_entry_query: the grade entry query
        :type grade_entry_query: ``osid.grading.GradeEntryQuery``
        :param grade_entry_search: the grade entry search
        :type grade_entry_search: ``osid.grading.GradeEntrySearch``
        :return: the grade entry search results
        :rtype: ``osid.grading.GradeEntrySearchResults``
        :raise: ``NullArgument`` -- ``grade_entry_query`` or ``grade_entry_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_entry_search`` or ``grade_entry_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_query_from_inspector(self, grade_entry_query_inspector):
        """Gets a grade entry query from an inspector.
        The inspector is available from an ``GradeEntrySearchResults``.

        :param grade_entry_query_inspector: a grade entry query inspector
        :type grade_entry_query_inspector: ``osid.grading.GradeEntryQueryInspector``
        :return: the grade entry query
        :rtype: ``osid.grading.GradeEntryQuery``
        :raise: ``NullArgument`` -- ``grade_entry_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``grade_entry_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradeEntryAdminSession

    def can_create_grade_entries(self):
        """Tests if this user can create grade entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a grade
        entry will result in a ``PermissionDenied``. This is intended as
        a hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``GradeEntry`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_grade_entry_with_record_types(self, grade_entry_record_types):
        """Tests if this user can create a single ``GradeEntry`` using the desired record types.
        While ``GradingManager.getGradeEntryRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``GradeEntry``.
        Providing an empty array tests if a ``GradeEntry`` can be
        created with no records.

        :param grade_entry_record_types: array of grade entry record types
        :type grade_entry_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``GradeEntry`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_entry_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_form_for_create(self, gradebook_column_id, resource_id, grade_entry_record_types):
        """Gets the grade entry form for creating new grade entries.
        A new form should be requested for each create transaction.

        :param gradebook_column_id: the gradebook column
        :type gradebook_column_id: ``osid.id.Id``
        :param resource_id: the key resource
        :type resource_id: ``osid.id.Id``
        :param grade_entry_record_types: array of grade entry record types
        :type grade_entry_record_types: ``osid.type.Type[]``
        :return: the grade entry form
        :rtype: ``osid.grading.GradeEntryForm``
        :raise: ``NotFound`` -- ``gradebook_column_id or resource_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_column_id, resource_id,`` or ``grade_entry_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_grade_entry(self, grade_entry_form):
        """Creates a new ``GradeEntry``.

        :param grade_entry_form: the form for this ``GradeEntry``
        :type grade_entry_form: ``osid.grading.GradeEntryForm``
        :return: the new ``GradeEntry``
        :rtype: ``osid.grading.GradeEntry``
        :raise: ``IllegalState`` -- ``grade_entry_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``grade_entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_entry_form`` did not originate from ``get_grade_entry_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_overridecalculated_grade_entries(self):
        """Tests if this user can override grade entries calculated from another.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a grade
        entry will result in a ``PermissionDenied``. This is intended as
        a hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``GradeEntry`` override is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_form_for_override(self, grade_entry_id, grade_entry_record_types):
        """Gets the grade entry form for overriding calculated grade entries.
        A new form should be requested for each create transaction.

        :param grade_entry_id: the ``Id`` of the grade entry to be overridden
        :type grade_entry_id: ``osid.id.Id``
        :param grade_entry_record_types: array of grade entry record types
        :type grade_entry_record_types: ``osid.type.Type[]``
        :return: the grade entry form
        :rtype: ``osid.grading.GradeEntryForm``
        :raise: ``AlreadyExists`` -- ``grade_entry_id`` is already overridden
        :raise: ``NotFound`` -- ``grade_entry_id`` not found or ``grade_entry_id`` is not a calculated entry
        :raise: ``NullArgument`` -- ``grade_entry_id`` or ``grade_entry_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def override_calculated_grade_entry(self, grade_entry_form):
        """Creates a new overriding ``GradeEntry``.

        :param grade_entry_form: the form for this ``GradeEntry``
        :type grade_entry_form: ``osid.grading.GradeEntryForm``
        :return: the new ``GradeEntry``
        :rtype: ``osid.grading.GradeEntry``
        :raise: ``IllegalState`` -- ``grade_entry_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``grade_entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_entry_form`` did not originate from ``get_grade_entry_form_for_override()``

        """
        raise UNIMPLEMENTED()

    def can_update_grade_entries(self):
        """Tests if this user can update grade entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``GradeEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if grade entry modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_grade_entry_form_for_update(self, grade_entry_id):
        """Gets the grade entry form for updating an existing entry.
        A new grade entry form should be requested for each update
        transaction.

        :param grade_entry_id: the ``Id`` of the ``GradeEntry``
        :type grade_entry_id: ``osid.id.Id``
        :return: the grade entry form
        :rtype: ``osid.grading.GradeEntryForm``
        :raise: ``NotFound`` -- ``grade_entry_id`` is not found
        :raise: ``NullArgument`` -- ``grade_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_grade_entry(self, grade_entry_form):
        """Updates an existing grade entry.

        :param grade_entry_form: the form containing the elements to be updated
        :type grade_entry_form: ``osid.grading.GradeEntryForm``
        :raise: ``IllegalState`` -- ``grade_entry_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``grade_entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_entry_form`` did not originate from ``get_grade_entry_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_grade_entries(self):
        """Tests if this user can delete grade entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``GradeEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``GradeEntry`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_grade_entry(self, grade_entry_id):
        """Deletes the ``GradeEntry`` identified by the given ``Id``.

        :param grade_entry_id: the ``Id`` of the ``GradeEntry`` to delete
        :type grade_entry_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``GradeEntry`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``grade_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_grade_entry_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``GradeEntries``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``GradeEntry`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_grade_entry(self, grade_entry_id, alias_id):
        """Adds an ``Id`` to a ``GradeEntry`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``GradeEntry`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another grade entry, it is
        reassigned to the given grade entry ``Id``.

        :param grade_entry_id: the ``Id`` of a ``GradeEntry``
        :type grade_entry_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``grade_entry_id`` not found
        :raise: ``NullArgument`` -- ``grade_entry_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.grading.GradeEntryNotificationSession

    def can_register_for_grade_entry_notifications(self):
        """Tests if this user can register for ``GradeEntry`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_grade_entries(self):
        """Register for notifications of new grade entries.
        ``GradeEntryReceiver.newGradeEntry()`` is invoked when a new
        grade entry is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_grade_entries_in_column(self, gradebook_column_id):
        """Registers for notification of a new grade entry for the specified gradebook column.
        ``GradeEntryReceiver.newGradeEntry()`` is invoked when a new
        entry for the resource is created.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn`` to monitor
        :type gradebook_column_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_column_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_grade_entries_for_resource(self, resource_id):
        """Registers for notification of a new grade entry for the specified resource.
        ``GradeEntryReceiver.newGradeEntry()`` is invoked when a new
        entry for the resource is created.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_grade_entries_by_grader(self, resource_id):
        """Registers for notification of a new grade entry for the specified grader agent.
        ``GradeEntryReceiver.newGradeEntry()`` is invoked when a new
        entry for the grader is created.

        :param resource_id: the ``Id`` of the ``Agent`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agent_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_grade_entries(self):
        """Registers for notification of updated grade entries.
        ``GradeEntryReceiver.changedGradeEntry()`` is invoked when a
        grade entry is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_grade_entries_in_column(self, gradebook_column_id):
        """Registers for notification of an updated grade entry for the specified gradebook column.
        ``GradeEntryReceiver.changedGradeEntry()`` is invoked when an
        entry for the column is updated.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn`` to monitor
        :type gradebook_column_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_column_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_grade_entries_for_resource(self, resource_id):
        """Registers for notification of an updated grade entry for the specified key resource.
        ``GradeEntryReceiver.changedGradeEntry()`` is invoked when an
        entry for the resource is updated.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_grade_entries_by_grader(self, resource_id):
        """Registers for notification of an updated grade entry for the specified grader.
        ``GradeEntryReceiver.changedGradeEntry()`` is invoked when an
        entry for the agent is updated.

        :param resource_id: the ``Id`` of the ``Agent`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agent_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_grade_entry(self, grade_entry_id):
        """Registers for notification of an updated grade entry.
        ``GradeEntryReceiver.changedGradeEntry()`` is invoked when the
        specified grade entry is changed.

        :param grade_entry_id: the ``Id`` of the ``GradeEntry`` to monitor
        :type grade_entry_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``grade_entry_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_grade_entries(self):
        """Registers for notification of deleted grade entries.
        ``GradeEntryReceiver.deletedGradeEntry()`` is invoked when a
        grade entry is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_grade_entries_in_column(self, gradebook_column_id):
        """Registers for notification of a deleted grade entry for the specified gradebook column.
        ``GradeEntryReceiver.changedGradeEntry()`` is invoked when an
        entry for the column is removed from this gradebook.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn`` to monitor
        :type gradebook_column_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_column_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_grade_entries_for_resource(self, resource_id):
        """Registers for notification of a deleted grade entry for the specified key resource.
        ``GradeEntryReceiver.changedGradeEntry()`` is invoked when an
        entry for the resource is removed from this gradebook.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_grade_entries_by_grader(self, resource_id):
        """Registers for notification of a deleted grade entry for the specified grader.
        ``GradeEntryReceiver.changedGradeEntry()`` is invoked when an
        entry for the agent is removed from this gradebook.

        :param resource_id: the ``Id`` of the ``Agent`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agent_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_grade_entry(self, grade_entry_id):
        """Registers for notification of a deleted grade entry.
        ``GradeEntryReceiver.deletedGradeEntry()`` is invoked when the
        specified entry is deleted.

        :param grade_entry_id: the ``Id`` of the ``GradeEntry`` to monitor
        :type grade_entry_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``grade_entry_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class GradebookList(osid_objects.OsidList):

    def get_next_gradebook(self):
        """Gets the next ``Gradebook`` in this list.

        :return: the next ``Gradebook`` in this list. The ``has_next()`` method should be used to test that a next ``Gradebook`` is available before calling this method.
        :rtype: ``osid.grading.Gradebook``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    next_gradebook = property(fget=get_next_gradebook)

    def get_next_gradebooks(self, n):
        """Gets the next set of ``Gradebook`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Gradebook`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Gradebook`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.grading.Gradebook``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()



class Gradebooks(GradingManager):
    pass


