

Markers
=======


Osid Primitive
--------------

.. py:class:: OsidPrimitive(abc_osid_markers.OsidPrimitive)
    A marker interface for an interface that behaves like a language primitive.


    Primitive types, such as numbers and strings, do not encapsulate
    behaviors supplied by an OSID Provider. More complex primitives are
    expressed through interface definitions but are treated in a similar
    fashion as a language primitive. OSID Primitives supplied by an OSID
    Consumer must be consumable by any OSID Provider.







Identifiable
------------

.. py:class:: Identifiable(abc_osid_markers.Identifiable)
    A marker interface for objects uniquely identified with an OSID ``Id``.

    .. py:method:: get_id():
        :noindex:


    .. py:attribute:: id_
        :noindex:


    .. py:attribute:: ident
        :noindex:


    .. py:method:: is_current():
        :noindex:


Extensible
----------

.. py:class:: Extensible(abc_osid_markers.Extensible)
    A marker interface for objects that contain ``OsidRecords``.

    .. py:method:: get_record_types():
        :noindex:


    .. py:attribute:: record_types
        :noindex:


    .. py:method:: has_record_type(record_type):
        :noindex:


Browsable
---------

.. py:class:: Browsable(abc_osid_markers.Browsable)
    A marker interface for objects that offer property inspection.

    .. py:method:: get_properties():
        :noindex:


    .. py:attribute:: properties
        :noindex:


    .. py:method:: get_properties_by_record_type(record_type):
        :noindex:


Suppliable
----------

.. py:class:: Suppliable(abc_osid_markers.Suppliable)
    A marker interface for OSID Provider-owned objects used to supply input from an OSID Consumer.



Temporal
--------

.. py:class:: Temporal(abc_osid_markers.Temporal)
    ``Temporal`` is used to indicate the object endures for a period of time.

    .. py:method:: is_effective():
        :noindex:


    .. py:method:: get_start_date():
        :noindex:


    .. py:attribute:: start_date
        :noindex:


    .. py:method:: get_end_date():
        :noindex:


    .. py:attribute:: end_date
        :noindex:


Subjugateable
-------------

.. py:class:: Subjugateable(abc_osid_markers.Subjugateable)
    A ``Subjugateable`` is an ``OsidObject`` dependent upon another ``OsidObject``.


    A ``Subjugateable`` is created in the context of the administering
    ``OsidObject`` that may not be reassigned.




    A ``Subjugateable`` always has a fixed Id of it administering
    ``OsidObject``.







Aggregateable
-------------

.. py:class:: Aggregateable(abc_osid_markers.Aggregateable)
    ``Aggregateable`` is used for an ``OsidObject`` to indicate that some or all of the definition
        is
    based on an included set of other ``OsidObjects`` which are directly accessible and do not exist
    outside the context of the parent object.


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







Containable
-----------

.. py:class:: Containable(abc_osid_markers.Containable)
    A ``Containable`` is a kind of aggregate where an ``OsidObject`` is defined as a recursive
    composition of itself directly accessible without knowledge of the originating service.

    .. py:method:: is_sequestered():
        :noindex:


Sourceable
----------

.. py:class:: Sourceable(abc_osid_markers.Sourceable)
    ``Sourceble`` is used for ``OsidObjects`` where information about a provider is appropriate.


    Examples of ``Sourceables`` are catalogs, compositions, and
    services.





    .. py:method:: get_provider_id():
        :noindex:


    .. py:attribute:: provider_id
        :noindex:


    .. py:method:: get_provider():
        :noindex:


    .. py:attribute:: provider
        :noindex:


    .. py:method:: get_branding_ids():
        :noindex:


    .. py:attribute:: branding_ids
        :noindex:


    .. py:method:: get_branding():
        :noindex:


    .. py:attribute:: branding
        :noindex:


    .. py:method:: get_license():
        :noindex:


    .. py:attribute:: license_
        :noindex:


Federateable
------------

.. py:class:: Federateable(abc_osid_markers.Federateable)
    ``Federateable`` is used to indicate an ``OsidObject`` can be federated using the OSID Hierarchy
    pattern.


    An OSID federation of ``OsidObjects`` is where it is inferred from
    the hiererarchy that any ``OsidObject`` "includes" its children.







Operable
--------

.. py:class:: Operable(abc_osid_markers.Operable)
    ``Operable`` is used to indicate an ``OsidObject`` performs operations.


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





    .. py:method:: is_active():
        :noindex:


    .. py:method:: is_enabled():
        :noindex:


    .. py:method:: is_disabled():
        :noindex:


    .. py:method:: is_operational():
        :noindex:


