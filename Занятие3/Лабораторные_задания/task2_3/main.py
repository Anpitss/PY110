import json


def task():
    filename = "input.json"
    with open(filename, 'r') as f:
        json_load = json.load(f)  # TODO считать содержимое JSON файла

    return max(json_load, key=lambda i: i['score'])  # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
