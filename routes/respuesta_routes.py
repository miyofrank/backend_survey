# routes/respuesta_routes.py
from fastapi import APIRouter, Depends, Request
from controllers import respuesta_controller
from models.respuesta_model import Respuesta
from auth.auth_bearer import JWTBearer
from controllers.respuesta_controller import get_by_encuesta_controller

# Quitamos el prefix aquí para que no se duplique al incluirlo en main.py
router = APIRouter(
    prefix="/respuestas",
    tags=["Respuestas"],
    dependencies=[Depends(JWTBearer())],
)

@router.get("/encuesta/{idEncuesta}", summary="Obtener todas las respuestas de una encuesta")
def respuestas_por_encuesta(idEncuesta: str, request: Request):
    # request.state.user["uid"] ya está validado por JWTBearer(), 
    # pero no lo usamos para filtrar aquí
    return get_by_encuesta_controller(idEncuesta)

@router.post("/", summary="Crear una nueva respuesta")
def create(respuesta: Respuesta, request: Request):
    uid = request.state.user["uid"]
    return respuesta_controller.create(respuesta, uid)