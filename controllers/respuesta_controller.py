# Controlador de respuestas con filtro por usuario

from models.respuesta_model import Respuesta
from services import respuesta_service
from models.schemas import Respuesta
from services.respuesta_service import guardar_respuesta_firestore
from datetime import datetime
from fastapi import HTTPException
from services.respuesta_service import obtener_respuestas_por_encuesta, get_by_encuesta  
import uuid

def get_all(uid: str):
    return respuesta_service.get_all_by_user(uid)

def create(respuesta: Respuesta, uid: str):
    respuesta.idPersona = uid
    return respuesta_service.create(respuesta)

def guardar_respuesta_publica(idEncuesta: str, respuesta: Respuesta):
    respuesta_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()
    # llama a la función que ahora duplica el guardado
    guardar_respuesta_firestore(idEncuesta, respuesta_id, respuesta, timestamp)
    return {"status": "ok", "id": respuesta_id}

def obtener_respuestas_individuales_controller(id_encuesta: str, user_id: str):
    respuestas = obtener_respuestas_por_encuesta(id_encuesta, user_id)
    if not respuestas:
        raise HTTPException(status_code=404, detail="No hay respuestas registradas")
    return respuestas

def get_by_encuesta_controller(idEncuesta: str, user_id: str):
    """
    Retorna TODAS las respuestas de la encuesta idEncuesta,
    para que el dueño de la encuesta (usuario autenticado) las vea.
    """
    respuestas = get_by_encuesta(idEncuesta)
    if not respuestas:
        raise HTTPException(status_code=404, detail="No hay respuestas registradas")
    return respuestas