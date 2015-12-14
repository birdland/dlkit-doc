


class OsidRecord:
    """``OsidRecord`` is a top-level interface for all record objects.


    A record is an auxiliary interface that can be retrieved from an
    OSID object, query, form or search order that contains method
    definitions outside the core OSID specification. An OSID record
    interface specification is identified with a ``Type``.


    """

    def implements_record_type(self, record_type):
        """Tests if the given type is implemented by this record.


        Other types than that directly indicated by ``get_type()`` may
        be supported through an inheritance scheme where the given type
        specifies a record that is a parent interface of the interface
        specified by ``getType()``.


        :param record_type: a type
        :type record_type: ``osid.type.Type``
        :return: ``true`` if the given record ``Type`` is implemented by this record, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``record_type`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean


