from ..osid import receivers as osid_receivers


class AgentReceiver(osid_receivers.OsidReceiver):
    """The agent receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Agent`` objects.

    A change to a key is a change to an ``Agent``.

    """
    def new_agent(self, agent_id):
        """The callback for notifications of new agents.

        :param agent_id: the ``Id`` of the new ``Agent``
        :type agent_id: ``osid.id.Id``

        """
        pass

    def changed_agent(self, agent_id):
        """The callback for notification of updated agents.

        :param agent_id: the ``Id`` of the updated ``Agent``
        :type agent_id: ``osid.id.Id``

        """
        pass

    def deleted_agent(self, agent_id):
        """the callback for notification of deleted agents.

        :param agent_id: the ``Id`` of the deleted ``Agent``
        :type agent_id: ``osid.id.Id``

        """
        pass


class AgencyReceiver(osid_receivers.OsidReceiver):
    """The agency receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Agency`` objects."""
    def new_agency(self, agency_id):
        """The callback for notifications of new agencies.

        :param agency_id: the ``Id`` of the new ``Agency``
        :type agency_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_agency(self, agency_id, ancestor_id):
        """The callback for notifications of new agency ancestors.

        :param agency_id: the ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :param ancestor_id: ``has_record_type(agency_record_type)`` is ``false``
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_agency(self, agency_id, descendant_id):
        """The callback for notifications of new agency descendants.

        :param agency_id: the ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Agency`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_agency(self, agency_id):
        """The callback for notification of updated agencies.

        :param agency_id: the ``Id`` of the updated ``Agency``
        :type agency_id: ``osid.id.Id``

        """
        pass

    def deleted_agency(self, agency_id):
        """The callback for notification of deleted agencies.

        :param agency_id: the ``Id`` of the deleted ``Agency``
        :type agency_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_agency(self, agency_id, ancestor_id):
        """The callback for notifications of deleted agency ancestors.

        :param agency_id: the ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Agency`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_agency(self, agency_id, descendant_id):
        """The callback for notifications of deleted agency descendants.

        :param agency_id: the ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Agency`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass


