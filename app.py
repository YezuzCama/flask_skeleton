import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# Initialize session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'next_id' not in st.session_state:
    st.session_state.next_id = 1


def add_task(text):
    """Add a new task."""
    if not text.strip():
        st.error("El texto de la tarea no puede estar vacío")
        return
    st.session_state.tasks.append({
        "id": st.session_state.next_id,
        "texto": text.strip(),
        "completada": False
    })
    st.session_state.next_id += 1
    st.success("Tarea agregada correctamente")


def toggle_task(task_id):
    """Toggle task completion status."""
    for task in st.session_state.tasks:
        if task["id"] == task_id:
            task["completada"] = not task["completada"]
            break


# Page configuration
st.set_page_config(
    page_title="Gestor de Tareas",
    page_icon="📋",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f2937;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .metrics-container {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin: 1.5rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 1rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        min-width: 150px;
    }
    .metric-card.en-progreso {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    .metric-card.terminadas {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    }
    .metric-card.total {
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
    }
    .metric-number {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.25rem;
    }
    .metric-label {
        font-size: 0.9rem;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .task-item {
        display: flex;
        align-items: center;
        padding: 1rem;
        background-color: #f8fafc;
        border-radius: 0.75rem;
        margin-bottom: 0.75rem;
        border-left: 5px solid #3b82f6;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        transition: all 0.3s;
    }
    .task-item:hover {
        transform: translateX(5px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .task-item.completed {
        opacity: 0.85;
        background-color: #f0fdf4;
        border-left-color: #10b981;
    }
    .task-text {
        flex-grow: 1;
        margin-left: 1rem;
        font-size: 1.15rem;
        font-weight: 500;
        color: #1f2937;
    }
    .task-text.completed {
        text-decoration: line-through;
        color: #64748b;
    }
    .stButton>button {
        background-color: #3b82f6;
        color: white;
        border: none;
        border-radius: 0.75rem;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s;
        box-shadow: 0 2px 4px rgba(59, 122, 246, 0.2);
    }
    .stButton>button:hover {
        background-color: #2563eb;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(59, 122, 246, 0.3);
    }
    .stTextInput>div>div>input {
        border-radius: 0.75rem;
        border: 2px solid #e2e8f0;
        padding: 0.875rem;
        font-size: 1.05rem;
    }
    .stTextInput>div>div>input:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.25);
    }
    .stAlert {
        border-radius: 0.75rem;
    }
    .section-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1f2937;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #e2e8f0;
    }
    .chart-container {
        background: white;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Main app
st.markdown('<h1 class="main-header">📋 Gestor de Tareas</h1>',
            unsafe_allow_html=True)

# Calculate metrics
total_tasks = len(st.session_state.tasks)
completed_tasks = sum(1 for t in st.session_state.tasks if t["completada"])
in_progress_tasks = total_tasks - completed_tasks
completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0

# Display metrics cards
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f'''
        <div class="metric-card total">
            <div class="metric-number">{total_tasks}</div>
            <div class="metric-label">Total</div>
        </div>
    ''', unsafe_allow_html=True)
with col2:
    st.markdown(f'''
        <div class="metric-card en-progreso">
            <div class="metric-number">{in_progress_tasks}</div>
            <div class="metric-label">En Progreso</div>
        </div>
    ''', unsafe_allow_html=True)
with col3:
    st.markdown(f'''
        <div class="metric-card terminadas">
            <div class="metric-number">{completed_tasks}</div>
            <div class="metric-label">Terminadas</div>
        </div>
    ''', unsafe_allow_html=True)

# Progress chart
st.markdown('<div class="chart-container">', unsafe_allow_html=True)
if total_tasks > 0:
    # Donut chart for task completion
    fig = go.Figure(data=[go.Pie(
        labels=['Completadas', 'En Progreso'],
        values=[completed_tasks, in_progress_tasks],
        hole=.5,
        marker_colors=['#10b981', '#f59e0b'],
        textfont_size=16,
        hovertemplate='%{label}: %{value} tareas (%{percent})<extra></extra>'
    )])
    fig.update_layout(
        title_text=f'Progreso de Tareas - {completion_rate:.0f}% Completado',
        title_font_size=20,
        title_x=0.5,
        showlegend=True,
        legend=dict(font_size=14, orientation='h', yanchor='bottom', y=-0.2, xanchor='center', x=0.5),
        margin=dict(t=50, b=40, l=20, r=20),
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("📊 Agrega tu primera tarea para ver el progreso")
st.markdown('</div>', unsafe_allow_html=True)

# Add task form
with st.form(key="add_task_form", clear_on_submit=True):
    col1, col2 = st.columns([4, 1])
    with col1:
        new_task = st.text_input(
            "Nueva tarea",
            placeholder="Escribe una nueva tarea...",
            label_visibility="collapsed"
        )
    with col2:
        submit_button = st.form_submit_button(
            "Agregar",
            use_container_width=True
        )

    if submit_button:
        add_task(new_task)

# Display tasks - Separate sections for En Progreso and Terminadas
col_left, col_right = st.columns(2)

# En Progreso column
with col_left:
    st.markdown('<p class="section-title">📬 En Progreso</p>', unsafe_allow_html=True)
    in_progress = [t for t in st.session_state.tasks if not t["completada"]]
    if not in_progress:
        st.info("📭 No hay tareas en progreso")
    else:
        for i, task in enumerate(in_progress):
            checked = st.checkbox(
                f"  {task['texto']}",
                key=f"inprogress_{task['id']}",
                value=False,
                help=f"ID: {task['id']}"
            )
            if checked:
                toggle_task(task['id'])
                # Rerun to update display
                st.rerun()

# Terminadas column  
with col_right:
    st.markdown('<p class="section-title">✅ Terminadas</p>', unsafe_allow_html=True)
    completed = [t for t in st.session_state.tasks if t["completada"]]
    if not completed:
        st.info("🏆 No hay tareas terminadas aún. ¡Sigue trabajando!")
    else:
        for i, task in enumerate(completed):
            checked = st.checkbox(
                f"  {task['texto']}",
                key=f"completed_{task['id']}",
                value=True,
                help=f"ID: {task['id']} - ¡Tarea completada!"
            )
            if not checked:
                toggle_task(task['id'])
                st.rerun()

# Footer
st.divider()
st.caption("Gestor de Tareas Profesional • Hecho con Streamlit")
