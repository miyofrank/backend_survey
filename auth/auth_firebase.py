from fastapi import HTTPException
from firebase_admin import auth
from pydantic import BaseModel
from models.user_model import LoginUser
from firebase.firebase_init import db

class RegisterUser(BaseModel):
    email: str
    password: str
    name: str

def login_user(data: LoginUser):
    # Firebase Admin SDK NO permite login con email/contraseña desde el backend
    raise HTTPException(
        status_code=400,
        detail="El inicio de sesión debe hacerse en el cliente usando Firebase SDK. Este endpoint es informativo."
    )

def register_user(data: RegisterUser):
    try:
        user = auth.create_user(
            email=data.email,
            password=data.password,
            display_name=data.name
        )
        db.collection("usuarios").document(user.uid).set({
            "email": data.email,
            "name": data.name
        })
        return {"uid": user.uid, "message": "Usuario registrado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def login_with_token(id_token: str):
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token["uid"]
        user = auth.get_user(uid)

        return {
            "uid": user.uid,
            "email": user.email,
            "name": user.display_name,
            "token": id_token  # devolver token original si lo necesitas en frontend
        }
    except Exception as e:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")