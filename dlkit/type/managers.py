
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class TypeProfile(osid_managers.OsidProfile):
    """The ``TypeProfile`` describes the interoperability among type services."""
    



    def supports_type_lookup(self):
        """Tests if ``Type`` lookup is supported.

        return: (boolean) - ``true`` if ``Type`` lookup is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def supports_type_admin(self):
        """Tests if a ``Type`` administrative service is supported.

        return: (boolean) - ``true`` if ``Type`` administration is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


class TypeManager(osid_managers.OsidManager, osid_sessions.OsidSession, TypeProfile):
    """This manager provides access to the available sessions of the type service.

    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.

    """
    



    def get_type_lookup_session(self):
        """Gets the ``OsidSession`` associated with the type lookup service.

        return: (osid.type.TypeLookupSession) - a ``TypeLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_type_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_type_lookup()`` is ``true``.*

        """
        return # osid.type.TypeLookupSession

    type_lookup_session = property(fget=get_type_lookup_session)


    def get_type_admin_session(self):
        """Gets the ``OsidSession`` associated with the type admin service.

        return: (osid.type.TypeAdminSession) - a ``TypeAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_type_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_type_admin()`` is ``true``.*

        """
        return # osid.type.TypeAdminSession

    type_admin_session = property(fget=get_type_admin_session)


