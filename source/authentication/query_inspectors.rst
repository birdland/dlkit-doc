.. currentmodule:: dlkit.authentication.query_inspectors
.. automodule:: dlkit.authentication.query_inspectors

Query Inspectors
================


Agent Query Inspector
---------------------

.. autoclass:: AgentQueryInspector
   :show-inheritance:

   .. autoattribute:: AgentQueryInspector.resource_id_terms

   .. autoattribute:: AgentQueryInspector.resource_terms

   .. autoattribute:: AgentQueryInspector.agency_id_terms

   .. autoattribute:: AgentQueryInspector.agency_terms

   .. automethod:: AgentQueryInspector.get_agent_query_inspector_record



Agency Query Inspector
----------------------

.. autoclass:: AgencyQueryInspector
   :show-inheritance:

   .. autoattribute:: AgencyQueryInspector.agent_id_terms

   .. autoattribute:: AgencyQueryInspector.agent_terms

   .. autoattribute:: AgencyQueryInspector.ancestor_agency_id_terms

   .. autoattribute:: AgencyQueryInspector.ancestor_agency_terms

   .. autoattribute:: AgencyQueryInspector.descendant_agency_id_terms

   .. autoattribute:: AgencyQueryInspector.descendant_agency_terms

   .. automethod:: AgencyQueryInspector.get_agency_query_inspector_record



