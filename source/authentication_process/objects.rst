.. currentmodule:: dlkit.authentication.process.objects
.. automodule:: dlkit.authentication.process.objects

Objects
=======


Authentication
--------------

.. autoclass:: Authentication
   :show-inheritance:

   .. autoattribute:: Authentication.agent_id

   .. autoattribute:: Authentication.agent

   .. automethod:: Authentication.is_valid

   .. automethod:: Authentication.has_expiration

   .. autoattribute:: Authentication.expiration

   .. automethod:: Authentication.has_credential

   .. automethod:: Authentication.get_credential

   .. automethod:: Authentication.get_authentication_record



Challenge
---------

.. autoclass:: Challenge
   :show-inheritance:

   .. automethod:: Challenge.get_challenge_record



Trust
-----

.. autoclass:: Trust
   :show-inheritance:

   .. automethod:: Trust.get_trust_record



Trust List
----------

.. autoclass:: TrustList
   :show-inheritance:

   .. autoattribute:: TrustList.next_trust

   .. automethod:: TrustList.get_next_trusts



