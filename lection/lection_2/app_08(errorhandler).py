from pathlib import PurePath, Path
from flask import Flask, url_for, render_template, request, abort
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return '<h2>Hi</h2>'


@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         file = request.files.get('file')
#         file_name = secure_filename(file.filename)
#         file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
#         return f"Файл {file_name} загружен на сервер"
#     return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
