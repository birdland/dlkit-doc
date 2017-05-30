# -*- coding: utf-8 -*-
"""Authorization Open Service Interface Definitions
authorization version 3.0.0

The Authorization OSID manages and queries authorizations.

Authorizations

An ``Authorization`` is an ``OsidRelationship`` that defines who can do
what to what. The grammar of an authorization incluides the subject or
the actor (who), the action or verb (do what), and the object or context
(to what). All three of these components must exist in an authorization
for it to have any explicit meaning. An ``Authorization`` is a mapping
among these three components.

  * ``Agent:`` the actor (eg: tom@coppeto.org)
  * ``Function:`` the action (eg: create purchase order)
  * ``Qualifier:`` the object or context within a Function (eg: on
    account 1967)


This tuple in essence defines a role. "Instructor" is not a role and is
not suitable for making an authorization decision. "Instructs Physics
101", both the function and qualifier, defines the complete role (within
the context of a particular college) that can be used for an
authorization decision.

The basic service of the Authorization OSID is to provide a means for
asking whether a given ``Agent`` is authorized to perform a ``Function``
with a ``Qualifier,`` in other words, if such a mapping exists. The
Agent will generally be obtained from an Authentication service and the
``Function`` and ``Qualifier`` generally known to the consuming
application (a server process needing to protect some resource).

Example
  Authentication auth = authNValidationSession.authenticate(creds);
  
  AuthorizationSession session = authZManager.getAuthorizationSession();
  boolean authorized = session.isAuthorized(auth.getAgentId(), functionId, qualifierId);



The rest of the Authorization OSID is concerned with managing
authorizations.

Explicit/Implicit Authorizations

Authorizations can be explcit or implcit. Explicit authorizations are
managed while implcit authorizations are derived from ``Resources,``
``Function`` and ``Qualifier`` hierrachies. Examples of implcit
authorizations:

  * The Authorization OSID can accept a ``Resource`` in lieu of an
    ``Agent`` as the actor so a Person, Group or Organization may be
    used to specify an authorization. In this case, the explicit
    authorization is the one containing the ``Resource`` and an implicit
    authorization exists for each ``Agent.``
  * ``Qualifiers`` only exist as Hierarchy Nodes since the Authorization
    OSID does not manage the objects used as qualifiers but may manage
    directly, or have access to, a Hierarchy service to obtain the
    identity and relationship among these objects. An explicit
    authorization for a given ``Qualifier`` creates an implcit
    authorization for every child of that ``Qualifier.``


The Authorization OSID manages ``Functions`` directly through its owned
defined sessions and exposes actors via the Resource OSID.
``Qualifiers`` are only exposed through the Hierarchy service as the
Authorization service doesn't have anything to say about the objects
represented by the ``Qualifiers``.

Vault Cataloging

``Authorizations, Functions`` and ``Qualifiers`` may be organized into
one or many ``Vaults``. This serves to categorize authorizatiion data
for the purpose of browsing or auditing. ``Vaults`` are hierarchical
where each node includes all the authorization data of its children. A
single root node will make available all known authorizations and is a
reasonable choice for a default ``Vault`` for a non-federated aware
consumer. A federated authorization scheme is one in which ``Vaults``
are available for selection.

Notifications

Certain consumers may wish to be notified of changes within the service.
Authorization supports notifications via
``AuthorizatioNotificationSession,``  ``FunctionNotificationSession``
and ``VaultNotificationSession``.
  if (manager.supportsAuthorizationNotification()) {
      AuthorizationNotificationSession ans = manager.getAuthorizationNotificationSession(receiver);           
      ans.registerForDeletedAuthorizations();
  }
  
  AuthorizationReceiver receiver {
      newAuthorization(Authorization a) {print("authorization created");}
      deletedAuthorization(Authorization a) {print("authorization removed");}
  }



Sub Packages

The Authorization OSID includes an Authorization Rules OSID for managing
the effectiveness of ``Authorizations``.

"""

from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects
from ..osid import records as osid_records
from ..osid import queries as osid_queries
from ..osid import searches as osid_searches


class AuthorizationProfile(osid_managers.OsidProfile):
    """The ``AuthorizationProfile`` describes the interoperability among authorization services."""

    def __init__(self):
        self._provider_manager = None


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
##
# The following methods are from osid.authorization.VaultLookupSession

    def can_lookup_vaults(self):
        """Tests if this user can perform ``Vault`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_vault_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_vault_view(self):
        """A complete view of the ``Vault`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_vault(self, vault_id):
        """Gets the ``Vault`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Vault`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Vault`` and retained for compatibility.

        :param vault_id: ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: the vault
        :rtype: ``osid.authorization.Vault``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.authorization.Vault

    def get_vaults_by_ids(self, vault_ids):
        """Gets a ``VaultList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the vaults
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Vault`` objects may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param vault_ids: the list of ``Ids`` to retrieve
        :type vault_ids: ``osid.id.IdList``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``vault_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    def get_vaults_by_genus_type(self, vault_genus_type):
        """Gets a ``VaultList`` corresponding to the given vault genus ``Type`` which does not include vaults of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :param vault_genus_type: a vault genus type
        :type vault_genus_type: ``osid.type.Type``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``vault_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    def get_vaults_by_parent_genus_type(self, vault_genus_type):
        """Gets a ``VaultList`` corresponding to the given vault genus ``Type`` and include any additional vaults with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :param vault_genus_type: a vault genus type
        :type vault_genus_type: ``osid.type.Type``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``vault_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    def get_vaults_by_record_type(self, vault_record_type):
        """Gets a ``VaultList`` containing the given vault record ``Type``.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :param vault_record_type: a vault record type
        :type vault_record_type: ``osid.type.Type``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``vault_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    def get_vaults_by_provider(self, resource_id):
        """Gets a ``VaultList`` from the given provider ````.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    def get_vaults(self):
        """Gets all ``Vaults``.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :return: a ``VaultList``
        :rtype: ``osid.authorization.VaultList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    vaults = property(fget=get_vaults)


##
# The following methods are from osid.authorization.VaultQuerySession

    def can_search_vaults(self):
        """Tests if this user can perform ``Vault`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_vault_query(self):
        """Gets a vault query.

        :return: a vault query
        :rtype: ``osid.authorization.VaultQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultQuery

    vault_query = property(fget=get_vault_query)

    def get_vaults_by_query(self, vault_query):
        """Gets a list of ``Vault`` objects matching the given search.

        :param vault_query: the vault query
        :type vault_query: ``osid.authorization.VaultQuery``
        :return: the returned ``VaultList``
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``vault_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``vault_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList


