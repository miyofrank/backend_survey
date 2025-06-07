from fastapi import APIRouter
from controllers import respuesta_controller
from models.respuesta_model import Respuesta

router = APIRouter()

@router.get("/")
def get_all():
    return respuesta_controller.get_all()

@router.get("/encuesta/{idEncuesta}")
def get_by_encuesta(idEncuesta: str):
    return respuesta_controller.get_by_encuesta(idEncuesta)

@router.post("/")
def create(respuesta: Respuesta):
    return respuesta_controller.create(respuesta)
