import PySimpleGUI as sg

def crearVentanaConColumnas():
    layout = [
        [sg.Column([
            [sg.Text("Mi texto: ")],
            [sg.Text("Otro texto: ")]
            ]),
         sg.Column([
             [sg.Input()],
             [sg.Input()]
             ])]
        
        ]
    return sg.Window("Mi ventana", layout, finalize=True)

ventanaConColumnas = crearVentanaConColumnas()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break