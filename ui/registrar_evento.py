import customtkinter as ctk
from tkinter import messagebox
from database.conexion import conectar
from datetime import datetime
from database.auditoria import registrar_auditoria

def pantalla_registrar(parent, usuario_actual):

    frame = ctk.CTkFrame(parent)
    frame.pack(fill="both", expand=True)

    titulo = ctk.CTkLabel(
        frame,
        text="Registrar Evento Clínico",
        font=("Arial", 28, "bold")
    )
    titulo.pack(pady=20)

    # ==================
    # GUARDAR
    # ==================

    def guardar_evento():

        paciente = entry_paciente.get()
        tipo = entry_tipo.get()
        descripcion = textbox_descripcion.get("1.0", "end").strip()
        responsable = usuario_actual
        area = entry_area.get()
        resultado = entry_resultado.get()
        prioridad = combo_prioridad.get()
        estado = combo_estado.get()
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if paciente == "" or tipo == "":
            messagebox.showerror(
                "Error",
                "Complete campos obligatorios"
            )
            return

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
      INSERT INTO eventos(
            paciente,
            tipo_evento,
            descripcion,
            responsable,
            area,
            fecha,
            resultado,
            estado,
            prioridad
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            paciente,
            tipo,
            descripcion,
            responsable,
            area,
            fecha,
            resultado,
            estado,
            prioridad
        ))

        conexion.commit()
        conexion.close()

        registrar_auditoria(
            usuario_actual,
            f"Registró evento de {paciente}"
        )

        messagebox.showinfo(
            "Éxito",
            "Evento guardado"
        )

    # ==================
    # FORM
    # ==================

    entry_paciente = ctk.CTkEntry(
        frame,
        placeholder_text="Paciente",
        width=400
    )
    entry_paciente.pack(pady=10)

    entry_tipo = ctk.CTkEntry(
        frame,
        placeholder_text="Tipo evento",
        width=400
    )
    entry_tipo.pack(pady=10)

    textbox_descripcion = ctk.CTkTextbox(
        frame,
        width=400,
        height=100
    )
    textbox_descripcion.pack(pady=10)

    entry_area = ctk.CTkEntry(
        frame,
        placeholder_text="Área",
        width=400
    )
    entry_area.pack(pady=10)

    entry_resultado = ctk.CTkEntry(
        frame,
        placeholder_text="Resultado",
        width=400
    )
    entry_resultado.pack(pady=10)

    combo_estado = ctk.CTkComboBox(
    frame,
    values=[
        "Pendiente",
        "En proceso",
        "Finalizado",
        "Crítico",
        "Cancelado"
    ],
    width=400
)

    combo_estado.pack(pady=10)
    combo_estado.set("Pendiente")

    combo_prioridad = ctk.CTkComboBox(
        frame,
        values=[
            "Baja",
            "Media",
            "Alta",
            "Urgente"
        ],
        width=400
    )

    combo_prioridad.pack(pady=10)
    combo_prioridad.set("Media")

    btn_guardar = ctk.CTkButton(
        frame,
        text="Guardar Evento",
        command=guardar_evento
    )
    btn_guardar.pack(pady=20)

    return frame