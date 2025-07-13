# Rutas de encuestas protegidas con JWT y acceso al UID del usuario

from fastapi import APIRouter, Depends, Request
from controllers import encuesta_controller
from models.encuesta_model import Encuesta
from auth.auth_bearer import JWTBearer, get_current_user
from controllers.encuesta_controller import obtener_resumen_encuesta


router = APIRouter()

@router.get("/", dependencies=[Depends(JWTBearer())])
def get_all(request: Request):
    uid = request.state.user["uid"]
    return encuesta_controller.get_all(uid)

@router.get("/{idEncuesta}", dependencies=[Depends(JWTBearer())])
def get_by_id(idEncuesta: str, request: Request):
    uid = request.state.user["uid"]
    return encuesta_controller.get_by_id(idEncuesta, uid)

@router.post("/", dependencies=[Depends(JWTBearer())])
def create(encuesta: Encuesta, request: Request):
    uid = request.state.user["uid"]
    return encuesta_controller.create(encuesta, uid)

@router.put("/{idEncuesta}", dependencies=[Depends(JWTBearer())])
def update(idEncuesta: str, encuesta: Encuesta, request: Request):
    uid = request.state.user["uid"]
    return encuesta_controller.update(idEncuesta, encuesta, uid)

@router.delete("/{idEncuesta}", dependencies=[Depends(JWTBearer())])
def delete(idEncuesta: str, request: Request):
    uid = request.state.user["uid"]
    return encuesta_controller.delete(idEncuesta, uid)

@router.get("/{idEncuesta}/resultados/resumen", dependencies=[Depends(JWTBearer())])
def get_resumen_encuesta(idEncuesta: str, user_data: dict = Depends(get_current_user)):
    return encuesta_controller.obtener_resumen_encuesta_controller(idEncuesta, user_data["uid"])