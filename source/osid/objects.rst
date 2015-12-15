

Objects
=======


Osid Object
-----------

.. py:class:: OsidObject(abc_osid_objects.OsidObject, osid_markers.Identifiable, osid_markers.Extensible, osid_markers.Browsable)
    ``OsidObject`` is the top level interface for all OSID Objects.


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





    .. py:method:: get_display_name():
        :noindex:


    .. py:attribute:: display_name
        :noindex:


    .. py:method:: get_description():
        :noindex:


    .. py:attribute:: description
        :noindex:


    .. py:method:: get_genus_type():
        :noindex:


    .. py:attribute:: genus_type
        :noindex:


    .. py:method:: is_of_genus_type(genus_type):
        :noindex:


Osid Relationship
-----------------

.. py:class:: OsidRelationship(abc_osid_objects.OsidRelationship, OsidObject, osid_markers.Temporal)
    A ``Relationship`` associates two OSID objects.


    Relationships are transient. They define a date range for which they
    are in effect.




    Unlike other ``OsidObjects`` that rely on the auxiliary Journaling
    OSID to track variance over time, ``OsidRelationships`` introduce a
    different concept of time independent from journaling. For example,
    in the present, a student was registered in a course and dropped it.
    The relationship between the student and the course remains
    pertinent, independent of any journaled changes that may have
    occurred to either the student or the course.




    Once the student has dropped the course, the relationship has
    expired such that ``is_effective()`` becomes false. It can be
    inferred that during the period of the effective dates, the student
    was actively registered in the course. Here is an example:




      * T1. September 1: Student registers for course for grades
      * T2. September 10: Student drops course
      * T3. September 15: Student re-registers for course pass/fail








    The relationships are:
      T1. R1 {effective,   September 1  -> end of term,  data=grades}
      T2. R1 {ineffective, September 1  -> September 10, data=grades}
      T3. R1 {ineffective, September 1  -> September 10, data=grades}
          R2 {effective,   September 10 -> end of term,  data=p/f}












    An OSID Provider may also permit dates to be set in the future in
    which case the relationship can become automatically become
    effective at a future time and later expire. More complex
    effectiveness management can be done through other rule-based
    services.




    OSID Consumer lookups and queries of relationships need to consider
    that it may be only effective relationshps are of interest.





    .. py:method:: has_end_reason():
        :noindex:


    .. py:method:: get_end_reason_id():
        :noindex:


    .. py:attribute:: end_reason_id
        :noindex:


    .. py:method:: get_end_reason():
        :noindex:


    .. py:attribute:: end_reason
        :noindex:


Osid Catalog
------------

.. py:class:: OsidCatalog(abc_osid_objects.OsidCatalog, OsidObject, osid_markers.Sourceable, osid_markers.Federateable)
    ``OsidCatalog`` is the top level interface for all OSID catalog-like objects.


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







Osid Rule
---------

.. py:class:: OsidRule(abc_osid_objects.OsidRule, OsidObject, osid_markers.Operable)
    An ``OsidRule`` identifies an explicit or implicit rule evaluation.


    An associated ``Rule`` may be available in cases where the behavior
    of the object can be explicitly modified using a defined rule. In
    many cases, an ``OsidObject`` may define specific methods to manage
    certain common behavioral aspects and delegate anything above and
    beyond what has been defined to a rule evaluation.




    Rules are defined to be operable. In the case of a statement
    evaluation, an enabled rule overrides any evaluation to return
    ``true`` and a disabled rule overrides any evaluation to return
    ``false``.




    ``Rules`` are never required to consume or implement. They serve as
    a mechanism to offer a level of management not attainable in the
    immediate service definition. Each Rule implies evaluating a set of
    facts known to the service to produce a resulting beavior. Rule
    evaluations may also accept input data or conditions, however,
    ``OsidRules`` as they appear in throughout the services may or may
    not provide a means of supplying ``OsidConditions`` directly. In the
    services where an explicit ``OsidCondition`` is absent they may be
    masquerading as another interface such as a ``Proxy`` or an
    ``OsidQuery`` .





    .. py:method:: has_rule():
        :noindex:


    .. py:method:: get_rule_id():
        :noindex:


    .. py:attribute:: rule_id
        :noindex:


    .. py:method:: get_rule():
        :noindex:


    .. py:attribute:: rule
        :noindex:


