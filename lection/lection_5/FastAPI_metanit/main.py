from fastapi import FastAPI, Path, Query, status
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()


@app.get('/')
def read_root():
    return FileResponse('public/index.html')
    # return {'message': 'Hello FastAPI'}
    # html_content = '<h2>Hello FastAPI</h2>'
    # return HTMLResponse(content=html_content)


@app.get('/about/')
def about():
    return {'message': 'о сайте'}


@app.get("/users/{name}/{age}")
def users(name: str = Path(min_length=3, max_length=20), age: int = Path(ge=18, lt=111)):
    return {"name": name, "age": age}


#
#
# @app.get('/user/{id_}/{age}')
# def users(id_: int, age):
#     return {'user_id': id_ + 5, 'user_age': age}
#
#
# @app.get("/users/{phone}")
# def users(phone: str = Path(regex="^\d{11}$")):
#     return {"phone": phone}


# Параметры строки запроса
@app.get("/users/")
def get_model(name: str = Query(min_length=3, max_length=20), age: int | None = Query(default=18, ge=18, lt=111)):
    return {"user_name": name, "user_age": age}


# http://127.0.0.1:8000/users/?name=Tom&age=38


@app.get("/users")
def users(people: list[str] = Query()):
    return {"people": people}


# http://127.0.0.1:8000/users?people=tom&people=Sam


@app.get("/notfound", status_code=status.HTTP_404_NOT_FOUND)
def notfound():
    return {"message": "Resource Not Found"}
