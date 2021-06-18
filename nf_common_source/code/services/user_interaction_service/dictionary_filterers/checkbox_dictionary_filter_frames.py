import tkinter

from nf_common_source.code.services.user_interaction_service.common_knowledge.window_return_types import \
    WindowReturnTypes
from nf_common_source.code.services.user_interaction_service.dictionary_filterers.checkbox_dictionary_filter_responses import \
    CheckboxDictionaryFilterResponses
from nf_common_source.code.services.user_interaction_service.frames.scrollable_frames import \
    ScrollableFrames


class CheckboxDictionaryFilterFrames:
    def __init__(
            self,
            title: str,
            dictionary: dict):
        self.title = \
            title

        self.dictionary = \
            dictionary

        self.window = \
            self.__create_window()

    selected_keys = {}

    button_clicked = \
        WindowReturnTypes.CANCEL

    def check_filter(
            self):
        self.__create_checkbox_frame(
            parent=self.window)

        self.__create_control_buttons(
            parent=self.window)

        tkinter.mainloop()

    def get_response(
            self) \
            -> CheckboxDictionaryFilterResponses:
        checkbox_dictionary_filter_response = \
            CheckboxDictionaryFilterResponses()

        checkbox_dictionary_filter_response.button_clicked = \
            CheckboxDictionaryFilterFrames.button_clicked

        if CheckboxDictionaryFilterFrames.button_clicked is WindowReturnTypes.CANCEL:
            return \
                checkbox_dictionary_filter_response

        for item in self.dictionary.items():
            if CheckboxDictionaryFilterFrames.selected_keys[item[0]].get():
                checkbox_dictionary_filter_response.selected_items[item[0]] = item[1]

        return \
            checkbox_dictionary_filter_response

    def __create_window(
            self):
        window = \
            tkinter.Tk()

        window.title(
            self.title)

        return \
            window

    def __create_checkbox_frame(
            self,
            parent):
        filter_frame = \
            ScrollableFrames(
                parent,
                borderwidth=5)

        filter_frame.pack(
            expand="true",
            fill="both")

        for item in self.dictionary.items():
            CheckboxDictionaryFilterFrames.__create_check_button(
                parent=filter_frame,
                item=item)

    @staticmethod
    def __create_check_button(
            parent,
            item: tuple):
        is_selected = \
            tkinter.BooleanVar()

        check_button = \
            tkinter.Checkbutton(
                parent.interior,
                text=item[1],
                variable=is_selected)

        check_button.grid(
            sticky=tkinter.W)

        CheckboxDictionaryFilterFrames.selected_keys[item[0]] = \
            is_selected

    def __create_control_buttons(
            self,
            parent):
        self.__create_button(
            parent,
            label='Cancel',
            command=self.__cancel_clicked)

        self.__create_button(
            parent,
            label='OK',
            command=self.__ok_clicked)

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

    def __cancel_clicked(
            self):
        CheckboxDictionaryFilterFrames.button_clicked = \
            WindowReturnTypes.CANCEL

        self.window.destroy()

    def __ok_clicked(
            self):
        CheckboxDictionaryFilterFrames.button_clicked = \
            WindowReturnTypes.OK

        self.window.destroy()
