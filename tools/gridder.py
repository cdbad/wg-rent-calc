import tkinter as tk
from tkinter import ttk

def on_focus(entry: ttk.Entry):
    if entry['foreground'].__str__() == 'grey':
        entry.delete(0, 'end')
        entry['foreground'] = 'black'

def on_unfocus(entry: ttk.Entry, default_placeholder: str):
    print(entry.get())
    if not entry.get() or entry.get() == '':
        entry['foreground'] = 'grey'
        entry.insert(0, default_placeholder)

def gridder(frame, names: dict, starting_row: int = 0):
    for arg in names.keys():
        lbl = ttk.Label(
            frame,
            text=arg,
            width=21,
            font=("Helvetica", 11)
        )
        lbl.grid(column=0, row=starting_row, sticky=tk.W)

        entry = ttk.Entry(frame)
        entry.insert(0, names[arg])
        entry['foreground'] = 'grey'
        entry.bind(
            '<FocusIn>',
            lambda e, entry=entry: on_focus(entry)
        )
        entry.bind(
            '<FocusOut>',
            lambda e, entry=entry: on_unfocus(entry, names[arg])
        )
        entry.grid(row=starting_row, column=1)

        starting_row += 1
