from flask import Flask, render_template, request, redirect, flash, url_for

# Задание №5
# 📌 Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# 📌 При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.

application = Flask(__name__)
application.secret_key = b'b0ee5a2c6515091072087d57c6693be951cd9fc4629e5e66324c8c33331b5768'


@application.route('/')
def index():
    return 'Hi'
    # redirect(url_for('math_get'))


@application.get('/math/')
def math_get():
    return render_template('math.html')


@application.post('/math/')
def math_post():
    res = 0
    num1 = int(request.form.get('num1'))
    num2 = int(request.form.get('num2'))
    operation = request.form.get('operation')
    if operation == 'plus':
        res = num1 + num2
    elif operation == 'minus':
        res = num1 - num2
    elif operation == 'mult':
        res = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'На ноль делить нельзя!'
        res = num1 / num2
    return str(res)


if __name__ == '__main__':
    application.run(debug=True)
