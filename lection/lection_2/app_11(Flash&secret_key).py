from pathlib import PurePath, Path
from flask import Flask, url_for, render_template, request, abort, redirect, flash
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/')
def index():
    return 'Hi'


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run()
