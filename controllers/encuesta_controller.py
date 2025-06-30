# Lógica de control que ahora incluye el UID para filtrar por usuario

from fastapi import HTTPException
from models.encuesta_model import Encuesta
from services import encuesta_service

def get_all(uid: str):
    return encuesta_service.get_all_by_user(uid)

def get_by_id(idEncuesta: str, uid: str):
    encuesta = encuesta_service.get_by_id_for_user(idEncuesta, uid)
    if encuesta is None:
        raise HTTPException(status_code=404, detail="Encuesta no encontrada")
    return encuesta

def create(encuesta: Encuesta, uid: str):
    encuesta.idPersona = uid
    return encuesta_service.create(encuesta)

def update(idEncuesta: str, encuesta: Encuesta, uid: str):
    encuesta.idPersona = uid
    result = encuesta_service.update(idEncuesta, encuesta, uid)
    if result is None:
        raise HTTPException(status_code=404, detail="Encuesta no encontrada")
    return result

def delete(idEncuesta: str, uid: str):
    encuesta_service.delete(idEncuesta, uid)
    return {"message": "Encuesta eliminada"}
