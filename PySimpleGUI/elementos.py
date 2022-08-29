import PySimpleGUI as sg

def crearVentanaPrincipal():
    vacunas = ["Pfizer", "Moderna", "AstraZeneca", "Sputnik", "Sinovac", "Cansino"]
    layout = [
        [sg.Text("Hola, soy un texto", font="Arial 30"),
         sg.Text("Yo también")],
        [sg.Button("Soy un botón", key="botón1", image_filename="eeeve.png"),
         sg.Button("Soy otro botón", key="botón2")],
        [sg.Text("Correo:"),
         sg.Input(key="input correo", default_text="Ingresa tu correo")],
        [sg.Text("Contraseña:"),
         sg.Input(key="input contraseña", password_char="*")],
        [sg.Text("Estado de vacunación"),
         sg.Radio("Estoy vacunado", key="radio vacunado sí", group_id="radio vacunación", enable_events=True),
         sg.Radio("No estoy vacunado", key="radio vacunado no", group_id="radio vacunación", default=True, enable_events=True)],
        [sg.Text("Marca de la vacuna:"),
         sg.Combo(vacunas, key="combo vacunas", default_value="Pfizer", disabled=True)],
        [sg.Text("Hobbies"),
         sg.Checkbox("Ver series", key="check series"),
         sg.Checkbox("Ver películas", key="check películas"),
         sg.Checkbox("Escuchar música", key="check música")]
        ]
    return sg.Window("Mi ventana principal", layout, finalize=True)

ventanaPrincipal = crearVentanaPrincipal()

while True:
    window, event, values = sg.read_all_windows()
    print(f"Window: {window} - Event: {event} - Values {values}")
    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    elif event == "botón1":
        print("Dieron click en el botón 1")
    elif event == "botón2":
        print("Dieron click en botón2")
    elif event == "radio vacunado sí":
        window["combo vacunas"].update(disabled=False)
    elif event == "radio vacunado no":
        window["combo vacunas"].update(disabled=True)