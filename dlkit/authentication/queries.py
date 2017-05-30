
from ..osid import queries as osid_queries


class AgentQuery(osid_queries.OsidObjectQuery):
    """This is the query for searching agents.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    The following example returns agents whose display name begins with
    "Tom" and whose "login name" is "tom" or "tjcoppet" in an agent
    record specified by ``companyAgentType``.
      Agent Query query = session.getAgentQuery();

      query.matchDisplayName("Tom*", wildcardStringMatchType, true);

      companyAgentQuery = query.getAgentQueryRecord(companyAgentType);
      companyAgentQuery.matchLoginName("tom");
      companyAgentQuery = query.getAgentQueryRecord(companyAgentType);
      companyAgentQuery.matchLoginName("tjcoppet");

      AgentList agentList = session.getAgentsByQuery(query);

    """

    def match_resource_id(self, agency_id, match):
        """Sets the resource ``Id`` for this query.

        :param agency_id: a resource ``Id``
        :type agency_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_resource_id_terms(self):
        """Clears the resource ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    resource_id_terms = property(fdel=clear_resource_id_terms)

    def supports_resource_query(self):
        """Tests if a ``ResourceQuery`` is available.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_resource_query(self):
        """Gets the query for a resource.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_query()`` is ``true``.*

        """
        return # osid.resource.ResourceQuery

    resource_query = property(fget=get_resource_query)

    def match_any_resource(self, match):
        """Matches agents with any resource.

        :param match: ``true`` if to match agents with a resource, ``false`` to match agents with no resource
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_resource_terms(self):
        """Clears the resource terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    resource_terms = property(fdel=clear_resource_terms)

    def match_agency_id(self, agency_id, match):
        """Sets the agency ``Id`` for this query.

        :param agency_id: an agency ``Id``
        :type agency_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_agency_id_terms(self):
        """Clears the agency ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    agency_id_terms = property(fdel=clear_agency_id_terms)

    def supports_agency_query(self):
        """Tests if an ``AgencyQuery`` is available.

        :return: ``true`` if an agency query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_agency_query(self):
        """Gets the query for an agency.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the agency query
        :rtype: ``osid.authentication.AgencyQuery``
        :raise: ``Unimplemented`` -- ``supports_agency_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_agency_query()`` is ``true``.*

        """
        return # osid.authentication.AgencyQuery

    agency_query = property(fget=get_agency_query)

    def clear_agency_terms(self):
        """Clears the agency terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    agency_terms = property(fdel=clear_agency_terms)

    def get_agent_query_record(self, agent_record_type):
        """Gets the agent query record corresponding to the given ``Agent`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param agent_record_type: an agent record type
        :type agent_record_type: ``osid.type.Type``
        :return: the agent query record
        :rtype: ``osid.authentication.records.AgentQueryRecord``
        :raise: ``NullArgument`` -- ``agent_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agent_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.records.AgentQueryRecord


