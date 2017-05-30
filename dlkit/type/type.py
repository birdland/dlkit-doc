
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions
from ..osid import markers as osid_markers
from ..osid import objects as osid_objects


class TypeProfile(osid_managers.OsidProfile):
    """The ``TypeProfile`` describes the interoperability among type services."""


##
# The following methods are from osid.type.TypeProfile




##
# The following methods are from osid.type.TypeManager




##
# The following methods are from osid.type.TypeProxyManager




##
# The following methods are from osid.type.Type

    def get_display_name(self):
        """Gets the full display name of this ``Type``.

        :return: the display name of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    display_name = property(fget=get_display_name)

    def get_display_label(self):
        """Gets the shorter display label for this ``Type``.

        Where a display name of a ``Type`` might be ``"`` Critical
        Logging Priority Type", the display label could be "critical".

        :return: the display label for this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    display_label = property(fget=get_display_label)

    def get_description(self):
        """Gets a description of this ``Type``.

        :return: the description of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    description = property(fget=get_description)

    def get_domain(self):
        """Gets the domain.

        The domain can provide an information label about ths
        application space of this Type.

        :return: the domain of this ``Type``
        :rtype: ``osid.locale.DisplayText``


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

        :return: the authority of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    authority = property(fget=get_authority)

    def get_identifier_namespace(self):
        """Gets the namespace of the identifier.

        This method is used to compare one ``Type`` to another.

        :return: the authority of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    identifier_namespace = property(fget=get_identifier_namespace)

    namespace = property(fget=get_identifier_namespace)

    def get_identifier(self):
        """Gets the identifier of this ``Type``.

        This method is used to compare one ``Type`` to another.

        :return: the identifier of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    identifier = property(fget=get_identifier)


##
# The following methods are from osid.type.TypeForm

    def get_display_name_metadata(self):
        """Gets the metadata for the display name.

        :return: metadata for the display name
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    display_name_metadata = property(fget=get_display_name_metadata)

    def set_display_name(self, display_name):
        """Sets a display name.

        :param display_name: the new display name
        :type display_name: ``string``
        :raise: ``InvalidArgument`` -- ``display_name`` is invalid
        :raise: ``NoAccess`` -- ``display_name`` cannot be modified
        :raise: ``NullArgument`` -- ``display_name`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_display_name(self):
        """Clears the display name.

        :raise: ``NoAccess`` -- ``display_name`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    display_name = property(fset=set_display_name, fdel=clear_display_name)

    def get_display_label_metadata(self):
        """Gets the metadata for the display label.

        :return: metadata for the display label
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    display_label_metadata = property(fget=get_display_label_metadata)

    def set_display_label(self, display_label):
        """Seta a display label.

        :param display_label: the new display label
        :type display_label: ``string``
        :raise: ``InvalidArgument`` -- ``display_label`` is invalid
        :raise: ``NoAccess`` -- ``display_label`` cannot be modified
        :raise: ``NullArgument`` -- ``display_label`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_display_label(self):
        """Clears the display label.

        :raise: ``NoAccess`` -- ``display_label`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    display_label = property(fset=set_display_label, fdel=clear_display_label)

    def get_description_metadata(self):
        """Gets the metadata for the description.

        :return: metadata for the description
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    description_metadata = property(fget=get_description_metadata)

    def set_description(self, description):
        """Sets a description.

        :param description: the new description
        :type description: ``string``
        :raise: ``InvalidArgument`` -- ``description`` is invalid
        :raise: ``NoAccess`` -- ``description`` cannot be modified
        :raise: ``NullArgument`` -- ``description`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_description(self):
        """Clears the description.

        :raise: ``NoAccess`` -- ``description`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    description = property(fset=set_description, fdel=clear_description)

    def get_domain_metadata(self):
        """Gets the metadata for the domain.

        :return: metadata for the domain
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    domain_metadata = property(fget=get_domain_metadata)

    def set_domain(self, domain):
        """Sets a domain.

        :param domain: the new domain
        :type domain: ``string``
        :raise: ``InvalidArgument`` -- ``domain`` is invalid
        :raise: ``NoAccess`` -- ``domain`` cannot be modified
        :raise: ``NullArgument`` -- ``domain`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_domain(self):
        """Clears the domain.

        :raise: ``NoAccess`` -- ``domain`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    domain = property(fset=set_domain, fdel=clear_domain)


