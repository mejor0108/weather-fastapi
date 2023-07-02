# CheckList de creación base de una aplicación WEB

## pasos para la implementacion de la estructura base de una aplicación

- [ ] Crear el entorno virtual  
```bash
$>  python -m venv .
```
- [ ] Activar en entorno 
```bash
$>  source Script/activate
```
- [ ] Instalar los paquetes necesarios 

```bash
$  pip install FastAPI
$  python -m pip install --upgrade pip
$  pip install python-dotenv
$  pip install HTTPX                # Alternativa a Requests
$  pip install pytest 
$  pip install uvicorn[standard]    # servidor ASGI [ alternativo Hypercorn]


$  pip install requests
$  python SQLAlchemy
$  pip install python-dotenv        # permite manejar 
$  pip install mysqlclient          # cliente Mysql 
$  pip install psycopg2             # cliente Postgresql
$  pip install pyodbc               # cliente SQLServer necesita ODBC
$  pip install redis                # cliente Redis
$  pip install pymongo              # cliente mongoDB
```

- [ ] Crear las carpetas básicas para el proyecto

```bash
$ mkdir <name_project>/<name_app>   # La carpeta raíz del proyecto 
$ cd <name_project>/<name_app>
$ touch main.py                     # Este es el punto de entrada principal de la aplicación FastAPI
$ mkdir api                         # sta carpeta contendrá todos los archivos y carpetas relacionados     
                                    # con la definición de tus rutas y endpoints de la API
$ mkdir models                      # Aquí puedes almacenar todos los modelos de datos o esquemas de
                                    # Pydantic utilizados en tu API
$ mkdir routers                     # Puedes organizar tus rutas y endpoints en archivos separados dentro 
                                    # de esta carpeta para mantener un enfoque modular.
$ mkdir services                    # para almacenar archivos relacionados con la lógica de negocio o 
                                    # servicios utilizados por tus endpoints de la API
$ mkdir utils                       # para almacenar archivos de utilidades o funciones auxiliares que 
    	                            # puedas necesitar en tu proyecto.
$ mkdir tests                       # organizar tus archivos de prueba dentro de esta carpeta.


```
- [ ] En main.py incorporamos el código base
```py
from typing import Union

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/api/v1/health")
async def health_check():
    return JSONResponse({"status":"ok"})


@app.get("/api/v1/")
async def read_root():
    return {"Hello": "World"}


```