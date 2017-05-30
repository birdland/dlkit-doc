
.. currentmodule:: dlkit.authorization.objects
.. automodule:: dlkit.authorization.objects

Objects
=======


Authorization
-------------

.. autoclass:: Authorization
   :show-inheritance:

   .. automethod:: Authorization.is_implicit

   .. automethod:: Authorization.has_resource

   .. autoattribute:: Authorization.resource_id

   .. autoattribute:: Authorization.resource

   .. automethod:: Authorization.has_trust

   .. autoattribute:: Authorization.trust_id

   .. autoattribute:: Authorization.trust

   .. automethod:: Authorization.has_agent

   .. autoattribute:: Authorization.agent_id

   .. autoattribute:: Authorization.agent

   .. autoattribute:: Authorization.function_id

   .. autoattribute:: Authorization.function

   .. autoattribute:: Authorization.qualifier_id

   .. autoattribute:: Authorization.qualifier

   .. automethod:: Authorization.get_authorization_record

Authorization Form
------------------

.. autoclass:: AuthorizationForm
   :show-inheritance:

   .. automethod:: AuthorizationForm.get_authorization_form_record

Authorization List
------------------

.. autoclass:: AuthorizationList
   :show-inheritance:

   .. autoattribute:: AuthorizationList.next_authorization

   .. automethod:: AuthorizationList.get_next_authorizations

Vault
-----

.. py:class:: Vault(abc_authorization_objects.Vault, osid_objects.OsidCatalog)
        :noindex:

   .. automethod:: Vault.get_vault_record

Vault Form
----------

.. autoclass:: VaultForm
   :show-inheritance:

   .. automethod:: VaultForm.get_vault_form_record

Vault List
----------

.. autoclass:: VaultList
   :show-inheritance:

   .. autoattribute:: VaultList.next_vault

   .. automethod:: VaultList.get_next_vaults

Vault Node
----------

.. autoclass:: VaultNode
   :show-inheritance:

   .. autoattribute:: VaultNode.vault

   .. autoattribute:: VaultNode.parent_vault_nodes

   .. autoattribute:: VaultNode.child_vault_nodes

Vault Node List
---------------

.. autoclass:: VaultNodeList
   :show-inheritance:

   .. autoattribute:: VaultNodeList.next_vault_node

   .. automethod:: VaultNodeList.get_next_vault_nodes

