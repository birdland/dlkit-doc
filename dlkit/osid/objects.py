
from ..osid import markers as osid_markers


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
    



    def get_display_name(self):
        """Gets the preferred display name associated with this instance of this OSID object appropriate for display to
        the user.

        return: (osid.locale.DisplayText) - the display name
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

        return: (osid.locale.DisplayText) - the description
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

        return: (osid.type.Type) - the genus type of this object
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    genus_type = property(fget=get_genus_type)


    def is_of_genus_type(self, genus_type):
        """Tests if this object is of the given genus ``Type``.

        The given genus type may be supported by the object through the
        type hierarchy.

        arg:    genus_type (osid.type.Type): a genus type
        return: (boolean) - ``true`` if this object is of the given
                genus ``Type,``  ``false`` otherwise
        raise:  NullArgument - ``genus_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


class OsidRelationship(OsidObject, osid_markers.Temporal):
    """A ``Relationship`` associates two OSID objects.

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

    """
    



    def has_end_reason(self):
        """Tests if a reason this relationship came to an end is known.

        return: (boolean) - ``true`` if an end reason is available,
                ``false`` otherwise
        raise:  IllegalState - ``is_effective()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_end_reason_id(self):
        """Gets a state ``Id`` indicating why this relationship has ended.

        return: (osid.id.Id) - a state ``Id``
        raise:  IllegalState - ``has_end_reason()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    end_reason_id = property(fget=get_end_reason_id)


    def get_end_reason(self):
        """Gets a state indicating why this relationship has ended.

        return: (osid.process.State) - a state
        raise:  IllegalState - ``has_end_reason()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.process.State

    end_reason = property(fget=get_end_reason)


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
    





class OsidRule(OsidObject, osid_markers.Operable):
    """An ``OsidRule`` identifies an explicit or implicit rule evaluation.

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

    """
    



    def has_rule(self):
        """Tests if an explicit rule is available.

        return: (boolean) - ``true`` if an explicit rule is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_rule_id(self):
        """Gets the explicit rule ``Id``.

        return: (osid.id.Id) - the rule ``Id``
        raise:  IllegalState - ``has_rule()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    rule_id = property(fget=get_rule_id)


    def get_rule(self):
        """Gets the explicit rule.

        return: (osid.rules.Rule) - the rule
        raise:  IllegalState - ``has_rule()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.rules.Rule

    rule = property(fget=get_rule)


class OsidEnabler(OsidRule, osid_markers.Temporal):
    """``OsidEnabler`` is used to manage the effectiveness, enabledness, or operation of an ``OsidObejct``.

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

    """
    



    def is_effective_by_schedule(self):
        """Tests if the effectiveness of the enabler is governed by a ``Schedule``.

        If a schedule exists, it is bounded by the effective dates of
        this enabler. If ``is_effective_by_schedule()`` is ``true,``
        ``is_effective_by_event()`` and
        ``is_effective_by_cyclic_event()`` must be ``false``.

        return: (boolean) - ``true`` if the enabler is governed by
                schedule, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_schedule_id(self):
        """Gets the schedule ``Id``.

        return: (osid.id.Id) - the schedule ``Id``
        raise:  IllegalState - ``is_effective_by_schedule()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    schedule_id = property(fget=get_schedule_id)


    def get_schedule(self):
        """Gets the schedule.

        return: (osid.calendaring.Schedule) - the schedule
        raise:  IllegalState - ``is_effective_by_schedule()`` is
                ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.Schedule

    schedule = property(fget=get_schedule)


    def is_effective_by_event(self):
        """Tests if the effectiveness of the enabler is governed by an ``Event`` such that the start and end dates of
        the event govern the effectiveness.

        The event may also be a ``RecurringEvent`` in which case the
        enabler is effective for start and end dates of each event in
        the series If an event exists, it is bounded by the effective
        dates of this enabler. If ``is_effective_by_event()`` is
        ``true,`` ``is_effective_by_schedule()`` and
        ``is_effective_by_cyclic_event()`` must be ``false``.

        return: (boolean) - ``true`` if the enabler is governed by an
                event, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_event_id(self):
        """Gets the event ``Id``.

        return: (osid.id.Id) - the event ``Id``
        raise:  IllegalState - ``is_effective_by_event()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    event_id = property(fget=get_event_id)


    def get_event(self):
        """Gets the event.

        return: (osid.calendaring.Event) - the event
        raise:  IllegalState - ``is_effective_by_event()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.Event

    event = property(fget=get_event)


    def is_effective_by_cyclic_event(self):
        """Tests if the effectiveness of the enabler is governed by a ``CyclicEvent``.

        If a cyclic event exists, it is evaluated by the accompanying
        cyclic time period. If ``is_effective_by_cyclic_event()`` is
        ``true,`` ``is_effective_by_schedule()`` and
        ``is_effective_by_event()`` must be ``false``.

        return: (boolean) - ``true`` if the enabler is governed by a
                cyclic event, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_cyclic_event_id(self):
        """Gets the cyclic event ``Id``.

        return: (osid.id.Id) - the cyclic event ``Id``
        raise:  IllegalState - ``is_effective_by_cyclic_event()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    cyclic_event_id = property(fget=get_cyclic_event_id)


    def get_cyclic_event(self):
        """Gets the cyclic event.

        return: (osid.calendaring.cycle.CyclicEvent) - the cyclic event
        raise:  IllegalState - ``is_effective_by_cyclic_event()`` is
                ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.cycle.CyclicEvent

    cyclic_event = property(fget=get_cyclic_event)


    def is_effective_for_demographic(self):
        """Tests if the effectiveness of the enabler applies to a demographic resource.

        return: (boolean) - ``true`` if the rule apples to a
                demographic. ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_demographic_id(self):
        """Gets the demographic resource ``Id``.

        return: (osid.id.Id) - the resource ``Id``
        raise:  IllegalState - ``is_effective_for_demographic()`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    demographic_id = property(fget=get_demographic_id)


    def get_demographic(self):
        """Gets the demographic resource.

        return: (osid.resource.Resource) - the resource representing the
                demographic
        raise:  IllegalState - ``is_effective_for_demographic()`` is
                ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Resource

    demographic = property(fget=get_demographic)


