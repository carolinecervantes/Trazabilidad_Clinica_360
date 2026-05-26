import customtkinter as ctk
from tkinter import messagebox

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from database.conexion import conectar


def generar_pdf():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT
        paciente,
        tipo_evento,
        responsable,
        fecha,
        resultado
    FROM eventos
    ORDER BY fecha DESC
    """)

    datos = cursor.fetchall()

    conexion.close()

    documento = SimpleDocTemplate(
        "reporte_clinico.pdf"
    )

    estilos = getSampleStyleSheet()

    elementos = []

    titulo = Paragraph(
        "Trazabilidad Clínica 360  - REPORTE CLÍNICO",
        estilos["Title"]
    )

    elementos.append(titulo)
    elementos.append(Spacer(1, 20))

    for evento in datos:

        paciente, tipo, responsable, fecha, resultado = evento

        texto = f"""
        <b>Paciente:</b> {paciente}<br/>
        <b>Evento:</b> {tipo}<br/>
        <b>Responsable:</b> {responsable}<br/>
        <b>Fecha:</b> {fecha}<br/>
        <b>Resultado:</b> {resultado}<br/><br/>
        """

        parrafo = Paragraph(
            texto,
            estilos["BodyText"]
        )

        elementos.append(parrafo)
        elementos.append(Spacer(1, 15))

    documento.build(elementos)

    messagebox.showinfo(
        "Reporte generado",
        "PDF generado correctamente"
    )


def pantalla_reportes(parent):

    frame = ctk.CTkFrame(
        parent,
        fg_color="#020617"
    )

    frame.pack(
        fill="both",
        expand=True
    )

    titulo = ctk.CTkLabel(
        frame,
        text="Reportes Clínicos",
        font=("Arial", 32, "bold")
    )

    titulo.pack(
        pady=40
    )

    descripcion = ctk.CTkLabel(
        frame,
        text="""
Genere reportes PDF del sistema:

• Eventos clínicos
• Procedimientos
• Auditoría
• Trazabilidad quirúrgica
""",
        justify="left",
        font=("Arial", 18)
    )

    descripcion.pack(
        pady=20
    )

    btn_pdf = ctk.CTkButton(
        frame,
        text="Generar PDF",
        width=250,
        height=50,
        font=("Arial", 18, "bold"),
        command=generar_pdf
    )

    btn_pdf.pack(
        pady=30
    )

    return frame