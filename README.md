# 🚀 Backend del Sistema Web de Encuestas

Bienvenido al **Backend del Sistema Web de Encuestas**, desarrollado con **FastAPI** y **Firestore**. Este servicio gestiona desde la autenticación hasta el análisis de resultados, permitiendo crear encuestas dinámicas y visualizar dashboards personalizados.

## ✨ Características Principales

- **🔐 Autenticación Firebase:** Registro y login seguros mediante **Firebase Authentication**.
- **📝 Gestión de Encuestas:** Crea, edita, elimina y consulta encuestas públicas o privadas.
- **📈 Respuestas Públicas y Privadas:** Recoge respuestas anónimas o autenticadas y obtén resúmenes estadísticos.
- **📈 Dashboards Dinámicos:** Crea dashboards personalizados con widgets y gráficos interactivos.
- **🚀 Firestore NoSQL:** Base de datos flexible y escalable.
- **🧽 Documentación Interactiva:** Swagger UI disponible en `/docs`.

---

## 🔗 Endpoints Principales

### 🔐 Autenticación

| Método | Endpoint         | Descripción                      |
| ------ | ---------------- | -------------------------------- |
| POST   | `/auth/register` | Registro de usuario              |
| POST   | `/auth/login`    | Login mediante token de Firebase |

### 📝 Encuestas

| Método | Endpoint                                     | Descripción                      |
| ------ | -------------------------------------------- | -------------------------------- |
| GET    | `/encuestas/`                                | Listado de encuestas del usuario |
| POST   | `/encuestas/`                                | Crear encuesta                   |
| GET    | `/encuestas/{idEncuesta}`                    | Obtener encuesta por ID          |
| PUT    | `/encuestas/{idEncuesta}`                    | Actualizar encuesta              |
| DELETE | `/encuestas/{idEncuesta}`                    | Eliminar encuesta                |
| GET    | `/encuestas/{idEncuesta}/public`             | Ver encuesta pública             |
| GET    | `/encuestas/{idEncuesta}/resultados/resumen` | Resumen estadístico              |

### 📈 Respuestas

| Método | Endpoint                                         | Descripción                      |
| ------ | ------------------------------------------------ | -------------------------------- |
| GET    | `/respuestas/`                                   | Respuestas del usuario           |
| POST   | `/respuestas/`                                   | Enviar respuesta (autenticado)   |
| GET    | `/respuestas/encuesta/{idEncuesta}`              | Respuestas privadas por encuesta |
| POST   | `/respuestas/encuesta/{idEncuesta}/public`       | Responder encuesta pública       |
| GET    | `/respuestas/encuesta/{idEncuesta}/public/items` | Ver respuestas públicas          |

### 📈 Dashboards

| Método | Endpoint                     | Descripción         |
| ------ | ---------------------------- | ------------------- |
| POST   | `/dashboards`                | Crear dashboard     |
| GET    | `/dashboards/{dashboard_id}` | Consultar dashboard |

---

## 🖃️ Esquemas de Datos

### 🔐 Autenticación

- **RegisterUser:** `{ email, password, name }`
- **FirebaseToken:** `{ token }`

### 📝 Encuestas

- **Encuesta-Input:** `{ idEncuesta, idPersona, nombre, estadoEncuesta, estadoLogico, fechaCreacion, preguntas }`
- **Encuesta-Output:** `{ idEncuesta, titulo, preguntas (con opciones) }`

### 📈 Respuestas

- **Respuesta Autenticada:** `{ idRespuesta, idEncuesta, idPersona, respuestas: [RespuestaPregunta], fechaRespuesta }`
- **Respuesta Pública:** `{ respuestas: [ { preguntaId, valor } ] }`

### 📈 Dashboards

- **DashboardModel:** `{ usuarioId, encuestaId, widgets, dashboardId?, nombre? }`
- **WidgetConfig:** `{ preguntaId, tipoGrafico, configuracion }`

---

## 🛠️ Instalación y Configuración Local

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/miyofrank/backend_survey.git
cd backend_survey
```

### 2️⃣ Crear un entorno virtual

```bash
python -m venv venv
# En Windows
.\venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🔧 Configuración de Firebase

1. **Crea un proyecto en **[**Firebase Console**](https://console.firebase.google.com/)**.**

2. **Genera una clave privada:**

   - Ir a **Configuración del Proyecto > Cuentas de servicio > Generar nueva clave privada**.
   - Descarga y guarda el archivo `.json`.

3. **Configura la variable de entorno:**

```bash
# Windows
set GOOGLE_APPLICATION_CREDENTIALS="C:\ruta\a\tu-clave-firebase.json"

# macOS / Linux
export GOOGLE_APPLICATION_CREDENTIALS="/ruta/a/tu-clave-firebase.json"
```

> ⚠️ **Importante:** No subas el archivo de credenciales a tu repositorio.

---

## 🚀 Ejecución local

```bash
uvicorn main:app --reload
```

La API estará disponible en:

- [**http://127.0.0.1:8000**](http://127.0.0.1:8000)
- **Documentación Swagger:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔑 Autenticación

Para acceder a los endpoints protegidos, debes obtener un **JWT** tras iniciar sesión con:

```http
POST /auth/login
```

El token de Firebase se convierte en un JWT válido para las rutas privadas.

---

## 📂 Estructura del Proyecto

```
backend_survey/
🕹️ auth/               # Lógica de autenticación Firebase
🕹️ controllers/        # Lógica de negocio
🕹️ firebase/           # Inicialización de Firestore
🕹️ models/             # Modelos y esquemas de datos
🕹️ routes/             # Rutas de la API
🕹️ services/           # Servicios auxiliares (dashboards, etc)
🕹️ main.py              # Punto de entrada FastAPI
🕹️ README.md           # Este archivo
```

---

## 🧲 Testing

Puedes probar todos los endpoints desde:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📬 Contacto

Desarrollado por **Frank Cruz**\
📧 [miyofrank@gmail.com](mailto\:miyofrank@gmail.com)\
🔗 [GitHub](https://github.com/miyofrank/backend_survey)
Visita http://127.0.0.1:8000/docs en tu navegador para interactuar con la API a través de Swagger UI.

🔑 Uso de la API
Para la mayoría de los endpoints protegidos, necesitarás un token JWT. Este token se obtiene después de un inicio de sesión exitoso mediante el endpoint /auth/login, al enviar un token de autenticación de Firebase
