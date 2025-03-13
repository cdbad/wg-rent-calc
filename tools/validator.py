from tkinter import ttk

class Validator:
    def validate_data(self, data: dict, error_lbl: ttk.Label) -> bool:
        zimmer_tot = 0

        if not data[self.kaltmiete_key]:
            error_lbl['text'] = 'Kaltmiete darf nicht null sein'
            return False
        
        if not data[self.grosse_key]:
            error_lbl['text'] = 'Größe darf nicht null sein'
            return False
        for z in self.zimmer_keys:
            zimmer_tot += float(data[z][self.grosse_key])

            if float(data[self.grosse_key]) < float(data[z][self.grosse_key]):
                error_lbl['text'] =\
                    'Zimmergröße ist mehr als Wohnungsgröße'
                return False
            for obj in data[z]:
                if not data[z][obj]:
                    error_lbl['text'] =\
                        'Zimmerdateien dürfen nicht null sein'
                    return False
        
        if float(data[self.grosse_key]) < zimmer_tot:
            error_lbl['text'] =\
                'Die Zimmer sind größer als die ganze Wohnung'
            return False
        
        return True