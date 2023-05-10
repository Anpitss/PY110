INPUT_FILE = "input.txt"


def task() -> None:
    with open('input.txt', 'r') as file:  # TODO открыть указатель на файл
        for word in file:  # TODO файл является итератором, который работает с циклом for в построчном режиме
            print(word, end='')

if __name__ == "__main__":
    task()
