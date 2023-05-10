OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, 'w') as f:
        for count in range(1, 11):
            space = " " * (10 - count)
            star = "*" * count
            f.write(f'{space + star}\n')
    # TODO записать лесенку в файл


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
