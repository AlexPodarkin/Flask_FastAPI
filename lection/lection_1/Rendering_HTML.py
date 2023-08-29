from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def html_index():
    context = {
        'title': 'личный блог',
        'name': 'Alex',
    }
    return render_template('index.html', **context)


@app.route('/if/')
def show_if():
    context = {
        'title': 'ветвление',
        'name': 'cool hack !',
        'number': 5,
    }
    return render_template('index.html', **context)


@app.route('/for/')
def show_for():
    poem = ['Вот не думал, не гадал,',
            'Программистом взял и стал.',
            'Хитрый знает он язык,',
            'Он к другому не привык.',
            ]
    return render_template('for.html', poem=poem)


# Инструкция для подключения стилей и картинок
# <link rel="stylesheet" href="/static/css/style.css">
# <img src="/static/image/foto.png" alt="Моё фото" width="300">


if __name__ == '__main__':
    app.run(debug=True)
