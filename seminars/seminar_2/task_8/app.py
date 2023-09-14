# Задание №8
# 📌 Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!"

from flask import Flask, render_template, request, redirect, flash, url_for

application = Flask(__name__)
application.secret_key = b'b0ee5a2c6515091072087d57c6693be951cd9fc4629e5e66324c8c33331b5768'


@application.route('/')
def index():
    return redirect(url_for('flash_form'))


@application.route('/flash_form/', methods=['POST', 'GET'])
def flash_form():
    if request.method == 'POST':
        if not request.form['name']:
            flash('Ошибка, введите имя!', 'danger')
            return redirect(url_for('flash_form'))
        name = request.form['name']
        flash(f'Привет, {name} !', 'success')
        return render_template('answer.html')
    return render_template('flash_form.html')


if __name__ == '__main__':
    application.run(debug=True)
