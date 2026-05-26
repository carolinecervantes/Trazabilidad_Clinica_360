# Trazabilidad Clínica 360

## Sistema de Trazabilidad Clínica y Quirúrgica

---

# Descripción

Trazabilidad Clínica 360 es una aplicación desarrollada en Python para la gestión y trazabilidad de eventos clínicos y quirúrgicos.

El sistema permite:

* Registrar eventos clínicos
* Consultar procedimientos
* Realizar seguimiento hospitalario
* Gestionar alertas clínicas
* Visualizar líneas de tiempo
* Mantener auditoría de acciones
* Generar reportes

El proyecto fue desarrollado utilizando Python, CustomTkinter y SQLite.

---

# Tecnologías Utilizadas

* Python 3.11 o superior
* CustomTkinter
* SQLite
* Tkinter

---

# Librerías Necesarias

Instalar las siguientes librerías antes de ejecutar el proyecto:

```bash
pip install customtkinter
pip install pillow
```

---

# Estructura del Proyecto

```txt
TRACE-CLINIC-360/
│
├── database/
│   ├── conexion.py
│   └── models.py
│
├── ui/
│   ├── login.py
│   ├── dashboard.py
│   ├── registrar_evento.py
│   ├── consultar_eventos.py
│   ├── auditoria_view.py
│   ├── timeline.py
│   ├── alertas.py
│   └── reportes.py
│
├── layout.py
├── main.py
└── database.db
```

---

# Cómo Ejecutar el Proyecto

## Paso 1 — Instalar Python

Descargar Python desde:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

Durante la instalación marcar:

```txt
Add Python to PATH
```

---

## Paso 2 — Descargar o Clonar el Proyecto

### Opción A — Descargar ZIP

Descargar el repositorio desde GitHub y extraerlo.

### Opción B — Clonar con Git

```bash
git clone URL_DEL_REPOSITORIO
```

---

## Paso 3 — Abrir el Proyecto

Abrir la carpeta del proyecto en:

* Visual Studio Code
* PyCharm
* Cursor
* cualquier editor compatible con Python

---

## Paso 4 — Instalar Dependencias

Abrir terminal dentro del proyecto y ejecutar:

```bash
pip install customtkinter
pip install pillow
```

---

# Paso 5 — Ejecutar el Sistema

Dentro de la carpeta principal ejecutar:

```bash
python main.py
```

---

# Funcionalidades Principales

## Dashboard Clínico

Visualización de:

* Eventos totales
* Eventos críticos
* Eventos pendientes
* Prioridades urgentes
* Eventos del día

---

## Registro de Eventos

Permite registrar:

* Pacientes
* Procedimientos
* Resultados
* Responsables
* Estados
* Prioridades

---

## Línea de Tiempo

Visualización cronológica de eventos clínicos.

---

## Alertas Clínicas

Generación automática de alertas para:

* Eventos críticos
* Eventos urgentes
* Eventos pendientes

---

## Auditoría

Seguimiento de acciones realizadas dentro del sistema.

---

# Base de Datos

El sistema utiliza SQLite como motor de base de datos local.

La base de datos se genera automáticamente al iniciar el proyecto.

---

# Posibles Mejoras Futuras

* Exportación PDF
* Exportación Excel
* Integración con IA
* Sistema multiusuario
* API REST
* Notificaciones en tiempo real
* Dashboard avanzado

---

# Autor

Proyecto académico desarrollado para gestión y trazabilidad clínica utilizando Python y CustomTkinter.

## integrantes: 
* Integrante 1: Caroline Elena Cervantes Faria
* Integrante 2: Valentina Diaz Pombo
* Integrante 3: Karol Daniela Salas Alvis   
* Integrante 4: Hally Valentina Beleño Julio 
* Integrante 5: Rosario Isabel Laucouture Alarzar 

