# Rutas de autenticación para registro y login con Firebase

from fastapi import APIRouter
from pydantic import BaseModel
from auth.auth_firebase import register_user, RegisterUser, login_with_token

class FirebaseToken(BaseModel):
    token: str  # Token enviado desde frontend tras login con Firebase SDK

router = APIRouter()

@router.post("/register")
def register(data: RegisterUser):
    """
    Registra un nuevo usuario en Firebase Authentication y Firestore.
    """
    return register_user(data)

@router.post("/login")
def login(token: FirebaseToken):
    """
    Valida el ID token del cliente y devuelve la información del usuario.
    """
    return login_with_token(token.token)
