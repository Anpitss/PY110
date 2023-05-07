def task(numbers: list) -> int:
    return sum(num_ ** 3 for num_ in numbers if num_ < 0)


if __name__ == "__main__":
    list_numbers = [-2, -1, 0, 1, -3, 2, -3]
    print(task(list_numbers))
