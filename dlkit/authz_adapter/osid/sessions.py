"""AuthZ Adapter implementations of osid sessions."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification



from ...abstract_osid.osid import sessions as abc_osid_sessions
from ..osid.osid_errors import IllegalState, Unimplemented
from ..primitives import Id


COMPARATIVE = 0
PLENARY = 1
FEDERATED = 0
ISOLATED = 1




class OsidSession(abc_osid_sessions.OsidSession):
    """Adapts underlying OsidSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        self._provider_session = provider_session
        self._authz_session = authz_session
        self._proxy = proxy
        self._id_namespace = None
        self._qualifier_id = None
        self._object_view = COMPARATIVE
        self._catalog_view = FEDERATED


    def _can(self, func_name, qualifier_id=None):
        """Tests if the named function is authorized with agent and qualifier."""
        function_id = Id(
            identifier=func_name,
            namespace=self._id_namespace,
            authority='ODL.MIT.EDU')
        if qualifier_id is None:
            qualifier_id = self._qualifier_id
        return self._authz_session.is_authorized(
            agent_id=self.get_effective_agent_id(),
            function_id=function_id,
            qualifier_id=qualifier_id)


    def _use_comparative_object_view(self):
        self._object_view = COMPARATIVE


    def _use_plenary_object_view(self):
        self._object_view = PLENARY


    def _is_comparative_object_view(self):
        return not bool(self._object_view)


    def _is_plenary_object_view(self):
        return bool(self._object_view)


    def _use_federated_catalog_view(self):
        self._catalog_view = FEDERATED


    def _use_isolated_catalog_view(self):
        self._catalog_view = ISOLATED


    def _is_federated_catalog_view(self):
        return not bool(self._catalog_view)


    def _is_isolated_catalog_view(self):
        return bool(self._catalog_view)


    def get_locale(self):
        pass

    locale = property(fget=get_locale)

    def is_authenticated(self):
        if self._proxy is None:
            return False
        elif self._proxy.has_authentication():
            return self._proxy.get_authentication().is_valid()
        else:
            return False

    def get_authenticated_agent_id(self):
        if self.is_authenticated():
            return self._proxy.get_authentication().get_agent_id()
        else:
            raise IllegalState()

    authenticated_agent_id = property(fget=get_authenticated_agent_id)

    def get_authenticated_agent(self):
        if self.is_authenticated():
            return self._proxy.get_authentication().get_agent()
        else:
            raise IllegalState()

    authenticated_agent = property(fget=get_authenticated_agent)

    def get_effective_agent_id(self):
        if self.is_authenticated():
            if self._proxy.has_effective_agent():
                return self._proxy.get_effective_agent_id()
            else:
                return self._proxy.get_authentication().get_agent_id()
        else:
            return Id(
                identifier='MC3GUE$T@MIT.EDU',
                namespace='agent.Agent',
                authority='MIT-OEIT')

    effective_agent_id = property(fget=get_effective_agent_id)

    def get_effective_agent(self):
        #effective_agent_id = self.get_effective_agent_id()
        # This may want to be extended to get the Agent directly from the Authentication
        # if available and if not effective agent is available in the proxy
        #return Agent(
        #    identifier=effective_agent_id.get_identifier(),
        #    namespace=effective_agent_id.get_namespace(),
        #    authority=effective_agent_id.get_authority())
        raise Unimplemented()

    effective_agent = property(fget=get_effective_agent)

    def get_date(self):
        raise Unimplemented()

    date = property(fget=get_date)

    def get_clock_rate(self):
        raise Unimplemented()

    clock_rate = property(fget=get_clock_rate)

    def get_format_type(self):
        raise Unimplemented()

    format_type = property(fget=get_format_type)

    def supports_transactions(self):
        raise Unimplemented()

    def start_transaction(self):
        raise Unimplemented()


