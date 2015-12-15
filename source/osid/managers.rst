

Managers
========


Osid Profile
------------

.. py:class:: OsidProfile(abc_osid_managers.OsidProfile, osid_markers.Sourceable)
    The ``OsidProfile`` defines the interoperability areas of an OSID.


    An ``OsidProfile`` is implemented by an ``OsidManager``. The top
    level ``OsidProfile`` tests for version compatibility. Each OSID
    extends this interface to include its own interoperability
    definitions within its managers.





    .. py:method:: get_id():
        :noindex:


    .. py:attribute:: id_
        :noindex:


    .. py:attribute:: ident
        :noindex:


    .. py:method:: get_display_name():
        :noindex:


    .. py:attribute:: display_name
        :noindex:


    .. py:method:: get_description():
        :noindex:


    .. py:attribute:: description
        :noindex:


    .. py:method:: get_version():
        :noindex:


    .. py:attribute:: version
        :noindex:


    .. py:method:: get_release_date():
        :noindex:


    .. py:attribute:: release_date
        :noindex:


    .. py:method:: supports_osid_version(version):
        :noindex:


    .. py:method:: get_locales():
        :noindex:


    .. py:attribute:: locales
        :noindex:


    .. py:method:: supports_journal_rollback():
        :noindex:


    .. py:method:: supports_journal_branching():
        :noindex:


    .. py:method:: get_branch_id():
        :noindex:


    .. py:attribute:: branch_id
        :noindex:


    .. py:method:: get_branch():
        :noindex:


    .. py:attribute:: branch
        :noindex:


    .. py:method:: get_proxy_record_types():
        :noindex:


    .. py:attribute:: proxy_record_types
        :noindex:


    .. py:method:: supports_proxy_record_type(proxy_record_type):
        :noindex:


Osid Manager
------------

.. py:class:: OsidManager(abc_osid_managers.OsidManager, OsidProfile)
    The ``OsidManager`` is the top level interface for all OSID managers.


    An OSID manager is instantiated through the ``OsidRuntimeManager``
    and represents an instance of a service. An OSID manager is
    responsible for implementing a profile for a service and creating
    sessions that, in general, correspond to the profile. An application
    need only create a single ``OsidManager`` per service and
    implementors must ensure the ``OsidManager`` is thread-safe ````.
    The ``OsidSessions`` spawned from an OSID manager are dedicated to
    single processing threads. The ``OsidManager`` defines methods in
    common throughout all OSID managers which implement this interface.





    .. py:method:: initialize(runtime):
        :noindex:


    .. py:method:: rollback_service(rollback_time):
        :noindex:


    .. py:method:: change_branch(branch_id):
        :noindex:


Osid Proxy Manager
------------------

.. py:class:: OsidProxyManager(abc_osid_managers.OsidProxyManager, OsidProfile)
    The ``OsidProxyManager`` is the top level interface for all OSID proxy managers.


    A proxy manager accepts parameters to pass through end-user
    authentication credentials and other necessary request parameters in
    a server environment. Native applications should use an
    ``OsidManager`` to maintain a higher degree of interoperability by
    avoiding this coupling.




    An OSID proxy manager is instantiated through the
    ``OsidRuntimeManager`` and represents an instance of a service. An
    OSID manager is responsible for defining clusters of
    interoperability within a service and creating sessions that
    generally correspond to these clusters, An application need only
    create a single ``OsidProxyManager`` per service and implementors
    must ensure the ``OsidProxyManager`` is thread-safe ````. The
    ``OsidSessions`` spawned from an OSID manager are dedicated to
    single processing threads. The ``OsidProxyManager`` defines methods
    in common throughout all OSID managers which implement this
    interface.





    .. py:method:: initialize(runtime):
        :noindex:


    .. py:method:: rollback_service(rollback_time, proxy):
        :noindex:


    .. py:method:: change_branch(branch_id, proxy):
        :noindex:


Osid Runtime Profile
--------------------

.. py:class:: OsidRuntimeProfile(abc_osid_managers.OsidRuntimeProfile, OsidProfile)
    The ``OsidRuntimeProfile`` defines the service aspects of the OSID runtime service.

    .. py:method:: supports_configuration():
        :noindex:


Osid Runtime Manager
--------------------

.. py:class:: OsidRuntimeManager(abc_osid_managers.OsidRuntimeManager, OsidManager, OsidRuntimeProfile)
        :noindex:

    .. py:method:: get_manager(osid, impl_class_name, version):
        :noindex:


    .. py:method:: get_proxy_manager(osid, implementation, version):
        :noindex:


    .. py:method:: get_configuration():
        :noindex:


    .. py:attribute:: configuration
        :noindex:


