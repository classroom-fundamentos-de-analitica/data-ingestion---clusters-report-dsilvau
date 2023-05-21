"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def format_input_string(input_string):
    output = []
    output.append(int(input_string[3:8]))
    output.append(int(input_string[9:15]))
    output.append(float(input_string[25:29].replace(',', '.')))
    fetch = input_string[41:]
    fetch = fetch.replace('\n', '')
    fetch = fetch.replace('.', '')
    fetch = re.sub(r' +', ' ', fetch)
    output.append(fetch)

    return output


def ingest_data():
    #
    # Inserta tu código aquí
    #

    with open("clusters_report.txt", "r") as file:
        lines = file.readlines()

    # Formato de nombre columnas
    headers = lines[:2]
    headers = [x.replace("\n", "").strip() for x in headers]
    headers = [re.split(r' {2,}', x) for x in headers]
    columns1 = headers[0]
    columns2 = headers[1]
    columns1[1] = columns1[1] + " " + columns2[0]
    columns1[2] = columns1[2] + " " + columns2[1]

    columns1 = [x.lower().replace(' ', '_') for x in columns1]

    # Formato de filas
    lines = lines[4:]
    formatted_input = ''.join(lines)
    formatted_input = re.split(r'\n *\n', formatted_input)
    formatted_input = list(filter(None, formatted_input))
    formatted_input = list(map(format_input_string, formatted_input))

    df = pd.DataFrame(formatted_input, columns=columns1)

    return df
