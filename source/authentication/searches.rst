.. currentmodule:: dlkit.abstract_osid.authentication.searches
.. automodule:: dlkit.abstract_osid.authentication.searches

Searches
========


Agent Search
------------

.. autoclass:: AgentSearch
   :show-inheritance:

.. automethod:: AgentSearch.search_among_agents

.. automethod:: AgentSearch.order_agent_results

.. automethod:: AgentSearch.get_agent_search_record



Agent Search Results
--------------------

.. autoclass:: AgentSearchResults
   :show-inheritance:

.. autoattribute:: AgentSearchResults.agents

.. autoattribute:: AgentSearchResults.agent_query_inspector

.. automethod:: AgentSearchResults.get_agent_search_results_record



Agency Search
-------------

.. autoclass:: AgencySearch
   :show-inheritance:

.. automethod:: AgencySearch.search_among_agencies

.. automethod:: AgencySearch.order_agency_results

.. automethod:: AgencySearch.get_agency_search_record



Agency Search Results
---------------------

.. autoclass:: AgencySearchResults
   :show-inheritance:

.. autoattribute:: AgencySearchResults.agencies

.. autoattribute:: AgencySearchResults.agency_query_inspector

.. automethod:: AgencySearchResults.get_agency_search_results_record



