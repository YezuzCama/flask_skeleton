# Streamlit Task Manager - Aplicación de Gestión de Tareas

Una aplicación web profesional construida con Streamlit para gestionar listas de tareas (To-Do list) con una interfaz visual atractiva y colores profesionales.

## Descripción

Esta es una aplicación web moderna y visualmente atractiva que permite a los usuarios:
- **Agregar** nuevas tareas a una lista con validación
- **Marcar** tareas como completadas/incompletas con casillas de verificación
- **Visualizar** todas las tareas con su estado actual y diseño profesional
- **Experiencia** mejorada con efectos hover, sombras y transiciones suaves

Las tareas se almacenan en la sesión de Streamlit (no persistentes entre reinicios del servidor).

## Características

- **Interfaz profesional** con paleta de colores azul moderna
- **Diseño responsivo** que se adapta a diferentes tamaños de pantalla
- **Validación de entrada** para evitar tareas vacías
- **Feedback visual** con mensajes de éxito y error
- **Tareas completadas** mostradas con tachado y estilo atenuado
- **Efectos hover** y transiciones suaves en botones y elementos interactivos
- **Header destacado** con icono y tipografía profesional
- **Información de ID** visible para cada tarea
- **Backend** simplificado con estado de sesión de Streamlit

## Requisitos

- Python 3.7+
- Streamlit 1.28.0+

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
    streamlit run app.py
    ```

2. Streamlit abrirá automáticamente tu navegador en:
    ```
    http://localhost:8501
    ```

3. Usa la interfaz para:
    - Agregar nuevas tareas escribiendo en el campo de texto y presionando "Agregar"
    - Marcar tareas como completadas/incompletas haciendo clic en la casilla de verificación
    - Visualizar el estado de todas las tareas con diseño profesional

## Estructura del Proyecto

```
flask_skeleton/
├── app.py                 # Aplicación principal Streamlit
├── requirements.txt       # Dependencias del proyecto
└── README.md             # Este archivo
```

## Arquitectura

### Aplicación Principal (`app.py`)

- **Streamlit App**: Configuración con tema centrado y personalización visual
- **Estado de Sesión**: Manejo de tareas y contador de IDs mediante `st.session_state`
- **Funciones**:
  - `add_task(text)` - Añade una tarea con validación y feedback visual
  - `toggle_task(task_id)` - Alterna el estado de completado de una tarea

### Personalización Visual

- **CSS Customizado**: Estilos profesionales con variables de color azul moderno
- **Componentes Destacados**:
  - Header principal con tamaño y peso de fuente aumentados
  - Tarjetas de tarea con sombras, bordes redondeados y bordes laterales coloreados
  - Efectos hover y transiciones en botones
  - Estilos diferenciados para tareas completadas vs pendientes
  - Campos de entrada con enfoque visual y validación

## Notas

- Las tareas se almacenan en la sesión de Streamlit, por lo que se perderán al reiniciar la aplicación
- No hay autenticación ni autorización (aplicación de demostración)
- No hay persistencia de datos (sin base de datos)
- Diseñado para desarrollo y demostración - fácil de extender con persistencias

## Licencia

MIT