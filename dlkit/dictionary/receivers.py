from ..osid import receivers as osid_receivers


class EntryReceiver(osid_receivers.OsidReceiver):
    """The dictionary entry receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Entry`` objects."""
    def new_entry(self, entry_id):
        """The callback for notifications of new dictionary entries.

        :param entry_id: the ``Id`` of the ``Entry``
        :type entry_id: ``osid.id.Id``

        """
        pass

    def changed_entry(self, entry_id):
        """The callback for notification of updated dictionary entries.

        :param entry_id: the ``Id`` of the ``Entry``
        :type entry_id: ``osid.id.Id``

        """
        pass

    def deleted_entry(self, entry_id):
        """the callback for notification of deleted dictionary entries.

        :param entry_id: the ``Id`` of the ``Entry``
        :type entry_id: ``osid.id.Id``

        """
        pass


class DictionaryReceiver(osid_receivers.OsidReceiver):
    """The dictionary receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Dictionary`` objects."""
    def new_dictionary(self, dictionary_id):
        """The callback for notifications of new dictionaries.

        :param dictionary_id: the ``Id`` of the new ``Dictionary``
        :type dictionary_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_endpoint(self, dictionary_id, ancestor_id):
        """The callback for notifications of new ancestors of a dictionary.

        :param dictionary_id: the ``Id`` of the registered ``Dictionary``
        :type dictionary_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ancestor dictionary
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_dictionary(self, dictionary_id, descendant_id):
        """The callback for notifications of new descendant of a dictionary.

        :param dictionary_id: the ``Id`` of the registered ``Dictionary``
        :type dictionary_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new descendant dictionary
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_dictionary(self, dictionary_id):
        """The callback for notification of updated dictionaries.

        :param dictionary_id: the ``Id`` of the updated ``Dictionary``
        :type dictionary_id: ``osid.id.Id``

        """
        pass

    def deleted_dictionary(self, dictionary_id):
        """the callback for notification of deleted dictionaries.

        :param dictionary_id: the ``Id`` of the deleted ``Dictionary``
        :type dictionary_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_dictionary(self, dictionary_id, ancestor_id):
        """The callback for notifications of deleted ancestors of a dictionary.

        :param dictionary_id: the ``Id`` of the registered ``Dictionary``
        :type dictionary_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ancestor dictionary
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_dictionary(self, dictionary_id, descendant_id):
        """The callback for notifications of deleted descendanta of a dictionary.

        :param dictionary_id: the ``Id`` of the registered ``Dictionary``
        :type dictionary_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the deleted descendant dictionary
        :type descendant_id: ``osid.id.Id``

        """
        pass


