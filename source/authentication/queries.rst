.. currentmodule:: dlkit.abstract_osid.authentication.queries
.. automodule:: dlkit.abstract_osid.authentication.queries

Queries
=======


Agent Query
-----------

.. autoclass:: AgentQuery
   :show-inheritance:

.. automethod:: AgentQuery.match_resource_id

.. autoattribute:: AgentQuery.resource_id_terms

.. automethod:: AgentQuery.supports_resource_query

.. autoattribute:: AgentQuery.resource_query

.. automethod:: AgentQuery.match_any_resource

.. autoattribute:: AgentQuery.resource_terms

.. automethod:: AgentQuery.match_agency_id

.. autoattribute:: AgentQuery.agency_id_terms

.. automethod:: AgentQuery.supports_agency_query

.. autoattribute:: AgentQuery.agency_query

.. autoattribute:: AgentQuery.agency_terms

.. automethod:: AgentQuery.get_agent_query_record



Agency Query
------------

.. autoclass:: AgencyQuery
   :show-inheritance:

.. automethod:: AgencyQuery.match_agent_id

.. autoattribute:: AgencyQuery.agent_id_terms

.. automethod:: AgencyQuery.supports_agent_query

.. autoattribute:: AgencyQuery.agent_query

.. automethod:: AgencyQuery.match_any_agent

.. autoattribute:: AgencyQuery.agent_terms

.. automethod:: AgencyQuery.match_ancestor_agency_id

.. autoattribute:: AgencyQuery.ancestor_agency_id_terms

.. automethod:: AgencyQuery.supports_ancestor_agency_query

.. autoattribute:: AgencyQuery.ancestor_agency_query

.. automethod:: AgencyQuery.match_any_ancestor_agency

.. autoattribute:: AgencyQuery.ancestor_agency_terms

.. automethod:: AgencyQuery.match_descendant_agency_id

.. autoattribute:: AgencyQuery.descendant_agency_id_terms

.. automethod:: AgencyQuery.supports_descendant_agency_query

.. autoattribute:: AgencyQuery.descendant_agency_query

.. automethod:: AgencyQuery.match_any_descendant_agency

.. autoattribute:: AgencyQuery.descendant_agency_terms

.. automethod:: AgencyQuery.get_agency_query_record



