# models/user_model.py (opcional si no lo habías hecho)

from pydantic import BaseModel

class LoginUser(BaseModel):
    email: str
    password: str  # Solo se usa en frontend, no se valida aquí
