import tkinter


class ScrollableFrames(
        tkinter.Frame):
    def __init__(
            self,
            master,
            **kwargs):
        tkinter.Frame.__init__(
            self,
            master,
            **kwargs)

        self.vertical_scrollbar = \
            tkinter.Scrollbar(
                self,
                orient=tkinter.VERTICAL)

        self.vertical_scrollbar.pack(
            side='right',
            fill='y',
            expand='false')

        self.canvas = \
            tkinter.Canvas(
                self,
                borderwidth=1,
                relief=tkinter.SUNKEN,
                height=350,
                highlightthickness=0,
                yscrollcommand=self.vertical_scrollbar.set)

        self.canvas.pack(
            side='left',
            fill='both',
            expand='true')

        self.vertical_scrollbar.config(
            command=self.canvas.yview)

        self.canvas.xview_moveto(
            0)

        self.canvas.yview_moveto(
            0)

        self.interior = \
            tkinter.Frame(
                self.canvas,
                **kwargs)

        self.canvas.create_window(
            0,
            0,
            window=self.interior,
            anchor="nw")

        self.bind(
            '<Configure>',
            self.set_scrollregion)

    def set_scrollregion(
            self,
            event=None):
        self.canvas.configure(
            scrollregion=self.canvas.bbox('all'))
