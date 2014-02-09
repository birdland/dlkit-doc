


class OsidPrimitive:
    """A marker interface for an interface that behaves like a language primitive.

    Primitive types, such as numbers and strings, do not encapsulate
    behaviors supplied by an OSID Provider. More complex primitives are
    expressed through interface definitions but are treated in a similar
    fashion as a language primitive. OSID Primitives supplied by an OSID
    Consumer must be consumable by any OSID Provider.

    """



class Identifiable:
    """A marker interface for objects uniquely identified with an OSID ``Id``."""
    def get_id(self):
        """Gets the Id associated with this instance of this OSID object.

        Persisting any reference to this object is done by persisting
        the Id returned from this method. The Id returned may be
        different than the Id used to query this object. In this case,
        the new Id should be preferred over the old one for future
        queries.

        :return: the ``Id``
        :rtype: ``osid.id.Id``

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

        """
        return # boolean


class Extensible:
    """A marker interface for objects that contain ``OsidRecords``."""
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

        """
        return # boolean


class Browsable:
    """A marker interface for objects that offer property inspection."""
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

        """
        return # osid.PropertyList


class Suppliable:
    """A marker interface for OSID Provider-owned objects used to supply input from an OSID Consumer."""



class Temporal:
    """``Temporal`` is used to indicate the object endures for a period of time."""
    def is_effective(self):
        """Tests if the current date is within the start end end dates inclusive.

        :return: ``true`` if this is effective, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_start_date(self):
        """Gets the start date.

        :return: the start date
        :rtype: ``osid.calendaring.DateTime``

        """
        return # osid.calendaring.DateTime

    start_date = property(fget=get_start_date)

    def get_end_date(self):
        """Gets the end date.

        :return: the end date
        :rtype: ``osid.calendaring.DateTime``

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



class Aggregateable:
    """``Aggregateable`` is used for an ``OsidObject`` to indicate that some or all of the definition is based on an included set of other ``OsidObjects`` which are directly accessible and do not exist outside the context of the parent object.

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



class Containable(Aggregateable):
    """A ``Containable`` is a kind of aggregate where an ``OsidObject`` is defined as a recursive composition of itself directly accessible without knowledge of the originating service."""
    def is_sequestered(self):
        """Tests if this ``Containable`` is sequestered in that it should not appear outside of its aggregated composition.

        :return: ``true`` if this containable is sequestered, ``false`` if this containable may appear outside its aggregate
        :rtype: ``boolean``

        """
        return # boolean


class Sourceable:
    """``Sourceble`` is used for ``OsidObjects`` where information about a provider is appropriate.

    Examples of ``Sourceables`` are catalogs, compositions, and
    services.

    """
    def get_provider_id(self):
        """Gets the ``Id`` of the provider.

        :return: the provider ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    provider_id = property(fget=get_provider_id)

    def get_provider(self):
        """Gets the ``Resource`` representing the provider.

        :return: the provider
        :rtype: ``osid.resource.Resource``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.resource.Resource

    provider = property(fget=get_provider)

    def get_branding_ids(self):
        """Gets the branding asset ``Ids``.

        :return: a list of asset ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.IdList

    branding_ids = property(fget=get_branding_ids)

    def get_branding(self):
        """Gets a branding, such as an image or logo, expressed using the ``Asset`` interface.

        :return: a list of assets
        :rtype: ``osid.repository.AssetList``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.repository.AssetList

    branding = property(fget=get_branding)

    def get_license(self):
        """Gets the terms of usage.

        An empty license means the terms are unknown.

        :return: the license
        :rtype: ``osid.locale.DisplayText``

        """
        return # osid.locale.DisplayText

    license = property(fget=get_license)


class Federateable:
    """``Federateable`` is used to indicate an ``OsidObject`` can be federated using the OSID Hierarchy pattern.

    An OSID federation of ``OsidObjects`` is where it is inferred from
    the hiererarchy that any ``OsidObject`` "includes" its children.

    """



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

        """
        return # boolean

    def is_enabled(self):
        """Tests if this operable is administravely enabled.

        Administratively enabling overrides any applied ``OsidEnabler``.
        If this method returns ``true`` then ``is_disabled()`` must
        return ``false``.

        :return: ``true`` if this operable is enabled, ``false`` if the active status is determined by other rules
        :rtype: ``boolean``

        """
        return # boolean

    def is_disabled(self):
        """Tests if this operable is administravely disabled.

        Administratively disabling overrides any applied
        ``OsidEnabler``. If this method returns ``true`` then
        ``is_enabled()`` must return ``false``.

        :return: ``true`` if this operable is disabled, ``false`` if the active status is determined by other rules
        :rtype: ``boolean``

        """
        return # boolean

    def is_operational(self):
        """Tests if this ``Operable`` is operational.

        This Operable is operational if any of the applied
        ``OsidEnablers`` are ``true``.

        :return: ``true`` if this operable is operational, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean


