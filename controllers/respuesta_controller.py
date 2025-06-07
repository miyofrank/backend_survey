from models.respuesta_model import Respuesta
from services import respuesta_service

def get_all():
    return respuesta_service.get_all()

def get_by_encuesta(idEncuesta: str):
    return respuesta_service.get_by_encuesta(idEncuesta)

def create(respuesta: Respuesta):
    return respuesta_service.create(respuesta)
