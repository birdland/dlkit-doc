# -*- coding: utf-8 -*-
"""Repository Open Service Interface Definitions
repository version 3.0.0

The Repository OSID provides the service of finding and managing digital
assets.

Assets

An ``Asset`` represents a unit of content, whether it be an image, a
video, an application document or some text. The Asset defines a core
set of definitions applicable to digital content, such as copyright and
publisher, and allows for a type specification to be appended as with
other ``OsidObjects``.

Asset content, such as a document, is defined such that there may be
multiple formats contained with the same asset. A document may be
accessible in both PDF and MS Word, but is the same document, for
example. An image may have both a large size and a thumbnail version.
Generally, an asset contains more than one version of content when it is
left to the application to decide which is most appropriate.

The ``Asset``  ``Type`` may define methods in common throughout the
content variations. An example asset is one whose content ``Types`` are
"Quicktime" and "MPEG", but the ``Asset``  ``Type`` is "movie" and
defines methods that describe the move aside from the formats. This
"double" Type hierarchy stemming from the asset requires more care in
defining interfaces.

``Assets`` also have "credits" which define the authors, editors,
creators, performers, producers or any other "role", identified with a
role ``Type,`` with the production of the asset. These are managed
externally to the asset through another ``OsidSession``.

Through additional optional ``OsidSessions,`` the ``Asset`` can be
"extended" to offer temporal information. An asset may pertain to a
date, a period of time, or a series of dates and periods. This mechanism
is to offer the ability to search for assets pertaining to a desired
date range without requiring understanding of a ``Type``.

Similarly, the ``Asset`` can also map to spatial information. A
photograph may be "geotagged" with the GPS coordinates where it was
taken, a conical shape in stellar coordinates could be described for an
astronimocal image, or there may be a desire to may a historical book to
the spatial coordinates of Boston and Philadelphia. Unlike temporal
mappings, the definition of the spatial coordinate is left to a spatial
Type to define. The Repository OSID simply manages spatial mappings to
the Asset.

Asset Tagging

``Assets`` may also relate to Ontology OSID ``Subjects``. The
``Subject`` provides the ability to normalize information related to
subject matter across the ``Assets`` to simplify management and provide
a more robust searching mechanism. For example, with a photograph of the
Empire State Building, one may wish to describe that it was designed by
Shreve, Lamb and Harmon and completed in 1931. The information about the
building itself can be described using a ``Subject`` and related to the
photograph, and any other photograph that captures the building. The
``Asset``  ``Type`` for the photograph may simply be "photograph" and
doesn't attempt to describe a building, while the ``AssetContent``
``Type`` is "image/jpeg".

An application performing a search for Empire State Building can be
execute the search over the ``Subjects,`` and once the user has narrowed
the subject area, then the related Assets can be retrieved, and from
there negotiate the content.

A provider wishing to construct a simple inventory database of buildings
in New York may decide to do so using the Resource OSID. The
``Resource``  ``Type`` may describe the construction dates, height,
location, style and architects of buildings. The ``Type`` may also
include a means of getting a reference image using the ``Asset``
interface. Since there is no explicit relationship between ``Subject``
and ``Resource,`` the ``Resource`` can be adapted to the ``Subject``
interface (mapping a ``building_resource_type`` to a
``building_subject_type`` ) to use the same data for ``Subject`` to
``Asset`` mappings and searching.

Asset Compositions

Asset compositions can be created using the ``Composition`` interface. A
``Composition`` is a group of ``Assets`` and compositions may be
structured into a hierarchy for the purpose of "building" larger
content. A content management system may make use of this interface to
construct a web page. The ``Composition`` hierarchy may map into an
XHTML structure and each ``Asset`` represent an image or a link in the
document. However, the produced web page at a given URL may be
represented by another single ``Asset`` that whose content has both the
URL and the XHTML stream.

Another example is an IMS Common Cartridge. The ``Composition`` may be
used to produce the zip file cartridge, but consumers may access the zip
file via an ``Asset`` .

Repository Cataloging

Finally, ``Assets`` and ``Compositions`` may be categorized into
``Repository`` objects. A ``Repository`` is a catalog-like interface to
help organize assets and subject matter. Repositories may be organized
into hierarchies for organization or federation purposes.

This number of service aspects to this Repository OSID produce a large
number of definitions. It is recommended to use the
``RepositoryManager`` definition to select a single ``OsidSession`` of
interest, and work that definition through its dependencies before
tackling another aspect.

Sub Packages

The Repository OSID includes a rules subpackage for managing dynamic
compositions.

"""
from ..osid import managers as osid_managers
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class RepositoryProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_asset_lookup(self):
        """Tests if asset lookup is supported.

        :return: ``true`` if asset lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_asset_query(self):
        """Tests if asset query is supported.

        :return: ``true`` if asset query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_asset_search(self):
        """Tests if asset search is supported.

        :return: ``true`` if asset search is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_asset_admin(self):
        """Tests if asset administration is supported.

        :return: ``true`` if asset administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_asset_notification(self):
        """Tests if asset notification is supported.
        A repository may send messages when assets are created,
        modified, or deleted.

        :return: ``true`` if asset notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_asset_repository(self):
        """Tests if retrieving mappings of assets and repositories is supported.

        :return: ``true`` if asset repository mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_asset_repository_assignment(self):
        """Tests if managing mappings of assets and repositories is supported.

        :return: ``true`` if asset repository assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_asset_smart_repository(self):
        """Tests if asset smart repository is supported.

        :return: ``true`` if asset smart repository is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_asset_temporal(self):
        """Tests if retrieving mappings of assets and time coverage is supported.

        :return: ``true`` if asset temporal mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_asset_temporal_assignment(self):
        """Tests if managing mappings of assets and time ocverage is supported.

        :return: ``true`` if asset temporal assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_asset_spatial(self):
        """Tests if retrieving mappings of assets and spatial coverage is supported.

        :return: ``true`` if asset spatial mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_asset_spatial_assignment(self):
        """Tests if managing mappings of assets and spatial ocverage is supported.

        :return: ``true`` if asset spatial assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_asset_composition(self):
        """Tests if assets are included in compositions.

        :return: ``true`` if asset composition supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_asset_composition_design(self):
        """Tests if mapping assets to compositions is supported.

        :return: ``true`` if designing asset compositions is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_composition_lookup(self):
        """Tests if composition lookup is supported.

        :return: ``true`` if composition lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_composition_query(self):
        """Tests if composition query is supported.

        :return: ``true`` if composition query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_composition_search(self):
        """Tests if composition search is supported.

        :return: ``true`` if composition search is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_composition_admin(self):
        """Tests if composition administration is supported.

        :return: ``true`` if composition administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_composition_notification(self):
        """Tests if composition notification is supported.

        :return: ``true`` if composition notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_composition_repository(self):
        """Tests if retrieval of composition to repository mappings is supported.

        :return: ``true`` if composition to repository mapping is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_composition_repository_assignment(self):
        """Tests if assigning composition to repository mappings is supported.

        :return: ``true`` if composition to repository assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_composition_smart_repository(self):
        """Tests if composition smart repository is supported.

        :return: ``true`` if composition smart repository is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_repository_lookup(self):
        """Tests if repository lookup is supported.

        :return: ``true`` if repository lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_repository_query(self):
        """Tests if repository query is supported.

        :return: ``true`` if repository query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_repository_search(self):
        """Tests if repository search is supported.

        :return: ``true`` if repository search is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_repository_admin(self):
        """Tests if repository administration is supported.

        :return: ``true`` if repository administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_repository_notification(self):
        """Tests if repository notification is supported.
        Messages may be sent when ``Repository`` objects are created,
        deleted or updated. Notifications for assets within repositories
        are sent via the asset notification session.

        :return: ``true`` if repository notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_repository_hierarchy(self):
        """Tests if a repository hierarchy traversal is supported.

        :return: ``true`` if a repository hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_repository_hierarchy_design(self):
        """Tests if a repository hierarchy design is supported.

        :return: ``true`` if a repository hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_repository_batch(self):
        """Tests if a repository batch service is supported.

        :return: ``true`` if a repository batch service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_repository_rules(self):
        """Tests if a repository rules service is supported.

        :return: ``true`` if a repository rules service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_asset_record_types(self):
        """Gets all the asset record types supported.

        :return: the list of supported asset record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    asset_record_types = property(fget=get_asset_record_types)

    def supports_asset_record_type(self, asset_record_type):
        """Tests if a given asset type is supported.

        :param asset_record_type: the asset record type
        :type asset_record_type: ``osid.type.Type``
        :return: ``true`` if the asset record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``asset_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_asset_search_record_types(self):
        """Gets all the asset search record types supported.

        :return: the list of supported asset search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    asset_search_record_types = property(fget=get_asset_search_record_types)

    def supports_asset_search_record_type(self, asset_search_record_type):
        """Tests if a given asset search record type is supported.

        :param asset_search_record_type: the asset search record type
        :type asset_search_record_type: ``osid.type.Type``
        :return: ``true`` if the asset search record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``asset_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_asset_content_record_types(self):
        """Gets all the asset content record types supported.

        :return: the list of supported asset content record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    asset_content_record_types = property(fget=get_asset_content_record_types)

    def supports_asset_content_record_type(self, asset_content_record_type):
        """Tests if a given asset content record type is supported.

        :param asset_content_record_type: the asset content record type
        :type asset_content_record_type: ``osid.type.Type``
        :return: ``true`` if the asset content record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``asset_content_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_composition_record_types(self):
        """Gets all the composition record types supported.

        :return: the list of supported composition record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    composition_record_types = property(fget=get_composition_record_types)

    def supports_composition_record_type(self, composition_record_type):
        """Tests if a given composition record type is supported.

        :param composition_record_type: the composition record type
        :type composition_record_type: ``osid.type.Type``
        :return: ``true`` if the composition record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``composition_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_composition_search_record_types(self):
        """Gets all the composition search record types supported.

        :return: the list of supported composition search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    composition_search_record_types = property(fget=get_composition_search_record_types)

    def supports_composition_search_record_type(self, composition_search_record_type):
        """Tests if a given composition search record type is supported.

        :param composition_search_record_type: the composition serach type
        :type composition_search_record_type: ``osid.type.Type``
        :return: ``true`` if the composition search record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``composition_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_repository_record_types(self):
        """Gets all the repository record types supported.

        :return: the list of supported repository record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    repository_record_types = property(fget=get_repository_record_types)

    def supports_repository_record_type(self, repository_record_type):
        """Tests if a given repository record type is supported.

        :param repository_record_type: the repository record type
        :type repository_record_type: ``osid.type.Type``
        :return: ``true`` if the repository record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``repository_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_repository_search_record_types(self):
        """Gets all the repository search record types supported.

        :return: the list of supported repository search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    repository_search_record_types = property(fget=get_repository_search_record_types)

    def supports_repository_search_record_type(self, repository_search_record_type):
        """Tests if a given repository search record type is supported.

        :param repository_search_record_type: the repository search type
        :type repository_search_record_type: ``osid.type.Type``
        :return: ``true`` if the repository search record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``repository_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_spatial_unit_record_types(self):
        """Gets all the spatial unit record types supported.

        :return: the list of supported spatial unit record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    spatial_unit_record_types = property(fget=get_spatial_unit_record_types)

    def supports_spatial_unit_record_type(self, spatial_unit_record_type):
        """Tests if a given spatial unit record type is supported.

        :param spatial_unit_record_type: the spatial unit record type
        :type spatial_unit_record_type: ``osid.type.Type``
        :return: ``true`` if the spatial unit record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``spatial_unit_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_coordinate_types(self):
        """Gets all the coordinate types supported.

        :return: the list of supported coordinate types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    coordinate_types = property(fget=get_coordinate_types)

    def supports_coordinate_type(self, coordinate_type):
        """Tests if a given coordinate type is supported.

        :param coordinate_type: the coordinate type
        :type coordinate_type: ``osid.type.Type``
        :return: ``true`` if the coordinate type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``coordinate_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class RepositoryManager(osid_managers.OsidManager, osid_sessions.OsidSession, RepositoryProfile):

    def get_asset_lookup_session(self):
        """Gets the ``OsidSession`` associated with the asset lookup service.

        :return: the new ``AssetLookupSession``
        :rtype: ``osid.repository.AssetLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    asset_lookup_session = property(fget=get_asset_lookup_session)

    def get_asset_lookup_session_for_repository(self, repository_id):
        """Gets the ``OsidSession`` associated with the asset lookup service for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: the new ``AssetLookupSession``
        :rtype: ``osid.repository.AssetLookupSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_query_session(self):
        """Gets an asset query session.

        :return: an ``AssetQuerySession``
        :rtype: ``osid.repository.AssetQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    asset_query_session = property(fget=get_asset_query_session)

    def get_asset_query_session_for_repository(self, repository_id):
        """Gets an asset query session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetQuerySession``
        :rtype: ``osid.repository.AssetQuerySession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_search_session(self):
        """Gets an asset search session.

        :return: an ``AssetSearchSession``
        :rtype: ``osid.repository.AssetSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    asset_search_session = property(fget=get_asset_search_session)

    def get_asset_search_session_for_repository(self, repository_id):
        """Gets an asset search session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetSearchSession``
        :rtype: ``osid.repository.AssetSearchSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_admin_session(self):
        """Gets an asset administration session for creating, updating and deleting assets.

        :return: an ``AssetAdminSession``
        :rtype: ``osid.repository.AssetAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    asset_admin_session = property(fget=get_asset_admin_session)

    def get_asset_admin_session_for_repository(self, repository_id):
        """Gets an asset administration session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetAdminSession``
        :rtype: ``osid.repository.AssetAdminSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_notification_session(self, asset_receiver):
        """Gets the notification session for notifications pertaining to asset changes.

        :param asset_receiver: the notification callback
        :type asset_receiver: ``osid.repository.AssetReceiver``
        :return: an ``AssetNotificationSession``
        :rtype: ``osid.repository.AssetNotificationSession``
        :raise: ``NullArgument`` -- ``asset_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_notification_session_for_repository(self, asset_receiver, repository_id):
        """Gets the asset notification session for the given repository.

        :param asset_receiver: the notification callback
        :type asset_receiver: ``osid.repository.AssetReceiver``
        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetNotificationSession``
        :rtype: ``osid.repository.AssetNotificationSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``asset_receiver`` or ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_repository_session(self):
        """Gets the session for retrieving asset to repository mappings.

        :return: an ``AssetRepositorySession``
        :rtype: ``osid.repository.AssetRepositorySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_repository()`` is ``false``

        """
        raise UNIMPLEMENTED()

    asset_repository_session = property(fget=get_asset_repository_session)

    def get_asset_repository_assignment_session(self):
        """Gets the session for assigning asset to repository mappings.

        :return: an ``AssetRepositoryAsignmentSession``
        :rtype: ``osid.repository.AssetRepositoryAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_repository_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    asset_repository_assignment_session = property(fget=get_asset_repository_assignment_session)

    def get_asset_smart_repository_session(self, repository_id):
        """Gets an asset smart repository session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetSmartRepositorySession``
        :rtype: ``osid.repository.AssetSmartRepositorySession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_smart_repository()``  ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_temporal_session(self):
        """Gets the session for retrieving temporal coverage of an asset.

        :return: an ``AssetTemporalSession``
        :rtype: ``osid.repository.AssetTemporalSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_temporal()`` is ``false``

        """
        raise UNIMPLEMENTED()

    asset_temporal_session = property(fget=get_asset_temporal_session)

    def get_asset_temporal_session_for_repository(self, repository_id):
        """Gets the session for retrieving temporal coverage of an asset for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetTemporalSession``
        :rtype: ``osid.repository.AssetTemporalSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_temporal()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_temporal_assignment_session(self):
        """Gets the session for assigning temporal coverage to an asset.

        :return: an ``AssetTemporalAssignmentSession``
        :rtype: ``osid.repository.AssetTemporalAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_temporal_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    asset_temporal_assignment_session = property(fget=get_asset_temporal_assignment_session)

    def get_asset_temporal_assignment_session_for_repository(self, repository_id):
        """Gets the session for assigning temporal coverage of an asset for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetTemporalAssignmentSession``
        :rtype: ``osid.repository.AssetTemporalAssignmentSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_temporal_assignment()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_spatial_session(self):
        """Gets the session for retrieving spatial coverage of an asset.

        :return: an ``AssetSpatialSession``
        :rtype: ``osid.repository.AssetSpatialSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_spatial_assets()`` is ``false``

        """
        raise UNIMPLEMENTED()

    asset_spatial_session = property(fget=get_asset_spatial_session)

    def get_asset_spatial_session_for_repository(self, repository_id):
        """Gets the session for retrieving spatial coverage of an asset for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetSpatialSession``
        :rtype: ``osid.repository.AssetSpatialSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_spatial()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_spatial_assignment_session(self):
        """Gets the session for assigning spatial coverage to an asset.

        :return: an ``AssetSpatialAssignmentSession``
        :rtype: ``osid.repository.AssetSpatialAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_spatial_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    asset_spatial_assignment_session = property(fget=get_asset_spatial_assignment_session)

    def get_asset_spatial_assignment_session_for_repository(self, repository_id):
        """Gets the session for assigning spatial coverage of an asset for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: an ``AssetSpatialAssignmentSession``
        :rtype: ``osid.repository.AssetSpatialAssignmentSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_spatial_assignment()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_composition_session(self):
        """Gets the session for retrieving asset compositions.

        :return: an ``AssetCompositionSession``
        :rtype: ``osid.repository.AssetCompositionSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_composition()`` is ``false``

        """
        raise UNIMPLEMENTED()

    asset_composition_session = property(fget=get_asset_composition_session)

    def get_asset_composition_design_session(self):
        """Gets the session for creating asset compositions.

        :return: an ``AssetCompositionDesignSession``
        :rtype: ``osid.repository.AssetCompositionDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_composition_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    asset_composition_design_session = property(fget=get_asset_composition_design_session)

    def get_composition_lookup_session(self):
        """Gets the ``OsidSession`` associated with the composition lookup service.

        :return: the new ``CompositionLookupSession``
        :rtype: ``osid.repository.CompositionLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    composition_lookup_session = property(fget=get_composition_lookup_session)

    def get_composition_lookup_session_for_repository(self, repository_id):
        """Gets the ``OsidSession`` associated with the composition lookup service for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: the new ``CompositionLookupSession``
        :rtype: ``osid.repository.CompositionLookupSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_query_session(self):
        """Gets a composition query session.

        :return: a ``CompositionQuerySession``
        :rtype: ``osid.repository.CompositionQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    composition_query_session = property(fget=get_composition_query_session)

    def get_composition_query_session_for_repository(self, repository_id):
        """Gets a composition query session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: a ``CompositionQuerySession``
        :rtype: ``osid.repository.CompositionQuerySession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_search_session(self):
        """Gets a composition search session.

        :return: a ``CompositionSearchSession``
        :rtype: ``osid.repository.CompositionSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    composition_search_session = property(fget=get_composition_search_session)

    def get_composition_search_session_for_repository(self, repository_id):
        """Gets a composition search session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: a ``CompositionSearchSession``
        :rtype: ``osid.repository.CompositionSearchSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_admin_session(self):
        """Gets a composition administration session for creating, updating and deleting compositions.

        :return: a ``CompositionAdminSession``
        :rtype: ``osid.repository.CompositionAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    composition_admin_session = property(fget=get_composition_admin_session)

    def get_composition_admin_session_for_repository(self, repository_id):
        """Gets a composiiton administrative session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: a ``CompositionAdminSession``
        :rtype: ``osid.repository.CompositionAdminSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_notification_session(self, composition_receiver):
        """Gets the notification session for notifications pertaining to composition changes.

        :param composition_receiver: the notification callback
        :type composition_receiver: ``osid.repository.CompositionReceiver``
        :return: a ``CompositionNotificationSession``
        :rtype: ``osid.repository.CompositionNotificationSession``
        :raise: ``NullArgument`` -- ``composition_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_notification_session_for_repository(self, composition_receiver, repository_id):
        """Gets the composition notification session for the given repository.

        :param composition_receiver: the notification callback
        :type composition_receiver: ``osid.repository.CompositionReceiver``
        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: a ``CompositionNotificationSession``
        :rtype: ``osid.repository.CompositionNotificationSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``composition_receiver`` or ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_repository_session(self):
        """Gets the session for retrieving composition to repository mappings.

        :return: a ``CompositionRepositorySession``
        :rtype: ``osid.repository.CompositionRepositorySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_repository()`` is ``false``

        """
        raise UNIMPLEMENTED()

    composition_repository_session = property(fget=get_composition_repository_session)

    def get_composition_repository_assignment_session(self):
        """Gets the session for assigning composition to repository mappings.

        :return: a ``CompositionRepositoryAssignmentSession``
        :rtype: ``osid.repository.CompositionRepositoryAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_repository_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    composition_repository_assignment_session = property(fget=get_composition_repository_assignment_session)

    def get_composition_smart_repository_session(self, repository_id):
        """Gets a composition smart repository session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :return: a ``CompositionSmartRepositorySession``
        :rtype: ``osid.repository.CompositionSmartRepositorySession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_smart_repository()``  ``false``

        """
        raise UNIMPLEMENTED()

    def get_repository_lookup_session(self):
        """Gets the repository lookup session.

        :return: a ``RepositoryLookupSession``
        :rtype: ``osid.repository.RepositoryLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    repository_lookup_session = property(fget=get_repository_lookup_session)

    def get_repository_query_session(self):
        """Gets the repository query session.

        :return: a ``RepositoryQuerySession``
        :rtype: ``osid.repository.RepositoryQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    repository_query_session = property(fget=get_repository_query_session)

    def get_repository_search_session(self):
        """Gets the repository search session.

        :return: a ``RepositorySearchSession``
        :rtype: ``osid.repository.RepositorySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    repository_search_session = property(fget=get_repository_search_session)

    def get_repository_admin_session(self):
        """Gets the repository administrative session for creating, updating and deleteing repositories.

        :return: a ``RepositoryAdminSession``
        :rtype: ``osid.repository.RepositoryAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    repository_admin_session = property(fget=get_repository_admin_session)

    def get_repository_notification_session(self, repository_receiver):
        """Gets the notification session for subscribing to changes to a repository.

        :param repository_receiver: the notification callback
        :type repository_receiver: ``osid.repository.RepositoryReceiver``
        :return: a ``RepositoryNotificationSession``
        :rtype: ``osid.repository.RepositoryNotificationSession``
        :raise: ``NullArgument`` -- ``repository_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_repository_hierarchy_session(self):
        """Gets the repository hierarchy traversal session.

        :return: ``a RepositoryHierarchySession``
        :rtype: ``osid.repository.RepositoryHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    repository_hierarchy_session = property(fget=get_repository_hierarchy_session)

    def get_repository_hierarchy_design_session(self):
        """Gets the repository hierarchy design session.

        :return: a ``RepostoryHierarchyDesignSession``
        :rtype: ``osid.repository.RepositoryHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    repository_hierarchy_design_session = property(fget=get_repository_hierarchy_design_session)

    def get_repository_batch_manager(self):
        """Gets a ``RepositoryBatchManager``.

        :return: a ``RepostoryBatchManager``
        :rtype: ``osid.repository.batch.RepositoryBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    repository_batch_manager = property(fget=get_repository_batch_manager)

    def get_repository_rules_manager(self):
        """Gets a ``RepositoryRulesManager``.

        :return: a ``RepostoryRulesManager``
        :rtype: ``osid.repository.rules.RepositoryRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_rules()`` is ``false``

        """
        raise UNIMPLEMENTED()

    repository_rules_manager = property(fget=get_repository_rules_manager)


##
# The following methods are from osid.repository.RepositoryLookupSession

    def can_lookup_repositories(self):
        """Tests if this user can perform ``Repository`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_repository_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_repository_view(self):
        """A complete view of the ``Repository`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_repository(self, repository_id):
        """Gets the ``Repository`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Repository`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Repository`` and retained
        for compatibility.

        :param repository_id: ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: the repository
        :rtype: ``osid.repository.Repository``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_repositories_by_ids(self, repository_ids):
        """Gets a ``RepositoryList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the
        repositories specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Repositories`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param repository_ids: the list of ``Ids`` to retrieve
        :type repository_ids: ``osid.id.IdList``
        :return: the returned ``Repository list``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``repository_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_repositories_by_genus_type(self, repository_genus_type):
        """Gets a ``RepositoryList`` corresponding to the given repository genus ``Type`` which does not include repositories of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :param repository_genus_type: a repository genus type
        :type repository_genus_type: ``osid.type.Type``
        :return: the returned ``Repository list``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NullArgument`` -- ``repository_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_repositories_by_parent_genus_type(self, repository_genus_type):
        """Gets a ``RepositoryList`` corresponding to the given repository genus ``Type`` and include any additional repositories with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :param repository_genus_type: a repository genus type
        :type repository_genus_type: ``osid.type.Type``
        :return: the returned ``Repository list``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NullArgument`` -- ``repository_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_repositories_by_record_type(self, repository_record_type):
        """Gets a ``RepositoryList`` containing the given repository record ``Type``.
        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :param repository_record_type: a repository record type
        :type repository_record_type: ``osid.type.Type``
        :return: the returned ``Repository list``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NullArgument`` -- ``repository_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_repositories_by_provider(self, resource_id):
        """Gets a ``RepositoryList`` from the given provider ````.
        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Repository list``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_repositories(self):
        """Gets all ``Repositories``.
        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :return: a list of ``Repositories``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    repositories = property(fget=get_repositories)


##
# The following methods are from osid.repository.RepositoryQuerySession

    def can_search_repositories(self):
        """Tests if this user can perform ``Repository`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_repository_query(self):
        """Gets a repository query.

        :return: the repository query
        :rtype: ``osid.repository.RepositoryQuery``

        """
        raise UNIMPLEMENTED()

    repository_query = property(fget=get_repository_query)

    def get_repositories_by_query(self, repository_query):
        """Gets a list of ``Repositories`` matching the given repository query.

        :param repository_query: the repository query
        :type repository_query: ``osid.repository.RepositoryQuery``
        :return: the returned ``RepositoryList``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NullArgument`` -- ``repository_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``repository_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.RepositorySearchSession

    def get_repository_search(self):
        """Gets a repository search.

        :return: the repository search
        :rtype: ``osid.repository.RepositorySearch``

        """
        raise UNIMPLEMENTED()

    repository_search = property(fget=get_repository_search)

    def get_repository_search_order(self):
        """Gets a repository search order.
        The ``RepositorySearchOrder`` is supplied to a
        ``RepositorySearch`` to specify the ordering of results.

        :return: the repository search order
        :rtype: ``osid.repository.RepositorySearchOrder``

        """
        raise UNIMPLEMENTED()

    repository_search_order = property(fget=get_repository_search_order)

    def get_repositories_by_search(self, repository_query, repository_search):
        """Gets the search results matching the given search query using the given search.

        :param repository_query: the repository query
        :type repository_query: ``osid.repository.RepositoryQuery``
        :param repository_search: the repository search
        :type repository_search: ``osid.repository.RepositorySearch``
        :return: the repository search results
        :rtype: ``osid.repository.RepositorySearchResults``
        :raise: ``NullArgument`` -- ``repository_query`` or ``repository_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``repository_query`` or ``repository_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_repository_query_from_inspector(self, repository_query_inspector):
        """Gets a repository query from an inspector.
        The inspector is available from a ``RepositorySearchResults``.

        :param repository_query_inspector: a repository query inspector
        :type repository_query_inspector: ``osid.repository.RepositoryQueryInspector``
        :return: the repository query
        :rtype: ``osid.repository.RepositoryQuery``
        :raise: ``NullArgument`` -- ``repository_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``repository_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.RepositoryAdminSession

    def can_create_repositories(self):
        """Tests if this user can create ``Repositories``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Repository`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_repository_with_record_types(self, repository_record_types):
        """Tests if this user can create a single ``Repository`` using the desired record types.
        While ``RepositoryManager.getRepositoryRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Repository``. Providing an empty array tests if a
        ``Repository`` can be created with no records.

        :param repository_record_types: array of repository record types
        :type repository_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Repository`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``repository_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_repository_form_for_create(self, repository_record_types):
        """Gets the repository form for creating new repositories.
        A new form should be requested for each create transaction.

        :param repository_record_types: array of repository record types
        :type repository_record_types: ``osid.type.Type[]``
        :return: the repository form
        :rtype: ``osid.repository.RepositoryForm``
        :raise: ``NullArgument`` -- ``repository_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_repository(self, repository_form):
        """Creates a new ``Repository``.

        :param repository_form: the form for this ``Repository``
        :type repository_form: ``osid.repository.RepositoryForm``
        :return: the new ``Repository``
        :rtype: ``osid.repository.Repository``
        :raise: ``IllegalState`` -- ``repository_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``repository_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``repository_form`` did not originate from ``get_repository_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_repositories(self):
        """Tests if this user can update ``Repositories``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Repository`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_repository_form_for_update(self, repository_id):
        """Gets the repository form for updating an existing repository.
        A new repository form should be requested for each update
        transaction.

        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: the repository form
        :rtype: ``osid.repository.RepositoryForm``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_repository(self, repository_form):
        """Updates an existing repository.

        :param repository_form: the form containing the elements to be updated
        :type repository_form: ``osid.repository.RepositoryForm``
        :raise: ``IllegalState`` -- ``repository_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``repository_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``repository_form`` did not originate from ``get_repository_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_repositories(self):
        """Tests if this user can delete ``Repositories``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Repository`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_repository(self, repository_id):
        """Deletes a ``Repository``.

        :param repository_id: the ``Id`` of the ``Repository`` to remove
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_repository_aliases(self):
        """Tests if this user can manage ``Id`` aliases for repositories.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Repository`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_repository(self, repository_id, alias_id):
        """Adds an ``Id`` to a ``Repository`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Repository`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another repository, it is reassigned
        to the given repository ``Id``.

        :param repository_id: the ``Id`` of a ``Repository``
        :type repository_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.RepositoryNotificationSession

    def can_register_for_repository_notifications(self):
        """Tests if this user can register for ``Repository`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_repositories(self):
        """Register for notifications of new repositories.
        ``RepositoryReceiver.newRepository()`` is invoked when a new
        ``Repository`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_repository_ancestors(self, repository_id):
        """Registers for notification if an ancestor is added to the specified repository in the repository hierarchy.
        ``RepositoryReceiver.newRepositoryAncestor()`` is invoked when
        the specified repository experiences an addition in ancestry.

        :param repository_id: the ``Id`` of the repository to monitor
        :type repository_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_repository_descendants(self, repository_id):
        """Registers for notification if a descendant is added to the specified repository in the repository hierarchy.
        ``RepositoryReceiver.newRepositoryDescendant()`` is invoked when
        the specified repository experiences an addition in descendants.

        :param repository_id: the ``Id`` of the repository to monitor
        :type repository_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_repositories(self):
        """Registers for notification of updated repositories.
        ``RepositoryReceiver.changedRepository()`` is invoked when a
        repository is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_repository(self, repository_id):
        """Registers for notification of an updated repository.
        ``RepositoryReceiver.changedRepository()`` is invoked when the
        specified repository is changed.

        :param repository_id: the ``Id`` of the ``Repository`` to monitor
        :type repository_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_repositories(self):
        """Registers for notification of deleted repositories.
        ``RepositoryReceiver.deletedRepository()`` is invoked when a
        repository is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_repository(self, repository_id):
        """Registers for notification of a deleted repository.
        ``RepositoryReceiver.deletedRepository()`` is invoked when the
        specified repository is deleted.

        :param repository_id: the ``Id`` of the ``Repository`` to monitor
        :type repository_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_repository_ancestors(self, repository_id):
        """Registers for notification if an ancestor is removed from the specified repository in the repository hierarchy.
        ``RepositoryReceiver.deletedRepositoryAncestor()`` is invoked
        when the specified repository experiences a removal of an
        ancestor.

        :param repository_id: the ``Id`` of the repository to monitor
        :type repository_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_repository_descendants(self, repository_id):
        """Registers for notification if a descendant is removed from fthe specified repository in the repository hierarchy.
        ``RepositoryReceiver.deletedRepositoryDescednant()`` is invoked
        when the specified repository experiences a removal of one of
        its descdendents.

        :param repository_id: the ``Id`` of the repository to monitor
        :type repository_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.RepositoryHierarchySession

    def get_repository_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    repository_hierarchy_id = property(fget=get_repository_hierarchy_id)

    def get_repository_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    repository_hierarchy = property(fget=get_repository_hierarchy)

    def can_access_repository_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_repository_ids(self):
        """Gets the root repository ``Ids`` in this hierarchy.

        :return: the root repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_repository_ids = property(fget=get_root_repository_ids)

    def get_root_repositories(self):
        """Gets the root repositories in the repository hierarchy.
        A node with no parents is an orphan. While all repository
        ``Ids`` are known to the hierarchy, an orphan does not appear in
        the hierarchy unless explicitly added as a root node or child of
        another node.

        :return: the root repositories
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_repositories = property(fget=get_root_repositories)

    def has_parent_repositories(self, repository_id):
        """Tests if the ``Repository`` has any parents.

        :param repository_id: a repository ``Id``
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if the repository has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_repository(self, id_, repository_id):
        """Tests if an ``Id`` is a direct parent of a repository.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``repository_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_repository_ids(self, repository_id):
        """Gets the parent ``Ids`` of the given repository.

        :param repository_id: a repository ``Id``
        :type repository_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the repository
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_repositories(self, repository_id):
        """Gets the parents of the given repository.

        :param repository_id: the ``Id`` to query
        :type repository_id: ``osid.id.Id``
        :return: the parents of the repository
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_repository(self, id_, repository_id):
        """Tests if an ``Id`` is an ancestor of a repository.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param repository_id: the Id of a repository
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``repository_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_repositories(self, repository_id):
        """Tests if a repository has any children.

        :param repository_id: a repository ``Id``
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if the ``repository_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_repository(self, id_, repository_id):
        """Tests if a node is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``repository_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_repository_ids(self, repository_id):
        """Gets the ``Ids`` of the children of the given repository.

        :param repository_id: the ``Id`` to query
        :type repository_id: ``osid.id.Id``
        :return: the children of the repository
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_repositories(self, repository_id):
        """Gets the children of the given repository.

        :param repository_id: the ``Id`` to query
        :type repository_id: ``osid.id.Id``
        :return: the children of the repository
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_repository(self, id_, repository_id):
        """Tests if an ``Id`` is a descendant of a repository.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``repository_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_repository_node_ids(self, repository_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given repository.

        :param repository_id: the ``Id`` to query
        :type repository_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: the specified repository node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_repository_nodes(self, repository_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given repository.

        :param repository_id: the ``Id`` to query
        :type repository_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: the specified repository node
        :rtype: ``osid.repository.RepositoryNode``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.RepositoryHierarchyDesignSession

    def can_modify_repository_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_repository(self, repository_id):
        """Adds a root repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``repository_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_repository(self, repository_id):
        """Removes a root repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not a root
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_repository(self, repository_id, child_id):
        """Adds a child to a repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``repository_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``repository_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_repository(self, repository_id, child_id):
        """Removes a child from a repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``repository_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_repositories(self, repository_id):
        """Removes all children from a repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class RepositoryProxyManager(osid_managers.OsidProxyManager, RepositoryProfile):

    def get_asset_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the asset lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetLookupSession``
        :rtype: ``osid.repository.AssetLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_lookup_session_for_repository(self, repository_id, proxy):
        """Gets the ``OsidSession`` associated with the asset lookup service for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetLookupSession``
        :rtype: ``osid.repository.AssetLookupSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the asset query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetQuerySession``
        :rtype: ``osid.repository.AssetQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_query_session_for_repository(self, repository_id, proxy):
        """Gets the ``OsidSession`` associated with the asset query service for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetQuerySession``
        :rtype: ``osid.repository.AssetQuerySession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_search_session(self, proxy):
        """Gets an asset search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetSearchSession``
        :rtype: ``osid.repository.AssetSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_search_session_for_repository(self, repository_id, proxy):
        """Gets an asset search session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetSearchSession``
        :rtype: ``osid.repository.AssetSearchSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_admin_session(self, proxy):
        """Gets an asset administration session for creating, updating and deleting assets.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetAdminSession``
        :rtype: ``osid.repository.AssetAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_admin_session_for_repository(self, repository_id, proxy):
        """Gets an asset administration session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetAdminSession``
        :rtype: ``osid.repository.AssetAdminSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_notification_session(self, asset_receiver, proxy):
        """Gets the notification session for notifications pertaining to asset changes.

        :param asset_receiver: the notification callback
        :type asset_receiver: ``osid.repository.AssetReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetNotificationSession``
        :rtype: ``osid.repository.AssetNotificationSession``
        :raise: ``NullArgument`` -- ``asset_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_notification_session_for_repository(self, asset_receiver, repository_id, proxy):
        """Gets the asset notification session for the given repository.

        :param asset_receiver: the notification callback
        :type asset_receiver: ``osid.repository.AssetReceiver``
        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetNotificationSession``
        :rtype: ``osid.repository.AssetNotificationSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``asset_receiver, repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_repository_session(self, proxy):
        """Gets the session for retrieving asset to repository mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetRepositorySession``
        :rtype: ``osid.repository.AssetRepositorySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_repository()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_repository_assignment_session(self, proxy):
        """Gets the session for assigning asset to repository mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetRepositoryAsignmentSession``
        :rtype: ``osid.repository.AssetRepositoryAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_repository_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_smart_repository_session(self, repository_id, proxy):
        """Gets an asset smart repository session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetSmartRepositorySession``
        :rtype: ``osid.repository.AssetSmartRepositorySession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_asset_smart_repository()``  ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_temporal_session(self, proxy):
        """Gets the session for retrieving temporal coverage of an asset.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetTemporalSession``
        :rtype: ``osid.repository.AssetTemporalSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_temporal()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_temporal_session_for_repository(self, repository_id, proxy):
        """Gets the session for retrieving temporal coverage of an asset for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetTemporalSession``
        :rtype: ``osid.repository.AssetTemporalSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_temporal()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_temporal_assignment_session(self, proxy):
        """Gets the session for assigning temporal coverage to an asset.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetTemporalAssignmentSession``
        :rtype: ``osid.repository.AssetTemporalAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_temporal_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_temporal_assignment_session_for_repository(self, repository_id, proxy):
        """Gets the session for assigning temporal coverage of an asset for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetTemporalAssignmentSession``
        :rtype: ``osid.repository.AssetTemporalAssignmentSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_temporal_assignment()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_spatial_session(self, proxy):
        """Gets the session for retrieving spatial coverage of an asset.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetSpatialSession``
        :rtype: ``osid.repository.AssetSpatialSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_spatial_assets()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_spatial_session_for_repository(self, repository_id, proxy):
        """Gets the session for retrieving spatial coverage of an asset for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetSpatialSession``
        :rtype: ``osid.repository.AssetSpatialSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_spatial()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_spatial_assignment_session(self, proxy):
        """Gets the session for assigning spatial coverage to an asset.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetSpatialAssignmentSession``
        :rtype: ``osid.repository.AssetSpatialAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_spatial_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_spatial_assignment_session_for_repository(self, repository_id, proxy):
        """Gets the session for assigning spatial coverage of an asset for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetSpatialAssignmentSession``
        :rtype: ``osid.repository.AssetSpatialAssignmentSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_spatial_assignment()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_composition_session(self, proxy):
        """Gets the session for retrieving asset compositions.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetCompositionSession``
        :rtype: ``osid.repository.AssetCompositionSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_composition()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_asset_composition_design_session(self, proxy):
        """Gets the session for creating asset compositions.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AssetCompositionDesignSession``
        :rtype: ``osid.repository.AssetCompositionDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_asset_composition_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the composition lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: the new ``CompositionLookupSession``
        :rtype: ``osid.repository.CompositionLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_lookup_session_for_repository(self, repository_id, proxy):
        """Gets the ``OsidSession`` associated with the composition lookup service for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: the new ``CompositionLookupSession``
        :rtype: ``osid.repository.CompositionLookupSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_query_session(self, proxy):
        """Gets a composition query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionQuerySession``
        :rtype: ``osid.repository.CompositionSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_query_session_for_repository(self, repository_id, proxy):
        """Gets a composition query session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionQuerySession``
        :rtype: ``osid.repository.CompositionQuerySession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_search_session(self, proxy):
        """Gets a composition search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionSearchSession``
        :rtype: ``osid.repository.CompositionSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_search_session_for_repository(self, repository_id, proxy):
        """Gets a composition search session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionSearchSession``
        :rtype: ``osid.repository.CompositionSearchSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_admin_session(self, proxy):
        """Gets a composition administration session for creating, updating and deleting compositions.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionAdminSession``
        :rtype: ``osid.repository.CompositionAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_admin_session_for_repository(self, repository_id, proxy):
        """Gets a composiiton administrative session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionAdminSession``
        :rtype: ``osid.repository.CompositionAdminSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_notification_session(self, composition_receiver, proxy):
        """Gets the notification session for notifications pertaining to composition changes.

        :param composition_receiver: the notification callback
        :type composition_receiver: ``osid.repository.CompositionReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionNotificationSession``
        :rtype: ``osid.repository.CompositionNotificationSession``
        :raise: ``NullArgument`` -- ``composition_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_notification_session_for_repository(self, composition_receiver, repository_id, proxy):
        """Gets the composition notification session for the given repository.

        :param composition_receiver: the notification callback
        :type composition_receiver: ``osid.repository.CompositionReceiver``
        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionNotificationSession``
        :rtype: ``osid.repository.CompositionNotificationSession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``composition_receiver, repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_repository_session(self, proxy):
        """Gets the session for retrieving composition to repository mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionRepositorySession``
        :rtype: ``osid.repository.CompositionRepositorySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_repository()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_repository_assignment_session(self, proxy):
        """Gets the session for assigning composition to repository mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionRepositoryAssignmentSession``
        :rtype: ``osid.repository.CompositionRepositoryAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_composition_repository_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_composition_smart_repository_session(self, repository_id, proxy):
        """Gets a composition smart repository session for the given repository.

        :param repository_id: the ``Id`` of the repository
        :type repository_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CompositionSmartRepositorySession``
        :rtype: ``osid.repository.CompositionSmartRepositorySession``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_composition_smart_repository()``  ``false``

        """
        raise UNIMPLEMENTED()

    def get_repository_lookup_session(self, proxy):
        """Gets the repository lookup session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RepositoryLookupSession``
        :rtype: ``osid.repository.RepositoryLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_repository_query_session(self, proxy):
        """Gets the repository query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RepositoryQuerySession``
        :rtype: ``osid.repository.RepositoryQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_repository_search_session(self, proxy):
        """Gets the repository search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RepositorySearchSession``
        :rtype: ``osid.repository.RepositorySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_repository_admin_session(self, proxy):
        """Gets the repository administrative session for creating, updating and deleteing repositories.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RepositoryAdminSession``
        :rtype: ``osid.repository.RepositoryAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_repository_notification_session(self, repository_receiver, proxy):
        """Gets the notification session for subscribing to changes to a repository.

        :param repository_receiver: the notification callback
        :type repository_receiver: ``osid.repository.RepositoryReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RepositoryNotificationSession``
        :rtype: ``osid.repository.RepositoryNotificationSession``
        :raise: ``NullArgument`` -- ``repository_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_repository_hierarchy_session(self, proxy):
        """Gets the repository hierarchy traversal session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a RepositoryHierarchySession``
        :rtype: ``osid.repository.RepositoryHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_repository_hierarchy_design_session(self, proxy):
        """Gets the repository hierarchy design session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RepostoryHierarchyDesignSession``
        :rtype: ``osid.repository.RepositoryHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_repository_batch_proxy_manager(self):
        """Gets a ``RepositoryBatchProxyManager``.

        :return: a ``RepostoryBatchProxyManager``
        :rtype: ``osid.repository.batch.RepositoryBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    repository_batch_proxy_manager = property(fget=get_repository_batch_proxy_manager)

    def get_repository_rules_proxy_manager(self):
        """Gets a ``RepositoryRulesProxyManager``.

        :return: a ``RepostoryRulesProxyManager``
        :rtype: ``osid.repository.rules.RepositoryRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_repository_rules()`` is ``false``

        """
        raise UNIMPLEMENTED()

    repository_rules_proxy_manager = property(fget=get_repository_rules_proxy_manager)



class Repository(osid_objects.OsidCatalog, osid_sessions.OsidSession):

    def get_repository_record(self, repository_record_type):
        """Gets the record corresponding to the given ``Repository`` record ``Type``.
        This method is used to retrieve an object implementing the
        requested record. The ``repository_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(repository_record_type)`` is ``true`` .

        :param repository_record_type: a repository record type
        :type repository_record_type: ``osid.type.Type``
        :return: the repository record
        :rtype: ``osid.repository.records.RepositoryRecord``
        :raise: ``NullArgument`` -- ``repository_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(repository_record_type)`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.AssetLookupSession

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    repository = property(fget=get_repository)

    def can_lookup_assets(self):
        """Tests if this user can perform ``Asset`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_asset_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_asset_view(self):
        """A complete view of the ``Asset`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.
        A federated view will include assets in repositories which are
        children of this repository in the repository hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this repository only.



        """
        raise UNIMPLEMENTED()

    def get_asset(self, asset_id):
        """Gets the ``Asset`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Asset`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Asset`` and retained for compatibility.

        :param asset_id: the ``Id`` of the ``Asset`` to retrieve
        :type asset_id: ``osid.id.Id``
        :return: the returned ``Asset``
        :rtype: ``osid.repository.Asset``
        :raise: ``NotFound`` -- no ``Asset`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_assets_by_ids(self, asset_ids):
        """Gets an ``AssetList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the assets
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Assets`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param asset_ids: the list of ``Ids`` to retrieve
        :type asset_ids: ``osid.id.IdList``
        :return: the returned ``Asset list``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``asset_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_assets_by_genus_type(self, asset_genus_type):
        """Gets an ``AssetList`` corresponding to the given asset genus ``Type`` which does not include assets of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        :param asset_genus_type: an asset genus type
        :type asset_genus_type: ``osid.type.Type``
        :return: the returned ``Asset list``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``asset_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_assets_by_parent_genus_type(self, asset_genus_type):
        """Gets an ``AssetList`` corresponding to the given asset genus ``Type`` and include any additional assets with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        :param asset_genus_type: an asset genus type
        :type asset_genus_type: ``osid.type.Type``
        :return: the returned ``Asset list``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``asset_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_assets_by_record_type(self, asset_record_type):
        """Gets an ``AssetList`` containing the given asset record ``Type``.
        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        :param asset_record_type: an asset record type
        :type asset_record_type: ``osid.type.Type``
        :return: the returned ``Asset list``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``asset_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_assets_by_provider(self, resource_id):
        """Gets an ``AssetList`` from the given provider.
        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Asset list``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_assets(self):
        """Gets all ``Assets``.
        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        :return: a list of ``Assets``
        :rtype: ``osid.repository.AssetList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    assets = property(fget=get_assets)


##
# The following methods are from osid.repository.AssetQuerySession

    def can_search_assets(self):
        """Tests if this user can perform ``Asset`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_asset_query(self):
        """Gets an asset query.

        :return: the asset query
        :rtype: ``osid.repository.AssetQuery``

        """
        raise UNIMPLEMENTED()

    asset_query = property(fget=get_asset_query)

    def get_assets_by_query(self, asset_query):
        """Gets a list of ``Assets`` matching the given asset query.

        :param asset_query: the asset query
        :type asset_query: ``osid.repository.AssetQuery``
        :return: the returned ``AssetList``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``asset_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- the ``asset_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.AssetSearchSession

    def get_asset_search(self):
        """Gets an asset search.

        :return: the asset search
        :rtype: ``osid.repository.AssetSearch``

        """
        raise UNIMPLEMENTED()

    asset_search = property(fget=get_asset_search)

    def get_asset_search_order(self):
        """Gets an asset search order.
        The ``AssetSearchOrder`` is supplied to an ``AssetSearch`` to
        specify the ordering of results.

        :return: the asset search order
        :rtype: ``osid.repository.AssetSearchOrder``

        """
        raise UNIMPLEMENTED()

    asset_search_order = property(fget=get_asset_search_order)

    def get_assets_by_search(self, asset_query, asset_search):
        """Gets the search results matching the given search query using the given search.

        :param asset_query: the asset query
        :type asset_query: ``osid.repository.AssetQuery``
        :param asset_search: the asset search
        :type asset_search: ``osid.repository.AssetSearch``
        :return: the asset search results
        :rtype: ``osid.repository.AssetSearchResults``
        :raise: ``NullArgument`` -- ``asset_query`` or ``asset_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``asset_query`` or ``asset_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_asset_query_from_inspector(self, asset_query_inspector):
        """Gets an asset query from an inspector.
        The inspector is available from a ``AssetSearchResults``.

        :param asset_query_inspector: an asset query inspector
        :type asset_query_inspector: ``osid.repository.AssetQueryInspector``
        :return: the asset query
        :rtype: ``osid.repository.AssetQuery``
        :raise: ``NullArgument`` -- ``asset_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``asset_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.AssetAdminSession

    def can_create_assets(self):
        """Tests if this user can create ``Assets``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Asset`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_asset_with_record_types(self, asset_record_types):
        """Tests if this user can create a single ``Asset`` using the desired record types.
        While ``RepositoryManager.getAssetRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Asset``.
        Providing an empty array tests if an ``Asset`` can be created
        with no records.

        :param asset_record_types: array of asset record types
        :type asset_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Asset`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``asset_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_asset_form_for_create(self, asset_record_types):
        """Gets the asset form for creating new assets.
        A new form should be requested for each create transaction.

        :param asset_record_types: array of asset record types
        :type asset_record_types: ``osid.type.Type[]``
        :return: the asset form
        :rtype: ``osid.repository.AssetForm``
        :raise: ``NullArgument`` -- ``asset_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_asset(self, asset_form):
        """Creates a new ``Asset``.

        :param asset_form: the form for this ``Asset``
        :type asset_form: ``osid.repository.AssetForm``
        :return: the new ``Asset``
        :rtype: ``osid.repository.Asset``
        :raise: ``IllegalState`` -- ``asset_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``asset_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``asset_form`` did not originate from ``get_asset_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_assets(self):
        """Tests if this user can update ``Assets``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if ``Asset`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_asset_form_for_update(self, asset_id):
        """Gets the asset form for updating an existing asset.
        A new asset form should be requested for each update
        transaction.

        :param asset_id: the ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :return: the asset form
        :rtype: ``osid.repository.AssetForm``
        :raise: ``NotFound`` -- ``asset_id`` is not found
        :raise: ``NullArgument`` -- ``asset_id`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_asset(self, asset_form):
        """Updates an existing asset.

        :param asset_form: the form containing the elements to be updated
        :type asset_form: ``osid.repository.AssetForm``
        :raise: ``IllegalState`` -- ``asset_form`` already used in anupdate transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``asset_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``asset_form`` did not originate from ``get_asset_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_assets(self):
        """Tests if this user can delete ``Assets``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Asset`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_asset(self, asset_id):
        """Deletes an ``Asset``.

        :param asset_id: the ``Id`` of the ``Asset`` to remove
        :type asset_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``asset_id`` not found
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_asset_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Assets``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Asset`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_asset(self, asset_id, alias_id):
        """Adds an ``Id`` to an ``Asset`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Asset`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another asset, it is
        reassigned to the given asset ``Id``.

        :param asset_id: the ``Id`` of an ``Asset``
        :type asset_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``asset_id`` not found
        :raise: ``NullArgument`` -- ``asset_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_create_asset_content(self):
        """Tests if this user can create content for ``Assets``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``AssetContent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Asset`` content creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_asset_content_with_record_types(self, asset_content_record_types):
        """Tests if this user can create an ``AssetContent`` using the desired record types.
        While ``RepositoryManager.getAssetContentRecordTypes()`` can be
        used to test which records are supported, this method tests
        which records are required for creating a specific
        ``AssetContent``. Providing an empty array tests if an
        ``AssetContent`` can be created with no records.

        :param asset_content_record_types: array of asset content record types
        :type asset_content_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``AssetContent`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``asset_content_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_asset_content_form_for_create(self, asset_id, asset_content_record_types):
        """Gets an asset content form for creating new assets.

        :param asset_id: the ``Id`` of an ``Asset``
        :type asset_id: ``osid.id.Id``
        :param asset_content_record_types: array of asset content record types
        :type asset_content_record_types: ``osid.type.Type[]``
        :return: the asset content form
        :rtype: ``osid.repository.AssetContentForm``
        :raise: ``NotFound`` -- ``asset_id`` is not found
        :raise: ``NullArgument`` -- ``asset_id`` or ``asset_content_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_asset_content(self, asset_content_form):
        """Creates new ``AssetContent`` for a given asset.

        :param asset_content_form: the form for this ``AssetContent``
        :type asset_content_form: ``osid.repository.AssetContentForm``
        :return: the new ``AssetContent``
        :rtype: ``osid.repository.AssetContent``
        :raise: ``IllegalState`` -- ``asset_content_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``asset_content_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``asset_content_form`` did not originate from ``get_asset_content_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_asset_contents(self):
        """Tests if this user can update ``AssetContent``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``AssetContent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``AssetContent`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_asset_content_form_for_update(self, asset_content_id):
        """Gets the asset content form for updating an existing asset content.
        A new asset content form should be requested for each update
        transaction.

        :param asset_content_id: the ``Id`` of the ``AssetContent``
        :type asset_content_id: ``osid.id.Id``
        :return: the asset content form
        :rtype: ``osid.repository.AssetContentForm``
        :raise: ``NotFound`` -- ``asset_content_id`` is not found
        :raise: ``NullArgument`` -- ``asset_content_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def update_asset_content(self, asset_content_form):
        """Updates an existing asset content.

        :param asset_content_form: the form containing the elements to be updated
        :type asset_content_form: ``osid.repository.AssetContentForm``
        :raise: ``IllegalState`` -- ``asset_content_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``asset_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``asset_content_form`` did not originate from ``get_asset_content_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_asset_contents(self):
        """Tests if this user can delete ``AssetsContents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``AssetContent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``AssetContent`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_asset_content(self, asset_content_id):
        """Deletes content from an ``Asset``.

        :param asset_content_id: the ``Id`` of the ``AssetContent``
        :type asset_content_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``asset_content_id`` is not found
        :raise: ``NullArgument`` -- ``asset_content_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.AssetNotificationSession

    def can_register_for_asset_notifications(self):
        """Tests if this user can register for ``Asset`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_assets(self):
        """Register for notifications of new assets.
        ``AssetReceiver.newAsset()`` is invoked when a new ``Asset``
        appears in this repository.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_assets_by_genus_type(self, asset_genus_type):
        """Registers for notification of new assets of the given asset genus type.
        ``AssetReceiver.newAsset()`` is invoked when an asset is appears
        in this repository.

        :param asset_genus_type: the genus type of the ``Asset`` to monitor
        :type asset_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``asset_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_assets(self):
        """Registers for notification of updated assets.
        ``AssetReceiver.changedAsset()`` is invoked when an asset in
        this repository is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_assets_by_genus_type(self, asset_genus_type):
        """Registers for notification of updated assets of the given asset genus type.
        ``AssetReceiver.changedAsset()`` is invoked when an asset in
        this repository is changed.

        :param asset_genus_type: the genus type of the ``Asset`` to monitor
        :type asset_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``asset_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_asset(self, asset_id):
        """Registers for notification of an updated asset.
        ``AssetReceiver.changedAsset()`` is invoked when the specified
        asset in this repository is changed.

        :param asset_id: the ``Id`` of the ``Asset`` to monitor
        :type asset_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_assets(self):
        """Registers for notification of deleted assets.
        ``AssetReceiver.deletedAsset()`` is invoked when an asset is
        deleted or removed from this repository.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_assets_by_genus_type(self, asset_genus_type):
        """Registers for notification of deleted assets of the given asset genus type.
        ``AssetReceiver.deletedAsset()`` is invoked when an asset is
        deleted or removed from this repository.

        :param asset_genus_type: the genus type of the ``Asset`` to monitor
        :type asset_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``asset_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_asset(self, asset_id):
        """Registers for notification of a deleted asset.
        ``AssetReceiver.deletedAsset()`` is invoked when the specified
        asset is deleted or removed from this repository.

        :param asset_id: the ``Id`` of the ``Asset`` to monitor
        :type asset_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.AssetRepositorySession

    def can_lookup_asset_repository_mappings(self):
        """Tests if this user can perform lookups of asset/repository mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_repository_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_repository_view(self):
        """A complete view of the ``Asset`` and ``Repository`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_asset_ids_by_repository(self, repository_id):
        """Gets the list of ``Asset``  ``Ids`` associated with a ``Repository``.

        :param repository_id: ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: list of related asset ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_assets_by_repository(self, repository_id):
        """Gets the list of ``Assets`` associated with a ``Repository``.

        :param repository_id: ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: list of related assets
        :rtype: ``osid.repository.AssetList``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_asset_ids_by_repositories(self, repository_ids):
        """Gets the list of ``Asset Ids`` corresponding to a list of ``Repository`` objects.

        :param repository_ids: list of repository ``Ids``
        :type repository_ids: ``osid.id.IdList``
        :return: list of asset ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``repository_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_assets_by_repositories(self, repository_ids):
        """Gets the list of ``Assets`` corresponding to a list of ``Repository`` objects.

        :param repository_ids: list of repository ``Ids``
        :type repository_ids: ``osid.id.IdList``
        :return: list of assets
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``repository_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_repository_ids_by_asset(self, asset_id):
        """Gets the list of ``Repository``  ``Ids`` mapped to an ``Asset``.

        :param asset_id: ``Id`` of an ``Asset``
        :type asset_id: ``osid.id.Id``
        :return: list of repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``asset_id`` is not found
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_repositories_by_asset(self, asset_id):
        """Gets the list of ``Repository`` objects mapped to an ``Asset``.

        :param asset_id: ``Id`` of an ``Asset``
        :type asset_id: ``osid.id.Id``
        :return: list of repositories
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NotFound`` -- ``asset_id`` is not found
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.AssetRepositoryAssignmentSession

    def can_assign_assets(self):
        """Tests if this user can alter asset/repository mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_assets_to_repository(self, repository_id):
        """Tests if this user can alter asset/repository mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_repository_ids(self, repository_id):
        """Gets a list of repositories including and under the given repository node in which any asset can be assigned.

        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: list of assignable repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_repository_ids_for_asset(self, repository_id, asset_id):
        """Gets a list of repositories including and under the given repository node in which a specific asset can be assigned.

        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :param asset_id: the ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :return: list of assignable repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``repository_id`` or ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_asset_to_repository(self, asset_id, repository_id):
        """Adds an existing ``Asset`` to a ``Repository``.

        :param asset_id: the ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``asset_id`` already assigned to ``repository_id``
        :raise: ``NotFound`` -- ``asset_id`` or ``repository_id`` not found
        :raise: ``NullArgument`` -- ``asset_id`` or ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_asset_from_repository(self, asset_id, repository_id):
        """Removes an ``Asset`` from a ``Repository``.

        :param asset_id: the ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``asset_id`` or ``repository_id`` not found or ``asset_id`` not assigned to ``repository_id``
        :raise: ``NullArgument`` -- ``asset_id`` or ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.AssetSmartRepositorySession

    def can_manage_smart_repository(self):
        """Tests if this user can manage smart repository.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart repository management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_asset_query(self, asset_query):
        """Applies an asset query to this repository.

        :param asset_query: the asset query
        :type asset_query: ``osid.repository.AssetQuery``
        :raise: ``NullArgument`` -- ``asset_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``asset_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_asset_query(self):
        """Gets an asset query inspector for this repository.

        :return: the asset query inspector
        :rtype: ``osid.repository.AssetQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_asset_sequencing(self, asset_search_order):
        """Applies an asset search order to this repository.

        :param asset_search_order: the asset search order
        :type asset_search_order: ``osid.repository.AssetSearchOrder``
        :raise: ``NullArgument`` -- ``asset_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``asset_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.AssetTemporalSession

    def can_lookup_temporal_coverage(self):
        """Tests if this user can perform temporal lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookups are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_temporal_coverage(self, asset_id):
        """Gets the temporal coverage related to the subject of this asset.
        Each element of the returned list describes a range of 2 times
        each described by a point in time with specified granularity and
        uncertainty. If the list contains more than one element, each
        element indicates a relevant time or period for the subject of
        this asset.

        :param asset_id: ``Id`` of the ``Asset`` to query
        :type asset_id: ``osid.id.Id``
        :return: a list of times relevant to the subject of this asset
        :rtype: ``osid.calendaring.DateTimeIntervalList``
        :raise: ``NotFound`` -- ``asset_id`` is not found
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_asset_ids_by_temporal_coverage(self, from_, to):
        """Gets asset ``Ids`` with temporal coverege within the specified dates inclusive.

        :param from: starting range
        :type from: ``osid.calendaring.DateTime``
        :param to: ending range
        :type to: ``osid.calendaring.DateTime``
        :return: list of asset ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_assets_by_temporal_coverage(self, from_, to):
        """Gets assets with temporal coverege within the specified dates inclusive.

        :param from: starting range
        :type from: ``osid.calendaring.DateTime``
        :param to: ending range
        :type to: ``osid.calendaring.DateTime``
        :return: list of assets
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.AssetTemporalAssignmentSession

    def can_assign_temporal_coverage(self):
        """Tests if this user can manage temporal lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer assignment
        operations.

        :return: ``false`` if temporal management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_temporal_coverage(self, asset_id, begin, end):
        """Adds a temporal coverage to this asset expressed as a range between two date/times.

        :param asset_id: ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param begin: start date/time
        :type begin: ``osid.calendaring.DateTime``
        :param end: end date/time
        :type end: ``osid.calendaring.DateTime``
        :raise: ``AlreadyExists`` -- interval already exists
        :raise: ``InvalidArgument`` -- ``begin`` is greater than ``end``
        :raise: ``NotFound`` -- ``asset_id`` not ``found``
        :raise: ``NullArgument`` -- ``asset_id, begin`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure

        """
        raise UNIMPLEMENTED()

    def remove_temporal_coverage(self, asset_id, begin, end):
        """Removes a temporal range from an asset.

        :param asset_id: ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param begin: start date/time
        :type begin: ``osid.calendaring.DateTime``
        :param end: end date/time
        :type end: ``osid.calendaring.DateTime``
        :raise: ``NotFound`` -- ``asset_id`` with ``begin`` and ``end`` not ``found``
        :raise: ``NullArgument`` -- ``asset_id, begin`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.AssetSpatialSession

    def can_lookup_spatial_coverage(self):
        """Tests if this user can perform spatial lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if spatial lookups are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_asset_location_ids(self, asset_id):
        """Gets the locations related to the subject of this asset.

        :param asset_id: ``Id`` of the ``Asset`` to query
        :type asset_id: ``osid.id.Id``
        :return: a list of locations relevant to the subject of this asset
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``asset_id`` is not found
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_asset_locations(self, asset_id):
        """Gets the locations related to the subject of this asset.

        :param asset_id: ``Id`` of the ``Asset`` to query
        :type asset_id: ``osid.id.Id``
        :return: a list of locations relevant to the subject of this asset
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NotFound`` -- ``asset_id`` is not found
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_asset_spatial_coverage(self, asset_id):
        """Gets the spacial coverage related to the subject of this asset.
        Each element of the returned list indicates a point in space
        with specified granularity and uncertainty, or a spatial area.
        If the list contains more than one element, each element
        indicates a relevant time or period for the subject of this
        asset.

        :param asset_id: ``Id`` of the ``Asset`` to query
        :type asset_id: ``osid.id.Id``
        :return: a list of locations relevant to the subject of this asset
        :rtype: ``osid.mapping.SpatialUnitList``
        :raise: ``NotFound`` -- ``asset_id`` is not found
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_asset_ids_by_location(self, location_id):
        """Gets a list of asset ``Ids`` included within the location.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: a list of asset ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_assets_by_location(self, location_id):
        """Gets a list of assets included within the given spatial coverage.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: a list of assets
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_asset_ids_by_spatial_coverage(self, spatial_unit):
        """Gets a list of asset ``Ids`` included within the given spatial coverage.

        :param spatial_unit: a spatial unit
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :return: a list of asset ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_assets_by_spatial_coverage(self, spatial_unit):
        """Gets a list of assets included within the given spatial coverage.

        :param spatial_unit: a spatial unit
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :return: a list of assets
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.AssetSpatialAssignmentSession

    def can_assign_spatial_coverage(self):
        """Tests if this user can manage spatial lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer assignment
        operations.

        :return: ``false`` if spatial management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_asset_location(self, asset_id, location_id):
        """Adds a location to an asset.

        :param asset_id: ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- asset already contains this spatial coverage
        :raise: ``NotFound`` -- ``asset_id`` or ``location_id`` not ``found``
        :raise: ``NullArgument`` -- ``asset_id`` or ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure

        """
        raise UNIMPLEMENTED()

    def add_asset_spatial_coverage(self, asset_id, spatial_unit):
        """Adds a spatial coverage to an asset.

        :param asset_id: ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param spatial_unit: spatial coverage
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :raise: ``AlreadyExists`` -- asset already contains this spatial coverage
        :raise: ``NotFound`` -- ``asset_id`` not ``found``
        :raise: ``NullArgument`` -- ``asset_id`` or ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure
        :raise: ``Unsupported`` -- ``spatial_unit`` not supported

        """
        raise UNIMPLEMENTED()

    def remove_asset_location(self, asset_id, location_id):
        """Removes a location from an asset.

        :param asset_id: ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param location_id: spatial coverage
        :type location_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``asset_id`` with ``location_id`` not ``found``
        :raise: ``NullArgument`` -- ``asset_id`` or ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure

        """
        raise UNIMPLEMENTED()

    def remove_asset_spatial_coverage(self, asset_id, spatial_unit):
        """Removes a spatial coverage from an asset.

        :param asset_id: ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param spatial_unit: spatial coverage
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :raise: ``NotFound`` -- ``asset_id`` with ``spatial_unit`` not ``found``
        :raise: ``NullArgument`` -- ``asset_id`` or ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.AssetCompositionSession

    def can_access_asset_compositions(self):
        """Tests if this user can perform composition lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_asset_composition_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_asset_composition_view(self):
        """A complete view of the returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_composition_assets(self, composition_id):
        """Gets the list of assets mapped to the given ``Composition``.

        :param composition_id: ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :return: list of assets
        :rtype: ``osid.repository.AssetList``
        :raise: ``NotFound`` -- ``composition_id`` not found
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_compositions_by_asset(self, asset_id):
        """Gets a list of compositions including the given asset.

        :param asset_id: ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :return: the returned ``Composition list``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NotFound`` -- ``asset_id`` is not found
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.AssetCompositionDesignSession

    def can_compose_assets(self):
        """Tests if this user can manage mapping of ``Assets`` to ``Compositions``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as an application hint that may opt not to offer composition
        operations.

        :return: ``false`` if asset composiion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_asset(self, asset_id, composition_id):
        """Appends an asset to a composition.

        :param asset_id: ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param composition_id: ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``asset_id`` already part ``composition_id``
        :raise: ``NotFound`` -- ``asset_id`` or ``composition_id`` not found
        :raise: ``NullArgument`` -- ``asset_id`` or ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure

        """
        raise UNIMPLEMENTED()

    def move_asset_ahead(self, asset_id, composition_id, reference_id):
        """Reorders assets in a composition by moving the specified asset in front of a reference asset.

        :param asset_id: ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param composition_id: ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :param reference_id: ``Id`` of the reference ``Asset``
        :type reference_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``asset_id`` or ``reference_id``  ``not found in composition_id``
        :raise: ``NullArgument`` -- ``asset_id, reference_id`` or ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure

        """
        raise UNIMPLEMENTED()

    def move_asset_behind(self, asset_id, composition_id, reference_id):
        """Reorders assets in a composition by moving the specified asset behind of a reference asset.

        :param asset_id: ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param composition_id: ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :param reference_id: ``Id`` of the reference ``Asset``
        :type reference_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``asset_id`` or ``reference_id``  ``not found in composition_id``
        :raise: ``NullArgument`` -- ``asset_id, reference_id`` or ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure

        """
        raise UNIMPLEMENTED()

    def order_assets(self, asset_ids, composition_id):
        """Reorders a set of assets in a composition.

        :param asset_ids: ``Ids`` for a set of ``Assets``
        :type asset_ids: ``osid.id.Id[]``
        :param composition_id: ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``composition_id`` not found or, an ``asset_id`` not related to ``composition_id``
        :raise: ``NullArgument`` -- ``instruction_ids`` or ``agenda_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_asset(self, asset_id, composition_id):
        """Removes an ``Asset`` from a ``Composition``.

        :param asset_id: ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param composition_id: ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``asset_id``  ``not found in composition_id``
        :raise: ``NullArgument`` -- ``asset_id`` or ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.CompositionLookupSession

    def can_lookup_compositions(self):
        """Tests if this user can perform ``Composition`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_composition_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_composition_view(self):
        """A complete view of the ``Composition`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_active_composition_view(self):
        """Only active compositions are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_any_status_composition_view(self):
        """All active and inactive compositions are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_sequestered_composition_view(self):
        """The methods in this session omit sequestered compositions."""
        raise UNIMPLEMENTED()

    def use_unsequestered_composition_view(self):
        """The methods in this session return all compositions, including sequestered compositions."""
        raise UNIMPLEMENTED()

    def get_composition(self, composition_id):
        """Gets the ``Composition`` specified by its ``Id``.

        :param composition_id: ``Id`` of the ``Composiiton``
        :type composition_id: ``osid.id.Id``
        :return: the composition
        :rtype: ``osid.repository.Composition``
        :raise: ``NotFound`` -- ``composition_id`` not found
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_compositions_by_ids(self, composition_ids):
        """Gets a ``CompositionList`` corresponding to the given ``IdList``.

        :param composition_ids: the list of ``Ids`` to retrieve
        :type composition_ids: ``osid.id.IdList``
        :return: the returned ``Composition list``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``composition_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_compositions_by_genus_type(self, composition_genus_type):
        """Gets a ``CompositionList`` corresponding to the given composition genus ``Type`` which does not include compositions of types derived from the specified ``Type``.

        :param composition_genus_type: a composition genus type
        :type composition_genus_type: ``osid.type.Type``
        :return: the returned ``Composition list``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NullArgument`` -- ``composition_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_compositions_by_parent_genus_type(self, composition_genus_type):
        """Gets a ``CompositionList`` corresponding to the given composition genus ``Type`` and include any additional compositions with genus types derived from the specified ``Type``.

        :param composition_genus_type: a composition genus type
        :type composition_genus_type: ``osid.type.Type``
        :return: the returned ``Composition list``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NullArgument`` -- ``composition_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_compositions_by_record_type(self, composition_record_type):
        """Gets a ``CompositionList`` containing the given composition record ``Type``.

        :param composition_record_type: a composition record type
        :type composition_record_type: ``osid.type.Type``
        :return: the returned ``Composition list``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NullArgument`` -- ``composition_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_compositions_by_provider(self, resource_id):
        """Gets a ``CompositionList`` from the given provider ````.
        In plenary mode, the returned list contains all known
        compositions or an error results. Otherwise, the returned list
        may contain only those compositions that are accessible through
        this session.

        In sequestered mode, no sequestered compositions are returned.
        In unsequestered mode, all compositions are returned.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Composition list``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_compositions(self):
        """Gets all ``Compositions``.

        :return: a list of ``Compositions``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    compositions = property(fget=get_compositions)


##
# The following methods are from osid.repository.CompositionQuerySession

    def can_search_compositions(self):
        """Tests if this user can perform ``Composition`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_composition_query(self):
        """Gets a composition query.

        :return: the composition query
        :rtype: ``osid.repository.CompositionQuery``

        """
        raise UNIMPLEMENTED()

    composition_query = property(fget=get_composition_query)

    def get_compositions_by_query(self, composition_query):
        """Gets a list of ``Compositions`` matching the given composition query.

        :param composition_query: the composition query
        :type composition_query: ``osid.repository.CompositionQuery``
        :return: the returned ``CompositionList``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NullArgument`` -- ``composition_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``composition_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.CompositionSearchSession

    def get_composition_search(self):
        """Gets a composition search.

        :return: the composition search
        :rtype: ``osid.repository.CompositionSearch``

        """
        raise UNIMPLEMENTED()

    composition_search = property(fget=get_composition_search)

    def get_composition_search_order(self):
        """Gets a composition search order.
        The ``CompositionSearchOrder`` is supplied to an
        ``CompositionSearch`` to specify the ordering of results.

        :return: the composition search order
        :rtype: ``osid.repository.CompositionSearchOrder``

        """
        raise UNIMPLEMENTED()

    composition_search_order = property(fget=get_composition_search_order)

    def get_compositions_by_search(self, composition_query, composition_search):
        """Gets the search results matching the given search query using the given search.

        :param composition_query: the composition query
        :type composition_query: ``osid.repository.CompositionQuery``
        :param composition_search: the composition search
        :type composition_search: ``osid.repository.CompositionSearch``
        :return: the composition search results
        :rtype: ``osid.repository.CompositionSearchResults``
        :raise: ``NullArgument`` -- ``composition_query`` or ``composition_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``composition_query`` or ``composition_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_composition_query_from_inspector(self, composition_query_inspector):
        """Gets a composition query from an inspector.
        The inspector is available from a ``CompositionSearchResults``.

        :param composition_query_inspector: a composition query inspector
        :type composition_query_inspector: ``osid.repository.CompositionQueryInspector``
        :return: the composition query
        :rtype: ``osid.repository.CompositionQuery``
        :raise: ``NullArgument`` -- ``composition_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``composition_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.CompositionAdminSession

    def can_create_compositions(self):
        """Tests if this user can create ``Compositions``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Composition`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Composition`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_composition_with_record_types(self, composition_record_types):
        """Tests if this user can create a single ``Composition`` using the desired record types.
        While ``RepositoryManager.getCompositionRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Composition``. Providing an empty array tests if a
        ``Composition`` can be created with no records.

        :param composition_record_types: array of composition record types
        :type composition_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Composition`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``composition_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_composition_form_for_create(self, composition_record_types):
        """Gets the composition form for creating new compositions.
        A new form should be requested for each create transaction.

        :param composition_record_types: array of composition record types
        :type composition_record_types: ``osid.type.Type[]``
        :return: the composition form
        :rtype: ``osid.repository.CompositionForm``
        :raise: ``NullArgument`` -- ``composition_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_composition(self, composiiton_form):
        """Creates a new ``Composition``.

        :param composiiton_form: the form for this ``Composition``
        :type composiiton_form: ``osid.repository.CompositionForm``
        :return: the new ``Composition``
        :rtype: ``osid.repository.Composition``
        :raise: ``IllegalState`` -- ``composition_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``composition_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``composition_form`` did not originate from ``get_composition_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_compositions(self):
        """Tests if this user can update ``Compositions``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Composition`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Composition`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_composition_form_for_update(self, composition_id):
        """Gets the composition form for updating an existing composition.
        A new composition form should be requested for each update
        transaction.

        :param composition_id: the ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :return: the composition form
        :rtype: ``osid.repository.CompositionForm``
        :raise: ``NotFound`` -- ``composition_id`` is not found
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_composition(self, composiiton_form):
        """Updates an existing composition.

        :param composiiton_form: the form containing the elements to be updated
        :type composiiton_form: ``osid.repository.CompositionForm``
        :raise: ``IllegalState`` -- ``composition_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``composition_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``composition_form`` did not originate from ``get_composition_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_compositions(self):
        """Tests if this user can delete ``Compositions``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Composition`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Composition`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_composition(self, composition_id):
        """Deletes a ``Composition``.

        :param composition_id: the ``Id`` of the ``Composition`` to remove
        :type composition_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``composition_id`` not found
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def delete_composition_node(self, composition_id):
        """Deletes a ``Composition`` and all contained children.

        :param composition_id: the ``Id`` of the ``Composition`` to remove
        :type composition_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``composition_id`` not found
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_composition_child(self, composition_id, child_composition_id):
        """Adds a composition to a parent composition.

        :param composition_id: the ``Id`` of a parent ``Composition``
        :type composition_id: ``osid.id.Id``
        :param child_composition_id: the ``Id`` of a child ``Composition``
        :type child_composition_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``child_composition_id`` is already a child of ``composition_id``
        :raise: ``NotFound`` -- ``composition_id`` or ``child_composition_id`` is not found
        :raise: ``NullArgument`` -- ``composition_id`` or ``child_composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_composition_child(self, composition_id, child_composition_id):
        """Removes a composition from a parent composition.

        :param composition_id: the ``Id`` of a parent ``Composition``
        :type composition_id: ``osid.id.Id``
        :param child_composition_id: the ``Id`` of a child ``Composition``
        :type child_composition_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``composition_id`` or ``child_composition_id`` is not found or not related
        :raise: ``NullArgument`` -- ``composition_id`` or ``child_composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_composition_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Compositions``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Composition`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_composition(self, composition_id, alias_id):
        """Adds an ``Id`` to a ``Composition`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Composition`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another composition, it is reassigned
        to the given composition ``Id``.

        :param composition_id: the ``Id`` of a ``Composition``
        :type composition_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``composition_id`` not found
        :raise: ``NullArgument`` -- ``composition_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.CompositionNotificationSession

    def can_register_for_composition_notifications(self):
        """Tests if this user can register for ``Composition`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_federated_composition_view(self):
        """Federates the view for asset methods in this session.
        A federated view will include assets in compositions of which
        are children of the specified composition in the composition
        hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_composition_view(self):
        """Isolates the view for asset methods in this session.
        An isolated view restricts notifications to the specified
        composition only.



        """
        raise UNIMPLEMENTED()

    def register_for_new_compositions(self):
        """Register for notifications of new composition.
        ``CompositionReceiver.newComposition()`` is invoked when a new
        ``Composition`` appears in this repository.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_assigned_assets_in_composition(self, composition_id):
        """Registers for notification if an asset is added to a specified composition.
        ``CompositionReceiver.newCompositionAsset()`` is invoked when an
        asset is added to the specified composition. In the federated
        composition view, notifications include additions to child
        compositions.

        :param composition_id: the ``Id`` of the composition to monitor
        :type composition_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_composition_ancestor(self, composition_id):
        """Registers for notification if an ancestor is added to the specified composition in the composition composition.
        ``CompositionReceiver.newCompositionAncestor()`` is invoked when
        the specified composition experiences an addition in ancestors.

        :param composition_id: the ``Id`` of the composition to monitor
        :type composition_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_composition_descendants(self, composition_id):
        """Registers for notification if a descendant is added to the specified composition in the composition composition.
        ``CompositionReceiver.newCompositionDescendant()`` is invoked
        when the specified composition experiences an addition in
        descendants.

        :param composition_id: the ``Id`` of the composition to monitor
        :type composition_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_compositions(self):
        """Register for notifications of new compositions.
        ``CompositionReceiver.changedComposition()`` is invoked when a
        ``Composition`` is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_composition(self, composition_id):
        """Registers for notification of an updated composition.
        ``CompositionReceiver.changedComposition()`` is invoked when the
        specified composition is changed.

        :param composition_id: the ``Id`` of the ``Composition`` to monitor
        :type composition_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_compositions(self):
        """Register for notifications of new compositions.
        ``CompositionReceiver.deletedComposition()`` is invoked when a
        ``Composition`` is removed from this repository.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_composition(self, composition_id):
        """Registers for notification of a deleted composition.
        ``CompositionReceiver.deletedComposition()`` is invoked when the
        specified composition is removed from this repository.

        :param composition_id: the ``Id`` of the ``Composition`` to monitor
        :type composition_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_unassigned_assets_in_composition(self, composition_id):
        """Registers for notification if an asset is removed from a specified composition.
        ``CompositionReceiver.deletedCompositionAsset()`` is invoked
        when an asset is removed from the specified composition. In the
        federated composition view, notifications include removals from
        child compositions.

        :param composition_id: the ``Id`` of the composition to monitor
        :type composition_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_composition_ancestors(self, composition_id):
        """Registers for notification if an ancestor removed from to the specified composition in the composition composition.
        ``CompositionReceiver.deletedCompositionAncestor()`` is invoked
        when the specified composition experiences a removal of an
        ancestor.

        :param composition_id: the ``Id`` of the composition to monitor
        :type composition_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_composition_descendants(self, composition_id):
        """Registers for notification if a descendant removed from to the specified composition in the composition composition.
        ``CompositionReceiver.deletedCompositionDescendant()`` is
        invoked when the specified composition experiences a removal of
        a descendant.

        :param composition_id: the ``Id`` of the composition to monitor
        :type composition_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.CompositionRepositorySession

    def use_comparative_composition_repository_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_composition_repository_view(self):
        """A complete view of the ``Composition`` and ``Repository`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def can_lookup_composition_repository_mappings(self):
        """Tests if this user can perform lookups of composition/repository mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_composition_ids_by_repository(self, repository_id):
        """Gets the list of ``Composition``  ``Ids`` associated with a ``Repository``.

        :param repository_id: ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: list of related composition ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_compositions_by_repository(self, repository_id):
        """Gets the list of ``Compositions`` associated with a ``Repository``.

        :param repository_id: ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: list of related compositions
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_composition_ids_by_repositories(self, repository_ids):
        """Gets the list of ``Composition``  ``Ids`` corresponding to a list of ``Repository`` objects.

        :param repository_ids: list of repository ``Ids``
        :type repository_ids: ``osid.id.IdList``
        :return: list of composition ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``repository_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_compoitions_by_repositories(self, repository_ids):
        """Gets the list of ``Compositions`` corresponding to a list of ``Repository`` objects.

        :param repository_ids: list of repository ``Ids``
        :type repository_ids: ``osid.id.IdList``
        :return: list of Compositions
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NullArgument`` -- ``repository_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_repository_ids_by_composition(self, composition_id):
        """Gets the ``Repository``  ``Ids`` mapped to a ``Composition``.

        :param composition_id: ``Id`` of a ``Composition``
        :type composition_id: ``osid.id.Id``
        :return: list of repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``composition_id`` is not found
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_repositories_by_composition(self, composition_id):
        """Gets the ``Repository`` objects mapped to a ``Composition``.

        :param composition_id: ``Id`` of a ``Composition``
        :type composition_id: ``osid.id.Id``
        :return: list of repositories
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NotFound`` -- ``composition_id`` is not found
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.CompositionRepositoryAssignmentSession

    def can_assign_compositions(self):
        """Tests if this user can alter composition/repository mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_compositions_to_repository(self, repository_id):
        """Tests if this user can alter composition/repository mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_repository_ids_for_composition(self, repository_id, composition_id):
        """Gets a list of repositories including and under the given repository node in which a specific composition can be assigned.

        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :param composition_id: the ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :return: list of assignable repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``repository_id`` or ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_composition_to_repository(self, composition_id, repository_id):
        """Adds an existing ``Composition`` to a ``Repository``.

        :param composition_id: the ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``composition_id`` already assigned to ``repository_id``
        :raise: ``NotFound`` -- ``composition_id`` or ``repository_id`` not found
        :raise: ``NullArgument`` -- ``composition_id`` or ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_composition_from_repository(self, composition_id, repository_id):
        """Removes ``Composition`` from a ``Repository``.

        :param composition_id: the ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``composition_id`` or ``repository_id`` not found or ``composition_id`` not assigned to ``repository_id``
        :raise: ``NullArgument`` -- ``composition_id`` or ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.repository.CompositionSmartRepositorySession

    def apply_composition_query(self, composition_query):
        """Applies a composition query to this repository.

        :param composition_query: the composition query
        :type composition_query: ``osid.repository.CompositionQuery``
        :raise: ``NullArgument`` -- ``composition_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``composition_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_composition_query(self):
        """Gets a composition query inspector for this repository.

        :return: the composition query inspector
        :rtype: ``osid.repository.CompositionQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_composition_sequencing(self, composition_search_order):
        """Applies a composition search order to this repository.

        :param composition_search_order: the composition search order
        :type composition_search_order: ``osid.repository.CompositionSearchOrder``
        :raise: ``NullArgument`` -- ``composition_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``composition_search_order`` not of this service

        """
        raise UNIMPLEMENTED()



class RepositoryList(osid_objects.OsidList):

    def get_next_repository(self):
        """Gets the next ``Repository`` in this list.

        :return: the next ``Repository`` in this list. The ``has_next()`` method should be used to test that a next ``Repository`` is available before calling this method.
        :rtype: ``osid.repository.Repository``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    next_repository = property(fget=get_next_repository)

    def get_next_repositories(self, n):
        """Gets the next set of ``Repository`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Repository`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Repository`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.repository.Repository``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()



class Repositories(RepositoryManager):
    pass


