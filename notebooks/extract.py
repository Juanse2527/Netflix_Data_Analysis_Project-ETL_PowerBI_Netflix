import pandas as pd
import os

csv_file_path = os.path.join("data", "netflix_titles.csv")

try:
    df_netflix = pd.read_csv(csv_file_path)
    print("todo salio bien")
    print(df_netflix.head())

except FileNotFoundError:
    print(f"No se encontro el archivo en la ruta: {csv_file_path}")

except Exception as e:
    print(f"Ocurrio un error al cargar el archivo {e}")
exit()
