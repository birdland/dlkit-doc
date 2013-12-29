.. currentmodule:: dlkit_doc.authentication.process
.. automodule:: dlkit_doc.authentication.process

Services
========


Authentication Process Manager
------------------------------

.. autoclass:: AuthenticationProcessManager
   :show-inheritance:





Authentication Process Profile Methods
______________________________

.. automethod:: AuthenticationProcessManager.supports_authentication_acquisition

.. automethod:: AuthenticationProcessManager.supports_authentication_validation

.. automethod:: AuthenticationProcessManager.supports_trust_lookup

.. automethod:: AuthenticationProcessManager.supports_circle_of_trust

.. automethod:: AuthenticationProcessManager.supports_challenge

.. autoattribute:: AuthenticationProcessManager.authentication_record_types

.. automethod:: AuthenticationProcessManager.supports_authentication_record_type

.. autoattribute:: AuthenticationProcessManager.authentication_input_record_types

.. automethod:: AuthenticationProcessManager.supports_authentication_input_record_type

.. autoattribute:: AuthenticationProcessManager.challenge_record_types

.. automethod:: AuthenticationProcessManager.supports_challenge_record_type

.. automethod:: AuthenticationProcessManager.supports_credential_export

.. autoattribute:: AuthenticationProcessManager.credential_types

.. automethod:: AuthenticationProcessManager.supports_credential_type

.. autoattribute:: AuthenticationProcessManager.trust_types

.. automethod:: AuthenticationProcessManager.supports_trust_type



Authentication Process Proxy Manager
------------------------------------

.. autoclass:: AuthenticationProcessProxyManager
   :show-inheritance:

.. automethod:: AuthenticationProcessProxyManager.get_authentication_acquisition_session

.. automethod:: AuthenticationProcessProxyManager.get_authentication_validation_session

.. automethod:: AuthenticationProcessProxyManager.get_trust_lookup_session

.. automethod:: AuthenticationProcessProxyManager.get_trust_lookup_session_for_agency

.. automethod:: AuthenticationProcessProxyManager.get_circle_of_trust_session

.. automethod:: AuthenticationProcessProxyManager.get_circle_of_trust_session_for_agency



