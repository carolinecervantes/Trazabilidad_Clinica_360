from database.conexion import conectar

def crear_tablas():

    conexion = conectar()
    cursor = conexion.cursor()

    # =========================
    # TABLA EVENTOS
    # =========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS eventos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente TEXT NOT NULL,
        tipo_evento TEXT NOT NULL,
        descripcion TEXT,
        responsable TEXT,
        area TEXT,
        fecha TEXT,
        resultado TEXT,
        estado TEXT,
        prioridad TEXT
    )
    """)

    # =========================
    # TABLA USUARIOS
    # =========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        usuario TEXT UNIQUE,
        password TEXT,
        rol TEXT
    )
    """)

    # =========================
    # TABLA AUDITORIA
    # =========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS auditoria(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT,
        accion TEXT,
        fecha TEXT
    )
    """)

    # =========================
    # CREAR ADMIN POR DEFECTO
    # =========================

    cursor.execute("""
    SELECT * FROM usuarios
    WHERE usuario = 'admin'
    """)

    admin = cursor.fetchone()

    if not admin:

        cursor.execute("""
        INSERT INTO usuarios(
            nombre,
            usuario,
            password,
            rol
        )
        VALUES (?, ?, ?, ?)
        """, (
            "Administrador",
            "admin",
            "1234",
            "Administrador"
        ))

    conexion.commit()
    conexion.close()