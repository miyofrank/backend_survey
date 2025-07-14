from pydantic import BaseModel
from typing import List, Optional, Union

class Opcion(BaseModel):
    texto: str

class Pregunta(BaseModel):
    idPregunta: str       # ✅ obligatorio
    texto: str
    tipo: str
    opciones: Optional[List[Opcion]] = []

class Encuesta(BaseModel):
    idEncuesta: str       # ✅ antes era `id`
    titulo: str
    preguntas: List[Pregunta]

class RespuestaPregunta(BaseModel):
    preguntaId: str
    valor: Union[str, int, List[str]]

class Respuesta(BaseModel):
    respuestas: List[RespuestaPregunta]