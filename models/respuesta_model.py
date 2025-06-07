from pydantic import BaseModel
from typing import List
from datetime import datetime

class RespuestaPregunta(BaseModel):
    idPregunta: str
    idItem: str

class Respuesta(BaseModel):
    idRespuesta: str
    idEncuesta: str
    idPersona: str
    respuestas: List[RespuestaPregunta]
    fechaRespuesta: datetime
