# Acceso a Firestore filtrando encuestas por UID

from models.encuesta_model import Encuesta
from firebase.firebase_init import db

def get_all_by_user(user_id: str):
    docs = db.collection("encuestas").where("idPersona", "==", user_id).stream()
    return [doc.to_dict() for doc in docs]

def get_by_id_for_user(idEncuesta: str, uid: str):
    doc = db.collection("encuestas").document(idEncuesta).get()
    if doc.exists and doc.to_dict().get("idPersona") == uid:
        return doc.to_dict()
    return None

def create(encuesta: Encuesta):
    doc_ref = db.collection("encuestas").document(encuesta.idEncuesta)
    doc_ref.set(encuesta.dict())
    return encuesta

def update(idEncuesta: str, updated: Encuesta, uid: str):
    doc_ref = db.collection("encuestas").document(idEncuesta)
    doc = doc_ref.get()
    if doc.exists and doc.to_dict().get("idPersona") == uid:
        doc_ref.set(updated.dict())
        return updated
    return None

def delete(idEncuesta: str, uid: str):
    doc_ref = db.collection("encuestas").document(idEncuesta)
    doc = doc_ref.get()
    if doc.exists and doc.to_dict().get("idPersona") == uid:
        doc_ref.delete()
