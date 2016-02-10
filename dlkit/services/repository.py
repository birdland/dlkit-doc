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
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects
from ..osid import markers as osid_markers
from ..osid import records as osid_records
from ..osid import queries as osid_queries
from ..osid import searches as osid_searches


class RepositoryProfile(osid_managers.OsidProfile):
    """The repository profile describes interoperability among repository services."""

    def __init__(self):
        self._provider_manager = None

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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_repository_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_repository_view(self):
        """A complete view of the ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.repository.Repository

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_repository_query(self):
        """Gets a repository query.

        :return: the repository query
        :rtype: ``osid.repository.RepositoryQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryQuery

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList


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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Repository

    def can_update_repositories(self):
        """Tests if this user can update ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Repository`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_repositories(self):
        """Tests if this user can delete ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Repository`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_repository(self, repository_id):
        """Deletes a ``Repository``.

        :param repository_id: the ``Id`` of the ``Repository`` to remove
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_repository_aliases(self):
        """Tests if this user can manage ``Id`` aliases for repositories.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Repository`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.repository.RepositoryHierarchySession

    def get_repository_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    repository_hierarchy_id = property(fget=get_repository_hierarchy_id)

    def get_repository_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_repository_view(self):
        """The returns from the repository methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_repository_view(self):
        """A complete view of the ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_root_repository_ids(self):
        """Gets the root repository ``Ids`` in this hierarchy.

        :return: the root repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Node

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryNode


##
# The following methods are from osid.repository.RepositoryHierarchyDesignSession

    def get_repository_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    repository_hierarchy_id = property(fget=get_repository_hierarchy_id)

    def get_repository_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    repository_hierarchy = property(fget=get_repository_hierarchy)

    def can_modify_repository_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def add_root_repository(self, repository_id):
        """Adds a root repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``repository_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_root_repository(self, repository_id):
        """Removes a root repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not a root
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_repositories(self, repository_id):
        """Removes all children from a repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




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

    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._repository_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)

    # def _get_view(self, view):
    #     """Gets the currently set view"""
    #     if view in self._views:
    #         return self._views[view]
    #     else:
    #         self._views[view] = DEFAULT
    #         return DEFAULT

    def _set_repository_view(self, session):
        """Sets the underlying repository view to match current view"""
        if self._repository_view == COMPARATIVE:
            try:
                session.use_comparative_repository_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_repository_view()
            except AttributeError:
                pass

    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        if self._proxy is None:
            self._proxy = proxy
        if session_name in self._provider_sessions:
            return self._provider_sessions[session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_repository_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[session_name] = session
            return session

    def _instantiate_session(self, method_name, proxy=None, *args, **kwargs):
        """Instantiates a provider session"""
        session_class = getattr(self._provider_manager, method_name)
        if proxy is None:
            return session_class(*args, **kwargs)
        else:
            return session_class(proxy=proxy, *args, **kwargs)

    def initialize(self, runtime):
        """OSID Manager initialize"""
        from .primitives import Id
        if self._runtime is not None:
            raise IllegalState('Manager has already been initialized')
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:repositoryProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('REPOSITORY', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('REPOSITORY', provider_impl)

    def close_sessions(self):
        """Close all sessions, unless session management is set to MANDATORY"""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()

    def use_automatic_session_management(self):
        """Session state will be saved unless closed by consumers"""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will be saved and can not be closed by consumers"""
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved"""
        self._session_management = DISABLED
        self.close_sessions()

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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_repository_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_repository_view(self):
        """A complete view of the ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.repository.Repository

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_repository_query(self):
        """Gets a repository query.

        :return: the repository query
        :rtype: ``osid.repository.RepositoryQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryQuery

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList


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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Repository

    def can_update_repositories(self):
        """Tests if this user can update ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Repository`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_repositories(self):
        """Tests if this user can delete ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Repository`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_repository(self, repository_id):
        """Deletes a ``Repository``.

        :param repository_id: the ``Id`` of the ``Repository`` to remove
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_repository_aliases(self):
        """Tests if this user can manage ``Id`` aliases for repositories.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Repository`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.repository.RepositoryHierarchySession

    def get_repository_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    repository_hierarchy_id = property(fget=get_repository_hierarchy_id)

    def get_repository_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_repository_view(self):
        """The returns from the repository methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_repository_view(self):
        """A complete view of the ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_root_repository_ids(self):
        """Gets the root repository ``Ids`` in this hierarchy.

        :return: the root repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Node

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryNode


##
# The following methods are from osid.repository.RepositoryHierarchyDesignSession

    def get_repository_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    repository_hierarchy_id = property(fget=get_repository_hierarchy_id)

    def get_repository_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    repository_hierarchy = property(fget=get_repository_hierarchy)

    def can_modify_repository_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def add_root_repository(self, repository_id):
        """Adds a root repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``repository_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_root_repository(self, repository_id):
        """Removes a root repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not a root
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_repositories(self, repository_id):
        """Removes all children from a repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




class RepositoryProxyManager(osid_managers.OsidProxyManager, RepositoryProfile):
    """The repository manager provides access to asset lookup and creation session and provides interoperability tests for
    various aspects of this service.

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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_repository_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_repository_view(self):
        """A complete view of the ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.repository.Repository

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_repository_query(self):
        """Gets a repository query.

        :return: the repository query
        :rtype: ``osid.repository.RepositoryQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryQuery

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList


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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Repository

    def can_update_repositories(self):
        """Tests if this user can update ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Repository`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_repositories(self):
        """Tests if this user can delete ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Repository`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_repository(self, repository_id):
        """Deletes a ``Repository``.

        :param repository_id: the ``Id`` of the ``Repository`` to remove
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_repository_aliases(self):
        """Tests if this user can manage ``Id`` aliases for repositories.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Repository`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.repository.RepositoryHierarchySession

    def get_repository_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    repository_hierarchy_id = property(fget=get_repository_hierarchy_id)

    def get_repository_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_repository_view(self):
        """The returns from the repository methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_repository_view(self):
        """A complete view of the ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_root_repository_ids(self):
        """Gets the root repository ``Ids`` in this hierarchy.

        :return: the root repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList

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

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Node

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryNode


##
# The following methods are from osid.repository.RepositoryHierarchyDesignSession

    def get_repository_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    repository_hierarchy_id = property(fget=get_repository_hierarchy_id)

    def get_repository_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    repository_hierarchy = property(fget=get_repository_hierarchy)

    def can_modify_repository_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def add_root_repository(self, repository_id):
        """Adds a root repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``repository_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_root_repository(self, repository_id):
        """Removes a root repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not a root
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_repositories(self, repository_id):
        """Removes all children from a repository.

        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




class Repository(osid_objects.OsidCatalog, osid_sessions.OsidSession):
    """A repository defines a collection of assets."""

    # WILL THIS EVER BE CALLED DIRECTLY - OUTSIDE OF A MANAGER?
    def __init__(self, provider_manager, catalog, proxy, **kwargs):
        self._provider_manager = provider_manager
        self._catalog = catalog
        osid.OsidObject.__init__(self, self._catalog) # This is to initialize self._object
        osid.OsidSession.__init__(self, proxy) # This is to initialize self._proxy
        self._catalog_id = catalog.get_id()
        self._provider_sessions = kwargs
        self._session_management = AUTOMATIC
        self._repository_view = DEFAULT
        self._object_views = dict()

    def _set_repository_view(self, session):
        """Sets the underlying repository view to match current view"""
        if self._repository_view == FEDERATED:
            try:
                session.use_federated_repository_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_repository_view()
            except AttributeError:
                pass

    def _set_object_view(self, session):
        """Sets the underlying object views to match current view"""
        for obj_name in self._object_views:
            if self._object_views[obj_name] == PLENARY:
                try:
                    getattr(session, 'use_plenary_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_comparative_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _get_provider_session(self, session_name):
        """Returns the requested provider session."""
        if session_name in self._provider_sessions:
            return self._provider_sessions[session_name]
        else:
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_repository')
            if self._proxy is None:
                session = session_class(self._catalog.get_id())
            else:
                session = session_class(self._catalog.get_id(), self._proxy)
            self._set_repository_view(session)
            self._set_object_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[session_name] = session
            return session

    def get_repository_id(self):
        """Gets the Id of this repository."""
        return self._catalog_id

    def get_repository(self):
        """Strange little method to assure conformance for inherited Sessions."""
        return self

    def get_objective_hierarchy_id(self):
        """WHAT am I doing here?"""
        return self._catalog_id

    def get_objective_hierarchy(self):
        """WHAT am I doing here?"""
        return self

    def __getattr__(self, name):
        if '_catalog' in self.__dict__:
            try:
                return self._catalog[name]
            except AttributeError:
                pass
        raise AttributeError

    def close_sessions(self):
        """Close all sessions currently being managed by this Manager to save memory."""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()
        raise IllegalState()

    def use_automatic_session_management(self):
        """Session state will be saved until closed by consumers."""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will always be saved and can not be closed by consumers."""
        # Session state will be saved and can not be closed by consumers 
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved."""
        self._session_management = DISABLED
        self.close_sessions()

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.records.RepositoryRecord
##
# The following methods are from osid.repository.AssetLookupSession

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Repository

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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_asset_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_asset_view(self):
        """A complete view of the ``Asset`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.

        A federated view will include assets in repositories which are
        children of this repository in the repository hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this repository only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Asset

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetList

    def get_assets(self):
        """Gets all ``Assets``.

        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        :return: a list of ``Assets``
        :rtype: ``osid.repository.AssetList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetList

    assets = property(fget=get_assets)


##
# The following methods are from osid.repository.AssetQuerySession

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_search_assets(self):
        """Tests if this user can perform ``Asset`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.

        A federated view will include assets in repositories which are
        children of this repository in the repository hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this repository only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_asset_query(self):
        """Gets an asset query.

        :return: the asset query
        :rtype: ``osid.repository.AssetQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetQuery

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetList


##
# The following methods are from osid.repository.AssetSearchSession

    def get_asset_search(self):
        """Gets an asset search.

        :return: the asset search
        :rtype: ``osid.repository.AssetSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetSearch

    asset_search = property(fget=get_asset_search)

    def get_asset_search_order(self):
        """Gets an asset search order.

        The ``AssetSearchOrder`` is supplied to an ``AssetSearch`` to
        specify the ordering of results.

        :return: the asset search order
        :rtype: ``osid.repository.AssetSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetSearchOrder

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetSearchResults

    def get_asset_query_from_inspector(self, asset_query_inspector):
        """Gets an asset query from an inspector.

        The inspector is available from a ``AssetSearchResults``.

        :param asset_query_inspector: an asset query inspector
        :type asset_query_inspector: ``osid.repository.AssetQueryInspector``
        :return: the asset query
        :rtype: ``osid.repository.AssetQuery``
        :raise: ``NullArgument`` -- ``asset_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``asset_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetQuery


##
# The following methods are from osid.repository.AssetAdminSession

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_create_assets(self):
        """Tests if this user can create ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Asset`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Asset

    def can_update_assets(self):
        """Tests if this user can update ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if ``Asset`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_assets(self):
        """Tests if this user can delete ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Asset`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_asset(self, asset_id):
        """Deletes an ``Asset``.

        :param asset_id: the ``Id`` of the ``Asset`` to remove
        :type asset_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``asset_id`` not found
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_asset_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Asset`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_create_asset_content(self):
        """Tests if this user can create content for ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``AssetContent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Asset`` content creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetContentForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetContent

    def can_update_asset_contents(self):
        """Tests if this user can update ``AssetContent``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``AssetContent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``AssetContent`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetContentForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_asset_contents(self):
        """Tests if this user can delete ``AssetsContents``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``AssetContent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``AssetContent`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_asset_content(self, asset_content_id):
        """Deletes content from an ``Asset``.

        :param asset_content_id: the ``Id`` of the ``AssetContent``
        :type asset_content_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``asset_content_id`` is not found
        :raise: ``NullArgument`` -- ``asset_content_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.repository.AssetNotificationSession

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_register_for_asset_notifications(self):
        """Tests if this user can register for ``Asset`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.

        A federated view will include assets in repositories which are
        children of this repository in the repository hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this repository
        only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def register_for_new_assets(self):
        """Register for notifications of new assets.

        ``AssetReceiver.newAssets()`` is invoked when a new ``Asset``
        appears in this repository.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_new_assets_by_genus_type(self, asset_genus_type):
        """Registers for notification of new assets of the given asset genus type.

        ``AssetReceiver.newAssets()`` is invoked when an asset is
        appears in this repository.

        :param asset_genus_type: the genus type of the ``Asset`` to monitor
        :type asset_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``asset_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_changed_assets(self):
        """Registers for notification of updated assets.

        ``AssetReceiver.changedAssets()`` is invoked when an asset in
        this repository is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_changed_assets_by_genus_type(self, asset_genus_type):
        """Registers for notification of updated assets of the given asset genus type.

        ``AssetReceiver.changedAssets()`` is invoked when an asset in
        this repository is changed.

        :param asset_genus_type: the genus type of the ``Asset`` to monitor
        :type asset_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``asset_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_changed_asset(self, asset_id):
        """Registers for notification of an updated asset.

        ``AssetReceiver.changedAssets()`` is invoked when the specified
        asset in this repository is changed.

        :param asset_id: the ``Id`` of the ``Asset`` to monitor
        :type asset_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_deleted_assets(self):
        """Registers for notification of deleted assets.

        ``AssetReceiver.deletedAssets()`` is invoked when an asset is
        deleted or removed from this repository.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_deleted_assets_by_genus_type(self, asset_genus_type):
        """Registers for notification of deleted assets of the given asset genus type.

        ``AssetReceiver.deletedAssets()`` is invoked when an asset is
        deleted or removed from this repository.

        :param asset_genus_type: the genus type of the ``Asset`` to monitor
        :type asset_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``asset_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_deleted_asset(self, asset_id):
        """Registers for notification of a deleted asset.

        ``AssetReceiver.deletedAssets()`` is invoked when the specified
        asset is deleted or removed from this repository.

        :param asset_id: the ``Id`` of the ``Asset`` to monitor
        :type asset_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def reliable_asset_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def unreliable_asset_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def acknowledge_asset_notification(self, notification_id):
        """Acknowledge an asset notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_repository_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_repository_view(self):
        """A complete view of the ``Asset`` and ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetList

    def get_asset_ids_by_repositories(self, repository_ids):
        """Gets the list of ``Asset Ids`` corresponding to a list of ``Repository`` objects.

        :param repository_ids: list of repository ``Ids``
        :type repository_ids: ``osid.id.IdList``
        :return: list of asset ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``repository_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_assets_by_repositories(self, repository_ids):
        """Gets the list of ``Assets`` corresponding to a list of ``Repository`` objects.

        :param repository_ids: list of repository ``Ids``
        :type repository_ids: ``osid.id.IdList``
        :return: list of assets
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``repository_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList


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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_assignable_repository_ids(self, repository_id):
        """Gets a list of repositories including and under the given repository node in which any asset can be assigned.

        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: list of assignable repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.repository.AssetCompositionSession

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_access_asset_compositions(self):
        """Tests if this user can perform composition lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_asset_composition_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_asset_composition_view(self):
        """A complete view of the returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.

        A federated view will include compositions in repositories which
        are children of this repository in the repository hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this repository only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.repository.AssetList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.CompositionList


##
# The following methods are from osid.repository.AssetCompositionDesignSession

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_compose_assets(self):
        """Tests if this user can manage mapping of ``Assets`` to ``Compositions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as an application hint that may opt not to offer composition
        operations.

        :return: ``false`` if asset composiion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.repository.CompositionLookupSession

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_lookup_compositions(self):
        """Tests if this user can perform ``Composition`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_composition_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_composition_view(self):
        """A complete view of the ``Composition`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.

        A federated view will include compositions in repositories which
        are children of this repository in the repository hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this repository only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_active_composition_view(self):
        """Only active compositions are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_any_status_composition_view(self):
        """All active and inactive compositions are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_sequestered_composition_view(self):
        """The methods in this session omit sequestered compositions.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_unsequestered_composition_view(self):
        """The methods in this session return all compositions, including sequestered compositions.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.repository.Composition

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.CompositionList

    def get_compositions_by_genus_type(self, composition_genus_type):
        """Gets a ``CompositionList`` corresponding to the given composition genus ``Type`` which does not include compositions of types derived from the specified ``Type``.

        :param composition_genus_type: a composition genus type
        :type composition_genus_type: ``osid.type.Type``
        :return: the returned ``Composition list``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NullArgument`` -- ``composition_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.CompositionList

    def get_compositions_by_parent_genus_type(self, composition_genus_type):
        """Gets a ``CompositionList`` corresponding to the given composition genus ``Type`` and include any additional compositions with genus types derived from the specified ``Type``.

        :param composition_genus_type: a composition genus type
        :type composition_genus_type: ``osid.type.Type``
        :return: the returned ``Composition list``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NullArgument`` -- ``composition_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.CompositionList

    def get_compositions_by_record_type(self, composition_record_type):
        """Gets a ``CompositionList`` containing the given composition record ``Type``.

        :param composition_record_type: a composition record type
        :type composition_record_type: ``osid.type.Type``
        :return: the returned ``Composition list``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NullArgument`` -- ``composition_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.CompositionList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.CompositionList

    def get_compositions(self):
        """Gets all ``Compositions``.

        :return: a list of ``Compositions``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.CompositionList

    compositions = property(fget=get_compositions)


##
# The following methods are from osid.repository.CompositionQuerySession

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_search_compositions(self):
        """Tests if this user can perform ``Composition`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.

        A federated view will include compositions in repositories which
        are children of this repository in the repository hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this repository only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_sequestered_composition_view(self):
        """The methods in this session omit sequestered compositions.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_unsequestered_composition_view(self):
        """The methods in this session return all compositions, including sequestered compositions.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_composition_query(self):
        """Gets a composition query.

        :return: the composition query
        :rtype: ``osid.repository.CompositionQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.CompositionQuery

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.CompositionList


##
# The following methods are from osid.repository.CompositionSearchSession

    def get_composition_search(self):
        """Gets a composition search.

        :return: the composition search
        :rtype: ``osid.repository.CompositionSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.CompositionSearch

    composition_search = property(fget=get_composition_search)

    def get_composition_search_order(self):
        """Gets a composition search order.

        The ``CompositionSearchOrder`` is supplied to an
        ``CompositionSearch`` to specify the ordering of results.

        :return: the composition search order
        :rtype: ``osid.repository.CompositionSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.CompositionSearchOrder

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.CompositionSearchResults

    def get_composition_query_from_inspector(self, composition_query_inspector):
        """Gets a composition query from an inspector.

        The inspector is available from a ``CompositionSearchResults``.

        :param composition_query_inspector: a composition query inspector
        :type composition_query_inspector: ``osid.repository.CompositionQueryInspector``
        :return: the composition query
        :rtype: ``osid.repository.CompositionQuery``
        :raise: ``NullArgument`` -- ``composition_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``composition_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.CompositionQuery


##
# The following methods are from osid.repository.CompositionAdminSession

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.

        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.

        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_create_compositions(self):
        """Tests if this user can create ``Compositions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Composition`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Composition`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.CompositionForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Composition

    def can_update_compositions(self):
        """Tests if this user can update ``Compositions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Composition`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Composition`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.CompositionForm

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_compositions(self):
        """Tests if this user can delete ``Compositions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Composition`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Composition`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_composition(self, composition_id):
        """Deletes a ``Composition``.

        :param composition_id: the ``Id`` of the ``Composition`` to remove
        :type composition_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``composition_id`` not found
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def delete_composition_node(self, composition_id):
        """Deletes a ``Composition`` and all contained children.

        :param composition_id: the ``Id`` of the ``Composition`` to remove
        :type composition_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``composition_id`` not found
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_composition_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Compositions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Composition`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


##
# The following methods are from osid.repository.CompositionRepositorySession

    def use_comparative_composition_repository_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_composition_repository_view(self):
        """A complete view of the ``Composition`` and ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def can_lookup_composition_repository_mappings(self):
        """Tests if this user can perform lookups of composition/repository mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.CompositionList

    def get_composition_ids_by_repositories(self, repository_ids):
        """Gets the list of ``Composition``  ``Ids`` corresponding to a list of ``Repository`` objects.

        :param repository_ids: list of repository ``Ids``
        :type repository_ids: ``osid.id.IdList``
        :return: list of composition ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``repository_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_compoitions_by_repositories(self, repository_ids):
        """Gets the list of ``Compositions`` corresponding to a list of ``Repository`` objects.

        :param repository_ids: list of repository ``Ids``
        :type repository_ids: ``osid.id.IdList``
        :return: list of Compositions
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NullArgument`` -- ``repository_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.CompositionList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.RepositoryList


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


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_assignable_repository_ids(self, repository_id):
        """Gets a list of repositories including and under the given repository node in which any composition can be assigned.

        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: list of assignable repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

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

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




class RepositoryList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``RepositoryList`` provides a means for accessing ``Repository`` elements sequentially either
    one at a time or many at a time.

    Examples: while (rl.hasNext()) { Repository repository =
    rl.getNextRepository(); }


    or
      while (rl.hasNext()) {
           Repository[] repositories = rl.getNextRepositories(rl.available());
      }



    """

    def get_next_repository(self):
        """Gets the next ``Repository`` in this list.

        :return: the next ``Repository`` in this list. The ``has_next()`` method should be used to test that a next ``Repository`` is available before calling this method.
        :rtype: ``osid.repository.Repository``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Repository

    next_repository = property(fget=get_next_repository)

    def get_next_repositories(self, n):
        """Gets the next set of ``Repository`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Repository`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Repository`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.repository.Repository``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Repository


