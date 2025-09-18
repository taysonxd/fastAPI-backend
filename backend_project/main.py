
from fastapi import FastAPI
from routers import users, basic_auth_users, jwt_auth_users, users_db

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(jwt_auth_users.router)
app.include_router(basic_auth_users.router)
app.include_router(users_db.router)  # Comentado temporalmente por problemas de conexión a MongoDB

app.include_router(users.router)

app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/')
async def root():
    return { 'message': 'Hello World!' }

@app.get('/health')
async def health_check():
    """Endpoint para verificar el estado de la aplicación y la base de datos"""
    from db.client import db_client
    import os
    from pymongo import MongoClient
    from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
    
    health_status = {
        "status": "ok",
        "database": "disconnected",
        "mongodb_url_configured": bool(os.getenv('MONGODB_URL')),
        "environment": os.getenv('VERCEL_ENV', 'local'),
        "connection_test": "not_attempted"
    }
    
    # Probar conexión directa para diagnóstico
    mongodb_url = os.getenv('MONGODB_URL', 'mongodb+srv://test:test@cluster0.rqgo5bl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&tls=true')
    
    try:
        # Crear cliente temporal para prueba
        test_client = MongoClient(
            mongodb_url,
            serverSelectionTimeoutMS=3000,
            connectTimeoutMS=3000,
            socketTimeoutMS=3000
        )
        
        # Probar conexión
        test_client.admin.command('ping')
        health_status["database"] = "connected"
        health_status["connection_test"] = "success"
        test_client.close()
        
    except ConnectionFailure as e:
        health_status["database"] = "connection_failure"
        health_status["connection_test"] = f"ConnectionFailure: {str(e)}"
    except ServerSelectionTimeoutError as e:
        health_status["database"] = "timeout"
        health_status["connection_test"] = f"ServerSelectionTimeoutError: {str(e)}"
    except Exception as e:
        health_status["database"] = "error"
        health_status["connection_test"] = f"Error: {str(e)}"
    
    return health_status
