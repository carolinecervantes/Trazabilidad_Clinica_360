import customtkinter as ctk
from database.conexion import conectar


def obtener_eventos():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT
        fecha,
        paciente,
        tipo_evento,
        responsable,
        resultado
    FROM eventos
    ORDER BY fecha DESC
    """)

    datos = cursor.fetchall()

    conexion.close()

    return datos


class TimelineView(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="#020617"
        )

        self.pack(
            fill="both",
            expand=True
        )

        self.crear_timeline()

    # =====================================
    # TIMELINE
    # =====================================

    def crear_timeline(self):

        titulo = ctk.CTkLabel(
            self,
            text="Línea de Tiempo Clínica",
            font=("Arial", 30, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=20,
            pady=20
        )

        # =====================================
        # SCROLL
        # =====================================

        self.scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )

        self.scroll.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        eventos = obtener_eventos()

        if not eventos:

            vacio = ctk.CTkLabel(
                self.scroll,
                text="No existen eventos registrados",
                font=("Arial", 18)
            )

            vacio.pack(pady=50)

            return

        for evento in eventos:

            self.crear_evento(evento)

    # =====================================
    # ITEM
    # =====================================

    def crear_evento(self, evento):

        fecha, paciente, tipo, responsable, resultado = evento

        card = ctk.CTkFrame(
            self.scroll,
            fg_color="#111827",
            corner_radius=15
        )

        card.pack(
            fill="x",
            padx=15,
            pady=10
        )

        fecha_label = ctk.CTkLabel(
            card,
            text=fecha,
            text_color="#60A5FA",
            font=("Arial", 13)
        )

        fecha_label.pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        titulo = ctk.CTkLabel(
            card,
            text=f"{tipo} - {paciente}",
            font=("Arial", 20, "bold")
        )

        titulo.pack(
            anchor="w",
            padx=20
        )

        detalle = ctk.CTkLabel(
            card,
            text=f"""
Responsable: {responsable}

Resultado: {resultado}
""",
            justify="left",
            font=("Arial", 15)
        )

        detalle.pack(
            anchor="w",
            padx=20,
            pady=(10, 20)
        )


# =====================================
# FUNCION PRINCIPAL
# =====================================

def pantalla_timeline(parent):

    return TimelineView(parent)