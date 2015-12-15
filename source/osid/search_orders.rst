

Search Orders
=============


Osid Search Order
-----------------

.. py:class:: OsidSearchOrder(abc_osid_search_orders.OsidSearchOrder, osid_markers.Suppliable)
    ``OsidSearchOrder`` specifies preferred ordering of search results.


    An ``OsidSearchOrder`` is available from an search session and
    supplied to an ``OsidSearch`` interface. OsidSearch os =
    session.getObjectSearch(); os.limitResultSet(1, 25); OsidSearchOrder
    order = session.getObjectSearchOrder(); order.orderByDisplayName();
    os.orderResults(order); OsidQuery queru; query =
    session.getObjectQuery(); query.addDescriptionMatch("*food*",
    wildcardStringMatchType, true); ObjectSearchResults results =
    session.getObjectsBySearch(query, os); ObjectList list =
    results.getObjectList();







Osid Identifiable Search Order
------------------------------

.. py:class:: OsidIdentifiableSearchOrder(abc_osid_search_orders.OsidIdentifiableSearchOrder, OsidSearchOrder)
    ``OsidIdentifiableSearchOrder`` specifies preferred ordering of search results.


    An ``OsidSearchOrder`` is available from an search session and
    supplied to an ``OsidSearch``.





    .. py:method:: order_by_id(style):
        :noindex:


Osid Extensible Search Order
----------------------------

.. py:class:: OsidExtensibleSearchOrder(abc_osid_search_orders.OsidExtensibleSearchOrder, OsidSearchOrder, osid_markers.Extensible)
    ``OsidExtensibleSearchOrder`` specifies preferred ordering of search results.


    An ``OsidSearchOrder`` is available from an search session and
    supplied to an ``OsidSearch``.







Osid Browsable Search Order
---------------------------

.. py:class:: OsidBrowsableSearchOrder(abc_osid_search_orders.OsidBrowsableSearchOrder, OsidSearchOrder)
    ``OsidBrowsableSearchOrder`` specifies preferred ordering of search results.


    An ``OsidSearchOrder`` is available from an search session and
    supplied to an ``OsidSearch``.







Osid Temporal Search Order
--------------------------

.. py:class:: OsidTemporalSearchOrder(abc_osid_search_orders.OsidTemporalSearchOrder, OsidSearchOrder)
    An interface for specifying the ordering of search results.

    .. py:method:: order_by_effective(style):
        :noindex:


    .. py:method:: order_by_start_date(style):
        :noindex:


    .. py:method:: order_by_end_date(style):
        :noindex:


Osid Subjugateable Search Order
-------------------------------

.. py:class:: OsidSubjugateableSearchOrder(abc_osid_search_orders.OsidSubjugateableSearchOrder, OsidSearchOrder)
    An interface for specifying the ordering of dependent object search results.



Osid Aggregateable Search Order
-------------------------------

.. py:class:: OsidAggregateableSearchOrder(abc_osid_search_orders.OsidAggregateableSearchOrder, OsidSearchOrder)
    An interface for specifying the ordering of assemblage search results.



Osid Containable Search Order
-----------------------------

.. py:class:: OsidContainableSearchOrder(abc_osid_search_orders.OsidContainableSearchOrder, OsidSearchOrder)
    An interface for specifying the ordering of search results.

    .. py:method:: order_by_sequestered(style):
        :noindex:


Osid Sourceable Search Order
----------------------------

.. py:class:: OsidSourceableSearchOrder(abc_osid_search_orders.OsidSourceableSearchOrder, OsidSearchOrder)
    An interface for specifying the ordering of search results.

    .. py:method:: order_by_provider(style):
        :noindex:


    .. py:method:: supports_provider_search_order():
        :noindex:


    .. py:method:: get_provider_search_order():
        :noindex:


    .. py:attribute:: provider_search_order
        :noindex:


Osid Federateable Search Order
------------------------------

.. py:class:: OsidFederateableSearchOrder(abc_osid_search_orders.OsidFederateableSearchOrder, OsidSearchOrder)
    An interface for specifying the ordering of search results.



Osid Operable Search Order
--------------------------

.. py:class:: OsidOperableSearchOrder(abc_osid_search_orders.OsidOperableSearchOrder, OsidSearchOrder)
    An interface for specifying the ordering of search results.

    .. py:method:: order_by_active(style):
        :noindex:


    .. py:method:: order_by_enabled(style):
        :noindex:


    .. py:method:: order_by_disabled(style):
        :noindex:


    .. py:method:: order_by_operational(style):
        :noindex:


Osid Object Search Order
------------------------

