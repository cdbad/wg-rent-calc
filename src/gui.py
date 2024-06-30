import tkinter as tk
# from tkinter import ttk
from datetime import datetime
import os
from os.path import exists

class GUI:
    '''GUI for the homepage'''

    rooms = dict()

    def __init__(self):
        # WINDOW
        self.root = tk.Tk()
        self.root.title('WG Kosten')
        self.root.geometry('400x500')
        self.root.minsize(400, 500)

        self.base_canvas = tk.Canvas(
                            self.root,
                            height=self.root.winfo_height(),
                            width=self.root.winfo_width()
                            )
        self.base_canvas.configure(
                        scrollregion=self.base_canvas.bbox('all')
                        )

        # scrollbar
        self.scrollbar = tk.Scrollbar(
                            self.root,
                            orient='vertical',
                            command=self.base_canvas.yview
                            )
        
        self.base_canvas.configure(
                            yscrollcommand=self.scrollbar.set
                            )
        
        self.scrollbar.pack(
                        side=tk.RIGHT,
                        fill=tk.Y
                        )
        self.base_canvas.pack(
                        side=tk.TOP,
                        anchor=tk.NW,
                        fill=tk.X
                        )
        
        #####################################
        
        self._input_frame(self.base_canvas)

        self._room_frame(self.base_canvas)

        self.error_frame = tk.Frame(self.base_canvas)

        self.error_frame.pack()

        # save button
        self.__button(
            self.base_canvas,
            'Generate',
            cmd=self.generate,
            font_size=13,
            )

        #########################################
        
        self.base_canvas.configure(
                    scrollregion=self.base_canvas.bbox('all')
                    )

        self.root.mainloop()

    def _input_frame(self, container):
        # DATA INPUT FRAME
        self.data_frame = tk.Frame(container)
        self.data_frame.columnconfigure(0, weight=1)
        self.data_frame.columnconfigure(1, weight=1)

        self.wg_title = self.__label(self.data_frame, 'WG')

        # fläche
        self.flaeche = self.__entry(
            self.data_frame,
            'Fläche der Wohnung:',
            2
        )
        # preis per sqm
        self.preis = self.__entry(
            self.data_frame,
            'Preis per Sqm:',
            3
        )
        # preis der heizung per sqm
        self.heizung = self.__entry(
            self.data_frame,
            'Preis der Heizung per Sqm:',
            4
        )
        # nebenkosten
        self.nebenkosten = self.__entry(
            self.data_frame,
            'Nebenkosten:',
            5
        )
        # extras
        self.extras = self.__entry(
            self.data_frame,
            'Extras:',
            6
        )

        self.data_frame.pack(pady=10)

    def _room_frame(self, container):
        # ROOMS FRAME
        self.rooms_frame = tk.Frame(
                                container,
                                highlightbackground='grey',
                                highlightthickness=1,
                                # padx=100
                                )
        
        self.zimmer_label = self.__label(
                                self.rooms_frame,
                                'Zimmer'
                                )
        
        # plus button
        self.plus_button = self.__button(
                                self.rooms_frame,
                                '+',
                                cmd=self.add_room
                                )

        self.rooms_frame.pack(fill=tk.X)

    def __label(self, container, txt, font_size=13,
                justify=tk.W, label_type='normal'):
        if label_type == 'normal':
            tk.Label(
                container,
                text=txt,
                anchor=justify,
                font=('Arial', font_size),
                fg='black'
                ).pack(
                    padx=5,
                    pady=(5, 10),
                    side=tk.TOP,
                    fill=tk.X
                    )
        elif label_type == 'error':
            l = tk.Label(
                container,
                text=txt,
                anchor=tk.W,
                font=('Arial', 10),
                fg='red'
                )
            # yield l
            l.pack(
                padx=5,
                pady=5,
                side=tk.TOP,
                fill=tk.X
                )
            return l

    def __entry(self, container, txt, r=0):
        frame = tk.Frame(
            container,
            width=self.base_canvas.winfo_width()
            )
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        tk.Label(
            frame,
            text=txt,
            padx=5,
            justify='left'
            ).grid(
                row=0, column=0,
                sticky=tk.W
                )

        e = tk.Entry(
            frame,
            justify='left'
            )
        e.grid(
            row=0, column=1,
            sticky=tk.E
            )

        frame.pack(fill=tk.X)

        return e

    def __button(self, container, txt, cmd=None, font_size=20, size=(0,0)):
        button_frame = tk.Frame(container)
        tk.Button(
            button_frame,
            text=txt,
            font=('Arial', font_size),
            command=cmd,
            anchor=tk.W,
            justify='left',
            height=size[1] if not size[1] else 1,
            width=size[0] if not size[0] else len(txt)
            ).pack(
                padx=5,
                pady=0,
                side=tk.LEFT
                )
        button_frame.pack(
            fill=tk.X,
            side=tk.TOP,
            pady=5
        )   

    def add_room(self):
        # print('Add room')
        
        count = len(self.rooms) + 1
        self.rooms[f'Zimmer {count}'] = {
            "Name": "Name",
            "Mitbewohnis": [],
            "Fläche": -1
        }

        self.room_frame = tk.Frame(self.rooms_frame)
        self.room_frame.columnconfigure(0, weight=1)
        self.room_frame.columnconfigure(1, weight=1)

        self.__entry(
            self.room_frame,
            'Zimmer Name',
            r=count
        )
        self.__entry(
            self.room_frame,
            'Mitbewohnis',
            r=count+1
        )
        self.__entry(
            self.room_frame,
            'Fläche',
            r=count+2
        )
        # self.__label(
        #     self.room_frame,
        #     'Zimmer entfernen',
        #     color='red',
        #     font_size=10,
        #     justify=tk.E
        #     )

        # print(
        #     f'base_canvas height: {self.base_canvas.winfo_height()}',
        #     f'window height: {self.root.winfo_height()}',
        #     sep='\n')
        
        self.room_frame.pack(pady=10)

    def remove_error_label(self):
        if hasattr(self, 'error_label'):
            self.error_label.destroy()

    def generate(self):
        entries = [self.flaeche.get(), self.preis.get(),
                   self.heizung.get(), self.nebenkosten.get(),
                   self.extras.get()]
        
        self.remove_error_label()

        if not all(entries):
            self.error_label : tk.Label = self.__label(
                self.error_frame,
                txt='You have to fill out all the entries',
                label_type='error'
                )
        else:
            self.remove_error_label()
            date = datetime.now().strftime("%d-%m-%y")
            path = f'./src/data/data-{date}.json'
            count = 0

            while exists(path):
                count += 1
                path = f'./src/data/data-{date}({count}).json'
                print(path)

            with open(path, 'x') as file:
                file.write(f'''{{
    "WG": {{
            "Fläche": {self.flaeche.get()},
            "Preis": {self.preis.get()},
            "Heizung": {self.heizung.get()},
            "Nebenkosten": {self.nebenkosten.get()},
            "Extras": {self.extras.get()}
    }}
}}''')
