from ..osid import receivers as osid_receivers


class FileReceiver(osid_receivers.OsidReceiver):
    """The file receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted files."""
    def new_file(self, file_path):
        """The callback for notifications of new files.

        :param file_path: absolute pathname to the new file
        :type file_path: ``string``

        """
        pass

    def changed_file(self, file_path):
        """The callback for notification of updated files.

        :param file_path: absolute pathname to the changed file
        :type file_path: ``string``

        """
        pass

    def deleted_file(self, file_path):
        """the callback for notification of deleted files.

        :param file_path: absolute pathname to the deleted file
        :type file_path: ``string``

        """
        pass


class DirectoryReceiver(osid_receivers.OsidReceiver):
    """The directory receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted directories."""
    def new_directory(self, directory_path):
        """The callback for notifications of new directories.

        :param directory_path: absolute pathname to the new directory
        :type directory_path: ``string``

        """
        pass

    def changed_directory(self, directory_path):
        """The callback for notification of updated directories.

        :param directory_path: absolute pathname to the changed directory
        :type directory_path: ``string``

        """
        pass

    def deleted_directory(self, directory_path):
        """the callback for notification of deleted directories.

        :param directory_path: absolute pathname to the deleted directory
        :type directory_path: ``string``

        """
        pass


