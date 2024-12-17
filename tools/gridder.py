import tkinter as tk
from tkinter import ttk


def gridder(frame, names: list):
    for arg in names:
        lbl = ttk.Label(frame, text=arg, width=18)
        lbl.grid(column=0, row=names.index(arg), sticky=tk.W)

        entry = ttk.Entry(frame)
        entry.grid(column=1, row=names.index(arg))
