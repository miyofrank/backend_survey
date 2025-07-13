# routes/respuesta_routes.py
from fastapi import APIRouter, Depends, Request
from controllers import respuesta_controller
from models.respuesta_model import Respuesta
from auth.auth_bearer import JWTBearer

# Quitamos el prefix aquí para que no se duplique al incluirlo en main.py
router = APIRouter(
    tags=["Respuestas"],
    dependencies=[Depends(JWTBearer())]
)

@router.get("/encuesta/{idEncuesta}", summary="Obtener respuestas de una encuesta específica para el usuario autenticado")
def get_by_encuesta(idEncuesta: str, request: Request):
    uid = request.state.user["uid"]
    return respuesta_controller.get_by_encuesta(idEncuesta, uid)

@router.get("/", summary="Obtener todas las respuestas del usuario autenticado")
def get_all(request: Request):
    uid = request.state.user["uid"]
    return respuesta_controller.get_all(uid)

@router.post("/", summary="Crear una nueva respuesta")
def create(respuesta: Respuesta, request: Request):
    uid = request.state.user["uid"]
    return respuesta_controller.create(respuesta, uid)