# Rutas de respuestas protegidas por JWT

from fastapi import APIRouter, Depends, Request
from controllers import respuesta_controller
from models.respuesta_model import Respuesta
from auth.auth_bearer import JWTBearer, get_current_user
from controllers import respuesta_controller

router = APIRouter()

@router.get("/", dependencies=[Depends(JWTBearer())])
def get_all(request: Request):
    uid = request.state.user["uid"]
    return respuesta_controller.get_all(uid)

@router.get("/encuesta/{idEncuesta}", dependencies=[Depends(JWTBearer())])
def get_by_encuesta(idEncuesta: str, request: Request):
    uid = request.state.user["uid"]
    return respuesta_controller.get_by_encuesta(idEncuesta, uid)

@router.post("/", dependencies=[Depends(JWTBearer())])
def create(respuesta: Respuesta, request: Request):
    uid = request.state.user["uid"]
    return respuesta_controller.create(respuesta, uid)
@router.get("/respuestas/encuesta/{idEncuesta}", dependencies=[Depends(JWTBearer())])
def obtener_respuestas_individuales(idEncuesta: str, user_data: dict = Depends(get_current_user)):
    return respuesta_controller.obtener_respuestas_individuales_controller(idEncuesta, user_data["uid"])