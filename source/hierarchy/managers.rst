

Managers
========


Hierarchy Profile
-----------------

.. py:class:: HierarchyProfile(osid_managers.OsidProfile, hierarchy_managers.HierarchyProfile)
    The hierarchy profile describes the interoperability among hierarchy services.

    .. py:method:: supports_visible_federation():
        :noindex:


    .. py:method:: supports_hierarchy_traversal():
        :noindex:


    .. py:method:: supports_hierarchy_design():
        :noindex:


    .. py:method:: supports_hierarchy_sequencing():
        :noindex:


    .. py:method:: supports_hierarchy_structure_notification():
        :noindex:


    .. py:method:: supports_hierarchy_lookup():
        :noindex:


    .. py:method:: supports_hierarchy_query():
        :noindex:


    .. py:method:: supports_hierarchy_search():
        :noindex:


    .. py:method:: supports_hierarchy_admin():
        :noindex:


    .. py:method:: supports_hierarchy_notification():
        :noindex:


    .. py:method:: get_hierarchy_record_types():
        :noindex:


    .. py:attribute:: hierarchy_record_types
        :noindex:


    .. py:method:: supports_hierarchy_record_type(hierarchy_record_type):
        :noindex:


    .. py:method:: get_hierarchy_search_record_types():
        :noindex:


    .. py:attribute:: hierarchy_search_record_types
        :noindex:


    .. py:method:: supports_hierarchy_search_record_type(hierarchy_search_record_type):
        :noindex:


Hierarchy Manager
-----------------

.. py:class:: HierarchyManager(osid_managers.OsidManager, HierarchyProfile, hierarchy_managers.HierarchyManager)
        :noindex:

    .. py:method:: get_hierarchy_traversal_session():
        :noindex:


    .. py:attribute:: hierarchy_traversal_session
        :noindex:


    .. py:method:: get_hierarchy_traversal_session_for_hierarchy(hierarchy_id):
        :noindex:


    .. py:method:: get_hierarchy_design_session():
        :noindex:


    .. py:attribute:: hierarchy_design_session
        :noindex:


    .. py:method:: get_hierarchy_design_session_for_hierarchy(hierarchy_id):
        :noindex:


    .. py:method:: get_hierarchy_sequencing_session():
        :noindex:


    .. py:attribute:: hierarchy_sequencing_session
        :noindex:


    .. py:method:: get_hierarchy_sequencing_session_for_hierarchy(hierarchy_id):
        :noindex:


    .. py:method:: get_hierarchy_structure_notification_session(hierarchy_structure_receiver):
        :noindex:


    .. py:method:: get_hierarchy_structure_notification_session_for_hierarchy(hierarchy_structure_receiver, hierarchy_id):
        :noindex:


    .. py:method:: get_hierarchy_lookup_session():
        :noindex:


    .. py:attribute:: hierarchy_lookup_session
        :noindex:


    .. py:method:: get_hierarchy_query_session():
        :noindex:


    .. py:attribute:: hierarchy_query_session
        :noindex:


    .. py:method:: get_hierarchy_search_session():
        :noindex:


    .. py:attribute:: hierarchy_search_session
        :noindex:


    .. py:method:: get_hierarchy_admin_session():
        :noindex:


    .. py:attribute:: hierarchy_admin_session
        :noindex:


    .. py:method:: get_hierarchy_notification_session(hierarchy_receiver):
        :noindex:


Hierarchy Proxy Manager
-----------------------

.. py:class:: HierarchyProxyManager(osid_managers.OsidProxyManager, HierarchyProfile, hierarchy_managers.HierarchyProxyManager)
        :noindex:

    .. py:method:: get_hierarchy_traversal_session(proxy):
        :noindex:


    .. py:method:: get_hierarchy_traversal_session_for_hierarchy(hierarchy_id, proxy):
        :noindex:


    .. py:method:: get_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_hierarchy_design_session_for_hierarchy(hierarchy_id, proxy):
        :noindex:


    .. py:method:: get_hierarchy_sequencing_session(proxy):
        :noindex:


    .. py:method:: get_hierarchy_sequencing_session_for_hierarchy(hierarchy_id, proxy):
        :noindex:


    .. py:method:: get_hierarchy_structure_notification_session(hierarchy_structure_receiver, proxy):
        :noindex:


    .. py:method:: get_hierarchy_structure_notification_session_for_hierarchy(hierarchy_structure_receiver, hierarchy_id, proxy):
        :noindex:


    .. py:method:: get_hierarchy_lookup_session(proxy):
        :noindex:


    .. py:method:: get_hierarchy_query_session(proxy):
        :noindex:


    .. py:method:: get_hierarchy_search_session(proxy):
        :noindex:


    .. py:method:: get_hierarchy_admin_session(proxy):
        :noindex:


    .. py:method:: get_hierarchy_notification_session(hierarchy_receiver, proxy):
        :noindex:


