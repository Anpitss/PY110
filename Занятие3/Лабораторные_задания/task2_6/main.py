import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)
    sort_ = sorted(json_data, key=lambda item: item['length'])
    #return sort_  # TODO отсортировать список словарей

    with open('output.json', 'w') as f:
        f.write(json.dumps(sort_, indent=4))
    return sort_

if __name__ == "__main__":
    data = task()
    print(json.dumps(data, indent=4))

   # TODO дополнительно записать отсортированный список в JSON файл
