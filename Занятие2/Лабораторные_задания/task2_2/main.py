def count(start_number: float = 1, step: float = 1):
    counter = start_number  # TODO написать функцию-генератор возвращающую целые числа
    while True:
        yield counter
        counter += step

if __name__ == "__main__":
    my_count = count(10, 0.5)
    for _ in range(10):
        print(next(my_count))
