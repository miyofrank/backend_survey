Backend del Sistema Web de Encuestas
Este es el backend para el Sistema Web de Encuestas, desarrollado con FastAPI y utilizando Firestore como base de datos. Este servicio permite la gestión de usuarios, creación y administración de encuestas, registro de respuestas y visualización de dashboards.

Características
Autenticación de Usuarios: Registro e inicio de sesión a través de Firebase Authentication.

Gestión de Encuestas:

Creación, lectura, actualización y eliminación de encuestas (CRUD).

Obtención de encuestas por ID o todas las encuestas.

Consulta de encuestas públicas.

Gestión de Respuestas:

Registro de respuestas a encuestas por parte de usuarios autenticados.

Registro de respuestas anónimas para encuestas públicas.

Obtención de respuestas por encuesta o todas las respuestas del usuario.

Resumen de resultados de encuestas.

Dashboards:

Creación y obtención de dashboards personalizados para visualizar resultados de encuestas.

Configuración de widgets para diferentes tipos de gráficos.

Base de Datos: Firestore para almacenamiento de datos.

Documentación Interactiva: Generada automáticamente con Swagger UI para probar los endpoints.

Endpoints Principales
Aquí hay un resumen de los endpoints más importantes de la API:

Autenticación
POST /auth/register: Registra un nuevo usuario con email y contraseña.

POST /auth/login: Inicia sesión con un token de Firebase.

Encuestas
GET /encuestas/: Obtiene todas las encuestas del usuario autenticado.

POST /encuestas/: Crea una nueva encuesta.

GET /encuestas/{idEncuesta}: Obtiene una encuesta por su ID.

PUT /encuestas/{idEncuesta}: Actualiza una encuesta existente.

DELETE /encuestas/{idEncuesta}: Elimina una encuesta.

GET /encuestas/{idEncuesta}/public: Obtiene una encuesta pública (sin autenticación).

GET /encuestas/{idEncuesta}/resultados/resumen: Obtiene un resumen de los resultados de una encuesta.

Respuestas
GET /respuestas/: Obtiene todas las respuestas del usuario autenticado.

POST /respuestas/: Crea una nueva respuesta a una encuesta (requiere autenticación).

GET /respuestas/encuesta/{idEncuesta}: Obtiene las respuestas de una encuesta específica para el usuario autenticado.

POST /respuestas/encuesta/{idEncuesta}/public: Registra una respuesta a una encuesta pública.

GET /respuestas/encuesta/{idEncuesta}/public/items: Obtiene todas las respuestas anónimas de una encuesta pública.

Dashboards
POST /dashboards: Crea un nuevo dashboard.

GET /dashboards/{dashboard_id}: Obtiene un dashboard por su ID.

Esquemas de Datos
La API utiliza los siguientes esquemas de datos principales:

RegisterUser: Para el registro de usuarios (email, password, name).

FirebaseToken: Para el inicio de sesión (token).

Encuesta-Input: Para la creación y actualización de encuestas, incluyendo campos como idEncuesta, idPersona, nombre, estadoEncuesta, estadoLogico, fechaCreacion, fechaModificacion, y una lista de preguntas.

Encuesta-Output: Representación de una encuesta pública, con idEncuesta, titulo, y preguntas con sus opciones.

Pregunta-Input: Define una pregunta de encuesta con idPregunta, nombre, texto, tipo, y items (para preguntas de selección).

Pregunta-Output: Representación de una pregunta para encuestas públicas, incluyendo idPregunta, texto, tipo, y opciones.

models__respuesta_model__Respuesta: Estructura para registrar respuestas de usuarios autenticados, con idRespuesta, idEncuesta, idPersona, respuestas (lista de RespuestaPregunta), y fechaRespuesta.

models__respuesta_model__RespuestaPregunta: Detalle de una respuesta a una pregunta (idPregunta, idItem).

models__schemas__Respuesta: Estructura para respuestas públicas, conteniendo una lista de respuestas (tipo models__schemas__RespuestaPregunta).

models__schemas__RespuestaPregunta: Detalle de una respuesta para encuestas públicas (preguntaId, valor).

DashboardModel: Para la creación de dashboards, incluyendo usuarioId, encuestaId, widgets, y opcionalmente dashboardId y nombre.

WidgetConfig: Configuración de un widget dentro de un dashboard (preguntaId, tipoGrafico, configuracion).

Instalación y Configuración Local
Sigue estos pasos para configurar y ejecutar el backend en tu entorno local:

Clonar el Repositorio:

Bash

git clone https://github.com/miyofrank/backend_survey.git
cd backend_survey
Crear y Activar un Entorno Virtual:

Bash

python -m venv venv
# En Windows
.\venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate
Instalar Dependencias:

Bash

pip install -r requirements.txt
(Asegúrate de tener un archivo requirements.txt con todas las dependencias del proyecto, como fastapi, uvicorn, firebase-admin, etc.)

Configuración de Firebase:

Crea un proyecto en Firebase Console.

Genera un archivo de clave de cuenta de servicio (JSON) para tu proyecto de Firebase. Puedes encontrarlo en Configuración del proyecto > Cuentas de servicio.

Guarda este archivo JSON en la raíz de tu proyecto backend o en una ubicación segura.

Configura la variable de entorno GOOGLE_APPLICATION_CREDENTIALS para que apunte a la ruta de tu archivo JSON de credenciales:

Bash

# En Windows
set GOOGLE_APPLICATION_CREDENTIALS="C:\ruta\a\tu\archivo-firebase-adminsdk.json"
# En macOS/Linux
export GOOGLE_APPLICATION_CREDENTIALS="/ruta/a/tu/archivo-firebase-adminsdk.json"
(Reemplaza "C:\ruta\a\tu\archivo-firebase-adminsdk.json" o "/ruta/a/tu/archivo-firebase-adminsdk.json" con la ruta real de tu archivo).

Ejecutar la Aplicación:

Bash

uvicorn main:app --reload
Esto iniciará el servidor de desarrollo de FastAPI. Podrás acceder a la API en http://127.0.0.1:8000.

Acceder a la Documentación Interactiva:
Una vez que la aplicación esté en funcionamiento, puedes acceder a la documentación interactiva de Swagger UI en http://127.0.0.1:8000/docs.

Uso de la API
La API requiere un token JWT para la mayoría de los endpoints protegidos. Este token se obtiene después de un inicio de sesión exitoso a través del endpoint /auth/login, enviando un token de Firebase.

Contribución
Si deseas contribuir a este proyecto, por favor, sigue las directrices de contribución (próximamente).

Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
