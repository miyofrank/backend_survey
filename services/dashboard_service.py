from firebase import firebase_init
from models.dashboard_model import DashboardModel

db = firebase_init.db

def guardar_dashboard(data: DashboardModel):
    dashboard_data = data.dict()
    ref = db.collection("dashboards").document()
    dashboard_data["dashboardId"] = ref.id
    ref.set(dashboard_data)
    return dashboard_data

def obtener_dashboard(dashboard_id: str):
    ref = db.collection("dashboards").document(dashboard_id)
    doc = ref.get()
    if doc.exists:
        return doc.to_dict()
    return None
