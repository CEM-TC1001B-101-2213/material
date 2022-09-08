import PySimpleGUI as sg

def crearVentanaConFrame():
    layout = [
        [sg.Frame("Título de mi frame", [
            [sg.Text("Texto dentro del frame")],
            [sg.Button("Botón dentro del frame")]],
                  key = "Mi Frame")],
        [sg.Button("Ocultar/Mostrar Frame", key="Botón")]
        ]
    return sg.Window("Mi ventana", layout, finalize=True)

ventanaConFrame = crearVentanaConFrame()
mostrar = True

while True:
    window, event, values = sg.read_all_windows()
    
    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    elif event == "Botón":
        mostrar = not mostrar
        window["Mi Frame"].update(visible = mostrar)