import customtkinter as ctk
from database.conexion import conectar


def obtener_alertas():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            paciente,
            tipo_evento,
            estado,
            prioridad,
            fecha
        FROM eventos
        WHERE estado = 'Crítico'
        OR prioridad = 'Urgente'
        OR estado = 'Pendiente'
        ORDER BY fecha DESC
    """)

    datos = cursor.fetchall()

    conexion.close()

    return datos


def crear_alerta(parent, alerta):

    paciente, evento, estado, prioridad, fecha = alerta

    card = ctk.CTkFrame(
        parent,
        fg_color="#7F1D1D",
        corner_radius=18
    )

    card.pack(
        fill="x",
        padx=20,
        pady=10
    )

    titulo = ctk.CTkLabel(
        card,
        text=f"⚠ {evento}",
        font=("Arial", 22, "bold")
    )

    titulo.pack(
        anchor="w",
        padx=20,
        pady=(15, 5)
    )

    detalle = ctk.CTkLabel(
        card,
        text=f"""
Paciente: {paciente}

Estado: {estado}

Prioridad: {prioridad}

Fecha: {fecha}
""",
        justify="left",
        font=("Arial", 15)
    )

    detalle.pack(
        anchor="w",
        padx=20,
        pady=(0, 20)
    )


def pantalla_alertas(parent):

    frame = ctk.CTkScrollableFrame(
        parent,
        fg_color="#020617"
    )

    frame.pack(
        fill="both",
        expand=True
    )

    titulo = ctk.CTkLabel(
        frame,
        text="Panel de Alertas Clínicas",
        font=("Arial", 30, "bold")
    )

    titulo.pack(
        anchor="w",
        padx=20,
        pady=20
    )

    alertas = obtener_alertas()

    if not alertas:

        vacio = ctk.CTkLabel(
            frame,
            text="No existen alertas activas",
            font=("Arial", 20)
        )

        vacio.pack(pady=50)

    else:

        for alerta in alertas:
            crear_alerta(frame, alerta)

    return frame