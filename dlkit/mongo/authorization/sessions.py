"""Mongodb implementations of authorization sessions."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package mongo package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification



from bson.objectid import ObjectId


from . import objects
from .. import utilities
from ...abstract_osid.authorization import sessions as abc_authorization_sessions
from ...abstract_osid.authorization.objects import AuthorizationForm as ABCAuthorizationForm
from ...abstract_osid.authorization.objects import VaultForm as ABCVaultForm
from ...abstract_osid.id.primitives import Id as ABCId
from ...abstract_osid.type.primitives import Type as ABCType
from ..osid.sessions import OsidSession
from ..primitives import DateTime
from ..primitives import Id
from ..primitives import Type
from ..utilities import MongoClientValidated
from ..utilities import overlap
from dlkit.abstract_osid.id.primitives import Id as ABCId
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.type.primitives import Type as ABCType
from dlkit.mongo.osid import sessions as osid_sessions


DESCENDING = -1
ASCENDING = 1
CREATED = True
UPDATED = True
ENCLOSURE_RECORD_TYPE = Type(
    identifier='enclosure',
    namespace='osid-object',
    authority='ODL.MIT.EDU')
COMPARATIVE = 0
PLENARY = 1




class AuthorizationSession(abc_authorization_sessions.AuthorizationSession, osid_sessions.OsidSession):
    """This is the basic session for verifying authorizations."""


    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        self._catalog_class = objects.Vault
        self._session_name = 'AuthorizationSession'
        self._catalog_name = 'Vault'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='authorization',
            cat_name='Vault',
            cat_class=objects.Vault)
        self._kwargs = kwargs


    def _get_qualifier_idstrs(self, qualifier_id):
        try:
            authority = qualifier_id.get_identifier_namespace().split('.')[0].upper()
            identifier = qualifier_id.get_identifier_namespace().split('.')[1].upper()
        except:
            return [str(qualifier_id)]
        root_qualifier_id = Id(
            authority=qualifier_id.get_authority(),
            namespace=qualifier_id.get_identifier_namespace(),
            identifier='ROOT')
        if qualifier_id.get_identifier() == 'ROOT':
            return [str(root_qualifier_id)]
        hierarchy_mgr = self._get_provider_manager('HIERARCHY') # local=True ???
        hierarchy_session = hierarchy_mgr.get_hierarchy_traversal_session_for_hierarchy(
            Id(authority=authority,
               namespace='CATALOG',
               identifier=identifier))
        node = hierarchy_session.get_nodes(qualifier_id, 10, 0, False)
        return self._get_ancestor_idstrs(node) + [str(root_qualifier_id)]


    def _get_ancestor_idstrs(self, node):
        node_list = [str(node.get_id())]
        if node.has_parents():
            for parent_node in node.get_parents():
                node_list = node_list + self._get_ancestor_idstrs(parent_node)
        return node_list


    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.


        return: (osid.id.Id) - the ``Vault Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        """Gets the ``Vault`` associated with this session.


        return: (osid.authorization.Vault) - the ``Vault`` associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    vault = property(fget=get_vault)

    def can_access_authorizations(self):
        """Tests if this user can perform authorization checks.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.


        return: (boolean) - ``false`` if authorization methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*


        """
        return True

    @utilities.arguments_not_none
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


        arg:    agent_id (osid.id.Id): the ``Id`` of an ``Agent``
        arg:    function_id (osid.id.Id): the ``Id`` of a ``Function``
        arg:    qualifier_id (osid.id.Id): the ``Id`` of a ``Qualifier``
        return: (boolean) - ``true`` if the user is authorized,
                ``false`` othersise
        raise:  NotFound - ``function_id`` is not found
        raise:  NullArgument - ``agent_id`` , ``function_id`` or
                ``qualifier_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure making request
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
        collection = MongoClientValidated('authorization',
                                          collection='Authorization',
                                          runtime=self._runtime)
        # NOTE: For now this only checks basic authorizations. It should
        # to be extended to deal with Resources and QualifierHierarchies
        #print 'AGENT ID=', str(agent_id)
        #print '    FUNCTION ID=', str(function_id)
        #print '    QUAL ID STRINGS=', self._get_qualifier_idstrs(qualifier_id)
        try:
            collection.find_one(
                {'agentId': str(agent_id),
                 'functionId': str(function_id),
                 'qualifierId': {'$in': self._get_qualifier_idstrs(qualifier_id)}})
        except errors.NotFound:
            return False
        else:
            return True

    @utilities.arguments_not_none
    def get_authorization_condition(self, function_id):
        """Gets the ``AuthorizationCondition`` for making conditional authorization checks.


        arg:    function_id (osid.id.Id): the ``Id`` of a ``Function``
        return: (osid.authorization.AuthorizationCondition) - an
                authorization condition
        raise:  NotFound - ``function_id`` is not found
        raise:  NullArgument - ``function_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure making request
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
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


        arg:    agent_id (osid.id.Id): the ``Id`` of an ``Agent``
        arg:    function_id (osid.id.Id): the ``Id`` of a ``Function``
        arg:    qualifier_id (osid.id.Id): the ``Id`` of a ``Qualifier``
        arg:    condition (osid.authorization.AuthorizationCondition):
                an authorization condition
        return: (boolean) - ``true`` if the user is authorized,
                ``false`` othersise
        raise:  NotFound - ``function_id`` is not found
        raise:  NullArgument - ``agent_id`` , ``function_id,
                qualifier_id`` , or ``condition`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure making request
        raise:  Unsupported - ``condition`` is not of this service
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
        raise errors.Unimplemented()


class AuthorizationLookupSession(abc_authorization_sessions.AuthorizationLookupSession, osid_sessions.OsidSession):
    """This session defines methods to search and retrieve ``Authorization`` mappings."""


    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Vault
        self._session_name = 'AuthorizationLookupSession'
        self._catalog_name = 'Vault'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='authorization',
            cat_name='Vault',
            cat_class=objects.Vault)
        self._kwargs = kwargs
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.


        return: (osid.id.Id) - the ``Vault Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        """Gets the ``Vault`` associated with this session.


        return: (osid.authorization.Vault) - the ``Vault`` associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    vault = property(fget=get_vault)

    def can_lookup_authorizations(self):
        """Tests if this user can perform authorization lookups.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.


        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.can_lookup_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_authorization_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


        This view is used when greater interoperability is desired at
        the expense of precision.


        *compliance: mandatory -- This method is must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_authorization_view(self):
        """A complete view of the ``Authorization`` returns is desired.


        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.


        *compliance: mandatory -- This method is must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_vault_view(self):
        """Federates the view for methods in this session.


        A federated view will include authorizations in vaults which are
        children of this vault in the vault hierarchy.


        *compliance: mandatory -- This method is must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_vault_view(self):
        """Isolates the view for methods in this session.


        An isolated view restricts lookups to this vault only.


        *compliance: mandatory -- This method is must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def use_effective_authorization_view(self):
        """Only authorizations whose effective dates are current are returned by methods in this session.


        *compliance: mandatory -- This method is must be implemented.*


        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.use_effective_relationship_view
        self._use_effective_view()

    def use_any_effective_authorization_view(self):
        """All authorizations of any effective dates are returned by all methods in this session.


        *compliance: mandatory -- This method is must be implemented.*


        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.use_any_effective_relationship_view
        self._use_any_effective_view()

    def use_implicit_authorization_view(self):
        """Sets the view for methods in this session to implicit authorizations.


        An implicit view will include authorizations derived from other
        authorizations as a result of the ``Qualifier,`` ``Function`` or
        ``Resource`` hierarchies. This method is the opposite of
        ``explicitAuthorizationView()``.


        *compliance: mandatory -- This method is must be implemented.*


        """
        raise errors.Unimplemented()

    def use_explicit_authorization_view(self):
        """Sets the view for methods in this session to explicit authorizations.


        An explicit view includes only those authorizations that were
        explicitly defined and not implied. This method is the opposite
        of ``implicitAuthorizationView()``.


        *compliance: mandatory -- This method is must be implemented.*


        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_authorization(self, authorization_id):
        """Gets the ``Authorization`` specified by its ``Id``.


        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Authorization`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``Authorization`` and
        retained for compatibility.


        arg:    authorization_id (osid.id.Id): the ``Id`` of the
                ``Authorization`` to retrieve
        return: (osid.authorization.Authorization) - the returned
                ``Authorization``
        raise:  NotFound - no ``Authorization`` found with the given
                ``Id``
        raise:  NullArgument - ``authorization_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        collection = MongoClientValidated('authorization',
                                          collection='Authorization',
                                          runtime=self._runtime)
        result = collection.find_one(
            dict({'_id': ObjectId(self._get_id(authorization_id, 'authorization').get_identifier())},
                 **self._view_filter()))
        return objects.Authorization(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_authorizations_by_ids(self, authorization_ids):
        """Gets an ``AuthorizationList`` corresponding to the given ``IdList``.


        In plenary mode, the returned list contains all of the
        authorizations specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Authorizations`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.


        arg:    authorization_ids (osid.id.IdList): the list of ``Ids``
                to retrieve
        return: (osid.authorization.AuthorizationList) - the returned
                ``Authorization list``
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``authorization_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        collection = MongoClientValidated('authorization',
                                          collection='Authorization',
                                          runtime=self._runtime)
        object_id_list = []
        for i in authorization_ids:
            object_id_list.append(ObjectId(self._get_id(i, 'authorization').get_identifier()))
        result = collection.find(
            dict({'_id': {'$in': object_id_list}},
                 **self._view_filter()))
        result = list(result)
        sorted_result = []
        for object_id in object_id_list:
            for object_map in result:
                if object_map['_id'] == object_id:
                    sorted_result.append(object_map)
                    break
        return objects.AuthorizationList(sorted_result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_authorizations_by_genus_type(self, authorization_genus_type):
        """Gets an ``AuthorizationList`` corresponding to the given authorization genus ``Type`` which does not include
            authorizations of genus types derived from the specified ``Type``.


        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.


        arg:    authorization_genus_type (osid.type.Type): an
                authorization genus type
        return: (osid.authorization.AuthorizationList) - the returned
                ``Authorization`` list
        raise:  NullArgument - ``authorization_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        collection = MongoClientValidated('authorization',
                                          collection='Authorization',
                                          runtime=self._runtime)
        result = collection.find(
            dict({'genusTypeId': str(authorization_genus_type)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.AuthorizationList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_authorizations_by_parent_genus_type(self, authorization_genus_type):
        """Gets an ``AuthorizationList`` corresponding to the given authorization genus ``Type`` and include
            authorizations of genus types derived from the specified ``Type``.


        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.


        arg:    authorization_genus_type (osid.type.Type): an
                authorization genus type
        return: (osid.authorization.AuthorizationList) - the returned
                ``Authorization`` list
        raise:  NullArgument - ``authorization_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        return objects.AuthorizationList([])

    @utilities.arguments_not_none
    def get_authorizations_by_record_type(self, authorization_record_type):
        """Gets an ``AuthorizationList`` containing the given authorization record ``Type``.


        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.


        arg:    authorization_record_type (osid.type.Type): an
                authorization record type
        return: (osid.authorization.AuthorizationList) - the returned
                ``Authorization`` list
        raise:  NullArgument - ``authorization_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.AuthorizationList([])

    @utilities.arguments_not_none
    def get_authorizations_on_date(self, from_, to):
        """Gets an ``AuthorizationList`` effective during the entire given date range inclusive but not confined to the
            date range.


        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.authorization.AuthorizationList) - the returned
                ``Authorization`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``from`` or ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_on_date
        authorization_list = []
        for authorization in self.get_authorizations():
            if overlap(from_, to, authorization.start_date, authorization.end_date):
                authorization_list.append(authorization)
        return objects.AuthorizationList(authorization_list, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_authorizations_for_resource(self, resource_id):
        """Gets a list of ``Authorizations`` associated with a given resource.


        Authorizations related to the given resource, including those
        related through an ``Agent,`` are returned. In plenary mode, the
        returned list contains all known authorizations or an error
        results. Otherwise, the returned list may contain only those
        authorizations that are accessible through this session.


        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.authorization.AuthorizationList) - the returned
                ``Authorization list``
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_authorizations_for_resource_on_date(self, resource_id, from_, to):
        """Gets an ``AuthorizationList`` effective during the entire given date range inclusive but not confined to the
            date range.


        Authorizations related to the given resource, including those
        related through an ``Agent,`` are returned.


        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.


        In effective mode, authorizations are returned that are
        currently effective. In any effective mode, active
        authorizations and those currently expired are returned.


        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.authorization.AuthorizationList) - the returned
                ``Authorization`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``resource_id, from`` or ``to`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_authorizations_for_agent(self, agent_id):
        """Gets a list of ``Authorizations`` associated with a given agent.


        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.


        arg:    agent_id (osid.id.Id): an agent ``Id``
        return: (osid.authorization.AuthorizationList) - the returned
                ``Authorization list``
        raise:  NullArgument - ``agent_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_authorizations_for_agent_on_date(self, agent_id, from_, to):
        """Gets an ``AuthorizationList`` for the given agent and effective during the entire given date range inclusive
            but not confined to the date range.


        arg:    agent_id (osid.id.Id): an agent ``Id``
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.authorization.AuthorizationList) - the returned
                ``Authorization`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``agent_id, from`` or ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_authorizations_for_function(self, function_id):
        """Gets a list of ``Authorizations`` associated with a given function.


        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.


        arg:    function_id (osid.id.Id): a function ``Id``
        return: (osid.authorization.AuthorizationList) - the returned
                ``Authorization list``
        raise:  NullArgument - ``function_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.learning.ActivityLookupSession.get_activities_for_objective_template
        # NOTE: This implementation currently ignores plenary view
        collection = MongoClientValidated('authorization',
                                          collection='Authorization',
                                          runtime=self._runtime)
        result = collection.find(
            dict({'functionId': str(function_id)},
                 **self._view_filter()))
        return objects.AuthorizationList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_authorizations_for_function_on_date(self, function_id, from_, to):
        """Gets an ``AuthorizationList`` for the given function and effective during the entire given date range
            inclusive but not confined to the date range.


        arg:    function_id (osid.id.Id): a function ``Id``
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.authorization.AuthorizationList) - the returned
                ``Authorization`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``function_id, from`` or ``to`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_authorizations_for_resource_and_function(self, resource_id, function_id):
        """Gets a list of ``Authorizations`` associated with a given resource.


        Authorizations related to the given resource, including those
        related through an ``Agent,`` are returned. In plenary mode, the
        returned list contains all known authorizations or an error
        results. Otherwise, the returned list may contain only those
        authorizations that are accessible through this session.


        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    function_id (osid.id.Id): a function ``Id``
        return: (osid.authorization.AuthorizationList) - the returned
                ``Authorization list``
        raise:  NullArgument - ``resource_id`` or ``function_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_for_peers
        # NOTE: This implementation currently ignores plenary and effective views
        collection = MongoClientValidated('authorization',
                                          collection='Authorization',
                                          runtime=self._runtime)
        result = collection.find(
            dict({'sourceId': str(resource_id),
                  'destinationId': str(function_id)},
                 **self._view_filter())).sort('_sort_id', ASCENDING)
        return objects.AuthorizationList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_authorizations_for_resource_and_function_on_date(self, resource_id, function_id, from_, to):
        """Gets an ``AuthorizationList`` effective during the entire given date range inclusive but not confined to the
            date range.


        Authorizations related to the given resource, including those
        related through an ``Agent,`` are returned.


        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.


        In effective mode, authorizations are returned that are
        currently effective. In any effective mode, active
        authorizations and those currently expired are returned.


        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    function_id (osid.id.Id): a function ``Id``
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.authorization.AuthorizationList) - the returned
                ``Authorization`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``resource_id, function_id, from`` or
                ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_authorizations_for_agent_and_function(self, agent_id, function_id):
        """Gets a list of ``Authorizations`` associated with a given agent.


        Authorizations related to the given resource, including those
        related through an ``Agent,`` are returned. In plenary mode, the
        returned list contains all known authorizations or an error
        results. Otherwise, the returned list may contain only those
        authorizations that are accessible through this session.


        arg:    agent_id (osid.id.Id): an agent ``Id``
        arg:    function_id (osid.id.Id): a function ``Id``
        return: (osid.authorization.AuthorizationList) - the returned
                ``Authorization list``
        raise:  NullArgument - ``agent_id`` or ``function_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_for_peers
        # NOTE: This implementation currently ignores plenary and effective views
        collection = MongoClientValidated('authorization',
                                          collection='Authorization',
                                          runtime=self._runtime)
        result = collection.find(
            dict({'sourceId': str(agent_id),
                  'destinationId': str(function_id)},
                 **self._view_filter())).sort('_sort_id', ASCENDING)
        return objects.AuthorizationList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_authorizations_for_agent_and_function_on_date(self, agent_id, function_id, from_, to):
        """Gets an ``AuthorizationList`` for the given agent and effective during the entire given date range inclusive
            but not confined to the date range.


        arg:    agent_id (osid.id.Id): an agent ``Id``
        arg:    function_id (osid.id.Id): a function ``Id``
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.authorization.AuthorizationList) - the returned
                ``Authorization`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``agent_id, function_id, from`` or ``to``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_authorizations_by_qualifier(self, qualifier_id):
        """Gets a list of ``Authorizations`` associated with a given qualifier.


        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.


        arg:    qualifier_id (osid.id.Id): a qualifier ``Id``
        return: (osid.authorization.AuthorizationList) - the returned
                ``Authorization list``
        raise:  NullArgument - ``qualifier_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_explicit_authorization(self, authorization_id):
        """Gets the explicit ``Authorization`` that generated the given implicit authorization.


        If the given ``Authorization`` is explicit, then the same
        ``Authorization`` is returned.


        arg:    authorization_id (osid.id.Id): an authorization
        return: (osid.authorization.Authorization) - the explicit
                ``Authorization``
        raise:  NotFound - ``authorization_id`` is not found
        raise:  NullArgument - ``authorization_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    def get_authorizations(self):
        """Geta all ``Authorizations``.


        In plenary mode, the returned list contains all known
        authorizations or an error results. Otherwise, the returned list
        may contain only those authorizations that are accessible
        through this session.


        return: (osid.authorization.AuthorizationList) - a list of
                ``Authorizations``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        collection = MongoClientValidated('authorization',
                                          collection='Authorization',
                                          runtime=self._runtime)
        result = collection.find(self._view_filter()).sort('_id', DESCENDING)
        return objects.AuthorizationList(result, runtime=self._runtime)

    authorizations = property(fget=get_authorizations)


class AuthorizationAdminSession(abc_authorization_sessions.AuthorizationAdminSession, osid_sessions.OsidSession):
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


    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Vault
        self._session_name = 'AuthorizationAdminSession'
        self._catalog_name = 'Vault'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='authorization',
            cat_name='Vault',
            cat_class=objects.Vault)
        self._forms = dict()
        self._kwargs = kwargs
    def get_vault_id(self):
        """Gets the ``Vault``  ``Id`` associated with this session.


        return: (osid.id.Id) - the ``Vault Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        """Gets the ``Vault`` associated with this session.


        return: (osid.authorization.Vault) - the ``Vault`` associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    vault = property(fget=get_vault)

    def can_create_authorizations(self):
        """Tests if this user can create ``Authorizations``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer create
        operations to unauthorized users.


        return: (boolean) - ``false`` if ``Authorization`` creation is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_authorization_with_record_types(self, authorization_record_types):
        """Tests if this user can create a single ``Authorization`` using the desired record types.


        While ``AuthorizationManager.getAuthorizationRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``Authorization``. Providing an empty array tests if an
        ``Authorization`` can be created with no records.


        arg:    authorization_record_types (osid.type.Type[]): array of
                authorization record types
        return: (boolean) - ``true`` if ``Authorization`` creation using
                the specified ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``authorization_record_types`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_authorization_form_for_create_for_agent(self, agent_id, function_id, qualifier_id,
        authorization_record_types):
        """Gets the authorization form for creating new authorizations.


        A new form should be requested for each create transaction.


        arg:    agent_id (osid.id.Id): the agent ``Id``
        arg:    function_id (osid.id.Id): the function ``Id``
        arg:    qualifier_id (osid.id.Id): the qualifier ``Id``
        arg:    authorization_record_types (osid.type.Type[]): array of
                authorization record types
        return: (osid.authorization.AuthorizationForm) - the
                authorization form
        raise:  NotFound - ``agent_id, function_id`` or ``qualifier_id``
                is not found
        raise:  NullArgument - ``agent_id, function_id, qualifier_id``
                or ``authorization_record_types`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form with requested record
                types
        *compliance: mandatory -- This method must be implemented.*


        """
        if not isinstance(agent_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        if not isinstance(function_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        if not isinstance(qualifier_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        for arg in authorization_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if authorization_record_types == []:
            ## WHY are we passing vault_id = self._catalog_id below, seems redundant:
            obj_form = objects.AuthorizationForm(
                vault_id=self._catalog_id,
                agent_id=agent_id,
                function_id=function_id,
                qualifier_id=qualifier_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime)
        else:
            obj_form = objects.AuthorizationForm(
                vault_id=self._catalog_id,
                record_types=relationship_record_types,
                agent_id=agent_id,
                function_id=function_id,
                qualifier_id=qualifier_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime)
        obj_form._for_update = False
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def get_authorization_form_for_create_for_resource(self, resource_id, function_id, qualifier_id,
        authorization_record_types):
        """Gets the authorization form for creating new authorizations.


        A new form should be requested for each create transaction.


        arg:    resource_id (osid.id.Id): the resource ``Id``
        arg:    function_id (osid.id.Id): the function ``Id``
        arg:    qualifier_id (osid.id.Id): the qualifier ``Id``
        arg:    authorization_record_types (osid.type.Type[]): array of
                authorization record types
        return: (osid.authorization.AuthorizationForm) - the
                authorization form
        raise:  NotFound - ``resource_id, function_id`` or
                ``qualifier_id`` is not found
        raise:  NullArgument - ``resource_id, function_id,
                qualifier_id,`` or ``authorization_record_types`` is
                ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form with requested record
                types
        *compliance: mandatory -- This method must be implemented.*


        """
        if not isinstance(resource_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        if not isinstance(function_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        if not isinstance(qualifier_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        for arg in authorization_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if authorization_record_types == []:
            ## WHY are we passing vault_id = self._catalog_id below, seems redundant:
            obj_form = objects.AuthorizationForm(
                vault_id=self._catalog_id,
                resource_id=resource_id,
                function_id=function_id,
                qualifier_id=qualifier_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime)
        else:
            obj_form = objects.AuthorizationForm(
                vault_id=self._catalog_id,
                record_types=relationship_record_types,
                resource_id=resource_id,
                function_id=function_id,
                qualifier_id=qualifier_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime)
        obj_form._for_update = False
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def get_authorization_form_for_create_for_resource_and_trust(self, resource_id, trust_id, function_id, qualifier_id,
        authorization_record_types):
        """Gets the authorization form for creating new authorizations.


        A new form should be requested for each create transaction.


        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    trust_id (osid.id.Id): an ``Id`` for a circle of trust
        arg:    function_id (osid.id.Id): a function ``Id``
        arg:    qualifier_id (osid.id.Id): the qualifier ``Id``
        arg:    authorization_record_types (osid.type.Type[]): array of
                authorization record types
        return: (osid.authorization.AuthorizationForm) - the
                authorization form
        raise:  NotFound - ``resource_id, trust_id, function_id`` , or
                ``qualifierid`` is not found
        raise:  NullArgument - ``resource_id, trust_id`` ,
                ``resource_id, qualifier_id`` or
                ``authorization_record_types`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form with requested record
                types
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def create_authorization(self, authorization_form):
        """Creates a new explicit ``Authorization``.


        arg:    authorization_form
                (osid.authorization.AuthorizationForm): the
                authorization form
        return: (osid.authorization.Authorization) - ``t`` he new
                ``Authorization``
        raise:  IllegalState - ``authorization_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``authorization_form`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``authorization_form`` did not originate
                from this service
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.create_resource_template
        collection = MongoClientValidated('authorization',
                                          collection='Authorization',
                                          runtime=self._runtime)
        if not isinstance(authorization_form, ABCAuthorizationForm):
            raise errors.InvalidArgument('argument type is not an AuthorizationForm')
        if authorization_form.is_for_update():
            raise errors.InvalidArgument('the AuthorizationForm is for update only, not create')
        try:
            if self._forms[authorization_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('authorization_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('authorization_form did not originate from this session')
        if not authorization_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(authorization_form._my_map)


        self._forms[authorization_form.get_id().get_identifier()] = CREATED
        result = objects.Authorization(
            collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime)


        return result

    def can_update_authorizations(self):
        """Tests if this user can update ``Authorizations``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Authorization`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.


        return: (boolean) - ``false`` if authorization modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_authorization_form_for_update(self, authorization_id):
        """Gets the authorization form for updating an existing authorization.


        A new authorization form should be requested for each update
        transaction.


        arg:    authorization_id (osid.id.Id): the ``Id`` of the
                ``Authorization``
        return: (osid.authorization.AuthorizationForm) - the
                authorization form
        raise:  NotFound - ``authorization_id`` is not found
        raise:  NullArgument - ``authorization_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_update_template
        collection = MongoClientValidated('authorization',
                                          collection='Authorization',
                                          runtime=self._runtime)
        if not isinstance(authorization_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if authorization_id.get_identifier_namespace() != 'authorization.Authorization':
            if authorization_id.get_authority() != self._authority:
                raise errors.InvalidArgument()
            else:
                authorization_id = self._get_authorization_id_with_enclosure(authorization_id)
        result = collection.find_one({'_id': ObjectId(authorization_id.get_identifier())})


        obj_form = objects.AuthorizationForm(result, runtime=self._runtime)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED


        return obj_form


    def _get_authorization_id_with_enclosure(self, enclosure_id):
        """Create an Authorization with an enclosed foreign object.


        return: (osid.id.Id) - the id of the new Authorization


        """
        mgr = self._get_provider_manager('REPOSITORY')
        query_session = mgr.get_authorization_query_session_for_vault(self._catalog_id)
        query_form = query_session.get_authorization_query()
        query_form.match_enclosed_object_id(enclosure_id)
        query_result = query_session.get_authorizations_by_query(query_form)
        if query_result.available() > 0:
            authorization_id = query_result.next().get_id()
        else:
            create_form = self.get_authorization_form_for_create([ENCLOSURE_RECORD_TYPE])
            create_form.set_enclosed_object(enclosure_id)
            authorization_id = self.create_authorization(create_form).get_id()
        return authorization_id


    @utilities.arguments_not_none
    def duplicate_authorization(self, authorization_id):
        collection = MongoClientValidated('authorization',
                                          collection='Authorization',
                                          runtime=self._runtime)
        mgr = self._get_provider_manager('AUTHORIZATION')
        lookup_session = mgr.get_authorization_lookup_session()
        lookup_session.use_federated_vault_view()
        try:
            lookup_session.use_unsequestered_authorization_view()
        except AttributeError:
            pass
        authorization_map = dict(lookup_session.get_authorization(authorization_id)._my_map)
        del authorization_map['_id']
        if 'vaultId' in authorization_map:
            authorization_map['vaultId'] = str(self._catalog_id)
        if 'assignedVaultIds' in authorization_map:
            authorization_map['assignedVaultIds'] = [str(self._catalog_id)]
        insert_result = collection.insert_one(authorization_map)
        result = objects.Authorization(
            collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime)
        return result

    @utilities.arguments_not_none
    def update_authorization(self, authorization_form):
        """Updates an existing authorization.


        arg:    authorization_form
                (osid.authorization.AuthorizationForm): the
                authorization ``Id``
        raise:  IllegalState - ``authorization_form`` already used in an
                update transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``authorization_form`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``authorization_form`` did not originate
                from ``get_authorization_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.update_resource_template
        collection = MongoClientValidated('authorization',
                                          collection='Authorization',
                                          runtime=self._runtime)
        if not isinstance(authorization_form, ABCAuthorizationForm):
            raise errors.InvalidArgument('argument type is not an AuthorizationForm')
        if not authorization_form.is_for_update():
            raise errors.InvalidArgument('the AuthorizationForm is for update only, not create')
        try:
            if self._forms[authorization_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('authorization_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('authorization_form did not originate from this session')
        if not authorization_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(authorization_form._my_map)


        self._forms[authorization_form.get_id().get_identifier()] = UPDATED


        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.Authorization(
            authorization_form._my_map,
            runtime=self._runtime)

    def can_delete_authorizations(self):
        """Tests if this user can delete ``Authorizations``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Authorization`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.


        return: (boolean) - ``false`` if ``Authorization`` deletion is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_authorization(self, authorization_id):
        """Deletes the ``Authorization`` identified by the given ``Id``.


        arg:    authorization_id (osid.id.Id): the ``Id`` of the
                ``Authorization`` to delete
        raise:  NotFound - an ``Authorization`` was not found identified
                by the given ``Id``
        raise:  NullArgument - ``authorization_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.delete_resource_template
        collection = MongoClientValidated('authorization',
                                          collection='Authorization',
                                          runtime=self._runtime)
        if not isinstance(authorization_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        authorization_map = collection.find_one(
            dict({'_id': ObjectId(authorization_id.get_identifier())},
                 **self._view_filter()))


        objects.Authorization(authorization_map, runtime=self._runtime)._delete()
        collection.delete_one({'_id': ObjectId(authorization_id.get_identifier())})

    def can_manage_authorization_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Authorizations``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        return: (boolean) - ``false`` if ``Authorization`` aliasing is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def alias_authorization(self, authorization_id, alias_id):
        """Adds an ``Id`` to an ``Authorization`` for the purpose of creating compatibility.


        The primary ``Id`` of the ``Authorization`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another authorization. it
        is reassigned to the given authorization ``Id``.


        arg:    authorization_id (osid.id.Id): the ``Id`` of an
                ``Authorization``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``authorization_id`` not found
        raise:  NullArgument - ``authorization_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.alias_resources_template
        self._alias_id(primary_id=authorization_id, equivalent_id=alias_id)


class VaultLookupSession(abc_authorization_sessions.VaultLookupSession, osid_sessions.OsidSession):
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


    _session_name = 'VaultLookupSession'


    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_view = COMPARATIVE
        self._kwargs = kwargs
    def can_lookup_vaults(self):
        """Tests if this user can perform ``Vault`` lookups.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.


        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.can_lookup_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_vault_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


        This view is used when greater interoperability is desired at
        the expense of precision.


        *compliance: mandatory -- This method is must be implemented.*


        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_comparative_bin_view
        self._catalog_view = COMPARATIVE

    def use_plenary_vault_view(self):
        """A complete view of the ``Vault`` returns is desired.


        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.


        *compliance: mandatory -- This method is must be implemented.*


        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_plenary_bin_view
        self._catalog_view = PLENARY

    @utilities.arguments_not_none
    def get_vault(self, vault_id):
        """Gets the ``Vault`` specified by its ``Id``.


        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Vault`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Vault`` and retained for compatibility.


        arg:    vault_id (osid.id.Id): ``Id`` of the ``Vault``
        return: (osid.authorization.Vault) - the vault
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*


        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bin
        collection = MongoClientValidated('authorization',
                                          collection='Vault',
                                          runtime=self._runtime)
        # Need to consider how to best deal with the "phantom root" catalog issue
        if vault_id.get_identifier() == '000000000000000000000000':
            return self._get_phantom_root_catalog(cat_class=objects.Vault, cat_name='Vault')
        try:
            result = collection.find_one({'_id': ObjectId(vault_id.get_identifier())})
        except errors.NotFound:
            # Try creating an orchestrated Vault.  Let it raise errors.NotFound()
            result = self._create_orchestrated_cat(vault_id, 'authorization', 'Vault')


        return objects.Vault(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_vaults_by_ids(self, vault_ids):
        """Gets a ``VaultList`` corresponding to the given ``IdList``.


        In plenary mode, the returned list contains all of the vaults
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Vault`` objects may be omitted from the list and
        may present the elements in any order including returning a
        unique set.


        arg:    vault_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.authorization.VaultList) - the returned ``Vault``
                list
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``vault_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        # NOTE: This implementation currently ignores plenary view
        # Also, this should be implemented to use get_Vault() instead of direct to database
        catalog_id_list = []
        for i in vault_ids:
            catalog_id_list.append(ObjectId(i.get_identifier()))
        collection = MongoClientValidated('authorization',
                                          collection='Vault',
                                          runtime=self._runtime)
        result = collection.find({'_id': {'$in': catalog_id_list}}).sort('_id', DESCENDING)


        return objects.VaultList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_vaults_by_genus_type(self, vault_genus_type):
        """Gets a ``VaultList`` corresponding to the given vault genus ``Type`` which does not include vaults of types
            derived from the specified ``Type``.


        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.


        arg:    vault_genus_type (osid.type.Type): a vault genus type
        return: (osid.authorization.VaultList) - the returned ``Vault``
                list
        raise:  NullArgument - ``vault_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_vaults_by_parent_genus_type(self, vault_genus_type):
        """Gets a ``VaultList`` corresponding to the given vault genus ``Type`` and include any additional vaults with
            genus types derived from the specified ``Type``.


        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.


        arg:    vault_genus_type (osid.type.Type): a vault genus type
        return: (osid.authorization.VaultList) - the returned ``Vault``
                list
        raise:  NullArgument - ``vault_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_vaults_by_record_type(self, vault_record_type):
        """Gets a ``VaultList`` containing the given vault record ``Type``.


        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.


        arg:    vault_record_type (osid.type.Type): a vault record type
        return: (osid.authorization.VaultList) - the returned ``Vault``
                list
        raise:  NullArgument - ``vault_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_vaults_by_provider(self, resource_id):
        """Gets a ``VaultList`` from the given provider ````.


        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.


        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.authorization.VaultList) - the returned ``Vault``
                list
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    def get_vaults(self):
        """Gets all ``Vaults``.


        In plenary mode, the returned list contains all known vaults or
        an error results. Otherwise, the returned list may contain only
        those vaults that are accessible through this session.


        return: (osid.authorization.VaultList) - a ``VaultList``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_template
        # NOTE: This implementation currently ignores plenary view
        collection = MongoClientValidated('authorization',
                                          collection='Vault',
                                          runtime=self._runtime)
        result = collection.find().sort('_id', DESCENDING)


        return objects.VaultList(result, runtime=self._runtime)

    vaults = property(fget=get_vaults)


class VaultAdminSession(abc_authorization_sessions.VaultAdminSession, osid_sessions.OsidSession):
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


    _session_name = 'VaultAdminSession'


    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._forms = dict()
        self._kwargs = kwargs
    def can_create_vaults(self):
        """Tests if this user can create ``Vaults``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Vault``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.


        return: (boolean) - ``false`` if ``Vault`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_vault_with_record_types(self, vault_record_types):
        """Tests if this user can create a single ``Vault`` using the desired record types.


        While ``AuthorizationManager.getVaultRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Vault``.
        Providing an empty array tests if a ``Vault`` can be created
        with no records.


        arg:    vault_record_types (osid.type.Type[]): array of vault
                record types
        return: (boolean) - ``true`` if ``Vault`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        raise:  NullArgument - ``vault_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_vault_form_for_create(self, vault_record_types):
        """Gets the vault form for creating new vaults.


        A new form should be requested for each create transaction.


        arg:    vault_record_types (osid.type.Type[]): array of vault
                record types
        return: (osid.authorization.VaultForm) - the vault form
        raise:  NullArgument - ``vault_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form qith requested record
                types
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        for arg in vault_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if vault_record_types == []:
            result = objects.VaultForm(
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id())
        else:
            result = objects.VaultForm(
                record_types=vault_record_types,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id())
        self._forms[result.get_id().get_identifier()] = not CREATED
        return result

    @utilities.arguments_not_none
    def create_vault(self, vault_form):
        """Creates a new ``Vault``.


        arg:    vault_form (osid.authorization.VaultForm): the form for
                this ``Vault``
        return: (osid.authorization.Vault) - the new ``Vault``
        raise:  IllegalState - ``vault_form`` already used in a create
                transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``vault_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``vault_form`` did not originate from
                ``get_vault_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.BinAdminSession.create_bin_template
        collection = MongoClientValidated('authorization',
                                          collection='Vault',
                                          runtime=self._runtime)
        if not isinstance(vault_form, ABCVaultForm):
            raise errors.InvalidArgument('argument type is not an VaultForm')
        if vault_form.is_for_update():
            raise errors.InvalidArgument('the VaultForm is for update only, not create')
        try:
            if self._forms[vault_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('vault_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('vault_form did not originate from this session')
        if not vault_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(vault_form._my_map)


        self._forms[vault_form.get_id().get_identifier()] = CREATED
        result = objects.Vault(
            collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime)


        return result

    def can_update_vaults(self):
        """Tests if this user can update ``Vaults``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Vault``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.


        return: (boolean) - ``false`` if ``Vault`` modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_vault_form_for_update(self, vault_id):
        """Gets the vault form for updating an existing vault.


        A new vault form should be requested for each update
        transaction.


        arg:    vault_id (osid.id.Id): the ``Id`` of the ``Vault``
        return: (osid.authorization.VaultForm) - the vault form
        raise:  NotFound - ``vault_id`` is not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        collection = MongoClientValidated('authorization',
                                          collection='Vault',
                                          runtime=self._runtime)
        if not isinstance(vault_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        result = collection.find_one({'_id': ObjectId(vault_id.get_identifier())})


        cat_form = objects.VaultForm(result, runtime=self._runtime)
        self._forms[cat_form.get_id().get_identifier()] = not UPDATED


        return cat_form

    @utilities.arguments_not_none
    def update_vault(self, vault_form):
        """Updates an existing vault.


        arg:    vault_form (osid.authorization.VaultForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``vault_form`` already used in an update
                transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``vault_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``vault_form`` did not originate from
                ``get_vault_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.BinAdminSession.update_bin_template
        collection = MongoClientValidated('authorization',
                                          collection='Vault',
                                          runtime=self._runtime)
        if not isinstance(vault_form, ABCVaultForm):
            raise errors.InvalidArgument('argument type is not an VaultForm')
        if not vault_form.is_for_update():
            raise errors.InvalidArgument('the VaultForm is for update only, not create')
        try:
            if self._forms[vault_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('vault_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('vault_form did not originate from this session')
        if not vault_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(vault_form._my_map) # save is deprecated - change to replace_one


        self._forms[vault_form.get_id().get_identifier()] = UPDATED


        # Note: this is out of spec. The OSIDs don't require an object to be returned
        return objects.Vault(vault_form._my_map, runtime=self._runtime)

    def can_delete_vaults(self):
        """Tests if this user can delete vaults.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Vault``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.


        return: (boolean) - ``false`` if ``Vault`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_vault(self, vault_id):
        """Deletes a ``Vault``.


        arg:    vault_id (osid.id.Id): the ``Id`` of the ``Vault`` to
                remove
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.BinAdminSession.delete_bin_template
        collection = MongoClientValidated('authorization',
                                          collection='Vault',
                                          runtime=self._runtime)
        if not isinstance(vault_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        for object_catalog in ['Authorization', 'Function', 'Qualifier', 'Vault']:
            obj_collection = MongoClientValidated('authorization',
                                                  collection=object_catalog,
                                                  runtime=self._runtime)
            if obj_collection.find({'assignedVaultIds': {'$in': [str(vault_id)]}}).count() != 0:
                raise errors.IllegalState('catalog is not empty')
        collection.delete_one({'_id': ObjectId(vault_id.get_identifier())})

    def can_manage_vault_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Vaults``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        return: (boolean) - ``false`` if ``Vault`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def alias_vault(self, vault_id, alias_id):
        """Adds an ``Id`` to a ``Vault`` for the purpose of creating compatibility.


        The primary ``Id`` of the ``Vault`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another vault it is
        reassigned to the given vault ``Id``.


        arg:    vault_id (osid.id.Id): the ``Id`` of a ``Vault``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``vault_id`` not found
        raise:  NullArgument - ``vault_id`` or ``alias_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.BinLookupSession.alias_bin_template
        # NEED TO FIGURE OUT HOW TO IMPLEMENT THIS SOMEDAY
        raise errors.Unimplemented()


