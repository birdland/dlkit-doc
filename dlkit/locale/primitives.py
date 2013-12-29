from ..osid import markers as osid_markers


class DisplayText(osid_markers.OsidPrimitive):
    """Text to be displayed."""
    def get_language_type(self):
        """Gets the language ``Type``.

        :return: the language type
        :rtype: ``osid.type.Type``

        """
        return # osid.type.Type

    language_type = property(fget=get_language_type)

    def get_script_type(self):
        """Gets the script ``Type``.

        :return: the script type
        :rtype: ``osid.type.Type``

        """
        return # osid.type.Type

    script_type = property(fget=get_script_type)

    def get_format_type(self):
        """Gets the format ``Type`` of the text string.

        :return: the format type
        :rtype: ``osid.type.Type``

        """
        return # osid.type.Type

    format_type = property(fget=get_format_type)

    def get_text(self):
        """Gets the text string.

        :return: the string
        :rtype: ``string``

        """
        return # string

    text = property(fget=get_text)


