from tkinter import *


def get_string(string, start, end):
    try:
        start = int(start)
        end = int(end)
    except ValueError:
        return "Промежуток не может быть пустым или буквой"

    if start > end:
        return "Начало не может быть больше конца"

    words = string.lower().split()

    if start > len(words) or end > len(words):
        return "Границы промежутка не должны быть больше количества слов в строке"

    input_range = range(start - 1, end)

    new_string = ""
    for i in range(len(words)):
        if i not in input_range:
            new_string += words[i] + " "

    for i in input_range:
        new_string += words[i] + " "

    return new_string


def take_input(output, input_string, input_from, input_to):
    output.config(state=NORMAL)
    output.delete('1.0', 'end')
    output.insert(END, get_string(input_string, input_from, input_to))
    output.config(state=DISABLED)
    output.pack()


def create_window():
    window = Tk()
    window.geometry("500x400")
    window.title("2 Задача Ильин 1 вар")

    win_width = window.winfo_reqwidth()
    win_height = window.winfo_reqheight()
    pos_right = int(window.winfo_screenwidth() / 2 - win_width / 2)
    pos_down = int(window.winfo_screenheight() / 2 - win_height / 2)
    window.geometry("+{}+{}".format(pos_right, pos_down))

    Label(text="Введите строку:", anchor=W).pack()
    input_string = Text(window, height=5, width=50)
    input_string.pack()

    Label(text="Начало:").pack()
    input_from = Text(window, height=1, width=3)
    input_from.pack()

    Label(text="Конец:").pack()
    input_to = Text(window, height=1, width=3)
    input_to.pack()

    Label(text="Результат:").pack()

    output = Text(window, height=5, width=50, state=DISABLED)
    output.pack()

    Button(window, height=2, width=20, text="Результат", command=lambda: take_input(output=output,
                                                input_string=input_string.get("1.0", "end-1c"),
                                                input_from=input_from.get("1.0", "end-1c"),
                                                input_to=input_to.get("1.0", "end-1c"))).pack()

    window.mainloop()


create_window()
