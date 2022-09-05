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
        [sg.Button("Menú Principal", key="Datos volver")]
        ]
    return sg.Window("Datos IME 2020", layout, finalize=True)

def crearVentanaFormulario():
    opciones = ["Muy Bajo", "Bajo", "Medio", "Alto", "Muy Alto"]
    layout = [
        [sg.Text("CVE_ENT"),
         sg.Input(key="CVE_ENT")],
        [sg.Text("NOM_ENT"),
         sg.Input(key="NOM_ENT")],
        [sg.Text("POB_TOT"),
         sg.Input(key="POB_TOT")],
        [sg.Text("ANALF"),
         sg.Input(key="ANALF")],
        [sg.Text("SBASC"),
         sg.Input(key="SBASC")],
        [sg.Text("OVSDE"),
         sg.Input(key="OVSDE")],
        [sg.Text("OVSEE"),
         sg.Input(key="OVSEE")],
        [sg.Text("IM_2020"),
         sg.Input(key="IM_2020")],
        [sg.Text("GM_2020"),
         sg.Combo(opciones, key="GM_2020")],
        [sg.Text("IMN_2020"),
         sg.Input(key="IMN_2020")],
        [sg.Text("ULT"),
         sg.Input(key="ULT")],
        [sg.Button("Registrar", key="Formulario registrar"),
         sg.Button("Volver", key="Formulario volver")]
        ]
    return sg.Window("Formulario de datos", layout, finalize=True)

def crearVentanaMenuPrincipal():
    layout = [
        [sg.Text("Menú principal")],
        [sg.Button("Tabla de datos", key="tabla datos")],
        [sg.Button("Formulario", key="formulario")],
        [sg.Button("Salir", key="salir")],
        ]
    return sg.Window("Menú Principal", layout, finalize=True)

ventanaInicioSesion = crearVentanaInicioSesion()
ventanaRegistro = None
ventanaMenuPrincipal = None
ventanaTablaDatos = None
ventanaFormulario = None

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
        
    # Menú Principal -> Tabla de datos
    elif window == ventanaMenuPrincipal and event == "tabla datos" and ventanaTablaDatos is None:
        window.close()
        ventanaMenuPrincipal = None
        ventanaTablaDatos = crearVentanaTablaDatos()
    
    # Tabla de datos -> Menú Principal
    elif window == ventanaTablaDatos and event == "Datos volver" and ventanaMenuPrincipal is None:
        window.close()
        ventanaTablaDatos = None
        ventanaMenuPrincipal = crearVentanaMenuPrincipal()
    
    # Menú Principal -> Formulario
    elif window == ventanaMenuPrincipal and event == "formulario" and ventanaFormulario is None:
        window.close()
        ventanaMenuPrincipal = None
        ventanaFormulario = crearVentanaFormulario()
    
    # Formulario -> Menú Principal (volver)
    elif window == ventanaFormulario and event == "Formulario volver" and ventanaMenuPrincipal is None:
        window.close()
        ventanaFormulario = None
        ventanaMenuPrincipal = crearVentanaMenuPrincipal()    
    
    # Formulario -> Menú Principal (registrar)
    elif window == ventanaFormulario and event == "Formulario registrar" and ventanaMenuPrincipal is None:
        nuevo_registro = {
            "CVE_ENT": values["CVE_ENT"],
            "NOM_ENT": values["NOM_ENT"],
            "POB_TOT": values["POB_TOT"],
            "POB_TOT": values["POB_TOT"],
            "ANALF": values["ANALF"],
            "SBASC": values["SBASC"],
            "OVSDE": values["OVSDE"],
            "OVSEE": values["OVSEE"],
            "IM_2020": values["IM_2020"],
            "IM_2020": values["IM_2020"],
            "GM_2020": values["GM_2020"],
            "IMN_2020": values["IMN_2020"],
            "ULT": values["ULT"]
            }
        datos = pd.read_csv("IME_2020.csv")
        datos = datos.append(nuevo_registro, ignore_index=True)
        datos.to_csv("IME_2020.csv", index = False)
        
        sg.Popup("Se ha guardado el registro.", title="Éxito")
        
        #window.close()
        #ventanaFormulario = None
        #ventanaMenuPrincipal = crearVentanaMenuPrincipal()