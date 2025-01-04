import tkinter as tk
from tkinter import ttk


def Calculator(frame: ttk.Frame):
    frame_data = dict()

    # title frame
    frame_data['Name'] = frame\
                        .children['!frame']\
                        .children['!label']\
                        .cget('text')

    # main frame
    main_frame = frame\
                .children['!frame2']\
                .children\
                .values()
    main_frame_vals = [obj.cget('text')\
                       if type(obj) == ttk.Label\
                       else obj.get()\
                       for obj in main_frame]
    
    i = 0
    while i < len(main_frame_vals):
        frame_data[main_frame_vals[i]] = main_frame_vals[i + 1]
        i += 2

    # room frame
    room_frames = frame.children['!frame4'].children
    
    print(room_frames)
