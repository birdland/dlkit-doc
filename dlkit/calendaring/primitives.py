from ..osid import markers as osid_markers


class Time(osid_markers.OsidPrimitive):
    """The ``Time`` interface defines a time."""
    def get_time_type(self):
        """Gets the time type.

        :return: the time type
        :rtype: ``osid.type.Type``

        """
        return # osid.type.Type

    time_type = property(fget=get_time_type)

    def get_hour(self):
        """Gets the hour of the day 0-23.

        :return: the hour of the day
        :rtype: ``cardinal``

        """
        return # cardinal

    hour = property(fget=get_hour)

    def get_minute(self):
        """Gets the minute of the hour 0-59.

        :return: the minute of the hour
        :rtype: ``cardinal``

        """
        return # cardinal

    minute = property(fget=get_minute)

    def get_second(self):
        """Gets the second of the minute 0-59.

        :return: the second of the minute
        :rtype: ``cardinal``

        """
        return # cardinal

    second = property(fget=get_second)

    def get_milliseconds(self):
        """Gets the number of milliseconds in this second 0-999.

        A millisecond is one thousandth of a second.

        :return: the milliseconds of the second
        :rtype: ``cardinal``

        """
        return # cardinal

    milliseconds = property(fget=get_milliseconds)

    def get_microseconds(self):
        """Gets the number of microseconds of the second 0-999.

        A microsecond is one millionth of a second.

        :return: the micrseconds of the millisecond
        :rtype: ``cardinal``

        """
        return # cardinal

    microseconds = property(fget=get_microseconds)

    def get_nanoseconds(self):
        """Gets the number of nanoseconds of the microsecond 0-999.

        A nanosecond is one billionth of a second.

        :return: the nanoseconds of the microsecond
        :rtype: ``cardinal``

        """
        return # cardinal

    nanoseconds = property(fget=get_nanoseconds)

    def get_picoseconds(self):
        """Gets the number of picoseconds of the nanosecond 0-999.

        A picosecond is one trillionth of a second.

        :return: the picoseconds of the nanosecond
        :rtype: ``cardinal``

        """
        return # cardinal

    picoseconds = property(fget=get_picoseconds)

    def get_femtoseconds(self):
        """Gets the number of femtoseconds of the picosecond 0-999.

        A femtosecond is one quadrillionth of a second.

        :return: the femtoseconds of the picosecond
        :rtype: ``cardinal``

        """
        return # cardinal

    femtoseconds = property(fget=get_femtoseconds)

    def get_attoseconds(self):
        """Gets the number of attoseconds of the femtoseconds 0-999.

        An attosecond is one quintillionth of a second.

        :return: the attoseconds of the femtosecond
        :rtype: ``cardinal``

        """
        return # cardinal

    attoseconds = property(fget=get_attoseconds)

    def get_zeptoseconds(self):
        """Gets the number of zeptoseconds of the attosecond 0-999.

        A zeptosecond is one sextillionth of a second.

        :return: the zeptoseconds of the attosecond
        :rtype: ``cardinal``

        """
        return # cardinal

    zeptoseconds = property(fget=get_zeptoseconds)

    def get_yoctoseconds(self):
        """Gets the number of yoctoseconds of the picosecond 0-999.

        A yoctosecond is one septillionth of a second. This is getting
        quite small.

        :return: the yoctoseconds of the picosecond
        :rtype: ``cardinal``

        """
        return # cardinal

    yoctoseconds = property(fget=get_yoctoseconds)

    def get_xoxxoseconds(self):
        """Gets the number of xoxxoseconds of the yoctosecond 0-999.

        A xoxxosecond is one octillionth of a second. We're going with
        Rudy Rucker here.

        :return: the xoxxoseconds of the yoctosecond
        :rtype: ``cardinal``

        """
        return # cardinal

    xoxxoseconds = property(fget=get_xoxxoseconds)

    def get_weebleseconds(self):
        """Gets the number of weebleseconds of the xoxxosecond 0-999.

        A weeblesecond is one nonillionth of a second.

        :return: the weebleseconds of the xoxxoseconds
        :rtype: ``cardinal``

        """
        return # cardinal

    weebleseconds = property(fget=get_weebleseconds)

    def get_vatoseconds(self):
        """Gets the number of vatoseconds of the xoxxosecond 0-999.

        A vatosecond is one decillionth of a second.

        :return: the vatoseconds of the weeblesecond
        :rtype: ``cardinal``

        """
        return # cardinal

    vatoseconds = property(fget=get_vatoseconds)

    def get_undaseconds(self):
        """Gets the number of undaseconds of the vatosecond 0-999.

        An undasecond is one unadecillionth of a second.

        :return: the undaseconds of the vatosecond
        :rtype: ``cardinal``

        """
        return # cardinal

    undaseconds = property(fget=get_undaseconds)

    def get_planck_seconds(self):
        """Gets the number of Plancks of the vatoseconds.

        A Planck is 10 quattuordecillionths of a second.

        :return: the plancks of the undasecond
        :rtype: ``cardinal``

        """
        return # cardinal

    planck_seconds = property(fget=get_planck_seconds)

    def get_granularity(self):
        """Gets the granularity of this time.

        The granularity indicates the resolution of the clock. More
        precision than what is specified in this method cannot be
        inferred from the available data.

        :return: granularity
        :rtype: ``osid.calendaring.DateTimeResolution``

        """
        return # osid.calendaring.DateTimeResolution

    granularity = property(fget=get_granularity)

    def get_granularity_multiplier(self):
        """If the granularity of the time equals ``get_granularity(),`` then the multiplier is 1.

        This method may return a different number when the granularity
        differs from one of the defined resolutions.

        :return: granularity multiplier
        :rtype: ``cardinal``

        """
        return # cardinal

    granularity_multiplier = property(fget=get_granularity_multiplier)


class DateTime(osid_markers.OsidPrimitive):
    """The DateTime interface defines a date and/or time.

    This interface provides a very broad range of dates, describes more
    or less precision, and/or conveys an uncertainty. A number of
    convenience methods for retrieving time elements are available but
    only those methods covered by the specified granularity are valid.

    A typical example is describing a day where the time isn't known,
    and the event did not occur at midnight.
      getMillennium() == 2
      getCentury() == 18
      getYear() == 1776
      getMonth() == 7
      getDay() == 4
      getHour() == 0
      getGranularity() == DateTimeResolution.DAY
      definesUncertainty() == false



    Another example showing that the time is probably 1pm but could have
    been as late as 3pm or early as noon.
      getMillennium() == 3
      getCentury() == 21
      getYear() == 2008
      getMonth() == 3
      getDay() == 17
      getHour() == 13
      getMinute() == 0
      getGranularity() == TimeResolution.MINUTE
      definesUncertainty() == true
      getUncertaintyGranularity() == DateTimeResolution.HOUR
      getUncertaintyMinus() == 1
      getUncertaintyPlus == 2



    An example marking the birth of the universe. 13.73 billion years
    +/- 120 million years. The granularity suggests that no more
    resolution than one million years can be inferred from the "clock",
    making errors in the exact number of millennia insignificant.
      getEpoch() == -13,730
      getMillennium() == 0
      getCentury() == 0
      getYear() == 0
      getGranularity() == TimeResolution.EPOCH
      definesUncertainty() == true
      getUncertaintyGranularity() == DateTimeResolution.EPOCH
      getUncertaintyMinus() == 120
      getUncertaintyPlus == 120



    """
    def get_calendar_type(self):
        """Gets the calendar type.

        :return: the calendar type
        :rtype: ``osid.type.Type``

        """
        return # osid.type.Type

    calendar_type = property(fget=get_calendar_type)

    def get_aeon(self):
        """Gets the aeon starting from 1.

        An aeon is 1B years.

        :return: the aeon
        :rtype: ``integer``

        """
        return # integer

    aeon = property(fget=get_aeon)

    def get_epoch(self):
        """Gets the epoch starting from 1.

        An epoch is 1M years.

        :return: the eposh
        :rtype: ``integer``

        """
        return # integer

    epoch = property(fget=get_epoch)

    def get_millennium(self):
        """Gets the millennium starting from 1.

        A millenium is 1,000 years.

        :return: the millennium
        :rtype: ``integer``

        """
        return # integer

    millennium = property(fget=get_millennium)

    def get_century(self):
        """Gets the century starting from 1.

        :return: the century
        :rtype: ``integer``

        """
        return # integer

    century = property(fget=get_century)

    def get_year(self):
        """Gets the year starting from 1.

        :return: the year
        :rtype: ``integer``

        """
        return # integer

    year = property(fget=get_year)

    def get_month(self):
        """Gets the month number starting from 1.

        :return: the month
        :rtype: ``cardinal``

        """
        return # cardinal

    month = property(fget=get_month)

    def get_day(self):
        """Gets the day of the month starting from 1.

        :return: the day of the month
        :rtype: ``cardinal``

        """
        return # cardinal

    day = property(fget=get_day)

    def get_time_type(self):
        """Gets the time type.

        :return: the time type
        :rtype: ``osid.type.Type``

        """
        return # osid.type.Type

    time_type = property(fget=get_time_type)

    def get_hour(self):
        """Gets the hour of the day 0-23.

        :return: the hour of the day
        :rtype: ``cardinal``

        """
        return # cardinal

    hour = property(fget=get_hour)

    def get_minute(self):
        """Gets the minute of the hour 0-59.

        :return: the minute of the hour
        :rtype: ``cardinal``

        """
        return # cardinal

    minute = property(fget=get_minute)

    def get_second(self):
        """Gets the second of the minute 0-59.

        :return: the second of the minute
        :rtype: ``cardinal``

        """
        return # cardinal

    second = property(fget=get_second)

    def get_milliseconds(self):
        """Gets the number of milliseconds in this second 0-999.

        A millisecond is one thousandth of a second.

        :return: the milliseconds of the second
        :rtype: ``cardinal``

        """
        return # cardinal

    milliseconds = property(fget=get_milliseconds)

    def get_microseconds(self):
        """Gets the number of microseconds of the second 0-999.

        A microsecond is one millionth of a second.

        :return: the micrseconds of the millisecond
        :rtype: ``cardinal``

        """
        return # cardinal

    microseconds = property(fget=get_microseconds)

    def get_nanoseconds(self):
        """Gets the number of nanoseconds of the microsecond 0-999.

        A nanosecond is one billionth of a second.

        :return: the nanoseconds of the microsecond
        :rtype: ``cardinal``

        """
        return # cardinal

    nanoseconds = property(fget=get_nanoseconds)

    def get_picoseconds(self):
        """Gets the number of picoseconds of the nanosecond 0-999.

        A picosecond is one trillionth of a second.

        :return: the picoseconds of the nanosecond
        :rtype: ``cardinal``

        """
        return # cardinal

    picoseconds = property(fget=get_picoseconds)

    def get_femtoseconds(self):
        """Gets the number of femtoseconds of the picosecond 0-999.

        A femtosecond is one quadrillionth of a second.

        :return: the femtoseconds of the picosecond
        :rtype: ``cardinal``

        """
        return # cardinal

    femtoseconds = property(fget=get_femtoseconds)

    def get_attoseconds(self):
        """Gets the number of attoseconds of the femtoseconds 0-999.

        An attosecond is one quintillionth of a second.

        :return: the attoseconds of the femtosecond
        :rtype: ``cardinal``

        """
        return # cardinal

    attoseconds = property(fget=get_attoseconds)

    def get_zeptoseconds(self):
        """Gets the number of zeptoseconds of the attosecond 0-999.

        A zeptosecond is one sextillionth of a second.

        :return: the zeptoseconds of the attosecond
        :rtype: ``cardinal``

        """
        return # cardinal

    zeptoseconds = property(fget=get_zeptoseconds)

    def get_yoctoseconds(self):
        """Gets the number of yoctoseconds of the picosecond 0-999.

        A yoctosecond is one septillionth of a second. This is getting
        quite small.

        :return: the yoctoseconds of the picosecond
        :rtype: ``cardinal``

        """
        return # cardinal

    yoctoseconds = property(fget=get_yoctoseconds)

    def get_xoxxoseconds(self):
        """Gets the number of xoxxoseconds of the yoctosecond 0-999.

        A xoxxosecond is one octillionth of a second. We're going with
        Rudy Rucker here.

        :return: the xoxxoseconds of the yoctosecond
        :rtype: ``cardinal``

        """
        return # cardinal

    xoxxoseconds = property(fget=get_xoxxoseconds)

    def get_weebleseconds(self):
        """Gets the number of weebleseconds of the xoxxosecond 0-999.

        A weeblesecond is one nonillionth of a second.

        :return: the weebleseconds of the xoxxoseconds
        :rtype: ``cardinal``

        """
        return # cardinal

    weebleseconds = property(fget=get_weebleseconds)

    def get_vatoseconds(self):
        """Gets the number of vatoseconds of the xoxxosecond 0-999.

        A vatosecond is one decillionth of a second.

        :return: the vatoseconds of the weeblesecond
        :rtype: ``cardinal``

        """
        return # cardinal

    vatoseconds = property(fget=get_vatoseconds)

    def get_undaseconds(self):
        """Gets the number of undaseconds of the vatosecond 0-999.

        An undasecond is one unadecillionth of a second.

        :return: the undaseconds of the vatosecond
        :rtype: ``cardinal``

        """
        return # cardinal

    undaseconds = property(fget=get_undaseconds)

    def get_planck_seconds(self):
        """Gets the number of Plancks of the vatoseconds.

        A Planck is 10 quattuordecillionths of a second.

        :return: the plancks of the undasecond
        :rtype: ``cardinal``

        """
        return # cardinal

    planck_seconds = property(fget=get_planck_seconds)

    def get_granularity(self):
        """Gets the granularity of this time.

        The granularity indicates the resolution of the clock. More
        precision than what is specified in this method cannot be
        inferred from the available data.

        :return: granularity
        :rtype: ``osid.calendaring.DateTimeResolution``

        """
        return # osid.calendaring.DateTimeResolution

    granularity = property(fget=get_granularity)

    def get_granularity_multiplier(self):
        """If the granularity of the time equals ``get_granularity(),`` then the multiplier is 1.

        This method may return a different number when the granularity
        differs from one of the defined resolutions.

        :return: granularity multiplier
        :rtype: ``cardinal``

        """
        return # cardinal

    granularity_multiplier = property(fget=get_granularity_multiplier)

    def defines_uncertainty(self):
        """Tests if uncertainty is defined for this time.

        :return: ``true`` if uncertainty is defined, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_uncertainty_units(self):
        """Gets the units of the uncertainty.

        :return: units of the uncertainty
        :rtype: ``osid.calendaring.DateTimeResolution``
        :raise: ``IllegalState`` -- ``defines_uncertainty()`` is ``false``

        """
        return # osid.calendaring.DateTimeResolution

    uncertainty_units = property(fget=get_uncertainty_units)

    def get_uncertainty_minus(self):
        """Gets the uncertainty of this time in the negative direction.

        :return: the uncertainty under this value
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- ``defines_uncertainty()`` is ``false``

        """
        return # cardinal

    uncertainty_minus = property(fget=get_uncertainty_minus)

    def get_uncertainty_plus(self):
        """Gets the uncertainty of this time in the positive direction.

        :return: the uncertainty over this value
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- ``defines_uncertainty()`` is ``false``

        """
        return # cardinal

    uncertainty_plus = property(fget=get_uncertainty_plus)

    def is_uncertainty_date_inclusive(self):
        """Tests if the uncertainty is inclusive of all dates.

        An inclusive uncertainty includes the entire range specified by
        the uncertainty units e.g. +/- 1 year includes all of the months
        and days within that interval. A non-inclusive uncertainty would
        mean the year is uncertain but the month and day is certain.

        :return: ``true`` if the uncertainty includes all dates, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``defines_uncertainty()`` is ``false``

        """
        return # boolean

    def is_uncertainty_time_inclusive(self):
        """Tests if the uncertainty is time inclusive.

        An inclusive uncertainty includes the entire range specified by
        the uncertainty units e.g. +/- 1 year includes all of the
        seconds within that interval. A non-inclusive uncertainty would
        mean the year is uncertain but the time is certain.

        :return: ``true`` if the uncertainty includes all times, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``defines_uncertainty()`` is ``false``

        """
        return # boolean


class Duration(osid_markers.OsidPrimitive):
    """The ``Duration`` a length of time."""
    def get_calendar_type(self):
        """Gets the calendar type.

        :return: the calendar type
        :rtype: ``osid.type.Type``

        """
        return # osid.type.Type

    calendar_type = property(fget=get_calendar_type)

    def get_time_type(self):
        """Gets the time type.

        :return: the time type
        :rtype: ``osid.type.Type``

        """
        return # osid.type.Type

    time_type = property(fget=get_time_type)

    def get_aeons(self):
        """Gets the number of aeons.

        An aeon is 1B years.

        :return: the number of aeons
        :rtype: ``decimal``

        """
        return # decimal

    aeons = property(fget=get_aeons)

    def get_epochs(self):
        """Gets the number of epochs.

        An epoch is 1M years.

        :return: the number of epochs
        :rtype: ``decimal``

        """
        return # decimal

    epochs = property(fget=get_epochs)

    def get_millennia(self):
        """Gets the number of millennia.

        A millennium is 1,000 years.

        :return: the number of millennia
        :rtype: ``decimal``

        """
        return # decimal

    millennia = property(fget=get_millennia)

    def get_centuries(self):
        """Gets the number of centuries.

        :return: the number of centuries
        :rtype: ``decimal``

        """
        return # decimal

    centuries = property(fget=get_centuries)

    def get_scores(self):
        """Gets the number of scores.

        :return: the number of scores
        :rtype: ``decimal``

        """
        return # decimal

    scores = property(fget=get_scores)

    def get_bluemoons(self):
        """Gets the number of blue moons.

        :return: the number of blue moons
        :rtype: ``decimal``

        """
        return # decimal

    bluemoons = property(fget=get_bluemoons)

    def get_years(self):
        """Gets the number of years.

        :return: the number of years
        :rtype: ``decimal``

        """
        return # decimal

    years = property(fget=get_years)

    def get_months(self):
        """Gets the number of months.

        :return: the number of months
        :rtype: ``decimal``

        """
        return # decimal

    months = property(fget=get_months)

    def get_weeks(self):
        """Gets the number of weeks.

        :return: the number of weeks
        :rtype: ``decimal``

        """
        return # decimal

    weeks = property(fget=get_weeks)

    def get_days(self):
        """Gets the number of days.

        :return: the number of days
        :rtype: ``decimal``

        """
        return # decimal

    days = property(fget=get_days)

    def get_hours(self):
        """Gets the number of hours.

        :return: the number of hours
        :rtype: ``decimal``

        """
        return # decimal

    hours = property(fget=get_hours)

    def get_minutes(self):
        """Gets the number of minutes.

        :return: the number of minutes
        :rtype: ``decimal``

        """
        return # decimal

    minutes = property(fget=get_minutes)

    def get_seconds(self):
        """Gets the number of seconds.

        :return: the number of seconds
        :rtype: ``decimal``

        """
        return # decimal

    seconds = property(fget=get_seconds)

    def get_milliseconds(self):
        """Gets the number of milliseconds.

        A millisecond is one thousandth of a second.

        :return: the number of milliseconds
        :rtype: ``decimal``

        """
        return # decimal

    milliseconds = property(fget=get_milliseconds)

    def get_microseconds(self):
        """Gets the number of microseconds.

        A microsecond is one millionth of a second.

        :return: the number of micrseconds
        :rtype: ``decimal``

        """
        return # decimal

    microseconds = property(fget=get_microseconds)

    def get_nanoseconds(self):
        """Gets the number of nanoseconds.

        A nanosecond is one billionth of a second.

        :return: the number of nanoseconds
        :rtype: ``decimal``

        """
        return # decimal

    nanoseconds = property(fget=get_nanoseconds)

    def get_picoseconds(self):
        """Gets the number of picoseconds.

        A picosecond is one trillionth of a second.

        :return: the number of picoseconds
        :rtype: ``decimal``

        """
        return # decimal

    picoseconds = property(fget=get_picoseconds)

    def get_femtoseconds(self):
        """Gets the number of femtoseconds.

        A femtosecond is one quadrillionth of a second.

        :return: the number of femtoseconds
        :rtype: ``decimal``

        """
        return # decimal

    femtoseconds = property(fget=get_femtoseconds)

    def get_attoseconds(self):
        """Gets the number of attoseconds.

        An attosecond is one quintillionth of a second.

        :return: the number of attoseconds
        :rtype: ``decimal``

        """
        return # decimal

    attoseconds = property(fget=get_attoseconds)

    def get_zeptoseconds(self):
        """Gets the number of zeptoseconds.

        A zeptosecond is one sextillionth of a second.

        :return: the number of zeptoseconds
        :rtype: ``decimal``

        """
        return # decimal

    zeptoseconds = property(fget=get_zeptoseconds)

    def get_yoctoseconds(self):
        """Gets the number of yoctoseconds.

        A yoctosecond is one septillionth of a second. This is getting
        quite small.

        :return: the number of yoctoseconds
        :rtype: ``decimal``

        """
        return # decimal

    yoctoseconds = property(fget=get_yoctoseconds)

    def get_xoxxoseconds(self):
        """Gets the number of xoxxoseconds.

        A xoxxosecond is one octillionth of a second. We're going with
        Rudy Rucker here.

        :return: the number of xoxxoseconds
        :rtype: ``decimal``

        """
        return # decimal

    xoxxoseconds = property(fget=get_xoxxoseconds)

    def get_weebleseconds(self):
        """Gets the number of weebleseconds.

        A weeblesecond is one nonillionth of a second.

        :return: the number of weebleseconds
        :rtype: ``decimal``

        """
        return # decimal

    weebleseconds = property(fget=get_weebleseconds)

    def get_vatoseconds(self):
        """Gets the number of vatoseconds.

        A vatosecond is one decillionth of a second.

        :return: the number of vatoseconds
        :rtype: ``decimal``

        """
        return # decimal

    vatoseconds = property(fget=get_vatoseconds)

    def get_undaseconds(self):
        """Gets the number of undaseconds.

        An undasecond is one unadecillionth of a second.

        :return: the number of undaseconds
        :rtype: ``decimal``

        """
        return # decimal

    undaseconds = property(fget=get_undaseconds)

    def get_planck_seconds(self):
        """Gets the number of Planck sseconds.

        A Planck is 10 quattuordecillionths of a second.

        :return: the number of planck seconds
        :rtype: ``decimal``

        """
        return # decimal

    planck_seconds = property(fget=get_planck_seconds)

    def get_granularity(self):
        """Gets the granularity of this duration.

        The granularity indicates the resolution of the clock. More
        precision than what is specified in this method cannot be
        inferred from the available data.

        :return: the time units
        :rtype: ``osid.calendaring.DateTimeResolution``

        """
        return # osid.calendaring.DateTimeResolution

    granularity = property(fget=get_granularity)

    def get_granularity_multiplier(self):
        """If the granularity of the time equals ``get_granularity(),`` then the multiplier is 1.

        This method may return a different number when the granularity
        differs from one of the defined resolutions.

        :return: granularity multiplier
        :rtype: ``cardinal``

        """
        return # cardinal

    granularity_multiplier = property(fget=get_granularity_multiplier)

    def defines_uncertainty(self):
        """Tests if uncertainty is defined for this time.

        :return: ``true`` if uncertainty is defined, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_uncertainty_units(self):
        """Gets the units of the uncertainty.

        :return: units of the uncertainty
        :rtype: ``osid.calendaring.DateTimeResolution``
        :raise: ``IllegalState`` -- ``defines_uncertainty()`` is ``false``

        """
        return # osid.calendaring.DateTimeResolution

    uncertainty_units = property(fget=get_uncertainty_units)

    def get_uncertainty_minus(self):
        """Gets the uncertainty of this time in the negative direction.

        :return: the uncertainty under this value
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- ``defines_uncertainty()`` is ``false``

        """
        return # cardinal

    uncertainty_minus = property(fget=get_uncertainty_minus)

    def get_uncertainty_plus(self):
        """Gets the uncertainty of this time in the positive direction.

        :return: the uncertainty over this value
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- ``defines_uncertainty()`` is ``false``

        """
        return # cardinal

    uncertainty_plus = property(fget=get_uncertainty_plus)


