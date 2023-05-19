INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, 'r') as input_f:
        with open(OUTPUT_FILE, 'w') as output_f:
            for upper_l in map(str.upper, input_f):
                output_f.write(upper_l)  # TODO перезаписать содержимое одного файла в другой


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
