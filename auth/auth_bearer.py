
from fastapi import Depends, Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from firebase_admin import auth

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            try:
                decoded_token = auth.verify_id_token(credentials.credentials)
                request.state.user = decoded_token  # almacena el usuario autenticado
                return credentials.credentials
            except Exception:
                raise HTTPException(status_code=401, detail="Token inválido o expirado")
        raise HTTPException(status_code=403, detail="No se proporcionaron credenciales")

def get_current_user(token: str = Depends(JWTBearer())):
    """
    Extrae el usuario autenticado desde el token JWT verificado previamente.
    """
    return auth.verify_id_token(token)