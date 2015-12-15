

Rules
=====


Proxy
-----

.. py:class:: Proxy(abc_proxy_rules.Proxy, osid_rules.OsidResult)
    A ``Proxy`` is used to transfer external information from an application server into an OSID
    Provider.

    .. py:method:: has_authentication():
        :noindex:


    .. py:method:: get_authentication():
        :noindex:


    .. py:attribute:: authentication
        :noindex:


    .. py:method:: has_effective_agent():
        :noindex:


    .. py:method:: get_effective_agent_id():
        :noindex:


    .. py:attribute:: effective_agent_id
        :noindex:


    .. py:method:: get_effective_agent():
        :noindex:


    .. py:attribute:: effective_agent
        :noindex:


    .. py:method:: has_effective_date():
        :noindex:


    .. py:method:: get_effective_date():
        :noindex:


    .. py:attribute:: effective_date
        :noindex:


    .. py:method:: get_effective_clock_rate():
        :noindex:


    .. py:attribute:: effective_clock_rate
        :noindex:


    .. py:method:: get_locale():
        :noindex:


    .. py:attribute:: locale
        :noindex:


    .. py:method:: has_format_type():
        :noindex:


    .. py:method:: get_format_type():
        :noindex:


    .. py:attribute:: format_type
        :noindex:


    .. py:method:: get_proxy_record(proxy_record_type):
        :noindex:


Proxy Condition
---------------

.. py:class:: ProxyCondition(abc_proxy_rules.ProxyCondition, osid_rules.OsidCondition)
    A ``ProxyCondition`` is used to transfer external information into a proxy.

    .. py:method:: set_effective_agent_id(agent_id):
        :noindex:


    .. py:attribute:: effective_agent_id
        :noindex:


    .. py:method:: set_effective_date(date, rate):
        :noindex:


    .. py:method:: set_language_type(language_type):
        :noindex:


    .. py:attribute:: language_type
        :noindex:


    .. py:method:: set_script_type(script_type):
        :noindex:


    .. py:attribute:: script_type
        :noindex:


    .. py:method:: set_calendar_type(calendar_type):
        :noindex:


    .. py:attribute:: calendar_type
        :noindex:


    .. py:method:: set_time_type(time_type):
        :noindex:


    .. py:attribute:: time_type
        :noindex:


    .. py:method:: set_currency_type(currency_type):
        :noindex:


    .. py:attribute:: currency_type
        :noindex:


    .. py:method:: set_unit_system_type(unit_system_type):
        :noindex:


    .. py:attribute:: unit_system_type
        :noindex:


    .. py:method:: set_format_type(format_type):
        :noindex:


    .. py:attribute:: format_type
        :noindex:


    .. py:method:: get_proxy_condition_record(proxy_condition_type):
        :noindex:


