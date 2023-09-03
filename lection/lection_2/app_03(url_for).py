from flask import Flask, url_for, render_template, request
from markupsafe import escape
# 16:03
app = Flask(__name__)


@app.route('/')
def index():
    return 'введите'


@app.route('/about/')
def about():
    context = {
        'title': 'Обо мне',
        'name': 'Харитон',
    }
    return render_template('about.html', **context)


if __name__ == '__main__':
    app.run()
