from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import encuesta_routes, respuesta_routes

app = FastAPI(
    title="API de Sistema Web de Encuestas",
    version="1.0"
)

# Configuración correcta de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://insight-inquire-ui.lovable.app"],  # Origen permitido
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

app.include_router(encuesta_routes.router, prefix="/encuestas", tags=["Encuestas"])
app.include_router(respuesta_routes.router, prefix="/respuestas", tags=["Respuestas"])

@app.get("/")
def read_root():
    return {"message": "API de Encuestas Mockeada (con modelo embebido) en FastAPI"}
