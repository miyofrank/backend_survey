# Rutas de respuestas protegidas por JWT

from fastapi import APIRouter, Depends, Request
from controllers import respuesta_controller
from models.respuesta_model import Respuesta
from auth.auth_bearer import JWTBearer

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
