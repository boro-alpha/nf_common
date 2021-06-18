from tkinter import Tk
from tkinter import filedialog

from nf_common_source.code.services.file_system_service.objects.files import Files


def select_file(
        title='Please select a file')\
    -> Files:
    root = \
        Tk()

    root.lift()

    file_path = \
        filedialog.askopenfile(
            parent=root,
            initialdir="/",
            title=title)

    root.withdraw()

    file = \
        Files(
            absolute_path_string=file_path.name)

    return \
        file