Osid Enabler
------------

.. py:class:: OsidEnabler(abc_osid_objects.OsidEnabler, OsidRule, osid_markers.Temporal)
    ``OsidEnabler`` is used to manage the effectiveness, enabledness, or operation of an
        ``OsidObejct``.


    The ``OsidEnabler`` itself is active or inactive When an
    ``OsidEnabler`` is active, any ``OsidObject`` mapped to it is "on."
    When all ``OsidEnablers`` mapped to an ``OsidObject`` are inactive,
    then the ``OsidObject`` is "off."




    The managed ``OsidObject`` may have varying semantics as to what its
    on/off status means and in particular, which methods are used to
    indicate the effect of an ``OsidEnabler``. Some axamples:




      * ``Operables:``  ``OsidEnablers`` effect the operational status.
      * ``Temporals:``  ``OsidEnablers`` may be used to extend or
        shorten the effectiveness of a ``Temporal`` such as an
        ``OsidRelationship.``








    In the case where an ``OsidEnabler`` may cause a discontinuity in a
    ``Temporal,`` the ``OsidEnabler`` may cause the creation of new
    ``Temporals`` to capture the gap in effectiveness.




    For example, An ``OsidRelationship`` that began in 2007 may be
    brought to an end in 2008 due to the absence of any active
    ``OsidEnablers``. When an effective ``OsidEnabler`` appears in 2009,
    a new ``OsidRelationship`` is created with a starting effective date
    of 2009 leaving the existing ``OsidRelationship`` with effective
    dates from 2007 to 2008.




    An ``OsidEnabler`` itself is both a ``Temporal`` and an ``OsidRule``
    whose activity status of the object may be controlled
    administratively, using a span of effective dates, through an
    external rule, or all three. The ``OsidEnabler`` defines a set of
    canned rules based on dates, events, and cyclic events.





    .. py:method:: is_effective_by_schedule():
        :noindex:


    .. py:method:: get_schedule_id():
        :noindex:


    .. py:attribute:: schedule_id
        :noindex:


    .. py:method:: get_schedule():
        :noindex:


    .. py:attribute:: schedule
        :noindex:


    .. py:method:: is_effective_by_event():
        :noindex:


    .. py:method:: get_event_id():
        :noindex:


    .. py:attribute:: event_id
        :noindex:


    .. py:method:: get_event():
        :noindex:


    .. py:attribute:: event
        :noindex:


    .. py:method:: is_effective_by_cyclic_event():
        :noindex:


    .. py:method:: get_cyclic_event_id():
        :noindex:


    .. py:attribute:: cyclic_event_id
        :noindex:


    .. py:method:: get_cyclic_event():
        :noindex:


    .. py:attribute:: cyclic_event
        :noindex:


    .. py:method:: is_effective_for_demographic():
        :noindex:


    .. py:method:: get_demographic_id():
        :noindex:


    .. py:attribute:: demographic_id
        :noindex:


    .. py:method:: get_demographic():
        :noindex:


    .. py:attribute:: demographic
        :noindex:


Osid Constrainer
----------------

.. py:class:: OsidConstrainer(abc_osid_objects.OsidConstrainer, OsidRule)
    An ``OsidConstrainer`` marks an interface as a control point to constrain another object.


    A constrainer may define specific methods to describe the
    constrainment or incorporate external logic using a rule.







Osid Processor
--------------

