from ..osid import markers as osid_markers


class Coordinate(osid_markers.OsidPrimitive):
    """A coordinate represents a position."""
    def get_coordinate_type(self):
        """Gets the ``Type`` of this ``Coordinate`` which indicates the format of the coordinate data.

        :return: the coordinate type
        :rtype: ``osid.type.Type``

        """
        return # osid.type.Type

    coordinate_type = property(fget=get_coordinate_type)

    def get_dimensions(self):
        """Gets the number of dimensions available in this coordinate.

        :return: the number of dimensions
        :rtype: ``cardinal``

        """
        return # cardinal

    dimensions = property(fget=get_dimensions)

    def get_values(self):
        """Gets the values of this coordinate.

        The size of the returned array should equal ``getDimensions()``.

        :return: the coordinate values
        :rtype: ``decimal``

        """
        return # decimal

    values = property(fget=get_values)

    def defines_uncertainty(self):
        """Tests if uncertainty is defined for this heading.

        :return: ``true`` if uncertainty is defined, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_uncertainty_minus(self):
        """Gets the uncertainty in the negtive direction for each value of this coordinate.

        The size of the returned array is typically one less than
        ``getDimensions()``.

        :return: the negative uncertainty values
        :rtype: ``decimal``

        """
        return # decimal

    uncertainty_minus = property(fget=get_uncertainty_minus)

    def get_uncertainty_plus(self):
        """Gets the uncertainty in the positive direction for each value of this coordinate.

        The size of the returned array is typically one less than
        ``getDimensions()``.

        :return: the positive uncertainty values
        :rtype: ``decimal``

        """
        return # decimal

    uncertainty_plus = property(fget=get_uncertainty_plus)


class Speed(osid_markers.OsidPrimitive):
    """A speed is a distance traveled over a unit of time."""
    def get_distance(self):
        """Gets the distance.

        :return: the distance
        :rtype: ``osid.mapping.Distance``

        """
        return # osid.mapping.Distance

    distance = property(fget=get_distance)

    def get_time_unit(self):
        """Gets the time unit.

        :return: the time unit
        :rtype: ``osid.calendaring.DateTimeResolution``

        """
        return # osid.calendaring.DateTimeResolution

    time_unit = property(fget=get_time_unit)


class Heading(osid_markers.OsidPrimitive):
    """A heading represents a direction."""
    def get_heading_type(self):
        """Gets the ``Type`` of this ``Heading`` which indicates the format of the heading values.

        :return: the coordinate type
        :rtype: ``osid.type.Type``

        """
        return # osid.type.Type

    heading_type = property(fget=get_heading_type)

    def get_dimensions(self):
        """Gets the number of dimensions of motion.

        :return: the number of dimensions
        :rtype: ``cardinal``

        """
        return # cardinal

    dimensions = property(fget=get_dimensions)

    def get_values(self):
        """Gets the values of this heading The size of the returned array is typically one less than ``getDimensions()``.

        :return: the heading values
        :rtype: ``decimal``

        """
        return # decimal

    values = property(fget=get_values)

    def defines_uncertainty(self):
        """Tests if uncertainty is defined for this heading.

        :return: ``true`` if uncertainty is defined, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_uncertainty_minus(self):
        """Gets the uncertainty in the negtive direction for each value of this heading.

        The size of the returned array is typically one less than
        ``getDimensions()``.

        :return: the negative uncertainty values
        :rtype: ``decimal``

        """
        return # decimal

    uncertainty_minus = property(fget=get_uncertainty_minus)

    def get_uncertainty_plus(self):
        """Gets the uncertainty in the positive direction for each value of this heading.

        The size of the returned array is typically one less than
        ``getDimensions()``.

        :return: the positive uncertainty values
        :rtype: ``decimal``

        """
        return # decimal

    uncertainty_plus = property(fget=get_uncertainty_plus)


class SpatialUnit(osid_markers.OsidPrimitive, osid_markers.Extensible):
    """A spatial unit can represent a single position or an area constructed of multiple positions or shapes.

    The data describing the spatial unit is defined in the record
    indicated by the record type.

    """
    def get_center_coordinate(self):
        """Gets a single corrdinate to represent the center of this spatial unit.

        :return: the center coordinate
        :rtype: ``osid.mapping.Coordinate``

        """
        return # osid.mapping.Coordinate

    center_coordinate = property(fget=get_center_coordinate)

    def get_bounding_coordinates(self):
        """Gets a list of bounding coordinates of this spatial unit.

        :return: the bounding coordinates
        :rtype: ``osid.mapping.CoordinateList``

        """
        return # osid.mapping.CoordinateList

    bounding_coordinates = property(fget=get_bounding_coordinates)

    def get_spatial_unit_record(self, spatial_unit_record_type):
        """Gets the spatial unit record corresponding to the given ``SpatialUnit`` record ``Type``.

        The ``spatial_unit_record_type`` may be the ``Type`` returned in
        ``get_record_types()`` or any of its parents in a ``Type``
        hierarchy where ``has_record_type(spatial_unit_record_type)`` is
        ``true`` .

        :param spatial_unit_record_type: the type of spatial unit record to retrieve
        :type spatial_unit_record_type: ``osid.type.Type``
        :return: the spatial unit record
        :rtype: ``osid.mapping.records.SpatialUnitRecord``
        :raise: ``NullArgument`` -- ``spatial_unit_record_type`` is ``null``
        :raise: ``Unsupported`` -- ``has_record_type(spatial_unit_record_type)`` is ``false``

        """
        return # osid.mapping.records.SpatialUnitRecord


class Distance(osid_markers.OsidPrimitive):
    """A distance."""
    def get_yotta_parsecs(self):
        """Gets the number of yottaparsecs.

        You should budget extra time to travel a yottaparsec.

        :return: the number of yottaparsecs
        :rtype: ``decimal``

        """
        return # decimal

    yotta_parsecs = property(fget=get_yotta_parsecs)

    def get_exa_parsecs(self):
        """Gets the number of exaparsecs.

        An exaparsec is much shorter.

        :return: the number of exaparsecs
        :rtype: ``decimal``

        """
        return # decimal

    exa_parsecs = property(fget=get_exa_parsecs)

    def get_giga_parsecs(self):
        """Get sthe number of gigaparsecs.

        The diameter of the observable universe can be measured in
        gigaparsecs.

        :return: the number of gigaparsecs
        :rtype: ``decimal``

        """
        return # decimal

    giga_parsecs = property(fget=get_giga_parsecs)

    def get_yottameters(self):
        """Gets this distance in yottameters.

        A yottameter is 1 trillion terameters.

        :return: the number of yottameters
        :rtype: ``decimal``

        """
        return # decimal

    yottameters = property(fget=get_yottameters)

    def get_zettameters(self):
        """Gets this distance in zettameters.

        A zettameter is one billion terameters.

        :return: the number of zettameters
        :rtype: ``decimal``

        """
        return # decimal

    zettameters = property(fget=get_zettameters)

    def get_exameters(self):
        """Gets this distance in exameters.

        A exameter is 1BB meters.

        :return: the number of exameters
        :rtype: ``decimal``

        """
        return # decimal

    exameters = property(fget=get_exameters)

    def get_parsecs(self):
        """Gets this distance in parsecs.

        A parsec is 30,857,000,000,000,000 meters.

        :return: the number of parsecs
        :rtype: ``decimal``

        """
        return # decimal

    parsecs = property(fget=get_parsecs)

    def get_light_years(self):
        """Gets this distance in light years.

        A light year is 9,460,730,472,580,800 meters.

        :return: the number of light years
        :rtype: ``decimal``

        """
        return # decimal

    light_years = property(fget=get_light_years)

    def get_petameters(self):
        """Gets this distance in petameters.

        A petameter is 1M gigameters.

        :return: the number of petameters
        :rtype: ``decimal``

        """
        return # decimal

    petameters = property(fget=get_petameters)

    def get_terameters(self):
        """Gets this distance in terameters.

        A terameter is one trillion meters.

        :return: the number of terameters
        :rtype: ``decimal``

        """
        return # decimal

    terameters = property(fget=get_terameters)

    def get_gigameters(self):
        """Gets this distance in gigameters.

        A gigameter is 1B meters.

        :return: the number of gigameters
        :rtype: ``decimal``

        """
        return # decimal

    gigameters = property(fget=get_gigameters)

    def get_megameters(self):
        """Gets this distance in megameters.

        A megameter is longer than a megaman.

        :return: the number of megameters
        :rtype: ``decimal``

        """
        return # decimal

    megameters = property(fget=get_megameters)

    def get_kilometers(self):
        """Gets this distance kilometers.

        A kilometer is 1,000 meters.

        :return: the number of kilometres
        :rtype: ``decimal``

        """
        return # decimal

    kilometers = property(fget=get_kilometers)

    def get_meters(self):
        """Gets this distance in meters.

        A meter is 0.0049709695379 furlongs.

        :return: the number of meters
        :rtype: ``decimal``

        """
        return # decimal

    meters = property(fget=get_meters)

    def get_atto_parsecs(self):
        """Gets this distance in attoparsecs.

        :return: the number of attoparsecs
        :rtype: ``decimal``

        """
        return # decimal

    atto_parsecs = property(fget=get_atto_parsecs)

    def get_centimeters(self):
        """Gets this distance in centimeters.

        A centimeter is one hundreth of a meter.

        :return: the number of centimeters
        :rtype: ``decimal``

        """
        return # decimal

    centimeters = property(fget=get_centimeters)

    def get_millimeters(self):
        """Gets this distance in millimeters.

        A millimeter is one thousandth of a meter.

        :return: the number of millimeters
        :rtype: ``decimal``

        """
        return # decimal

    millimeters = property(fget=get_millimeters)

    def get_microns(self):
        """Gets this distance in micrometers.

        A micron is one millionth of a meter.

        :return: the number of microns
        :rtype: ``decimal``

        """
        return # decimal

    microns = property(fget=get_microns)

    def get_nanometers(self):
        """Gets this distance in nanometers.

        A nanometer is one billionth of a meter.

        :return: the number of nanometers
        :rtype: ``decimal``

        """
        return # decimal

    nanometers = property(fget=get_nanometers)

    def get_angstroms(self):
        """Gets this distance in angstroms.

        An angstrom is one ten billionth of a meter.

        :return: the number of angstroms
        :rtype: ``decimal``

        """
        return # decimal

    angstroms = property(fget=get_angstroms)

    def get_picometers(self):
        """Gets this distance in picometers.

        A picometer is one trillionth of a meter.

        :return: the number of picometers
        :rtype: ``decimal``

        """
        return # decimal

    picometers = property(fget=get_picometers)

    def get_femtometers(self):
        """Gets this distance in femotometers.

        A femoto is one quadrillionth of a meter.

        :return: the number of femtometers
        :rtype: ``decimal``

        """
        return # decimal

    femtometers = property(fget=get_femtometers)

    def get_attometers(self):
        """Gets this distance in attometers.

        An attometer is one quintillionth of a meter.

        :return: the number of attometers
        :rtype: ``decimal``

        """
        return # decimal

    attometers = property(fget=get_attometers)

    def get_zeptometers(self):
        """Gets this distance in zeptometers.

        A zeptometer is one sextillionth of a meter.

        :return: the number of zeptometers
        :rtype: ``decimal``

        """
        return # decimal

    zeptometers = property(fget=get_zeptometers)

    def get_yoctometers(self):
        """Gets this distance in yoctometers.

        A yoctometer is one septillionth of a meter.

        :return: the number of yoctometers
        :rtype: ``decimal``

        """
        return # decimal

    yoctometers = property(fget=get_yoctometers)

    def get_xoxxometers(self):
        """Gets this distance in xoxxometers.

        A xoxxometer is one octillionth of a meter.

        :return: the number of xoxxometers
        :rtype: ``decimal``

        """
        return # decimal

    xoxxometers = property(fget=get_xoxxometers)

    def get_weebleometers(self):
        """Gets this distance in weeblemeters.

        A weeblemeter is one nonillionth of a meter.

        :return: the number of weeblemeters
        :rtype: ``decimal``

        """
        return # decimal

    weebleometers = property(fget=get_weebleometers)

    def get_vatometers(self):
        """Gets this distance in vatometers.

        A vatometer is one decillionth of a meter.

        :return: the number of vatometers
        :rtype: ``decimal``

        """
        return # decimal

    vatometers = property(fget=get_vatometers)

    def get_plancks(self):
        """Gets this distance in plancks.

        Plancks are really small.

        :return: the number of plancks
        :rtype: ``decimal``

        """
        return # decimal

    plancks = property(fget=get_plancks)

    def get_granularity(self):
        """Gets the granularity of this distance.

        The granularity indicates the resolution of the yardstick. More
        precision than what is specified in this method cannot be
        inferred from the available data.

        :return: granularity
        :rtype: ``osid.mapping.DistanceResolution``

        """
        return # osid.mapping.DistanceResolution

    granularity = property(fget=get_granularity)

    def get_granularity_multiplier(self):
        """If the granularity of the measurement equals ``get_granularity(),`` then the multiplier is 1.

        This method may return a different number when the granularity
        differs from one of the defined resolutions.

        :return: granularity multiplier
        :rtype: ``cardinal``

        """
        return # cardinal

    granularity_multiplier = property(fget=get_granularity_multiplier)

    def defines_uncertainty(self):
        """Tests if uncertainty is defined for this distance.

        :return: ``true`` if uncertainty is defined, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_uncertainty_units(self):
        """Gets the units of the uncertainty.

        :return: units of the uncertainty
        :rtype: ``osid.mapping.DistanceResolution``
        :raise: ``IllegalState`` -- ``defines_uncertainty()`` is ``false``

        """
        return # osid.mapping.DistanceResolution

    uncertainty_units = property(fget=get_uncertainty_units)

    def get_uncertainty_minus(self):
        """Gets the uncertainty of this distance in the negative direction in meters.

        :return: the uncertainty under this value
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- ``defines_uncertainty()`` is ``false``

        """
        return # decimal

    uncertainty_minus = property(fget=get_uncertainty_minus)

    def get_uncertainty_plus(self):
        """Gets the uncertainty of this distance in the positive direction in meters.

        :return: the uncertainty over this value
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- ``defines_uncertainty()`` is ``false``

        """
        return # decimal

    uncertainty_plus = property(fget=get_uncertainty_plus)


