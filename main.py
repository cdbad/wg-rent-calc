import tkinter as tk
from tkinter import ttk

from tools.btn_add_room import add_room
from tools.gridder import gridder
from tools.scrollbar_setup import scrollbar_setup


root = tk.Tk()
root.title('WG Rent Calculator')
root.geometry('400x400')
root.minsize(400, 200)
root.maxsize(400, 1000)

scrollbar_frame = scrollbar_setup(root)

# MAIN FRAME #####################################
main_frame = ttk.Frame(scrollbar_frame)

gridder(main_frame,
        [
            'Name der WG',
            'Größe',
            'Heizung',
            'Nebenkosten',
            'Extra'
        ])

main_frame.pack(padx=5, pady=5, fill=tk.X, expand=True)
##################################################

# MIDDLE FRAME ###################################
middle_frame = ttk.Frame(scrollbar_frame, width=400)

title = ttk.Label(
    middle_frame,
    text='Zimmer',
    width=33
).pack(side=tk.LEFT)

btn_add = ttk.Button(
    middle_frame,
    text='+',
    command=lambda: add_room(scrollbar_frame),
    width=4
).pack(side=tk.RIGHT)

middle_frame.pack()
##################################################

add_room(scrollbar_frame)

btn_calc = ttk.Button(
    scrollbar_frame,
    text='Calculate',
    command=lambda: print('Calculate')
).pack()

root.mainloop()
