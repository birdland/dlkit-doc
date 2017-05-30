
.. currentmodule:: dlkit.services.authentication
.. automodule:: dlkit.services.authentication

Service Managers
================


Authentication Profile
----------------------

.. autoclass:: AuthenticationProfile
   :show-inheritance:

   .. automethod:: AuthenticationProfile.supports_agent_lookup

   .. autoattribute:: AuthenticationProfile.agent_record_types

   .. autoattribute:: AuthenticationProfile.agent_search_record_types

   .. autoattribute:: AuthenticationProfile.agency_record_types

   .. autoattribute:: AuthenticationProfile.agency_search_record_types

Authentication Manager
----------------------

.. autoclass:: AuthenticationManager
   :show-inheritance:

   .. autoattribute:: AuthenticationManager.authentication_batch_manager

   .. autoattribute:: AuthenticationManager.authentication_keys_manager

   .. autoattribute:: AuthenticationManager.authentication_process_manager



