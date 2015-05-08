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


class AuthorizationProfile(osid_managers.OsidProfile):

    def get_authorization_record_types(self):
        """Gets the supported ``Authorization`` record types.

        :return: a list containing the supported authorization record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    authorization_record_types = property(fget=get_authorization_record_types)

    def get_authorization_search_record_types(self):
        """Gets the supported ``Authorization`` search record types.

        :return: a list containing the supported authorization search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    authorization_search_record_types = property(fget=get_authorization_search_record_types)

    def get_function_record_types(self):
        """Gets the supported ``Function`` record types.

        :return: a list containing the supported ``Function`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    function_record_types = property(fget=get_function_record_types)

    def get_function_search_record_types(self):
        """Gets the supported ``Function`` search record types.

        :return: a list containing the supported ``Function`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    function_search_record_types = property(fget=get_function_search_record_types)

    def get_qualifier_record_types(self):
        """Gets the supported ``Qualifier`` record types.

        :return: a list containing the supported ``Qualifier`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    qualifier_record_types = property(fget=get_qualifier_record_types)

    def get_qualifier_search_record_types(self):
        """Gets the supported ``Qualifier`` search record types.

        :return: a list containing the supported ``Qualifier`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    qualifier_search_record_types = property(fget=get_qualifier_search_record_types)

    def get_vault_record_types(self):
        """Gets the supported ``Vault`` record types.

        :return: a list containing the supported ``Vault`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    vault_record_types = property(fget=get_vault_record_types)

    def get_vault_search_record_types(self):
        """Gets the supported vault search record types.

        :return: a list containing the supported ``Vault`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    vault_search_record_types = property(fget=get_vault_search_record_types)

    def get_authorization_condition_record_types(self):
        """Gets the supported ``AuthorizationCondition`` record types.

        :return: a list containing the supported ``AuthorizationCondition`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    authorization_condition_record_types = property(fget=get_authorization_condition_record_types)



class AuthorizationManager(osid_managers.OsidManager, osid_sessions.OsidSession, AuthorizationProfile):

    def get_authorization_batch_manager(self):
        """Gets an ``AuthorizationBatchManager``.

        :return: an ``AuthorizationBatchManager``
        :rtype: ``osid.authorization.batch.AuthorizationBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_batch() is false``

        """
        return # osid.authorization.batch.AuthorizationBatchManager

    authorization_batch_manager = property(fget=get_authorization_batch_manager)

    def get_authorization_rules_manager(self):
        """Gets an ``AuthorizationRulesManager``.

        :return: an ``AuthorizationRulesManager``
        :rtype: ``osid.authorization.rules.AuthorizationRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_rules() is false``

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

        """
        return # boolean

    def use_comparative_vault_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_vault_view(self):
        """A complete view of the ``Vault`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



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

        """
        return # boolean

    def get_vault_query(self):
        """Gets a vault query.

        :return: a vault query
        :rtype: ``osid.authorization.VaultQuery``

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

        """
        return # osid.authorization.VaultList


##
# The following methods are from osid.authorization.VaultSearchSession

    def get_vault_search(self):
        """Gets a vault search.

        :return: a vault search
        :rtype: ``osid.authorization.VaultSearch``

        """
        return # osid.authorization.VaultSearch

    vault_search = property(fget=get_vault_search)

    def get_vault_search_order(self):
        """Gets a vault search order.
        The ``VaultSearchOrder`` is supplied to a ``VaultSearch`` to
        specify the ordering of results.

        :return: the vault search order
        :rtype: ``osid.authorization.VaultSearchOrder``

        """
        return # osid.authorization.VaultSearchOrder

    vault_search_order = property(fget=get_vault_search_order)

    def get_vaults_by_search(self, vault_query, vault_search):
        """Gets the search results matching the given search query using the given search.

        :param vault_query: the vault query
        :type vault_query: ``osid.authorization.VaultQuery``
        :param vault_search: the vault search
        :type vault_search: ``osid.authorization.VaultSearch``
        :return: the search results
        :rtype: ``osid.authorization.VaultSearchResults``
        :raise: ``NullArgument`` -- ``vault_query`` or ``vault_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``vault_query`` or ``vault_search`` is not of this service

        """
        return # osid.authorization.VaultSearchResults

    def get_vault_query_from_inspector(self, vault_query_inspector):
        """Gets a vault query from an inspector.
        The inspector is available from a ``VaultSearchResults``.

        :param vault_query_inspector: a vault query inspector
        :type vault_query_inspector: ``osid.authorization.VaultQueryInspector``
        :return: the vault query
        :rtype: ``osid.authorization.VaultQuery``
        :raise: ``NullArgument`` -- ``vault_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``vault_query_inspector`` is not of this service

        """
        return # osid.authorization.VaultQuery


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

        """
        pass


##
# The following methods are from osid.authorization.VaultNotificationSession

    def can_register_for_vault_notifications(self):
        """Tests if this user can register for ``Vault`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def reliable_vault_notifications(self):
        """Reliable notifications are desired.
        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_vault_notification()`` .



        """
        pass

    def unreliable_vault_notifications(self):
        """Unreliable notifications are desired.
        In unreliable mode, notifications do not need to be
        acknowledged.



        """
        pass

    def acknowledge_vault_notification(self, notification_id):
        """Acknowledge a vault notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_vaults(self):
        """Register for notifications of new vaults.
        ``VaultReceiver.newVaults()`` is invoked when a new ``Vault`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_vaults(self):
        """Registers for notification of updated vaults.
        ``VaultReceiver.changedVaults()`` is invoked when a vault is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_vault(self, vault_id):
        """Registers for notification of an updated vault.
        ``VaultReceiver.changedVaults()`` is invoked when the specified
        vault is changed.

        :param vault_id: the Id of the vault to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_vaults(self):
        """Registers for notification of deleted vaults.
        ``VaultReceiver.deletedVaults()`` is invoked when a vault is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_vault(self, vault_id):
        """Registers for notification of a deleted vault.
        ``VaultReceiver.deletedVaults()`` is invoked when the specified
        vault is deleted.

        :param vault_id: the Id of the vault to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_vault_hierarchy(self):
        """Registers for notification of an updated vault hierarchy structure.
        ``VaultReceiver.changedChildOfVaults()`` is invoked when a node
        experiences a change in its children.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_vault_hierarchy_for_ancestors(self, vault_id):
        """Registers for notification of an updated vault hierarchy structure.
        ``VaultReceiver.changedChildOfVaults()`` is invoked when the
        specified node or any of its ancestors experiences a change in
        its children.

        :param vault_id: the ``Id`` of the ``Vault`` node to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_vault_hierarchy_for_descendants(self, vault_id):
        """Registers for notification of an updated vault hierarchy structure.
        ``VaultReceiver.changedChildOfVaults()`` is invoked when the
        specified node or any of its descendants experiences a change in
        its children.

        :param vault_id: the ``Id`` of the ``Vault`` node to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


##
# The following methods are from osid.authorization.VaultHierarchySession

    def get_vault_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    vault_hierarchy_id = property(fget=get_vault_hierarchy_id)

    def get_vault_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

    vault_hierarchy = property(fget=get_vault_hierarchy)

    def can_access_vault_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_root_vault_ids(self):
        """Gets the root vault ``Ids`` in this hierarchy.

        :return: the root vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    root_vault_ids = property(fget=get_root_vault_ids)

    def get_root_vaults(self):
        """Gets the root vaults in this vault hierarchy.

        :return: the root vaults
        :rtype: ``osid.authorization.VaultList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.authorization.VaultList

    root_vaults = property(fget=get_root_vaults)

    def has_parent_vaults(self, vault_id):
        """Tests if the ``Vault`` has any parents.

        :param vault_id: a vault ``Id``
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if the vault has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def is_parent_of_vault(self, id_, vault_id):
        """Tests if an ``Id`` is a direct parent of a vault.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``vault_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_parent_vault_ids(self, vault_id):
        """Gets the parent ``Ids`` of the given vault.

        :param vault_id: a vault ``Id``
        :type vault_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the vault
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_parent_vaults(self, vault_id):
        """Gets the parents of the given vault.

        :param vault_id: a vault ``Id``
        :type vault_id: ``osid.id.Id``
        :return: the parents of the vault
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.authorization.VaultList

    def is_ancestor_of_vault(self, id_, vault_id):
        """Tests if an ``Id`` is an ancestor of a vault.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``vault_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def has_child_vaults(self, vault_id):
        """Tests if a vault has any children.

        :param vault_id: a ``vault_id``
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if the ``vault_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def is_child_of_vault(self, id_, vault_id):
        """Tests if a vault is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``vault_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_child_vault_ids(self, vault_id):
        """Gets the child ``Ids`` of the given vault.

        :param vault_id: the ``Id`` to query
        :type vault_id: ``osid.id.Id``
        :return: the children of the vault
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_child_vaults(self, vault_id):
        """Gets the children of the given vault.

        :param vault_id: the ``Id`` to query
        :type vault_id: ``osid.id.Id``
        :return: the children of the vault
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.authorization.VaultList

    def is_descendant_of_vault(self, id_, vault_id):
        """Tests if an ``Id`` is a descendant of a vault.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``vault_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_vault_node_ids(self, vault_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given vault.

        :param vault_id: the ``Id`` to query
        :type vault_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a vault node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Node

    def get_vault_nodes(self, vault_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given vault.

        :param vault_id: the ``Id`` to query
        :type vault_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a vault node
        :rtype: ``osid.authorization.VaultNode``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.authorization.VaultNode


##
# The following methods are from osid.authorization.VaultHierarchyDesignSession

    def can_modify_vault_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def add_root_vault(self, vault_id):
        """Adds a root vault.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``vault_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_root_vault(self, vault_id):
        """Removes a root vault from this hierarchy.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``vault_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``vault_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def add_child_vault(self, vault_id, child_id):
        """Adds a child to a vault.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``vault_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``vault_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_child_vault(self, vault_id, child_id):
        """Removes a child from a vault.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``vault_id`` not parent of ``child_id``
        :raise: ``NullArgument`` -- ``vault_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_child_vaults(self, vault_id):
        """Removes all children from a vault.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``vault_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass



class AuthorizationProxyManager(osid_managers.OsidProxyManager, AuthorizationProfile):

    def get_authorization_batch_proxy_manager(self):
        """Gets an ``AuthorizationBatchProxyManager``.

        :return: an ``AuthorizationBatchProxyManager``
        :rtype: ``osid.authorization.batch.AuthorizationBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_batch() is false``

        """
        return # osid.authorization.batch.AuthorizationBatchProxyManager

    authorization_batch_proxy_manager = property(fget=get_authorization_batch_proxy_manager)

    def get_authorization_rules_proxy_manager(self):
        """Gets an ``AuthorizationRulesProxyManager``.

        :return: an ``AuthorizationRulesProxyManager``
        :rtype: ``osid.authorization.rules.AuthorizationRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_rules() is false``

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

        """
        return # boolean

    def use_comparative_vault_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.




        """
        pass

    def use_plenary_vault_view(self):
        """A complete view of the ``Vault`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.




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

        """
        return # boolean

    def get_vault_query(self):
        """Gets a vault query.

        :return: a vault query
        :rtype: ``osid.authorization.VaultQuery``

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

        """
        return # osid.authorization.VaultList


##
# The following methods are from osid.authorization.VaultSearchSession

    def get_vault_search(self):
        """Gets a vault search.

        :return: a vault search
        :rtype: ``osid.authorization.VaultSearch``

        """
        return # osid.authorization.VaultSearch

    vault_search = property(fget=get_vault_search)

    def get_vault_search_order(self):
        """Gets a vault search order.
        The ``VaultSearchOrder`` is supplied to a ``VaultSearch`` to
        specify the ordering of results.


        :return: the vault search order
        :rtype: ``osid.authorization.VaultSearchOrder``

        """
        return # osid.authorization.VaultSearchOrder

    vault_search_order = property(fget=get_vault_search_order)

    def get_vaults_by_search(self, vault_query, vault_search):
        """Gets the search results matching the given search query using the given search.

        :param vault_query: the vault query
        :type vault_query: ``osid.authorization.VaultQuery``
        :param vault_search: the vault search
        :type vault_search: ``osid.authorization.VaultSearch``
        :return: the search results
        :rtype: ``osid.authorization.VaultSearchResults``
        :raise: ``NullArgument`` -- ``vault_query`` or ``vault_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``vault_query`` or ``vault_search`` is not of this service

        """
        return # osid.authorization.VaultSearchResults

    def get_vault_query_from_inspector(self, vault_query_inspector):
        """Gets a vault query from an inspector.
        The inspector is available from a ``VaultSearchResults``.


        :param vault_query_inspector: a vault query inspector
        :type vault_query_inspector: ``osid.authorization.VaultQueryInspector``
        :return: the vault query
        :rtype: ``osid.authorization.VaultQuery``
        :raise: ``NullArgument`` -- ``vault_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``vault_query_inspector`` is not of this service

        """
        return # osid.authorization.VaultQuery


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

        """
        pass


##
# The following methods are from osid.authorization.VaultNotificationSession

    def can_register_for_vault_notifications(self):
        """Tests if this user can register for ``Vault`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.


        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def reliable_vault_notifications(self):
        """Reliable notifications are desired.
        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_vault_notification()`` .




        """
        pass

    def unreliable_vault_notifications(self):
        """Unreliable notifications are desired.
        In unreliable mode, notifications do not need to be
        acknowledged.




        """
        pass

    def acknowledge_vault_notification(self, notification_id):
        """Acknowledge a vault notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_vaults(self):
        """Register for notifications of new vaults.
        ``VaultReceiver.newVaults()`` is invoked when a new ``Vault`` is
        created.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_vaults(self):
        """Registers for notification of updated vaults.
        ``VaultReceiver.changedVaults()`` is invoked when a vault is
        changed.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_vault(self, vault_id):
        """Registers for notification of an updated vault.
        ``VaultReceiver.changedVaults()`` is invoked when the specified
        vault is changed.


        :param vault_id: the Id of the vault to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_vaults(self):
        """Registers for notification of deleted vaults.
        ``VaultReceiver.deletedVaults()`` is invoked when a vault is
        deleted.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_vault(self, vault_id):
        """Registers for notification of a deleted vault.
        ``VaultReceiver.deletedVaults()`` is invoked when the specified
        vault is deleted.


        :param vault_id: the Id of the vault to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_vault_hierarchy(self):
        """Registers for notification of an updated vault hierarchy structure.
        ``VaultReceiver.changedChildOfVaults()`` is invoked when a node
        experiences a change in its children.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_vault_hierarchy_for_ancestors(self, vault_id):
        """Registers for notification of an updated vault hierarchy structure.
        ``VaultReceiver.changedChildOfVaults()`` is invoked when the
        specified node or any of its ancestors experiences a change in
        its children.


        :param vault_id: the ``Id`` of the ``Vault`` node to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_vault_hierarchy_for_descendants(self, vault_id):
        """Registers for notification of an updated vault hierarchy structure.
        ``VaultReceiver.changedChildOfVaults()`` is invoked when the
        specified node or any of its descendants experiences a change in
        its children.


        :param vault_id: the ``Id`` of the ``Vault`` node to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


##
# The following methods are from osid.authorization.VaultHierarchySession

    def get_vault_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    vault_hierarchy_id = property(fget=get_vault_hierarchy_id)

    def get_vault_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

    vault_hierarchy = property(fget=get_vault_hierarchy)

    def can_access_vault_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.


        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_root_vault_ids(self):
        """Gets the root vault ``Ids`` in this hierarchy.

        :return: the root vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    root_vault_ids = property(fget=get_root_vault_ids)

    def get_root_vaults(self):
        """Gets the root vaults in this vault hierarchy.

        :return: the root vaults
        :rtype: ``osid.authorization.VaultList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.authorization.VaultList

    root_vaults = property(fget=get_root_vaults)

    def has_parent_vaults(self, vault_id):
        """Tests if the ``Vault`` has any parents.

        :param vault_id: a vault ``Id``
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if the vault has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def is_parent_of_vault(self, id_, vault_id):
        """Tests if an ``Id`` is a direct parent of a vault.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``vault_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_parent_vault_ids(self, vault_id):
        """Gets the parent ``Ids`` of the given vault.

        :param vault_id: a vault ``Id``
        :type vault_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the vault
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_parent_vaults(self, vault_id):
        """Gets the parents of the given vault.

        :param vault_id: a vault ``Id``
        :type vault_id: ``osid.id.Id``
        :return: the parents of the vault
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.authorization.VaultList

    def is_ancestor_of_vault(self, id_, vault_id):
        """Tests if an ``Id`` is an ancestor of a vault.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``vault_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def has_child_vaults(self, vault_id):
        """Tests if a vault has any children.

        :param vault_id: a ``vault_id``
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if the ``vault_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def is_child_of_vault(self, id_, vault_id):
        """Tests if a vault is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``vault_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_child_vault_ids(self, vault_id):
        """Gets the child ``Ids`` of the given vault.

        :param vault_id: the ``Id`` to query
        :type vault_id: ``osid.id.Id``
        :return: the children of the vault
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_child_vaults(self, vault_id):
        """Gets the children of the given vault.

        :param vault_id: the ``Id`` to query
        :type vault_id: ``osid.id.Id``
        :return: the children of the vault
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.authorization.VaultList

    def is_descendant_of_vault(self, id_, vault_id):
        """Tests if an ``Id`` is a descendant of a vault.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``vault_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_vault_node_ids(self, vault_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given vault.

        :param vault_id: the ``Id`` to query
        :type vault_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a vault node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Node

    def get_vault_nodes(self, vault_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given vault.

        :param vault_id: the ``Id`` to query
        :type vault_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a vault node
        :rtype: ``osid.authorization.VaultNode``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.authorization.VaultNode


##
# The following methods are from osid.authorization.VaultHierarchyDesignSession

    def can_modify_vault_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.


        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def add_root_vault(self, vault_id):
        """Adds a root vault.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``vault_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_root_vault(self, vault_id):
        """Removes a root vault from this hierarchy.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``vault_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``vault_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def add_child_vault(self, vault_id, child_id):
        """Adds a child to a vault.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``vault_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``vault_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_child_vault(self, vault_id, child_id):
        """Removes a child from a vault.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``vault_id`` not parent of ``child_id``
        :raise: ``NullArgument`` -- ``vault_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_child_vaults(self, vault_id):
        """Removes all children from a vault.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``vault_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass



class Vaults(AuthorizationManager):
    pass


