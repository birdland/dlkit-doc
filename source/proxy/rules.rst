.. currentmodule:: dlkit.proxy.rules
.. automodule:: dlkit.proxy.rules

Rules
=====


Proxy
-----

.. autoclass:: Proxy
   :show-inheritance:

.. automethod:: Proxy.has_authentication

.. autoattribute:: Proxy.authentication

.. automethod:: Proxy.has_effective_agent

.. autoattribute:: Proxy.effective_agent_id

.. automethod:: Proxy.has_effective_date

.. autoattribute:: Proxy.effective_date

.. autoattribute:: Proxy.effective_clock_rate

.. autoattribute:: Proxy.locale

.. automethod:: Proxy.get_proxy_record



Proxy Condition
---------------

.. autoclass:: ProxyCondition
   :show-inheritance:

.. autoattribute:: ProxyCondition.effective_agent_id

.. automethod:: ProxyCondition.set_effective_date

.. autoattribute:: ProxyCondition.language_type

.. autoattribute:: ProxyCondition.script_type

.. autoattribute:: ProxyCondition.calendar_type

.. autoattribute:: ProxyCondition.time_type

.. autoattribute:: ProxyCondition.currency_type

.. autoattribute:: ProxyCondition.unit_system_type

.. automethod:: ProxyCondition.get_proxy_condition_record



