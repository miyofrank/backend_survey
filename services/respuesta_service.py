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

def guardar_respuesta_firestore(idEncuesta, respuesta_id, respuesta_obj, timestamp):
    db.collection("respuestas").document(idEncuesta).collection("items").document(respuesta_id).set({
        "timestamp": timestamp,
        "respuestas": [r.dict() for r in respuesta_obj.respuestas]
    })

def calcular_resumen_respuestas(idEncuesta: str):
    respuestas = db.collection("respuestas").document(idEncuesta).collection("items").stream()
    conteo = {}

    for doc in respuestas:
        data = doc.to_dict()
        for r in data.get("respuestas", []):
            pid = r["preguntaId"]
            val = r["valor"]
            if isinstance(val, list):
                for item in val:
                    conteo.setdefault(pid, {}).setdefault(item, 0)
                    conteo[pid][item] += 1
            else:
                conteo.setdefault(pid, {}).setdefault(val, 0)
                conteo[pid][val] += 1
    return conteo

def obtener_respuestas_por_encuesta(id_encuesta: str, user_id: str):
    respuestas_ref = db.collection("respuestas")
    query = respuestas_ref.where("encuestaId", "==", id_encuesta).where("usuarioId", "==", user_id)
    docs = query.stream()
    return [doc.to_dict() for doc in docs]

def guardar_respuesta_publica(idEncuesta, respuesta_id, respuesta_obj, timestamp):
    # 1) guardado en nested collection (ya existía)
    db.collection("respuestas")\
      .document(idEncuesta)\
      .collection("items")\
      .document(respuesta_id)\
      .set({
        "timestamp": timestamp,
        "respuestas": [r.dict() for r in respuesta_obj.respuestas]
    })

    # 2) guardado en colección raíz para consulta protegida
    db.collection("respuestas")\
      .document(respuesta_id)\
      .set({
        "idRespuesta": respuesta_id,
        "idEncuesta": idEncuesta,
        "idPersona": None,            # o "public" si quieres marcarlo
        "respuestas": [r.dict() for r in respuesta_obj.respuestas],
        "fechaRespuesta": timestamp
    })
