from Modulos.data_manager import cargar_datos, filtrar_datos

ruta_archivo = "C:/Users/JACOBO/Suelos_pereira/resultado_laboratorio_suelo.xlsx"
df = cargar_datos(ruta_archivo)

if df is not None:
    departamento = input("Ingrese el Departamento: ")
    municipio = input("Ingrese el Municipio: ")
    cultivo = input("Ingrese el Cultivo: ")

    df_filtrado = filtrar_datos(df, departamento, municipio, cultivo)

    if not df_filtrado.empty:
        print(df_filtrado.head())  # Mostrar primeras filas
    else:
        print("⚠ No se encontraron datos con esos filtros.")
