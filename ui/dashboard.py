import customtkinter as ctk
from database.conexion import conectar
from tkinter import ttk


def obtener_total_eventos():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM eventos")
    total = cursor.fetchone()[0]

    conexion.close()

    return total


def obtener_eventos_hoy():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM eventos
    WHERE DATE(fecha) = DATE('now')
    """)

    total = cursor.fetchone()[0]

    conexion.close()

    return total

def contar_estado(estado):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM eventos
    WHERE estado = ?
    """, (estado,))

    total = cursor.fetchone()[0]

    conexion.close()

    return total


def contar_prioridad(prioridad):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM eventos
    WHERE prioridad = ?
    """, (prioridad,))

    total = cursor.fetchone()[0]

    conexion.close()

    return total

def obtener_ultimos_eventos():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT
        paciente,
        tipo_evento,
        responsable,
        estado,
        prioridad,
        fecha
    FROM eventos
    ORDER BY id DESC
    LIMIT 10
    """)

    datos = cursor.fetchall()

    conexion.close()

    return datos


def crear_card(parent, titulo, valor, color):

    card = ctk.CTkFrame(
        parent,
        width=280,
        height=150,
        corner_radius=20,
        fg_color=color
    )
    card.pack_propagate(False)

    titulo_label = ctk.CTkLabel(
        card,
        text=titulo,
        font=("Arial", 20, "bold")
    )
    titulo_label.pack(pady=(20, 10))

    valor_label = ctk.CTkLabel(
        card,
        text=str(valor),
        font=("Arial", 42, "bold")
    )
    valor_label.pack()

    return card


def pantalla_dashboard(parent):

    frame = ctk.CTkFrame(parent)

    # =====================
    # TITULO
    # =====================

    titulo = ctk.CTkLabel(
        frame,
        text="Dashboard Clínico",
        font=("Arial", 30, "bold")
    )
    titulo.pack(pady=20)

    # =====================
    # CARDS
    # =====================

    cards_frame = ctk.CTkFrame(frame, fg_color="transparent")
    cards_frame.pack(pady=20)

    total_eventos = obtener_total_eventos()
    eventos_hoy = obtener_eventos_hoy()
    pendientes = contar_estado("Pendiente")
    criticos = contar_estado("Crítico")
    finalizados = contar_estado("Finalizado")
    urgentes = contar_prioridad("Urgente")

    card1 = crear_card(
    cards_frame,
    "Eventos Totales",
    total_eventos,
    "#1E293B"
)

    card1.grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )

    card2 = crear_card(
        cards_frame,
        "Eventos Hoy",
        eventos_hoy,
        "#1D4ED8"
    )

    card2.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )

    card3 = crear_card(
        cards_frame,
        "Pendientes",
        pendientes,
        "#92400E"
    )

    card3.grid(
        row=0,
        column=2,
        padx=10,
        pady=10
    )

    card4 = crear_card(
        cards_frame,
        "Críticos",
        criticos,
        "#7F1D1D"
    )

    card4.grid(
        row=0,
        column=3,
        padx=10,
        pady=10
    )

    card5 = crear_card(
        cards_frame,
        "Urgentes",
        urgentes,
        "#991B1B"
    )

    card5.grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )

    card6 = crear_card(
        cards_frame,
        "Finalizados",
        finalizados,
        "#065F46"
    )

    card6.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )

    # =====================
    # TABLA
    # =====================

    subtitulo = ctk.CTkLabel(
        frame,
        text="Últimos Eventos Registrados",
        font=("Arial", 24, "bold")
    )
    subtitulo.pack(pady=20)

    columnas = (
        "Paciente",
        "Evento",
        "Responsable",
        "Estado",
        "Prioridad",
        "Fecha"
    )

    tabla = ttk.Treeview(
        frame,
        columns=columnas,
        show="headings",
        height=12
    )

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=250)

    tabla.pack(fill="both", expand=True, padx=20, pady=20)

    eventos = obtener_ultimos_eventos()

    for evento in eventos:
        tabla.insert("", "end", values=evento)

    return frame