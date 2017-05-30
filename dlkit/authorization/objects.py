
from ..osid import objects as osid_objects
from ..osid import sessions as osid_sessions


class Authorization(osid_objects.OsidRelationship):
    """An Authorization is a mapping among an actor, a ``Function`` and a ``Qualifier``.

    This interface is not required for performing authorization checks
    but is used for examining and managing authorizations.

    The actor of an authorization may be specified in a variety of
    forms.

      * ``Agent``
      * ``Resource:`` the authorization provider uses all the ``Agents``
        associated with a ``Resource`` for matching authorizations
      * ``Resource`` and ``Trust:`` the authorization provider uses the
        associated ``Agents`` within a cicle of ``Trust``


    An explicit ``Authorization`` represents the mappings as they are
    specified in the authorization provdier. Implicit authorizations may
    be retrieved which are authorizations inferred through the
    ``Function`` or ``Qualifier`` hierarchies. An implicit
    ``Authorization`` is one where ``is_implicit()`` is true and should
    not be used for modification as it is only available for auditing
    purposes.

    An ``Authorization`` containing a ``Resource`` may also provide the
    associated Agent in a request for implicit authorizations or for all
    the authorizations, both explicit and implicit, for a given
    ``Agent``.

    """

    def is_implicit(self):
        """Tests if this authorization is implicit.

        :return: ``true`` if this authorization is implicit, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def has_resource(self):
        """Tests if this authorization has a ``Resource``.

        :return: ``true`` if this authorization has a ``Resource,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_resource_id(self):
        """Gets the ``resource _id`` for this authorization.

        :return: the ``Resource Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_resource()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    resource_id = property(fget=get_resource_id)

    def get_resource(self):
        """Gets the ``Resource`` for this authorization.

        :return: the ``Resource``
        :rtype: ``osid.resource.Resource``
        :raise: ``IllegalState`` -- ``has_resource()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Resource

    resource = property(fget=get_resource)

    def has_trust(self):
        """Tests if this authorization has a ``Trust``.

        :return: ``true`` if this authorization has a ``Trust,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_trust_id(self):
        """Gets the ``Trust``  ``Id`` for this authorization.

        :return: the trust ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_trust()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    trust_id = property(fget=get_trust_id)

    def get_trust(self):
        """Gets the ``Trust`` for this authorization.

        :return: the ``Trust``
        :rtype: ``osid.authentication.process.Trust``
        :raise: ``IllegalState`` -- ``has_trust()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.process.Trust

    trust = property(fget=get_trust)

    def has_agent(self):
        """Tests if this authorization has an ``Agent``.

        An implied authorization may have an ``Agent`` in addition to a
        specified ``Resource``.

        :return: ``true`` if this authorization has an ``Agent,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_agent_id(self):
        """Gets the ``Agent Id`` for this authorization.

        :return: the ``Agent Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_agent()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    agent_id = property(fget=get_agent_id)

    def get_agent(self):
        """Gets the ``Agent`` for this authorization.

        :return: the ``Agent``
        :rtype: ``osid.authentication.Agent``
        :raise: ``IllegalState`` -- ``has_agent()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.Agent

    agent = property(fget=get_agent)

    def get_function_id(self):
        """Gets the ``Function Id`` for this authorization.

        :return: the function ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    function_id = property(fget=get_function_id)

    def get_function(self):
        """Gets the ``Function`` for this authorization.

        :return: the function
        :rtype: ``osid.authorization.Function``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.Function

    function = property(fget=get_function)

    def get_qualifier_id(self):
        """Gets the ``Qualifier Id`` for this authorization.

        :return: the qualifier ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    qualifier_id = property(fget=get_qualifier_id)

    def get_qualifier(self):
        """Gets the qualifier for this authorization.

        :return: the qualifier
        :rtype: ``osid.authorization.Qualifier``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.Qualifier

    qualifier = property(fget=get_qualifier)

    def get_authorization_record(self, authorization_record_type):
        """Gets the authorization record corresponding to the given ``Authorization`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``authorization_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(authorization_record_type)`` is ``true`` .

        :param authorization_record_type: the type of the record to retrieve
        :type authorization_record_type: ``osid.type.Type``
        :return: the authorization record
        :rtype: ``osid.authorization.records.AuthorizationRecord``
        :raise: ``NullArgument`` -- ``authorization_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(authorization_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.records.AuthorizationRecord


class AuthorizationForm(osid_objects.OsidRelationshipForm):
    """This is the form for creating and updating ``Authorizations``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AuthorizationAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.

    """

    def get_authorization_form_record(self, authorization_record_type):
        """Gets the ``AuthorizationFormRecord`` corresponding to the given authorization record ``Type``.

        :param authorization_record_type: the authorization record type
        :type authorization_record_type: ``osid.type.Type``
        :return: the authorization form record
        :rtype: ``osid.authorization.records.AuthorizationFormRecord``
        :raise: ``NullArgument`` -- ``authorization_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(authorization_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.records.AuthorizationFormRecord


class AuthorizationList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``AuthorizationList`` provides a means for accessing ``Authorization`` elements sequentially either one at a time or many at a time.

    Examples: while (al.hasNext()) { Authorization authorization =
    al.getNextAuthorization(); }

    or
      while (al.hasNext()) {
           Authorization[] authorizations = al.getNextAuthorizations(al.available());
      }

    """

    def get_next_authorization(self):
        """Gets the next ``Authorization`` in this list.

        :return: the next ``Authorization`` in this list. The ``has_next()`` method should be used to test that a next ``Authorization`` is available before calling this method.
        :rtype: ``osid.authorization.Authorization``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.Authorization

    next_authorization = property(fget=get_next_authorization)

    def get_next_authorizations(self, n):
        """Gets the next set of ``Authorization`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Authorization`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Authorization`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.authorization.Authorization``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.Authorization


class Vault(osid_objects.OsidCatalog, osid_sessions.OsidSession):
    """A vault defines a collection of authorizations and functions."""

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


class VaultForm(osid_objects.OsidCatalogForm):
    """This is the form for creating and updating vaults.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``VaultAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """

    def get_vault_form_record(self, vault_record_type):
        """Gets the ``VaultFormRecord`` corresponding to the given vault record ``Type``.

        :param vault_record_type: a vault record type
        :type vault_record_type: ``osid.type.Type``
        :return: the vault form record
        :rtype: ``osid.authorization.records.VaultFormRecord``
        :raise: ``NullArgument`` -- ``vault_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(vault_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.records.VaultFormRecord


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


class VaultNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``VaultHierarchySession``.

    """

    def get_vault(self):
        """Gets the ``Vault`` at this node.

        :return: the vault represented by this node
        :rtype: ``osid.authorization.Vault``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.Vault

    vault = property(fget=get_vault)

    def get_parent_vault_nodes(self):
        """Gets the parents of this vault.

        :return: the parents of this vault
        :rtype: ``osid.authorization.VaultNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultNodeList

    parent_vault_nodes = property(fget=get_parent_vault_nodes)

    def get_child_vault_nodes(self):
        """Gets the children of this vault.

        :return: the children of this vault
        :rtype: ``osid.authorization.VaultNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultNodeList

    child_vault_nodes = property(fget=get_child_vault_nodes)


class VaultNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``VaultNodeList`` provides a means for accessing ``VaultNode`` elements sequentially either one at a time or many at a time.

    Examples: while (vnl.hasNext()) { VaultNode node =
    vnl.getNextVaultNode(); }

    or
      while (vnl.hasNext()) {
           VaultNode[] nodes = vnl.getNextVaultNodes(vnl.available());
      }

    """

    def get_next_vault_node(self):
        """Gets the next ``VaultNode`` in this list.

        :return: the next ``VaultNode`` in this list. The ``has_next()`` method should be used to test that a next ``VaultNode`` is available before calling this method.
        :rtype: ``osid.authorization.VaultNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultNode

    next_vault_node = property(fget=get_next_vault_node)

    def get_next_vault_nodes(self, n):
        """Gets the next set of ``VaultNode`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``VaultNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``VaultNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.authorization.VaultNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authorization.VaultNode


