"""AuthZ Adapter implementations of authorization sessions."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification



from ...abstract_osid.authorization import sessions as abc_authorization_sessions
from ..osid.osid_errors import NotFound
from ..osid.osid_errors import PermissionDenied, NullArgument, Unimplemented
from ..osid.osid_errors import Unsupported
from ..primitives import Id
from ..utilities import QueryWrapper
from dlkit.authz_adapter.osid import sessions as osid_sessions




class AuthorizationSession(abc_authorization_sessions.AuthorizationSession, osid_sessions.OsidSession):
    """Adapts underlying AuthorizationSession methodswith authorization checks."""

    def get_vault_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_vault_id()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault()

    vault = property(fget=get_vault)

    def can_access_authorizations(self):
        raise Unimplemented()

    def is_authorized(self, agent_id, function_id, qualifier_id):
        raise Unimplemented()

    def get_authorization_condition(self, function_id):
        raise Unimplemented()

    def is_authorized_on_condition(self, agent_id, function_id, qualifier_id, condition):
        raise Unimplemented()


class AuthorizationLookupSession(abc_authorization_sessions.AuthorizationLookupSession, osid_sessions.OsidSession):
    """Adapts underlying AuthorizationLookupSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None, **kwargs):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        if 'hierarchy_session' in kwargs:
            self._hierarchy_session = kwargs['hierarchy_session']
        else:
            self._hierarchy_session = None
        if 'query_session' in kwargs:
            self._query_session = kwargs['query_session']
        else:
            self._query_session = None


        self._qualifier_id = provider_session.get_vault_id()
        self._id_namespace = 'authorization.Authorization'


    def get_vault_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_vault_id()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault()

    vault = property(fget=get_vault)

    def can_lookup_authorizations(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._can('lookup')

    def use_comparative_authorization_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_authorization_view()

    def use_plenary_authorization_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_authorization_view()

    def use_federated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_vault_view()

    def use_isolated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_vault_view()

    def use_effective_authorization_view(self):
        raise Unimplemented()

    def use_any_effective_authorization_view(self):
        raise Unimplemented()

    def use_implicit_authorization_view(self):
        raise Unimplemented()

    def use_explicit_authorization_view(self):
        raise Unimplemented()

    def get_authorization(self, authorization_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_authorization(authorization_id)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_authorization_query()
            query.match_id(authorization_id, match=True)
            results = self._try_harder(query)
            if results.available() > 0:
                return results.next()
            else:
                raise NotFound()

    def get_authorizations_by_ids(self, authorization_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_authorizations_by_ids(authorization_ids)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_authorization_query()
            for authorization_id in (authorization_ids):
                query.match_id(authorization_id, match=True)
            return self._try_harder(query)

    def get_authorizations_by_genus_type(self, authorization_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_authorizations_by_genus_type(authorization_genus_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_authorization_query()
            query.match_genus_type(authorization_genus_type, match=True)
            return self._try_harder(query)

    def get_authorizations_by_parent_genus_type(self, authorization_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_authorizations_by_parent_genus_type(authorization_genus_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_authorization_query()
            query.match_parent_genus_type(authorization_genus_type, match=True)
            return self._try_harder(query)

    def get_authorizations_by_record_type(self, authorization_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_authorizations_by_record_type(authorization_record_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_authorization_query()
            query.match_record_type(authorization_record_type, match=True)
            return self._try_harder(query)

    def get_authorizations_on_date(self, from_, to):
        raise Unimplemented()

    def get_authorizations_for_resource(self, resource_id):
        raise Unimplemented()

    def get_authorizations_for_resource_on_date(self, resource_id, from_, to):
        raise Unimplemented()

    def get_authorizations_for_agent(self, agent_id):
        raise Unimplemented()

    def get_authorizations_for_agent_on_date(self, agent_id, from_, to):
        raise Unimplemented()

    def get_authorizations_for_function(self, function_id):
        # Implemented from azosid template for -
        # osid.learning.ActivityLookupSession.get_activities_for_objective_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_authorizations_for_function(function_id)

    def get_authorizations_for_function_on_date(self, function_id, from_, to):
        raise Unimplemented()

    def get_authorizations_for_resource_and_function(self, resource_id, function_id):
        raise Unimplemented()

    def get_authorizations_for_resource_and_function_on_date(self, resource_id, function_id, from_, to):
        raise Unimplemented()

    def get_authorizations_for_agent_and_function(self, agent_id, function_id):
        raise Unimplemented()

    def get_authorizations_for_agent_and_function_on_date(self, agent_id, function_id, from_, to):
        raise Unimplemented()

    def get_authorizations_by_qualifier(self, qualifier_id):
        raise Unimplemented()

    def get_explicit_authorization(self, authorization_id):
        raise Unimplemented()

    def get_authorizations(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_authorizations()
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_authorization_query()
            query.match_any(match=True)
            return self._try_harder(query)

    authorizations = property(fget=get_authorizations)


class AuthorizationQuerySession(abc_authorization_sessions.AuthorizationQuerySession, osid_sessions.OsidSession):
    """Adapts underlying AuthorizationQuerySession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None, **kwargs):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        if 'hierarchy_session' in kwargs:
            self._hierarchy_session = kwargs['hierarchy_session']
        else:
            self._hierarchy_session = None
        if 'query_session' in kwargs:
            self._query_session = kwargs['query_session']
        else:
            self._query_session = None


        self._qualifier_id = provider_session.get_vault_id()
        self._id_namespace = 'authorization.Authorization'


    def _get_unauth_vault_ids(self, vault_id):
        if self._can('search', vault_id):
            return [] # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(vault_id)]
        if self._hierarchy_session.has_child_vaults(vault_id):
            for child_vault_id in self._hierarchy_session.get_child_vault_ids(vault_id):
                unauth_list = unauth_list + self._get_unauth_vault_ids(child_vault_id)
        return unauth_list


    def _try_harder(self, query):
        if self._hierarchy_session is None:
            # Should probably try to return empty result instead
            # perhaps through a query.match_any(match = None)?
            raise PermissionDenied()
        for vault_id in self._get_unauth_vault_ids(self._qualifier_id):
            query._provider_query.match_vault_id(vault_id, match=False)
        return self._provider_session.get_authorizations_by_query(query)


    class AuthorizationQueryWrapper(QueryWrapper):
        """Wrapper for AuthorizationQueries to override match_vault_id method"""


        def match_vault_id(self, vault_id, match=True):
            self.cat_id_args_list.append({'vault_id': vault_id, 'match': match})


    def get_vault_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_vault_id()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault()

    vault = property(fget=get_vault)

    def can_search_authorizations(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._can('search')

    def use_federated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_vault_view()

    def use_isolated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_vault_view()

    def use_implicit_authorization_view(self):
        raise Unimplemented()

    def use_explicit_authorization_view(self):
        raise Unimplemented()

    def get_authorization_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and 
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.AuthorizationQueryWrapper(self._provider_session.get_authorization_query())

    authorization_query = property(fget=get_authorization_query)

    def get_authorizations_by_query(self, authorization_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(authorization_query, 'cat_id_args_list'):
            raise Unsupported('authorization_query not from this session')
        for kwargs in authorization_query.cat_id_args_list:
            if self._can('search', kwargs['vault_id']):
                authorization_query._provider_query.match_vault_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_authorizations_by_query(authorization_query)
        elif self._is_isolated_catalog_view():
            raise PermissionDenied()
        else:
            result = self._try_harder(authorization_query)
            authorization_query._provider_query.clear_vault_terms()
            return result


class AuthorizationSearchSession(abc_authorization_sessions.AuthorizationSearchSession, AuthorizationQuerySession):
    """Adapts underlying AuthorizationSearchSession methodswith authorization checks."""

    def get_authorization_search(self):
        """Pass through to provider AuthorizationSearchSession.get_authorization_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_authorization_search()

    authorization_search = property(fget=get_authorization_search)

    def get_authorization_search_order(self):
        raise Unimplemented()

    authorization_search_order = property(fget=get_authorization_search_order)

    def get_authorizations_by_search(self, authorization_query, authorization_search):
        """Pass through to provider AuthorizationSearchSession.get_authorizations_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_authorizations_by_search(authorization_query, authorization_search)

    def get_authorization_query_from_inspector(self, authorization_query_inspector):
        raise Unimplemented()


class AuthorizationAdminSession(abc_authorization_sessions.AuthorizationAdminSession, osid_sessions.OsidSession):
    """Adapts underlying AuthorizationAdminSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = provider_session.get_vault_id()
        self._id_namespace = 'authorization.Authorization'


    def get_vault_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_vault_id()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault()

    vault = property(fget=get_vault)

    def can_create_authorizations(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    def can_create_authorization_with_record_types(self, authorization_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if authorization_record_types == None:
            raise NullArgument() # Just 'cause the spec says to :)
        else:
            return self._can('create')

    def get_authorization_form_for_create_for_agent(self, agent_id, function_id, qualifier_id, authorization_record_types):
        raise Unimplemented()

    def get_authorization_form_for_create_for_resource(self, resource_id, function_id, qualifier_id, authorization_record_types):
        raise Unimplemented()

    def get_authorization_form_for_create_for_resource_and_trust(self, resource_id, trust_id, function_id, qualifier_id, authorization_record_types):
        raise Unimplemented()

    def create_authorization(self, authorization_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.create_authorization(authorization_form)

    def can_update_authorizations(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('update')

    def get_authorization_form_for_update(self, authorization_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_authorization_form_for_update(authorization_id)

    def duplicate_authorization(self, authorization_id):
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.duplicate_authorization(authorization_id)

    def update_authorization(self, authorization_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.update_authorization(authorization_form)

    def can_delete_authorizations(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('delete')

    def delete_authorization(self, authorization_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can('delete'):
            raise PermissionDenied()
        else:
            return self._provider_session.delete_authorization(authorization_id)

    def can_manage_authorization_aliases(self):
        raise Unimplemented()

    def alias_authorization(self, authorization_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can('alias'):
            raise PermissionDenied()
        else:
            return self._provider_session.alias_authorization(authorization_id, alias_id)


class AuthorizationNotificationSession(abc_authorization_sessions.AuthorizationNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying AuthorizationNotificationSession methodswith authorization checks."""

    def get_vault_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_vault_id()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault()

    vault = property(fget=get_vault)

    def can_register_for_authorization_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_vault_view()

    def use_isolated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_vault_view()

    def reliable_authorization_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_authorization_notifications()

    def unreliable_authorization_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_authorization_notifications()

    def acknowledge_authorization_notification(self, notification_id):
        raise Unimplemented()

    def use_implicit_authorization_view(self):
        raise Unimplemented()

    def use_explicit_authorization_view(self):
        raise Unimplemented()

    def register_for_new_authorizations(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_new_authorizations()

    def register_for_new_authorizations_for_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_new_authorizations_for_resource()

    def register_for_new_authorizations_for_function(self, function_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_new_authorizations_for_function()

    def register_for_changed_authorizations(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_authorizations()

    def register_for_changed_authorizations_for_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_authorizations_for_resource(resource_id)

    def register_for_changed_authorizations_for_function(self, function_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_authorizations_for_function(function_id)

    def register_for_changed_authorization(self, authorization_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_authorization(authorization_id)

    def register_for_deleted_authorizations(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_authorizations()

    def register_for_deleted_authorizations_for_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_authorizations_for_resource(resource_id)

    def register_for_deleted_authorizations_for_function(self, function_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_authorizations_for_function(function_id)

    def register_for_deleted_authorization(self, authorization_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_authorization(authorization_id)

    def reliable_authorization_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_authorization_notifications()

    def unreliable_authorization_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_authorization_notifications()

    def acknowledge_authorization_notification(self, notification_id):
        raise Unimplemented()


class AuthorizationVaultSession(abc_authorization_sessions.AuthorizationVaultSession, osid_sessions.OsidSession):
    """Adapts underlying AuthorizationVaultSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = Id('authorization.Qualifier%3AROOT%40ODL.MIT.EDU') # This needs to be done right
        self._id_namespace = 'authorization.AuthorizationVault'


    def use_comparative_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_vault_view()

    def use_plenary_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_vault_view()

    def can_lookup_authorization_vault_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def get_authorization_ids_by_vault(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_authorization_ids_by_vault(vault_id)

    def get_authorizations_by_vault(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_authorization_ids_by_vault(vault_id)

    def get_authorizations_ids_by_vault(self, vault_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_authorization_ids_by_vault(vault_id)

    def get_authorizations_by_vault(self, vault_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_authorization_ids_by_vault(vault_id)

    def get_vault_ids_by_authorization(self, authorization_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault_ids_by_authorization(authorization_id)

    def get_vault_by_authorization(self, authorization_id):
        raise Unimplemented()


class AuthorizationVaultAssignmentSession(abc_authorization_sessions.AuthorizationVaultAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying AuthorizationVaultAssignmentSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = Id('authorization.Qualifier%3AROOT%40ODL.MIT.EDU') # This needs to be done right
        self._id_namespace = 'authorization.AuthorizationVault'


    def can_assign_authorizations(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    def can_assign_authorizations_to_vault(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=bin_id)

    def get_assignable_vault_ids(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_assignable_vault_ids()

    def get_assignable_vault_ids_for_authorization(self, vault_id, authorization_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_assignable_vault_ids_for_authorization(authorization_id)

    def assign_authorization_to_vault(self, authorization_id, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.assign_authorization_to_vault(authorization_id, vault_id)

    def unassign_authorization_from_vault(self, authorization_id, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.unassign_authorization_from_vault(authorization_id, vault_id)

    def reassign_authorization_to_vault(self, authorization_id, from_vault_id, to_vault_id):
        raise Unimplemented()


class AuthorizationSmartVaultSession(abc_authorization_sessions.AuthorizationSmartVaultSession, osid_sessions.OsidSession):
    """Adapts underlying AuthorizationSmartVaultSession methodswith authorization checks."""

    def get_vault_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_vault_id()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault()

    vault = property(fget=get_vault)

    def can_manage_smart_vault(self):
        raise Unimplemented()

    def get_authorization_query(self):
        raise Unimplemented()

    authorization_query = property(fget=get_authorization_query)

    def get_authorization_search_order(self):
        raise Unimplemented()

    authorization_search_order = property(fget=get_authorization_search_order)

    def apply_authorization_query(self, authorization_query):
        raise Unimplemented()

    def inspect_authorization_query(self):
        raise Unimplemented()

    def apply_authorization_sequencing(self, authorization_search_order):
        raise Unimplemented()

    def get_authorization_query_from_inspector(self, authorization_query_inspector):
        raise Unimplemented()


class FunctionLookupSession(abc_authorization_sessions.FunctionLookupSession, osid_sessions.OsidSession):
    """Adapts underlying FunctionLookupSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None, **kwargs):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        if 'hierarchy_session' in kwargs:
            self._hierarchy_session = kwargs['hierarchy_session']
        else:
            self._hierarchy_session = None
        if 'query_session' in kwargs:
            self._query_session = kwargs['query_session']
        else:
            self._query_session = None
        self._qualifier_id = provider_session.get_vault_id()
        self._id_namespace = 'authorization.Function'
        self.use_federated_vault_view()
        self.use_comparative_function_view()


    def _get_unauth_vault_ids(self, vault_id):
        if self._can('lookup', vault_id):
            return [] # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(vault_id)]
        if self._hierarchy_session.has_child_vaults(vault_id):
            for child_vault_id in self._hierarchy_session.get_child_vault_ids(vault_id):
                unauth_list = unauth_list + self._get_unauth_vault_ids(child_vault_id)
        return unauth_list


    def _try_harder(self, query):
        if self._hierarchy_session is None or self._query_session is None:
            # Should probably try to return empty result instead
            # perhaps through a query.match_any(match = None)?
            raise PermissionDenied()
        for vault_id in self._get_unauth_vault_ids(self._qualifier_id):
            query.match_vault_id(vault_id, match=False)
        return self._query_session.get_functions_by_query(query)


    def get_vault_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_vault_id()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault()

    vault = property(fget=get_vault)

    def can_lookup_functions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._can('lookup')

    def use_comparative_function_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_function_view()

    def use_plenary_function_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_function_view()

    def use_federated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_vault_view()

    def use_isolated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_vault_view()

    def use_active_function_view(self):
        raise Unimplemented()

    def use_any_status_function_view(self):
        raise Unimplemented()

    def get_function(self, function_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_function(function_id)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_function_query()
            query.match_id(function_id, match=True)
            results = self._try_harder(query)
            if results.available() > 0:
                return results.next()
            else:
                raise NotFound()

    def get_functions_by_ids(self, function_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_functions_by_ids(function_ids)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_function_query()
            for function_id in (function_ids):
                query.match_id(function_id, match=True)
            return self._try_harder(query)

    def get_functions_by_genus_type(self, function_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_functions_by_genus_type(function_genus_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_function_query()
            query.match_genus_type(function_genus_type, match=True)
            return self._try_harder(query)

    def get_functions_by_parent_genus_type(self, function_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_functions_by_parent_genus_type(function_genus_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_function_query()
            query.match_parent_genus_type(function_genus_type, match=True)
            return self._try_harder(query)

    def get_functions_by_record_type(self, function_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_functions_by_record_type(function_record_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_function_query()
            query.match_record_type(function_record_type, match=True)
            return self._try_harder(query)

    def get_functions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_functions()
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_function_query()
            query.match_any(match=True)
            return self._try_harder(query)

    functions = property(fget=get_functions)


class FunctionQuerySession(abc_authorization_sessions.FunctionQuerySession, osid_sessions.OsidSession):
    """Adapts underlying FunctionQuerySession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None, **kwargs):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        if 'hierarchy_session' in kwargs:
            self._hierarchy_session = kwargs['hierarchy_session']
        else:
            self._hierarchy_session = None
        self._qualifier_id = provider_session.get_vault_id()
        self._id_namespace = 'authorization.Function'
        self.use_federated_vault_view()


    def _get_unauth_vault_ids(self, vault_id):
        if self._can('search', vault_id):
            return [] # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(vault_id)]
        if self._hierarchy_session.has_child_vaults(vault_id):
            for child_vault_id in self._hierarchy_session.get_child_vault_ids(vault_id):
                unauth_list = unauth_list + self._get_unauth_vault_ids(child_vault_id)
        return unauth_list


    def _try_harder(self, query):
        if self._hierarchy_session is None:
            # Should probably try to return empty result instead
            # perhaps through a query.match_any(match = None)?
            raise PermissionDenied()
        for vault_id in self._get_unauth_vault_ids(self._qualifier_id):
            query._provider_query.match_vault_id(vault_id, match=False)
        return self._provider_session.get_functions_by_query(query)


    class FunctionQueryWrapper(QueryWrapper):
        """Wrapper for FunctionQueries to override match_vault_id method"""


        def match_vault_id(self, vault_id, match=True):
            self.cat_id_args_list.append({'vault_id': vault_id, 'match': match})


    def get_vault_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_vault_id()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault()

    vault = property(fget=get_vault)

    def can_search_functions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._can('search')

    def use_federated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_vault_view()

    def use_isolated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_vault_view()

    def get_function_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and 
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.FunctionQueryWrapper(self._provider_session.get_function_query())

    function_query = property(fget=get_function_query)

    def get_functions_by_query(self, function_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(function_query, 'cat_id_args_list'):
            raise Unsupported('function_query not from this session')
        for kwargs in function_query.cat_id_args_list:
            if self._can('search', kwargs['vault_id']):
                function_query._provider_query.match_vault_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_functions_by_query(function_query)
        elif self._is_isolated_catalog_view():
            raise PermissionDenied()
        else:
            result = self._try_harder(function_query)
            function_query._provider_query.clear_vault_terms()
            return result


class FunctionSearchSession(abc_authorization_sessions.FunctionSearchSession, FunctionQuerySession):
    """Adapts underlying FunctionSearchSession methodswith authorization checks."""

    def get_function_search(self):
        """Pass through to provider FunctionSearchSession.get_function_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_function_search()

    function_search = property(fget=get_function_search)

    def get_function_search_order(self):
        raise Unimplemented()

    function_search_order = property(fget=get_function_search_order)

    def get_functions_by_search(self, function_query, function_search):
        """Pass through to provider FunctionSearchSession.get_functions_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_functions_by_search(function_query, function_search)

    def get_function_query_from_inspector(self, function_query_inspector):
        raise Unimplemented()


class FunctionAdminSession(abc_authorization_sessions.FunctionAdminSession, osid_sessions.OsidSession):
    """Adapts underlying FunctionAdminSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = provider_session.get_vault_id()
        self._id_namespace = 'authorization.Function'


    def get_vault_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_vault_id()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault()

    vault = property(fget=get_vault)

    def can_create_functions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    def can_create_function_with_record_types(self, function_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if function_record_types == None:
            raise NullArgument() # Just 'cause the spec says to :)
        else:
            return self._can('create')

    def get_function_form_for_create(self, function_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_function_form_for_create(function_record_types)

    def create_function(self, function_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.create_function(function_form)

    def can_update_functions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('update')

    def get_function_form_for_update(self, function_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_function_form_for_update(function_id)

    def duplicate_function(self, function_id):
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.duplicate_function(function_id)

    def update_function(self, function_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.update_function(function_form)

    def can_delete_functions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('delete')

    def delete_function(self, function_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can('delete'):
            raise PermissionDenied()
        else:
            return self._provider_session.delete_function(function_id)

    def can_manage_function_aliases(self):
        raise Unimplemented()

    def alias_function(self, function_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can('alias'):
            raise PermissionDenied()
        else:
            return self._provider_session.alias_function(function_id, alias_id)


class FunctionNotificationSession(abc_authorization_sessions.FunctionNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying FunctionNotificationSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = provider_session.get_vault_id()
        self._id_namespace = 'authorization.Function'


    def get_vault_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_vault_id()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault()

    vault = property(fget=get_vault)

    def can_register_for_function_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_vault_view()

    def use_isolated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_vault_view()

    def reliable_function_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_function_notifications()

    def unreliable_function_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_function_notifications()

    def acknowledge_function_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_functions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_new_functions()

    def register_for_changed_functions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_functions()

    def register_for_changed_function(self, function_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_function(function_id)

    def register_for_deleted_functions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_functions()

    def register_for_deleted_function(self, function_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_function(function_id)

    def reliable_function_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_function_notifications()

    def unreliable_function_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_function_notifications()

    def acknowledge_function_notification(self, notification_id):
        raise Unimplemented()


class FunctionVaultSession(abc_authorization_sessions.FunctionVaultSession, osid_sessions.OsidSession):
    """Adapts underlying FunctionVaultSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = Id('authorization.Qualifier%3AROOT%40ODL.MIT.EDU') # This needs to be done right
        self._id_namespace = 'authorization.FunctionVault'


    def can_lookup_function_vault_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def use_comparative_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_vault_view()

    def use_plenary_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_vault_view()

    def get_function_ids_by_vault(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_function_ids_by_vault(vault_id)

    def get_functions_by_vault(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_function_ids_by_vault(vault_id)

    def get_function_ids_by_vaults(self, vault_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_function_ids_by_vaults(vault_ids)

    def get_functions_by_vaults(self, vault_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_functions_ids_by_vaults(vault_ids)

    def get_vault_ids_by_function(self, function_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault_ids_by_function(function_id)

    def get_vaults_by_function(self, function_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vaults_by_function(function_id)


class FunctionVaultAssignmentSession(abc_authorization_sessions.FunctionVaultAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying FunctionVaultAssignmentSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = Id('authorization.Qualifier%3AROOT%40ODL.MIT.EDU') # This needs to be done right
        self._id_namespace = 'authorization.FunctionVault'


    def can_assign_functions(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    def can_assign_functions_to_vault(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=bin_id)

    def get_assignable_vault_ids(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_assignable_vault_ids()

    def get_assignable_vault_ids_for_function(self, vault_id, function_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_assignable_vault_ids_for_function(function_id)

    def assign_function_to_vault(self, function_id, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.assign_function_to_vault(function_id, vault_id)

    def unassign_function_from_vault(self, function_id, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.unassign_function_from_vault(function_id, vault_id)

    def reassign_function_to_vault(self, function_id, from_vault_id, to_vault_id):
        raise Unimplemented()


class FunctionSmartVaultSession(abc_authorization_sessions.FunctionSmartVaultSession, osid_sessions.OsidSession):
    """Adapts underlying FunctionSmartVaultSession methodswith authorization checks."""

    def get_vault_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_vault_id()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault()

    vault = property(fget=get_vault)

    def can_manage_smart_vaults(self):
        raise Unimplemented()

    def get_function_query(self):
        raise Unimplemented()

    function_query = property(fget=get_function_query)

    def get_function_search_order(self):
        raise Unimplemented()

    function_search_order = property(fget=get_function_search_order)

    def apply_function_query(self, function_query):
        raise Unimplemented()

    def inspect_function_query(self):
        raise Unimplemented()

    def apply_function_sequencing(self, function_search_order):
        raise Unimplemented()

    def get_function_query_from_inspector(self, function_query_inspector):
        raise Unimplemented()


class QualifierLookupSession(abc_authorization_sessions.QualifierLookupSession, osid_sessions.OsidSession):
    """Adapts underlying QualifierLookupSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None, **kwargs):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        if 'hierarchy_session' in kwargs:
            self._hierarchy_session = kwargs['hierarchy_session']
        else:
            self._hierarchy_session = None
        if 'query_session' in kwargs:
            self._query_session = kwargs['query_session']
        else:
            self._query_session = None
        self._qualifier_id = provider_session.get_vault_id()
        self._id_namespace = 'authorization.Qualifier'
        self.use_federated_vault_view()
        self.use_comparative_qualifier_view()


    def _get_unauth_vault_ids(self, vault_id):
        if self._can('lookup', vault_id):
            return [] # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(vault_id)]
        if self._hierarchy_session.has_child_vaults(vault_id):
            for child_vault_id in self._hierarchy_session.get_child_vault_ids(vault_id):
                unauth_list = unauth_list + self._get_unauth_vault_ids(child_vault_id)
        return unauth_list


    def _try_harder(self, query):
        if self._hierarchy_session is None or self._query_session is None:
            # Should probably try to return empty result instead
            # perhaps through a query.match_any(match = None)?
            raise PermissionDenied()
        for vault_id in self._get_unauth_vault_ids(self._qualifier_id):
            query.match_vault_id(vault_id, match=False)
        return self._query_session.get_qualifiers_by_query(query)


    def get_vault_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_vault_id()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault()

    vault = property(fget=get_vault)

    def can_lookup_qualifiers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._can('lookup')

    def use_comparative_qualifier_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_qualifier_view()

    def use_plenary_qualifier_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_qualifier_view()

    def use_federated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_vault_view()

    def use_isolated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_vault_view()

    def get_qualifier(self, qualifier_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_qualifier(qualifier_id)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_qualifier_query()
            query.match_id(qualifier_id, match=True)
            results = self._try_harder(query)
            if results.available() > 0:
                return results.next()
            else:
                raise NotFound()

    def get_qualifiers_by_ids(self, qualifier_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_qualifiers_by_ids(qualifier_ids)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_qualifier_query()
            for qualifier_id in (qualifier_ids):
                query.match_id(qualifier_id, match=True)
            return self._try_harder(query)

    def get_qualifiers_by_genus_type(self, qualifier_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_qualifiers_by_genus_type(qualifier_genus_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_qualifier_query()
            query.match_genus_type(qualifier_genus_type, match=True)
            return self._try_harder(query)

    def get_qualifiers_by_parent_genus_type(self, qualifier_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_qualifiers_by_parent_genus_type(qualifier_genus_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_qualifier_query()
            query.match_parent_genus_type(qualifier_genus_type, match=True)
            return self._try_harder(query)

    def get_qualifiers_by_record_type(self, qualifier_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_qualifiers_by_record_type(qualifier_record_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_qualifier_query()
            query.match_record_type(qualifier_record_type, match=True)
            return self._try_harder(query)

    def get_qualifiers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_qualifiers()
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_qualifier_query()
            query.match_any(match=True)
            return self._try_harder(query)

    qualifiers = property(fget=get_qualifiers)


class QualifierQuerySession(abc_authorization_sessions.QualifierQuerySession, osid_sessions.OsidSession):
    """Adapts underlying QualifierQuerySession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None, **kwargs):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        if 'hierarchy_session' in kwargs:
            self._hierarchy_session = kwargs['hierarchy_session']
        else:
            self._hierarchy_session = None
        self._qualifier_id = provider_session.get_vault_id()
        self._id_namespace = 'authorization.Qualifier'
        self.use_federated_vault_view()


    def _get_unauth_vault_ids(self, vault_id):
        if self._can('search', vault_id):
            return [] # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(vault_id)]
        if self._hierarchy_session.has_child_vaults(vault_id):
            for child_vault_id in self._hierarchy_session.get_child_vault_ids(vault_id):
                unauth_list = unauth_list + self._get_unauth_vault_ids(child_vault_id)
        return unauth_list


    def _try_harder(self, query):
        if self._hierarchy_session is None:
            # Should probably try to return empty result instead
            # perhaps through a query.match_any(match = None)?
            raise PermissionDenied()
        for vault_id in self._get_unauth_vault_ids(self._qualifier_id):
            query._provider_query.match_vault_id(vault_id, match=False)
        return self._provider_session.get_qualifiers_by_query(query)


    class QualifierQueryWrapper(QueryWrapper):
        """Wrapper for QualifierQueries to override match_vault_id method"""


        def match_vault_id(self, vault_id, match=True):
            self.cat_id_args_list.append({'vault_id': vault_id, 'match': match})


    def get_vault_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_vault_id()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault()

    vault = property(fget=get_vault)

    def can_search_qualifiers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._can('search')

    def use_federated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_vault_view()

    def use_isolated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_vault_view()

    def get_qualifier_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and 
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.QualifierQueryWrapper(self._provider_session.get_qualifier_query())

    qualifier_query = property(fget=get_qualifier_query)

    def get_qualifiers_by_query(self, qualifier_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(qualifier_query, 'cat_id_args_list'):
            raise Unsupported('qualifier_query not from this session')
        for kwargs in qualifier_query.cat_id_args_list:
            if self._can('search', kwargs['vault_id']):
                qualifier_query._provider_query.match_vault_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_qualifiers_by_query(qualifier_query)
        elif self._is_isolated_catalog_view():
            raise PermissionDenied()
        else:
            result = self._try_harder(qualifier_query)
            qualifier_query._provider_query.clear_vault_terms()
            return result


class QualifierSearchSession(abc_authorization_sessions.QualifierSearchSession, QualifierQuerySession):
    """Adapts underlying QualifierSearchSession methodswith authorization checks."""

    def get_qualifier_search(self):
        """Pass through to provider QualifierSearchSession.get_qualifier_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_qualifier_search()

    qualifier_search = property(fget=get_qualifier_search)

    def get_qualifier_search_order(self):
        raise Unimplemented()

    qualifier_search_order = property(fget=get_qualifier_search_order)

    def get_qualifiers_by_search(self, qualifier_query, qualifier_search):
        """Pass through to provider QualifierSearchSession.get_qualifiers_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_qualifiers_by_search(qualifier_query, qualifier_search)

    def get_qualifier_query_from_inspector(self, qualifier_query_inspector):
        raise Unimplemented()


class QualifierAdminSession(abc_authorization_sessions.QualifierAdminSession, osid_sessions.OsidSession):
    """Adapts underlying QualifierAdminSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = provider_session.get_vault_id()
        self._id_namespace = 'authorization.Qualifier'


    def get_vault_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_vault_id()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault()

    vault = property(fget=get_vault)

    def can_create_qualifiers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    def can_create_qualifier_with_record_types(self, qualifier_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if qualifier_record_types == None:
            raise NullArgument() # Just 'cause the spec says to :)
        else:
            return self._can('create')

    def get_qualifier_form_for_create(self, qualifier_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_qualifier_form_for_create(qualifier_record_types)

    def create_qualifier(self, qualifier_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.create_qualifier(qualifier_form)

    def can_update_qualifiers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('update')

    def get_qualifier_form_for_update(self, qualifier_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_qualifier_form_for_update(qualifier_id)

    def duplicate_qualifier(self, qualifier_id):
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.duplicate_qualifier(qualifier_id)

    def update_qualifier(self, qualifier_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.update_qualifier(qualifier_form)

    def can_delete_qualifiers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('delete')

    def delete_qualifier(self, qualifier_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can('delete'):
            raise PermissionDenied()
        else:
            return self._provider_session.delete_qualifier(qualifier_id)

    def can_manage_qualifier_aliases(self):
        raise Unimplemented()

    def alias_qualifier(self, qualifier_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can('alias'):
            raise PermissionDenied()
        else:
            return self._provider_session.alias_qualifier(qualifier_id, alias_id)


class QualifierNotificationSession(abc_authorization_sessions.QualifierNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying QualifierNotificationSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = provider_session.get_vault_id()
        self._id_namespace = 'authorization.Qualifier'


    def get_vault_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_vault_id()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault()

    vault = property(fget=get_vault)

    def can_register_for_qualifier_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_vault_view()

    def use_isolated_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_vault_view()

    def reliable_qualifier_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_qualifier_notifications()

    def unreliable_qualifier_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_qualifier_notifications()

    def acknowledge_qualifier_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_qualifiers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_new_qualifiers()

    def register_for_changed_qualifiers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_qualifiers()

    def register_for_changed_qualifier(self, qualifier_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_qualifier(qualifier_id)

    def register_for_deleted_qualifiers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_qualifiers()

    def register_for_deleted_qualifier(self, qualifier_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_qualifier(qualifier_id)

    def register_for_changed_qualifier_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_qualifier_hierarchy()

    def register_for_changed_qualifier_hierarchy_for_ancestors(self, qualifier_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_qualifier_hierarchy_for_ancestors(qualifier_id)

    def register_for_changed_qualifier_hierarchy_for_descendants(self, qualifier_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_qualifier_hierarchy_for_descendants(qualifier_id)

    def reliable_qualifier_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_qualifier_notifications()

    def unreliable_qualifier_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_qualifier_notifications()

    def acknowledge_qualifier_notification(self, notification_id):
        raise Unimplemented()


class QualifierHierarchySession(abc_authorization_sessions.QualifierHierarchySession, osid_sessions.OsidSession):
    """Adapts underlying QualifierHierarchySession methodswith authorization checks."""

    def get_qualifier_hierarchy_id(self):
        raise Unimplemented()

    qualifier_hierarchy_id = property(fget=get_qualifier_hierarchy_id)

    def get_qualifier_hierarchy(self):
        raise Unimplemented()

    qualifier_hierarchy = property(fget=get_qualifier_hierarchy)

    def can_access_qualifier_hierarchy(self):
        raise Unimplemented()

    def use_comparative_qualifier_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_qualifier_view()

    def use_plenary_qualifier_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_qualifier_view()

    def get_root_qualifier_ids(self):
        raise Unimplemented()

    root_qualifier_ids = property(fget=get_root_qualifier_ids)

    def get_root_qualifiers(self):
        raise Unimplemented()

    root_qualifiers = property(fget=get_root_qualifiers)

    def has_parent_qualifiers(self, qualifier_id):
        raise Unimplemented()

    def is_parent_of_qualifier(self, id_, qualifier_id):
        raise Unimplemented()

    def get_parent_qualifier_ids(self, qualifier_id):
        raise Unimplemented()

    def get_parent_qualifiers(self, qualifier_id):
        raise Unimplemented()

    def is_ancestor_of_qualifier(self, id_, qualifier_id):
        raise Unimplemented()

    def has_child_qualifiers(self, qualifier_id):
        raise Unimplemented()

    def is_child_of_qualifier(self, id_, qualifier_id):
        raise Unimplemented()

    def get_child_qualifier_ids(self, qualifier_id):
        raise Unimplemented()

    def get_child_qualifiers(self, qualifier_id):
        raise Unimplemented()

    def is_descendant_of_qualifier(self, id_, qualifier_id):
        raise Unimplemented()

    def get_qualifier_node_ids(self, qualifier_id, ancestor_levels, descendant_levels, include_siblings):
        raise Unimplemented()

    def get_qualifier_nodes(self, qualifier_id, ancestor_levels, descendant_levels, include_siblings):
        raise Unimplemented()


class QualifierHierarchyDesignSession(abc_authorization_sessions.QualifierHierarchyDesignSession, osid_sessions.OsidSession):
    """Adapts underlying QualifierHierarchyDesignSession methodswith authorization checks."""

    def get_qualifier_hierarchy_id(self):
        raise Unimplemented()

    qualifier_hierarchy_id = property(fget=get_qualifier_hierarchy_id)

    def get_qualifier_hierarchy(self):
        raise Unimplemented()

    qualifier_hierarchy = property(fget=get_qualifier_hierarchy)

    def can_modify_qualifier_hierarchy(self):
        raise Unimplemented()

    def add_root_qualifier(self, qualifier_id):
        raise Unimplemented()

    def remove_root_qualifier(self, qualifier_id):
        raise Unimplemented()

    def add_child_qualifier(self, qualifier_id, child_id):
        raise Unimplemented()

    def remove_child_qualifier(self, qualifier_id, child_id):
        raise Unimplemented()

    def remove_child_qualifiers(self, qualifier_id):
        raise Unimplemented()


class QualifierVaultSession(abc_authorization_sessions.QualifierVaultSession, osid_sessions.OsidSession):
    """Adapts underlying QualifierVaultSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = Id('authorization.Qualifier%3AROOT%40ODL.MIT.EDU') # This needs to be done right
        self._id_namespace = 'authorization.QualifierVault'


    def can_lookup_qualifier_vault_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def use_comparative_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_vault_view()

    def use_plenary_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_vault_view()

    def get_qualifier_ids_by_vault(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_qualifier_ids_by_vault(vault_id)

    def get_qualifiers_by_vault(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_qualifier_ids_by_vault(vault_id)

    def get_qualifier_ids_by_vaults(self, vault_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_qualifier_ids_by_vaults(vault_ids)

    def get_qualifiers_by_vaults(self, vault_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_qualifiers_ids_by_vaults(vault_ids)

    def get_vault_ids_by_qualifier(self, qualifier_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault_ids_by_qualifier(qualifier_id)

    def get_vaults_by_qualifier(self, qualifier_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vaults_by_qualifier(qualifier_id)


class QualifierVaultAssignmentSession(abc_authorization_sessions.QualifierVaultAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying QualifierVaultAssignmentSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = Id('authorization.Qualifier%3AROOT%40ODL.MIT.EDU') # This needs to be done right
        self._id_namespace = 'authorization.QualifierVault'


    def can_assign_qualifiers(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    def can_assign_qualifiers_to_vault(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=bin_id)

    def get_assignable_vault_ids(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_assignable_vault_ids()

    def get_assignable_vault_ids_for_qualifier(self, vault_id, qualifier_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_assignable_vault_ids_for_qualifier(qualifier_id)

    def assign_qualifier_to_vault(self, qualifier_id, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.assign_qualifier_to_vault(qualifier_id, vault_id)

    def unassign_qualifier_from_vault(self, qualifier_id, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.unassign_qualifier_from_vault(qualifier_id, vault_id)

    def reassign_qualifier_to_vault(self, qualifier_id, from_vault_id, to_vault_id):
        raise Unimplemented()


class QualifierSmartVaultSession(abc_authorization_sessions.QualifierSmartVaultSession, osid_sessions.OsidSession):
    """Adapts underlying QualifierSmartVaultSession methodswith authorization checks."""

    def get_vault_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_vault_id()

    vault_id = property(fget=get_vault_id)

    def get_vault(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault()

    vault = property(fget=get_vault)

    def can_manage_smart_vaults(self):
        raise Unimplemented()

    def get_qualifier_query(self):
        raise Unimplemented()

    qualifier_query = property(fget=get_qualifier_query)

    def get_qualifier_search_order(self):
        raise Unimplemented()

    qualifier_search_order = property(fget=get_qualifier_search_order)

    def apply_qualifier_query(self, qualifier_query):
        raise Unimplemented()

    def inspect_qualifier_query(self):
        raise Unimplemented()

    def apply_qualifier_sequencing(self, qualifier_search_order):
        raise Unimplemented()

    def get_qualifier_query_from_inspector(self, qualifier_query_inspector):
        raise Unimplemented()


class VaultLookupSession(abc_authorization_sessions.VaultLookupSession, osid_sessions.OsidSession):
    """Adapts underlying VaultLookupSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('authorization.Vault%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'authorization.Vault'


    def can_lookup_vaults(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._can('lookup')

    def use_comparative_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_vault_view()

    def use_plenary_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_vault_view()

    def get_vault(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault(vault_id)

    def get_vaults_by_ids(self, vault_ids):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vaults_by_ids(vault_ids)

    def get_vaults_by_genus_type(self, vault_genus_type):
        raise Unimplemented()

    def get_vaults_by_parent_genus_type(self, vault_genus_type):
        raise Unimplemented()

    def get_vaults_by_record_type(self, vault_record_type):
        raise Unimplemented()

    def get_vaults_by_provider(self, resource_id):
        raise Unimplemented()

    def get_vaults(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vaults()

    vaults = property(fget=get_vaults)


class VaultQuerySession(abc_authorization_sessions.VaultQuerySession, osid_sessions.OsidSession):
    """Adapts underlying VaultQuerySession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('authorization.Vault%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'authorization.Vault'


    def can_search_vaults(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._can('search')

    def get_vault_query(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bin_query_template
        if not self._can('search'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault_query()

    vault_query = property(fget=get_vault_query)

    def get_vaults_by_query(self, vault_query):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bins_by_query_template
        if not self._can('search'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vaults_by_query(vault_query)


class VaultSearchSession(abc_authorization_sessions.VaultSearchSession, VaultQuerySession):
    """Adapts underlying VaultSearchSession methodswith authorization checks."""

    def get_vault_search(self):
        raise Unimplemented()

    vault_search = property(fget=get_vault_search)

    def get_vault_search_order(self):
        raise Unimplemented()

    vault_search_order = property(fget=get_vault_search_order)

    def get_vaults_by_search(self, vault_query, vault_search):
        raise Unimplemented()

    def get_vault_query_from_inspector(self, vault_query_inspector):
        raise Unimplemented()


class VaultAdminSession(abc_authorization_sessions.VaultAdminSession, osid_sessions.OsidSession):
    """Adapts underlying VaultAdminSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('authorization.Vault%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'authorization.Vault'


    def can_create_vaults(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    def can_create_vault_with_record_types(self, vault_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if vault_record_types == None:
            raise NullArgument() # Just 'cause the spec says to :)
        else:
            return self._can('create')

    def get_vault_form_for_create(self, vault_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault_form_for_create(vault_record_types)

    def create_vault(self, vault_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.create_bin_template
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.create_vault(vault_form)

    def can_update_vaults(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('update')

    def get_vault_form_for_update(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault_form_for_update(vault_id)

    def update_vault(self, vault_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.update_bin_template
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.update_vault(vault_form)

    def can_delete_vaults(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('delete')

    def delete_vault(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.delete_bin_template
        if not self._can('delete'):
            raise PermissionDenied()
        else:
            return self._provider_session.delete_vault(vault_id)

    def can_manage_vault_aliases(self):
        raise Unimplemented()

    def alias_vault(self, vault_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.alias_bin_template
        if not self._can('alias'):
            raise PermissionDenied()
        else:
            return self._provider_session.alias_vault(vault_id)


class VaultNotificationSession(abc_authorization_sessions.VaultNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying VaultNotificationSession methodswith authorization checks."""

    def can_register_for_vault_notifications(self):
        raise Unimplemented()

    def reliable_vault_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_vault_notifications()

    def unreliable_vault_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_vault_notifications()

    def acknowledge_vault_notification(self, notification_id):
        raise Unimplemented()

    def register_for_new_vaults(self):
        raise Unimplemented()

    def register_for_changed_vaults(self):
        raise Unimplemented()

    def register_for_changed_vault(self, vault_id):
        raise Unimplemented()

    def register_for_deleted_vaults(self):
        raise Unimplemented()

    def register_for_deleted_vault(self, vault_id):
        raise Unimplemented()

    def register_for_changed_vault_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_vault_hierarchy()

    def register_for_changed_vault_hierarchy_for_ancestors(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_vault_hierarchy_for_ancestors(vault_id)

    def register_for_changed_vault_hierarchy_for_descendants(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_vault_hierarchy_for_descendants(vault_id)

    def reliable_vault_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_vault_notifications()

    def unreliable_vault_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_vault_notifications()

    def acknowledge_vault_notification(self, notification_id):
        raise Unimplemented()


class VaultHierarchySession(abc_authorization_sessions.VaultHierarchySession, osid_sessions.OsidSession):
    """Adapts underlying VaultHierarchySession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('authorization.Vault%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'authorization.Vault'


    def get_vault_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_vault_hierarchy_id()

    vault_hierarchy_id = property(fget=get_vault_hierarchy_id)

    def get_vault_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault_hierarchy()

    vault_hierarchy = property(fget=get_vault_hierarchy)

    def can_access_vault_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        return self._can('access')

    def use_comparative_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_vault_view()

    def use_plenary_vault_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_vault_view()

    def get_root_vault_ids(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_root_vault_ids()

    root_vault_ids = property(fget=get_root_vault_ids)

    def get_root_vaults(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bins
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_root_vaults()

    root_vaults = property(fget=get_root_vaults)

    def has_parent_vaults(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.has_parent_vaults(vault_id)

    def is_parent_of_vault(self, id_, vault_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_parent_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.is_parent_of_vault(id_, vault_id)

    def get_parent_vault_ids(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_parent_vault_ids(vault_id)

    def get_parent_vaults(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_parent_vaults(vault_id)

    def is_ancestor_of_vault(self, id_, vault_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.is_ancestor_of_vault(id_, vault_id)

    def has_child_vaults(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_child_bins
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.has_child_vaults(vault_id)

    def is_child_of_vault(self, id_, vault_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_child_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.is_child_of_vault(id_, vault_id)

    def get_child_vault_ids(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_child_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_child_vault_ids(vault_id)

    def get_child_vaults(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_child_vaults(vault_id)

    def is_descendant_of_vault(self, id_, vault_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.is_descendant_of_vault(id_, vault_id)

    def get_vault_node_ids(self, vault_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_node_ids
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault_node_ids(
                vault_id,
                ancestor_levels,
                descendant_levels,
                include_siblings)

    def get_vault_nodes(self, vault_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_nodes
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault_nodes(
                vault_id,
                ancestor_levels,
                descendant_levels,
                include_siblings)


class VaultHierarchyDesignSession(abc_authorization_sessions.VaultHierarchyDesignSession, osid_sessions.OsidSession):
    """Adapts underlying VaultHierarchyDesignSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('authorization.Vault%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'authorization.Vault' # should this be 'authorization.VaultHierarchy' ?


    def get_vault_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_vault_hierarchy_id()

    vault_hierarchy_id = property(fget=get_vault_hierarchy_id)

    def get_vault_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_vault_hierarchy()

    vault_hierarchy = property(fget=get_vault_hierarchy)

    def can_modify_vault_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy
        return self._can('modify')

    def add_root_vault(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.add_root_bin_template
        if not self._can('modify'):
            raise PermissionDenied()
        else:
            return self._provider_session.add_root_vault(vault_id)

    def remove_root_vault(self, vault_id):
        if not self._can('modify'):
            raise PermissionDenied()
        else:
            return self._provider_session.remove_root_vault(vault_id)

    def add_child_vault(self, vault_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        else:
            return self._provider_session.add_child_vault(vault_id, child_id)

    def remove_child_vault(self, vault_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        else:
            return self._provider_session.remove_child_vault(vault_id, child_id)

    def remove_child_vaults(self, vault_id):
        if not self._can('modify'):
            raise PermissionDenied()
        else:
            return self._provider_session.remove_child_vaults(vault_id)


