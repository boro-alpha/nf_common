import os
from nf_common_source.code.services.file_system_service.objects.files import Files
from nf_common_source.code.services.file_system_service.objects.folders import Folders


def get_all_files_of_extension_from_folder(
        folder: Folders,
        dot_extension_string: str) \
        -> list:
    list_of_files_of_extension = \
        list()

    for file_name in os.listdir(folder.absolute_path_string):
        list_of_files_of_extension = \
            __add_file_of_specific_extension(
                file_name=file_name,
                dot_extension_string=dot_extension_string,
                list_of_files_of_extension=list_of_files_of_extension,
                folder=folder)

    return \
        list_of_files_of_extension


def __add_file_of_specific_extension(
        file_name: str,
        dot_extension_string: str,
        list_of_files_of_extension: list,
        folder: Folders) \
        -> list:
    if not file_name.endswith(dot_extension_string):
        return list_of_files_of_extension

    file_absolute_path_string = \
        os.path.join(
            folder.absolute_path_string,
            file_name)

    file = \
        Files(
            absolute_path_string=file_absolute_path_string)

    list_of_files_of_extension.append(
        file)

    return \
        list_of_files_of_extension
