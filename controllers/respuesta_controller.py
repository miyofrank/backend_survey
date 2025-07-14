# Controlador de respuestas con filtro por usuario

from models.respuesta_model import Respuesta
from services import respuesta_service
from models.schemas import Respuesta
from services.respuesta_service import guardar_respuesta_firestore
from datetime import datetime
from fastapi import HTTPException
from services.respuesta_service import obtener_respuestas_por_encuesta, guardar_respuesta_publica as svc_guardar_publica
import uuid

def get_all(uid: str):
    return respuesta_service.get_all_by_user(uid)

def get_by_encuesta(idEncuesta: str, uid: str):
    return respuesta_service.get_by_encuesta_and_user(idEncuesta, uid)

def create(respuesta: Respuesta, uid: str):
    respuesta.idPersona = uid
    return respuesta_service.create(respuesta)

def guardar_respuesta_publica(idEncuesta: str, respuesta: Respuesta):
    """
    Controlador para guardar una respuesta pública.
    Genera un ID único y timestamp, y delega en el servicio.
    """
    respuesta_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()
    try:
        svc_guardar_publica(idEncuesta, respuesta_id, respuesta, timestamp)
    except Exception as e:
        # Atrapa errores de Firestore y devuelve 400
        raise HTTPException(status_code=400, detail=f"No se pudo guardar la respuesta: {e}")
    return {"status": "ok", "id": respuesta_id}

def obtener_respuestas_individuales_controller(id_encuesta: str, user_id: str):
    respuestas = obtener_respuestas_por_encuesta(id_encuesta, user_id)
    if not respuestas:
        raise HTTPException(status_code=404, detail="No hay respuestas registradas")
    return respuestas