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
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects
from ..osid import markers as osid_markers
from ..osid import records as osid_records
from ..osid import queries as osid_queries
from ..osid import searches as osid_searches


class GradingProfile(osid_managers.OsidProfile):
    """The ``GradingProfile`` describes the interoperability among grading services."""

    def __init__(self):
        self._provider_manager = None

    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_grade_system_lookup(self):
        """Tests if a grade system lookup service is supported.

        :return: true if grade system lookup is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_grade_system_query(self):
        """Tests if a grade system query service is supported.

        :return: ``true`` if grade system query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_grade_system_search(self):
        """Tests if a grade system search service is supported.

        :return: ``true`` if grade system search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_grade_system_admin(self):
        """Tests if a grade system administrative service is supported.

        :return: ``true`` if grade system admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_grade_system_notification(self):
        """Tests if grade system notification is supported.

        Messages may be sent when grade entries are created, modified,
        or deleted.

        :return: ``true`` if grade system notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_grade_system_gradebook(self):
        """Tests if a grade system to gradebook lookup session is available.

        :return: ``true`` if grade system gradebook lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_grade_system_gradebook_assignment(self):
        """Tests if a grade system to gradebook assignment session is available.

        :return: ``true`` if grade system gradebook assignment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_grade_system_smart_gradebook(self):
        """Tests if a grade system smart gradebook session is available.

        :return: ``true`` if grade system smart gradebook is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_grade_entry_lookup(self):
        """Tests if a grade entry lookup service is supported.

        :return: true if grade entry lookup is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_grade_entry_query(self):
        """Tests if a grade entry query service is supported.

        :return: true if grade entry query is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_grade_entry_search(self):
        """Tests if a grade entry search service is supported.

        :return: ``true`` if grade entry search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_grade_entry_admin(self):
        """Tests if a grade entry administrative service is supported.

        :return: ``true`` if grade entry admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_grade_entry_notification(self):
        """Tests if grade entry notification is supported.

        :return: ``true`` if grade entry notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_gradebook_column_lookup(self):
        """Tests if a gradebook column lookup service is supported.

        :return: true if gradebook column lookup is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_gradebook_column_query(self):
        """Tests if a gradebook column query service is supported.

        :return: ``true`` if grade system query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_gradebook_column_search(self):
        """Tests if a gradebook column search service is supported.

        :return: ``true`` if grade system search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_gradebook_column_admin(self):
        """Tests if a gradebook column administrative service is supported.

        :return: ``true`` if gradebook column admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_gradebook_column_notification(self):
        """Tests if gradebook column notification is supported.

        Messages may be sent when grade entries are created, modified,
        or deleted.

        :return: ``true`` if gradebook column notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_gradebook_column_gradebook(self):
        """Tests if a gradebook column to gradebook lookup session is available.

        :return: ``true`` if gradebook column gradebook lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_gradebook_column_gradebook_assignment(self):
        """Tests if a gradebook column to gradebook assignment session is available.

        :return: ``true`` if gradebook column gradebook assignment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_gradebook_column_smart_gradebook(self):
        """Tests if a gradebook column smart gradebookt session is available.

        :return: ``true`` if gradebook column amsrt gradebook is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_gradebook_lookup(self):
        """Tests if a gradebook lookup service is supported.

        :return: ``true`` if gradebook lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_gradebook_query(self):
        """Tests if a gradebook query service is supported.

        :return: ``true`` if gradebook query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_gradebook_search(self):
        """Tests if a gradebook search service is supported.

        :return: ``true`` if gradebook search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_gradebook_admin(self):
        """Tests if a gradebook administrative service is supported.

        :return: ``true`` if gradebook admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_gradebook_notification(self):
        """Tests if gradebook notification is supported.

        Messages may be sent when gradebooks are created, modified, or
        deleted.

        :return: ``true`` if gradebook notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_gradebook_hierarchy(self):
        """Tests if a gradebook hierarchy traversal is supported.

        :return: ``true`` if a gradebook hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_gradebook_hierarchy_design(self):
        """Tests if gradebook hierarchy design is supported.

        :return: ``true`` if a gradebook hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_grading_batch(self):
        """Tests if a grading batch service is supported.

        :return: ``true`` if a grading batch service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_grading_calculation(self):
        """Tests if a grading calculation service is supported.

        :return: ``true`` if a grading calculation service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_grading_transform(self):
        """Tests if a grade system transform service is supported.

        :return: ``true`` if a grading transform service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_grade_record_types(self):
        """Gets the supported ``Grade`` record types.

        :return: a list containing the supported ``Grade`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    grade_record_types = property(fget=get_grade_record_types)

    def supports_grade_record_type(self, grade_record_type):
        """Tests if the given ``Grade`` record type is supported.

        :param grade_record_type: a ``Type`` indicating a ``Grade`` record type
        :type grade_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_grade_system_record_types(self):
        """Gets the supported ``GradeSystem`` record types.

        :return: a list containing the supported ``GradeSystem`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    grade_system_record_types = property(fget=get_grade_system_record_types)

    def supports_grade_system_record_type(self, grade_system_record_type):
        """Tests if the given ``GradeSystem`` record type is supported.

        :param grade_system_record_type: a ``Type`` indicating a ``GradeSystem`` record type
        :type grade_system_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_grade_system_search_record_types(self):
        """Gets the supported ``GradeSystem`` search record types.

        :return: a list containing the supported ``GradeSystem`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    grade_system_search_record_types = property(fget=get_grade_system_search_record_types)

    def supports_grade_system_search_record_type(self, grade_system_search_record_type):
        """Tests if the given ``GradeSystem`` search record type is supported.

        :param grade_system_search_record_type: a ``Type`` indicating a ``GradeSystem`` search record type
        :type grade_system_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_grade_entry_record_types(self):
        """Gets the supported ``GradeEntry`` record types.

        :return: a list containing the supported ``GradeEntry`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    grade_entry_record_types = property(fget=get_grade_entry_record_types)

    def supports_grade_entry_record_type(self, grade_entry_record_type):
        """Tests if the given ``GradeEntry`` record type is supported.

        :param grade_entry_record_type: a ``Type`` indicating a ``GradeEntry`` record type
        :type grade_entry_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_entry_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_grade_entry_search_record_types(self):
        """Gets the supported ``GradeEntry`` search record types.

        :return: a list containing the supported ``GradeEntry`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    grade_entry_search_record_types = property(fget=get_grade_entry_search_record_types)

    def supports_grade_entry_search_record_type(self, grade_entry_search_record_type):
        """Tests if the given ``GradeEntry`` search record type is supported.

        :param grade_entry_search_record_type: a ``Type`` indicating a ``GradeEntry`` search record type
        :type grade_entry_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_entry_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_gradebook_column_record_types(self):
        """Gets the supported ``GradebookColumn`` record types.

        :return: a list containing the supported ``GradebookColumn`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    gradebook_column_record_types = property(fget=get_gradebook_column_record_types)

    def supports_gradebook_column_record_type(self, gradebook_column_record_type):
        """Tests if the given ``GradebookColumn`` record type is supported.

        :param gradebook_column_record_type: a ``Type`` indicating a ``GradebookColumn`` type
        :type gradebook_column_record_type: ``osid.type.Type``
        :return: ``true`` if the given gradebook column record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_gradebook_column_search_record_types(self):
        """Gets the supported gradebook column search record types.

        :return: a list containing the supported ``GradebookColumn`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    gradebook_column_search_record_types = property(fget=get_gradebook_column_search_record_types)

    def supports_gradebook_column_search_record_type(self, gradebook_column_search_record_type):
        """Tests if the given gradebook column search record type is supported.

        :param gradebook_column_search_record_type: a ``Type`` indicating a ``GradebookColumn`` search record type
        :type gradebook_column_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_gradebook_column_summary_record_types(self):
        """Gets the supported ``GradebookColumnSummary`` record types.

        :return: a list containing the supported ``GradebookColumnSummary`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    gradebook_column_summary_record_types = property(fget=get_gradebook_column_summary_record_types)

    def supports_gradebook_column_summary_record_type(self, gradebook_column_summary_record_type):
        """Tests if the given ``GradebookColumnSummary`` record type is supported.

        :param gradebook_column_summary_record_type: a ``Type`` indicating a ``GradebookColumnSummary`` type
        :type gradebook_column_summary_record_type: ``osid.type.Type``
        :return: ``true`` if the given gradebook column summary record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_gradebook_record_types(self):
        """Gets the supported ``Gradebook`` record types.

        :return: a list containing the supported ``Gradebook`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    gradebook_record_types = property(fget=get_gradebook_record_types)

    def supports_gradebook_record_type(self, gradebook_record_type):
        """Tests if the given ``Gradebook`` record type is supported.

        :param gradebook_record_type: a ``Type`` indicating a ``Gradebook`` type
        :type gradebook_record_type: ``osid.type.Type``
        :return: ``true`` if the given gradebook record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_gradebook_search_record_types(self):
        """Gets the supported gradebook search record types.

        :return: a list containing the supported ``Gradebook`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    gradebook_search_record_types = property(fget=get_gradebook_search_record_types)

    def supports_gradebook_search_record_type(self, gradebook_search_record_type):
        """Tests if the given gradebook search record type is supported.

        :param gradebook_search_record_type: a ``Type`` indicating a ``Gradebook`` search record type
        :type gradebook_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean
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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_gradebook_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_gradebook_view(self):
        """A complete view of the ``Gradebook`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_gradebook(self, gradebook_id):
        """Gets the ``Gradebook`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Gradebook`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Gradebook`` and retained
        for compatility.

        :param gradebook_id: ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: the gradebook
        :rtype: ``osid.grading.Gradebook``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.grading.Gradebook

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

    def get_gradebooks_by_genus_type(self, gradebook_genus_type):
        """Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` which does not include
        gradebooks of types derived from the specified ``Type``.

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

    def get_gradebooks_by_parent_genus_type(self, gradebook_genus_type):
        """Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` and include any additional
        gradebooks with genus types derived from the specified ``Type``.

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

    def get_gradebooks(self):
        """Gets all ``Gradebooks``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :return: a ``GradebookList``
        :rtype: ``osid.grading.GradebookList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

    gradebooks = property(fget=get_gradebooks)


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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Gradebook

    def can_update_gradebooks(self):
        """Tests if this user can update ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Gradebook`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_gradebooks(self):
        """Tests if this user can delete gradebooks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Gradebook`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_gradebook(self, gradebook_id):
        """Deletes a ``Gradebook``.

        :param gradebook_id: the ``Id`` of the ``Gradebook`` to remove
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_gradebook_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Gradebook`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




