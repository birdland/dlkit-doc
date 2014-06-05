from ..osid import receivers as osid_receivers


class RuleReceiver(osid_receivers.OsidReceiver):
    """The rule receiver is the consumer supplied interface for receiving notifications pertaining to new or deleted rules."""
    def new_rule(self, rule_id):
        """The callback for notifications of new rules.

        :param rule_id: the ``Id`` of the new rule
        :type rule_id: ``osid.id.Id``

        """
        pass

    def changed_rule(self, rule_id):
        """the callback for notification of changed rules.

        :param rule_id: the ``Id`` of the changed rule
        :type rule_id: ``osid.id.Id``

        """
        pass

    def deleted_rule(self, rule_id):
        """the callback for notification of deleted rules.

        :param rule_id: the ``Id`` of the deleted rule
        :type rule_id: ``osid.id.Id``

        """
        pass


class EngineReceiver(osid_receivers.OsidReceiver):
    """The engine receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Engine`` objects."""
    def new_engine(self, engine_id):
        """The callback for notifications of new engines.

        :param engine_id: the ``Id`` of the new ``Engine``
        :type engine_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_engine(self, engine_id, ancestor_id):
        """The callback for notifications of new ancestors of an engine.

        :param engine_id: the ``Id`` of the registered ``Engine``
        :type engine_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ancestor engine
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_engine(self, engine_id, descendant_id):
        """The callback for notifications of new descendant of an engine.

        :param engine_id: the ``Id`` of the registered ``Engine``
        :type engine_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new descendant engine
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_engine(self, engine_id):
        """The callback for notification of updated engines.

        :param engine_id: the ``Id`` of the updated ``Engine``
        :type engine_id: ``osid.id.Id``

        """
        pass

    def deleted_engine(self, engine_id):
        """the callback for notification of deleted engines.

        :param engine_id: the ``Id`` of the registered ``Engine``
        :type engine_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_engine(self, engine_id, ancestor_id):
        """The callback for notifications of deleted ancestors of an engine.

        :param engine_id: the ``Id`` of the registered ``Engine``
        :type engine_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ancestor engine
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_engine(self, engine_id, descendant_id):
        """The callback for notifications of deleted descendants of an engine.

        :param engine_id: the ``Id`` of the registered ``Engine``
        :type engine_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the deleted descendant engine
        :type descendant_id: ``osid.id.Id``

        """
        pass


