
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class GradingProfile(osid_managers.OsidProfile):
    """The ``GradingProfile`` describes the interoperability among grading services."""
    



    def supports_visible_federation(self):
        """Tests if federation is visible.

        return: (boolean) - ``true`` if visible federation is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_grade_system_lookup(self):
        """Tests if a grade system lookup service is supported.

        return: (boolean) - true if grade system lookup is supported,
                false otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_grade_system_query(self):
        """Tests if a grade system query service is supported.

        return: (boolean) - ``true`` if grade system query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_grade_system_search(self):
        """Tests if a grade system search service is supported.

        return: (boolean) - ``true`` if grade system search is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_grade_system_admin(self):
        """Tests if a grade system administrative service is supported.

        return: (boolean) - ``true`` if grade system admin is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_grade_system_notification(self):
        """Tests if grade system notification is supported.

        Messages may be sent when grade entries are created, modified,
        or deleted.

        return: (boolean) - ``true`` if grade system notification is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_grade_system_gradebook(self):
        """Tests if a grade system to gradebook lookup session is available.

        return: (boolean) - ``true`` if grade system gradebook lookup
                session is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_grade_system_gradebook_assignment(self):
        """Tests if a grade system to gradebook assignment session is available.

        return: (boolean) - ``true`` if grade system gradebook
                assignment is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_grade_system_smart_gradebook(self):
        """Tests if a grade system smart gradebook session is available.

        return: (boolean) - ``true`` if grade system smart gradebook is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_grade_entry_lookup(self):
        """Tests if a grade entry lookup service is supported.

        return: (boolean) - true if grade entry lookup is supported,
                false otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_grade_entry_query(self):
        """Tests if a grade entry query service is supported.

        return: (boolean) - true if grade entry query is supported,
                false otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_grade_entry_search(self):
        """Tests if a grade entry search service is supported.

        return: (boolean) - ``true`` if grade entry search is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_grade_entry_admin(self):
        """Tests if a grade entry administrative service is supported.

        return: (boolean) - ``true`` if grade entry admin is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_grade_entry_notification(self):
        """Tests if grade entry notification is supported.

        return: (boolean) - ``true`` if grade entry notification is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_gradebook_column_lookup(self):
        """Tests if a gradebook column lookup service is supported.

        return: (boolean) - true if gradebook column lookup is
                supported, false otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_gradebook_column_query(self):
        """Tests if a gradebook column query service is supported.

        return: (boolean) - ``true`` if grade system query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_gradebook_column_search(self):
        """Tests if a gradebook column search service is supported.

        return: (boolean) - ``true`` if grade system search is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_gradebook_column_admin(self):
        """Tests if a gradebook column administrative service is supported.

        return: (boolean) - ``true`` if gradebook column admin is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_gradebook_column_notification(self):
        """Tests if gradebook column notification is supported.

        Messages may be sent when grade entries are created, modified,
        or deleted.

        return: (boolean) - ``true`` if gradebook column notification is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_gradebook_column_gradebook(self):
        """Tests if a gradebook column to gradebook lookup session is available.

        return: (boolean) - ``true`` if gradebook column gradebook
                lookup session is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_gradebook_column_gradebook_assignment(self):
        """Tests if a gradebook column to gradebook assignment session is available.

        return: (boolean) - ``true`` if gradebook column gradebook
                assignment is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_gradebook_column_smart_gradebook(self):
        """Tests if a gradebook column smart gradebookt session is available.

        return: (boolean) - ``true`` if gradebook column amsrt gradebook
                is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_gradebook_lookup(self):
        """Tests if a gradebook lookup service is supported.

        return: (boolean) - ``true`` if gradebook lookup is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_gradebook_query(self):
        """Tests if a gradebook query service is supported.

        return: (boolean) - ``true`` if gradebook query is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_gradebook_search(self):
        """Tests if a gradebook search service is supported.

        return: (boolean) - ``true`` if gradebook search is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_gradebook_admin(self):
        """Tests if a gradebook administrative service is supported.

        return: (boolean) - ``true`` if gradebook admin is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_gradebook_notification(self):
        """Tests if gradebook notification is supported.

        Messages may be sent when gradebooks are created, modified, or
        deleted.

        return: (boolean) - ``true`` if gradebook notification is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_gradebook_hierarchy(self):
        """Tests if a gradebook hierarchy traversal is supported.

        return: (boolean) - ``true`` if a gradebook hierarchy traversal
                is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_gradebook_hierarchy_design(self):
        """Tests if gradebook hierarchy design is supported.

        return: (boolean) - ``true`` if a gradebook hierarchy design is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_grading_batch(self):
        """Tests if a grading batch service is supported.

        return: (boolean) - ``true`` if a grading batch service is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_grading_calculation(self):
        """Tests if a grading calculation service is supported.

        return: (boolean) - ``true`` if a grading calculation service is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_grading_transform(self):
        """Tests if a grade system transform service is supported.

        return: (boolean) - ``true`` if a grading transform service is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grade_record_types(self):
        """Gets the supported ``Grade`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Grade`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    grade_record_types = property(fget=get_grade_record_types)


    def supports_grade_record_type(self, grade_record_type):
        """Tests if the given ``Grade`` record type is supported.

        arg:    grade_record_type (osid.type.Type): a ``Type``
                indicating a ``Grade`` record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``grade_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grade_system_record_types(self):
        """Gets the supported ``GradeSystem`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``GradeSystem`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    grade_system_record_types = property(fget=get_grade_system_record_types)


    def supports_grade_system_record_type(self, grade_system_record_type):
        """Tests if the given ``GradeSystem`` record type is supported.

        arg:    grade_system_record_type (osid.type.Type): a ``Type``
                indicating a ``GradeSystem`` record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``grade_system_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grade_system_search_record_types(self):
        """Gets the supported ``GradeSystem`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``GradeSystem`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    grade_system_search_record_types = property(fget=get_grade_system_search_record_types)


    def supports_grade_system_search_record_type(self, grade_system_search_record_type):
        """Tests if the given ``GradeSystem`` search record type is supported.

        arg:    grade_system_search_record_type (osid.type.Type): a
                ``Type`` indicating a ``GradeSystem`` search record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``grade_system_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grade_entry_record_types(self):
        """Gets the supported ``GradeEntry`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``GradeEntry`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    grade_entry_record_types = property(fget=get_grade_entry_record_types)


    def supports_grade_entry_record_type(self, grade_entry_record_type):
        """Tests if the given ``GradeEntry`` record type is supported.

        arg:    grade_entry_record_type (osid.type.Type): a ``Type``
                indicating a ``GradeEntry`` record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``grade_entry_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_grade_entry_search_record_types(self):
        """Gets the supported ``GradeEntry`` search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``GradeEntry`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    grade_entry_search_record_types = property(fget=get_grade_entry_search_record_types)


    def supports_grade_entry_search_record_type(self, grade_entry_search_record_type):
        """Tests if the given ``GradeEntry`` search record type is supported.

        arg:    grade_entry_search_record_type (osid.type.Type): a
                ``Type`` indicating a ``GradeEntry`` search record type
        return: (boolean) - ``true`` if the given Type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``grade_entry_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_gradebook_column_record_types(self):
        """Gets the supported ``GradebookColumn`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``GradebookColumn`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    gradebook_column_record_types = property(fget=get_gradebook_column_record_types)


    def supports_gradebook_column_record_type(self, gradebook_column_record_type):
        """Tests if the given ``GradebookColumn`` record type is supported.

        arg:    gradebook_column_record_type (osid.type.Type): a
                ``Type`` indicating a ``GradebookColumn`` type
        return: (boolean) - ``true`` if the given gradebook column
                record ``Type`` is supported, ``false`` otherwise
        raise:  NullArgument - ``gradebook_column_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_gradebook_column_search_record_types(self):
        """Gets the supported gradebook column search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``GradebookColumn`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    gradebook_column_search_record_types = property(fget=get_gradebook_column_search_record_types)


    def supports_gradebook_column_search_record_type(self, gradebook_column_search_record_type):
        """Tests if the given gradebook column search record type is supported.

        arg:    gradebook_column_search_record_type (osid.type.Type): a
                ``Type`` indicating a ``GradebookColumn`` search record
                type
        return: (boolean) - ``true`` if the given search record ``Type``
                is supported, ``false`` otherwise
        raise:  NullArgument - ``gradebook_column_search_record_type``
                is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_gradebook_column_summary_record_types(self):
        """Gets the supported ``GradebookColumnSummary`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``GradebookColumnSummary`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    gradebook_column_summary_record_types = property(fget=get_gradebook_column_summary_record_types)


    def supports_gradebook_column_summary_record_type(self, gradebook_column_summary_record_type):
        """Tests if the given ``GradebookColumnSummary`` record type is supported.

        arg:    gradebook_column_summary_record_type (osid.type.Type): a
                ``Type`` indicating a ``GradebookColumnSummary`` type
        return: (boolean) - ``true`` if the given gradebook column
                summary record ``Type`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``gradebook_column_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_gradebook_record_types(self):
        """Gets the supported ``Gradebook`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Gradebook`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    gradebook_record_types = property(fget=get_gradebook_record_types)


    def supports_gradebook_record_type(self, gradebook_record_type):
        """Tests if the given ``Gradebook`` record type is supported.

        arg:    gradebook_record_type (osid.type.Type): a ``Type``
                indicating a ``Gradebook`` type
        return: (boolean) - ``true`` if the given gradebook record
                ``Type`` is supported, ``false`` otherwise
        raise:  NullArgument - ``gradebook_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_gradebook_search_record_types(self):
        """Gets the supported gradebook search record types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Gradebook`` search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    gradebook_search_record_types = property(fget=get_gradebook_search_record_types)


    def supports_gradebook_search_record_type(self, gradebook_search_record_type):
        """Tests if the given gradebook search record type is supported.

        arg:    gradebook_search_record_type (osid.type.Type): a
                ``Type`` indicating a ``Gradebook`` search record type
        return: (boolean) - ``true`` if the given search record ``Type``
                is supported, ``false`` otherwise
        raise:  NullArgument - ``gradebook_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


class GradingManager(osid_managers.OsidManager, osid_sessions.OsidSession, GradingProfile):
    """The grading manager provides access to grading sessions and provides interoperability tests for various aspects of this
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
    



    def get_grade_system_lookup_session(self):
        """Gets the ``OsidSession`` associated with the grade system lookup service.

        return: (osid.grading.GradeSystemLookupSession) - a
                ``GradeSystemLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_system_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_lookup()`` is ``true``.*

        """
        return # osid.grading.GradeSystemLookupSession

    grade_system_lookup_session = property(fget=get_grade_system_lookup_session)


    def get_grade_system_lookup_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system lookup service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradeSystemLookupSession) - ``a
                GradeSystemLookupSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_system_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeSystemLookupSession


    def get_grade_system_query_session(self):
        """Gets the ``OsidSession`` associated with the grade system query service.

        return: (osid.grading.GradeSystemQuerySession) - a
                ``GradeSystemQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_system_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` is ``true``.*

        """
        return # osid.grading.GradeSystemQuerySession

    grade_system_query_session = property(fget=get_grade_system_query_session)


    def get_grade_system_query_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system query service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradeSystemQuerySession) - ``a
                GradeSystemQuerySession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_system_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeSystemQuerySession


    def get_grade_system_search_session(self):
        """Gets the ``OsidSession`` associated with the grade system search service.

        return: (osid.grading.GradeSystemSearchSession) - a
                ``GradeSystemSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_system_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_search()`` is ``true``.*

        """
        return # osid.grading.GradeSystemSearchSession

    grade_system_search_session = property(fget=get_grade_system_search_session)


    def get_grade_system_search_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system search service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradeSystemSearchSession) - ``a
                GradeSystemSearchSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_system_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeSystemSearchSession


    def get_grade_system_admin_session(self):
        """Gets the ``OsidSession`` associated with the grade system administration service.

        return: (osid.grading.GradeSystemAdminSession) - a
                ``GradeSystemAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_system_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_admin()`` is ``true``.*

        """
        return # osid.grading.GradeSystemAdminSession

    grade_system_admin_session = property(fget=get_grade_system_admin_session)


    def get_grade_system_admin_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system admin service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradeSystemAdminSession) - ``a
                GradeSystemAdminSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_system_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeSystemAdminSession


    def get_grade_system_notification_session(self, grade_system_receiver):
        """Gets the notification session for notifications pertaining to grade system changes.

        arg:    grade_system_receiver
                (osid.grading.GradeSystemReceiver): the grade system
                receiver
        return: (osid.grading.GradeSystemNotificationSession) - a
                ``GradeSystemNotificationSession``
        raise:  NullArgument - ``grade_system_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_system_notification()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_notification()`` is ``true``.*

        """
        return # osid.grading.GradeSystemNotificationSession


    def get_grade_system_notification_session_for_gradebook(self, grade_system_receiver, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade system notification service for the given gradebook.

        arg:    grade_system_receiver
                (osid.grading.GradeSystemReceiver): the grade system
                receiver
        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradeSystemNotificationSession) - ``a
                _grade_system_notification_session``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``grade_system_receiver`` or
                ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_system_notification()``
                or ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeSystemNotificationSession


    def get_grade_system_gradebook_session(self):
        """Gets the session for retrieving grade system to gradebook mappings.

        return: (osid.grading.GradeSystemGradebookSession) - a
                ``GradeSystemGradebookSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_system_gradebook()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_gradebook()`` is ``true``.*

        """
        return # osid.grading.GradeSystemGradebookSession

    grade_system_gradebook_session = property(fget=get_grade_system_gradebook_session)


    def get_grade_system_gradebook_assignment_session(self):
        """Gets the session for assigning grade system to gradebook mappings.

        return: (osid.grading.GradeSystemGradebookSession) - a
                ``GradeSystemGradebookAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_grade_system_gradebook_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_gradebook_assignment()`` is ``true``.*

        """
        return # osid.grading.GradeSystemGradebookSession

    grade_system_gradebook_assignment_session = property(fget=get_grade_system_gradebook_assignment_session)


    def get_grade_system_smart_gradebook_session(self, gradebook_id):
        """Gets the session for managing smart gradebooks of grade systems.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradeSystemSmartGradebookSession) - a
                ``GradeSystemSmartGradebookSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_grade_system_smart_gradebook()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_system_smart_gradebook()`` is ``true``.*

        """
        return # osid.grading.GradeSystemSmartGradebookSession


    def get_grade_entry_lookup_session(self):
        """Gets the ``OsidSession`` associated with the grade entry lookup service.

        return: (osid.grading.GradeEntryLookupSession) - a
                ``GradeEntryLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_entry_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_lookup()`` is ``true``.*

        """
        return # osid.grading.GradeEntryLookupSession

    grade_entry_lookup_session = property(fget=get_grade_entry_lookup_session)


    def get_grade_entry_lookup_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry lookup service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradeEntryLookupSession) - ``a
                GradeEntryLookupSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_entry_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeEntryLookupSession


    def get_grade_entry_query_session(self):
        """Gets the ``OsidSession`` associated with the grade entry query service.

        return: (osid.grading.GradeEntryQuerySession) - a
                ``GradeEntryQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_entry_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` is ``true``.*

        """
        return # osid.grading.GradeEntryQuerySession

    grade_entry_query_session = property(fget=get_grade_entry_query_session)


    def get_grade_entry_query_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry query service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradeEntryQuerySession) - ``a
                GradeEntryQuerySession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_entry_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeEntryQuerySession


    def get_grade_entry_search_session(self):
        """Gets the ``OsidSession`` associated with the grade entry search service.

        return: (osid.grading.GradeEntrySearchSession) - a
                ``GradeEntrySearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_entry_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_search()`` is ``true``.*

        """
        return # osid.grading.GradeEntrySearchSession

    grade_entry_search_session = property(fget=get_grade_entry_search_session)


    def get_grade_entry_search_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry search service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradeEntrySearchSession) - ``a
                GradeEntrySearchSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_entry_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeEntrySearchSession


    def get_grade_entry_admin_session(self):
        """Gets the ``OsidSession`` associated with the grade entry administration service.

        return: (osid.grading.GradeEntryAdminSession) - a
                ``GradeEntryAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_entry_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_admin()`` is ``true``.*

        """
        return # osid.grading.GradeEntryAdminSession

    grade_entry_admin_session = property(fget=get_grade_entry_admin_session)


    def get_grade_entry_admin_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry admin service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradeEntryAdminSession) - ``a
                GradeEntryAdminSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_entry_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeEntryAdminSession


    def get_grade_entry_notification_session(self, receiver):
        """Gets the notification session for notifications pertaining to grade entry changes.

        arg:    receiver (osid.grading.GradeEntryReceiver): the grade
                entry receiver
        return: (osid.grading.GradeEntryNotificationSession) - a
                ``GradeEntryNotificationSession``
        raise:  NullArgument - ``receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grade_entry_notification()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_notification()`` is ``true``.*

        """
        return # osid.grading.GradeEntryNotificationSession


    def get_grade_entry_notification_session_for_gradebook(self, receiver, gradebook_id):
        """Gets the ``OsidSession`` associated with the grade entry notification service for the given gradebook.

        arg:    receiver (osid.grading.GradeEntryReceiver): the grade
                entry receiver
        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradeEntryNotificationSession) - ``a
                _grade_entry_notification_session``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``receiver`` or ``gradebook_id`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_grade_entry_notification()``
                or ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_grade_entry_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradeEntryNotificationSession


    def get_gradebook_column_lookup_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column lookup service.

        return: (osid.grading.GradebookColumnLookupSession) - a
                ``GradebookColumnLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_column_lookup()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_lookup()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnLookupSession

    gradebook_column_lookup_session = property(fget=get_gradebook_column_lookup_session)


    def get_gradebook_column_lookup_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column lookup service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradebookColumnLookupSession) - ``a
                _gradebook_column_lookup_session``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_gradebook_column_lookup()``
                or ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradebookColumnLookupSession


    def get_gradebook_column_query_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column query service.

        return: (osid.grading.GradebookColumnQuerySession) - a
                ``GradebookColumnQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_column_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnQuerySession

    gradebook_column_query_session = property(fget=get_gradebook_column_query_session)


    def get_gradebook_column_query_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column query service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradebookColumnQuerySession) - ``a
                GradebookColumnQuerySession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_gradebook_column_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradebookColumnQuerySession


    def get_gradebook_column_search_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column search service.

        return: (osid.grading.GradebookColumnSearchSession) - a
                ``GradebookColumnSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_column_search()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_search()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnSearchSession

    gradebook_column_search_session = property(fget=get_gradebook_column_search_session)


    def get_gradebook_column_search_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column search service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradebookColumnSearchSession) - ``a
                _gradebook_column_search_session``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_gradebook_column_search()``
                or ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradebookColumnSearchSession


    def get_gradebook_column_admin_session(self):
        """Gets the ``OsidSession`` associated with the gradebook column administration service.

        return: (osid.grading.GradebookColumnAdminSession) - a
                ``GradebookColumnAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_column_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_admin()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnAdminSession

    gradebook_column_admin_session = property(fget=get_gradebook_column_admin_session)


    def get_gradebook_column_admin_session_for_gradebook(self, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column admin service for the given gradebook.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradebookColumnAdminSession) - ``a
                GradebookColumnAdminSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_gradebook_column_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradebookColumnAdminSession


    def get_gradebook_column_notification_session(self, gradebook_column_receiver):
        """Gets the notification session for notifications pertaining to gradebook column changes.

        arg:    gradebook_column_receiver
                (osid.grading.GradebookColumnReceiver): the grade system
                receiver
        return: (osid.grading.GradebookColumnNotificationSession) - a
                ``GradebookColumnNotificationSession``
        raise:  NullArgument - ``gradebook_column_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_gradebook_column_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_notification()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnNotificationSession


    def get_gradebook_column_notification_session_for_gradebook(self, gradebook_column_receiver, gradebook_id):
        """Gets the ``OsidSession`` associated with the gradebook column notification service for the given gradebook.

        arg:    gradebook_column_receiver
                (osid.grading.GradebookColumnReceiver): the gradebook
                column receiver
        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradebookColumnNotificationSession) - ``a
                _gradebook_column_notification_session``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_column_receiver`` or
                ``gradebook_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented -
                ``supports_gradebook_column_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_notification()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.grading.GradebookColumnNotificationSession


    def get_gradebook_column_gradebook_session(self):
        """Gets the session for retrieving gradebook column to gradebook mappings.

        return: (osid.grading.GradebookColumnGradebookSession) - a
                ``GradebookColumnGradebookSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_gradebook_column_gradebook()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_gradebook()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnGradebookSession

    gradebook_column_gradebook_session = property(fget=get_gradebook_column_gradebook_session)


    def get_gradebook_column_gradebook_assignment_session(self):
        """Gets the session for assigning gradebook column to gradebook mappings.

        return: (osid.grading.GradebookColumnGradebookAssignmentSession)
                - a ``GradebookColumnGradebookAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_gradebook_column_gradebook_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_gradebook_assignment()`` is
        ``true``.*

        """
        return # osid.grading.GradebookColumnGradebookAssignmentSession

    gradebook_column_gradebook_assignment_session = property(fget=get_gradebook_column_gradebook_assignment_session)


    def get_gradebook_column_smart_gradebook_session(self, gradebook_id):
        """Gets the session for managing smart gradebooks of gradebook columns.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the gradebook
        return: (osid.grading.GradebookColumnSmartGradebookSession) - a
                ``GradebookColumnSmartGradebookSession``
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_gradebook_column_smart_gradebook()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_column_smart_gradebook()`` is ``true``.*

        """
        return # osid.grading.GradebookColumnSmartGradebookSession


    def get_gradebook_lookup_session(self):
        """Gets the OsidSession associated with the gradebook lookup service.

        return: (osid.grading.GradebookLookupSession) - a
                ``GradebookLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_lookup() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_lookup()`` is true.*

        """
        return # osid.grading.GradebookLookupSession

    gradebook_lookup_session = property(fget=get_gradebook_lookup_session)


    def get_gradebook_query_session(self):
        """Gets the OsidSession associated with the gradebook query service.

        return: (osid.grading.GradebookQuerySession) - a
                ``GradebookQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_query() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_query()`` is true.*

        """
        return # osid.grading.GradebookQuerySession

    gradebook_query_session = property(fget=get_gradebook_query_session)


    def get_gradebook_search_session(self):
        """Gets the OsidSession associated with the gradebook search service.

        return: (osid.grading.GradebookSearchSession) - a
                ``GradebookSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_search() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_search()`` is true.*

        """
        return # osid.grading.GradebookSearchSession

    gradebook_search_session = property(fget=get_gradebook_search_session)


    def get_gradebook_admin_session(self):
        """Gets the OsidSession associated with the gradebook administration service.

        return: (osid.grading.GradebookAdminSession) - a
                ``GradebookAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_admin() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_admin()`` is true.*

        """
        return # osid.grading.GradebookAdminSession

    gradebook_admin_session = property(fget=get_gradebook_admin_session)


    def get_gradebook_notification_session(self, gradebook_receiver):
        """Gets the notification session for notifications pertaining to gradebook service changes.

        arg:    gradebook_receiver (osid.grading.GradebookReceiver): the
                gradebook receiver
        return: (osid.grading.GradebookNotificationSession) - a
                ``GradebookNotificationSession``
        raise:  NullArgument - ``gradebook_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_notification() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_notification()`` is true.*

        """
        return # osid.grading.GradebookNotificationSession


    def get_gradebook_hierarchy_session(self):
        """Gets the session traversing gradebook hierarchies.

        return: (osid.grading.GradebookHierarchySession) - a
                ``GradebookHierarchySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_hierarchy() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_hierarchy()`` is true.*

        """
        return # osid.grading.GradebookHierarchySession

    gradebook_hierarchy_session = property(fget=get_gradebook_hierarchy_session)


    def get_gradebook_hierarchy_design_session(self):
        """Gets the session designing gradebook hierarchies.

        return: (osid.grading.GradebookHierarchyDesignSession) - a
                ``GradebookHierarchyDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_gradebook_hierarchy_design()
                is false``
        *compliance: optional -- This method must be implemented if
        ``supports_gradebook_hierarchy_design()`` is true.*

        """
        return # osid.grading.GradebookHierarchyDesignSession

    gradebook_hierarchy_design_session = property(fget=get_gradebook_hierarchy_design_session)


    def get_grading_batch_manager(self):
        """Gets the ``GradingBatchManager``.

        return: (osid.grading.batch.GradingBatchManager) - a
                ``GradingBatchManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grading_batch() is false``
        *compliance: optional -- This method must be implemented if
        ``supports_grading_batch()`` is true.*

        """
        return # osid.grading.batch.GradingBatchManager

    grading_batch_manager = property(fget=get_grading_batch_manager)


    def get_grading_calculation_manager(self):
        """Gets the ``GradingCalculationManager``.

        return: (osid.grading.calculation.GradingCalculationManager) - a
                ``GradingCalculationManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grading_calculation() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_grading_calculation()`` is true.*

        """
        return # osid.grading.calculation.GradingCalculationManager

    grading_calculation_manager = property(fget=get_grading_calculation_manager)


    def get_grading_transform_manager(self):
        """Gets the ``GradingTransformManager``.

        return: (osid.grading.transform.GradingTransformManager) - a
                ``GradingTransformManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_grading_transform() is
                false``
        *compliance: optional -- This method must be implemented if
        ``supports_grading_transform()`` is true.*

        """
        return # osid.grading.transform.GradingTransformManager

    grading_transform_manager = property(fget=get_grading_transform_manager)


