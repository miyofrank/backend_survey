from fastapi import APIRouter, Depends, Request
from models.respuesta_model import Respuesta
from controllers.respuesta_controller import (
    get_all,
    create,
    get_by_encuesta_controller,
    guardar_respuesta_publica,
    get_public_respuestas,
)
from auth.auth_bearer import JWTBearer

router = APIRouter(
    prefix="/respuestas",
    tags=["Respuestas"]
)

# ─── RUTAS PROTEGIDAS (requieren JWT) ─────────────────────────────────

@router.get("/", dependencies=[Depends(JWTBearer())])
def listar_todas(request: Request):
    uid = request.state.user["uid"]
    return get_all(uid)

@router.post("/", dependencies=[Depends(JWTBearer())])
def crear_protegida(respuesta: Respuesta, request: Request):
    uid = request.state.user["uid"]
    return create(respuesta, uid)

@router.get("/encuesta/{idEncuesta}", dependencies=[Depends(JWTBearer())])
def listar_por_encuesta_protegida(idEncuesta: str, request: Request):
    uid = request.state.user["uid"]
    return get_by_encuesta_controller(idEncuesta, uid)

# ─── RUTAS PÚBLICAS (anónimas) ────────────────────────────────────────

@router.post("/encuesta/{idEncuesta}/public")
def crear_publica(idEncuesta: str, respuesta: Respuesta):
    return guardar_respuesta_publica(idEncuesta, respuesta)

@router.get("/encuesta/{idEncuesta}/public")
def listar_por_encuesta_publica(idEncuesta: str):
    return get_public_respuestas(idEncuesta)
