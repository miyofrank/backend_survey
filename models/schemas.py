from pydantic import BaseModel
from typing import List, Optional, Union

class Opcion(BaseModel):
    texto: str

class Pregunta(BaseModel):
    id: str
    texto: str
    tipo: str
    opciones: Optional[List[Opcion]] = []

class Encuesta(BaseModel):
    id: str
    titulo: str
    preguntas: List[Pregunta]

class RespuestaPregunta(BaseModel):
    preguntaId: str
    valor: Union[str, int, List[str]]

class Respuesta(BaseModel):
    respuestas: List[RespuestaPregunta]