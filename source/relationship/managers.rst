
.. currentmodule:: dlkit.relationship.managers
.. automodule:: dlkit.relationship.managers

Managers
========


Relationship Profile
--------------------

.. autoclass:: RelationshipProfile
   :show-inheritance:

   .. automethod:: RelationshipProfile.supports_visible_federation

   .. automethod:: RelationshipProfile.supports_relationship_lookup

   .. automethod:: RelationshipProfile.supports_relationship_query

   .. automethod:: RelationshipProfile.supports_relationship_search

   .. automethod:: RelationshipProfile.supports_relationship_admin

   .. automethod:: RelationshipProfile.supports_relationship_notification

   .. automethod:: RelationshipProfile.supports_relationship_family

   .. automethod:: RelationshipProfile.supports_relationship_family_assignment

   .. automethod:: RelationshipProfile.supports_relationship_smart_family

   .. automethod:: RelationshipProfile.supports_family_lookup

   .. automethod:: RelationshipProfile.supports_family_query

   .. automethod:: RelationshipProfile.supports_family_search

   .. automethod:: RelationshipProfile.supports_family_admin

   .. automethod:: RelationshipProfile.supports_family_notification

   .. automethod:: RelationshipProfile.supports_family_hierarchy

   .. automethod:: RelationshipProfile.supports_family_hierarchy_design

   .. automethod:: RelationshipProfile.supports_relationship_batch

   .. automethod:: RelationshipProfile.supports_relationship_rules

   .. autoattribute:: RelationshipProfile.relationship_record_types

   .. automethod:: RelationshipProfile.supports_relationship_record_type

   .. autoattribute:: RelationshipProfile.relationship_search_record_types

   .. automethod:: RelationshipProfile.supports_relationship_search_record_type

   .. autoattribute:: RelationshipProfile.family_record_types

   .. automethod:: RelationshipProfile.supports_family_record_type

   .. autoattribute:: RelationshipProfile.family_search_record_types

   .. automethod:: RelationshipProfile.supports_family_search_record_type

Relationship Manager
--------------------

.. autoclass:: RelationshipManager
   :show-inheritance:

   .. autoattribute:: RelationshipManager.relationship_lookup_session

   .. automethod:: RelationshipManager.get_relationship_lookup_session_for_family

   .. autoattribute:: RelationshipManager.relationship_query_session

   .. automethod:: RelationshipManager.get_relationship_query_session_for_family

   .. autoattribute:: RelationshipManager.relationship_search_session

   .. automethod:: RelationshipManager.get_relationship_search_session_for_family

   .. autoattribute:: RelationshipManager.relationship_admin_session

   .. automethod:: RelationshipManager.get_relationship_admin_session_for_family

   .. automethod:: RelationshipManager.get_relationship_notification_session

   .. automethod:: RelationshipManager.get_relationship_notification_session_for_family

   .. autoattribute:: RelationshipManager.relationship_family_session

   .. autoattribute:: RelationshipManager.relationship_family_assignment_session

   .. automethod:: RelationshipManager.get_relationship_smart_family_session

   .. autoattribute:: RelationshipManager.family_lookup_session

   .. autoattribute:: RelationshipManager.family_query_session

   .. autoattribute:: RelationshipManager.family_search_session

   .. autoattribute:: RelationshipManager.family_admin_session

   .. automethod:: RelationshipManager.get_family_notification_session

   .. autoattribute:: RelationshipManager.family_hierarchy_session

   .. autoattribute:: RelationshipManager.family_hierarchy_design_session

   .. autoattribute:: RelationshipManager.relationship_batch_manager

   .. autoattribute:: RelationshipManager.relationship_rules_manager

Relationship Proxy Manager
--------------------------

.. autoclass:: RelationshipProxyManager
   :show-inheritance:

   .. automethod:: RelationshipProxyManager.get_relationship_lookup_session

   .. automethod:: RelationshipProxyManager.get_relationship_lookup_session_for_family

   .. automethod:: RelationshipProxyManager.get_relationship_query_session

   .. automethod:: RelationshipProxyManager.get_relationship_query_session_for_family

   .. automethod:: RelationshipProxyManager.get_relationship_search_session

   .. automethod:: RelationshipProxyManager.get_relationship_search_session_for_family

   .. automethod:: RelationshipProxyManager.get_relationship_admin_session

   .. automethod:: RelationshipProxyManager.get_relationship_admin_session_for_family

   .. automethod:: RelationshipProxyManager.get_relationship_notification_session

   .. automethod:: RelationshipProxyManager.get_relationship_notification_session_for_family

   .. automethod:: RelationshipProxyManager.get_relationship_family_session

   .. automethod:: RelationshipProxyManager.get_relationship_family_assignment_session

   .. automethod:: RelationshipProxyManager.get_relationship_smart_family_session

   .. automethod:: RelationshipProxyManager.get_family_lookup_session

   .. automethod:: RelationshipProxyManager.get_family_query_session

   .. automethod:: RelationshipProxyManager.get_family_search_session

   .. automethod:: RelationshipProxyManager.get_family_admin_session

   .. automethod:: RelationshipProxyManager.get_family_notification_session

   .. automethod:: RelationshipProxyManager.get_family_hierarchy_session

   .. automethod:: RelationshipProxyManager.get_family_hierarchy_design_session

   .. autoattribute:: RelationshipProxyManager.relationship_batch_proxy_manager

   .. autoattribute:: RelationshipProxyManager.relationship_rules_proxy_manager

