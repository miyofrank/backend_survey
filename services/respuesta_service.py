from models.respuesta_model import Respuesta
from firebase.firebase_init import db
from typing import List

def get_all_by_user(uid: str) -> List[dict]:
    docs = db.collection("respuestas")\
             .where("idPersona", "==", uid)\
             .stream()
    return [doc.to_dict() for doc in docs]

def get_by_encuesta(idEncuesta: str) -> List[dict]:
    docs = db.collection("respuestas")\
             .where("idEncuesta", "==", idEncuesta)\
             .stream()
    return [doc.to_dict() for doc in docs]

def get_public_respuestas_by_encuesta(idEncuesta: str) -> List[dict]:
    # Sólo aquellas marcadas como anónimas/public
    docs = db.collection("respuestas")\
             .where("idEncuesta", "==", idEncuesta)\
             .where("idPersona", "in", [None, "public"])\
             .stream()
    return [doc.to_dict() for doc in docs]

def create(respuesta: Respuesta) -> Respuesta:
    doc_ref = db.collection("respuestas").document(respuesta.idRespuesta)
    doc_ref.set(respuesta.dict())
    return respuesta

def guardar_respuesta_publica(
    idEncuesta: str,
    respuesta_id: str,
    respuesta_obj: Respuesta,
    timestamp: str
):
    # 1) nested collection (para sumar en resumen si lo quieres)
    db.collection("respuestas")\
      .document(idEncuesta)\
      .collection("items")\
      .document(respuesta_id)\
      .set({
          "timestamp": timestamp,
          "respuestas": [r.dict() for r in respuesta_obj.respuestas]
      })

    # 2) colección raíz para la lista completa
    db.collection("respuestas")\
      .document(respuesta_id)\
      .set({
          "idRespuesta": respuesta_id,
          "idEncuesta": idEncuesta,
          "idPersona": respuesta_obj.idPersona or "public",
          "respuestas": [r.dict() for r in respuesta_obj.respuestas],
          "fechaRespuesta": timestamp
      })
