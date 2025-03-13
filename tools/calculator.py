from tkinter import ttk
from tools.pdf_maker import make_pdf
from .fetcher import Fetcher
from .validator import Validator
import re


class Calculator(Fetcher, Validator):    
    def calculate(self):
        self.table = list()

        # mitbewohnis
        mitbewohnis = ['Mitbewohner']
 
        # titles
        self.table = [[
            'Mitbewohner',
            'Zimmer',
            self.grosse_key,
            self.kaltmiete_key,
            self.heizung_key,
            self.nebenkosten_key,
            self.extra_key,
            'Summe'
        ]]

        # values
        alle_mitbewohnis = list()
        shared_space: float = self.grosse - sum([
                            float(self.data[room_name][self.grosse_key])\
                            for room_name in self.zimmer_keys
                            ])
        price_per_sqm: float = self.kaltmiete / self.grosse

        for z_name in self.zimmer_keys:
            room = self.data[z_name]

            mitbewohnis = re.split(
                r'\s*,\s*',
                room['Mitbewohnis']
            )
            alle_mitbewohnis.extend(mitbewohnis)

            for mitbewohni in mitbewohnis:
                z_grosse: float = float(room[self.grosse_key]) / len(mitbewohnis)
                z_kalt: float = shared_space * price_per_sqm +\
                                z_grosse * price_per_sqm

                self.table.append([
                    mitbewohni.capitalize(),
                    z_name,
                    f'{z_grosse:.2f} m²',
                    f'€ {z_kalt:.2f}',
                    f'€ {self.heizung:.2f}',
                    f'€ {self.nebenkosten:.2f}',
                    f'€ {self.extra:.2f}',
                    f'€ {(z_kalt + self.heizung + self.nebenkosten + self.extra):.2f}'
                ])

        print(self.table)

    def reverse_table(self):
        self.pdf_table = list()
        
        for col in range(len(self.table[0])):
            self.pdf_table.append(list())
            for d in self.table:
                self.pdf_table[col].append(d[col])

    def send_data(self, frame: ttk.Frame, error_lbl: ttk.Label):
        self.frame = frame
        self.error_lbl = error_lbl

        self.error_lbl['text'] = ''

        self.data = self.fetch_data(self.frame)

        self.keys = self.data.keys()
        self.name_key, self.kaltmiete_key, self.grosse_key, self.heizung_key,\
            self.nebenkosten_key, self.extra_key, *self.zimmer_keys = self.keys
        self.name = self.data[self.name_key]
        self.kaltmiete = float(self.data[self.kaltmiete_key])
        self.grosse = float(self.data[self.grosse_key])
        self.heizung = float(self.data[self.heizung_key])
        self.nebenkosten = float(self.data[self.nebenkosten_key])
        self.extra = float(self.data[self.extra_key])
        
        if self.validate_data(self.data, self.error_lbl):
            self.calculate()
            self.reverse_table()

            make_pdf(self.pdf_table, self.name, self.kaltmiete)
