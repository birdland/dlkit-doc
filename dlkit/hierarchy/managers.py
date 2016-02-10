
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class HierarchyProfile(osid_managers.OsidProfile):
    """The hierarchy profile describes the interoperability among hierarchy services."""

    def supports_hierarchy_traversal(self):
        """Tests if hierarchy traversal is supported.

        :return: ``true`` if hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_hierarchy_design(self):
        """Tests if hierarchy design is supported.

        :return: ``true`` if hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_hierarchy_lookup(self):
        """Tests if a hierarchy lookup is supported.

        :return: ``true`` if hierarchy lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_hierarchy_admin(self):
        """Tests if a hierarchy administration is supported.

        :return: ``true`` if hierarchy administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_hierarchy_record_types(self):
        """Gets the supported ``Hierarchy`` types.

        :return: a list containing the supported ``Hierarchy`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    hierarchy_record_types = property(fget=get_hierarchy_record_types)

    def get_hierarchy_search_record_types(self):
        """Gets the supported ``Hierarchy`` search record types.

        :return: a list containing the supported ``Hierarchy`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    hierarchy_search_record_types = property(fget=get_hierarchy_search_record_types)


class HierarchyManager(osid_managers.OsidManager, osid_sessions.OsidSession, HierarchyProfile):
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