class OsidConstrainer(OsidRule):
    """An ``OsidConstrainer`` marks an interface as a control point to constrain another object.

    A constrainer may define specific methods to describe the
    constrainment or incorporate external logic using a rule.

    """
    





class OsidProcessor(OsidRule):
    """An ``OsidProcessor`` is an interface describing the operation of another object.

    A processor may define specific methods to manage processing, or
    incorporate external logic using a rule.

    """
    





class OsidGovernator(OsidObject, osid_markers.Operable, osid_markers.Sourceable):
    """An ``OsidGovernator`` is a control point to govern the behavior of a service.

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

    """
    





class OsidCompendium(OsidObject, osid_markers.Subjugateable):
    """``OsidCompendium`` is the top level interface for reports based on measurements, calculations, summaries, or views of
        transactional activity within periods of time.

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

    """
    



    def get_start_date(self):
        """Gets the start date used in the evaluation of the transactional data on which this report is based.

        return: (osid.calendaring.DateTime) - the date
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.DateTime

    start_date = property(fget=get_start_date)


    def get_end_date(self):
        """Gets the end date used in the evaluation of the transactional data on which this report is based.

        return: (osid.calendaring.DateTime) - the date
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.DateTime

    end_date = property(fget=get_end_date)


    def is_interpolated(self):
        """Tests if this report is interpolated within measured data or known transactions.

        Interpolation may occur if the start or end date fall between
        two known facts or managed time period.

        return: (boolean) - ``true`` if this report is interpolated,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def is_extrapolated(self):
        """Tests if this report is extrapolated outside measured data or known transactions.

        Extrapolation may occur if the start or end date fall outside
        two known facts or managed time period. Extrapolation may occur
        within a managed time period in progress where the results of
        the entire time period are projected.

        return: (boolean) - ``true`` if this report is extrapolated,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


class OsidCapsule:
    """``OsidCapsule`` wraps other objects.

    The interface has no meaning other than to return a set of
    semantically unrelated objects from a method.

    """
    





