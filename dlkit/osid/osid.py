
from ..osid import markers as osid_markers
from ..osid import rules as osid_rules


class OsidPrimitive:
    """A marker interface for an interface that behaves like a language primitive.

    Primitive types, such as numbers and strings, do not encapsulate
    behaviors supplied by an OSID Provider. More complex primitives are
    expressed through interface definitions but are treated in a similar
    fashion as a language primitive. OSID Primitives supplied by an OSID
    Consumer must be consumable by any OSID Provider.

    """
    pass



class Identifiable:
    """A marker interface for objects uniquely identified with an OSID ``Id``."""

    def __init__(self, osid_object): # I will never be called :(
        self._osid_object = osid_object

    def get_id(self):
        """Gets the Id associated with this instance of this OSID object.

        Persisting any reference to this object is done by persisting
        the Id returned from this method. The Id returned may be
        different than the Id used to query this object. In this case,
        the new Id should be preferred over the old one for future
        queries.

        :return: the ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: The ``Id`` is intended to be constant
        and persistent. A consumer may at any time persist the ``Id``
        for retrieval at any future time. Ideally, the Id should
        consistently resolve into the designated object and not be
        reused. In cases where objects are deactivated after a certain
        lifetime the provider should endeavor not to obliterate the
        object or its ``Id`` but instead should update the properties of
        the object including the deactiavted status and the elimination
        of any unwanted pieces of data. As such, there is no means for
        updating an ``Id`` and providers should consider carefully the
        identification scheme to implement.  ``Id`` assignments for
        objects are strictly in the realm of the provider and any errors
        should be fixed directly with the backend supporting system.
        Once an Id has been assigned in a production service it should
        be honored such that it may be necessary for the backend system
        to support Id aliasing to redirect the lookup to the current
        ``Id``. Use of an Id OSID may be helpful to accomplish this task
        in a modular manner.

        """
        return # osid.id.Id

    id_ = property(fget=get_id)

    ident = property(fget=get_id)

    def is_current(self):
        """Tests to see if the last method invoked retrieved up-to-date data.

        Simple retrieval methods do not specify errors as, generally,
        the data is retrieved once at the time this object is
        instantiated. Some implementations may provide real-time data
        though the application may not always care. An implementation
        providing a real-time service may fall back to a previous
        snapshot in case of error. This method returns false if the data
        last retrieved was stale.

        :return: ``true`` if the last data retrieval was up to date, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: Providers should return false unless all
        getters are implemented using real-time queries, or some trigger
        process keeps the data in this object current. Providers should
        populate basic data elements at the time this object is
        instantiated, or set an error, to ensure some data availability.

        """
        return # boolean


class Extensible:
    """A marker interface for objects that contain ``OsidRecords``."""

    def __init__(self, osid_object): # I will never be called :(
        self._osid_object = osid_object

    def get_record_types(self):
        """Gets the record types available in this object.

        A record ``Type`` explicitly indicates the specification of an
        interface to the record. A record may or may not inherit other
        record interfaces through interface inheritance in which case
        support of a record type may not be explicit in the returned
        list. Interoperability with the typed interface to this object
        should be performed through ``hasRecordType()``.

        :return: the record types available
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    record_types = property(fget=get_record_types)

    def has_record_type(self, record_type):
        """Tests if this object supports the given record ``Type``.

        The given record type may be supported by the object through
        interface/type inheritence. This method should be checked before
        retrieving the record interface.

        :param record_type: a type
        :type record_type: ``osid.type.Type``
        :return: ``true`` if a record of the given record ``Type`` is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


class Browsable:
    """A marker interface for objects that offer property inspection."""

    def __init__(self, osid_object): # I will never be called :(
        self._osid_object = osid_object

    def get_properties(self):
        """Gets a list of properties.

        Properties provide a means for applications to display a
        representation of the contents of a record without understanding
        its ``Type`` specification. Applications needing to examine a
        specific property should use the extension interface defined by
        its ``Type``.

        :return: a list of properties
        :rtype: ``osid.PropertyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- an authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.PropertyList

    properties = property(fget=get_properties)

    def get_properties_by_record_type(self, record_type):
        """Gets a list of properties corresponding to the specified record type.

        Properties provide a means for applications to display a
        representation of the contents of a record without understanding
        its record interface specification. Applications needing to
        examine a specific propertyshould use the methods defined by the
        record ``Type``. The resulting set includes properties specified
        by parents of the record ``type`` in the case a record's
        interface extends another.

        :param record_type: the record type corresponding to the properties set to retrieve
        :type record_type: ``osid.type.Type``
        :return: a list of properties
        :rtype: ``osid.PropertyList``
        :raise: ``NullArgument`` -- ``record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- an authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.PropertyList


