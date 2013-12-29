.. currentmodule:: dlkit.authorization.receivers
.. automodule:: dlkit.authorization.receivers

Receivers
=========


Authorization Receiver
----------------------

.. autoclass:: AuthorizationReceiver
   :show-inheritance:

.. automethod:: AuthorizationReceiver.new_authorization

.. automethod:: AuthorizationReceiver.changed_authorization

.. automethod:: AuthorizationReceiver.deleted_authorization



Function Receiver
-----------------

.. autoclass:: FunctionReceiver
   :show-inheritance:

.. automethod:: FunctionReceiver.new_function

.. automethod:: FunctionReceiver.changed_function

.. automethod:: FunctionReceiver.deleted_function



Qualifier Receiver
------------------

.. autoclass:: QualifierReceiver
   :show-inheritance:

.. automethod:: QualifierReceiver.new_qualifier

.. automethod:: QualifierReceiver.new_ancestor_qualifier

.. automethod:: QualifierReceiver.new_descendant_qualifier

.. automethod:: QualifierReceiver.changed_qualifier

.. automethod:: QualifierReceiver.deleted_qualifier

.. automethod:: QualifierReceiver.deleted_ancestor_qualifier

.. automethod:: QualifierReceiver.deleted_descendant_qualifier



Vault Receiver
--------------

.. autoclass:: VaultReceiver
   :show-inheritance:

.. automethod:: VaultReceiver.new_vault

.. automethod:: VaultReceiver.new_ancestor_vault

.. automethod:: VaultReceiver.new_descendant_vault

.. automethod:: VaultReceiver.changed_vault

.. automethod:: VaultReceiver.deleted_vault

.. automethod:: VaultReceiver.deleted_ancestor_vault

.. automethod:: VaultReceiver.deleted_descendant_vault



