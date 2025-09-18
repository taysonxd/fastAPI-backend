
from fastapi import HTTPException, APIRouter, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(
    prefix='/usersdb',
    tags=['usersdb'],
    responses={
        status.HTTP_404_NOT_FOUND: {'message': 'No encontrado' }
    }
)

users_list = []

@router.get('/', response_model=list[User])
async def users():
    if db_client is None:
        raise HTTPException(
            status_code=503, 
            detail="Servicio de base de datos no disponible"
        )
    try:
        return users_schema(db_client.users.find())
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error al obtener usuarios: {str(e)}"
        )

# path
@router.get('/{id}')
async def user_path(id: str):
    if db_client is None:
        raise HTTPException(
            status_code=503, 
            detail="Servicio de base de datos no disponible"
        )
    return search_user('_id', ObjectId(id))

# query
@router.get('/')
async def user_query(id: str):
    if db_client is None:
        raise HTTPException(
            status_code=503, 
            detail="Servicio de base de datos no disponible"
        )
    return search_user('_id', ObjectId(id))

@router.post('/', response_model= User , status_code= 201)
async def user(user: User):        
    if db_client is None:
        raise HTTPException(
            status_code=503, 
            detail="Servicio de base de datos no disponible"
        )
    
    if isinstance(search_user('email', user.email), User):
        raise HTTPException(status_code = 400, detail = 'El usuario ya existe')

    user_dict = dict(user)
    del user_dict['id']

    try:
        id = db_client.users.insert_one(user_dict).inserted_id    
        new_user = user_schema( db_client.users.find_one({ '_id': id }) )
        return User(**new_user)
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error al crear usuario: {str(e)}"
        )

@router.put('/', response_model=User)
async def user(user: User):
    if db_client is None:
        raise HTTPException(
            status_code=503, 
            detail="Servicio de base de datos no disponible"
        )

    user_dict = dict(user)
    del user_dict['id']

    try:
        db_client.users.find_one_and_replace({ '_id': ObjectId(user.id) }, user_dict)
        return search_user('_id', ObjectId(user.id))
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error al actualizar usuario: {str(e)}"
        )

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):
    if db_client is None:
        raise HTTPException(
            status_code=503, 
            detail="Servicio de base de datos no disponible"
        )
    
    try:
        found = db_client.users.find_one_and_delete({ '_id': ObjectId(id) })
        if not found:
            raise HTTPException(
                status_code=404, 
                detail="Usuario no encontrado"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error al eliminar usuario: {str(e)}"
        )

def search_user(field: str, key):
    if db_client is None:
        raise HTTPException(
            status_code=503, 
            detail="Servicio de base de datos no disponible"
        )
    
    try:
        user = db_client.users.find_one({ field: key })
        if user is None:
            raise HTTPException(
                status_code=404, 
                detail="Usuario no encontrado"
            )
        return User.model_validate(user_schema(user))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error al buscar usuario: {str(e)}"
        )
