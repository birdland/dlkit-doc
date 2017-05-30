
from ..osid import objects as osid_objects


class Locale:
    """A locale is a collection of types.

    ``Locale`` defines a set of types that together define the
    formatting, language, calendaring, and currency for a locale or
    culture.

    """

    def get_language_type(self):
        """Gets the language ``Type``.

        :return: the language type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    language_type = property(fget=get_language_type)

    def get_script_type(self):
        """Gets the script ``Type``.

        :return: the script type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    script_type = property(fget=get_script_type)

    def get_calendar_type(self):
        """Gets the calendar ``Type``.

        :return: the calendar type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    calendar_type = property(fget=get_calendar_type)

    def get_time_type(self):
        """Gets the time ``Type``.

        :return: the time type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    time_type = property(fget=get_time_type)

    def get_currency_type(self):
        """Gets the currency ``Type``.

        :return: the currency type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    currency_type = property(fget=get_currency_type)

    def get_unit_system_type(self):
        """Gets the unit system ``Type``.

        :return: the unit system type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    unit_system_type = property(fget=get_unit_system_type)

    def get_numeric_format_type(self):
        """Gets the numeric format ``Type``.

        :return: the numeric format type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    numeric_format_type = property(fget=get_numeric_format_type)

    def get_calendar_format_type(self):
        """Gets the calendar format ``Type``.

        :return: the calendar format type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    calendar_format_type = property(fget=get_calendar_format_type)

    def get_time_format_type(self):
        """Gets the time format ``Type``.

        :return: the time format type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    time_format_type = property(fget=get_time_format_type)

    def get_currency_format_type(self):
        """Gets the currency format ``Type``.

        :return: the currency format type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    currency_format_type = property(fget=get_currency_format_type)

    def get_coordinate_format_type(self):
        """Gets the coordinate format ``Type``.

        :return: the coordinate format type
        :rtype: ``osid.type.Type``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    coordinate_format_type = property(fget=get_coordinate_format_type)


class LocaleList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``LocaleList`` provides a means for accessing ``Locale`` elements sequentially either one at a time or many at a time.

    Examples: while (ll.hasNext()) { Locale locale = ll.getNextLocale();
    }

    or
      while (ll.hasNext()) {
           Locale[] locales = ll.getNextLocales(ll.available());
      }

    """

    def get_next_locale(self):
        """Gets the next ``Locale`` in this list.

        :return: the next ``Locale`` in this list. The ``has_next()`` method should be used to test that a next ``Locale`` is available before calling this method.
        :rtype: ``osid.locale.Locale``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.Locale

    next_locale = property(fget=get_next_locale)

    def get_next_locales(self, n):
        """Gets the next set of ``Locale`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Locale`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Locale`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.locale.Locale``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.Locale


