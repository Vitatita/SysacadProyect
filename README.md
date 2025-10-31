# SYSACAD
Repositorio oficial del proyecto 👉 [https://github.com/Vitatita/SysacadProyect.git](https://github.com/Vitatita/SysacadProyect.git)

---

## Descripción

**SYSACAD** es una **API REST** desarrollada en **Python** con el framework **Flask**, construida bajo la filosofía **TDD (Test Driven Development)**.  
El sistema está orientado a la **gestión de universidades, usuarios y tareas**, permitiendo realizar operaciones CRUD (crear, leer, actualizar y eliminar) de forma ágil y estructurada.

La aplicación implementa **migraciones de base de datos**, **separación de entornos** (desarrollo, testing y producción) y configuración mediante **variables de entorno (.env)**, lo que asegura flexibilidad y escalabilidad en su implementación.

---

## Tecnologías Utilizadas

- **Python** → Lenguaje de programación principal.  
- **Flask** → Framework backend para construir la API REST.  
- **HTML5 / CSS3** → Interfaz básica de frontend.  
- **SQLAlchemy** → ORM (Object-Relational Mapping) para la interacción con la base de datos.  
- **PostgreSQL** → Sistema de gestión de base de datos relacional (RDBMS).  
- **Flask-Migrate** → Control y gestión de migraciones de base de datos.  
- **Dotenv (.env)** → Configuración de variables de entorno.  

---

## Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/Vitatita/SysacadProyect.git
cd SysacadProyect
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / Mac:**
```bash
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
*(También puede usarse `./install.sh` si el archivo está disponible.)*

---

### 4. Configurar las bases de datos
Crear tres bases de datos en PostgreSQL:
```
sysacad_dev
sysacad_test
sysacad_prod
```

---

### 5. Configurar variables de entorno
Copiar el archivo de ejemplo y editarlo:
```bash
cp env_example .env
```

---

### 6. Crear migraciones y tablas
```bash
flask db init
flask db migrate
flask db upgrade
```

---

### 7. Seleccionar entorno y ejecutar aplicación
Usar el script `boot.sh` para elegir entorno de ejecución y correr la aplicación:
```bash
./boot.sh development
```
o
```bash
./boot.sh production
```

---

## Uso de la API

Una vez iniciada la aplicación, la API estará disponible en:
```
http://localhost:5000/api/v1
```

### Ejemplos de endpoints

**Obtener todas las universidades:**
```
GET http://localhost:5000/api/v1/universidad
```

**Crear una nueva universidad:**
```
POST http://localhost:5000/api/v1/universidad
```

**Body (JSON):**
```json
{
  "nombre": "Universidad de Ejemplo",
  "sigla": "UEX",
  "tipo": "Privada"
}
```

**Obtener universidad por Hashid:**
```
GET http://localhost:5000/api/v1/universidad/Y10NDOQA72bnPwqK
```

---

## Características Principales

- CRUD completo de universidades.  
- Separación de entornos (desarrollo, testing, producción).  
- Migraciones gestionadas con Flask-Migrate.  
- Variables de entorno configurables (.env).  
- Arquitectura modular y escalable.  
- Desarrollado bajo la filosofía TDD (Desarrollo Guiado por Pruebas).

---

## Autores

- [@victoria_rios](https://github.com/Vitatita)  
- [@ana_gomez](https://github.com/ann4gg)  
- [@carolina_bravo](https://github.com/CNBRAVOCUENCA)

---

© 2025 - Proyecto académico desarrollado en Python / Flask.

