# Flask Skeleton - Aplicación de Gestión de Tareas

Una aplicación web simple construida con Flask para gestionar listas de tareas (To-Do list).

## Descripción

Esta es una aplicación web minimalista que permite a los usuarios:
- **Agregar** nuevas tareas a una lista
- **Marcar** tareas como completadas
- **Visualizar** todas las tareas con su estado actual

Las tareas se almacenan en memoria (no persistentes entre reinicios del servidor).

## Características

- Interfaz web sencilla y funcional
- Validación de entrada de texto vacía
- Tareas marcadas con tachado visual cuando están completadas
- Backend en Flask con rutas RESTful
- Frontend con HTML + Jinja2 templates

## Requisitos

- Python 3.7+
- Flask 3.0.0+

## Instalación

1. Clona o navega al directorio del proyecto:

   ```bash
   cd flask_skeleton
   ```

2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta la aplicación:

   ```bash
   python app.py
   ```

2. Abre tu navegador y navega a:

   ```
   http://127.0.0.1:5000/
   ```

3. Usa la interfaz para:
   - Agregar nuevas tareas escribiendo en el campo de texto y presionando "Agregar"
   - Marcar tareas como completadas presionando el botón "Completar"

## Estructura del Proyecto

```
flask_skeleton/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias del proyecto
├── templates/
│   └── index.html        # Template HTML principal
└── README.md             # Este archivo
```

## Arquitectura

### Backend (`app.py`)

- **Flask App**: Configuración básica con modo debug habilitado
- **Rutas**:
  - `GET /` - Muestra la lista de tareas
  - `POST /` - Procesa acciones (agregar/completar tareas)
- **Funciones**:
  - `agregar_tarea(texto)` - Añade una tarea y devuelve su ID
  - `completar_tarea(id)` - Marca una tarea como completada

### Frontend (`templates/index.html`)

- Template Jinja2 que renderiza la lista de tareas
- Formulario para agregar nuevas tareas
- Botones para completar tareas existentes
- Visualización condicional (tachado) para tareas completadas

## Notas

- Las tareas se almacenan en memoria, por lo que se perderán al reiniciar el servidor
- No hay autenticación ni autorización (aplicación de demostración)
- No hay persistencia de datos (sin base de datos)
- El modo debug está habilitado - **no usar en producción**

## Licencia

MIT