class Suppliable:
    """A marker interface for OSID Provider-owned objects used to supply input from an OSID Consumer."""
    pass



class Temporal:
    """``Temporal`` is used to indicate the object endures for a period of time."""

    def is_effective(self):
        """Tests if the current date is within the start end end dates inclusive.

        :return: ``true`` if this is effective, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_start_date(self):
        """Gets the start date.

        :return: the start date
        :rtype: ``osid.calendaring.DateTime``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.DateTime

    start_date = property(fget=get_start_date)

    def get_end_date(self):
        """Gets the end date.

        :return: the end date
        :rtype: ``osid.calendaring.DateTime``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.DateTime

    end_date = property(fget=get_end_date)


class Subjugateable:
    """A ``Subjugateable`` is an ``OsidObject`` dependent upon another ``OsidObject``.

    A ``Subjugateable`` is created in the context of the administering
    ``OsidObject`` that may not be reassigned.

    A ``Subjugateable`` always has a fixed Id of it administering
    ``OsidObject``.

    """
    pass



class Aggregateable:
    """``Aggregateable`` is used for an ``OsidObject`` to indicate that some or all of the definition is based on an
        included
        set of other ``OsidObjects`` which are directly accessible and do not exist outside the context of the parent
        object.

    ``Aggregateables`` allow for an ``OsidObject`` to stand alone
    without knowledge of the originating service.

    An ``Asset`` is an example of an aggregate by including the
    ``AssetContents``. An Asset also contains a provider however in this
    case the provider is categorized as a simple data attribute of the
    ``Asset`` that can be changed by updating the ``Asset`` using an
    ``AssetForm``. The ``AssetContent`` differs in there exists a
    explicit mapping to the ``Asset`` managed through an ``OsidSession``
    but accessible directly within the ``Asset`` to enable its
    consumption outside the Repository OSID.

    This marker has little practicality other than to identify a service
    pattern that is neither a data attribute nor a separately accessible
    relationship or mapping.

    """
    pass



class Containable:
    """A ``Containable`` is a kind of aggregate where an ``OsidObject`` is defined as a recursive composition of itself
        directly accessible without knowledge of the originating service."""

    def is_sequestered(self):
        """Tests if this ``Containable`` is sequestered in that it should not appear outside of its aggregated
        composition.

        :return: ``true`` if this containable is sequestered, ``false`` if this containable may appear outside its
        aggregate
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


