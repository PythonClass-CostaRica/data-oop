from csv_reader import read_csv_to_list_if_dict
from delito import Delito, Delitos


raw_data = read_csv_to_list_if_dict('data/input_data.csv')

delitos = Delitos(raw_csv_data=raw_data)

print(f"Cantidad de delitos en Heredia: {delitos.count_delitos_in_province('Heredia')}")
print(f"Cantidad de delitos en Cartago: {delitos.count_delitos_in_province('Cartago')}")
print(f"Cantidad de delitos en San Jose: {delitos.count_delitos_in_province('San Jose')}")
print(f"Cantidad de delitos en Guanacaste: {delitos.count_delitos_in_province('Guanacaste')}")
print(f"Cantidad de delitos en Limon: {delitos.count_delitos_in_province('Limon')}")
print(f"Cantidad de delitos en Puntarenas: {delitos.count_delitos_in_province('Puntarenas')}")
print(f"Cantidad de delitos en Alajuela: {delitos.count_delitos_in_province('Alajuela')}")


