import json
from tarea import Tarea

def guardar_tareas(tareas, ruta="data/tareas.json"):
    lista_dict = [tarea.to_dict() for tarea in tareas]
    with open(ruta, "w") as archivo:
        json.dump(lista_dict, archivo, indent=4)

def cargar_tareas(ruta= "data/tareas.json"):
    try:
         with open(ruta, "r") as archivo:
            lista_dict = json.load(archivo)
            tareas = [Tarea.from_dict(dato) for dato in lista_dict]
         return tareas
    except FileNotFoundError:
        return []