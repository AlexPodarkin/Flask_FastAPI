from pathlib import PurePath, Path
from flask import Flask, url_for, render_template, request, abort
from markupsafe import escape
from werkzeug.utils import secure_filename
# 39:04
app = Flask(__name__)


@app.route('/')
def index():
    return '<h2>Hi !</h2>'


@app.route('/blog/<int:id_>')
def get_blog_by_id(id_):
    result = None
    if result is None:
        abort(404)


@app.errorhandler(500)
def page_not_found(e):
    app.logger.error(e)
    context = {
        'title': 'Ошибка сервера',
        'url': request.base_url,
    }
    return render_template('500.html', **context), 500
# Функция abort() также используется для обработки ошибок в Flask. Она позволяет
# вызвать ошибку и передать ей код ошибки и сообщение для отображения
# пользователю.
# Например, чтобы вызвать ошибку 404 с сообщением "Страница не найдена",
# необходимо использовать функцию abort():


@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


if __name__ == '__main__':
    app.run(debug=True)
