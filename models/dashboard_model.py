from pydantic import BaseModel
from typing import List, Optional, Dict

class WidgetConfig(BaseModel):
    preguntaId: str
    tipoGrafico: str  # "barras", "pastel", "tabla", etc.
    configuracion: Optional[Dict] = None

class DashboardModel(BaseModel):
    dashboardId: Optional[str] = None
    usuarioId: str
    encuestaId: str
    widgets: List[WidgetConfig]
    nombre: Optional[str] = "Mi Dashboard"
