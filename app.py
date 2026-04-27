from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

_tareas: list[dict] = []
_next_id: int = 1


def agregar_tarea(texto: str) -> int:
    """Añade una tarea y devuelve su id."""
    global _next_id
    if not (texto or "").strip():
        raise ValueError("El texto de la tarea no puede estar vacío")
    tid = _next_id
    _next_id += 1
    _tareas.append({"id": tid, "texto": texto.strip(), "completada": False})
    return tid


def completar_tarea(id: int) -> bool:
    """Marca la tarea como completada. Devuelve True si existía."""
    for t in _tareas:
        if t["id"] == id:
            t["completada"] = True
            return True
    return False


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        action = request.form.get("action")
        if action == "agregar":
            try:
                agregar_tarea(request.form.get("texto", ""))
            except ValueError:
                pass
        elif action == "completar":
            try:
                completar_tarea(int(request.form.get("id", "0")))
            except (TypeError, ValueError):
                pass
        return redirect(url_for("index"))
    return render_template("index.html", tareas=_tareas)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
