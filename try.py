from tkinter import *

root = Tk()
base_frame = Frame(root)

base_canvas = Canvas(base_frame,background="blue", height = 500,width =500)
base_canvas.configure(scrollregion=base_canvas.bbox("all"))

scroll = Scrollbar(base_frame ,orient="vertical", command=base_canvas.yview)
base_canvas.configure(yscrollcommand=scroll.set)

scroll.pack(side="right", fill="y")
base_canvas.pack(side = BOTTOM, anchor = NW,fill="x")
base_frame.pack(anchor = W, fill = "x")

base_canvas.create_line(0, 0, 500, 1000)
base_canvas.configure(scrollregion=base_canvas.bbox("all"))

root.mainloop()