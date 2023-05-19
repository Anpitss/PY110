def min_len_check(fn):
    def wrapper(arg: str):
        if len(arg) >= 10:  # TODO записать обертку для исходной функции
            print("Строка подходящего размера")
        else:
            raise ValueError("Строка слишком короткая")
        result = fn(arg)
        return result
    return wrapper


@min_len_check# TODO задекорировать функцию
def some_func(str_arg: str):
    ...


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо

    some_func("Short str")  # ValueError("Строка слишком короткая")
