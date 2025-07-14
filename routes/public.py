from fastapi import APIRouter, HTTPException
from models.schemas import Encuesta, Respuesta
from controllers.respuesta_controller import guardar_respuesta_publica
from controllers.encuesta_controller import obtener_encuesta_publica
from services.respuesta_service import get_items_publicos

router = APIRouter(tags=["Público"])

@router.get("/encuestas/{idEncuesta}/public", response_model=Encuesta)
def get_encuesta_publica(idEncuesta: str):
    return obtener_encuesta_publica(idEncuesta)

@router.post("/respuestas/encuesta/{idEncuesta}/public")
def post_respuesta_publica(idEncuesta: str, respuesta: Respuesta):
    return guardar_respuesta_publica(idEncuesta, respuesta)


@router.get("/respuestas/encuesta/{idEncuesta}/public/items")
def get_respuestas_publicas(idEncuesta: str):
    """
    Devuelve todas las respuestas anónimas de una encuesta,
    leyendo la subcolección `items`.
    """
    return get_items_publicos(idEncuesta)

