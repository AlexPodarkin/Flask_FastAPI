from fastapi import FastAPI

import logging

from typing import Optional
from pydantic import BaseModel


FORMAT = '{levelname:<8} - {asctime} - >>> {msg}'
logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get('/')
async def read_root():
    logger.info('Отработал GET запрос.')
    return {'message': 'Hello World'}


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post("/items/")
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}


@app.delete('/items/{item_id}')
async def delete_item(item_id: int):
    logger.info(f'Отработал DELETE запрос для item id = {item_id}')
    return {'item_id': item_id}




# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}
# http://127.0.0.1:8000/items/42?q=text


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return {"skip": skip, "limit": limit}
# http://127.0.0.1:8000/items/ (по умолчанию)
# http://127.0.0.1:8000/items/?skip=10&limit=100


# @app.get("/users/{user_id}/orders/{order_id}")
# async def read_item(user_id: int, order_id: int):
#     # обработка данных
#     return {"user_id": user_id, "order_id": order_id}
# http://127.0.0.1:8000/users/5/orders/15


# ТУТ Я писал от начало лекции
# # @app.get('/items/{item_id}')
# # async def read_item(item_id: int, q: str = None):
# #     logger.info('Отработал GET запрос.')
# #     return {'item_id': item_id, 'q': q}
# #  (GET запрос)вот как можно передать item_id и q, http://127.0.0.1:8000/items/5?q=text
#
#
# # Обработка HTTP-запросов и ответов
# # POST запрос
# @app.post("/items/")
# async def create_item(item: Item):
#     logger.info('Отработал POST запрос.')
#     return item
#
#
# # PUT запрос
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     logger.info(f'Отработал PUT запрос для item id = {item_id}.')
#     return {"item_id": item_id, "item": item}
#
#
# @app.delete('/items/{item_id}')
# async def delete_item(item_id: int):
#     logger.info(f'Отработал DELETE запрос для item id = {item_id}')
#     return {'item_id': item_id}

# для запуска приложения ввести команду:
# uvicorn lection.lection_5.lection.main:app --reload  (если стартовать из корня проекта)
# ОБРАТИ ВНИМАНИЕ ТОЧЕЧНАЯ НАТАЦИЯ, не слеш ! отсутствие разрешения .py у файла 'main'
# либо из этой директории исполняемого файла, командой: uvicorn main:app --reload
# (main название файла app название переменной FastAPI)
