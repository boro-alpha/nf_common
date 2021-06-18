from nf_common_source.code.services.file_system_service.objects.file_system_objects import FileSystemObjects


class Files(
        FileSystemObjects):

    def __init__(
            self,
            absolute_path_string: str,
            parent_folder: 'Folders' = None):
        super().__init__(
            absolute_path_string=absolute_path_string)

        self.__add_to_parent(
            parent_folder=parent_folder)

    def __add_to_parent(
            self,
            parent_folder: 'Folders'):
        if parent_folder is None:
            return

        self.parent_folder = \
            parent_folder

        parent_folder.add_to_child_files(
            self)
