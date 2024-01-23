from tkinter import *

all_numbers = {'zero': 0,
               'one': 1,
               'two': 2,
               'three': 3,
               'four': 4,
               'five': 5,
               'six': 6,
               'seven': 7,
               'eight': 8,
               'nine': 9,
               'ten': 10,
               'eleven': 11,
               'twelve': 12,
               'thirteen': 13,
               'fourteen': 14,
               'fifteen': 15,
               'sixteen': 16,
               'seventeen': 17,
               'eighteen': 18,
               'nineteen': 19,
               'twenty': 20,
               'thirty': 30,
               'forty': 40,
               'fifty': 50,
               'sixty': 60,
               'seventy': 70,
               'eighty': 80,
               'ninety': 90,
               }

ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

from11to19 = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def get_string(string):
    words = string.lower().split()

    if len(words) == 0:
        return 'Строка не может быть пустой'

    if len(words) == 1 and words[0] == 'hundred':
        return 'Перед сотней должна быть цифра, указывающая на количество сотен'

    if len(words) == 1 and is_correct_word(words[0]):
        return get_number_from_word(words[0])

    if not is_correct_word(words[0]):
        return 'Слово - ' + words[0] + ' содержит ошибку'

    if words.count('hundred') > 1:
        return 'В строке не может быть несколько слов - hundred'

    if words[0] == 'zero':
        return 'Число не может начинаться с нуля'

    result_number = get_number_from_word(words[0])

    for i in range(1, len(words)):
        if not is_correct_word(words[i]):
            return 'Слово - ' + words[i] + ' содержит ошибку'

        if words[i] == 'zero':
            return 'Ноль может быть только отдельной цифрой'

        if not is_correct_sequence(words[i - 1], words[i]):
            return ('Число ' + get_format(words[i - 1]) + ' - ' + words[i - 1]
                    + ' не может идти перед числом ' + get_format(words[i]) + ' - ' + words[i])

        if words[i] != 'hundred':
            result_number += get_number_from_word(words[i])
        else:
            result_number = get_number_from_word(words[i - 1]) * 100

    if result_number > 999:
        return 'Число задается в диапазоне 0-999'

    return result_number


def is_correct_word(word):
    if word in all_numbers or word == 'hundred':
        return True

    return False


def get_format(number):
    if number in ones:
        return "единичного формата"
    if number in tens:
        return "десятичного формата"
    if number in from11to19:
        return "формата 11-19"


def is_correct_sequence(word_left, word_right):
    if word_left in ones and (word_right in from11to19 or word_right in tens or word_right in ones):
        return False

    if word_left in from11to19 and (word_right in ones or word_right in tens or word_right in from11to19):
        return False

    if word_left in tens and (word_right in from11to19 or word_right in tens):
        return False

    if word_left == 'ten' and (word_right in ones or word_right in tens or word_right in from11to19):
        return False

    return True


def get_number_from_word(word):
    return all_numbers.get(word)


def take_input(output, input_string):
    output.config(state=NORMAL)
    output.delete('1.0', 'end')
    output.insert(END, get_string(input_string))
    output.config(state=DISABLED)
    output.pack()


def create_window():
    window = Tk()
    window.geometry("500x400")
    window.title("1 Задача Ильин Английский язык")

    win_width = window.winfo_reqwidth()
    win_height = window.winfo_reqheight()
    pos_right = int(window.winfo_screenwidth() / 2 - win_width / 2)
    pos_down = int(window.winfo_screenheight() / 2 - win_height / 2)
    window.geometry("+{}+{}".format(pos_right, pos_down))

    Label(text="Введите строку (числа словами от 0-999):", anchor=W).pack()
    input_string = Text(window, height=5, width=50)
    input_string.pack()

    Label(text="Результат:").pack()

    output = Text(window, height=5, width=50, state=DISABLED)
    output.pack()

    Button(window, height=2, width=20, text="Результат", command=lambda: take_input(output=output,
                                                                                    input_string=input_string.get("1.0",
                                                                                                                  "end-1c"))).pack()

    window.mainloop()


create_window()
