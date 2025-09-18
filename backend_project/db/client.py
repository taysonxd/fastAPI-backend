
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
    
    logger.info(f"Intentando conectar a MongoDB...")
    logger.info(f"URL de MongoDB: {mongodb_url[:50]}...")  # Solo mostrar los primeros 50 caracteres por seguridad
    
    # Configuración optimizada para Vercel
    client_options = {
        'serverSelectionTimeoutMS': 10000,  # 10 segundos
        'connectTimeoutMS': 10000,
        'socketTimeoutMS': 10000,
        'maxPoolSize': 10,
        'minPoolSize': 1,
        'maxIdleTimeMS': 30000,
        'retryWrites': True,
        'retryReads': True,
        'directConnection': False,  # Importante para Vercel
        'tls': True,  # Forzar TLS
        'tlsAllowInvalidCertificates': False,
        'tlsAllowInvalidHostnames': False
    }
    
    # Crear cliente con configuración optimizada
    client = MongoClient(mongodb_url, **client_options)
    
    logger.info("Cliente MongoDB creado, probando conexión...")
    
    # Probar la conexión con timeout más largo
    client.admin.command('ping')
    db_client = client.test
    logger.info("✅ Conexión a MongoDB establecida correctamente")
    
except (ConnectionFailure, ServerSelectionTimeoutError) as e:
    logger.error(f"❌ Error conectando a MongoDB: {e}")
    logger.error(f"Tipo de error: {type(e).__name__}")
    # Crear un cliente mock para desarrollo local
    db_client = None
except Exception as e:
    logger.error(f"❌ Error inesperado: {e}")
    logger.error(f"Tipo de error: {type(e).__name__}")
    db_client = None
