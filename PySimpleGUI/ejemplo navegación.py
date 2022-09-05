import PySimpleGUI as sg
import pandas as pd

def crearVentanaInicioSesion():
    layout = [
        [sg.Text("Correo"),
         sg.Input(key="InicioSesión correo")],
        [sg.Text("Contraseña"),
         sg.Input(key="InicioSesión contraseña", password_char="*")],
        [sg.Button("Iniciar sesión", key="inicio sesión"),
         sg.Button("Registrarse", key="registrarse")]
        ]
    return sg.Window("Inicio de sesión", layout, finalize=True)

def crearVentanaRegistro():
    layout= [
        [sg.Text("Correo"),
         sg.Input(key="Registro correo")],
        [sg.Text("Contraseña"),
         sg.Input(key="Registro contraseña", password_char="*")],
        [sg.Text("Repetir contraseña"),
         sg.Input(key="Registro repetir contraseña", password_char="*")],
        [sg.Checkbox("Recibir notificaciones", key="notificaciones")],
        [sg.Button("Registrar", key="registrar"),
         sg.Button("Volver", key="volver")]
        ]
    return sg.Window("Registro", layout, finalize=True)

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
        [sg.Text(f"Mínimo: {minimo}")],
        [sg.Button("Menú Principal", key="Datos Menú Principal")]
        ]
    return sg.Window("Datos IME 2020", layout, finalize=True)

def crearVentanaMenuPrincipal():
    layout = [
        [sg.Text("Menú principal")],
        [sg.Button("Tabla de dato", key="tabla datos")],
        [sg.Button("Salir", key="salir")],
        ]
    return sg.Window("Menú Principal", layout, finalize=True)

ventanaInicioSesion = crearVentanaInicioSesion()
ventanaRegistro = None
ventanaMenuPrincipal = None
ventanaTablaDatos = None

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED or event == "salir":
        window.close()
        break
    
    # Reviso:
    # Estoy en la ventana correcta
    # El botón es el que me va a mandar a otra ventana
    # La otra ventana estaba cerrada antes de mandarme allá
    
    # InicioSesión -> Menú Principal
    if window == ventanaInicioSesion and event == "inicio sesión" and ventanaMenuPrincipal is None:
        window.close()
        ventanaInicioSesion = None
        ventanaMenuPrincipal = crearVentanaMenuPrincipal()
    # IncioSesión -> Registro
    elif window == ventanaInicioSesion and event == "registrarse" and ventanaRegistro is None:
        window.close()
        ventanaInicioSesion = None
        ventanaRegistro = crearVentanaRegistro()
    
    # Registro -> Menú Principal (registrar)
    elif window == ventanaRegistro and event == "registrar" and ventanaMenuPrincipal is None:
        contraseña = values["Registro contraseña"]
        repetir_contraseña = values["Registro repetir contraseña"]
        if contraseña == repetir_contraseña:
            window.close()
            ventanaRegistro = None
            ventanaMenuPrincipal = crearVentanaMenuPrincipal()
        else:
            sg.Popup("La contraseña no es igual.", title="Error")
    # Registro -> InicioSesión (volver)
    elif window == ventanaRegistro and event == "volver" and ventanaInicioSesion is None:
        window.close()
        ventanaRegistro = None
        ventanaInicioSesion = crearVentanaInicioSesion()