##
# The following methods are from osid.authorization.VaultAdminSession

    def can_create_vaults(self):
        """Tests if this user can create ``Vaults``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Vault``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Vault`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_create_vault_with_record_types(self, vault_record_types):
        """Tests if this user can create a single ``Vault`` using the desired record types.

        While ``AuthorizationManager.getVaultRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Vault``.
        Providing an empty array tests if a ``Vault`` can be created
        with no records.

        :param vault_record_types: array of vault record types
        :type vault_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Vault`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``vault_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_vault_form_for_create(self, vault_record_types):
        """Gets the vault form for creating new vaults.

        A new form should be requested for each create transaction.

        :param vault_record_types: array of vault record types
        :type vault_record_types: ``osid.type.Type[]``
        :return: the vault form
        :rtype: ``osid.authorization.VaultForm``
        :raise: ``NullArgument`` -- ``vault_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form qith requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultForm

    def create_vault(self, vault_form):
        """Creates a new ``Vault``.

        :param vault_form: the form for this ``Vault``
        :type vault_form: ``osid.authorization.VaultForm``
        :return: the new ``Vault``
        :rtype: ``osid.authorization.Vault``
        :raise: ``IllegalState`` -- ``vault_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``vault_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``vault_form`` did not originate from ``get_vault_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.Vault

    def can_update_vaults(self):
        """Tests if this user can update ``Vaults``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Vault``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Vault`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_vault_form_for_update(self, vault_id):
        """Gets the vault form for updating an existing vault.

        A new vault form should be requested for each update
        transaction.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: the vault form
        :rtype: ``osid.authorization.VaultForm``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultForm

    def update_vault(self, vault_form):
        """Updates an existing vault.

        :param vault_form: the form containing the elements to be updated
        :type vault_form: ``osid.authorization.VaultForm``
        :raise: ``IllegalState`` -- ``vault_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``vault_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``vault_form`` did not originate from ``get_vault_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_vaults(self):
        """Tests if this user can delete vaults.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Vault``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Vault`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_vault(self, vault_id):
        """Deletes a ``Vault``.

        :param vault_id: the ``Id`` of the ``Vault`` to remove
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_vault_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Vaults``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Vault`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def alias_vault(self, vault_id, alias_id):
        """Adds an ``Id`` to a ``Vault`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Vault`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another vault it is
        reassigned to the given vault ``Id``.

        :param vault_id: the ``Id`` of a ``Vault``
        :type vault_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




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

    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._vault_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)
        self._sub_package_provider_managers = dict()

    def _set_vault_view(self, session):
        """Sets the underlying vault view to match current view"""
        if self._vault_view == COMPARATIVE:
            try:
                session.use_comparative_vault_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_vault_view()
            except AttributeError:
                pass

    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_vault_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _get_sub_package_provider_manager(self, sub_package_name):
        if sub_package_name in self._sub_package_provider_managers:
            return self._sub_package_provider_managers[sub_package_name]
        config = self._runtime.get_configuration()
        parameter_id = Id('parameter:{0}ProviderImpl@dlkit_service'.format(sub_package_name))
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            sub_package = self._runtime.get_manager(sub_package_name.upper(), provider_impl)
        else:
            # need to add version argument
            sub_package = self._runtime.get_proxy_manager(sub_package_name.upper(), provider_impl)
        self._sub_package_provider_managers[sub_package_name] = sub_package
        return sub_package

    def _get_sub_package_provider_session(self, sub_package, session_name, proxy=None):
        """Gets the session from a sub-package"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            manager = self._get_sub_package_provider_manager(sub_package)
            session = self._instantiate_session('get_' + session_name + '_for_bank',
                                                proxy=self._proxy,
                                                manager=manager)
            self._set_bank_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _instantiate_session(self, method_name, proxy=None, *args, **kwargs):
        """Instantiates a provider session"""
        session_class = getattr(self._provider_manager, method_name)
        if proxy is None:
            try:
                return session_class(bank_id=self._catalog_id, *args, **kwargs)
            except AttributeError:
                return session_class(*args, **kwargs)
        else:
            try:
                return session_class(bank_id=self._catalog_id, proxy=proxy, *args, **kwargs)
            except AttributeError:
                return session_class(proxy=proxy, *args, **kwargs)

    def initialize(self, runtime):
        """OSID Manager initialize"""
        from .primitives import Id
        if self._runtime is not None:
            raise IllegalState('Manager has already been initialized')
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:authorizationProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('AUTHORIZATION', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('AUTHORIZATION', provider_impl)

    def close_sessions(self):
        """Close all sessions, unless session management is set to MANDATORY"""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()

    def use_automatic_session_management(self):
        """Session state will be saved unless closed by consumers"""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will be saved and can not be closed by consumers"""
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved"""
        self._session_management = DISABLED
        self.close_sessions()

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
##
# The following methods are from osid.authorization.VaultLookupSession

    def can_lookup_vaults(self):
        """Tests if this user can perform ``Vault`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_vault_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_vault_view(self):
        """A complete view of the ``Vault`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_vault(self, vault_id):
        """Gets the ``Vault`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Vault`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Vault`` and retained for compatibility.

        :param vault_id: ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: the vault
        :rtype: ``osid.authorization.Vault``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.authorization.Vault

    def get_vaults_by_ids(self, vault_ids):
        """Gets a ``VaultList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the vaults
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Vault`` objects may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param vault_ids: the list of ``Ids`` to retrieve
        :type vault_ids: ``osid.id.IdList``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``vault_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    def get_vaults_by_genus_type(self, vault_genus_type):
        """Gets a ``VaultList`` corresponding to the given vault genus ``Type`` which does not include vaults of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :param vault_genus_type: a vault genus type
        :type vault_genus_type: ``osid.type.Type``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``vault_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    def get_vaults_by_parent_genus_type(self, vault_genus_type):
        """Gets a ``VaultList`` corresponding to the given vault genus ``Type`` and include any additional vaults with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :param vault_genus_type: a vault genus type
        :type vault_genus_type: ``osid.type.Type``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``vault_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    def get_vaults_by_record_type(self, vault_record_type):
        """Gets a ``VaultList`` containing the given vault record ``Type``.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :param vault_record_type: a vault record type
        :type vault_record_type: ``osid.type.Type``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``vault_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    def get_vaults_by_provider(self, resource_id):
        """Gets a ``VaultList`` from the given provider ````.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    def get_vaults(self):
        """Gets all ``Vaults``.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :return: a ``VaultList``
        :rtype: ``osid.authorization.VaultList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    vaults = property(fget=get_vaults)


