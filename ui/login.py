import customtkinter as ctk
from tkinter import messagebox
from database.conexion import conectar


def pantalla_login(app, callback_login):

    frame = ctk.CTkFrame(app)
    frame.pack(fill="both", expand=True)

    titulo = ctk.CTkLabel(
        frame,
        text="Trazabilidad Clínica 360 ",
        font=("Arial", 34, "bold")
    )
    titulo.pack(pady=50)

    subtitulo = ctk.CTkLabel(
        frame,
        text="Inicio de Sesión",
        font=("Arial", 24)
    )
    subtitulo.pack(pady=10)

    entry_usuario = ctk.CTkEntry(
        frame,
        placeholder_text="Usuario",
        width=350
    )
    entry_usuario.pack(pady=10)

    entry_password = ctk.CTkEntry(
        frame,
        placeholder_text="Contraseña",
        show="*",
        width=350
    )
    entry_password.pack(pady=10)

    def iniciar_sesion():

        usuario = entry_usuario.get()
        password = entry_password.get()

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        SELECT nombre, rol
        FROM usuarios
        WHERE usuario = ?
        AND password = ?
        """, (usuario, password))

        resultado = cursor.fetchone()

        conexion.close()

        if resultado:

            nombre = resultado[0]
            rol = resultado[1]

            callback_login(nombre, rol)

        else:
            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos"
            )

    btn_login = ctk.CTkButton(
        frame,
        text="Iniciar Sesión",
        command=iniciar_sesion,
        width=250,
        height=45
    )
    btn_login.pack(pady=30)

    return frame