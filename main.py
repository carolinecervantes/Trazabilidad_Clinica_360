import customtkinter as ctk

from database.models import crear_tablas
from ui.login import pantalla_login
from layout import LayoutApp

# =========================
# CONFIG APP
# =========================

crear_tablas()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()

app.geometry("1600x900")
app.title("Trazabilidad Clínica 360 ")

# =========================
# LOGIN CORRECTO
# =========================

def iniciar_sistema(usuario, rol):

    login_frame.destroy()

    LayoutApp(
        app,
        usuario,
        rol
    )

# =========================
# LOGIN
# =========================

login_frame = pantalla_login(
    app,
    iniciar_sistema
)

app.mainloop()