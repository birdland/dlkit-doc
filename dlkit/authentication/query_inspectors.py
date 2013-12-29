from ..osid import query_inspectors as osid_query_inspectors


class AgentQueryInspector(osid_query_inspectors.OsidObjectQueryInspector):
    """This is the query inspector for examining agent queries."""
    def get_resource_id_terms(self):
        """Gets the resource ``Id`` terms.

        :return: the resource ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    resource_id_terms = property(fget=get_resource_id_terms)

    def get_resource_terms(self):
        """Gets the resource terms.

        :return: the resource terms
        :rtype: ``osid.resource.ResourceQueryInspector``

        """
        return # osid.resource.ResourceQueryInspector

    resource_terms = property(fget=get_resource_terms)

    def get_agency_id_terms(self):
        """Gets the agency ``Id`` terms.

        :return: the agency ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    agency_id_terms = property(fget=get_agency_id_terms)

    def get_agency_terms(self):
        """Gets the agency terms.

        :return: the agency terms
        :rtype: ``osid.authentication.AgencyQueryInspector``

        """
        return # osid.authentication.AgencyQueryInspector

    agency_terms = property(fget=get_agency_terms)

    def get_agent_query_inspector_record(self, agent_record_type):
        """Gets the query inspector record corresponding to the given ``Agent`` record ``Type``.

        :param agent_record_type: an agent record type
        :type agent_record_type: ``osid.type.Type``
        :return: the agent query inspector record
        :rtype: ``osid.authentication.records.AgentQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``agent_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agent_record_type)`` is ``false``

        """
        return # osid.authentication.records.AgentQueryInspectorRecord


class AgencyQueryInspector(osid_query_inspectors.OsidCatalogQueryInspector):
    """This is the query inspector for examining queries."""
    def get_agent_id_terms(self):
        """Gets the agent ``Id`` terms.

        :return: the agent ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    agent_id_terms = property(fget=get_agent_id_terms)

    def get_agent_terms(self):
        """Gets the agent terms.

        :return: the query terms
        :rtype: ``osid.authentication.AgentQueryInspector``

        """
        return # osid.authentication.AgentQueryInspector

    agent_terms = property(fget=get_agent_terms)

    def get_ancestor_agency_id_terms(self):
        """Gets the ancestor agency ``Id`` terms.

        :return: the ancestor agency ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    ancestor_agency_id_terms = property(fget=get_ancestor_agency_id_terms)

    def get_ancestor_agency_terms(self):
        """Gets the ancestor agency terms.

        :return: the ancestor agency terms
        :rtype: ``osid.authentication.AgencyQueryInspector``

        """
        return # osid.authentication.AgencyQueryInspector

    ancestor_agency_terms = property(fget=get_ancestor_agency_terms)

    def get_descendant_agency_id_terms(self):
        """Gets the descendant agency ``Id`` terms.

        :return: the descendant agency ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    descendant_agency_id_terms = property(fget=get_descendant_agency_id_terms)

    def get_descendant_agency_terms(self):
        """Gets the descendant agency terms.

        :return: the descendant agency terms
        :rtype: ``osid.authentication.AgencyQueryInspector``

        """
        return # osid.authentication.AgencyQueryInspector

    descendant_agency_terms = property(fget=get_descendant_agency_terms)

    def get_agency_query_inspector_record(self, agency_record_type):
        """Gets the agency query inspector record corresponding to the given ``Agency`` record ``Type``.

        :param agency_record_type: an agency record type
        :type agency_record_type: ``osid.type.Type``
        :return: the agency query inspector record
        :rtype: ``osid.authentication.records.AgencyQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``agency_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agency_record_type)`` is ``false``

        """
        return # osid.authentication.records.AgencyQueryInspectorRecord


