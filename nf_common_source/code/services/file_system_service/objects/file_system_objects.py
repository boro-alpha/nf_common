from nf_common_source.code.services.file_system_service.objects.wrappers.absolute_path_wrappers import \
    AbsolutePathWrappers
from nf_common_source.code.services.identification_services.uuid_service.uuid_helpers.uuid_factory import create_new_uuid


class FileSystemObjects:

    def __init__(
            self,
            absolute_path_string: str):
        self.uuid = \
            create_new_uuid()

        self.__path = \
            AbsolutePathWrappers(
                absolute_path_string)

    @property
    def base_name(
            self) \
            -> str:
        return \
            self.__path.base_name

    @property
    def absolute_path_string(
            self) \
            -> str:
        return \
            self.__path.absolute_path_string

    @property
    def absolute_level(
            self) \
            -> int:
        return \
            self.__path.absolute_level

    @property
    def parent_absolute_path_string(
            self) \
            -> str:
        return \
            str(self.__path.parent)

    def extend_path(
            self,
            path_extension: str) \
            -> str:
        return \
            self.__path.extend_path(
                path_extension)

    def exists(
            self) \
            -> bool:
        return \
            self.__path.exists()

    def list_of_components(self):
        return \
            self.__path.list_of_components()

    def item_count(
            self) \
            -> int:
        return \
            self.__path.item_count()
