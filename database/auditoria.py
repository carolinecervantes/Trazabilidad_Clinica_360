from database.conexion import conectar
from datetime import datetime


def registrar_auditoria(usuario, accion):

    conexion = conectar()
    cursor = conexion.cursor()

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO auditoria(
        usuario,
        accion,
        fecha
    )
    VALUES (?, ?, ?)
    """, (
        usuario,
        accion,
        fecha
    ))

    conexion.commit()
    conexion.close()