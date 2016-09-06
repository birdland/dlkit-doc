Introduction to DLKit
=====================

Basic OSID terms
----------------

Some familiarity with the OSID models and terms will help understand how to use DLKit.

Each service has its own set of packages. Some commonly used DLKit services
include ``assessment``, ``learning``, and ``repository``. Within each service,
users encounter three types of objects: ``managers``, ``sessions``, and ``objects``.
``sessions`` are the verbs of the system (what you want to do), while
``objects`` are the nouns (what you are working on). For example, to look
up learning objectives in the ``learning`` service, you would use a
``ObjectiveLookupSession``, which has all the methods you need to look up
objectives, like ``get_objective()``, ``get_objectives_by_ids()``, etc.

Managers
^^^^^^^^

Managers act as the entry points to each service by granting access to
sessions. For basic DLKit usage, users will most likely use the service managers
to get the service catalog, which has been overloaded to include the most
used methods (i.e. the catalog for ``learning`` is an ``ObjectiveBank``).

Advanced users can use the service manager in a strict OSID fashion
as well.

Sessions
^^^^^^^^

Sessions allow users to perform a certain action on a desired ``object``.
For basic users, they will most likely never encounter a ``session``,
so the usage is only address in the advanced usage page.

Objects
^^^^^^^

In each OSID service, there are typically two types of ``objects`` -- the
overall catalog, as well as the more granular object that resides in the catalogs.

Catalogs are generally used for authorization (who can do what actions to what
objects), and in DLKit these authorizations flow down. If catalog B is a parent
of catalog C, and I can create things in catalog B, then I can automatically create
things in catalog C as well.

For example, in the ``learning`` service, the catalog is an ``ObjectiveBank``,
and the more granular resources are ``objectives``.

Usage
-----

While DLKit is an implementation of the OSIDs, a convenience layer has
been built on top of the OSID implementation. This layer is called ``dlkit.services``,
and it is recommended that new developers start working with this layer, first.
General instructions for these are outlined in the :ref:`basic-usage` section.

If users find certain functionality missing or inconvenient, then they
should check out the :ref:`advanced-usage` section.

Directory Structure
-------------------

Until we have a good way to package DLKit and make it available as a Python
installable, the easiest way to use it is to ``git clone`` it into your
project directory along with its submodules. An example directory
structure is:

  | my_project/
  |   |----__init__.py
  |   |----my_project/
  |   |----dlkit/
  |          |----aws_adapter/
  |          |----handcar/
  |          |----mongo/records/
  |          |----primordium/
  |   |----dlkit_runtime/
  |          |----configs.py
  |          |----registry.py


Dependencies
------------

DLKit has several dependencies that are also listed as git submodules. They
are relisted here for convenience, along with their git repositories:

  * AWS Adapter (for storing / retrieving files from Amazon AWS S3): https://bitbucket.org/cjshaw/aws_adapter
  * Handcar (MC3 learning service-based implementation): https://bitbucket.org/cjshaw/handcar
  * Primordium (basic object types): https://bitbucket.org/cjshaw/primordium
  * Record extensions (for extending objects in the MongoDB implementation): https://github.mit.edu/sei/dlkit_records
