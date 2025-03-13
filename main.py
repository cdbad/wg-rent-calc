import tkinter as tk
from tkinter import ttk
from ui.btn_add_room import add_room
from ui.gridder import gridder
from ui.scrollbar_setup import scrollbar_setup
from ui.labels import label_name
from tools.calculator import Calculator

class UI(Calculator):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('WG Rent Calculator')
        self.root.geometry('400x400')
        self.root.minsize(400, 200)
        self.root.maxsize(400, 1000)

        self.scrollbar_frame = scrollbar_setup(self.root)

        # TITLE FRAME ####################################
        title_frame = ttk.Frame(self.scrollbar_frame)

        label_name(
            title_frame,
            name='My WG',
            parent_frame=title_frame,
        )

        title_frame.pack()
        ##################################################

        # MAIN FRAME #####################################
        main_frame = ttk.Frame(self.scrollbar_frame)

        gridder(main_frame,
            {
                'Kaltmiete': '1200',
                'Größe': '112',
                'Heizung': '1.2',
                'Nebenkosten': '20',
                'Extra': '10'
            },
            1
        )

        main_frame.pack(padx=5, pady=5, fill=tk.X, expand=True)
        ##################################################

        # MIDDLE FRAME ###################################
        middle_frame = ttk.Frame(self.scrollbar_frame, width=400)

        ttk.Label(
            middle_frame,
            text='Zimmer',
            width=41,
            font=('Helvetica', 10, 'bold')
        ).pack(side=tk.LEFT)

        ttk.Button(
            middle_frame,
            text='+',
            command=lambda: add_room(room_frame),
            width=4
        ).pack(side=tk.RIGHT)

        middle_frame.pack(pady=(7.5, 0))
        ##################################################

        # ROOM FRAME #####################################
        room_frame = ttk.Frame(self.scrollbar_frame, width=450)

        add_room(room_frame)

        room_frame.pack()
        ##################################################

        self.error_lbl = ttk.Label(
            self.scrollbar_frame,
            text='',
            foreground='red'
        )
        self.error_lbl.pack()

        ttk.Button(
            self.scrollbar_frame,
            text='Calculate',
            command=lambda: self.send_data(
                self.scrollbar_frame,
                self.error_lbl
            )
        ).pack(pady=(10, 20))

        self.root.mainloop()

if __name__ == '__main__':
    UI()
