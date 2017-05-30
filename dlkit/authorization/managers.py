
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class AuthorizationProfile(osid_managers.OsidProfile):
    """The ``AuthorizationProfile`` describes the interoperability among authorization services."""

    def supports_authorization(self):
        """Tests for the availability of an authorization service which is the basic service for checking authorizations.

        :return: ``true`` if authorization is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_authorization_lookup(self):
        """Tests if an authorization lookup service is supported.

        An authorization lookup service defines methods to access
        authorizations.

        :return: true if authorization lookup is supported, false otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_authorization_query(self):
        """Tests if an authorization query service is supported.

        :return: ``true`` if authorization query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_authorization_admin(self):
        """Tests if an authorization administrative service is supported.

        :return: ``true`` if authorization admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_vault_lookup(self):
        """Tests if a vault lookup service is supported.

        A vault lookup service defines methods to access authorization
        vaults.

        :return: ``true`` if function lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_vault_query(self):
        """Tests if a vault query service is supported.

        :return: ``true`` if vault query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_vault_admin(self):
        """Tests if a vault administrative service is supported.

        :return: ``true`` if vault admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_authorization_record_types(self):
        """Gets the supported ``Authorization`` record types.

        :return: a list containing the supported authorization record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    authorization_record_types = property(fget=get_authorization_record_types)

    def get_authorization_search_record_types(self):
        """Gets the supported ``Authorization`` search record types.

        :return: a list containing the supported authorization search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    authorization_search_record_types = property(fget=get_authorization_search_record_types)

    def get_function_record_types(self):
        """Gets the supported ``Function`` record types.

        :return: a list containing the supported ``Function`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    function_record_types = property(fget=get_function_record_types)

    def get_function_search_record_types(self):
        """Gets the supported ``Function`` search record types.

        :return: a list containing the supported ``Function`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    function_search_record_types = property(fget=get_function_search_record_types)

    def get_qualifier_record_types(self):
        """Gets the supported ``Qualifier`` record types.

        :return: a list containing the supported ``Qualifier`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    qualifier_record_types = property(fget=get_qualifier_record_types)

    def get_qualifier_search_record_types(self):
        """Gets the supported ``Qualifier`` search record types.

        :return: a list containing the supported ``Qualifier`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    qualifier_search_record_types = property(fget=get_qualifier_search_record_types)

    def get_vault_record_types(self):
        """Gets the supported ``Vault`` record types.

        :return: a list containing the supported ``Vault`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    vault_record_types = property(fget=get_vault_record_types)

    def get_vault_search_record_types(self):
        """Gets the supported vault search record types.

        :return: a list containing the supported ``Vault`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    vault_search_record_types = property(fget=get_vault_search_record_types)

    def get_authorization_condition_record_types(self):
        """Gets the supported ``AuthorizationCondition`` record types.

        :return: a list containing the supported ``AuthorizationCondition`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    authorization_condition_record_types = property(fget=get_authorization_condition_record_types)


class AuthorizationManager(osid_managers.OsidManager, osid_sessions.OsidSession, AuthorizationProfile):
    """The authorization manager provides access to authorization sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``AuthorizationSession:`` a session to performs authorization
        checks
      * ``AuthorizationLookupSession:`` a session to look up
        ``Authorizations``
      * ``AuthorizationQuerySession:`` a session to query
        ``Authorizations``
      * ``AuthorizationSearchSession:`` a session to search
        ``Authorizations``
      * ``AuthorizationAdminSession:`` a session to create, modify and
        delete ``Authorizations``
      * ``AuthorizationNotificationSession: a`` session to receive
        messages pertaining to ``Authorization`` changes
      * ``AuthorizationVaultSession:`` a session to look up
        authorization to vault mappings
      * ``AuthorizationVaultAssignmentSession:`` a session to manage
        authorization to vault mappings
      * ``AuthorizationSmartVaultSession:`` a session to manage smart
        authorization vaults

      * ``FunctionLookupSession:`` a session to look up ``Functions``
      * ``FunctionQuerySession:`` a session to query ``Functions``
      * ``FunctionSearchSession:`` a session to search ``Functions``
      * ``FunctionAdminSession:`` a session to create, modify and delete
        ``Functions``
      * ``FunctionNotificationSession: a`` session to receive messages
        pertaining to ``Function`` changes
      * ``FunctionVaultSession:`` a session for looking up function and
        vault mappings
      * ``FunctionVaultAssignmentSession:`` a session for managing
        function and vault mappings
      * ``FunctionSmartVaultSession:`` a session to manage dynamic
        function vaults

      * ``QualifierLookupSession:`` a session to look up ``Qualifiers``
      * ``QualifierQuerySession:`` a session to query ``Qualifiers``
      * ``QualifierSearchSession:`` a session to search ``Qualifiers``
      * ``QualifierAdminSession:`` a session to create, modify and
        delete ``Qualifiers``
      * ``QualifierNotificationSession: a`` session to receive messages
        pertaining to ``Qualifier`` changes
      * ``QualifierHierarchySession:`` a session for traversing
        qualifier hierarchies
      * ``QualifierHierarchyDesignSession:`` a session for managing
        qualifier hierarchies
      * ``QualifierVaultSession:`` a session for looking up qualifier
        and vault mappings
      * ``QualifierVaultAssignmentSession:`` a session for managing
        qualifier and vault mappings
      * ``QualifierSmartVaultSession:`` a session to manage dynamic
        qualifier vaults

      * ``VaultLookupSession:`` a session to lookup vaults
      * ``VaultQuerySession:`` a session to query Vaults
      * ``VaultSearchSession`` : a session to search vaults
      * ``VaultAdminSession`` : a session to create, modify and delete
        vaults
      * ``VaultNotificationSession`` : a session to receive messages
        pertaining to ``Vault`` changes
      * ``VaultHierarchySession`` : a session to traverse the ``Vault``
        hierarchy
      * ``VaultHierarchyDesignSession`` : a session to manage the
        ``Vault`` hierarchy

    """

    def get_authorization_batch_manager(self):
        """Gets an ``AuthorizationBatchManager``.

        :return: an ``AuthorizationBatchManager``
        :rtype: ``osid.authorization.batch.AuthorizationBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_batch() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_batch()`` is true.*

        """
        return # osid.authorization.batch.AuthorizationBatchManager

    authorization_batch_manager = property(fget=get_authorization_batch_manager)

    def get_authorization_rules_manager(self):
        """Gets an ``AuthorizationRulesManager``.

        :return: an ``AuthorizationRulesManager``
        :rtype: ``osid.authorization.rules.AuthorizationRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_rules() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_rules()`` is true.*

        """
        return # osid.authorization.rules.AuthorizationRulesManager

    authorization_rules_manager = property(fget=get_authorization_rules_manager)


class AuthorizationProxyManager(osid_managers.OsidProxyManager, AuthorizationProfile):
    """The authorization manager provides access to authorization sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` object.
    The sessions included in this manager are:

      * ``AuthorizationSession:`` a session to performs authorization
        checks
      * ``AuthorizationLookupSession:`` a session to look up
        ``Authorizations``
      * ``AuthorizationSearchSession:`` a session to search
        ``Authorizations``
      * ``AuthorizationAdminSession:`` a session to create, modify and
        delete ``Authorizations``
      * ``AuthorizationNotificationSession: a`` session to receive
        messages pertaining to ``Authorization`` changes
      * ``AuthorizationVaultSession:`` a session to look up
        authorization to vault mappings
      * ``AuthorizationVaultAssignmentSession:`` a session to manage
        authorization to vault mappings
      * ``AuthorizationSmartVaultSession:`` a session to manage smart
        authorization vault

      * ``FunctionLookupSession:`` a session to look up ``Functions``
      * ``FunctionQuerySession:`` a session to query ``Functions``
      * ``FunctionSearchSession:`` a session to search ``Functions``
      * ``FunctionAdminSession:`` a session to create, modify and delete
        ``Functions``
      * ``FunctionNotificationSession: a`` session to receive messages
        pertaining to ``Function`` changes
      * ``FunctionVaultSession:`` a session for looking up function and
        vault mappings
      * ``FunctionVaultAssignmentSession:`` a session for managing
        function and vault mappings
      * ``FunctionSmartVaultSession:`` a session to manage dynamic
        function vaults

      * ``QualifierLookupSession:`` a session to look up ``Qualifiers``
      * ``QualifierQuerySession:`` a session to query ``Qualifiers``
      * ``QualifierSearchSession:`` a session to search ``Qualifiers``
      * ``QualifierAdminSession:`` a session to create, modify and
        delete ``Qualifiers``
      * ``QualifierNotificationSession: a`` session to receive messages
        pertaining to ``Qualifier`` changes
      * ``QualifierHierarchySession:`` a session for traversing
        qualifier hierarchies
      * ``QualifierHierarchyDesignSession:`` a session for managing
        qualifier hierarchies
      * ``QualifierVaultSession:`` a session for looking up qualifier
        and vault mappings
      * ``QualifierVaultAssignmentSession:`` a session for managing
        qualifier and vault mappings
      * ``QualifierSmartVaultSession:`` a session to manage dynamic
        qualifier vaults

      * ``VaultLookupSession:`` a session to lookup vaults
      * ``VaultQuerySession:`` a session to query Vaults
      * ``VaultSearchSession`` : a session to search vaults
      * ``VaultAdminSession`` : a session to create, modify and delete
        vaults
      * ``VaultNotificationSession`` : a session to receive messages
        pertaining to ``Vault`` changes
      * ``VaultHierarchySession`` : a session to traverse the ``Vault``
        hierarchy
      * ``VaultHierarchyDesignSession`` : a session to manage the
        ``Vault`` hierarchy

    """

    def get_authorization_batch_proxy_manager(self):
        """Gets an ``AuthorizationBatchProxyManager``.

        :return: an ``AuthorizationBatchProxyManager``
        :rtype: ``osid.authorization.batch.AuthorizationBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_batch() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_batch()`` is true.*

        """
        return # osid.authorization.batch.AuthorizationBatchProxyManager

    authorization_batch_proxy_manager = property(fget=get_authorization_batch_proxy_manager)

    def get_authorization_rules_proxy_manager(self):
        """Gets an ``AuthorizationRulesProxyManager``.

        :return: an ``AuthorizationRulesProxyManager``
        :rtype: ``osid.authorization.rules.AuthorizationRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_rules() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_authorization_rules()`` is true.*

        """
        return # osid.authorization.rules.AuthorizationRulesProxyManager

    authorization_rules_proxy_manager = property(fget=get_authorization_rules_proxy_manager)


