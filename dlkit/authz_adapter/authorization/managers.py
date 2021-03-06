"""AuthZ Adapter implementations of authorization managers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification



from . import sessions
from ..osid.osid_errors import Unimplemented, OperationFailed
from ..osid.osid_errors import Unsupported
from ..primitives import Id
from dlkit.authz_adapter.osid import managers as osid_managers
from dlkit.manager_impls.authorization import managers as authorization_managers




class AuthorizationProfile(osid_managers.OsidProfile, authorization_managers.AuthorizationProfile):
    """Adapts underlying AuthorizationProfile methodswith authorization checks."""


    def __init__(self, interface_name):
        osid_managers.OsidProfile.__init__(self)


    def _get_hierarchy_session(self):
        try:
            return self._provider_manager.get_vault_hierarchy_session(
                Id(authority='AUTHORIZATION',
                   namespace='CATALOG',
                   identifier='VAULT'))
        except Unsupported:
            return None


    def supports_authorization(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_authorization()

    def supports_authorization_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_authorization_lookup()

    def supports_authorization_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_authorization_admin()

    def supports_vault_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_vault_lookup()

    def supports_vault_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_vault_admin()

    def get_authorization_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_authorization_record_types()

    authorization_record_types = property(fget=get_authorization_record_types)

    def get_authorization_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_authorization_search_record_types()

    authorization_search_record_types = property(fget=get_authorization_search_record_types)

    def get_function_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_function_record_types()

    function_record_types = property(fget=get_function_record_types)

    def get_function_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_function_search_record_types()

    function_search_record_types = property(fget=get_function_search_record_types)

    def get_qualifier_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_qualifier_record_types()

    qualifier_record_types = property(fget=get_qualifier_record_types)

    def get_qualifier_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_qualifier_search_record_types()

    qualifier_search_record_types = property(fget=get_qualifier_search_record_types)

    def get_vault_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_vault_record_types()

    vault_record_types = property(fget=get_vault_record_types)

    def get_vault_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_vault_search_record_types()

    vault_search_record_types = property(fget=get_vault_search_record_types)

    def get_authorization_condition_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_authorization_condition_record_types()

    authorization_condition_record_types = property(fget=get_authorization_condition_record_types)


class AuthorizationManager(osid_managers.OsidManager, AuthorizationProfile, authorization_managers.AuthorizationManager):
    """Adapts underlying AuthorizationManager methodswith authorization checks."""


    def __init__(self):
        AuthorizationProfile.__init__(self)


    def initialize(self, runtime):
        osid_managers.OsidManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:authorizationProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_manager('AUTHORIZATION', provider_impl) # need to add version argument


    def get_authorization_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AuthorizationSession')(
                self._provider_manager.get_authorization_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    authorization_session = property(fget=get_authorization_session)

    def get_authorization_session_for_vault(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AuthorizationSession')(
                self._provider_manager.get_authorization_session_for_vault(vault_id),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    def get_authorization_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_authorization_query_session()
            query_session.use_federated_vault_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AuthorizationLookupSession')(
                self._provider_manager.get_authorization_lookup_session(),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    authorization_lookup_session = property(fget=get_authorization_lookup_session)

    def get_authorization_lookup_session_for_vault(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_authorization_query_session_for_vault(vault_id)
            query_session.use_federated_vault_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AuthorizationLookupSession')(
                self._provider_manager.get_authorization_lookup_session_for_vault(vault_id),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_authorization_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AuthorizationAdminSession')(
                self._provider_manager.get_authorization_admin_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    authorization_admin_session = property(fget=get_authorization_admin_session)

    def get_authorization_admin_session_for_vault(self, vault_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AuthorizationAdminSession')(
                self._provider_manager.get_authorization_admin_session_for_vault(vault_id),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    def get_vault_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'VaultLookupSession')(
                self._provider_manager.get_vault_lookup_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    vault_lookup_session = property(fget=get_vault_lookup_session)

    def get_vault_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'VaultAdminSession')(
                self._provider_manager.get_vault_admin_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    vault_admin_session = property(fget=get_vault_admin_session)

    def get_authorization_batch_manager(self):
        raise Unimplemented()

    authorization_batch_manager = property(fget=get_authorization_batch_manager)

    def get_authorization_rules_manager(self):
        raise Unimplemented()

    authorization_rules_manager = property(fget=get_authorization_rules_manager)


class AuthorizationProxyManager(osid_managers.OsidProxyManager, AuthorizationProfile, authorization_managers.AuthorizationProxyManager):
    """Adapts underlying AuthorizationProxyManager methodswith authorization checks."""


    def __init__(self):
        AuthorizationProfile.__init__(self, 'AuthorizationProxyManager')


    def initialize(self, runtime):
        osid_managers.OsidProxyManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:authorizationProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_proxy_manager('AUTHORIZATION', provider_impl) # need to add version
            argument


    def get_authorization_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AuthorizationSession')(
                self._provider_manager.get_authorization_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_authorization_session_for_vault(self, vault_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AuthorizationSession')(
                self._provider_manager.get_authorization_session_for_vault(vault_id, proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_authorization_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_authorization_query_session(proxy)
            query_session.use_federated_vault_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AuthorizationLookupSession')(
                self._provider_manager.get_authorization_lookup_session(proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_authorization_lookup_session_for_vault(self, vault_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_authorization_query_session_for_vault(vault_id, proxy)
            query_session.use_federated_vault_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AuthorizationLookupSession')(
                self._provider_manager.get_authorization_lookup_session_for_vault(vault_id, proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_authorization_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AuthorizationAdminSession')(
                self._provider_manager.get_authorization_admin_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_authorization_admin_session_for_vault(self, vault_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AuthorizationAdminSession')(
                self._provider_manager.get_authorization_admin_session_for_vault(vault_id, proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_vault_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'VaultLookupSession')(
                self._provider_manager.get_vault_lookup_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_vault_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'VaultAdminSession')(
                self._provider_manager.get_vault_admin_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_authorization_batch_proxy_manager(self):
        raise Unimplemented()

    authorization_batch_proxy_manager = property(fget=get_authorization_batch_proxy_manager)

    def get_authorization_rules_proxy_manager(self):
        raise Unimplemented()

    authorization_rules_proxy_manager = property(fget=get_authorization_rules_proxy_manager)


