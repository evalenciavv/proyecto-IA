# 🚀 API de Usuarios – FastAPI + PostgreSQL

Esta API permite gestionar usuarios mediante operaciones CRUD, garantizando trazabilidad con un campo de estado (`activo/inactivo`).  
El proyecto está desarrollado con **FastAPI**, **SQLAlchemy (async)** y **PostgreSQL**.

---

## 📘 Especificaciones generales

- **Framework:** FastAPI  
- **Base de datos:** PostgreSQL  
- **ORM:** SQLAlchemy (modo asíncrono)  
- **Formato OpenAPI:** 3.0.3  
- **Documentación automática:**
  - Swagger UI → [`http://localhost:8000/docs`](http://localhost:8000/docs)
  - ReDoc → [`http://localhost:8000/redoc`](http://localhost:8000/redoc)

---

## 🧩 Estructura principal del proyecto

```
src/
├── main.py                # Punto de entrada de la aplicación
├── database.py            # Configuración de conexión a la BD
├── models/
│   └── usuario.py         # Definición del modelo Usuario
├── routers/
│   └── usuario_router.py  # Endpoints CRUD para usuarios
└── schemas/
    └── usuario_schema.py  # Esquemas Pydantic (request/response)
```

---

## ⚙️ Configuración inicial

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/<tu-usuario>/<tu-repo>.git
cd <tu-repo>
```

### 2️⃣ Crear entorno virtual e instalar dependencias

```bash
python -m venv .venv
source .venv/bin/activate    # Mac/Linux
# .venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 3️⃣ Variables de entorno (.env)

Crea un archivo `.env` con tu configuración de PostgreSQL:

```bash
DATABASE_URL=postgresql+asyncpg://usuario:password@localhost:5432/nombre_bd
```

### 4️⃣ Ejecutar el servidor

```bash
uvicorn src.main:app --reload
python -m fastapi dev src/main.py
```

### 5️⃣ Importar base de datos

Desde el motor de postgres o cualquier adminsitrador de base de datos postgres importar el backup llamado proyetco_ia_bd el cual contiene la información de la base de datos, esquemas y tablas requeridas para la ejecución del codigo


### 6️⃣ Probar con colección de postman

Importar y probar con la colección de postman llamada Proyecto IA.postman_collection.json

---

## 📚 Endpoints principales

### 👥 `/usuarios/`

#### **GET** → Listar usuarios activos
Devuelve todos los usuarios cuyo `estado = true`.

**Respuesta 200:**
```json
[
  {
    "id": "uuid",
    "nombre": "string",
    "correo": "user@example.com",
    "estado": true
  }
]
```

---

#### **POST** → Crear un nuevo usuario
**Cuerpo (JSON):**
```json
{
  "nombre": "Juan Pérez",
  "correo": "juan@example.com",
  "contrasena": "123456"
}
```

**Respuesta 200:**
```json
{
  "id": "uuid",
  "nombre": "Juan Pérez",
  "correo": "juan@example.com",
  "estado": true
}
```

---

### 👤 `/usuarios/{usuario_id}`

#### **GET** → Obtener usuario por ID (solo si está activo)
**Respuesta 200:**
```json
{
  "id": "uuid",
  "nombre": "Juan Pérez",
  "correo": "juan@example.com",
  "estado": true
}
```

**Error 404:** si el usuario no existe o está inactivo.

---

#### **PUT** → Actualizar usuario
**Cuerpo (JSON):**
```json
{
  "nombre": "Juan Actualizado",
  "correo": "juan.new@example.com",
  "estado": true
}
```

**Respuesta 200:**
```json
{
  "id": "uuid",
  "nombre": "Juan Actualizado",
  "correo": "juan.new@example.com",
  "estado": true
}
```

---

#### **DELETE** → Eliminar usuario (marcar como inactivo)
No elimina el registro, solo cambia `estado = false`.

**Respuesta 200:**
```json
{
  "message": "Usuario desactivado correctamente"
}
```

---

## 🧠 Esquemas de datos

### 🟢 `UsuarioCreate`
| Campo | Tipo | Requerido | Descripción |
|--------|------|------------|--------------|
| nombre | string | ✅ | Nombre completo del usuario |
| correo | string (email) | ✅ | Correo electrónico único |
| contrasena | string | ✅ | Contraseña (se encripta antes de guardar) |

---

### 🟡 `UsuarioUpdate`
| Campo | Tipo | Requerido | Descripción |
|--------|------|------------|--------------|
| nombre | string | ❌ | Nuevo nombre |
| correo | string (email) | ❌ | Nuevo correo |
| estado | boolean | ❌ | Cambiar estado activo/inactivo |

---

### 🔵 `UsuarioResponse`
| Campo | Tipo | Descripción |
|--------|------|-------------|
| id | uuid | Identificador único |
| nombre | string | Nombre del usuario |
| correo | string | Correo electrónico |
| estado | boolean | Estado actual del usuario |

---

## 🧩 Licencia

Este proyecto está bajo la licencia MIT.  
Puedes usarlo, modificarlo y distribuirlo libremente.

---

## 👨‍💻 Autor

**Esteban Valencia**

**Juan Agurre**

**Anyi Laverde**

---
**FastAPI**.
-