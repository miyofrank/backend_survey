from fastapi import HTTPException
from models.dashboard_model import DashboardModel
from services import dashboard_service

def crear_dashboard_controller(data: DashboardModel):
    return dashboard_service.guardar_dashboard(data)

def obtener_dashboard_controller(dashboard_id: str):
    dashboard = dashboard_service.obtener_dashboard(dashboard_id)
    if not dashboard:
        raise HTTPException(status_code=404, detail="Dashboard no encontrado")
    return dashboard
