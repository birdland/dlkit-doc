from ..osid import managers as osid_managers


class IdProfile(osid_managers.OsidProfile):
    """The ``IdProfile`` describes the interoperability among id services."""
    def supports_id_lookup(self):
        """Tests if ``Id`` lookup is supported.

        :return: ``true`` if ``Id`` lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_id_admin(self):
        """Tests if an ``Id`` administrative service is supported.

        :return: ``true`` if ``Id`` administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean


class IdManager(osid_managers.OsidManager, IdProfile):
    """This manager provides access to the available sessions of the Id service.

    ``Ids`` are created through the ``IdAdminSession`` which provides
    the means for creating a unique identifier.

    The ``IdLookupSession`` can be used for mapping one ``Id`` to
    another in addition to getting a list of the assigned identifiers.

    """
    def get_id_lookup_session(self):
        """Gets the session associated with the id lookup service.

        :return: an ``IdLookupSession``
        :rtype: ``osid.id.IdLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_id_lookup()`` is ``false``

        """
        return # osid.id.IdLookupSession

    id_lookup_session = property(fget=get_id_lookup_session)

    def get_id_admin_session(self):
        """Gets the session associated with the id admin service.

        :return: the new ``IdAdminSession``
        :rtype: ``osid.id.IdAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_id_admin()`` is ``false``

        """
        return # osid.id.IdAdminSession

    id_admin_session = property(fget=get_id_admin_session)


class IdProxyManager(osid_managers.OsidProxyManager, IdProfile):
    """This manager provides access to the available sessions of the Id service.

    Methods in this manager support the passing of a ``Proxy`` object
    for the purpose of pasisng information from a server envrionment.

    ``Ids`` are created through the ``IdAdminSession`` which provides
    the means for creating a unique identifier. The ``IdBrowserSession``
    can be used for mapping one ``Id`` to another in addition to getting
    a list of the assigned identifiers.

    """
    def get_id_lookup_session(self, proxy):
        """Gets the session associated with the id lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``IdLookupSession``
        :rtype: ``osid.id.IdLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_id_lookup()`` is ``false``

        """
        return # osid.id.IdLookupSession

    def get_id_admin_session(self, proxy):
        """Gets the session associated with the id administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``IdAdminSession``
        :rtype: ``osid.id.IdAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_id_admin()`` is ``false``

        """
        return # osid.id.IdAdminSession


