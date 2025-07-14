from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import encuesta_routes, respuesta_routes, auth_routes
from routes.public import router as public_router
from routes.dashboard_routes import router as dashboard_router

app = FastAPI(
    title="API de Sistema Web de Encuestas",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://insight-inquire-ui.lovable.app"],  # origen de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas de autenticación (Firebase)
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])

# Rutas protegidas de encuestas
app.include_router(encuesta_routes.router, prefix="/encuestas", tags=["Encuestas"])

# Rutas protegidas y públicas de respuestas
# - Dentro de respuesta_routes.py ya están montadas tanto las rutas JWT (/respuestas/...) 
#   como las públicas (/respuestas/encuesta/{idEncuesta}/public).
app.include_router(respuesta_routes.router, prefix="/respuestas", tags=["Respuestas"])

# Rutas públicas de encuestas y respuestas anónimas
app.include_router(public_router, tags=["Público"])

# Rutas de dashboards (protegidas)
app.include_router(dashboard_router, tags=["Dashboards"])

@app.get("/")
def read_root():
    return {"message": "Backend de encuestas"}



