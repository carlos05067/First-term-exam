# CRUD de Usuarios + Ataque de Fuerza Bruta

API REST con FastAPI que gestiona usuarios y un script que prueba credenciales contra el endpoint `/login`.

## Instalación

pip install fastapi uvicorn sqlmodel requests matplotlib

## Ejecutar la API
### Esta dividida por comentarios para que sea mas facil saber donde empieza y termina cada Endpoints.

uvicorn main:app --reload

Documentación interactiva en: `http://127.0.0.1:8000/docs`

## Endpoints

Endpoints CRUD para usuarios:

POST /users — crear usuario (recibir password en texto).

GET /users — listar usuarios (o paginado).

GET /users/{id} — obtener usuario.

PUT /users/{id} — actualizar (excepto password).

DELETE /users/{id} — eliminar usuario.

POST /login — autenticar usuario (devuelve mensaje simple de login exitoso/login fallido).

## Ejecutar el ataque

### 1. Crear usuario víctima en `/docs`

{ "id": 0, "username": "carlos", "password": "199" }

> La contraseña debe ser corta para que no se demore demasiado.

### 2. Correr el FuerzaBruta (en otra terminal)

python fuerza_bruta.py

El script prueba combinaciones hasta encontrar la contraseña, genera una gráfica, los intentos y el tiempo que le tomo.


