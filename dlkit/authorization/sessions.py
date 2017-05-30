
from ..osid import sessions as osid_sessions


class AuthorizationSession(osid_sessions.OsidSession):
    """This is the basic session for verifying authorizations."""

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


class AuthorizationLookupSession(osid_sessions.OsidSession):
    """This session defines methods to search and retrieve ``Authorization`` mappings."""

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


class AuthorizationQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching ``Authorization`` objects.

    The search query is constructed using the ``AuthorizationQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated view: searches include authorizations in ``Vaults`` of
        which this vault is a ancestor in the vault hierarchy
      * isolated view: searches are restricted to authorizations in this
        ``Vault``
      * implicit authorization view: authorizations include implicit
        authorizations
      * explicit authorization view: only explicit authorizations are
        returned

    """

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


class AuthorizationAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Authorizations``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create an
    ``Authorization,`` an ``AuthorizationForm`` is requested using
    ``get_authorization_form_for_create()`` specifying the desired
    relationship peers and record ``Types`` or none if no record
    ``Types`` are needed. The returned ``AuthorizationForm`` will
    indicate that it is to be used with a create operation and can be
    used to examine metdata or validate data prior to creation. Once the
    ``AuthorizationForm`` is submiited to a create operation, it cannot
    be reused with another create operation unless the first operation
    was unsuccessful. Each ``AuthorizationForm`` corresponds to an
    attempted transaction.

    For updates, ``AuthorizationForms`` are requested to the
    ``Authorization``  ``Id`` that is to be updated using
    ``getAuthorizationFormForUpdate()``. Similarly, the
    ``AuthorizationForm`` has metadata about the data that can be
    updated and it can perform validation before submitting the update.
    The ``AuthorizationForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``Authorizations``. To unmap an
    ``Authorization`` from the current ``Vault,`` the
    ``AuthorizationVaultAssignmentSession`` should be used. These delete
    operations attempt to remove the ``Authorization`` itself thus
    removing it from all known ``Vault`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """

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


class VaultLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Vault`` objects.

    The ``Vault`` represents a collection of ``Functions`` and
    ``Authorizations``.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Vaults`` it can access, without breaking execution.
    However, an administrative application may require all ``Vault``
    elements to be available.

    Vaults may have an additional records indicated by their respective
    record types. The record may not be accessed through a cast of the
    ``Vault``.

    """

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


class VaultQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among ``Vault`` objects.

    The search query is constructed using the ``VaultQuery``.

    Vaults may have a query record indicated by their respective record
    types. The query record is accessed via the ``VaultQuery``.

    """

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


class VaultAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Vaults``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Vault,`` a ``VaultForm`` is requested using
    ``get_vault_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``VaultForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``VaultForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``VaultForm`` corresponds
    to an attempted transaction.

    For updates, ``VaultForms`` are requested to the ``Vault``  ``Id``
    that is to be updated using ``getVaultFormForUpdate()``. Similarly,
    the ``VaultForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``VaultForm`` can only be used once for a successful update and
    cannot be reused.

    The delete operations delete ``Vaults``. It is safer to remove all
    mappings to the ``Vault`` catalogs before deletion.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """

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


