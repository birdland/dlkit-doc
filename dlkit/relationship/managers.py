from ..osid import managers as osid_managers


class RelationshipProfile(osid_managers.OsidProfile):
    """The relationship profile describes the interoperability among relationship services."""
    def supports_relationship_lookup(self):
        """Tests if looking up relationships is supported.

        :return: ``true`` if relationship lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_relationship_admin(self):
        """Tests if relationship administrative service is supported.

        :return: ``true`` if relationship administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_family_lookup(self):
        """Tests if looking up families is supported.

        :return: ``true`` if family lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_family_admin(self):
        """Tests if familyadministrative service is supported.

        :return: ``true`` if family administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_family_hierarchy(self):
        """Tests for the availability of a family hierarchy traversal service.

        :return: ``true`` if family hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_family_hierarchy_design(self):
        """Tests for the availability of a family hierarchy design service.

        :return: ``true`` if family hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_relationship_record_types(self):
        """Gets the supported ``Relationship`` record types.

        :return: a list containing the supported ``Relationship`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    relationship_record_types = property(fget=get_relationship_record_types)

    def get_relationship_search_record_types(self):
        """Gets the supported ``Relationship`` search record types.

        :return: a list containing the supported ``Relationship`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    relationship_search_record_types = property(fget=get_relationship_search_record_types)

    def get_family_record_types(self):
        """Gets the supported ``Family`` record types.

        :return: a list containing the supported ``Family`` types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    family_record_types = property(fget=get_family_record_types)

    def get_family_search_record_types(self):
        """Gets the supported ``Family`` search record types.

        :return: a list containing the supported ``Family`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    family_search_record_types = property(fget=get_family_search_record_types)


class RelationshipManager(osid_managers.OsidManager, RelationshipProfile):
    """The relationship manager provides access to relationship sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``RelationshipLookupSession:`` a session to retrieve and examine
        relationships
      * ``RelationshipQuerySession:`` a session to query relationships
      * ``RelationshipSearchSession:`` a session to search for
        relationships
      * ``RelationshipAdminSession:`` a session to manage relationships
      * ``RelationshipNotificationSession:`` a session to receive
        notifications pertaining to relationship changes
      * ``RelationshipFamilySession:`` a session to look up relationship
        to family mappings
      * ``RelationshipFamilyAssignmentSession:`` a session to manage
        relationship to family catalog mappings
      * ``RelationshipSmartFamilySession:`` a session to manage dynamic
        relationship families

      * ``FamilyLookupSession:`` a session to retrieve families
      * ``FamilyQuerySession:`` a session to query families
      * ``FamilySearchSession:`` a session to search for families
      * ``FamilyAdminSession:`` a session to create and delete families
      * ``FamilyNotificationSession:`` a session to receive
        notifications pertaining to family changes
      * ``FamilyHierarchySession:`` a session to traverse a hierarchy of
        families
      * ``FamilyHierarchyDesignSession:`` a session to manage a family
        hierarchy


    """
    def get_relationship_lookup_session(self):
        """Gets the ``OsidSession`` associated with the relationship lookup service.

        :return: a ``RelationshipLookupSession``
        :rtype: ``osid.relationship.RelationshipLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_lookup()`` is ``false``

        """
        return # osid.relationship.RelationshipLookupSession

    relationship_lookup_session = property(fget=get_relationship_lookup_session)

    def get_relationship_lookup_session_for_family(self, family_id):
        """Gets the ``OsidSession`` associated with the relationship lookup service for the given family.

        :param family_id: the ``Id`` of the family
        :type family_id: ``osid.id.Id``
        :return: a ``RelationshipLookupSession``
        :rtype: ``osid.relationship.RelationshipLookupSession``
        :raise: ``NotFound`` -- no ``Family`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.relationship.RelationshipLookupSession

    def get_relationship_admin_session(self):
        """Gets the ``OsidSession`` associated with the relationship administration service.

        :return: a ``RelationshipAdminSession``
        :rtype: ``osid.relationship.RelationshipAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_admin()`` is ``false``

        """
        return # osid.relationship.RelationshipAdminSession

    relationship_admin_session = property(fget=get_relationship_admin_session)

    def get_relationship_admin_session_for_family(self, family_id):
        """Gets the ``OsidSession`` associated with the relationship administration service for the given family.

        :param family_id: the ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :return: a ``RelationshipAdminSession``
        :rtype: ``osid.relationship.RelationshipAdminSession``
        :raise: ``NotFound`` -- no family found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.relationship.RelationshipAdminSession

    def get_family_lookup_session(self):
        """Gets the ``OsidSession`` associated with the family lookup service.

        :return: a ``FamilyLookupSession``
        :rtype: ``osid.relationship.FamilyLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_lookup()`` is ``false``

        """
        return # osid.relationship.FamilyLookupSession

    family_lookup_session = property(fget=get_family_lookup_session)

    def get_family_admin_session(self):
        """Gets the ``OsidSession`` associated with the family administrative service.

        :return: a ``FamilyAdminSession``
        :rtype: ``osid.relationship.FamilyAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_admin()`` is ``false``

        """
        return # osid.relationship.FamilyAdminSession

    family_admin_session = property(fget=get_family_admin_session)

    def get_family_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the family hierarchy service.

        :return: a ``FamilyHierarchySession`` for families
        :rtype: ``osid.relationship.FamilyHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_hierarchy()`` is ``false``

        """
        return # osid.relationship.FamilyHierarchySession

    family_hierarchy_session = property(fget=get_family_hierarchy_session)

    def get_family_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the family hierarchy design service.

        :return: a ``HierarchyDesignSession`` for families
        :rtype: ``osid.relationship.FamilyHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_hierarchy_design()`` is ``false``

        """
        return # osid.relationship.FamilyHierarchyDesignSession

    family_hierarchy_design_session = property(fget=get_family_hierarchy_design_session)

    def get_relationship_batch_manager(self):
        """Gets the relationship batch manager.

        :return: a ``RelationshipBatchManager``
        :rtype: ``osid.relationship.batch.RelationshipBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_batch()`` is ``false``

        """
        return # osid.relationship.batch.RelationshipBatchManager

    relationship_batch_manager = property(fget=get_relationship_batch_manager)

    def get_relationship_rules_manager(self):
        """Gets the relationship rules manager.

        :return: a ``RelationshipRulesManager``
        :rtype: ``osid.relationship.rules.RelationshipRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_rules()`` is ``false``

        """
        return # osid.relationship.rules.RelationshipRulesManager

    relationship_rules_manager = property(fget=get_relationship_rules_manager)


