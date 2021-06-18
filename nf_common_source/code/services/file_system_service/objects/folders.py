from nf_common_source.code.services.file_system_service.objects.file_system_objects import FileSystemObjects
from nf_common_source.code.services.file_system_service.objects.files import Files


class Folders(
        FileSystemObjects):

    def __init__(
            self,
            absolute_path_string: str,
            parent_folder: 'Folders' = None):
        super().__init__(
            absolute_path_string=absolute_path_string)

        self.parent_folder = \
            parent_folder

        self.child_folders = \
            []

        self.child_files = \
            []

        self.__add_to_parent(
            parent_folder=parent_folder)

    def add_to_child_folders(
            self,
            child_file_system_object: 'Folders'):
        self.child_folders.append(
            child_file_system_object)

    def add_to_child_files(
            self,
            child_file_system_object: Files):
        self.child_files.append(
            child_file_system_object)

    def __add_to_parent(
            self,
            parent_folder: 'Folders'):
        if parent_folder is None:
            return

        parent_folder.add_to_child_folders(
            self)
