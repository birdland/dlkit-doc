

Sessions
========


Proxy Session
-------------

.. py:class:: ProxySession(abc_proxy_sessions.ProxySession, osid_sessions.OsidSession)
    This session converts external data into a proxy for use in OSID proxy managers.


    The external data is specified in the form of a ``ProxyCondition``.





    .. py:method:: get_proxy_condition():
        :noindex:


    .. py:attribute:: proxy_condition
        :noindex:


    .. py:method:: get_proxy(input_):
        :noindex:


