
from pymongo import MongoClient
import os
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Intentar conectar a MongoDB con manejo de errores
try:
    # Usar variable de entorno si está disponible, sino usar la URL por defecto
    mongodb_url = os.getenv('MONGODB_URL', 'mongodb+srv://test:test@cluster0.rqgo5bl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    
    # Crear cliente con timeout
    client = MongoClient(
        mongodb_url,
        serverSelectionTimeoutMS=5000,  # 5 segundos de timeout
        connectTimeoutMS=5000,
        socketTimeoutMS=5000
    )
    
    # Probar la conexión
    client.admin.command('ping')
    db_client = client.test
    logger.info("Conexión a MongoDB establecida correctamente")
    
except (ConnectionFailure, ServerSelectionTimeoutError) as e:
    logger.error(f"Error conectando a MongoDB: {e}")
    # Crear un cliente mock para desarrollo local
    db_client = None
except Exception as e:
    logger.error(f"Error inesperado: {e}")
    db_client = None
