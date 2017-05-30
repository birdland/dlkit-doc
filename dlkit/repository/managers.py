
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class RepositoryProfile(osid_managers.OsidProfile):
    """The repository profile describes interoperability among repository services."""


    def get_asset_content_lookup_session(self, *args, **kwargs):
        """Pass through to provider """
        return self._provider_manager.get_asset_content_lookup_session(*args, **kwargs)

    asset_content_lookup_session = property(fget=get_asset_content_lookup_session)

    def get_asset_content_lookup_session_for_repository(self, *args, **kwargs):
        """Pass through to provider """
        return self._provider_manager.get_asset_content_lookup_session_for_repository(args, kwargs)
    def supports_asset_lookup(self):
        """Tests if asset lookup is supported.

        :return: ``true`` if asset lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_asset_query(self):
        """Tests if asset query is supported.

        :return: ``true`` if asset query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_asset_search(self):
        """Tests if asset search is supported.

        :return: ``true`` if asset search is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_asset_admin(self):
        """Tests if asset administration is supported.

        :return: ``true`` if asset administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_asset_notification(self):
        """Tests if asset notification is supported.

        A repository may send messages when assets are created,
        modified, or deleted.

        :return: ``true`` if asset notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_asset_repository(self):
        """Tests if retrieving mappings of assets and repositories is supported.

        :return: ``true`` if asset repository mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_asset_repository_assignment(self):
        """Tests if managing mappings of assets and repositories is supported.

        :return: ``true`` if asset repository assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_asset_composition(self):
        """Tests if assets are included in compositions.

        :return: ``true`` if asset composition supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_asset_composition_design(self):
        """Tests if mapping assets to compositions is supported.

        :return: ``true`` if designing asset compositions is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_composition_lookup(self):
        """Tests if composition lookup is supported.

        :return: ``true`` if composition lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_composition_query(self):
        """Tests if composition query is supported.

        :return: ``true`` if composition query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_composition_search(self):
        """Tests if composition search is supported.

        :return: ``true`` if composition search is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_composition_admin(self):
        """Tests if composition administration is supported.

        :return: ``true`` if composition administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_composition_repository(self):
        """Tests if retrieval of composition to repository mappings is supported.

        :return: ``true`` if composition to repository mapping is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_composition_repository_assignment(self):
        """Tests if assigning composition to repository mappings is supported.

        :return: ``true`` if composition to repository assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_repository_lookup(self):
        """Tests if repository lookup is supported.

        :return: ``true`` if repository lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_repository_query(self):
        """Tests if repository query is supported.

        :return: ``true`` if repository query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_repository_admin(self):
        """Tests if repository administration is supported.

        :return: ``true`` if repository administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_repository_hierarchy(self):
        """Tests if a repository hierarchy traversal is supported.

        :return: ``true`` if a repository hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_repository_hierarchy_design(self):
        """Tests if a repository hierarchy design is supported.

        :return: ``true`` if a repository hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_asset_record_types(self):
        """Gets all the asset record types supported.

        :return: the list of supported asset record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    asset_record_types = property(fget=get_asset_record_types)

    def get_asset_search_record_types(self):
        """Gets all the asset search record types supported.

        :return: the list of supported asset search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    asset_search_record_types = property(fget=get_asset_search_record_types)

    def get_asset_content_record_types(self):
        """Gets all the asset content record types supported.

        :return: the list of supported asset content record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    asset_content_record_types = property(fget=get_asset_content_record_types)

    def get_composition_record_types(self):
        """Gets all the composition record types supported.

        :return: the list of supported composition record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    composition_record_types = property(fget=get_composition_record_types)

    def get_composition_search_record_types(self):
        """Gets all the composition search record types supported.

        :return: the list of supported composition search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    composition_search_record_types = property(fget=get_composition_search_record_types)

    def get_repository_record_types(self):
        """Gets all the repository record types supported.

        :return: the list of supported repository record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    repository_record_types = property(fget=get_repository_record_types)

    def get_repository_search_record_types(self):
        """Gets all the repository search record types supported.

        :return: the list of supported repository search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    repository_search_record_types = property(fget=get_repository_search_record_types)

    def get_spatial_unit_record_types(self):
        """Gets all the spatial unit record types supported.

        :return: the list of supported spatial unit record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    spatial_unit_record_types = property(fget=get_spatial_unit_record_types)

    def get_coordinate_types(self):
        """Gets all the coordinate types supported.

        :return: the list of supported coordinate types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    coordinate_types = property(fget=get_coordinate_types)


class RepositoryManager(osid_managers.OsidManager, osid_sessions.OsidSession, RepositoryProfile):
    """The repository manager provides access to asset lookup and creation session and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``AssetLookupSession:`` a session to retrieve assets
      * ``AssetQuerySession:`` a session to query assets
      * ``AssetSearchSession:`` a session to search for assets
      * ``AssetAdminSession:`` a session to create and delete assets
      * ``AssetNotificationSession:`` a session to receive notifications
        pertaining to asset changes
      * ``AssetRepositorySession:`` a session to look up asset to
        repository mappings
      * ``AssetRepositoryAssignmentSession:`` a session to manage asset
        to repository mappings
      * ``AssetSmartRepositorySession:`` a session to manage dynamic
        repositories of assets
      * ``AssetTemporalSession:`` a session to access the temporal
        coverage of an asset
      * ``AssetTemporalAssignmentSession:`` a session to manage the
        temporal coverage of an asset
      * ``AssetSpatialSession:`` a session to access the spatial
        coverage of an asset
      * ``AssetSpatialAssignmentSession:`` a session to manage the
        spatial coverage of an asset
      * ``AssetCompositionSession:`` a session to look up asset
        composition mappings
      * ``AssetCompositionDesignSession:`` a session to map assets to
        compositions

      * ``CompositionLookupSession: a`` session to retrieve compositions
      * ``CompositionQuerySession:`` a session to query compositions
      * ``CompositionSearchSession:`` a session to search for
        compositions
      * ``CompositionAdminSession:`` a session to create, update and
        delete compositions
      * ``CompositionNotificationSession:`` a session to receive
        notifications pertaining to changes in compositions
      * ``CompositionRepositorySession:`` a session to retrieve
        composition repository mappings
      * ``CompositionRepositoryAssignmentSession:`` a session to manage
        composition repository mappings
      * ``CompositionSmartRepositorySession:`` a session to manage
        dynamic repositories of compositions

      * ``RepositoryLookupSession: a`` session to retrieve repositories
      * ``RepositoryQuerySession:`` a session to query repositories
      * ``RepositorySearchSession:`` a session to search for
        repositories
      * ``RepositoryAdminSession:`` a session to create, update and
        delete repositories
      * ``RepositoryNotificationSession:`` a session to receive
        notifications pertaining to changes in repositories
      * ``RepositoryHierarchySession:`` a session to traverse repository
        hierarchies
      * ``RepositoryHierarchyDesignSession:`` a session to manage
        repository hierarchies

    """

    def get_repository_batch_manager(self):
        """Gets a ``RepositoryBatchManager``.

        :return: a ``RepostoryBatchManager``
        :rtype: ``osid.repository.batch.RepositoryBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_batch()`` is ``true``.*

        """
        return # osid.repository.batch.RepositoryBatchManager

    repository_batch_manager = property(fget=get_repository_batch_manager)

    def get_repository_rules_manager(self):
        """Gets a ``RepositoryRulesManager``.

        :return: a ``RepostoryRulesManager``
        :rtype: ``osid.repository.rules.RepositoryRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_rules()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_rules()`` is ``true``.*

        """
        return # osid.repository.rules.RepositoryRulesManager

    repository_rules_manager = property(fget=get_repository_rules_manager)


class RepositoryProxyManager(osid_managers.OsidProxyManager, RepositoryProfile):
    """The repository manager provides access to asset lookup and creation session and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` for the
    purposes of passing information from a server environment. The
    sessions included in this manager are:

      * ``AssetLookupSession:`` a session to retrieve assets
      * ``AssetQuerySession:`` a session to query assets
      * ``AssetSearchSession:`` a session to search for assets
      * ``AssetAdminSession:`` a session to create and delete assets
      * ``AssetNotificationSession:`` a session to receive notifications
        pertaining to asset changes
      * ``AssetRepositorySession:`` a session to look up asset to
        repository mappings
      * ``AssetRepositoryAssignmentSession:`` a session to manage asset
        to repository mappings
      * ``AssetSmartRepositorySession:`` a session to manage dynamic
        repositories of assets
      * ``AssetTemporalSession:`` a session to access the temporal
        coverage of an asset
      * ``AssetTemporalAssignmentSession:`` a session to manage the
        temporal coverage of an asset
      * ``AssetSpatialSession:`` a session to access the spatial
        coverage of an asset
      * ``AssetSpatialAssignmentSession:`` a session to manage the
        spatial coverage of an asset
      * ``AssetCompositionSession:`` a session to look up asset
        composition mappings
      * ``AssetCompositionDesignSession:`` a session to map assets to
        compositions

      * ``CompositionLookupSession: a`` session to retrieve compositions
      * ``CompositionQuerySession:`` a session to query compositions
      * ``CompositionSearchSession:`` a session to search for
        compositions
      * ``CompositionAdminSession:`` a session to create, update and
        delete compositions
      * ``CompositionNotificationSession:`` a session to receive
        notifications pertaining to changes in compositions
      * ``CompositionRepositorySession:`` a session to retrieve
        composition repository mappings
      * ``CompositionRepositoryAssignmentSession:`` a session to manage
        composition repository mappings
      * ``CompositionSmartRepositorySession:`` a session to manage
        dynamic repositories of compositions

      * ``RepositoryLookupSession: a`` session to retrieve repositories
      * ``RepositoryQuerySession:`` a session to query repositories
      * ``RepositorySearchSession:`` a session to search for
        repositories
      * ``RepositoryAdminSession:`` a session to create, update and
        delete repositories
      * ``RepositoryNotificationSession:`` a session to receive
        notifications pertaining to changes in repositories
      * ``RepositoryHierarchySession:`` a session to traverse repository
        hierarchies
      * ``RepositoryHierarchyDesignSession:`` a session to manage
        repository hierarchies

    """

    def get_repository_batch_proxy_manager(self):
        """Gets a ``RepositoryBatchProxyManager``.

        :return: a ``RepostoryBatchProxyManager``
        :rtype: ``osid.repository.batch.RepositoryBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_batch()`` is ``true``.*

        """
        return # osid.repository.batch.RepositoryBatchProxyManager

    repository_batch_proxy_manager = property(fget=get_repository_batch_proxy_manager)

    def get_repository_rules_proxy_manager(self):
        """Gets a ``RepositoryRulesProxyManager``.

        :return: a ``RepostoryRulesProxyManager``
        :rtype: ``osid.repository.rules.RepositoryRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_rules()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_repository_rules()`` is ``true``.*

        """
        return # osid.repository.rules.RepositoryRulesProxyManager

    repository_rules_proxy_manager = property(fget=get_repository_rules_proxy_manager)


