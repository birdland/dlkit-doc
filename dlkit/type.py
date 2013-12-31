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
from . import osid
from .osid_errors import Unimplemented, IllegalState, OperationFailed


class TypeProfile(osid.OsidProfile):

    def supports_type_lookup(self):
        """Tests if ``Type`` lookup is supported.

        :return: ``true`` if ``Type`` lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_type_admin(self):
        """Tests if a ``Type`` administrative service is supported.

        :return: ``true`` if ``Type`` administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()



class TypeManager(osid.OsidManager, osid.OsidSession, TypeProfile):

    def get_type_lookup_session(self):
        """Gets the ``OsidSession`` associated with the type lookup service.

        :return: a ``TypeLookupSession``
        :rtype: ``osid.type.TypeLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_type_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    type_lookup_session = property(fget=get_type_lookup_session)

    def get_type_admin_session(self):
        """Gets the ``OsidSession`` associated with the type admin service.

        :return: a ``TypeAdminSession``
        :rtype: ``osid.type.TypeAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_type_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    type_admin_session = property(fget=get_type_admin_session)


##
# The following methods are from osid.type.TypeProfile

    def supports_type_lookup(self):
        """Tests if ``Type`` lookup is supported.

        :return: ``true`` if ``Type`` lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_type_admin(self):
        """Tests if a ``Type`` administrative service is supported.

        :return: ``true`` if ``Type`` administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.type.TypeManager

    def get_type_lookup_session(self):
        """Gets the ``OsidSession`` associated with the type lookup service.

        :return: a ``TypeLookupSession``
        :rtype: ``osid.type.TypeLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_type_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    type_lookup_session = property(fget=get_type_lookup_session)

    def get_type_admin_session(self):
        """Gets the ``OsidSession`` associated with the type admin service.

        :return: a ``TypeAdminSession``
        :rtype: ``osid.type.TypeAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_type_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    type_admin_session = property(fget=get_type_admin_session)


##
# The following methods are from osid.type.TypeProxyManager




