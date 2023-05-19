def pow_gen(base: int):
    numbers = 0  # TODO записать функцию-генератор
    while True:
        yield base ** numbers
        numbers += 1


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
