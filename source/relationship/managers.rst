

Managers
========


Relationship Profile
--------------------

.. py:class:: RelationshipProfile(osid_managers.OsidProfile, relationship_managers.RelationshipProfile)
    The relationship profile describes the interoperability among relationship services.

    .. py:method:: supports_visible_federation():
        :noindex:


    .. py:method:: supports_relationship_lookup():
        :noindex:


    .. py:method:: supports_relationship_query():
        :noindex:


    .. py:method:: supports_relationship_search():
        :noindex:


    .. py:method:: supports_relationship_admin():
        :noindex:


    .. py:method:: supports_relationship_notification():
        :noindex:


    .. py:method:: supports_relationship_family():
        :noindex:


    .. py:method:: supports_relationship_family_assignment():
        :noindex:


    .. py:method:: supports_relationship_smart_family():
        :noindex:


    .. py:method:: supports_family_lookup():
        :noindex:


    .. py:method:: supports_family_query():
        :noindex:


    .. py:method:: supports_family_search():
        :noindex:


    .. py:method:: supports_family_admin():
        :noindex:


    .. py:method:: supports_family_notification():
        :noindex:


    .. py:method:: supports_family_hierarchy():
        :noindex:


    .. py:method:: supports_family_hierarchy_design():
        :noindex:


    .. py:method:: supports_relationship_batch():
        :noindex:


    .. py:method:: supports_relationship_rules():
        :noindex:


    .. py:method:: get_relationship_record_types():
        :noindex:


    .. py:attribute:: relationship_record_types
        :noindex:


    .. py:method:: supports_relationship_record_type(relationship_record_type):
        :noindex:


    .. py:method:: get_relationship_search_record_types():
        :noindex:


    .. py:attribute:: relationship_search_record_types
        :noindex:


    .. py:method:: supports_relationship_search_record_type(relationship_search_record_type):
        :noindex:


    .. py:method:: get_family_record_types():
        :noindex:


    .. py:attribute:: family_record_types
        :noindex:


    .. py:method:: supports_family_record_type(family_record_type):
        :noindex:


    .. py:method:: get_family_search_record_types():
        :noindex:


    .. py:attribute:: family_search_record_types
        :noindex:


    .. py:method:: supports_family_search_record_type(family_search_record_type):
        :noindex:


Relationship Manager
--------------------

.. py:class:: RelationshipManager(osid_managers.OsidManager, RelationshipProfile, relationship_managers.RelationshipManager)
        :noindex:

    .. py:method:: get_relationship_lookup_session():
        :noindex:


    .. py:attribute:: relationship_lookup_session
        :noindex:


    .. py:method:: get_relationship_lookup_session_for_family(family_id):
        :noindex:


    .. py:method:: get_relationship_query_session():
        :noindex:


    .. py:attribute:: relationship_query_session
        :noindex:


    .. py:method:: get_relationship_query_session_for_family(family_id):
        :noindex:


    .. py:method:: get_relationship_search_session():
        :noindex:


    .. py:attribute:: relationship_search_session
        :noindex:


    .. py:method:: get_relationship_search_session_for_family(family_id):
        :noindex:


    .. py:method:: get_relationship_admin_session():
        :noindex:


    .. py:attribute:: relationship_admin_session
        :noindex:


    .. py:method:: get_relationship_admin_session_for_family(family_id):
        :noindex:


    .. py:method:: get_relationship_notification_session(relationship_receiver):
        :noindex:


    .. py:method:: get_relationship_notification_session_for_family(relationship_receiver, family_id):
        :noindex:


    .. py:method:: get_relationship_family_session():
        :noindex:


    .. py:attribute:: relationship_family_session
        :noindex:


    .. py:method:: get_relationship_family_assignment_session():
        :noindex:


    .. py:attribute:: relationship_family_assignment_session
        :noindex:


    .. py:method:: get_relationship_smart_family_session(family_id):
        :noindex:


    .. py:method:: get_family_lookup_session():
        :noindex:


    .. py:attribute:: family_lookup_session
        :noindex:


    .. py:method:: get_family_query_session():
        :noindex:


    .. py:attribute:: family_query_session
        :noindex:


    .. py:method:: get_family_search_session():
        :noindex:


    .. py:attribute:: family_search_session
        :noindex:


    .. py:method:: get_family_admin_session():
        :noindex:


    .. py:attribute:: family_admin_session
        :noindex:


    .. py:method:: get_family_notification_session(family_receiver):
        :noindex:


    .. py:method:: get_family_hierarchy_session():
        :noindex:


    .. py:attribute:: family_hierarchy_session
        :noindex:


    .. py:method:: get_family_hierarchy_design_session():
        :noindex:


    .. py:attribute:: family_hierarchy_design_session
        :noindex:


    .. py:method:: get_relationship_batch_manager():
        :noindex:


    .. py:attribute:: relationship_batch_manager
        :noindex:


    .. py:method:: get_relationship_rules_manager():
        :noindex:


    .. py:attribute:: relationship_rules_manager
        :noindex:


Relationship Proxy Manager
--------------------------

.. py:class:: RelationshipProxyManager(osid_managers.OsidProxyManager, RelationshipProfile, relationship_managers.RelationshipProxyManager)
        :noindex:

    .. py:method:: get_relationship_lookup_session(proxy):
        :noindex:


    .. py:method:: get_relationship_lookup_session_for_family(family_id, proxy):
        :noindex:


    .. py:method:: get_relationship_query_session(proxy):
        :noindex:


    .. py:method:: get_relationship_query_session_for_family(family_id, proxy):
        :noindex:


    .. py:method:: get_relationship_search_session(proxy):
        :noindex:


    .. py:method:: get_relationship_search_session_for_family(family_id, proxy):
        :noindex:


    .. py:method:: get_relationship_admin_session(proxy):
        :noindex:


    .. py:method:: get_relationship_admin_session_for_family(family_id, proxy):
        :noindex:


    .. py:method:: get_relationship_notification_session(relationship_receiver, proxy):
        :noindex:


    .. py:method:: get_relationship_notification_session_for_family(relationship_receiver, family_id, proxy):
        :noindex:


    .. py:method:: get_relationship_family_session(proxy):
        :noindex:


    .. py:method:: get_relationship_family_assignment_session(proxy):
        :noindex:


    .. py:method:: get_relationship_smart_family_session(family_id, proxy):
        :noindex:


    .. py:method:: get_family_lookup_session(proxy):
        :noindex:


    .. py:method:: get_family_query_session(proxy):
        :noindex:


    .. py:method:: get_family_search_session(proxy):
        :noindex:


    .. py:method:: get_family_admin_session(proxy):
        :noindex:


    .. py:method:: get_family_notification_session(family_receiver, proxy):
        :noindex:


    .. py:method:: get_family_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_family_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_relationship_batch_proxy_manager():
        :noindex:


    .. py:attribute:: relationship_batch_proxy_manager
        :noindex:


    .. py:method:: get_relationship_rules_proxy_manager():
        :noindex:


    .. py:attribute:: relationship_rules_proxy_manager
        :noindex:


