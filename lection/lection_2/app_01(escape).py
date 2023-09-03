from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return 'введите путь к файлу'


@app.route('/<path:file>/')
def get_file(file):
    print(file)
    return f'путь к вашему файлу: {escape(file)}'


if __name__ == '__main__':
    app.run(debug=True)

# А теперь вместо пути, передадим следующую строку:
# http://127.0.0.1:5000/<script>alert("I am haсker")</script>/
# На страницу будет выведен текст без пути. И одновременно сработает js скрипт с
# всплывающим сообщением о хакере. А ведь код может быть не таким безобидным как в примере