##
# The following methods are from osid.type.TypeList

    def get_next_type(self):
        """Gets the next ``Type`` in this list.

        :return: the next ``Type`` in this list. The ``has_next()`` method should be used to test that a next ``Type`` is available before calling this method.
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    next_type = property(fget=get_next_type)

    def get_next_types(self, n):
        """Gets the next set of ``Types`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Type`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Type`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type




class TypeManager(osid_managers.OsidManager, osid_sessions.OsidSession, TypeProfile):
    """This manager provides access to the available sessions of the type service.

    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.

    """


##
# The following methods are from osid.type.TypeProfile




##
# The following methods are from osid.type.TypeManager




##
# The following methods are from osid.type.TypeProxyManager




##
# The following methods are from osid.type.Type

    def get_display_name(self):
        """Gets the full display name of this ``Type``.

        :return: the display name of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    display_name = property(fget=get_display_name)

    def get_display_label(self):
        """Gets the shorter display label for this ``Type``.

        Where a display name of a ``Type`` might be ``"`` Critical
        Logging Priority Type", the display label could be "critical".

        :return: the display label for this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    display_label = property(fget=get_display_label)

    def get_description(self):
        """Gets a description of this ``Type``.

        :return: the description of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    description = property(fget=get_description)

    def get_domain(self):
        """Gets the domain.

        The domain can provide an information label about ths
        application space of this Type.

        :return: the domain of this ``Type``
        :rtype: ``osid.locale.DisplayText``


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

        :return: the authority of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    authority = property(fget=get_authority)

    def get_identifier_namespace(self):
        """Gets the namespace of the identifier.

        This method is used to compare one ``Type`` to another.

        :return: the authority of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    identifier_namespace = property(fget=get_identifier_namespace)

    namespace = property(fget=get_identifier_namespace)

    def get_identifier(self):
        """Gets the identifier of this ``Type``.

        This method is used to compare one ``Type`` to another.

        :return: the identifier of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    identifier = property(fget=get_identifier)


##
# The following methods are from osid.type.TypeForm

    def get_display_name_metadata(self):
        """Gets the metadata for the display name.

        :return: metadata for the display name
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    display_name_metadata = property(fget=get_display_name_metadata)

    def set_display_name(self, display_name):
        """Sets a display name.

        :param display_name: the new display name
        :type display_name: ``string``
        :raise: ``InvalidArgument`` -- ``display_name`` is invalid
        :raise: ``NoAccess`` -- ``display_name`` cannot be modified
        :raise: ``NullArgument`` -- ``display_name`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_display_name(self):
        """Clears the display name.

        :raise: ``NoAccess`` -- ``display_name`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    display_name = property(fset=set_display_name, fdel=clear_display_name)

    def get_display_label_metadata(self):
        """Gets the metadata for the display label.

        :return: metadata for the display label
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    display_label_metadata = property(fget=get_display_label_metadata)

    def set_display_label(self, display_label):
        """Seta a display label.

        :param display_label: the new display label
        :type display_label: ``string``
        :raise: ``InvalidArgument`` -- ``display_label`` is invalid
        :raise: ``NoAccess`` -- ``display_label`` cannot be modified
        :raise: ``NullArgument`` -- ``display_label`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_display_label(self):
        """Clears the display label.

        :raise: ``NoAccess`` -- ``display_label`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    display_label = property(fset=set_display_label, fdel=clear_display_label)

    def get_description_metadata(self):
        """Gets the metadata for the description.

        :return: metadata for the description
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    description_metadata = property(fget=get_description_metadata)

    def set_description(self, description):
        """Sets a description.

        :param description: the new description
        :type description: ``string``
        :raise: ``InvalidArgument`` -- ``description`` is invalid
        :raise: ``NoAccess`` -- ``description`` cannot be modified
        :raise: ``NullArgument`` -- ``description`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_description(self):
        """Clears the description.

        :raise: ``NoAccess`` -- ``description`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    description = property(fset=set_description, fdel=clear_description)

    def get_domain_metadata(self):
        """Gets the metadata for the domain.

        :return: metadata for the domain
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    domain_metadata = property(fget=get_domain_metadata)

    def set_domain(self, domain):
        """Sets a domain.

        :param domain: the new domain
        :type domain: ``string``
        :raise: ``InvalidArgument`` -- ``domain`` is invalid
        :raise: ``NoAccess`` -- ``domain`` cannot be modified
        :raise: ``NullArgument`` -- ``domain`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_domain(self):
        """Clears the domain.

        :raise: ``NoAccess`` -- ``domain`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    domain = property(fset=set_domain, fdel=clear_domain)


##
# The following methods are from osid.type.TypeList

    def get_next_type(self):
        """Gets the next ``Type`` in this list.

        :return: the next ``Type`` in this list. The ``has_next()`` method should be used to test that a next ``Type`` is available before calling this method.
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    next_type = property(fget=get_next_type)

    def get_next_types(self, n):
        """Gets the next set of ``Types`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Type`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Type`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type




