from fastapi import APIRouter, Depends
from auth.auth_bearer import JWTBearer
from models.dashboard_model import DashboardModel
from controllers import dashboard_controller

router = APIRouter()

@router.post("/dashboards", dependencies=[Depends(JWTBearer())])
def crear_dashboard(data: DashboardModel):
    return dashboard_controller.crear_dashboard_controller(data)

@router.get("/dashboards/{dashboard_id}", dependencies=[Depends(JWTBearer())])
def obtener_dashboard(dashboard_id: str):
    return dashboard_controller.obtener_dashboard_controller(dashboard_id)
