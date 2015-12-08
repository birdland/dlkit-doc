
.. currentmodule:: dlkit.services.osid
.. automodule:: dlkit.services.osid

Service Managers
================


Osid Runtime Manager
--------------------

.. autoclass:: OsidRuntimeManager
   :show-inheritance:

   .. automethod:: OsidRuntimeManager.get_manager

   .. automethod:: OsidRuntimeManager.get_proxy_manager

   .. autoattribute:: OsidRuntimeManager.configuration



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



