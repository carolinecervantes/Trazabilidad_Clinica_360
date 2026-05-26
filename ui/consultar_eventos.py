import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox

from database.conexion import conectar
from database.auditoria import registrar_auditoria


def pantalla_consultar(parent):

    frame = ctk.CTkFrame(parent)
    frame.pack(fill="both", expand=True)

    # =========================
    # TITULO
    # =========================

    titulo = ctk.CTkLabel(
        frame,
        text="Consultar Trazabilidad",
        font=("Arial", 28, "bold")
    )
    titulo.pack(pady=20)

    # =========================
    # FORMULARIO
    # =========================

    form_frame = ctk.CTkFrame(frame)
    form_frame.pack(fill="x", padx=20, pady=10)

    entry_id = ctk.CTkEntry(
        form_frame,
        placeholder_text="ID",
        width=100
    )
    entry_id.grid(row=0, column=0, padx=10, pady=10)

    entry_paciente = ctk.CTkEntry(
        form_frame,
        placeholder_text="Paciente",
        width=200
    )
    entry_paciente.grid(row=0, column=1, padx=10)

    entry_evento = ctk.CTkEntry(
        form_frame,
        placeholder_text="Evento",
        width=200
    )
    entry_evento.grid(row=0, column=2, padx=10)

    entry_responsable = ctk.CTkEntry(
        form_frame,
        placeholder_text="Responsable",
        width=200
    )
    entry_responsable.grid(row=1, column=0, padx=10, pady=10)

    entry_area = ctk.CTkEntry(
        form_frame,
        placeholder_text="Área",
        width=200
    )
    entry_area.grid(row=1, column=1, padx=10)

    entry_resultado = ctk.CTkEntry(
        form_frame,
        placeholder_text="Resultado",
        width=200
    )
    entry_resultado.grid(row=1, column=2, padx=10)

    # =========================
    # TABLA
    # =========================

    columnas = (
        "ID",
        "Paciente",
        "Evento",
        "Responsable",
        "Área",
        "Fecha",
        "Resultado"
    )

    tabla = ttk.Treeview(
        frame,
        columns=columnas,
        show="headings",
        height=15
    )

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=150)

    tabla.pack(fill="both", expand=True, padx=20, pady=20)

    # =========================
    # CARGAR DATOS
    # =========================

    def cargar_datos():

        for fila in tabla.get_children():
            tabla.delete(fila)

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        SELECT
            id,
            paciente,
            tipo_evento,
            responsable,
            area,
            fecha,
            resultado
        FROM eventos
        ORDER BY id DESC
        """)

        registros = cursor.fetchall()

        conexion.close()

        for fila in registros:
            tabla.insert("", "end", values=fila)

    cargar_datos()

    # =========================
    # SELECCIONAR FILA
    # =========================

    def seleccionar_fila(event):

        seleccionado = tabla.focus()

        datos = tabla.item(seleccionado)

        fila = datos["values"]

        if fila:

            entry_id.delete(0, "end")
            entry_id.insert(0, fila[0])

            entry_paciente.delete(0, "end")
            entry_paciente.insert(0, fila[1])

            entry_evento.delete(0, "end")
            entry_evento.insert(0, fila[2])

            entry_responsable.delete(0, "end")
            entry_responsable.insert(0, fila[3])

            entry_area.delete(0, "end")
            entry_area.insert(0, fila[4])

            entry_resultado.delete(0, "end")
            entry_resultado.insert(0, fila[6])

    tabla.bind("<<TreeviewSelect>>", seleccionar_fila)

    # =========================
    # ACTUALIZAR
    # =========================

    def actualizar_evento():

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        UPDATE eventos
        SET
            paciente = ?,
            tipo_evento = ?,
            responsable = ?,
            area = ?,
            resultado = ?
        WHERE id = ?
        """, (
            entry_paciente.get(),
            entry_evento.get(),
            entry_responsable.get(),
            entry_area.get(),
            entry_resultado.get(),
            entry_id.get()
        ))

        conexion.commit()
        conexion.close()

        registrar_auditoria(
            "Sistema",
            f"Actualizó evento ID {entry_id.get()}"
        )

        messagebox.showinfo(
            "Éxito",
            "Evento actualizado"
        )

        cargar_datos()

    # =========================
    # ELIMINAR
    # =========================

    def eliminar_evento():

        confirmacion = messagebox.askyesno(
            "Confirmar",
            "¿Desea eliminar este evento?"
        )

        if not confirmacion:
            return

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        DELETE FROM eventos
        WHERE id = ?
        """, (entry_id.get(),))

        conexion.commit()
        conexion.close()

        registrar_auditoria(
            "Sistema",
            f"Eliminó evento ID {entry_id.get()}"
        )

        messagebox.showinfo(
            "Éxito",
            "Evento eliminado"
        )

        cargar_datos()

    # =========================
    # BOTONES
    # =========================

    botones = ctk.CTkFrame(frame)
    botones.pack(pady=10)

    btn_actualizar = ctk.CTkButton(
        botones,
        text="Actualizar",
        command=actualizar_evento,
        width=180
    )
    btn_actualizar.grid(row=0, column=0, padx=10)

    btn_eliminar = ctk.CTkButton(
        botones,
        text="Eliminar",
        command=eliminar_evento,
        width=180
    )
    btn_eliminar.grid(row=0, column=1, padx=10)

    return frame