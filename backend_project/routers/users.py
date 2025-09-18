
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={
        404: {'message': 'No encontrado' }
    }
)

class User(BaseModel):
    id: int
    name: str
    lastname: str
    web: str
    age: int

users_list = [
    User(id = 1, name = 'John', lastname = 'Doe', web = 'https://webJohn.com', age = 36 ),
    User(id = 2, name = 'Mark', lastname = 'Town', web = 'https://webMark.com', age = 32 ),
    User(id = 3, name = 'Charles', lastname = 'Cheez', web = 'https://webCharles.com', age = 33 ),
]

@router.get('/')
async def users():
    return users_list

# path
@router.get('/{id}')
async def user_path(id: int = 0):
    return search_user(id)

# query
@router.get('/')
async def user_query(id: int = 0):
    return search_user(id)

@router.post('/', response_model= User , status_code= 201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code = 400, detail = 'El usuario ya existe')   

    users_list.append(user)
    return user

@router.put('/')
async def user(user: User):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return { 'error': 'No se ha actualizado el usuario' }

    return user

@router.delete('/{id}')
async def user(id: int):
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            found = True
            users_list.remove(saved_user)
            break

    if not found:
        return { 'error': 'No se ha eliminado el usuario' }

    return { 'message': 'Usuario eliminado'}

def search_user(id: int):
    users_filter = filter(lambda user: user.id == id, users_list)
    try:
        return list(users_filter)[0]
    except:
        return { 'error': 'No se ha encontrado el usuario' }
