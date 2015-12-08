
.. currentmodule:: dlkit.osid.managers
.. automodule:: dlkit.osid.managers

Managers
========


Osid Profile
------------

.. autoclass:: OsidProfile
   :show-inheritance:

   .. autoattribute:: OsidProfile.ident

   .. autoattribute:: OsidProfile.display_name

   .. autoattribute:: OsidProfile.description

   .. autoattribute:: OsidProfile.version

   .. autoattribute:: OsidProfile.release_date

   .. automethod:: OsidProfile.supports_osid_version

   .. autoattribute:: OsidProfile.locales

   .. automethod:: OsidProfile.supports_journal_rollback

   .. automethod:: OsidProfile.supports_journal_branching

   .. autoattribute:: OsidProfile.branch_id

   .. autoattribute:: OsidProfile.branch

   .. autoattribute:: OsidProfile.proxy_record_types

   .. automethod:: OsidProfile.supports_proxy_record_type



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



Osid Manager
------------

.. autoclass:: OsidManager
   :show-inheritance:

   .. automethod:: OsidManager.initialize

   .. automethod:: OsidManager.rollback_service

   .. automethod:: OsidManager.change_branch



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



Osid Proxy Manager
------------------

.. autoclass:: OsidProxyManager
   :show-inheritance:

   .. automethod:: OsidProxyManager.initialize

   .. automethod:: OsidProxyManager.rollback_service

   .. automethod:: OsidProxyManager.change_branch



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



Osid Runtime Profile
--------------------

.. autoclass:: OsidRuntimeProfile
   :show-inheritance:

   .. automethod:: OsidRuntimeProfile.supports_configuration



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



