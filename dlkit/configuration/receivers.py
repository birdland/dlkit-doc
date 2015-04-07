from ..osid import receivers as osid_receivers


class ParameterReceiver(osid_receivers.OsidReceiver):
    """The parameter receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Parameter`` objects."""
    def new_parameter(self, parameter_id):
        """The callback for notifications of new parameters.

        :param parameter_id: the ``Id`` of the new ``Parameter``
        :type parameter_id: ``osid.id.Id``

        """
        pass

    def changed_parameter(self, parameter_id):
        """The callback for notification of updated parameters.

        :param parameter_id: the ``Id`` of the updated ``Parameter``
        :type parameter_id: ``osid.id.Id``

        """
        pass

    def deleted_parameter(self, parameter_id):
        """the callback for notification of deleted parameters.

        :param parameter_id: the ``Id`` of the deleted ``Parameter``
        :type parameter_id: ``osid.id.Id``

        """
        pass


class ValueReceiver(osid_receivers.OsidReceiver):
    """The value receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Values``."""
    def new_value(self, value_id):
        """The callback for notification of new values.

        :param value_id: the ``Id`` of the ``Value``
        :type value_id: ``osid.id.Id``

        """
        pass

    def changed_value(self, value_id):
        """The callback for notification of changed values.

        :param value_id: the ``Id`` of the ``Value``
        :type value_id: ``osid.id.Id``

        """
        pass

    def deleted_value(self, value_id):
        """The callback for notification of removed values.

        :param value_id: the ``Id`` of the ``Value``
        :type value_id: ``osid.id.Id``

        """
        pass


class ConfigurationReceiver(osid_receivers.OsidReceiver):
    """The configuration receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Configuration`` objects."""
    def new_configuration(self, configuration_id):
        """The callback for notifications of new configurations.

        :param configuration_id: the ``Id`` of the new ``Configuration``
        :type configuration_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_configuration(self, configuration_id, ancestor_id):
        """The callback for notifications of new configuration ancestors.

        :param configuration_id: the ``Id`` of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ``Configuration`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_configuration(self, configuration_id, descendant_id):
        """The callback for notifications of new configuration descendants.

        :param configuration_id: the ``Id`` of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Configuration`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_configuration(self, configuration_id):
        """The callback for notification of updated configurations.

        :param configuration_id: the ``Id`` of the updated ``Configuration``
        :type configuration_id: ``osid.id.Id``

        """
        pass

    def deleted_configuration(self, configuration_id):
        """The callback for notification of deleted configurations.

        :param configuration_id: the ``Id`` of the deleted ``Configuration``
        :type configuration_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_configuration(self, configuration_id, ancestor_id):
        """The callback for notifications of deleted configuration ancestors.

        :param configuration_id: the ``Id`` of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Configuration`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_configuration(self, configuration_id, descendant_id):
        """The callback for notifications of deleted configuration descendants.

        :param configuration_id: the ``Id`` of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Configuration`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass


