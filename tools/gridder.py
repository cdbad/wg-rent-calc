import tkinter as tk
from tkinter import ttk


def gridder(frame, names: list, starting_row: int = 0):
    for arg in names:
        lbl = ttk.Label(
            frame,
            text=arg,
            width=21,
            font=("Helvetica", 11)
        )
        lbl.grid(column=0, row=starting_row, sticky=tk.W)

        entry = ttk.Entry(frame)
        entry.grid(column=1, row=starting_row)

        starting_row += 1
