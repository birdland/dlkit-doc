# -*- coding: utf-8 -*-
"""Installation Open Service Interface Definitions
installation version 3.0.0

The Installation OSID describes two categories of services. One service
is to find, retrieve and manage installation packages in remote
repositories, or ``Depots``. The other service is to manage
installations (downloaded packages) on ``Sites``. Sites are generally,
but not required to be, on local disk.

Packages

``Packages`` define a set of core data and map to an independently
retrieved and managed data stream. The data stream may be an archive
file of a certain format. A ``Package`` may include multiple formats.
``Packages`` also may have other packages on which it depends for
operation. Each version of a software package is a separate ``Package``
identified by a separate ``Id``. Version chains may be defined to
communicate newer available versions.

Installations

An installed package on a ``Site`` is an ``Installation``.
``Installations`` are similar to ``Packages`` with a different set of
core data and no access to the archive stream. ``Installations`` may
also have dependencies and versioning.

Methods are defined to check for updates available in a ``Depot`` for an
``Installation,`` at which time the consumer may elect to install the
new ``Package``  ``Id`` for the updated version. Depending on whether a
provider keeps the older version around, delete operations may be
available for outdated versions and allow for dependency management
across versions.

``Sites`` are assumed to be fixed to the runtime environment and are not
manageable through the Installation OSID. As such, ``Sites`` are not
modeled as ``OsidCatalogs`` and a single ``Installation`` may belong to
only one ``Site``.

Depot Cataloging

``Packages`` are organized into ``Depots`` for categorization and
federation using the OSID hierarchy pattern. Dynamic virtual ``Depots``
may be created by filtering on various ``Package`` attributes.

Versions

The Installation OSID defines an ``OsidPrimitive`` for a ``Version``. A
``Version`` describes a version number.

Orchestration

The Installation OSID may be orchestrated with a Configuration OSID to
retrieve or manage installation configurations.

Sub Packages

The Installation OSID contains an Installation Batch OSID for managing
``Packages`` and ``Installations`` in bulk.

"""
from ..osid import managers as osid_managers
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class InstallationProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_installation_lookup(self):
        """Tests if an installation lookup service is supported.

        :return: true if installation lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_installation_query(self):
        """Tests if an installation query service is supported.

        :return: true if installation query is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_installation_search(self):
        """Tests if an installation search service is supported.

        :return: ``true`` if installation search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_installation_management(self):
        """Tests if an installation management service is supported.

        :return: ``true`` if package management is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_installation_update(self):
        """Tests if an installation update service is supported.

        :return: ``true`` if package update is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_installation_notification(self):
        """Tests if installation notification is supported.
        Messages may be sent when installations are installed or
        removed.

        :return: ``true`` if installation notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_site_lookup(self):
        """Tests if a site lookup service is supported.

        :return: true if site lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_package_lookup(self):
        """Tests if a package lookup service is supported.
        A package lookup service defines methods to access packages.

        :return: true if package lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_package_query(self):
        """Tests if querying packages is supported.

        :return: ``true`` if packages query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_package_search(self):
        """Tests if a package search service is supported.

        :return: ``true`` if package search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_package_admin(self):
        """Tests if a package administrative service is supported.

        :return: ``true`` if package admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_package_notification(self):
        """Tests if package notification is supported.
        Messages may be sent when packages are created, modified, or
        deleted.

        :return: ``true`` if package notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_package_depot(self):
        """Tests if a package to depot lookup session is available.

        :return: ``true`` if package depot lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_package_depot_assignment(self):
        """Tests if a package to depot assignment session is available.

        :return: ``true`` if package depot assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_package_smart_depot(self):
        """Tests if package smart depots are available.

        :return: ``true`` if package smart depots are supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_depot_lookup(self):
        """Tests if a depot lookup service is supported.

        :return: ``true`` if depot lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_depot_query(self):
        """Tests if a depot query service is supported.

        :return: ``true`` if depot query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_depot_search(self):
        """Tests if a depot search service is supported.

        :return: ``true`` if depot search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_depot_admin(self):
        """Tests if a depot administrative service is supported.

        :return: ``true`` if depot admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_depot_notification(self):
        """Tests if depot notification is supported.
        Messages may be sent when depots are created, modified, or
        deleted.

        :return: ``true`` if depot notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_depot_hierarchy(self):
        """Tests if a depot hierarchy traversal is supported.

        :return: ``true`` if a depot hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_depot_hierarchy_design(self):
        """Tests if depot hierarchy design is supported.

        :return: ``true`` if a depot hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_installation_batch(self):
        """Tests if an installation batch service is supported.

        :return: ``true`` if an installation batch service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_installation_record_types(self):
        """Gets the supported ``Installation`` record types.

        :return: a list containing the supported ``Installation`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    installation_record_types = property(fget=get_installation_record_types)

    def supports_installation_record_type(self, installation_record_type):
        """Tests if the given ``Installation`` record type is supported.

        :param installation_record_type: a ``Type`` indicating an ``Installation`` record type
        :type installation_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``installation_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_installation_search_record_types(self):
        """Gets the supported ``Installation`` search record types.

        :return: a list containing the supported ``Installation`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    installation_search_record_types = property(fget=get_installation_search_record_types)

    def supports_installation_search_record_type(self, installation_search_record_type):
        """Tests if the given ``Installation`` search record type is supported.

        :param installation_search_record_type: a ``Type`` indicating an ``Installation`` search record type
        :type installation_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``installation_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_site_record_types(self):
        """Gets the supported ``Site`` record types.

        :return: a list containing the supported ``Site`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    site_record_types = property(fget=get_site_record_types)

    def supports_site_record_type(self, site_record_type):
        """Tests if the given ``Site`` record type is supported.

        :param site_record_type: a ``Type`` indicating a ``Site`` record type
        :type site_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``site_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_package_record_types(self):
        """Gets the supported ``Package`` record types.

        :return: a list containing the supported ``Package`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    package_record_types = property(fget=get_package_record_types)

    def supports_package_record_type(self, package_record_type):
        """Tests if the given ``Package`` record type is supported.

        :param package_record_type: a ``Type`` indicating a ``Package`` record type
        :type package_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``package_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_package_search_record_types(self):
        """Gets the supported ``Package`` search record types.

        :return: a list containing the supported ``Package`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    package_search_record_types = property(fget=get_package_search_record_types)

    def supports_package_search_record_type(self, package_search_record_type):
        """Tests if the given ``Package`` search record type is supported.

        :param package_search_record_type: a ``Type`` indicating a ``Package`` search record type
        :type package_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``package_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_installation_content_record_types(self):
        """Gets the supported ``InstallationContent`` record types.

        :return: a list containing the supported ``InstallationContent`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    installation_content_record_types = property(fget=get_installation_content_record_types)

    def supports_installation_content_record_type(self, installation_content_record_type):
        """Tests if the given ``InstallationContent`` record type is supported.

        :param installation_content_record_type: a ``Type`` indicating an ``InstallationContent`` record type
        :type installation_content_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``installation_content_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_depot_record_types(self):
        """Gets the supported ``Depot`` record types.

        :return: a list containing the supported ``Depot`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    depot_record_types = property(fget=get_depot_record_types)

    def supports_depot_record_type(self, depot_record_type):
        """Tests if the given ``Depot`` record type is supported.

        :param depot_record_type: a ``Type`` indicating a ``Depot`` type
        :type depot_record_type: ``osid.type.Type``
        :return: ``true`` if the given depot record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``depot_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_depot_search_record_types(self):
        """Gets the supported depot search record types.

        :return: a list containing the supported ``Depot`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    depot_search_record_types = property(fget=get_depot_search_record_types)

    def supports_depot_search_record_type(self, depot_search_record_type):
        """Tests if the given depot search record type is supported.

        :param depot_search_record_type: a ``Type`` indicating a ``Depot`` search record type
        :type depot_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``depot_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class InstallationManager(osid_managers.OsidManager, osid_sessions.OsidSession, InstallationProfile):

    def get_installation_lookup_session(self):
        """Gets the ``OsidSession`` associated with the installation lookup service.

        :return: an ``InstallationLookupSession``
        :rtype: ``osid.installation.InstallationLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    installation_lookup_session = property(fget=get_installation_lookup_session)

    def get_installation_lookup_session_for_site(self, site_id):
        """Gets the ``OsidSession`` associated with the installation lookup service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :return: ``an _installation_lookup_session``
        :rtype: ``osid.installation.InstallationLookupSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_installation_query_session(self):
        """Gets the ``OsidSession`` associated with the installation query service.

        :return: an ``InstallationQuerySession``
        :rtype: ``osid.installation.InstallationQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    installation_query_session = property(fget=get_installation_query_session)

    def get_installation_query_session_for_site(self, site_id):
        """Gets the ``OsidSession`` associated with the installation query service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :return: ``an _installation_query_session``
        :rtype: ``osid.installation.InstallationQuerySession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_installation_search_session(self):
        """Gets the ``OsidSession`` associated with the installation search service.

        :return: an ``InstallationSearchSession``
        :rtype: ``osid.installation.InstallationSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    installation_search_session = property(fget=get_installation_search_session)

    def get_installation_search_session_for_site(self, site_id):
        """Gets the ``OsidSession`` associated with the installation search service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :return: ``an _installation_search_session``
        :rtype: ``osid.installation.InstallationSearchSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_installation_management_session(self):
        """Gets the ``OsidSession`` associated with the installation management service.

        :return: an ``InstallationAdminSession``
        :rtype: ``osid.installation.InstallationManagementSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_management()`` is ``false``

        """
        raise UNIMPLEMENTED()

    installation_management_session = property(fget=get_installation_management_session)

    def get_installation_management_session_for_site(self, site_id):
        """Gets the ``OsidSession`` associated with the installation management service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :return: ``an _installation_admin_session``
        :rtype: ``osid.installation.InstallationManagementSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_management()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_installation_update_session(self):
        """Gets the ``OsidSession`` associated with the installation update service.

        :return: an ``InstallationAdminSession``
        :rtype: ``osid.installation.InstallationUpdateSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_update()`` is ``false``

        """
        raise UNIMPLEMENTED()

    installation_update_session = property(fget=get_installation_update_session)

    def get_installation_update_session_for_site(self, site_id):
        """Gets the ``OsidSession`` associated with the installation update service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :return: ``an _installation_update_session``
        :rtype: ``osid.installation.InstallationUpdateSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_update()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_installation_notification_session(self, installation_receiver):
        """Gets the notification session for notifications pertaining to installation changes.

        :param installation_receiver: the installation receiver
        :type installation_receiver: ``osid.installation.InstallationReceiver``
        :return: an ``InstallationNotificationSession``
        :rtype: ``osid.installation.InstallationNotificationSession``
        :raise: ``NullArgument`` -- ``installation_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_installation_notification_session_for_site(self, installation_receiver, site_id):
        """Gets the ``OsidSession`` associated with the installation notification service for the given site.

        :param installation_receiver: the installation receiver
        :type installation_receiver: ``osid.installation.InstallationReceiver``
        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :return: ``an _installation_notification_session``
        :rtype: ``osid.installation.InstallationNotificationSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``installation_receiver`` or ``site_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_site_lookup_session(self):
        """Gets the ``OsidSession`` associated with the site lookup service.

        :return: a ``SiteLookupSession``
        :rtype: ``osid.installation.SiteLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_site_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    site_lookup_session = property(fget=get_site_lookup_session)

    def get_package_lookup_session(self):
        """Gets the ``OsidSession`` associated with the package lookup service.

        :return: a ``PackageLookupSession``
        :rtype: ``osid.installation.PackageLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    package_lookup_session = property(fget=get_package_lookup_session)

    def get_package_lookup_session_for_depot(self, depot_id):
        """Gets the ``OsidSession`` associated with the package lookup service for the given depot.

        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :return: ``a PackageLookupSession``
        :rtype: ``osid.installation.PackageLookupSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_package_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_query_session(self):
        """Gets the ``OsidSession`` associated with the package query service.

        :return: a ``PackageQuerySession``
        :rtype: ``osid.installation.PackageQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    package_query_session = property(fget=get_package_query_session)

    def get_package_query_session_for_depot(self, depot_id):
        """Gets the ``OsidSession`` associated with the package query service for the given depot.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: a ``PackageQuerySession``
        :rtype: ``osid.installation.PackageQuerySession``
        :raise: ``NotFound`` -- no ``Depot`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_search_session(self):
        """Gets the ``OsidSession`` associated with the package search service.

        :return: a ``PackageSearchSession``
        :rtype: ``osid.installation.PackageSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    package_search_session = property(fget=get_package_search_session)

    def get_package_search_session_for_depot(self, depot_id):
        """Gets the ``OsidSession`` associated with the package search service for the given depot.

        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :return: ``a PackageSearchSession``
        :rtype: ``osid.installation.PackageSearchSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_package_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_admin_session(self):
        """Gets the ``OsidSession`` associated with the package administration service.

        :return: a ``PackageAdminSession``
        :rtype: ``osid.installation.PackageAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    package_admin_session = property(fget=get_package_admin_session)

    def get_package_admin_session_for_depot(self, depot_id):
        """Gets the ``OsidSession`` associated with the package admin service for the given depot.

        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :return: ``a PackageAdminSession``
        :rtype: ``osid.installation.PackageAdminSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_package_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_notification_session(self, package_receiver):
        """Gets the notification session for notifications pertaining to package changes.

        :param package_receiver: the package receiver
        :type package_receiver: ``osid.installation.PackageReceiver``
        :return: a ``PackageNotificationSession``
        :rtype: ``osid.installation.PackageNotificationSession``
        :raise: ``NullArgument`` -- ``package_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_notification_session_for_depot(self, package_receiver, depot_id):
        """Gets the ``OsidSession`` associated with the package notification service for the given depot.

        :param package_receiver: the package receiver
        :type package_receiver: ``osid.installation.PackageReceiver``
        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :return: ``a PackageNotificationSession``
        :rtype: ``osid.installation.PackageNotificationSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``package_receiver`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_package_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_depot_session(self):
        """Gets the session for retrieving package to depot mappings.

        :return: a ``PackageDepotSession``
        :rtype: ``osid.installation.PackageDepotSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_depot()`` is ``false``

        """
        raise UNIMPLEMENTED()

    package_depot_session = property(fget=get_package_depot_session)

    def get_package_depot_assignment_session(self):
        """Gets the session for assigning package to depot mappings.

        :return: a ``PackageDepotAssignmentSession``
        :rtype: ``osid.installation.PackageDepotSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_depot_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    package_depot_assignment_session = property(fget=get_package_depot_assignment_session)

    def get_package_smart_depot_session(self, depot_id):
        """Gets the session for managing dynamic package depot.

        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :return: a ``PackageSmartDepotSession``
        :rtype: ``osid.installation.PackageSmartDepotSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_smart_depot()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_depot_lookup_session(self):
        """Gets the OsidSession associated with the depot lookup service.

        :return: a ``DepotLookupSession``
        :rtype: ``osid.installation.DepotLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_lookup() is false``

        """
        raise UNIMPLEMENTED()

    depot_lookup_session = property(fget=get_depot_lookup_session)

    def get_depot_query_session(self):
        """Gets the depot query session.

        :return: a ``DepotQuerySession``
        :rtype: ``osid.installation.DepotQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    depot_query_session = property(fget=get_depot_query_session)

    def get_depot_search_session(self):
        """Gets the OsidSession associated with the depot search service.

        :return: a ``DepotSearchSession``
        :rtype: ``osid.installation.DepotSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_search() is false``

        """
        raise UNIMPLEMENTED()

    depot_search_session = property(fget=get_depot_search_session)

    def get_depot_admin_session(self):
        """Gets the OsidSession associated with the depot administration service.

        :return: a ``DepotAdminSession``
        :rtype: ``osid.installation.DepotAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_admin() is false``

        """
        raise UNIMPLEMENTED()

    depot_admin_session = property(fget=get_depot_admin_session)

    def get_depot_notification_session(self, depot_receiver):
        """Gets the notification session for notifications pertaining to depot service changes.

        :param depot_receiver: the depot receiver
        :type depot_receiver: ``osid.installation.DepotReceiver``
        :return: a ``DepotNotificationSession``
        :rtype: ``osid.installation.DepotNotificationSession``
        :raise: ``NullArgument`` -- ``depot_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_notification() is false``

        """
        raise UNIMPLEMENTED()

    def get_depot_hierarchy_session(self):
        """Gets the session traversing depot hierarchies.

        :return: a ``DepotHierarchySession``
        :rtype: ``osid.installation.DepotHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_hierarchy() is false``

        """
        raise UNIMPLEMENTED()

    depot_hierarchy_session = property(fget=get_depot_hierarchy_session)

    def get_depot_hierarchy_design_session(self):
        """Gets the session designing depot hierarchies.

        :return: a ``DepotHierarchyDesignSession``
        :rtype: ``osid.installation.DepotHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_hierarchy_design() is false``

        """
        raise UNIMPLEMENTED()

    depot_hierarchy_design_session = property(fget=get_depot_hierarchy_design_session)

    def get_installation_batch_manager(self):
        """Gets an ``InstallationBatchManager``.

        :return: an ``InstallationBatchManager``
        :rtype: ``osid.installation.batch.InstallationBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_batch() is false``

        """
        raise UNIMPLEMENTED()

    installation_batch_manager = property(fget=get_installation_batch_manager)


##
# The following methods are from osid.installation.DepotLookupSession

    def can_lookup_depots(self):
        """Tests if this user can perform ``Depot`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_depot_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_depot_view(self):
        """A complete view of the ``Depot`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_depot(self, depot_id):
        """Gets the ``Depot`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Depot`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Depot`` and retained for compatility.

        :param depot_id: ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: the depot
        :rtype: ``osid.installation.Depot``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depots_by_ids(self, depot_ids):
        """Gets a ``DepotList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the depots
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Depot`` objects may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param depot_ids: the list of ``Ids`` to retrieve
        :type depot_ids: ``osid.id.IdList``
        :return: the returned ``Depot`` list
        :rtype: ``osid.installation.DepotList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``depot_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depots_by_genus_type(self, depot_genus_type):
        """Gets a ``DepotList`` corresponding to the given depot genus ``Type`` which does not include depots of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known depots or
        an error results. Otherwise, the returned list may contain only
        those depots that are accessible through this session.

        :param depot_genus_type: a depot genus type
        :type depot_genus_type: ``osid.type.Type``
        :return: the returned ``Depot`` list
        :rtype: ``osid.installation.DepotList``
        :raise: ``NullArgument`` -- ``depot_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depots_by_parent_genus_type(self, depot_genus_type):
        """Gets a ``DepotList`` corresponding to the given depot genus ``Type`` and include any additional depots with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known depots or
        an error results. Otherwise, the returned list may contain only
        those depots that are accessible through this session.

        :param depot_genus_type: a depot genus type
        :type depot_genus_type: ``osid.type.Type``
        :return: the returned ``Depot`` list
        :rtype: ``osid.installation.DepotList``
        :raise: ``NullArgument`` -- ``depot_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depots_by_record_type(self, depot_record_type):
        """Gets a ``DepotList`` containing the given depot record ``Type``.
        In plenary mode, the returned list contains all known depots or
        an error results. Otherwise, the returned list may contain only
        those depots that are accessible through this session.

        :param depot_record_type: a depot record type
        :type depot_record_type: ``osid.type.Type``
        :return: the returned ``Depot`` list
        :rtype: ``osid.installation.DepotList``
        :raise: ``NullArgument`` -- ``depot_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depots_by_provider(self, resource_id):
        """Gets a ``DepotList`` for the given provider ````.
        In plenary mode, the returned list contains all known depots or
        an error results. Otherwise, the returned list may contain only
        those depots that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Depot`` list
        :rtype: ``osid.installation.DepotList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depots(self):
        """Gets all ``Depots``.
        In plenary mode, the returned list contains all known depots or
        an error results. Otherwise, the returned list may contain only
        those depots that are accessible through this session.

        :return: a ``DepotList``
        :rtype: ``osid.installation.DepotList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    depots = property(fget=get_depots)


##
# The following methods are from osid.installation.DepotQuerySession

    def can_search_depots(self):
        """Tests if this user can perform ``Depot`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_depot_query(self):
        """Gets a depot query.

        :return: a depot query
        :rtype: ``osid.installation.DepotQuery``

        """
        raise UNIMPLEMENTED()

    depot_query = property(fget=get_depot_query)

    def get_depots_by_query(self, depot_query):
        """Gets a list of ``Depot`` objects matching the given depot query.

        :param depot_query: the depot query
        :type depot_query: ``osid.installation.DepotQuery``
        :return: the returned ``DepotList``
        :rtype: ``osid.installation.DepotList``
        :raise: ``NullArgument`` -- ``depot_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``depot_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.DepotSearchSession

    def get_depot_search(self):
        """Gets a depot search.

        :return: a depot search
        :rtype: ``osid.installation.DepotSearch``

        """
        raise UNIMPLEMENTED()

    depot_search = property(fget=get_depot_search)

    def get_depot_search_order(self):
        """Gets a depot search order.
        The ``DepotSearchOrder`` is supplied to a ``DepotSearch`` to
        specify the ordering of results.

        :return: the depot search order
        :rtype: ``osid.installation.DepotSearchOrder``

        """
        raise UNIMPLEMENTED()

    depot_search_order = property(fget=get_depot_search_order)

    def get_depots_by_search(self, depot_query, depot_search):
        """Gets the search results matching the given search query using the given search.

        :param depot_query: the depot query
        :type depot_query: ``osid.installation.DepotQuery``
        :param depot_search: the depot search
        :type depot_search: ``osid.installation.DepotSearch``
        :return: the depot search results
        :rtype: ``osid.installation.DepotSearchResults``
        :raise: ``NullArgument`` -- ``depot_query`` or ``depot_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``depot_query`` or ``depot_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_depot_query_from_inspector(self, depot_query_inspector):
        """Gets a depot query from an inspector.
        The inspector is available from a ``DepotSearchResults``.

        :param depot_query_inspector: a depot query inspector
        :type depot_query_inspector: ``osid.installation.DepotQueryInspector``
        :return: the depot query
        :rtype: ``osid.installation.DepotQuery``
        :raise: ``NullArgument`` -- ``depot_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``depot_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.DepotAdminSession

    def can_create_depots(self):
        """Tests if this user can create ``Depots``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Depot``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Depot`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_depot_with_record_types(self, depot_record_types):
        """Tests if this user can create a single ``Depot`` using the desired record types.
        While ``InstallationManager.getDepotRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Depot``.
        Providing an empty array tests if a ``Depot`` can be created
        with no records.

        :param depot_record_types: array of depot record types
        :type depot_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Depot`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``depot_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_depot_form_for_create(self, depot_record_types):
        """Gets the depot form for creating new depots.
        A new form should be requested for each create transaction.

        :param depot_record_types: array of depot record types
        :type depot_record_types: ``osid.type.Type[]``
        :return: the depot form
        :rtype: ``osid.installation.DepotForm``
        :raise: ``NullArgument`` -- ``depot_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_depot(self, depot_form):
        """Creates a new ``Depot``.

        :param depot_form: the form for this ``Depot``
        :type depot_form: ``osid.installation.DepotForm``
        :return: the new ``Depot``
        :rtype: ``osid.installation.Depot``
        :raise: ``IllegalState`` -- ``depot_form`` already used for a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``depot_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``depot_form`` did not originate from ``get_depot_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_depots(self):
        """Tests if this user can update ``Depots``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Depot``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Depot`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_update_depot(self, depot_id):
        """Tests if this user can update a specified ``Depot``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating the
        ``Depot`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: ``false`` if depot modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_depot_form_for_update(self, depot_id):
        """Gets the depot form for updating an existing depot.
        A new depot form should be requested for each update
        transaction.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: the depot form
        :rtype: ``osid.installation.DepotForm``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_depot(self, depot_form):
        """Updates an existing depot.

        :param depot_form: the form containing the elements to be updated
        :type depot_form: ``osid.installation.DepotForm``
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``depot_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``depot_form`` did not originate from ``get_depot_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_depots(self):
        """Tests if this user can delete depots.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Depot``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Depot`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_delete_depot(self, depot_id):
        """Tests if this user can delete a specified ``Depot``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting the
        ``Depot`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: ``false`` if deletion of this ``Depot`` is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def delete_depot(self, depot_id):
        """Deletes a ``Depot``.

        :param depot_id: the ``Id`` of the ``Depot`` to remove
        :type depot_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_depot_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Depots``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Depot`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_depot(self, depot_id, alias_id):
        """Adds an ``Id`` to a ``Depot`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Depot`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another depot it is
        reassigned to the given depot ``Id``.

        :param depot_id: the ``Id`` of a ``Depot``
        :type depot_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.DepotNotificationSession

    def can_register_for_depot_notifications(self):
        """Tests if this user can register for ``Depot`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_depots(self):
        """Register for notifications of new depots.
        ``DepotReceiver.newDepot()`` is invoked when a new ``Depot`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_depot_ancestors(self, depot_id):
        """Registers for notification if an ancestor is added to the specified depot in the depot hierarchy.
        ``DepotReceiver.newDepotAncestor()`` is invoked when the
        specified depot experiences an addition in ancestry.

        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_depot_descendants(self, depot_id):
        """Registers for notification if a descendant is added to the specified depot in the depot hierarchy.
        ``DepotReceiver.newDepotDescendant()`` is invoked when the
        specified depot experiences an addition in descendants.

        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_depots(self):
        """Registers for notification of updated depots.
        ``DepotReceiver.changedDepot()`` is invoked when a depot is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_depot(self, depot_id):
        """Registers for notification of an updated depot.
        ``DepotReceiver.changedDepot()`` is invoked when the specified
        depot is changed.

        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_depots(self):
        """Registers for notification of deleted depots.
        ``DepotReceiver.deletedDepot()`` is invoked when a depot is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_depot(self, depot_id):
        """Registers for notification of a deleted depot.
        ``DepotReceiver.deletedDepot()`` is invoked when the specified
        depot is deleted.

        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_depot_ancestors(self, depot_id):
        """Registers for notification if an ancestor is removed from the specified depot in the depot hierarchy.
        ``DepotReceiver.deletedDepotAncestor()`` is invoked when the
        specified depot experiences a removal of an ancestor.

        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_depot_descendants(self, depot_id):
        """Registers for notification if a descendant is removed from fthe specified depot in the depot hierarchy.
        ``DepotReceiver.deletedDepotDescednant()`` is invoked when the
        specified depot experiences a removal of one of its descendants.

        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.DepotHierarchySession

    def get_depot_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    depot_hierarchy_id = property(fget=get_depot_hierarchy_id)

    def get_depot_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    depot_hierarchy = property(fget=get_depot_hierarchy)

    def can_access_depot_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer hierrachy
        traversal operations to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_depot_ids(self):
        """Gets the root depot ``Ids`` in this hierarchy.

        :return: the root depot ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_depot_ids = property(fget=get_root_depot_ids)

    def get_root_depots(self):
        """Gets the root depots in this depot hierarchy.

        :return: the root depots
        :rtype: ``osid.installation.DepotList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_depots = property(fget=get_root_depots)

    def has_parent_depots(self, depot_id):
        """Tests if the ``Depot`` has any parents.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if the depot has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_depot(self, id_, depot_id):
        """Tests if an ``Id`` is a direct parent of a depot.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``depot_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_depot_ids(self, depot_id):
        """Gets the parent ``Ids`` of the given depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the depot
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_depots(self, depot_id):
        """Gets the parents of the given depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: the parents of the depot
        :rtype: ``osid.installation.DepotList``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_depot(self, id_, depot_id):
        """Tests if an ``Id`` is an ancestor of a depot.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``depot_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_depots(self, depot_id):
        """Tests if a depot has any children.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if the ``depot_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_depot(self, id_, depot_id):
        """Tests if a depot is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``depot_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_depot_ids(self, depot_id):
        """Gets the child ``Ids`` of the given depot.

        :param depot_id: the ``Id`` to query
        :type depot_id: ``osid.id.Id``
        :return: the children of the depot
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_depots(self, depot_id):
        """Gets the children of the given depot.

        :param depot_id: the ``Id`` to query
        :type depot_id: ``osid.id.Id``
        :return: the children of the depot
        :rtype: ``osid.installation.DepotList``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_depot(self, id_, depot_id):
        """Tests if an ``Id`` is a descendant of a depot.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``depot_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depot_node_ids(self, depot_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given depot.

        :param depot_id: the ``Id`` to query
        :type depot_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a depot node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depot_nodes(self, depot_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given depot.

        :param depot_id: the ``Id`` to query
        :type depot_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a depot node
        :rtype: ``osid.installation.DepotNode``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.DepotHierarchyDesignSession

    def can_modify_depot_hierarchy(self):
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

    def add_root_depot(self, depot_id):
        """Adds a root depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``depot_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_depot(self, depot_id):
        """Removes a root depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``depot_id`` is not a root
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_depot(self, depot_id, child_id):
        """Adds a child to a depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``depot_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``depot_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_depot(self, depot_id, child_id):
        """Removes a child from a depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``depot_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``depot_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_depots(self, depot_id):
        """Removes all children from a depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class InstallationProxyManager(osid_managers.OsidProxyManager, InstallationProfile):

    def get_installation_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the installation lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InstallationLookupSession``
        :rtype: ``osid.installation.InstallationLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_installation_lookup_session_for_site(self, site_id, proxy):
        """Gets the ``OsidSession`` associated with the installation lookup service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _installation_lookup_session``
        :rtype: ``osid.installation.InstallationLookupSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_installation_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the installation query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InstallationQuerySession``
        :rtype: ``osid.installation.InstallationQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_installation_query_session_for_site(self, site_id, proxy):
        """Gets the ``OsidSession`` associated with the installation query service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _installation_query_session``
        :rtype: ``osid.installation.InstallationQuerySession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_installation_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the installation search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InstallationSearchSession``
        :rtype: ``osid.installation.InstallationSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_installation_search_session_for_site(self, site_id, proxy):
        """Gets the ``OsidSession`` associated with the installation search service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _installation_search_session``
        :rtype: ``osid.installation.InstallationSearchSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_installation_management_session(self, proxy):
        """Gets the ``OsidSession`` associated with the installation management service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InstallationAdminSession``
        :rtype: ``osid.installation.InstallationManagementSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_management()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_installation_management_session_for_site(self, site_id, proxy):
        """Gets the ``OsidSession`` associated with the installation management service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _installation_admin_session``
        :rtype: ``osid.installation.InstallationManagementSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_management()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_installation_update_session(self, proxy):
        """Gets the ``OsidSession`` associated with the installation update service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InstallationAdminSession``
        :rtype: ``osid.installation.InstallationUpdateSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_update()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_installation_update_session_for_site(self, site_id, proxy):
        """Gets the ``OsidSession`` associated with the installation update service for the given site.

        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _installation_update_session``
        :rtype: ``osid.installation.InstallationUpdateSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``site_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_update()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_installation_notification_session(self, installation_receiver, proxy):
        """Gets the notification session for notifications pertaining to installation changes.

        :param installation_receiver: the installation receiver
        :type installation_receiver: ``osid.installation.InstallationReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InstallationNotificationSession``
        :rtype: ``osid.installation.InstallationNotificationSession``
        :raise: ``NullArgument`` -- ``installation_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_installation_notification_session_for_site(self, installation_receiver, site_id, proxy):
        """Gets the ``OsidSession`` associated with the installation notification service for the given site.

        :param installation_receiver: the installation receiver
        :type installation_receiver: ``osid.installation.InstallationReceiver``
        :param site_id: the ``Id`` of the site
        :type site_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _installation_notification_session``
        :rtype: ``osid.installation.InstallationNotificationSession``
        :raise: ``NotFound`` -- ``site_id`` not found
        :raise: ``NullArgument`` -- ``installation_receiver, site_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_installation_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_site_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the site lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SiteLookupSession``
        :rtype: ``osid.installation.SiteLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_site_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the package lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageLookupSession``
        :rtype: ``osid.installation.PackageLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_lookup_session_for_depot(self, depot_id, proxy):
        """Gets the ``OsidSession`` associated with the package lookup service for the given depot.

        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a PackageLookupSession``
        :rtype: ``osid.installation.PackageLookupSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_package_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the package query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageQuerySession``
        :rtype: ``osid.installation.PackageQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_query_session_for_depot(self, depot_id, proxy):
        """Gets the ``OsidSession`` associated with the package query service for the given depot.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageQuerySession``
        :rtype: ``osid.installation.PackageQuerySession``
        :raise: ``NotFound`` -- no ``Depot`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``depot_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the package search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageSearchSession``
        :rtype: ``osid.installation.PackageSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_search_session_for_depot(self, depot_id, proxy):
        """Gets the ``OsidSession`` associated with the package search service for the given depot.

        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a PackageSearchSession``
        :rtype: ``osid.installation.PackageSearchSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_package_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the package administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageAdminSession``
        :rtype: ``osid.installation.PackageAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_admin_session_for_depot(self, depot_id, proxy):
        """Gets the ``OsidSession`` associated with the package admin service for the given depot.

        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a PackageAdminSession``
        :rtype: ``osid.installation.PackageAdminSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_package_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_notification_session(self, package_receiver, proxy):
        """Gets the notification session for notifications pertaining to package changes.

        :param package_receiver: the package receiver
        :type package_receiver: ``osid.installation.PackageReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageNotificationSession``
        :rtype: ``osid.installation.PackageNotificationSession``
        :raise: ``NullArgument`` -- ``package_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_notification_session_for_depot(self, package_receiver, depot_id, proxy):
        """Gets the ``OsidSession`` associated with the package notification service for the given depot.

        :param package_receiver: the package receiver
        :type package_receiver: ``osid.installation.PackageReceiver``
        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a PackageNotificationSession``
        :rtype: ``osid.installation.PackageNotificationSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``package_receiver, depot_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_package_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_depot_session(self, proxy):
        """Gets the session for retrieving package to depot mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageDepotSession``
        :rtype: ``osid.installation.PackageDepotSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_depot()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_depot_assignment_session(self, proxy):
        """Gets the session for assigning package to depot mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageDepotAssignmentSession``
        :rtype: ``osid.installation.PackageDepotSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_depot_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_package_smart_depot_session(self, depot_id, proxy):
        """Gets the session for managing dynamic package depot.

        :param depot_id: the ``Id`` of the depot
        :type depot_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``PackageSmartDepotSession``
        :rtype: ``osid.installation.PackageSmartDepotSession``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_package_smart_depot()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_depot_lookup_session(self, proxy):
        """Gets the OsidSession associated with the depot lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DepotLookupSession``
        :rtype: ``osid.installation.DepotLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_lookup() is false``

        """
        raise UNIMPLEMENTED()

    def get_depot_query_session(self, proxy):
        """Gets the depot query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DepotQuerySession``
        :rtype: ``osid.installation.DepotQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_depot_search_session(self, proxy):
        """Gets the OsidSession associated with the depot search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DepotSearchSession``
        :rtype: ``osid.installation.DepotSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_search() is false``

        """
        raise UNIMPLEMENTED()

    def get_depot_admin_session(self, proxy):
        """Gets the OsidSession associated with the depot administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DepotAdminSession``
        :rtype: ``osid.installation.DepotAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_admin() is false``

        """
        raise UNIMPLEMENTED()

    def get_depot_notification_session(self, depot_receiver, proxy):
        """Gets the notification session for notifications pertaining to depot service changes.

        :param depot_receiver: the depot receiver
        :type depot_receiver: ``osid.installation.DepotReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DepotNotificationSession``
        :rtype: ``osid.installation.DepotNotificationSession``
        :raise: ``NullArgument`` -- ``depot_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_notification() is false``

        """
        raise UNIMPLEMENTED()

    def get_depot_hierarchy_session(self, proxy):
        """Gets the session traversing depot hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DepotHierarchySession``
        :rtype: ``osid.installation.DepotHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_hierarchy() is false``

        """
        raise UNIMPLEMENTED()

    def get_depot_hierarchy_design_session(self, proxy):
        """Gets the session designing depot hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``DepotHierarchyDesignSession``
        :rtype: ``osid.installation.DepotHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_depot_hierarchy_design() is false``

        """
        raise UNIMPLEMENTED()

    def get_installation_batch_proxy_manager(self):
        """Gets an ``InstallationBatchProxyManager``.

        :return: an ``InstallationBatchProxyManager``
        :rtype: ``osid.installation.batch.InstallationBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_installation_batch() is false``

        """
        raise UNIMPLEMENTED()

    installation_batch_proxy_manager = property(fget=get_installation_batch_proxy_manager)


##
# The following methods are from osid.installation.DepotLookupSession

    def can_lookup_depots(self):
        """Tests if this user can perform ``Depot`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.


        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_depot_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.




        """
        raise UNIMPLEMENTED()

    def use_plenary_depot_view(self):
        """A complete view of the ``Depot`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.




        """
        raise UNIMPLEMENTED()

    def get_depot(self, depot_id):
        """Gets the ``Depot`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Depot`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Depot`` and retained for compatility.


        :param depot_id: ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: the depot
        :rtype: ``osid.installation.Depot``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depots_by_ids(self, depot_ids):
        """Gets a ``DepotList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the depots
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Depot`` objects may be omitted from the list and
        may present the elements in any order including returning a
        unique set.


        :param depot_ids: the list of ``Ids`` to retrieve
        :type depot_ids: ``osid.id.IdList``
        :return: the returned ``Depot`` list
        :rtype: ``osid.installation.DepotList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``depot_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depots_by_genus_type(self, depot_genus_type):
        """Gets a ``DepotList`` corresponding to the given depot genus ``Type`` which does not include depots of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known depots or
        an error results. Otherwise, the returned list may contain only
        those depots that are accessible through this session.


        :param depot_genus_type: a depot genus type
        :type depot_genus_type: ``osid.type.Type``
        :return: the returned ``Depot`` list
        :rtype: ``osid.installation.DepotList``
        :raise: ``NullArgument`` -- ``depot_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depots_by_parent_genus_type(self, depot_genus_type):
        """Gets a ``DepotList`` corresponding to the given depot genus ``Type`` and include any additional depots with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known depots or
        an error results. Otherwise, the returned list may contain only
        those depots that are accessible through this session.


        :param depot_genus_type: a depot genus type
        :type depot_genus_type: ``osid.type.Type``
        :return: the returned ``Depot`` list
        :rtype: ``osid.installation.DepotList``
        :raise: ``NullArgument`` -- ``depot_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depots_by_record_type(self, depot_record_type):
        """Gets a ``DepotList`` containing the given depot record ``Type``.
        In plenary mode, the returned list contains all known depots or
        an error results. Otherwise, the returned list may contain only
        those depots that are accessible through this session.


        :param depot_record_type: a depot record type
        :type depot_record_type: ``osid.type.Type``
        :return: the returned ``Depot`` list
        :rtype: ``osid.installation.DepotList``
        :raise: ``NullArgument`` -- ``depot_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depots_by_provider(self, resource_id):
        """Gets a ``DepotList`` for the given provider ````.
        In plenary mode, the returned list contains all known depots or
        an error results. Otherwise, the returned list may contain only
        those depots that are accessible through this session.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Depot`` list
        :rtype: ``osid.installation.DepotList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depots(self):
        """Gets all ``Depots``.
        In plenary mode, the returned list contains all known depots or
        an error results. Otherwise, the returned list may contain only
        those depots that are accessible through this session.


        :return: a ``DepotList``
        :rtype: ``osid.installation.DepotList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    depots = property(fget=get_depots)


##
# The following methods are from osid.installation.DepotQuerySession

    def can_search_depots(self):
        """Tests if this user can perform ``Depot`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_depot_query(self):
        """Gets a depot query.

        :return: a depot query
        :rtype: ``osid.installation.DepotQuery``

        """
        raise UNIMPLEMENTED()

    depot_query = property(fget=get_depot_query)

    def get_depots_by_query(self, depot_query):
        """Gets a list of ``Depot`` objects matching the given depot query.

        :param depot_query: the depot query
        :type depot_query: ``osid.installation.DepotQuery``
        :return: the returned ``DepotList``
        :rtype: ``osid.installation.DepotList``
        :raise: ``NullArgument`` -- ``depot_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``depot_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.DepotSearchSession

    def get_depot_search(self):
        """Gets a depot search.

        :return: a depot search
        :rtype: ``osid.installation.DepotSearch``

        """
        raise UNIMPLEMENTED()

    depot_search = property(fget=get_depot_search)

    def get_depot_search_order(self):
        """Gets a depot search order.
        The ``DepotSearchOrder`` is supplied to a ``DepotSearch`` to
        specify the ordering of results.


        :return: the depot search order
        :rtype: ``osid.installation.DepotSearchOrder``

        """
        raise UNIMPLEMENTED()

    depot_search_order = property(fget=get_depot_search_order)

    def get_depots_by_search(self, depot_query, depot_search):
        """Gets the search results matching the given search query using the given search.

        :param depot_query: the depot query
        :type depot_query: ``osid.installation.DepotQuery``
        :param depot_search: the depot search
        :type depot_search: ``osid.installation.DepotSearch``
        :return: the depot search results
        :rtype: ``osid.installation.DepotSearchResults``
        :raise: ``NullArgument`` -- ``depot_query`` or ``depot_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``depot_query`` or ``depot_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_depot_query_from_inspector(self, depot_query_inspector):
        """Gets a depot query from an inspector.
        The inspector is available from a ``DepotSearchResults``.


        :param depot_query_inspector: a depot query inspector
        :type depot_query_inspector: ``osid.installation.DepotQueryInspector``
        :return: the depot query
        :rtype: ``osid.installation.DepotQuery``
        :raise: ``NullArgument`` -- ``depot_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``depot_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.DepotAdminSession

    def can_create_depots(self):
        """Tests if this user can create ``Depots``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Depot``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.


        :return: ``false`` if ``Depot`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_depot_with_record_types(self, depot_record_types):
        """Tests if this user can create a single ``Depot`` using the desired record types.
        While ``InstallationManager.getDepotRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Depot``.
        Providing an empty array tests if a ``Depot`` can be created
        with no records.


        :param depot_record_types: array of depot record types
        :type depot_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Depot`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``depot_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_depot_form_for_create(self, depot_record_types):
        """Gets the depot form for creating new depots.
        A new form should be requested for each create transaction.


        :param depot_record_types: array of depot record types
        :type depot_record_types: ``osid.type.Type[]``
        :return: the depot form
        :rtype: ``osid.installation.DepotForm``
        :raise: ``NullArgument`` -- ``depot_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_depot(self, depot_form):
        """Creates a new ``Depot``.

        :param depot_form: the form for this ``Depot``
        :type depot_form: ``osid.installation.DepotForm``
        :return: the new ``Depot``
        :rtype: ``osid.installation.Depot``
        :raise: ``IllegalState`` -- ``depot_form`` already used for a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``depot_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``depot_form`` did not originate from ``get_depot_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_depots(self):
        """Tests if this user can update ``Depots``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Depot``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.


        :return: ``false`` if ``Depot`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_update_depot(self, depot_id):
        """Tests if this user can update a specified ``Depot``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating the
        ``Depot`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.


        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: ``false`` if depot modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_depot_form_for_update(self, depot_id):
        """Gets the depot form for updating an existing depot.
        A new depot form should be requested for each update
        transaction.


        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: the depot form
        :rtype: ``osid.installation.DepotForm``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_depot(self, depot_form):
        """Updates an existing depot.

        :param depot_form: the form containing the elements to be updated
        :type depot_form: ``osid.installation.DepotForm``
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``depot_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``depot_form`` did not originate from ``get_depot_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_depots(self):
        """Tests if this user can delete depots.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Depot``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.


        :return: ``false`` if ``Depot`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_delete_depot(self, depot_id):
        """Tests if this user can delete a specified ``Depot``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting the
        ``Depot`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.


        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: ``false`` if deletion of this ``Depot`` is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def delete_depot(self, depot_id):
        """Deletes a ``Depot``.

        :param depot_id: the ``Id`` of the ``Depot`` to remove
        :type depot_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_depot_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Depots``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``Depot`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_depot(self, depot_id, alias_id):
        """Adds an ``Id`` to a ``Depot`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Depot`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another depot it is
        reassigned to the given depot ``Id``.


        :param depot_id: the ``Id`` of a ``Depot``
        :type depot_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.DepotNotificationSession

    def can_register_for_depot_notifications(self):
        """Tests if this user can register for ``Depot`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.


        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_depots(self):
        """Register for notifications of new depots.
        ``DepotReceiver.newDepot()`` is invoked when a new ``Depot`` is
        created.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_depot_ancestors(self, depot_id):
        """Registers for notification if an ancestor is added to the specified depot in the depot hierarchy.
        ``DepotReceiver.newDepotAncestor()`` is invoked when the
        specified depot experiences an addition in ancestry.


        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_depot_descendants(self, depot_id):
        """Registers for notification if a descendant is added to the specified depot in the depot hierarchy.
        ``DepotReceiver.newDepotDescendant()`` is invoked when the
        specified depot experiences an addition in descendants.


        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_depots(self):
        """Registers for notification of updated depots.
        ``DepotReceiver.changedDepot()`` is invoked when a depot is
        changed.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_depot(self, depot_id):
        """Registers for notification of an updated depot.
        ``DepotReceiver.changedDepot()`` is invoked when the specified
        depot is changed.


        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_depots(self):
        """Registers for notification of deleted depots.
        ``DepotReceiver.deletedDepot()`` is invoked when a depot is
        deleted.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_depot(self, depot_id):
        """Registers for notification of a deleted depot.
        ``DepotReceiver.deletedDepot()`` is invoked when the specified
        depot is deleted.


        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_depot_ancestors(self, depot_id):
        """Registers for notification if an ancestor is removed from the specified depot in the depot hierarchy.
        ``DepotReceiver.deletedDepotAncestor()`` is invoked when the
        specified depot experiences a removal of an ancestor.


        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_depot_descendants(self, depot_id):
        """Registers for notification if a descendant is removed from fthe specified depot in the depot hierarchy.
        ``DepotReceiver.deletedDepotDescednant()`` is invoked when the
        specified depot experiences a removal of one of its descendants.


        :param depot_id: the ``Id`` of the depot to monitor
        :type depot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``depot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.DepotHierarchySession

    def get_depot_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    depot_hierarchy_id = property(fget=get_depot_hierarchy_id)

    def get_depot_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    depot_hierarchy = property(fget=get_depot_hierarchy)

    def can_access_depot_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer hierrachy
        traversal operations to unauthorized users.


        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_depot_ids(self):
        """Gets the root depot ``Ids`` in this hierarchy.

        :return: the root depot ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_depot_ids = property(fget=get_root_depot_ids)

    def get_root_depots(self):
        """Gets the root depots in this depot hierarchy.

        :return: the root depots
        :rtype: ``osid.installation.DepotList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_depots = property(fget=get_root_depots)

    def has_parent_depots(self, depot_id):
        """Tests if the ``Depot`` has any parents.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if the depot has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_depot(self, id_, depot_id):
        """Tests if an ``Id`` is a direct parent of a depot.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``depot_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_depot_ids(self, depot_id):
        """Gets the parent ``Ids`` of the given depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the depot
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_depots(self, depot_id):
        """Gets the parents of the given depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: the parents of the depot
        :rtype: ``osid.installation.DepotList``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_depot(self, id_, depot_id):
        """Tests if an ``Id`` is an ancestor of a depot.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``depot_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_depots(self, depot_id):
        """Tests if a depot has any children.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if the ``depot_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_depot(self, id_, depot_id):
        """Tests if a depot is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``depot_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_depot_ids(self, depot_id):
        """Gets the child ``Ids`` of the given depot.

        :param depot_id: the ``Id`` to query
        :type depot_id: ``osid.id.Id``
        :return: the children of the depot
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_depots(self, depot_id):
        """Gets the children of the given depot.

        :param depot_id: the ``Id`` to query
        :type depot_id: ``osid.id.Id``
        :return: the children of the depot
        :rtype: ``osid.installation.DepotList``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_depot(self, id_, depot_id):
        """Tests if an ``Id`` is a descendant of a depot.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``depot_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depot_node_ids(self, depot_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given depot.

        :param depot_id: the ``Id`` to query
        :type depot_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a depot node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depot_nodes(self, depot_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given depot.

        :param depot_id: the ``Id`` to query
        :type depot_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a depot node
        :rtype: ``osid.installation.DepotNode``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.DepotHierarchyDesignSession

    def can_modify_depot_hierarchy(self):
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

    def add_root_depot(self, depot_id):
        """Adds a root depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``depot_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_depot(self, depot_id):
        """Removes a root depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``depot_id`` is not a root
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_depot(self, depot_id, child_id):
        """Adds a child to a depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``depot_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``depot_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_depot(self, depot_id, child_id):
        """Removes a child from a depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``depot_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``depot_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_depots(self, depot_id):
        """Removes all children from a depot.

        :param depot_id: the ``Id`` of a depot
        :type depot_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``depot_id`` not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class Depot(osid_objects.OsidCatalog, osid_sessions.OsidSession):

    def get_depot_record(self, depot_record_type):
        """Gets the depot record corresponding to the given ``Depot`` record ``Type``.
        This method is used to retrieve an object implementing the
        requested record. The ``depot_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(depot_record_type)``
        is ``true`` .

        :param depot_record_type: a depot record type
        :type depot_record_type: ``osid.type.Type``
        :return: the depot record
        :rtype: ``osid.installation.records.DepotRecord``
        :raise: ``NullArgument`` -- ``depot_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(depot_record_type)`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.InstallationLookupSession

    def get_site_id(self):
        """Gets the ``Site``  ``Id`` associated with this session.

        :return: the ``Site Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    site_id = property(fget=get_site_id)

    def get_site(self):
        """Gets the ``Site`` associated with this session.

        :return: the ``Site`` associated with this session
        :rtype: ``osid.installation.Site``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    site = property(fget=get_site)

    def can_lookup_installations(self):
        """Tests if this user can perform ``Installation`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_installation_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_installation_view(self):
        """A complete view of the ``Installation`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_normalized_version_view(self):
        """The returns from the lookup methods may omit multiple versions of the same installation."""
        raise UNIMPLEMENTED()

    def use_denormalized_version_view(self):
        """All versions of the same installation are returned."""
        raise UNIMPLEMENTED()

    def get_installation(self, installation_id):
        """Gets the ``Installation`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Installation`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``Installation`` and
        retained for compatibility.

        :param installation_id: ``Id`` of the ``Installation``
        :type installation_id: ``osid.id.Id``
        :return: the installation
        :rtype: ``osid.installation.Installation``
        :raise: ``NotFound`` -- ``installation_id`` not found
        :raise: ``NullArgument`` -- ``installation_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_installations_by_ids(self, installation_ids):
        """Gets an ``InstallationList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the
        installations specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Installations`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param installation_ids: the list of ``Ids`` to retrieve
        :type installation_ids: ``osid.id.IdList``
        :return: the returned ``Installation`` list
        :rtype: ``osid.installation.InstallationList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``installation_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_installations_by_genus_type(self, installation_genus_type):
        """Gets an ``InstallationList`` corresponding to the given installation genus ``Type`` which does not include installations of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        installations or an error results. Otherwise, the returned list
        may contain only those installations that are accessible through
        this session.

        :param installation_genus_type: an installation genus type
        :type installation_genus_type: ``osid.type.Type``
        :return: the returned ``Installation`` list
        :rtype: ``osid.installation.InstallationList``
        :raise: ``NullArgument`` -- ``installation_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_installations_by_parent_genus_type(self, installation_genus_type):
        """Gets an ``InstallationList`` corresponding to the given installation genus ``Type`` and include any additional installations with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        installations or an error results. Otherwise, the returned list
        may contain only those installations that are accessible through
        this session.

        :param installation_genus_type: an installation genus type
        :type installation_genus_type: ``osid.type.Type``
        :return: the returned ``Installation`` list
        :rtype: ``osid.installation.InstallationList``
        :raise: ``NullArgument`` -- ``installation_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_installations_by_record_type(self, installation_record_type):
        """Gets an ``InstallationList`` containing the given installation record ``Type``.
        In plenary mode, the returned list contains all known
        installations or an error results. Otherwise, the returned list
        may contain only those installations that are accessible through
        this session.

        :param installation_record_type: an installation record type
        :type installation_record_type: ``osid.type.Type``
        :return: the returned ``Installation`` list
        :rtype: ``osid.installation.InstallationList``
        :raise: ``NullArgument`` -- ``installation_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_installations_by_package(self, package_id):
        """Gets an ``InstallationList`` corresponding to the given ``Package``.
        In plenary mode, the returned list contains all of the
        installations for the specified package, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Installations`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param package_id: ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :return: the returned ``Installation`` list
        :rtype: ``osid.installation.InstallationList``
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_installations(self):
        """Gets all ``Installations``.
        In plenary mode, the returned list contains all known
        installations or an error results. Otherwise, the returned list
        may contain only those installations that are accessible through
        this session. In both cases, the order of the set is not
        specified.

        :return: an ``InstallationList``
        :rtype: ``osid.installation.InstallationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    installations = property(fget=get_installations)


##
# The following methods are from osid.installation.InstallationQuerySession

    def can_search_installations(self):
        """Tests if this user can perform ``Installation`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_normalized_dependency_view(self):
        """A normalized view uses a single ``Installation`` to represent a set of package dependencies."""
        raise UNIMPLEMENTED()

    def use_denormalized_dependency_view(self):
        """A denormalized view returns all dependencies."""
        raise UNIMPLEMENTED()

    def get_installation_query(self):
        """Gets an installation query.

        :return: the installation query
        :rtype: ``osid.installation.InstallationQuery``

        """
        raise UNIMPLEMENTED()

    installation_query = property(fget=get_installation_query)

    def get_installations_by_query(self, installation_query):
        """Gets a list of ``Installations`` matching the given installation query.

        :param installation_query: the installation query
        :type installation_query: ``osid.installation.InstallationQuery``
        :return: the returned ``InstallationList``
        :rtype: ``osid.installation.InstallationList``
        :raise: ``NullArgument`` -- ``installation_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``installation_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.InstallationSearchSession

    def get_installation_search(self):
        """Gets an installation search.

        :return: the installation search
        :rtype: ``osid.installation.InstallationSearch``

        """
        raise UNIMPLEMENTED()

    installation_search = property(fget=get_installation_search)

    def get_installation_search_order(self):
        """Gets an installation search order.
        The ``InstallationSearchOrder`` is supplied to an
        ``InstallationSearch`` to specify the ordering of results.

        :return: the installation search order
        :rtype: ``osid.installation.InstallationSearchOrder``

        """
        raise UNIMPLEMENTED()

    installation_search_order = property(fget=get_installation_search_order)

    def get_installations_by_search(self, installation_query, installation_search):
        """Gets the search results matching the given search query using the given search.

        :param installation_query: the installation query
        :type installation_query: ``osid.installation.InstallationQuery``
        :param installation_search: the installation search
        :type installation_search: ``osid.installation.InstallationSearch``
        :return: the returned search results
        :rtype: ``osid.installation.InstallationSearchResults``
        :raise: ``NullArgument`` -- ``installation_query`` or ``installation_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``installation_search`` or ``installation_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_installations_query_from_inspector(self, installaton_query_inspector):
        """Gets a installation query from an inspector.
        The inspector is available from a ``InstallationSearchResults``.

        :param installaton_query_inspector: a installation query inspector
        :type installaton_query_inspector: ``osid.installation.InstallationQueryInspector``
        :return: the installaton query
        :rtype: ``osid.installation.InstallationQuery``
        :raise: ``NullArgument`` -- ``installation_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``installation_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.InstallationManagementSession

    def can_manage_installations(self):
        """Tests if this user can manage installations A return of true does not guarantee successful authorization.
        A return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer management
        operations to unauthorized users.

        :return: ``false`` if ``Package`` installation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def install_package(self, package_id):
        """Installs a package at a default site.

        :param package_id: an ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :return: the resulting ``Installation``
        :rtype: ``osid.installation.Installation``
        :raise: ``AlreadyExists`` -- package is already installed
        :raise: ``NotFound`` -- ``package_id`` is not found
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_installation(self, installation_id):
        """Removes an installation.

        :param installation_id: an ``Id`` of an ``Installation``
        :type installation_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``installation_id`` is not found
        :raise: ``NullArgument`` -- ``installation_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_installations(self):
        """Removes all installations at the site.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.InstallationUpdateSession

    def can_get_installation_updates(self):
        """Tests if this user can get installation updates.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may wish not to offer update
        operations to unauthorized users.

        :return: ``false`` if package updates are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def is_installation_current(self):
        """Tests if the given installation is current.

        :return: ``true`` if the installation is up to date, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_installations_to_update(self):
        """Gets a list of installations requiring update.
        This just returns installations that are out of date.
        ``get_packages_to_update()`` or
        ``get_packages_to_update_for_installation()`` should be used to
        acquire the packages to install.

        :return: the resulting ``InstallationList``
        :rtype: ``osid.installation.InstallationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    installations_to_update = property(fget=get_installations_to_update)

    def get_current_packages(self):
        """Gets the packages to install to bring the site up to date.

        :return: the next packages to install
        :rtype: ``osid.installation.PackageList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    current_packages = property(fget=get_current_packages)

    def get_current_packages_for_installation(self, installation_id):
        """Gets the packages to install to bring the specified installation up to date.

        :param installation_id: an ``Id`` of an ``Installation``
        :type installation_id: ``osid.id.Id``
        :return: the next packages to install
        :rtype: ``osid.installation.PackageList``
        :raise: ``NotFound`` -- ``installation_id`` is not found
        :raise: ``NullArgument`` -- ``installation_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_installation_obsolete(self):
        """Tests if the given installation is obsolete.

        :return: ``true`` if the installation is obsolete, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_obsolete_installations(self):
        """Gets the installations whose packages are obsolete.

        :return: the obsolete installations
        :rtype: ``osid.installation.InstallationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    obsolete_installations = property(fget=get_obsolete_installations)

    def update_installation(self, installation_id):
        """Updates a single installation.

        :param installation_id: an ``Id`` of an ``Installation``
        :type installation_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``installation_id`` is not found
        :raise: ``NullArgument`` -- ``installation_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def synchronize_installations(self):
        """Performs an auto-update by adding all new updated installations and removing of all obsolete installations on the site.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.InstallationNotificationSession

    def can_register_for_installation_notifications(self):
        """Tests if this user can register for ``Installation`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer notification
        functions to unauthorized users.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_installations(self):
        """Register for notifications of new installations.
        ``InstallationReceiver.newInstallation()`` is invoked when a new
        installation is installed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_installations(self):
        """Registers for notification of deleted installations.
        ``InstallationReceiver.deletedInstallation()`` is invoked when a
        installation is removed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_installation(self, installation_id):
        """Registers for notification of a deleted installation.
        ``InstallationReceiver.deletedInstallation()`` is invoked when
        the specified installation is removed.

        :param installation_id: the ``Id`` of the ``Installation`` to monitor
        :type installation_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``installation_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.SiteLookupSession

    def can_lookup_sites(self):
        """Tests if this user can perform ``Site`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_site_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_site_view(self):
        """A complete view of the ``Site`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_sites(self):
        """Gets all ``Sites``.
        In plenary mode, the returned list contains all known sites or
        an error results. Otherwise, the returned list may contain only
        those sites that are accessible through this session.

        :return: a ``SiteList``
        :rtype: ``osid.installation.SiteList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    sites = property(fget=get_sites)


##
# The following methods are from osid.installation.PackageLookupSession

    def get_depot_id(self):
        """Gets the ``Depot``  ``Id`` associated with this session.

        :return: the ``Depot Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    depot_id = property(fget=get_depot_id)

    def get_depot(self):
        """Gets the ``Depot`` associated with this session.

        :return: the ``Depot`` associated with this session
        :rtype: ``osid.installation.Depot``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    depot = property(fget=get_depot)

    def can_lookup_packages(self):
        """Tests if this user can perform ``Package`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_package_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_package_view(self):
        """A complete view of the ``Package`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_depot_view(self):
        """Federates the view for methods in this session.
        A federated view will include packages in depots which are
        children of this depot in the depot hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_depot_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this depot only.



        """
        raise UNIMPLEMENTED()

    def get_package(self, package_id):
        """Gets the ``Package`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Package`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Package`` and retained for
        compatibility.

        :param package_id: ``Id`` of the ``Package``
        :type package_id: ``osid.id.Id``
        :return: the package
        :rtype: ``osid.installation.Package``
        :raise: ``NotFound`` -- ``package_id`` not found
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_packages_by_ids(self, package_ids):
        """Gets a ``PackageList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the packages
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Packages`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param package_ids: the list of ``Ids`` to retrieve
        :type package_ids: ``osid.id.IdList``
        :return: the returned ``Package`` list
        :rtype: ``osid.installation.PackageList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``package_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_packages_by_genus_type(self, package_genus_type):
        """Gets a ``PackageList`` corresponding to the given package genus ``Type`` which does not include packages of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known packages
        or an error results. Otherwise, the returned list may contain
        only those packages that are accessible through this session.

        :param package_genus_type: a package genus type
        :type package_genus_type: ``osid.type.Type``
        :return: the returned ``Package`` list
        :rtype: ``osid.installation.PackageList``
        :raise: ``NullArgument`` -- ``package_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_packages_by_parent_genus_type(self, package_genus_type):
        """Gets a ``PackageList`` corresponding to the given package genus ``Type`` and include any additional package with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known packages
        or an error results. Otherwise, the returned list may contain
        only those packages that are accessible through this session.

        :param package_genus_type: a package genus type
        :type package_genus_type: ``osid.type.Type``
        :return: the returned ``Package`` list
        :rtype: ``osid.installation.PackageList``
        :raise: ``NullArgument`` -- ``package_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_packages_by_record_type(self, package_record_type):
        """Gets a ``PackageList`` containing the given package record ``Type``.
        In plenary mode, the returned list contains all known packages
        or an error results. Otherwise, the returned list may contain
        only those packages that are accessible through this session.

        :param package_record_type: a package record type
        :type package_record_type: ``osid.type.Type``
        :return: the returned ``Package`` list
        :rtype: ``osid.installation.PackageList``
        :raise: ``NullArgument`` -- ``package_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_packages_by_provider(self, resource_id):
        """Gets a ``PackageList`` for the given provider.
        In plenary mode, the returned list contains all known packages
        or an error results. Otherwise, the returned list may contain
        only those packages that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Package`` list
        :rtype: ``osid.installation.PackageList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_dependent_packages(self, package_id):
        """Gets a list of packages depending on the given package.

        :param package_id: an ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :return: list of package dependents
        :rtype: ``osid.installation.PackageList``
        :raise: ``NotFound`` -- ``package_id`` is not found
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_package_versions(self, package_id):
        """Gets a list of packages in the specified package version chain.

        :param package_id: an ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :return: list of dependencies
        :rtype: ``osid.installation.PackageList``
        :raise: ``NotFound`` -- ``package_id`` is not found
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_packages(self):
        """Gets all ``Packages``.
        In plenary mode, the returned list contains all known packages
        or an error results. Otherwise, the returned list may contain
        only those packages that are accessible through this session.

        :return: a ``PackageList``
        :rtype: ``osid.installation.PackageList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    packages = property(fget=get_packages)


##
# The following methods are from osid.installation.PackageQuerySession

    def can_search_packages(self):
        """Tests if this user can perform ``Package`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_package_query(self):
        """Gets a package query.

        :return: the package query
        :rtype: ``osid.installation.PackageQuery``

        """
        raise UNIMPLEMENTED()

    package_query = property(fget=get_package_query)

    def get_packages_by_query(self, package_query):
        """Gets a list of ``Packages`` matching the given package query.

        :param package_query: the package query
        :type package_query: ``osid.installation.PackageQuery``
        :return: the returned ``PackageList``
        :rtype: ``osid.installation.PackageList``
        :raise: ``NullArgument`` -- ``package_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``package_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.PackageSearchSession

    def get_package_search(self):
        """Gets a package search.

        :return: the package search
        :rtype: ``osid.installation.PackageSearch``

        """
        raise UNIMPLEMENTED()

    package_search = property(fget=get_package_search)

    def get_package_search_order(self):
        """Gets a package search order.
        The ``PackageSearchOrder`` is supplied to a ``PackageSearch`` to
        specify the ordering of results.

        :return: the package search order
        :rtype: ``osid.installation.PackageSearchOrder``

        """
        raise UNIMPLEMENTED()

    package_search_order = property(fget=get_package_search_order)

    def get_packages_by_search(self, package_query, package_search):
        """Gets the search results matching the given search query using the given search.

        :param package_query: the package query
        :type package_query: ``osid.installation.PackageQuery``
        :param package_search: the package search
        :type package_search: ``osid.installation.PackageSearch``
        :return: the returned search results
        :rtype: ``osid.installation.PackageSearchResults``
        :raise: ``NullArgument`` -- ``package_query`` or ``package_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``package_search`` or ``package_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_package_query_from_inspector(self, package_query_inspector):
        """Gets a package query from an inspector.
        The inspector is available from a ``PackageeSearchResults``.

        :param package_query_inspector: a package query inspector
        :type package_query_inspector: ``osid.installation.PackageQueryInspector``
        :return: the package query
        :rtype: ``osid.installation.PackageQuery``
        :raise: ``NullArgument`` -- ``package_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``package_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.PackageAdminSession

    def can_create_packages(self):
        """Tests if this user can create ``Packages``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Package`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Package`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_package_with_record_types(self, package_record_types):
        """Tests if this user can create a single ``Package`` using the desired record types.
        While ``InstallationManager.getPackageRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Package``. Providing an empty array tests if a ``Package`` can
        be created with no records.

        :param package_record_types: array of package record types
        :type package_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Package`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``package_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_package_form_for_create(self, package_record_types):
        """Gets the package form for creating new packages.
        A new form should be requested for each create transaction.

        :param package_record_types: array of package record types
        :type package_record_types: ``osid.type.Type[]``
        :return: the package form
        :rtype: ``osid.installation.PackageForm``
        :raise: ``NullArgument`` -- ``package_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_package(self, package_form):
        """Creates a new ``Package``.

        :param package_form: the form for this ``Package``
        :type package_form: ``osid.installation.PackageForm``
        :return: the new ``Package``
        :rtype: ``osid.installation.Package``
        :raise: ``IllegalState`` -- ``package_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``package_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``package_form`` did not originate from ``get_package_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_packages(self):
        """Tests if this user can update ``Packages``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Package`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if package modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_update_package(self, package_id):
        """Tests if this user can update a specified package.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating the package
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer an update
        operation to an unauthorized user for this function.

        :param package_id: the ``Id`` of the ``Package``
        :type package_id: ``osid.id.Id``
        :return: ``false`` if package modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``package_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_package_form_for_update(self, package_id):
        """Gets the package form for updating an existing package.
        A new package form should be requested for each update
        transaction.

        :param package_id: the ``Id`` of the ``Package``
        :type package_id: ``osid.id.Id``
        :return: the package form
        :rtype: ``osid.installation.PackageForm``
        :raise: ``NotFound`` -- ``package_id`` is not found
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_package(self, package_form):
        """Updates an existing package.

        :param package_form: the form containing the elements to be updated
        :type package_form: ``osid.installation.PackageForm``
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``package_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``package_form`` did not originate from ``get_package_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_packages(self):
        """Tests if this user can delete ``Packages``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Package`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Package`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_delete_package(self, package_id):
        """Tests if this user can delete a specified ``Package``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting the
        ``Package`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer a
        delete operation to an unauthorized user for this function.

        :param package_id: the ``Id`` of the ``Package``
        :type package_id: ``osid.id.Id``
        :return: ``false`` if ``Package`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``package_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def delete_package(self, package_id):
        """Deletes the ``Package`` identified by the given ``Id``.

        :param package_id: the ``Id`` of the ``Package`` to delete
        :type package_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Package`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_package_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Packages``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Package`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_package(self, package_id, alias_id):
        """Adds an ``Id`` to a ``Package`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Package`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another package it is
        reassigned to the given package ``Id``.

        :param package_id: the ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``package_id`` not found
        :raise: ``NullArgument`` -- ``package_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_create_installation_content(self):
        """Tests if this user can create content for ``Packages``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``InstallationContent`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer create operations to an unauthorized user.

        :return: ``false`` if ``installation`` content creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_installation_content_with_record_types(self, installation_content_record_types):
        """Tests if this user can create an ``InstallationContent`` using the desired record types.
        While
        ``InstallationManager.getInstallationContentRecordTypes()`` can
        be used to test which records are supported, this method tests
        which records are required for creating a specific
        ``InstallationContent``. Providing an empty array tests if an
        ``InstallationContent`` can be created with no records.

        :param installation_content_record_types: array of installation content record types
        :type installation_content_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``InstallationContent`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``installation_content_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_installation_content_form_for_create(self, package_id, installation_content_record_types):
        """Gets an installation content form for creating new installation contents.

        :param package_id: the ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :param installation_content_record_types: array of installation content record types
        :type installation_content_record_types: ``osid.type.Type[]``
        :return: the installation content form
        :rtype: ``osid.installation.InstallationContentForm``
        :raise: ``NotFound`` -- ``package_id`` is not found
        :raise: ``NullArgument`` -- ``package_id`` or ``installation_content_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_installation_content(self, installation_content_form):
        """Creates new ``InstallationContent`` for a given package.

        :param installation_content_form: the form for this ``InstallationContent``
        :type installation_content_form: ``osid.installation.InstallationContentForm``
        :return: the new ``InstallationContent``
        :rtype: ``osid.installation.InstallationContent``
        :raise: ``IllegalState`` -- ``installation_content_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``installation_content_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``installation_content_form`` did not originate from ``get_installation_content_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_installation_contents(self):
        """Tests if this user can update ``InstallationContent``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``InstallationContent`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: ``false`` if ``InstallationContent`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_installation_content_form_for_update(self, installation_content_id):
        """Gets the installation content form for updating an existing installation content.
        A new installation content form should be requested for each
        update transaction.

        :param installation_content_id: the ``Id`` of the ``InstallationContent``
        :type installation_content_id: ``osid.id.Id``
        :return: the v content form
        :rtype: ``osid.installation.InstallationContentForm``
        :raise: ``NotFound`` -- ``installation_content_id`` is not found
        :raise: ``NullArgument`` -- ``installation_content_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def update_installation_content(self, installation_content_form):
        """Updates an existing installation content.

        :param installation_content_form: the form containing the elements to be updated
        :type installation_content_form: ``osid.installation.InstallationContentForm``
        :raise: ``IllegalState`` -- ``installation_content_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``installation_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``installation_content_form`` did not originate from ``get_installation_content_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_installation_contents(self):
        """Tests if this user can delete ``InstallationContents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``InstallationContent`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer delete operations to an unauthorized user.

        :return: ``false`` if ``InstallationContent`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_installation_content(self, installation_content_id):
        """Deletes content from a package.

        :param installation_content_id: the ``Id`` of the ``InstallationContent``
        :type installation_content_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``installation_content_id`` is not found
        :raise: ``NullArgument`` -- ``installation_content_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_package_versions(self):
        """Tests if this user can manage package versions.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known version methods will
        result in a ``PermissionDenied``. This is intended as a hint to
        an application that may opt not to offer delete operations to an
        unauthorized user.

        :return: ``false`` if package versioning is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_package_version(self, package_id, next_package_id):
        """Sets the given package to be the next version of another package.

        :param package_id: the ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :param next_package_id: the ``Id`` of the net package version
        :type next_package_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``next_package_id`` or ``package_id`` already part of a version chain
        :raise: ``NotFound`` -- ``package_id`` or ``next_package_id`` not found
        :raise: ``NullArgument`` -- ``package_id`` or ``next_package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_package_version(self, package_id, next_package_id):
        """Removes a package from being the next version of another package.

        :param package_id: the ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :param next_package_id: the ``Id`` of the net package version
        :type next_package_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``next_package_id`` does not follow ``package_id``
        :raise: ``NullArgument`` -- ``package_id`` or ``dependency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.PackageNotificationSession

    def can_register_for_package_notifications(self):
        """Tests if this user can register for ``Package`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_packages(self):
        """Register for notifications of new packages.
        ``PackageReceiver.newPackage()`` is invoked when a new package
        is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_packages(self):
        """Registers for notification of updated packages.
        ``PackageReceiver.changedPackage()`` is invoked when a package
        is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_package(self, package_id):
        """Registers for notification of an updated package.
        ``PackageReceiver.changedPackage()`` is invoked when the
        specified package is changed.

        :param package_id: the ``Id`` of the ``Package`` to monitor
        :type package_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``package_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_packages(self):
        """Registers for notification of deleted packages.
        ``PackageReceiver.deletedPackage()`` is invoked when a package
        is removed from this depot.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_package(self, package_id):
        """Registers for notification of a deleted package.
        ``PackageReceiver.deletedPackage()`` is invoked when the
        specified package is removed from this depot.

        :param package_id: the ``Id`` of the ``Package`` to monitor
        :type package_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``package_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.PackageDepotSession

    def can_lookup_package_depot_mappings(self):
        """Tests if this user can perform lookups of package/depot mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_depot_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_depot_view(self):
        """A complete view of the ``Package`` and ``Depot`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_package_ids_by_depot(self, depot_id):
        """Gets the list of ``Package``  ``Ids`` associated with a ``Depot``.

        :param depot_id: ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: list of related package ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_packages_by_depot(self, depot_id):
        """Gets the list of ``Packages`` associated with a ``Depot``.

        :param depot_id: ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: list of related packages
        :rtype: ``osid.installation.PackageList``
        :raise: ``NotFound`` -- ``depot_id`` is not found
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_package_ids_by_depots(self, depot_ids):
        """Gets the list of ``Package Ids`` corresponding to a list of ``Depots``.

        :param depot_ids: list of depot ``Ids``
        :type depot_ids: ``osid.id.IdList``
        :return: list of package ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``depot_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_packages_by_depots(self, depot_ids):
        """Gets the list of ``Packages`` corresponding to a list of ``Depots``.

        :param depot_ids: list of depot ``Ids``
        :type depot_ids: ``osid.id.IdList``
        :return: list of packages
        :rtype: ``osid.installation.PackageList``
        :raise: ``NullArgument`` -- ``depot_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depot_ids_by_package(self, package_id):
        """Gets the list of ``Depot``  ``Ids`` mapped to a ``Package``.

        :param package_id: ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :return: list of depot ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``package_id`` is not found
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_depots_by_package(self, package_id):
        """Gets the list of ``Depots`` mapped to a ``Package``.

        :param package_id: ``Id`` of a ``Package``
        :type package_id: ``osid.id.Id``
        :return: list of depots
        :rtype: ``osid.installation.DepotList``
        :raise: ``NotFound`` -- ``package_id`` is not found
        :raise: ``NullArgument`` -- ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.PackageDepotAssignmentSession

    def can_assign_packages(self):
        """Tests if this user can alter package/depot mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_packages_to_depot(self, depot_id):
        """Tests if this user can alter package/depot mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_depot_ids(self, depot_id):
        """Gets a list of depot including and under the given depot node in which any package can be assigned.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :return: list of assignable depot ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_depot_ids_for_package(self, depot_id, package_id):
        """Gets a list of depot including and under the given depot node in which a specific package can be assigned.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :param package_id: the ``Id`` of the ``Package``
        :type package_id: ``osid.id.Id``
        :return: list of assignable depot ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``depot_id`` or ``package_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_package_to_depot(self, package_id, depot_id):
        """Adds an existing ``Package`` to a ``Depot``.

        :param package_id: the ``Id`` of the ``Package``
        :type package_id: ``osid.id.Id``
        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``package_id`` is already assigned to ``depot_id``
        :raise: ``NotFound`` -- ``package_id`` or ``depot_id`` not found
        :raise: ``NullArgument`` -- ``package_id`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_package_from_depot(self, package_id, depot_id):
        """Removes a ``Package`` from a ``Depot``.

        :param package_id: the ``Id`` of the ``Package``
        :type package_id: ``osid.id.Id``
        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``package_id`` or ``depot_id`` not found or ``package_id`` not assigned to ``depot_id``
        :raise: ``NullArgument`` -- ``package_id`` or ``depot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.installation.PackageSmartDepotSession

    def can_manage_smart_depot(self):
        """Tests if this user can manage smart depot.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart depot management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_package_query(self, package_query):
        """Applies a package query to this depot.

        :param package_query: the package query
        :type package_query: ``osid.installation.PackageQuery``
        :raise: ``NullArgument`` -- ``package_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``package_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_package_query(self):
        """Gets a package query inspector for this depot.

        :return: the package query inspector
        :rtype: ``osid.installation.PackageQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_package_sequencing(self, package_search_order):
        """Applies a package search order to this depot.

        :param package_search_order: the package search order
        :type package_search_order: ``osid.installation.PackageSearchOrder``
        :raise: ``NullArgument`` -- ``package_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``package_search_order`` not of this service

        """
        raise UNIMPLEMENTED()



class DepotList(osid_objects.OsidList):

    def get_next_depot(self):
        """Gets the next ``Depot`` in this list.

        :return: the next ``Depot`` in this list. The ``has_next()`` method should be used to test that a next ``Depot`` is available before calling this method.
        :rtype: ``osid.installation.Depot``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    next_depot = property(fget=get_next_depot)

    def get_next_depots(self, n):
        """Gets the next set of ``Depot`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Depot`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Depot`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.installation.Depot``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()



class Depots(InstallationManager):
    pass


