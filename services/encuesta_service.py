from models.encuesta_model import Encuesta
from typing import List

encuestas: List[Encuesta] = []

def get_all():
    return encuestas

def get_by_id(idEncuesta: str):
    return next((e for e in encuestas if e.idEncuesta == idEncuesta), None)

def create(encuesta: Encuesta):
    encuestas.append(encuesta)
    return encuesta

def update(idEncuesta: str, updated: Encuesta):
    for idx, e in enumerate(encuestas):
        if e.idEncuesta == idEncuesta:
            encuestas[idx] = updated
            return updated
    return None

def delete(idEncuesta: str):
    global encuestas
    encuestas = [e for e in encuestas if e.idEncuesta != idEncuesta]
