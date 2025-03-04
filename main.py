import tkinter as tk
from tkinter import simpledialog
from Modulos.data_manager import cargar_datos, filtrar_datos
from Modulos.ui import iniciar_ui

ruta_archivo = "C:/Users/JACOBO/Suelos_pereira/resultado_laboratorio_suelo.xlsx"
df = cargar_datos(ruta_archivo)

if df is not None:
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter

    departamento = simpledialog.askstring("Entrada", "Ingrese el Departamento:")
    municipio = simpledialog.askstring("Entrada", "Ingrese el Municipio:")
    cultivo = simpledialog.askstring("Entrada", "Ingrese el Cultivo:")

    df_filtrado = filtrar_datos(df, departamento, municipio, cultivo)

    if not df_filtrado.empty:
        print(df_filtrado.head())  # Para depuración en consola
    else:
        print("⚠ No se encontraron datos con esos filtros.")

if __name__ == "__main__":
    iniciar_ui()
