from tkinter import Tk
from tkinter import filedialog

from nf_common_source.code.services.file_system_service.objects.folders import Folders


def select_folder(
        title='Please select a directory')\
    -> Folders:
    root = \
        Tk()

    root.lift()

    file_path = \
        filedialog.askdirectory(
            parent=root,
            initialdir="/",
            title=title)

    root.withdraw()

    folder = \
        Folders(
            absolute_path_string=file_path)

    return \
        folder
