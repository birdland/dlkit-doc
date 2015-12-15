

Sessions
========


Resource Lookup Session
-----------------------

.. py:class:: ResourceLookupSession(abc_resource_sessions.ResourceLookupSession, osid_sessions.OsidSession)
    This session defines methods for retrieving resources.


    A ``Resource`` is an arbitrary entity that may represent a person,
    place or thing used to identify an object used in various services.




    This lookup session defines several views:




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition
      * isolated bin view: All resource methods in this session operate,
        retrieve and pertain to resources defined explicitly in the
        current bin. Using an isolated view is useful for managing
        ``Resources`` with the ``ResourceAdminSession.``
      * federated bin view: All resource methods in this session
        operate, retrieve and pertain to all resources defined in this
        bin and any other resources implicitly available in this bin
        through bin inheritence.








    The methods ``use_federated_bin_view()`` and
    ``use_isolated_bin_view()`` behave as a radio group and one should
    be selected before invoking any lookup methods.




    Resources may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Resource``.





    .. py:method:: get_bin_id():
        :noindex:


    .. py:attribute:: bin_id
        :noindex:


    .. py:method:: get_bin():
        :noindex:


    .. py:attribute:: bin
        :noindex:


    .. py:method:: can_lookup_resources():
        :noindex:


    .. py:method:: use_comparative_resource_view():
        :noindex:


    .. py:method:: use_plenary_resource_view():
        :noindex:


    .. py:method:: use_federated_bin_view():
        :noindex:


    .. py:method:: use_isolated_bin_view():
        :noindex:


    .. py:method:: get_resource(resource_id):
        :noindex:


    .. py:method:: get_resources_by_ids(resource_ids):
        :noindex:


    .. py:method:: get_resources_by_genus_type(resource_genus_type):
        :noindex:


    .. py:method:: get_resources_by_parent_genus_type(resource_genus_type):
        :noindex:


    .. py:method:: get_resources_by_record_type(resource_record_type):
        :noindex:


    .. py:method:: get_resources():
        :noindex:


    .. py:attribute:: resources
        :noindex:


Resource Query Session
----------------------

.. py:class:: ResourceQuerySession(abc_resource_sessions.ResourceQuerySession, osid_sessions.OsidSession)
    This session provides methods for searching among ``Resource`` objects.


    The search query is constructed using the ``ResourceQuery``.




    This session defines views that offer differing behaviors for
    searching.




      * federated bin view: searches include resources in bins of which
        this bin is a ancestor in the bin hierarchy
      * isolated bin view: searches are restricted to resources in this
        bin








    Resources may have a resource record indicated by their respective
    record types. The resource query record is accessed via the
    ``ResourceQuery``.





    .. py:method:: get_bin_id():
        :noindex:


    .. py:attribute:: bin_id
        :noindex:


    .. py:method:: get_bin():
        :noindex:


    .. py:attribute:: bin
        :noindex:


    .. py:method:: can_search_resources():
        :noindex:


    .. py:method:: use_federated_bin_view():
        :noindex:


    .. py:method:: use_isolated_bin_view():
        :noindex:


    .. py:method:: get_resource_query():
        :noindex:


    .. py:attribute:: resource_query
        :noindex:


    .. py:method:: get_resources_by_query(resource_query):
        :noindex:


Resource Search Session
-----------------------