class GradingManager(osid_managers.OsidManager, osid_sessions.OsidSession, GradingProfile):
    """The grading manager provides access to grading sessions and provides interoperability tests for various aspects
        of this
        service.

    The sessions included in this manager are:

      * ``GradeSystemLookupSession:`` a session to look up grades and
        grade systems
      * ``GradeSystemQuerySession:`` a session to query grade systems
        ``None``
      * ``GradeSystemSearchSession:`` a session to search grade systems
      * ``GradeSystemAdminSession:`` a session to manage grade systems
      * ``GradeSystemNotificationSession`` a session for subscribing to
        new or deleted grades or grade systems
      * ``GradeSystemGradebookSession:`` a session for retrieving grade
        system to gradebook mappings
      * ``GradeSystemGradebookAssignmentSession:`` a session for
        managing grade system to gradebook mappings
      * ``GradeSystemSmartGradebookSession:`` a session for managing
        smart gradebooks of grade systems

      * ``GradeEntryLookupSession:`` a session to look up grade entries
      * ``GradeEntryQuerySession:`` a session to query grade entries
        ``None``
      * ``GradeEntrySearchSession:`` a session to search grade entries
      * ``GradeEntryAdminSession:`` a session to create, modify and
        delete grade entries ``None``
      * ``GradeEntryNotificationSession: a`` session to receive messages
        pertaining to grade entry ```` changes

      * ``GradebookColumnLookupSession:`` a session to look up gradebook
        columns
      * ``GradebookColumnQuerySession:`` a session to query gradebook
        columns ``None``
      * ``GradebookColumnSearchSession:`` a session to search gradebook
        columns
      * ``GradebookColumnAdminSession:`` a session to manage gradebook
        columns
      * ``GradebookColumnNotificationSession`` a session for subscribing
        to new or deleted gradebook columns
      * ``GradebookColumnGradebookSession:`` a session for retrieving
        gradebook column to gradebook mappings
      * ``GradebookColumnGradebookAssignmentSession:`` a session for
        managing gradebook column to gradebook mappings
      * ``GradebookColumnSmartGradebookSession:`` a session for managing
        smart gradebooks of gradebook columns

      * ``GradebookLookupSession:`` a session to lookup gradebooks
      * ``GradebookQuerySession:`` a session to query gradebooks
      * ``GradebookSearchSession`` : a session to search gradebooks
      * ``GradebookAdminSession`` : a session to create, modify and
        delete gradebooks
      * ``GradebookNotificationSession`` : a session to receive messages
        pertaining to gradebook changes
      * ``GradebookHierarchySession:`` a session to traverse the
        gradebook hierarchy
      * ``GradebookHierarchyDesignSession:`` a session to manage the
        gradebook hierarchy

    """

    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._gradebook_view = DEFAULT
        osid.OsidSession.__init__(self, proxy) # This is to initialize self._proxy

    # def _get_view(self, view):
    #     """Gets the currently set view"""
    #     if view in self._views:
    #         return self._views[view]
    #     else:
    #         self._views[view] = DEFAULT
    #         return DEFAULT

    def _set_gradebook_view(self, session):
        """Sets the underlying gradebook view to match current view"""
        if self._gradebook_view == COMPARATIVE:
            try:
                session.use_comparative_gradebook_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_gradebook_view()
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
            self._set_gradebook_view(session)
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
        parameter_id = Id('parameter:gradingProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('GRADING', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('GRADING', provider_impl)

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

    def get_grade_system_lookup_session(self):
        """Gets the ``OsidSession`` associated with the grade system lookup service.

        :return: a ``GradeSystemLookupSession``
        :rtype: ``osid.grading.GradeSystemLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_lookup()`` is ``true``.*

        """
        return # osid.grading.GradeSystemLookupSession

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
        :raise: ``Unimplemented`` -- ``supports_grade_system_lookup()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeSystemLookupSession

    def get_grade_system_query_session(self):
        """Gets the ``OsidSession`` associated with the grade system query service.

        :return: a ``GradeSystemQuerySession``
        :rtype: ``osid.grading.GradeSystemQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` is ``true``.*

        """
        return # osid.grading.GradeSystemQuerySession

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

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeSystemQuerySession

    def get_grade_system_search_session(self):
        """Gets the ``OsidSession`` associated with the grade system search service.

        :return: a ``GradeSystemSearchSession``
        :rtype: ``osid.grading.GradeSystemSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_search()`` is ``true``.*

        """
        return # osid.grading.GradeSystemSearchSession

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
        :raise: ``Unimplemented`` -- ``supports_grade_system_search()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeSystemSearchSession

    def get_grade_system_admin_session(self):
        """Gets the ``OsidSession`` associated with the grade system administration service.

        :return: a ``GradeSystemAdminSession``
        :rtype: ``osid.grading.GradeSystemAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_admin()`` is ``true``.*

        """
        return # osid.grading.GradeSystemAdminSession

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

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeSystemAdminSession

    def get_grade_system_notification_session(self, grade_system_receiver):
        """Gets the notification session for notifications pertaining to grade system changes.

        :param grade_system_receiver: the grade system receiver
        :type grade_system_receiver: ``osid.grading.GradeSystemReceiver``
        :return: a ``GradeSystemNotificationSession``
        :rtype: ``osid.grading.GradeSystemNotificationSession``
        :raise: ``NullArgument`` -- ``grade_system_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_notification()`` is ``true``.*

        """
        return # osid.grading.GradeSystemNotificationSession

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
        :raise: ``Unimplemented`` -- ``supports_grade_system_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeSystemNotificationSession

    def get_grade_system_gradebook_session(self):
        """Gets the session for retrieving grade system to gradebook mappings.

        :return: a ``GradeSystemGradebookSession``
        :rtype: ``osid.grading.GradeSystemGradebookSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_gradebook()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_gradebook()`` is ``true``.*

        """
        return # osid.grading.GradeSystemGradebookSession

    grade_system_gradebook_session = property(fget=get_grade_system_gradebook_session)

    def get_grade_system_gradebook_assignment_session(self):
        """Gets the session for assigning grade system to gradebook mappings.

        :return: a ``GradeSystemGradebookAssignmentSession``
        :rtype: ``osid.grading.GradeSystemGradebookSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_gradebook_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_gradebook_assignment()`` is ``true``.*

        """
        return # osid.grading.GradeSystemGradebookSession

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

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_smart_gradebook()`` is ``true``.*

        """
        return # osid.grading.GradeSystemSmartGradebookSession

    def get_grade_entry_lookup_session(self):
        """Gets the ``OsidSession`` associated with the grade entry lookup service.

        :return: a ``GradeEntryLookupSession``
        :rtype: ``osid.grading.GradeEntryLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_lookup()`` is ``true``.*

        """
        return # osid.grading.GradeEntryLookupSession

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

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeEntryLookupSession

    def get_grade_entry_query_session(self):
        """Gets the ``OsidSession`` associated with the grade entry query service.

        :return: a ``GradeEntryQuerySession``
        :rtype: ``osid.grading.GradeEntryQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` is ``true``.*

        """
        return # osid.grading.GradeEntryQuerySession

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

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeEntryQuerySession

    def get_grade_entry_search_session(self):
        """Gets the ``OsidSession`` associated with the grade entry search service.

        :return: a ``GradeEntrySearchSession``
        :rtype: ``osid.grading.GradeEntrySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_search()`` is ``true``.*

        """
        return # osid.grading.GradeEntrySearchSession

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

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeEntrySearchSession

    def get_grade_entry_admin_session(self):
        """Gets the ``OsidSession`` associated with the grade entry administration service.

        :return: a ``GradeEntryAdminSession``
        :rtype: ``osid.grading.GradeEntryAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_admin()`` is ``true``.*

        """
        return # osid.grading.GradeEntryAdminSession

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

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeEntryAdminSession

    def get_grade_entry_notification_session(self, receiver):
        """Gets the notification session for notifications pertaining to grade entry changes.

        :param receiver: the grade entry receiver
        :type receiver: ``osid.grading.GradeEntryReceiver``
        :return: a ``GradeEntryNotificationSession``
        :rtype: ``osid.grading.GradeEntryNotificationSession``
        :raise: ``NullArgument`` -- ``receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_notification()`` is ``true``.*

        """
        return # osid.grading.GradeEntryNotificationSession

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
        :raise: ``Unimplemented`` -- ``supports_grade_entry_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeEntryNotificationSession

    def get_gradebook_column_lookup_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column lookup service.

        :return: a ``GradebookColumnLookupSession``
        :rtype: ``osid.grading.GradebookColumnLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_lookup()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnLookupSession

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
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_lookup()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradebookColumnLookupSession

    def get_gradebook_column_query_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column query service.

        :return: a ``GradebookColumnQuerySession``
        :rtype: ``osid.grading.GradebookColumnQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnQuerySession

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
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradebookColumnQuerySession

    def get_gradebook_column_search_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column search service.

        :return: a ``GradebookColumnSearchSession``
        :rtype: ``osid.grading.GradebookColumnSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_search()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnSearchSession

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
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_search()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradebookColumnSearchSession

    def get_gradebook_column_admin_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column administration service.

        :return: a ``GradebookColumnAdminSession``
        :rtype: ``osid.grading.GradebookColumnAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_admin()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnAdminSession

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
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_admin()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradebookColumnAdminSession

    def get_gradebook_column_notification_session(self, gradebook_column_receiver):
        """Gets the notification session for notifications pertaining to gradebook column changes.

        :param gradebook_column_receiver: the grade system receiver
        :type gradebook_column_receiver: ``osid.grading.GradebookColumnReceiver``
        :return: a ``GradebookColumnNotificationSession``
        :rtype: ``osid.grading.GradebookColumnNotificationSession``
        :raise: ``NullArgument`` -- ``gradebook_column_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_notification()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnNotificationSession

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
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_notification()`` or ``supports_visible_federation()``
        is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradebookColumnNotificationSession

    def get_gradebook_column_gradebook_session(self):
        """Gets the session for retrieving gradebook column to gradebook mappings.

        :return: a ``GradebookColumnGradebookSession``
        :rtype: ``osid.grading.GradebookColumnGradebookSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_gradebook()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_gradebook()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnGradebookSession

    gradebook_column_gradebook_session = property(fget=get_gradebook_column_gradebook_session)

    def get_gradebook_column_gradebook_assignment_session(self):
        """Gets the session for assigning gradebook column to gradebook mappings.

        :return: a ``GradebookColumnGradebookAssignmentSession``
        :rtype: ``osid.grading.GradebookColumnGradebookAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_gradebook_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_gradebook_assignment()`` is
        ``true``.*

        """
        return # osid.grading.GradebookColumnGradebookAssignmentSession

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

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_smart_gradebook()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnSmartGradebookSession

    def get_gradebook_lookup_session(self):
        """Gets the OsidSession associated with the gradebook lookup service.

        :return: a ``GradebookLookupSession``
        :rtype: ``osid.grading.GradebookLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_lookup() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_lookup()`` is true.*

        """
        return # osid.grading.GradebookLookupSession

    gradebook_lookup_session = property(fget=get_gradebook_lookup_session)

    def get_gradebook_query_session(self):
        """Gets the OsidSession associated with the gradebook query service.

        :return: a ``GradebookQuerySession``
        :rtype: ``osid.grading.GradebookQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_query() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_query()`` is true.*

        """
        return # osid.grading.GradebookQuerySession

    gradebook_query_session = property(fget=get_gradebook_query_session)

    def get_gradebook_search_session(self):
        """Gets the OsidSession associated with the gradebook search service.

        :return: a ``GradebookSearchSession``
        :rtype: ``osid.grading.GradebookSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_search() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_search()`` is true.*

        """
        return # osid.grading.GradebookSearchSession

    gradebook_search_session = property(fget=get_gradebook_search_session)

    def get_gradebook_admin_session(self):
        """Gets the OsidSession associated with the gradebook administration service.

        :return: a ``GradebookAdminSession``
        :rtype: ``osid.grading.GradebookAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_admin() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_admin()`` is true.*

        """
        return # osid.grading.GradebookAdminSession

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

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_notification()`` is true.*

        """
        return # osid.grading.GradebookNotificationSession

    def get_gradebook_hierarchy_session(self):
        """Gets the session traversing gradebook hierarchies.

        :return: a ``GradebookHierarchySession``
        :rtype: ``osid.grading.GradebookHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_hierarchy() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_hierarchy()`` is true.*

        """
        return # osid.grading.GradebookHierarchySession

    gradebook_hierarchy_session = property(fget=get_gradebook_hierarchy_session)

    def get_gradebook_hierarchy_design_session(self):
        """Gets the session designing gradebook hierarchies.

        :return: a ``GradebookHierarchyDesignSession``
        :rtype: ``osid.grading.GradebookHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_hierarchy_design() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_hierarchy_design()`` is true.*

        """
        return # osid.grading.GradebookHierarchyDesignSession

    gradebook_hierarchy_design_session = property(fget=get_gradebook_hierarchy_design_session)

    def get_grading_batch_manager(self):
        """Gets the ``GradingBatchManager``.

        :return: a ``GradingBatchManager``
        :rtype: ``osid.grading.batch.GradingBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_batch() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_grading_batch()`` is true.*

        """
        return # osid.grading.batch.GradingBatchManager

    grading_batch_manager = property(fget=get_grading_batch_manager)

    def get_grading_calculation_manager(self):
        """Gets the ``GradingCalculationManager``.

        :return: a ``GradingCalculationManager``
        :rtype: ``osid.grading.calculation.GradingCalculationManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_calculation() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_grading_calculation()`` is true.*

        """
        return # osid.grading.calculation.GradingCalculationManager

    grading_calculation_manager = property(fget=get_grading_calculation_manager)

    def get_grading_transform_manager(self):
        """Gets the ``GradingTransformManager``.

        :return: a ``GradingTransformManager``
        :rtype: ``osid.grading.transform.GradingTransformManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_transform() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_grading_transform()`` is true.*

        """
        return # osid.grading.transform.GradingTransformManager

    grading_transform_manager = property(fget=get_grading_transform_manager)
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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_gradebook_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_gradebook_view(self):
        """A complete view of the ``Gradebook`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_gradebook(self, gradebook_id):
        """Gets the ``Gradebook`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Gradebook`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Gradebook`` and retained
        for compatility.

        :param gradebook_id: ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: the gradebook
        :rtype: ``osid.grading.Gradebook``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.grading.Gradebook

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

    def get_gradebooks_by_genus_type(self, gradebook_genus_type):
        """Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` which does not include
        gradebooks of types derived from the specified ``Type``.

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

    def get_gradebooks_by_parent_genus_type(self, gradebook_genus_type):
        """Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` and include any additional
        gradebooks with genus types derived from the specified ``Type``.

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

    def get_gradebooks(self):
        """Gets all ``Gradebooks``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :return: a ``GradebookList``
        :rtype: ``osid.grading.GradebookList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

    gradebooks = property(fget=get_gradebooks)


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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Gradebook

    def can_update_gradebooks(self):
        """Tests if this user can update ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Gradebook`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_gradebooks(self):
        """Tests if this user can delete gradebooks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Gradebook`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_gradebook(self, gradebook_id):
        """Deletes a ``Gradebook``.

        :param gradebook_id: the ``Id`` of the ``Gradebook`` to remove
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_gradebook_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Gradebook`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




class GradingProxyManager(osid_managers.OsidProxyManager, GradingProfile):
    """The grading manager provides access to grading sessions and provides interoperability tests for various aspects
        of this
        service.

    Methods in this manager accept a ``Proxy`` for passing information
    from server environments.The sessions included in this manager are:

      * ``GradeSystemLookupSession:`` a session to look up grades and
        grade systems
      * ``GradeSystemQuerySession:`` a session to query grade systems
        ``None``
      * ``GradeSystemSearchSession:`` a session to search grade systems
      * ``GradeSystemAdminSession:`` a session to manage grade systems
      * ``GradeSystemNotificationSession`` a session for subscribing to
        new or deleted grades or grade systems
      * ``GradeSystemGradebookSession:`` a session for retrieving grade
        system to gradebook mappings
      * ``GradeSystemGradebookAssignmentSession:`` a session for
        managing grade system to gradebook mappings
      * ``GradeSystemSmartGradebookSession:`` a session for managing
        smart gradebooks of grade systems

      * ``GradeEntryLookupSession:`` a session to look up grade entries
      * ``GradeEntryQuerySession:`` a session to query grade entries
        ``None``
      * ``GradeEntrySearchSession:`` a session to search grade entries
      * ``GradeEntryAdminSession:`` a session to create, modify and
        delete grade entries ``None``
      * ``GradeEntryNotificationSession: a`` session to receive messages
        pertaining to grade entry ```` changes

      * ``GradebookColumnLookupSession:`` a session to look up gradebook
        columns
      * ``GradebookColumnQuerySession:`` a session to query gradebook
        columns ``None``
      * ``GradebookColumnSearchSession:`` a session to search gradebook
        columns
      * ``GradebookColumnAdminSession:`` a session to manage gradebook
        columns
      * ``GradebookColumnDerivationSession:`` a session to manage
        derived gradebook columns
      * ``GradebookColumnNotificationSession`` a session for subscribing
        to new or deleted gradebook columns
      * ``GradebookColumnGradebookSession:`` a session for retrieving
        gradebook column to gradebook mappings
      * ``GradebookColumnGradebookAssignmentSession:`` a session for
        managing gradebook column to gradebook mappings
      * ``GradebookColumnSmartGradebookSession:`` a session for managing
        smart gradebooks of gradebook columns

      * ``GradebookLookupSession:`` a session to lookup gradebooks
      * ``GradebookQuerySession:`` a session to query gradebooks
      * ``GradebookSearchSession`` : a session to search gradebooks
      * ``GradebookAdminSession`` : a session to create, modify and
        delete gradebooks
      * ``GradebookNotificationSession`` : a session to receive messages
        pertaining to gradebook changes
      * ``GradebookHierarchySession:`` a session to traverse the
        gradebook hierarchy
      * ``GradebookHierarchyDesignSession:`` a session to manage the
        gradebook hierarchy

    """

    def get_grade_system_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade system lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemLookupSession``
        :rtype: ``osid.grading.GradeSystemLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_lookup()`` is ``true``.*

        """
        return # osid.grading.GradeSystemLookupSession

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
        :raise: ``Unimplemented`` -- ``supports_grade_system_lookup()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeSystemLookupSession

    def get_grade_system_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade system query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemQuerySession``
        :rtype: ``osid.grading.GradeSystemQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` is ``true``.*

        """
        return # osid.grading.GradeSystemQuerySession

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

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeSystemQuerySession

    def get_grade_system_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade system search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemSearchSession``
        :rtype: ``osid.grading.GradeSystemSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_search()`` is ``true``.*

        """
        return # osid.grading.GradeSystemSearchSession

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
        :raise: ``Unimplemented`` -- ``supports_grade_system_search()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeSystemSearchSession

    def get_grade_system_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade system administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemAdminSession``
        :rtype: ``osid.grading.GradeSystemAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_admin()`` is ``true``.*

        """
        return # osid.grading.GradeSystemAdminSession

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

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeSystemAdminSession

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

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_notification()`` is ``true``.*

        """
        return # osid.grading.GradeSystemNotificationSession

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
        :raise: ``Unimplemented`` -- ``supports_grade_system_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeSystemNotificationSession

    def get_grade_system_gradebook_session(self, proxy):
        """Gets the session for retrieving grade system to gradebook mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemGradebookSession``
        :rtype: ``osid.grading.GradeSystemGradebookSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_gradebook()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_gradebook()`` is ``true``.*

        """
        return # osid.grading.GradeSystemGradebookSession

    def get_grade_system_gradebook_assignment_session(self, proxy):
        """Gets the session for assigning grade system to gradebook mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeSystemGradebookAssignmentSession``
        :rtype: ``osid.grading.GradeSystemGradebookSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_system_gradebook_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_gradebook_assignment()`` is ``true``.*

        """
        return # osid.grading.GradeSystemGradebookSession

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

        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_smart_gradebook()`` is ``true``.*

        """
        return # osid.grading.GradeSystemSmartGradebookSession

    def get_grade_entry_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade entry lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeEntryLookupSession``
        :rtype: ``osid.grading.GradeEntryLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_lookup()`` is ``true``.*

        """
        return # osid.grading.GradeEntryLookupSession

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

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeEntryLookupSession

    def get_grade_entry_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade entry query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeEntryQuerySession``
        :rtype: ``osid.grading.GradeEntryQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` is ``true``.*

        """
        return # osid.grading.GradeEntryQuerySession

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

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeEntryQuerySession

    def get_grade_entry_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade entry search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeEntrySearchSession``
        :rtype: ``osid.grading.GradeEntrySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_search()`` is ``true``.*

        """
        return # osid.grading.GradeEntrySearchSession

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

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeEntrySearchSession

    def get_grade_entry_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the grade entry administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradeEntryAdminSession``
        :rtype: ``osid.grading.GradeEntryAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grade_entry_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_admin()`` is ``true``.*

        """
        return # osid.grading.GradeEntryAdminSession

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

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeEntryAdminSession

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

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_notification()`` is ``true``.*

        """
        return # osid.grading.GradeEntryNotificationSession

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
        :raise: ``Unimplemented`` -- ``supports_grade_entry_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeEntryNotificationSession

    def get_gradebook_column_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnLookupSession``
        :rtype: ``osid.grading.GradebookColumnLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_lookup()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnLookupSession

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
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_lookup()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradebookColumnLookupSession

    def get_gradebook_column_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnQuerySession``
        :rtype: ``osid.grading.GradebookColumnQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnQuerySession

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
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_query()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradebookColumnQuerySession

    def get_gradebook_column_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnSearchSession``
        :rtype: ``osid.grading.GradebookColumnSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_search()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnSearchSession

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
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_search()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradebookColumnSearchSession

    def get_gradebook_column_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the gradebook column administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnAdminSession``
        :rtype: ``osid.grading.GradebookColumnAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_admin()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnAdminSession

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
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_admin()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradebookColumnAdminSession

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

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_notification()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnNotificationSession

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
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_notification()`` or ``supports_visible_federation()``
        is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradebookColumnNotificationSession

    def get_gradebook_column_gradebook_session(self, proxy):
        """Gets the session for retrieving gradebook column to gradebook mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnGradebookSession``
        :rtype: ``osid.grading.GradebookColumnGradebookSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_gradebook()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_gradebook()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnGradebookSession

    def get_gradebook_column_gradebook_assignment_session(self, proxy):
        """Gets the session for assigning gradebook column to gradebook mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookColumnGradebookAssignmentSession``
        :rtype: ``osid.grading.GradebookColumnGradebookAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_column_gradebook_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_gradebook_assignment()`` is
        ``true``.*

        """
        return # osid.grading.GradebookColumnGradebookAssignmentSession

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

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_smart_gradebook()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnSmartGradebookSession

    def get_gradebook_lookup_session(self, proxy):
        """Gets the OsidSession associated with the gradebook lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookLookupSession``
        :rtype: ``osid.grading.GradebookLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_lookup() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_lookup()`` is true.*

        """
        return # osid.grading.GradebookLookupSession

    def get_gradebook_query_session(self, proxy):
        """Gets the OsidSession associated with the gradebook query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookQuerySession``
        :rtype: ``osid.grading.GradebookQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_query() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_query()`` is true.*

        """
        return # osid.grading.GradebookQuerySession

    def get_gradebook_search_session(self, proxy):
        """Gets the OsidSession associated with the gradebook search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookSearchSession``
        :rtype: ``osid.grading.GradebookSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_search() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_search()`` is true.*

        """
        return # osid.grading.GradebookSearchSession

    def get_gradebook_admin_session(self, proxy):
        """Gets the OsidSession associated with the gradebook administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookAdminSession``
        :rtype: ``osid.grading.GradebookAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_admin() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_admin()`` is true.*

        """
        return # osid.grading.GradebookAdminSession

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

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_notification()`` is true.*

        """
        return # osid.grading.GradebookNotificationSession

    def get_gradebook_hierarchy_session(self, proxy):
        """Gets the session traversing gradebook hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookHierarchySession``
        :rtype: ``osid.grading.GradebookHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_hierarchy() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_hierarchy()`` is true.*

        """
        return # osid.grading.GradebookHierarchySession

    def get_gradebook_hierarchy_design_session(self, proxy):
        """Gets the session designing gradebook hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``GradebookHierarchyDesignSession``
        :rtype: ``osid.grading.GradebookHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_gradebook_hierarchy_design() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_hierarchy_design()`` is true.*

        """
        return # osid.grading.GradebookHierarchyDesignSession

    def get_grading_batch_proxy_manager(self):
        """Gets the ``GradingBatchProxyManager``.

        :return: a ``GradingBatchProxyManager``
        :rtype: ``osid.grading.batch.GradingBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_batch() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_grading_batch()`` is true.*

        """
        return # osid.grading.batch.GradingBatchProxyManager

    grading_batch_proxy_manager = property(fget=get_grading_batch_proxy_manager)

    def get_grading_calculation_proxy_manager(self):
        """Gets the ``GradingCalculationProxyManager``.

        :return: a ``GradingCalculationProxyManager``
        :rtype: ``osid.grading.calculation.GradingCalculationProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_calculation() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_grading_calculation()`` is true.*

        """
        return # osid.grading.calculation.GradingCalculationProxyManager

    grading_calculation_proxy_manager = property(fget=get_grading_calculation_proxy_manager)

    def get_grading_transform_proxy_manager(self):
        """Gets the ``GradingTransformProxyManager``.

        :return: a ``GradingTransformManager``
        :rtype: ``osid.grading.transform.GradingTransformProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_grading_transform() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_grading_transform()`` is true.*

        """
        return # osid.grading.transform.GradingTransformProxyManager

    grading_transform_proxy_manager = property(fget=get_grading_transform_proxy_manager)
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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_gradebook_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_gradebook_view(self):
        """A complete view of the ``Gradebook`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_gradebook(self, gradebook_id):
        """Gets the ``Gradebook`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Gradebook`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Gradebook`` and retained
        for compatility.

        :param gradebook_id: ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: the gradebook
        :rtype: ``osid.grading.Gradebook``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.grading.Gradebook

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

    def get_gradebooks_by_genus_type(self, gradebook_genus_type):
        """Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` which does not include
        gradebooks of types derived from the specified ``Type``.

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

    def get_gradebooks_by_parent_genus_type(self, gradebook_genus_type):
        """Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` and include any additional
        gradebooks with genus types derived from the specified ``Type``.

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

    def get_gradebooks(self):
        """Gets all ``Gradebooks``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :return: a ``GradebookList``
        :rtype: ``osid.grading.GradebookList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookList

    gradebooks = property(fget=get_gradebooks)


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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Gradebook

    def can_update_gradebooks(self):
        """Tests if this user can update ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Gradebook`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_gradebooks(self):
        """Tests if this user can delete gradebooks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Gradebook`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_gradebook(self, gradebook_id):
        """Deletes a ``Gradebook``.

        :param gradebook_id: the ``Id`` of the ``Gradebook`` to remove
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_gradebook_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Gradebook`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




class Gradebook(osid_objects.OsidCatalog, osid_sessions.OsidSession):
    """A gradebook defines a collection of grade entries."""

    # WILL THIS EVER BE CALLED DIRECTLY - OUTSIDE OF A MANAGER?
    def __init__(self, provider_manager, catalog, proxy, **kwargs):
        self._provider_manager = provider_manager
        self._catalog = catalog
        osid.OsidObject.__init__(self, self._catalog) # This is to initialize self._object
        osid.OsidSession.__init__(self, proxy) # This is to initialize self._proxy
        self._catalog_id = catalog.get_id()
        self._provider_sessions = kwargs
        self._session_management = AUTOMATIC
        self._gradebook_view = DEFAULT
        self._object_views = dict()

    def _set_gradebook_view(self, session):
        """Sets the underlying gradebook view to match current view"""
        if self._gradebook_view == FEDERATED:
            try:
                session.use_federated_gradebook_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_gradebook_view()
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
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_gradebook')
            if self._proxy is None:
                session = session_class(self._catalog.get_id())
            else:
                session = session_class(self._catalog.get_id(), self._proxy)
            self._set_gradebook_view(session)
            self._set_object_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[session_name] = session
            return session

    def get_gradebook_id(self):
        """Gets the Id of this gradebook."""
        return self._catalog_id

    def get_gradebook(self):
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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.records.GradebookRecord
##
# The following methods are from osid.grading.GradeSystemLookupSession

    def get_gradebook_id(self):
        """Gets the ``GradeSystem``  ``Id`` associated with this session.

        :return: the ``GradeSystem Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Gradebook

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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_grade_system_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_grade_system_view(self):
        """A complete view of the ``GradeSystem`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include grade entries in gradebooks which
        are children of this gradebook in the gradebook hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this gradebook only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.grading.GradeSystem

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.grading.GradeSystem

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystemList

    def get_grade_systems_by_genus_type(self, grade_system_genus_type):
        """Gets a ``GradeSystemList`` corresponding to the given grade system genus ``Type`` which does not include
        systems of genus types derived from the specified ``Type``.

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystemList

    def get_grade_systems_by_parent_genus_type(self, grade_system_genus_type):
        """Gets a ``GradeSystemList`` corresponding to the given grade system genus ``Type`` and include any additional
        systems with genus types derived from the specified ``Type``.

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystemList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystemList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystemList

    grade_systems = property(fget=get_grade_systems)


##
# The following methods are from osid.grading.GradeSystemQuerySession

    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_search_grade_systems(self):
        """Tests if this user can perform ``GradeSystem`` searches.

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

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include grades in gradebooks which are
        children of this gradebook in the gradebook hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this gradebook only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_grade_system_query(self):
        """Gets a grade system query.

        :return: a grade system query
        :rtype: ``osid.grading.GradeSystemQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystemQuery

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystemList


##
# The following methods are from osid.grading.GradeSystemAdminSession

    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_create_grade_systems(self):
        """Tests if this user can create ``GradeSystems``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``GradeSystem`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystemForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystem

    def can_update_grade_systems(self):
        """Tests if this user can update ``GradeSystems``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``GradeSystem`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeSystemForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_grade_systems(self):
        """Tests if this user can delete grade systems.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``GradeSystem`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_grade_system(self, grade_system_id):
        """Deletes a ``GradeSystem``.

        :param grade_system_id: the ``Id`` of the ``GradeSystem`` to remove
        :type grade_system_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``grade_system_id`` not found
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_grade_system_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``GradeSystems``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``GradeSystem`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Grade

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_grade(self, grade_id):
        """Deletes a ``Grade``.

        :param grade_id: the ``Id`` of the ``Grade`` to remove
        :type grade_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``grade_id`` not found
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_grade_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Grades``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Grade`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.grading.GradeEntryLookupSession

    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_lookup_grade_entries(self):
        """Tests if this user can perform ``GradeEntry`` lookups.

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

    def use_comparative_grade_entry_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_grade_entry_view(self):
        """A complete view of the ``GradeEntry`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include grade entries in gradebooks which
        are children of this gradebook in the gradebook hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this gradebook only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_effective_grade_entry_view(self):
        """Only grade entries whose effective dates are current are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_any_effective_grade_entry_view(self):
        """All grade entries of any effective dates are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.grading.GradeEntry

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_by_genus_type(self, grade_entry_genus_type):
        """Gets a ``GradeEntryList`` corresponding to the given grade entry genus ``Type`` which does not include grade
        entries of genus types derived from the specified ``Type``.

        :param grade_entry_genus_type: a grade entry genus type
        :type grade_entry_genus_type: ``osid.type.Type``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``grade_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_by_parent_genus_type(self, grade_entry_genus_type):
        """Gets a ``GradeEntryList`` corresponding to the given grade entry genus ``Type`` and include any additional
        grade entry with genus types derived from the specified ``Type``.

        :param grade_entry_genus_type: a grade entry genus type
        :type grade_entry_genus_type: ``osid.type.Type``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``grade_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_by_record_type(self, grade_entry_record_type):
        """Gets a ``GradeEntryList`` containing the given grade entry record ``Type``.

        :param grade_entry_record_type: a grade entry record type
        :type grade_entry_record_type: ``osid.type.Type``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``grade_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_on_date(self, from_, to):
        """Gets a ``GradeEntryList`` effective during the entire given date range inclusive but not confined to the date
        range.

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_for_gradebook_column(self, gradebook_column_id):
        """Gets a ``GradeEntryList`` for the gradebook column.

        :param gradebook_column_id: a gradebook column ``Id``
        :type gradebook_column_id: ``osid.id.Id``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_for_gradebook_column_on_date(self, gradebook_column_id, from_, to):
        """Gets a ``GradeEntryList`` for the given gradebook column and effective during the entire given date range
        inclusive but not confined to the date range.

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_for_resource(self, resource_id):
        """Gets a ``GradeEntryList`` for the given key key resource.

        :param resource_id: a key resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_for_resource_on_date(self, resource_id, from_, to):
        """Gets a ``GradeEntryList`` for the given key resource and effective during the entire given date range
        inclusive but not confined to the date range.

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_for_gradebook_column_and_resource_on_date(self, gradebook_column_id, resource_id, from_, to):
        """Gets a ``GradeEntryList`` for the given gradebook column, resource, and effective during the entire given
        date range inclusive but not confined to the date range.

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_by_grader(self, resource_id):
        """Gets a ``GradeEntryList`` for the given grader.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries(self):
        """Gets all grade entries.

        :return: a ``GradeEntryList``
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryList

    grade_entries = property(fget=get_grade_entries)


##
# The following methods are from osid.grading.GradeEntryQuerySession

    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_search_grade_entries(self):
        """Tests if this user can perform ``GradeEntry`` searches.

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

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include grade entries in gradebooks which
        are children of this gradebook in the gradebook hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this gradebook only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_grade_entry_query(self):
        """Gets a grade entry query.

        :return: the grade entry query
        :rtype: ``osid.grading.GradeEntryQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryQuery

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryList


##
# The following methods are from osid.grading.GradeEntryAdminSession

    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_create_grade_entries(self):
        """Tests if this user can create grade entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a grade
        entry will result in a ``PermissionDenied``. This is intended as
        a hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``GradeEntry`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_create_grade_entry_with_record_types(self, grade_entry_record_types):
        """Tests if this user can create a single ``GradeEntry`` using the desired record types.

        While ``GradingManager.getGradeEntryRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``GradeEntry``.
        Providing an empty array tests if a ``GradeEntry`` can be
        created with no records.

        :param grade_entry_record_types: array of grade entry record types
        :type grade_entry_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``GradeEntry`` creation using the specified record ``Types`` is supported, ``false``
        otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_entry_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntry

    def can_overridecalculated_grade_entries(self):
        """Tests if this user can override grade entries calculated from another.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a grade
        entry will result in a ``PermissionDenied``. This is intended as
        a hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``GradeEntry`` override is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntry

    def can_update_grade_entries(self):
        """Tests if this user can update grade entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``GradeEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if grade entry modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradeEntryForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_grade_entries(self):
        """Tests if this user can delete grade entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``GradeEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``GradeEntry`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_grade_entry(self, grade_entry_id):
        """Deletes the ``GradeEntry`` identified by the given ``Id``.

        :param grade_entry_id: the ``Id`` of the ``GradeEntry`` to delete
        :type grade_entry_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``GradeEntry`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``grade_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_grade_entry_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``GradeEntries``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``GradeEntry`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.grading.GradebookColumnLookupSession

    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Gradebook

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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_gradebook_column_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_gradebook_column_view(self):
        """A complete view of the ``GradebookColumn`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include gradebook columns in gradebooks
        which are children of this gradebook in the gradebook hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this gradebook only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.grading.GradebookColumn

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookColumnList

    def get_gradebook_columns_by_genus_type(self, gradebook_column_genus_type):
        """Gets a ``GradebookColumnList`` corresponding to the given gradebook column genus ``Type`` which does not
        include gradebook columns of genus types derived from the specified ``Type``.

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookColumnList

    def get_gradebook_columns_by_parent_genus_type(self, gradebook_column_genus_type):
        """Gets a ``GradebookColumnList`` corresponding to the given gradebook column genus ``Type`` and include any
        additional columns with genus types derived from the specified ``Type``.

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookColumnList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookColumnList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookColumnList

    gradebook_columns = property(fget=get_gradebook_columns)

    def supports_summary(self):
        """Tests if a summary entry is available.

        :return: ``true`` if a summary entry is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.grading.GradebookColumnSummary


##
# The following methods are from osid.grading.GradebookColumnQuerySession

    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_search_gradebook_columns(self):
        """Tests if this user can perform ``GradebookColumn`` searches.

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

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include gradebook columns in gradebooks
        which are children of this gradebook in the gradebook hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this gradebook only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_gradebook_column_query(self):
        """Gets a gradebook column query.

        :return: the gradebook column
        :rtype: ``osid.grading.GradebookColumnQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookColumnQuery

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookColumnList


##
# The following methods are from osid.grading.GradebookColumnAdminSession

    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_create_gradebook_columns(self):
        """Tests if this user can create gradebook columns.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a gradebook
        column will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``GradebookColumn`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_create_gradebook_column_with_record_types(self, gradebook_column_record_types):
        """Tests if this user can create a single ``GradebookColumn`` using the desired record types.

        While ``GradingManager.getGradebookColumnRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``GradebookColumn``. Providing an empty array tests if a
        ``GradebookColumn`` can be created with no records.

        :param gradebook_column_record_types: array of gradebook column record types
        :type gradebook_column_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``GradebookColumn`` creation using the specified record ``Types`` is supported, ``false``
        otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookColumnForm

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
        :raise: ``Unsupported`` -- ``gradebook_column_form`` did not originate from
        ``get_gradebook_column_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookColumn

    def can_update_gradebook_columns(self):
        """Tests if this user can update gradebook columns.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``GradebookColumn`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: ``false`` if gradebook column modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.GradebookColumnForm

    def update_gradebook_column(self, gradebook_column_form):
        """Updates an existing gradebook column.

        :param gradebook_column_form: the form containing the elements to be updated
        :type gradebook_column_form: ``osid.grading.GradebookColumnForm``
        :raise: ``IllegalState`` -- ``gradebook_column_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``gradebook_column_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``gradebook_column_form`` did not originate from
        ``get_gradebook_column_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def sequence_gradebook_columns(self, gradebook_column_ids):
        """Resequences the gradebook columns.

        :param gradebook_column_ids: the ``Ids`` of the ``GradebookColumns``
        :type gradebook_column_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_column_id_list`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_gradebook_columns(self):
        """Tests if this user can delete gradebook columns.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``GradebookColumn`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer delete operations to an unauthorized user.

        :return: ``false`` if ``GradebookColumn`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_gradebook_column(self, gradebook_column_id):
        """Deletes the ``GradebookColumn`` identified by the given ``Id``.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn`` to delete
        :type gradebook_column_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``GradebookColumn`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_gradebook_column_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``GradebookColumns``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``GradebookColumn`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




class GradebookList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``GradebookList`` provides a means for accessing ``Gradebook`` elements sequentially
        either one
        at a time or many at a time.

    Examples: while (gl.hasNext()) { Gradebook gradebook =
    gl.getNextGradebook(); }

    or
      while (gl.hasNext()) {
           Gradebook[] gradebooks = gl.getNextGradebooks(gl.available());
      }


    """

    def get_next_gradebook(self):
        """Gets the next ``Gradebook`` in this list.

        :return: the next ``Gradebook`` in this list. The ``has_next()`` method should be used to test that a next
        ``Gradebook`` is available before calling this method.
        :rtype: ``osid.grading.Gradebook``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Gradebook

    next_gradebook = property(fget=get_next_gradebook)

    def get_next_gradebooks(self, n):
        """Gets the next set of ``Gradebook`` elements in this list which must be less than or equal to the return from
        ``available()``.

        :param n: the number of ``Gradebook`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Gradebook`` elements.The length of the array is less than or equal to the number
        specified.
        :rtype: ``osid.grading.Gradebook``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.grading.Gradebook


