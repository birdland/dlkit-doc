.. currentmodule:: dlkit.services.type
.. automodule:: dlkit.services.type

Services
========


Type Manager
------------

.. autoclass:: TypeManager
   :show-inheritance:





Type
____

.. automethod:: TypeManager.supports_type_lookup

.. automethod:: TypeManager.supports_type_admin



Type
____





Type Proxy
__________

.. automethod:: TypeManager.get_type_lookup_session

.. automethod:: TypeManager.get_type_admin_session



Type Lookup
___________

.. automethod:: TypeManager.can_lookup_types

.. automethod:: TypeManager.get_type

.. automethod:: TypeManager.has_type

.. automethod:: TypeManager.get_types_by_domain

.. automethod:: TypeManager.get_types_by_authority

.. automethod:: TypeManager.get_types_by_domain_and_authority

.. autoattribute:: TypeManager.types

.. automethod:: TypeManager.is_equivalent

.. automethod:: TypeManager.implies_support

.. automethod:: TypeManager.has_base_type

.. automethod:: TypeManager.get_base_types



Type Admin
__________

.. automethod:: TypeManager.can_create_types

.. autoattribute:: TypeManager.type_form_for_create

.. automethod:: TypeManager.create_type

.. automethod:: TypeManager.can_update_types

.. automethod:: TypeManager.can_update_type

.. automethod:: TypeManager.get_type_form_for_update

.. automethod:: TypeManager.update_type

.. automethod:: TypeManager.can_delete_types

.. automethod:: TypeManager.can_delete_type

.. automethod:: TypeManager.delete_type

.. automethod:: TypeManager.make_equivalent

.. automethod:: TypeManager.add_base_type

.. automethod:: TypeManager.remove_base_type






.. autoattribute:: TypeManager.display_name

.. autoattribute:: TypeManager.display_label

.. autoattribute:: TypeManager.description

.. autoattribute:: TypeManager.domain

.. autoattribute:: TypeManager.authority

.. autoattribute:: TypeManager.namespace

.. autoattribute:: TypeManager.identifier



Type
____

.. autoattribute:: TypeManager.display_name_metadata

.. autoattribute:: TypeManager.display_name

.. autoattribute:: TypeManager.display_label_metadata

.. autoattribute:: TypeManager.display_label

.. autoattribute:: TypeManager.description_metadata

.. autoattribute:: TypeManager.description

.. autoattribute:: TypeManager.domain_metadata

.. autoattribute:: TypeManager.domain



Type
____

.. autoattribute:: TypeManager.next_type

.. automethod:: TypeManager.get_next_types



Type Proxy Manager
------------------

.. autoclass:: TypeProxyManager
   :show-inheritance:

.. automethod:: TypeProxyManager.get_type_lookup_session

.. automethod:: TypeProxyManager.get_type_admin_session



