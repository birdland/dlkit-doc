
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class GradingProfile(osid_managers.OsidProfile):
    """The ``GradingProfile`` describes the interoperability among grading services."""

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

    def supports_grade_system_admin(self):
        """Tests if a grade system administrative service is supported.

        :return: ``true`` if grade system admin is supported, ``false`` otherwise
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

    def supports_grade_entry_admin(self):
        """Tests if a grade entry administrative service is supported.

        :return: ``true`` if grade entry admin is supported, ``false`` otherwise
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

    def supports_gradebook_column_admin(self):
        """Tests if a gradebook column administrative service is supported.

        :return: ``true`` if gradebook column admin is supported, ``false`` otherwise
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

    def supports_gradebook_admin(self):
        """Tests if a gradebook administrative service is supported.

        :return: ``true`` if gradebook admin is supported, ``false`` otherwise
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

    def get_grade_system_record_types(self):
        """Gets the supported ``GradeSystem`` record types.

        :return: a list containing the supported ``GradeSystem`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    grade_system_record_types = property(fget=get_grade_system_record_types)

    def get_grade_system_search_record_types(self):
        """Gets the supported ``GradeSystem`` search record types.

        :return: a list containing the supported ``GradeSystem`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    grade_system_search_record_types = property(fget=get_grade_system_search_record_types)

    def get_grade_entry_record_types(self):
        """Gets the supported ``GradeEntry`` record types.

        :return: a list containing the supported ``GradeEntry`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    grade_entry_record_types = property(fget=get_grade_entry_record_types)

    def get_grade_entry_search_record_types(self):
        """Gets the supported ``GradeEntry`` search record types.

        :return: a list containing the supported ``GradeEntry`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    grade_entry_search_record_types = property(fget=get_grade_entry_search_record_types)

    def get_gradebook_column_record_types(self):
        """Gets the supported ``GradebookColumn`` record types.

        :return: a list containing the supported ``GradebookColumn`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    gradebook_column_record_types = property(fget=get_gradebook_column_record_types)

    def get_gradebook_column_search_record_types(self):
        """Gets the supported gradebook column search record types.

        :return: a list containing the supported ``GradebookColumn`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    gradebook_column_search_record_types = property(fget=get_gradebook_column_search_record_types)

    def get_gradebook_column_summary_record_types(self):
        """Gets the supported ``GradebookColumnSummary`` record types.

        :return: a list containing the supported ``GradebookColumnSummary`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    gradebook_column_summary_record_types = property(fget=get_gradebook_column_summary_record_types)

    def get_gradebook_record_types(self):
        """Gets the supported ``Gradebook`` record types.

        :return: a list containing the supported ``Gradebook`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    gradebook_record_types = property(fget=get_gradebook_record_types)

    def get_gradebook_search_record_types(self):
        """Gets the supported gradebook search record types.

        :return: a list containing the supported ``Gradebook`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    gradebook_search_record_types = property(fget=get_gradebook_search_record_types)


class GradingManager(osid_managers.OsidManager, osid_sessions.OsidSession, GradingProfile):
    """The grading manager provides access to grading sessions and provides interoperability tests for various aspects of this service.

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


class GradingProxyManager(osid_managers.OsidProxyManager, GradingProfile):
    """The grading manager provides access to grading sessions and provides interoperability tests for various aspects of this service.

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


