from fastapi import APIRouter
from controllers import encuesta_controller
from models.encuesta_model import Encuesta

router = APIRouter()

@router.get("/")
def get_all():
    return encuesta_controller.get_all()

@router.get("/{idEncuesta}")
def get_by_id(idEncuesta: str):
    return encuesta_controller.get_by_id(idEncuesta)

@router.post("/")
def create(encuesta: Encuesta):
    return encuesta_controller.create(encuesta)

@router.put("/{idEncuesta}")
def update(idEncuesta: str, encuesta: Encuesta):
    return encuesta_controller.update(idEncuesta, encuesta)

@router.delete("/{idEncuesta}")
def delete(idEncuesta: str):
    return encuesta_controller.delete(idEncuesta)