class TypeProxyManager(osid_managers.OsidProxyManager, TypeProfile):
    """This manager provides access to the available sessions of the type service.

    Methods in this manager support the passing of a ``Proxy`` object
    for the purpose of passing information from a server environment.
    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.

    """


##
# The following methods are from osid.type.TypeProfile




##
# The following methods are from osid.type.TypeManager




##
# The following methods are from osid.type.TypeProxyManager




##
# The following methods are from osid.type.Type

    def get_display_name(self):
        """Gets the full display name of this ``Type``.

        :return: the display name of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    display_name = property(fget=get_display_name)

    def get_display_label(self):
        """Gets the shorter display label for this ``Type``.

        Where a display name of a ``Type`` might be ``"`` Critical
        Logging Priority Type", the display label could be "critical".

        :return: the display label for this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    display_label = property(fget=get_display_label)

    def get_description(self):
        """Gets a description of this ``Type``.

        :return: the description of this ``Type``
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.DisplayText

    description = property(fget=get_description)

    def get_domain(self):
        """Gets the domain.

        The domain can provide an information label about ths
        application space of this Type.

        :return: the domain of this ``Type``
        :rtype: ``osid.locale.DisplayText``


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

        :return: the authority of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    authority = property(fget=get_authority)

    def get_identifier_namespace(self):
        """Gets the namespace of the identifier.

        This method is used to compare one ``Type`` to another.

        :return: the authority of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    identifier_namespace = property(fget=get_identifier_namespace)

    namespace = property(fget=get_identifier_namespace)

    def get_identifier(self):
        """Gets the identifier of this ``Type``.

        This method is used to compare one ``Type`` to another.

        :return: the identifier of this ``Type``
        :rtype: ``string``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # string

    identifier = property(fget=get_identifier)


##
# The following methods are from osid.type.TypeForm

    def get_display_name_metadata(self):
        """Gets the metadata for the display name.

        :return: metadata for the display name
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    display_name_metadata = property(fget=get_display_name_metadata)

    def set_display_name(self, display_name):
        """Sets a display name.

        :param display_name: the new display name
        :type display_name: ``string``
        :raise: ``InvalidArgument`` -- ``display_name`` is invalid
        :raise: ``NoAccess`` -- ``display_name`` cannot be modified
        :raise: ``NullArgument`` -- ``display_name`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_display_name(self):
        """Clears the display name.

        :raise: ``NoAccess`` -- ``display_name`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    display_name = property(fset=set_display_name, fdel=clear_display_name)

    def get_display_label_metadata(self):
        """Gets the metadata for the display label.

        :return: metadata for the display label
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    display_label_metadata = property(fget=get_display_label_metadata)

    def set_display_label(self, display_label):
        """Seta a display label.

        :param display_label: the new display label
        :type display_label: ``string``
        :raise: ``InvalidArgument`` -- ``display_label`` is invalid
        :raise: ``NoAccess`` -- ``display_label`` cannot be modified
        :raise: ``NullArgument`` -- ``display_label`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_display_label(self):
        """Clears the display label.

        :raise: ``NoAccess`` -- ``display_label`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    display_label = property(fset=set_display_label, fdel=clear_display_label)

    def get_description_metadata(self):
        """Gets the metadata for the description.

        :return: metadata for the description
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    description_metadata = property(fget=get_description_metadata)

    def set_description(self, description):
        """Sets a description.

        :param description: the new description
        :type description: ``string``
        :raise: ``InvalidArgument`` -- ``description`` is invalid
        :raise: ``NoAccess`` -- ``description`` cannot be modified
        :raise: ``NullArgument`` -- ``description`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_description(self):
        """Clears the description.

        :raise: ``NoAccess`` -- ``description`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    description = property(fset=set_description, fdel=clear_description)

    def get_domain_metadata(self):
        """Gets the metadata for the domain.

        :return: metadata for the domain
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    domain_metadata = property(fget=get_domain_metadata)

    def set_domain(self, domain):
        """Sets a domain.

        :param domain: the new domain
        :type domain: ``string``
        :raise: ``InvalidArgument`` -- ``domain`` is invalid
        :raise: ``NoAccess`` -- ``domain`` cannot be modified
        :raise: ``NullArgument`` -- ``domain`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_domain(self):
        """Clears the domain.

        :raise: ``NoAccess`` -- ``domain`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    domain = property(fset=set_domain, fdel=clear_domain)


##
# The following methods are from osid.type.TypeList

    def get_next_type(self):
        """Gets the next ``Type`` in this list.

        :return: the next ``Type`` in this list. The ``has_next()`` method should be used to test that a next ``Type`` is available before calling this method.
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    next_type = property(fget=get_next_type)

    def get_next_types(self, n):
        """Gets the next set of ``Types`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Type`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Type`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type