##
# The following methods are from osid.authorization.VaultQuerySession

    def can_search_vaults(self):
        """Tests if this user can perform ``Vault`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_vault_query(self):
        """Gets a vault query.

        :return: a vault query
        :rtype: ``osid.authorization.VaultQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultQuery

    vault_query = property(fget=get_vault_query)

    def get_vaults_by_query(self, vault_query):
        """Gets a list of ``Vault`` objects matching the given search.

        :param vault_query: the vault query
        :type vault_query: ``osid.authorization.VaultQuery``
        :return: the returned ``VaultList``
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``vault_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``vault_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList


##
# The following methods are from osid.authorization.VaultAdminSession

    def can_create_vaults(self):
        """Tests if this user can create ``Vaults``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Vault``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Vault`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_create_vault_with_record_types(self, vault_record_types):
        """Tests if this user can create a single ``Vault`` using the desired record types.

        While ``AuthorizationManager.getVaultRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Vault``.
        Providing an empty array tests if a ``Vault`` can be created
        with no records.

        :param vault_record_types: array of vault record types
        :type vault_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Vault`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``vault_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_vault_form_for_create(self, vault_record_types):
        """Gets the vault form for creating new vaults.

        A new form should be requested for each create transaction.

        :param vault_record_types: array of vault record types
        :type vault_record_types: ``osid.type.Type[]``
        :return: the vault form
        :rtype: ``osid.authorization.VaultForm``
        :raise: ``NullArgument`` -- ``vault_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form qith requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultForm

    def create_vault(self, vault_form):
        """Creates a new ``Vault``.

        :param vault_form: the form for this ``Vault``
        :type vault_form: ``osid.authorization.VaultForm``
        :return: the new ``Vault``
        :rtype: ``osid.authorization.Vault``
        :raise: ``IllegalState`` -- ``vault_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``vault_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``vault_form`` did not originate from ``get_vault_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.Vault

    def can_update_vaults(self):
        """Tests if this user can update ``Vaults``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Vault``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Vault`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_vault_form_for_update(self, vault_id):
        """Gets the vault form for updating an existing vault.

        A new vault form should be requested for each update
        transaction.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: the vault form
        :rtype: ``osid.authorization.VaultForm``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultForm

    def update_vault(self, vault_form):
        """Updates an existing vault.

        :param vault_form: the form containing the elements to be updated
        :type vault_form: ``osid.authorization.VaultForm``
        :raise: ``IllegalState`` -- ``vault_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``vault_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``vault_form`` did not originate from ``get_vault_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_vaults(self):
        """Tests if this user can delete vaults.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Vault``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Vault`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_vault(self, vault_id):
        """Deletes a ``Vault``.

        :param vault_id: the ``Id`` of the ``Vault`` to remove
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_vault_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Vaults``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Vault`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def alias_vault(self, vault_id, alias_id):
        """Adds an ``Id`` to a ``Vault`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Vault`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another vault it is
        reassigned to the given vault ``Id``.

        :param vault_id: the ``Id`` of a ``Vault``
        :type vault_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




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
##
# The following methods are from osid.authorization.VaultLookupSession

    def can_lookup_vaults(self):
        """Tests if this user can perform ``Vault`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_vault_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_vault_view(self):
        """A complete view of the ``Vault`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_vault(self, vault_id):
        """Gets the ``Vault`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Vault`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Vault`` and retained for compatibility.

        :param vault_id: ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: the vault
        :rtype: ``osid.authorization.Vault``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.authorization.Vault

    def get_vaults_by_ids(self, vault_ids):
        """Gets a ``VaultList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the vaults
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Vault`` objects may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param vault_ids: the list of ``Ids`` to retrieve
        :type vault_ids: ``osid.id.IdList``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``vault_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    def get_vaults_by_genus_type(self, vault_genus_type):
        """Gets a ``VaultList`` corresponding to the given vault genus ``Type`` which does not include vaults of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :param vault_genus_type: a vault genus type
        :type vault_genus_type: ``osid.type.Type``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``vault_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    def get_vaults_by_parent_genus_type(self, vault_genus_type):
        """Gets a ``VaultList`` corresponding to the given vault genus ``Type`` and include any additional vaults with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :param vault_genus_type: a vault genus type
        :type vault_genus_type: ``osid.type.Type``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``vault_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    def get_vaults_by_record_type(self, vault_record_type):
        """Gets a ``VaultList`` containing the given vault record ``Type``.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :param vault_record_type: a vault record type
        :type vault_record_type: ``osid.type.Type``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``vault_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    def get_vaults_by_provider(self, resource_id):
        """Gets a ``VaultList`` from the given provider ````.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Vault`` list
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    def get_vaults(self):
        """Gets all ``Vaults``.

        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.

        :return: a ``VaultList``
        :rtype: ``osid.authorization.VaultList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList

    vaults = property(fget=get_vaults)


##
# The following methods are from osid.authorization.VaultQuerySession

    def can_search_vaults(self):
        """Tests if this user can perform ``Vault`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_vault_query(self):
        """Gets a vault query.

        :return: a vault query
        :rtype: ``osid.authorization.VaultQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultQuery

    vault_query = property(fget=get_vault_query)

    def get_vaults_by_query(self, vault_query):
        """Gets a list of ``Vault`` objects matching the given search.

        :param vault_query: the vault query
        :type vault_query: ``osid.authorization.VaultQuery``
        :return: the returned ``VaultList``
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NullArgument`` -- ``vault_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``vault_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultList


##
# The following methods are from osid.authorization.VaultAdminSession

    def can_create_vaults(self):
        """Tests if this user can create ``Vaults``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Vault``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Vault`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_create_vault_with_record_types(self, vault_record_types):
        """Tests if this user can create a single ``Vault`` using the desired record types.

        While ``AuthorizationManager.getVaultRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Vault``.
        Providing an empty array tests if a ``Vault`` can be created
        with no records.

        :param vault_record_types: array of vault record types
        :type vault_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Vault`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``vault_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_vault_form_for_create(self, vault_record_types):
        """Gets the vault form for creating new vaults.

        A new form should be requested for each create transaction.

        :param vault_record_types: array of vault record types
        :type vault_record_types: ``osid.type.Type[]``
        :return: the vault form
        :rtype: ``osid.authorization.VaultForm``
        :raise: ``NullArgument`` -- ``vault_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form qith requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultForm

    def create_vault(self, vault_form):
        """Creates a new ``Vault``.

        :param vault_form: the form for this ``Vault``
        :type vault_form: ``osid.authorization.VaultForm``
        :return: the new ``Vault``
        :rtype: ``osid.authorization.Vault``
        :raise: ``IllegalState`` -- ``vault_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``vault_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``vault_form`` did not originate from ``get_vault_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.Vault

    def can_update_vaults(self):
        """Tests if this user can update ``Vaults``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Vault``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Vault`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_vault_form_for_update(self, vault_id):
        """Gets the vault form for updating an existing vault.

        A new vault form should be requested for each update
        transaction.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: the vault form
        :rtype: ``osid.authorization.VaultForm``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultForm

    def update_vault(self, vault_form):
        """Updates an existing vault.

        :param vault_form: the form containing the elements to be updated
        :type vault_form: ``osid.authorization.VaultForm``
        :raise: ``IllegalState`` -- ``vault_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``vault_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``vault_form`` did not originate from ``get_vault_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_vaults(self):
        """Tests if this user can delete vaults.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Vault``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Vault`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_vault(self, vault_id):
        """Deletes a ``Vault``.

        :param vault_id: the ``Id`` of the ``Vault`` to remove
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_vault_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Vaults``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Vault`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def alias_vault(self, vault_id, alias_id):
        """Adds an ``Id`` to a ``Vault`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Vault`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another vault it is
        reassigned to the given vault ``Id``.

        :param vault_id: the ``Id`` of a ``Vault``
        :type vault_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