class RelationshipProxyManager(osid_managers.OsidProxyManager, RelationshipProfile):
    """The relationship manager provides access to relationship sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a Proxy. The sessions
    included in this manager are:

      * ``RelationshipLookupSession:`` a session to retrieve and examine
        relationships
      * ``RelationshipQuerySession:`` a session to query relationships
      * ``RelationshipSearchSession:`` a session to search for
        relationships
      * ``RelationshipAdminSession:`` a session to manage relationships
      * ``RelationshipNotificationSession:`` a session to receive
        notifications pertaining to relationship changes
      * ``RelationshipFamilySession:`` a session to look up relationship
        to family mappings
      * ``RelationshipFamilyAssignmentSession:`` a session to manage
        relationship to family catalog mappings
      * ``RelationshipSmartFamilySession:`` a session to manage dynamic
        relationship families

      * ``FamilyLookupSession:`` a session to retrieve families
      * ``FamilyQuerySession:`` a session to query families
      * ``FamilySearchSession:`` a session to search for families
      * ``FamilyAdminSession:`` a session to create and delete families
      * ``FamilyNotificationSession:`` a session to receive
        notifications pertaining to family changes
      * ``FamilyHierarchySession:`` a session to traverse a hierarchy of
        families
      * ``FamilyHierarchyDesignSession:`` a session to manage a family
        hierarchy


    """
    def get_relationship_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the relationship lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipLookupSession``
        :rtype: ``osid.relationship.RelationshipLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_lookup()`` is ``false``

        """
        return # osid.relationship.RelationshipLookupSession

    def get_relationship_lookup_session_for_family(self, family_id, proxy):
        """Gets the ``OsidSession`` associated with the relationship lookup service for the given family.

        :param family_id: the ``Id`` of the family
        :type family_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipLookupSession``
        :rtype: ``osid.relationship.RelationshipLookupSession``
        :raise: ``NotFound`` -- no ``Family`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.relationship.RelationshipLookupSession

    def get_relationship_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the relationship administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipAdminSession``
        :rtype: ``osid.relationship.RelationshipAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_admin()`` is ``false``

        """
        return # osid.relationship.RelationshipAdminSession

    def get_relationship_admin_session_for_family(self, family_id, proxy):
        """Gets the ``OsidSession`` associated with the relationship administration service for the given family.

        :param family_id: the ``Id`` of the family
        :type family_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipAdminSession``
        :rtype: ``osid.relationship.RelationshipAdminSession``
        :raise: ``NotFound`` -- no ``Family`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.relationship.RelationshipAdminSession

    def get_family_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FamilyLookupSession``
        :rtype: ``osid.relationship.FamilyLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_lookup()`` is ``false``

        """
        return # osid.relationship.FamilyLookupSession

    def get_family_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FamilyAdminSession``
        :rtype: ``osid.relationship.FamilyAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_admin()`` is ``false``

        """
        return # osid.relationship.FamilyAdminSession

    def get_family_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family hierarchy service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FamilyHierarchySession`` for families
        :rtype: ``osid.relationship.FamilyHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_hierarchy()`` is ``false``

        """
        return # osid.relationship.FamilyHierarchySession

    def get_family_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyDesignSession`` for families
        :rtype: ``osid.relationship.FamilyHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_hierarchy_design()`` is ``false``

        """
        return # osid.relationship.FamilyHierarchyDesignSession

    def get_relationship_batch_proxy_manager(self):
        """Gets the relationship batch proxy manager.

        :return: a ``RelationshipBatchProxyManager``
        :rtype: ``osid.relationship.batch.RelationshipBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_rules()`` is ``false``

        """
        return # osid.relationship.batch.RelationshipBatchProxyManager

    relationship_batch_proxy_manager = property(fget=get_relationship_batch_proxy_manager)

    def get_relationship_rules_proxy_manager(self):
        """Gets the relationship rules proxy manager.

        :return: a ``RelationshipRulesProxyManager``
        :rtype: ``osid.relationship.rules.RelationshipRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_rules()`` is ``false``

        """
        return # osid.relationship.rules.RelationshipRulesProxyManager

    relationship_rules_proxy_manager = property(fget=get_relationship_rules_proxy_manager)


