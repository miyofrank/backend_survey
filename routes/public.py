from fastapi import APIRouter, HTTPException
from models.schemas import Encuesta, Respuesta
from controllers.respuesta_controller import guardar_respuesta_publica
from controllers.encuesta_controller import obtener_encuesta_publica
from services.respuesta_service import get_items_publicos

router = APIRouter(tags=["Público"])


@router.get("/encuestas/{idEncuesta}/public", response_model=Encuesta)
def get_encuesta_publica(idEncuesta: str):
    """
    Devuelve una encuesta pública (sin autenticación).
    """
    return obtener_encuesta_publica(idEncuesta)


@router.post("/respuestas/encuesta/{idEncuesta}/public")
def post_respuesta_publica(idEncuesta: str, respuesta: Respuesta):
    return guardar_respuesta_publica(idEncuesta, respuesta)

@router.get("/respuestas/encuesta/{idEncuesta}/public/items")
def get_respuestas_publicas(idEncuesta: str):
    """
    Devuelve todas las respuestas anónimas enviadas a una encuesta pública,
    leyendo desde la subcolección Firestore: respuestas/{idEncuesta}/items.
    """
    respuestas = get_items_publicos(idEncuesta)
    if not respuestas:
        raise HTTPException(status_code=404, detail="No se encontraron respuestas públicas para esta encuesta")
    return respuestas
