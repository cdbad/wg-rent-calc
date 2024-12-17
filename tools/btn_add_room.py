import tkinter as tk
from tkinter import ttk

from tools.gridder import gridder


def add_room(frame):
    room_frame = ttk.Frame(frame)

    gridder(room_frame, [
        'Zimmername',
        'Größe',
        'Mitbewohnis'
    ])

    btn_rm = ttk.Button(
        room_frame,
        text='Dieses Zimmer entfernen'
    )
    btn_rm.grid(column=0, row=3, columnspan=2, sticky=tk.W)

    room_frame.pack(padx=3, pady=5)
