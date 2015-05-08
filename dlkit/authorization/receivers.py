from ..osid import receivers as osid_receivers


class AuthorizationReceiver(osid_receivers.OsidReceiver):
    """The authorization receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Authorizations``."""
    def new_authorizations(self, notification_id, authorization_ids):
        """The callback for notifications of new authorizations.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param authorization_ids: the Id of the new ``Authorizations``
        :type authorization_ids: ``osid.id.IdList``

        """
        pass

    def changed_authorizations(self, notification_id, authorization_ids):
        """The callback for notification of updated authorization.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param authorization_ids: the Id of the updated ``Authorizations``
        :type authorization_ids: ``osid.id.IdList``

        """
        pass

    def deleted_authorizations(self, notification_id, authorization_ids):
        """The callback for notification of deleted authorizations.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param authorization_ids: the Id of the deleted ``Authorizations``
        :type authorization_ids: ``osid.id.IdList``

        """
        pass


class FunctionReceiver(osid_receivers.OsidReceiver):
    """The function receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Functions``."""
    def new_functions(self, notification_id, function_ids):
        """The callback for notifications of new functions.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param function_ids: the Id of the new ``Functions``
        :type function_ids: ``osid.id.IdList``

        """
        pass

    def changed_functions(self, notification_id, function_ids):
        """The callback for notification of updated functions.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param function_ids: the Id of the updated ``Functions``
        :type function_ids: ``osid.id.IdList``

        """
        pass

    def deleted_functions(self, notification_id, function_ids):
        """The callback for notification of deleted functions.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param function_ids: the Id of the deleted ``Functions``
        :type function_ids: ``osid.id.IdList``

        """
        pass


class QualifierReceiver(osid_receivers.OsidReceiver):
    """The qualifier receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Qualifier`` objects."""
    def new_qualifiers(self, notification_id, qualifier_ids):
        """The callback for notifications of new qualifiers.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param qualifier_ids: the ``Id`` of the new ``Qualifiers``
        :type qualifier_ids: ``osid.id.IdList``

        """
        pass

    def changed_qualifiers(self, notification_id, qualifier_ids):
        """The callback for notification of updated qualifiers.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param qualifier_ids: the ``Id`` of the updated ``Qualifiers``
        :type qualifier_ids: ``osid.id.IdList``

        """
        pass

    def deleted_qualifiers(self, notification_id, qualifier_ids):
        """the callback for notification of deleted qualifiers.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param qualifier_ids: the ``Id`` of the deleted ``Qualifiers``
        :type qualifier_ids: ``osid.id.IdList``

        """
        pass

    def changed_child_of_billings(self, notification_id, qualifier_ids):
        """The callback for notifications of changes to children of qualifier hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param qualifier_ids: the ``Ids`` of the ``Qualifiers`` whose children have changed
        :type qualifier_ids: ``osid.id.IdList``

        """
        pass


class VaultReceiver(osid_receivers.OsidReceiver):
    """The vault receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Vault`` objects."""
    def new_vaults(self, notification_id, vault_ids):
        """The callback for notifications of new vaults.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param vault_ids: the ``Id`` of the new ``Vaults``
        :type vault_ids: ``osid.id.IdList``

        """
        pass

    def changed_vaults(self, notification_id, vault_ids):
        """The callback for notification of updated vaults.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param vault_ids: the ``Id`` of the updated ``Vaults``
        :type vault_ids: ``osid.id.IdList``

        """
        pass

    def deleted_vaults(self, notification_id, vault_ids):
        """The callback for notification of deleted vaults.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param vault_ids: the ``Id`` of the deleted ``Vaults``
        :type vault_ids: ``osid.id.IdList``

        """
        pass

    def changed_child_of_vaults(self, notification_id, vault_ids):
        """The callback for notifications of changes to children of vault hierarchy nodes.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param vault_ids: the ``Ids`` of the ``Vaults`` whose children have changed
        :type vault_ids: ``osid.id.IdList``

        """
        pass


