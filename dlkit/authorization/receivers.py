from ..osid import receivers as osid_receivers


class AuthorizationReceiver(osid_receivers.OsidReceiver):
    """The authorization receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Authorizations``."""
    def new_authorization(self, authorization_id):
        """The callback for notifications of new authorizations.

        :param authorization_id: the Id of the new ``Authorization``
        :type authorization_id: ``osid.id.Id``

        """
        pass

    def changed_authorization(self, authorization_id):
        """The callback for notification of updated authorization.

        :param authorization_id: the Id of the updated ``Authorization``
        :type authorization_id: ``osid.id.Id``

        """
        pass

    def deleted_authorization(self, authorization_id):
        """The callback for notification of deleted authorizations.

        :param authorization_id: the Id of the deleted ``Authorization``
        :type authorization_id: ``osid.id.Id``

        """
        pass


class FunctionReceiver(osid_receivers.OsidReceiver):
    """The function receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Functions``."""
    def new_function(self, function_id):
        """The callback for notifications of new functions.

        :param function_id: the Id of the new ``Function``
        :type function_id: ``osid.id.Id``

        """
        pass

    def changed_function(self, function_id):
        """The callback for notification of updated functions.

        :param function_id: the Id of the updated ``Function``
        :type function_id: ``osid.id.Id``

        """
        pass

    def deleted_function(self, function_id):
        """The callback for notification of deleted functions.

        :param function_id: the Id of the deleted ``Function``
        :type function_id: ``osid.id.Id``

        """
        pass


class QualifierReceiver(osid_receivers.OsidReceiver):
    """The qualifier receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Qualifier`` objects."""
    def new_qualifier(self, qualifier_id):
        """The callback for notifications of new qualifiers.

        :param qualifier_id: the ``Id`` of the new ``Qualifier``
        :type qualifier_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_qualifier(self, qualifier_id, ancestor_id):
        """The callback for notifications of new qualifier ancestors.

        :param qualifier_id: the ``Id`` of the ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ``Qualifier`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_qualifier(self, qualifier_id, descendant_id):
        """The callback for notifications of new qualifier descendants.

        :param qualifier_id: the ``Id`` of the ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Qualifier`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_qualifier(self, qualifier_id):
        """The callback for notification of updated qualifiers.

        :param qualifier_id: the ``Id`` of the updated ``Qualifier``
        :type qualifier_id: ``osid.id.Id``

        """
        pass

    def deleted_qualifier(self, qualifier_id):
        """the callback for notification of deleted qualifiers.

        :param qualifier_id: the ``Id`` of the deleted ``Qualifier``
        :type qualifier_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_qualifier(self, qualifier_id, ancestor_id):
        """The callback for notifications of deleted qualifier ancestors.

        :param qualifier_id: the ``Id`` of the ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Qualifier`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_qualifier(self, qualifier_id, descendant_id):
        """The callback for notifications of deleted qualifier descendants.

        :param qualifier_id: the ``Id`` of the ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Qualifier`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass


class VaultReceiver(osid_receivers.OsidReceiver):
    """The vault receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Vault`` objects."""
    def new_vault(self, vault_id):
        """The callback for notifications of new vaults.

        :param vault_id: the ``Id`` of the new ``Vault``
        :type vault_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_vault(self, vault_id, ancestor_id):
        """The callback for notifications of new vault ancestors.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :param ancestor_id: ``has_record_type(vault_record_type) is false``
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_vault(self, vault_id, descendant_id):
        """The callback for notifications of new vault descendants.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Vault`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_vault(self, vault_id):
        """The callback for notification of updated vaults.

        :param vault_id: the ``Id`` of the updated ``Vault``
        :type vault_id: ``osid.id.Id``

        """
        pass

    def deleted_vault(self, vault_id):
        """The callback for notification of deleted vaults.

        :param vault_id: the ``Id`` of the deleted ``Vault``
        :type vault_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_vault(self, vault_id, ancestor_id):
        """The callback for notifications of deleted vault ancestors.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Vault`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_vault(self, vault_id, descendant_id):
        """The callback for notifications of deleted vault descendants.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Vault`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass


