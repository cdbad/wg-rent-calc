import tkinter as tk
from tkinter import ttk
from tools.room_name import label_name
from tools.btn_remove_room import remove_room
from tools.gridder import gridder


def add_room(frame: ttk.Frame):
    room_frame = ttk.Frame(frame)

    style = ttk.Style()
    style.configure(
        'Rm.TLabel',
        font = ('Helvetica', 10),
    )

    label_name(room_frame, parent_frame=frame)

    lbl_rm = ttk.Label(
        room_frame,
        text='Entfernen',
        style='Rm.TLabel',
        cursor='hand2'
    )
    lbl_rm.bind(
        '<Button-1>',
        lambda e: remove_room(room_frame)
    )
    lbl_rm.grid(row=0, column=1, sticky=tk.E)

    gridder(
        room_frame,
        [
            'Größe',
            'Mitbewohnis'
        ],
        1
    )

    room_frame.pack(padx=3, pady=(6, 0))
