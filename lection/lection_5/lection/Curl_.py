# Curl (client URL) — это инструмент командной строки на основе библиотеки libcurl для
# передачи данных с сервера и на сервер при помощи различных протоколов, в том числе
# HTTP, HTTPS, FTP, FTPS, IMAP, IMAPS, POP3, POP3S, SMTP и SMTPS. Он очень популярен в
# сфере автоматизации и скриптов благодаря широкому диапазону функций и
# поддерживаемых протоколов.

# Для отправки POST запроса нашему серверу введём в терминале следующую
# строку(не выключая сервер!):


# Хороший короткий PUT запрос:
# curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept: application/json' -H 'Content-Ty
# pe: application/json' -d '{"name": "NewName", "price": 77.7}'


# curl -X 'POST' 'http://127.0.0.1:8000/items/'
# -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"na
# me": "BestSale", "description": "The best of the best", "price": 9.99, "tax": 0.99}'


# Invoke-WebRequest -Uri "http://127.0.0.1:8000/items/" -Headers $headers -d '{"na
# me": "BestSale", "description": "The best of the best", "price": 9.99, "tax": 0.99}'
# $headers = @{
#     "Accept" = "application/json"
#     "Content-Type" = "application/json"
# }
# $mydict = @{
#     "name": "BestSale"
#     "description": "The best of the best"
#     "price": 9.99
#     "tax": 0.99
# }


# curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept: application/json' -H 'Con
# tent-Type: application/json' -d '{"name": "NewName", "price": 77.7}'

# curl -X POST http://localhost:8000/items/42 -H 'Content-Type: application/json' -d
# '{"name": "NewName", "price": 77.7}'

# -d {"name": "BestSale", "description": "The best of the best", "price": 9.99, "tax": 0.99}

# curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept: application/json' -H 'Content-Type: application/j
# son' -d '{"name": "NewName", "description": "New description of the object", "price": 77.7, "tax": 10.01}'
# curl -X 'PUT' 'http://127.0.0.1:8000/items/42' -H 'accept: application/json' -H 'Con
# tent-Type: application/json' -d '{"name": "NewName", "price": 77.7}'


# curl -X 'GET' \
#   'http://127.0.0.1:8000/' \
#   -H 'accept: application/json'
#
# curl XPOST -H 'accept: application/json' -H 'Content-Type: application/json' -d "{\"na
# me\": \"Alex\", \"description\": \"blabla\", \"price\": 100, \"tax\": 5}"
#
# curl -X 'POST' \
#   'http://127.0.0.1:8000/items/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d "{\"name\": \"Alex\", \"description\": \"blabla\", \"price\": 100, \"tax\": 5}"
#
# curl XPOST -H $headers -d "{'name': 'Alex', 'description': 'blabla', 'price': 100, 'tax': 5}"

# Invoke-WebRequest -Uri 'POST' 'http://127.0.0.1:8000/items/' -H 'accept: application/json' -H
# 'Content-Type: application/json' -d '{"name": "Alex", "description": "blabla", "price": 100, "tax": 5}'