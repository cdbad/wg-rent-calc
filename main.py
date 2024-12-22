import tkinter as tk
from tkinter import ttk
from tools.btn_add_room import add_room
from tools.gridder import gridder
from tools.scrollbar_setup import scrollbar_setup
from tools.room_name import label_name

root = tk.Tk()
root.title('WG Rent Calculator')
root.geometry('400x400')
root.minsize(400, 200)
root.maxsize(400, 1000)

scrollbar_frame = scrollbar_setup(root)

# TITLE FRAME ####################################
title_frame = ttk.Frame(scrollbar_frame)

label_name(title_frame, title_frame, name='My WG')

title_frame.pack()
##################################################

# MAIN FRAME #####################################
main_frame = ttk.Frame(scrollbar_frame)

gridder(main_frame,
    [
        # 'Name der WG',
        'Kaltmiete',
        'Größe',
        'Heizung',
        'Nebenkosten',
        'Extra'
    ],
    1
)

main_frame.pack(padx=5, pady=5, fill=tk.X, expand=True)
##################################################

# MIDDLE FRAME ###################################
middle_frame = ttk.Frame(scrollbar_frame, width=400)

title = ttk.Label(
    middle_frame,
    text='Zimmer',
    width=41,
    font=('Helvetica', 10, 'bold')
).pack(side=tk.LEFT)

btn_add = ttk.Button(
    middle_frame,
    text='+',
    command=lambda: add_room(room_frame),
    width=4
).pack(side=tk.RIGHT)

middle_frame.pack(pady=(7.5, 0))
##################################################

# ROOM FRAME #####################################
room_frame = ttk.Frame(scrollbar_frame, width=450)

add_room(room_frame)

room_frame.pack()
##################################################

btn_calc = ttk.Button(
    scrollbar_frame,
    text='Calculate',
    command=lambda: print('Calculate')
).pack(pady=(10, 20))

root.mainloop()
