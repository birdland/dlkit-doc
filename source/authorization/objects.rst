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



Function
--------

.. autoclass:: Function
   :show-inheritance:

   .. autoattribute:: Function.qualifier_hierarchy_id

   .. autoattribute:: Function.qualifier_hierarchy

   .. automethod:: Function.get_function_record



Function Form
-------------

.. autoclass:: FunctionForm
   :show-inheritance:

   .. autoattribute:: FunctionForm.qualifier_hierarchy_metadata

   .. autoattribute:: FunctionForm.qualifier_hierarchy

   .. automethod:: FunctionForm.get_function_form_record



Function List
-------------

.. autoclass:: FunctionList
   :show-inheritance:

   .. autoattribute:: FunctionList.next_function

   .. automethod:: FunctionList.get_next_functions



Qualifier
---------

.. autoclass:: Qualifier
   :show-inheritance:

   .. automethod:: Qualifier.get_qualifier_record



Qualifier Form
--------------

.. autoclass:: QualifierForm
   :show-inheritance:

   .. automethod:: QualifierForm.get_qualifier_form_record



Qualifier List
--------------

.. autoclass:: QualifierList
   :show-inheritance:

   .. autoattribute:: QualifierList.next_qualifier

   .. automethod:: QualifierList.get_next_qualifiers



Qualifier Node
--------------

.. autoclass:: QualifierNode
   :show-inheritance:

   .. autoattribute:: QualifierNode.qualifier

   .. autoattribute:: QualifierNode.parent_qualifier_nodes

   .. autoattribute:: QualifierNode.child_qualifier_nodes



Qualifier Node List
-------------------

.. autoclass:: QualifierNodeList
   :show-inheritance:

   .. autoattribute:: QualifierNodeList.next_qualifier_node

   .. automethod:: QualifierNodeList.get_next_qualifier_nodes



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



