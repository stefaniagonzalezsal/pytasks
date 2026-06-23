from datetime import datetime

class Tarea:
    def __init__(self, id, descripcion, completada=False, fecha_creacion=None, fecha_limite=None):
        self.id = id
        self.descripcion = descripcion
        self.completada = completada
        self.fecha_creacion = fecha_creacion or datetime.now().strftime("%Y-%m-%d %H:%M")
        self.fecha_limite = fecha_limite
    
    def marcar_completada(self):
        self.completada = True

    def to_dict(self): #Convertir tarea a un diccionario (Para guardarla en JSON)
        return{
            "id": self.id,
            "descripcion": self.descripcion,
            "completada": self.completada,
            "fecha_creacion": self.fecha_creacion,
            "fecha_limite": self.fecha_limite
        }
    @classmethod
    def from_dict(cls, data): #crea una tarea apartir de un diccionario (Al leerla del JSON)
        return cls(
            id=data["id"],
            descripcion=data["descripcion"],
            completada=data["completada"],
            fecha_creacion=data["fecha_creacion"],
            fecha_limite=data["fecha_limite"]
        )
    def __str__(self):
        estado = "[X]" if self.completada else "[ ]"
        texto_base = f"{estado} ({self.id}) {self.descripcion}"
        if self.fecha_limite:
            return f"{texto_base} — vence: {self.fecha_limite}"
        else:
            return texto_base

