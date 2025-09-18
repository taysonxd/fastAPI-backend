
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
    
    health_status = {
        "status": "ok",
        "database": "disconnected",
        "mongodb_url_configured": bool(os.getenv('MONGODB_URL')),
        "environment": os.getenv('VERCEL_ENV', 'local')
    }
    
    if db_client is not None:
        try:
            # Probar la conexión
            db_client.command('ping')
            health_status["database"] = "connected"
        except Exception as e:
            health_status["database"] = f"error: {str(e)}"
    
    return health_status
