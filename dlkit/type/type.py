
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions
from ..osid import markers as osid_markers
from ..osid import objects as osid_objects


class TypeProfile(osid_managers.OsidProfile):
    """The ``TypeProfile`` describes the interoperability among type services."""

    def supports_type_lookup(self):
        """Tests if ``Type`` lookup is supported.


        :return: ``true`` if ``Type`` lookup is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_type_admin(self):
        """Tests if a ``Type`` administrative service is supported.


        :return: ``true`` if ``Type`` administration is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean


class TypeManager(osid_managers.OsidManager, osid_sessions.OsidSession, TypeProfile):
    """This manager provides access to the available sessions of the type service.


    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.


    """




    def __init__(self, proxy=None):
        import settings
        import importlib
        self._runtime = None
        provider_module = importlib.import_module(settings.TYPE_PROVIDER_MANAGER_PATH, settings.ANCHOR_PATH)
        provider_manager_class = getattr(provider_module, 'TypeManager')
        self._provider_manager = provider_manager_class()
        self._provider_sessions = dict()
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)


    def _get_provider_session(self, session):
        if session in self._provider_sessions:
            return self._provider_sessions[session]
        else:
            try:
                get_session = getattr(self._provider_manager, 'get_' + session)
            except:
                raise # Unimplemented???
            else:
                self._provider_sessions[session] = get_session()
            return self._provider_sessions[session]


    def initialize(self, runtime):
        """OSID Manager initialize"""
        from .primitives import Id
        if self._runtime is not None:
            raise IllegalState('Manager has already been initialized')
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:typeProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        # do not account for TypeProxyManager yet...not used in Handcar
        # need to add version argument
        self._provider_manager = runtime.get_manager('TYPE', provider_impl)


    def get_types(self, *args, **kwargs):
        """Pass through to provider method"""
        # Implemented from
        # osid.type.TypeLookupSession.get_types
        return self._get_provider_session('type_lookup_session').get_types(*args, **kwargs)
    def get_type_lookup_session(self):
        """Gets the ``OsidSession`` associated with the type lookup service.


        :return: a ``TypeLookupSession``
        :rtype: ``osid.type.TypeLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_type_lookup()`` is ``false``


        *compliance: optional -- This method must be implemented if
        ``supports_type_lookup()`` is ``true``.*


        """
        return # osid.type.TypeLookupSession

    type_lookup_session = property(fget=get_type_lookup_session)

    def get_type_admin_session(self):
        """Gets the ``OsidSession`` associated with the type admin service.


        :return: a ``TypeAdminSession``
        :rtype: ``osid.type.TypeAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_type_admin()`` is ``false``


        *compliance: optional -- This method must be implemented if
        ``supports_type_admin()`` is ``true``.*


        """
        return # osid.type.TypeAdminSession

    type_admin_session = property(fget=get_type_admin_session)


class TypeProxyManager(osid_managers.OsidProxyManager, TypeProfile):
    """This manager provides access to the available sessions of the type service.


    Methods in this manager support the passing of a ``Proxy`` object
    for the purpose of passing information from a server environment.
    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.


    """

    def get_type_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the type lookup service.


        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TypeLookupSession``
        :rtype: ``osid.type.TypeLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_type_lookup()`` is ``false``


        *compliance: optional -- This method must be implemented if
        ``supports_type_lookup()`` is ``true``.*


        """
        return # osid.type.TypeLookupSession

    def get_type_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the ``TypeAdmin`` service.


        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: the new ``TypeAdminSession``
        :rtype: ``osid.type.TypeAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_type_admin()`` is ``false``


        *compliance: optional -- This method must be implemented if
        ``supports_type_admin()`` is ``true``.*


        """
        return # osid.type.TypeAdminSession


