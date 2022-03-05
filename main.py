import csv

diccionario = {}
#lectura de mi archivo csv
with open('synergy_logistics_database.csv', 'r') as archivo_csv:
    lector = csv.reader(archivo_csv)
    for linea in lector:
        print(linea)