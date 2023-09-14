from pathlib import PurePath, Path
from flask import Flask, url_for, render_template, request, abort, redirect, flash
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


@app.route('/')
def index():
    return 'Hi'

# Знакомство с flash
# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     if request.method == 'POST':
#         # Обработка данных формы
#         flash('Форма успешно отправлена!', 'success')
#         return redirect(url_for('form'))
#     return render_template('flash_form.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run()
