import tkinter


class SelectFolderFrames(
        tkinter.Frame):
    def __init__(
            self,
            master,
            label_text,
            **kwargs):
        tkinter.Frame.__init__(
            self,
            master,
            **kwargs)

        self.text_box_label = \
            tkinter.Text(
                height=1, width=100)

        self.text_box_label.pack()

        self.text_box_label.insert(
            tkinter.END,
            label_text)

        self.text_box = \
            tkinter.Text(
                height=1, width=100)

        self.text_box.pack()

        # self.text_box.insert(tkinter.END, "Just a text Widget\nin two lines\n")


