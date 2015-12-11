
from ..osid import markers as osid_markers


class Type(osid_markers.OsidPrimitive):
    """The Type is a form of identifier that is primarily used to identify interface specifications.

    The ``Type`` differs from ``Id`` in that it offers display
    information and ``Types`` may be arranged in hierarchies to indicate
    an extended interface. Semantically, an ``Id`` identifies any OSID
    object while the ``Type`` identifies a specification.

    The components of the Type that make up its identification are:

      * identifier: a unique key or guid
      * namespace: the namespace of the identifier
      * authority: the isuer of the identifier


    Persisting a type reference means to persist the above
    identification elements. In addition to these identifier components,
    A ``Type`` mai also provide some additional metadata such as a name,
    description and domain.

    """
    



    def get_display_name(self):
        """Gets the full display name of this ``Type``.

        return: (osid.locale.DisplayText) - the display name of this
                ``Type``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    display_name = property(fget=get_display_name)


    def get_display_label(self):
        """Gets the shorter display label for this ``Type``.

        Where a display name of a ``Type`` might be ``"`` Critical
        Logging Priority Type", the display label could be "critical".

        return: (osid.locale.DisplayText) - the display label for this
                ``Type``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    display_label = property(fget=get_display_label)


    def get_description(self):
        """Gets a description of this ``Type``.

        return: (osid.locale.DisplayText) - the description of this
                ``Type``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    description = property(fget=get_description)


    def get_domain(self):
        """Gets the domain.

        The domain can provide an information label about ths
        application space of this Type.

        return: (osid.locale.DisplayText) - the domain of this ``Type``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    domain = property(fget=get_domain)


    def get_authority(self):
        """Gets the authority of this ``Type``.

        The authority is a string used to ensure the uniqueness of this
        ``Type`` when using a non- federated identifier space.
        Generally, it is a domain name identifying the party responsible
        for this ``Type``. This method is used to compare one ``Type``
        to another.

        return: (string) - the authority of this ``Type``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    authority = property(fget=get_authority)


    def get_identifier_namespace(self):
        """Gets the namespace of the identifier.

        This method is used to compare one ``Type`` to another.

        return: (string) - the authority of this ``Type``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    identifier_namespace = property(fget=get_identifier_namespace)

    namespace = property(fget=get_identifier_namespace)


    def get_identifier(self):
        """Gets the identifier of this ``Type``.

        This method is used to compare one ``Type`` to another.

        return: (string) - the identifier of this ``Type``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    identifier = property(fget=get_identifier)


