from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from psutil import users

from tabacaria_pj.schemas import Message, UserDB, UserPublic, UserSchema, Userlist
Userlist
app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'ola mundo'}


@app.post('/users/', response_model=UserPublic, status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    user_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_id)
    return user_id

@app.get('/users/', status_code=HTTPStatus.OK, response_model=Userlist)
def read_user():
    return {users: database}

@app.put('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    user_With_id = UserDB(id=user_id, **user.model_dump())
    database[user_id - 1] = user_With_id
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')
    return user_With_id
 
@app.delete('/users/{user_id}', status_code=HTTPStatus.NO_CONTENT)
def delete_user(user_id: int):
    user_With_id = UserDB(id=user_id, **user.model_dump())
    database[user_id - 1] = user_With_id
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')
    return database.pop(user_id - 1)