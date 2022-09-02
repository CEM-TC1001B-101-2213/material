import pandas as pd
import PySimpleGUI as sg

def crearVentanaTablaDatos():
    # Abre el archivo y lo carga en nuestra variable datos
    datos = pd.read_csv("IME_2020.csv")
    # Obtenemos el nombre de nuestras columnas
    columnas = datos.columns.tolist()
    # Mostraremos las primeras 10 filas
    valores = datos.head(10).values.tolist()
    layout = [
        [sg.Text("Tabla de IME 2020")],
        [sg.Table(headings=columnas, values=valores)]
        ]
    return sg.Window("Datos IME 2020", layout, finalize=True)

ventanaTablaDatos = crearVentanaTablaDatos()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break