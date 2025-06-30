from pydantic import BaseModel
from typing import List
from datetime import datetime

class Item(BaseModel):
    idItem: str
    contenido: str

class Pregunta(BaseModel):
    idPregunta: str
    nombre: str
    texto: str
    tipo: str
    items: List[Item]

class Encuesta(BaseModel):
    idEncuesta: str
    idPersona: str
    nombre: str
    estadoEncuesta: str
    estadoLogico: bool
    fechaCreacion: datetime
    fechaModificacion: datetime
    preguntas: List[Pregunta]
    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime('%Y-%m-%d %H:%M')
        }
