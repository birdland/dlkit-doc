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