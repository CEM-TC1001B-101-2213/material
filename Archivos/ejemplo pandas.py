import pandas as pd

# df -> DataFrame
df = pd.read_csv("CertificadosNacionalidadMexicanaPorNacimiento.csv")

print(df.head())

certificados_marzo = df["MAR"].sum()
promedio_certificados_marzo = df["MAR"].mean()

print(f"El total de certificados en marzo son: {certificados_marzo}")
print(f"El promedio de certificados en marzo son: {promedio_certificados_marzo}")

# Estadísticas descriptivas
print(df.describe())