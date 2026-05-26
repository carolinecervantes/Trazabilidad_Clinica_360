import customtkinter as ctk

from ui.dashboard import pantalla_dashboard
from ui.registrar_evento import pantalla_registrar
from ui.consultar_eventos import pantalla_consultar
from ui.auditoria_view import pantalla_auditoria
from ui.timeline import pantalla_timeline
from ui.alertas import pantalla_alertas
from ui.reportes import pantalla_reportes


class LayoutApp:

    def __init__(self, app, usuario, rol):

        self.app = app
        self.usuario = usuario
        self.rol = rol

        self.current_frame = None

        self.crear_layout()

    # =====================================
    # LAYOUT PRINCIPAL
    # =====================================

    def crear_layout(self):

        # =========================
        # SIDEBAR
        # =========================

        self.sidebar = ctk.CTkFrame(
            self.app,
            width=280,
            fg_color="#0F172A",
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        # =========================
        # LOGO
        # =========================

        logo = ctk.CTkLabel(
            self.sidebar,
            text="Trazabilidad Clínica 360 ",
            font=("Arial", 28, "bold"),
            text_color="#3B82F6"
        )

        logo.pack(pady=(30, 10))

        descripcion = ctk.CTkLabel(
            self.sidebar,
            text="Sistema para trazabilidad\nclínica, quirúrgica\ny hospitalaria",
            justify="left",
            font=("Arial", 18)
        )

        descripcion.pack(
            padx=20,
            pady=(0, 30),
            anchor="w"
        )

        # =========================
        # USUARIO
        # =========================

        usuario_frame = ctk.CTkFrame(
            self.sidebar,
            fg_color="#111827",
            corner_radius=15
        )

        usuario_frame.pack(
            fill="x",
            padx=15,
            pady=10
        )

        usuario_label = ctk.CTkLabel(
            usuario_frame,
            text=f"👤 {self.usuario}\n{self.rol}",
            justify="left",
            font=("Arial", 16)
        )

        usuario_label.pack(
            anchor="w",
            padx=15,
            pady=15
        )

        # =========================
        # MENU
        # =========================

        menu_titulo = ctk.CTkLabel(
            self.sidebar,
            text="MENÚ PRINCIPAL",
            font=("Arial", 14, "bold"),
            text_color="gray"
        )

        menu_titulo.pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        self.crear_boton_menu(
            "🏠 Inicio",
            "dashboard"
        )

        self.crear_boton_menu(
            "🕒 Línea de tiempo",
            "timeline"
        )

        self.crear_boton_menu(
            "🚨 Alertas",
            "alertas"
        )

        self.crear_boton_menu(
            "📄 Reportes",
            "reportes"
        )

        self.crear_boton_menu(
            "➕ Registrar evento",
            "registrar"
        )

        self.crear_boton_menu(
            "🔎 Consultar trazabilidad",
            "consultar"
        )

        self.crear_boton_menu(
            "🛡 Auditoría",
            "auditoria"
        )

        # =========================
        # CONTENIDO DERECHO
        # =========================

        self.right_container = ctk.CTkFrame(
            self.app,
            fg_color="#020617",
            corner_radius=0
        )

        self.right_container.pack(
            side="right",
            expand=True,
            fill="both"
        )

        # =========================
        # NAVBAR
        # =========================

        self.navbar = ctk.CTkFrame(
            self.right_container,
            height=80,
            fg_color="#0F172A",
            corner_radius=0
        )

        self.navbar.pack(
            fill="x"
        )

        self.navbar.pack_propagate(False)

        navbar_title = ctk.CTkLabel(
            self.navbar,
            text="Trazabilidad Clínica 360 ",
            font=("Arial", 22, "bold")
        )

        navbar_title.pack(
            side="left",
            padx=30
        )

        navbar_user = ctk.CTkLabel(
            self.navbar,
            text=f"👤 {self.usuario}",
            font=("Arial", 16)
        )

        navbar_user.pack(
            side="right",
            padx=30
        )

        # =========================
        # CONTENIDO DINAMICO
        # =========================

        self.content = ctk.CTkFrame(
            self.right_container,
            fg_color="#020617"
        )

        self.content.pack(
            expand=True,
            fill="both",
            padx=20,
            pady=20
        )

        self.mostrar_vista("dashboard")

    # =====================================
    # BOTONES MENU
    # =====================================

    def crear_boton_menu(self, texto, vista):

        btn = ctk.CTkButton(
            self.sidebar,
            text=texto,
            anchor="w",
            height=45,
            corner_radius=10,
            fg_color="transparent",
            hover_color="#1E293B",
            font=("Arial", 16),
            command=lambda: self.mostrar_vista(vista)
        )

        btn.pack(
            fill="x",
            padx=15,
            pady=5
        )

    # =====================================
    # CAMBIO DE VISTAS
    # =====================================

    def mostrar_vista(self, vista):

    # =====================================
    # LIMPIAR CONTENEDOR COMPLETAMENTE
    # =====================================

        for widget in self.content.winfo_children():
            widget.destroy()

        self.current_frame = None

        # =====================================
        # CARGAR NUEVA VISTA
        # =====================================

        if vista == "dashboard":

            self.current_frame = pantalla_dashboard(
                self.content
            )

        elif vista == "registrar":

            self.current_frame = pantalla_registrar(
                self.content,
                self.usuario
            )

        elif vista == "consultar":

            self.current_frame = pantalla_consultar(
                self.content
            )

        elif vista == "timeline":

            self.current_frame = pantalla_timeline(
                self.content
            )

        elif vista == "alertas":

            self.current_frame = pantalla_alertas(
                self.content
            )

        elif vista == "reportes":

            self.current_frame = pantalla_reportes(
                self.content
            )

        elif vista == "auditoria":

            self.current_frame = pantalla_auditoria(
                self.content
            )

        # =====================================
        # FORZAR ACTUALIZACION UI
        # =====================================

        if self.current_frame:

            self.current_frame.pack(
                fill="both",
                expand=True
            )

        self.content.update_idletasks()