.. py:class:: OsidProcessor(abc_osid_objects.OsidProcessor, OsidRule)
    An ``OsidProcessor`` is an interface describing the operation of another object.


    A processor may define specific methods to manage processing, or
    incorporate external logic using a rule.







Osid Governator
---------------

.. py:class:: OsidGovernator(abc_osid_objects.OsidGovernator, OsidObject, osid_markers.Operable, osid_markers.Sourceable)
    An ``OsidGovernator`` is a control point to govern the behavior of a service.


    ``OsidGovernators`` generally indicate the presence of
    ``OsidEnablers`` and other rule governing interfaces to provide a
    means of managing service operations and constraints from a "behind
    the scenes" perspective. The ``OsidGovernator`` is a focal point for
    these various rules.




    ``OsidGovernators`` are ``Sourceable``. An ``OsidGovernator``
    implies a governance that often corresponds to a provider of a
    process as opposed to a catalog provider of ``OsidObjects``.




    ``OsidGovernators`` are ``Operable``. They indicate an active and
    operational status and related rules may be administratively
    overridden using this control point. Administratively setting the
    enabled or disabled flags in the operator overrides any enabling
    rule mapped to this ``OsidGovernator``.







Osid Compendium
---------------

.. py:class:: OsidCompendium(abc_osid_objects.OsidCompendium, OsidObject, osid_markers.Subjugateable)
    ``OsidCompendium`` is the top level interface for reports based on measurements, calculations,
    summaries, or views of transactional activity within periods of time.


    This time dimension of this report may align with managed time
    periods, specific dates, or both. Oh my.




    Reports are often derived dynamically based on an examination of
    data managed elsewhere in an OSID. Reports may also be directly
    managed outside where it is desirable to capture summaries without
    the detail of the implied evaluated data. The behavior of a direct
    create or update of a report is not specified but is not limited to
    an override or a cascading update of underlying data.




    The start and end date represents the date range used in the
    evaluation of the transactional data on which this report is based.
    The start and end date may be the same indicating that the
    evaluation occurred at a point in time rather than across a date
    range. The start and end date requested may differ from the start
    and end date indicated in this report because of the inability to
    interpolate or extrapolate the date. These dates should be examined
    to understand what actually occurred and to what dates the
    information in this report pertains.




    These dates differ from the dates the report itself was requested,
    created, or modified. The dates refer to the context of the
    evaluation. In a managed report, the dates are simply the dates to
    which the report information pertains. The history of a single
    report may be examined in the Journaling OSID.




    For example, the Location of a Resource at 12:11pm is reported to be
    in Longwood and at 12:23pm is reported to be at Chestnut Hill. A
    request of a ``ResourceLocation``. A data correction may update the
    Longwood time to be 12:09pm. The update of the ``ResourceLocation``
    from 12:11pm to 12:09pm may be examined in the Journaling OSID while
    the 12:11pm time would not longer be visible in current versions of
    this report.




    Reports may be indexed by a managed time period such as a ``Term``
    or ``FiscalPeriod``. The evaluation dates may map to the opening and
    closing dates of the time period. Evaluation dates that differ from
    the time period may indicate that the transactional data is
    incomplete for that time period or that the report was calculated
    using a requested date range.




    ``OsidCompendiums`` are subjugates to other ``OsidObjects`` in that
    what is reported is tied to an instance of a dimension such as a
    person, account, or an ``OsidCatalog`` .





    .. py:method:: get_start_date():
        :noindex:


    .. py:attribute:: start_date
        :noindex:


    .. py:method:: get_end_date():
        :noindex:


    .. py:attribute:: end_date
        :noindex:


    .. py:method:: is_interpolated():
        :noindex:


    .. py:method:: is_extrapolated():
        :noindex:


Osid Capsule
------------

.. py:class:: OsidCapsule(abc_osid_objects.OsidCapsule)
    ``OsidCapsule`` wraps other objects.


    The interface has no meaning other than to return a set of
    semantically unrelated objects from a method.