class OsidForm(osid_markers.Identifiable, osid_markers.Suppliable):
    """The ``OsidForm`` is the vehicle used to create and update objects.

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


    """
    



    def is_for_update(self):
        """Tests if this form is for an update operation.

        return: (boolean) - ``true`` if this form is for an update
                operation, ``false`` if for a create operation
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_default_locale(self):
        """Gets a default locale for ``DisplayTexts`` when a locale is not specified.

        return: (osid.locale.Locale) - the default locale
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.Locale

    default_locale = property(fget=get_default_locale)


    def get_locales(self):
        """Gets a list of locales for available ``DisplayText`` translations that can be performed using this form.

        return: (osid.locale.LocaleList) - a list of available locales
                or an empty list if no translation operations are
                available
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.LocaleList

    locales = property(fget=get_locales)


    def set_locale(self, language_type, script_type):
        """Specifies a language and script type for ``DisplayText`` fields in this form.

        Setting a locale to something other than the default locale may
        affect the ``Metadata`` in this form.

        If multiple locales are available for managing translations, the
        ``Metadata`` indicates the fields are unset as they may be
        returning a defeult value based on the default locale.

        arg:    language_type (osid.type.Type): the language type
        arg:    script_type (osid.type.Type): the script type
        raise:  NullArgument - ``language_type`` or ``script_type`` is
                null
        raise:  Unsupported - ``language_type`` and ``script_type`` not
                available from ``get_locales()``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def get_journal_comment_metadata(self):
        """Gets the metadata for the comment corresponding to this form submission.

        The comment is used for describing the nature of the change to
        the corresponding object for the purposes of logging and
        auditing.

        return: (osid.Metadata) - metadata for the comment
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    journal_comment_metadata = property(fget=get_journal_comment_metadata)


    def set_journal_comment(self, comment):
        """Sets a comment.

        arg:    comment (string): the new comment
        raise:  InvalidArgument - ``comment`` is invalid
        raise:  NoAccess - ``Metadata.isReadonly()`` is ``true``
        raise:  NullArgument - ``comment`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    journal_comment = property(fset=set_journal_comment)


    def is_valid(self):
        """Tests if ths form is in a valid state for submission.

        A form is valid if all required data has been supplied compliant
        with any constraints.

        return: (boolean) - ``false`` if there is a known error in this
                form, ``true`` otherwise
        raise:  OperationFailed - attempt to perform validation failed
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_validation_messages(self):
        """Gets text messages corresponding to additional instructions to pass form validation.

        return: (osid.locale.DisplayText) - a list of messages
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    validation_messages = property(fget=get_validation_messages)


    def get_invalid_metadata(self):
        """Gets a list of metadata for the elements in this form which are not valid.

        return: (osid.Metadata) - invalid metadata
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    invalid_metadata = property(fget=get_invalid_metadata)


class OsidIdentifiableForm(OsidForm):
    """The ``OsidIdentifiableForm`` is used to create and update identifiable objects.

    The form is a container for data to be sent to an update or create
    method of a session.

    """
    





class OsidExtensibleForm(OsidForm, osid_markers.Extensible):
    """The ``OsidExtensibleForm`` is used to create and update extensible objects.

    The form is a container for data to be sent to an update or create
    method of a session.

    """
    



    def get_required_record_types(self):
        """Gets the required record types for this form.

        The required records may change as a result of other data in
        this form and should be checked before submission.

        return: (osid.type.TypeList) - a list of required record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    required_record_types = property(fget=get_required_record_types)


class OsidBrowsableForm(OsidForm):
    """The ``OsidBrowsableForm`` is used to create and update browsable objects.

    The form is a container for data to be sent to an update or create
    method of a session.

    """
    





class OsidTemporalForm(OsidForm):
    """This form is used to create and update temporals."""
    



    def get_start_date_metadata(self):
        """Gets the metadata for a start date.

        return: (osid.Metadata) - metadata for the date
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    start_date_metadata = property(fget=get_start_date_metadata)


    def set_start_date(self, date):
        """Sets the start date.

        arg:    date (osid.calendaring.DateTime): the new date
        raise:  InvalidArgument - ``date`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``date`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_start_date(self):
        """Clears the start date.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    start_date = property(fset=set_start_date, fdel=clear_start_date)


    def get_end_date_metadata(self):
        """Gets the metadata for an end date.

        return: (osid.Metadata) - metadata for the date
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    end_date_metadata = property(fget=get_end_date_metadata)


    def set_end_date(self, date):
        """Sets the end date.

        arg:    date (osid.calendaring.DateTime): the new date
        raise:  InvalidArgument - ``date`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``date`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_end_date(self):
        """Clears the end date.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    end_date = property(fset=set_end_date, fdel=clear_end_date)


class OsidSubjugateableForm(OsidForm):
    """This form is used to create and update dependent objects."""
    





class OsidAggregateableForm(OsidForm):
    """This form is used to create and update assemblages."""
    





class OsidContainableForm(OsidForm):
    """This form is used to create and update containers."""
    



    def get_sequestered_metadata(self):
        """Gets the metadata for the sequestered flag.

        return: (osid.Metadata) - metadata for the sequestered flag
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    sequestered_metadata = property(fget=get_sequestered_metadata)


    def set_sequestered(self, sequestered):
        """Sets the sequestered flag.

        arg:    sequestered (boolean): the new sequestered flag
        raise:  InvalidArgument - ``sequestered`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_sequestered(self):
        """Clears the sequestered flag.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    sequestered = property(fset=set_sequestered, fdel=clear_sequestered)


class OsidSourceableForm(OsidForm):
    """This form is used to create and update sourceables."""
    



    def get_provider_metadata(self):
        """Gets the metadata for a provider.

        return: (osid.Metadata) - metadata for the provider
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    provider_metadata = property(fget=get_provider_metadata)


    def set_provider(self, provider_id):
        """Sets a provider.

        arg:    provider_id (osid.id.Id): the new provider
        raise:  InvalidArgument - ``provider_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``provider_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_provider(self):
        """Removes the provider.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    provider = property(fset=set_provider, fdel=clear_provider)


    def get_branding_metadata(self):
        """Gets the metadata for the asset branding.

        return: (osid.Metadata) - metadata for the asset branding.
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    branding_metadata = property(fget=get_branding_metadata)


    def set_branding(self, asset_ids):
        """Sets the branding.

        arg:    asset_ids (osid.id.Id[]): the new assets
        raise:  InvalidArgument - ``asset_ids`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``asset_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_branding(self):
        """Removes the branding.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    branding = property(fset=set_branding, fdel=clear_branding)


    def get_license_metadata(self):
        """Gets the metadata for the license.

        return: (osid.Metadata) - metadata for the license
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    license_metadata = property(fget=get_license_metadata)


    def set_license(self, license_):
        """Sets the license.

        arg:    license (string): the new license
        raise:  InvalidArgument - ``license`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``license`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_license(self):
        """Removes the license.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    license_ = property(fset=set_license, fdel=clear_license)


class OsidFederateableForm(OsidForm):
    """This form is used to create and update federateables."""
    





class OsidOperableForm(OsidForm):
    """This form is used to create and update operables."""
    



    def get_enabled_metadata(self):
        """Gets the metadata for the enabled flag.

        return: (osid.Metadata) - metadata for the enabled flag
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    enabled_metadata = property(fget=get_enabled_metadata)


    def set_enabled(self, enabled):
        """Sets the administratively enabled flag.

        arg:    enabled (boolean): the new enabled flag
        raise:  InvalidArgument - ``enabled`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_enabled(self):
        """Removes the administratively enabled flag.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    enabled = property(fset=set_enabled, fdel=clear_enabled)


    def get_disabled_metadata(self):
        """Gets the metadata for the disabled flag.

        return: (osid.Metadata) - metadata for the disabled flag
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    disabled_metadata = property(fget=get_disabled_metadata)


    def set_disabled(self, disabled):
        """Sets the administratively disabled flag.

        arg:    disabled (boolean): the new disabled flag
        raise:  InvalidArgument - ``disabled`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_disabled(self):
        """Removes the administratively disabled flag.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    disabled = property(fset=set_disabled, fdel=clear_disabled)


