import tkinter as tk
from tkinter import ttk

def label_name(
    frame,
    parent_frame: ttk.Frame = None,
    entry: ttk.Entry = None,
    name: str = None
):
    if entry:
        entry.destroy()
    
    if not name:
        current_room = len(parent_frame.children.keys())

        room_lbl = tk.Label(
            frame,
            text=f'Zimmer {current_room}',
            font=('Helvetica', 11)
        )
    else:
        room_lbl = tk.Label(
                frame,
                text=name,
                font=('Helvetica', 11)
            )
    
    room_lbl.bind(
        '<Double-Button-1>',
        lambda e: entry_name(frame, room_lbl)
    )
    room_lbl.grid(row=0, column=0, 
                  sticky=tk.W, pady=5)

def entry_name(frame, label: ttk.Label):
    label.destroy()

    new_name = ttk.Entry(frame)
    new_name.bind(
        '<Return>',
        lambda e: label_name(
            frame,
            name=new_name.get(),
            entry=new_name
        )
    )
    new_name.grid(row=0, column=0, 
                  sticky=tk.W, pady=5)