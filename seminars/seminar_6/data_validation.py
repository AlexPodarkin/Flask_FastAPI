from fastapi import FastAPI, Path, Query

app = FastAPI()

# # Path — это класс, который используется для работы с параметрами пути
# # (path parameters) в URL и проверки данных. Он позволяет определять параметры
# # пути, которые будут передаваться в URL, а также задавать для них ограничения на
# # тип данных и значения.


@app.get("/items/{item_id}")
async def item(item_id: int = Path(..., ge=1), q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/read/{item_id}")
async def read_item(item_id: int = Path(..., title="The ID of the item"), q: str = None):
    return {"item_id": item_id, "q": q}


# Query — это класс, который используется для работы с параметрами запроса
# и проверки строк. Он позволяет определять параметры запроса, которые будут
# передаваться в URL, а также задавать для них ограничения на тип данных и
# значения.

@app.get("/it/")
async def read_items(q: str = Query(None, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Spam"}, {"item_id": "Eggs"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Spam"}, {"item_id": "Eggs"}]}
    if q:
        results.update({"q": q})
    return results


# На самом деле Query, Path, Field и другие фильтры создают объекты подклассов
# общего класса Param, который сам является подклассом класса FieldInfo из модуля
# Pydantic. Все они возвращают объекты подкласса FieldInfo.

# Как результат Field работает так же Query, как Path, имеет все те же параметры и т.д.
# Важно лишь выбрать нужную в текущей реализации функцию
