# Controlador de respuestas con filtro por usuario

from models.respuesta_model import Respuesta
from services import respuesta_service

def get_all(uid: str):
    return respuesta_service.get_all_by_user(uid)

def get_by_encuesta(idEncuesta: str, uid: str):
    return respuesta_service.get_by_encuesta_and_user(idEncuesta, uid)

def create(respuesta: Respuesta, uid: str):
    respuesta.idPersona = uid
    return respuesta_service.create(respuesta)
