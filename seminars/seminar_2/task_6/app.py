# Задание №6
# 📌 Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

from flask import Flask, render_template, request, redirect, flash, url_for, abort

application = Flask(__name__)
application.secret_key = b'b0ee5a2c6515091072087d57c6693be951cd9fc4629e5e66324c8c33331b5768'


@application.route('/')
def index():
    return redirect(url_for('checker_get'))


@application.get('/checker/')
def checker_get():
    return render_template('checker.html')


@application.post('/checker/')
def checker_post():
    name = request.form.get('name')
    age = int(request.form.get('age'))
    if age > 17:
        return f'<h2> {name}, Успешный вход ! </h2>'
    else:
        return '<h2>Слишком молод !</h2>'


if __name__ == '__main__':
    application.run(debug=True)
