
from ..osid import managers as osid_managers


class ProxyProfile(osid_managers.OsidProfile):
    """The ``ProxyProfile`` describes the interoperability among proxy services."""
    



    def supports_proxy(self):
        """Tests if a proxy session is supported.

        return: (boolean) - ``true`` if proxy is supported ``,``
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_proxy_record_types(self):
        """Gets the supported ``Proxy`` record interface types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Proxy`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    proxy_record_types = property(fget=get_proxy_record_types)


    def supports_proxy_record_type(self, proxy_record_type):
        """Tests if the given ``Proxy`` record interface type is supported.

        arg:    proxy_record_type (osid.type.Type): a ``Type``
                indicating a ``Proxy`` record type
        return: (boolean) - ``true`` if the given type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``proxy_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_proxy_condition_record_types(self):
        """Gets the supported ``ProxyCondition`` record interface types.

        return: (osid.type.TypeList) - a list containing the supported
                ``ProxyCondition`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    proxy_condition_record_types = property(fget=get_proxy_condition_record_types)


    def supports_proxy_condition_record_type(self, proxy_condition_record_type):
        """Tests if the given ``ProxyCondition`` record interface type is supported.

        arg:    proxy_condition_record_type (osid.type.Type): a ``Type``
                indicating a ``ProxyCondition`` record type
        return: (boolean) - ``true`` if the given type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``proxy_condition_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


