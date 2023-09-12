import requests
from multiprocessing import Process
import time

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]


def download(url_):
    response = requests.get(url_)
    filename = 'multiprocessing_' + url_.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(f'parsing\\{filename}', "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url_} in {time.time() - start_time:.2f}seconds")


processes = []
start_time = time.time()

if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
