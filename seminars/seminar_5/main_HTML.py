from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="./lection/lection_5/lection/templates")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello HTMLResponse</h1>"


@app.get("/message")
async def read_message():
    message = {"message": "Hello JSONResponse"}
    return JSONResponse(content=message, status_code=200)


@app.get("/{name}", response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    return templates.TemplateResponse("item.html", {"request": request, "name": name})


# Swagger: http://127.0.0.1:8000/docs
