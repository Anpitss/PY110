def task() -> str:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return min(list_words, key=lambda word: len(word))   # используй ключевую у функции min, по которой она долна определять минимальный элемент

if __name__ == "__main__":
    print(task())
