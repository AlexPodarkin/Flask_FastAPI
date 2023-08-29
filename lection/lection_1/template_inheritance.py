from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def base_ex_1():
    menu_ = ['1. Наследование', '2. Работа с шаблонами', '3. Flask', '4. Пункт', '5. Пункт']
    context = {'menu': menu_,
               'title': '(работа с шаблонами)'}
    return render_template('base_ex_1.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
