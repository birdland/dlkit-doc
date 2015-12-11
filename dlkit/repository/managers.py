
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class RepositoryProfile(osid_managers.OsidProfile):
    """The repository profile describes interoperability among repository services."""
    



    def supports_visible_federation(self):
        """Tests if federation is visible.

        return: (boolean) - ``true`` if visible federation is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_asset_lookup(self):
        """Tests if asset lookup is supported.

        return: (boolean) - ``true`` if asset lookup is supported ``,``
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_asset_query(self):
        """Tests if asset query is supported.

        return: (boolean) - ``true`` if asset query is supported ``,``
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_asset_search(self):
        """Tests if asset search is supported.

        return: (boolean) - ``true`` if asset search is supported ``,``
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_asset_admin(self):
        """Tests if asset administration is supported.

        return: (boolean) - ``true`` if asset administration is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_asset_notification(self):
        """Tests if asset notification is supported.

        A repository may send messages when assets are created,
        modified, or deleted.

        return: (boolean) - ``true`` if asset notification is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_asset_repository(self):
        """Tests if retrieving mappings of assets and repositories is supported.

        return: (boolean) - ``true`` if asset repository mapping
                retrieval is supported ``,`` ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_asset_repository_assignment(self):
        """Tests if managing mappings of assets and repositories is supported.

        return: (boolean) - ``true`` if asset repository assignment is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_asset_smart_repository(self):
        """Tests if asset smart repository is supported.

        return: (boolean) - ``true`` if asset smart repository is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_asset_temporal(self):
        """Tests if retrieving mappings of assets and time coverage is supported.

        return: (boolean) - ``true`` if asset temporal mapping retrieval
                is supported ``,`` ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_asset_temporal_assignment(self):
        """Tests if managing mappings of assets and time ocverage is supported.

        return: (boolean) - ``true`` if asset temporal assignment is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_asset_spatial(self):
        """Tests if retrieving mappings of assets and spatial coverage is supported.

        return: (boolean) - ``true`` if asset spatial mapping retrieval
                is supported ``,`` ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_asset_spatial_assignment(self):
        """Tests if managing mappings of assets and spatial ocverage is supported.

        return: (boolean) - ``true`` if asset spatial assignment is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_asset_composition(self):
        """Tests if assets are included in compositions.

        return: (boolean) - ``true`` if asset composition supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_asset_composition_design(self):
        """Tests if mapping assets to compositions is supported.

        return: (boolean) - ``true`` if designing asset compositions is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_composition_lookup(self):
        """Tests if composition lookup is supported.

        return: (boolean) - ``true`` if composition lookup is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_composition_query(self):
        """Tests if composition query is supported.

        return: (boolean) - ``true`` if composition query is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_composition_search(self):
        """Tests if composition search is supported.

        return: (boolean) - ``true`` if composition search is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_composition_admin(self):
        """Tests if composition administration is supported.

        return: (boolean) - ``true`` if composition administration is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_composition_notification(self):
        """Tests if composition notification is supported.

        return: (boolean) - ``true`` if composition notification is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_composition_repository(self):
        """Tests if retrieval of composition to repository mappings is supported.

        return: (boolean) - ``true`` if composition to repository
                mapping is supported ``,`` ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_composition_repository_assignment(self):
        """Tests if assigning composition to repository mappings is supported.

        return: (boolean) - ``true`` if composition to repository
                assignment is supported ``,`` ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_composition_smart_repository(self):
        """Tests if composition smart repository is supported.

        return: (boolean) - ``true`` if composition smart repository is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_repository_lookup(self):
        """Tests if repository lookup is supported.

        return: (boolean) - ``true`` if repository lookup is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_repository_query(self):
        """Tests if repository query is supported.

        return: (boolean) - ``true`` if repository query is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_repository_search(self):
        """Tests if repository search is supported.

        return: (boolean) - ``true`` if repository search is supported
                ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_repository_admin(self):
        """Tests if repository administration is supported.

        return: (boolean) - ``true`` if repository administration is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_repository_notification(self):
        """Tests if repository notification is supported.

        Messages may be sent when ``Repository`` objects are created,
        deleted or updated. Notifications for assets within repositories
        are sent via the asset notification session.

        return: (boolean) - ``true`` if repository notification is
                supported ``,``  ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_repository_hierarchy(self):
        """Tests if a repository hierarchy traversal is supported.

        return: (boolean) - ``true`` if a repository hierarchy traversal
                is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_repository_hierarchy_design(self):
        """Tests if a repository hierarchy design is supported.

        return: (boolean) - ``true`` if a repository hierarchy design is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_repository_batch(self):
        """Tests if a repository batch service is supported.

        return: (boolean) - ``true`` if a repository batch service is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_repository_rules(self):
        """Tests if a repository rules service is supported.

        return: (boolean) - ``true`` if a repository rules service is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_asset_record_types(self):
        """Gets all the asset record types supported.

        return: (osid.type.TypeList) - the list of supported asset
                record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    asset_record_types = property(fget=get_asset_record_types)


    def supports_asset_record_type(self, asset_record_type):
        """Tests if a given asset type is supported.

        arg:    asset_record_type (osid.type.Type): the asset record
                type
        return: (boolean) - ``true`` if the asset record type is
                supported ``,``  ``false`` otherwise
        raise:  NullArgument - ``asset_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_asset_search_record_types(self):
        """Gets all the asset search record types supported.

        return: (osid.type.TypeList) - the list of supported asset
                search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    asset_search_record_types = property(fget=get_asset_search_record_types)


    def supports_asset_search_record_type(self, asset_search_record_type):
        """Tests if a given asset search record type is supported.

        arg:    asset_search_record_type (osid.type.Type): the asset
                search record type
        return: (boolean) - ``true`` if the asset search record type is
                supported ``,``  ``false`` otherwise
        raise:  NullArgument - ``asset_search_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_asset_content_record_types(self):
        """Gets all the asset content record types supported.

        return: (osid.type.TypeList) - the list of supported asset
                content record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    asset_content_record_types = property(fget=get_asset_content_record_types)


    def supports_asset_content_record_type(self, asset_content_record_type):
        """Tests if a given asset content record type is supported.

        arg:    asset_content_record_type (osid.type.Type): the asset
                content record type
        return: (boolean) - ``true`` if the asset content record type is
                supported ``,``  ``false`` otherwise
        raise:  NullArgument - ``asset_content_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_composition_record_types(self):
        """Gets all the composition record types supported.

        return: (osid.type.TypeList) - the list of supported composition
                record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    composition_record_types = property(fget=get_composition_record_types)


    def supports_composition_record_type(self, composition_record_type):
        """Tests if a given composition record type is supported.

        arg:    composition_record_type (osid.type.Type): the
                composition record type
        return: (boolean) - ``true`` if the composition record type is
                supported ``,``  ``false`` otherwise
        raise:  NullArgument - ``composition_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_composition_search_record_types(self):
        """Gets all the composition search record types supported.

        return: (osid.type.TypeList) - the list of supported composition
                search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    composition_search_record_types = property(fget=get_composition_search_record_types)


    def supports_composition_search_record_type(self, composition_search_record_type):
        """Tests if a given composition search record type is supported.

        arg:    composition_search_record_type (osid.type.Type): the
                composition serach type
        return: (boolean) - ``true`` if the composition search record
                type is supported ``,`` ``false`` otherwise
        raise:  NullArgument - ``composition_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_repository_record_types(self):
        """Gets all the repository record types supported.

        return: (osid.type.TypeList) - the list of supported repository
                record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    repository_record_types = property(fget=get_repository_record_types)


    def supports_repository_record_type(self, repository_record_type):
        """Tests if a given repository record type is supported.

        arg:    repository_record_type (osid.type.Type): the repository
                record type
        return: (boolean) - ``true`` if the repository record type is
                supported ``,``  ``false`` otherwise
        raise:  NullArgument - ``repository_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_repository_search_record_types(self):
        """Gets all the repository search record types supported.

        return: (osid.type.TypeList) - the list of supported repository
                search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    repository_search_record_types = property(fget=get_repository_search_record_types)


    def supports_repository_search_record_type(self, repository_search_record_type):
        """Tests if a given repository search record type is supported.

        arg:    repository_search_record_type (osid.type.Type): the
                repository search type
        return: (boolean) - ``true`` if the repository search record
                type is supported ``,`` ``false`` otherwise
        raise:  NullArgument - ``repository_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_spatial_unit_record_types(self):
        """Gets all the spatial unit record types supported.

        return: (osid.type.TypeList) - the list of supported spatial
                unit record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    spatial_unit_record_types = property(fget=get_spatial_unit_record_types)


    def supports_spatial_unit_record_type(self, spatial_unit_record_type):
        """Tests if a given spatial unit record type is supported.

        arg:    spatial_unit_record_type (osid.type.Type): the spatial
                unit record type
        return: (boolean) - ``true`` if the spatial unit record type is
                supported ``,``  ``false`` otherwise
        raise:  NullArgument - ``spatial_unit_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_coordinate_types(self):
        """Gets all the coordinate types supported.

        return: (osid.type.TypeList) - the list of supported coordinate
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    coordinate_types = property(fget=get_coordinate_types)


    def supports_coordinate_type(self, coordinate_type):
        """Tests if a given coordinate type is supported.

        arg:    coordinate_type (osid.type.Type): the coordinate type
        return: (boolean) - ``true`` if the coordinate type is supported
                ``,``  ``false`` otherwise
        raise:  NullArgument - ``coordinate_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


class RepositoryManager(osid_managers.OsidManager, osid_sessions.OsidSession, RepositoryProfile):
    """The repository manager provides access to asset lookup and creation session and provides interoperability tests for
        various aspects of this service.

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
    



    def get_asset_lookup_session(self):
        """Gets the ``OsidSession`` associated with the asset lookup service.

        return: (osid.repository.AssetLookupSession) - the new
                ``AssetLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_asset_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_lookup()`` is ``true``.*

        """
        return # osid.repository.AssetLookupSession

    asset_lookup_session = property(fget=get_asset_lookup_session)


    def get_asset_lookup_session_for_repository(self, repository_id):
        """Gets the ``OsidSession`` associated with the asset lookup service for the given repository.

        arg:    repository_id (osid.id.Id): the ``Id`` of the repository
        return: (osid.repository.AssetLookupSession) - the new
                ``AssetLookupSession``
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``repository_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_asset_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.repository.AssetLookupSession


    def get_asset_query_session(self):
        """Gets an asset query session.

        return: (osid.repository.AssetQuerySession) - an
                ``AssetQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_asset_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_query()`` is ``true``.*

        """
        return # osid.repository.AssetQuerySession

    asset_query_session = property(fget=get_asset_query_session)


    def get_asset_query_session_for_repository(self, repository_id):
        """Gets an asset query session for the given repository.

        arg:    repository_id (osid.id.Id): the ``Id`` of the repository
        return: (osid.repository.AssetQuerySession) - an
                ``AssetQuerySession``
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``repository_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_asset_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_query()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return # osid.repository.AssetQuerySession


    def get_asset_search_session(self):
        """Gets an asset search session.

        return: (osid.repository.AssetSearchSession) - an
                ``AssetSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_asset_search()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_search()`` is ``true``.*

        """
        return # osid.repository.AssetSearchSession

    asset_search_session = property(fget=get_asset_search_session)


    def get_asset_search_session_for_repository(self, repository_id):
        """Gets an asset search session for the given repository.

        arg:    repository_id (osid.id.Id): the ``Id`` of the repository
        return: (osid.repository.AssetSearchSession) - an
                ``AssetSearchSession``
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``repository_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_asset_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.repository.AssetSearchSession


    def get_asset_admin_session(self):
        """Gets an asset administration session for creating, updating and deleting assets.

        return: (osid.repository.AssetAdminSession) - an
                ``AssetAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_asset_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_admin()`` is ``true``.*

        """
        return # osid.repository.AssetAdminSession

    asset_admin_session = property(fget=get_asset_admin_session)


    def get_asset_admin_session_for_repository(self, repository_id):
        """Gets an asset administration session for the given repository.

        arg:    repository_id (osid.id.Id): the ``Id`` of the repository
        return: (osid.repository.AssetAdminSession) - an
                ``AssetAdminSession``
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``repository_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_asset_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_admin()`` and ``supports_visible_federation()``
        are ``true``.*

        """
        return # osid.repository.AssetAdminSession


    def get_asset_notification_session(self, asset_receiver):
        """Gets the notification session for notifications pertaining to asset changes.

        arg:    asset_receiver (osid.repository.AssetReceiver): the
                notification callback
        return: (osid.repository.AssetNotificationSession) - an
                ``AssetNotificationSession``
        raise:  NullArgument - ``asset_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_asset_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_notification()`` is ``true``.*

        """
        return # osid.repository.AssetNotificationSession


    def get_asset_notification_session_for_repository(self, asset_receiver, repository_id):
        """Gets the asset notification session for the given repository.

        arg:    asset_receiver (osid.repository.AssetReceiver): the
                notification callback
        arg:    repository_id (osid.id.Id): the ``Id`` of the repository
        return: (osid.repository.AssetNotificationSession) - an
                ``AssetNotificationSession``
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``asset_receiver`` or ``repository_id``
                is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_asset_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_notfication()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.repository.AssetNotificationSession


    def get_asset_repository_session(self):
        """Gets the session for retrieving asset to repository mappings.

        return: (osid.repository.AssetRepositorySession) - an
                ``AssetRepositorySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_asset_repository()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_repository()`` is ``true``.*

        """
        return # osid.repository.AssetRepositorySession

    asset_repository_session = property(fget=get_asset_repository_session)


    def get_asset_repository_assignment_session(self):
        """Gets the session for assigning asset to repository mappings.

        return: (osid.repository.AssetRepositoryAssignmentSession) - an
                ``AssetRepositoryAsignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_asset_repository_assignment()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_repository_assignment()`` is ``true``.*

        """
        return # osid.repository.AssetRepositoryAssignmentSession

    asset_repository_assignment_session = property(fget=get_asset_repository_assignment_session)


    def get_asset_smart_repository_session(self, repository_id):
        """Gets an asset smart repository session for the given repository.

        arg:    repository_id (osid.id.Id): the ``Id`` of the repository
        return: (osid.repository.AssetSmartRepositorySession) - an
                ``AssetSmartRepositorySession``
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``repository_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_asset_smart_repository()``
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_smart_repository()`` is ``true``.*

        """
        return # osid.repository.AssetSmartRepositorySession


    def get_asset_temporal_session(self):
        """Gets the session for retrieving temporal coverage of an asset.

        return: (osid.repository.AssetTemporalSession) - an
                ``AssetTemporalSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_asset_temporal()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_temporal()`` is ``true``.*

        """
        return # osid.repository.AssetTemporalSession

    asset_temporal_session = property(fget=get_asset_temporal_session)


    def get_asset_temporal_session_for_repository(self, repository_id):
        """Gets the session for retrieving temporal coverage of an asset for the given repository.

        arg:    repository_id (osid.id.Id): the ``Id`` of the repository
        return: (osid.repository.AssetTemporalSession) - an
                ``AssetTemporalSession``
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``repository_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_asset_temporal()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_temporal()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.repository.AssetTemporalSession


    def get_asset_temporal_assignment_session(self):
        """Gets the session for assigning temporal coverage to an asset.

        return: (osid.repository.AssetTemporalAssignmentSession) - an
                ``AssetTemporalAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_asset_temporal_assignment()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_temporal_assignment()`` is ``true``.*

        """
        return # osid.repository.AssetTemporalAssignmentSession

    asset_temporal_assignment_session = property(fget=get_asset_temporal_assignment_session)


    def get_asset_temporal_assignment_session_for_repository(self, repository_id):
        """Gets the session for assigning temporal coverage of an asset for the given repository.

        arg:    repository_id (osid.id.Id): the ``Id`` of the repository
        return: (osid.repository.AssetTemporalAssignmentSession) - an
                ``AssetTemporalAssignmentSession``
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``repository_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_asset_temporal_assignment()``
                or ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_temporal_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.repository.AssetTemporalAssignmentSession


    def get_asset_spatial_session(self):
        """Gets the session for retrieving spatial coverage of an asset.

        return: (osid.repository.AssetSpatialSession) - an
                ``AssetSpatialSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_spatial_assets()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_spatial_assets()`` is ``true``.*

        """
        return # osid.repository.AssetSpatialSession

    asset_spatial_session = property(fget=get_asset_spatial_session)


    def get_asset_spatial_session_for_repository(self, repository_id):
        """Gets the session for retrieving spatial coverage of an asset for the given repository.

        arg:    repository_id (osid.id.Id): the ``Id`` of the repository
        return: (osid.repository.AssetSpatialSession) - an
                ``AssetSpatialSession``
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``repository_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_asset_spatial()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_spatial()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.repository.AssetSpatialSession


    def get_asset_spatial_assignment_session(self):
        """Gets the session for assigning spatial coverage to an asset.

        return: (osid.repository.AssetSpatialAssignmentSession) - an
                ``AssetSpatialAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_asset_spatial_assignment()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_spatial_assignment()`` is ``true``.*

        """
        return # osid.repository.AssetSpatialAssignmentSession

    asset_spatial_assignment_session = property(fget=get_asset_spatial_assignment_session)


    def get_asset_spatial_assignment_session_for_repository(self, repository_id):
        """Gets the session for assigning spatial coverage of an asset for the given repository.

        arg:    repository_id (osid.id.Id): the ``Id`` of the repository
        return: (osid.repository.AssetSpatialAssignmentSession) - an
                ``AssetSpatialAssignmentSession``
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``repository_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_asset_spatial_assignment()``
                or ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_spatial_assignment()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.repository.AssetSpatialAssignmentSession


    def get_asset_composition_session(self):
        """Gets the session for retrieving asset compositions.

        return: (osid.repository.AssetCompositionSession) - an
                ``AssetCompositionSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_asset_composition()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_composition()`` is ``true``.*

        """
        return # osid.repository.AssetCompositionSession

    asset_composition_session = property(fget=get_asset_composition_session)


    def get_asset_composition_design_session(self):
        """Gets the session for creating asset compositions.

        return: (osid.repository.AssetCompositionDesignSession) - an
                ``AssetCompositionDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_asset_composition_design()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_asset_composition_design()`` is ``true``.*

        """
        return # osid.repository.AssetCompositionDesignSession

    asset_composition_design_session = property(fget=get_asset_composition_design_session)


    def get_composition_lookup_session(self):
        """Gets the ``OsidSession`` associated with the composition lookup service.

        return: (osid.repository.CompositionLookupSession) - the new
                ``CompositionLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_composition_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_composition_lookup()`` is ``true``.*

        """
        return # osid.repository.CompositionLookupSession

    composition_lookup_session = property(fget=get_composition_lookup_session)


    def get_composition_lookup_session_for_repository(self, repository_id):
        """Gets the ``OsidSession`` associated with the composition lookup service for the given repository.

        arg:    repository_id (osid.id.Id): the ``Id`` of the repository
        return: (osid.repository.CompositionLookupSession) - the new
                ``CompositionLookupSession``
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``repository_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_composition_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_composition_lookup()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.repository.CompositionLookupSession


    def get_composition_query_session(self):
        """Gets a composition query session.

        return: (osid.repository.CompositionQuerySession) - a
                ``CompositionQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_composition_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_composition_query()`` is ``true``.*

        """
        return # osid.repository.CompositionQuerySession

    composition_query_session = property(fget=get_composition_query_session)


    def get_composition_query_session_for_repository(self, repository_id):
        """Gets a composition query session for the given repository.

        arg:    repository_id (osid.id.Id): the ``Id`` of the repository
        return: (osid.repository.CompositionQuerySession) - a
                ``CompositionQuerySession``
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``repository_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_composition_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_composition_query()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.repository.CompositionQuerySession


    def get_composition_search_session(self):
        """Gets a composition search session.

        return: (osid.repository.CompositionSearchSession) - a
                ``CompositionSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_composition_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_composition_search()`` is ``true``.*

        """
        return # osid.repository.CompositionSearchSession

    composition_search_session = property(fget=get_composition_search_session)


    def get_composition_search_session_for_repository(self, repository_id):
        """Gets a composition search session for the given repository.

        arg:    repository_id (osid.id.Id): the ``Id`` of the repository
        return: (osid.repository.CompositionSearchSession) - a
                ``CompositionSearchSession``
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``repository_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_composition_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_composition_search()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.repository.CompositionSearchSession


    def get_composition_admin_session(self):
        """Gets a composition administration session for creating, updating and deleting compositions.

        return: (osid.repository.CompositionAdminSession) - a
                ``CompositionAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_composition_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_composition_admin()`` is ``true``.*

        """
        return # osid.repository.CompositionAdminSession

    composition_admin_session = property(fget=get_composition_admin_session)


    def get_composition_admin_session_for_repository(self, repository_id):
        """Gets a composiiton administrative session for the given repository.

        arg:    repository_id (osid.id.Id): the ``Id`` of the repository
        return: (osid.repository.CompositionAdminSession) - a
                ``CompositionAdminSession``
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``repository_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_composition_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_composition_admin()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.repository.CompositionAdminSession


    def get_composition_notification_session(self, composition_receiver):
        """Gets the notification session for notifications pertaining to composition changes.

        arg:    composition_receiver
                (osid.repository.CompositionReceiver): the notification
                callback
        return: (osid.repository.CompositionNotificationSession) - a
                ``CompositionNotificationSession``
        raise:  NullArgument - ``composition_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_composition_notification()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_composition_notification()`` is ``true``.*

        """
        return # osid.repository.CompositionNotificationSession


    def get_composition_notification_session_for_repository(self, composition_receiver, repository_id):
        """Gets the composition notification session for the given repository.

        arg:    composition_receiver
                (osid.repository.CompositionReceiver): the notification
                callback
        arg:    repository_id (osid.id.Id): the ``Id`` of the repository
        return: (osid.repository.CompositionNotificationSession) - a
                ``CompositionNotificationSession``
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``composition_receiver`` or
                ``repository_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_composition_notification()``
                or ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_composition_notfication()`` and
        ``supports_visible_federation()`` are ``true``.*

        """
        return # osid.repository.CompositionNotificationSession


    def get_composition_repository_session(self):
        """Gets the session for retrieving composition to repository mappings.

        return: (osid.repository.CompositionRepositorySession) - a
                ``CompositionRepositorySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_composition_repository()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_composition_repository()`` is ``true``.*

        """
        return # osid.repository.CompositionRepositorySession

    composition_repository_session = property(fget=get_composition_repository_session)


    def get_composition_repository_assignment_session(self):
        """Gets the session for assigning composition to repository mappings.

        return: (osid.repository.CompositionRepositoryAssignmentSession)
                - a ``CompositionRepositoryAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_composition_repository_assignment()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_composition_repository_assignment()`` is ``true``.*

        """
        return # osid.repository.CompositionRepositoryAssignmentSession

    composition_repository_assignment_session = property(fget=get_composition_repository_assignment_session)


    def get_composition_smart_repository_session(self, repository_id):
        """Gets a composition smart repository session for the given repository.

        arg:    repository_id (osid.id.Id): the ``Id`` of the repository
        return: (osid.repository.CompositionSmartRepositorySession) - a
                ``CompositionSmartRepositorySession``
        raise:  NotFound - ``repository_id`` not found
        raise:  NullArgument - ``repository_id`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented -
                ``supports_composition_smart_repository()``  ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_composition_smart_repository()`` is ``true``.*

        """
        return # osid.repository.CompositionSmartRepositorySession


    def get_repository_lookup_session(self):
        """Gets the repository lookup session.

        return: (osid.repository.RepositoryLookupSession) - a
                ``RepositoryLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_repository_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_repository_lookup()`` is ``true``.*

        """
        return # osid.repository.RepositoryLookupSession

    repository_lookup_session = property(fget=get_repository_lookup_session)


    def get_repository_query_session(self):
        """Gets the repository query session.

        return: (osid.repository.RepositoryQuerySession) - a
                ``RepositoryQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_repository_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_repository_query()`` is ``true``.*

        """
        return # osid.repository.RepositoryQuerySession

    repository_query_session = property(fget=get_repository_query_session)


    def get_repository_search_session(self):
        """Gets the repository search session.

        return: (osid.repository.RepositorySearchSession) - a
                ``RepositorySearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_repository_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_repository_search()`` is ``true``.*

        """
        return # osid.repository.RepositorySearchSession

    repository_search_session = property(fget=get_repository_search_session)


    def get_repository_admin_session(self):
        """Gets the repository administrative session for creating, updating and deleteing repositories.

        return: (osid.repository.RepositoryAdminSession) - a
                ``RepositoryAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_repository_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_repository_admin()`` is ``true``.*

        """
        return # osid.repository.RepositoryAdminSession

    repository_admin_session = property(fget=get_repository_admin_session)


    def get_repository_notification_session(self, repository_receiver):
        """Gets the notification session for subscribing to changes to a repository.

        arg:    repository_receiver
                (osid.repository.RepositoryReceiver): the notification
                callback
        return: (osid.repository.RepositoryNotificationSession) - a
                ``RepositoryNotificationSession``
        raise:  NullArgument - ``repository_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_repository_notification()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_repository_notification()`` is ``true``.*

        """
        return # osid.repository.RepositoryNotificationSession


    def get_repository_hierarchy_session(self):
        """Gets the repository hierarchy traversal session.

        return: (osid.repository.RepositoryHierarchySession) - ``a
                RepositoryHierarchySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_repository_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_repository_hierarchy()`` is ``true``.*

        """
        return # osid.repository.RepositoryHierarchySession

    repository_hierarchy_session = property(fget=get_repository_hierarchy_session)


    def get_repository_hierarchy_design_session(self):
        """Gets the repository hierarchy design session.

        return: (osid.repository.RepositoryHierarchyDesignSession) - a
                ``RepostoryHierarchyDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented -
                ``supports_repository_hierarchy_design()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_repository_hierarchy_design()`` is ``true``.*

        """
        return # osid.repository.RepositoryHierarchyDesignSession

    repository_hierarchy_design_session = property(fget=get_repository_hierarchy_design_session)


    def get_repository_batch_manager(self):
        """Gets a ``RepositoryBatchManager``.

        return: (osid.repository.batch.RepositoryBatchManager) - a
                ``RepostoryBatchManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_repository_batch()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_repository_batch()`` is ``true``.*

        """
        return # osid.repository.batch.RepositoryBatchManager

    repository_batch_manager = property(fget=get_repository_batch_manager)


    def get_repository_rules_manager(self):
        """Gets a ``RepositoryRulesManager``.

        return: (osid.repository.rules.RepositoryRulesManager) - a
                ``RepostoryRulesManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_repository_rules()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_repository_rules()`` is ``true``.*

        """
        return # osid.repository.rules.RepositoryRulesManager

    repository_rules_manager = property(fget=get_repository_rules_manager)


