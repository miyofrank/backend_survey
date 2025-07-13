from fastapi import APIRouter, Depends, Request
from controllers import respuesta_controller
from models.respuesta_model import Respuesta
from auth.auth_bearer import JWTBearer

router = APIRouter(
    prefix="/respuestas",
    tags=["Respuestas"],
    dependencies=[Depends(JWTBearer())]
)

@router.get("/", summary="Obtener todas las respuestas del usuario autenticado")
def get_all(request: Request):
    uid = request.state.user["uid"]
    return respuesta_controller.get_all(uid)

@router.get("/encuesta/{idEncuesta}", summary="Obtener respuestas de una encuesta específica para el usuario autenticado")
def get_by_encuesta(idEncuesta: str, request: Request):
    uid = request.state.user["uid"]
    return respuesta_controller.get_by_encuesta(idEncuesta, uid)

@router.post("/", summary="Crear una nueva respuesta (solo admin o uso interno)")
def create(respuesta: Respuesta, request: Request):
    uid = request.state.user["uid"]
    return respuesta_controller.create(respuesta, uid)