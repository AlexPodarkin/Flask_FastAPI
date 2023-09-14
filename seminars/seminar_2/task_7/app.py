# Задание №7
# 📌 Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

from flask import Flask, render_template, request, redirect, flash, url_for, abort

application = Flask(__name__)
application.secret_key = b'b0ee5a2c6515091072087d57c6693be951cd9fc4629e5e66324c8c33331b5768'


@application.route('/')
def index():
    return redirect(url_for('sqrt_get'))


@application.get('/sqrt/')
def sqrt_get():
    return render_template('sqrt.html')


@application.post('/sqrt/')
def sqrt_post():
    num = int(request.form.get('num'))
    return f'<h2>{num} в квадрате = {num ** 2}</h2>'


if __name__ == '__main__':
    application.run(debug=True)
