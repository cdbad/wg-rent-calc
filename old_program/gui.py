import PySimpleGUI as sg
# from calc import write_doc
import json
# from abc import abstractmethod

sg.set_options(font=('Helvetica', 13))

def singleton(class_):
    instance = None
    
    def inner():
        nonlocal instance

        if not instance:
            instance = class_()
        return instance

    return inner

@singleton
class GUI:
    def __init__(self) -> None:
        self._window = sg.Window(title='WG rent calc')

    def _build_data_frame(self):
        def data_manipulation():
            if self.bearbeiten:
                print('bearbeiten')
            else:
                zimmer = ''
                for el in self.data['Pro_zimmer'].keys():
                    zimmer += el + f": {self.data['Pro_zimmer'][el]} m²\n"
                return zimmer

        return sg.Frame(
            None,
            [
                [
                    sg.Text(
                        f'''KOSTEN
Ganzes Kaltpreis: €{self.data['Totals']['Kalt']}
Ganzen Wohnflächen: {self.data['Totals']['Wohnfläche']} m²
Preis per m²: €{self.data['Kosten']['Fläche']}
Ganze Heizung: €{self.data['Totals']['Heizung']}
\nZIMMER
{data_manipulation()}'''),
                ],
                # [
                    
                #     sg.Table(
                #         [['A', 'B'], ['C', 'D']],
                #         size=(400,200)
                #     )
                # ]
            ],
            size=(400,300),
            font="Helvetica 13",
        )
    
    def _build_buttons(self):
        return sg.Frame(
            None,
            [
                [
                    sg.Button(
                        button_text="Bearbeiten",
                        key="-BEARBEITEN-",
                        font='Helvetica 13',
                    ),
                    sg.Button(
                        button_text="Herunterladen",
                        key="-HERUNTERLADEN-",
                        font='Helvetica 13',
                    ),
                ]
            ],
            font="Any 20",
            size=(400,50),
            vertical_alignment='bottom'
        )

    def read_event(self):
        return self._window.read()
    
    def close(self):
        self._window.close()

gui = GUI()
while True:
    event, values = gui._window.read()
    if event != sg.WIN_CLOSED:
        if event == '-BEARBEITEN-':
            print('bearbeiten', event, values)
        elif event == '-HERUNTERLADEN-':
            print('herunterladen', event, values)
    else:
        break
gui.close()