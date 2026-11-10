import threading

counter = 0
lock = threading.Lock()


def worker() -> None:
    global counter
    for _ in range(100_000):
        with lock:            # критическая секция: атомарный инкремент
            counter += 1


if __name__ == "__main__":
    threads = [threading.Thread(target=worker) for _ in range(8)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print(counter)            # стабильно 800000
