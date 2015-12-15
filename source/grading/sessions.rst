

Sessions
========


Grade System Lookup Session
---------------------------

.. py:class:: GradeSystemLookupSession(abc_grading_sessions.GradeSystemLookupSession, osid_sessions.OsidSession)
    The session defines methods for retrieving ``Grades`` and ``GradeSystems``.


    A Grade represents a qualified ranking defined in some grade system.




    Two views are defined in this session:




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition
      * federated gradebook view: lookups include grade systems from
        this gradebook and other gradebooks which are children of this
        gradebook in the gradebook hierarchy
      * isolated gradebook view: lookups include only those grade
        systems defined in this gradebook








    Grades and grade systems may have an additional records indicated by
    their respective record types. The record may not be accessed
    through a cast of the object.





    .. py:method:: get_gradebook_id():
        :noindex:


    .. py:attribute:: gradebook_id
        :noindex:


    .. py:method:: get_gradebook():
        :noindex:


    .. py:attribute:: gradebook
        :noindex:


    .. py:method:: can_lookup_grade_systems():
        :noindex:


    .. py:method:: use_comparative_grade_system_view():
        :noindex:


    .. py:method:: use_plenary_grade_system_view():
        :noindex:


    .. py:method:: use_federated_gradebook_view():
        :noindex:


    .. py:method:: use_isolated_gradebook_view():
        :noindex:


    .. py:method:: get_grade_system(grade_system_id):
        :noindex:


    .. py:method:: get_grade_system_by_grade(grade_id):
        :noindex:


    .. py:method:: get_grade_systems_by_ids(grade_system_ids):
        :noindex:


    .. py:method:: get_grade_systems_by_genus_type(grade_system_genus_type):
        :noindex:


    .. py:method:: get_grade_systems_by_parent_genus_type(grade_system_genus_type):
        :noindex:


    .. py:method:: get_grade_systems_by_record_type(grade_system_record_type):
        :noindex:


    .. py:method:: get_grade_systems():
        :noindex:


    .. py:attribute:: grade_systems
        :noindex:


Grade System Query Session
--------------------------

.. py:class:: GradeSystemQuerySession(abc_grading_sessions.GradeSystemQuerySession, osid_sessions.OsidSession)
    This session provides methods for searching among ``GradeSystems``.


    The search query is constructed using the ``GradeSystemQuery``.




    This session defines views that offer differing behaviors for
    searching.




      * federated gradebook view: searches include grade systems in
        gradebooks of which this gradebook is a ancestor in the
        gradebook hierarchy
      * isolated gradebook view: searches are restricted to grade
        systems in this gradebook








    Grade systems may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``GradeSystemQuery``.





    .. py:method:: get_gradebook_id():
        :noindex:


    .. py:attribute:: gradebook_id
        :noindex:


    .. py:method:: get_gradebook():
        :noindex:


    .. py:attribute:: gradebook
        :noindex:


    .. py:method:: can_search_grade_systems():
        :noindex:


    .. py:method:: use_federated_gradebook_view():
        :noindex:


    .. py:method:: use_isolated_gradebook_view():
        :noindex:


    .. py:method:: get_grade_system_query():
        :noindex:


    .. py:attribute:: grade_system_query
        :noindex:


    .. py:method:: get_grade_systems_by_query(grade_system_query):
        :noindex:


Grade System Admin Session
--------------------------

