import tkinter as tk
from tkinter import ttk

def label_name(
    frame,
    parent_frame: ttk.Frame = None,
    entry: ttk.Entry = None,
    name: str = None,
    font: tuple = ('Helvetica', 11)
):
    if entry:
        name = entry.get()
        entry.destroy()
    
    if not name:
        current_room = len(parent_frame.children.keys())

        room_lbl = tk.Label(
            frame,
            text=f'Zimmer {current_room}',
            font=font
        )
    else:
        room_lbl = tk.Label(
                frame,
                text=name,
                font=font
            )
    
    room_lbl.bind(
        '<Double-Button-1>',
        lambda e: entry_name(frame, parent_frame, room_lbl)
    )
    room_lbl.grid(row=0, column=0, 
                  sticky=tk.W, pady=5)

def entry_name(frame, parent_frame, label: ttk.Label):
    label.destroy()

    new_name = ttk.Entry(frame)
    new_name.focus_set()

    new_name.bind(
        '<Return>',
        lambda e: label_name(
            frame,
            parent_frame=parent_frame,
            entry=new_name
        )
    )
    new_name.grid(row=0, column=0, 
                  sticky=tk.W, pady=5)