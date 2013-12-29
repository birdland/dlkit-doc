from ..osid import sessions as osid_sessions


class ProxySession(osid_sessions.OsidSession):
    """This session converts external data into a proxy for use in OSID proxy managers.

    The external data is specified in the form of a ``ProxyCondition``.

    """
    def get_proxy_condition(self):
        """Gets a proxy condition for acquiring a proxy.

        A new proxy condition should be acquired for each proxy request.

        :return: a proxy condiiton
        :rtype: ``osid.proxy.ProxyCondition``

        """
        return # osid.proxy.ProxyCondition

    proxy_condition = property(fget=get_proxy_condition)

    def get_proxy(self, input):
        """Gets a proxy.

        :param input: a proxy condition
        :type input: ``osid.proxy.ProxyCondition``
        :return: a proxy
        :rtype: ``osid.proxy.Proxy``
        :raise: ``NullArgument`` -- ``input`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``input`` is not of this service

        """
        return # osid.proxy.Proxy


