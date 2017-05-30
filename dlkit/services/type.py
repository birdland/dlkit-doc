# -*- coding: utf-8 -*-
"""Type Open Service Interface Definitions
type version 3.0.0

The Type OSID defines a set of interfaces for managing ``Type``
definitions. ``Types`` are used as an identifier primarily for
identification of interface extensions throughout the OSIDs and
occasionally used as an extensible enumeration. An agreement between an
OSID Consumer and an OSID Provider means they support the same ``Type``.

Types

A ``Type`` is similar to an Id but includes other data for display and
organization. The identification portion of the Type is globally unique
and contains:

  * authority: the name of the entity or organization responsible for
    the type. Using a domain name is a reasonable convention.
  * identifier: a string serving as an id. The identifier may be a urn,
    guid, oid or some other means of identification. Since all of the
    identification elements including the domain and authority create an
    overall unique Type, the identifier may even be a sequence number
    defined within a particular domain.
  * namespace: a string identifying the namespace of the identifier,
    such as "urn" or "oid".


Example
  Type type = lookupSession.getType("asset", "uri",         
                                    "http://harvestroad.com/osidTypes/image",
                                    "harvestroad.com");
  print type.getDisplayName();



The sessions in this OSID offer the capabilities of a ``Type`` registry
to centrally manage definitions and localized display strings and
descriptions. Applications may opt to construct their own ``Types``
directly and bypass this service.

Type Hierarchies

Types are part of an internal hierarchy. A ``Type`` in a hierarchy
includes the ``Types`` of its children. For example, an ``Asset`` may
have a "photograph" ``Type`` included as part of an "image" base
``Type``.

Unless an application will display a type, it can simply construct a
type based on the identification components. OSID Providers may benefit
by using this service to manage the type hierarchy, to provide a place
to perform mappings across different type definitions, and to provide
displayable metadata to its consumers.

Type Type Relations

``Types`` may relate to other ``Types`` to describe constraints or
compositions. The relationship is expressed as another Type. For
example, a ``Position`` of type "researcher" may be appropriately
associated with an ``Organization`` of type "laboratory" using a
relation Type of "allowed." Or, a root ``Event`` type depends on a root
``TimePeriod`` type using a relationship type of "depends on."

Types for Constraints and Side Effects

An OSID Provider may link a ``Type,`` such as a genus, to a set of
constraints that are made known to the application as ``Metadata``
through an ``OsidForm``. Types of an ``OsidObject`` may also be used by
an OSID Provider to constrain the possible relationship ``Types`` that
may be possible to that ``OsidObject``. In these uses of ``Types,``
there is a semantic accompanying the ``Type`` definition managed within
an OSID Provider. The Type OSID manages the metadata of the ``Type``
itself. Logic implementing the meaning of the ``Type`` is managed
completely within an OSID Provider.

OSIDs emphasize relationships over data typing since type agreements are
often an impediment to interoperability. Generally, the rule of thumb
for record ``Types`` is to first explore other ``OsidObjects,`` even
those in other OSIDs for a place for extra data. Often, what is hiding
behind a list of data elements is a separate service that can be
provided as a separate module and serves to keep the principal
``OsidObject`` lighter and more flexible.

Genus ``Types`` primarily serve as a quick and dirty way to unclutter
the record ``Types`` with "is kind of like" tags. ``OsidCatalogs`` can
be used for a richer solution. For example, a genus ``Type`` may be used
to identify all ``Events`` on a ``Calendar`` which are classes at a
school and is accompanied by constraint logic such that the ``Events``
occur at a ``Location`` on campus.

Another pathway to explore is to create a smart ``Calendar`` from an
``EventQuery`` that specifies constrraints on the ``Event`` sponsor,
``Location,`` or other data required for classes. Creates and updates
for Events in that smart ``Calendar`` will be similarly constrained and
surfaced to the OSID Consumer through the ``Metadata`` in the
EventForms. While this path is certainly more difficult than simply
nailing up some logic indexed by a genus Type, it can be considered if
there is a need to expose the logic and authoring capabilities.

OsidPrimitives

Most OSID interfaces are used to encapsulate implementation-specific
objects from provider to consumer. ``Type`` is an ``OsidPrimitive`` and
as such cannot be used to encapsulate implementation-specific data other
than what is defined explicitly in the ``Type``. An OSID Provider must
respect any ``Type`` constructed by an OSID Consumer.

"""

from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions
from ..osid import markers as osid_markers
from ..osid import objects as osid_objects


class TypeProfile(osid_managers.OsidProfile):
    """The ``TypeProfile`` describes the interoperability among type services."""


##
# The following methods are from osid.type.TypeProfile




##
# The following methods are from osid.type.TypeManager




##
# The following methods are from osid.type.TypeProxyManager




##
# The following methods are from osid.type.Type

    def get_display_name(self):
        """Gets the full display name of this ``Type``.

        :return: the display name of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    display_name = property(fget=get_display_name)

    def get_display_label(self):
        """Gets the shorter display label for this ``Type``.

        Where a display name of a ``Type`` might be ``"`` Critical
        Logging Priority Type", the display label could be "critical".

        :return: the display label for this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    display_label = property(fget=get_display_label)

    def get_description(self):
        """Gets a description of this ``Type``.

        :return: the description of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    description = property(fget=get_description)

    def get_domain(self):
        """Gets the domain.

        The domain can provide an information label about ths
        application space of this Type.

        :return: the domain of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    domain = property(fget=get_domain)

    def get_authority(self):
        """Gets the authority of this ``Type``.

        The authority is a string used to ensure the uniqueness of this
        ``Type`` when using a non- federated identifier space.
        Generally, it is a domain name identifying the party responsible
        for this ``Type``. This method is used to compare one ``Type``
        to another.

        :return: the authority of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    authority = property(fget=get_authority)

    def get_identifier_namespace(self):
        """Gets the namespace of the identifier.

        This method is used to compare one ``Type`` to another.

        :return: the authority of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    identifier_namespace = property(fget=get_identifier_namespace)

    namespace = property(fget=get_identifier_namespace)

    def get_identifier(self):
        """Gets the identifier of this ``Type``.

        This method is used to compare one ``Type`` to another.

        :return: the identifier of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    identifier = property(fget=get_identifier)


##
# The following methods are from osid.type.TypeForm

    def get_display_name_metadata(self):
        """Gets the metadata for the display name.

        :return: metadata for the display name
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    display_name_metadata = property(fget=get_display_name_metadata)

    def set_display_name(self, display_name):
        """Sets a display name.

        :param display_name: the new display name
        :type display_name: ``string``
        :raise: ``InvalidArgument`` -- ``display_name`` is invalid
        :raise: ``NoAccess`` -- ``display_name`` cannot be modified
        :raise: ``NullArgument`` -- ``display_name`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_display_name(self):
        """Clears the display name.

        :raise: ``NoAccess`` -- ``display_name`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    display_name = property(fset=set_display_name, fdel=clear_display_name)

    def get_display_label_metadata(self):
        """Gets the metadata for the display label.

        :return: metadata for the display label
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    display_label_metadata = property(fget=get_display_label_metadata)

    def set_display_label(self, display_label):
        """Seta a display label.

        :param display_label: the new display label
        :type display_label: ``string``
        :raise: ``InvalidArgument`` -- ``display_label`` is invalid
        :raise: ``NoAccess`` -- ``display_label`` cannot be modified
        :raise: ``NullArgument`` -- ``display_label`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_display_label(self):
        """Clears the display label.

        :raise: ``NoAccess`` -- ``display_label`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    display_label = property(fset=set_display_label, fdel=clear_display_label)

    def get_description_metadata(self):
        """Gets the metadata for the description.

        :return: metadata for the description
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    description_metadata = property(fget=get_description_metadata)

    def set_description(self, description):
        """Sets a description.

        :param description: the new description
        :type description: ``string``
        :raise: ``InvalidArgument`` -- ``description`` is invalid
        :raise: ``NoAccess`` -- ``description`` cannot be modified
        :raise: ``NullArgument`` -- ``description`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_description(self):
        """Clears the description.

        :raise: ``NoAccess`` -- ``description`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    description = property(fset=set_description, fdel=clear_description)

    def get_domain_metadata(self):
        """Gets the metadata for the domain.

        :return: metadata for the domain
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    domain_metadata = property(fget=get_domain_metadata)

    def set_domain(self, domain):
        """Sets a domain.

        :param domain: the new domain
        :type domain: ``string``
        :raise: ``InvalidArgument`` -- ``domain`` is invalid
        :raise: ``NoAccess`` -- ``domain`` cannot be modified
        :raise: ``NullArgument`` -- ``domain`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_domain(self):
        """Clears the domain.

        :raise: ``NoAccess`` -- ``domain`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    domain = property(fset=set_domain, fdel=clear_domain)


##
# The following methods are from osid.type.TypeList

    def get_next_type(self):
        """Gets the next ``Type`` in this list.

        :return: the next ``Type`` in this list. The ``has_next()`` method should be used to test that a next ``Type`` is available before calling this method.
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    next_type = property(fget=get_next_type)

    def get_next_types(self, n):
        """Gets the next set of ``Types`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Type`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Type`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type




class TypeManager(osid_managers.OsidManager, osid_sessions.OsidSession, TypeProfile):
    """This manager provides access to the available sessions of the type service.

    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.

    """


    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._bin_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)
        self._sub_package_provider_managers = dict()

    def _get_provider_session(self, session):
        if session in self._provider_sessions:
            return self._provider_sessions[session]
        else:
            try:
                get_session = getattr(self._provider_manager, 'get_' + session)
            except:
                raise  # Unimplemented???
            else:
                self._provider_sessions[session] = get_session()
            return self._provider_sessions[session]

    def initialize(self, runtime):
        """OSID Manager initialize"""
        from .primitives import Id
        if self._runtime is not None:
            raise IllegalState('Manager has already been initialized')
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:typeProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        # do not account for TypeProxyManager yet...not used in Handcar
        # need to add version argument
        self._provider_manager = runtime.get_manager('TYPE', provider_impl)

    def get_types(self, *args, **kwargs):
        """Pass through to provider method"""
        # Implemented from
        # osid.type.TypeLookupSession.get_types
        return self._get_provider_session('type_lookup_session').get_types(*args, **kwargs)

    def get_type_lookup_session(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._provider_manager.get_type_lookup_session(*args, **kwargs)

    def get_type_admin_session(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._provider_manager.get_type_admin_session(*args, **kwargs)


##
# The following methods are from osid.type.TypeProfile




##
# The following methods are from osid.type.TypeManager




##
# The following methods are from osid.type.TypeProxyManager




##
# The following methods are from osid.type.Type

    def get_display_name(self):
        """Gets the full display name of this ``Type``.

        :return: the display name of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    display_name = property(fget=get_display_name)

    def get_display_label(self):
        """Gets the shorter display label for this ``Type``.

        Where a display name of a ``Type`` might be ``"`` Critical
        Logging Priority Type", the display label could be "critical".

        :return: the display label for this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    display_label = property(fget=get_display_label)

    def get_description(self):
        """Gets a description of this ``Type``.

        :return: the description of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    description = property(fget=get_description)

    def get_domain(self):
        """Gets the domain.

        The domain can provide an information label about ths
        application space of this Type.

        :return: the domain of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    domain = property(fget=get_domain)

    def get_authority(self):
        """Gets the authority of this ``Type``.

        The authority is a string used to ensure the uniqueness of this
        ``Type`` when using a non- federated identifier space.
        Generally, it is a domain name identifying the party responsible
        for this ``Type``. This method is used to compare one ``Type``
        to another.

        :return: the authority of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    authority = property(fget=get_authority)

    def get_identifier_namespace(self):
        """Gets the namespace of the identifier.

        This method is used to compare one ``Type`` to another.

        :return: the authority of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    identifier_namespace = property(fget=get_identifier_namespace)

    namespace = property(fget=get_identifier_namespace)

    def get_identifier(self):
        """Gets the identifier of this ``Type``.

        This method is used to compare one ``Type`` to another.

        :return: the identifier of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    identifier = property(fget=get_identifier)