.. py:class:: GradeSystemAdminSession(abc_grading_sessions.GradeSystemAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``GradeSystems``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create a
    ``GradeSystem,`` a ``GradeSystemForm`` is requested using
    ``get_grade_system_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``GradeSystemForm`` will indicate that it is to be used with a
    create operation and can be used to examine metdata or validate data
    prior to creation. Once the ``GradeSystemForm`` is submiited to a
    create operation, it cannot be reused with another create operation
    unless the first operation was unsuccessful. Each
    ``GradeSystemForm`` corresponds to an attempted transaction.




    For updates, ``GradeSystemForms`` are requested to the
    ``GradeSystem``  ``Id`` that is to be updated using
    ``getGradeSystemFormForUpdate()``. Similarly, the
    ``GradeSystemForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``GradeSystemForm`` can only be used once for a successful update
    and cannot be reused.




    The delete operations delete ``GradeSystems`` To unmap a
    ``GradeSystem`` from the current ``Gradebook,`` the
    ``GradeSystemGradebookAssignmentSession`` should be used. These
    delete operations attempt to remove the ``GradeSystem`` itself thus
    removing it from all known ``Gradebook`` catalogs.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: get_gradebook_id():
        :noindex:


    .. py:attribute:: gradebook_id
        :noindex:


    .. py:method:: get_gradebook():
        :noindex:


    .. py:attribute:: gradebook
        :noindex:


    .. py:method:: can_create_grade_systems():
        :noindex:


    .. py:method:: can_create_grade_system_with_record_types(grade_system_record_types):
        :noindex:


    .. py:method:: get_grade_system_form_for_create(grade_system_record_types):
        :noindex:


    .. py:method:: create_grade_system(grade_system_form):
        :noindex:


    .. py:method:: can_update_grade_systems():
        :noindex:


    .. py:method:: get_grade_system_form_for_update(grade_system_id):
        :noindex:


    .. py:method:: update_grade_system(grade_system_form):
        :noindex:


    .. py:method:: can_delete_grade_systems():
        :noindex:


    .. py:method:: delete_grade_system(grade_system_id):
        :noindex:


    .. py:method:: can_manage_grade_system_aliases():
        :noindex:


    .. py:method:: alias_grade_system(grade_system_id, alias_id):
        :noindex:


    .. py:method:: can_create_grades(grade_system_id):
        :noindex:


    .. py:method:: can_create_grade_with_record_types(grade_system_id, grade_record_types):
        :noindex:


    .. py:method:: get_grade_form_for_create(grade_system_id, grade_record_types):
        :noindex:


    .. py:method:: create_grade(grade_form):
        :noindex:


    .. py:method:: can_update_grades(grade_system_id):
        :noindex:


    .. py:method:: get_grade_form_for_update(grade_id):
        :noindex:


    .. py:method:: update_grade(grade_form):
        :noindex:


    .. py:method:: can_delete_grades(grade_system_id):
        :noindex:


    .. py:method:: delete_grade(grade_id):
        :noindex:


    .. py:method:: can_manage_grade_aliases():
        :noindex:


    .. py:method:: alias_grade(grade_id, alias_id):
        :noindex:


Grade Entry Lookup Session
--------------------------

.. py:class:: GradeEntryLookupSession(abc_grading_sessions.GradeEntryLookupSession, osid_sessions.OsidSession)
    This session provides methods for retrieving ``GradeEntrie`` s.

    .. py:method:: get_gradebook_id():
        :noindex:


    .. py:attribute:: gradebook_id
        :noindex:


    .. py:method:: get_gradebook():
        :noindex:


    .. py:attribute:: gradebook
        :noindex:


    .. py:method:: can_lookup_grade_entries():
        :noindex:


    .. py:method:: use_comparative_grade_entry_view():
        :noindex:


    .. py:method:: use_plenary_grade_entry_view():
        :noindex:


    .. py:method:: use_federated_gradebook_view():
        :noindex:


    .. py:method:: use_isolated_gradebook_view():
        :noindex:


    .. py:method:: use_effective_grade_entry_view():
        :noindex:


    .. py:method:: use_any_effective_grade_entry_view():
        :noindex:


    .. py:method:: get_grade_entry(grade_entry_id):
        :noindex:


    .. py:method:: get_grade_entries_by_ids(grade_entry_ids):
        :noindex:


    .. py:method:: get_grade_entries_by_genus_type(grade_entry_genus_type):
        :noindex:


    .. py:method:: get_grade_entries_by_parent_genus_type(grade_entry_genus_type):
        :noindex:


    .. py:method:: get_grade_entries_by_record_type(grade_entry_record_type):
        :noindex:


    .. py:method:: get_grade_entries_on_date(from_, to):
        :noindex:


    .. py:method:: get_grade_entries_for_gradebook_column(gradebook_column_id):
        :noindex:


    .. py:method:: get_grade_entries_for_gradebook_column_on_date(gradebook_column_id, from_, to):
        :noindex:


    .. py:method:: get_grade_entries_for_resource(resource_id):
        :noindex:


    .. py:method:: get_grade_entries_for_resource_on_date(resource_id, from_, to):
        :noindex:


    .. py:method:: get_grade_entries_for_gradebook_column_and_resource(gradebook_column_id, resource_id):
        :noindex:


    .. py:method:: get_grade_entries_for_gradebook_column_and_resource_on_date(gradebook_column_id, resource_id, from_, to):
        :noindex:


    .. py:method:: get_grade_entries_by_grader(resource_id):
        :noindex:


    .. py:method:: get_grade_entries():
        :noindex:


    .. py:attribute:: grade_entries
        :noindex:


Grade Entry Query Session
-------------------------

.. py:class:: GradeEntryQuerySession(abc_grading_sessions.GradeEntryQuerySession, osid_sessions.OsidSession)
    This session provides methods for searching ``GradeEntry`` objects.


    The search query is constructed using the ``GradeEntryQuery``. The
    grade entry record ``Type`` also specifies the record interface for
    the grade entry query.




    This session defines views that offer differing behaviors for
    searching.




      * federated gradebook view: searches include grade entries in
        gradebooks of which this gradebook is a ancestor in the
        gradebook hierarchy
      * isolated gradebook view: searches are restricted to grade
        entries in this gradebook








    Grade entries may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``GradeEntryQuery``.





    .. py:method:: get_gradebook_id():
        :noindex:


    .. py:attribute:: gradebook_id
        :noindex:


    .. py:method:: get_gradebook():
        :noindex:


    .. py:attribute:: gradebook
        :noindex:


    .. py:method:: can_search_grade_entries():
        :noindex:


    .. py:method:: use_federated_gradebook_view():
        :noindex:


    .. py:method:: use_isolated_gradebook_view():
        :noindex:


    .. py:method:: get_grade_entry_query():
        :noindex:


    .. py:attribute:: grade_entry_query
        :noindex:


    .. py:method:: get_grade_entries_by_query(grade_entry_query):
        :noindex:


Grade Entry Admin Session
-------------------------

.. py:class:: GradeEntryAdminSession(abc_grading_sessions.GradeEntryAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``GradeEntries``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create a
    ``GradeEntry,`` a ``GradeEntryForm`` is requested using
    ``get_grade_entry_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``GradeEntryForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``GradeEntryForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``GradeEntryForm``
    corresponds to an attempted transaction.




    For updates, ``GradeEntryForms`` are requested to the ``GradeEntry``
    ``Id`` that is to be updated using ``getGradeEntryFormForUpdate()``.
    Similarly, the ``GradeEntryForm`` has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ``GradeEntryForm`` can only be used once for a
    successful update and cannot be reused.




    The delete operations delete ``GradeEntries``. To unmap a
    ``GradeEntry`` from the current ``Gradebook,`` the
    ``GradeEntryGradebookAssignmentSession`` should be used. These
    delete operations attempt to remove the ``GradeEntry`` itself thus
    removing it from all known ``Gradebook`` catalogs.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: get_gradebook_id():
        :noindex:


    .. py:attribute:: gradebook_id
        :noindex:


    .. py:method:: get_gradebook():
        :noindex:


    .. py:attribute:: gradebook
        :noindex:


    .. py:method:: can_create_grade_entries():
        :noindex:


    .. py:method:: can_create_grade_entry_with_record_types(grade_entry_record_types):
        :noindex:


    .. py:method:: get_grade_entry_form_for_create(gradebook_column_id, resource_id, grade_entry_record_types):
        :noindex:


    .. py:method:: create_grade_entry(grade_entry_form):
        :noindex:


    .. py:method:: can_overridecalculated_grade_entries():
        :noindex:


    .. py:method:: get_grade_entry_form_for_override(grade_entry_id, grade_entry_record_types):
        :noindex:


    .. py:method:: override_calculated_grade_entry(grade_entry_form):
        :noindex:


    .. py:method:: can_update_grade_entries():
        :noindex:


    .. py:method:: get_grade_entry_form_for_update(grade_entry_id):
        :noindex:


    .. py:method:: update_grade_entry(grade_entry_form):
        :noindex:


    .. py:method:: can_delete_grade_entries():
        :noindex:


    .. py:method:: delete_grade_entry(grade_entry_id):
        :noindex:


    .. py:method:: can_manage_grade_entry_aliases():
        :noindex:


    .. py:method:: alias_grade_entry(grade_entry_id, alias_id):
        :noindex:


Gradebook Column Lookup Session
-------------------------------

.. py:class:: GradebookColumnLookupSession(abc_grading_sessions.GradebookColumnLookupSession, osid_sessions.OsidSession)
    This session provides methods for retrieving ``GradebookColumns``.

    .. py:method:: get_gradebook_id():
        :noindex:


    .. py:attribute:: gradebook_id
        :noindex:


    .. py:method:: get_gradebook():
        :noindex:


    .. py:attribute:: gradebook
        :noindex:


    .. py:method:: can_lookup_gradebook_columns():
        :noindex:


    .. py:method:: use_comparative_gradebook_column_view():
        :noindex:


    .. py:method:: use_plenary_gradebook_column_view():
        :noindex:


    .. py:method:: use_federated_gradebook_view():
        :noindex:


    .. py:method:: use_isolated_gradebook_view():
        :noindex:


    .. py:method:: get_gradebook_column(gradebook_column_id):
        :noindex:


    .. py:method:: get_gradebook_columns_by_ids(gradebook_column_ids):
        :noindex:


    .. py:method:: get_gradebook_columns_by_genus_type(gradebook_column_genus_type):
        :noindex:


    .. py:method:: get_gradebook_columns_by_parent_genus_type(gradebook_column_genus_type):
        :noindex:


    .. py:method:: get_gradebook_columns_by_record_type(gradebook_column_record_type):
        :noindex:


    .. py:method:: get_gradebook_columns():
        :noindex:


    .. py:attribute:: gradebook_columns
        :noindex:


    .. py:method:: supports_summary():
        :noindex:


    .. py:method:: get_gradebook_column_summary(gradebook_column_id):
        :noindex:


Gradebook Column Query Session
------------------------------

.. py:class:: GradebookColumnQuerySession(abc_grading_sessions.GradebookColumnQuerySession, osid_sessions.OsidSession)
    This session provides methods for searching ``GradebookColumn`` objects.


    The search query is constructed using the ``GradebookColumnQuery``.




    This session defines views that offer differing behaviors for
    searching.




      * federated gradebook view: searches include columns in gradebooks
        of which this gradebook is a ancestor in the gradebook hierarchy
      * isolated gradebook view: searches are restricted to columns in
        this gradebook








    Gradebook columns may have a query record indicated by their
    respective record types. The query record is accessed via the
    ``GradebookColumnQuery``.





    .. py:method:: get_gradebook_id():
        :noindex:


    .. py:attribute:: gradebook_id
        :noindex:


    .. py:method:: get_gradebook():
        :noindex:


    .. py:attribute:: gradebook
        :noindex:


    .. py:method:: can_search_gradebook_columns():
        :noindex:


    .. py:method:: use_federated_gradebook_view():
        :noindex:


    .. py:method:: use_isolated_gradebook_view():
        :noindex:


    .. py:method:: get_gradebook_column_query():
        :noindex:


    .. py:attribute:: gradebook_column_query
        :noindex:


    .. py:method:: get_gradebook_columns_by_query(gradebook_column_query):
        :noindex:


Gradebook Column Admin Session
------------------------------

.. py:class:: GradebookColumnAdminSession(abc_grading_sessions.GradebookColumnAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``GradebookColumns``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create a
    ``GradebookColumn,`` a ``GradebookColumnForm`` is requested using
    ``get_gradebook_column_form_for_create()`` specifying the desired
    record ``Types`` or none if no record ``Types`` are needed. The
    returned ``GradebookColumnForm`` will indicate that it is to be used
    with a create operation and can be used to examine metdata or
    validate data prior to creation. Once the ``GradebookColumnForm`` is
    submiited to a create operation, it cannot be reused with another
    create operation unless the first operation was unsuccessful. Each
    ``GradebookColumnForm`` corresponds to an attempted transaction.




    For updates, ``GradebookColumnForms`` are requested to the
    ``GradebookColumn``  ``Id`` that is to be updated using
    ``getGradebookColumnFormForUpdate()``. Similarly, the
    ``GradebookColumnForm`` has metadata about the data that can be
    updated and it can perform validation before submitting the update.
    The ``GradebookColumnForm`` can only be used once for a successful
    update and cannot be reused.




    The delete operations delete ``GradebookColumns`` To unmap a
    ``GradebookColumn`` from the current ``Gradebook,`` the
    ``GradebookColumnGradebookAssignmentSession`` should be used. These
    delete operations attempt to remove the ``GradebookColumnForm``
    itself thus removing it from all known ``Gradebook`` catalogs.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: get_gradebook_id():
        :noindex:


    .. py:attribute:: gradebook_id
        :noindex:


    .. py:method:: get_gradebook():
        :noindex:


    .. py:attribute:: gradebook
        :noindex:


    .. py:method:: can_create_gradebook_columns():
        :noindex:


    .. py:method:: can_create_gradebook_column_with_record_types(gradebook_column_record_types):
        :noindex:


    .. py:method:: get_gradebook_column_form_for_create(gradebook_column_record_types):
        :noindex:


    .. py:method:: create_gradebook_column(gradebook_column_form):
        :noindex:


    .. py:method:: can_update_gradebook_columns():
        :noindex:


    .. py:method:: get_gradebook_column_form_for_update(gradebook_column_id):
        :noindex:


    .. py:method:: update_gradebook_column(gradebook_column_form):
        :noindex:


    .. py:method:: sequence_gradebook_columns(gradebook_column_ids):
        :noindex:


    .. py:method:: move_gradebook_column(front_gradebook_column_id, back_gradebook_column_id):
        :noindex:


    .. py:method:: copy_gradebook_column_entries(source_gradebook_column_id, target_gradebook_column_id):
        :noindex:


    .. py:method:: can_delete_gradebook_columns():
        :noindex:


    .. py:method:: delete_gradebook_column(gradebook_column_id):
        :noindex:


    .. py:method:: can_manage_gradebook_column_aliases():
        :noindex:


    .. py:method:: alias_gradebook_column(gradebook_column_id, alias_id):
        :noindex:


Gradebook Lookup Session
------------------------

.. py:class:: GradebookLookupSession(abc_grading_sessions.GradebookLookupSession, osid_sessions.OsidSession)
    This session provides methods for retrieving ``Gradebook`` objects.


    The ``Gradebook`` represents a collection of grade systems, entries,
    and gradebook columns.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition








    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Gradebooks`` it can access, without breaking
    execution. However, an administrative application may require all
    ``Gradebook`` elements to be available.




    Gradebooks may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Gradebook``.





    .. py:method:: can_lookup_gradebooks():
        :noindex:


    .. py:method:: use_comparative_gradebook_view():
        :noindex:


    .. py:method:: use_plenary_gradebook_view():
        :noindex:


    .. py:method:: get_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_gradebooks_by_ids(gradebook_ids):
        :noindex:


    .. py:method:: get_gradebooks_by_genus_type(gradebook_genus_type):
        :noindex:


    .. py:method:: get_gradebooks_by_parent_genus_type(gradebook_genus_type):
        :noindex:


    .. py:method:: get_gradebooks_by_record_type(gradebook_record_type):
        :noindex:


    .. py:method:: get_gradebooks_by_provider(resource_id):
        :noindex:


    .. py:method:: get_gradebooks():
        :noindex:


    .. py:attribute:: gradebooks
        :noindex:


Gradebook Admin Session
-----------------------

.. py:class:: GradebookAdminSession(abc_grading_sessions.GradebookAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``Gradebooks``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create a
    ``Gradebook,`` a ``GradebookForm`` is requested using
    ``get_gradebook_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``GradebookForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``GradebookForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``GradebookForm``
    corresponds to an attempted transaction.




    For updates, ``GradebookForms`` are requested to the ``Gradebook``
    ``Id`` that is to be updated using ``getGradebookFormForUpdate()``.
    Similarly, the ``GradebookForm`` has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ``GradebookForm`` can only be used once for a successful
    update and cannot be reused.




    The delete operations delete ``Gradebooks``.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: can_create_gradebooks():
        :noindex:


    .. py:method:: can_create_gradebook_with_record_types(gradebook_record_types):
        :noindex:


    .. py:method:: get_gradebook_form_for_create(gradebook_record_types):
        :noindex:


    .. py:method:: create_gradebook(gradebook_form):
        :noindex:


    .. py:method:: can_update_gradebooks():
        :noindex:


    .. py:method:: get_gradebook_form_for_update(gradebook_id):
        :noindex:


    .. py:method:: update_gradebook(gradebook_form):
        :noindex:


    .. py:method:: can_delete_gradebooks():
        :noindex:


    .. py:method:: delete_gradebook(gradebook_id):
        :noindex:


    .. py:method:: can_manage_gradebook_aliases():
        :noindex:


    .. py:method:: alias_gradebook(gradebook_id, alias_id):
        :noindex:


