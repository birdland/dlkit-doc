from ..osid import markers as osid_markers


class Version(osid_markers.OsidPrimitive):
    """A ``Version`` represents a version in a scheme."""
    def get_scheme(self):
        """Gets the versioining scheme as a type.

        :return: the versioning scheme type
        :rtype: ``osid.type.Type``

        """
        return # osid.type.Type

    scheme = property(fget=get_scheme)

    def get_components(self):
        """Gets the components of the version.

        In a major.minor[.maintenance[.build]] scheme, an example is {3,
        0, 0}.

        :return: the version components
        :rtype: ``string``

        """
        return # string

    components = property(fget=get_components)


