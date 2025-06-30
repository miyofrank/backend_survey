# Servicio para respuestas, ahora filtrando por UID del usuario autenticado

from models.respuesta_model import Respuesta
from firebase.firebase_init import db

def get_all_by_user(uid: str):
    docs = db.collection("respuestas").where("idPersona", "==", uid).stream()
    return [doc.to_dict() for doc in docs]

def get_by_encuesta_and_user(idEncuesta: str, uid: str):
    docs = db.collection("respuestas")\
        .where("idEncuesta", "==", idEncuesta)\
        .where("idPersona", "==", uid)\
        .stream()
    return [doc.to_dict() for doc in docs]

def create(respuesta: Respuesta):
    doc_ref = db.collection("respuestas").document(respuesta.idRespuesta)
    doc_ref.set(respuesta.dict())
    return respuesta