.. py:class:: OsidObjectSearchOrder(abc_osid_search_orders.OsidObjectSearchOrder, OsidIdentifiableSearchOrder, OsidExtensibleSearchOrder, OsidBrowsableSearchOrder)
    ``OsidObjectSearchOrder`` specifies preferred ordering of search results.


    An ``OsidSearchOrder`` is available from an search session and
    supplied to an ``OsidSearch``. OsidObjectSearch os =
    session.getObjectSearch(); os.limitResultSet(1, 25);
    OsidObjectSearchOrder order = session.getObjectSearchOrder();
    order.orderByDisplayName(); os.orderResults(order); OsidObjectQuery
    query; query = session.getObjectQuery();
    query.addDescriptionMatch("*food*", wildcardStringMatchType, true);
    ObjectSearchResults results = session.getObjectsBySearch(query, os);
    ObjectList list = results.getObjectList();





    .. py:method:: order_by_display_name(style):
        :noindex:


    .. py:method:: order_by_description(style):
        :noindex:


    .. py:method:: order_by_genus_type(style):
        :noindex:


    .. py:method:: order_by_state(process_id, style):
        :noindex:


    .. py:method:: order_by_cumulative_rating(book_id, style):
        :noindex:


    .. py:method:: order_by_statistic(meter_id, style):
        :noindex:


    .. py:method:: order_by_create_time(style):
        :noindex:


    .. py:method:: order_by_last_modified_time(style):
        :noindex:


Osid Relationship Search Order
------------------------------

.. py:class:: OsidRelationshipSearchOrder(abc_osid_search_orders.OsidRelationshipSearchOrder, OsidObjectSearchOrder, OsidTemporalSearchOrder)
    An interface for specifying the ordering of search results.

    .. py:method:: order_by_end_reason(style):
        :noindex:


    .. py:method:: supports_end_reason_search_order():
        :noindex:


    .. py:method:: get_end_reason_search_order():
        :noindex:


    .. py:attribute:: end_reason_search_order
        :noindex:


Osid Catalog Search Order
-------------------------

.. py:class:: OsidCatalogSearchOrder(abc_osid_search_orders.OsidCatalogSearchOrder, OsidObjectSearchOrder, OsidSourceableSearchOrder, OsidFederateableSearchOrder)
    An interface for specifying the ordering of catalog search results.



Osid Rule Search Order
----------------------

.. py:class:: OsidRuleSearchOrder(abc_osid_search_orders.OsidRuleSearchOrder, OsidObjectSearchOrder, OsidOperableSearchOrder)
    An interface for specifying the ordering of search results.

    .. py:method:: order_by_rule(style):
        :noindex:


    .. py:method:: supports_rule_search_order():
        :noindex:


    .. py:method:: get_rule_search_order():
        :noindex:


    .. py:attribute:: rule_search_order
        :noindex:


Osid Enabler Search Order
-------------------------

.. py:class:: OsidEnablerSearchOrder(abc_osid_search_orders.OsidEnablerSearchOrder, OsidRuleSearchOrder, OsidTemporalSearchOrder)
    An interface for specifying the ordering of search results.

    .. py:method:: order_by_schedule(style):
        :noindex:


    .. py:method:: supports_schedule_search_order():
        :noindex:


    .. py:method:: get_schedule_search_order():
        :noindex:


    .. py:attribute:: schedule_search_order
        :noindex:


    .. py:method:: order_by_event(style):
        :noindex:


    .. py:method:: supports_event_search_order():
        :noindex:


    .. py:method:: get_event_search_order():
        :noindex:


    .. py:attribute:: event_search_order
        :noindex:


    .. py:method:: order_by_cyclic_event(style):
        :noindex:


    .. py:method:: supports_cyclic_event_search_order():
        :noindex:


    .. py:method:: get_cyclic_event_search_order():
        :noindex:


    .. py:attribute:: cyclic_event_search_order
        :noindex:


    .. py:method:: order_by_demographic(style):
        :noindex:


    .. py:method:: supports_demographic_search_order():
        :noindex:


    .. py:method:: get_demographic_search_order():
        :noindex:


    .. py:attribute:: demographic_search_order
        :noindex:


Osid Constrainer Search Order
-----------------------------

.. py:class:: OsidConstrainerSearchOrder(abc_osid_search_orders.OsidConstrainerSearchOrder, OsidRuleSearchOrder)
    An interface for specifying the ordering of search results.



Osid Processor Search Order
---------------------------

.. py:class:: OsidProcessorSearchOrder(abc_osid_search_orders.OsidProcessorSearchOrder, OsidRuleSearchOrder)
    An interface for specifying the ordering of search results.



Osid Governator Search Order
----------------------------

.. py:class:: OsidGovernatorSearchOrder(abc_osid_search_orders.OsidGovernatorSearchOrder, OsidObjectSearchOrder, OsidOperableSearchOrder, OsidSourceableSearchOrder)
    An interface for specifying the ordering of search results.



Osid Compendium Search Order
----------------------------

.. py:class:: OsidCompendiumSearchOrder(abc_osid_search_orders.OsidCompendiumSearchOrder, OsidObjectSearchOrder, OsidSubjugateableSearchOrder)
    An interface for specifying the ordering of search results.

    .. py:method:: order_by_start_date(style):
        :noindex:


    .. py:method:: order_by_end_date(style):
        :noindex:


    .. py:method:: order_by_interpolated(style):
        :noindex:


    .. py:method:: order_by_extrapolated(style):
        :noindex:


Osid Capsule Search Order
-------------------------

.. py:class:: OsidCapsuleSearchOrder(abc_osid_search_orders.OsidCapsuleSearchOrder, OsidSearchOrder)
    An interface for specifying the ordering of search results.



