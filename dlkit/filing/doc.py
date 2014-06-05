# -*- coding: utf-8 -*-
"""Filing Open Service Interface Definitions
filing version 3.0.0

The Filing OSID provides a means for managing and accessing files and
directories. The Filing OSID is used to abstract assumptions made about
using a specific file system, or can be used to provide a file-based
application a file system oriented view of other OSIDs.

Files

The Filing OSID defines a file access session that maps to a single
``File``. This is the simplest application of the Filing OSID can be
used in circumstances when it is desirable to confine knowledge of
directories within a provider.

Directories

``Directories`` are hierarchical ``OsidCatalogs`` of Files.

Differences from OSID Patterns

The Filing OSID assumes the pathname and filename of a ``File`` or
``Directory`` is globally unique. Typically, only the ``Id`` field is
unique in an ``OsidObject``. In the Filing OSID, there are two unique
identifiers for identifying ``Files`` and Directories.

The ``Id`` is used to conform to existing OSID patterns and more easily
create relationships to other auxiliary services such as the Journaling
OSID, Relationship OSID, or the Ontology OSID. However, in a file system
one is accustomed to traversing a file system using path names.

The standard ``OsidSessions`` refer to ``Files`` and ``Directories``
using their ``Ids``. The file system-oriented and content sessions
access and manipulate the file system using path names. Access to these
sessions via the ``OsidManagers`` provide for both a path name and
``Directory``  ``Id``.

The cataloging in the file system and content sessions behave
differently than that in other OsidSessions. Typically, one is
constrained to ``OsidObjects`` within the ``OsidCatalog,`` and its
children in a federated view. In these sessions which use the path name
as a key, ``Files`` and ``Directories`` outside the local Directory may
be accessed with the use of absolute path names.

Finally, there are no hierarchical service patterns in the ``Directory``
``OsidCatalog`` and a ``File`` or sub-directory may belong to one and
only one ``Directory`` .

Example
  FilieSession session = filingManager.getFileContentSession();
  DataInputStream dis = session.getInputStream("/etc/passwd");



Sub Packages

The Filing OSID contains a Filing Allocation OSID for examining and
managing file system utilization and user quotas.

"""