##
# The following methods are from osid.type.TypeForm

    def get_display_name_metadata(self):
        """Gets the metadata for the display name.

        :return: metadata for the display name
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    display_name_metadata = property(fget=get_display_name_metadata)

    def set_display_name(self, display_name):
        """Sets a display name.

        :param display_name: the new display name
        :type display_name: ``string``
        :raise: ``InvalidArgument`` -- ``display_name`` is invalid
        :raise: ``NoAccess`` -- ``display_name`` cannot be modified
        :raise: ``NullArgument`` -- ``display_name`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_display_name(self):
        """Clears the display name.

        :raise: ``NoAccess`` -- ``display_name`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    display_name = property(fset=set_display_name, fdel=clear_display_name)

    def get_display_label_metadata(self):
        """Gets the metadata for the display label.

        :return: metadata for the display label
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    display_label_metadata = property(fget=get_display_label_metadata)

    def set_display_label(self, display_label):
        """Seta a display label.

        :param display_label: the new display label
        :type display_label: ``string``
        :raise: ``InvalidArgument`` -- ``display_label`` is invalid
        :raise: ``NoAccess`` -- ``display_label`` cannot be modified
        :raise: ``NullArgument`` -- ``display_label`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_display_label(self):
        """Clears the display label.

        :raise: ``NoAccess`` -- ``display_label`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    display_label = property(fset=set_display_label, fdel=clear_display_label)

    def get_description_metadata(self):
        """Gets the metadata for the description.

        :return: metadata for the description
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    description_metadata = property(fget=get_description_metadata)

    def set_description(self, description):
        """Sets a description.

        :param description: the new description
        :type description: ``string``
        :raise: ``InvalidArgument`` -- ``description`` is invalid
        :raise: ``NoAccess`` -- ``description`` cannot be modified
        :raise: ``NullArgument`` -- ``description`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_description(self):
        """Clears the description.

        :raise: ``NoAccess`` -- ``description`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    description = property(fset=set_description, fdel=clear_description)

    def get_domain_metadata(self):
        """Gets the metadata for the domain.

        :return: metadata for the domain
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    domain_metadata = property(fget=get_domain_metadata)

    def set_domain(self, domain):
        """Sets a domain.

        :param domain: the new domain
        :type domain: ``string``
        :raise: ``InvalidArgument`` -- ``domain`` is invalid
        :raise: ``NoAccess`` -- ``domain`` cannot be modified
        :raise: ``NullArgument`` -- ``domain`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_domain(self):
        """Clears the domain.

        :raise: ``NoAccess`` -- ``domain`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    domain = property(fset=set_domain, fdel=clear_domain)


