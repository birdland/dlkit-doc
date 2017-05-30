
from ..osid import searches as osid_searches


class AgentSearch(osid_searches.OsidSearch):
    """``AgentSearch`` defines the interface for specifying agent search options.

    This example gets a limited set of squid-like agents. AgentSearch as
    = session.getAgentSearch(); as.limitResultSet(25, 50); AgentQuery
    queries[1]; queries[0] = session.getAgentQuery(); String kword =
    "squid"; queries[0].matchKeywords(kword, true); AgentSearchResults
    results = session.getAgentsBySearch(queries, as); AgentList list =
    results.getAgents();

    """

    def search_among_agents(self, agent_ids):
        """Execute this search among the given list of agents.

        :param agent_ids: list of agents
        :type agent_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``agent_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_agent_results(self, agent_search_order):
        """Specify an ordering to the search results.

        :param agent_search_order: agent search order
        :type agent_search_order: ``osid.authentication.AgentSearchOrder``
        :raise: ``NullArgument`` -- ``agent_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``agent_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_agent_search_record(self, agent_search_record_type):
        """Gets the record corresponding to the given agent search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param agent_search_record_type: an agent search record type
        :type agent_search_record_type: ``osid.type.Type``
        :return: the agent search record
        :rtype: ``osid.authentication.records.AgentSearchRecord``
        :raise: ``NullArgument`` -- ``agent_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agent_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.records.AgentSearchRecord


class AgentSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search.

    AgentSearch as = session.getAgentSearch(); as.limitResultSet(25,
    50); AgentQuery queries[1]; queries[0] = session.getAgentQuery();
    String kwords[1]; kwords[0] = "squid";
    queries[0].matchKeywords(kwords); AgentSearchResults results =
    session.getAgentsBySearch(queries, as); AgentList list =
    results.getAgents();

    """

    def get_agents(self):
        """Gets the agent list resulting from the search.

        :return: the agent list
        :rtype: ``osid.authentication.AgentList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.AgentList

    agents = property(fget=get_agents)

    def get_agent_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.authentication.AgentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.AgentQueryInspector

    agent_query_inspector = property(fget=get_agent_query_inspector)

    def get_agent_search_results_record(self, agent_search_record_type):
        """Gets the record corresponding to the given agent search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param agent_search_record_type: an agent search record type
        :type agent_search_record_type: ``osid.type.Type``
        :return: the agent search results record
        :rtype: ``osid.authentication.records.AgentSearchResultsRecord``
        :raise: ``NullArgument`` -- ``agent_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agent_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.records.AgentSearchResultsRecord


