.. currentmodule:: dlkit.abstract_osid.osid.markers
.. automodule:: dlkit.abstract_osid.osid.markers

Markers
=======


Osid Primitive
--------------

.. autoclass:: OsidPrimitive
   :show-inheritance:





Identifiable
------------

.. autoclass:: Identifiable
   :show-inheritance:

.. autoattribute:: Identifiable.ident

.. automethod:: Identifiable.is_current



Extensible
----------

.. autoclass:: Extensible
   :show-inheritance:

.. autoattribute:: Extensible.record_types

.. automethod:: Extensible.has_record_type



Browsable
---------

.. autoclass:: Browsable
   :show-inheritance:

.. autoattribute:: Browsable.properties

.. automethod:: Browsable.get_properties_by_record_type



Suppliable
----------

.. autoclass:: Suppliable
   :show-inheritance:





Temporal
--------

.. autoclass:: Temporal
   :show-inheritance:

.. automethod:: Temporal.is_effective

.. autoattribute:: Temporal.start_date

.. autoattribute:: Temporal.end_date



Subjugateable
-------------

.. autoclass:: Subjugateable
   :show-inheritance:





Aggregateable
-------------

.. autoclass:: Aggregateable
   :show-inheritance:





Containable
-----------

.. autoclass:: Containable
   :show-inheritance:

.. automethod:: Containable.is_sequestered



Sourceable
----------

.. autoclass:: Sourceable
   :show-inheritance:

.. autoattribute:: Sourceable.provider_id

.. autoattribute:: Sourceable.provider

.. autoattribute:: Sourceable.branding

.. autoattribute:: Sourceable.license



Federateable
------------

.. autoclass:: Federateable
   :show-inheritance:





Operable
--------

.. autoclass:: Operable
   :show-inheritance:

.. automethod:: Operable.is_active

.. automethod:: Operable.is_enabled

.. automethod:: Operable.is_disabled

.. automethod:: Operable.is_operational



