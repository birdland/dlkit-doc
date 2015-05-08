from ..osid import managers as osid_managers


class HierarchyProfile(osid_managers.OsidProfile):
    """The hierarchy profile describes the interoperability among hierarchy services."""
    def supports_hierarchy_traversal(self):
        """Tests if hierarchy traversal is supported.

        :return: ``true`` if hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_hierarchy_design(self):
        """Tests if hierarchy design is supported.

        :return: ``true`` if hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_hierarchy_lookup(self):
        """Tests if a hierarchy lookup is supported.

        :return: ``true`` if hierarchy lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_hierarchy_admin(self):
        """Tests if a hierarchy administration is supported.

        :return: ``true`` if hierarchy administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_hierarchy_record_types(self):
        """Gets the supported ``Hierarchy`` types.

        :return: a list containing the supported ``Hierarchy`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    hierarchy_record_types = property(fget=get_hierarchy_record_types)

    def get_hierarchy_search_record_types(self):
        """Gets the supported ``Hierarchy`` search record types.

        :return: a list containing the supported ``Hierarchy`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    hierarchy_search_record_types = property(fget=get_hierarchy_search_record_types)


class HierarchyManager(osid_managers.OsidManager, HierarchyProfile):
    """The hierarchy manager provides access sessions to traverse and manage hierrachies of ``Ids``.

    The sessions included in this manager are:

      * ``HierarchyTraversalSession:`` a basic session traversing a
        hierarchy
      * ``HierarchyDesignSession:`` a session to design a hierarchy
      * ``HierarchySequencingSession:`` a session to sequence nodes in a
        hierarchy
      * ``HierarchyStructureNotificationSession:`` a session for
        notififcations within a hierarchy structure
      * ``HierarchyLookupSession:`` a session looking up hiererachies
      * ``HierarchyQuerySession:`` a session querying hiererachies
      * ``HierarchySearchSession:`` a session for searching for
        hierarchies
      * ``HierarchyAdminSession:`` a session for creating and deleting
        hierarchies
      * ``HierarchyNotificationSession:`` a session for subscribing to
        changes in hierarchies


    """
    def get_hierarchy_traversal_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service.

        :return: a ``HierarchyTraversalSession``
        :rtype: ``osid.hierarchy.HierarchyTraversalSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_traversal()`` is ``false``

        """
        return # osid.hierarchy.HierarchyTraversalSession

    hierarchy_traversal_session = property(fget=get_hierarchy_traversal_session)

    def get_hierarchy_traversal_session_for_hierarchy(self, hierarchy_id):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service for the given hierarchy.

        :param hierarchy_id: the ``Id`` of the hierarchy
        :type hierarchy_id: ``osid.id.Id``
        :return: the new ``HierarchyTraversalSession``
        :rtype: ``osid.hierarchy.HierarchyTraversalSession``
        :raise: ``NotFound`` -- ``hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``hierarchyid`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_hierarchy_traversal()`` or ``supports_visible_fedaration()`` is ``false``

        """
        return # osid.hierarchy.HierarchyTraversalSession

    def get_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy design service.

        :return: a ``HierarchyDesignSession``
        :rtype: ``osid.hierarchy.HierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_design()`` is ``false``

        """
        return # osid.hierarchy.HierarchyDesignSession

    hierarchy_design_session = property(fget=get_hierarchy_design_session)

    def get_hierarchy_design_session_for_hierarchy(self, hierarchy_id):
        """Gets the ``OsidSession`` associated with the topology design service using for the given hierarchy.

        :param hierarchy_id: the ``Id`` of the graph
        :type hierarchy_id: ``osid.id.Id``
        :return: a ``HierarchyDesignSession``
        :rtype: ``osid.hierarchy.HierarchyDesignSession``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_design()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.hierarchy.HierarchyDesignSession

    def get_hierarchy_lookup_session(self):
        """Gets the ``OsidSession`` associated with the hierarchy lookup service.

        :return: a ``HierarchyLookupSession``
        :rtype: ``osid.hierarchy.HierarchyLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_lookup()`` is ``false``

        """
        return # osid.hierarchy.HierarchyLookupSession

    hierarchy_lookup_session = property(fget=get_hierarchy_lookup_session)

    def get_hierarchy_admin_session(self):
        """Gets the hierarchy administrative session.

        :return: a ``HierarchyAdminSession``
        :rtype: ``osid.hierarchy.HierarchyAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_admin()`` is ``false``

        """
        return # osid.hierarchy.HierarchyAdminSession

    hierarchy_admin_session = property(fget=get_hierarchy_admin_session)


class HierarchyProxyManager(osid_managers.OsidProxyManager, HierarchyProfile):
    """The hierarchy manager provides access sessions to traverse and manage hierrachies of ``Ids``.

    Methods in this manager accept a ``Proxy`` to pass information from
    server environments. The sessions included in this manager are:

      * ``HierarchyTraversalSession:`` a basic session traversing a
        hierarchy
      * ``HierarchyDesignSession:`` a session to design a hierarchy
      * ``HierarchySequencingSession:`` a session to sequence nodes in a
        hierarchy
      * ``HierarchyStructureNotificationSession:`` a session for
        notififcations within a hierarchy structure
      * ``HierarchyLookupSession:`` a session looking up hiererachies
      * ``HierarchyQuerySession:`` a session querying hiererachies
      * ``HierarchySearchSession:`` a session for searching for
        hierarchies
      * ``HierarchyAdminSession:`` a session for creating and deleting
        hierarchies
      * ``HierarchyNotificationSession:`` a session for subscribing to
        changes in hierarchies


    """
    def get_hierarchy_traversal_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyTraversalSession``
        :rtype: ``osid.hierarchy.HierarchyTraversalSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_traversal()`` is ``false``

        """
        return # osid.hierarchy.HierarchyTraversalSession

    def get_hierarchy_traversal_session_for_hierarchy(self, hierarchy_id, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy traversal service for the given hierarchy.

        :param hierarchy_id: the ``Id`` of the hierarchy
        :type hierarchy_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyTraversalSession``
        :rtype: ``osid.hierarchy.HierarchyTraversalSession``
        :raise: ``NotFound`` -- ``hierarchyid`` not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_hierarchy_traversal()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.hierarchy.HierarchyTraversalSession

    def get_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyDesignSession``
        :rtype: ``osid.hierarchy.HierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_design()`` is ``false``

        """
        return # osid.hierarchy.HierarchyDesignSession

    def get_hierarchy_design_session_for_hierarchy(self, hierarchy_id, proxy):
        """Gets the ``OsidSession`` associated with the topology design service using for the given hierarchy.

        :param hierarchy_id: the ``Id`` of the hierarchy
        :type hierarchy_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyDesignSession``
        :rtype: ``osid.hierarchy.HierarchyDesignSession``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_design()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.hierarchy.HierarchyDesignSession

    def get_hierarchy_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the hierarchy lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyLookupSession``
        :rtype: ``osid.hierarchy.HierarchyLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_lookup()`` is ``false``

        """
        return # osid.hierarchy.HierarchyLookupSession

    def get_hierarchy_admin_session(self, proxy):
        """Gets the hierarchy administrative session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyAdminSession``
        :rtype: ``osid.hierarchy.HierarchyAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_hierarchy_admin()`` is ``false``

        """
        return # osid.hierarchy.HierarchyAdminSession