Osid Form
---------

.. py:class:: OsidForm(abc_osid_objects.OsidForm, osid_markers.Identifiable, osid_markers.Suppliable)
    The ``OsidForm`` is the vehicle used to create and update objects.


    The form is a container for data to be sent to an update or create
    method of a session. Applications should persist their own data
    until a form is successfully submitted in an update or create
    transaction.




    The form may provide some feedback as to the validity of certain
    data updates before the update transaction is issued to the
    correspodning session but a successful modification of the form is
    not a guarantee of success for the update transaction. A consumer
    may elect to perform all updates within a single update transaction
    or break up a large update intio smaller units. The tradeoff is the
    granularity of error feedback vs. the performance gain of a single
    transaction.




    ``OsidForms`` are ``Identifiable``. The ``Id`` of the ``OsidForm``
    is used to uniquely identify the update or create transaction and
    not that of the object being updated. Currently, it is not necessary
    to have these ``Ids`` persisted.




    As with all aspects of the OSIDs, nulls cannot be used. Methods to
    clear values are also defined in the form.




    A new ``OsidForm`` should be acquired for each transaction upon an
    ``OsidObject``. Forms should not be reused from one object to
    another even if the supplied data is the same as the forms may
    encapsulate data specific to the object requested. Example of
    changing a display name and a color defined in a color interface
    extension:
      ObjectForm form = session.getObjectFormForUpdate(objectId);
      form.setDisplayName("new name");
      ColorForm recordForm = form.getFormRecord(colorRecordType);
      recordForm.setColor("green");
      session.updateObject(objectId, form);









    .. py:method:: is_for_update():
        :noindex:


    .. py:method:: get_default_locale():
        :noindex:


    .. py:attribute:: default_locale
        :noindex:


    .. py:method:: get_locales():
        :noindex:


    .. py:attribute:: locales
        :noindex:


    .. py:method:: set_locale(language_type, script_type):
        :noindex:


    .. py:method:: get_journal_comment_metadata():
        :noindex:


    .. py:attribute:: journal_comment_metadata
        :noindex:


    .. py:method:: set_journal_comment(comment):
        :noindex:


    .. py:attribute:: journal_comment
        :noindex:


    .. py:method:: is_valid():
        :noindex:


    .. py:method:: get_validation_messages():
        :noindex:


    .. py:attribute:: validation_messages
        :noindex:


    .. py:method:: get_invalid_metadata():
        :noindex:


    .. py:attribute:: invalid_metadata
        :noindex:


Osid Identifiable Form
----------------------

.. py:class:: OsidIdentifiableForm(abc_osid_objects.OsidIdentifiableForm, OsidForm)
    The ``OsidIdentifiableForm`` is used to create and update identifiable objects.


    The form is a container for data to be sent to an update or create
    method of a session.







Osid Extensible Form
--------------------

.. py:class:: OsidExtensibleForm(abc_osid_objects.OsidExtensibleForm, OsidForm, osid_markers.Extensible)
    The ``OsidExtensibleForm`` is used to create and update extensible objects.


    The form is a container for data to be sent to an update or create
    method of a session.





    .. py:method:: get_required_record_types():
        :noindex:


    .. py:attribute:: required_record_types
        :noindex:


Osid Browsable Form
-------------------

.. py:class:: OsidBrowsableForm(abc_osid_objects.OsidBrowsableForm, OsidForm)
    The ``OsidBrowsableForm`` is used to create and update browsable objects.


    The form is a container for data to be sent to an update or create
    method of a session.







Osid Temporal Form
------------------

