from ..osid import search_orders as osid_search_orders


class AgentSearchOrder(osid_search_orders.OsidObjectSearchOrder):
    """An interface for specifying the ordering of search results."""
    def order_by_resource(self, style):
        """Orders the results by resource.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_resource_search_order(self):
        """Tests if a ``ResourceSearchOrder`` is available.

        :return: ``true`` if a resource search order interface is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_resource_search_order(self):
        """Gets the resource search order.

        :return: the resource search odrer
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_resource_search_order()`` is ``false``

        """
        return # osid.resource.ResourceSearchOrder

    resource_search_order = property(fget=get_resource_search_order)

    def get_agent_search_order_record(self, agent_record_type):
        """Gets the agent search order record corresponding to the given agent record ``Type``.

        Multiple retrievals return the same underlying object.

        :param agent_record_type: an agent record type
        :type agent_record_type: ``osid.type.Type``
        :return: the agent search order record
        :rtype: ``osid.authentication.records.AgentSearchOrderRecord``
        :raise: ``NullArgument`` -- ``agent_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agent_record_type)`` is ``false``

        """
        return # osid.authentication.records.AgentSearchOrderRecord


class AgencySearchOrder(osid_search_orders.OsidCatalogSearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_agency_search_order_record(self, agency_record_type):
        """Gets the agency search order record corresponding to the given agency record ``Type``.

        Multiple retrievals return the same underlying object.

        :param agency_record_type: an agency record type
        :type agency_record_type: ``osid.type.Type``
        :return: the agency search order record
        :rtype: ``osid.authentication.records.AgencySearchOrderRecord``
        :raise: ``NullArgument`` -- ``agency_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agency_record_type)`` is ``false``

        """
        return # osid.authentication.records.AgencySearchOrderRecord


