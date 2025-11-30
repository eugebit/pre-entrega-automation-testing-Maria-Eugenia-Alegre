import csv
import os
import json

# funcion que recibbe el archivo a  leer
def get_login_csv(csv_file="data_login.csv"):
    current_file = os.path.dirname(__file__)  # guardo el archivo donde esta ubicado en una variable
    csv_file = os.path.join(current_file, "..", "data", csv_file)  # le digo donde está guardado el archivo
    csv_file = os.path.abspath(csv_file)  # paso la ruta absoluta

    casos = []

    with open(csv_file, newline="") as archivo:
        read = csv.DictReader(archivo)
        # recibe el archivo transforma el archivo a un diccionario donde la primer linea va a ser de clave y las siguiente valores
        for i in read:
            username = i["username"]
            password = i["password"]
            login_example = i["login_example"].lower() == "true"
            casos.append((username, password, login_example))
    return casos

# def get_login_json():
def get_login_json(json_file="data_login.json"):
    current_file = os.path.dirname(__file__)  # guardo el archivo donde esta ubicado en una variable
    json_file = os.path.join(current_file, "..", "data", json_file)  # le digo donde está guardado el archivo
    json_file = os.path.abspath(json_file)  # paso la ruta absoluta

    casos = []

    with open(json_file, newline="") as archivo:
        datos = json.load(archivo)
        # recibe el archivo transforma el archivo a un diccionario donde la primer linea va a ser de clave y las siguiente valores
        for i in datos:
            username = i["username"]
            password = i["password"]
            login_example = i["login_example"]
            casos.append((username, password, login_example))
    return casos

