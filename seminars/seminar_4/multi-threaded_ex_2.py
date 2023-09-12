import threading
# import time


# def worker(num):
#     print(f'Начало работы потока {num}')
#     time.sleep(3)
#     print(f'Конец работы потока {num}')
#
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     threads.append(t)
#     t.start()
#
#
# for t in threads:
#     t.join()
#
#
# print('Все потоки завершили работу !')


counter = 0


def increment():
    global counter
    for _ in range(1_000_000):
        counter += 1
    print(f"Значение счетчика: {counter:_}")


threads = []
for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()
for t in threads:
    t.join()

print(f"Значение счетчика в финале: {counter:_}")
