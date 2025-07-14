from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import encuesta_routes, respuesta_routes, auth_routes  # 👈 Agregado
from routes.public import router as public_router
from routes.dashboard_routes import router as dashboard_router
from routes.public import router as public_resp_router

app = FastAPI(
    title="API de Sistema Web de Encuestas",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])  # 👈 Nuevo
app.include_router(encuesta_routes.router, prefix="/encuestas", tags=["Encuestas"])
app.include_router(respuesta_routes.router, prefix="/respuestas", tags=["Respuestas"])
app.include_router(public_router, tags=["Público"])
app.include_router(public_resp_router)
app.include_router(dashboard_router, tags=["Dashboards"])

@app.get("/")
def read_root():
    return {"message": "Backend de encuestas"}



