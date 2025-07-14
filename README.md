#🚀 Backend del Sistema Web de Encuestas 🚀
¡Bienvenido al corazón del Sistema Web de Encuestas! Este backend, construido con FastAPI, es el motor que impulsa todas las funcionalidades, desde la gestión de usuarios hasta la creación de dashboards dinámicos. Usamos Firestore como nuestra base de datos, garantizando flexibilidad y escalabilidad.

✨ Características Principales
Autenticación Robusta: Implementamos la autenticación de usuarios a través de Firebase Authentication, asegurando un registro e inicio de sesión seguros.

Gestión Integral de Encuestas: Realiza operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en encuestas. También puedes obtener encuestas específicas, todas las encuestas de un usuario o acceder a encuestas públicas.

Manejo Eficiente de Respuestas: Registra respuestas de usuarios autenticados y también permite respuestas anónimas para encuestas públicas. Podrás consultar respuestas por encuesta o ver todas las respuestas de un usuario, además de obtener resúmenes detallados de los resultados.

Dashboards Personalizables: Crea y visualiza dashboards interactivos para analizar los resultados de tus encuestas. Configura widgets con diferentes tipos de gráficos para una mejor comprensión de los datos.

Base de Datos NoSQL: Aprovechamos el poder de Firestore para un almacenamiento de datos ágil y sin problemas.

Documentación Interactiva: Gracias a FastAPI, la API cuenta con una documentación Swagger UI autogenerada, perfecta para explorar y probar los endpoints de manera sencilla.

#🔗 Endpoints Clave de la API
Aquí tienes un vistazo rápido a algunos de los endpoints más importantes:

#🔐 Autenticación
POST /auth/register: Registra un nuevo usuario con email y contraseña.

POST /auth/login: Inicia sesión validando un token de Firebase.

#📝 Encuestas
GET /encuestas/: Obtiene todas las encuestas del usuario autenticado.

POST /encuestas/: Crea una nueva encuesta.

GET /encuestas/{idEncuesta}: Obtiene una encuesta por su ID.

PUT /encuestas/{idEncuesta}: Actualiza una encuesta existente.

DELETE /encuestas/{idEncuesta}: Elimina una encuesta.

GET /encuestas/{idEncuesta}/public: Accede a una encuesta pública (sin autenticación).

GET /encuestas/{idEncuesta}/resultados/resumen: Obtiene un resumen estadístico de los resultados de una encuesta.

#📊 Respuestas
GET /respuestas/: Consulta todas las respuestas del usuario autenticado.

POST /respuestas/: Envía una nueva respuesta a una encuesta (requiere autenticación).

GET /respuestas/encuesta/{idEncuesta}: Obtiene las respuestas de una encuesta específica para el usuario autenticado.

POST /respuestas/encuesta/{idEncuesta}/public: Registra una respuesta a una encuesta pública (anónima).

GET /respuestas/encuesta/{idEncuesta}/public/items: Accede a todas las respuestas anónimas de una encuesta pública.

#📈 Dashboards
POST /dashboards: Crea un nuevo dashboard personalizado.

GET /dashboards/{dashboard_id}: Obtiene un dashboard por su ID.

#📦 Esquemas de Datos
La API utiliza modelos de datos claros y bien definidos para cada interacción:

RegisterUser: Para el registro (email, password, name).

FirebaseToken: Para el inicio de sesión (token).

Encuesta-Input: Para crear/actualizar encuestas (incluye idEncuesta, idPersona, nombre, estadoEncuesta, estadoLogico, fechaCreacion, fechaModificacion, preguntas).

Encuesta-Output: Representación pública de una encuesta (idEncuesta, titulo, preguntas con opciones).

Pregunta-Input: Define una pregunta de encuesta (idPregunta, nombre, texto, tipo, items para selección).

Pregunta-Output: Pregunta para encuestas públicas (idPregunta, texto, tipo, opciones).

models__respuesta_model__Respuesta: Para respuestas autenticadas (idRespuesta, idEncuesta, idPersona, respuestas - lista de RespuestaPregunta, fechaRespuesta).

models__respuesta_model__RespuestaPregunta: Detalle de una respuesta a una pregunta (idPregunta, idItem).

models__schemas__Respuesta: Estructura para respuestas públicas (lista de respuestas tipo models__schemas__RespuestaPregunta).

models__schemas__RespuestaPregunta: Detalle de una respuesta pública (preguntaId, valor).

DashboardModel: Para crear dashboards (usuarioId, encuestaId, widgets, y opcionales dashboardId, nombre).

WidgetConfig: Configuración de un widget de dashboard (preguntaId, tipoGrafico, configuracion).

#🛠️ Instalación y Configuración Local
Sigue estos sencillos pasos para poner en marcha el backend en tu máquina:

Clona el Repositorio:

Bash

git clone https://github.com/miyofrank/backend_survey.git
cd backend_survey
Crea y Activa un Entorno Virtual:
Es una buena práctica para gestionar las dependencias del proyecto.

Bash

python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
Instala las Dependencias:
Asegúrate de que tu proyecto tenga un archivo requirements.txt con todas las bibliotecas necesarias (FastAPI, Uvicorn, firebase-admin, etc.).

Bash

pip install -r requirements.txt
Configuración de Firebase:

Crea un Proyecto en Firebase: Dirígete a la Firebase Console y crea un nuevo proyecto.

Genera una Clave de Cuenta de Servicio: En tu proyecto de Firebase, ve a Configuración del proyecto > Cuentas de servicio. Haz clic en "Generar nueva clave privada" y descarga el archivo JSON.

Guarda el Archivo de Credenciales: Coloca este archivo JSON en una ubicación segura en tu máquina.

Configura la Variable de Entorno: Establece la variable de entorno GOOGLE_APPLICATION_CREDENTIALS para que apunte a la ruta de tu archivo JSON de credenciales. Importante: ¡No subas este archivo a tu repositorio público!

Bash

# Ejemplo en Windows (reemplaza la ruta):
set GOOGLE_APPLICATION_CREDENTIALS="C:\Users\TuUsuario\Documents\tu-proyecto-firebase-adminsdk.json"
# Ejemplo en macOS/Linux (reemplaza la ruta):
export GOOGLE_APPLICATION_CREDENTIALS="/home/tu_usuario/documentos/tu-proyecto-firebase-adminsdk.json"
Ejecuta la Aplicación:
Una vez que todo esté configurado, puedes iniciar el servidor FastAPI.

Bash

uvicorn main:app --reload
El backend estará accesible en http://127.0.0.1:8000.

Accede a la Documentación Interactiva:
Visita http://127.0.0.1:8000/docs en tu navegador para interactuar con la API a través de Swagger UI.

🔑 Uso de la API
Para la mayoría de los endpoints protegidos, necesitarás un token JWT. Este token se obtiene después de un inicio de sesión exitoso mediante el endpoint /auth/login, al enviar un token de autenticación de Firebase
