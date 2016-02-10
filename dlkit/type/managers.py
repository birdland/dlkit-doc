
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class TypeProfile(osid_managers.OsidProfile):
    """The ``TypeProfile`` describes the interoperability among type services."""




class TypeManager(osid_managers.OsidManager, osid_sessions.OsidSession, TypeProfile):
    """This manager provides access to the available sessions of the type service.

    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.

    """




class TypeProxyManager(osid_managers.OsidProxyManager, TypeProfile):
    """This manager provides access to the available sessions of the type service.

    Methods in this manager support the passing of a ``Proxy`` object
    for the purpose of passing information from a server environment.
    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.

    """




