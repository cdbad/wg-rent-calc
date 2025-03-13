import tkinter as tk
from tkinter import ttk


def scrollbar_setup(root):
    # main frame
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    # canvas
    canvas = tk.Canvas(main_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    # scrollbar to canvas
    scrollbar = ttk.Scrollbar(
        main_frame,
        orient=tk.VERTICAL,
        command=canvas.yview
    )
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # config canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind(
        '<Configure>',
        lambda e: canvas.configure(scrollregion=canvas.bbox('all'))
    )

    # frame inside canvas
    second_frame = tk.Frame(canvas)

    # add frame to window in canvas
    canvas.create_window((0, 0), window=second_frame, anchor=tk.NW)

    return second_frame
