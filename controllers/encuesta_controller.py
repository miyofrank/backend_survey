# Lógica de control que ahora incluye el UID para filtrar por usuario

from fastapi import HTTPException
from models.encuesta_model import Encuesta
from services.encuesta_service import get_encuesta_by_id
from services import encuesta_service
from services.respuesta_service import calcular_resumen_respuestas
from services.encuesta_service import calcular_resumen_encuesta

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

def obtener_encuesta_publica(idEncuesta: str):
    encuesta = get_encuesta_by_id(idEncuesta)
    if not encuesta:
        raise HTTPException(status_code=404, detail="Encuesta no encontrada")
    return encuesta
    
def obtener_resumen_encuesta(idEncuesta: str):
    return calcular_resumen_respuestas(idEncuesta)


def obtener_resumen_encuesta_controller(id_encuesta: str, user_id: str):
    resumen = calcular_resumen_encuesta(id_encuesta, user_id)
    if not resumen:
        raise HTTPException(status_code=404, detail="No hay datos para esta encuesta")
    return resumen