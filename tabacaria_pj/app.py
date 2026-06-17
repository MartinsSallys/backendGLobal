from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from typing import List

from tabacaria_pj.schemas import (
    UserDB,
    UserPublic,
    UserSchema,
)

app = FastAPI()

database = []


@app.post('/users/', response_model=UserPublic, status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    user_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_id)
    return user_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=list[UserPublic])
def read_users():
    print(database)
    return database


@app.get('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserDB)
def read_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
   
    return database[user_id - 1]

@app.put('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):

    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found'
        )

    user_With_id = UserDB(id=user_id, **user.model_dump())

    database[user_id - 1] = user_With_id

    return user_With_id

@app.delete('/users/{user_id}', status_code=HTTPStatus.NO_CONTENT)
def delete_user(user_id: int):

    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found'
        )

    return database.pop(user_id - 1)