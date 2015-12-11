
from ..osid import objects as osid_objects


class TypeForm(osid_objects.OsidForm):
    """This form provides a means of updating various fields in the ``Type``.

    Note that the domain, authority and identifier are part of the
    ``Type`` identification, and as such not modifiable.

    """
    



    def get_display_name_metadata(self):
        """Gets the metadata for the display name.

        return: (osid.Metadata) - metadata for the display name
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    display_name_metadata = property(fget=get_display_name_metadata)


    def set_display_name(self, display_name):
        """Sets a display name.

        arg:    display_name (string): the new display name
        raise:  InvalidArgument - ``display_name`` is invalid
        raise:  NoAccess - ``display_name`` cannot be modified
        raise:  NullArgument - ``display_name`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_display_name(self):
        """Clears the display name.

        raise:  NoAccess - ``display_name`` cannot be modified
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    display_name = property(fset=set_display_name, fdel=clear_display_name)


    def get_display_label_metadata(self):
        """Gets the metadata for the display label.

        return: (osid.Metadata) - metadata for the display label
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    display_label_metadata = property(fget=get_display_label_metadata)


    def set_display_label(self, display_label):
        """Seta a display label.

        arg:    display_label (string): the new display label
        raise:  InvalidArgument - ``display_label`` is invalid
        raise:  NoAccess - ``display_label`` cannot be modified
        raise:  NullArgument - ``display_label`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_display_label(self):
        """Clears the display label.

        raise:  NoAccess - ``display_label`` cannot be modified
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    display_label = property(fset=set_display_label, fdel=clear_display_label)


    def get_description_metadata(self):
        """Gets the metadata for the description.

        return: (osid.Metadata) - metadata for the description
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    description_metadata = property(fget=get_description_metadata)


    def set_description(self, description):
        """Sets a description.

        arg:    description (string): the new description
        raise:  InvalidArgument - ``description`` is invalid
        raise:  NoAccess - ``description`` cannot be modified
        raise:  NullArgument - ``description`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_description(self):
        """Clears the description.

        raise:  NoAccess - ``description`` cannot be modified
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    description = property(fset=set_description, fdel=clear_description)


    def get_domain_metadata(self):
        """Gets the metadata for the domain.

        return: (osid.Metadata) - metadata for the domain
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    domain_metadata = property(fget=get_domain_metadata)


    def set_domain(self, domain):
        """Sets a domain.

        arg:    domain (string): the new domain
        raise:  InvalidArgument - ``domain`` is invalid
        raise:  NoAccess - ``domain`` cannot be modified
        raise:  NullArgument - ``domain`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_domain(self):
        """Clears the domain.

        raise:  NoAccess - ``domain`` cannot be modified
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    domain = property(fset=set_domain, fdel=clear_domain)


class TypeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``TypeList`` provides a means for accessing ``Type`` elements sequentially either one at a time
        or many at a time.

    Examples: while (tl.hasNext()) { Type type = tl.getNextType(); }

    or
      while (tl.hasNext()) {
           Type[] types = tl.getNextTypes(tl.available());
      }


    """
    



    def get_next_type(self):
        """Gets the next ``Type`` in this list.

        return: (osid.type.Type) - the next ``Type`` in this list. The
                ``has_next()`` method should be used to test that a next
                ``Type`` is available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type

    next_type = property(fget=get_next_type)


    def get_next_types(self, n):
        """Gets the next set of ``Types`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``Type`` elements requested
                which must be less than or equal to ``available()``
        return: (osid.type.Type) - an array of ``Type`` elements.The
                length of the array is less than or equal to the number
                specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.Type


