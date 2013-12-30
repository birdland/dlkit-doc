from ..osid import managers as osid_managers


class TypeProfile(osid_managers.OsidProfile):
    """The ``TypeProfile`` describes the interoperability among type services."""
    def supports_type_lookup(self):
        """Tests if ``Type`` lookup is supported.

        :return: ``true`` if ``Type`` lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_type_admin(self):
        """Tests if a ``Type`` administrative service is supported.

        :return: ``true`` if ``Type`` administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean


class TypeManager(osid_managers.OsidManager, TypeProfile):
    """This manager provides access to the available sessions of the type service.

    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.

    """
    def get_type_lookup_session(self):
        """Gets the ``OsidSession`` associated with the type lookup service.

        :return: a ``TypeLookupSession``
        :rtype: ``osid.type.TypeLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_type_lookup()`` is ``false``

        """
        return # osid.type.TypeLookupSession

    type_lookup_session = property(fget=get_type_lookup_session)

    def get_type_admin_session(self):
        """Gets the ``OsidSession`` associated with the type admin service.

        :return: a ``TypeAdminSession``
        :rtype: ``osid.type.TypeAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_type_admin()`` is ``false``

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

        """
        return # osid.type.TypeAdminSession

