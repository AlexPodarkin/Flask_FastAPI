from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/world/')
@app.route('/my_world/')
def hello_world():
    return 'Hello World !'


# Функция представления имеет два декоратора. При переходе по любому из этих
# адресов в браузере отобразится одна и та же строка


@app.route('/Alex/')
def hello_alex():
    return 'Hello Alex'


@app.route('/<name>/')
def hello_name(name='None'):
    return f'Hello, {name.capitalize()}'


# Функция будет отрабатывать корневой адрес и адреса, где передаётся любой текст
# между корневым слешем и замыкающим. При этом текст из браузера сохраняется в
# переменной <name>. Далее функция hello() принимает на вход содержимое переменной
# name. Если в браузере ничего не ввести, будет подставлено значение по умолчанию — «None».

# string — (по умолчанию) принимает текст без слеша
# ● int — принимает позитивные целые числа
# ● float — принимает позитивные числа с плавающей точкой
# ● path — как string, но принимает слеши
# ● uuid — принимает строки UUID


@app.route('/file/<path:file>/')
def set_path(file):
    print(type(file))
    # тип String
    return f'path = {file}'


# ● path — как string, но принимает слеши
# 🔥 Внимание! Переменная file содержит строку типа str. Разница в типах
# именно в восприятии слешей как части содержимого строки


@app.route('/numb/<int:num>/')
def num_mult(num):
    num *= 5
    return f'передано({num / 5}) * 5 = {num}'


# Если вы попытаетесь передать данные другого типа, получим ошибку 404, страница
# не будет отработана.


@app.route('/text/')
def text_html():
    poem = ['Вот не думал, не гадал,', 'Программистом взял и стал.',
            'Хитрый знает он язык,', 'Он к другому не привык.']
    text = f'<h3> Стих </h3>\n </p>{"<br>".join(poem)}</p>'
    return text


if __name__ == '__main__':
    app.run(debug=True)