class Sourceable:
    """``Sourceble`` is used for ``OsidObjects`` where information about a provider is appropriate.

    Examples of ``Sourceables`` are catalogs, compositions, and
    services.

    """

    def __init__(self, osid_object): # I will never be called :(
        self._osid_object = osid_object

    def get_provider_id(self):
        """Gets the ``Id`` of the provider.

        :return: the provider ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    provider_id = property(fget=get_provider_id)

    def get_provider(self):
        """Gets the ``Resource`` representing the provider.

        :return: the provider
        :rtype: ``osid.resource.Resource``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Resource

    provider = property(fget=get_provider)

    def get_branding_ids(self):
        """Gets the branding asset ``Ids``.

        :return: a list of asset ``Ids``
        :rtype: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    branding_ids = property(fget=get_branding_ids)

    def get_branding(self):
        """Gets a branding, such as an image or logo, expressed using the ``Asset`` interface.

        :return: a list of assets
        :rtype: ``osid.repository.AssetList``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetList

    branding = property(fget=get_branding)

    def get_license(self):
        """Gets the terms of usage.

        An empty license means the terms are unknown.

        :return: the license
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    license_ = property(fget=get_license)


class Federateable:
    """``Federateable`` is used to indicate an ``OsidObject`` can be federated using the OSID Hierarchy pattern.

    An OSID federation of ``OsidObjects`` is where it is inferred from
    the hiererarchy that any ``OsidObject`` "includes" its children.

    """
    pass



class Operable:
    """``Operable`` is used to indicate an ``OsidObject`` performs operations.

    The active status indicates if the ``Operable`` is on or off. The
    active status is determined from the operational status and the
    enabling rules.

    The operational status indicates the Operable is functioning. This
    status is not set administratively but instead refelects suitable
    conditions for operation.

    Operables may be administratively turned on of off through the
    enabled and disabled administrative overrides. If there are no
    related ``OsidEnabler`` rules, then ``is_enabled()`` should be set
    to ``true`` and ``is_disabled()`` set to ``false`` for the
    ``Operable`` to be on and ``is_enabled()`` set to ``false`` and
    ``is_disabled()`` set to true for the ``Operable`` to be ``off``.
    ``is_enabled()`` and ``is_disabled()`` cannot both be ``tru`` e.

    If there are related ``OsidEnabler`` rules, the active status of at
    least one ``OsidEnabler`` results in a ``true`` value for
    ``isOperational()``. This active status can be overridden by setting
    ``is_disabled()`` to ``true``. If there are no active
    ``OsidEnabler`` rules, ``is_operational()`` is false resulting in an
    ``off``  ``Operable`` unless ``is_enabled()`` is ``true`` .

    For the active status to be completely determined by the
    ``OsidEnablers,`` both ``is_enabled()`` and ``is_disabled()`` should
    be ``false`` where the ``is_active()`` status is completely driven
    from ``isOperational()``.

    """

    def is_active(self):
        """Tests if this operable is active.

        ``is_active()`` is ``true`` if ``is_operational()`` is ``true``
        and ``is_disabled()`` is ``false,`` or ``is_enabled()`` is
        ``true``.

        :return: ``true`` if this operable is on, ``false`` if it is off
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def is_enabled(self):
        """Tests if this operable is administravely enabled.

        Administratively enabling overrides any applied ``OsidEnabler``.
        If this method returns ``true`` then ``is_disabled()`` must
        return ``false``.

        :return: ``true`` if this operable is enabled, ``false`` if the active status is determined by other rules
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def is_disabled(self):
        """Tests if this operable is administravely disabled.

        Administratively disabling overrides any applied
        ``OsidEnabler``. If this method returns ``true`` then
        ``is_enabled()`` must return ``false``.

        :return: ``true`` if this operable is disabled, ``false`` if the active status is determined by other rules
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def is_operational(self):
        """Tests if this ``Operable`` is operational.

        This Operable is operational if any of the applied
        ``OsidEnablers`` are ``true``.

        :return: ``true`` if this operable is operational, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


class OsidProfile(osid_markers.Sourceable):
    """The ``OsidProfile`` defines the interoperability areas of an OSID.

    An ``OsidProfile`` is implemented by an ``OsidManager``. The top
    level ``OsidProfile`` tests for version compatibility. Each OSID
    extends this interface to include its own interoperability
    definitions within its managers.

    """

    def __init__(self):
        self._provider_manager = None

    def get_id(self):
        """Gets an identifier for this service implementation.

        The identifier is unique among services but multiple
        instantiations of the same service use the same ``Id``. This
        identifier is the same identifier used in managing OSID
        installations.

        :return: the ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    id_ = property(fget=get_id)

    ident = property(fget=get_id)

    def get_display_name(self):
        """Gets a display name for this service implementation.

        :return: a display name
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    display_name = property(fget=get_display_name)

    def get_description(self):
        """Gets a description of this service implementation.

        :return: a description
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    description = property(fget=get_description)

    def get_version(self):
        """Gets the version of this service implementation.

        :return: the service implementation version
        :rtype: ``osid.installation.Version``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.installation.Version

    version = property(fget=get_version)

    def get_release_date(self):
        """Gets the date this service implementation was released.

        :return: the release date
        :rtype: ``osid.calendaring.DateTime``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.DateTime

    release_date = property(fget=get_release_date)

    def supports_osid_version(self, version):
        """Test for support of an OSID specification version.

        :param version: the specification version to test
        :type version: ``osid.installation.Version``
        :return: ``true`` if this manager supports the given OSID version, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: An implementation may support multiple
        versions of an OSID.

        """
        return # boolean

    def get_locales(self):
        """Gets the locales supported in this service.

        :return: list of locales supported
        :rtype: ``osid.locale.LocaleList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.LocaleList

    locales = property(fget=get_locales)

    def supports_journal_rollback(self):
        """Test for support of a journaling rollback service.

        :return: ``true`` if this manager supports the journal rollback, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_journal_branching(self):
        """Test for support of a journal branching service.

        :return: ``true`` if this manager supports the journal branching, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_branch_id(self):
        """Gets the ``Branch Id`` representing this service branch.

        :return: the branch ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``Unimplemented`` -- ``supports_journal_branching()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    branch_id = property(fget=get_branch_id)

    def get_branch(self):
        """Gets this service branch.

        :return: the service branch
        :rtype: ``osid.journaling.Branch``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_journal_branching()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.journaling.Branch

    branch = property(fget=get_branch)

    def get_proxy_record_types(self):
        """Gets the proxy record ``Types`` supported in this service.

        If no proxy manager is available, an empty list is returned.

        :return: list of proxy record types supported
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    proxy_record_types = property(fget=get_proxy_record_types)

    def supports_proxy_record_type(self, proxy_record_type):
        """Test for support of a proxy type.

        :param proxy_record_type: a proxy record type
        :type proxy_record_type: ``osid.type.Type``
        :return: ``true`` if this service supports the given proxy record type, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``proxy_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


class OsidManager(OsidProfile):
    """The ``OsidManager`` is the top level interface for all OSID managers.

    An OSID manager is instantiated through the ``OsidRuntimeManager``
    and represents an instance of a service. An OSID manager is
    responsible for implementing a profile for a service and creating
    sessions that, in general, correspond to the profile. An application
    need only create a single ``OsidManager`` per service and
    implementors must ensure the ``OsidManager`` is thread-safe ````.
    The ``OsidSessions`` spawned from an OSID manager are dedicated to
    single processing threads. The ``OsidManager`` defines methods in
    common throughout all OSID managers which implement this interface.

    """

    def initialize(self, runtime):
        """Initializes this manager.

        A manager is initialized once at the time of creation.

        :param runtime: the runtime environment
        :type runtime: ``osid.OsidRuntimeManager``
        :raise: ``ConfigurationError`` -- an error with implementation configuration
        :raise: ``IllegalState`` -- this manager has already been initialized by the ``OsidRuntime``
        :raise: ``NullArgument`` -- ``runtime`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: In addition to loading its runtime
        configuration an implementation may create shared resources such
        as connection pools to be shared among all sessions of this
        service and released when this manager is closed. Providers must
        thread-protect any data stored in the manager.  To maximize
        interoperability, providers should not honor a second call to
        ``initialize()`` and must set an ``IllegalState`` error.

        """
        pass

    def rollback_service(self, rollback_time):
        """Rolls back this service to a point in time.

        :param rollback_time: the requested time
        :type rollback_time: ``timestamp``
        :return: the journal entry corresponding to the actual state of this service
        :rtype: ``osid.journaling.JournalEntry``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unimplemented`` -- ``supports_journal_rollback()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.journaling.JournalEntry

    def change_branch(self, branch_id):
        """Changes the service branch.

        :param branch_id: the new service branch
        :type branch_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``branch_id`` not found
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unimplemented`` -- ``supports_journal_branching()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class OsidProxyManager(OsidProfile):
    """The ``OsidProxyManager`` is the top level interface for all OSID proxy managers.

    A proxy manager accepts parameters to pass through end-user
    authentication credentials and other necessary request parameters in
    a server environment. Native applications should use an
    ``OsidManager`` to maintain a higher degree of interoperability by
    avoiding this coupling.

    An OSID proxy manager is instantiated through the
    ``OsidRuntimeManager`` and represents an instance of a service. An
    OSID manager is responsible for defining clusters of
    interoperability within a service and creating sessions that
    generally correspond to these clusters, An application need only
    create a single ``OsidProxyManager`` per service and implementors
    must ensure the ``OsidProxyManager`` is thread-safe ````. The
    ``OsidSessions`` spawned from an OSID manager are dedicated to
    single processing threads. The ``OsidProxyManager`` defines methods
    in common throughout all OSID managers which implement this
    interface.

    """

    def initialize(self, runtime):
        """Initializes this manager.

        A manager is initialized once at the time of creation.

        :param runtime: the runtime environment
        :type runtime: ``osid.OsidRuntimeManager``
        :raise: ``ConfigurationError`` -- an error with implementation configuration
        :raise: ``IllegalState`` -- this manager has already been initialized by the ``OsidRuntime``
        :raise: ``NullArgument`` -- ``runtime`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: In addition to loading its runtime
        configuration an implementation may create shared resources such
        as connection pools to be shared among all sessions of this
        service and released when this manager is closed. Providers must
        thread-protect any data stored in the manager.  To maximize
        interoperability, providers should not honor a second call to
        ``initialize()`` and must set an ``IllegalState`` error.

        """
        pass

    def rollback_service(self, rollback_time, proxy):
        """Rolls back this service to a point in time.

        :param rollback_time: the requested time
        :type rollback_time: ``timestamp``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: the journal entry corresponding to the actual state of this service
        :rtype: ``osid.journaling.JournalEntry``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unimplemented`` -- ``supports_journal_rollback()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.journaling.JournalEntry

    def change_branch(self, branch_id, proxy):
        """Changes the service branch.

        :param branch_id: the new service branch
        :type branch_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :raise: ``NotFound`` -- ``branch_id`` not found
        :raise: ``NullArgument`` -- ``branch_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unimplemented`` -- ``supports_journal_branching()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class OsidSession:
    """The ``OsidSession`` is the top level interface for all OSID sessions.

    An ``OsidSession`` is created through its corresponding
    ``OsidManager``. A new ``OsidSession`` should be created for each
    user of a service and for each processing thread. A session
    maintains a single authenticated user and is not required to ensure
    thread-protection. A typical OSID session defines a set of service
    methods corresponding to some compliance level as defined by the
    service and is generally responsible for the management and
    retrieval of ``OsidObjects``.

    ``OsidSession`` defines a set of common methods used throughout all
    OSID sessions. An OSID session may optionally support transactions
    through the transaction interface.

    """


    COMPARATIVE = 0
    PLENARY = 1
    FEDERATED = 0
    ISOLATED = 1

    def __init__(self, proxy):
        self._proxy = proxy

    def get_locale(self):
        """Gets the locale indicating the localization preferences in effect for this session.

        :return: the locale
        :rtype: ``osid.locale.Locale``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.Locale

    locale = property(fget=get_locale)

    def is_authenticated(self):
        """Tests if an agent is authenticated to this session.

        :return: ``true`` if valid authentication credentials exist, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_authenticated_agent_id(self):
        """Gets the ``Id`` of the agent authenticated to this session.

        This is the agent for which credentials are used either acquired
        natively or via an ``OsidProxyManager``.

        :return: the authenticated agent ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``is_authenticated()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    authenticated_agent_id = property(fget=get_authenticated_agent_id)

    def get_authenticated_agent(self):
        """Gets the agent authenticated to this session.

        This is the agent for which credentials are used either acquired
        natively or via an ``OsidProxyManager``.

        :return: the authenticated agent
        :rtype: ``osid.authentication.Agent``
        :raise: ``IllegalState`` -- ``is_authenticated()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.Agent

    authenticated_agent = property(fget=get_authenticated_agent)

    def get_effective_agent_id(self):
        """Gets the ``Id`` of the effective agent in use by this session.

        If ``is_authenticated()`` is true, then the effective agent may
        be the same as the agent returned by
        ``getAuthenticatedAgent()``. If ``is_authenticated()`` is
        ``false,`` then the effective agent may be a default agent used
        for authorization by an unknwon or anonymous user.

        :return: the effective agent
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    effective_agent_id = property(fget=get_effective_agent_id)

    def get_effective_agent(self):
        """Gets the effective agent in use by this session.

        If ``is_authenticated()`` is true, then the effective agent may
        be the same as the agent returned by
        ``getAuthenticatedAgent()``. If ``is_authenticated()`` is
        ``false,`` then the effective agent may be a default agent used
        for authorization by an unknwon or anonymous user.

        :return: the effective agent
        :rtype: ``osid.authentication.Agent``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.Agent

    effective_agent = property(fget=get_effective_agent)

    def get_date(self):
        """Gets the service date which may be the current date or the effective date in which this session exists.

        :return: the service date
        :rtype: ``timestamp``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # timestamp

    date = property(fget=get_date)

    def get_clock_rate(self):
        """Gets the rate of the service clock.

        :return: the clock rate
        :rtype: ``decimal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # decimal

    clock_rate = property(fget=get_clock_rate)

    def get_format_type(self):
        """Gets the ``DisplayText`` format ``Type`` preference in effect for this session.

        :return: the effective ``DisplayText`` format ``Type``
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    format_type = property(fget=get_format_type)

    def supports_transactions(self):
        """Tests for the availability of transactions.

        :return: ``true`` if transaction methods are available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def start_transaction(self):
        """Starts a new transaction for this sesson.

        Transactions are a means for an OSID to provide an all-or-
        nothing set of operations within a session and may be used to
        coordinate this service from an external transaction manager. A
        session supports one transaction at a time. Starting a second
        transaction before the previous has been committed or aborted
        results in an ``IllegalState`` error.

        :return: a new transaction
        :rtype: ``osid.transaction.Transaction``
        :raise: ``IllegalState`` -- a transaction is already open
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- transactions not supported

        *compliance: optional -- This method must be implemented if
        ``supports_transactions()`` is true.*
        *implementation notes*: Ideally, a provider that supports
        transactions should guarantee atomicity, consistency, isolation
        and durability in a 2 phase commit process. This is not always
        possible in distributed systems and a transaction provider may
        simply allow for a means of processing bulk updates.  To
        maximize interoperability, providers should honor the one-
        transaction-at-a-time rule.

        """
        return # osid.transaction.Transaction


class OsidObject(osid_markers.Identifiable, osid_markers.Extensible, osid_markers.Browsable):
    """``OsidObject`` is the top level interface for all OSID Objects.

    An OSID Object is an object identified by an OSID ``Id`` and may
    implements optional interfaces. OSID Objects also contain a display
    name and a description. These fields are required but may be used
    for a variety of purposes ranging from a primary name and
    description of the object to a more user friendly display of various
    attributes.

    Creation of OSID Objects and the modification of their data is
    managed through the associated ``OsidSession`` which removes the
    dependency of updating data elements upon object retrieval.The
    ``OsidManager`` should be used to test if updates are available and
    determine what ``PropertyTypes`` are supported. The ``OsidManager``
    is also used to create the appropriate ``OsidSession`` for object
    creation, updates and deletes.

    All ``OsidObjects`` are identified by an immutable ``Id``. An ``Id``
    is assigned to an object upon creation of the object and cannot be
    changed once assigned.

    An ``OsidObject`` may support one or more supplementary records
    which are expressed in the form of interfaces. Each record interface
    is identified by a Type. A record interface may extend another
    record interface where support of the parent record interface is
    implied. In this case of interface inheritance, support of the
    parent record type may be implied through ``has_record_type()`` and
    not explicit in ``getRecordTypes()``.

    For example, if recordB extends recordA, typeB is a child of typeA.
    If a record implements typeB, than it also implements typeA. An
    application that only knows about typeA retrieves recordA. An
    application that knows about typeB, retrieves recordB which is the
    union of methods specified in typeA and typeB. If an application
    requests typeA, it may not attempt to access methods defined in
    typeB as they may not exist until explicitly requested. The
    mechanics of this polymorphism is defined by the language binder.
    One mechanism might be the use of casting.

    In addition to the record ``Types,`` OSID Objects also have a genus
    ``Type``. A genus ``Type`` indicates a classification or kind of the
    object where an "is a" relationship exists. The purpose of of the
    genus ``Type`` is to avoid the creation of unnecessary record types
    that may needlessly complicate an interface hierarchy or introduce
    interoperability issues. For example, an OSID object may have a
    record ``Type`` of ``Publication`` that defines methods pertinent to
    publications, such as an ISBN number. A provider may wish to
    distinguish between books and journals without having the need of
    new record interfaces. In this case, the genus ``Type`` may be one
    of ``Book`` or ``Journal``. While this distinction can aid a search,
    these genres should be treated in such a way that do not introduce
    interoperability problems.

    Like record Types, the genus Types may also exist in an implicit
    type hierarchy. An OSID object always has at least one genus. Genus
    types should not be confused with subject tagging, which is managed
    externally to the object. Unlike record ``Types,`` an object's genus
    may be modified. However, once an object's record is created with a
    record ``Type,`` it cannot be changed.

    Methods that return values are not permitted to return nulls. If a
    value is not set, it is indicated in the ``Metadata`` of the update
    form.

    """

    def __init__(self, osid_object):
        self._osid_object = osid_object

    def get_display_name(self):
        """Gets the preferred display name associated with this instance of this OSID object appropriate for display to
        the user.

        :return: the display name
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: A display name is a string used for
        identifying an object in human terms. A provider may wish to
        initialize the display name based on one or more object
        attributes. In some cases, the display name may not map to a
        specific or significant object attribute but simply be used as a
        preferred display name that can be modified. A provider may also
        wish to translate the display name into a specific locale using
        the Locale service. Some OSIDs define methods for more detailed
        naming.

        """
        return # osid.locale.DisplayText

    display_name = property(fget=get_display_name)

    def get_description(self):
        """Gets the description associated with this instance of this OSID object.

        :return: the description
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: A description is a string used for
        describing an object in human terms and may not have
        significance in the underlying system. A provider may wish to
        initialize the description based on one or more object
        attributes and/or treat it as an auxiliary piece of data that
        can be modified. A provider may also wish to translate the
        description into a specific locale using the Locale service.

        """
        return # osid.locale.DisplayText

    description = property(fget=get_description)

    def get_genus_type(self):
        """Gets the genus type of this object.

        :return: the genus type of this object
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    genus_type = property(fget=get_genus_type)

    def is_of_genus_type(self, genus_type):
        """Tests if this object is of the given genus ``Type``.

        The given genus type may be supported by the object through the
        type hierarchy.

        :param genus_type: a genus type
        :type genus_type: ``osid.type.Type``
        :return: ``true`` if this object is of the given genus ``Type,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``genus_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


class OsidCatalog(OsidObject, osid_markers.Sourceable, osid_markers.Federateable):
    """``OsidCatalog`` is the top level interface for all OSID catalog-like objects.

    A catalog relates to other OSID objects for the purpose of
    organization and federation and almost always are hierarchical. An
    example catalog is a ``Repository`` that relates to a collection of
    ``Assets``.

    ``OsidCatalogs`` allow for the retrieval of a provider identity and
    branding.

    Collections visible through an ``OsidCatalog`` may be the output of
    a dynamic query or some other rules-based evaluation. The facts
    surrounding the evaluation are the ``OsidObjects`` visible to the
    ``OsidCatalog`` from its position in the federated hierarchy. The
    input conditions may satisifed on a service-wide basis using an
    ``OsidQuery`` or environmental conditions supplied to the services
    via a ``Proxy`` .

    Often, the selection of an ``OsidCatalog`` in instantiating an
    ``OsidSession`` provides access to a set of ``OsidObjects`` .
    Because the view inside an ``OsidCatalog`` can also be produced
    behaviorally using a rules evaluation, the ``Id`` (or well-known
    alias) of the ``OsidCatalog`` may be used as an abstract means of
    requesting a predefined set of behaviors or data constraints from an
    OSID Provider.

    The flexibility of interpretation together with its central role in
    federation to build a rich and complex service from a set of
    individual OSID Providers makes cataloging an essential pattern to
    achieve abstraction from implementations in the OSIDs without loss
    of functionality. Most OSIDs include a cataloging pattern.

    """
    pass



class OsidList:
    """``OsidList`` is the top-level interface for all OSID lists.

    An OSID list provides sequential access, one at a time or many at a
    time, access to a set of elements. These elements are not required
    to be OsidObjects but generally are. The element retrieval methods
    are defined in the sub-interface of ``OsidList`` where the
    appropriate return type is defined.

    Osid lists are a once pass through iteration of elements. The size
    of the object set and the means in which the element set is
    generated or stored is not known. Assumptions based on the length of
    the element set by copying the entire contents of the list into a
    fixed buffer should be done with caution a awareness that an
    implementation may return a number of elements ranging from zero to
    infinity.

    Lists are returned by methods when multiple return values are
    possible. There is no guarantee that successive calls to the same
    method will return the same set of elements in a list. Unless an
    order is specified in an interface definition, the order of the
    elements is not known.

    """

    def __init__(self, iter_object=None, count=None):
        if iter_object is None:
            iter_object = []
        if count != None:
            self._count = count
        elif isinstance(iter_object, dict) or isinstance(iter_object, list):
            self._count = len(iter_object)
        self._iter_object = iter(iter_object)

    def __iter__(self):
        return self

    def next(self):
        try:
            next_object = self._iter_object.next()
        except:
            raise
        if self._count != None:
            self._count -= 1
        return next_object

    def len(self):
        return self.available()

    def has_next(self):
        """Tests if there are more elements in this list.

        :return: ``true`` if more elements are available in this list, ``false`` if the end of the list has been reached
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: Any errors that may result from accesing
        the underlying set of elements are to be deferred until the
        consumer attempts retrieval in which case the provider must
        return ``true`` for this method.

        """
        return # boolean

    def available(self):
        """Gets the number of elements available for retrieval.

        The number returned by this method may be less than or equal to
        the total number of elements in this list. To determine if the
        end of the list has been reached, the method ``has_next()``
        should be used. This method conveys what is known about the
        number of remaining elements at a point in time and can be used
        to determine a minimum size of the remaining elements, if known.
        A valid return is zero even if ``has_next()`` is true.

        This method does not imply asynchronous usage. All OSID methods
        may block.

        :return: the number of elements available for retrieval
        :rtype: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: Any errors that may result from accesing
        the underlying set of elements are to be deferred until the
        consumer attempts retrieval in which case the provider must
        return a positive integer for this method so the consumer can
        continue execution to receive the error. In all other
        circumstances, the provider must not return a number greater
        than the number of elements known since this number will be fed
        as a parameter to the bulk retrieval method.

        """
        return # cardinal

    def skip(self, n):
        """Skip the specified number of elements in the list.

        If the number skipped is greater than the number of elements in
        the list, hasNext() becomes false and available() returns zero
        as there are no more elements to retrieve.

        :param n: the number of elements to skip
        :type n: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class OsidRuntimeProfile(OsidProfile):
    """The ``OsidRuntimeProfile`` defines the service aspects of the OSID runtime service."""

    def supports_configuration(self):
        """Tests if a configuration service is provided within this runtime environment.

        :return: ``true`` if a configuration service is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


class OsidRuntimeManager(OsidManager, OsidRuntimeProfile):
    """The ``OsidRuntimeManager`` represents and OSID platform and contains the information required for running OSID
        implementations such as search paths and configurations."""

    def get_manager(self, osid, impl_class_name, version):
        """Finds, loads and instantiates providers of OSID managers.

        Providers must conform to an OsidManager interface. The
        interfaces are defined in the OSID enumeration. For all OSID
        requests, an instance of ``OsidManager`` that implements the
        ``OsidManager`` interface is returned. In bindings where
        permitted, this can be safely cast into the requested manager.

        :param osid: represents the OSID
        :type osid: ``osid.OSID``
        :param impl_class_name: the name of the implementation
        :type impl_class_name: ``string``
        :param version: the minimum required OSID specification version
        :type version: ``osid.installation.Version``
        :return: the manager of the service
        :rtype: ``osid.OsidManager``
        :raise: ``ConfigurationError`` -- an error in configuring the implementation
        :raise: ``NotFound`` -- the implementation class was not found
        :raise: ``NullArgument`` -- ``impl_class_name`` or ``version`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``impl_class_name`` does not support the requested OSID

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: After finding and instantiating the
        requested ``OsidManager,`` providers must invoke
        ``OsidManager.initialize(OsidRuntimeManager)`` where the
        environment is an instance of the current environment that
        includes the configuration for the service being initialized.
        The ``OsidRuntimeManager`` passed may include information useful
        for the configuration such as the identity of the service being
        instantiated.

        """
        return # osid.OsidManager

    def get_proxy_manager(self, osid, implementation, version):
        """Finds, loads and instantiates providers of OSID managers.

        Providers must conform to an ``OsidManager`` interface. The
        interfaces are defined in the OSID enumeration. For all OSID
        requests, an instance of ``OsidManager`` that implements the
        ``OsidManager`` interface is returned. In bindings where
        permitted, this can be safely cast into the requested manager.

        :param osid: represents the OSID
        :type osid: ``osid.OSID``
        :param implementation: the name of the implementation
        :type implementation: ``string``
        :param version: the minimum required OSID specification version
        :type version: ``osid.installation.Version``
        :return: the manager of the service
        :rtype: ``osid.OsidProxyManager``
        :raise: ``ConfigurationError`` -- an error in configuring the implementation
        :raise: ``NotFound`` -- the implementation class was not found
        :raise: ``NullArgument`` -- ``implementation`` or ``version`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``implementation`` does not support the requested OSID

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: After finding and instantiating the
        requested ``OsidManager,`` providers must invoke
        ``OsidManager.initialize(OsidRuntimeManager)`` where the
        environment is an instance of the current environment that
        includes the configuration for the service being initialized.
        The ``OsidRuntimeManager`` passed may include information useful
        for the configuration such as the identity of the service being
        instantiated.

        """
        return # osid.OsidProxyManager

    def get_configuration(self):
        """Gets the current configuration in the runtime environment.

        :return: a configuration
        :rtype: ``osid.configuration.ValueLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- an authorization failure occured
        :raise: ``Unimplemented`` -- a configuration service is not supported

        *compliance: optional -- This method must be implemented if
        ``supports_configuration()`` is ``true``.*

        """
        return # osid.configuration.ValueLookupSession

    configuration = property(fget=get_configuration)


