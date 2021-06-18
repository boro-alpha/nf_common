import tkinter

from nf_common_source.code.services.user_interaction_service.common_knowledge.window_return_types import \
    WindowReturnTypes
from nf_common_source.code.services.user_interaction_service.frames.select_folder_frames import SelectFolderFrames


class SelectTwoFoldersFrames:
    def __init__(
            self,
            title: str):
        self.title = \
            title

        self.window = \
            self.__create_window()

    selected_keys = {}

    button_clicked = \
        WindowReturnTypes.CANCEL

    def select_two_folders(
            self):
        self.__create_first_selection_frame(
            parent=self.window)

        tkinter.mainloop()

    def __create_window(
            self):
        window = \
            tkinter.Tk()

        window.title(
            self.title)

        return \
            window

    def __create_first_selection_frame(
            self,
            parent):
        self.select_folder_frame = \
            SelectFolderFrames(
                master=parent,
                label_text='Select root of files to be analsed',
                borderwidth=5)

        self.select_second_frame = \
            SelectFolderFrames(
                master=parent,
                label_text='Select results folder',
                borderwidth=5)

    @staticmethod
    def __create_button(
            parent,
            label: str,
            command: classmethod):
        button = \
            tkinter.Button(
                parent,
                text=label,
                command=command,
                width=10)

        button.pack(
            side=tkinter.RIGHT,
            padx=5,
            pady=5)
