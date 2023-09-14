from pathlib import PurePath, Path
from flask import Flask, url_for, render_template, request, abort, redirect, flash, make_response
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)
# Небольшое отступление. Чтобы не получать ошибки вида при работе с сессией
# RuntimeError: The session is unavailable because no secret key
# was set. Set the secret_key on the application to something
# unique and secret.
# необходимо добавить в Flask приложение секретный ключ.
# Простейший способ генерации такого ключа, выполнить следующие пару строк
# кода
# >>> import secrets
# >>> secrets.token_hex()
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'

# знакомство с cookie
# @app.route('/')
# def index():
#     # устанавливаем cookie
#     response = make_response("Cookie установлен")
#     response.set_cookie('username', 'admin')
#     return response
#
#
# @app.route('/getcookie/')
# def get_cookies():
#     # получаем значение cookie
#     name = request.cookies.get('username')
#     return f"Значение cookie: {name}"


@app.route('/')
def index():
    context = {
        'title': 'Главная',
        'name': 'Харитон'
    }
    response = make_response(render_template('main.html', **context))
    response.headers['new_head'] = 'New value'
    response.set_cookie('username', context['name'])
    return response


if __name__ == '__main__':
    app.run()
