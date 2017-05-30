
from ..osid import searches as osid_searches


class AuthorizationSearch(osid_searches.OsidSearch):
    """``AuthorizationSearch`` defines the interface for specifying authorization search options."""

    def search_among_authorizations(self, authorization_ids):
        """Execute this search among the given list of authorizations.

        :param authorization_ids: list of authorizations
        :type authorization_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``authorization_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_authorization_results(self, authorization_search_order):
        """Specify an ordering to the search results.

        :param authorization_search_order: authorization search order
        :type authorization_search_order: ``osid.authorization.AuthorizationSearchOrder``
        :raise: ``NullArgument`` -- ``authorization_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``authorization_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_authorization_search_record(self, authorization_search_record_type):
        """Gets the authorization search record corresponding to the given authorization search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param authorization_search_record_type: an authorization search record type
        :type authorization_search_record_type: ``osid.type.Type``
        :return: the authorization search record
        :rtype: ``osid.authorization.records.AuthorizationSearchRecord``
        :raise: ``NullArgument`` -- ``authorization_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(authorization_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.records.AuthorizationSearchRecord


class AuthorizationSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""

    def get_authorizations(self):
        """Gets the authorization list resulting from the search.

        :return: the authorization list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``IllegalState`` -- list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    authorizations = property(fget=get_authorizations)

    def get_authorization_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.authorization.AuthorizationQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationQueryInspector

    authorization_query_inspector = property(fget=get_authorization_query_inspector)

    def get_authorization_search_results_record(self, authorization_search_record_type):
        """Gets the authorization search results record corresponding to the given authorization search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param authorization_search_record_type: an authorization search record type
        :type authorization_search_record_type: ``osid.type.Type``
        :return: the authorization search results record
        :rtype: ``osid.authorization.records.AuthorizationSearchResultsRecord``
        :raise: ``NullArgument`` -- ``authorization_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(authorization_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.records.AuthorizationSearchResultsRecord


class VaultSearch(osid_searches.OsidSearch):
    """The interface for governing vault searches."""

    def search_among_vaults(self, vault_ids):
        """Execute this search among the given list of vaults.

        :param vault_ids: list of vaults
        :type vault_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_vault_results(self, vault_search_order):
        """Specify an ordering to the search results.

        :param vault_search_order: vault search order
        :type vault_search_order: ``osid.authorization.VaultSearchOrder``
        :raise: ``NullArgument`` -- ``vault_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``vault_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_vault_search_record(self, vault_search_record_type):
        """Gets the vault search record corresponding to the given vault search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param vault_search_record_type: a vault search record type
        :type vault_search_record_type: ``osid.type.Type``
        :return: the vault search record
        :rtype: ``osid.authorization.records.VaultSearchRecord``
        :raise: ``NullArgument`` -- ``vault_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(vault_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.records.VaultSearchRecord


class VaultSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""

    def get_vaults(self):
        """Gets the vault list resulting from the search.

        :return: the vault list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``IllegalState`` -- list has already been retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    vaults = property(fget=get_vaults)

    def get_vault_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the vault query inspector
        :rtype: ``osid.authorization.VaultQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultQueryInspector

    vault_query_inspector = property(fget=get_vault_query_inspector)

    def get_vault_search_results_record(self, vault_search_record_type):
        """Gets the vault search results record corresponding to the given vault search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param vault_search_record_type: a vault search record type
        :type vault_search_record_type: ``osid.type.Type``
        :return: the vault search results record
        :rtype: ``osid.authorization.records.VaultSearchResultsRecord``
        :raise: ``NullArgument`` -- ``vault_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(vault_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.records.VaultSearchResultsRecord


