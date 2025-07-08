# Acceso a Firestore filtrando encuestas por UID

from models.encuesta_model import Encuesta
from firebase.firebase_init import db
from collections import Counter

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

def get_encuesta_by_id(idEncuesta: str):
    doc = db.collection("encuestas").document(idEncuesta).get()
    if doc.exists:
        data = doc.to_dict()
        data["id"] = idEncuesta
        return data
    return None

def calcular_resumen_encuesta(id_encuesta: str, user_id: str):
    respuestas_ref = db.collection("respuestas")
    query = respuestas_ref.where("encuestaId", "==", id_encuesta).where("usuarioId", "==", user_id)
    docs = query.stream()

    agregados = {}
    total_nps = []

    for doc in docs:
        data = doc.to_dict()
        for pregunta_id, respuesta in data["respuestas"].items():
            if isinstance(respuesta, list):
                for r in respuesta:
                    agregados.setdefault(pregunta_id, []).append(r)
            else:
                agregados.setdefault(pregunta_id, []).append(respuesta)
            
            if "nps" in pregunta_id.lower():
                try:
                    total_nps.append(int(respuesta))
                except:
                    continue

    resumen = {}

    for pregunta_id, respuestas in agregados.items():
        conteo = dict(Counter(respuestas))
        resumen[pregunta_id] = {
            "total": len(respuestas),
            "conteo": conteo
        }

    if total_nps:
        promotores = len([n for n in total_nps if n >= 9])
        pasivos = len([n for n in total_nps if 7 <= n <= 8])
        detractores = len([n for n in total_nps if n <= 6])
        total = len(total_nps)
        nps_score = ((promotores - detractores) / total) * 100
        resumen["nps"] = {
            "promotores": promotores,
            "pasivos": pasivos,
            "detractores": detractores,
            "score": round(nps_score, 2)
        }

    return resumen