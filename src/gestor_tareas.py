from tarea import Tarea
from almacenamiento import guardar_tareas, cargar_tareas

class GestorTareas:
    def __init__(self, ruta= "data/tareas.json"):
        self.ruta = ruta
        self.tareas = cargar_tareas(ruta)
    
    def agregar_tarea(self, descripcion, fecha_limite=None):
        nuevo_id = len(self.tareas) + 1
        nueva_tarea = Tarea(id=nuevo_id, descripcion=descripcion, fecha_limite=fecha_limite)
        self.tareas.append(nueva_tarea)
        guardar_tareas(self.tareas, self.ruta)
    
    def completar_tarea(self, id_tarea):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                tarea.marcar_completada()
                guardar_tareas(self.tarea, self.ruta)
                return
    
    def eliminar_tarea(self, id_tarea):
        self.tareas = [tarea for tarea in self.tareas if tarea.id != id_tarea]
        guardar_tareas(self.tareas, self.ruta)