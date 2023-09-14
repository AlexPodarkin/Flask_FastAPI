from flask import Flask, url_for, render_template, request
from markupsafe import escape
# 16:03
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi'


@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'уровень = {level}<br>'
    else:
        text = 'ты новичок.<br>'
    return f'{text} {request.args}'


if __name__ == '__main__':
    app.run()

# В первую очередь мы импортировали request — глобальный объект Flask, который
# даёт доступ к локальной информации для каждого контекста запроса. Звучит
# сложно. Если проще, то request содержит данные, которую клиент передаёт на
# сторону сервера.
# Дополнительные параметры собираются в словаре args объекта request. И раз
# перед нами словарь, можно получить значение обратившись к ключу через метод
# get().
# Перейдём по адресу http://127.0.0.1:5000/get/?name=alex&age=13&level=80 и
# увидим следующий вывод:
# уровень 80
# так мы передали значения ?' name=alex & age=13 & level=80' без пробелов !