.. py:class:: ResourceSearchSession(abc_resource_sessions.ResourceSearchSession, ResourceQuerySession)
    This session provides methods for searching among ``Resource`` objects.


    The search query is constructed using the ``ResourceQuery``.




    ``get_resources_by_query()`` is the basic search method and returns
    a list of ``Resources``. A more advanced search may be performed
    with ``getResourcesBySearch()``. It accepts an ``ResourceSearch`` in
    addition to the query for the purpose of specifying additional
    options affecting the entire search, such as ordering.
    ``get_resources_by_search()`` returns an ``ResourceSearchResults``
    that can be used to access the resulting ``ResourceList`` or be used
    to perform a search within the result set through ``ResourceList``.




    This session defines views that offer differing behaviors for
    searching.




      * federated bin view: searches include resources in bins of which
        this bin is a ancestor in the bin hierarchy
      * isolated bin view: searches are restricted to resources in this
        bin








    Resources may have a resource query record indicated by their
    respective record types. The resource query record is accessed via
    the ``ResourceQuery``.





    .. py:method:: get_resource_search():
        :noindex:


    .. py:attribute:: resource_search
        :noindex:


    .. py:method:: get_resource_search_order():
        :noindex:


    .. py:attribute:: resource_search_order
        :noindex:


    .. py:method:: get_resources_by_search(resource_query, resource_search):
        :noindex:


    .. py:method:: get_resource_query_from_inspector(resource_query_inspector):
        :noindex:


Resource Admin Session
----------------------

.. py:class:: ResourceAdminSession(abc_resource_sessions.ResourceAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``Resources``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create a
    ``Resource,`` a ``ResourceForm`` is requested using
    ``get_resource_form_for_create()`` specifying desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``ResourceForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``ResourceForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``ResourceForm``
    corresponds to an attempted transaction.




    For updates, ``ResourceForms`` are requested to the ``Resource``
    ``Id`` that is to be updated using ``getResourceFormForUpdate()``.
    Similarly, the ``ResourceForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``ResourceForm`` can only be used once for a successful
    update and cannot be reused.




    The delete operations delete ``Resources``. To unmap a ``Resource``
    from the current ``Bin,`` the ``ResourceBinAssignmentSession``
    should be used. These delete operations attempt to remove the
    ``Resource`` itself thus removing it from all known ``Bin``
    catalogs.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: get_bin_id():
        :noindex:


    .. py:attribute:: bin_id
        :noindex:


    .. py:method:: get_bin():
        :noindex:


    .. py:attribute:: bin
        :noindex:


    .. py:method:: can_create_resources():
        :noindex:


    .. py:method:: can_create_resource_with_record_types(resource_record_types):
        :noindex:


    .. py:method:: get_resource_form_for_create(resource_record_types):
        :noindex:


    .. py:method:: create_resource(resource_form):
        :noindex:


    .. py:method:: can_update_resources():
        :noindex:


    .. py:method:: get_resource_form_for_update(resource_id):
        :noindex:


    .. py:method:: update_resource(resource_form):
        :noindex:


    .. py:method:: can_delete_resources():
        :noindex:


    .. py:method:: delete_resource(resource_id):
        :noindex:


    .. py:method:: can_manage_resource_aliases():
        :noindex:


    .. py:method:: alias_resource(resource_id, alias_id):
        :noindex:


Resource Notification Session
-----------------------------

.. py:class:: ResourceNotificationSession(abc_resource_sessions.ResourceNotificationSession, osid_sessions.OsidSession)
    This session defines methods to receive notifications on adds/changes to ``Resource`` objects in
    this ``Bin``.


    This also includes existing resources that may appear or disappear
    due to changes in the ``Bin`` hierarchy, This session is intended
    for consumers needing to synchronize their state with this service
    without the use of polling. Notifications are cancelled when this
    session is closed.




    The two views defined in this session correspond to the views in the
    ``ResourceLookupSession``.





    .. py:method:: get_bin_id():
        :noindex:


    .. py:attribute:: bin_id
        :noindex:


    .. py:method:: get_bin():
        :noindex:


    .. py:attribute:: bin
        :noindex:


    .. py:method:: can_register_for_resource_notifications():
        :noindex:


    .. py:method:: use_federated_bin_view():
        :noindex:


    .. py:method:: use_isolated_bin_view():
        :noindex:


    .. py:method:: register_for_new_resources():
        :noindex:


    .. py:method:: register_for_changed_resources():
        :noindex:


    .. py:method:: register_for_changed_resource(resource_id):
        :noindex:


    .. py:method:: register_for_deleted_resources():
        :noindex:


    .. py:method:: register_for_deleted_resource(resource_id):
        :noindex:


    .. py:method:: reliable_resource_notifications():
        :noindex:


    .. py:method:: unreliable_resource_notifications():
        :noindex:


    .. py:method:: acknowledge_resource_notification(notification_id):
        :noindex:


Resource Bin Session
--------------------

.. py:class:: ResourceBinSession(abc_resource_sessions.ResourceBinSession, osid_sessions.OsidSession)
    This session provides methods to retrieve ``Resource`` to ``Bin`` mappings.


    A ``Resource`` may appear in multiple ``Bins``. Each ``Bin`` may
    have its own authorizations governing who is allowed to look at it.




    This lookup session defines several views:




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition





    .. py:method:: use_comparative_bin_view():
        :noindex:


    .. py:method:: use_plenary_bin_view():
        :noindex:


    .. py:method:: can_lookup_resource_bin_mappings():
        :noindex:


    .. py:method:: get_resource_ids_by_bin(bin_id):
        :noindex:


    .. py:method:: get_resources_by_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_ids_by_bins(bin_ids):
        :noindex:


    .. py:method:: get_resources_by_bins(bin_ids):
        :noindex:


    .. py:method:: get_bin_ids_by_resource(resource_id):
        :noindex:


    .. py:method:: get_bins_by_resource(resource_id):
        :noindex:


Resource Bin Assignment Session
-------------------------------

.. py:class:: ResourceBinAssignmentSession(abc_resource_sessions.ResourceBinAssignmentSession, osid_sessions.OsidSession)
    This session provides methods to re-assign ``Resources`` to ``Bins``.


    A ``Resource`` may map to multiple ``Bin`` objects and removing the
    last reference to a ``Resource`` is the equivalent of deleting it.
    Each ``Bin`` may have its own authorizations governing who is
    allowed to operate on it.




    Moving or adding a reference of a ``Resource`` to another ``Bin`` is
    not a copy operation (eg: does not change its ``Id`` ).





    .. py:method:: can_assign_resources():
        :noindex:


    .. py:method:: can_assign_resources_to_bin(bin_id):
        :noindex:


    .. py:method:: get_assignable_bin_ids(bin_id):
        :noindex:


    .. py:method:: get_assignable_bin_ids_for_resource(bin_id, resource_id):
        :noindex:


    .. py:method:: assign_resource_to_bin(resource_id, bin_id):
        :noindex:


    .. py:method:: unassign_resource_from_bin(resource_id, bin_id):
        :noindex:


Resource Agent Session
----------------------

.. py:class:: ResourceAgentSession(abc_resource_sessions.ResourceAgentSession, osid_sessions.OsidSession)
    This session provides methods to retrieve ``Resource`` to ``Agent`` mappings.


    An ``Agent`` may map to only one ``Resource`` while a ``Resource``
    may map to multiple ``Agents``.




    This lookup session defines several views




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition





    .. py:method:: get_bin_id():
        :noindex:


    .. py:attribute:: bin_id
        :noindex:


    .. py:method:: get_bin():
        :noindex:


    .. py:attribute:: bin
        :noindex:


    .. py:method:: can_lookup_resource_agent_mappings():
        :noindex:


    .. py:method:: use_comparative_agent_view():
        :noindex:


    .. py:method:: use_plenary_agent_view():
        :noindex:


    .. py:method:: use_federated_bin_view():
        :noindex:


    .. py:method:: use_isolated_bin_view():
        :noindex:


    .. py:method:: get_resource_id_by_agent(agent_id):
        :noindex:


    .. py:method:: get_resource_by_agent(agent_id):
        :noindex:


    .. py:method:: get_agent_ids_by_resource(resource_id):
        :noindex:


    .. py:method:: get_agents_by_resource(resource_id):
        :noindex:


Resource Agent Assignment Session
---------------------------------

.. py:class:: ResourceAgentAssignmentSession(abc_resource_sessions.ResourceAgentAssignmentSession, osid_sessions.OsidSession)
    This session provides methods to re-assign ``Resource`` to ``Agents``.


    A ``Resource`` may be associated with multiple ``Agents``. An
    ``Agent`` may map to only one ``Resource``.





    .. py:method:: get_bin_id():
        :noindex:


    .. py:attribute:: bin_id
        :noindex:


    .. py:method:: get_bin():
        :noindex:


    .. py:attribute:: bin
        :noindex:


    .. py:method:: can_assign_agents():
        :noindex:


    .. py:method:: can_assign_agents_to_resource(resource_id):
        :noindex:


    .. py:method:: assign_agent_to_resource(agent_id, resource_id):
        :noindex:


    .. py:method:: unassign_agent_from_resource(agent_id, resource_id):
        :noindex:


Bin Lookup Session
------------------

.. py:class:: BinLookupSession(abc_resource_sessions.BinLookupSession, osid_sessions.OsidSession)
    This session provides methods for retrieving ``Bin`` objects.


    The ``Bin`` represents a collection resources.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition








    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Bins`` it can access, without breaking execution.
    However, an administrative application may require all ``Bin``
    elements to be available.




    Bins may have an additional records indicated by their respective
    record types. The record may not be accessed through a cast of the
    ``Bin``.





    .. py:method:: can_lookup_bins():
        :noindex:


    .. py:method:: use_comparative_bin_view():
        :noindex:


    .. py:method:: use_plenary_bin_view():
        :noindex:


    .. py:method:: get_bin(bin_id):
        :noindex:


    .. py:method:: get_bins_by_ids(bin_ids):
        :noindex:


    .. py:method:: get_bins_by_genus_type(bin_genus_type):
        :noindex:


    .. py:method:: get_bins_by_parent_genus_type(bin_genus_type):
        :noindex:


    .. py:method:: get_bins_by_record_type(bin_record_type):
        :noindex:


    .. py:method:: get_bins_by_provider(resource_id):
        :noindex:


    .. py:method:: get_bins():
        :noindex:


    .. py:attribute:: bins
        :noindex:


Bin Query Session
-----------------

.. py:class:: BinQuerySession(abc_resource_sessions.BinQuerySession, osid_sessions.OsidSession)
    This session provides methods for searching among ``Bin`` objects.


    The search query is constructed using the ``BinQuery``.




    Bins may have a bin query record indicated by their respective
    record types. The bin query record is accessed via the ``BinQuery``.





    .. py:method:: can_search_bins():
        :noindex:


    .. py:method:: get_bin_query():
        :noindex:


    .. py:attribute:: bin_query
        :noindex:


    .. py:method:: get_bins_by_query(bin_query):
        :noindex:


Bin Admin Session
-----------------

.. py:class:: BinAdminSession(abc_resource_sessions.BinAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``Bins``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create a
    ``Bin,`` a ``BinForm`` is requested using
    ``get_bin_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``BinForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``BinForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``BinForm`` corresponds
    to an attempted transaction.




    For updates, ``BinForms`` are requested to the ``Bin``  ``Id`` that
    is to be updated using ``getBinFormForUpdate()``. Similarly, the
    ``BinForm`` has metadata about the data that can be updated and it
    can perform validation before submitting the update. The ``BinForm``
    can only be used once for a successful update and cannot be reused.




    The delete operations delete ``Bins``.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: can_create_bins():
        :noindex:


    .. py:method:: can_create_bin_with_record_types(bin_record_types):
        :noindex:


    .. py:method:: get_bin_form_for_create(bin_record_types):
        :noindex:


    .. py:method:: create_bin(bin_form):
        :noindex:


    .. py:method:: can_update_bins():
        :noindex:


    .. py:method:: get_bin_form_for_update(bin_id):
        :noindex:


    .. py:method:: update_bin(bin_form):
        :noindex:


    .. py:method:: can_delete_bins():
        :noindex:


    .. py:method:: delete_bin(bin_id):
        :noindex:


    .. py:method:: can_manage_bin_aliases():
        :noindex:


    .. py:method:: alias_bin(bin_id, alias_id):
        :noindex:


Bin Hierarchy Session
---------------------

.. py:class:: BinHierarchySession(abc_resource_sessions.BinHierarchySession, osid_sessions.OsidSession)
    This session defines methods for traversing a hierarchy of ``Bin`` objects.


    Each node in the hierarchy is a unique ``Bin``. The hierarchy may be
    traversed recursively to establish the tree structure through
    ``get_parent_bins()`` and ``getChildBins()``. To relate these
    ``Ids`` to another OSID, ``get_bin_nodes()`` can be used for
    retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Bin`` available in the Resource OSID is known to this hierarchy
    but does not appear in the hierarchy traversal until added as a root
    node or a child of another node.




    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_bins()`` or ``get_child_bins()`` in lieu of
    a ``PermissionDenied`` error that may disrupt the traversal through
    authorized pathways.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: bin elements may be silently omitted or re-
        ordered
      * plenary view: provides a complete set or is an error condition





    .. py:method:: get_bin_hierarchy_id():
        :noindex:


    .. py:attribute:: bin_hierarchy_id
        :noindex:


    .. py:method:: get_bin_hierarchy():
        :noindex:


    .. py:attribute:: bin_hierarchy
        :noindex:


    .. py:method:: can_access_bin_hierarchy():
        :noindex:


    .. py:method:: use_comparative_bin_view():
        :noindex:


    .. py:method:: use_plenary_bin_view():
        :noindex:


    .. py:method:: get_root_bin_ids():
        :noindex:


    .. py:attribute:: root_bin_ids
        :noindex:


    .. py:method:: get_root_bins():
        :noindex:


    .. py:attribute:: root_bins
        :noindex:


    .. py:method:: has_parent_bins(bin_id):
        :noindex:


    .. py:method:: is_parent_of_bin(id_, bin_id):
        :noindex:


    .. py:method:: get_parent_bin_ids(bin_id):
        :noindex:


    .. py:method:: get_parent_bins(bin_id):
        :noindex:


    .. py:method:: is_ancestor_of_bin(id_, bin_id):
        :noindex:


    .. py:method:: has_child_bins(bin_id):
        :noindex:


    .. py:method:: is_child_of_bin(id_, bin_id):
        :noindex:


    .. py:method:: get_child_bin_ids(bin_id):
        :noindex:


    .. py:method:: get_child_bins(bin_id):
        :noindex:


    .. py:method:: is_descendant_of_bin(id_, bin_id):
        :noindex:


    .. py:method:: get_bin_node_ids(bin_id, ancestor_levels, descendant_levels, include_siblings):
        :noindex:


    .. py:method:: get_bin_nodes(bin_id, ancestor_levels, descendant_levels, include_siblings):
        :noindex:


Bin Hierarchy Design Session
----------------------------

.. py:class:: BinHierarchyDesignSession(abc_resource_sessions.BinHierarchyDesignSession, osid_sessions.OsidSession)
    This session defines methods for managing a hierarchy of ``Bin`` objects.


    Each node in the hierarchy is a unique ``Bin``.





    .. py:method:: get_bin_hierarchy_id():
        :noindex:


    .. py:attribute:: bin_hierarchy_id
        :noindex:


    .. py:method:: get_bin_hierarchy():
        :noindex:


    .. py:attribute:: bin_hierarchy
        :noindex:


    .. py:method:: can_modify_bin_hierarchy():
        :noindex:


    .. py:method:: add_root_bin(bin_id):
        :noindex:


    .. py:method:: remove_root_bin(bin_id):
        :noindex:


    .. py:method:: add_child_bin(bin_id, child_id):
        :noindex:


    .. py:method:: remove_child_bin(bin_id, child_id):
        :noindex:


    .. py:method:: remove_child_bins(bin_id):
        :noindex:


