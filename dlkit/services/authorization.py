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
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class AuthorizationProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_authorization(self):
        """Tests for the availability of an authorization service which is the basic service for checking authorizations.

        :return: ``true`` if authorization is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_authorization_lookup(self):
        """Tests if an authorization lookup service is supported.
        An authorization lookup service defines methods to access
        authorizations.

        :return: true if authorization lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_authorization_query(self):
        """Tests if an authorization query service is supported.

        :return: ``true`` if authorization query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_authorization_search(self):
        """Tests if an authorization search service is supported.

        :return: ``true`` if authorization search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_authorization_admin(self):
        """Tests if an authorization administrative service is supported.

        :return: ``true`` if authorization admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_authorization_notification(self):
        """Tests if authorization notification is supported.
        Messages may be sent when authorizations are created, modified,
        or deleted.

        :return: ``true`` if authorization notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_authorization_vault(self):
        """Tests if an authorization to vault lookup session is available.

        :return: ``true`` if authorization vault lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_authorization_vault_assignment(self):
        """Tests if an authorization to vault assignment session is available.

        :return: ``true`` if authorization vault assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_authorization_smart_vault(self):
        """Tests if an authorization smart vaulting session is available.

        :return: ``true`` if authorization smart vaulting is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_function_lookup(self):
        """Tests if a function lookup service is supported.
        A function lookup service defines methods to access
        authorization functions.

        :return: ``true`` if function lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_function_query(self):
        """Tests if a function query service is supported.

        :return: ``true`` if function query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_function_search(self):
        """Tests if a function search service is supported.

        :return: ``true`` if function search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_function_admin(self):
        """Tests if a function administrative service is supported.

        :return: ``true`` if function admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_function_notification(self):
        """Tests if function notification is supported.
        Messages may be sent when functions are created, modified, or
        deleted.

        :return: ``true`` if function notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_function_vault(self):
        """Tests if a function to vault lookup session is available.

        :return: ``true`` if function vault lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_function_vault_assignment(self):
        """Tests if a function to vault assignment session is available.

        :return: ``true`` if function vault assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_function_smart_vault(self):
        """Tests if a function smart vaulting session is available.

        :return: ``true`` if function smart vaulting is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_qualifier_lookup(self):
        """Tests if a qualifier lookup service is supported.
        A function lookup service defines methods to access
        authorization qualifiers.

        :return: ``true`` if qualifier lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_qualifier_query(self):
        """Tests if a qualifier query service is supported.

        :return: ``true`` if qualifier query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_qualifier_search(self):
        """Tests if a qualifier search service is supported.

        :return: ``true`` if qualifier search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_qualifier_admin(self):
        """Tests if a qualifier administrative service is supported.

        :return: ``true`` if qualifier admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_qualifier_notification(self):
        """Tests if qualifier notification is supported.
        Messages may be sent when qualifiers are created, modified, or
        deleted.

        :return: ``true`` if qualifier notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_qualifier_hierarchy(self):
        """Tests if a qualifier hierarchy traversal is supported.

        :return: ``true`` if a qualifier hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_qualifier_hierarchy_design(self):
        """Tests if qualifier hierarchy design is supported.

        :return: ``true`` if a qualifier hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_qualifier_vault(self):
        """Tests if a qualifier to vault lookup session is available.

        :return: ``true`` if qualifier vault lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_qualifier_vault_assignment(self):
        """Tests if a qualifier to vault assignment session is available.

        :return: ``true`` if qualifier vault assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_qualifier_smart_vault(self):
        """Tests if a qualifier smart vaulting session is available.

        :return: ``true`` if qualifier smart vault session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_vault_lookup(self):
        """Tests if a vault lookup service is supported.
        A vault lookup service defines methods to access authorization
        vaults.

        :return: ``true`` if function lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_vault_query(self):
        """Tests if a vault query service is supported.

        :return: ``true`` if vault query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_vault_search(self):
        """Tests if a vault search service is supported.

        :return: ``true`` if vault search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_vault_admin(self):
        """Tests if a vault administrative service is supported.

        :return: ``true`` if vault admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_vault_notification(self):
        """Tests if vault notification is supported.
        Messages may be sent when vaults are created, modified, or
        deleted.

        :return: ``true`` if vault notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_vault_hierarchy(self):
        """Tests if a vault hierarchy traversal is supported.

        :return: ``true`` if a vault hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_vault_hierarchy_design(self):
        """Tests if vault hierarchy design is supported.

        :return: ``true`` if a function hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_authorizatin_batch(self):
        """Tests if an authorization batch service is supported.

        :return: ``true`` if an authorization batch service design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_authorizatin_rules(self):
        """Tests if an authorization rules service is supported.

        :return: ``true`` if an authorization rules service design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_authorization_record_types(self):
        """Gets the supported ``Authorization`` record types.

        :return: a list containing the supported authorization record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    authorization_record_types = property(fget=get_authorization_record_types)

    def supports_authorization_record_type(self, authorization_record_type):
        """Tests if the given authorization record type is supported.

        :param authorization_record_type: a ``Type`` indicating an authorization record type
        :type authorization_record_type: ``osid.type.Type``
        :return: ``true`` if the given record Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``authorization_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_authorization_search_record_types(self):
        """Gets the supported ``Authorization`` search record types.

        :return: a list containing the supported authorization search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    authorization_search_record_types = property(fget=get_authorization_search_record_types)

    def supports_authorization_search_record_type(self, authorization_search_record_type):
        """Tests if the given authorization search record type is supported.

        :param authorization_search_record_type: a ``Type`` indicating an authorization search record type
        :type authorization_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``authorization_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_function_record_types(self):
        """Gets the supported ``Function`` record types.

        :return: a list containing the supported ``Function`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    function_record_types = property(fget=get_function_record_types)

    def supports_function_record_type(self, function_record_type):
        """Tests if the given ``Function`` record type is supported.

        :param function_record_type: a ``Type`` indicating a ``Function`` record type
        :type function_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``function_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_function_search_record_types(self):
        """Gets the supported ``Function`` search record types.

        :return: a list containing the supported ``Function`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    function_search_record_types = property(fget=get_function_search_record_types)

    def supports_function_search_record_type(self, function_search_record_type):
        """Tests if the given ``Function`` search record type is supported.

        :param function_search_record_type: a ``Type`` indicating a ``Function`` search record type
        :type function_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``function_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_record_types(self):
        """Gets the supported ``Qualifier`` record types.

        :return: a list containing the supported ``Qualifier`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    qualifier_record_types = property(fget=get_qualifier_record_types)

    def supports_qualifier_record_type(self, qualifier_record_type):
        """Tests if the given ``Qualifier`` record type is supported.

        :param qualifier_record_type: a ``Type`` indicating a ``Qualifier`` record type
        :type qualifier_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``qualifier_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_search_record_types(self):
        """Gets the supported ``Qualifier`` search record types.

        :return: a list containing the supported ``Qualifier`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    qualifier_search_record_types = property(fget=get_qualifier_search_record_types)

    def supports_qualifier_search_record_type(self, qualifier_search_record_type):
        """Tests if the given ``Qualifier`` search record type is supported.

        :param qualifier_search_record_type: a ``Type`` indicating a ``Qualifier`` search record type
        :type qualifier_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``qualifier_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_vault_record_types(self):
        """Gets the supported ``Vault`` record types.

        :return: a list containing the supported ``Vault`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    vault_record_types = property(fget=get_vault_record_types)

    def supports_vault_record_type(self, vault_record_type):
        """Tests if the given ``Vault`` record type is supported.

        :param vault_record_type: a ``Type`` indicating a ``Vault`` type
        :type vault_record_type: ``osid.type.Type``
        :return: ``true`` if the given vault record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``vault_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_vault_search_record_types(self):
        """Gets the supported vault search record types.

        :return: a list containing the supported ``Vault`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    vault_search_record_types = property(fget=get_vault_search_record_types)

    def supports_vault_search_record_type(self, vault_search_record_type):
        """Tests if the given vault search record type is supported.

        :param vault_search_record_type: a ``Type`` indicating a ``Vault`` search record type
        :type vault_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``vault_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_authorization_condition_record_types(self):
        """Gets the supported ``AuthorizationCondition`` record types.

        :return: a list containing the supported ``AuthorizationCondition`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    authorization_condition_record_types = property(fget=get_authorization_condition_record_types)

    def supports_authorization_condition_record_type(self, authorization_condition_record_type):
        """Tests if the given ``AuthorizationCondition`` record type is supported.

        :param authorization_condition_record_type: a ``Type`` indicating an ``AuthorizationCondition`` record type
        :type authorization_condition_record_type: ``osid.type.Type``
        :return: ``true`` if the given authorization condition record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``authorization_condition_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class AuthorizationManager(osid_managers.OsidManager, osid_sessions.OsidSession, AuthorizationProfile):

    def get_authorization_session(self):
        """Gets an ``AuthorizationSession`` which is responsible for performing authorization checks.

        :return: an authorization session for this service
        :rtype: ``osid.authorization.AuthorizationSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization()`` is ``false``

        """
        raise UNIMPLEMENTED()

    authorization_session = property(fget=get_authorization_session)

    def get_authorization_session_for_vault(self, vault_id):
        """Gets an ``AuthorizationSession`` which is responsible for performing authorization checks for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``an _authorization_session``
        :rtype: ``osid.authorization.AuthorizationSession``
        :raise: ``NotFound`` -- ``vault_id``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_lookup_session(self):
        """Gets the ``OsidSession`` associated with the authorization lookup service.

        :return: an ``AuthorizationLookupSession``
        :rtype: ``osid.authorization.AuthorizationLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    authorization_lookup_session = property(fget=get_authorization_lookup_session)

    def get_authorization_lookup_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the authorization lookup service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``an _authorization_lookup_session``
        :rtype: ``osid.authorization.AuthorizationLookupSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_query_session(self):
        """Gets the ``OsidSession`` associated with the authorization query service.

        :return: an ``AuthorizationQuerySession``
        :rtype: ``osid.authorization.AuthorizationQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    authorization_query_session = property(fget=get_authorization_query_session)

    def get_authorization_query_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the authorization query service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``an _authorization_query_session``
        :rtype: ``osid.authorization.AuthorizationQuerySession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_search_session(self):
        """Gets the ``OsidSession`` associated with the authorization search service.

        :return: an ``AuthorizationSearchSession``
        :rtype: ``osid.authorization.AuthorizationSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    authorization_search_session = property(fget=get_authorization_search_session)

    def get_authorization_search_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the authorization search service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``an _authorization_search_session``
        :rtype: ``osid.authorization.AuthorizationSearchSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_admin_session(self):
        """Gets the ``OsidSession`` associated with the authorization administration service.

        :return: an ``AuthorizationAdminSession``
        :rtype: ``osid.authorization.AuthorizationAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    authorization_admin_session = property(fget=get_authorization_admin_session)

    def get_authorization_admin_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the authorization admin service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``an _authorization_admin_session``
        :rtype: ``osid.authorization.AuthorizationAdminSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_notification_session(self, authorization_receiver):
        """Gets the notification session for notifications pertaining to authorization changes.

        :param authorization_receiver: the authorization receiver
        :type authorization_receiver: ``osid.authorization.AuthorizationReceiver``
        :return: an ``AuthorizationNotificationSession``
        :rtype: ``osid.authorization.AuthorizationNotificationSession``
        :raise: ``NullArgument`` -- ``authorization_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_notification_session_for_vault(self, authorization_receiver, vault_id):
        """Gets the ``OsidSession`` associated with the authorization notification service for the given vault.

        :param authorization_receiver: the authorization receiver
        :type authorization_receiver: ``osid.authorization.AuthorizationReceiver``
        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``an _authorization_notification_session``
        :rtype: ``osid.authorization.AuthorizationNotificationSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``authorization_receiver`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_vault_session(self):
        """Gets the session for retrieving authorization to vault mappings.

        :return: an ``AuthorizationVaultSession``
        :rtype: ``osid.authorization.AuthorizationVaultSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_vault()`` is ``false``

        """
        raise UNIMPLEMENTED()

    authorization_vault_session = property(fget=get_authorization_vault_session)

    def get_authorization_vault_assignment_session(self):
        """Gets the session for assigning authorizations to vault mappings.

        :return: a ``AuthorizationVaultAssignmentSession``
        :rtype: ``osid.authorization.AuthorizationVaultAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_vault_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    authorization_vault_assignment_session = property(fget=get_authorization_vault_assignment_session)

    def get_authorization_smart_vault_session(self, vault_id):
        """Gets the session for managing dynamic authorization vaults.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``AuthorizationSmartVaultSession``
        :rtype: ``osid.authorization.AuthorizationSmartVaultSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_smart_vault()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_lookup_session(self):
        """Gets the ``OsidSession`` associated with the function lookup service.

        :return: a ``FunctionLookupSession``
        :rtype: ``osid.authorization.FunctionLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    function_lookup_session = property(fget=get_function_lookup_session)

    def get_function_lookup_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the function lookup service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``a FunctionLookupSession``
        :rtype: ``osid.authorization.FunctionLookupSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_query_session(self):
        """Gets the ``OsidSession`` associated with the function query service.

        :return: a ``FunctionQuerySession``
        :rtype: ``osid.authorization.FunctionQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    function_query_session = property(fget=get_function_query_session)

    def get_function_query_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the function query service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``FunctionQuerySession``
        :rtype: ``osid.authorization.FunctionQuerySession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_search_session(self):
        """Gets the ``OsidSession`` associated with the function search service.

        :return: a ``FunctionSearchSession``
        :rtype: ``osid.authorization.FunctionSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    function_search_session = property(fget=get_function_search_session)

    def get_function_search_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the function search service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``FunctionSearchSession``
        :rtype: ``osid.authorization.FunctionSearchSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_admin_session(self):
        """Gets the ``OsidSession`` associated with the function administration service.

        :return: a ``FunctionAdminSession``
        :rtype: ``osid.authorization.FunctionAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    function_admin_session = property(fget=get_function_admin_session)

    def get_function_admin_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the function admin service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``a FunctionAdminSession``
        :rtype: ``osid.authorization.FunctionAdminSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_notification_session(self, function_receiver):
        """Gets the notification session for notifications pertaining to function changes.

        :param function_receiver: the function receiver
        :type function_receiver: ``osid.authorization.FunctionReceiver``
        :return: a ``FunctionNotificationSession``
        :rtype: ``osid.authorization.FunctionNotificationSession``
        :raise: ``NullArgument`` -- ``function_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_notification_session_for_vault(self, function_receiver, vault_id):
        """Gets the ``OsidSession`` associated with the function notification service for the given vault.

        :param function_receiver: the function receiver
        :type function_receiver: ``osid.authorization.FunctionReceiver``
        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: ``a FunctionNotificationSession``
        :rtype: ``osid.authorization.FunctionNotificationSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``function_receiver`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_vault_session(self):
        """Gets the session for retrieving function to vault mappings.

        :return: a ``FunctionVaultSession``
        :rtype: ``osid.authorization.FunctionVaultSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_vault()`` is ``false``

        """
        raise UNIMPLEMENTED()

    function_vault_session = property(fget=get_function_vault_session)

    def get_function_vault_assignment_session(self):
        """Gets the session for assigning function to vault mappings.

        :return: a ``FunctionVaultAssignmentSession``
        :rtype: ``osid.authorization.FunctionVaultAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_vault_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    function_vault_assignment_session = property(fget=get_function_vault_assignment_session)

    def get_function_smart_vault_session(self, vault_id):
        """Gets the session associated with the function smart vault for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``FunctionSmartVaultSession``
        :rtype: ``osid.authorization.FunctionSmartVaultSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_smart_vault()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_lookup_session(self):
        """Gets the ``OsidSession`` associated with the qualifier lookup service.

        :return: a ``QualifierLookupSession``
        :rtype: ``osid.authorization.QualifierLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    qualifier_lookup_session = property(fget=get_qualifier_lookup_session)

    def get_qualifier_lookup_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the qualifier lookup service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``QualifierLookupSession``
        :rtype: ``osid.authorization.QualifierLookupSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_query_session(self):
        """Gets the ``OsidSession`` associated with the qualifier query service.

        :return: a ``QualifierQuerySession``
        :rtype: ``osid.authorization.QualifierQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    qualifier_query_session = property(fget=get_qualifier_query_session)

    def get_qualifier_query_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the qualifier query service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``QualifierQuerySession``
        :rtype: ``osid.authorization.QualifierQuerySession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_search_session(self):
        """Gets the ``OsidSession`` associated with the qualifier search service.

        :return: a ``QualifierSearchSession``
        :rtype: ``osid.authorization.QualifierSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    qualifier_search_session = property(fget=get_qualifier_search_session)

    def get_qualifier_search_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the qualifier search service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``QualifierSearchSession``
        :rtype: ``osid.authorization.QualifierSearchSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_admin_session(self):
        """Gets the ``OsidSession`` associated with the qualifier administration service.

        :return: a ``QualifierAdminSession``
        :rtype: ``osid.authorization.QualifierAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    qualifier_admin_session = property(fget=get_qualifier_admin_session)

    def get_qualifier_admin_session_for_vault(self, vault_id):
        """Gets the ``OsidSession`` associated with the qualifier admin service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``QualifierAdminSession``
        :rtype: ``osid.authorization.QualifierAdminSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_notification_session(self, qualifier_receiver):
        """Gets the notification session for notifications pertaining to qualifier changes.

        :param qualifier_receiver: the qualifier receiver
        :type qualifier_receiver: ``osid.authorization.QualifierReceiver``
        :return: a ``QualifierNotificationSession``
        :rtype: ``osid.authorization.QualifierNotificationSession``
        :raise: ``NullArgument`` -- ``qualifier_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_notification_session_for_vault(self, qualifier_receiver, vault_id):
        """Gets the ``OsidSession`` associated with the qualifier notification service for the given vault.

        :param qualifier_receiver: the qualifier receiver
        :type qualifier_receiver: ``osid.authorization.QualifierReceiver``
        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``QualifierNotificationSession``
        :rtype: ``osid.authorization.QualifierNotificationSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_receiver`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_hierarchy_session(self, qualifier_hierarchy_id):
        """Gets the ``OsidSession`` associated with the qualifier hierarchy traversal service.
        The authorization service uses distinct hierarchies that can be
        managed through a Hierarchy OSID.

        :param qualifier_hierarchy_id: the ``Id`` of a qualifier hierarchy
        :type qualifier_hierarchy_id: ``osid.id.Id``
        :return: a ``QualifierHierarchySession``
        :rtype: ``osid.authorization.QualifierHierarchySession``
        :raise: ``NotFound`` -- ``qualifier_hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_hierarchy_design_session(self, qualifier_hierarchy_id):
        """Gets the ``OsidSession`` associated with the qualifier hierarchy design service.

        :param qualifier_hierarchy_id: the ``Id`` of a qualifier hierarchy
        :type qualifier_hierarchy_id: ``osid.id.Id``
        :return: a ``QualifierHierarchyDesignSession``
        :rtype: ``osid.authorization.QualifierHierarchyDesignSession``
        :raise: ``NotFound`` -- ``qualifier_hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_vault_session(self):
        """Gets the session for retrieving qualifier to vault mappings.

        :return: a ``QualifierVaultSession``
        :rtype: ``osid.authorization.QualifierVaultSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_vault()`` is ``false``

        """
        raise UNIMPLEMENTED()

    qualifier_vault_session = property(fget=get_qualifier_vault_session)

    def get_qualifier_vault_assignment_session(self):
        """Gets the session for assigning qualifier to vault mappings.

        :return: a ``QualifierVaultAssignmentSession``
        :rtype: ``osid.authorization.QualifierVaultSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_vault_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    qualifier_vault_assignment_session = property(fget=get_qualifier_vault_assignment_session)

    def get_qualifier_smart_vault_session(self, vault_id):
        """Gets the session associated with the qualifier smart vault for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :return: a ``QualifierSmartVaultSession``
        :rtype: ``osid.authorization.QualifierSmartVaultSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_smart_vault()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_vault_lookup_session(self):
        """Gets the OsidSession associated with the vault lookup service.

        :return: a ``VaultLookupSession``
        :rtype: ``osid.authorization.VaultLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_lookup() is false``

        """
        raise UNIMPLEMENTED()

    vault_lookup_session = property(fget=get_vault_lookup_session)

    def get_vault_query_session(self):
        """Gets the OsidSession associated with the vault query service.

        :return: a ``VaultQuerySession``
        :rtype: ``osid.authorization.VaultQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_query() is false``

        """
        raise UNIMPLEMENTED()

    vault_query_session = property(fget=get_vault_query_session)

    def get_vault_search_session(self):
        """Gets the OsidSession associated with the vault search service.

        :return: a ``VaultSearchSession``
        :rtype: ``osid.authorization.VaultSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_search() is false``

        """
        raise UNIMPLEMENTED()

    vault_search_session = property(fget=get_vault_search_session)

    def get_vault_admin_session(self):
        """Gets the OsidSession associated with the vault administration service.

        :return: a ``VaultAdminSession``
        :rtype: ``osid.authorization.VaultAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_admin() is false``

        """
        raise UNIMPLEMENTED()

    vault_admin_session = property(fget=get_vault_admin_session)

    def get_vault_notification_session(self, vaultreceiver):
        """Gets the notification session for notifications pertaining to vault service changes.

        :param vaultreceiver: the vault receiver
        :type vaultreceiver: ``osid.authorization.VaultReceiver``
        :return: a ``VaultNotificationSession``
        :rtype: ``osid.authorization.VaultNotificationSession``
        :raise: ``NullArgument`` -- ``vault_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_notification() is false``

        """
        raise UNIMPLEMENTED()

    def get_vault_hierarchy_session(self):
        """Gets the session traversing vault hierarchies.

        :return: a ``VaultHierarchySession``
        :rtype: ``osid.authorization.VaultHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_hierarchy() is false``

        """
        raise UNIMPLEMENTED()

    vault_hierarchy_session = property(fget=get_vault_hierarchy_session)

    def get_vault_hierarchy_design_session(self):
        """Gets the session designing vault hierarchies.

        :return: a ``VaultHierarchyDesignSession``
        :rtype: ``osid.authorization.VaultHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_hierarchy_design() is false``

        """
        raise UNIMPLEMENTED()

    vault_hierarchy_design_session = property(fget=get_vault_hierarchy_design_session)

    def get_authorization_batch_manager(self):
        """Gets an ``AuthorizationBatchManager``.

        :return: an ``AuthorizationBatchManager``
        :rtype: ``osid.authorization.batch.AuthorizationBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_batch() is false``

        """
        raise UNIMPLEMENTED()

    authorization_batch_manager = property(fget=get_authorization_batch_manager)

    def get_authorization_rules_manager(self):
        """Gets an ``AuthorizationRulesManager``.

        :return: an ``AuthorizationRulesManager``
        :rtype: ``osid.authorization.rules.AuthorizationRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_rules() is false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def use_comparative_vault_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_vault_view(self):
        """A complete view of the ``Vault`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_vault_query(self):
        """Gets a vault query.

        :return: a vault query
        :rtype: ``osid.authorization.VaultQuery``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.VaultSearchSession

    def get_vault_search(self):
        """Gets a vault search.

        :return: a vault search
        :rtype: ``osid.authorization.VaultSearch``

        """
        raise UNIMPLEMENTED()

    vault_search = property(fget=get_vault_search)

    def get_vault_search_order(self):
        """Gets a vault search order.
        The ``VaultSearchOrder`` is supplied to a ``VaultSearch`` to
        specify the ordering of results.

        :return: the vault search order
        :rtype: ``osid.authorization.VaultSearchOrder``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def delete_vault(self, vault_id):
        """Deletes a ``Vault``.

        :param vault_id: the ``Id`` of the ``Vault`` to remove
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


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
        raise UNIMPLEMENTED()

    def register_for_new_vaults(self):
        """Register for notifications of new vaults.
        ``VaultReceiver.newVault()`` is invoked when a new ``Vault`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_vault_ancestors(self, vault_id):
        """Registers for notification if an ancestor is added to the specified vault in the vault hierarchy.
        ``VaultReceiver.newVaultAncestor()`` is invoked when the
        specified vault experiences an addition in ancestry.

        :param vault_id: the ``Id`` of the vault to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_vault_descendants(self, vault_id):
        """Registers for notification if a descendant is added to the specified vault in the vault hierarchy.
        ``VaultReceiver.newVaultDescendant()`` is invoked when the
        specified vault experiences an addition in descendants.

        :param vault_id: the ``Id`` of the vault to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_vaults(self):
        """Registers for notification of updated vaults.
        ``VaultReceiver.changedVault()`` is invoked when a vault is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_vault(self, vault_id):
        """Registers for notification of an updated vault.
        ``VaultReceiver.changedVault()`` is invoked when the specified
        vault is changed.

        :param vault_id: the Id of the vault to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_vaults(self):
        """Registers for notification of deleted vaults.
        ``VaultReceiver.deletedVault()`` is invoked when a vault is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_vault(self, vault_id):
        """Registers for notification of a deleted vault.
        ``VaultReceiver.deletedVault()`` is invoked when the specified
        vault is deleted.

        :param vault_id: the Id of the vault to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_vault_ancestors(self, vault_id):
        """Registers for notification if an ancestor is removed from the specified vault in the vault hierarchy.
        ``VaultReceiver.deletedVaultAncestor()`` is invoked when the
        specified vault experiences a removal of an ancestor.

        :param vault_id: the Id of the vault to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_vault_descendants(self, vault_id):
        """Registers for notification if a descendant is removed from fthe specified vault in the vault hierarchy.
        ``VaultReceiver.deletedVaultDescednant()`` is invoked when the
        specified vault experiences a removal of one of its descendants.

        :param vault_id: the Id of the vault to monitor
        :type vault_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``vault_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.VaultHierarchySession

    def get_vault_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    vault_hierarchy_id = property(fget=get_vault_hierarchy_id)

    def get_vault_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_root_vault_ids(self):
        """Gets the root vault ``Ids`` in this hierarchy.

        :return: the root vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_vault_ids = property(fget=get_root_vault_ids)

    def get_root_vaults(self):
        """Gets the root vaults in this vault hierarchy.

        :return: the root vaults
        :rtype: ``osid.authorization.VaultList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()


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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def remove_root_vault(self, vault_id):
        """Removes a root vault from this hierarchy.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``vault_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``vault_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def remove_child_vaults(self, vault_id):
        """Removes all children from a vault.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``vault_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class AuthorizationProxyManager(osid_managers.OsidProxyManager, AuthorizationProfile):

    def get_authorization_session(self, proxy):
        """Gets an ``AuthorizationSession`` which is responsible for performing authorization checks.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an authorization session for this service
        :rtype: ``osid.authorization.AuthorizationSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_session_for_vault(self, vault_id, proxy):
        """Gets an ``AuthorizationSession`` which is responsible for performing authorization checks for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _authorization_session``
        :rtype: ``osid.authorization.AuthorizationSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the authorization lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AuthorizationLookupSession``
        :rtype: ``osid.authorization.AuthorizationLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_lookup_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the authorization lookup service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _authorization_lookup_session``
        :rtype: ``osid.authorization.AuthorizationLookupSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the authorization query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AuthorizationQuerySession``
        :rtype: ``osid.authorization.AuthorizationQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_query_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the authorization query service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _authorization_query_session``
        :rtype: ``osid.authorization.AuthorizationQuerySession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the authorization search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AuthorizationSearchSession``
        :rtype: ``osid.authorization.AuthorizationSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_search_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the authorization search service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _authorization_search_session``
        :rtype: ``osid.authorization.AuthorizationSearchSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the authorization administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AuthorizationAdminSession``
        :rtype: ``osid.authorization.AuthorizationAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_admin_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the authorization admin service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _authorization_admin_session``
        :rtype: ``osid.authorization.AuthorizationAdminSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_notification_session(self, authorization_receiver, proxy):
        """Gets the notification session for notifications pertaining to authorization changes.

        :param authorization_receiver: the authorization receiver
        :type authorization_receiver: ``osid.authorization.AuthorizationReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AuthorizationNotificationSession``
        :rtype: ``osid.authorization.AuthorizationNotificationSession``
        :raise: ``NullArgument`` -- ``authorization_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_notification_session_for_vault(self, authorization_receiver, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the authorization notification service for the given vault.

        :param authorization_receiver: the authorization receiver
        :type authorization_receiver: ``osid.authorization.AuthorizationReceiver``
        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _authorization_notification_session``
        :rtype: ``osid.authorization.AuthorizationNotificationSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``authorization_receiver`` or ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_authorization_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_vault_session(self, proxy):
        """Gets the session for retrieving authorization to vault mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AuthorizationVaultSession``
        :rtype: ``osid.authorization.AuthorizationVaultSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_vault()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_vault_assignment_session(self, proxy):
        """Gets the session for assigning authorization to vault mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``AuthorizationVaultAssignmentSession``
        :rtype: ``osid.authorization.AuthorizationVaultAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_vault_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_smart_vault_session(self, vault_id, proxy):
        """Gets the session for managing dynamic authorization vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``AuthorizationSmartVaultSession``
        :rtype: ``osid.authorization.AuthorizationSmartVaultSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_smart_vault()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the function lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionLookupSession``
        :rtype: ``osid.authorization.FunctionLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_lookup_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the function lookup service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a FunctionLookupSession``
        :rtype: ``osid.authorization.FunctionLookupSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the function query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionQuerySession``
        :rtype: ``osid.authorization.FunctionQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_query_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the function query service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionQuerySession``
        :rtype: ``osid.authorization.FunctionQuerySession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the function search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionSearchSession``
        :rtype: ``osid.authorization.FunctionSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_search_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the function search service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionSearchSession``
        :rtype: ``osid.authorization.FunctionSearchSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the function administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionAdminSession``
        :rtype: ``osid.authorization.FunctionAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_admin_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the function admin service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a FunctionAdminSession``
        :rtype: ``osid.authorization.FunctionAdminSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_notification_session(self, function_receiver, proxy):
        """Gets the notification session for notifications pertaining to function changes.

        :param function_receiver: the function receiver
        :type function_receiver: ``osid.authorization.FunctionReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionNotificationSession``
        :rtype: ``osid.authorization.FunctionNotificationSession``
        :raise: ``NullArgument`` -- ``function_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_notification_session_for_vault(self, function_receiver, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the function notification service for the given vault.

        :param function_receiver: the function receiver
        :type function_receiver: ``osid.authorization.FunctionReceiver``
        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a FunctionNotificationSession``
        :rtype: ``osid.authorization.FunctionNotificationSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``function_receiver`` or ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_function_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_vault_session(self, proxy):
        """Gets the session for retrieving function to vault mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionVaultSession``
        :rtype: ``osid.authorization.FunctionVaultSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_vault()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_vault_assignment_session(self, proxy):
        """Gets the session for assigning function to vault mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FunctionVaultAssignmentSession``
        :rtype: ``osid.authorization.FunctionVaultAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_vault_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_function_smart_vault_session(self, vault_id, proxy):
        """Gets the session for managing dynamic function vaults for the given vault.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``vault_id`` not found
        :rtype: ``osid.authorization.FunctionSmartVaultSession``
        :raise: ``NotFound`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_function_smart_vault()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the qualifier lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierLookupSession``
        :rtype: ``osid.authorization.QualifierLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_lookup_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the qualifier lookup service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierLookupSession``
        :rtype: ``osid.authorization.QualifierLookupSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the qualifier query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierQuerySession``
        :rtype: ``osid.authorization.QualifierQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_query_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the qualifier query service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierQuerySession``
        :rtype: ``osid.authorization.QualifierQuerySession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the qualifier search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierSearchSession``
        :rtype: ``osid.authorization.QualifierSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_search_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the qualifier search service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierSearchSession``
        :rtype: ``osid.authorization.QualifierSearchSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the qualifier administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierAdminSession``
        :rtype: ``osid.authorization.QualifierAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_admin_session_for_vault(self, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the qualifier admin service for the given vault.

        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierAdminSession``
        :rtype: ``osid.authorization.QualifierAdminSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_notification_session(self, qualifier_receiver, proxy):
        """Gets the notification session for notifications pertaining to qualifier changes.

        :param qualifier_receiver: the qualifier receiver
        :type qualifier_receiver: ``osid.authorization.QualifierReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierNotificationSession``
        :rtype: ``osid.authorization.QualifierNotificationSession``
        :raise: ``NullArgument`` -- ``qualifier_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_notification_session_for_vault(self, qualifier_receiver, vault_id, proxy):
        """Gets the ``OsidSession`` associated with the qualifier notification service for the given vault.

        :param qualifier_receiver: the qualifier receiver
        :type qualifier_receiver: ``osid.authorization.QualifierReceiver``
        :param vault_id: the ``Id`` of the vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierNotificationSession``
        :rtype: ``osid.authorization.QualifierNotificationSession``
        :raise: ``NotFound`` -- ``vault_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_receiver`` or ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_qualifier_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_hierarchy_session(self, qualifier_hierarchy_id, proxy):
        """Gets the ``OsidSession`` associated with the qualifier hierarchy traversal service.
        The authorization service uses distinct hierarchies that can be
        managed through a Hierarchy OSID.

        :param qualifier_hierarchy_id: the ``Id`` of a qualifier hierarchy
        :type qualifier_hierarchy_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierHierarchySession``
        :rtype: ``osid.authorization.QualifierHierarchySession``
        :raise: ``NotFound`` -- ``qualifier_hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_hierarchy_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_hierarchy_design_session(self, qualifier_hierarchy_id, proxy):
        """Gets the ``OsidSession`` associated with the qualifier hierarchy design service.

        :param qualifier_hierarchy_id: the ``Id`` of a qualifier hierarchy
        :type qualifier_hierarchy_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierHierarchyDesignSession``
        :rtype: ``osid.authorization.QualifierHierarchyDesignSession``
        :raise: ``NotFound`` -- ``qualifier_hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_hierarchy_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_vault_session(self, proxy):
        """Gets the session for retrieving qualifier to vault mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierVaultSession``
        :rtype: ``osid.authorization.QualifierVaultSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_vault()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_vault_assignment_session(self, proxy):
        """Gets the session for assigning qualifier to vault mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``QualifierVaultAssignmentSession``
        :rtype: ``osid.authorization.QualifierVaultSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_vault_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_smart_vault_session(self, vault_id, proxy):
        """Gets the session for managing dynamic qualifier vaults for the given vault.

        :param vault_id: the ``Id`` of a vault
        :type vault_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``vault_id`` not found
        :rtype: ``osid.authorization.QualifierSmartVaultSession``
        :raise: ``NotFound`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``NullArgument`` -- ``vault_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_qualifier_smart_vault()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_vault_lookup_session(self, proxy):
        """Gets the OsidSession associated with the vault lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``VaultLookupSession``
        :rtype: ``osid.authorization.VaultLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_lookup() is false``

        """
        raise UNIMPLEMENTED()

    def get_vault_query_session(self, proxy):
        """Gets the OsidSession associated with the vault query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``VaultQuerySession``
        :rtype: ``osid.authorization.VaultQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_query() is false``

        """
        raise UNIMPLEMENTED()

    def get_vault_search_session(self, proxy):
        """Gets the OsidSession associated with the vault search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``VaultSearchSession``
        :rtype: ``osid.authorization.VaultSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_search() is false``

        """
        raise UNIMPLEMENTED()

    def get_vault_admin_session(self, proxy):
        """Gets the OsidSession associated with the vault administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``VaultAdminSession``
        :rtype: ``osid.authorization.VaultAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_admin() is false``

        """
        raise UNIMPLEMENTED()

    def get_vault_notification_session(self, vault_receiver, proxy):
        """Gets the notification session for notifications pertaining to vault service changes.

        :param vault_receiver: the vault receiver
        :type vault_receiver: ``osid.authorization.VaultReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``VaultNotificationSession``
        :rtype: ``osid.authorization.VaultNotificationSession``
        :raise: ``NullArgument`` -- ``vault_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_notification() is false``

        """
        raise UNIMPLEMENTED()

    def get_vault_hierarchy_session(self, proxy):
        """Gets the session traversing vault hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``VaultHierarchySession``
        :rtype: ``osid.authorization.VaultHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_hierarchy() is false``

        """
        raise UNIMPLEMENTED()

    def get_vault_hierarchy_design_session(self, proxy):
        """Gets the session designing vault hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``VaultHierarchySession``
        :rtype: ``osid.authorization.VaultHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_vault_hierarchy_design() is false``

        """
        raise UNIMPLEMENTED()

    def get_authorization_batch_proxy_manager(self):
        """Gets an ``AuthorizationBatchProxyManager``.

        :return: an ``AuthorizationBatchProxyManager``
        :rtype: ``osid.authorization.batch.AuthorizationBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_batch() is false``

        """
        raise UNIMPLEMENTED()

    authorization_batch_proxy_manager = property(fget=get_authorization_batch_proxy_manager)

    def get_authorization_rules_proxy_manager(self):
        """Gets an ``AuthorizationRulesProxyManager``.

        :return: an ``AuthorizationRulesProxyManager``
        :rtype: ``osid.authorization.rules.AuthorizationRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authorization_rules() is false``

        """
        raise UNIMPLEMENTED()

    authorization_rules_proxy_manager = property(fget=get_authorization_rules_proxy_manager)



class Vault(osid_objects.OsidCatalog, osid_sessions.OsidSession):

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

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.AuthorizationSession

    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.

        :return: the ``Vault Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        """Gets the ``Vault`` associated with this session.

        :return: the ``Vault`` associated with this session
        :rtype: ``osid.authorization.Vault``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.AuthorizationLookupSession

    def can_lookup_authorizations(self):
        """Tests if this user can perform authorization lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_authorization_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_authorization_view(self):
        """A complete view of the ``Authorization`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_vault_view(self):
        """Federates the view for methods in this session.
        A federated view will include authorizations in vaults which are
        children of this vault in the vault hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_vault_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this vault only.



        """
        raise UNIMPLEMENTED()

    def use_effective_authorization_view(self):
        """Only authorizations whose effective dates are current are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_any_effective_authorization_view(self):
        """All authorizations of any effective dates are returned by all methods in this session."""
        raise UNIMPLEMENTED()

    def use_implicit_authorization_view(self):
        """Sets the view for methods in this session to implicit authorizations.
        An implicit view will include authorizations derived from other
        authorizations as a result of the ``Qualifier,`` ``Function`` or
        ``Resource`` hierarchies. This method is the opposite of
        ``explicitAuthorizationView()``.



        """
        raise UNIMPLEMENTED()

    def use_explicit_authorization_view(self):
        """Sets the view for methods in this session to explicit authorizations.
        An explicit view includes only those authorizations that were
        explicitly defined and not implied. This method is the opposite
        of ``implicitAuthorizationView()``.



        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    authorizations = property(fget=get_authorizations)


##
# The following methods are from osid.authorization.AuthorizationQuerySession

    def can_search_authorizations(self):
        """Tests if this user can perform authorization searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_authorization_query(self):
        """Gets an authorization query.

        :return: the authorization query
        :rtype: ``osid.authorization.AuthorizationQuery``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.AuthorizationSearchSession

    def get_authorization_search(self):
        """Gets an authorization search.

        :return: the authorization search
        :rtype: ``osid.authorization.AuthorizationSearch``

        """
        raise UNIMPLEMENTED()

    authorization_search = property(fget=get_authorization_search)

    def get_authorization_search_order(self):
        """Gets an authorization search order.
        The ``AuthorizationSearchOrder`` is supplied to an
        ``AuthorizationSearch`` to specify the ordering of results.

        :return: the authorization search order
        :rtype: ``osid.authorization.AuthorizationSearchOrder``

        """
        raise UNIMPLEMENTED()

    authorization_search_order = property(fget=get_authorization_search_order)

    def get_authorizations_by_search(self, authorization_query, authorization_search):
        """Gets the search results matching the given search query using the given search.

        :param authorization_query: the authorization query
        :type authorization_query: ``osid.authorization.AuthorizationQuery``
        :param authorization_search: the authorization search
        :type authorization_search: ``osid.authorization.AuthorizationSearch``
        :return: the returned search results
        :rtype: ``osid.authorization.AuthorizationSearchResults``
        :raise: ``NullArgument`` -- ``authorization_query`` or ``authorization_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``authorization_search`` or ``authorization_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_authorization_query_from_inspector(self, authorization_query_inspector):
        """Gets an authorization query from an inspector.
        The inspector is available from an
        ``AuthorizationSearchResults``.

        :param authorization_query_inspector: an authorization query inspector
        :type authorization_query_inspector: ``osid.authorization.AuthorizationQueryInspector``
        :return: the authorization query
        :rtype: ``osid.authorization.AuthorizationQuery``
        :raise: ``NullArgument`` -- ``authorization_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``authorization_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.AuthorizationAdminSession

    def can_create_authorizations(self):
        """Tests if this user can create ``Authorizations``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Authorization`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    def get_authorization_form_for_create_for_resource_and_trust(self, resource_id, trust_id, function_id, qualifier_id, authorization_record_types):
        """Gets the authorization form for creating new authorizations.
        A new form should be requested for each create transaction.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param trust_id: an ``Id`` for a circle of trust
        :type trust_id: ``osid.type.Type``
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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    def can_update_authorizations(self):
        """Tests if this user can update ``Authorizations``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Authorization`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if authorization modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    def can_delete_authorizations(self):
        """Tests if this user can delete ``Authorizations``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Authorization`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Authorization`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_authorization(self, authorization_id):
        """Deletes the ``Authorization`` identified by the given ``Id``.

        :param authorization_id: the ``Id`` of the ``Authorization`` to delete
        :type authorization_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``Authorization`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_authorization_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Authorizations``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Authorization`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.AuthorizationNotificationSession

    def can_register_for_authorization_notifications(self):
        """Tests if this user can register for ``Authorization`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_authorizations(self):
        """Register for notifications of new authorizations.
        ``AuthorizationReceiver.newAuthorization()`` is invoked when a
        new ``Authorization`` appears in this vault.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_authorizations_for_resource(self, resource_id):
        """Registers for notification of new authorizations for the given resource including any authorizations related to the resource through an agent.
        ``AuthorizationReceiver.newAuthorization()`` is invoked when an
        authorization appears in this vault.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_authorizations_for_function(self, function_id):
        """Register for notifications of new authorizations for the given function.
        ``AuthorizationReceiver.newAuthorization()`` is invoked when a
        new ``Authorization`` appears in this vault.

        :param function_id: the ``Id`` of the ``Function`` to monitor
        :type function_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_authorizations(self):
        """Registers for notification of updated authorizations.
        ``AuthorizationReceiver.changedAuthorization()`` is invoked when
        an authorization in this vault is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_authorizations_for_resource(self, resource_id):
        """Registers for notification of updated authorizations for the given resource including any authorizations related to the resource through an agent.
        ``AuthorizationReceiver.changedAuthorization()`` is invoked when
        an authorization in this vault is changed.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_authorizations_for_function(self, function_id):
        """Registers for notification of updated authorizations for the given function.
        ``AuthorizationReceiver.changedAuthorization()`` is invoked when
        an authorization in this vault is changed.

        :param function_id: the ``Id`` of the ``Function`` to monitor
        :type function_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_authorization(self, authorization_id):
        """Registers for notification of an updated authorization.
        ``AuthorizationReceiver.changedAuthorization()`` is invoked when
        the specified authorization in this vault is changed.

        :param authorization_id: the ``Id`` of the ``Authorization`` to monitor
        :type authorization_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_authorizations(self):
        """Registers for notification of deleted authorizations.
        ``AuthorizationReceiver.deletedAuthorization()`` is invoked when
        an authorization is removed from this vault.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_authorizations_for_resource(self, resource_id):
        """Registers for notification of deleted authorizations for the given resource including any authorizations related to the resource through an agent.
        ``AuthorizationReceiver.deletedAuthorization()`` is invoked when
        an authorization is removed from this vault.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_authorizations_for_function(self, function_id):
        """Registers for notification of deleted authorizations for the given function.
        ``AuthorizationReceiver.deletedAuthorization()`` is invoked when
        an authorization is removed from this vault.

        :param function_id: the ``Id`` of the ``Function`` to monitor
        :type function_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_authorization(self, authorization_id):
        """Registers for notification of a deleted authorization.
        ``AuthorizationReceiver.deletedAuthorization()`` is invoked when
        the specified authorization is removed from this vault.

        :param authorization_id: the ``Id`` of the ``Authorization`` to monitor
        :type authorization_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.AuthorizationVaultSession

    def use_comparative_vault_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_vault_view(self):
        """A complete view of the ``Authorization`` and ``Vault`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def can_lookup_authorization_vault_mappings(self):
        """Tests if this user can perform lookups of authorization/vault mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_authorization_ids_by_vault(self, vault_id):
        """Gets the list of ``Authorization``  ``Ids`` associated with a ``Vault``.

        :param vault_id: ``Id`` of a ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: list of related authorization ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_authorizations_by_vault(self, vault_id):
        """Gets the list of ``Authorizations`` associated with a ``Vault``.

        :param vault_id: ``Id`` of a ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: list of related authorization
        :rtype: ``osid.authorization.AuthorizationList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_authorizations_ids_by_vault(self, vault_ids):
        """Gets the list of ``Authorization Ids`` corresponding to a list of ``Vault`` objects.

        :param vault_ids: list of vault ``Ids``
        :type vault_ids: ``osid.id.IdList``
        :return: list of authorization ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_vault_ids_by_authorization(self, authorization_id):
        """Gets the list of ``Vault``  ``Ids`` mapped to an ``Authorization``.

        :param authorization_id: ``Id`` of an ``Authorization``
        :type authorization_id: ``osid.id.Id``
        :return: list of vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``authorization_id`` is not found
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_vault_by_authorization(self, authorization_id):
        """Gets the list of ``Vault`` objects mapped to an ``Authorization``.

        :param authorization_id: ``Id`` of an ``Authorization``
        :type authorization_id: ``osid.id.Id``
        :return: list of vault
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NotFound`` -- ``authorization_id`` is not found
        :raise: ``NullArgument`` -- ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.AuthorizationVaultAssignmentSession

    def can_assign_authorizations(self):
        """Tests if this user can alter authorization/vault mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_authorizations_to_vault(self, vault_id):
        """Tests if this user can alter authorization/vault mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_vault_ids(self, vault_id):
        """Gets a list of vault including and under the given vault node in which any authorization can be assigned.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: list of assignable vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_vault_ids_for_authorization(self, vault_id, authorization_id):
        """Gets a list of vault including and under the given vault node in which a specific authorization can be assigned.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :param authorization_id: the ``Id`` of the ``Authorization``
        :type authorization_id: ``osid.id.Id``
        :return: list of assignable vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_id`` or ``authorization_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_authorization_to_vault(self, authorization_id, vault_id):
        """Adds an existing ``Authorization`` to a ``Vault``.

        :param authorization_id: the ``Id`` of the ``Authorization``
        :type authorization_id: ``osid.id.Id``
        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``authorization_id`` is already assigned to ``vault_id``
        :raise: ``NotFound`` -- ``authorization_id`` or ``vault_id`` not found
        :raise: ``NullArgument`` -- ``authorization_id`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_authorization_from_vault(self, authorization_id, vault_id):
        """Removes an ``Authorization`` from a ``Vault``.

        :param authorization_id: the ``Id`` of the ``Authorization``
        :type authorization_id: ``osid.id.Id``
        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``authorization_id`` or ``vault_id`` not found or ``authorization_id`` not assigned to ``vault_id``
        :raise: ``NullArgument`` -- ``authorization_id`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.AuthorizationSmartVaultSession

    def can_manage_smart_vault(self):
        """Tests if this user can manage smart vault.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart vault management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_authorization_query(self, authorization_query):
        """Applies a authorization query to this vault.

        :param authorization_query: the authorization query
        :type authorization_query: ``osid.authorization.AuthorizationQuery``
        :raise: ``NullArgument`` -- ``authorization_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``authorization_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_authorization_query(self):
        """Gets a authorization query inspector for this vault.

        :return: the authorization query inspector
        :rtype: ``osid.authorization.AuthorizationQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_authorization_sequencing(self, authorization_search_order):
        """Applies a authorization search order to this vault.

        :param authorization_search_order: the authorization search order
        :type authorization_search_order: ``osid.authorization.AuthorizationSearchOrder``
        :raise: ``NullArgument`` -- ``authorization_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``authorization_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.FunctionLookupSession

    def can_lookup_functions(self):
        """Tests if this user can perform ``Function`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_function_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_function_view(self):
        """A complete view of the ``Function`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_active_function_view(self):
        """Only active functions are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_any_status_function_view(self):
        """Active and inactive functions are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def get_function(self, function_id):
        """Gets the ``Function`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Function`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Function`` and retained for
        compatibility.

        :param function_id: the ``Id`` of the ``Function`` to retrieve
        :type function_id: ``osid.id.Id``
        :return: the returned ``Function``
        :rtype: ``osid.authorization.Function``
        :raise: ``NotFound`` -- no ``Function`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_functions_by_ids(self, function_ids):
        """Gets a ``FunctionList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the functions
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Functions`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param function_ids: the list of ``Ids`` to retrieve
        :type function_ids: ``osid.id.IdList``
        :return: the returned ``Function`` list
        :rtype: ``osid.authorization.FunctionList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``function_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_functions_by_genus_type(self, function_genus_type):
        """Gets a ``FunctionList`` corresponding to the given function genus ``Type`` which does not include functions of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known functions
        or an error results. Otherwise, the returned list may contain
        only those functions that are accessible through this session.

        :param function_genus_type: a function genus type
        :type function_genus_type: ``osid.type.Type``
        :return: the returned ``Function`` list
        :rtype: ``osid.authorization.FunctionList``
        :raise: ``NullArgument`` -- ``function_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_functions_by_parent_genus_type(self, function_genus_type):
        """Gets a ``FunctionList`` corresponding to the given function genus ``Type`` and include any additional functions with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known functions
        or an error results. Otherwise, the returned list may contain
        only those functions that are accessible through this session.

        :param function_genus_type: a function genus type
        :type function_genus_type: ``osid.type.Type``
        :return: the returned ``Function`` list
        :rtype: ``osid.authorization.FunctionList``
        :raise: ``NullArgument`` -- ``function_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_functions_by_record_type(self, function_record_type):
        """Gets a ``FunctionList`` containing the given function record ``Type``.
        In plenary mode, the returned list contains all known functions
        or an error results. Otherwise, the returned list may contain
        only those functions that are accessible through this session.

        :param function_record_type: a function record type
        :type function_record_type: ``osid.type.Type``
        :return: the returned ``Function`` list
        :rtype: ``osid.authorization.FunctionList``
        :raise: ``NullArgument`` -- ``function_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_functions(self):
        """Gets all ``Functions``.
        In plenary mode, the returned list contains all known functions
        or an error results. Otherwise, the returned list may contain
        only those functions that are accessible through this session.

        :return: a list of ``Functions``
        :rtype: ``osid.authorization.FunctionList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    functions = property(fget=get_functions)


##
# The following methods are from osid.authorization.FunctionQuerySession

    def can_search_functions(self):
        """Tests if this user can perform ``Function`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_function_query(self):
        """Gets a function query.

        :return: the function query
        :rtype: ``osid.authorization.FunctionQuery``

        """
        raise UNIMPLEMENTED()

    function_query = property(fget=get_function_query)

    def get_functions_by_query(self, function_query):
        """Gets a list of ``Functions`` matching the given query.

        :param function_query: the function query
        :type function_query: ``osid.authorization.FunctionQuery``
        :return: the returned ``FunctionList``
        :rtype: ``osid.authorization.FunctionList``
        :raise: ``NullArgument`` -- ``function_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``function_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.FunctionSearchSession

    def get_function_search(self):
        """Gets a function search.

        :return: the function search
        :rtype: ``osid.authorization.FunctionSearch``

        """
        raise UNIMPLEMENTED()

    function_search = property(fget=get_function_search)

    def get_function_search_order(self):
        """Gets a function search order.
        The ``FunctionSearchOrder`` is supplied to a ``FunctionSearch``
        to specify the ordering of results.

        :return: the function search order
        :rtype: ``osid.authorization.FunctionSearchOrder``

        """
        raise UNIMPLEMENTED()

    function_search_order = property(fget=get_function_search_order)

    def get_functions_by_search(self, function_query, function_search):
        """Gets the search results matching the given search query using the given search.

        :param function_query: the function query
        :type function_query: ``osid.authorization.FunctionQuery``
        :param function_search: the function search
        :type function_search: ``osid.authorization.FunctionSearch``
        :return: the returned search results
        :rtype: ``osid.authorization.FunctionSearchResults``
        :raise: ``NullArgument`` -- ``function_query`` or ``function_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``function_search`` or ``function_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_function_query_from_inspector(self, function_query_inspector):
        """Gets a function query from an inspector.
        The inspector is available from a ``FunctionSearchResults``.

        :param function_query_inspector: a function query inspector
        :type function_query_inspector: ``osid.authorization.FunctionQueryInspector``
        :return: the function query
        :rtype: ``osid.authorization.FunctionQuery``
        :raise: ``NullArgument`` -- ``function_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``function_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.FunctionAdminSession

    def can_create_functions(self):
        """Tests if this user can create ``Functions``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Function`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Function`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_function_with_record_types(self, function_record_types):
        """Tests if this user can create a single ``Function`` using the desired record types.
        While ``AuthorizationManager.getFunctionRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Function``. Providing an empty array tests if a ``Function``
        can be created with no records.

        :param function_record_types: array of function record types
        :type function_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Function`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``function_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_function_form_for_create(self, function_record_types):
        """Gets the function form for creating new functions.
        A new form should be requested for each create transaction.

        :param function_record_types: array of function record types
        :type function_record_types: ``osid.type.Type[]``
        :return: the function form
        :rtype: ``osid.authorization.FunctionForm``
        :raise: ``NullArgument`` -- ``function_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form qith requested record types

        """
        raise UNIMPLEMENTED()

    def create_function(self, function_form):
        """Creates a new ``Function``.

        :param function_form: the form for this ``Function``
        :type function_form: ``osid.authorization.FunctionForm``
        :return: the new ``Function``
        :rtype: ``osid.authorization.Function``
        :raise: ``IllegalState`` -- ``function_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``function_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``function_form`` did not originate from ``get_function_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_functions(self):
        """Tests if this user can update ``Functions``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Function`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if function modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_function_form_for_update(self, function_id):
        """Gets the function form for updating an existing function.
        A new function form should be requested for each update
        transaction.

        :param function_id: the ``Id`` of the ``Function``
        :type function_id: ``osid.id.Id``
        :return: the function form
        :rtype: ``osid.authorization.FunctionForm``
        :raise: ``NotFound`` -- ``function_id`` is not found
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_function(self, function_form):
        """Updates an existing function.

        :param function_form: the form containing the elements to be updated
        :type function_form: ``osid.authorization.FunctionForm``
        :raise: ``IllegalState`` -- ``function_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``function_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``function_form`` did not originate from ``get_function_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_functions(self):
        """Tests if this user can delete ``Functions``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Function`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Function`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_function(self, function_id):
        """Deletes the ``Function`` identified by the given ``Id``.

        :param function_id: the ``Id`` of the ``Function`` to delete
        :type function_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Function`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_function_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Functions``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Function`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_function(self, function_id, alias_id):
        """Adds an ``Id`` to a ``Function`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Function`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another function, it is
        reassigned to the given function ``Id``.

        :param function_id: the ``Id`` of a ``Function``
        :type function_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``function_id`` not found
        :raise: ``NullArgument`` -- ``function_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.FunctionNotificationSession

    def can_register_for_function_notifications(self):
        """Tests if this user can register for ``Function`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_functions(self):
        """Register for notifications of new functions.
        ``FunctionReceiver.newFunction()`` is invoked when a new
        Function is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_functions(self):
        """Registers for notification of updated functions.
        ``FunctionReceiver.changedFunction()`` is invoked when a
        function is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_function(self, function_id):
        """Registers for notification of an updated function.
        ``FunctionReceiver.changedFunction()`` is invoked when the
        specified function is changed.

        :param function_id: the ``Id`` of the ``Function`` to monitor
        :type function_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``function_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_functions(self):
        """Registers for notification of deleted functions.
        ``FunctionReceiver.deletedFunction()`` is invoked when a
        function is removed from this vault.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_function(self, function_id):
        """Registers for notification of a deleted function.
        ``FunctionReceiver.changedFunction()`` is invoked when the
        specified function is removed from this vault.

        :param function_id: the ``Id`` of the ``Function`` to monitor
        :type function_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``function_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.FunctionVaultSession

    def can_lookup_function_vault_mappings(self):
        """Tests if this user can perform lookups of function/vault mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_function_ids_by_vault(self, vault_id):
        """Gets the list of ``Function``  ``Ids`` associated with a ``Vault``.

        :param vault_id: ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: list of related function ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_functions_by_vault(self, vault_id):
        """Gets the list of ``Functions`` associated with a ``Vault``.

        :param vault_id: ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: list of related functions
        :rtype: ``osid.authorization.FunctionList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_function_ids_by_vaults(self, vault_ids):
        """Gets the list of ``Function Ids`` corresponding to a list of ``Vaults``.

        :param vault_ids: list of vault ``Ids``
        :type vault_ids: ``osid.id.IdList``
        :return: list of function ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_functions_by_vaults(self, vault_ids):
        """Gets the list of ``Functions`` corresponding to a list of ``Vaults``.

        :param vault_ids: list of vault ``Ids``
        :type vault_ids: ``osid.id.IdList``
        :return: list of functions
        :rtype: ``osid.authorization.FunctionList``
        :raise: ``NullArgument`` -- ``vault_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_vault_ids_by_function(self, function_id):
        """Gets the list of ``Vault``  ``Ids`` mapped to a ``Function``.

        :param function_id: ``Id`` of a ``Function``
        :type function_id: ``osid.id.Id``
        :return: list of vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``function_id`` is not found
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_vaults_by_function(self, function_id):
        """Gets the list of ``Vaults`` mapped to a ``Function``.

        :param function_id: ``Id`` of a ``Function``
        :type function_id: ``osid.id.Id``
        :return: list of vaults
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NotFound`` -- ``function_id`` is not found
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.FunctionVaultAssignmentSession

    def can_assign_functions(self):
        """Tests if this user can alter function/vault mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_functions_to_vault(self, vault_id):
        """Tests if this user can alter function/vault mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_vault_ids_for_function(self, vault_id, function_id):
        """Gets a list of vault including and under the given vault node in which a specific function can be assigned.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :param function_id: the ``Id`` of the ``Function``
        :type function_id: ``osid.id.Id``
        :return: list of assignable vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_id`` or ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_function_to_vault(self, function_id, vault_id):
        """Adds an existing ``Function`` to a ``Vault``.

        :param function_id: the ``Id`` of the ``Function``
        :type function_id: ``osid.id.Id``
        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``function_id`` is already assigned to ``vault_id``
        :raise: ``NotFound`` -- ``function_id`` or ``vault_id`` not found
        :raise: ``NullArgument`` -- ``function_id`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_function_from_vault(self, function_id, vault_id):
        """Removes a ``Function`` from a ``Vault``.

        :param function_id: the ``Id`` of the ``Function``
        :type function_id: ``osid.id.Id``
        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``function_id`` or ``vault_id`` not found or ``function_id`` not assigned to ``vault_id``
        :raise: ``NullArgument`` -- ``function_id`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.FunctionSmartVaultSession

    def can_manage_smart_vaults(self):
        """Tests if this user can manage smart vaults.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart vault management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_function_query(self, function_query):
        """Applies a function query to this vault.

        :param function_query: the function query
        :type function_query: ``osid.authorization.FunctionQuery``
        :raise: ``NullArgument`` -- ``function_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``function_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_function_query(self):
        """Gets a function query inspector for this vault.

        :return: the function query inspector
        :rtype: ``osid.authorization.FunctionQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_function_sequencing(self, function_search_order):
        """Applies a function search order to this vault.

        :param function_search_order: the function search order
        :type function_search_order: ``osid.authorization.FunctionSearchOrder``
        :raise: ``NullArgument`` -- ``function_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``function_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.QualifierLookupSession

    def can_lookup_qualifiers(self):
        """Tests if this user can perform ``Qualifier`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_qualifier_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_qualifier_view(self):
        """A complete view of the ``Qualifier`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_qualifier(self, qualifier_id):
        """Gets the ``Qualifier`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Qualifier`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Qualifier`` and retained
        for compatibility.

        :param qualifier_id: ``Id`` of the ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :return: the qualifier
        :rtype: ``osid.authorization.Qualifier``
        :raise: ``NotFound`` -- ``qualifier_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_qualifiers_by_ids(self, qualifier_ids):
        """Gets a ``QualifierList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the
        qualifiers specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Qualifiers`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param qualifier_ids: the list of ``Ids`` to retrieve
        :type qualifier_ids: ``osid.id.IdList``
        :return: the returned ``Qualifier`` list
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``qualifier_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_qualifiers_by_genus_type(self, qualifier_genus_type):
        """Gets a ``QualifierList`` corresponding to the given qualifier genus ``Type`` which does not include qualifiers of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known qualifiers
        or an error results. Otherwise, the returned list may contain
        only those qualifiers that are accessible through this session.
        In both cases, the order of the set is not specified.

        :param qualifier_genus_type: a qualifier genus type
        :type qualifier_genus_type: ``osid.type.Type``
        :return: the returned ``Qualifier`` list
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NullArgument`` -- ``qualifier_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_qualifiers_by_parent_genus_type(self, qualifier_genus_type):
        """Gets a ``QualifierList`` corresponding to the given qualifier genus ``Type`` and include any additional qualifiers with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known qualifiers
        or an error results. Otherwise, the returned list may contain
        only those qualifiers that are accessible through this session.

        :param qualifier_genus_type: a qualifier genus type
        :type qualifier_genus_type: ``osid.type.Type``
        :return: the returned ``Qualifier`` list
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NullArgument`` -- ``qualifier_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_qualifiers_by_record_type(self, qualifier_record_type):
        """Gets a ``QualifierList`` corresponding to the given qualifier record ``Type``.
        The set of qualifiers implementing the given record type is
        returned. In plenary mode, the returned list contains all known
        qualifiers or an error results. Otherwise, the returned list may
        contain only those qualifiers that are accessible through this
        session.

        :param qualifier_record_type: a qualifier record type
        :type qualifier_record_type: ``osid.type.Type``
        :return: the returned ``Qualifier`` list
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NullArgument`` -- ``qualifier_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_qualifiers(self):
        """Gets all ``Qualifiers``.
        In plenary mode, the returned list contains all known qualifiers
        or an error results. Otherwise, the returned list may contain
        only those qualifiers that are accessible through this session.

        :return: a list of ``Qualifiers``
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    qualifiers = property(fget=get_qualifiers)


##
# The following methods are from osid.authorization.QualifierQuerySession

    def can_search_qualifiers(self):
        """Tests if this user can perform ``Qualifier`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_query(self):
        """Gets a qualifier query.

        :return: the qualifier query
        :rtype: ``osid.authorization.QualifierQuery``

        """
        raise UNIMPLEMENTED()

    qualifier_query = property(fget=get_qualifier_query)

    def get_qualifiers_by_query(self, qualifier_query):
        """Gets a list of ``Qualifiers`` matching the given search.

        :param qualifier_query: the search query array
        :type qualifier_query: ``osid.authorization.QualifierQuery``
        :return: the returned ``QualifierList``
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NullArgument`` -- ``qualifier_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``qualifier_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.QualifierSearchSession

    def get_qualifier_search(self):
        """Gets a qualifier search.

        :return: the qualifier search
        :rtype: ``osid.authorization.QualifierSearch``

        """
        raise UNIMPLEMENTED()

    qualifier_search = property(fget=get_qualifier_search)

    def get_qualifier_search_order(self):
        """Gets a qualifier search order.
        The ``QualifierSearchOrder`` is supplied to a
        ``QualifierSearch`` to specify the ordering of results.

        :return: the qualifier search order
        :rtype: ``osid.authorization.QualifierSearchOrder``

        """
        raise UNIMPLEMENTED()

    qualifier_search_order = property(fget=get_qualifier_search_order)

    def get_qualifiers_by_search(self, qualifier_query, qualifier_search):
        """Gets the search results matching the given search query using the given search.

        :param qualifier_query: the qualifier query
        :type qualifier_query: ``osid.authorization.QualifierQuery``
        :param qualifier_search: the qualifier search
        :type qualifier_search: ``osid.authorization.QualifierSearch``
        :return: the search results
        :rtype: ``osid.authorization.QualifierSearchResults``
        :raise: ``NullArgument`` -- ``qualifier_queriy`` or ``qualifier_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``qualifier_query`` or ``qualifier_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_qualifier_query_from_inspector(self, qualifier_query_inspector):
        """Gets a qualifier query from an inspector.
        The inspector is available from a ``QualifierSearchResults``.

        :param qualifier_query_inspector: a qualifier query inspector
        :type qualifier_query_inspector: ``osid.authorization.QualifierQueryInspector``
        :return: the qualifier query
        :rtype: ``osid.authorization.QualifierQuery``
        :raise: ``NullArgument`` -- ``qualifier_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``qualifier_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.QualifierAdminSession

    def can_create_qualifiers(self):
        """Tests if this user can create ``Qualifiers``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Qualifier`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Qualifier`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_qualifier_with_record_types(self, qualifier_record_types):
        """Tests if this user can create a single ``Qualifier`` using the desired record types.
        While ``AuthorizationManager.getQualifierRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Qualifier``. Providing an empty array tests if a ``Qualifier``
        can be created with no records.

        :param qualifier_record_types: array of qualifier record types
        :type qualifier_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Qualifier`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``qualifier_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_form_for_create(self, qualifier_record_types):
        """Gets the qualifier form for creating new qualifiers.
        A new form should be requested for each create transaction.

        :param qualifier_record_types: array of qualifier record types
        :type qualifier_record_types: ``osid.type.Type[]``
        :return: the qualifier form
        :rtype: ``osid.authorization.QualifierForm``
        :raise: ``NullArgument`` -- ``qualifier_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        """
        raise UNIMPLEMENTED()

    def create_qualifier(self, qualifier_form):
        """Creates a new ``Qualifier``.

        :param qualifier_form: the form for this ``Qualifier``
        :type qualifier_form: ``osid.authorization.QualifierForm``
        :return: the new ``Qualifier``
        :rtype: ``osid.authorization.Qualifier``
        :raise: ``IllegalState`` -- ``qualifier_form`` already used for a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``qualifier_forms`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``qualifier_form`` did not originate from ``get_qualifier_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_qualifiers(self):
        """Tests if this user can update ``Qualifiers``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Qualifier`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``Qualifier`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_form_for_update(self, qualifier_id):
        """Gets the qualifier form for updating an existing qualifier.
        A new qualifier form should be requested for each update
        transaction.

        :param qualifier_id: the ``Id`` of the ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :return: the qualifier form
        :rtype: ``osid.authorization.QualifierForm``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_qualifier(self, qualifier_form):
        """Updates an existing qualifier.

        :param qualifier_form: the form containing the elements to be updated
        :type qualifier_form: ``osid.authorization.QualifierForm``
        :raise: ``IllegalState`` -- ``qualifier_form`` already used for an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``qualifier_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``qualifier_form`` did not originate from ``get_qualifier_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_qualifiers(self):
        """Tests if this user can delete ``Qualifiers``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Qualifier`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Qualifier`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_qualifier(self, qualifier_id):
        """Deletes a ``Qualifier``.

        :param qualifier_id: the ``Id`` of the ``Qualifier`` to remove
        :type qualifier_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``qualifier_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_qualifier_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Qualifiers``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Qualifier`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_qualifier(self, qualifier_id, alias_id):
        """Adds an ``Id`` to a ``Qualifier`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Qualifier`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another qualifier, it is
        reassigned to the given qualifier ``Id``.

        :param qualifier_id: the ``Id`` of a ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``qualifier_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.QualifierNotificationSession

    def can_register_for_qualifier_notifications(self):
        """Tests if this user can register for ``Qualifier`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_qualifiers(self):
        """Register for notifications of new qualifiers.
        ``QualifierReceiver.newQualifier()`` is invoked when a new
        ``Qualifier`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_qualifier_ancestors(self, qualifier_id):
        """Registers for notification if an ancestor is added to the specified qualifier in the qualifier hierarchy.
        ``QualifierReceiver.newQualifierAncestor()`` is invoked when the
        specified qualifier experiences an addition in ancestry.

        :param qualifier_id: the ``Id`` of the qualifier to monitor
        :type qualifier_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_qualifier_descendants(self, qualifier_id):
        """Registers for notification if a descendant is added to fthe specified qualifier in the qualifier hierarchy.
        ``QualifierReceiver.newQualifierDescendant()`` is invoked when
        the specified qualifier experiences an addition in descdendants.

        :param qualifier_id: the ``Id`` of the qualifier to monitor
        :type qualifier_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_qualifiers(self):
        """Registers for notification of updated qualifiers.
        ``QualifierReceiver.changedQualifier()`` is invoked when a
        qualifier is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_qualifier(self, qualifier_id):
        """Registers for notification of an updated qualifier.
        ``QualifierReceiver.changedQualifier()`` is invoked when the
        specified qualifier is changed.

        :param qualifier_id: the ``Id`` of the ``Qualifier`` to monitor
        :type qualifier_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_qualifiers(self):
        """Registers for notification of deleted qualifiers.
        ``QualifierReceiver.deletedQualifier()`` is invoked when a
        qualifier is removed from this vault.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_qualifier(self, qualifier_id):
        """Registers for notification of a deleted qualifier.
        ``QualifierReceiver.deletedQualifier()`` is invoked when the
        specified qualifier is removed from this vault.

        :param qualifier_id: the ``Id`` of the ``Qualifier`` to monitor
        :type qualifier_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_qualifier_ancestors(self, qualifier_id):
        """Registers for notification if an ancestor is removed from the specified qualifier in the qualifier hierarchy.
        ``QualifierReceiver.deletedQualifierAncestor()`` is invoked when
        the specified qualifier experiences a removal of an ancestor.

        :param qualifier_id: the ``Id`` of the qualifier to monitor
        :type qualifier_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_qualifier_descendants(self, qualifier_id):
        """Registers for notification if a descendant is removed from fthe specified qualifier in the qualifier hierarchy.
        ``QualifierReceiver.deletedQualifierDescednant()`` is invoked
        when the specified qualifier experiences a removal of one of its
        descendants.

        :param qualifier_id: the ``Id`` of the qualifier to monitor
        :type qualifier_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.QualifierHierarchySession

    def get_qualifier_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    qualifier_hierarchy_id = property(fget=get_qualifier_hierarchy_id)

    def get_qualifier_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    qualifier_hierarchy = property(fget=get_qualifier_hierarchy)

    def can_access_qualifier_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_qualifier_ids(self):
        """Gets the root qualifier ``Ids`` in this hierarchy.

        :return: the root qualifier ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_qualifier_ids = property(fget=get_root_qualifier_ids)

    def get_root_qualifiers(self):
        """Gets the root qualifiers in this qualifier hierarchy.

        :return: the root qualifiers
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_qualifiers = property(fget=get_root_qualifiers)

    def has_parent_qualifiers(self, qualifier_id):
        """Tests if the ``Qualifier`` has any parents.

        :param qualifier_id: a qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :return: ``true`` if the qualifier has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_qualifier(self, id_, qualifier_id):
        """Tests if an ``Id`` is a direct parent of qualifier.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``qualifier_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_qualifier_ids(self, qualifier_id):
        """Gets the parent ``Ids`` of the given qualifier.

        :param qualifier_id: a qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the qualifier
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_qualifiers(self, qualifier_id):
        """Gets the parents of the given qualifier.

        :param qualifier_id: a qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :return: the parents of the qualifier
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_qualifier(self, id_, qualifier_id):
        """Tests if an ``Id`` is an ancestor of a qualifier.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``qualifier_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``qualifier_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_qualifiers(self, qualifier_id):
        """Tests if a qualifier has any children.

        :param qualifier_id: a qualifier ``Id``
        :type qualifier_id: ``osid.id.Id``
        :return: ``true`` if the ``qualifier_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``qualifier_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_qualifier(self, id_, qualifier_id):
        """Tests if a node is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``qualifier_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``qualifier_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_qualifier_ids(self, qualifier_id):
        """Gets the child ``Ids`` of the given qualifier.

        :param qualifier_id: the ``Id`` to query
        :type qualifier_id: ``osid.id.Id``
        :return: the children of the qualifier
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_qualifiers(self, qualifier_id):
        """Gets the children of the given qualifier.

        :param qualifier_id: the ``Id`` to query
        :type qualifier_id: ``osid.id.Id``
        :return: the children of the qualifier
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_qualifier(self, id_, qualifier_id):
        """Tests if an ``Id`` is a descendant of a qualifier.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``qualifier_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``qualifier_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_qualifier_node_ids(self, qualifier_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given qualifier.

        :param qualifier_id: the ``Id`` to query
        :type qualifier_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a qualifier node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``function_id`` is not found
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_qualifier_nodes(self, qualifier_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given qualifier.

        :param qualifier_id: the ``Id`` to query
        :type qualifier_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a qualifier node
        :rtype: ``osid.authorization.QualifierNode``
        :raise: ``NotFound`` -- ``function_id`` is not found
        :raise: ``NullArgument`` -- ``function_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.QualifierHierarchyDesignSession

    def can_modify_qualifier_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_qualifier(self, qualifier_id):
        """Adds a root qualifier.

        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``qualifier_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``qualifier_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_qualifier(self, qualifier_id):
        """Removes a root qualifier from this hierarchy.

        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``qualifier_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_qualifier(self, qualifier_id, child_id):
        """Adds a child to a qualifier.

        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``qualifier_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``qualifier_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_qualifier(self, qualifier_id, child_id):
        """Removes a child from a qualifier.

        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``qualifier_id`` not parent of ``child_id``
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_qualifiers(self, qualifier_id):
        """Removes all children from a qualifier.

        :param qualifier_id: the ``Id`` of a qualifier
        :type qualifier_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``qualifier_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.QualifierVaultSession

    def can_lookup_qualifier_vault_mappings(self):
        """Tests if this user can perform lookups of qualifier/vault mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_qualifier_ids_by_vault(self, vault_id):
        """Gets the list of ``Qualifier``  ``Ids`` associated with a ``Vault``.

        :param vault_id: ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: list of related qualifier ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_qualifiers_by_vault(self, vault_id):
        """Gets the list of ``Qualifier`` associated with a ``Vault``.

        :param vault_id: ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: list of related qualifiers
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NotFound`` -- ``vault_id`` is not found
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_qualifier_ids_by_vaults(self, vault_ids):
        """Gets the list of ``Qualifier Ids`` corresponding to a list of ``Vaults``.

        :param vault_ids: list of vault ``Ids``
        :type vault_ids: ``osid.id.IdList``
        :return: list of vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_qualifiers_by_vaults(self, vault_ids):
        """Gets the list of ``Qualifiers`` corresponding to a list of ``Vaults``.

        :param vault_ids: list of vault ``Ids``
        :type vault_ids: ``osid.id.IdList``
        :return: list of qualifiers
        :rtype: ``osid.authorization.QualifierList``
        :raise: ``NullArgument`` -- ``vault_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_vault_ids_by_qualifier(self, qualifier_id):
        """Gets the list of ``Vault``  ``Ids`` mapped to a ``Qualifier``.

        :param qualifier_id: ``Id`` of a ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :return: list of vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_vaults_by_qualifier(self, qualifier_id):
        """Gets the list of ``Vaults`` mapped to a ``Qualifier``.

        :param qualifier_id: ``Id`` of a ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :return: list of vaults
        :rtype: ``osid.authorization.VaultList``
        :raise: ``NotFound`` -- ``qualifier_id`` is not found
        :raise: ``NullArgument`` -- ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.QualifierVaultAssignmentSession

    def can_assign_qualifiers(self):
        """Tests if this user can alter qualifier/vault mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_qualifiers_to_vault(self, vault_id):
        """Tests if this user can alter qualifier/vault mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``vault_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_vault_ids_for_qualifier(self, vault_id, qualifier_id):
        """Gets a list of vault including and under the given vault node in which a specific qualifier can be assigned.

        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :param qualifier_id: the ``Id`` of the ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :return: list of assignable vault ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``vault_id`` or ``qualifier_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_qualifier_to_vault(self, qualifier_id, vault_id):
        """Adds an existing ``Qualifier`` to a ``Vault``.

        :param qualifier_id: the ``Id`` of the ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``qualifier_id`` is already assigned to ``vault_id``
        :raise: ``NotFound`` -- ``qualifier_id`` or ``vault_id`` not found
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_qualifier_from_vault(self, qualifier_id, vault_id):
        """Removes a ``Qualifier`` from a ``Vault``.

        :param qualifier_id: the ``Id`` of the ``Qualifier``
        :type qualifier_id: ``osid.id.Id``
        :param vault_id: the ``Id`` of the ``Vault``
        :type vault_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``qualifier_id`` or ``vault_id`` not found or ``qualifier_id`` not assigned to ``vault_id``
        :raise: ``NullArgument`` -- ``qualifier_id`` or ``vault_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authorization.QualifierSmartVaultSession

    def apply_qualifier_query(self, qualifier_query):
        """Applies a qualifier query to this vault.

        :param qualifier_query: the qualifier query
        :type qualifier_query: ``osid.authorization.QualifierQuery``
        :raise: ``NullArgument`` -- ``qualifier_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``qualifier_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_qualifier_query(self):
        """Gets a qualifier query inspector for this vault.

        :return: the qualifier query inspector
        :rtype: ``osid.authorization.QualifierQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_qualifier_sequencing(self, qualifier_search_order):
        """Applies a qualifier search order to this vault.

        :param qualifier_search_order: the qualifier search order
        :type qualifier_search_order: ``osid.authorization.QualifierSearchOrder``
        :raise: ``NullArgument`` -- ``qualifier_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``qualifier_search_order`` not of this service

        """
        raise UNIMPLEMENTED()



class VaultList(osid_objects.OsidList):

    def get_next_vault(self):
        """Gets the next ``Vault`` in this list.

        :return: the next ``Vault`` in this list. The ``has_next()`` method should be used to test that a next ``Vault`` is available before calling this method.
        :rtype: ``osid.authorization.Vault``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    next_vault = property(fget=get_next_vault)

    def get_next_vaults(self, n):
        """Gets the next set of ``Vault`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Vault`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Vault`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.authorization.Vault``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()



class Vaults(AuthorizationManager):
    pass


