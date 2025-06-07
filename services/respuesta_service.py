from models.respuesta_model import Respuesta
from typing import List

respuestas: List[Respuesta] = []

def get_all():
    return respuestas

def get_by_encuesta(idEncuesta: str):
    return [r for r in respuestas if r.idEncuesta == idEncuesta]

def create(respuesta: Respuesta):
    respuestas.append(respuesta)
    return respuesta
