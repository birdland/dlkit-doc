Configuring DLKit
=================

DLKit requires the use of a runtime environment, from which you
configure the user proxy object, get managers, and define which
implementations are used for each service (among other things).
For example, you might use the built-in MongoDB ``learning``
service, or you may decide to use the MC3_ RESTful service,
Handcar.

.. _MC3: http://mc3.mit.edu

Two examples are available, one for Open edX and another for Django. You
can also build your own, using these as templates:

* Open edX runtime: https://github.mit.edu/sei/dlkit_edx
* Django runtime: https://github.mit.edu/sei/dlkit_django

Both runtimes require the addition of ``configs.py`` and
``registry.py`` files. These allow different instances of
DLKit to behave differently, depending on the project's needs.

**NOTE:** With the Django runtime, you can establish the configuration
values in your project's ``settings.py`` file, which is then referenced
in the runtime files below. This is for your convenience. You can
also configure the settings directly in the files below, as shown
in the Open edX runtime.

.. _runtime-config:

configs.py
----------

This file allows you to define various parameters used in the production
runtime as well as a testing runtime. The only required values are for
``BOOTSTRAP`` and ``SERVICE`` (and for running the DLKit tests,
``TEST_SERVICE``).

``SERVICE`` should point to the implementation you want to use for each
service (i.e. Handcar for the ``learning`` service, MongoDB for the
assessment service).

Currently, this file also lets you manage the following

* Amazon AWS credentials, if using the AWS shim adapter.
* MongoDB authority, for identifying objects / IDs created by this instance.
* MongoDB database prefix, to namespace your collections and documents.
* MongoDB fields to index on.
* MongoDB fields to search on, for keyword searches.
* MongoDB host URI, if using a sharded repository.

An example skeleton is included in the runtime repository.

registry.py
-----------

Similar to ``setup.py``, this file includes the various entry points
for each service and implementation. For example, if you expect to use the ``grading``
service from the MongoDB implementation, you need to make sure it has
an entry in this file. An example skeleton is included in the repository.


handcar_configs.py
------------------

If you are using the `MC3 Handcar` learning service, then you will also
need to add in proxy agent keys for the appropriate service / server combination
in this file, if you want more than read-access.

.. _MC3 Handcar: http://mc3.mit.edu