.. py:class:: OsidTemporalForm(abc_osid_objects.OsidTemporalForm, OsidForm)
    This form is used to create and update temporals.

    .. py:method:: get_start_date_metadata():
        :noindex:


    .. py:attribute:: start_date_metadata
        :noindex:


    .. py:method:: set_start_date(date):
        :noindex:


    .. py:method:: clear_start_date():
        :noindex:


    .. py:attribute:: start_date
        :noindex:


    .. py:method:: get_end_date_metadata():
        :noindex:


    .. py:attribute:: end_date_metadata
        :noindex:


    .. py:method:: set_end_date(date):
        :noindex:


    .. py:method:: clear_end_date():
        :noindex:


    .. py:attribute:: end_date
        :noindex:


Osid Subjugateable Form
-----------------------

.. py:class:: OsidSubjugateableForm(abc_osid_objects.OsidSubjugateableForm, OsidForm)
    This form is used to create and update dependent objects.



Osid Aggregateable Form
-----------------------

.. py:class:: OsidAggregateableForm(abc_osid_objects.OsidAggregateableForm, OsidForm)
    This form is used to create and update assemblages.



Osid Containable Form
---------------------

.. py:class:: OsidContainableForm(abc_osid_objects.OsidContainableForm, OsidForm)
    This form is used to create and update containers.

    .. py:method:: get_sequestered_metadata():
        :noindex:


    .. py:attribute:: sequestered_metadata
        :noindex:


    .. py:method:: set_sequestered(sequestered):
        :noindex:


    .. py:method:: clear_sequestered():
        :noindex:


    .. py:attribute:: sequestered
        :noindex:


Osid Sourceable Form
--------------------

.. py:class:: OsidSourceableForm(abc_osid_objects.OsidSourceableForm, OsidForm)
    This form is used to create and update sourceables.

    .. py:method:: get_provider_metadata():
        :noindex:


    .. py:attribute:: provider_metadata
        :noindex:


    .. py:method:: set_provider(provider_id):
        :noindex:


    .. py:method:: clear_provider():
        :noindex:


    .. py:attribute:: provider
        :noindex:


    .. py:method:: get_branding_metadata():
        :noindex:


    .. py:attribute:: branding_metadata
        :noindex:


    .. py:method:: set_branding(asset_ids):
        :noindex:


    .. py:method:: clear_branding():
        :noindex:


    .. py:attribute:: branding
        :noindex:


    .. py:method:: get_license_metadata():
        :noindex:


    .. py:attribute:: license_metadata
        :noindex:


    .. py:method:: set_license(license_):
        :noindex:


    .. py:method:: clear_license():
        :noindex:


    .. py:attribute:: license_
        :noindex:


Osid Federateable Form
----------------------

.. py:class:: OsidFederateableForm(abc_osid_objects.OsidFederateableForm, OsidForm)
    This form is used to create and update federateables.



Osid Operable Form
------------------

.. py:class:: OsidOperableForm(abc_osid_objects.OsidOperableForm, OsidForm)
    This form is used to create and update operables.

    .. py:method:: get_enabled_metadata():
        :noindex:


    .. py:attribute:: enabled_metadata
        :noindex:


    .. py:method:: set_enabled(enabled):
        :noindex:


    .. py:method:: clear_enabled():
        :noindex:


    .. py:attribute:: enabled
        :noindex:


    .. py:method:: get_disabled_metadata():
        :noindex:


    .. py:attribute:: disabled_metadata
        :noindex:


    .. py:method:: set_disabled(disabled):
        :noindex:


    .. py:method:: clear_disabled():
        :noindex:


    .. py:attribute:: disabled
        :noindex:


Osid Object Form
----------------