##
# The following methods are from osid.type.TypeLookupSession

    def can_lookup_types(self):
        """Tests if this user can perform ``Type`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_type(self, namespace, identifier, authority):
        """Gets a ``Type`` by its string representation which is a combination of the authority and identifier.
        This method only returns the ``Type`` if it is known by the
        given identification components.

        :param namespace: the identifier namespace
        :type namespace: ``string``
        :param identifier: the identifier
        :type identifier: ``string``
        :param authority: the authority
        :type authority: ``string``
        :return: the ``Type``
        :rtype: ``osid.type.Type``
        :raise: ``NotFound`` -- the type is not found
        :raise: ``NullArgument`` -- ``null`` argument provided
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_type(self, type_):
        """Tests if the given ``Type`` is known.

        :param type: the ``Type`` to look for
        :type type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is known, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_types_by_domain(self, domain):
        """Gets all the known Types by domain.

        :param domain: the domain
        :type domain: ``string``
        :return: the list of ``Types`` with the given domain
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``domain`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_types_by_authority(self, authority):
        """Gets all the known Types by authority.

        :param authority: the authority
        :type authority: ``string``
        :return: the list of ``Types`` with the given authority
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``authority`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- respect my authoritay

        """
        raise UNIMPLEMENTED()

    def get_types_by_domain_and_authority(self, domain, authority):
        """Gets all the known Types by domain and authority.

        :param domain: the domain
        :type domain: ``string``
        :param authority: the authority
        :type authority: ``string``
        :return: the list of ``Types`` with the given domain and authority
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``domain`` or ``authority`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_types(self):
        """Gets all the known Types.

        :return: the list of all known ``Types``
        :rtype: ``osid.type.TypeList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    types = property(fget=get_types)

    def is_equivalent(self, type_, equivalent_type):
        """Tests if the given types are equivalent.

        :param type: a type
        :type type: ``osid.type.Type``
        :param equivalent_type: another type
        :type equivalent_type: ``osid.type.Type``
        :return: ``true`` if both types are equivalent, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def implies_support(self, type_, base_type):
        """Tests if the given type is implies support of a base type.

        :param type: a type
        :type type: ``osid.type.Type``
        :param base_type: another type
        :type base_type: ``osid.type.Type``
        :return: ``true`` if ``base_type`` if supported by ``type,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``type`` or ``base_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_base_type(self, type_):
        """Tests if the given type is derived from a base type.

        :param type: a type
        :type type: ``osid.type.Type``
        :return: ``true`` is the given type is derived from a base type, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_base_types(self, type_):
        """Gets the immediate base types of this type.

        :param type: a type
        :type type: ``osid.type.Type``
        :return: the base types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.type.TypeAdminSession

    def can_create_types(self):
        """Tests if this user can create ``Types``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Type``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Type`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_type_form_for_create(self):
        """Gets the type form for creating new types.
        A new form should be requested for each create transaction.

        :return: the type form
        :rtype: ``osid.type.TypeForm``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    type_form_for_create = property(fget=get_type_form_for_create)

    def create_type(self, authority, identifier_ns, identifier, type_form):
        """Creates a new ``Type``.

        :param authority: the authority
        :type authority: ``string``
        :param identifier_ns: the namespace of the identifier
        :type identifier_ns: ``string``
        :param identifier: the identifier
        :type identifier: ``string``
        :param type_form: the type form
        :type type_form: ``osid.type.TypeForm``
        :return: the created ``Type``
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- ``log_entry_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the arguments is invalid
        :raise: ``NullArgument`` -- one or more of the arguments is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``type_form`` did not originate from ``get_type_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_types(self):
        """Tests if this user can update types.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Type``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if type modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_update_type(self, type_):
        """Tests if this user can update the specified type.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating the ``Type``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :param type: the ``Type`` to be updated
        :type type: ``osid.type.Type``
        :return: ``false`` if type modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_type_form_for_update(self, type_):
        """Gets the type form for creating new types.
        A new form should be requested for each create transaction.

        :param type: the ``Type`` to be updated
        :type type: ``osid.type.Type``
        :return: the type form
        :rtype: ``osid.type.TypeForm``
        :raise: ``IllegalState`` -- ``type_form`` already used in an update transaction
        :raise: ``NotFound`` -- ``type`` not found
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_type(self, type_, type_form):
        """Updates a type.

        :param type: the ``Type`` to be updated
        :type type: ``osid.type.Type``
        :param type_form: the type form
        :type type_form: ``osid.type.TypeForm``
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NotFound`` -- ``type`` is not found
        :raise: ``NullArgument`` -- ``type`` or ``type_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``type_form`` did not originate from ``get_type_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_types(self):
        """Tests if this user can delete ``Types`` from this ``ItemBank``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Type``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Item`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_delete_type(self, type_):
        """Tests if this user can delete the specified type.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleteing the
        ``Type`` will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :param type: the ``Type`` to be deleted
        :type type: ``osid.type.Type``
        :return: ``false`` if type deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def delete_type(self, type_):
        """Removes a ``Type``.

        :param type: the ``Type`` to remove
        :type type: ``osid.type.Type``
        :raise: ``NotFound`` -- ``type`` is not found
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def make_equivalent(self, primary_type, equivalent_type):
        """Makes two ``Types`` equivalent.
        Calls to ``TypeLookupSession.getType(equivalentType)`` return
        the ``primaryType``.

        :param primary_type: the primary ``Type``
        :type primary_type: ``osid.type.Type``
        :param equivalent_type: a ``Type`` to be made equivalent
        :type equivalent_type: ``osid.type.Type``
        :raise: ``NotFound`` -- ``primary_type`` or ``equivalent_type`` is not found
        :raise: ``NullArgument`` -- ``primary_type`` or ``equivalent_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_base_type(self, type_, base_type):
        """Adds a base type to a type.
        A base type is a parent of the type where the type implies
        support of the base type.

        :param type: a ``Type``
        :type type: ``osid.type.Type``
        :param base_type: a base type
        :type base_type: ``osid.type.Type``
        :raise: ``NotFound`` -- ``type`` or ``base_type`` is not found
        :raise: ``NullArgument`` -- ``type`` or ``base_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_base_type(self, type_, base_type):
        """Removes a base type from a type.

        :param type: a ``Type``
        :type type: ``osid.type.Type``
        :param base_type: a base type
        :type base_type: ``osid.type.Type``
        :raise: ``NotFound`` -- ``type`` or ``base_type`` is not found
        :raise: ``NullArgument`` -- ``type`` or ``base_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.type.Type

    def get_display_name(self):
        """Gets the full display name of this ``Type``.

        :return: the display name of this ``Type``
        :rtype: ``osid.locale.DisplayText``

        """
        raise UNIMPLEMENTED()

    display_name = property(fget=get_display_name)

    def get_display_label(self):
        """Gets the shorter display label for this ``Type``.
        Where a display name of a ``Type`` might be ``"`` Critical
        Logging Priority Type", the display label could be "critical".

        :return: the display label for this ``Type``. The display name is returned when there is no metadata availavle for this ``Type``.
        :rtype: ``osid.locale.DisplayText``

        """
        raise UNIMPLEMENTED()

    display_label = property(fget=get_display_label)

    def get_description(self):
        """Gets a description of this ``Type``.

        :return: the description of this ``Type``. An empty string is returned when no description is available for this ``Type``.
        :rtype: ``osid.locale.DisplayText``

        """
        raise UNIMPLEMENTED()

    description = property(fget=get_description)

    def get_domain(self):
        """Gets the domain.
        The domain can provide an information label about ths
        application space of this Type.

        :return: the domain of this ``Type``
        :rtype: ``osid.locale.DisplayText``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    authority = property(fget=get_authority)

    def get_identifier_namespace(self):
        """Gets the namespace of the identifier.
        This method is used to compare one ``Type`` to another.

        :return: the authority of this ``Type``
        :rtype: ``string``

        """
        raise UNIMPLEMENTED()

    identifier_namespace = property(fget=get_identifier_namespace)

    namespace = property(fget=get_identifier_namespace)

    def get_identifier(self):
        """Gets the identifier of this ``Type``.
        This method is used to compare one ``Type`` to another.

        :return: the identifier of this ``Type``
        :rtype: ``string``

        """
        raise UNIMPLEMENTED()

    identifier = property(fget=get_identifier)


##
# The following methods are from osid.type.TypeForm

    def get_display_name_metadata(self):
        """Gets the metadata for the display name.

        :return: metadata for the display name
        :rtype: ``osid.Metadata``

        """
        raise UNIMPLEMENTED()

    display_name_metadata = property(fget=get_display_name_metadata)

    def set_display_name(self, display_name):
        """Sets a display name.
        A display name is required and if not set will be set by the
        provider.

        :param display_name: the new display name
        :type display_name: ``string``
        :raise: ``InvalidArgument`` -- ``display_name`` is invalid
        :raise: ``NoAccess`` -- ``display_name`` cannot be modified
        :raise: ``NullArgument`` -- ``display_name`` is ``null``

        """
        raise UNIMPLEMENTED()

    display_name = property(fset=set_display_name)

    def get_display_label_metadata(self):
        """Gets the metadata for the display label.

        :return: metadata for the display label
        :rtype: ``osid.Metadata``

        """
        raise UNIMPLEMENTED()

    display_label_metadata = property(fget=get_display_label_metadata)

    def set_display_label(self, display_label):
        """Seta a display label.

        :param display_label: the new display label
        :type display_label: ``string``
        :raise: ``InvalidArgument`` -- ``display_label`` is invalid
        :raise: ``NoAccess`` -- ``display_label`` cannot be modified
        :raise: ``NullArgument`` -- ``display_label`` is ``null``

        """
        raise UNIMPLEMENTED()

    display_label = property(fset=set_display_label)

    def get_description_metadata(self):
        """Gets the metadata for the description.

        :return: metadata for the description
        :rtype: ``osid.Metadata``

        """
        raise UNIMPLEMENTED()

    description_metadata = property(fget=get_description_metadata)

    def set_description(self, description):
        """Sets a description.

        :param description: the new description
        :type description: ``string``
        :raise: ``InvalidArgument`` -- ``description`` is invalid
        :raise: ``NoAccess`` -- ``description`` cannot be modified
        :raise: ``NullArgument`` -- ``description`` is ``null``

        """
        raise UNIMPLEMENTED()

    def clear_description(self):
        """Clears the description.

        :raise: ``NoAccess`` -- ``description`` cannot be modified

        """
        raise UNIMPLEMENTED()

    description = property(fget=set_description, fdel=clear_description)

    def get_domain_metadata(self):
        """Gets the metadata for the domain.

        :return: metadata for the domain
        :rtype: ``osid.Metadata``

        """
        raise UNIMPLEMENTED()

    domain_metadata = property(fget=get_domain_metadata)

    def set_domain(self, domain):
        """Sets a domain.

        :param domain: the new domain
        :type domain: ``string``
        :raise: ``InvalidArgument`` -- ``domain`` is invalid
        :raise: ``NoAccess`` -- ``domain`` cannot be modified
        :raise: ``NullArgument`` -- ``domain`` is ``null``

        """
        raise UNIMPLEMENTED()

    def clear_domain(self):
        """Clears the domain.

        :raise: ``NoAccess`` -- ``domain`` cannot be modified

        """
        raise UNIMPLEMENTED()

    domain = property(fget=set_domain, fdel=clear_domain)


##
# The following methods are from osid.type.TypeList

    def get_next_type(self):
        """Gets the next ``Type`` in this list.

        :return: the next ``Type`` in this list. The ``has_next()`` method should be used to test that a next ``Type`` is available before calling this method.
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()



class TypeProxyManager(osid.OsidProxyManager, TypeProfile):
    pass




