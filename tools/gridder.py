import tkinter as tk
from tkinter import ttk


def on_focus(entry: ttk.Entry):
    if entry['foreground'].__str__() == 'grey':
        # placeholders[entry.winfo_id()] = names['']
        entry.delete(0, 'end')
        entry['foreground'] = 'black'

def on_unfocus(entry: ttk.Entry, placeholders: dict):
    if not entry.get() or entry.get() == '':
        entry['foreground'] = 'grey'
        entry.insert(0, placeholders[entry.winfo_id()])

def gridder(frame: ttk.Frame, names: dict, starting_row: int = 0):
    placeholders = dict()

    for arg in names.keys():
        lbl = ttk.Label(
            frame,
            text=arg,
            width=21,
            font=("Helvetica", 11)
        )
        lbl.grid(column=0, row=starting_row, sticky=tk.W)

        entry = ttk.Entry(frame)
        placeholders[entry.winfo_id()] = names[arg]
        entry.insert(0, names[arg])
        entry['foreground'] = 'grey'
        entry.bind(
            '<FocusIn>',
            lambda e, entry=entry: on_focus(entry)
        )
        entry.bind(
            '<FocusOut>',
            lambda e, entry=entry: on_unfocus(entry, placeholders)
        )
        entry.grid(row=starting_row, column=1)

        starting_row += 1