##
# The following methods are from osid.type.TypeList

    def get_next_type(self):
        """Gets the next ``Type`` in this list.

        :return: the next ``Type`` in this list. The ``has_next()`` method should be used to test that a next ``Type`` is available before calling this method.
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    next_type = property(fget=get_next_type)

    def get_next_types(self, n):
        """Gets the next set of ``Types`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Type`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Type`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type




class TypeProxyManager(osid_managers.OsidProxyManager, TypeProfile):
    """This manager provides access to the available sessions of the type service.

    Methods in this manager support the passing of a ``Proxy`` object
    for the purpose of passing information from a server environment.
    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.

    """


##
# The following methods are from osid.type.TypeProfile




##
# The following methods are from osid.type.TypeManager




##
# The following methods are from osid.type.TypeProxyManager




##
# The following methods are from osid.type.Type

    def get_display_name(self):
        """Gets the full display name of this ``Type``.

        :return: the display name of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    display_name = property(fget=get_display_name)

    def get_display_label(self):
        """Gets the shorter display label for this ``Type``.

        Where a display name of a ``Type`` might be ``"`` Critical
        Logging Priority Type", the display label could be "critical".

        :return: the display label for this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    display_label = property(fget=get_display_label)

    def get_description(self):
        """Gets a description of this ``Type``.

        :return: the description of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    description = property(fget=get_description)

    def get_domain(self):
        """Gets the domain.

        The domain can provide an information label about ths
        application space of this Type.

        :return: the domain of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    domain = property(fget=get_domain)

    def get_authority(self):
        """Gets the authority of this ``Type``.

        The authority is a string used to ensure the uniqueness of this
        ``Type`` when using a non- federated identifier space.
        Generally, it is a domain name identifying the party responsible
        for this ``Type``. This method is used to compare one ``Type``
        to another.

        :return: the authority of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    authority = property(fget=get_authority)

    def get_identifier_namespace(self):
        """Gets the namespace of the identifier.

        This method is used to compare one ``Type`` to another.

        :return: the authority of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    identifier_namespace = property(fget=get_identifier_namespace)

    namespace = property(fget=get_identifier_namespace)

    def get_identifier(self):
        """Gets the identifier of this ``Type``.

        This method is used to compare one ``Type`` to another.

        :return: the identifier of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    identifier = property(fget=get_identifier)


##
# The following methods are from osid.type.TypeForm

    def get_display_name_metadata(self):
        """Gets the metadata for the display name.

        :return: metadata for the display name
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    display_name_metadata = property(fget=get_display_name_metadata)

    def set_display_name(self, display_name):
        """Sets a display name.

        :param display_name: the new display name
        :type display_name: ``string``
        :raise: ``InvalidArgument`` -- ``display_name`` is invalid
        :raise: ``NoAccess`` -- ``display_name`` cannot be modified
        :raise: ``NullArgument`` -- ``display_name`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_display_name(self):
        """Clears the display name.

        :raise: ``NoAccess`` -- ``display_name`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    display_name = property(fset=set_display_name, fdel=clear_display_name)

    def get_display_label_metadata(self):
        """Gets the metadata for the display label.

        :return: metadata for the display label
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    display_label_metadata = property(fget=get_display_label_metadata)

    def set_display_label(self, display_label):
        """Seta a display label.

        :param display_label: the new display label
        :type display_label: ``string``
        :raise: ``InvalidArgument`` -- ``display_label`` is invalid
        :raise: ``NoAccess`` -- ``display_label`` cannot be modified
        :raise: ``NullArgument`` -- ``display_label`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_display_label(self):
        """Clears the display label.

        :raise: ``NoAccess`` -- ``display_label`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    display_label = property(fset=set_display_label, fdel=clear_display_label)

    def get_description_metadata(self):
        """Gets the metadata for the description.

        :return: metadata for the description
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    description_metadata = property(fget=get_description_metadata)

    def set_description(self, description):
        """Sets a description.

        :param description: the new description
        :type description: ``string``
        :raise: ``InvalidArgument`` -- ``description`` is invalid
        :raise: ``NoAccess`` -- ``description`` cannot be modified
        :raise: ``NullArgument`` -- ``description`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_description(self):
        """Clears the description.

        :raise: ``NoAccess`` -- ``description`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    description = property(fset=set_description, fdel=clear_description)

    def get_domain_metadata(self):
        """Gets the metadata for the domain.

        :return: metadata for the domain
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    domain_metadata = property(fget=get_domain_metadata)

    def set_domain(self, domain):
        """Sets a domain.

        :param domain: the new domain
        :type domain: ``string``
        :raise: ``InvalidArgument`` -- ``domain`` is invalid
        :raise: ``NoAccess`` -- ``domain`` cannot be modified
        :raise: ``NullArgument`` -- ``domain`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_domain(self):
        """Clears the domain.

        :raise: ``NoAccess`` -- ``domain`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    domain = property(fset=set_domain, fdel=clear_domain)


##
# The following methods are from osid.type.TypeList

    def get_next_type(self):
        """Gets the next ``Type`` in this list.

        :return: the next ``Type`` in this list. The ``has_next()`` method should be used to test that a next ``Type`` is available before calling this method.
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    next_type = property(fget=get_next_type)

    def get_next_types(self, n):
        """Gets the next set of ``Types`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Type`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Type`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type




