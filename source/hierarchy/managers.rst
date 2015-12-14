
.. currentmodule:: dlkit.hierarchy.managers
.. automodule:: dlkit.hierarchy.managers

Managers
========


Hierarchy Profile
-----------------

.. autoclass:: HierarchyProfile
   :show-inheritance:

   .. automethod:: HierarchyProfile.supports_visible_federation

   .. automethod:: HierarchyProfile.supports_hierarchy_traversal

   .. automethod:: HierarchyProfile.supports_hierarchy_design

   .. automethod:: HierarchyProfile.supports_hierarchy_sequencing

   .. automethod:: HierarchyProfile.supports_hierarchy_structure_notification

   .. automethod:: HierarchyProfile.supports_hierarchy_lookup

   .. automethod:: HierarchyProfile.supports_hierarchy_query

   .. automethod:: HierarchyProfile.supports_hierarchy_search

   .. automethod:: HierarchyProfile.supports_hierarchy_admin

   .. automethod:: HierarchyProfile.supports_hierarchy_notification

   .. autoattribute:: HierarchyProfile.hierarchy_record_types

   .. automethod:: HierarchyProfile.supports_hierarchy_record_type

   .. autoattribute:: HierarchyProfile.hierarchy_search_record_types

   .. automethod:: HierarchyProfile.supports_hierarchy_search_record_type

Hierarchy Manager
-----------------

.. autoclass:: HierarchyManager
   :show-inheritance:

   .. autoattribute:: HierarchyManager.hierarchy_traversal_session

   .. automethod:: HierarchyManager.get_hierarchy_traversal_session_for_hierarchy

   .. autoattribute:: HierarchyManager.hierarchy_design_session

   .. automethod:: HierarchyManager.get_hierarchy_design_session_for_hierarchy

   .. autoattribute:: HierarchyManager.hierarchy_sequencing_session

   .. automethod:: HierarchyManager.get_hierarchy_sequencing_session_for_hierarchy

   .. automethod:: HierarchyManager.get_hierarchy_structure_notification_session

   .. automethod:: HierarchyManager.get_hierarchy_structure_notification_session_for_hierarchy

   .. autoattribute:: HierarchyManager.hierarchy_lookup_session

   .. autoattribute:: HierarchyManager.hierarchy_query_session

   .. autoattribute:: HierarchyManager.hierarchy_search_session

   .. autoattribute:: HierarchyManager.hierarchy_admin_session

   .. automethod:: HierarchyManager.get_hierarchy_notification_session

Hierarchy Proxy Manager
-----------------------

.. autoclass:: HierarchyProxyManager
   :show-inheritance:

   .. automethod:: HierarchyProxyManager.get_hierarchy_traversal_session

   .. automethod:: HierarchyProxyManager.get_hierarchy_traversal_session_for_hierarchy

   .. automethod:: HierarchyProxyManager.get_hierarchy_design_session

   .. automethod:: HierarchyProxyManager.get_hierarchy_design_session_for_hierarchy

   .. automethod:: HierarchyProxyManager.get_hierarchy_sequencing_session

   .. automethod:: HierarchyProxyManager.get_hierarchy_sequencing_session_for_hierarchy

   .. automethod:: HierarchyProxyManager.get_hierarchy_structure_notification_session

   .. automethod:: HierarchyProxyManager.get_hierarchy_structure_notification_session_for_hierarchy

   .. automethod:: HierarchyProxyManager.get_hierarchy_lookup_session

   .. automethod:: HierarchyProxyManager.get_hierarchy_query_session

   .. automethod:: HierarchyProxyManager.get_hierarchy_search_session

   .. automethod:: HierarchyProxyManager.get_hierarchy_admin_session

   .. automethod:: HierarchyProxyManager.get_hierarchy_notification_session

