from fastapi import HTTPException
from models.encuesta_model import Encuesta
from services import encuesta_service

def get_all():
    return encuesta_service.get_all()

def get_by_id(idEncuesta: str):
    encuesta = encuesta_service.get_by_id(idEncuesta)
    if encuesta is None:
        raise HTTPException(status_code=404, detail="Encuesta no encontrada")
    return encuesta

def create(encuesta: Encuesta):
    return encuesta_service.create(encuesta)

def update(idEncuesta: str, encuesta: Encuesta):
    result = encuesta_service.update(idEncuesta, encuesta)
    if result is None:
        raise HTTPException(status_code=404, detail="Encuesta no encontrada")
    return result

def delete(idEncuesta: str):
    encuesta_service.delete(idEncuesta)
    return {"message": "Encuesta eliminada"}
