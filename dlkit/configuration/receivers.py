from ..osid import receivers as osid_receivers


class ParameterReceiver(osid_receivers.OsidReceiver):
    """The parameter receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Parameter`` objects."""
    def new_parameters(self, notification_id, parameter_ids):
        """The callback for notifications of new parameters.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param parameter_ids: the ``Ids`` of the new ``Parameters``
        :type parameter_ids: ``osid.id.IdList``

        """
        pass

    def changed_parameters(self, notification_id, parameter_ids):
        """The callback for notification of updated parameters.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param parameter_ids: the ``Ids`` of the updated ``Parameters``
        :type parameter_ids: ``osid.id.IdList``

        """
        pass

    def deleted_parameters(self, notification_id, parameter_ids):
        """the callback for notification of deleted parameters.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param parameter_ids: the ``Ids`` of the deleted ``Parameters``
        :type parameter_ids: ``osid.id.IdList``

        """
        pass


class ValueReceiver(osid_receivers.OsidReceiver):
    """The value receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Values``."""
    def new_values(self, notification_id, value_ids):
        """The callback for notification of new values.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param value_ids: the ``Ids`` of the ``Values``
        :type value_ids: ``osid.id.IdList``

        """
        pass

    def changed_values(self, notification_id, value_ids):
        """The callback for notification of changed values.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param value_ids: the ``Ids`` of the ``Values``
        :type value_ids: ``osid.id.IdList``

        """
        pass

    def deleted_values(self, notification_id, value_ids):
        """The callback for notification of removed values.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param value_ids: the ``Ids`` of the ``Values``
        :type value_ids: ``osid.id.IdList``

        """
        pass


class ConfigurationReceiver(osid_receivers.OsidReceiver):
    """The configuration receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Configuration`` objects."""
    def new_configurations(self, notification_id, configuration_ids):
        """The callback for notifications of new configurations.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param configuration_ids: the ``Ids`` of the new ``Configurations``
        :type configuration_ids: ``osid.id.IdList``

        """
        pass

    def changed_configurations(self, notification_id, configuration_ids):
        """The callback for notification of updated configurations.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param configuration_ids: the ``Ids`` of the updated ``Configurations``
        :type configuration_ids: ``osid.id.IdList``

        """
        pass

    def deleted_configurations(self, notification_id, configuration_ids):
        """The callback for notification of deleted configurations.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param configuration_ids: the ``Ids`` of the deleted ``Configurations``
        :type configuration_ids: ``osid.id.IdList``

        """
        pass

    def changed_child_of_confgurations(self, notification_id, configuration_ids):
        """The callback for notifications of changes to children of configuration hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param configuration_ids: the ``Ids`` of the ``Configurations`` whose children have changed
        :type configuration_ids: ``osid.id.IdList``

        """
        pass