.. py:class:: OsidObjectForm(abc_osid_objects.OsidObjectForm, OsidIdentifiableForm, OsidExtensibleForm, OsidBrowsableForm)
    The ``OsidObjectForm`` is used to create and update ``OsidObjects``.


    The form is not an ``OsidObject`` but merely a container for data to
    be sent to an update or create method of a session. A provider may
    or may not combine the ``OsidObject`` and ``OsidObjectForm``
    interfaces into a single object.




    Generally, a set method parallels each get method of an
    ``OsidObject``. Additionally, ``Metadata`` may be examined for each
    data element to assist in understanding particular rules concerning
    acceptable data.




    The form may provide some feedback as to the validity of certain
    data updates before the update transaction is issued to the
    correspodning session but a successful modification of the form is
    not a guarantee of success for the update transaction. A consumer
    may elect to perform all updates within a single update transaction
    or break up a large update intio smaller units. The tradeoff is the
    granularity of error feedback vs. the performance gain of a single
    transaction.




    As with all aspects of the OSIDs, nulls cannot be used. Methods to
    clear values are also defined in the form.




    A new ``OsidForm`` should be acquired for each transaction upon an
    ``OsidObject``. Forms should not be reused from one object to
    another even if the supplied data is the same as the forms may
    encapsulate data specific to the object requested. Example of
    changing a display name and a color defined in a color interface
    extension:
      ObjectForm form = session.getObjectFormForUpdate(objectId);
      form.setDisplayName("new name");
      ColorForm recordForm = form.getFormRecord(colorRecordType);
      recordForm.setColor("green");
      session.updateObject(objectId, form);









    .. py:method:: get_display_name_metadata():
        :noindex:


    .. py:attribute:: display_name_metadata
        :noindex:


    .. py:method:: set_display_name(display_name):
        :noindex:


    .. py:method:: clear_display_name():
        :noindex:


    .. py:attribute:: display_name
        :noindex:


    .. py:method:: get_description_metadata():
        :noindex:


    .. py:attribute:: description_metadata
        :noindex:


    .. py:method:: set_description(description):
        :noindex:


    .. py:method:: clear_description():
        :noindex:


    .. py:attribute:: description
        :noindex:


    .. py:method:: get_genus_type_metadata():
        :noindex:


    .. py:attribute:: genus_type_metadata
        :noindex:


    .. py:method:: set_genus_type(genus_type):
        :noindex:


    .. py:method:: clear_genus_type():
        :noindex:


    .. py:attribute:: genus_type
        :noindex:


Osid Relationship Form
----------------------

.. py:class:: OsidRelationshipForm(abc_osid_objects.OsidRelationshipForm, OsidObjectForm, OsidTemporalForm)
    This form is used to create and update relationshps.



Osid Catalog Form
-----------------

.. py:class:: OsidCatalogForm(abc_osid_objects.OsidCatalogForm, OsidObjectForm, OsidSourceableForm, OsidFederateableForm)
    This form is used to create and update catalogs.



Osid Rule Form
--------------

.. py:class:: OsidRuleForm(abc_osid_objects.OsidRuleForm, OsidObjectForm, OsidOperableForm)
    This form is used to create and update rules.

    .. py:method:: get_rule_metadata():
        :noindex:


    .. py:attribute:: rule_metadata
        :noindex:


    .. py:method:: set_rule(rule_id):
        :noindex:


    .. py:method:: clear_rule():
        :noindex:


    .. py:attribute:: rule
        :noindex:


Osid Enabler Form
-----------------

.. py:class:: OsidEnablerForm(abc_osid_objects.OsidEnablerForm, OsidRuleForm, OsidTemporalForm)
    This form is used to create and update enablers.

    .. py:method:: get_schedule_metadata():
        :noindex:


    .. py:attribute:: schedule_metadata
        :noindex:


    .. py:method:: set_schedule(schedule_id):
        :noindex:


    .. py:method:: clear_schedule():
        :noindex:


    .. py:attribute:: schedule
        :noindex:


    .. py:method:: get_event_metadata():
        :noindex:


    .. py:attribute:: event_metadata
        :noindex:


    .. py:method:: set_event(event_id):
        :noindex:


    .. py:method:: clear_event():
        :noindex:


    .. py:attribute:: event
        :noindex:


    .. py:method:: get_cyclic_event_metadata():
        :noindex:


    .. py:attribute:: cyclic_event_metadata
        :noindex:


    .. py:method:: set_cyclic_event(cyclic_event_id):
        :noindex:


    .. py:method:: clear_cyclic_event():
        :noindex:


    .. py:attribute:: cyclic_event
        :noindex:


    .. py:method:: get_demographic_metadata():
        :noindex:


    .. py:attribute:: demographic_metadata
        :noindex:


    .. py:method:: set_demographic(resource_id):
        :noindex:


    .. py:method:: clear_demographic():
        :noindex:


    .. py:attribute:: demographic
        :noindex:


Osid Constrainer Form
---------------------

.. py:class:: OsidConstrainerForm(abc_osid_objects.OsidConstrainerForm, OsidRuleForm)
    This form is used to create and update constrainers.



Osid Processor Form
-------------------

.. py:class:: OsidProcessorForm(abc_osid_objects.OsidProcessorForm, OsidRuleForm)
    This form is used to create and update processors.



Osid Governator Form
--------------------

.. py:class:: OsidGovernatorForm(abc_osid_objects.OsidGovernatorForm, OsidObjectForm, OsidOperableForm, OsidSourceableForm)
    This form is used to create and update governators.



Osid Compendium Form
--------------------

.. py:class:: OsidCompendiumForm(abc_osid_objects.OsidCompendiumForm, OsidObjectForm, OsidSubjugateableForm)
    This form is used to create and update governators.

    .. py:method:: get_start_date_metadata():
        :noindex:


    .. py:attribute:: start_date_metadata
        :noindex:


    .. py:method:: set_start_date(date):
        :noindex:


    .. py:method:: clear_start_date():
        :noindex:


    .. py:attribute:: start_date
        :noindex:


    .. py:method:: get_end_date_metadata():
        :noindex:


    .. py:attribute:: end_date_metadata
        :noindex:


    .. py:method:: set_end_date(date):
        :noindex:


    .. py:method:: clear_end_date():
        :noindex:


    .. py:attribute:: end_date
        :noindex:


    .. py:method:: get_interpolated_metadata():
        :noindex:


    .. py:attribute:: interpolated_metadata
        :noindex:


    .. py:method:: set_interpolated(interpolated):
        :noindex:


    .. py:method:: clear_interpolated():
        :noindex:


    .. py:attribute:: interpolated
        :noindex:


    .. py:method:: get_extrapolated_metadata():
        :noindex:


    .. py:attribute:: extrapolated_metadata
        :noindex:


    .. py:method:: set_extrapolated(extrapolated):
        :noindex:


    .. py:method:: clear_extrapolated():
        :noindex:


    .. py:attribute:: extrapolated
        :noindex:


Osid Capsule Form
-----------------

.. py:class:: OsidCapsuleForm(abc_osid_objects.OsidCapsuleForm, OsidForm)
    This form is used to create and update capsules.



Osid List
---------

.. py:class:: OsidList(abc_osid_objects.OsidList)
    ``OsidList`` is the top-level interface for all OSID lists.


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





    .. py:method:: has_next():
        :noindex:


    .. py:method:: available():
        :noindex:


    .. py:method:: skip(n):
        :noindex:


Osid Node
---------

.. py:class:: OsidNode(abc_osid_objects.OsidNode, osid_markers.Identifiable, osid_markers.Containable)
    A node interface for hierarchical objects.


    The ``Id`` of the node is the ``Id`` of the object represented at
    this node.





    .. py:method:: is_root():
        :noindex:


    .. py:method:: has_parents():
        :noindex:


    .. py:method:: get_parent_ids():
        :noindex:


    .. py:attribute:: parent_ids
        :noindex:


    .. py:method:: is_leaf():
        :noindex:


    .. py:method:: has_children():
        :noindex:


    .. py:method:: get_child_ids():
        :noindex:


    .. py:attribute:: child_ids
        :noindex:


