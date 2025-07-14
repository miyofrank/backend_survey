from models.respuesta_model import Respuesta
from services import respuesta_service
from fastapi import HTTPException
from datetime import datetime
import uuid
from typing import List, Dict

def get_all(uid: str) -> List[Dict]:
    return respuesta_service.get_all_by_user(uid)

def create(respuesta: Respuesta, uid: str) -> Respuesta:
    respuesta.idPersona = uid
    return respuesta_service.create(respuesta)

def guardar_respuesta_publica(idEncuesta: str, respuesta: Respuesta) -> Dict:
    respuesta_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()
    # rellenar campos de Respuesta para guardar
    respuesta.idRespuesta = respuesta_id
    respuesta.idEncuesta = idEncuesta
    respuesta.idPersona = None
    respuesta.fechaRespuesta = datetime.utcnow()
    respuesta_service.guardar_respuesta_publica(
        idEncuesta, respuesta_id, respuesta, timestamp
    )
    return {"status": "ok", "id": respuesta_id}

def get_by_encuesta_controller(idEncuesta: str, user_id: str) -> List[Dict]:
    respuestas = respuesta_service.get_by_encuesta(idEncuesta)
    if not respuestas:
        raise HTTPException(404, "No hay respuestas registradas para esta encuesta")
    return respuestas

def get_public_respuestas(idEncuesta: str) -> List[Dict]:
    respuestas = respuesta_service.get_public_respuestas_by_encuesta(idEncuesta)
    if not respuestas:
        raise HTTPException(404, "No hay respuestas públicas para esta encuesta")
    return respuestas
