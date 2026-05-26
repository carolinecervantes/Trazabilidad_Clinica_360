import customtkinter as ctk
from tkinter import ttk
from database.conexion import conectar


def pantalla_auditoria(parent):

    frame = ctk.CTkFrame(parent)
    frame.pack(fill="both", expand=True)

    titulo = ctk.CTkLabel(
        frame,
        text="Auditoría del Sistema",
        font=("Arial", 30, "bold")
    )
    titulo.pack(pady=20)

    columnas = (
        "Usuario",
        "Acción",
        "Fecha"
    )

    tabla = ttk.Treeview(
        frame,
        columns=columnas,
        show="headings",
        height=20
    )

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=300)

    tabla.pack(fill="both", expand=True, padx=20, pady=20)

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT
        usuario,
        accion,
        fecha
    FROM auditoria
    ORDER BY id DESC
    """)

    registros = cursor.fetchall()

    conexion.close()

    for fila in registros:
        tabla.insert("", "end", values=fila)

    return frame