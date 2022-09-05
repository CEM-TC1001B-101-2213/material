import pandas as pd
import PySimpleGUI as sg

def crearVentanaTablaDatos():
    # Abre el archivo y lo carga en nuestra variable datos
    datos = pd.read_csv("IME_2020.csv")
    # Obtenemos el nombre de nuestras columnas
    columnas = datos.columns.tolist()
    # Mostraremos las primeras 10 filas
    valores = datos.head(10).values.tolist()
    suma = datos["ULT"].sum()
    promedio = datos["ULT"].mean()
    maximo = datos["ULT"].max()
    minimo = datos["ULT"].min()
    layout = [
        [sg.Text("Tabla de IME 2020")],
        [sg.Table(headings=columnas, values=valores)],
        [sg.Text(f"Suma: {suma}")],
        [sg.Text(f"Promedio: {promedio}")],
        [sg.Text(f"Máximo: {maximo}")],
        [sg.Text(f"Mínimo: {minimo}")]
        ]
    return sg.Window("Datos IME 2020", layout, finalize=True)

ventanaTablaDatos = crearVentanaTablaDatos()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break