class OsidObjectForm(OsidIdentifiableForm, OsidExtensibleForm, OsidBrowsableForm):
    """The ``OsidObjectForm`` is used to create and update ``OsidObjects``.

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


    """
    



    def get_display_name_metadata(self):
        """Gets the metadata for a display name.

        return: (osid.Metadata) - metadata for the display name
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    display_name_metadata = property(fget=get_display_name_metadata)


    def set_display_name(self, display_name):
        """Sets a display name.

        A display name is required and if not set, will be set by the
        provider.

        arg:    display_name (string): the new display name
        raise:  InvalidArgument - ``display_name`` is invalid
        raise:  NoAccess - ``Metadata.isReadonly()`` is ``true``
        raise:  NullArgument - ``display_name`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_display_name(self):
        """Clears the display name.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    display_name = property(fset=set_display_name, fdel=clear_display_name)


    def get_description_metadata(self):
        """Gets the metadata for a description.

        return: (osid.Metadata) - metadata for the description
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    description_metadata = property(fget=get_description_metadata)


    def set_description(self, description):
        """Sets a description.

        arg:    description (string): the new description
        raise:  InvalidArgument - ``description`` is invalid
        raise:  NoAccess - ``Metadata.isReadonly()`` is ``true``
        raise:  NullArgument - ``description`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_description(self):
        """Clears the description.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    description = property(fset=set_description, fdel=clear_description)


    def get_genus_type_metadata(self):
        """Gets the metadata for a genus type.

        return: (osid.Metadata) - metadata for the genus
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    genus_type_metadata = property(fget=get_genus_type_metadata)


    def set_genus_type(self, genus_type):
        """Sets a genus.

        A genus cannot be cleared because all objects have at minimum a
        root genus.

        arg:    genus_type (osid.type.Type): the new genus
        raise:  InvalidArgument - ``genus_type`` is invalid
        raise:  NoAccess - ``Metadata.isReadonly()`` is ``true``
        raise:  NullArgument - ``genus_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_genus_type(self):
        """Clears the genus type.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    genus_type = property(fset=set_genus_type, fdel=clear_genus_type)


class OsidRelationshipForm(OsidObjectForm, OsidTemporalForm):
    """This form is used to create and update relationshps."""
    





class OsidCatalogForm(OsidObjectForm, OsidSourceableForm, OsidFederateableForm):
    """This form is used to create and update catalogs."""
    





class OsidRuleForm(OsidObjectForm, OsidOperableForm):
    """This form is used to create and update rules."""
    



    def get_rule_metadata(self):
        """Gets the metadata for an associated rule.

        return: (osid.Metadata) - metadata for the rule
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    rule_metadata = property(fget=get_rule_metadata)


    def set_rule(self, rule_id):
        """Sets a rule.

        arg:    rule_id (osid.id.Id): the new rule
        raise:  InvalidArgument - ``rule_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``rule_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_rule(self):
        """Removes the rule.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rule = property(fset=set_rule, fdel=clear_rule)


class OsidEnablerForm(OsidRuleForm, OsidTemporalForm):
    """This form is used to create and update enablers."""
    



    def get_schedule_metadata(self):
        """Gets the metadata for an associated schedule.

        return: (osid.Metadata) - metadata for the schedule
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    schedule_metadata = property(fget=get_schedule_metadata)


    def set_schedule(self, schedule_id):
        """Sets a schedule.

        arg:    schedule_id (osid.id.Id): the new schedule
        raise:  InvalidArgument - ``schedule_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``schedule_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_schedule(self):
        """Removes the schedule.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    schedule = property(fset=set_schedule, fdel=clear_schedule)


    def get_event_metadata(self):
        """Gets the metadata for an associated event.

        return: (osid.Metadata) - metadata for the event
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    event_metadata = property(fget=get_event_metadata)


    def set_event(self, event_id):
        """Sets an event.

        arg:    event_id (osid.id.Id): the new event
        raise:  InvalidArgument - ``event_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``event_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_event(self):
        """Removes the event.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    event = property(fset=set_event, fdel=clear_event)


    def get_cyclic_event_metadata(self):
        """Gets the metadata for the cyclic event.

        return: (osid.Metadata) - metadata for the cyclic event
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    cyclic_event_metadata = property(fget=get_cyclic_event_metadata)


    def set_cyclic_event(self, cyclic_event_id):
        """Sets the cyclic event.

        arg:    cyclic_event_id (osid.id.Id): the new cyclic event
        raise:  InvalidArgument - ``cyclic_event_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``cyclic_event_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_cyclic_event(self):
        """Removes the cyclic event.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    cyclic_event = property(fset=set_cyclic_event, fdel=clear_cyclic_event)


    def get_demographic_metadata(self):
        """Gets the metadata for an associated demographic.

        return: (osid.Metadata) - metadata for the resource.
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    demographic_metadata = property(fget=get_demographic_metadata)


    def set_demographic(self, resource_id):
        """Sets a resource demographic.

        arg:    resource_id (osid.id.Id): the new resource
        raise:  InvalidArgument - ``resource_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``resource_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_demographic(self):
        """Removes the resource demographic.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    demographic = property(fset=set_demographic, fdel=clear_demographic)


class OsidConstrainerForm(OsidRuleForm):
    """This form is used to create and update constrainers."""
    





class OsidProcessorForm(OsidRuleForm):
    """This form is used to create and update processors."""
    





class OsidGovernatorForm(OsidObjectForm, OsidOperableForm, OsidSourceableForm):
    """This form is used to create and update governators."""
    





class OsidCompendiumForm(OsidObjectForm, OsidSubjugateableForm):
    """This form is used to create and update governators."""
    



    def get_start_date_metadata(self):
        """Gets the metadata for a start date.

        return: (osid.Metadata) - metadata for the date
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    start_date_metadata = property(fget=get_start_date_metadata)


    def set_start_date(self, date):
        """Sets the start date.

        arg:    date (osid.calendaring.DateTime): the new date
        raise:  InvalidArgument - ``date`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``date`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_start_date(self):
        """Clears the start date.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    start_date = property(fset=set_start_date, fdel=clear_start_date)


    def get_end_date_metadata(self):
        """Gets the metadata for an end date.

        return: (osid.Metadata) - metadata for the date
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    end_date_metadata = property(fget=get_end_date_metadata)


    def set_end_date(self, date):
        """Sets the end date.

        arg:    date (osid.calendaring.DateTime): the new date
        raise:  InvalidArgument - ``date`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``date`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_end_date(self):
        """Clears the end date.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    end_date = property(fset=set_end_date, fdel=clear_end_date)


    def get_interpolated_metadata(self):
        """Gets the metadata for the interpolated flag.

        return: (osid.Metadata) - metadata for the interpolated flag
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    interpolated_metadata = property(fget=get_interpolated_metadata)


    def set_interpolated(self, interpolated):
        """Sets the interpolated flag.

        arg:    interpolated (boolean): the new interpolated flag
        raise:  InvalidArgument - ``interpolated`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_interpolated(self):
        """Clears the interpolated flag.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    interpolated = property(fset=set_interpolated, fdel=clear_interpolated)


    def get_extrapolated_metadata(self):
        """Gets the metadata for the extrapolated flag.

        return: (osid.Metadata) - metadata for the extrapolated flag
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    extrapolated_metadata = property(fget=get_extrapolated_metadata)


    def set_extrapolated(self, extrapolated):
        """Sets the extrapolated flag.

        arg:    extrapolated (boolean): the new extrapolated flag
        raise:  InvalidArgument - ``extrapolated`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_extrapolated(self):
        """Clears the extrapolated flag.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    extrapolated = property(fset=set_extrapolated, fdel=clear_extrapolated)


class OsidCapsuleForm(OsidForm):
    """This form is used to create and update capsules."""
    





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
    



    def has_next(self):
        """Tests if there are more elements in this list.

        return: (boolean) - ``true`` if more elements are available in
                this list, ``false`` if the end of the list has been
                reached
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

        return: (cardinal) - the number of elements available for
                retrieval
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

        arg:    n (cardinal): the number of elements to skip
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class OsidNode(osid_markers.Identifiable, osid_markers.Containable):
    """A node interface for hierarchical objects.

    The ``Id`` of the node is the ``Id`` of the object represented at
    this node.

    """
    



    def is_root(self):
        """Tests if this node is a root in the hierarchy (has no parents).

        A node may have no more parents available in this node structure
        but is not a root in the hierarchy. If both ``is_root()`` and
        ``has_parents()`` is false, the parents of this node may be
        accessed thorugh another node structure retrieval.

        return: (boolean) - ``true`` if this node is a root in the
                hierarchy, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def has_parents(self):
        """Tests if any parents are available in this node structure.

        There may be no more parents in this node structure however
        there may be parents that exist in the hierarchy.

        return: (boolean) - ``true`` if this node has parents, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_parent_ids(self):
        """Gets the parents of this node.

        return: (osid.id.IdList) - the parents of this node
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    parent_ids = property(fget=get_parent_ids)


    def is_leaf(self):
        """Tests if this node is a leaf in the hierarchy (has no children).

        A node may have no more children available in this node
        structure but is not a leaf in the hierarchy. If both
        ``is_leaf()`` and ``has_children()`` is false, the children of
        this node may be accessed thorugh another node structure
        retrieval.

        return: (boolean) - ``true`` if this node is a leaf in the
                hierarchy, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def has_children(self):
        """Tests if any children are available in this node structure.

        There may be no more children available in this node structure
        but this node may have children in the hierarchy.

        return: (boolean) - ``true`` if this node has children,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_child_ids(self):
        """Gets the children of this node.

        return: (osid.id.IdList) - the children of this node
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    child_ids = property(fget=get_child_ids)


