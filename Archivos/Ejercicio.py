import pandas as pd

def reporte_tiempos_traslados(nombre):
    df = pd.read_csv(nombre)
    # print(df.head())
    # lista = ["Hasta 15 minutos", "16 a 30 minutos", "31 minutos a 1 hora"]
    lista = df["Time to Work"].unique() # Obtiene los valores únicos de la columna Time to Work
    # print(lista)
    for i in lista:
        # Filtra por la columna Time to Work que sea igual al contenido de i
        suma = df[df["Time to Work"] == i]["Population"].sum()
        print(f"{i} - {suma}")
      
opcion = 0
while opcion != 3:
    
    if opcion == 1:
        nombre_archivo = input("Indica el nombre del archivo: ")
        reporte_tiempos_traslados(nombre_archivo)
    
    print("""1.  Reportes de Tiempos de traslados
2.  Captura de tiempo al trabajo según el medio de transporte de 2020 -
3.  Salir""")
    opcion = int(input("¿Qué opción desea llevar a cabo?: "))