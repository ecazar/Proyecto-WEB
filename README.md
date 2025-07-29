# Proyecto-WEB

# 📚 Bibliotek One - Sistema de Gestión de Biblioteca Universitaria

**Bibliotek One** es una plataforma moderna e inteligente desarrollada con Python y FastAPI para optimizar el sistema de préstamos, devoluciones y gestión de usuarios en bibliotecas universitarias.

---

## 🚀 Problemática y Solución

En muchas bibliotecas universitarias, los sistemas actuales son obsoletos, manuales o poco intuitivos, lo que provoca retrasos en los préstamos, mala gestión de multas y falta de trazabilidad en los libros.

**Bibliotek One** nace como una solución integral, ágil y automatizada que facilita la administración de préstamos y usuarios, garantizando eficiencia, control y trazabilidad en todo momento.

---

## 🎯 Misión y Visión

**Misión**  
Brindar una solución tecnológica de vanguardia que digitalice y simplifique la gestión bibliotecaria en entornos educativos.

**Visión**  
Convertirnos en el sistema de gestión bibliotecaria más confiable y utilizado en instituciones educativas de Latinoamérica.

---

## 🛠️ Funcionalidades Principales

- Registro y gestión de usuarios (profesores y alumnos).
- Control de préstamos y devoluciones de ejemplares.
- Gestión de multas por retrasos.
- Clasificación automática del estado del usuario: Activo, Moroso o Multado.
- Soporte para datos personalizados según tipo de usuario.
- Sistema escalable y listo para futuras integraciones.

---

## 🧪 Tecnología Utilizada

- **Backend:** Python + FastAPI
- **ORM:** SQLAlchemy
- **Base de Datos:** SQLite (desarrollo), PostgreSQL (producción)
- **Documentación:** Swagger UI (auto-generada por FastAPI)
- **Otros:** Pydantic, Uvicorn

---

## 🧱 Arquitectura General

- **Modelos bien estructurados** para representar Usuarios, Préstamos, Multas y Ejemplares.
- **Relaciones claras** entre entidades (Ej. Usuario → Préstamos → Ejemplares).
- **Diseño modular** para permitir futuras mejoras o migración a microservicios.
- **Separación lógica** entre la lógica de dominio, la API REST y la capa de persistencia.

---

## ✅ Beneficios Claves

- Gestión automatizada y confiable.
- Interfaz clara y documentada.
- Escalabilidad y mantenibilidad.
- Control de usuarios y ejemplares.
- Reducción de errores humanos.

---

## 🔮 ¿Qué Sigue?

- Implementación de autenticación y roles de usuario.
- Panel administrativo con interfaz gráfica.
- Soporte para códigos QR y escaneo rápido.
- Notificaciones por correo electrónico.
- Estadísticas e informes de uso.

---

## 💡 Cómo Ejecutar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/bibliotek-one.git
   cd bibliotek-one

   Crea un entorno virtual:


python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
Instala las dependencias:


pip install -r requirements.txt
Ejecuta la aplicación:


uvicorn main:app --reload
Abre tu navegador en:


http://localhost:8000/docs

### Dependencias Backend
Instalar dentro del entorno virtual:
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv

pip install -r requirements.txt

pip install "pydantic<2"
pip install pydantic-settings
pip install python-jose
pip install requests
### Dependencias Frontend
npm install react-router-dom
npm install axios
npm install @mui/material @emotion/react @emotion/styled

## 🧠 Contribuciones
¡Las contribuciones son bienvenidas! Si deseas proponer mejoras, por favor abre un issue o haz un pull request.


``` © Bibliotek One - 2025
Una solución universitaria inteligente para la gestión de bibliotecas.