class Vault(osid_objects.OsidCatalog, osid_sessions.OsidSession):
    """A vault defines a collection of authorizations and functions."""

    # WILL THIS EVER BE CALLED DIRECTLY - OUTSIDE OF A MANAGER?
    def __init__(self, provider_manager, catalog, runtime, proxy, **kwargs):
        self._provider_manager = provider_manager
        self._catalog = catalog
        self._runtime = runtime
        osid.OsidObject.__init__(self, self._catalog)  # This is to initialize self._object
        osid.OsidSession.__init__(self, proxy)  # This is to initialize self._proxy
        self._catalog_id = catalog.get_id()
        self._provider_sessions = kwargs
        self._session_management = AUTOMATIC
        self._vault_view = DEFAULT
        self._object_views = dict()
        self._operable_views = dict()
        self._containable_views = dict()

    def _set_vault_view(self, session):
        """Sets the underlying vault view to match current view"""
        if self._vault_view == FEDERATED:
            try:
                session.use_federated_vault_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_vault_view()
            except AttributeError:
                pass

    def _set_object_view(self, session):
        """Sets the underlying object views to match current view"""
        for obj_name in self._object_views:
            if self._object_views[obj_name] == PLENARY:
                try:
                    getattr(session, 'use_plenary_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_comparative_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _set_operable_view(self, session):
        """Sets the underlying operable views to match current view"""
        for obj_name in self._operable_views:
            if self._operable_views[obj_name] == ACTIVE:
                try:
                    getattr(session, 'use_active_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_any_status_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _set_containable_view(self, session):
        """Sets the underlying containable views to match current view"""
        for obj_name in self._containable_views:
            if self._containable_views[obj_name] == SEQUESTERED:
                try:
                    getattr(session, 'use_sequestered_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_unsequestered_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _get_provider_session(self, session_name):
        """Returns the requested provider session.

        Instantiates a new one if the named session is not already known.

        """
        agent_key = self._get_agent_key()
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_vault')
            if self._proxy is None:
                session = session_class(self._catalog.get_id())
            else:
                session = session_class(self._catalog.get_id(), self._proxy)
            self._set_vault_view(session)
            self._set_object_view(session)
            self._set_operable_view(session)
            self._set_containable_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def get_vault_id(self):
        """Gets the Id of this vault."""
        return self._catalog_id

    def get_vault(self):
        """Strange little method to assure conformance for inherited Sessions."""
        return self

    def get_objective_hierarchy_id(self):
        """WHAT am I doing here?"""
        return self._catalog_id

    def get_objective_hierarchy(self):
        """WHAT am I doing here?"""
        return self

    def __getattr__(self, name):
        if '_catalog' in self.__dict__:
            try:
                return self._catalog[name]
            except AttributeError:
                pass
        raise AttributeError

    def close_sessions(self):
        """Close all sessions currently being managed by this Manager to save memory."""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()
        else:
            raise IllegalState()

    def use_automatic_session_management(self):
        """Session state will be saved until closed by consumers."""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will always be saved and can not be closed by consumers."""
        # Session state will be saved and can not be closed by consumers
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved."""
        self._session_management = DISABLED
        self.close_sessions()

    def get_vault_record(self, vault_record_type):
        """Gets the vault record corresponding to the given ``Vault`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``vault_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(vault_record_type)``
        is ``true`` .

        :param vault_record_type: a vault record type
        :type vault_record_type: ``osid.type.Type``
        :return: the vault record
        :rtype: ``osid.authorization.records.VaultRecord``
        :raise: ``NullArgument`` -- ``vault_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(vault_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.records.VaultRecord
##
# The following methods are from osid.authorization.AuthorizationSession

    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.Vault

    vault = property(fget=get_vault)

    def can_access_authorizations(self):
        """Tests if this user can perform authorization checks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if authorization methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def is_authorized(self, agent_id, function_id, qualifier_id):
        """Determines if the given agent is authorized.

        An agent is authorized if an active authorization exists whose
        ``Agent,`` ``Function`` and ``Qualifier`` matches the supplied
        parameters. Authorizations may be defined using groupings or
        hieratchical structures for both the ``Agent`` and the
        ``Qualifier`` but are queried in the de-nornmalized form.

        The ``Agent`` is generally determined through the use of an
        Authentication OSID. The ``Function`` and ``Qualifier`` are
        already known as they map to the desired authorization to
        validate.

        :param agent_id: the ``Id`` of an ``Agent``
        :type agent_id: ``osid.id.Id``
        :param function_id: the ``Id`` of a ``Function``
        :type function_id: ``osid.id.Id``
        :param qualifier_id: the ``Id`` of a ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :return: ``true`` if the user is authorized, ``false`` othersise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``function_id`` is not found
        :raise: ``NullArgument`` -- ``agent_id`` , ``function_id`` or ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure making request

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: Authorizations may be stored in a
        normalized form with respect to various Resources and created
        using specific nodes in a ``Function`` or ``Qualifer``
        hierarchy. The provider needs to maintain a de-normalized
        implicit authorization store or expand the applicable
        hierarchies on the fly to honor this query.  Querying the
        authorization service may in itself require a separate
        authorization. A ``PermissionDenied`` is a result of this
        authorization failure. If no explicit or implicit authorization
        exists for the queried tuple, this method should return
        ``false``.

        """
        return # boolean

    def get_authorization_condition(self, function_id):
        """Gets the ``AuthorizationCondition`` for making conditional authorization checks.

        :param function_id: the ``Id`` of a ``Function``
        :type function_id: ``osid.id.Id``
        :return: an authorization condition
        :rtype: ``osid.authorization.AuthorizationCondition``
        :raise: ``NotFound`` -- ``function_id`` is not found
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure making request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationCondition

    def is_authorized_on_condition(self, agent_id, function_id, qualifier_id, condition):
        """Determines if the given agent is authorized.

        An agent is authorized if an active authorization exists whose
        ``Agent,`` ``Function`` and ``Qualifier`` matches the supplied
        parameters. Authorizations may be defined using groupings or
        hieratchical structures for both the ``Agent`` and the
        ``Qualifier`` but are queried in the de-nornmalized form.

        The ``Agent`` is generally determined through the use of an
        Authentication OSID. The ``Function`` and ``Qualifier`` are
        already known as they map to the desired authorization to
        validate.

        :param agent_id: the ``Id`` of an ``Agent``
        :type agent_id: ``osid.id.Id``
        :param function_id: the ``Id`` of a ``Function``
        :type function_id: ``osid.id.Id``
        :param qualifier_id: the ``Id`` of a ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :param condition: an authorization condition
        :type condition: ``osid.authorization.AuthorizationCondition``
        :return: ``true`` if the user is authorized, ``false`` othersise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``function_id`` is not found
        :raise: ``NullArgument`` -- ``agent_id`` , ``function_id, qualifier_id`` , or ``condition`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure making request
        :raise: ``Unsupported`` -- ``condition`` is not of this service

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: Authorizations may be stored in a
        normalized form with respect to various Resources and created
        using specific nodes in a ``Function`` or ``Qualifer``
        hierarchy. The provider needs to maintain a de-normalized
        implicit authorization store or expand the applicable
        hierarchies on the fly to honor this query.  Querying the
        authorization service may in itself require a separate
        authorization. A ``PermissionDenied`` is a result of this
        authorization failure. If no explicit or implicit authorization
        exists for the queried tuple, this method should return
        ``false``.

        """
        return # boolean


##
# The following methods are from osid.authorization.AuthorizationLookupSession

    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.Vault

    vault = property(fget=get_vault)

    def can_lookup_authorizations(self):
        """Tests if this user can perform authorization lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_authorization_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_authorization_view(self):
        """A complete view of the ``Authorization`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_vault_view(self):
        """Federates the view for methods in this session.

        A federated view will include authorizations in vaults which are
        children of this vault in the vault hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_vault_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this vault only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_effective_authorization_view(self):
        """Only authorizations whose effective dates are current are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_any_effective_authorization_view(self):
        """All authorizations of any effective dates are returned by all methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_implicit_authorization_view(self):
        """Sets the view for methods in this session to implicit authorizations.

        An implicit view will include authorizations derived from other
        authorizations as a result of the ``Qualifier,`` ``Function`` or
        ``Resource`` hierarchies. This method is the opposite of
        ``explicitAuthorizationView()``.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_explicit_authorization_view(self):
        """Sets the view for methods in this session to explicit authorizations.

        An explicit view includes only those authorizations that were
        explicitly defined and not implied. This method is the opposite
        of ``implicitAuthorizationView()``.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_authorization(self, authorization_id):
        """Gets the ``Authorization`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Authorization`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``Authorization`` and
        retained for compatibility.

        :param authorization_id: the ``Id`` of the ``Authorization`` to retrieve
        :type authorization_id: ``osid.id.Id``
        :return: the returned ``Authorization``
        :rtype: ``osid.authorization.Authorization``
        :raise: ``NotFound`` -- no ``Authorization`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.Authorization

    def get_authorizations_by_ids(self, authorization_ids):
        """Gets an ``AuthorizationList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        authorizations specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Authorizations`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param authorization_ids: the list of ``Ids`` to retrieve
        :type authorization_ids: ``osid.id.IdList``
        :return: the returned ``Authorization list``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``authorization_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    def get_authorizations_by_genus_type(self, authorization_genus_type):
        """Gets an ``AuthorizationList`` corresponding to the given authorization genus ``Type`` which does not include authorizations of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        :param authorization_genus_type: an authorization genus type
        :type authorization_genus_type: ``osid.type.Type``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``authorization_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    def get_authorizations_by_parent_genus_type(self, authorization_genus_type):
        """Gets an ``AuthorizationList`` corresponding to the given authorization genus ``Type`` and include authorizations of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        :param authorization_genus_type: an authorization genus type
        :type authorization_genus_type: ``osid.type.Type``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``authorization_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    def get_authorizations_by_record_type(self, authorization_record_type):
        """Gets an ``AuthorizationList`` containing the given authorization record ``Type``.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        :param authorization_record_type: an authorization record type
        :type authorization_record_type: ``osid.type.Type``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``authorization_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    def get_authorizations_on_date(self, from_, to):
        """Gets an ``AuthorizationList`` effective during the entire given date range inclusive but not confined to the date range.

        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    def get_authorizations_for_resource(self, resource_id):
        """Gets a list of ``Authorizations`` associated with a given resource.

        Authorizations related to the given resource, including those
        related through an ``Agent,`` are returned. In plenary mode, the
        returned list contains all known authorizations or an error
        results. Otherwise, the returned list may contain only those
        authorizations that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Authorization list``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    def get_authorizations_for_resource_on_date(self, resource_id, from_, to):
        """Gets an ``AuthorizationList`` effective during the entire given date range inclusive but not confined to the date range.

        Authorizations related to the given resource, including those
        related through an ``Agent,`` are returned.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        In effective mode, authorizations are returned that are
        currently effective. In any effective mode, active
        authorizations and those currently expired are returned.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    def get_authorizations_for_agent(self, agent_id):
        """Gets a list of ``Authorizations`` associated with a given agent.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :return: the returned ``Authorization list``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    def get_authorizations_for_agent_on_date(self, agent_id, from_, to):
        """Gets an ``AuthorizationList`` for the given agent and effective during the entire given date range inclusive but not confined to the date range.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``agent_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    def get_authorizations_for_function(self, function_id):
        """Gets a list of ``Authorizations`` associated with a given function.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        :param function_id: a function ``Id``
        :type function_id: ``osid.id.Id``
        :return: the returned ``Authorization list``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    def get_authorizations_for_function_on_date(self, function_id, from_, to):
        """Gets an ``AuthorizationList`` for the given function and effective during the entire given date range inclusive but not confined to the date range.

        :param function_id: a function ``Id``
        :type function_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``function_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    def get_authorizations_for_resource_and_function(self, resource_id, function_id):
        """Gets a list of ``Authorizations`` associated with a given resource.

        Authorizations related to the given resource, including those
        related through an ``Agent,`` are returned. In plenary mode, the
        returned list contains all known authorizations or an error
        results. Otherwise, the returned list may contain only those
        authorizations that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param function_id: a function ``Id``
        :type function_id: ``osid.id.Id``
        :return: the returned ``Authorization list``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``resource_id`` or ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    def get_authorizations_for_resource_and_function_on_date(self, resource_id, function_id, from_, to):
        """Gets an ``AuthorizationList`` effective during the entire given date range inclusive but not confined to the date range.

        Authorizations related to the given resource, including those
        related through an ``Agent,`` are returned.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        In effective mode, authorizations are returned that are
        currently effective. In any effective mode, active
        authorizations and those currently expired are returned.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param function_id: a function ``Id``
        :type function_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, function_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    def get_authorizations_for_agent_and_function(self, agent_id, function_id):
        """Gets a list of ``Authorizations`` associated with a given agent.

        Authorizations related to the given resource, including those
        related through an ``Agent,`` are returned. In plenary mode, the
        returned list contains all known authorizations or an error
        results. Otherwise, the returned list may contain only those
        authorizations that are accessible through this session.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :param function_id: a function ``Id``
        :type function_id: ``osid.id.Id``
        :return: the returned ``Authorization list``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``agent_id`` or ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    def get_authorizations_for_agent_and_function_on_date(self, agent_id, function_id, from_, to):
        """Gets an ``AuthorizationList`` for the given agent and effective during the entire given date range inclusive but not confined to the date range.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :param function_id: a function ``Id``
        :type function_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Authorization`` list
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``agent_id, function_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    def get_authorizations_by_qualifier(self, qualifier_id):
        """Gets a list of ``Authorizations`` associated with a given qualifier.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        :param qualifier_id: a qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :return: the returned ``Authorization list``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    def get_explicit_authorization(self, authorization_id):
        """Gets the explicit ``Authorization`` that generated the given implicit authorization.

        If the given ``Authorization`` is explicit, then the same
        ``Authorization`` is returned.

        :param authorization_id: an authorization
        :type authorization_id: ``osid.id.Id``
        :return: the explicit ``Authorization``
        :rtype: ``osid.authorization.Authorization``
        :raise: ``NotFound`` -- ``authorization_id`` is not found
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.Authorization

    def get_authorizations(self):
        """Geta all ``Authorizations``.

        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.

        :return: a list of ``Authorizations``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList

    authorizations = property(fget=get_authorizations)


##
# The following methods are from osid.authorization.AuthorizationQuerySession

    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.Vault

    vault = property(fget=get_vault)

    def can_search_authorizations(self):
        """Tests if this user can perform authorization searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_federated_vault_view(self):
        """Federates the view for methods in this session.

        A federated view will include authorizations in vaults which are
        children of this vault in the vault hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_vault_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this vault only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_implicit_authorization_view(self):
        """Sets the view for methods in this session to implicit authorizations.

        An implicit view will include authorizations derived from other
        authorizations as a result of the ``Qualifier,`` ``Function`` or
        ``Resource`` hierarchies. This method is the opposite of
        ``explicit_aut``



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_explicit_authorization_view(self):
        """Sets the view for methods in this session to explicit authorizations.

        An explicit view includes only those authorizations that were
        explicitly defined and not implied. This method is the opposite
        of ``implicitAuthorizationView()``.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_authorization_query(self):
        """Gets an authorization query.

        :return: the authorization query
        :rtype: ``osid.authorization.AuthorizationQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationQuery

    authorization_query = property(fget=get_authorization_query)

    def get_authorizations_by_query(self, authorization_query):
        """Gets a list of ``Authorizations`` matching the given query.

        :param authorization_query: the authorization query
        :type authorization_query: ``osid.authorization.AuthorizationQuery``
        :return: the returned ``AuthorizationList``
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NullArgument`` -- ``authorization_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``authorization_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationList


##
# The following methods are from osid.authorization.AuthorizationAdminSession

    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.Vault

    vault = property(fget=get_vault)

    def can_create_authorizations(self):
        """Tests if this user can create ``Authorizations``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Authorization`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_create_authorization_with_record_types(self, authorization_record_types):
        """Tests if this user can create a single ``Authorization`` using the desired record types.

        While ``AuthorizationManager.getAuthorizationRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``Authorization``. Providing an empty array tests if an
        ``Authorization`` can be created with no records.

        :param authorization_record_types: array of authorization record types
        :type authorization_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Authorization`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``authorization_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_authorization_form_for_create_for_agent(self, agent_id, function_id, qualifier_id, authorization_record_types):
        """Gets the authorization form for creating new authorizations.

        A new form should be requested for each create transaction.

        :param agent_id: the agent ``Id``
        :type agent_id: ``osid.id.Id``
        :param function_id: the function ``Id``
        :type function_id: ``osid.id.Id``
        :param qualifier_id: the qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :param authorization_record_types: array of authorization record types
        :type authorization_record_types: ``osid.type.Type[]``
        :return: the authorization form
        :rtype: ``osid.authorization.AuthorizationForm``
        :raise: ``NotFound`` -- ``agent_id, function_id`` or ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``agent_id, function_id, qualifier_id`` or ``authorization_record_types`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationForm

    def get_authorization_form_for_create_for_resource(self, resource_id, function_id, qualifier_id, authorization_record_types):
        """Gets the authorization form for creating new authorizations.

        A new form should be requested for each create transaction.

        :param resource_id: the resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param function_id: the function ``Id``
        :type function_id: ``osid.id.Id``
        :param qualifier_id: the qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :param authorization_record_types: array of authorization record types
        :type authorization_record_types: ``osid.type.Type[]``
        :return: the authorization form
        :rtype: ``osid.authorization.AuthorizationForm``
        :raise: ``NotFound`` -- ``resource_id, function_id`` or ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id, function_id, qualifier_id,`` or ``authorization_record_types`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationForm

    def get_authorization_form_for_create_for_resource_and_trust(self, resource_id, trust_id, function_id, qualifier_id, authorization_record_types):
        """Gets the authorization form for creating new authorizations.

        A new form should be requested for each create transaction.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param trust_id: an ``Id`` for a circle of trust
        :type trust_id: ``osid.id.Id``
        :param function_id: a function ``Id``
        :type function_id: ``osid.id.Id``
        :param qualifier_id: the qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :param authorization_record_types: array of authorization record types
        :type authorization_record_types: ``osid.type.Type[]``
        :return: the authorization form
        :rtype: ``osid.authorization.AuthorizationForm``
        :raise: ``NotFound`` -- ``resource_id, trust_id, function_id`` , or ``qualifierid`` is not found
        :raise: ``NullArgument`` -- ``resource_id, trust_id`` , ``resource_id, qualifier_id`` or ``authorization_record_types`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationForm

    def create_authorization(self, authorization_form):
        """Creates a new explicit ``Authorization``.

        :param authorization_form: the authorization form
        :type authorization_form: ``osid.authorization.AuthorizationForm``
        :return: ``t`` he new ``Authorization``
        :rtype: ``osid.authorization.Authorization``
        :raise: ``IllegalState`` -- ``authorization_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``authorization_form`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``authorization_form`` did not originate from this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.Authorization

    def can_update_authorizations(self):
        """Tests if this user can update ``Authorizations``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Authorization`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if authorization modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_authorization_form_for_update(self, authorization_id):
        """Gets the authorization form for updating an existing authorization.

        A new authorization form should be requested for each update
        transaction.

        :param authorization_id: the ``Id`` of the ``Authorization``
        :type authorization_id: ``osid.id.Id``
        :return: the authorization form
        :rtype: ``osid.authorization.AuthorizationForm``
        :raise: ``NotFound`` -- ``authorization_id`` is not found
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.AuthorizationForm

    def update_authorization(self, authorization_form):
        """Updates an existing authorization.

        :param authorization_form: the authorization ``Id``
        :type authorization_form: ``osid.authorization.AuthorizationForm``
        :raise: ``IllegalState`` -- ``authorization_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``authorization_form`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``authorization_form`` did not originate from ``get_authorization_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_authorizations(self):
        """Tests if this user can delete ``Authorizations``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Authorization`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Authorization`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_authorization(self, authorization_id):
        """Deletes the ``Authorization`` identified by the given ``Id``.

        :param authorization_id: the ``Id`` of the ``Authorization`` to delete
        :type authorization_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``Authorization`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_authorization_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Authorizations``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Authorization`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def alias_authorization(self, authorization_id, alias_id):
        """Adds an ``Id`` to an ``Authorization`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Authorization`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another authorization. it
        is reassigned to the given authorization ``Id``.

        :param authorization_id: the ``Id`` of an ``Authorization``
        :type authorization_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``authorization_id`` not found
        :raise: ``NullArgument`` -- ``authorization_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass




class VaultList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``VaultList`` provides a means for accessing ``Vault`` elements sequentially either one at a time or many at a time.

    Examples: while (vl.hasNext()) { Vault vault = vl.getNextVault(); }

    or
      while (vl.hasNext()) {
           Vault[] vaults = vl.getNextVaults(vl.available());
      }

    """

    def get_next_vault(self):
        """Gets the next ``Vault`` in this list.

        :return: the next ``Vault`` in this list. The ``has_next()`` method should be used to test that a next ``Vault`` is available before calling this method.
        :rtype: ``osid.authorization.Vault``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.Vault

    next_vault = property(fget=get_next_vault)

    def get_next_vaults(self, n):
        """Gets the next set of ``Vault`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Vault`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Vault`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.authorization.Vault``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.Vault


